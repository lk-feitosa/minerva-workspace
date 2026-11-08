---
tags:
  - ai/skill/doc
  - skill/google-gke-manifest-generation
skill: "google-gke-manifest-generation"
source: "references\network-policy.md"
updated_at: "2026-11-08T08:03:32.773Z"
---

# Documento: network-policy (Skill: google-gke-manifest-generation)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-gke-manifest-generation]]**.  
> **Caminho de origem:** `references\network-policy.md`

---

# Network Policy Example

This reference example demonstrates configuring Kubernetes `NetworkPolicy`
resources on GKE.

It includes:

-   Default-deny ingress NetworkPolicy to isolate pods in the namespace
-   Targeted ingress NetworkPolicy allowing traffic strictly from specific pods

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: nginx-ingress-deny-all
  namespace: nginx-ns
spec:
  podSelector:
    matchLabels:
      app.kubernetes.io/name: nginx
  policyTypes:
    - Ingress
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-ingress-from-my-app
  namespace: nginx-ns
spec:
  podSelector:
    matchLabels:
      app.kubernetes.io/name: nginx
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app.kubernetes.io/name: my-app
      ports:
        - protocol: TCP
          port: 8080
```

