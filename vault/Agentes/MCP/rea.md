---
tags:
  - ai/mcp
  - mcp-server
name: "rea"
updated_at: "2026-11-08T06:43:45.894Z"
---

# Servidor MCP: Reverse Engineer Anything (REA)

> [!INFO] **Visão Geral**
> **Identificador:** `rea`  
> **Origem / Repositório:** [https://github.com/morluto/rea](https://github.com/morluto/rea)  
> **Tipo de Conexão:** CLI Local (Stdio via binário/npx)

### Descrição
Ferramenta de engenharia reversa para descompilar APKs, binários nativos (PE, ELF, Mach-O), web bundles e tráfego de rede.

---

### Como Usar
Peça no chat: "use o REA para inspecionar este binário/apk"

---

### Configuração
```json
{
  "rea": {
    "command": "npx",
    "args": [
      "-y",
      "rea-agents@latest",
      "mcp"
    ]
  }
}
```
