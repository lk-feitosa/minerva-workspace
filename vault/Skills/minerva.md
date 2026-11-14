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
Skill raiz de orquestração e bootstrap por workspace (`/minerva`). Verifica a raiz global (`~/.minerva`), blinda `.gitignore`, estrutura `.agents/` (`AGENTS.md`, `MINERVA.md`, `roles/`) + `docs/`, inicializa `ai-memory` + `.kanban/board.json`, sobe **Painel (`:3333`)** + **Kanban (`:3334`)** com Portais no Maestri, ativa economia de contexto local (`context-mode` MCP, hook local do `rtk`, `ponytail`) e coordena Modo Padrão, `[GRILL-ME]` + `[CONSELHO]` e delegação multi-modelo (`alethe` + `maestri`) em branches semânticas.

## Ver também
* [[Skills/painel-agents|📊 painel-agents]] · [[Skills/kanban-agents|📋 kanban-agents]] · [[Workspace/Orquestração de Projetos - Minerva & Conselho|Orquestração Minerva]]
