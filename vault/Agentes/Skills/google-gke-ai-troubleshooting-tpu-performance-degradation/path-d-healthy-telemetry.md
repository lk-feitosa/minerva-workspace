---
tags:
  - ai/skill/doc
  - skill/google-gke-ai-troubleshooting-tpu-performance-degradation
skill: "google-gke-ai-troubleshooting-tpu-performance-degradation"
source: "references\path-d-healthy-telemetry.md"
updated_at: "2026-11-08T08:03:32.689Z"
---

# Documento: path-d-healthy-telemetry (Skill: google-gke-ai-troubleshooting-tpu-performance-degradation)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-gke-ai-troubleshooting-tpu-performance-degradation]]**.  
> **Caminho de origem:** `references\path-d-healthy-telemetry.md`

---

# Path D: Healthy telemetry (rule out performance degradation) `[Low Risk]`

If there are no `PERFORMANCE_DEGRADATION` events in the window, TPU duty cycle
shows no drop of 15% or more, and HBM and host memory aren't close to their
limits, rule out TPU performance degradation. Tell the user that no remediation
is needed.

