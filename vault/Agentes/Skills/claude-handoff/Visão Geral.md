---
tags:
  - ai/skill
  - agent-tooling
name: "claude-handoff"
github: "https://github.com/mattpocock/skills"
updated_at: "2026-11-08T20:55:33.734Z"
---

# Skill: claude-handoff

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\claude-handoff`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
Hand the current conversation off to a fresh background agent that picks up the work immediately.





---

## Instruções Principais & Comandos Técnicos


Write a handoff summary of the current conversation so a fresh agent can continue the work. Save it to the temporary directory of the user's OS, then launch a background agent seeded with it as its prompt: `claude --bg --name "<descriptive name>" -- "$(cat <summary file>)"`. Passing the file keeps the shell from running backticks or expanding `$` in the summary. It starts in the current working directory and returns immediately; the user manages it with `claude agents`.

Always pass `-n`/`--name` with a descriptive name (e.g. `--name "Fix login bug"`); it sets the display name shown in the job list, session picker, and terminal title.

Include a "suggested skills" section in the summary, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information, since the summary becomes the agent's prompt.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the summary accordingly.

