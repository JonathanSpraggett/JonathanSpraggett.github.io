---
title: Sim2Real Reinforcement Learning for Soccer Skills
description: Learning humanoid walking, kicking and jumping with PPO and adversarial motion priors.
img: /assets/img/portfolio/sim2real.webp
img_alt: Humanoid soccer policy in simulation
importance: 8
category: Robot learning
related_publications:
- spraggett2023thesis
---

**BASc Thesis · University of Toronto, 2023 · [Full thesis (PDF)](/assets/pdf/thesis_2023.pdf)**

I explored how reinforcement and imitation learning can create humanoid soccer skills with less hand-tuned motion programming.

## Approach

- **PPO** for policy optimization.
- **Adversarial motion priors** to encourage reference-like motion.
- **Curriculum and domain randomization** for robust training.

## Skills from the original portfolio

<div class="project-gallery">
<figure><img src="/legacy/images/walk.gif" alt="Walking policy" loading="lazy"/><figcaption>Walking policy</figcaption></figure>
<figure><img src="/legacy/images/kick.gif" alt="Kicking policy" loading="lazy"/><figcaption>Kicking policy</figcaption></figure>
<figure><img src="/legacy/images/jump.gif" alt="Jumping policy" loading="lazy"/><figcaption>Jumping policy</figcaption></figure>
<figure><img src="/legacy/images/t1.png" alt="Original thesis system overview" loading="lazy"/><figcaption>Original thesis system overview</figcaption></figure>
<figure><img src="/legacy/images/t10.png" alt="Original thesis results slide" loading="lazy"/><figcaption>Original thesis results slide</figcaption></figure>
</div>

**Result:** Promising behaviors in simulation; physical sim-to-real transfer was **not successful**. The gap informed my later [cross-morphology recovery work](/projects/humanoid-zero-shot-getup/).
