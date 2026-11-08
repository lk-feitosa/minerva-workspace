---
tags:
  - ai/skill
  - agent-tooling
name: "support-ticket-triage"
github: "https://github.com/composio-community/awesome-codex-skills"
updated_at: "2026-11-08T08:03:33.682Z"
---

# Skill: support-ticket-triage

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\support-ticket-triage`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
Triage customer support tickets/emails/chats into categories, priority, and next action; draft responses and create reproducible steps; use for Zendesk/Intercom/Help Scout exports or pasted threads.





---

## Instruções Principais & Comandos Técnicos


# Support Ticket Triage

Standardize how to classify and respond to incoming tickets.

## Inputs to gather
- Ticket text (include attachments/links), product area, customer plan/tier if known.
- Desired outputs: category taxonomy, priority levels, SLA hints, tone/brand voice, whether to draft a reply.

## Workflow
1) Parse context: identify issue type, product surface, severity, customer impact, reproduction hints, and blockers.
2) Categorize: assign category and subcategory; set priority (e.g., P0–P3) with short justification.
3) Draft response (if asked): concise acknowledgment, empathy, restate issue, next steps, and ask for missing info; include reproduction checklist when uncertain.
4) Internal notes: suspected root cause, logs to pull, teams to loop, and tracking IDs to create/attach.
5) Output: tabular or bullet summary with `Category`, `Priority`, `Summary`, `Proposed Fix/Next Steps`, `Reply Draft`.

## Quality checks
- Avoid promises; give ranges not exact ETAs unless provided.
- Mask PII if copying to public channels.
- If signal is weak, present 2–3 likely categories and what evidence would disambiguate.

