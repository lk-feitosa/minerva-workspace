---
tags:
  - ai/skill/doc
  - skill/google-cloud-logging-query-generation
skill: "google-cloud-logging-query-generation"
source: "references\query_service_usage.md"
updated_at: "2026-11-08T20:55:34.372Z"
---

# Documento: query_service_usage (Skill: google-cloud-logging-query-generation)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-cloud-logging-query-generation]]**.  
> **Caminho de origem:** `references\query_service_usage.md`

---

# API enable and disable LQL queries

## Example queries

### Google Cloud Service API enablement audit logs

**Variables to replace:** None

```lql
resource.type="audited_resource" AND
protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.EnableService"
```

### Google Cloud Service API disablement audit logs

**Variables to replace:** None

```lql
resource.type="audited_resource" AND
protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.DisableService"
```

### Logging API disabled

**Variables to replace:** None

```lql
resource.type="audited_resource"
protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.DisableService"
protoPayload.authorizationInfo.granted="true"
protoPayload.response.service.state="DISABLED"
protoPayload.authorizationInfo.resource="services/logging.googleapis.com"
```

