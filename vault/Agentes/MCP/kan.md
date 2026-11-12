---
tags:
  - ai/mcp
  - mcp-server
  - project-management
  - kanban
  - open-source
name: "kan"
github: "https://github.com/kanbn/kan"
updated_at: "2026-11-12T18:50:00.000Z"
---

# 📋 Servidor MCP: Kan (Kanban Open-Source & MCP Server)

> [!INFO] **Visão Geral Oficial**
> **Repositório Oficial:** [https://github.com/kanbn/kan](https://github.com/kanbn/kan)  
> **Website Oficial:** [https://kan.bn](https://kan.bn)  
> **Documentação da API/MCP:** [https://docs.kan.bn/mcp](https://docs.kan.bn/mcp)  
> **Pacote MCP:** `@kan.bn/mcp`  
> **Licença:** AGPLv3  
> **Identificador MCP:** `kan`

---

## 💡 O que é o Kan? (Resumo Oficial)

O **Kan** é uma alternativa moderna e de código aberto ao Trello para gestão ágil de projetos e tarefas, construído com foco em colaboração e integração profunda com inteligência artificial via **Model Context Protocol (MCP)**.

### Principais Recursos do Kan:
* **Gestão de Quadros e Listas:** Controle total de visibilidade, listas (To-Do, Doing, Done) e cartões.
* **Membros e Workspace:** Colaboração em equipe e atribuição de donos para cada card.
* **Histórico e Atividades:** Auditoria detalhada de todas as alterações feitas nos cartões.
* **Importação Fácil do Trello:** Migração simples de quadros existentes.
* **Suporte Nativo a MCP:** Permite que qualquer agente de IA compatível (Claude Code, Codex, Antigravity, Cursor) crie, consulte, mova e comente em cards usando linguagem natural.

---

## 🛠️ Como Funciona e Como Usar no Projeto

### 1. Execução Rápida do Servidor MCP (Zero Instalação)
O servidor MCP do Kan é distribuído como pacote npx, não exigindo clonar o repositório nem instalação global:

```bash
npx -y @kan.bn/mcp
```

### 2. Variáveis de Ambiente Necessárias
Para conectar o servidor MCP à sua instância (local ou na nuvem em kan.bn):

| Variável | Descrição | Exemplo |
| :--- | :--- | :--- |
| `KAN_BASE_URL` | URL base da sua instalação ou da nuvem | `http://localhost:3000` ou `https://api.kan.bn` |
| `KAN_API_TOKEN` | Token de API gerado em **Settings → API Keys** | `kan_live_abc123...` |

---

## 🔌 Configuração Oficial no MCP (Model Context Protocol)

Adicione ao seu arquivo de configuração MCP (`~/.claude.json`, Codex, etc.):

```json
{
  "mcpServers": {
    "kan": {
      "command": "cmd.exe",
      "args": [
        "/d",
        "/c",
        "npx",
        "-y",
        "@kan.bn/mcp"
      ],
      "env": {
        "KAN_BASE_URL": "http://localhost:3000",
        "KAN_API_TOKEN": "SEU_TOKEN_AQUI"
      }
    }
  }
}
```

---

## 📋 Ferramentas MCP Disponíveis para os Agentes

Quando conectado, o agente de IA ganha as seguintes ferramentas nativas:
* `list_workspaces`, `create_workspace`, `get_workspace`
* `list_boards`, `create_board`, `get_board`, `update_board`
* `create_list`, `update_list`, `delete_list`
* `create_card`, `get_card`, `update_card`, `delete_card` (mover entre colunas)
* `add_card_comment`, `toggle_card_label`, `create_checklist`

---

## 📖 README Oficial do Repositório (Kanbn Upstream)

<details>
<summary><strong>📄 Clique aqui para expandir o README oficial original (em inglês)</strong></summary>

```markdown
# Kan

The open-source project management alternative to Trello.

Website: https://kan.bn
Docs: https://docs.kan.bn

## Features
- Board Visibility & Workspace Members
- Labels, Filters, Comments & Activity Log
- Custom Templates & Trello Imports
- Native MCP Server for AI Agents

## MCP Server
Run it with npx:
```bash
npx -y @kan.bn/mcp
```
Configure with `KAN_BASE_URL` and `KAN_API_TOKEN`.

## License
AGPLv3.
```

</details>
