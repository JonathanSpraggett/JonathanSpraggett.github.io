---
title: Multi-Sensor State Estimation
description: EKF fusion of stereo visual odometry, GNSS/RTK, UWB and LiDAR for resilient state estimation.
img: /assets/img/portfolio/estimation.webp
img_alt: State estimation plots from multiple sensors
importance: 3
category: Aerial robotics
---

**Role:** State estimation and sensor-fusion software, Mostavio  
**Sensors:** Stereo visual odometry, GNSS/RTK, UWB, IMU and LiDAR  
**Core methods:** Extended Kalman filtering, coordinate transforms, innovation gating

## Why no single sensor is enough

Autonomous flight requires a consistent estimate of position, velocity and orientation, but the available sensors disagree about how to describe the world. GNSS provides an absolute reference that can degrade, cameras provide relative motion that can drift, and local ranging systems have different coverage and uncertainty characteristics.

I built a ROS 2 estimation pipeline that combines these sources rather than allowing any single sensor to dictate the entire vehicle state.

## Data flow

1. Convert measurements into well-defined reference frames and check timestamps.
2. Track each sensor's uncertainty and expected update rate.
3. Fuse complementary observations through an **EKF-based estimator**.
4. Evaluate innovations and reject inconsistent observations before they destabilize the solution.
5. Publish a state estimate usable by both motion planning and flight control.

The nontrivial work happens at subsystem boundaries: delays between camera processing and control, inconsistent yaw conventions, partial sensor outages, covariance tuning and changes between GNSS-available and degraded environments.

## How I investigate performance

I use synchronized logs, residual traces and trajectory comparisons to determine whether an apparent tracking failure begins in the estimator or in the controller receiving its output. Comparing estimators requires care: a visually smooth trajectory is not necessarily accurate, and uncertainty should grow rather than remain artificially confident when measurements disappear.

## Earlier foundation: humanoid field-line localization

Before the eVTOL stack, I developed **field-line-based visual localization and an unscented Kalman filter** for humanoid RoboSoccer. That pipeline projected camera detections onto the ground plane, matched them to a known field map, and combined the result with odometry. It is a distinct application, but the same lessons about frame consistency, uncertainty and measurement quality carry through.

![Field-line matching geometry from the RoboSoccer localization project](/legacy/images/point_to_line_filter.png)

*Archived project figure: matching perceived field-line points against geometric constraints.*

The original technical write-up includes [the RoboSoccer UKF design and its observations](/projects/legacy-3-robosoccer-ukf/) and [field-line detection pipeline](/projects/legacy-5-robosoccer-fieldline/).
