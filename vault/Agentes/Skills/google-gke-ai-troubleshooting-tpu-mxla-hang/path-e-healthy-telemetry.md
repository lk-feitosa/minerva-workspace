---
tags:
  - ai/skill/doc
  - skill/google-gke-ai-troubleshooting-tpu-mxla-hang
skill: "google-gke-ai-troubleshooting-tpu-mxla-hang"
source: "references\path-e-healthy-telemetry.md"
updated_at: "2026-11-08T20:55:34.864Z"
---

# Documento: path-e-healthy-telemetry (Skill: google-gke-ai-troubleshooting-tpu-mxla-hang)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-gke-ai-troubleshooting-tpu-mxla-hang]]**.  
> **Caminho de origem:** `references\path-e-healthy-telemetry.md`

---

# Path E: Healthy telemetry (rule out an MXLA hang) `[Low Risk]`

If there are no `HANG_DETECTED` logs or hang monitored events in the window, and
the multi-slice latencies and TPU duty cycle are steady, rule out an MXLA hang.
Tell the user that no remediation is needed.

