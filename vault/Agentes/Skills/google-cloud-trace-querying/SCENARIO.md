---
tags:
  - ai/skill/doc
  - skill/google-cloud-trace-querying
skill: "google-cloud-trace-querying"
source: "assets\queries\slow_db\SCENARIO.md"
updated_at: "2026-11-08T06:43:45.277Z"
---

# Documento: SCENARIO (Skill: google-cloud-trace-querying)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-cloud-trace-querying]]**.  
> **Caminho de origem:** `assets\queries\slow_db\SCENARIO.md`

---

# Scenario: Slow Database Queries

Find traces that contain any database span (marked with `db.system.name` attribute) taking 500 milliseconds or more.
This helps isolate database performance issues from overall application latency.

This query leverages:
*   `db.system.name`: Span label matching the database system name semantic convention.
*   `latency`: Filtering for traces that have at least one span meeting the duration threshold.

