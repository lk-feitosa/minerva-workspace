---
tags:
  - ai/skill/doc
  - skill/google-developer-device-platform-basics
skill: "google-developer-device-platform-basics"
source: "references\session_status.md"
updated_at: "2026-11-08T20:55:34.584Z"
---

# Documento: session_status (Skill: google-developer-device-platform-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-developer-device-platform-basics]]**.  
> **Caminho de origem:** `references\session_status.md`

---

# Session Status

To check the status of a device session, send a GET request to the API:

```bash
curl -s -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  "https://devicestreaming.googleapis.com/v1/{session_name}"
```

