---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
Welcome to my portfolio website, a platform that showcases my love for robotics and AI. As a Bachelor of Applied Science student in Engineering Science at the University of Toronto, I have developed my skills in areas such as machine learning, computer vision, and robot modeling and control. My proficiency in these areas is highlighted by my role as the project manager and software team lead of UTRA Robosoccer, Canada's first undergraduate-led humanoid robot team.

My research interests in robotics focus on reinforcement learning, computer vision, and localization. I have employed reinforcement learning algorithms, including Proximal Policy Optimization (PPO) and Adversarial Imitation Learning, to train humanoid robots in tasks such as walking, jumping, and kicking, resulting in improved stability, accuracy, and performance. My experience in computer vision encompasses writing object detection and segmentation software to extract crucial information from the surrounding environment, as well as localization techniques using an Unscented Kalman Filter (UKF) to fuse odometry, IMU orientation, point clouds, and field landmarks for precise robot localization.

I am thrilled to share my experiences and accomplishments in the field of robotics and AI, and I invite you to delve into my portfolio to learn more. Whether you're interested in my technical expertise, leadership skills, or research interests, you'll find everything here!

Reinforcement Learning for Soccer Skills Research Thesis
======

This thesis presents a new approach for training control-related tasks in humanoid robots to participate in the RoboCup Humanoid Soccer League. The proposed approach combines Deep Reinforcement Learning (RL) with the Proximal Policy Optimization (PPO) algorithm and Adversarial Motion Priors (AMP) technique to train a neural network in a simulated environment. The PPO algorithm is used to improve the stability and reduce programming effort, while the AMP technique allows the robot to imitate behavior from a reference motion dataset, increasing flexibility and reducing the need for complex reward functions. The trained model is fine-tuned and deployed in a real-world setting using domain randomization to address any discrepancies between the simulated environment and actual conditions. This research will enable a humanoid robot to react dynamically to the environment of a soccer match and make more complex decisions, including team play, and lays the foundation for future RL projects utilizing AMP to transfer complex skills to physical robots.

Walking Task               |  Kicking Task             |  Jumping Task
:-------------------------:|:-------------------------:|:-------------------------:
[Video](https://drive.google.com/file/d/19GCgfvvGYjweLEn7ZBMhO4SBAYYqVL6E/view?usp=sharing)<img src="/images/walk.gif" width="300"/>   |  [Video](https://drive.google.com/file/d/1Cyms_T3oWZoMaW69t-5PMxBNRFpFf_eY/view?usp=sharing)<img src="/images/kick.gif" width="300"/> |  [Video](https://drive.google.com/file/d/1kOQWXYKEsBclPH4ebD-uuuZmzzrWTaHk/view?usp=sharing)<img src="/images/jump.gif" width="300"/>

Autonomous Drone for Nuclear Safety Inspections Capstone
======

Designed and developed a cutting-edge drone for nuclear safety inspections. Equipped with CV object detection (YoloV5), the drone can read critical data from radiated zones, while its visual SLAM enables accurate localization, RRT* allows for obstacle-free path planning and precise way-point motion planning for navigation through these zones.
### Assembled Drone 
<p align="center">
<img src="/images/Hardware.png" width="1000"/>
</p>

RoboSoccer Highlights
======

As a skilled Robotic Software Developer and Team Lead at UTRA Humanoid, I have made significant contributions to the field of robotics through software solutions. I utilized Python, OpenCV, and ROS to implement the Adaptive Monte Carlo Localization (AMCL) and Unscented Kalman Filter (UKF) algorithms, which ensured precise robot positioning. I also developed an FSM-based AI for soccer games' strategic decision-making. My leadership skills were put to the test as I led a team of 30 to build a cost-effective humanoid robot that placed 5th in the Robocup 2022 competition in Bangkok. I am proud of my impact in the field and excited to continue driving innovation and growth.

### Robot Capabilities 
Qualification Video                 
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/PnHDpNx1NyU/0.jpg)](https://youtu.be/PnHDpNx1NyU)

Short Clip     
![Demo CountPages alpha](/images/gif.gif)
 
### Unscented Kalman Filter (UKF) 
<p align="center">
<img src="/images/ukf.png" />
</p>

### Object Detection (Yolov5) 
<p align="center">
<img src="/images/detect.png" />
</p>

### Field Line Detection 
Field Lines   
<p align="center">
<img src="/images/field_lines.png"  width='500'/>  
</p>

Point Cloud 
<p align="center">
<img src="/images/scattered_points.png" width='500'/>
</p>
