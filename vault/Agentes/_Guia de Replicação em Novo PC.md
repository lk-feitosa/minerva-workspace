---
tags:
  - ai/setup
  - guia-de-instalacao
  - replicacao
  - automacao
updated_at: "2026-11-13T00:30:00Z"
---

# Guia Passo a Passo: Como Replicar Este Ecossistema em Outro PC

> [!NOTE] **Objetivo Deste Guia**  
> Roteiro 100% portável (Windows, Linux e macOS) para subir o ecossistema Minerva em qualquer máquina nova sem caminhos fixos.

---

## 1. Pré-Requisitos no Novo Computador

1. **Git:** `winget install Git.Git` *(ou gerenciador do seu SO)*
2. **Node.js (LTS v20+):** `winget install OpenJS.NodeJS.LTS` *(necessário para `npx skills` e `context-mode`)*
3. **Python 3.11+:** `winget install Python.Python.3.12` *(necessário para `painel-agents` e `kanban-agents`)*
4. **Obsidian (opcional):** `winget install Obsidian.Obsidian`
5. **Rust / `ai-memory` (opcional):** [github.com/akitaonrails/ai-memory/releases](https://github.com/akitaonrails/ai-memory/releases)
6. **RTK (opcional):** `cargo install rtk` (`rtk-ai/rtk`)

---

## 2. Opção A — Instalação Rápida via `skills.sh`

```bash
npx skills add lk-feitosa/minerva-workspace
```
Depois, abra seu agente de IA no terminal e execute **`/minerva`**. Se a base global ainda não existir, a própria skill orienta/executa o clone e o setup completo.

---

## 3. Opção B — Clone + Setup Global Completo (1 Comando)

### No Windows (PowerShell):
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
.\setup.ps1
```
*(Ou `.\setup.bat` no CMD. Passe `-Profile full` para instalar também o catálogo estendido do `skills-manifest.json`).*

### No Linux ou macOS:
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
chmod +x setup.sh && ./setup.sh
```
*(Passe `--full` para o catálogo estendido).*

### O que o `setup` faz automaticamente:
1. Cria as junctions/symlinks globais ligando `~/.agents`, `~/.codex/skills`, `~/.claude/skills` e `~/.gemini/config/skills` ao repositório clonado.
2. Instala via `npx -y skills add` as skills curadas do perfil `core` (ou `full`) em `skills-manifest.json`.
3. Verifica ou clona os repositórios companheiros **[painel-agents](https://github.com/lk-feitosa/painel-agents)** e **[kanban-agents](https://github.com/lk-feitosa/kanban-agents)**.

---

## 4. Usando no Dia a Dia: `/minerva` em Qualquer Projeto

1. Entre na pasta de qualquer projeto: `cd <SEU_PROJETO>`
2. Abra **Claude Code**, **Codex**, **Gemini CLI**, **Antigravity** ou **Maestri** e digite **`/minerva`**.
3. O `/minerva` configura **apenas o workspace atual** (sem alterar outros terminais):
   * Sobe **Painel (`:3333`)** e **Kanban (`:3334`)** apontando para `.kanban/board.json` do projeto.
   * Injeta **`context-mode`** (`npx -y context-mode`) e `ai-memory` no `.mcp.json` do projeto.
   * Ativa o hook local do **`rtk`** em `.claude/settings.local.json` (se `rtk` existir no `PATH`).
   * Oferece gerar grafo **`graphify`** (`graphify-out/`) para repositórios maiores.

---

## 5. Abrindo o Cofre no Obsidian

1. Abra o **Obsidian** -> **"Open folder as vault"**.
2. Selecione `<PASTA_DO_REPO>/vault/Agentes` (ou `~/.agents/vault/Agentes`).
