---
tags:
  - ai/skill
  - agent-tooling
name: "research"
github: "https://github.com/mattpocock/skills"
updated_at: "2026-11-08T06:43:45.833Z"
---

# Skill: research

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\research`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent.





---

## Instruções Principais & Comandos Técnicos


Spin up a **background agent** to do the research, so you keep working while it reads. Start it with a fresh context window.

Its job:

1. Investigate the question against **primary sources** (official docs, source code, specs, first-party APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Write the findings to a single Markdown file, citing each claim's source.
3. Save it where the repo already keeps such notes; match the existing convention, and if there is none, put it somewhere sensible and say where.

