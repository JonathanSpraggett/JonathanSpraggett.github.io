---
title: UTRA RoboSoccer — Software & Autonomy
description: Leading humanoid perception, field localization and match behaviors.
img: /assets/img/portfolio/robocup.webp
img_alt: Humanoid robot used in RoboSoccer
importance: 9
category: Humanoid robotics
---

**Software Team Lead · UTRA RoboSoccer · 2019–2023**

I led a roughly 30-person software team building the perception, localization and behavior stack for autonomous humanoid soccer. The team placed **4th at RoboCup 2023**.

## From camera to action

![Object perception, localization, behavior and motion](/assets/img/diagrams/robocup-pipeline.svg)

- **Vision:** YOLO-based ball, goal and robot detection.
- **Localization:** projected field lines and an unscented Kalman filter.
- **Behavior:** robot and team-level decision logic.

## Original project media

<div class="project-gallery">
<figure><img src="/legacy/images/detect.png" alt="Object detection on a soccer field" loading="lazy"/><figcaption>Object detection on a soccer field</figcaption></figure>
<figure><img src="/legacy/images/field_lines.png" alt="Field-line perception" loading="lazy"/><figcaption>Field-line perception</figcaption></figure>
<figure><img src="/legacy/images/bez_kick.png" alt="Humanoid kicking experiments" loading="lazy"/><figcaption>Humanoid kicking experiments</figcaption></figure>
<figure><img src="/legacy/images/bez_walk.png" alt="Humanoid walking experiments" loading="lazy"/><figcaption>Humanoid walking experiments</figcaption></figure>
</div>

Technical details: [field-line detection](/projects/legacy-5-robosoccer-fieldline/) · [UKF localization](/projects/legacy-3-robosoccer-ukf/).
