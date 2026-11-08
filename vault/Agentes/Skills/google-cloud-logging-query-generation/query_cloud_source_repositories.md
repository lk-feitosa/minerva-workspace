---
tags:
  - ai/skill/doc
  - skill/google-cloud-logging-query-generation
skill: "google-cloud-logging-query-generation"
source: "references\query_cloud_source_repositories.md"
updated_at: "2026-11-08T20:55:34.356Z"
---

# Documento: query_cloud_source_repositories (Skill: google-cloud-logging-query-generation)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-cloud-logging-query-generation]]**.  
> **Caminho de origem:** `references\query_cloud_source_repositories.md`

---

# Cloud Source Repositories LQL queries

## Example queries

### Cloud Source Repository logs

**Variables to replace:** `<REPOSITORY_NAME>`

```lql
resource.type="csr_repository" AND
resource.labels.name="<REPOSITORY_NAME>"
```

