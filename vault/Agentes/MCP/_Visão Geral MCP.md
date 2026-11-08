---
tags:
  - ai/mcp
  - configuration
updated_at: "2026-11-08T08:03:33.725Z"
---

# Servidores MCP Globais

Arquivo Mestre no S: `S:\DEV\agents\mcp_config.json`  
Espelhado no C: `C:\Users\lukas\.agents\mcp_config.json`

---

## Servidores Configurados
* [[magicpath|🔌 magicpath]]
* [[rea|🔌 rea]]
* [[agent-desktop|🔌 agent-desktop]]
* [[ai-memory|🔌 ai-memory]]
* [[kan|🔌 kan]]

---

### Configuração Completa (JSON):
```json
{
  "mcpServers": {
    "magicpath": {
      "url": "https://api.magicpath.ai/mcp"
    },
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
    },
    "kan": {
      "command": "npx",
      "args": [
        "-y",
        "@kan.bn/mcp"
      ],
      "env": {
        "KAN_BASE_URL": "http://localhost:3000",
        "KAN_API_TOKEN": "YOUR_KAN_API_TOKEN"
      }
    }
  }
}
```
