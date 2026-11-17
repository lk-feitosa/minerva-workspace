#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
minerva_quotas.py - Consulta Direta de Contas, TODOS os Modelos e Cotas direto dos CLIs no PC
(com fallback para Maestri .status.json e cache local, sem poluir sessões do usuário).

Fontes consultadas diretamente nos CLIs:
  1. Antigravity CLI (`agy`):
     - `agy models` -> lista todos os modelos disponíveis (Gemini 4 Argon/Hydrogen, Gemini 3.8 Flash, Claude Opus/Sonnet 5.5, GPT-OSS 120B)
     - `agy -p /usage --output-format json` (ou cache recente em live_quota.json) -> cotas por grupo/modelo (5h e Semanal)
  2. OpenAI Codex CLI (`codex`):
     - `codex app-server --stdio` (com CODEX_SQLITE_HOME isolado em ~/.minerva/.cache/codex-usage para zero poluição no /resume)
     - Métodos JSON-RPC: `account/rateLimits/read` (cotas e plano) + `model/list` (todos os modelos: GPT-6-Luna, GPT-5.6-Terra, níveis de esforço)
  3. Claude Code CLI (`claude`):
     - Verifica login em `~/.claude.json` (`oauthAccount`) e, se autenticado, consulta `claude -p ... --no-session-persistence` (`get_usage` + `model_scoped`)
"""

import argparse
import base64
import json
import os
import shutil
import subprocess
import time
from pathlib import Path


def _read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        text = path.read_text(encoding="utf-8", errors="ignore").lstrip("\ufeff")
        return json.loads(text)
    except Exception:
        return {}


def _decode_jwt_email(token: str | None) -> str | None:
    if not token or "." not in token:
        return None
    try:
        payload_b64 = token.split(".")[1]
        padding = "=" * (-len(payload_b64) % 4)
        data = json.loads(base64.urlsafe_b64decode(payload_b64 + padding).decode("utf-8", errors="ignore"))
        return data.get("email")
    except Exception:
        return None


def query_agy_cli_direct(home: Path, live_refresh: bool = False) -> dict:
    """Consulta modelos e cotas diretamente do Antigravity CLI (agy)."""
    agy_bin = shutil.which("agy.exe") or shutil.which("agy")
    local_agy = home / "AppData" / "Local" / "agy" / "bin" / "agy.exe"
    if not agy_bin and local_agy.exists():
        agy_bin = str(local_agy)

    info = {
        "id": "antigravity",
        "name": "Antigravity",
        "preset_name": "Antigravity",
        "installed": bool(agy_bin),
        "authenticated": False,
        "source": "cli direto (agy)",
        "models": [],
        "quotas": [],
    }
    if not agy_bin:
        return info

    # 1. Lista todos os modelos via `agy models`
    try:
        proc = subprocess.run(
            [agy_bin, "models"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=10,
        )
        for line in proc.stdout.splitlines():
            if "\t" in line:
                slug, label = line.split("\t", 1)
                info["models"].append({"id": slug.strip(), "label": label.strip()})
        if info["models"]:
            info["authenticated"] = True
    except Exception:
        pass

    # 2. Cotas: usa `agy -p /usage --output-format json` se live_refresh ou se cache > 5 min
    live_quota_path = home / ".gemini" / "antigravity-cli" / "live_quota.json"
    maestri_status_path = home / ".maestri" / "usage" / "providers" / ".status.json"
    groups_loaded = False

    if live_refresh or not live_quota_path.exists() or (time.time() - live_quota_path.stat().st_mtime > 300):
        try:
            u_proc = subprocess.run(
                [agy_bin, "-p", "/usage", "--output-format", "json"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore",
                timeout=20,
            )
            if u_proc.returncode == 0 and u_proc.stdout.strip().startswith("{"):
                raw = json.loads(u_proc.stdout)
                for g in (raw.get("command", {}).get("data", {}).get("groups") or []):
                    g_name = g.get("name", "Gemini")
                    for b in (g.get("buckets") or []):
                        rem_frac = float(b.get("remaining_fraction", 1.0))
                        rem_pct = round(max(0.0, min(100.0, rem_frac * 100.0)), 1)
                        info["quotas"].append(
                            {
                                "meter": g_name,
                                "window": b.get("window") or b.get("id"),
                                "usedPercent": round(100.0 - rem_pct, 1),
                                "remainingPercent": rem_pct,
                                "resetsAt": b.get("reset_time"),
                            }
                        )
                if info["quotas"]:
                    groups_loaded = True
                    info["authenticated"] = True
                    info["source"] = "cli direto (agy -p /usage)"
        except Exception:
            pass

    # Fallback rápido: live_quota.json ou .maestri/.status.json
    if not groups_loaded and live_quota_path.exists():
        agy_cache = _read_json(live_quota_path).get("agy", {})
        for m in agy_cache.get("meters", []):
            for w in m.get("windows", []):
                rem = float(w.get("remainingPercent", 100.0))
                info["quotas"].append(
                    {
                        "meter": m.get("label"),
                        "window": w.get("window"),
                        "usedPercent": round(100.0 - rem, 1),
                        "remainingPercent": round(rem, 1),
                        "resetsAt": w.get("resetsAt"),
                    }
                )
        if info["quotas"]:
            groups_loaded = True
            info["authenticated"] = True
            info["source"] = "cli cache (live_quota.json)"

    if not groups_loaded and maestri_status_path.exists():
        st = _read_json(maestri_status_path)
        for prov in st.get("providers", []):
            if prov.get("id") == "antigravity":
                info["authenticated"] = prov.get("state") == "ready"
                for m in prov.get("meters", []):
                    for w in m.get("windows", []):
                        used = float(w.get("usedPercent", 0.0))
                        rem = round(max(0.0, 100.0 - used), 1)
                        info["quotas"].append(
                            {
                                "meter": m.get("label") or m.get("id"),
                                "window": w.get("title") or w.get("id"),
                                "usedPercent": round(used, 1),
                                "remainingPercent": rem,
                                "resetsAt": w.get("resetsAt"),
                            }
                        )
                info["source"] = "cli via maestri (.status.json)"

    return info


def query_codex_cli_direct(home: Path) -> dict:
    """Consulta modelos e cotas diretamente do Codex CLI via `codex app-server --stdio`."""
    codex_bin = shutil.which("codex.exe") or shutil.which("codex")
    local_codex = home / "AppData" / "Local" / "Programs" / "OpenAI" / "Codex" / "bin" / "codex.exe"
    if not codex_bin and local_codex.exists():
        codex_bin = str(local_codex)

    auth_file = home / ".codex" / "auth.json"
    auth_doc = _read_json(auth_file)
    email = _decode_jwt_email((auth_doc.get("tokens") or {}).get("id_token"))

    info = {
        "id": "codex",
        "name": "Codex",
        "preset_name": "Codex",
        "installed": bool(codex_bin),
        "authenticated": auth_file.exists(),
        "account": email,
        "plan": "unknown",
        "source": "cli direto (codex app-server --stdio)",
        "models": [],
        "quotas": [],
    }
    if not codex_bin or not auth_file.exists():
        return info

    cache_dir = home / ".minerva" / ".cache" / "codex-usage"
    cache_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["CODEX_SQLITE_HOME"] = str(cache_dir)

    p = None
    try:
        p = subprocess.Popen(
            [codex_bin, "app-server", "--stdio"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
            errors="ignore",
            env=env,
        )
        assert p.stdin is not None and p.stdout is not None
        p.stdin.write(
            json.dumps(
                {
                    "id": 1,
                    "method": "initialize",
                    "params": {"clientInfo": {"name": "minerva", "title": "Minerva", "version": "1"}},
                }
            )
            + "\n"
        )
        p.stdin.flush()

        deadline = time.time() + 8.0
        while time.time() < deadline:
            line = p.stdout.readline()
            if not line:
                break
            if line.strip().startswith("{") and json.loads(line).get("id") == 1:
                break

        p.stdin.write(json.dumps({"method": "initialized"}) + "\n")
        p.stdin.write(
            json.dumps({"id": 2, "method": "account/rateLimits/read", "params": {"excludeResetCreditDetails": True}})
            + "\n"
        )
        p.stdin.write(json.dumps({"id": 3, "method": "model/list", "params": {}}) + "\n")
        p.stdin.flush()

        got = set()
        while len(got) < 2 and time.time() < deadline:
            line = p.stdout.readline()
            if not line:
                break
            if not line.strip().startswith("{"):
                continue
            msg = json.loads(line)
            mid = msg.get("id")
            if mid == 2 and "result" in msg:
                got.add(2)
                res = msg["result"]
                rl = res.get("rateLimits") or {}
                info["plan"] = rl.get("planType") or "standard"
                prim = rl.get("primary")
                if prim and isinstance(prim.get("usedPercent"), (int, float)):
                    used = float(prim["usedPercent"])
                    info["quotas"].append(
                        {
                            "meter": rl.get("limitName") or "Codex",
                            "window": "Primária",
                            "usedPercent": round(used, 1),
                            "remainingPercent": round(max(0.0, 100.0 - used), 1),
                            "resetsAt": prim.get("resetsAt"),
                        }
                    )
                sec = rl.get("secondary")
                if sec and isinstance(sec.get("usedPercent"), (int, float)):
                    used = float(sec["usedPercent"])
                    info["quotas"].append(
                        {
                            "meter": rl.get("limitName") or "Codex",
                            "window": "Secundária",
                            "usedPercent": round(used, 1),
                            "remainingPercent": round(max(0.0, 100.0 - used), 1),
                            "resetsAt": sec.get("resetsAt"),
                        }
                    )
            elif mid == 3 and "result" in msg:
                got.add(3)
                for m in (msg["result"].get("data") or []):
                    if not m.get("hidden"):
                        efforts = [
                            e.get("reasoningEffort") for e in (m.get("supportedReasoningEfforts") or []) if e.get("reasoningEffort")
                        ]
                        info["models"].append(
                            {
                                "id": m.get("id"),
                                "label": m.get("displayName") or m.get("id"),
                                "defaultEffort": m.get("defaultReasoningEffort"),
                                "efforts": efforts,
                                "isDefault": bool(m.get("isDefault")),
                            }
                        )
    except Exception:
        pass
    finally:
        if p is not None:
            try:
                if p.stdin:
                    p.stdin.close()
                p.terminate()
                p.wait(timeout=2)
            except Exception:
                pass

    return info


def query_claude_cli_direct(home: Path) -> dict:
    """Verifica login e cotas diretamente do Claude Code CLI (`--no-session-persistence`)."""
    claude_bin = shutil.which("claude.exe") or shutil.which("claude")
    local_claude = home / ".local" / "bin" / "claude.exe"
    if not claude_bin and local_claude.exists():
        claude_bin = str(local_claude)

    claude_doc = _read_json(home / ".claude.json")
    email = (claude_doc.get("oauthAccount") or {}).get("emailAddress")

    info = {
        "id": "claude",
        "name": "Claude Code",
        "preset_name": "Claude Code",
        "installed": bool(claude_bin),
        "authenticated": bool(email),
        "account": email,
        "plan": "unknown",
        "source": "cli direto (~/.claude.json + claude --no-session-persistence)",
        "models": [
            {"id": "claude-sonnet-4-6", "label": "Claude Sonnet 4.6"},
            {"id": "claude-opus-4-6", "label": "Claude Opus 4.6"},
            {"id": "claude-haiku-4-5", "label": "Claude Haiku 4.5"},
        ],
        "quotas": [],
    }
    if not email:
        info["note"] = "Sem oauthAccount ativa em ~/.claude.json (rode `claude login` se quiser usar o CLI nativo do Claude)"
        return info

    if claude_bin:
        try:
            req = json.dumps(
                {
                    "type": "control_request",
                    "request_id": "minerva-usage",
                    "request": {"subtype": "get_usage", "skip_behaviors": True},
                }
            )
            proc = subprocess.run(
                [
                    claude_bin,
                    "-p",
                    "--input-format",
                    "stream-json",
                    "--output-format",
                    "stream-json",
                    "--verbose",
                    "--no-session-persistence",
                ],
                input=req + "\n",
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore",
                timeout=12,
            )
            for line in proc.stdout.splitlines():
                if not line.strip().startswith("{"):
                    continue
                msg = json.loads(line)
                if msg.get("type") == "control_response":
                    resp = (msg.get("response") or {}).get("response") or {}
                    info["plan"] = resp.get("subscription_type") or "pro"
                    rl = resp.get("rate_limits") or {}
                    for w_key, w_label in [("five_hour", "Sessão 5h"), ("seven_day", "Semanal 7d")]:
                        w = rl.get(w_key)
                        if w and isinstance(w.get("utilization"), (int, float)):
                            used = float(w["utilization"])
                            info["quotas"].append(
                                {
                                    "meter": "Claude Plan",
                                    "window": w_label,
                                    "usedPercent": round(used, 1),
                                    "remainingPercent": round(max(0.0, 100.0 - used), 1),
                                    "resetsAt": w.get("resets_at"),
                                }
                            )
                    for ms in (rl.get("model_scoped") or []):
                        if isinstance(ms.get("utilization"), (int, float)):
                            used = float(ms["utilization"])
                            info["quotas"].append(
                                {
                                    "meter": ms.get("display_name", "Model"),
                                    "window": "Semanal",
                                    "usedPercent": round(used, 1),
                                    "remainingPercent": round(max(0.0, 100.0 - used), 1),
                                    "resetsAt": ms.get("resets_at"),
                                }
                            )
        except Exception:
            pass

    return info


def pick_best_agy_model_for_role(agy_info: dict, role_key: str) -> str:
    """Escolhe o melhor modelo dentro do Antigravity olhando a cota de cada família (Claude/GPT vs Gemini)."""
    claude_gpt_rem = 100.0
    gemini_sem_rem = 100.0
    for q in agy_info.get("quotas", []):
        meter = str(q.get("meter") or "").lower()
        win = str(q.get("window") or "").lower()
        if "claude" in meter or "gpt" in meter:
            claude_gpt_rem = min(claude_gpt_rem, float(q.get("remainingPercent", 100.0)))
        elif "gemini models" in meter and ("semanal" in win or "week" in win or "7d" in win):
            gemini_sem_rem = float(q.get("remainingPercent", 100.0))

    if role_key == "review" and claude_gpt_rem >= 20.0:
        return "claude-opus-5-5-high (ou claude-sonnet-5-5-high via Antigravity — 100% cota 3P livre)"
    if role_key == "ui":
        if claude_gpt_rem >= 30.0 and gemini_sem_rem < 15.0:
            return "claude-sonnet-5-5-high (ou gemini-3.8-flash-high via Antigravity)"
        return "gemini-4-hydrogen-high / claude-sonnet-5-5-high (via Antigravity)"
    return "claude-sonnet-5-5-high / gemini-3.8-flash-high (via Antigravity)"


def build_team_recommendations(providers: dict) -> list[dict]:
    available = [p for p in providers.values() if p.get("installed") and p.get("authenticated")]
    avail_ids = {p["id"] for p in available}
    usage_count = {pid: 0 for pid in avail_ids}

    agy_info = providers.get("antigravity", {})
    codex_models = providers.get("codex", {}).get("models", [])
    default_codex_model = next(
        (f"{m['id']} ({m.get('defaultEffort') or 'high'})" for m in codex_models if m.get("isDefault")),
        "gpt-6-luna (high)",
    )

    roles = [
        {
            "key": "ui",
            "role": "Front-End Specialist (agent/ui)",
            "preferred": ["antigravity", "claude", "codex"],
            "reason_hint": "UI/UX, componentes, animações e fidelidade visual",
        },
        {
            "key": "backend",
            "role": "Back-End Specialist (agent/backend)",
            "preferred": ["codex", "claude", "antigravity"],
            "reason_hint": "Arquitetura de APIs, banco de dados e regras de negócio",
        },
        {
            "key": "tests",
            "role": "Test & QA Specialist (agent/tests)",
            "preferred": ["codex", "antigravity", "claude"],
            "reason_hint": "Testes automatizados, Playwright E2E e validação CLI",
        },
        {
            "key": "review",
            "role": "Code & Security Reviewer (agent/review)",
            "preferred": ["claude", "antigravity", "codex"],
            "reason_hint": "Auditoria crítica, segurança e conformidade com spec",
        },
    ]

    table = []
    for r in roles:
        candidates = [pid for pid in r["preferred"] if pid in avail_ids]
        chosen_id = None
        if candidates:
            candidates.sort(key=lambda pid: usage_count.get(pid, 0))
            chosen_id = candidates[0]
            usage_count[chosen_id] = usage_count.get(chosen_id, 0) + 1

        if chosen_id:
            p = providers[chosen_id]
            if chosen_id == "antigravity":
                model_rec = pick_best_agy_model_for_role(agy_info, r["key"])
            elif chosen_id == "codex":
                model_rec = default_codex_model
            else:
                model_rec = "claude-sonnet-4-6 / claude-opus-4-6"

            failovers = [providers[pid]["preset_name"] for pid in candidates[1:]]
            table.append(
                {
                    "role": r["role"],
                    "preset": p["preset_name"],
                    "recommended_model": model_rec,
                    "provider_id": chosen_id,
                    "failover_presets": failovers or [p["preset_name"]],
                    "reason": r["reason_hint"],
                }
            )
        else:
            table.append(
                {
                    "role": r["role"],
                    "preset": "Antigravity",
                    "recommended_model": "claude-sonnet-5-5-high",
                    "provider_id": "antigravity",
                    "failover_presets": ["Codex", "Claude Code"],
                    "reason": "Fallback padrão",
                }
            )
    return table


def inspect_all(live_agy: bool = False) -> dict:
    home = Path.home()
    providers = {
        "antigravity": query_agy_cli_direct(home, live_refresh=live_agy),
        "codex": query_codex_cli_direct(home),
        "claude": query_claude_cli_direct(home),
    }
    return {
        "providers": providers,
        "recommended_team_codes": build_team_recommendations(providers),
    }


def main():
    parser = argparse.ArgumentParser(description="Consulta Contas, TODOS os Modelos e Cotas direto dos CLIs no PC")
    parser.add_argument("--live", action="store_true", help="Força refresh ao vivo do `agy -p /usage` além do `codex app-server`")
    parser.add_argument("--json", action="store_true", help="Retorna saída estritamente em JSON")
    args = parser.parse_args()

    data = inspect_all(live_agy=args.live)
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    print("==========================================================================")
    print("  📊 MINERVA DIRECT CLI QUOTA & MODEL INSPECTOR (Todos os Modelos do PC)")
    print("==========================================================================")
    for pid, p in data["providers"].items():
        auth_str = "AUTENTICADO" if p["authenticated"] else "NÃO LOGADO"
        acct = f" ({p['account']})" if p.get("account") else ""
        print(f"\n🔹 {p['name']}{acct} [Preset Maestri: --preset \"{p['preset_name']}\"]")
        print(f"   Status  : {auth_str} | Fonte: {p['source']}")
        if p.get("note"):
            print(f"   Nota    : {p['note']}")
        if p.get("models"):
            m_list = ", ".join(m["id"] for m in p["models"][:8])
            extra = f" (+{len(p['models']) - 8} outros)" if len(p["models"]) > 8 else ""
            print(f"   Modelos : {len(p['models'])} disponíveis -> {m_list}{extra}")
        if p.get("quotas"):
            for q in p["quotas"]:
                print(
                    f"   Cota    : {q['meter']} ({q['window']}) -> {q['remainingPercent']}% livre (usado: {q['usedPercent']}%)"
                )
        else:
            print("   Cota    : Sem limite ativo reportado")

    print("\n--------------------------------------------------------------------------")
    print("  🤝 SUGESTÃO ANTI-MONOCULTURA POR PAPEL, MODELO & COTA (TEAM CODES)")
    print("--------------------------------------------------------------------------")
    for rec in data["recommended_team_codes"]:
        fo = ", ".join(rec["failover_presets"])
        print(f"  • {rec['role']}")
        print(f"    -> Preset: {rec['preset']} | Modelo ideal: {rec['recommended_model']} | Failover: {fo}")
    print("==========================================================================")


if __name__ == "__main__":
    main()
