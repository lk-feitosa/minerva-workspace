---
tags:
  - ai/hub
  - dashboard
updated_at: "2026-11-12T22:20:00Z"
---

# Central de IA (Hub de Skills, MCPs, Mods & Frameworks)

> [!TIP] **Documentação & Guias do Ecossistema**  
> * 🏗️ **Conceito & Arquitetura:** **[[_Arquitetura e Documentação do Ecossistema|Arquitetura, Conceito & Organização Global]]**  
> * 🧠 **Orquestração de Projetos:** **[[Orquestração de Projetos - Minerva & Conselho|Minerva, Conselho dos 5 & Team CODES]]**  
> * 🚀 **Setup em Outro PC:** **[[_Guia de Replicação em Novo PC|Guia Passo a Passo para Replicar em Novo Computador]]**  
> * 🏛️ **Créditos & Atribuições:** **[[_Créditos e Atribuições|Reconhecimento Open-Source & Autores Originais]]**

Estrutura enxuta e 100% em PT-BR no Obsidian:
* 📁 **[[Workspace/Orquestração de Projetos - Minerva & Conselho|Workspace/]]** — Governança, arquitetura do time e orquestração de projetos
* 📁 **Skills/** — **381 skills** organizadas em **8 Hubs de Categoria** no Grafo (resumo PT-BR + links oficiais para GitHub / `skills.sh`)
* 📁 **[[MCP/_Visão Geral MCP|MCP/]]** — Servidores MCP ativos (`ai-memory`, `rea`, `agent-desktop`, `magicpath`, `kan`)
* 📁 **[[MODS/vibe-coding-toolkit|MODS/]]** — Toolkits curados de desenvolvimento
* 📁 **[[Frameworks/_Visão Geral Frameworks|Frameworks/]]** — Frameworks e bibliotecas agênticas (`kan`, `alethe-agents`, `claude-cookbooks`, etc.)
* 📁 **[[Opcionais/_Visão Geral Opcionais|Opcionais/]]** — Ferramentas complementares e telemetria local (`painel-agents`, `ai-statusline`, `kan-kanban`)

---

## Estatísticas & Fontes (`skills.sh`)

* **Skills Ativas:** **381** (183 rastreadas via `skills.sh` em `.skill-lock.json` + 186 do pacote `google/skills` + 12 locais/Maestri)
* **Servidores MCP:** **5** integrados (`ai-memory`, `rea`, `agent-desktop`, `magicpath`, `kan`)
* **IAs Integradas:** Antigravity (Google), Codex (OpenAI), Claude Code (Anthropic), Gemini CLI, Maestri
* **Atualizar Skills Públicas:** `npx skills update -g` (descobrir novas: `npx skills find <termo>`)

---

## 🗂️ Hubs de Categoria (Navegação no Grafo)

* **[[Skills/🎨 Design, UI & Frontend Systems|🎨 Design, UI & Frontend Systems]]** — *Design Systems, acabamento anti-slop, React/Next.js, acessibilidade e geração visual.*
* **[[Skills/🏗️ Arquitetura, Planejamento & TDD|🏗️ Arquitetura, Planejamento & TDD]]** — *Specs, modelagem de domínio, `grill-me`, planejamento, TDD e ADRs.*
* **[[Skills/🤖 Orquestração, Agentes & Maestri|🤖 Orquestração, Agentes & Maestri]]** — *Maestri Canvas, Alethe, LLM Council, Painel de Agentes, `find-skills` e MCPs.*
* **[[Skills/🛡️ Segurança, Code Review & Qualidade|🛡️ Segurança, Code Review & Qualidade]]** — *Auditorias, code review, debugging, verification-loop, Ponytail e Playwright.*
* **[[Skills/⚙️ Backend, APIs, Dados & Scraping|⚙️ Backend, APIs, Dados & Scraping]]** — *Backend patterns, APIs, `agent-desktop`, Scrapling, ML e REA.*
* **[[Skills/🚀 DevOps, CI-CD & Ferramentas CLI|🚀 DevOps, CI-CD & Ferramentas CLI]]** — *Git/PRs, CI/CD, Vercel, Bun, Datadog, Sentry, Linear e Notion.*
* **[[Skills/📝 Pesquisa, Conteúdo & Documentação|📝 Pesquisa, Conteúdo & Documentação]]** — *Deep research, escrita técnica, apresentações e documentos.*
* **[[Skills/☁️ Google Cloud & Enterprise|☁️ Google Cloud & Enterprise]]** — *GKE, BigQuery, Cloud Run, Spanner, AlloyDB, Genkit, Gemini Platform e Ads.*

---

## 🔌 Servidores MCP, Frameworks & Toolkits

### Servidores MCP
* [[MCP/magicpath|🔌 magicpath]]
* [[MCP/rea|🔌 rea]]
* [[MCP/agent-desktop|🔌 agent-desktop]]
* [[MCP/ai-memory|🔌 ai-memory]]
* [[MCP/kan|🔌 kan]]

### Frameworks & Opcionais
* [[Frameworks/agent-teams-ai|🧩 Agent Teams AI]] · [[Frameworks/alethe-agents|🧩 Alethe Agents]] · [[Frameworks/claude-cookbooks|🧩 Claude Cookbooks]] · [[Frameworks/kan|🧩 Kan]] · [[Frameworks/openwork|🧩 OpenWork]] · [[Frameworks/ottomator-agents|🧩 Ottomator Agents]] · [[Frameworks/scrapling|🧩 Scrapling]]
* [[Opcionais/painel-agents|📊 Painel de Agentes]] · [[Opcionais/kan-kanban|📋 Kan Kanban]] · [[Opcionais/ai-statusline|📟 AI Statusline]] · [[MODS/vibe-coding-toolkit|🚀 Vibe Coding Toolkit]]

---

## ⭐ Skills em Destaque (Atalhos Rápidos)

* [[Skills/design-taste-frontend|🎨 design-taste-frontend]] — Frontend anti-slop no nível de `figma.com` e `x.ai`.
* [[Skills/awesome-design-md|📐 awesome-design-md]] — Catálogo de especificações `DESIGN.md` (Linear, Stripe, Apple, Vercel, Supabase).
* [[Skills/vercel-react-best-practices|⚡ vercel-react-best-practices]] — Performance React/Next.js oficial da Vercel.
* [[Skills/playwright-cli|🎭 playwright-cli]] — Automação e snapshots de navegador via CLI (Microsoft).
* [[Skills/web-design-guidelines|♿ web-design-guidelines]] — Auditoria de acessibilidade e interface (Vercel).
* [[Skills/find-skills|🔍 find-skills]] — Descoberta dinâmica e instalação via `skills.sh`.
* [[Skills/alethe|🤖 alethe]] · [[Skills/llm-council|🏛️ llm-council]] · [[Skills/ponytail|🦥 ponytail]] · [[Skills/painel-agents|📊 painel-agents]]

---

## 📦 Origens Oficiais (`skills.sh` & Repositórios)

| Fonte / Pacote | Qtd | Comando `skills.sh` |
| :--- | :---: | :--- |
| `google/skills` | 186 | `npx skills add google/skills -g -y` |
| `composio-community/awesome-codex-skills` | 48 | `npx skills add composio-community/awesome-codex-skills -g -y` |
| `affaan-m/ECC` | 47 | `npx skills add affaan-m/ECC -g -y` |
| `mattpocock/skills` | 39 | `npx skills add mattpocock/skills -g -y` |
| `addyosmani/agent-skills` | 25 | `npx skills add addyosmani/agent-skills -g -y` |
| `vercel-labs/agent-skills` | 9 | `npx skills add vercel-labs/agent-skills -g -y` |
| `Maestri (Local)` | 8 | Integrado ao Maestri Canvas |
| `DietrichGebert/ponytail` | 6 | `npx skills add dietrichgebert/ponytail -g -y` |
| `Local (Minerva Workspace)` | 3 | `painel-agents`, `scrapling`, `cloudflare-security-audit` |
| `vercel-labs/agent-desktop` | 2 | `npx skills add vercel-labs/agent-desktop -s agent-desktop agent-desktop-windows -g -y` |
| `vercel-labs/skills` | 1 | `npx skills add vercel-labs/skills -s find-skills -g -y` |
| `Leonxlnx/taste-skill` | 1 | `npx skills add leonxlnx/taste-skill -s design-taste-frontend -g -y` |
| `wearescientist/awesome-design-md` | 1 | `npx skills add wearescientist/awesome-design-md -s awesome-design-md -g -y` |
| `microsoft/playwright-cli` | 1 | `npx skills add microsoft/playwright-cli -s playwright-cli -g -y` |
| `Kc1t/alethe-orchestrate-skill` | 1 | `npx skills add kc1t/alethe-orchestrate-skill -s alethe -g -y` |
| `aiwithremy/claude-skills-llm-council` | 1 | `npx skills add aiwithremy/claude-skills-llm-council -s llm-council -g -y` |
| `MagicPathAI/agent-skills` | 1 | `npx skills add MagicPathAI/agent-skills -s magicpath -g -y` |
| `morluto/rea` | 1 | `npx skills add morluto/rea -s reverse-engineer-anything -g -y` |
