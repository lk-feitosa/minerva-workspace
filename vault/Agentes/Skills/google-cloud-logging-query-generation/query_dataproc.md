---
tags:
  - ai/skill/doc
  - skill/google-cloud-logging-query-generation
skill: "google-cloud-logging-query-generation"
source: "references\query_dataproc.md"
updated_at: "2026-11-08T08:03:32.458Z"
---

# Documento: query_dataproc (Skill: google-cloud-logging-query-generation)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-cloud-logging-query-generation]]**.  
> **Caminho de origem:** `references\query_dataproc.md`

---

# Managed Service for Apache Spark LQL queries

## Example queries

### Dataproc Apache Hadoop logs

**Variables to replace:** None

```lql
resource.type="cloud_dataproc_cluster" AND
jsonPayload.class:"org.apache.hadoop.mapreduce"
```

