<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="200" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva & AI Agents Ecosystem

**Unified Multi-Agent `init` Hub (`/minerva`), Single Global Root (`~/.minerva`), Per-Project Context Economy & Obsidian Vault.**

🌐 **[English](README.en.md)** | **[Português](README.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-quick-cross-platform-installation)
[![skills.sh](https://img.shields.io/badge/skills.sh-minerva--workspace-blue.svg?style=flat-square)](skills/)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20integrated-purple.svg?style=flat-square)](vault/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## 💡 Why This Project Exists

AI coding tools evolve every week, and every CLI or IDE creates its own isolated folder (`~/.claude`, `~/.codex`, `~/.gemini`, `~/.agents`). For anyone **getting started** — or switching between models daily — this forces you to **re-download the same skills across different paths, reconfigure MCP servers, and repeat project rules over and over**.

**`minerva-workspace`** is built as a centralized **`init` in `~/.minerva`**:

1. **One Global Root (`~/.minerva` / `%USERPROFILE%\.minerva`):** install once; the setup script scans existing skills across your system (migrating without duplicates), installs all curated project skills from `skills.sh`, and points **Claude Code**, **Codex**, **Antigravity / Gemini CLI**, and **Maestri** to the exact same folder.
2. **Full Per-Project Bootstrap (`/minerva`):** outside a project your shell stays clean; inside any repo, typing **`/minerva`** runs the complete project governance setup (`.gitignore`, `.agents/`, `docs/`, `ai-memory`, `.kanban/board.json`, Dashboard `:3333` + Kanban `:3334`, Maestri Portals, and scoped context economy).
3. **Zero Upstream Doc Duplication:** community skills resolve via **`skills.sh`**, and companion apps keep their full manuals in their official repositories.

---

## Global Structure (`~/.minerva`)

```text
~/.minerva/ (or %USERPROFILE%\.minerva -> repository root)
│
├── 📁 skills/                         <-- All centralized skills (3 authorial + 188 via skills.sh)
├── 📁 templates/project/              <-- /minerva bootstrap templates (.agents/, docs/, .kanban/, .mcp.json, rtk)
├── 📄 skills-manifest.json            <-- Single unified skills list (no core/full split)
├── 📄 mcp_config.json                 <-- Base Model Context Protocol (MCP) configuration
├── 📁 toolkits/                       <-- Vibe Coding Toolkit, agent_sort.py & statusline
├── 📁 vault/                          <-- Direct Obsidian Vault root (PT-BR)
│   ├── 📄 _Hub de Skills & MCPs.md
│   ├── 📄 _Arquitetura e Documentação do Ecossistema.md
│   ├── 📄 _Guia de Replicação em Novo PC.md
│   ├── 📁 Workspace/                  <-- Minerva Orchestration, Council & Team CODES
│   ├── 📁 Skills/                     <-- Concise skill notes (includes painel-agents & kanban-agents) + 7 Hubs
│   ├── 📁 MCP/                        <-- Manuals (ai-memory, rea, agent-desktop, magicpath, context-mode)
│   ├── 📁 MODS/                       <-- vibe-coding-toolkit & ai-statusline
│   └── 📁 Frameworks/                 <-- Agent libraries (alethe, claude-cookbooks, etc.)
│
├── 📄 setup.bat                       <-- Windows installer (CMD)
├── 📄 setup.ps1                       <-- Windows installer (PowerShell)
└── 📄 setup.sh                        <-- Linux & macOS installer
```

---

## Quick Cross-Platform Installation

### Step 1 — Clone & run Global Setup (1 command):

**Windows (PowerShell):**
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git $HOME\.minerva
cd $HOME\.minerva
.\setup.ps1
```
*(Or `setup.bat` in CMD).*

**Linux / macOS:**
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/.minerva
cd ~/.minerva
chmod +x setup.sh && ./setup.sh
```

**What the installer automates:**
1. Scans pre-existing skills in `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills`, and `~/.agents/skills`, moving them into `~/.minerva/skills` with zero duplicates.
2. Uses `~/.minerva` as the single canonical root and links all AI CLI skill folders to `~/.minerva/skills`.
3. Installs all curated skills from `skills-manifest.json` via `npx skills add` and checks/clones `painel-agents` & `kanban-agents`.

*(Alternative quick entry: `npx skills add lk-feitosa/minerva-workspace` — then run `/minerva` inside your terminal to guide the global setup).*

---

## What `/minerva` Executes Inside a Project

When opening any project (**Claude Code**, **Codex**, **Gemini CLI**, **Antigravity**, or **Maestri**) and running **`/minerva`**, it replaces manual mega-prompts by executing:

1. **Git Shielding (`.gitignore`):** keeps `.maestri/`, `.kanban/`, `.agents/cache/`, `.ai-memory/cache/`, `graphify-out/`, `*.session`, `*.tmp`, and env/build files out of Git.
2. **Agent Governance (`.agents/`) & Scoped Economy:** scaffolds `.agents/AGENTS.md`, `.agents/MINERVA.md` (10 Fundamental Laws), and `.agents/roles/` (`front-end`, `back-end`, `test-qa`, `review`), configures `.mcp.json` (`context-mode` + `ai-memory`), and adds optional local `rtk` hook in `.claude/settings.local.json`.
3. **Product Docs (`docs/`):** initializes `docs/spec.md`, `docs/architecture.md`, and `docs/adr/`.
4. **Memory, Kanban & Maestri Portals:** initializes `ai-memory`, creates `.kanban/board.json` (5 columns), ensures **Painel (`:3333`)** + **Kanban (`:3334`)** are running silently, and opens both Maestri Portals automatically (`maestri portal create`).
5. **Demand Modes:** Standard agile flow by default; `[GRILL-ME]` / `[CONSELHO]` trigger critical stress-testing on demand; micro-tweaks run as 1-line fast-track edits.
6. **Semantic Branches & Unrestricted `cwd`:** forbids `sprint-1`/`sprint-2`, enforces `feature/<slug>` / `fix/<slug>` at the project root.
7. **Consultative Multi-Model Delegation (`alethe` + `maestri`):** checks live accounts/quotas before spawning Team CODES terminals and asks for confirmation first.

---

## How to Open the Vault in Obsidian

1. Open **Obsidian** and click **"Open folder as vault"**.
2. Select **`~/.minerva/vault`** (or `<REPO_DIR>/vault`).
3. Start from **`_Hub de Skills & MCPs.md`** and **`Workspace/Orquestração de Projetos - Minerva & Conselho.md`**.

---

## 🧩 Official Companion Apps

Full installation guides and technical specs live in each upstream repository:

| Project | Port | Role in Ecosystem | Official Repository |
| :--- | :--- | :--- | :--- |
| **Painel de Agentes** | `127.0.0.1:3333` | Passive telemetry, 3D quotas, live logs, and architecture graph | [`lk-feitosa/painel-agents`](https://github.com/lk-feitosa/painel-agents) |
| **Kanban Agents** | `127.0.0.1:3334` | Lightweight offline board saved to `.kanban/board.json` per repo | [`lk-feitosa/kanban-agents`](https://github.com/lk-feitosa/kanban-agents) |

---

## Credits, Attribution & Licenses

All intellectual property, trademarks, and third-party code belong strictly to their original authors. Full attribution links:  
👉 **[CREDITS.md](CREDITS.md)** *(Português: [CREDITS.pt-br.md](CREDITS.pt-br.md))*
