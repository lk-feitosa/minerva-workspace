---
name: kanban-agents
description: Inicia e opera o Kanban Minimalista local (porta 3334, arquivo .kanban/board.json) para gerenciar tarefas por projeto. Use quando o usuário pedir para abrir o kanban, criar/atualizar cartões ou como parte da inicialização do /minerva.
user-invocable: true
---

# Kanban Agents (Kanban Minimalista por Projeto)

Quadro ágil leve em Python puro (`https://github.com/lk-feitosa/kanban-agents`, zero Docker, zero login) servido na porta `3334` (`http://localhost:3334`), sincronizado em tempo real com `.kanban/board.json` na raiz de cada projeto.

## Localização Portátil

Resolva o diretório da ferramenta nesta ordem:
1. Variável de ambiente `$MINERVA_KANBAN_DIR` (ou `$MINERVA_TOOLS_DIR/kanban-agents`)
2. Diretório irmão ao workspace global: `~/.agents/../kanban-agents` ou `~/.agents/tools/kanban-agents`

Se ainda não estiver instalado localmente:
```bash
git clone https://github.com/lk-feitosa/kanban-agents.git ~/.agents/tools/kanban-agents
```

## Comandos

* **Subir para o projeto atual (salto automático de porta se `3334` estiver ocupada):**
  ```bash
  python "<KANBAN_DIR>/kanban.py" --projeto "<PROJECT_DIR>" --sem-portal
  ```
* **Abrir também no navegador padrão:**
  ```bash
  python "<KANBAN_DIR>/kanban.py" --projeto "<PROJECT_DIR>" --navegador
  ```
* **Background silencioso no Windows:**
  ```cmd
  wscript.exe "<KANBAN_DIR>\iniciar-silencioso.vbs"
  ```
* **Abrir como Portal no Maestri Canvas (quando usando Maestri):**
  ```bash
  maestri portal create http://localhost:3334 "Kanban"
  ```

## Operação com `.kanban/board.json`

* Cada repositório mantém seu estado isolado em `<PROJECT_DIR>/.kanban/board.json` (criado automaticamente ao iniciar `kanban.py` ou pelo `/minerva`).
* Colunas padrão: **Backlog** (`col-backlog`), **A Fazer** (`col-todo`), **Em Progresso** (`col-progresso`), **Revisão** (`col-revisao`) e **Concluído** (`col-concluido`).
* Agentes atualizam títulos, descrições, responsáveis (`agente`), etiquetas, prioridade e checklists diretamente no JSON para refletir imediatamente na interface web.
