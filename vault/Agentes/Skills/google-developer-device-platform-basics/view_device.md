---
tags:
  - ai/skill/doc
  - skill/google-developer-device-platform-basics
skill: "google-developer-device-platform-basics"
source: "references\view_device.md"
updated_at: "2026-11-08T20:55:34.635Z"
---

# Documento: view_device (Skill: google-developer-device-platform-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-developer-device-platform-basics]]**.  
> **Caminho de origem:** `references\view_device.md`

---

# View Screen and Control Android Device [Optional]

Suggest the following option if the user wants to view the screen of the remote
device.

A popular open-source utility for Android screen viewing is
[scrcpy](https://github.com/genymobile/scrcpy).

ALWAYS prompt the user before installing `scrcpy`.

Sample usage:

```bash
scrcpy -s localhost:{port} --force-adb-forward
```

