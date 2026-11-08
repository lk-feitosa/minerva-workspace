---
tags:
  - ai/skill/doc
  - skill/google-developer-device-platform-basics
skill: "google-developer-device-platform-basics"
source: "references\cancel_session.md"
updated_at: "2026-11-08T08:03:32.562Z"
---

# Documento: cancel_session (Skill: google-developer-device-platform-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-developer-device-platform-basics]]**.  
> **Caminho de origem:** `references\cancel_session.md`

---

# Cancel Session

To cancel a device session, send a POST request with an empty body (`{}`) to the
cancel endpoint:

```bash
curl -s -X POST \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{}" \
  "https://devicestreaming.googleapis.com/v1/{session_name}:cancel"
```

