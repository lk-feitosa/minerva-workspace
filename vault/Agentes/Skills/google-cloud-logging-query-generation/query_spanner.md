---
tags:
  - ai/skill/doc
  - skill/google-cloud-logging-query-generation
skill: "google-cloud-logging-query-generation"
source: "references\query_spanner.md"
updated_at: "2026-11-08T06:43:45.224Z"
---

# Documento: query_spanner (Skill: google-cloud-logging-query-generation)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-cloud-logging-query-generation]]**.  
> **Caminho de origem:** `references\query_spanner.md`

---

# Spanner LQL queries

## Example queries

### Cloud Spanner logs for a specific Spanner instance

**Variables to replace:** `<SPANNER_INSTANCE>`

```lql
resource.type="spanner_instance" AND
resource.labels.instance_id="<SPANNER_INSTANCE>"
```

