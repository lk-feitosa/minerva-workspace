<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="200" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva & AI Agents Ecosystem

**Unified Multi-Agent `init` Hub (`/minerva`), Portable `skills.sh` Base, Per-Workspace Context Economy & Obsidian Knowledge Vault.**

🌐 **[English](README.en.md)** | **[Português](README.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-quick-cross-platform-installation)
[![skills.sh](https://img.shields.io/badge/skills.sh-minerva--workspace-blue.svg?style=flat-square)](skills/)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20integrated-purple.svg?style=flat-square)](vault/Agentes/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## 💡 Why This Project Exists

The AI tooling landscape shifts every week, and every CLI or IDE expects its own isolated directory (`~/.claude`, `~/.codex`, `~/.gemini`, `~/.agents`). For anyone **just getting started** — or switching between multiple coding agents daily — that means **downloading the same skills over and over across different paths, reconfiguring MCP servers, and duplicating setup work on every project**.

**`minerva-workspace`** is designed as a centralized **`init` starter kit**:

1. **One Global Brain:** clone or install once, and link **Claude Code**, **Codex**, **Antigravity / Gemini CLI**, and **Maestri** to the exact same canonical skills and MCP configuration (via junctions/symlinks, zero duplication).
2. **Scoped Project Activation (`/minerva`):** outside a project your shell stays untouched; inside any workspace, running `/minerva` enables context economy, local companion tools, and structured orchestration strictly for that folder.
3. **Zero Upstream Doc Bloat:** community skills come straight from **`skills.sh`**, and companion/upstream tools keep their full documentation in their own official repositories.

---

## Repository Structure

```text
minerva-workspace/                     <-- Single Canonical Repository Root
│
├── 📁 skills/                         <-- Authorial Skills (minerva, painel-agents, kanban-agents)
├── 📁 templates/project/              <-- Project templates (.mcp.json, AGENTS.md, local rtk hook)
├── 📄 skills-manifest.json            <-- Curated skills.sh catalog (core: 35 | full: 188)
├── 📄 mcp_config.json                 <-- Base Model Context Protocol (MCP) configuration
├── 📁 toolkits/                       <-- Vibe Coding Toolkit & terminal statusline
├── 📁 vault/Agentes/                  <-- Lean Obsidian Knowledge Vault (PT-BR, 7 Category Hubs)
├── 📄 setup.bat                       <-- Windows installer (CMD)
├── 📄 setup.ps1                       <-- Windows installer (PowerShell)
└── 📄 setup.sh                        <-- Linux & macOS installer
```

---

## Quick Cross-Platform Installation

### Option 1 — Quick Entry via `skills.sh`:
```bash
npx skills add lk-feitosa/minerva-workspace
```
Open your AI CLI (**Claude Code**, **Codex**, **Gemini CLI**, or **Antigravity**) in any folder and type **`/minerva`** — the skill walks through global bootstrap (if missing) and initializes the current project.

### Option 2 — Clone + Full Global Base (1 command):

**Windows (PowerShell):**
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
.\setup.ps1
```
*(Or `setup.bat` in CMD. Pass `.\setup.ps1 -Profile full` to install the extended community catalog too).*

**Linux / macOS:**
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
chmod +x setup.sh && ./setup.sh
```
*(Pass `./setup.sh --full` for the extended catalog).*

The setup creates global links (`~/.agents`, `~/.codex/skills`, `~/.claude/skills`, and `~/.gemini/config/skills`), installs the curated **`core`** profile (**35 `skills.sh` skills** + **3 authorial**), and verifies companion repos.

---

## Architecture: `/minerva`, Context Economy & Orchestration

* **Minerva (`/minerva`):** Configures only the current workspace (`.mcp.json`, `AGENTS.md`, `.kanban/board.json`) and coordinates multi-agent work across semantic branches (`feature/<slug>`, `fix/<slug>`).
* **5-Advisor Council (`llm-council`) + `grill-me`:** On-demand stress testing and critical questioning before major architectural decisions.
* **Project-Scoped Context Economy:**
  * [`context-mode`](https://github.com/mksglu/context-mode) *(workspace MCP)* — sandboxes heavy commands and large logs outside the chat window.
  * [`ponytail`](https://github.com/DietrichGebert/ponytail) *(in `core`)* — enforces minimal, clean diffs without over-engineering.
  * [`rtk`](https://github.com/rtk-ai/rtk) *(optional local hook in `.claude/settings.local.json`)* — compacts noisy CLI outputs per project.
  * [`graphify`](https://github.com/Graphify-Labs/graphify) *(optional AST CLI)* — builds a local codebase graph (`graphify-out/`) to avoid repetitive searches.
* **Ready-to-Use UI & Design Stack:** `design-taste-frontend`, `awesome-design-md` ([VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)), `transitions-dev` + `transitions-polish` ([transitions.dev](https://github.com/Jakubantalik/transitions.dev)), `shadcn` + `@react-bits` registry ([react-bits](https://github.com/DavidHDev/react-bits)), `magicpath`, and `vercel-react-best-practices`.
* **Obsidian Vault:** open `<REPO_DIR>/vault/Agentes` as an Obsidian vault and start with `_Hub de Skills & MCPs.md` and `Workspace/Orquestração de Projetos - Minerva & Conselho.md`.

### Managing Skills via `skills.sh`
```bash
npx skills find <query>         # Discover new skills from skills.sh
npx skills update -g            # Update installed global skills
```

---

## 🧩 Official Companion Apps

Launched automatically by `/minerva` per workspace *(full documentation lives in each project's official repository)*:

| Project | Port / Scope | Role in Ecosystem | Official Repository |
| :--- | :--- | :--- | :--- |
| **Painel de Agentes** | `127.0.0.1:3333` | Live telemetry, 3D model quotas, logs, and architecture graph | [`lk-feitosa/painel-agents`](https://github.com/lk-feitosa/painel-agents) |
| **Kanban Agents** | `127.0.0.1:3334` | Lightweight offline board stored in `.kanban/board.json` per repo | [`lk-feitosa/kanban-agents`](https://github.com/lk-feitosa/kanban-agents) |

---

## Autonomous Setup via AI Agent (Optional)

If you prefer an AI assistant (**Claude Code**, **Codex**, **Gemini CLI**, **Antigravity**, or **Cursor**) to run the setup after cloning, paste this prompt:

```text
I just cloned minerva-workspace onto this machine.
Detect my OS and run the native installer (`.\setup.ps1` on Windows or `./setup.sh` on Linux/macOS) to create global links (~/.agents, ~/.codex/skills, ~/.claude/skills, ~/.gemini/config/skills), install the 'core' profile from `skills-manifest.json`, and validate Git, Node.js, and Python 3. Print a concise summary confirming the Obsidian vault path (`vault/Agentes`) and setup status.
```

---

## Credits, Attribution & Licenses

All intellectual property, trademarks, and third-party code belong strictly to their original authors. Full attribution links:  
👉 **[CREDITS.md](CREDITS.md)** *(Português: [CREDITS.pt-br.md](CREDITS.pt-br.md))*
