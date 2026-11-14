---
tags:
  - ai/setup
  - guia-de-instalacao
  - replicacao
  - automacao
updated_at: "2026-11-14T12:00:00Z"
---

# Guia Passo a Passo: Como Replicar Este Ecossistema em Outro PC

> [!NOTE] **Objetivo Deste Guia**  
> Roteiro 100% portável (Windows, Linux e macOS) para subir toda a infraestrutura Minerva em **`~/.minerva`** sem caminhos fixos e sem duplicação.

---

## 1. Pré-Requisitos no Novo Computador

1. **Git:** `winget install Git.Git` *(ou gerenciador do seu SO)*
2. **Node.js (LTS v20+):** `winget install OpenJS.NodeJS.LTS` *(necessário para `npx skills` e `context-mode`)*
3. **Python 3.11+:** `winget install Python.Python.3.12` *(necessário para `painel-agents` e `kanban-agents`)*
4. **Obsidian (opcional):** `winget install Obsidian.Obsidian`
5. **AI Memory (opcional):** [github.com/akitaonrails/ai-memory/releases](https://github.com/akitaonrails/ai-memory/releases)
6. **RTK & Graphify (opcionais de economia):**
   * `rtk`: no Windows baixe `rtk.exe` de [`rtk-ai/rtk/releases`](https://github.com/rtk-ai/rtk/releases) para `~/.local/bin` *(ou `cargo install rtk` se tiver Rust)* — o `/minerva` ativa só dentro dos projetos.
   * `graphify`: `uv tool install graphifyy` (`Graphify-Labs/graphify`).

---

## 2. Instalação Completa (`~/.minerva` + Todas as Skills + Migração)

### No Windows (PowerShell):
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git $HOME\.minerva
cd $HOME\.minerva
.\setup.ps1
```
*(Ou `setup.bat` no CMD).*

### No Linux ou macOS:
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/.minerva
cd ~/.minerva
chmod +x setup.sh && ./setup.sh
```

### O que o `setup` faz automaticamente:
1. **Vasculha & migra skills antigas:** procura skills já instaladas em `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills` e `~/.agents/skills`, movendo para `~/.minerva/skills` sem duplicar.
2. **Centraliza em `~/.minerva`:** mantém `~/.minerva` como raiz canônica única e conecta todos os CLIs para `~/.minerva/skills/`.
3. **Instala todo o catálogo do `skills-manifest.json`** via `npx -y skills add`.
4. **Verifica/clona os apps companheiros:** [`painel-agents`](https://github.com/lk-feitosa/painel-agents) e [`kanban-agents`](https://github.com/lk-feitosa/kanban-agents).

*(Entrada alternativa via CLI: `npx skills add lk-feitosa/minerva-workspace` — depois execute `/minerva` no terminal para concluir a configuração global).*

---

## 3. Usando no Dia a Dia: `/minerva` em Qualquer Projeto

1. Entre na pasta de qualquer projeto: `cd <SEU_PROJETO>`
2. Abra **Claude Code**, **Codex**, **Gemini CLI**, **Antigravity** ou **Maestri** e digite **`/minerva`**.
3. Ele executa o bootstrap completo do workspace:
   * Blinda `.gitignore` (`.maestri/`, `.kanban/`, `.agents/cache/`, `.ai-memory/cache/`, `graphify-out/`, `*.session`, `*.tmp`).
   * Cria `.agents/` (`AGENTS.md`, `MINERVA.md`, `roles/`) + `docs/` (`spec.md`, `architecture.md`, `adr/`).
   * Inicializa `ai-memory` + `.kanban/board.json`, sobe **Painel (`:3333`)** + **Kanban (`:3334`)** e abre os Portais no Maestri.
   * Ativa economia local com **`context-mode`** (`.mcp.json`) e hook local do **`rtk`** em `.claude/settings.local.json`.

---

## 4. Abrindo o Cofre no Obsidian

1. Abra o **Obsidian** -> **"Open folder as vault"**.
2. Selecione **`~/.minerva/vault`** (ou `<PASTA_DO_REPO>/vault`).
