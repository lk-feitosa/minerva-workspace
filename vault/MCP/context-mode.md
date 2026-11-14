---
tags:
  - ai/mcp
  - economia-contexto
  - sandbox
updated_at: "2026-11-14T14:38:00Z"
---

# Context Mode (MCP de Economia de Contexto)

> [!NOTE] **Escopo por Workspace**  
> Configurado automaticamente em `<PROJECT_DIR>/.mcp.json` quando você executa `/minerva` (não polui sessões fora de projetos).

## Para que serve

* Executa comandos, buscas extensas e leitura de saídas grandes em sandbox local (`ctx_execute`, `ctx_execute_file`, `ctx_search`), indexando resultados em **SQLite FTS5** para economizar até ~98% da janela de contexto do agente.
* Repositório oficial: [`mksglu/context-mode`](https://github.com/mksglu/context-mode)
* Skills auxiliares instaladas em `~/.minerva/skills/`: `ctx-stats`, `ctx-doctor`.

## Configuração no Projeto (`.mcp.json`)

```json
{
  "mcpServers": {
    "context-mode": {
      "command": "npx",
      "args": ["-y", "context-mode"]
    }
  }
}
```
