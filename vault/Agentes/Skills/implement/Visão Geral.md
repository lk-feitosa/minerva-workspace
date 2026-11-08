---
tags:
  - ai/skill
  - agent-tooling
name: "implement"
github: "https://github.com/mattpocock/skills"
updated_at: "2026-11-08T08:03:33.314Z"
---

# Skill: implement

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\implement`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
Implement a piece of work based on a spec or set of tickets.





---

## Instruções Principais & Comandos Técnicos


Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Call the Skill tool with "tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, call the Skill tool with "code-review" to review the work.

Commit your work to the current branch.

