---
tags:
  - ai/skill/doc
  - skill/google-developer-device-platform-basics
skill: "google-developer-device-platform-basics"
source: "references\update_session_expiration.md"
updated_at: "2026-11-08T20:55:34.634Z"
---

# Documento: update_session_expiration (Skill: google-developer-device-platform-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-developer-device-platform-basics]]**.  
> **Caminho de origem:** `references\update_session_expiration.md`

---

# Update Device Session Expiration Time

To update a device session expiration time, send a PATCH request with the
`updateMask=ttl` query parameter and specify the new remaining duration `ttl`
(e.g., `3600s`).

```bash
curl -s -X PATCH \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "ttl": "3600s"
  }' \
  "https://devicestreaming.googleapis.com/v1/{session_name}?updateMask=ttl"
```

