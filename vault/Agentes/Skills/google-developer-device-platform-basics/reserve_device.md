---
tags:
  - ai/skill/doc
  - skill/google-developer-device-platform-basics
skill: "google-developer-device-platform-basics"
source: "references\reserve_device.md"
updated_at: "2026-11-08T06:43:45.313Z"
---

# Documento: reserve_device (Skill: google-developer-device-platform-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-developer-device-platform-basics]]**.  
> **Caminho de origem:** `references\reserve_device.md`

---

# Reserve Device

To reserve a device session, send a POST request to the API:

```bash
curl -s -X POST \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "androidDevice": {
      "androidModelId": "{model_id}",
      "androidVersionId": "{version_id}"
    },
    "clientInfo": {
      "client": "skills/cloud/developer-device-platform-basics"
    }
  }' \
  "https://devicestreaming.googleapis.com/v1/projects/${PROJECT_ID}/deviceSessions"
```

### Client Info

*   `client`: Required. Client identifier set to
    `"skills/cloud/developer-device-platform-basics"` to track sessions
    initiated by this skill.

