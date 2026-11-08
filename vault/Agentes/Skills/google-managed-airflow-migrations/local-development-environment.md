---
tags:
  - ai/skill/doc
  - skill/google-managed-airflow-migrations
skill: "google-managed-airflow-migrations"
source: "references\local-development-environment.md"
updated_at: "2026-11-08T06:43:45.661Z"
---

# Documento: local-development-environment (Skill: google-managed-airflow-migrations)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-managed-airflow-migrations]]**.  
> **Caminho de origem:** `references\local-development-environment.md`

---

# Local Development Environment Verification

If you want to verify your changes locally before deploying to the target
environment, you can use the Composer Local Development CLI tool
(`composer-dev`).

## 1. List and Describe Local Environments

1.  **List Local Environments:** `composer-dev list`
2.  **Describe Local Environment:** `composer-dev describe <LOCAL_ENV_NAME>`

## 2. Identify Active Environment and DAGs Location

*   **Active Environment:** Specified by `<LOCAL_ENV_NAME>`.
*   **DAGs Location:** Shown in `composer-dev describe` output under `Dags
    directory`. Copy your migrated DAGs to this directory to test.

## 3. Verify DAGs and Check for Import Errors

1.  **List Parsed DAGs:**

    ```bash
    composer-dev run-airflow-cmd <LOCAL_ENV_NAME> dags list
    ```

2.  **Check for Import Errors:**

    ```bash
    composer-dev run-airflow-cmd <LOCAL_ENV_NAME> dags list-import-errors
    ```

