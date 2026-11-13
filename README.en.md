<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="200" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva & AI Agents Ecosystem

**Unified Multi-Agent Orchestration Hub (`/minerva`), Portable `skills.sh` Base, Per-Workspace Context Economy, MCP Servers & PT-BR Obsidian Vault.**

🌐 **[English](README.en.md)** | **[Português](README.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-quick-cross-platform-installation)
[![skills.sh](https://img.shields.io/badge/skills.sh-minerva--workspace-blue.svg?style=flat-square)](skills/)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20integrated-purple.svg?style=flat-square)](vault/Agentes/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## Overview

This repository centralizes a multi-agent software development infrastructure, connecting leading AI coding tools (**Antigravity / Gemini CLI**, **Claude Code**, **Codex**, and **Maestri Canvas**) under a clean hybrid architecture:

* **Single Global Skills Base (`skills` + `setup`):** keeps lightweight skills centralized via junctions/symlinks (without duplicating across tools or projects) using **`skills.sh`** as the official source.
* **Per-Workspace Activation (`/minerva`):** inside any project terminal, `/minerva` activates scoped context economy (**Context Mode**, **Ponytail**, local **RTK** hook, optional **Graphify**) and starts **Dashboard (`:3333`) + Kanban (`:3334`)**, leaving the rest of the system clean.

```text
minerva-workspace/                     <-- Single Canonical Repository Root
│
├── 📁 skills/                         <-- Authorial Skills (minerva, painel-agents, kanban-agents)
├── 📁 templates/project/              <-- Portable workspace templates (.mcp.json, AGENTS.md, local rtk hook)
├── 📄 skills-manifest.json            <-- Curated skills.sh catalog (core & full profiles)
├── 📄 mcp_config.json                 <-- Base Model Context Protocol (MCP) configuration
├── 📁 toolkits/                       <-- Vibe Coding Toolkit & scripts (statusline)
├── 📁 vault/Agentes/                  <-- Lean Obsidian Knowledge Vault (PT-BR)
│   ├── 📁 Workspace/                  <-- Minerva Architecture, Council & Team CODES
│   ├── 📁 Skills/                     <-- Concise PT-BR skill summaries + 7 Category Hubs
│   ├── 📁 MCP/                        <-- Manuals (ai-memory, rea, agent-desktop, magicpath)
│   ├── 📁 MODS/                       <-- Curated toolkits (vibe-coding-toolkit)
│   ├── 📁 Frameworks/                 <-- Agent libraries (alethe, claude-cookbooks, etc.)
│   ├── 📁 Opcionais/                  <-- Companion tools (painel-agents, kanban-agents, ai-statusline)
│   └── 📄 _Hub de Skills & MCPs.md    <-- Obsidian interactive hub & dashboard
│
├── 📄 setup.bat                       <-- 1-Click Windows installer (CMD)
├── 📄 setup.ps1                       <-- 1-Click Windows installer (PowerShell)
└── 📄 setup.sh                        <-- 1-Click Linux & macOS installer
```

---

## Quick Cross-Platform Installation

Install directly via **`skills.sh`** or clone the repository once to provision the unified global base.

### Via `skills.sh` (1-Command Entry):

```bash
npx skills add lk-feitosa/minerva-workspace
```
Then open your AI CLI (**Claude Code**, **Codex**, **Gemini CLI**, or **Antigravity**) and type **`/minerva`** — the skill guides global bootstrap if missing or initializes the current project workspace.

---

### On Windows:

Open PowerShell (or Command Prompt) and run:
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
.\setup.ps1
```
*(Or CMD: `setup.bat`. Pass `.\setup.ps1 -Profile full` to install the extended community catalog as well).*

The script automatically provisions NTFS Junctions linking the repository to standard agent paths (`~/.agents`, `~/.codex/skills`, `~/.claude/skills`, and `~/.gemini/config/skills`) and installs the curated **`core`** `skills.sh` profile.

---

### On Linux or macOS:

Open your terminal and run:
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
chmod +x setup.sh
./setup.sh
```
*(Pass `./setup.sh --full` for the extended catalog).*

The script creates symbolic links (`~/.agents`, `~/.codex/skills`, `~/.claude/skills`, `~/.gemini/config/skills`), installs the curated `skills.sh` packs, and checks companion tools.

---

## How to Open the Vault in Obsidian

1. Open **Obsidian**.
2. Click **"Open folder as vault"**.
3. Select the directory:
   * **On Windows:** `<REPO_DIR>\vault\Agentes` (or `%USERPROFILE%\.agents\vault\Agentes`)
   * **On Linux/macOS:** `<REPO_DIR>/vault/Agentes` (or `~/.agents/vault/Agentes`)
4. Done! The vault opens with:
   * **Excalidraw** pre-configured in Dark Mode.
   * Essential community plugins enabled.
   * Interactive dashboard in `_Hub de Skills & MCPs.md` and 7 Graph Category Hubs.
   * Master workflow spec in `Workspace/Orquestração de Projetos - Minerva & Conselho.md`.

### Managing Skills via `skills.sh`
```bash
npx skills find <query>         # Discover new skills on skills.sh
npx skills update -g            # Update installed global skills
```

---

## Orchestration Architecture: Minerva, Economy & Team CODES

Explore the full architectural guide inside Obsidian:  
👉 **`Workspace/Orquestração de Projetos - Minerva & Conselho.md`**

* **Minerva (`/minerva`):** Master Orchestrator preparing each project workspace, enabling token optimization, and coordinating semantic branches (`feature/<slug>`, `fix/<slug>`).
* **The 5 Council Advisors (`llm-council`) + `grill-me`:** Contrarian, First-Principles, Expansionist, Outsider, and Executor triggered on demand before coding critical decisions.
* **Project-Scoped Context Economy:** **Context Mode** (`npx -y context-mode` in project `.mcp.json`), **Ponytail** (minimal diffs), **RTK** (optional local `.claude/settings.local.json` hook), and **Graphify** (optional AST graph).
* **Team CODES:** 12-role engineering pipeline (`spec`, `plan`, `dev`, `front-end`, `back-end`, `test`, `qa`, `qualidade`, `webperf`, `code-simpl`, `review`, `ship`).

---

## 🧩 Official Companion Apps (Auto-Started with `/minerva`)

1. **📊 [Agent Dashboard (`painel-agents`)](https://github.com/lk-feitosa/painel-agents):**
   * **Local Port:** `http://127.0.0.1:3333/`
   * **Features:**
     * **Real-Time Telemetry & 3D Quotas:** 5h and weekly capacity meters (Antigravity / Gemini, Claude Code, Codex) with task synchronization.
     * **Live Activity Logs Feed (`📜 Logs`):** Chronological timeline of incoming demands, Kanban updates, and terminal dispatches.
     * **Live Architecture Graph (`🗺️ Architecture`):** Interactive real-time dependency graph (60 FPS SVG) with glowing markers for files edited in the last 15 minutes and mission dispatch controls.
   * **Maestri Portal:** `maestri portal create http://localhost:3333 "Painel de Agentes"`

2. **📋 [Kanban for Agents (`kanban-agents`)](https://github.com/lk-feitosa/kanban-agents):**
   * **Local Port:** `http://127.0.0.1:3334/`
   * **Features:**
     * **Minimalist Agile Board:** Lightweight (< 20 MB RAM, zero Docker, zero auth), persisted in `.kanban/board.json` at each project's root.
     * **Sprint Cycles:** Switch between active board and archived sprints with 1-click sprint archiving.
     * **Scroll Preservation & Anti-Collision:** Zero jump on refresh and automatic port fallback if `3334` is busy.
   * **Maestri Portal:** `maestri portal create http://localhost:3334 "Kanban"`

---

## Autonomous Setup via AI Agent (Ready-to-Use Prompt)

If you use an AI assistant in your terminal or editor (**Antigravity**, **Claude Code**, **Codex**, or **Cursor**) and prefer it to configure your OS automatically, clone this repository and paste the prompt below:

```text
You are my AI assistant configuring this computer.
I just cloned Minerva Workspace (minerva-workspace) onto this machine.
Please configure my environment to adopt this unified global architecture:

1. Identify my Operating System (Windows / Linux / macOS) and the directory where this repository was cloned.
2. Run the native setup script (`.\setup.ps1` on Windows or `./setup.sh` on Linux/macOS) — or create the global links pointing to this repository:
   - Windows (NTFS Junctions):
     * %USERPROFILE%\.agents -> [this_repository_path]
     * %USERPROFILE%\.codex\skills -> [this_repository_path]\skills
     * %USERPROFILE%\.claude\skills -> [this_repository_path]\skills
     * %USERPROFILE%\.gemini\config\skills -> [this_repository_path]\skills
   - Linux / macOS (ln -s):
     * ~/.agents -> [this_repository_path]
     * ~/.codex/skills -> [this_repository_path]/skills
     * ~/.claude/skills -> [this_repository_path]/skills
     * ~/.gemini/config/skills -> [this_repository_path]/skills
3. Validate that Node.js, Python 3, and Git are on PATH and confirm the curated 'core' skills profile from `skills-manifest.json` was installed.
4. Confirm the Obsidian vault is at 'vault/Agentes' and print a concise summary with the status of each configured item.
```

---

## Credits, Attribution & Licenses

This repository acts as an integration hub. All intellectual property, trademarks, and third-party code belong strictly to their original authors (Anthropic, Vercel Labs, Fabio Akita, DietrichGebert, mksglu, rtk-ai, Graphify Labs, Addy Osmani, Matt Pocock, Affaan M, Composio, etc.).

See the full attribution table:  
👉 **[CREDITS.md](CREDITS.md)** *(Versão em português: [CREDITS.pt-br.md](CREDITS.pt-br.md))*
