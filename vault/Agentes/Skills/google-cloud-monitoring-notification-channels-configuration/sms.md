---
tags:
  - ai/skill/doc
  - skill/google-cloud-monitoring-notification-channels-configuration
skill: "google-cloud-monitoring-notification-channels-configuration"
source: "references\sms.md"
updated_at: "2026-11-08T20:55:34.436Z"
---

# Documento: sms (Skill: google-cloud-monitoring-notification-channels-configuration)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-cloud-monitoring-notification-channels-configuration]]**.  
> **Caminho de origem:** `references\sms.md`

---

# SMS Notification Channels

## Prerequisites

### Target Phone Number

SMS notification channels require a phone number to send alert notifications to.
If it has not been provided already, you MUST prompt the user to ask which phone
number you need to use to configure the notification channel.

## Specification

### Terraform HCL

```terraform
resource "google_monitoring_notification_channel" "sms_notification_channel" {
  project      = {gcp_project}
  display_name = "SMS Notification Channel ({target_phone_number})"
  type         = "sms"
  labels = {
    number = {target_phone_number}
  }
  user_labels = {
    created-with-google-skill = "cloud-monitoring-notification-channels-configuration"
  }
}
```

Where:

*   `{gcp_project}`: The GCP project ID to deploy the notification channel to.
*   `{target_phone_number}`: The target phone number to send notifications to
    through the channel.

