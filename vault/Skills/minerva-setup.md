---
tags:
  - ai/skill
  - category/orchestration
  - source/lk-feitosa-minerva-workspace
name: "minerva-setup"
category: "🤖 Orquestração, Agentes & Maestri"
source: "lk-feitosa/minerva-workspace"
github: "https://github.com/lk-feitosa/minerva-workspace"
updated_at: "2026-11-17T20:05:00Z"
---

# 🤖 Skill Autoral: `minerva-setup` (`/minerva-setup`)

> [!TIP] **Setup Global do PC em 1 Comando**
> * **Repositório:** [lk-feitosa/minerva-workspace](https://github.com/lk-feitosa/minerva-workspace)
> * **Caminho Local:** `~/.minerva/skills/minerva-setup/SKILL.md`
> * **Quando usar:** Uma única vez ao configurar um PC novo (especialmente após rodar `npx skills add lk-feitosa/minerva-workspace -g -y`) ou para atualizar/reparar a base global `~/.minerva`.

---

## Resumo em Português

Enquanto o comando **`/minerva`** é usado **dentro do workspace de cada projeto**, o comando **`/minerva-setup`** é o instalador global da máquina:
1. Clona ou atualiza `lk-feitosa/minerva-workspace` na raiz canônica única **`~/.minerva`** (`%USERPROFILE%\.minerva`).
2. Vasculha e migra **skills antigas** (`~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills`, `~/.agents/skills`) para `~/.minerva/skills/` sem duplicar.
3. Sincroniza e mescla **MCPs globais** (`ai-memory`, `rea`, `agent-desktop`) nos arquivos dos CLIs sem apagar nem duplicar servidores MCP que o usuário já tenha.
4. Instala os **17 pacotes curados** do `skills-manifest.json` via `skills.sh` e garante os apps companheiros **`painel-agents` (`:3333`)** e **`kanban-agents` (`:3334`)**.

## Links
* **Hub da Categoria:** [[Skills/🤖 Orquestração, Agentes & Maestri|🤖 Orquestração, Agentes & Maestri]]
* **Próximo Passo no Projeto:** [[Skills/minerva|🐍 minerva (/minerva)]]
