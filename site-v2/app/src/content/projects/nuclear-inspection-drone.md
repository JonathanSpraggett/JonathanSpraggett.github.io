---
title: Autonomous UAV for Nuclear Safety Inspections
description: University of Toronto capstone combining object detection, visual SLAM and collision-free motion planning.
img: /legacy/images/drone.jpg
img_alt: Nuclear inspection drone from original engineering portfolio
importance: 10
category: Student projects
---

**University of Toronto Engineering Science capstone · 2023**  
**Supervisor:** Prof. Jonathan Kelly · **Focus:** ROS-based autonomy, computer vision, SLAM and motion planning

## The problem we designed for

Inspecting instruments in potentially hazardous industrial areas can expose people to unnecessary risk. Our capstone explored an autonomous UAV that could navigate an inspection environment, recognize relevant visual information, and travel between requested locations without manual piloting at every step.

I worked on the autonomy architecture connecting perception, localization and waypoint-level planning. The project was a student engineering prototype, not a claim of production nuclear-site deployment.

## Hardware and flight platform

The first challenge was integrating a physical quadrotor with the compute, sensing and control components needed for autonomous experiments.

![Assembled inspection drone and onboard hardware](/legacy/images/Hardware.png)

*Original capstone hardware photograph, retained from my previous portfolio.*

![Second view of the assembled inspection platform](/legacy/images/Hardware_2.png)

## Perception and localization

The vision system used **YOLOv5** to detect instruments and relevant objects. Visual SLAM provided localization information that could be consumed by the navigation stack. In an inspection task, these functions have to cooperate: a detected object is useful only if its location and the vehicle's pose are sufficiently well understood.

## Planning and navigation

We used **RRT*** for obstacle-aware route generation, with waypoint navigation translating the planned path into drone motion.

### Progression through the capstone challenges

The legacy portfolio documents incremental evaluations rather than only a final demonstration:

1. **Stable hover:** establish a controlled platform before enabling higher-level navigation.
2. **Waypoint navigation:** follow planned targets in a repeatable environment.
3. **Navigation with obstacles:** evaluate the planner when a direct route is unavailable.

![Waypoint planning experiment from the capstone](/legacy/images/c3_4.png)

*Waypoint-navigation visualization from the original capstone report.*

![Obstacle-avoidance planning experiment](/legacy/images/c4_2.png)

*Obstacle-avoidance results preserved from the original website.*

### Demonstration videos

[Stable hover](https://www.youtube.com/watch?v=8mcuc0-HUeY) · [Waypoint navigation](https://www.youtube.com/watch?v=pLiu4lUnUiU) · [Obstacle navigation](https://www.youtube.com/watch?v=VCbzIF69IFw) · [Project demonstration](https://www.youtube.com/watch?v=Ou9ef7QbNfE)

## What carried forward

The capstone shaped how I now separate **mapping, geometric planning, motion execution and validation** in a larger autonomous flight stack. For the industrial-scale application of these ideas, see [planning and constrained MPC](/projects/motion-planning-mpc/).
