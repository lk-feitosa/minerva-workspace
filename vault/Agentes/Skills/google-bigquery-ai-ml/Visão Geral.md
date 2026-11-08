---
tags:
  - ai/skill
  - agent-tooling
name: "google-bigquery-ai-ml"
github: "https://github.com/google/skills"
updated_at: "2026-11-08T08:03:32.385Z"
---

# Skill: google-bigquery-ai-ml

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/google/skills](https://github.com/google/skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\google-bigquery-ai-ml`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
>-




---

### Documentos & Manuais Inclusos
* 📄 [[ai_agg]]
* 📄 [[ai_causal_effect]]
* 📄 [[ai_classify]]
* 📄 [[ai_detect_anomalies]]
* 📄 [[ai_evaluate]]
* 📄 [[ai_forecast]]
* 📄 [[ai_generate]]
* 📄 [[ai_generate_embedding]]
* 📄 [[ai_generate_table]]
* 📄 [[ai_if]]
* 📄 [[ai_key_drivers]]
* 📄 [[ai_score]]
* 📄 [[ai_search]]
* 📄 [[ai_similarity]]
* 📄 [[attribution]]
* 📄 [[ml_contribution_analysis]]
* 📄 [[ml_correlation]]
* 📄 [[ml_detect_change_points]]
* 📄 [[ml_seasonality]]
* 📄 [[ml_trend]]
* 📄 [[remote_models]]
* 📄 [[vector_search]]


---

## Instruções Principais & Comandos Técnicos


# BigQuery AI & ML

BigQuery integrates with Vertex AI to provide powerful machine learning and
generative AI capabilities directly within SQL queries using built-in functions
like `AI.FORECAST`, `AI.KEY_DRIVERS`, `AI.DETECT_ANOMALIES`, and `AI.GENERATE`.

## Attribution

**MUST READ**: Before executing any `gcloud`, REST API, or MCP command, you
MUST read [Usage Attribution](references/attribution.md). For commands executed
directly in the terminal (never in generated scripts, Terraform, or user code),
prefix `gcloud` with
`CLOUDSDK_METRICS_REQUEST_ATTRIBUTION="agent-skills/1.0 (skill:bigquery-ai-ml)"`
and append `agent-skills/1.0 (skill:bigquery-ai-ml)` to `User-Agent` headers.

## Reference Directory

-   **Functions Reference**:

    -   **AI.AGG**: [ai_agg.md](references/ai_agg.md) - Multi-row semantic
        aggregation and summarization.
    -   **AI.CAUSAL_EFFECT**:
        [ai_causal_effect.md](references/ai_causal_effect.md) - Quantifies the
        impact of an intervention on a time series.
    -   **AI.CLASSIFY**: [ai_classify.md](references/ai_classify.md) - Classify
        text.
    -   **AI.DETECT_ANOMALIES**:
        [ai_detect_anomalies.md](references/ai_detect_anomalies.md) - Detect
        anomalies.
    -   **AI.EVALUATE**: [ai_evaluate.md](references/ai_evaluate.md) - Evaluate
        models.
    -   **AI.FORECAST**: [ai_forecast.md](references/ai_forecast.md) -
        Time-series forecasting.
    -   **AI.GENERATE**: [ai_generate.md](references/ai_generate.md) - Generate
        text using LLMs.
    -   **AI.GENERATE_EMBEDDING**:
        [ai_generate_embedding.md](references/ai_generate_embedding.md) -
        Generate embeddings.
    -   **AI.GENERATE_TABLE**:
        [ai_generate_table.md](references/ai_generate_table.md) - Table-valued
        AI generation.
    -   **AI.IF**: [ai_if.md](references/ai_if.md) - Evaluate semantic
        conditions.
    -   **AI.KEY_DRIVERS**: [ai_key_drivers.md](references/ai_key_drivers.md) -
        Identifies key drivers, this is a TVF.
    -   **AI.SCORE**: [ai_score.md](references/ai_score.md) - Score data.
    -   **AI.SEARCH**: [ai_search.md](references/ai_search.md) - Semantic
        search.
    -   **AI.SIMILARITY**: [ai_similarity.md](references/ai_similarity.md) -
        Semantic similarity.
    -   **Remote Models**: [remote_models.md](references/remote_models.md) -
        Working with remote models (Vertex AI).
    -   **CONTRIBUTION_ANALYSIS**:
        [ml_contribution_analysis.md](references/ml_contribution_analysis.md)
        -   Finds contributing factors, key drivers of change. Requires creating
            a MODEL entity.
    -   **ML.CORRELATION**: [ml_correlation.md](references/ml_correlation.md) -
        Calculates correlation between columns, optionally sliced by dimensions.
    -   **ML.DETECT_CHANGE_POINTS**:
        [ml_detect_change_points.md](references/ml_detect_change_points.md) -
        Detects structural breaks or sustained shifts in a time series.
    -   **ML.SEASONALITY**: [ml_seasonality.md](references/ml_seasonality.md) -
        Extracts seasonal components from a time series.
    -   **ML.TREND**: [ml_trend.md](references/ml_trend.md) - Extracts the
        long-term trend component from a time series.
    -   **VECTOR_SEARCH**: [vector_search.md](references/vector_search.md) -
        Vector search best practices.

## Related Skills

-   [BigQuery Basics Skill](../bigquery-basics): SKILL.md file for core BigQuery
    concepts, resource management, CLI, and client libraries.

