---
tags:
  - ai/skill/doc
  - skill/google-bigquery-ai-ml
skill: "google-bigquery-ai-ml"
source: "references\remote_models.md"
updated_at: "2026-11-08T20:55:34.188Z"
---

# Documento: remote_models (Skill: google-bigquery-ai-ml)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-bigquery-ai-ml]]**.  
> **Caminho de origem:** `references\remote_models.md`

---

# Creating Remote Models
Generative and embedding functions require a remote model that points to a
specific endpoint (e.g., Gemini). Remote models are created using a connection
to interact with Vertex AI.

### Syntax
```sql
CREATE [OR REPLACE] MODEL `project.dataset.model_name`
REMOTE WITH CONNECTION { DEFAULT | `project.region.connection_id` }
OPTIONS (ENDPOINT = 'endpoint_name');
```

### Available Endpoints

* **Generative**: `gemini-2.5-pro`, `gemini-2.5-flash`
* **Embedding**: `text-embedding-005`, `text-multilingual-embedding-002`,
  `gemini-embedding-001`.

### Connection Usage
If `REMOTE WITH CONNECTION DEFAULT` is used, BigQuery automatically attempts to
use a default connection in the model's region. Default connection should be
the default behavior. Otherwise, you must specify a fully qualified connection
ID (e.g., `my-project.us.my-connection`).

