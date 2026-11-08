---
tags:
  - ai/skill/doc
  - skill/google-firebase-basics
skill: "google-firebase-basics"
source: "references\firebase-cli-guide.md"
updated_at: "2026-11-08T20:55:34.777Z"
---

# Documento: firebase-cli-guide (Skill: google-firebase-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-firebase-basics]]**.  
> **Caminho de origem:** `references\firebase-cli-guide.md`

---

# Exploring Commands

The Firebase CLI documents itself. Use help commands to discover functionality.

-   **Global Help**: List all available commands and categories.

    ```bash
    npx -y firebase-tools@latest --help
    ```

-   **Command Help**: Get detailed usage for a specific command.

    ```bash
    npx -y firebase-tools@latest [command] --help
    # Example:
    npx -y firebase-tools@latest deploy --help
    npx -y firebase-tools@latest firestore:indexes --help
    ```

