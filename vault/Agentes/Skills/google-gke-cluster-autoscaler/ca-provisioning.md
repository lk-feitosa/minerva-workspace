---
tags:
  - ai/skill/doc
  - skill/google-gke-cluster-autoscaler
skill: "google-gke-cluster-autoscaler"
source: "references\ca-provisioning.md"
updated_at: "2026-11-08T08:03:32.730Z"
---

# Documento: ca-provisioning (Skill: google-gke-cluster-autoscaler)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-gke-cluster-autoscaler]]**.  
> **Caminho de origem:** `references\ca-provisioning.md`

---

# Cluster Autoscaler: Provisioning & Strategies

## Enabling Scaling (Standard)

### cluster autoscaler - Per Pool

- **Enable (New Pool):**
  ```bash
  gcloud container node-pools create <POOL> \
    --enable-autoscaling --min-nodes=1 --max-nodes=10
  ```
- **Enable (Existing Pool):**
  ```bash
  gcloud container clusters update <CLUSTER> \
    --enable-autoscaling --node-pool=<POOL> \
    --min-nodes=1 --max-nodes=10
  ```

### Node Auto Provisioning - Cluster-wide

- **Enable:**
  ```bash
  gcloud container clusters update <CLUSTER> \
    --enable-autoprovisioning \
    --min-cpu=4 --max-cpu=200 \
    --min-memory=16 --max-memory=800
  ```

### Node pool auto-creation - Per ComputeClass

- **Enable:** Set `nodePoolAutoCreation.enabled: true` in the ComputeClass.
- **GKE 1.33.3+:** Works without cluster-wide Node Auto Provisioning enabled.

## Provisioning Strategies

| Strategy | Strengths | Use Case |
|----------|-----------|----------|
| **Manual Pools** | Fast scheduling; Stable names. | Latency-sensitive; manual management. |
| **node pool auto-creation (ComputeClass)** | Best obtainability; Scale-to-zero. | Bursty; batch; cost-sensitive. |
| **Hybrid** | Manual pool at top; node pool auto-creation fallback. | **Recommended for Production.** |

## Cutover: Node Auto Provisioning to node pool auto-creation
1. **Apply ComputeClasses:** Create classes with `nodePoolAutoCreation.enabled: true`.
2. **Opt Workloads In:** Apply `nodeSelector: cloud.google.com/compute-class: <name>`.
3. **Drain Old Pools:** `kubectl drain` nodes in old Node Auto Provisioning-managed pools.

## Scale-to-Zero Behavior
- **Manual Pools:** Standard cluster autoscaler keeps ≥1 node unless empty pool deletion is supported/enabled.
- **node pool auto-creation-managed:** Autoscaler can delete the entire pool when empty.

