---
tags:
  - ai/skill/doc
  - skill/google-cloud-logging-query-generation
skill: "google-cloud-logging-query-generation"
source: "references\query_cloud_tasks.md"
updated_at: "2026-11-08T08:03:32.456Z"
---

# Documento: query_cloud_tasks (Skill: google-cloud-logging-query-generation)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-cloud-logging-query-generation]]**.  
> **Caminho de origem:** `references\query_cloud_tasks.md`

---

# Cloud Tasks LQL queries

## Example queries

### Cloud Tasks queue logs

**Variables to replace:** `<QUEUE_ID>`

```lql
resource.type="cloud_tasks_queue" AND
resource.labels.queue_id="<QUEUE_ID>"
```

