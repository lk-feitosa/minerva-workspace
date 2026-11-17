---
tags:
  - ai/skill
  - orquestracao
  - minerva
  - workspace
  - skills-sh
name: "minerva"
source: "lk-feitosa/minerva-workspace"
updated_at: "2026-11-13T00:30:00Z"
---

# 🦉 minerva

> [!INFO] **Fonte Oficial**
> * **Repositório:** [github.com/lk-feitosa/minerva-workspace](https://github.com/lk-feitosa/minerva-workspace)
> * **Instalação (`skills.sh`):** `npx skills add lk-feitosa/minerva-workspace -g -y`

## Resumo
Skill de bootstrap e orquestração **por workspace de projeto** (`/minerva` — para configurar o PC globalmente, use [[Skills/minerva-setup|🛠️ minerva-setup (`/minerva-setup`)]]).

**Como usar ao abrir um projeto:**
1. Selecione primeiro a **Persona Minerva (Orquestrador Central)** no terminal principal (especialmente no Maestri).
2. Digite **`/minerva`**.

Ela executa `toolkits/minerva_bootstrap.py` em 1 comando (`.gitignore`, `.agents/`, `docs/`, `.mcp.json` com `context-mode` + `ai-memory`, hook local do `rtk`, `.agents/skills.json` via `agent_sort.py`, `.kanban/board.json`, **Painel `:3333`** + **Kanban `:3334`** e Portais no Maestri), aplica `ponytail` e coordena o **Team CODES** com **Alocação Anti-Monocultura por Cota** e **Failover Automático de IA no Terminal** (se uma IA falhar ao abrir no Maestri, abre outra IA disponível e repassa a demanda sem codar sozinha).

## Ver também
* [[Skills/minerva-setup|🛠️ minerva-setup]] · [[Skills/painel-agents|📊 painel-agents]] · [[Skills/kanban-agents|📋 kanban-agents]] · [[Workspace/Orquestração de Projetos - Minerva & Conselho|Orquestração Minerva]]
