---
tags:
  - ai/skill/doc
  - skill/google-google-cloud-solution-agentic-analytics-spark-knowledge-catalog
skill: "google-google-cloud-solution-agentic-analytics-spark-knowledge-catalog"
source: "references\product-selection-guidance.md"
updated_at: "2026-11-08T06:43:45.561Z"
---

# Documento: product-selection-guidance (Skill: google-google-cloud-solution-agentic-analytics-spark-knowledge-catalog)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-google-cloud-solution-agentic-analytics-spark-knowledge-catalog]]**.  
> **Caminho de origem:** `references\product-selection-guidance.md`

---

# Product selection guide

Use the guidance in this file to recommend products and features for a governed,
secure pipeline for agentic analytics solution across structured and
unstructured data that's distributed across Google Cloud, on-premises systems,
and other cloud providers.

**Note**: When generating solution designs, architecture diagrams, and
documentation, use the latest Google Cloud product names, as listed in the
following table:

|Old name|New name|
|---| ---|
|BigLake|Lakehouse for Apache Iceberg|
|Dataproc Serverless|Managed Service for Apache Spark|
|Dataplex|Knowledge Catalog|

The underlying APIs, gcloud commands, Terraform resources, and IAM roles often
retain the old names.

**Important**:
*   Don't recommend any products that are deprecated, retired, decommissioned,
    or unsupported. Verify the status of the products by using the resources
    that are listed in the "Ground all generated content" section in
    `../SKILL.md`.
*   Don't recommend any features that are deprecated, retired, decommissioned,
    or unsupported. Verify the status of the features by using the resources
    that are listed in the "Ground all generated content" section in
    `../SKILL.md`.
*   If multiple products or features can be used for a component of the
    workload, then do the following:
    *   Recommend the most appropriate product or feature. When alternative
        products exist, the relevant product documentation might provide
        guidance on when to recommend each product. Follow that guidance.
    *   Mention the available alternative products or features.
    *   Explain the pros and cons of each alternative product or feature.

## Product recommendations

*   **Central metadata and data governance**
    *   **Recommended product**: Knowledge Catalog (to capture business
        glossaries, columns descriptions, and custom metadata aspect types)
        integrated with Lakehouse for Apache Iceberg
*   **Processing engine**
    *   **Recommended product**: Managed Service for Apache Spark with Lightning
        Engine (configured with Iceberg REST Catalog)
    *   **Alternative product**: BigQuery
        *   **Pros**: Easy to write standard SQL queries directly over external
            BigLake tables.
*   **Raw data storage**
    *   **Recommended product**: Cloud Storage
    *   **Alternative product**: BigQuery
        *   **Cons**: Not designed for raw blob storage of unstructured files
            like PDFs.
*   **Connectivity to external data sources**
    *   **Recommended products**:
        *   **For cross-cloud connectivity:** Cross-Cloud Interconnect
        *   **For on-premises to cloud connectivity:** Cloud Interconnect
*   **Operational data storage**
    *   **Recommended product**: AlloyDB for PostgreSQL
        *   **Pros**: Supports column-cache vector acceleration for fast joins,
            which is ideal for real-time operational query acceleration.
    *   **Alternative product**: Cloud SQL for PostgreSQL
        *   **Pros**: Highly cost-effective for simpler, smaller relational
            workloads.
        *   **Cons**: Lacks advanced column-cache vector acceleration (AlloyDB
            columnar engine) for fast joins.
*   **User and agentic interactions**:
    *   **Recommended product**: Antigravity IDE or VS Code with the Google
        Cloud Data Agent Kit (provides IDE grounding)

