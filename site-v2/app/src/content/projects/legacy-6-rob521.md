---
title: Robot Navigation Foundations — ROB521
description: RRT* global planning, local trajectory rollout, wheel-odometry estimation and LiDAR occupancy mapping.
img: /legacy/images/rrtstar.png
img_alt: RRT-star tree and robot navigation plan from ROB521 exercises
importance: 31
category: Earlier projects
---

**University of Toronto · ROB521 laboratory projects · 2023**

## Learning the full navigation loop

These laboratory exercises were focused on connecting the pieces of a mobile robot navigation system: planning a route, executing it with local obstacle-aware control, estimating motion and building a map.

## Global and local planning

For a TurtleBot navigation task, I implemented **RRT*** as a global path planner and **trajectory rollout** as a local motion-planning technique. A global route gave the robot a direction through an office environment, while the rollout stage evaluated candidate short-horizon motions during execution.

[Watch RRT* route generation](https://youtu.be/iP9Ojx0jmSM) · [Watch trajectory rollout along a planned office route](https://youtu.be/c56PMTSNvyE)

## Mapping and odometry

A separate lab developed encoder-based odometry and an **occupancy grid** using LiDAR observations. This brought in another core navigation consideration: the planner relies on the quality and timeliness of the map and estimated robot pose.

[Watch occupancy-map generation](https://youtu.be/s7eq3KrU5SU)

These projects provided a foundation for the more demanding [3D aerial motion-planning and MPC systems](/projects/motion-planning-mpc/).
