---
tags:
  - ai/skill
  - agent-tooling
name: "google-cloud-sql-basics"
github: "https://github.com/google/skills"
updated_at: "2026-11-08T08:03:32.507Z"
---

# Skill: google-cloud-sql-basics

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/google/skills](https://github.com/google/skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\google-cloud-sql-basics`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
>-




---

### Documentos & Manuais Inclusos
* 📄 [[attribution]]
* 📄 [[cli-usage]]
* 📄 [[client-library-usage]]
* 📄 [[core-concepts]]
* 📄 [[dr-backups]]
* 📄 [[iac-usage]]
* 📄 [[iam-security]]
* 📄 [[mcp-usage]]


---

## Instruções Principais & Comandos Técnicos


# Cloud SQL Basics

Cloud SQL is a fully managed relational database service for MySQL, PostgreSQL,
and SQL Server. It automates time-consuming tasks like patches, updates,
backups, and replicas, while providing high performance and availability for
your applications.

## Attribution

**MUST READ**: Before executing any `gcloud`, REST API, or MCP command, you
MUST read [Usage Attribution](references/attribution.md). For commands executed
directly in the terminal (never in generated scripts, Terraform, or user code),
prefix `gcloud` with
`CLOUDSDK_METRICS_REQUEST_ATTRIBUTION="agent-skills/1.0 (skill:cloud-sql-basics)"`
and append `agent-skills/1.0 (skill:cloud-sql-basics)` to `User-Agent` headers.

## Prerequisites

Ensure you have the necessary IAM permissions to create and manage Cloud SQL
instances. The **Cloud SQL Admin** (`roles/cloudsql.admin`) role provides full
access to Cloud SQL resources.

## Quick Start (PostgreSQL)

1.  **Enable the API:**
    
    ```bash
    gcloud services enable sqladmin.googleapis.com --quiet
    ```

2.  **Create an Instance:**
    
    ```bash
    gcloud sql instances create INSTANCE_NAME \
      --database-version=POSTGRES_18 \
      --cpu=2 \
      --memory=7680MiB \
      --region=REGION \
      --quiet
    ```

3.  **Set a password for the default user:**

    Because this is a Cloud SQL for PostgreSQL instance, the default admin user
    is `postgres`:
    
    ```bash
    gcloud sql users set-password postgres \
      --instance=INSTANCE_NAME --password=PASSWORD \
      --quiet
    ```

4.  **Create a database:**
    
    ```bash
    gcloud sql databases create DATABASE_NAME \
      --instance=INSTANCE_NAME \
      --quiet
    ```

5.  **Get the instance connection name:**

    You need the instance connection name (which is formatted as
    `PROJECT_ID:REGION:INSTANCE_NAME`) to connect using the Cloud SQL Auth
    Proxy. Retrieve it with the following command:
    
    ```bash
    gcloud sql instances describe INSTANCE_NAME \
      --format="value(connectionName)" \
      --quiet
    ```

6.  **Connect to the instance:**

    The Cloud SQL Auth Proxy must be running to be able to connect to the
    instance. In a separate terminal, start the proxy using the connection name:
    
    ```bash
    ./cloud-sql-proxy INSTANCE_CONNECTION_NAME
    ```

    With the proxy running, connect using `psql` in another terminal:
    
    ```bash
    psql "host=127.0.0.1 port=5432 user=postgres dbname=DATABASE_NAME password=PASSWORD sslmode=disable"
    ```

## Reference Directory

-   [Core Concepts](references/core-concepts.md): Cloud SQL editions (Enterprise
    & Enterprise Plus), instance architecture, read pools, high availability (HA),
    and supported database engines.

-   [CLI Usage](references/cli-usage.md): Essential `gcloud sql` commands for
    instance, database, and user management.

-   [Client Libraries & Connectors](references/client-library-usage.md):
    Connecting to Cloud SQL using Python, Java, Node.js, and Go.

-   [MCP Usage](references/mcp-usage.md): Using the Cloud SQL remote MCP
    server and Gemini CLI extension.

-   [Infrastructure as Code](references/iac-usage.md): Terraform
    configuration for instances, databases, and users.

-   [IAM & Security](references/iam-security.md): Predefined roles, SSL/TLS
    certificates, and Auth Proxy configuration.

-   [Disaster Recovery & Backups](references/dr-backups.md): Backup types,
    Point-in-Time Recovery (PITR), replicas, read pools comparison, and Enterprise Plus Advanced DR.

*If you need product information not found in these references, use the
    Developer Knowledge MCP server `search_documents` tool.*

