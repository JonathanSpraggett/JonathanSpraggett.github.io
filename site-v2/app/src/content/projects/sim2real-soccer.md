---
title: Sim2Real Reinforcement Learning for Soccer Skills
description: Undergraduate thesis on PPO, adversarial motion priors, and humanoid walking, kicking and jumping.
img: /assets/img/portfolio/sim2real.webp
img_alt: Simulated humanoid attempting a soccer skill
importance: 8
category: Humanoid robotics
related_publications:
- spraggett2023thesis
---

**BASc thesis:** *Sim2Real Reinforcement Learning for Soccer Skills* · April 2023  
**Supervisor:** Prof. Michael Guerzhoy · [Read the thesis (PDF)](/assets/pdf/thesis_2023.pdf)

## Why study learned soccer skills?

Classical humanoid motion routines can be effective, but building and tuning separate controllers for every contact-rich behavior takes significant engineering effort. My undergraduate thesis examined whether reinforcement learning and imitation learning could develop more flexible **walking, kicking and jumping** policies in simulation and then transfer those policies to a physical robot.

The research used PPO, curriculum learning and **Adversarial Motion Priors (AMP)**, with simulation environments including NVIDIA Isaac Gym and Webots.

## Training architecture

The learning setup combined an observation space, an action policy, task objectives and a motion-prior signal. Curriculum design gradually exposed the policy to more demanding versions of each task.

![Training and control system overview from the 2023 thesis](/legacy/images/t1.png)

*The original thesis overview, preserved from the academic portfolio.*

The AMP component encouraged motions similar to reference examples while the task reward optimized soccer-relevant outcomes. This was important for contact-rich behaviors where a purely hand-designed reward can lead to mechanically successful but unnatural movement.

## Three learned skills

### Kicking

The policy had to combine balance, contact timing and a directed swing rather than maximizing a single joint movement.

![Humanoid kicking in simulation](/assets/img/portfolio/sim2real-kick.gif)

### Walking

Walking required repeated balance and support transitions, with domain randomization used to explore robustness to changes in the simulated dynamics.

![Humanoid walking in simulation](/assets/img/portfolio/sim2real-walk.gif)

### Jumping

Jumping introduced a different contact sequence: loading, flight and landing.

![Humanoid jumping in simulation](/assets/img/portfolio/sim2real-jump.gif)

## Evaluation and the reality gap

The policies demonstrated improved simulated behaviors, but the **transfer to the physical humanoid was unsuccessful**, as documented in the thesis abstract. This limitation is as important as the simulated results: contact modeling, actuation dynamics, sensing, and timing can prevent a policy that works in a simulator from working on hardware.

![Results summary from the original thesis presentation](/legacy/images/t10.png)

*Results figure retained from the thesis-era portfolio.*

I carried those lessons forward into more general humanoid learning research, including [the unified zero-shot fall-recovery policy](/projects/humanoid-zero-shot-getup/).
