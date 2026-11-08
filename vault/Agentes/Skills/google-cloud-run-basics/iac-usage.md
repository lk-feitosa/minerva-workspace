---
tags:
  - ai/skill/doc
  - skill/google-cloud-run-basics
skill: "google-cloud-run-basics"
source: "references\iac-usage.md"
updated_at: "2026-11-08T20:55:34.472Z"
---

# Documento: iac-usage (Skill: google-cloud-run-basics)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-cloud-run-basics]]**.  
> **Caminho de origem:** `references\iac-usage.md`

---

# Cloud Run Infrastructure as Code

Cloud Run resources can be provisioned and managed using Terraform and other IaC
tools.

## Terraform

The Google Cloud Terraform provider supports Cloud Run services, jobs, and worker pools.

### Cloud Run service example

```terraform
resource "google_cloud_run_v2_service" "default" {
  name     = "cloudrun-service"
  location = "us-central1"
  deletion_protection = false
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello"
    }
  }
}

resource "google_cloud_run_v2_service_iam_member" "noauth" {
  location = google_cloud_run_v2_service.default.location
  name     = google_cloud_run_v2_service.default.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
```

### Cloud Run job example

```terraform
resource "google_cloud_run_v2_job" "default" {
  name     = "cloudrun-job"
  location = "us-central1"

  template {
    template {
      containers {
        image = "us-docker.pkg.dev/cloudrun/container/job"
      }
    }
  }
}
```

### Cloud Run worker pool example

```terraform
resource "google_cloud_run_v2_worker_pool" "default" {
  name     = "cloudrun-workerpool"
  location = "us-central1"

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/worker-pool:latest"
    }
  }
}
```

### Reference documentation

- [Terraform Google Provider - Cloud Run v2 Service](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service)

- [Terraform Google Provider - Cloud Run v2 Job](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job)
- [Terraform Google Provider - Cloud Run v2 Worker pool](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_worker_pool)

## YAML

Cloud Run resources can also be defined using YAML. For more information, see
[Cloud Run YAML reference](https://docs.cloud.google.com/run/docs/reference/yaml/v1.md.txt).

