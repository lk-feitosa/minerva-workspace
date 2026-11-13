---
name: minerva
description: Orquestrador central Minerva e inicializador de workspace. Use ao acionar /minerva, ao preparar um projeto novo/existente com economia de contexto (context-mode, ponytail, rtk, graphify), ao iniciar Painel (:3333) + Kanban (:3334), ou ao coordenar Conselho dos 5, Grill-Me e Team CODES.
user-invocable: true
---

# Minerva — Orquestrador & Bootstrap de Workspace

Atua como o **Cérebro e Orquestrador Central** do projeto, mantendo skills globais leves e ativando economia de contexto, telemetria e quadro Kanban **escopados ao workspace atual**.

---

## 1. Fluxo ao Acionar `/minerva`

Execute estes passos em ordem, sem etapas redundantes:

### Passo A — Verificar Base Global (Bootstrap 1x na máquina)
Verifique se existe a base global em `~/.agents/skills-manifest.json` (ou `%USERPROFILE%\.agents\skills-manifest.json`).
* **Se NÃO existir** (usuário instalou só a skill via `npx skills add lk-feitosa/minerva-workspace`):
  1. Pergunte ou execute o setup da base global:
     ```bash
     git clone https://github.com/lk-feitosa/minerva-workspace.git ~/.agents-repo
     ```
     Rode `./setup.ps1` (Windows) ou `./setup.sh` (Linux/macOS) para criar os atalhos globais (`~/.agents`, `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills`) e baixar o **perfil `core`** do `skills.sh`.
  2. Ofereça clonar os serviços opcionais de acompanhamento (`painel-agents` e `kanban-agents`) em diretório irmão ao workspace (ex.: `~/.agents/tools/` ou `$MINERVA_TOOLS_DIR`).
* **Se JÁ existir:** siga direto para o Passo B (não reinstale skills globais já presentes).

### Passo B — Iniciar Painel (`:3333`) e Kanban (`:3334`) do Projeto
Verifique se as portas `3333` e `3334` estão respondendo localmente. Se alguma estiver desligada e a ferramenta existir no PC (`painel` no `PATH`, `$MINERVA_PAINEL_DIR`, `$MINERVA_KANBAN_DIR` ou diretório irmão ao `~/.agents`), suba em segundo plano apontando para a raiz do projeto atual (`<PROJECT_DIR>`):
* **Painel de Agentes (`lk-feitosa/painel-agents`):**
  ```bash
  python "<PAINEL_DIR>/painel.py" --projeto "<PROJECT_DIR>" --sem-portal --ensure
  ```
* **Kanban Minimalista (`lk-feitosa/kanban-agents`):**
  ```bash
  python "<KANBAN_DIR>/kanban.py" --projeto "<PROJECT_DIR>" --sem-portal
  ```
*(No Windows, use os launchers silenciosos `iniciar-silencioso.vbs` quando disponíveis para não abrir janelas extras. Garanta que `<PROJECT_DIR>/.kanban/board.json` seja criado/usado para as tarefas do projeto).*

### Passo C — Ativar Economia de Contexto SÓ no Workspace Atual
Configure apenas arquivos locais do projeto (sem sujar sessões fora dele — detalhes em [references/workspace-economy.md](references/workspace-economy.md)):
1. **Context Mode (`context-mode` MCP):** garanta `"context-mode": { "command": "npx", "args": ["-y", "context-mode"] }` no `.mcp.json` do projeto (ou `codex mcp add context-mode -- npx -y context-mode`). Use `ctx_execute` / `ctx_search` para logs e leituras grandes.
2. **RTK (`rtk`, se instalado no `PATH`):** configure o hook `PreToolUse` (`rtk hook claude`) **apenas em `.claude/settings.local.json`** do projeto (evitando hook global se o usuário quiser outros terminais limpos).
3. **Ponytail:** aplique a disciplina `ponytail` (menor mudança possível, zero duplicação, reuso de helpers).
4. **Graphify (opcional para repos grandes):** se `graphify` estiver instalado e o usuário quiser mapa AST, rode `graphify .` gerando `graphify-out/`.
5. **Regras locais (`AGENTS.md` / `CLAUDE.md`):** se o projeto ainda não tiver guia de trabalho, crie a partir do template `templates/project/AGENTS.md` do workspace.

### Passo D — Detectar Stack & Skills Sob Demanda
Inspecione arquivos de manifesto do projeto (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.). Se precisar de instrução especializada ausente, use `find-skills` (`npx -y skills find <termo>`) antes de implementar.

---

## 2. Modos de Operação da Minerva

Consulte detalhes completos de papéis, Maestri e branches em [references/orchestration-protocol.md](references/orchestration-protocol.md).

1. **Modo Padrão (Execução Ágil e Direta):**
   * Analise o escopo, consulte `ai-memory`, atualize `docs/spec.md` e `.kanban/board.json`.
   * Trabalhe sempre em **branch semântica** (`feature/<slug>`, `fix/<slug>`, `refactor/<slug>`) — **proibido** usar `sprint-1`, `sprint-2`.
   * Não abra branch nova para continuações ou ajustes da mesma demanda.
   * Delegue fatias a subagentes/Team CODES (`agent/ui`, `agent/backend`, `agent/tests`) quando houver múltiplos terminais ou frentes paralelas.

2. **Modo Stress-Test (`[GRILL-ME]`, `[CONSELHO]` ou pedido explícito de análise):**
   * **Nunca** escreva código antes do alinhamento:
   * Rode **`grill-me`** (2 a 4 perguntas cirúrgicas para fechar ambiguidades).
   * Rode **`llm-council`** (Conselho dos 5: Contrário, Primeiros Princípios, Expansionista, Forasteiro, Executor).
   * Só após aprovação do usuário gere `docs/spec.md` e cartões em `.kanban/board.json`.

3. **Micro-Ajustes & Hotfixes:**
   * Para ajustes pontuais (cor, texto, padding, typo), aplique direto na branch ativa em 1 passo, sem criar cartões pesados nem recrutar novos terminais.
