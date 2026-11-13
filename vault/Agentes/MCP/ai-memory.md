---
tags:
  - ai/mcp
  - mcp-server
  - memory
  - long-term-memory
  - rust
name: "ai-memory"
github: "https://github.com/akitaonrails/ai-memory"
updated_at: "2026-11-12T18:50:00.000Z"
---

# 🧠 Servidor MCP: AI Memory (Memória Persistente Compartilhada)

> [!INFO] **Visão Geral Oficial**
> **Repositório Oficial:** [https://github.com/akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)  
> **Autor / Mantenedor:** Fabio Akita ([@akitaonrails](https://github.com/akitaonrails))  
> **Website Oficial:** [https://aimemory.sh](https://aimemory.sh)  
> **Identificador MCP:** `ai-memory`  
> **Tipo de Conexão:** Binário nativo em Rust via Stdio (`ai-memory` no `PATH`)  
> **Diretório de Dados Padrão:** `~/.agents/ai-memory` (ou `--data-dir <PASTA_MEMORIA>`)

---

## 💡 O que é o ai-memory? (Resumo Oficial)

O **ai-memory** é um sistema de **memória de longo prazo persistente** para agentes de desenvolvimento de IA.

Seu principal propósito é resolver o maior gargalo do trabalho com múltiplos agentes: **a perda de contexto ao trocar de ferramenta ou encerrar a sessão**. Com o ai-memory, você pode fechar o Claude Code no meio de uma tarefa, abrir o OpenAI Codex no mesmo diretório e continuar trabalhando sem precisar reexplicar a arquitetura, abordagens descartadas ou decisões anteriores.

### Principais Diferenciais Arquiteturais:
* **Handoffs Tipados entre 20+ IAs:** Conecta Claude Code, Codex, Cursor, Gemini CLI, Antigravity, OpenCode e outros em uma única memória compartilhada. Handoffs possuem donos explícitos e são reivindicados exatamente uma vez.
* **Armazenamento em Markdown Aberto (Git-Backed):** A fonte da verdade é uma wiki em arquivos `.md` comuns versionados no Git. Pode ser lida diretamente pelo Obsidian, pesquisada via `grep` ou editada à mão. Não há dependência de vector databases proprietários ou bancos bloqueados.
* **Zero Chamadas de LLM por Padrão:** Captura de contexto, busca textual e handoffs funcionam com zero chamadas de API de IA e sem consumir tokens de LLM.
* **Envelhecimento & Decaimento Inteligente:** Memórias pouco acessadas decaem e são compactadas com o tempo, enquanto memórias frequentemente consultadas têm sua retenção renovada automaticamente.

---

## 🛠️ Como Funciona e Como Usar no Projeto

### 1. Iniciar o Servidor Localmente
```bash
ai-memory serve --transport stdio --data-dir "~/.agents/ai-memory"
```

### 2. Comandos Principais do CLI
```bash
# Iniciar um agente com contexto herdado e memória atrelada:
ai-memory run codex
ai-memory run claude

# Consultar memórias ativas do projeto:
ai-memory search "regras fiscais do MEI"

# Criar um handoff explícito para o próximo agente:
ai-memory handoff create --to "Front-End" --summary "API de certidões implementada; falta criar o card visual no dashboard"
```

---

## 🔌 Configuração Oficial no MCP (Model Context Protocol)

Adicione à seção `mcpServers` do seu harness (`~/.claude.json`, Codex, etc.):

```json
{
  "mcpServers": {
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

---

## 📖 README Oficial do Repositório (ai-memory Upstream)

<details>
<summary><strong>📄 Clique aqui para expandir o README oficial original (em inglês)</strong></summary>

```markdown
# ai-memory

Long-term memory for AI coding agents. Quit Claude Code mid-task, start OpenAI Codex in the same directory, continue without re-explaining the architecture, the failed approaches, or the open questions.

Website: https://aimemory.sh

- Follows you across agents: Claude Code, Codex, Cursor, Gemini, OpenCode and 20+ harnesses.
- Pure markdown backing: Git-backed wiki of plain .md files.
- Zero LLM calls for capture and search by default.
- Access-weighted retention and lossless compaction.

## Getting Started
```bash
cargo install ai-memory
ai-memory init
ai-memory run claude
```

## License
MIT. Copyright (c) Fabio Akita.
```

</details>
