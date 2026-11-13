<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="180" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva Workspace — Orchestrator & Unified AI Base

**Publishable `skills.sh` skill (`/minerva`) + Portable Global Skills Base, Per-Workspace Context Economy, Local Dashboard + Kanban & Lean PT-BR Obsidian Vault.**

🌐 **[English](README.en.md)** | **[Português](README.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-quick-installation)
[![skills.sh](https://img.shields.io/badge/skills.sh-minerva--workspace-blue.svg?style=flat-square)](skills/minerva/)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20integrated-purple.svg?style=flat-square)](vault/Agentes/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## How It Works (Global Base + Per-Project `/minerva` Activation)

1. **Lightweight global skills (single source of truth):** `setup.ps1` / `setup.sh` links `~/.agents`, `~/.codex/skills`, `~/.claude/skills`, and `~/.gemini/config/skills` to this single folder and installs the curated profile (`core` by default, or `--full`) straight from **`skills.sh`** (`llm-council`, `grill-me`, `ponytail`, `find-skills`, UI/UX, TDD, Playwright, Agent Desktop, REA).
2. **Project-scoped context economy & services (`/minerva`):** open any project terminal and run **`/minerva`** to configure only that workspace without polluting global sessions:
   * **Dashboard (`:3333`) + Kanban (`:3334`):** auto-starts [painel-agents](https://github.com/lk-feitosa/painel-agents) and [kanban-agents](https://github.com/lk-feitosa/kanban-agents) pointed at the project's `.kanban/board.json`.
   * **Context Mode (`npx -y context-mode`):** local `.mcp.json` sandbox so massive logs/reads stay out of your LLM context window.
   * **Ponytail + RTK + Graphify:** minimal-diff discipline (`ponytail`), optional project-local `rtk` hook in `.claude/settings.local.json`, and optional AST code graph (`graphify-out/`).

---

## Repository Structure

```text
minerva-workspace/
├── 📁 skills/
│   ├── 📁 minerva/                    <-- Master orchestrator (/minerva) & protocols
│   ├── 📁 painel-agents/              <-- Agent Dashboard skill (:3333)
│   └── 📁 kanban-agents/              <-- Minimalist Kanban skill (:3334)
├── 📁 templates/project/              <-- Portable workspace templates (.mcp.json, AGENTS.md, local hooks)
├── 📄 skills-manifest.json            <-- Curated skills.sh manifest (core & full profiles)
├── 📄 mcp_config.json                 <-- Base MCP servers (magicpath, rea, agent-desktop, ai-memory)
├── 📁 toolkits/                       <-- Prompt kits & utilities
├── 📁 vault/Agentes/                  <-- Lean Obsidian Knowledge Vault (PT-BR)
├── 📄 setup.bat                       <-- Windows installer (CMD)
├── 📄 setup.ps1                       <-- Windows installer (PowerShell: -Profile core|full)
└── 📄 setup.sh                        <-- Linux / macOS installer (--core | --full)
```

---

## Quick Installation

### Option 1 — Via `skills.sh` (1-Command Entry)
```bash
npx skills add lk-feitosa/minerva-workspace
```
Open your AI CLI (**Claude Code**, **Codex**, **Gemini CLI**, or **Antigravity**) in any folder and run **`/minerva`** — it detects whether the global base is installed yet and either completes bootstrap or initializes the active project.

### Option 2 — Clone + Full Global Setup (`setup.ps1` / `setup.sh`)

#### Windows (PowerShell):
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
.\setup.ps1
```
*(Pass `-Profile full` to install the extended community catalog as well).*

#### Linux or macOS:
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
chmod +x setup.sh && ./setup.sh
```
*(Pass `--full` for the extended catalog).*

---

## Opening the Obsidian Vault

1. Launch **Obsidian** and click **"Open folder as vault"**.
2. Select `<REPO_DIR>/vault/Agentes` (or `~/.agents/vault/Agentes`).
3. Start with **`_Hub de Skills & MCPs.md`** or **`Workspace/Orquestração de Projetos - Minerva & Conselho.md`**.

---

## Official Companion Apps (`lk-feitosa`)

1. **[painel-agents](https://github.com/lk-feitosa/painel-agents)** (`http://127.0.0.1:3333`) — Real-time agent telemetry, 3D quota cards, live architecture graph, and `.kanban/board.json` sync.
2. **[kanban-agents](https://github.com/lk-feitosa/kanban-agents)** (`http://127.0.0.1:3334`) — Zero-Docker, zero-auth minimalist Kanban (< 20 MB RAM) backed by `.kanban/board.json`.

---

## Credits, Attribution & Licenses

This repository is an integration ecosystem. All third-party skills and MCP tools belong strictly to their original authors.  
See: 👉 **[CREDITS.md](CREDITS.md)** *(Versão em português: [CREDITS.pt-br.md](CREDITS.pt-br.md))*
