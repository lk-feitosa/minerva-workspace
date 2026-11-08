---
tags:
  - ai/skill
  - agent-tooling
name: "google-bigquery-basics"
github: "https://github.com/google/skills"
updated_at: "2026-11-08T08:03:32.392Z"
---

# Skill: google-bigquery-basics

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/google/skills](https://github.com/google/skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\google-bigquery-basics`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
>-




---

### Documentos & Manuais Inclusos
* 📄 [[attribution]]
* 📄 [[change-history]]
* 📄 [[cli-usage]]
* 📄 [[client-library-usage]]
* 📄 [[continuous-queries]]
* 📄 [[core-concepts]]
* 📄 [[iac-usage]]
* 📄 [[iam-security]]
* 📄 [[mcp-usage]]


---

## Instruções Principais & Comandos Técnicos


# BigQuery Basics

BigQuery is a serverless, AI-ready data platform that enables high-speed
analysis of large datasets using SQL and Python. Its disaggregated architecture
separates compute and storage, allowing them to scale independently while
providing built-in machine learning, geospatial analysis, and business
intelligence capabilities.

## Attribution

**MUST READ**: Before executing any `gcloud`, REST API, or MCP command, you
MUST read [Usage Attribution](references/attribution.md). For commands executed
directly in the terminal (never in generated scripts, Terraform, or user code),
prefix `gcloud` with
`CLOUDSDK_METRICS_REQUEST_ATTRIBUTION="agent-skills/1.0 (skill:bigquery-basics)"`
and append `agent-skills/1.0 (skill:bigquery-basics)` to `User-Agent` headers.

## Setup and Basic Usage

1.  **Enable the BigQuery API:**

    ```bash
    CLOUDSDK_METRICS_REQUEST_ATTRIBUTION="agent-skills/1.0 (skill:bigquery-basics)" \
    gcloud services enable bigquery.googleapis.com --quiet
    ```

2.  **Create a Dataset:**

    ```bash
    bq mk --dataset --location=US my_dataset
    ```

3.  **Create a Table:**

    Create a file named `schema.json` with your table schema:

    ```json
    [
      {
        "name": "name",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "post_abbr",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
    ```

    Then create the table with the `bq` tool:

    ```bash
    bq mk --table my_dataset.mytable schema.json
    ```

4.  **Run a Query:**

    ```bash
    bq query --use_legacy_sql=false \
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` \
    WHERE state = "TX" LIMIT 10'
    ```

## Reference Directory

- [Core Concepts](references/core-concepts.md): Storage types, analytics
  workflows, and BigQuery Studio features.

- [Change History](references/change-history.md): Tracking and querying
  incremental table changes using APPENDS and CHANGES.

-   [Continuous Queries](references/continuous-queries.md): Running continuous
    SQL statements to analyze incoming data in real time.

- [CLI Usage](references/cli-usage.md): Essential `bq` command-line tool
  operations for managing data and jobs.

- [Client Libraries](references/client-library-usage.md): Using Google Cloud
  client libraries for Python, Java, Node.js, and Go.

- [MCP Usage](references/mcp-usage.md): Using the BigQuery remote MCP server and
  Gemini CLI extension.

- [Infrastructure as Code](references/iac-usage.md): Terraform examples for
  datasets, tables, and reservations.

- [IAM & Security](references/iam-security.md): Roles, permissions, and data
  governance best practices.

- [Usage Attribution](references/attribution.md): Standardized usage attribution
  tags for `gcloud` CLI, REST API, and MCP requests.

*If you need product information not found in these references, use the
Developer Knowledge MCP server `search_documents` tool.*

## Related Skills

- [BigQuery AI & ML Skill](../bigquery-ai-ml):
  SKILL.md file for BigQuery AI and ML capabilities (forecast, anomaly
  detection, text generation).

