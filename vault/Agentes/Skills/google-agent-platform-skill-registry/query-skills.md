---
tags:
  - ai/skill/doc
  - skill/google-agent-platform-skill-registry
skill: "google-agent-platform-skill-registry"
source: "references\query-skills.md"
updated_at: "2026-11-08T20:55:33.946Z"
---

# Documento: query-skills (Skill: google-agent-platform-skill-registry)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-agent-platform-skill-registry]]**.  
> **Caminho de origem:** `references\query-skills.md`

---

# Skill Discovery

This document covers safe, read-only operations for finding and inspecting
skills as well as their revision histories in the Skill Registry.

## Search Skills
Find skills matching a semantic search term.

### Supported Flags

*   `--query` (Required): The semantic query to find matching skills.
*   `--top-k` (Optional): The maximum number of skills to return. Defaults to 5.

```bash
python3 scripts/skill_registry_ops.py search \
  --query "test skill" \
  --top-k 5
```

## List Skills
List all skills in the registry for the configured project and location.

### Supported Flags

*(None)*

```bash
python3 scripts/skill_registry_ops.py list
```

## Get Skill
Retrieve details for a specific skill by its ID.

### Supported Flags

*   `--skill-id` (Required): The unique identifier for the skill.

```bash
python3 scripts/skill_registry_ops.py get --skill-id "my-skill"
```

## List Revisions
Inspect the history of changes / versions for a specific skill. (Read-only
metadata about lifecycle).

### Supported Flags

*   `--skill-id` (Required): The unique identifier for the skill.

```bash
python3 scripts/skill_registry_ops.py list-revision --skill-id "my-skill"
```

## Get Revision
Fetch details of a specific revision.

### Supported Flags

*   `--skill-id` (Required): The unique identifier for the skill.
*   `--revision-id` (Required): The specific revision ID to fetch (e.g., from
    list-revision).

```bash
python3 scripts/skill_registry_ops.py get-revision \
  --skill-id "my-skill" \
  --revision-id "test-revision-123"
```

