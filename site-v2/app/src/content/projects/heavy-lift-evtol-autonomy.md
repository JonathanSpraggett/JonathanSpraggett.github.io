---
title: Heavy-Lift eVTOL — Full-Stack Autonomy
description: Planning, estimation, mission execution and flight validation on a full-scale coaxial aircraft.
img: /assets/img/portfolio/aircraft.webp
img_alt: Mostavio heavy-lift aircraft on the test stand
importance: 1
category: Aerial robotics
related_publications:
- spraggett2026digitalfilter
---

**Mostavio · Robotics Software Engineer · 2023–present**  
ROS 2 · C++ · Python · PX4 · Gazebo · Jetson

I lead the autonomy integration for a heavy-lift eVTOL. The challenge is making planning, sensing and safety work together on an aircraft where every real-world test matters.

## System architecture

![Mission, planning, guidance and PX4 data flow](/assets/img/diagrams/evtol-architecture.svg)

- **Mission execution:** behaviors, safety gating and recovery.
- **Navigation:** 3D RRT*, trajectory optimization and constrained guidance.
- **Estimation:** stereo VO, GNSS/RTK, UWB and LiDAR fusion.
- **Flight testing:** custom flight-deck software, telemetry and post-flight analysis.

## From simulation to aircraft

<div class="project-gallery">
<figure><img src="/assets/img/portfolio/flight-test.webp" alt="Full-scale aircraft during flight testing" loading="lazy"/><figcaption>Full-scale aircraft during flight testing</figcaption></figure>
<figure><img src="/assets/img/portfolio/gazebo-aircraft.webp" alt="Aircraft model for SITL/HITL validation" loading="lazy"/><figcaption>Aircraft model for SITL/HITL validation</figcaption></figure>
<figure><img src="/legacy/images/mostavio.jpeg" alt="Aircraft photograph retained from the original portfolio" loading="lazy"/><figcaption>Aircraft photograph retained from the original portfolio</figcaption></figure>
</div>

**Validation:** More than 1,500 subscale flights and 100 full-scale tests documented in my CV.

Related work: [planning & MPC](/projects/motion-planning-mpc/) · [estimation](/projects/state-estimation-localization/) · [flight-tested filtering](/projects/flight-testing-filtering/).
