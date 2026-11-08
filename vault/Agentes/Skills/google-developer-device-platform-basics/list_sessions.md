---
tags:
  - ai/skill/doc
  - skill/google-developer-device-platform-basics
skill: "google-developer-device-platform-basics"
source: "references\list_sessions.md"
updated_at: "2026-11-08T20:55:34.582Z"
---

# Documento: list_sessions (Skill: google-developer-device-platform-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-developer-device-platform-basics]]**.  
> **Caminho de origem:** `references\list_sessions.md`

---

# List Active Sessions

To list active device sessions and filter for those in the `ACTIVE` state:

```bash
curl -s -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  "https://devicestreaming.googleapis.com/v1/projects/${PROJECT_ID}/deviceSessions" \
  | python3 -c "
import sys, json
data = json.load(sys.stdin)
sessions = data.get('deviceSessions', [])
active = [s for s in sessions if s.get('state') == 'ACTIVE']
print(json.dumps(active, indent=2))
"
```

