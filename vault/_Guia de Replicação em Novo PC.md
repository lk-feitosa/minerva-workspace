---
tags:
  - ai/setup
  - guia
  - replicacao
  - cross-platform
updated_at: "2026-11-17T23:52:00Z"
---

# Guia de Replicação em Novo Computador (`~/.minerva`)

Este guia mostra como instalar o ecossistema **Minerva** em qualquer computador (**Windows, Linux ou macOS**) com **uma única raiz global (`~/.minerva`)**, migrando skills e MCPs antigos sem duplicar, e como iniciar cada projeto no dia a dia.

---

## 1. Pré-requisitos Rápidos

* **Git** (`git --version`)
* **Node.js 20+** (`node -v` — fornece `npx` para o `skills.sh` e para o MCP `context-mode`)
* **Python 3.10+** (`python --version` — roda `minerva_bootstrap.py`, `minerva_quotas.py`, `painel-agents` `:3333` e `kanban-agents` `:3334` sem dependências externas)
* *(Opcional)* **Obsidian** (para abrir `~/.minerva/vault`), **`rtk`** (economia de tokens em Bash) e **`graphify`** (`uv tool install graphifyy`).

---

## 2. Comandos da Suite Minerva (`skills.sh`)

Ao instalar `lk-feitosa/minerva-workspace`, você tem **4 comandos (`/` commands)** separados por função:

| Comando | Onde Usar | O que faz |
| :--- | :--- | :--- |
| **`/minerva-setup`** | **1x no PC** | Instala/atualiza `~/.minerva`, migra skills e MCPs globais antigos sem duplicar, cria junctions e baixa todas as skills + `painel-agents` e `kanban-agents`. |
| **`/minerva`** | **No Workspace do Projeto** | *(Após selecionar a Persona Minerva)* Roda `minerva_bootstrap.py` e assume a orquestração do projeto com `ponytail`, `context-mode`, `rtk`, Conselho/Grill-Me e Team CODES. |
| **`/painel-agents`** | Projeto / Global | Abre, consulta cotas ou faz auto-heal do Painel de Agentes (`:3333`). |
| **`/kanban-agents`** | Projeto | Abre ou opera o Kanban Minimalista (`:3334` / `.kanban/board.json`). |

---

## 3. Passo 1 — Configurar o PC Globalmente (`1x por Máquina`)

### Opção A — Via `skills.sh` + `/minerva-setup`:
```bash
npx skills add lk-feitosa/minerva-workspace -g -y
```
Depois abra seu agente no terminal e digite **`/minerva-setup`**.

### Opção B — Clone Direto + Instalador Nativo:

**No Windows (PowerShell):**
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git $HOME\.minerva
cd $HOME\.minerva
.\setup.ps1
```

**No Linux ou macOS:**
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/.minerva
cd ~/.minerva
chmod +x setup.sh && ./setup.sh
```

### O que o `/minerva-setup` (`setup.ps1` / `setup.sh`) faz sozinho:
1. **Vasculha & migra skills antigas sem duplicar:** move skills de `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills` e `~/.agents/skills` para `~/.minerva/skills` e cria junctions/symlinks em todos os CLIs.
2. **Sincroniza MCPs Globais sem duplicar:** mescla `ai-memory`, `rea` e `agent-desktop` de `~/.minerva/mcp_config.json` em `~/.gemini/mcp_config.json` e `~/.claude.json` preservando qualquer outro MCP já existente na máquina.
3. **Instala todo o catálogo (`skills-manifest.json`):** baixa os 19 pacotes curados via `npx -y skills add` e garante [`painel-agents`](https://github.com/lk-feitosa/painel-agents) + [`kanban-agents`](https://github.com/lk-feitosa/kanban-agents) em `~/.minerva/tools/`.

---

## 4. Passo 2 — Usando em um Projeto Novo ou Existente (`/minerva`)

1. Entre na pasta do projeto (`cd <SEU_PROJETO>`) ou abra o projeto no **[Maestri Canvas](https://www.themaestri.app/pt-br)**.
2. **Primeiro configure/selecione a Persona Minerva:** no terminal principal, selecione a responsabilidade **"Minerva - Orquestrador Central"**.
3. **Depois digite `/minerva`:** ele executará `python ~/.minerva/toolkits/minerva_bootstrap.py .` configurando:
   * `.gitignore` blindado + `.agents/` (`AGENTS.md`, `MINERVA.md`, `roles/`, `skills.json` via `agent_sort.py` + `session-mode.json`) + `docs/` (`spec.md`, `architecture.md`, `adr/`).
   * `.mcp.json` do workspace (`context-mode` + `ai-memory`), hook local do `rtk` e disciplina `ponytail`.
   * `.kanban/board.json` + **Painel (`:3333`)** + **Kanban (`:3334`)** + Portais automáticos no Maestri.
   * **Consulta Direta dos CLIs (`minerva_quotas.py`):** lista todos os modelos e cotas direto de `agy`, `codex` e `claude` para sugerir o **Team CODES Anti-Monocultura** (sem abrir um time todo da mesma IA).
   * **Busca e Injeção de Skills (`agent_sort.py --match` + `find-skills`):** descobre qual skill usar para cada demanda e injeta o caminho explícito no terminal.
   * **Escolha do Modo de Sessões (`ephemeral` vs. `persistent`):** permite usar sessões temporárias isoladas em `.agents/cache/` (para não poluir o `/resume` do seu CLI global) ou sessões salvas no histórico, além de **Failover Automático de IA no Terminal** (`--replace`).

---

## 5. Mapa Completo de Endereços (Onde Tudo Fica Salvo)

| Item | Endereço / Caminho Salvo |
| :--- | :--- |
| **Raiz Global da Minerva** | `~/.minerva` (`%USERPROFILE%\.minerva`) |
| **Cofre do Obsidian (Abrir como Vault)** | **`~/.minerva/vault`** (`%USERPROFILE%\.minerva\vault`) |
| **Skills Centralizadas** | `~/.minerva/skills` (`%USERPROFILE%\.minerva\skills`) |
| **MCPs Globais** | `~/.minerva/mcp_config.json` (mesclado em `~/.gemini/mcp_config.json` e `~/.claude.json`) |
| **Painel de Agentes (Web / Portal)** | `http://localhost:3333` (`~/.minerva/tools/painel-agents`) |
| **Kanban Minimalista (Web / Portal)** | `http://localhost:3334` (`~/.minerva/tools/kanban-agents` + `<PROJETO>/.kanban/board.json`) |
| **Governança, Skills & Sessões do Projeto** | `<PROJETO>/.agents/` (`MINERVA.md`, `AGENTS.md`, `roles/`, `skills.json`, `session-mode.json`, `cache/`) |
| **Documentação Viva do Projeto** | `<PROJETO>/docs/` (`spec.md`, `architecture.md`, `adr/`) |
| **MCPs do Workspace do Projeto** | `<PROJETO>/.mcp.json` (`context-mode` + `ai-memory`) |
