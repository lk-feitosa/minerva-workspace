---
tags:
  - ai/skill
  - agent-tooling
name: "painel-agents"
github: "Local / Ecossistema Pessoal"
updated_at: "2026-11-08T20:55:36.189Z"
---

# Skill: painel-agents

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [Local / Ecossistema Pessoal](Local / Ecossistema Pessoal)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\painel-agents`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
Abre e gerencia o Painel de Agentes do Maestri em tempo real. Use quando o usuário pedir para ver o status dos agentes, abrir o painel, monitorar cotas ou tarefas ativas no canvas.





---

## Instruções Principais & Comandos Técnicos


# Painel de Agentes (Maestri)

Monitor em tempo real para visualizar as tarefas, cápsulas 3D de cotas por conta (`Antigravity`, `Codex`, `Claude Code`), sincronização do Kanban, aprovações pendentes e o ecossistema de **Skills & MCPs do Projeto** no workspace atual do Maestri.

## Como acionar

Qualquer agente pode abrir, verificar ou reativar silenciosamente o painel:

### Comandos disponíveis:

- `painel` — Inicia o monitor e abre automaticamente o card de Portal no canvas do Maestri (`http://localhost:3333`).
- `wscript.exe "S:\DEV\painel-agents\iniciar-silencioso.vbs"` — **(Auto-Heal no Windows)** Verifica se a porta `3333` já está ativa (`--ensure`) e, se estiver desligada (ex.: após reiniciar o PC), sobe o servidor silenciosamente em segundo plano sem bloquear o terminal.
- `python "S:\DEV\painel-agents\painel.py" --sem-portal --ensure` — Garante que o coletor/servidor na porta `3333` esteja ativo sem criar janelas duplicadas.
- `painel --uma-vez` — Faz uma passada única de leitura dos agentes, cotas, Kanban e Skills/MCPs e atualiza `publico/dados.json` e `publico/dados.js`.
- `painel --porta 3333` — Define a porta HTTP local.

## O que o Painel exibe (`http://localhost:3333`)

1. **Tabela de Agentes (Frente e Verso 3D):** Estado (`Trabalhando` / `Ocioso`), modelo, contexto (`%`), PR/CI e a **Missão** sincronizada automaticamente com os cartões ativos do `.kanban/board.json`.
2. **Cards de Cota 3D por Conta (`cotas.js`):** Cápsulas interativas com régua de tempo decorrido (5h e Semana), tilt 3D e tarja pixelada de privacidade no e-mail para **Antigravity (Google AI Pro)**, **Codex CLI** e **Claude Code**.
3. **Precisa de Você:** Cartões 3D com passo a passo para aprovações pendentes do usuário (ex.: aprovação da Spec e escolha consultiva de modelos do Team CODES).
4. **Portas & Serviços Locais (Anti-Colisão `#secao-portas`):** Seção isolada e recolhível com mapa de portas IPv4/IPv6 do projeto (`docs/ports.md`), evitando conflitos com serviços externos.
5. **Skills, MCPs & Modelos do Projeto (`#ecossistema`):**
   - Tabela de **Alocação Consultiva de Modelos (Team CODES)** sugerida pela Minerva;
   - **Skills em Uso no Projeto** (`maestri`, `alethe`, `painel-agents`, `frontend-ui-engineering`, `tdd-workflow`, `security-review`, etc.);
   - **Servidores MCP & Barramentos Conectados** (`ai-memory`, `kan`, `maestri-ipc`, `agent-desktop`, `rea`, `magicpath`).
6. **Integração com Missões do Kanban:** Leitura viva do quadro Kanban oficial para alimentar automaticamente o status das missões de cada terminal na tabela de agentes e alertar quando houver pontos de decisão pendentes com o usuário.

