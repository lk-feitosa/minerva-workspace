---
tags:
  - ai/skill/doc
  - skill/google-firebase-basics
skill: "google-firebase-basics"
source: "references\refresh\gemini-cli.md"
updated_at: "2026-11-08T08:03:32.635Z"
---

# Documento: gemini-cli (Skill: google-firebase-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-firebase-basics]]**.  
> **Caminho de origem:** `references\refresh\gemini-cli.md`

---

# Refresh Gemini CLI Local Environment

Follow these steps to refresh Gemini CLI's local environment, ensuring that
their agent skills and plugins are fully up-to-date.

Use the native Gemini CLI extension manager instead of `npx`.

1.  **Update the Extension:** Run the specific CLI command to update:

    ```bash
    gemini extensions update firebase
    ```

    *Note: If the extension is named differently, replace `firebase` with the
    correct name from `gemini extensions list`.*

