---
title: Autonomous UAV for Nuclear Safety Inspections
description: Engineering Science capstone combining visual SLAM, object detection and RRT* navigation.
img: /legacy/images/drone.jpg
img_alt: Inspection drone from original capstone portfolio
importance: 10
category: Student projects
---

**University of Toronto · Engineering Science capstone · 2023**

We designed an inspection-drone prototype to reduce manual exposure in hazardous environments. My focus was integrating **perception, localization and autonomous navigation**.

## Inspection architecture

![Capstone perception, localization, planning and navigation](/assets/img/diagrams/capstone-pipeline.svg)

- YOLOv5 detection for inspection targets.
- Visual SLAM for navigation state.
- RRT* for waypoint routing and obstacle handling.

## Hardware and simulation

<div class="project-gallery">
<figure><img src="/legacy/images/Hardware.png" alt="Original assembled inspection-drone hardware" loading="lazy"/><figcaption>Original assembled inspection-drone hardware</figcaption></figure>
<figure><img src="/legacy/images/Hardware_2.png" alt="Second hardware configuration" loading="lazy"/><figcaption>Second hardware configuration</figcaption></figure>
<figure><img src="/legacy/images/c3_4.png" alt="Waypoint-navigation experiment" loading="lazy"/><figcaption>Waypoint-navigation experiment</figcaption></figure>
<figure><img src="/legacy/images/c4_2.png" alt="Obstacle-avoidance experiment" loading="lazy"/><figcaption>Obstacle-avoidance experiment</figcaption></figure>
</div>

Watch the original [hover](https://youtu.be/8mcuc0-HUeY), [waypoint](https://youtu.be/pLiu4lUnUiU) and [obstacle](https://youtu.be/VCbzIF69IFw) demonstrations.
