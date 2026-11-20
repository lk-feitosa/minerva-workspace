<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="200" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva & AI Agents Ecosystem

**Unified Multi-Agent `init` Hub (`/minerva-setup` & `/minerva`), Single Global Root (`~/.minerva`), Per-Project Context Economy & Obsidian Vault.**

**[English](README.en.md)** | **[Português](README.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-pc-installation-1x-per-machine)
[![skills.sh](https://skills.sh/b/lk-feitosa/minerva-workspace)](https://skills.sh/lk-feitosa/minerva-workspace)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20integrated-purple.svg?style=flat-square)](vault/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## Why This Project Exists

AI coding tools evolve every week, and every CLI or IDE creates its own isolated folder (`~/.claude`, `~/.codex`, `~/.gemini`, `~/.agents`). For anyone getting started — or switching between models daily — this forces you to re-download the same skills across different paths, reconfigure MCP servers, and repeat project rules over and over.

**`minerva-workspace`** is built as a centralized **`init` in `~/.minerva`**:

1. **One Global Root (`~/.minerva` / `%USERPROFILE%\.minerva`):** install once via **`/minerva-setup`** (or `setup.ps1`/`setup.sh`); the installer scans pre-existing **skills and global MCPs** across your system (migrating and merging with zero duplicates), installs all curated project skills from `skills.sh`, and links **Claude Code**, **Codex**, **Antigravity / Gemini CLI**, and **[Maestri](https://www.themaestri.app/pt-br)** to the exact same folder.
2. **Full Per-Project Bootstrap (`/minerva`):** outside a project your shell stays clean; inside any repo, select the **Minerva Persona** first and run **`/minerva`** to execute the deterministic project setup (`minerva_bootstrap.py`: `.gitignore`, `.agents/`, `docs/`, `.mcp.json`, `rtk`, `ponytail`, `ai-memory`, `.kanban/board.json`, Dashboard `:3333` + Kanban `:3334`, and Maestri Portals).
3. **Smart Multi-Model Orchestration (Anti-Monoculture + Automatic AI Failover):** when delegating tasks to **Team CODES**, Minerva queries local CLIs directly to pick the best model per role based on your **live accounts and quotas** (never spawning a monoculture team on a single AI) and, if a terminal fails, **automatically switches to another available AI** and hands off the task (instead of throwing an error or coding it herself).

---

## Skill Commands (`skills.sh`)

Installing via `skills.sh` (`npx skills add lk-feitosa/minerva-workspace -g -y`) gives you **4 slash commands**:

| Command | Scope | Purpose |
| :--- | :--- | :--- |
| **`/minerva-setup`** | **1x on PC** (Any terminal) | Clones/updates `~/.minerva`, migrates existing skills & global MCPs without duplicates, creates CLI junctions, and installs the full catalog + `painel-agents` & `kanban-agents`. |
| **`/minerva`** | **Inside each Project Workspace** | *(Run after selecting the Minerva Persona)* Bootstraps the repo (`minerva_bootstrap.py`) and activates token-saving orchestration, Council/Grill-Me, and Team CODES. |
| **`/painel-agents`** | Project / Global | Opens, inspects quotas, or auto-heals the **Agent Dashboard** (`http://127.0.0.1:3333`). |
| **`/kanban-agents`** | Project | Opens or manages the project's **Minimalist Kanban** (`http://127.0.0.1:3334` / `.kanban/board.json`). |

---

## Global Structure (`~/.minerva`)

```text
~/.minerva/ (or %USERPROFILE%\.minerva -> single canonical root)
│
├── skills/                            <-- All centralized skills (4 authorial + 19 packages via skills.sh)
│   ├── minerva-setup/                 <-- /minerva-setup (Global PC setup)
│   ├── minerva/                       <-- /minerva (Per-project workspace bootstrap & orchestration)
│   ├── painel-agents/                 <-- /painel-agents (Dashboard :3333)
│   └── kanban-agents/                 <-- /kanban-agents (Kanban :3334)
├── templates/project/                 <-- /minerva bootstrap templates (.agents/, docs/, .kanban/, .mcp.json, rtk)
├── skills-manifest.json               <-- Single unified skills list (no core/full split)
├── mcp_config.json                    <-- Global MCP servers (ai-memory, rea, agent-desktop)
├── toolkits/                          <-- minerva_bootstrap.py, minerva_quotas.py, agent_sort.py & statusline
├── vault/                             <-- Direct Obsidian Vault root (PT-BR)
│   ├── _Hub de Skills & MCPs.md
│   ├── _Arquitetura e Documentação do Ecossistema.md
│   ├── _Guia de Replicação em Novo PC.md
│   ├── Workspace/                     <-- Minerva Orchestration, Council & Team CODES
│   ├── Skills/                        <-- Concise skill notes + 7 Category Hubs
│   ├── MCP/                           <-- Manuals (ai-memory, rea, agent-desktop, context-mode)
│   ├── MODS/                          <-- vibe-coding-toolkit & ai-statusline
│   └── Frameworks/                    <-- Agent libraries (alethe, claude-cookbooks, etc.)
│
├── setup.bat                          <-- Windows installer (CMD)
├── setup.ps1                          <-- Windows installer (PowerShell)
└── setup.sh                           <-- Linux & macOS installer
```

---

## PC Installation (1x per Machine)

### Option A — Via `skills.sh` + `/minerva-setup`:
```bash
npx skills add lk-feitosa/minerva-workspace -g -y
```
Then open your agent in the terminal and run **`/minerva-setup`**.

### Option B — Direct Clone + Native Installer:

**Windows (PowerShell):**
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git $HOME\.minerva
cd $HOME\.minerva
.\setup.ps1
```

**Linux / macOS:**
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/.minerva
cd ~/.minerva
chmod +x setup.sh && ./setup.sh
```

**What `/minerva-setup` (`setup.ps1` / `setup.sh`) automates:**
1. **Deduplicated Skill Migration:** scans `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills`, and `~/.agents/skills`, moving them into `~/.minerva/skills` with zero duplicates.
2. **Deduplicated Global MCP Sync:** merges global MCPs (`ai-memory`, `rea`, `agent-desktop`) into `~/.gemini/mcp_config.json` and `~/.claude.json` while preserving your existing custom MCPs (keeping `context-mode` scoped to each project's `.mcp.json`).
3. **Full Catalog Install:** installs all 19 curated skill packages from `skills-manifest.json` via `npx skills add` and checks/clones `painel-agents` & `kanban-agents` in `~/.minerva/tools/`.

---

## How to Use Inside a Project (Step by Step)

Whenever you open a new or existing project:

1. **Step 1 — Select the Minerva Persona:** in your main project terminal (especially inside **[Maestri Canvas](https://www.themaestri.app/pt-br)**), select the **"Minerva - Orquestrador Central"** role/persona first.
2. **Step 2 — Run `/minerva`:** type **`/minerva`** in the project terminal.

### What `/minerva` executes inside the project workspace:
1. **1-Command Bootstrap (`minerva_bootstrap.py`):** shields `.gitignore`, scaffolds `.agents/` (`AGENTS.md`, `MINERVA.md`, `roles/`), `docs/` (`spec.md`, `architecture.md`, `adr/`), `.kanban/board.json`, and classifies project skills in `.agents/skills.json` (**DAILY vs. LIBRARY** via `agent_sort.py`).
2. **Active Token Economy:** configures workspace `.mcp.json` (`context-mode` + `ai-memory`), enables the optional local `rtk` hook in `.claude/settings.local.json`, and enforces **`ponytail`** minimal-diff discipline.
3. **Dashboard (`:3333`), Kanban (`:3334`) & Maestri Portals:** ensures both servers are running silently and opens both Maestri Portals automatically.
4. **All Models & Quotas Directly from Local CLIs + Tier N-1 Policy (`minerva_quotas.py` — Anti-Monoculture):** queries installed CLIs directly (`agy`, `codex`, `claude`) to list **every available model** and defaults to the **Tier N-1 / daily workhorse model** of each account (e.g., `Hydrogen` below `Neon`/`Argon` on Gemini; `Sonnet` below `Fable`/`Opus` on Claude; `medium` effort on Codex), reserving the flagship top model only when explicitly requested (`--top-tier`), **without spawning an all-same-AI monoculture team**.
5. **Mandatory Backlog Approval Gate + Previous Sprint Archiving (`--archive-sprint`):** upon receiving a request, archives the previous sprint into `.kanban/archive/`, creates **the complete task Backlog in `.kanban/board.json`**, and **waits for your explicit Backlog approval ("OK")** before Team CODES starts executing tasks.
6. **Per-Task Skill Discovery & Injection (`agent_sort.py --match` + `find-skills`):** combines role skills (`.agents/roles/`) and stack skills (`.agents/skills.json`) with instant local matching (`agent_sort.py --match`) and remote discovery via **`find-skills`** (`npx skills find <term>`), explicitly injecting skill paths into each terminal prompt.
7. **Configurable Ephemeral vs. Persistent Sessions + Automatic Terminal AI Failover:** lets you choose between **ephemeral workspace-isolated sessions in `.agents/cache/`** (so your global CLI `/resume` list is never polluted by sub-agent sessions) or **persistent sessions** (1 reused session per role). If a terminal fails in Maestri, Minerva **replaces it in-place (`--replace`) with another available AI and hands off the task** (never erroring out or coding it herself).

### What Minerva replies when `/minerva` completes:

1. The workspace checklist and exact file paths created (`.gitignore`, `.agents/`, `docs/`, `.mcp.json`, `rtk`, `skills.json`, Dashboard `:3333`, and Kanban `:3334`).
2. The **live Accounts, Models & Quotas table** pulled directly from your local CLIs (`agy`, `codex`, `claude`) with the **Anti-Monoculture + Failover** recommendation for Team CODES.
3. **Two quick questions before coding:**
   * **Which session mode do you want for sub-agents in this project?**
     * `[1] Ephemeral / Workspace-Isolated Sessions (ephemeral — Recommended)`: stored inside `.agents/cache/` so your global CLI `/resume` history stays 100% clean.
     * `[2] Normal / Persistent Sessions (persistent)`: saved in your global CLI history for later inspection via `/resume`.
   * **What is the first feature or task we are building?**

---

## Obsidian Vault & Complete Path Map

1. Open **Obsidian** and click **"Open folder as vault"**.
2. Select **`~/.minerva/vault`** (on Windows: **`%USERPROFILE%\.minerva\vault`**, e.g. `C:\Users\YourUser\.minerva\vault`).
3. Start from **`_Hub de Skills & MCPs.md`** and **`Workspace/Orquestração de Projetos - Minerva & Conselho.md`**.

### Complete Map of Saved Paths & Local Ports

| Component | Local Path / URL | Scope |
| :--- | :--- | :--- |
| **Minerva Single Root** | `~/.minerva` (`%USERPROFILE%\.minerva`) | Global (PC) |
| **Obsidian Vault** | **`~/.minerva/vault`** (`%USERPROFILE%\.minerva\vault`) | Global (PC) |
| **Centralized Skills** | `~/.minerva/skills` *(linked via junction/symlink to `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills`, and `~/.agents/skills`)* | Global (PC) |
| **Global MCP Config** | `~/.minerva/mcp_config.json` *(merged into `~/.gemini/mcp_config.json` and `~/.claude.json`)* | Global (PC) |
| **Agent Dashboard (Web / Portal)** | `http://localhost:3333` *(installed at `~/.minerva/tools/painel-agents`)* | Local Server |
| **Minimalist Kanban (Web / Portal)** | `http://localhost:3334` *(installed at `~/.minerva/tools/kanban-agents`)* | Local Server |
| **Governance, Roles & Laws (`/minerva`)** | `<PROJECT>/.agents/MINERVA.md`, `.agents/AGENTS.md`, `.agents/roles/` | Per Project |
| **Project Skills & Session Mode** | `<PROJECT>/.agents/skills.json` & `<PROJECT>/.agents/session-mode.json` (cache in `.agents/cache/`) | Per Project |
| **Spec, Architecture & ADRs** | `<PROJECT>/docs/spec.md`, `<PROJECT>/docs/architecture.md`, `<PROJECT>/docs/adr/` | Per Project |
| **Project Kanban Board File** | `<PROJECT>/.kanban/board.json` | Per Project |
| **Workspace MCPs & Context Economy** | `<PROJECT>/.mcp.json` (`context-mode` + `ai-memory`) & `<PROJECT>/.claude/settings.local.json` (`rtk`) | Per Project |

---

## Official Companion Apps

Full installation guides and technical specs live in each upstream repository:

| Project | Port | Role in Ecosystem | Official Repository |
| :--- | :--- | :--- | :--- |
| **Painel de Agentes** | `127.0.0.1:3333` | Passive telemetry, 3D quotas, live logs, and architecture graph | [`lk-feitosa/painel-agents`](https://github.com/lk-feitosa/painel-agents) |
| **Kanban Agents** | `127.0.0.1:3334` | Lightweight offline board saved to `.kanban/board.json` per repo | [`lk-feitosa/kanban-agents`](https://github.com/lk-feitosa/kanban-agents) |

---

## Credits, Attribution & Licenses

All intellectual property, trademarks, and third-party code belong strictly to their original authors. Full attribution links:  
**[CREDITS.md](CREDITS.md)** *(Português: [CREDITS.pt-br.md](CREDITS.pt-br.md))*
