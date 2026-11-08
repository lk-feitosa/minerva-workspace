---
tags:
  - ai/skill/doc
  - skill/google-bigquery-basics
skill: "google-bigquery-basics"
source: "references\iam-security.md"
updated_at: "2026-11-08T20:55:34.202Z"
---

# Documento: iam-security (Skill: google-bigquery-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-bigquery-basics]]**.  
> **Caminho de origem:** `references\iam-security.md`

---

# BigQuery IAM & Security

BigQuery uses Identity and Access Management (IAM) to provide granular access
control to its resources. As a security best practice, follow the
**principle of least privilege**: grant only the permissions required to
perform a specific action. This includes using the least permissive IAM role at
the most granular level—such as the table or view level—that is necessary.

## Predefined IAM Roles

For a complete list of predefined roles and detailed usage information, see [BigQuery IAM roles](https://docs.cloud.google.com/bigquery/docs/access-control.md.txt).

## Service Accounts and Agents

- **Default Service Account:** BigQuery uses a managed service account
  (`bq-PROJECT_NUMBER@bigquery-encryption.iam.gserviceaccount.com` or the more
  general BigQuery Service Agent
  `service-PROJECT_NUMBER@gcp-sa-bigquery.iam.gserviceaccount.com`) for
  internal operations.

- **Service Account Impersonation:** Use
  `gcloud config set auth/impersonate_service_account` for secure, temporary
  credential access.

## Data Security

- **Encryption at Rest:** All data is encrypted by default using Google-managed
  keys. Use Customer-Managed Encryption Keys (CMEK) for greater control.

- **VPC Service Controls:** Define a service perimeter to prevent data
  exfiltration.

- **Column-Level Security:** Use policy tags to restrict access to sensitive
  columns.

- **Row-Level Security:** Use row access policies to filter data based on user
  identity.

- **Data Masking:** Obscure sensitive data in a table while still permitting
  authorized users to access surrounding data.

- **Audit Logs:** Record user activity and system events to enforce data
  governance policies and identify potential security risks.

- **Authorized Views:** Allow users to query a view without granting them access
  to the underlying tables.

For more detailed information, see:
[BigQuery Security Overview](https://cloud.google.com/bigquery/docs/data-governance).

