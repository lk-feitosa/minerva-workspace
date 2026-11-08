---
tags:
  - ai/mcp
  - mcp-server
name: "kan"
updated_at: "2026-11-08T08:03:33.734Z"
---

# Servidor MCP: Kan Kanban (@kan.bn/mcp)

> [!INFO] **Visão Geral**
> **Identificador:** `kan`  
> **Origem / Repositório:** [https://github.com/kanbn/kan](https://github.com/kanbn/kan)  
> **Tipo de Conexão:** CLI Local (Stdio via binário/npx)

### Descrição
Servidor MCP oficial do Kan para manipulação autônoma de workspaces, quadros, listas, cartões e checklists.

---

### Como Usar
Permite que Minerva e subagentes criem e movam tarefas no Kanban em tempo real enquanto o usuário visualiza no Maestri Canvas.

---

### Configuração
```json
{
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
```
