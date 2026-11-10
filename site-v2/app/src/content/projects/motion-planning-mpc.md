---
title: Kinodynamic Motion Planning & 3D MPC
description: From 3D RRT* paths to smooth trajectories and constrained flight commands.
img: /assets/img/portfolio/mapping.webp
img_alt: Three-dimensional mapping and environment reconstruction
importance: 2
category: Aerial robotics
---

**Mostavio · Navigation & guidance software**  
3D RRT* · Minimum-snap · CVXPY / QP · MPC · nvblox ESDF

A route around obstacles is not enough: the aircraft must be able to **follow it** with finite acceleration, braking distance and sensor latency.

## Navigation pipeline

![Kinodynamic planning, minimum-snap, constrained MPC and PX4](/assets/img/diagrams/planning-pipeline.svg)

- **Plan:** kinodynamic RRT* generates feasible global paths.
- **Smooth:** minimum-snap optimization provides a continuous reference.
- **Track:** constrained MPC computes flight-guidance commands.
- **Avoid:** ESDF obstacle distance informs replanning and local constraints.

## Development environments

<div class="project-gallery">
<figure><img src="/assets/img/portfolio/gazebo-terrain.webp" alt="Terrain-based navigation simulation" loading="lazy"/><figcaption>Terrain-based navigation simulation</figcaption></figure>
<figure><img src="/legacy/images/rrtstar.png" alt="RRT* planning from my earlier ROB521 work" loading="lazy"/><figcaption>RRT* planning from my earlier ROB521 work</figcaption></figure>
</div>

**Engineering focus:** corner tracking, braking overshoot, latency, obstacle clearance and solver feasibility.
