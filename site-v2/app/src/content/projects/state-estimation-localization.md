---
title: Multi-Sensor State Estimation
description: Fusing asynchronous cameras, positioning sensors and ranging data for reliable navigation.
img: /assets/img/portfolio/estimation.webp
img_alt: Flight localization and sensor-fusion traces
importance: 3
category: Aerial robotics
---

**Mostavio · ROS 2 · EKF · Stereo VO · GNSS/RTK · UWB · LiDAR**

A planning algorithm can only be as reliable as the state estimate it receives. My estimation work focuses on **coordinate frames, sensor timing, covariance and failure handling**.

## Fusion pipeline

![Sensor fusion pipeline with frames and timestamp alignment](/assets/img/diagrams/estimation-pipeline.svg)

- Align measurements in space and time.
- Fuse complementary observations through an EKF.
- Reject inconsistent data and monitor filter innovations.
- Publish state estimates for guidance and flight control.

## Foundations from RoboSoccer

<div class="project-gallery">
<figure><img src="/legacy/images/point_to_line_filter.png" alt="Field-point correspondence for visual localization" loading="lazy"/><figcaption>Field-point correspondence for visual localization</figcaption></figure>
<figure><img src="/legacy/images/ukf.png" alt="Legacy UKF localization results" loading="lazy"/><figcaption>Legacy UKF localization results</figcaption></figure>
</div>

The same ideas—geometry, uncertainty and observable failures—connect my [earlier humanoid UKF](/projects/legacy-3-robosoccer-ukf/) to modern aerial sensor fusion.
