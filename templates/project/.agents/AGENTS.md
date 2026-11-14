# AGENTS.md — Regras Gerais do Projeto

Este repositório é orquestrado pela **Minerva** (`~/.minerva` / `.agents/MINERVA.md`).

## 1. Fluxo Git & Branches Semânticas
* **Proibido** criar branches genéricas (`sprint-1`, `sprint-2`, `teste`).
* Crie sempre branches semânticas ligadas à demanda: `feature/<slug-semantico>`, `fix/<slug>`, `refactor/<slug>`, `docs/<slug>`.
* Sub-branches opcionais para trabalho paralelo do Team CODES: `agent/ui`, `agent/backend`, `agent/tests`, `agent/docs`.
* **Continuidade:** ajustes da mesma demanda permanecem na mesma branch ativa.

## 2. Convenção de Commits com Emojis
* `✨ feat(<escopo>):` nova funcionalidade
* `🐛 fix(<escopo>):` correção de bug
* `🎨 style/ui(<escopo>):` layout, CSS, design system
* `♻️ refactor(<escopo>):` melhoria interna sem alterar comportamento
* `🧪 test(<escopo>):` testes unitários, integração ou E2E
* `📄 docs(<escopo>):` documentação (`docs/`, ADR, README)
* `🔧 chore(<escopo>):` configuração, dependências, CI/tooling

## 3. Disciplina de Código & Economia de Contexto
* **`ponytail`:** faça a menor alteração limpa que resolve o problema, sem duplicar helpers ou criar abstrações especulativas.
* **`context-mode`:** use `ctx_execute` / `ctx_search` para logs e inspeções pesadas sem poluir a janela de contexto.
* **`ai-memory`:** consulte decisões anteriores no `ai-memory` e registre novas decisões relevantes em `docs/adr/` e no MCP.
* **Kanban:** mantenha `.kanban/board.json` sincronizado ao iniciar, mover ou concluir tarefas.
