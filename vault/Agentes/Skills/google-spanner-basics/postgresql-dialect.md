---
tags:
  - ai/skill/doc
  - skill/google-spanner-basics
skill: "google-spanner-basics"
source: "references\postgresql-dialect.md"
updated_at: "2026-11-08T20:55:36.013Z"
---

# Documento: postgresql-dialect (Skill: google-spanner-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-spanner-basics]]**.  
> **Caminho de origem:** `references\postgresql-dialect.md`

---

# PostgreSQL Dialect Support

Spanner provides PostgreSQL dialect support by expressing Spanner database
features through a subset of open source PostgreSQL dialect constructs.

## Key Considerations

*   **Portability**: Easier migration to other PostgreSQL databases if needed.
*   **Familiarity**: Leverages existing knowledge of PostgreSQL syntax and
    tools.
*   **Ecosystem**: Supports tools like `psql` and PostgreSQL drivers (via
    PGAdapter).

## Features and Extensions

Spanner includes extensions to support Spanner-specific features within the
PostgreSQL dialect:

- Interleaved tables
- Time to live (TTL)
- Query hints

## Limitations

Spanner does not support some open source PostgreSQL features: 

- Triggers 
- `SERIAL` 
- Transactional DDL 
- User-defined data types and operators

For more information, see
[The PostgreSQL language in Spanner](https://docs.cloud.google.com/spanner/docs/reference/postgresql/overview.md.txt).

