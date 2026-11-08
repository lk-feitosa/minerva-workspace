---
tags:
  - ai/mcp
  - mcp-server
name: "agent-desktop"
updated_at: "2026-11-08T08:03:33.733Z"
---

# Servidor MCP: Agent Desktop (Computer Use)

> [!INFO] **Visão Geral**
> **Identificador:** `agent-desktop`  
> **Origem / Repositório:** [https://github.com/vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop)  
> **Tipo de Conexão:** CLI Local (Stdio via binário/npx)

### Descrição
Automação visual e de janelas do sistema operacional Windows (cliques, digitação, captura de tela, leitura de UI).

---

### Como Usar
Peça no chat: "abra a janela X e clique no botão Y usando o agent-desktop"

---

### Configuração
```json
{
  "agent-desktop": {
    "command": "npx",
    "args": [
      "-y",
      "agent-desktop@latest",
      "mcp"
    ]
  }
}
```
