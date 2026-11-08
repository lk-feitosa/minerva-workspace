---
tags:
  - ai/skill/doc
  - skill/google-cloud-logging-query-generation
skill: "google-cloud-logging-query-generation"
source: "references\query_dataflow.md"
updated_at: "2026-11-08T08:03:32.458Z"
---

# Documento: query_dataflow (Skill: google-cloud-logging-query-generation)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-cloud-logging-query-generation]]**.  
> **Caminho de origem:** `references\query_dataflow.md`

---

# Dataflow LQL queries

## Example queries

### Warnings or errors from Dataflow workers

**Variables to replace:** None

```lql
resource.type="dataflow_step"
log_id("dataflow.googleapis.com/worker")
severity >= WARNING
```

