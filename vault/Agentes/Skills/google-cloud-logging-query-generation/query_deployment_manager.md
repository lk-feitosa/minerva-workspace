---
tags:
  - ai/skill/doc
  - skill/google-cloud-logging-query-generation
skill: "google-cloud-logging-query-generation"
source: "references\query_deployment_manager.md"
updated_at: "2026-11-08T06:43:45.220Z"
---

# Documento: query_deployment_manager (Skill: google-cloud-logging-query-generation)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-cloud-logging-query-generation]]**.  
> **Caminho de origem:** `references\query_deployment_manager.md`

---

# Cloud Deployment Manager LQL queries

## Base schema and structural patterns

Cloud Deployment Manager uses the `deployment` resource type natively to record
log payloads and errors encountered during template execution and infrastructure
creation.

### Core resource types

*   **Deployments (`deployment`)**: Captures the operational events, validation
    logs, and execution errors directly related to your deployment stack.

### Targeting specific deployments

*   Filter by `resource.labels.name="<DEPLOYMENT_NAME>"` to track all relevant
    logs isolated to a specific deployment configuration block.

## Example queries

### Deployment Manager errors

**Variables to replace:** None

```lql
resource.type="deployment" AND
severity>=ERROR
```

