---
tags:
  - ai/skill/doc
  - skill/google-gke-manifest-generation
skill: "google-gke-manifest-generation"
source: "references\gateway-api.md"
updated_at: "2026-11-08T20:55:34.978Z"
---

# Documento: gateway-api (Skill: google-gke-manifest-generation)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-gke-manifest-generation]]**.  
> **Caminho de origem:** `references\gateway-api.md`

---

# GKE Gateway API Routing Example

This reference example demonstrates exposing workloads via the GKE Gateway API
(L7 Internal HTTP Load Balancer).

It includes:

-   `Gateway` resource with `gatewayClassName: gke-l7-rilb`
-   `HTTPRoute` resource referencing the backend Service

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: internal-http-gateway
  namespace: nginx-ns
spec:
  gatewayClassName: gke-l7-rilb
  listeners:
    - name: http
      protocol: HTTP
      port: 80
      allowedRoutes:
        namespaces:
          from: Same
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: nginx-http-route
  namespace: nginx-ns
spec:
  parentRefs:
    - name: internal-http-gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: nginx-service
          port: 80
```

