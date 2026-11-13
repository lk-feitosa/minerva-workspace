---
tags:
  - ai/skill
  - context-economy
  - mcp
  - skills-sh
name: "context-mode"
source: "mksglu/context-mode"
updated_at: "2026-11-13T00:30:00Z"
---

# 🗜️ context-mode

> [!INFO] **Fonte Oficial (`skills.sh`)**
> * **Repositório:** [github.com/mksglu/context-mode](https://github.com/mksglu/context-mode)
> * **Skills CLI (`skills.sh`):** `npx skills add mksglu/context-mode -s ctx-stats ctx-doctor -g -y`
> * **MCP de Workspace:** `npx -y context-mode`

## Resumo
Servidor MCP + skill com sandbox local (`ctx_execute`, `ctx_search`) e rastreamento SQLite FTS5/BM25 para impedir que saídas gigantes de terminal, logs e leituras múltiplas saturem a janela de contexto dos agentes. Configurado por projeto via `/minerva` no `.mcp.json`.
