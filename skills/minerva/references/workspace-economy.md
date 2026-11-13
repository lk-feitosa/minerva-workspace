# Economia de Contexto no Workspace (`/minerva`)

Objetivo: reduzir tokens gastos na janela da sessão **sem alterar terminais globais fora do projeto**.

## 1. Context Mode (MCP por Projeto — Recomendado)
* **Repositório:** `mksglu/context-mode`
* **No `.mcp.json` do projeto:**
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
* **No Codex CLI:** `codex mcp add context-mode -- npx -y context-mode`
* **Uso:** executa comandos pesados, inspeções e buscas em sandbox local (`ctx_execute`, `ctx_search` com SQLite FTS5), evitando despejar logs gigantes no contexto.

## 2. Ponytail (Skill Global — Sem Dependências)
* **Repositório:** `DietrichGebert/ponytail`
* **Efeito:** força alterações mínimas, zero duplicação e revisão cirúrgica (`ponytail`, `ponytail-audit`, `ponytail-debt`, `ponytail-review`).

## 3. RTK — Rust Token Killer (Binário Único + Hook Local)
* **Repositório:** `rtk-ai/rtk`
* **Escopo limpo:** em vez de rodar `rtk init -g` (global), grave o hook apenas em `<PROJECT_DIR>/.claude/settings.local.json`:
  ```json
  {
    "hooks": {
      "PreToolUse": [
        {
          "matcher": "Bash",
          "hooks": [{ "type": "command", "command": "rtk hook claude" }]
        }
      ]
    }
  }
  ```
* **Benefício:** filtra saídas verbosas (`git`, testes, builds) só dentro dos projetos inicializados pelo `/minerva`.

## 4. Graphify (Opcional para Codebases Maiores)
* **Repositório:** `Graphify-Labs/graphify` (`uv tool install graphifyy`)
* **Uso no projeto:** `graphify .` cria `graphify-out/` (`graph.json`, `GRAPH_REPORT.md`, `graph.html`) via AST (`tree-sitter`) local para evitar greps repetitivos. Adicione `graphify-out/` ao `.gitignore`.

## 5. Nota sobre Headroom (Avançado / Opt-In)
* `headroomlabs-ai/headroom` exige Python 3.13, daemon proxy HTTP (`127.0.0.1:8787`) e override de `ANTHROPIC_BASE_URL`. Não faz parte do bootstrap automático para manter a instalação zero-atrito e multi-CLI.
