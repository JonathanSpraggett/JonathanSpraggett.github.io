---
title: Skyguard — Autonomous Security Drone
description: Target detection, tracking, geolocation and reusable mission behaviors.
img: /assets/img/portfolio/aerial-perception.webp
img_alt: Aerial camera perception view
importance: 6
category: Applied autonomy
---

**Mostavio / Skyguard · ROS 2 · RF-DETR · Tracking · Camera geometry**

A detection is useful only if the aircraft can **track it, locate it and decide what to do**.

## Perception to action

![Object detection, tracking, geolocation and mission actions](/assets/img/diagrams/security-pipeline.svg)

- **Perception:** object detection and persistent target tracking.
- **Geolocation:** pixel-to-world geometry using camera and vehicle state.
- **Behaviors:** patrol, watch, investigate, follow and recovery.
- **Safety:** account for uncertainty and missing observations before acting.

## Operational viewpoint

<div class="project-gallery">
<figure><img src="/assets/img/portfolio/site-security.webp" alt="Aerial monitoring scene from the portfolio" loading="lazy"/><figcaption>Aerial monitoring scene from the portfolio</figcaption></figure>
</div>

This overview shows software architecture without releasing customer-specific site data.
