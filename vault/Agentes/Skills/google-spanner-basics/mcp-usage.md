---
tags:
  - ai/skill/doc
  - skill/google-spanner-basics
skill: "google-spanner-basics"
source: "references\mcp-usage.md"
updated_at: "2026-11-08T06:43:45.690Z"
---

# Documento: mcp-usage (Skill: google-spanner-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-spanner-basics]]**.  
> **Caminho de origem:** `references\mcp-usage.md`

---

# MCP Usage

Spanner supports Model Context Protocol (MCP) to connect your database to LLM
agents.

## Connecting to MCP Server

You can use pre-built tools provided by Spanner to connect your IDE or
application to Spanner using MCP.

For detailed instructions, see the official documentation:
[Connect your IDE to Spanner using MCP](https://docs.cloud.google.com/spanner/docs/use-spanner-mcp.md.txt)

## MCP Tools for Spanner

The Spanner MCP server exposes the following tools to LLM agents:

- `get_instance`: Get information about a specific Spanner instance.
- `list_instances`: List all Spanner instances in a given project.
- `list_configs`: List instance configurations available in a project.
- `get_config`: Get information about a specific instance configuration.
- `create_instance`: Create a new Spanner instance.
- `update_instance`: Update a Spanner instance.
- `create_database`: Create a database in a given instance.
- `get_database_ddl`: Retrieve the database schema (DDL).
- `list_databases`: List all databases in a given instance.
- `create_session`: Create a session in a database for query execution.
- `execute_sql`: Execute a SQL statement (both DQL and DML supported).
- `execute_sql_readonly`: Execute a SQL query statement in a single-use read-only transaction.
- `commit`: Commit a transaction.
- `update_database_schema`: Update the schema for a given database.
- `get_operation`: Get the status of a long-running operation.

For more details, see the [Spanner MCP reference](https://docs.cloud.google.com/spanner/docs/reference/mcp.md.txt).

