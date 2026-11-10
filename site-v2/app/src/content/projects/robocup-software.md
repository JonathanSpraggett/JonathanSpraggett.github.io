---
title: RoboCup Humanoid Soccer — Software Leadership
description: Led a 30-member humanoid soccer software team, combining vision, localization and robot behaviors.
img: /assets/img/portfolio/robocup.webp
img_alt: Humanoid soccer robot with a ball at an event
importance: 9
category: Humanoid robotics
---

**Organization:** UTRA RoboSoccer · University of Toronto Robotics Association  
**Software Team Lead:** 2019–2023 · **Result:** 4th place worldwide, RoboCup 2023

## Building a complete autonomous soccer robot

A humanoid soccer robot must recognize a ball, estimate where it is on the field, decide which behavior to execute, and recover when a movement or perception estimate fails. I led a **30-person robotics software team** developing those capabilities on real humanoid platforms.

The interesting work happened at the interfaces between modules. Good detection without localization did not produce useful navigation; reliable locomotion without decisions did not produce a useful teammate.

## 1. Vision and object localization

We developed real-time object perception for soccer balls, opponents, goalposts and field landmarks. The legacy stack used YOLOv5, while later embedded vision work included model optimization and newer detector architectures.

![Ball, robots and goals detected by the legacy vision pipeline](/legacy/images/detect.png)

*YOLO object-detection output from the earlier ROS vision pipeline.*

[Watch the object-detection demonstration](https://youtu.be/pjOoMTzA_8E).

## 2. Field geometry and state estimation

Vision also provides a map-relative cue. We extracted white field-line regions, projected detections from camera pixels onto the ground plane, and compared them against known field geometry. The resulting visual localization measurements were combined with odometry in an **unscented Kalman filter (UKF)**.

![Field lines segmented from the robot's camera](/legacy/images/field_lines.png)

*Field-line extraction is designed to retain the observed line region, not just its centerline.*

![UKF localization results from the original RoboSoccer portfolio](/legacy/images/ukf.png)

*Archived trajectory and estimation results from the RoboSoccer project.*

Read the dedicated [field-line processing](/projects/legacy-5-robosoccer-fieldline/) and [UKF localization](/projects/legacy-3-robosoccer-ukf/) breakdowns for more of the original algorithms and diagrams.

## 3. Autonomy and multi-robot behavior

The robots needed a hierarchy of decisions: game state, player role, local action and recovery. We developed finite-state and hierarchical task-planning approaches to coordinate robot behaviors, with experiments in constrained multi-agent task assignment.

## 4. Testing on physical humanoids

Qualification, simulation and field tests were essential for identifying failure modes that a static perception benchmark cannot capture.

[Watch the RoboCup qualification video](https://youtu.be/bINm34lQ1Jg)

## From RoboCup to research

The physical humanoid platform also motivated my later work on reinforcement learning for soccer skills and cross-morphology fall recovery.

Related: [Sim2Real humanoid soccer skills](/projects/sim2real-soccer/) · [Zero-shot humanoid recovery](/projects/humanoid-zero-shot-getup/).
