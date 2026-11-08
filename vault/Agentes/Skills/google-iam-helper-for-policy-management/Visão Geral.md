---
tags:
  - ai/skill
  - agent-tooling
name: "google-iam-helper-for-policy-management"
github: "https://github.com/google/skills"
updated_at: "2026-11-08T08:03:33.157Z"
---

# Skill: google-iam-helper-for-policy-management

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [https://github.com/google/skills](https://github.com/google/skills)  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\google-iam-helper-for-policy-management`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
>-




---

### Documentos & Manuais Inclusos
* 📄 [[attribution]]
* 📄 [[v1-allow-policies]]
* 📄 [[v2-deny-policies]]


---

## Instruções Principais & Comandos Técnicos


# IAM Helper for Policy Management

Orchestrates the lifecycle and management of IAM allow and deny policies across
IAM v1 (allow policies) and IAM v2 (deny policies).

## Usage Attribution

**MUST READ**: Before executing any `gcloud`, REST API, or MCP command, you
MUST read and follow the instructions in
[Usage Attribution](references/attribution.md).

--------------------------------------------------------------------------------

## Core Concepts & Paradigms

IAM operates across two policy paradigms:

1.  **IAM v1 (Allow Policies)**: Grants roles to principals (users, service
    accounts, groups, domains) on specific resources. Supports Resource Manager
    resources (organizations, folders, projects) as well as individual resources
    across supported Google Cloud services.
2.  **IAM v2 (Deny Policies)**: Sets explicit organization-, folder-, or
    project-level guardrails that prevent specified principals from using
    designated permissions, regardless of any allow policies granted. Evaluated
    before allow policies.

--------------------------------------------------------------------------------

## Workflow & Decision Tree

When receiving a policy management request, determine whether the operation is
**Read-Only** or **Mutating**, and whether it targets **IAM v1 (Allow
Policies)** or **IAM v2 (Deny Policies)**:

### 1. Read-Only Operations (Autonomous Execution)

Read-only actions include the following:

-   **IAM v1 Allow Policies**: `get-iam-policy` on project/folder/organization,
    or `gcloud iam list-testable-permissions
    //cloudresourcemanager.googleapis.com/projects/PROJECT_ID`.
-   **IAM v2 Deny Policies**: `gcloud iam policies list` or `gcloud iam policies
    get` with `--attachment-point` and `--kind=denypolicies`.

For read-only actions, execute the command autonomously to inspect state, and
present the query results clearly to the user.

### 2. Mutating Operations (Plan & Confirm Protocol)

Mutating operations include the following:

-   **IAM v1 Allow Policies**: `add-iam-policy-binding`,
    `remove-iam-policy-binding`, or `set-iam-policy` across project, folder,
    organization, or resource levels (see
    [references/v1-allow-policies.md](references/v1-allow-policies.md)).
-   **IAM v2 Deny Policies**: `create`, `update`, or `delete` deny policies on
    attachment points
    (`cloudresourcemanager.googleapis.com/projects/PROJECT_ID`,
    `cloudresourcemanager.googleapis.com/folders/FOLDER_ID`, or
    `cloudresourcemanager.googleapis.com/organizations/ORG_ID`) using YAML/JSON
    policy files (see
    [references/v2-deny-policies.md](references/v2-deny-policies.md)).

For mutating operations, follow the **Plan & Confirm Protocol** below. **DO
NOT** execute mutating commands autonomously without prior user approval.

--------------------------------------------------------------------------------

## Execution & Safety Protocol

-   **Plan and Confirm (No Autonomous Mutation)**: Mutating allow and deny
    policy changes modify live security perimeters and access controls. You MUST
    NOT execute mutating `gcloud` commands directly via tool calls without
    explicit prior confirmation from the user. When asked to apply a mutating
    change, do the following:
    1.  **Formulate the Command**: Generate the exact, fully constructed
        `gcloud` command (including all parameters such as `--member`, `--role`,
        `--attachment-point`, `--kind=denypolicies`, and `--policy-file`).
    2.  **Warn of Impact & Propagation**: Issue a general warning that the
        change could impact access in a live environment and takes time to
        propagate across Google Cloud global infrastructure.
    3.  **Request User Confirmation**: Prompt the user for approval before
        applying the changes to the live environment.
-   **Post-Execution Verification**: After the user approves and the mutating
    policy change is executed, run the corresponding verification command (see
    [references/v1-allow-policies.md](references/v1-allow-policies.md) and
    [references/v2-deny-policies.md](references/v2-deny-policies.md) for exact
    verification steps) to verify that the active state matches expectations
    before reporting completion.
-   **Security Guardrail (Public & Blanket Access Refusal)**: Never grant
    `allUsers` or `allAuthenticatedUsers` basic roles (`roles/owner`,
    `roles/editor`, `roles/viewer`, `roles/admin`, `roles/writer`, and
    `roles/reader`) or broad permissions. Explicitly refuse blanket public
    access requests, explain the severe security risks of public project
    ownership/access, and propose scoped, least-privileged role bindings for
    specific authenticated identities instead.

--------------------------------------------------------------------------------

## Supporting Links

-   [IAM Overview](https://cloud.google.com/iam/docs/overview)
-   [IAM Deny Policies](https://cloud.google.com/iam/docs/deny-overview)

