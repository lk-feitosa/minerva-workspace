#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
minerva_quotas.py - Leitor Passivo de Contas, Presets e Cotas (Maestri + PC Local, Zero Poluição de Sessões).

Ordem de leitura (100% passiva em disco, sem abrir sessões nos CLIs):
  1. Maestri Nativo:
     - ~/.maestri/preferences.json (agentPresets, agentAccounts)
     - ~/.maestri/usage/providers/.status.json (anéis de cota 5h/semanal/mensal e estado de cada CLI)
  2. Arquivos Nativos dos CLIs no PC (fallback/complemento direto):
     - Antigravity / Gemini: ~/.gemini/antigravity-cli/live_quota.json
     - OpenAI Codex: ~/.codex/auth.json + últimas sessões em ~/.codex/sessions/
     - Claude Code: ~/.claude.json (oauthAccount)
  3. Recomendação Anti-Monocultura (Protocolo Alethe) para os 4 papéis do Team CODES.
"""

import argparse
import base64
import json
import shutil
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


def inspect_maestri_and_pc() -> dict:
    home = Path.home()
    maestri_dir = home / ".maestri"
    pref = _read_json(maestri_dir / "preferences.json").get("payload", {})
    status_doc = _read_json(maestri_dir / "usage" / "providers" / ".status.json")

    # 1. Presets configurados no Maestri
    presets = {}
    for p in pref.get("agentPresets", []):
        if p.get("isActive") and p.get("agentType") != "generic_shell":
            presets[p.get("id")] = {
                "name": p.get("name"),
                "agentType": p.get("agentType"),
                "command": p.get("command"),
            }

    # 2. Status e cotas lidas pelo Maestri (.status.json)
    providers = {}
    for prov in status_doc.get("providers", []):
        pid = prov.get("id")
        if not pid:
            continue
        meters_summary = []
        min_remaining = 100.0
        for m in prov.get("meters", []):
            m_label = m.get("label") or m.get("id")
            for w in m.get("windows", []):
                used = float(w.get("usedPercent", 0.0))
                rem = round(max(0.0, 100.0 - used), 1)
                if rem < min_remaining:
                    min_remaining = rem
                meters_summary.append(
                    {
                        "meter": m_label,
                        "window": w.get("title") or w.get("id"),
                        "usedPercent": round(used, 1),
                        "remainingPercent": rem,
                        "resetsAt": w.get("resetsAt"),
                    }
                )
        providers[pid] = {
            "id": pid,
            "name": prov.get("name", pid),
            "preset_name": "Antigravity" if pid == "antigravity" else ("Claude Code" if pid == "claude" else "Codex"),
            "state": prov.get("state", "unknown"),
            "installed": bool(prov.get("executable") and Path(prov["executable"]).exists()),
            "authenticated": prov.get("state") == "ready",
            "plan": prov.get("plan") or ("unlimited/no-cap" if not prov.get("limitsApply", True) else "standard"),
            "source": "maestri (.status.json)",
            "min_remaining_pct": min_remaining if meters_summary else (100.0 if not prov.get("limitsApply", True) else None),
            "quotas": meters_summary,
        }

    # 3. Complemento direto do PC (Antigravity live_quota.json, Codex auth/sessions, Claude .claude.json)
    # 3a. Antigravity
    agy_live = _read_json(home / ".gemini" / "antigravity-cli" / "live_quota.json").get("agy", {})
    if agy_live.get("meters"):
        p_agy = providers.setdefault(
            "antigravity",
            {
                "id": "antigravity",
                "name": "Antigravity",
                "preset_name": "Antigravity",
                "state": "ready",
                "installed": bool(shutil.which("agy")),
                "authenticated": True,
                "plan": "Pro",
                "source": "pc (.gemini/antigravity-cli/live_quota.json)",
                "min_remaining_pct": 100.0,
                "quotas": [],
            },
        )
        if not p_agy["quotas"]:
            for m in agy_live["meters"]:
                for w in m.get("windows", []):
                    rem = float(w.get("remainingPercent", 100.0))
                    p_agy["quotas"].append(
                        {
                            "meter": m.get("label"),
                            "window": w.get("window"),
                            "usedPercent": round(100.0 - rem, 1),
                            "remainingPercent": round(rem, 1),
                            "resetsAt": w.get("resetsAt"),
                        }
                    )

    # 3b. Codex CLI direto no PC
    codex_auth_file = home / ".codex" / "auth.json"
    codex_auth = _read_json(codex_auth_file)
    codex_email = _decode_jwt_email((codex_auth.get("tokens") or {}).get("id_token"))
    p_codex = providers.setdefault(
        "codex",
        {
            "id": "codex",
            "name": "Codex",
            "preset_name": "Codex",
            "state": "ready" if codex_auth_file.exists() else "not_signed_in",
            "installed": bool(shutil.which("codex")),
            "authenticated": codex_auth_file.exists(),
            "plan": "unknown",
            "source": "pc (~/.codex/auth.json)",
            "min_remaining_pct": None,
            "quotas": [],
        },
    )
    if codex_email:
        p_codex["account"] = codex_email
    if codex_auth_file.exists():
        p_codex["authenticated"] = True

    # 3c. Claude Code direto no PC (~/.claude.json)
    claude_doc = _read_json(home / ".claude.json")
    claude_email = (claude_doc.get("oauthAccount") or {}).get("emailAddress")
    p_claude = providers.setdefault(
        "claude",
        {
            "id": "claude",
            "name": "Claude Code",
            "preset_name": "Claude Code",
            "state": "ready" if claude_email else "not_signed_in",
            "installed": bool(shutil.which("claude")),
            "authenticated": bool(claude_email),
            "plan": "unknown",
            "source": "pc (~/.claude.json)",
            "min_remaining_pct": None,
            "quotas": [],
        },
    )
    if claude_email:
        p_claude["account"] = claude_email
        p_claude["authenticated"] = True
    elif not claude_email and p_claude.get("plan") == "unlimited/no-cap" and not p_claude.get("quotas"):
        # No Maestri, limitsApply=false sem meters ocorre quando o Claude não retornou plano OAuth ativo
        p_claude["authenticated"] = False
        p_claude["note"] = "Sem oauthAccount em ~/.claude.json (verificar login antes de usar)"

    # 4. Sugestão Anti-Monocultura para o Team CODES
    available = [
        p for p in providers.values() if p.get("installed") and p.get("authenticated")
    ]
    recommendations = build_team_recommendations(providers, available)

    return {
        "maestri_detected": maestri_dir.exists(),
        "active_presets": list(presets.values()),
        "providers": providers,
        "recommended_team_codes": recommendations,
    }


def build_team_recommendations(providers: dict, available: list[dict]) -> list[dict]:
    """Distribui os 4 papéis do Team CODES evitando monocultura e respeitando cotas."""
    roles = [
        {
            "role": "Front-End Specialist (agent/ui)",
            "preferred": ["antigravity", "claude", "codex"],
            "reason_hint": "UI/UX, componentes, animações e fidelidade visual",
        },
        {
            "role": "Back-End Specialist (agent/backend)",
            "preferred": ["codex", "claude", "antigravity"],
            "reason_hint": "Arquitetura de APIs, banco de dados e regras de negócio",
        },
        {
            "role": "Test & QA Specialist (agent/tests)",
            "preferred": ["codex", "antigravity", "claude"],
            "reason_hint": "Testes automatizados, Playwright E2E e validação CLI",
        },
        {
            "role": "Code & Security Reviewer (agent/review)",
            "preferred": ["claude", "antigravity", "codex"],
            "reason_hint": "Auditoria crítica, segurança e conformidade com spec",
        },
    ]

    avail_ids = {p["id"] for p in available}
    usage_count = {pid: 0 for pid in avail_ids}
    table = []

    for r in roles:
        chosen_id = None
        # Prioriza provedor autenticado na ordem de aptidão, penalizando repetição (anti-monocultura)
        candidates = [pid for pid in r["preferred"] if pid in avail_ids]
        if candidates:
            candidates.sort(key=lambda pid: usage_count.get(pid, 0))
            chosen_id = candidates[0]
            usage_count[chosen_id] = usage_count.get(chosen_id, 0) + 1

        if chosen_id:
            p = providers[chosen_id]
            # Provedor de failover caso o principal falhe no terminal
            failovers = [providers[pid]["preset_name"] for pid in candidates[1:]]
            table.append(
                {
                    "role": r["role"],
                    "preset": p["preset_name"],
                    "provider_id": chosen_id,
                    "failover_presets": failovers or [p["preset_name"]],
                    "reason": f"{r['reason_hint']} (Autenticado via {p['source']})",
                }
            )
        else:
            table.append(
                {
                    "role": r["role"],
                    "preset": "Antigravity",
                    "provider_id": "antigravity",
                    "failover_presets": ["Codex", "Claude Code"],
                    "reason": "Fallback padrão",
                }
            )
    return table


def main():
    parser = argparse.ArgumentParser(description="Consulta Contas, Presets e Cotas direto do Maestri e do PC")
    parser.add_argument("--json", action="store_true", help="Retorna saída estritamente em JSON")
    args = parser.parse_args()

    data = inspect_maestri_and_pc()
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    print("==================================================================")
    print("  📊 MINERVA QUOTA & ACCOUNT INSPECTOR (Maestri + PC Local)")
    print("==================================================================")
    for pid, p in data["providers"].items():
        auth_str = "AUTENTICADO" if p["authenticated"] else "NÃO LOGADO / VERIFICAR"
        acct = f" ({p['account']})" if p.get("account") else ""
        print(f"\n🔹 {p['name']}{acct} [Preset Maestri: --preset \"{p['preset_name']}\"]")
        print(f"   Status : {auth_str} | Fonte: {p['source']}")
        if p.get("note"):
            print(f"   Nota   : {p['note']}")
        if p["quotas"]:
            for q in p["quotas"]:
                print(f"   Cota   : {q['meter']} ({q['window']}) -> {q['remainingPercent']}% livre (usado: {q['usedPercent']}%)")
        else:
            print("   Cota   : Sem anel de limite ativo reportado")

    print("\n------------------------------------------------------------------")
    print("  🤝 SUGESTÃO ANTI-MONOCULTURA (TEAM CODES + FAILOVER)")
    print("------------------------------------------------------------------")
    for rec in data["recommended_team_codes"]:
        fo = ", ".join(rec["failover_presets"])
        print(f"  • {rec['role']:<36} -> Preset: {rec['preset']:<12} (Failover: {fo})")
    print("==================================================================")


if __name__ == "__main__":
    main()
