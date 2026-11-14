---
tags:
  - ai/mcp
  - configuration
updated_at: "2026-11-13T00:30:00Z"
---

# Servidores MCP Base & Workspace

Arquivo Base Global: `~/.minerva/mcp_config.json` (no repositório clonado: `<REPO_DIR>/mcp_config.json`)  
Template por Projeto (ativado pelo `/minerva`): `<PROJECT_DIR>/.mcp.json` (com `context-mode` + `ai-memory`)

---

## Servidores Base
* [[rea|🔌 rea]]
* [[agent-desktop|🔌 agent-desktop]]
* [[ai-memory|🔌 ai-memory]]
* [[context-mode|🔌 context-mode]] *(escopado por projeto via `/minerva`)*

---

### Configuração Base (`mcp_config.json`):
```json
{
  "mcpServers": {
    "rea": {
      "command": "npx",
      "args": [
        "-y",
        "rea-agents@latest",
        "mcp"
      ]
    },
    "agent-desktop": {
      "command": "npx",
      "args": [
        "-y",
        "agent-desktop@latest",
        "mcp"
      ]
    },
    "ai-memory": {
      "command": "ai-memory",
      "args": [
        "serve",
        "--transport",
        "stdio"
      ]
    }
  }
}
```
