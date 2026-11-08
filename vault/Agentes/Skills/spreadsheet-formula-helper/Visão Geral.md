---
tags:
  - ai/skill
  - agent-tooling
name: "spreadsheet-formula-helper"
github: "https://github.com/composio-community/awesome-codex-skills"
updated_at: "2026-11-08T20:55:36.342Z"
---

# Skill: spreadsheet-formula-helper

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\spreadsheet-formula-helper`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
Write and debug spreadsheet formulas (Excel/Google Sheets), pivot tables, and array formulas; translate between dialects; use when users need working formulas with examples and edge-case checks.





---

## Instruções Principais & Comandos Técnicos


# Spreadsheet Formula Helper

Produce reliable spreadsheet formulas with explanations.

## Inputs to gather
- Platform (Excel/Sheets), locale (comma vs. semicolon separators), sample data layout (headers, ranges), expected outputs, and constraints (volatile functions allowed?).
- Provide small example rows and the desired result for them.

## Workflow
1) Restate the problem with explicit ranges and sheet names; propose a minimal sample to verify.
2) Draft formula(s); when dynamic arrays are available, prefer them over copy-down formulas.
3) Explain how it works and where to place it; include named ranges if helpful.
4) Edge cases: blank rows, mixed types, timezone/date quirks, duplicates; offer guardrails (e.g., `IFERROR`, `LET`, `LAMBDA`).
5) Variants: if porting between Excel and Sheets, provide both versions.

## Output
- Primary formula, short explanation, and a 2–3 row worked example showing inputs → outputs.
- Optional: quick troubleshooting checklist for common errors.

