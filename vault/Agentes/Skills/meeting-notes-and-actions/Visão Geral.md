---
tags:
  - ai/skill
  - agent-tooling
name: "meeting-notes-and-actions"
github: "https://github.com/composio-community/awesome-codex-skills"
updated_at: "2026-11-08T06:43:45.739Z"
---

# Skill: meeting-notes-and-actions

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\meeting-notes-and-actions`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
Turn meeting transcripts or rough notes into crisp summaries with decisions, risks, and owner-tagged action items; use for Zoom/Meet/Teams transcripts, call notes, or long meeting chats to generate share-ready outputs.





---

## Instruções Principais & Comandos Técnicos


# Meeting Notes & Actions

Process transcripts into structured notes and action items.

## Inputs to ask for
- Source: pasted transcript/text or file path; meeting title/date; attendees and their handles.
- Output style: terse bullets vs. narrative, action-item format, due date/owner tags, redaction rules if any.

## Workflow
1) Normalize text: strip timestamps/speaker labels if noisy; lightly clean filler words; keep quoted statements intact.
2) Extract essentials: agenda topics, key decisions, open questions, risks/blocked items.
3) Action items: who/what/when. Convert vague asks into concrete tasks; propose due dates if missing.
4) Produce output:
   - Header with meeting title, date, attendees.
   - Sections: `Summary`, `Decisions`, `Open Questions/Risks`, `Action Items` (checkboxes with owner + due).
5) Quality checks: ensure names are consistent; no hallucinated facts; flag ambiguities as clarifying questions.

## Optional extras
- Include timeline of major moments if timestamps exist.
- Provide short Slack/Email-ready blurb (2–3 sentences) plus the full notes.

