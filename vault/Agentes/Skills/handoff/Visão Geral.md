---
tags:
  - ai/skill
  - agent-tooling
name: "handoff"
github: "https://github.com/mattpocock/skills"
updated_at: "2026-11-08T06:43:45.702Z"
---

# Skill: handoff

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\handoff`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
Compact the current conversation into a handoff document for another agent to pick up.





---

## Instruções Principais & Comandos Técnicos


Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows) - not the current workspace.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.

