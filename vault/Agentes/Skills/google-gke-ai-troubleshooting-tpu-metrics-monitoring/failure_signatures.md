---
tags:
  - ai/skill/doc
  - skill/google-gke-ai-troubleshooting-tpu-metrics-monitoring
skill: "google-gke-ai-troubleshooting-tpu-metrics-monitoring"
source: "references\failure_signatures.md"
updated_at: "2026-11-08T06:43:45.406Z"
---

# Documento: failure_signatures (Skill: google-gke-ai-troubleshooting-tpu-metrics-monitoring)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-gke-ai-troubleshooting-tpu-metrics-monitoring]]**.  
> **Caminho de origem:** `references\failure_signatures.md`

---

# GKE TPU Metrics Signatures

This document describes key metric signatures and what they indicate for GKE TPU workloads.

## 1. Node Unready Signature

- **Metric**: `kubernetes.io/node/status_condition`
- **Signature**: `condition="Ready"`, `status="False"` (or `status="Unknown"`)
- **Meaning**: The GKE node hosting the TPU is not healthy. Workloads on this node will be disrupted.

## 2. Node Pool Error Signature

- **Metric**: `kubernetes.io/node_pool/status`
- **Signature**: `status="Error"`
- **Meaning**: The multi-host TPU node pool has encountered an error (e.g., provisioning failure).

## 3. Node Preemption Signature

- **Metric**: `kubernetes.io/node/interruption_count`
- **Signature**: `interruption_type="PreemptionEvent"`
- **Meaning**: The node was preempted (common for Spot VMs). Workload needs to be rescheduled.

## 4. Host Error Signature

- **Metric**: `kubernetes.io/node/interruption_count`
- **Signature**: `interruption_type="TerminationEvent"`, `interruption_reason="HostError"`
- **Meaning**: The underlying physical host encountered a hardware error. GKE should trigger AutoRepair.

## 5. Low TPU Utilization Signature

- **Metric**: `kubernetes.io/container/accelerator/duty_cycle` or `kubernetes.io/container/accelerator/tensorcore_utilization`
- **Signature**: Value `< 0.2` (20%) during active training.
- **Meaning**: The TPU is heavily underutilized, likely due to data bottleneck or small batch size.

