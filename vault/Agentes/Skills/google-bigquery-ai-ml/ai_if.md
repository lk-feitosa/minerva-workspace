---
tags:
  - ai/skill/doc
  - skill/google-bigquery-ai-ml
skill: "google-bigquery-ai-ml"
source: "references\ai_if.md"
updated_at: "2026-11-08T20:55:34.173Z"
---

# Documento: ai_if (Skill: google-bigquery-ai-ml)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-bigquery-ai-ml]]**.  
> **Caminho de origem:** `references\ai_if.md`

---

# BigQuery AI.If

`AI.IF` is a semantic boolean function used to evaluate a condition described in
natural language.

The function can be used to filter and join data based on conditions described
in natural language or multimodal input. The following are common use cases:

-   Sentiment analysis: Find customer reviews with negative sentiment.
-   Topic analysis: Identify news articles related to a specific subject.
-   Image analysis: Select images that contain a specific item.
-   Security: Identify suspicious emails.

## Syntax Reference

```sql
AI.IF(
  [ prompt => ] 'PROMPT'
  [, connection_id => 'CONNECTION_ID' ]
  [, endpoint => 'ENDPOINT' ]
)
```

### Input Arguments

| Argument            | Requirement  | Type          | Description            |
| :------------------ | :----------- | :------------ | :--------------------- |
| **`prompt`**        | **Required** | String/Struct | The prompt text or a   |
:                     :              :               : struct/tuple of        :
:                     :              :               : `(data, instruction)`. :
| **`connection_id`** | Optional     | String        | The connection ID to   |
:                     :              :               : use for the LLM.       :
| **`endpoint`**      | Optional     | String        | The model endpoint     |
:                     :              :               : (e.g.                  :
:                     :              :               : `'gemini-2.5-flash'`). :

### Output Schema

| Column Name         | Type   | Description                               |
| :------------------ | :----- | :---------------------------------------- |
| **(Scalar Result)** | `BOOL` | `TRUE` if the condition is met, `FALSE`   |
:                     :        : otherwise. Returns `NULL` on error/safety :
:                     :        : filter.                                   :

## Examples

### Filter rows based on semantic meaning

```sql
SELECT *
FROM `dataset.table`
WHERE AI.IF(
  (content_column, 'Is this review positive?')
);
```

