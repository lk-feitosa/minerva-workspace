---
tags:
  - ai/skill/doc
  - skill/google-data-manager-api-audience-ingestion
skill: "google-data-manager-api-audience-ingestion"
source: "references\formatting.md"
updated_at: "2026-11-08T06:43:45.296Z"
---

# Documento: formatting (Skill: google-data-manager-api-audience-ingestion)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-data-manager-api-audience-ingestion]]**.  
> **Caminho de origem:** `references\formatting.md`

---

# Format User Data

*   Fetch the [Format user data](https://developers.google.com/data-manager/api/devguides/concepts/formatting.md.txt)
    guide and use that as the source of truth for formatting and
    normalization rules.

*   Use the utility library to format, hash, and encrypt user data
    (emails, phone numbers, addresses).

    **Python Example:**

    ```python
    from google.ads.datamanager_util import Formatter
    from google.ads.datamanager_util.format import Encoding

    formatter: Formatter = Formatter()

    processed_email: str = formatter.process_email_address(
        email, Encoding.HEX
    )
    ```

