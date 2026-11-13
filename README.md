<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="180" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva Workspace — Orquestrador & Base Global de Agentes

**Skill publicável no `skills.sh` (`/minerva`) + Base Global portátil de Skills, Economia de Contexto por Workspace, Painel + Kanban locais e Cofre PT-BR no Obsidian.**

🌐 **[Português](README.md)** | **[English](README.en.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-instalação-rápida)
[![skills.sh](https://img.shields.io/badge/skills.sh-minerva--workspace-blue.svg?style=flat-square)](skills/minerva/)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20PT--BR-purple.svg?style=flat-square)](vault/Agentes/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## Como Funciona (Híbrido: Base Global + Ativação `/minerva` por Projeto)

1. **Skills leves e globais (em um só lugar):** `setup.ps1` / `setup.sh` liga `~/.agents`, `~/.codex/skills`, `~/.claude/skills` e `~/.gemini/config/skills` para esta base única e baixa o perfil curado (`core` por padrão, ou `--full`) direto do **`skills.sh`** (`llm-council`, `grill-me`, `ponytail`, `find-skills`, UI/UX, TDD, Playwright, Agent Desktop, REA).
2. **Economia de contexto e serviços SÓ dentro do projeto (`/minerva`):** ao abrir qualquer projeto no terminal e rodar **`/minerva`**, a skill configura apenas o workspace atual (sem sujar outras sessões da máquina):
   * **Painel (`:3333`) + Kanban (`:3334`):** sobe [painel-agents](https://github.com/lk-feitosa/painel-agents) e [kanban-agents](https://github.com/lk-feitosa/kanban-agents) apontando para `.kanban/board.json` do projeto.
   * **Context Mode (`npx -y context-mode`):** MCP local no `.mcp.json` para rodar leituras/logs pesados fora da janela de contexto.
   * **Ponytail + RTK + Graphify:** edição mínima (`ponytail`), hook local opcional do `rtk` em `.claude/settings.local.json` e grafo AST opcional (`graphify-out/`).

---

## Estrutura do Repositório

```text
minerva-workspace/
├── 📁 skills/
│   ├── 📁 minerva/                    <-- Orquestrador central (/minerva) & protocolos
│   ├── 📁 painel-agents/              <-- Skill do Painel de Agentes (:3333)
│   └── 📁 kanban-agents/              <-- Skill do Kanban Minimalista (:3334)
├── 📁 templates/project/              <-- Modelos portáteis (.mcp.json, AGENTS.md, hooks locais)
├── 📄 skills-manifest.json            <-- Catálogo curado skills.sh (perfis core e full)
├── 📄 mcp_config.json                 <-- Servidores MCP base (magicpath, rea, agent-desktop, ai-memory)
├── 📁 toolkits/                       <-- Prompts e scripts utilitários
├── 📁 vault/Agentes/                  <-- Cofre enxuto 100% em PT-BR do Obsidian
├── 📄 setup.bat                       <-- Instalador Windows (CMD)
├── 📄 setup.ps1                       <-- Instalador Windows (PowerShell: -Profile core|full)
└── 📄 setup.sh                        <-- Instalador Linux / macOS (--core | --full)
```

---

## Instalação Rápida

### Opção 1 — Direto via `skills.sh` (para quem quer começar em 1 comando)
```bash
npx skills add lk-feitosa/minerva-workspace
```
Depois, abra seu agente (**Claude Code**, **Codex**, **Gemini CLI** ou **Antigravity**) em qualquer pasta e digite **`/minerva`** — a skill detecta se a base global já existe e ajuda a finalizar o setup ou inicializar o projeto atual.

### Opção 2 — Clone + Setup Global Completo (`setup.ps1` / `setup.sh`)

#### No Windows (PowerShell):
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
.\setup.ps1
```
*(Use `.\setup.ps1 -Profile full` para instalar também o catálogo estendido da comunidade).*

#### No Linux ou macOS:
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
chmod +x setup.sh && ./setup.sh
```
*(Use `./setup.sh --full` para o catálogo estendido).*

---

## Como Abrir o Cofre no Obsidian

1. Abra o **Obsidian** e clique em **"Open folder as vault"**.
2. Selecione `<PASTA_DO_REPO>/vault/Agentes` (ou `~/.agents/vault/Agentes`).
3. Comece pelo dashboard **`_Hub de Skills & MCPs.md`** ou pelo protocolo em **`Workspace/Orquestração de Projetos - Minerva & Conselho.md`**.

---

## Projetos Companheiros Oficiais (`lk-feitosa`)

1. **[painel-agents](https://github.com/lk-feitosa/painel-agents)** (`http://127.0.0.1:3333`) — Telemetria em tempo real, cotas 3D, mapa de arquitetura e sincronização com `.kanban/board.json`.
2. **[kanban-agents](https://github.com/lk-feitosa/kanban-agents)** (`http://127.0.0.1:3334`) — Quadro Kanban leve (< 20 MB RAM, zero Docker, zero login) gravado na raiz de cada projeto em `.kanban/board.json`.

---

## Créditos, Atribuições & Licenças

Este projeto é um ecossistema integrador. Todos os direitos de código e skills de terceiros pertencem aos seus respectivos autores originais.  
Consulte: 👉 **[CREDITS.pt-br.md](CREDITS.pt-br.md)** *(English: [CREDITS.md](CREDITS.md))*
