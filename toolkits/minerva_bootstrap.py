#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
minerva_bootstrap.py - Bootstrap determinístico de 1 comando para o /minerva em qualquer projeto.
Executa em < 2s:
  1. Blindagem de .gitignore (mescla sem duplicar)
  2. Estrutura .agents/ (AGENTS.md, MINERVA.md, roles/) e AGENTS.md na raiz
  3. Estrutura docs/ (spec.md, architecture.md, adr/)
  4. Mescla sem duplicar .mcp.json (context-mode + ai-memory) e hook local do rtk (.claude/settings.local.json)
  5. Cria .kanban/board.json (5 colunas padrão)
  6. Gera .agents/skills.json (DAILY vs LIBRARY via agent_sort.py)
  7. Faz Auto-Heal das portas 3333 (Painel) e 3334 (Kanban) + Portais no Maestri (se disponível)
"""

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
import time
from pathlib import Path


def is_port_open(port: int, host: str = "127.0.0.1") -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.4)
        return s.connect_ex((host, port)) == 0


def merge_gitignore(project_dir: Path, template_gitignore: Path) -> str:
    target = project_dir / ".gitignore"
    if not template_gitignore.exists():
        return "template ausente"
    tpl_lines = [
        line.rstrip("\r\n")
        for line in template_gitignore.read_text(encoding="utf-8").splitlines()
    ]
    if not target.exists():
        target.write_text("\n".join(tpl_lines) + "\n", encoding="utf-8")
        return "criado"

    existing_text = target.read_text(encoding="utf-8", errors="ignore")
    existing_set = {
        l.strip()
        for l in existing_text.splitlines()
        if l.strip() and not l.strip().startswith("#")
    }
    missing = [
        l
        for l in tpl_lines
        if l.strip() and not l.strip().startswith("#") and l.strip() not in existing_set
    ]
    if not missing:
        return "já blindado"

    block = "\n# --- Minerva Workspace Shield ---\n" + "\n".join(missing) + "\n"
    target.write_text(existing_text.rstrip() + "\n" + block, encoding="utf-8")
    return f"mesclado (+{len(missing)} regras)"


def copy_if_missing(src: Path, dst: Path, force: bool = False) -> bool:
    if dst.exists() and not force:
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def merge_mcp_json(project_dir: Path, template_mcp: Path) -> str:
    target = project_dir / ".mcp.json"
    if not template_mcp.exists():
        return "template ausente"
    tpl_data = json.loads(template_mcp.read_text(encoding="utf-8"))
    if not target.exists():
        target.write_text(
            json.dumps(tpl_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        return "criado (context-mode + ai-memory)"

    try:
        cur_data = json.loads(target.read_text(encoding="utf-8"))
    except Exception:
        return "existente (JSON customizado preservado)"

    cur_servers = cur_data.setdefault("mcpServers", {})
    added = []
    for name, cfg in tpl_data.get("mcpServers", {}).items():
        if name not in cur_servers:
            cur_servers[name] = cfg
            added.append(name)

    if added:
        target.write_text(
            json.dumps(cur_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        return f"mesclado (+{', '.join(added)})"
    return "já configurado"


def ensure_rtk_hook(project_dir: Path) -> str:
    if not shutil.which("rtk"):
        return "rtk ausente no PATH (opcional)"
    settings_path = project_dir / ".claude" / "settings.local.json"
    hook_cmd = "rtk hook claude"
    data = {}
    if settings_path.exists():
        try:
            data = json.loads(settings_path.read_text(encoding="utf-8"))
        except Exception:
            return "settings.local.json existente preservado"

    hooks = data.setdefault("hooks", {})
    pre = hooks.setdefault("PreToolUse", [])
    for entry in pre:
        for h in entry.get("hooks", []):
            if h.get("command") == hook_cmd:
                return "já ativo em .claude/settings.local.json"

    pre.append(
        {
            "matcher": "Bash",
            "hooks": [{"type": "command", "command": hook_cmd}],
        }
    )
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    settings_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return "ativado em .claude/settings.local.json"


def resolve_companion_dir(minerva_home: Path, name: str, env_var: str) -> Path | None:
    env_val = os.environ.get(env_var)
    if env_val and Path(env_val).is_dir():
        return Path(env_val)
    tools_env = os.environ.get("MINERVA_TOOLS_DIR")
    if tools_env and (Path(tools_env) / name).is_dir():
        return Path(tools_env) / name
    candidates = [
        minerva_home / "tools" / name,
        minerva_home.parent / name,
    ]
    for c in candidates:
        if c.is_dir():
            return c
    return None


def spawn_detached(cmd: list[str], cwd: Path, wait_port: int | None = None) -> bool:
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    try:
        if os.name == "nt":
            CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)
            # 1) Metodo primario no Windows: Win32_Process.Create (WMI) com ShowWindow=0
            # Cria o processo sob WmiPrvSE.exe (servico do Windows), 100% FORA do Job Object
            # da tool call do agente (que possui JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE).
            win_cmd = list(cmd)
            if win_cmd and "python" in Path(win_cmd[0]).name.lower() and "-X" not in win_cmd:
                win_cmd = [win_cmd[0], "-X", "utf8"] + win_cmd[1:]
            cmdline = subprocess.list2cmdline(win_cmd)
            ps_escaped_cmd = cmdline.replace("'", "''")
            ps_escaped_cwd = str(cwd).replace("'", "''")
            ps_script = (
                "$si = New-CimInstance -ClassName Win32_ProcessStartup -ClientOnly -Property @{ShowWindow=[uint16]0}; "
                f"$r = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{{CommandLine='{ps_escaped_cmd}'; CurrentDirectory='{ps_escaped_cwd}'; ProcessStartupInformation=$si}}; "
                "if ($r.ReturnValue -eq 0) { exit 0 } else { exit 1 }"
            )
            spawned = False
            try:
                res = subprocess.run(
                    ["powershell", "-NoProfile", "-Command", ps_script],
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=8,
                    creationflags=CREATE_NO_WINDOW,
                )
                spawned = res.returncode == 0
            except Exception:
                spawned = False

            # 2) Fallback Popen caso WMI esteja indisponivel
            if not spawned:
                subprocess.Popen(
                    cmd,
                    cwd=str(cwd),
                    env=env,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | CREATE_NO_WINDOW,
                    close_fds=True,
                )
                spawned = True

            if wait_port:
                for _ in range(20):
                    if is_port_open(wait_port):
                        return True
                    time.sleep(0.25)
            return spawned
        else:
            subprocess.Popen(
                cmd,
                cwd=str(cwd),
                env=env,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
                close_fds=True,
            )
            if wait_port:
                for _ in range(10):
                    if is_port_open(wait_port):
                        return True
                    time.sleep(0.25)
            return True
    except Exception:
        return False


def ensure_services_and_portals(minerva_home: Path, project_dir: Path) -> dict:
    status = {"painel_3333": "offline", "kanban_3334": "offline", "maestri_portals": "skipped"}
    py = sys.executable or "python"

    # 1. Painel (:3333)
    if is_port_open(3333):
        status["painel_3333"] = "online (127.0.0.1:3333)"
    else:
        painel_dir = resolve_companion_dir(minerva_home, "painel-agents", "MINERVA_PAINEL_DIR")
        if painel_dir and (painel_dir / "painel.py").exists():
            ok = spawn_detached(
                [py, str(painel_dir / "painel.py"), "--projeto", str(project_dir), "--sem-portal", "--ensure"],
                project_dir,
                wait_port=3333,
            )
            status["painel_3333"] = "online (127.0.0.1:3333)" if is_port_open(3333) else ("iniciado em background (:3333)" if ok else "falha ao iniciar")
        elif shutil.which("painel"):
            ok = spawn_detached(["painel", "--projeto", str(project_dir), "--sem-portal", "--ensure"], project_dir, wait_port=3333)
            status["painel_3333"] = "online (127.0.0.1:3333)" if is_port_open(3333) else ("iniciado via PATH (:3333)" if ok else "falha ao iniciar")

    # 2. Kanban (:3334)
    if is_port_open(3334):
        status["kanban_3334"] = "online (127.0.0.1:3334)"
    else:
        kanban_dir = resolve_companion_dir(minerva_home, "kanban-agents", "MINERVA_KANBAN_DIR")
        if kanban_dir and (kanban_dir / "kanban.py").exists():
            ok = spawn_detached(
                [py, str(kanban_dir / "kanban.py"), "--projeto", str(project_dir), "--sem-portal"],
                project_dir,
                wait_port=3334,
            )
            status["kanban_3334"] = "online (127.0.0.1:3334)" if is_port_open(3334) else ("iniciado em background (:3334)" if ok else "falha ao iniciar")

    # 3. Portais e Persona Global no Maestri (quando CLI maestri ou ~/.maestri estiverem presentes)
    minerva_md_tpl = minerva_home / "templates" / "project" / ".agents" / "MINERVA.md"
    minerva_prompt = minerva_md_tpl.read_text(encoding="utf-8") if minerva_md_tpl.exists() else ""
    maestri_pref = Path.home() / ".maestri" / "preferences.json"
    if minerva_prompt and maestri_pref.exists():
        try:
            pref_doc = json.loads(maestri_pref.read_text(encoding="utf-8"))
            payload = pref_doc.setdefault("payload", {})
            roles = payload.setdefault("rolePresets", [])
            found = False
            for r in roles:
                r_name = str(r.get("name") or "").strip("` ")
                if r_name.lower() == "minerva - orquestrador central":
                    r["name"] = "Minerva - Orquestrador Central"
                    r["prompt"] = minerva_prompt
                    r.pop("workspaceId", None)  # Garante escopo global
                    found = True
                    break
            if not found:
                roles.append({
                    "color": "#5AC8FA",
                    "icon": "brain",
                    "id": "9903F97E-8F05-4620-BC28-70F0A1136CFF",
                    "name": "Minerva - Orquestrador Central",
                    "prompt": minerva_prompt,
                })
            maestri_pref.write_text(json.dumps(pref_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        except Exception:
            pass

    has_maestri_env = any(
        os.environ.get(k)
        for k in ("MAESTRI_SURFACE_ID", "MAESTRI_SOCKET", "MAESTRI_PIPE", "MAESTRI_TERMINAL_ID", "MAESTRI_WORKSPACE_ID")
    )
    maestri_bin = os.environ.get("MAESTRI_CLI") or shutil.which("maestri") or shutil.which("maestri.exe")
    if not maestri_bin:
        for mac_cand in [
            Path("/Applications/Maestri.app/Contents/Resources/cli/maestri"),
            Path.home() / "Applications" / "Maestri.app" / "Contents" / "Resources" / "cli" / "maestri",
        ]:
            if mac_cand.exists():
                maestri_bin = str(mac_cand)
                break
    if not maestri_bin:
        try:
            appimage_bins = sorted(
                Path("/tmp").glob(".mount_Maestr*/resources/cli/maestri"),
                key=lambda p: p.stat().st_mtime,
                reverse=True,
            )
            if appimage_bins:
                maestri_bin = str(appimage_bins[0])
        except Exception:
            pass

    maestri_env = os.environ.copy()
    if not maestri_env.get("MAESTRI_SOCKET"):
        try:
            socks = sorted(Path("/tmp").glob("maestri-*/maestri.sock"), key=lambda p: p.stat().st_mtime, reverse=True)
            if socks:
                maestri_env["MAESTRI_SOCKET"] = str(socks[0])
                has_maestri_env = True
        except Exception:
            pass

    if maestri_bin and (has_maestri_env or (project_dir / ".maestri").exists()):
        try:
            if minerva_prompt:
                res = subprocess.run(
                    [maestri_bin, "role", "write", "Minerva - Orquestrador Central", minerva_prompt],
                    cwd=str(project_dir),
                    env=maestri_env,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=4,
                )
                if res.returncode != 0:
                    subprocess.run(
                        [maestri_bin, "role", "create", "Minerva - Orquestrador Central", minerva_prompt, "--scope", "global"],
                        cwd=str(project_dir),
                        env=maestri_env,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        timeout=4,
                    )
            subprocess.run(
                [maestri_bin, "portal", "create", "http://localhost:3333", "Painel de Agentes"],
                cwd=str(project_dir),
                env=maestri_env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=4,
            )
            subprocess.run(
                [maestri_bin, "portal", "create", "http://localhost:3334", "Kanban"],
                cwd=str(project_dir),
                env=maestri_env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=4,
            )
            status["maestri_portals"] = "portais 3333 e 3334 acionados"
        except Exception:
            status["maestri_portals"] = "maestri detectado (portais manuais)"

    return status


def configure_session_mode(project_dir: Path, mode: str) -> str:
    """Configura o modo de sessão dos sub-agentes em .agents/session-mode.json."""
    session_file = project_dir / ".agents" / "session-mode.json"
    cache_dir = project_dir / ".agents" / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)

    if session_file.exists() and mode == "ask":
        try:
            cur = json.loads(session_file.read_text(encoding="utf-8"))
            return f"preservado ({cur.get('mode', 'ask')})"
        except Exception:
            pass

    if mode == "ephemeral":
        (cache_dir / "codex-home").mkdir(parents=True, exist_ok=True)
        (cache_dir / "claude-config").mkdir(parents=True, exist_ok=True)

    codex_home = str((cache_dir / "codex-home").resolve())
    payload = {
        "mode": mode,
        "description": (
            "ephemeral: aplica isolamento real em Claude (--no-session-persistence) e Codex (CODEX_SQLITE_HOME local em .agents/cache/). "
            "Nota: o Antigravity CLI (agy) nao possui flag nativa de sessao efemera — reutilize sempre 1 terminal fixo por papel e use Ctrl+F (Grouped View) no /resume. "
            "persistent: sub-agentes salvam no historico global para consulta via /resume (1 sessao reutilizada por papel)."
        ),
        "ephemeral_env": {
            "CODEX_SQLITE_HOME": codex_home,
            "CLAUDE_ARGS": "--no-session-persistence",
        },
        "ephemeral_recruit_commands": {
            "claude": "claude --no-session-persistence",
            "codex_powershell": f"$env:CODEX_SQLITE_HOME='{codex_home}'; codex",
            "codex_bash": f"CODEX_SQLITE_HOME='{codex_home}' codex",
            "antigravity_note": "agy nao tem flag efemera nativa; reutilize 1 terminal fixo por papel (nunca dismiss+recruit) e priorize Codex/Claude para sub-agentes descartaveis.",
        },
    }
    session_file.parent.mkdir(parents=True, exist_ok=True)
    session_file.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return f"configurado ({mode})"


def archive_previous_sprint(project_dir: Path, sprint_label: str) -> str:
    """Arquiva os cartões do sprint anterior em .kanban/archive/ e limpa o board.json para o novo Backlog."""
    board_file = project_dir / ".kanban" / "board.json"
    if not board_file.exists():
        return "board.json ainda nao existe"
    try:
        board = json.loads(board_file.read_text(encoding="utf-8"))
    except Exception:
        return "erro ao ler board.json"

    cards = board.get("cartoes") or []
    if not cards:
        return "nenhum cartao para arquivar"

    import datetime
    import re

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", sprint_label.strip()).strip("-") or "sprint"
    archive_dir = project_dir / ".kanban" / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_path = archive_dir / f"{stamp}_{slug}.json"

    archive_doc = {
        "sprint": sprint_label,
        "archived_at": datetime.datetime.now().isoformat(),
        "total_cards": len(cards),
        "cartoes": cards,
    }
    archive_path.write_text(json.dumps(archive_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    board["cartoes"] = []
    board_file.write_text(json.dumps(board, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return f"arquivado ({len(cards)} cartoes salvos em .kanban/archive/{archive_path.name})"


def main():
    parser = argparse.ArgumentParser(description="Bootstrap determinístico de projeto (/minerva)")
    parser.add_argument("project_dir", nargs="?", default=".", help="Diretório raiz do projeto")
    parser.add_argument(
        "--session-mode",
        choices=["ask", "ephemeral", "persistent"],
        default="ask",
        help="Modo de histórico de sessões dos terminais: ask (pergunta ao usuário), ephemeral (temporário sem poluir /resume global) ou persistent (salva no /resume)",
    )
    parser.add_argument(
        "--archive-sprint",
        type=str,
        default=None,
        help="Arquiva o sprint anterior em .kanban/archive/<data>_<nome>.json e limpa o board.json para o novo Backlog",
    )
    parser.add_argument("--force", action="store_true", help="Sobrescreve arquivos de template existentes")
    parser.add_argument("--json", action="store_true", help="Saída em JSON")
    args = parser.parse_args()

    minerva_home = Path(__file__).resolve().parent.parent
    templates_dir = minerva_home / "templates" / "project"
    project_dir = Path(args.project_dir).resolve()
    project_dir.mkdir(parents=True, exist_ok=True)

    report = {
        "project_dir": str(project_dir),
        "gitignore": merge_gitignore(project_dir, templates_dir / ".gitignore.minerva"),
        "created_files": [],
        "preserved_files": [],
        "mcp_json": merge_mcp_json(project_dir, templates_dir / ".mcp.json"),
        "rtk_hook": ensure_rtk_hook(project_dir),
        "session_mode": configure_session_mode(project_dir, args.session_mode),
        "agent_sort": "skipped",
        "services": {},
    }

    rel_templates = [
        ".agents/AGENTS.md",
        ".agents/MINERVA.md",
        ".agents/roles/front-end.md",
        ".agents/roles/back-end.md",
        ".agents/roles/test-qa.md",
        ".agents/roles/review.md",
        "AGENTS.md",
        "docs/spec.md",
        "docs/architecture.md",
        "docs/adr/0001-architecture-decision-template.md",
        ".kanban/board.json",
    ]
    always_sync_governance = {
        ".agents/MINERVA.md",
        ".agents/roles/front-end.md",
        ".agents/roles/back-end.md",
        ".agents/roles/test-qa.md",
        ".agents/roles/review.md",
    }
    for rel in rel_templates:
        src = templates_dir / rel
        dst = project_dir / rel
        if src.exists():
            should_force = args.force or (rel in always_sync_governance)
            if copy_if_missing(src, dst, force=should_force):
                report["created_files"].append(rel)
            else:
                report["preserved_files"].append(rel)

    if args.archive_sprint:
        report["sprint_archive"] = archive_previous_sprint(project_dir, args.archive_sprint)

    # Executa agent_sort.py para gerar .agents/skills.json
    agent_sort_script = minerva_home / "toolkits" / "agent_sort.py"
    if agent_sort_script.exists():
        try:
            subprocess.run(
                [sys.executable or "python", str(agent_sort_script), str(project_dir), "--json"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10,
                check=False,
            )
            if (project_dir / ".agents" / "skills.json").exists():
                report["agent_sort"] = ".agents/skills.json atualizado"
        except Exception as e:
            report["agent_sort"] = f"erro ({e})"

    report["services"] = ensure_services_and_portals(minerva_home, project_dir)

    # Inspeciona contas, cotas e sugestão Anti-Monocultura direto do Maestri + PC
    quotas_script = minerva_home / "toolkits" / "minerva_quotas.py"
    if quotas_script.exists():
        try:
            q_out = subprocess.run(
                [sys.executable or "python", str(quotas_script), "--json"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=8,
                check=False,
            )
            if q_out.returncode == 0 and q_out.stdout.strip():
                report["quotas"] = json.loads(q_out.stdout)
        except Exception:
            pass

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return

    print("=======================================================")
    print(f"  🐍 MINERVA WORKSPACE BOOTSTRAP: {project_dir.name}")
    print("=======================================================")
    print(f"  [0] Cofre do Obsidian: {minerva_home / 'vault'}")
    print(f"  [1] .gitignore       : {report['gitignore']} ({project_dir / '.gitignore'})")
    print(f"  [2] Governanca & Docs: {project_dir / '.agents'} | {project_dir / 'docs'}")
    print(f"  [3] Arquivos criados : {len(report['created_files'])} ({', '.join(report['created_files']) if report['created_files'] else 'nenhum novo'})")
    print(f"  [4] .mcp.json        : {report['mcp_json']} ({project_dir / '.mcp.json'})")
    print(f"  [5] Hook RTK local   : {report['rtk_hook']}")
    print(f"  [6] Modo de Sessões  : {report['session_mode']} ({project_dir / '.agents' / 'session-mode.json'})")
    print(f"  [7] Agent-Sort       : {report['agent_sort']} ({project_dir / '.agents' / 'skills.json'})")
    print(f"  [8] Painel (:3333)   : {report['services']['painel_3333']} -> http://localhost:3333")
    print(f"  [9] Kanban (:3334)   : {report['services']['kanban_3334']} -> http://localhost:3334 ({project_dir / '.kanban' / 'board.json'})")
    print(f"  [10] Portais Maestri : {report['services']['maestri_portals']}")
    if report.get("quotas", {}).get("recommended_team_codes"):
        print("  [11] Team CODES sugerido (Direto dos CLIs no PC):")
        for rec in report["quotas"]["recommended_team_codes"]:
            fo = ", ".join(rec.get("failover_presets", []))
            mdl = rec.get("recommended_model", "")
            print(f"       • {rec['role']:<36} -> {rec['preset']} [{mdl}] (Failover: {fo})")
    print("-------------------------------------------------------")
    print("  👉 PERGUNTE AO USUARIO NA RESPOSTA DO /minerva:")
    print("     1) Modo de Sessoes: [1] Temporarias/Isoladas (ephemeral - nao polui /resume global)")
    print("                         [2] Normais/Salvas no Historico (persistent - aparece no /resume)")
    print("     2) Qual e a primeira demanda ou funcionalidade que vamos construir?")
    print("=======================================================")


if __name__ == "__main__":
    main()
