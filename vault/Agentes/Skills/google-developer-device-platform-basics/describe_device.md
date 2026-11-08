---
tags:
  - ai/skill/doc
  - skill/google-developer-device-platform-basics
skill: "google-developer-device-platform-basics"
source: "references\describe_device.md"
updated_at: "2026-11-08T20:55:34.582Z"
---

# Documento: describe_device (Skill: google-developer-device-platform-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-developer-device-platform-basics]]**.  
> **Caminho de origem:** `references\describe_device.md`

---

# Describe Device

To see detailed information about a specific device in DDP, send a GET request
to the API using the CATALOG_ID from `gcloud beta device-run devices list`:

```bash
curl \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  "https://devicerun.googleapis.com/v1alpha/projects/${PROJECT_ID}/locations/global/devices/${CATALOG_ID}"
```

