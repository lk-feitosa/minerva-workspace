---
tags:
  - ai/hub
  - dashboard
updated_at: "2026-11-14T12:00:00Z"
---

# Central Minerva (Hub de Skills, MCPs, Mods & Frameworks)

> [!TIP] **Documentação & Guias do Ecossistema (`~/.minerva/vault/`)**  
> * 🏗️ **Conceito & Arquitetura:** **[[_Arquitetura e Documentação do Ecossistema|Arquitetura, Conceito & Raiz Global ~/.minerva]]**  
> * 🧠 **Orquestração de Projetos:** **[[Orquestração de Projetos - Minerva & Conselho|Minerva, Conselho dos 5 & Team CODES]]**  
> * 🚀 **Setup em Outro PC:** **[[_Guia de Replicação em Novo PC|Guia Passo a Passo para Replicar em Novo Computador]]**  
> * 🏛️ **Créditos & Atribuições:** **[[_Créditos e Atribuições|Reconhecimento Open-Source & Autores Originais]]**

Estrutura enxuta dentro de **`~/.minerva/vault/`**:
* 📁 **[[Workspace/Orquestração de Projetos - Minerva & Conselho|Workspace/]]** — Governança `/minerva`, Conselho dos 5 e Team CODES
* 📁 **Skills/** — Notas resumidas PT-BR (incluindo `painel-agents` e `kanban-agents`) + **7 Hubs de Categoria** no Grafo
* 📁 **[[MCP/_Visão Geral MCP|MCP/]]** — Servidores MCP (`ai-memory`, `rea`, `agent-desktop`, `magicpath` + `context-mode` por projeto)
* 📁 **[[MODS/vibe-coding-toolkit|MODS/]]** — Toolkits e statusline (`vibe-coding-toolkit`, `[[MODS/ai-statusline|ai-statusline]]`)
* 📁 **[[Frameworks/_Visão Geral Frameworks|Frameworks/]]** — Bibliotecas e frameworks agênticos (`alethe-agents`, `claude-cookbooks`, etc.)

---

## Estatísticas do Catálogo (`skills.sh`)

* **Raiz Canônica no PC:** `~/.minerva` (`%USERPROFILE%\.minerva` no Windows), unificando `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills` e `~/.agents/skills`.
* **Skills Autorais (`lk-feitosa/minerva-workspace`):** `minerva`, `painel-agents`, `kanban-agents` *(todas centralizadas em `~/.minerva/skills/`)*.
* **Catálogo Único Curado:** **188 skills** da comunidade via `skills.sh` + **3 autorais** *(pacote de 186 skills redundantes da Google removido; instalação única completa sem divisão `core`/`full`)*.
* **Ativação por Projeto (`/minerva`):** cria `.gitignore`, `.agents/` (`AGENTS.md`, `MINERVA.md`, `roles/`), `docs/`, `.mcp.json` (`context-mode` + `ai-memory`), hook local opcional do `rtk`, `.kanban/board.json` e sobe Painel (`:3333`) + Kanban (`:3334`) com Portais no Maestri.
* **Atualizar Skills Públicas:** `npx skills update -g` (descobrir novas: `npx skills find <termo>`)

---

## 🗂️ Hubs de Categoria (Navegação no Grafo)

* **[[Skills/🎨 Design, UI & Frontend Systems|🎨 Design, UI & Frontend Systems]]** — *Design Systems, acabamento anti-slop, React/Next.js, `transitions-dev`, `shadcn`/`@react-bits` e acessibilidade.*
* **[[Skills/🏗️ Arquitetura, Planejamento & TDD|🏗️ Arquitetura, Planejamento & TDD]]** — *Specs, modelagem de domínio, `grill-me`, planejamento, TDD e ADRs.*
* **[[Skills/🤖 Orquestração, Agentes & Maestri|🤖 Orquestração, Agentes & Maestri]]** — *`minerva`, `painel-agents`, `kanban-agents`, Maestri Canvas, `alethe`, `llm-council`, `find-skills` e MCPs.*
* **[[Skills/🛡️ Segurança, Code Review & Qualidade|🛡️ Segurança, Code Review & Qualidade]]** — *Auditorias, code review, debugging, verification-loop, Ponytail e Playwright.*
* **[[Skills/⚙️ Backend, APIs, Dados & Scraping|⚙️ Backend, APIs, Dados & Scraping]]** — *Backend patterns, APIs, `agent-desktop`, Scrapling, ML e REA.*
* **[[Skills/🚀 DevOps, CI-CD & Ferramentas CLI|🚀 DevOps, CI-CD & Ferramentas CLI]]** — *Git/PRs, CI/CD, Vercel, Bun, Datadog, Sentry, Linear e Notion.*
* **[[Skills/📝 Pesquisa, Conteúdo & Documentação|📝 Pesquisa, Conteúdo & Documentação]]** — *Deep research, escrita técnica, apresentações e documentos.*

---

## 🔌 Servidores MCP, Frameworks & Mods

* **MCP Base:** [[MCP/magicpath|🔌 magicpath]] · [[MCP/rea|🔌 rea]] · [[MCP/agent-desktop|🔌 agent-desktop]] · [[MCP/ai-memory|🔌 ai-memory]] · *(Por projeto via `/minerva`:)* `context-mode`
* **Frameworks:** [[Frameworks/agent-teams-ai|🧩 Agent Teams AI]] · [[Frameworks/alethe-agents|🧩 Alethe Agents]] · [[Frameworks/claude-cookbooks|🧩 Claude Cookbooks]] · [[Frameworks/openwork|🧩 OpenWork]] · [[Frameworks/ottomator-agents|🧩 Ottomator Agents]] · [[Frameworks/scrapling|🧩 Scrapling]]
* **Mods & Utilitários:** [[MODS/vibe-coding-toolkit|🚀 Vibe Coding Toolkit]] · [[MODS/ai-statusline|📟 AI Statusline]]

---

## 📦 Origens Oficiais (`skills.sh` & Repositórios)

| Fonte / Pacote | Qtd. Skills | Comando `skills.sh` |
| :--- | :---: | :--- |
| `lk-feitosa/minerva-workspace` *(Autoral)* | 3 | `npx skills add lk-feitosa/minerva-workspace -g -y` |
| `composio-community/awesome-codex-skills` | 48 | `npx skills add composio-community/awesome-codex-skills -g -y` |
| `affaan-m/ECC` | 47 | `npx skills add affaan-m/ECC -g -y` |
| `mattpocock/skills` | 38 | `npx skills add mattpocock/skills -g -y` |
| `addyosmani/agent-skills` | 25 | `npx skills add addyosmani/agent-skills -g -y` |
| `vercel-labs/agent-skills` | 9 | `npx skills add vercel-labs/agent-skills -g -y` |
| `DietrichGebert/ponytail` | 6 | `npx skills add DietrichGebert/ponytail -g -y` |
| `mksglu/context-mode` | 2 | `npx skills add mksglu/context-mode -s ctx-stats ctx-doctor -g -y` |
| `vercel-labs/agent-desktop` | 2 | `npx skills add vercel-labs/agent-desktop -g -y` |
| `Jakubantalik/transitions.dev` | 2 | `npx skills add Jakubantalik/transitions.dev -s transitions-dev transitions-polish -g -y` |
| `shadcn-ui/ui` *(+ registry `@react-bits`)* | 2 | `npx skills add shadcn-ui/ui -g -y` |
| `Kc1t/alethe-orchestrate-skill` | 1 | `npx skills add Kc1t/alethe-orchestrate-skill -s alethe -g -y` |
| `vercel-labs/skills` | 1 | `npx skills add vercel-labs/skills -s find-skills -g -y` |
| `Leonxlnx/taste-skill` | 1 | `npx skills add Leonxlnx/taste-skill -s design-taste-frontend -g -y` |
| `wearescientist/awesome-design-md` | 1 | `npx skills add wearescientist/awesome-design-md -s awesome-design-md -g -y` |
| `MagicPathAI/agent-skills` | 1 | `npx skills add MagicPathAI/agent-skills -s magicpath -g -y` |
| `aiwithremy/claude-skills-llm-council` | 1 | `npx skills add aiwithremy/claude-skills-llm-council -s llm-council -g -y` |
| `microsoft/playwright-cli` | 1 | `npx skills add microsoft/playwright-cli -s playwright-cli -g -y` |
| `morluto/rea` | 1 | `npx skills add morluto/rea -s reverse-engineer-anything -g -y` |
