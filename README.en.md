<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="180" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva & AI Agents Ecosystem

**Unified Multi-Agent Orchestration Hub, Library of 368 Battle-Tested Skills, MCP Servers & Obsidian Knowledge Vault.**

🌐 **[English](README.en.md)** | **[Português](README.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#quick-cross-platform-installation)
[![Skills: 368](https://img.shields.io/badge/skills-368%20curated-blue.svg?style=flat-square)](skills/)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20integrated-purple.svg?style=flat-square)](vault/Agentes/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## Overview

This repository centralizes a state-of-the-art agentic software development infrastructure, seamlessly connecting industry-leading AI assistants (**Antigravity / Gemini CLI**, **Claude Code**, **Codex**, **Hermes Agent**, and **Maestri Canvas**) under a unified and synchronized architecture.

```text
agents/                                <-- Repository Root
│
├── 📁 skills/                         <-- 368 Ready-to-use development skills
├── 📁 mcp_config.json                 <-- Unified Model Context Protocol (MCP) servers
├── 📁 toolkits/                       <-- Vibe Coding Toolkit & advanced playbooks
├── 📁 vault/Agentes/                  <-- Complete Obsidian Knowledge Vault
│   ├── 📁 Workspace/                  <-- Minerva Architecture, Council & Team CODES
│   ├── 📁 Skills/                     <-- 368 Folders with manuals & documentation
│   ├── 📁 MCP/                        <-- Manuals (ai-memory, rea, agent-desktop, magicpath)
│   ├── 📁 Frameworks/                 <-- Agent libraries (alethe, claude-cookbooks, etc.)
│   ├── 📁 Apps/                       <-- Local applications with GPU/CPU acceleration
│   ├── 📁 Opcionais/                  <-- Supporting tools (painel-agents telemetry)
│   └── 📄 _Hub de Skills & MCPs.md    <-- Obsidian interactive hub & dashboard
│
├── 📄 setup.bat                       <-- 1-Click Windows installer (CMD)
├── 📄 setup.ps1                       <-- 1-Click Windows installer (PowerShell)
├── 📄 setup.sh                        <-- 1-Click Linux & macOS installer
└── 📄 sync_obsidian.mjs               <-- Continuous vault synchronization script
```

---

## Quick Cross-Platform Installation

Clone this repository on any operating system (**Windows, Linux, or macOS**) and execute a single command to have your environment fully provisioned.

### On Windows:

Open Command Prompt (or PowerShell) and run:
```cmd
git clone https://github.com/lk-feitosa/minerva-workspace.git S:\DEV\agents
cd S:\DEV\agents
setup.bat
```
*(Or in PowerShell: `.\setup.ps1`)*

The script automatically provisions NTFS Junctions linking the repository to agent default search paths (`~/.agents`, `~/.codex/skills`, and `%LOCALAPPDATA%\hermes\skins`).

---

### On Linux or macOS:

Open your terminal and run:
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/agents
cd ~/DEV/agents
chmod +x setup.sh
./setup.sh
```

The script automatically creates standard UNIX symbolic links (`~/.agents`, `~/.codex/skills`, `~/.hermes/skins`).

---

## How to Open the Vault in Obsidian

1. Open the **Obsidian** desktop application.
2. Click **"Open folder as vault"**.
3. Select the directory:
   * **On Windows:** `S:\DEV\agents\vault\Agentes` (or `C:\Users\YOUR_USER\.agents\vault\Agentes`)
   * **On Linux/macOS:** `~/DEV/agents/vault/Agentes` (or `~/.agents/vault/Agentes`)
4. Done! The vault opens with:
   * **Excalidraw** pre-configured in Dark Mode.
   * Community plugins activated.
   * Interactive dashboard in `_Hub de Skills & MCPs.md`.
   * Master governance guide in `Workspace/Orquestração de Projetos - Minerva & Conselho.md`.

---

## Synchronization and Maintenance

Whenever you add or update skills, MCP servers, or tools, run the synchronization script:

```bash
node sync_obsidian.mjs
```

It rebuilds the hierarchical index, updates Portuguese documentation summaries, and refreshes metrics on the Obsidian dashboard.

---

## Orchestration Architecture: Minerva & Team CODES

Explore the full architectural specification inside Obsidian:  
👉 **`Workspace/Orquestração de Projetos - Minerva & Conselho.md`**

* **Minerva:** Master Orchestrator supervising parallel terminals autonomously on Maestri Canvas (Zero Human-in-the-Loop).
* **The 5 Council Advisors:** The Contrarian, First-Principles Thinker, Expansionist, Outsider, and Executor.
* **Team CODES:** A 12-role engineering pipeline (Spec, Plan, Dev, UI, Backend, Tests, Review, Ship, etc.).
* **Git Branch Topology:** Semantic demand-based branches (`feature/<demand>`, `fix/<bug>`), avoiding proliferation of generic or redundant branches.

---

## 🧩 Recommended Satellite Addons for Maestri Canvas

To enhance spatial development with multiple concurrent agents and terminals on [Maestri Spatial Development Workspace](https://maestri.app), the ecosystem features two standalone local companion applications with **unified tab navigation** (allowing full control from a single integrated window):

1. **📊 [Agent Dashboard (`painel-agents`)](https://github.com/lk-feitosa/painel-agents):**
   * **Local Port:** `http://localhost:3333/`
   * **Features:**
     * **Real-Time Telemetry & 3D Quotas:** Weekly and 5h capacity meters (Gemini, Claude, OpenAI) with automated role-to-model inference (Back-End $\rightarrow$ Codex GPT-5.6, Front-End $\rightarrow$ Claude Sonnet 4.6).
     * **Live Activity Logs Feed (`📜 Logs`):** Chronological timeline tracking demand intake, Kanban board syncs, and terminal task dispatches.
     * **Live Architecture Graph (`🗺️ Architecture`):** Interactive real-time code dependency graph (60 FPS SVG with draggable nodes, pan/zoom, glowing markers for files touched in the last 15 min), and a mission dispatch drawer (refactor, test, audit).
     * **Integrated Tab Navigation:** Dedicated `[ 🦉 Kanban (:3334) ]` tab to switch into project tasks without opening extra browser windows.
   * **Maestri Portal:** `maestri portal create http://localhost:3333 "Painel de Agentes"`

2. **📋 [Kanban for Maestri (`kanban-agents`)](https://github.com/lk-feitosa/kanban-agents):**
   * **Local Port:** `http://localhost:3334/`
   * **Features:**
     * **Lightweight Agile Board:** (< 20 MB RAM, zero Docker, zero login), directly synced with `.kanban/board.json`.
     * **Unified Header Tabs:** Seamless switching between `[ 📌 Active Board ]`, `[ 📦 Archived Sprints ]`, and embedded `[ 📊 Agent Dashboard (:3333) ]`.
     * **Sprint Archiving:** Fast `[ 🏁 Finalize Sprint ]` action that moves completed tasks into permanent history and clears the column for the next iteration.
     * **Scroll Preservation & Anti-Collision:** No screen jumping on refresh, and automatic port fallback if 3334 is busy.
   * **Maestri Portal:** `maestri portal create http://localhost:3334 "Kanban"`

---

## Autonomous Setup via AI Agent (Ready-to-Use Prompt)

If you use an AI coding assistant in your terminal or IDE (**Antigravity**, **Claude Code**, **Codex**, **Cursor**, or **Aider**) and prefer having your agent configure your operating system automatically to adopt this unified global architecture, simply clone this repository and paste the prompt below into your assistant:

```text
You are my AI assistant configuring this computer.
I just cloned the Minerva & Agents ecosystem (minerva-workspace) onto this machine.
Please configure my local environment to adopt this unified global architecture:

1. Identify my Operating System (Windows / Linux / macOS) and the directory path where this repository was cloned.
2. Instead of using isolated or fragmented default paths, configure global pointings by creating the necessary links:
   - On Windows: Create NTFS Junctions linking:
     * %USERPROFILE%\.agents -> [this_repository_path]
     * %USERPROFILE%\.codex\skills -> [this_repository_path]\skills
     * %LOCALAPPDATA%\hermes\skins -> [this_repository_path]\hermes\skins
   - On Linux or macOS: Create symbolic links (ln -s):
     * ~/.agents -> [this_repository_path]
     * ~/.codex/skills -> [this_repository_path]/skills
     * ~/.hermes/skins -> [this_repository_path]/hermes/skins
3. Validate that Node.js, Python 3, and Git are available in the system PATH.
4. Confirm that the Obsidian vault is located at 'vault/Agentes' within this repository and explain how to open it.
5. Present a clean summary report displaying the status of each configured item.
```

---

## Credits, Attribution & Licenses

This project acts as an integration and orchestration ecosystem. All intellectual property rights, trademarks, and third-party code belong strictly to their original creators (Google, Anthropic, Vercel Labs, Kanbn, Fabio Akita, Addy Osmani, Matt Pocock, Affaan M, Composio, etc.).

For the complete attribution table and links to all official repositories, see:  
👉 **[CREDITS.md](CREDITS.md)** *(Versão em português: [CREDITS.pt-br.md](CREDITS.pt-br.md))*

