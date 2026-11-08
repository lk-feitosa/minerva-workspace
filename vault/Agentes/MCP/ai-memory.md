---
tags:
  - ai/mcp
  - mcp-server
name: "ai-memory"
updated_at: "2026-11-08T08:03:33.733Z"
---

# Servidor MCP: AI Memory (Akita on Rails)

> [!INFO] **Visão Geral**
> **Identificador:** `ai-memory`  
> **Origem / Repositório:** [https://github.com/akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)  
> **Tipo de Conexão:** CLI Local (Stdio via binário/npx)

### Descrição
Memória persistente de longo prazo em Rust com isolamento total por projeto/repositório Git. Sintetiza regras, padrões aprendidos e decisões de engenharia automaticamente.

---

### Como Usar
Ativo via Stdio. Mantém o contexto de cada projeto (ex: `Snorlax`, `kota`) estritamente separado através da pasta local de execução e do git root.

---

### Configuração
```json
{
  "ai-memory": {
    "command": "ai-memory",
    "args": [
      "serve",
      "--transport",
      "stdio"
    ]
  }
}
```
