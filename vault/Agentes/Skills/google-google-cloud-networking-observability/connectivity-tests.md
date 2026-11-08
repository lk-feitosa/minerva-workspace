---
tags:
  - ai/skill/doc
  - skill/google-google-cloud-networking-observability
skill: "google-google-cloud-networking-observability"
source: "references\connectivity-tests.md"
updated_at: "2026-11-08T06:43:45.528Z"
---

# Documento: connectivity-tests (Skill: google-google-cloud-networking-observability)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-google-cloud-networking-observability]]**.  
> **Caminho de origem:** `references\connectivity-tests.md`

---

# Connectivity Tests Reference

## Connectivity Tests (Path Diagnostics)

Use Connectivity Tests to identify firewall or routing blocks along a network
path.

### Critical Verification: Instance State

**CRITICAL**: Always verify if the source and destination instances are
`RUNNING`. A `REACHABLE` path analysis result (which is a static configuration
analysis) does not mean traffic will flow if the VM is powered off.

-   Check the `status` field in the instance details.
-   Review step metadata in the connectivity test traces.

**CRITICAL**: You MUST execute the delete command as your final tool call before
providing the result to the user. Do not simply state that it was deleted;
provide the command output as proof.

### Tooling

-   **Primary**: [NetworkManagement MCP](mcp-usage.md#networkmanagement-mcp)
    (`create_connectivity_test`)
-   **Polling**: [NetworkManagement MCP](mcp-usage.md#networkmanagement-mcp)
    (`get_connectivity_test`)
-   **Cleanup**: ALWAYS delete the test resource after use with
    [NetworkManagement MCP](mcp-usage.md#networkmanagement-mcp)
    (`delete_connectivity_test`).

#### Fallback: gcloud

-   **Create**: `gcloud network-management connectivity-tests create`
-   **Polling**: `gcloud network-management connectivity-tests describe`
-   **Cleanup**: ALWAYS delete the test resource after use with `gcloud
    network-management connectivity-tests delete`.

