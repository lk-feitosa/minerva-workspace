# Minerva Workspace Rules

Este projeto opera sob a orquestração **Minerva** (`skills/minerva`).

## Economia de Contexto & Código Enxuto
- **Edições Mínimas (`ponytail`):** faça a menor alteração correta possível; reutilize helpers existentes; nunca duplique lógica nem adicione abstrações especulativas.
- **Saídas Pesadas (`context-mode`):** quando `context-mode` estiver ativo no `.mcp.json`, prefira executar leituras/logs extensos via sandbox (`ctx_execute` / `ctx_search`) para não poluir a janela.
- **Estado do Projeto:** tarefas vivem em `.kanban/board.json` (servido pelo `kanban-agents`) e decisões/especificações em `docs/spec.md` + `ai-memory`.

## Fluxo de Trabalho
- **Modo Padrão:** analise a demanda, atualize `docs/spec.md` e `.kanban/board.json`, e execute em branch semântica (`feature/<slug>`, `fix/<slug>`, `refactor/<slug>`). Nunca use nomes genéricos como `sprint-1`.
- **Stress-Test (`[GRILL-ME]` / `[CONSELHO]`):** antes de codar decisões críticas, rode 2–4 perguntas cirúrgicas (`grill-me`) e o parecer do Conselho dos 5 (`llm-council`).
- **Micro-Ajustes:** correções pontuais são aplicadas direto sem abrir cartões pesados nem recrutar terminais extras.
