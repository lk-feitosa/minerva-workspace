---
tags:
  - ai/skill/doc
  - skill/google-ima-sdk-client-side
skill: "google-ima-sdk-client-side"
source: "references\ima-sdk-web-mobile-safari.md"
updated_at: "2026-11-08T08:03:33.189Z"
---

# Documento: ima-sdk-web-mobile-safari (Skill: google-ima-sdk-client-side)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-ima-sdk-client-side]]**.  
> **Caminho de origem:** `references\ima-sdk-web-mobile-safari.md`

---

# Google IMA HTML5 SDK on Mobile Safari (iOS) guide

This guide covers best practices for the Google Interactive Media Ads (IMA)
HTML5 SDK to support mobile Safari (iOS).

## Essential setup

You must do the following steps:

*   Check and make sure that the `playsinline` attribute is added for the HTML
    `<video>` element.

*   Add a play button to initiate playback by user gesture.

Example:

```html
<!-- This video will attempt to play within its layout on iOS -->
<video playsinline controls></video>
```
