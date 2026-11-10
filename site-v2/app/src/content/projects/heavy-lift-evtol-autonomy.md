---
title: Heavy-Lift eVTOL — Full-Stack Autonomy
description: Autonomy architecture, planning, localization, control integration, simulation, and flight testing
  on a large coaxial aircraft.
img: /assets/img/portfolio/aircraft.webp
img_alt: Mostavio heavy-lift coaxial eVTOL on a test platform
importance: 1
category: Aerial robotics
related_publications:
- spraggett2026digitalfilter
---

**Role:** Robotics Software Engineer, Mostavio · May 2023–present  
**Systems:** ROS 2, C++, Python, PX4, Gazebo SITL/HITL, NVIDIA Jetson

## The challenge

Autonomous operation on a large, coaxial electric aircraft is not simply a scaled-up quadcopter problem. Navigation and planning modules must handle asynchronous sensor data, limited flight envelopes, changing conditions, safety interventions, and a physical platform that cannot be reset like a simulation. I lead the autonomy-software effort that connects high-level mission goals to the components that keep the aircraft operating predictably.

## Architecture: from mission to flight action

The autonomy stack separates **mission decisions**, **flight-action execution**, **planning and localization**, and **aircraft-level stabilization**. A modular behavior-tree mission layer coordinates takeoff, navigation, landing and recovery behaviors. Flight-action interfaces translate these decisions into references for the lower-level PX4 system.

That separation matters during failures: a degraded localization source or an aborted mission should change the mission state and permitted actions without entangling the guidance algorithm with the entire safety architecture.

## Planning, perception and estimation

The navigation stack combines a kinodynamic 3D RRT* planner, smooth minimum-snap trajectory generation, a constrained model predictive controller, and 3D obstacle mapping using NVIDIA nvblox. Separately, an EKF-based estimation pipeline combines stereo visual odometry with GNSS/RTK, UWB and LiDAR where available.

These modules need explicit frame conventions, time alignment, trajectory feasibility checks, and interfaces that make their status observable to the mission manager.

![Simulation model of the coaxial aircraft](/assets/img/portfolio/gazebo-aircraft.webp)

*Aircraft simulation used to develop and exercise autonomy interfaces before hardware trials.*

## Flight testing is part of software development

My work spans simulation and the flight-test environment. The supplied CV documents **more than 1,500 subscale flights and 100 full-scale flight tests**, including stabilization, mission integration and performance validation. I built telemetry collection, custom flight-data analysis, and a flight-deck interface for monitoring, commanding and carrying out preflight checks.

![Aircraft during indoor test preparations](/assets/img/portfolio/flight-test.webp)

*Physical test aircraft. Software changes are assessed against real telemetry rather than simulation alone.*

## Validation infrastructure

Gazebo-based software-in-the-loop and hardware-in-the-loop environments support iterative testing against a representative propulsion and vehicle model. Docker deployment and automated regression pipelines help keep the same autonomy components usable between development, simulation and field work.

The aircraft also supports [published research on vibration mitigation and flight-control stability](/projects/flight-testing-filtering/). For a closer look at individual subsystems, see [planning and MPC](/projects/motion-planning-mpc/), [state estimation](/projects/state-estimation-localization/) and [flight validation](/projects/flight-testing-filtering/).

**Related publication:** [AIAA SciTech 2026 paper (PDF)](/assets/pdf/aiaa2026_fft.pdf).
