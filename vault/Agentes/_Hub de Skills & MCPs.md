---
tags:
  - ai/hub
  - dashboard
updated_at: "2026-11-13T00:30:00Z"
---

# Central de IA (Hub de Skills, MCPs, Mods & Frameworks)

> [!TIP] **Documentação & Guias do Ecossistema**  
> * 🏗️ **Conceito & Arquitetura:** **[[_Arquitetura e Documentação do Ecossistema|Arquitetura, Conceito & Organização Global]]**  
> * 🧠 **Orquestração de Projetos:** **[[Orquestração de Projetos - Minerva & Conselho|Minerva, Conselho dos 5 & Team CODES]]**  
> * 🚀 **Setup em Outro PC:** **[[_Guia de Replicação em Novo PC|Guia Passo a Passo para Replicar em Novo Computador]]**  
> * 🏛️ **Créditos & Atribuições:** **[[_Créditos e Atribuições|Reconhecimento Open-Source & Autores Originais]]**

Estrutura enxuta e 100% em PT-BR no Obsidian:
* 📁 **[[Workspace/Orquestração de Projetos - Minerva & Conselho|Workspace/]]** — Governança, `/minerva`, Conselho e Team CODES
* 📁 **Skills/** — Notas resumidas PT-BR + **7 Hubs de Categoria** no Grafo (pacote `google/skills` removido)
* 📁 **[[MCP/_Visão Geral MCP|MCP/]]** — Servidores MCP (`ai-memory`, `rea`, `agent-desktop`, `magicpath` + `context-mode` por projeto)
* 📁 **[[MODS/vibe-coding-toolkit|MODS/]]** — Toolkits curados de desenvolvimento
* 📁 **[[Frameworks/_Visão Geral Frameworks|Frameworks/]]** — Frameworks e bibliotecas agênticas (`alethe-agents`, `claude-cookbooks`, etc.)
* 📁 **[[Opcionais/_Visão Geral Opcionais|Opcionais/]]** — Ferramentas companheiras (`painel-agents`, `kanban-agents`, `ai-statusline`)

---

## Estatísticas & Perfis (`skills.sh`)

* **Skills Autorais (no repositório):** `minerva`, `painel-agents`, `kanban-agents` (`npx skills add lk-feitosa/minerva-workspace`)
* **Perfil Padrão (`core`):** **32 skills** curadas do `skills.sh` + **3 autorais** (inclui Conselho, Grill-Me, Ponytail, Context Mode MCP + `ctx-stats`/`ctx-doctor`, Find-Skills, UI/UX, TDD, Playwright, Agent Desktop, REA)
* **Perfil Estendido (`full`):** **184 skills** da comunidade sem o bloco Google (`setup.ps1 -Profile full` ou `./setup.sh --full`)
* **Ativação por Workspace (`/minerva`):** configura `.mcp.json` (`context-mode`), hook local opcional do `rtk`, `.kanban/board.json` e sobe Painel (`:3333`) + Kanban (`:3334`)
* **Atualizar Skills Públicas:** `npx skills update -g` (descobrir novas: `npx skills find <termo>`)

---

## 🗂️ Hubs de Categoria (Navegação no Grafo)

* **[[Skills/🎨 Design, UI & Frontend Systems|🎨 Design, UI & Frontend Systems]]** — *Design Systems, acabamento anti-slop, React/Next.js, acessibilidade e geração visual.*
* **[[Skills/🏗️ Arquitetura, Planejamento & TDD|🏗️ Arquitetura, Planejamento & TDD]]** — *Specs, modelagem de domínio, `grill-me`, planejamento, TDD e ADRs.*
* **[[Skills/🤖 Orquestração, Agentes & Maestri|🤖 Orquestração, Agentes & Maestri]]** — *Minerva, Maestri Canvas, Alethe, LLM Council, Painel, Kanban, `find-skills` e MCPs.*
* **[[Skills/🛡️ Segurança, Code Review & Qualidade|🛡️ Segurança, Code Review & Qualidade]]** — *Auditorias, code review, debugging, verification-loop, Ponytail e Playwright.*
* **[[Skills/⚙️ Backend, APIs, Dados & Scraping|⚙️ Backend, APIs, Dados & Scraping]]** — *Backend patterns, APIs, `agent-desktop`, Scrapling, ML e REA.*
* **[[Skills/🚀 DevOps, CI-CD & Ferramentas CLI|🚀 DevOps, CI-CD & Ferramentas CLI]]** — *Git/PRs, CI/CD, Vercel, Bun, Datadog, Sentry, Linear e Notion.*
* **[[Skills/📝 Pesquisa, Conteúdo & Documentação|📝 Pesquisa, Conteúdo & Documentação]]** — *Deep research, escrita técnica, apresentações e documentos.*

---

## 🔌 Servidores MCP, Frameworks & Toolkits

### Servidores MCP Base
* [[MCP/magicpath|🔌 magicpath]]
* [[MCP/rea|🔌 rea]]
* [[MCP/agent-desktop|🔌 agent-desktop]]
* [[MCP/ai-memory|🔌 ai-memory]]
* *(Por projeto via `/minerva`:)* `context-mode` (`npx -y context-mode`)

### Frameworks & Opcionais
* [[Frameworks/agent-teams-ai|🧩 Agent Teams AI]] · [[Frameworks/alethe-agents|🧩 Alethe Agents]] · [[Frameworks/claude-cookbooks|🧩 Claude Cookbooks]] · [[Frameworks/openwork|🧩 OpenWork]] · [[Frameworks/ottomator-agents|🧩 Ottomator Agents]] · [[Frameworks/scrapling|🧩 Scrapling]]
* [[Opcionais/painel-agents|📊 Painel de Agentes (:3333)]] · [[Opcionais/kan-kanban|📋 Kanban Agents (:3334)]] · [[Opcionais/ai-statusline|📟 AI Statusline]] · [[MODS/vibe-coding-toolkit|🚀 Vibe Coding Toolkit]]

---

## ⭐ Skills em Destaque (Núcleo `/minerva`)

* [[Skills/design-taste-frontend|🎨 design-taste-frontend]] · [[Skills/awesome-design-md|📐 awesome-design-md]] · [[Skills/vercel-react-best-practices|⚡ vercel-react-best-practices]]
* [[Skills/playwright-cli|🎭 playwright-cli]] · [[Skills/web-design-guidelines|♿ web-design-guidelines]] · [[Skills/find-skills|🔍 find-skills]]
* [[Skills/alethe|🤖 alethe]] · [[Skills/llm-council|🏛️ llm-council]] · [[Skills/grill-me|🔥 grill-me]] · [[Skills/ponytail|🦥 ponytail]] · [[Skills/painel-agents|📊 painel-agents]]

---

## 📦 Origens Oficiais (`skills.sh` & Repositórios)

| Fonte / Pacote | Perfil `core` | Perfil `full` | Comando `skills.sh` |
| :--- | :---: | :---: | :--- |
| `lk-feitosa/minerva-workspace` *(Autoral)* | 3 | 3 | `npx skills add lk-feitosa/minerva-workspace -g -y` |
| `DietrichGebert/ponytail` | 6 | 6 | `npx skills add DietrichGebert/ponytail -g -y` |
| `mksglu/context-mode` | 2 | 2 | `npx skills add mksglu/context-mode -s ctx-stats ctx-doctor -g -y` |
| `aiwithremy/claude-skills-llm-council` | 1 | 1 | `npx skills add aiwithremy/claude-skills-llm-council -s llm-council -g -y` |
| `mattpocock/skills` | 4 | 38 | `npx skills add mattpocock/skills -g -y` |
| `addyosmani/agent-skills` | 4 | 25 | `npx skills add addyosmani/agent-skills -g -y` |
| `affaan-m/ECC` | 3 | 47 | `npx skills add affaan-m/ECC -g -y` |
| `vercel-labs/agent-skills` | 3 | 9 | `npx skills add vercel-labs/agent-skills -g -y` |
| `vercel-labs/agent-desktop` | 2 | 2 | `npx skills add vercel-labs/agent-desktop -g -y` |
| `composio-community/awesome-codex-skills` | — | 48 | `npx skills add composio-community/awesome-codex-skills -g -y` |
| `Kc1t/alethe-orchestrate-skill` | 1 | 1 | `npx skills add Kc1t/alethe-orchestrate-skill -s alethe -g -y` |
| `vercel-labs/skills` | 1 | 1 | `npx skills add vercel-labs/skills -s find-skills -g -y` |
| `Leonxlnx/taste-skill` | 1 | 1 | `npx skills add Leonxlnx/taste-skill -s design-taste-frontend -g -y` |
| `wearescientist/awesome-design-md` | 1 | 1 | `npx skills add wearescientist/awesome-design-md -s awesome-design-md -g -y` |
| `MagicPathAI/agent-skills` | 1 | 1 | `npx skills add MagicPathAI/agent-skills -s magicpath -g -y` |
| `microsoft/playwright-cli` | 1 | 1 | `npx skills add microsoft/playwright-cli -s playwright-cli -g -y` |
| `morluto/rea` | 1 | 1 | `npx skills add morluto/rea -s reverse-engineer-anything -g -y` |
