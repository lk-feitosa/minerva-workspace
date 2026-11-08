---
tags:
  - ai/skill/doc
  - skill/setup-matt-pocock-skills
skill: "setup-matt-pocock-skills"
source: "triage-labels.md"
updated_at: "2026-11-08T08:03:33.663Z"
---

# Documento: triage-labels (Skill: setup-matt-pocock-skills)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|setup-matt-pocock-skills]]**.  
> **Caminho de origem:** `triage-labels.md`

---

# Triage Labels

The skills speak in terms of five canonical triage roles. This file maps those roles to the actual label strings used in this repo's issue tracker.

| Label in mattpocock/skills | Label in our tracker | Meaning                                  |
| -------------------------- | -------------------- | ---------------------------------------- |
| `needs-triage`             | `needs-triage`       | Maintainer needs to evaluate this issue  |
| `needs-info`               | `needs-info`         | Waiting on reporter for more information |
| `ready-for-agent`          | `ready-for-agent`    | Fully specified, ready for an AFK agent  |
| `ready-for-human`          | `ready-for-human`    | Requires human implementation            |
| `wontfix`                  | `wontfix`            | Will not be actioned                     |

When a skill mentions a role (e.g. "apply the AFK-ready triage label"), use the corresponding label string from this table.

Edit the "Label in our tracker" column to match whatever vocabulary you actually use.

