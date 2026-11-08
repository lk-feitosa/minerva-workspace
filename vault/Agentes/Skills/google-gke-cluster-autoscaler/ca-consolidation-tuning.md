---
tags:
  - ai/skill/doc
  - skill/google-gke-cluster-autoscaler
skill: "google-gke-cluster-autoscaler"
source: "references\ca-consolidation-tuning.md"
updated_at: "2026-11-08T20:55:34.925Z"
---

# Documento: ca-consolidation-tuning (Skill: google-gke-cluster-autoscaler)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-gke-cluster-autoscaler]]**.  
> **Caminho de origem:** `references\ca-consolidation-tuning.md`

---

# Cluster Autoscaler: Consolidation Tuning

## `autoscalingPolicy` (ComputeClass)
Overrides cluster-wide profile defaults for class-managed nodes.
```yaml
spec:
  autoscalingPolicy:
    consolidationDelayMinutes: 5     # Floor = 1 min
    consolidationThreshold: 0        # % CPU util (0 = always candidate)
    gpuConsolidationThreshold: 0     # Accelerator counterpart
```

## Tuning by Workload
- **Serving:** 5–15 min delay; default threshold. Prevents "thrashing" on traffic spikes.
- **Batch:** 1–2 min delay; `0` threshold. Aggressive cost recovery.
- **Stateful:** 10+ min delay. Pair with PDBs to control churn.

## Disruption Constraints
Consolidation respects:
- **PodDisruptionBudgets (PDB):** Node is skipped if eviction breaches `maxUnavailable`.
- **`safe-to-evict: "false"`:** Annotation pins the node indefinitely.

*Note:* Maintenance windows do **NOT** block consolidation. Use PDBs for time-windowed suppression.

