---
title: One Policy, Seven Humanoids — Zero-Shot Recovery
description: A shared reinforcement-learning controller for standing up across different humanoid robots.
img: /assets/img/portfolio/humanoid-suite.webp
img_alt: Seven humanoid robot models of different sizes
importance: 7
category: Robot learning
related_publications:
- spraggett2025getup
---

**RoboCup Symposium 2025 · [Paper (PDF)](/assets/pdf/robocup2025.pdf)**

Can one learned controller recover from falls on **different humanoid bodies**, including robots it has never trained on?

## Shared policy

![Shared policy training and zero-shot evaluation](/assets/img/diagrams/humanoid-policy.svg)

- Trained a shared RL recovery policy across seven morphologies.
- Evaluated unseen robots **without fine-tuning**.
- Reached up to **86 ± 7%** zero-shot recovery success in reported experiments.

## Recovery examples

<div class="project-gallery">
<figure><img src="/assets/img/portfolio/humanoid-getup-front.gif" alt="Forward-fall recovery demonstration" loading="lazy"/><figcaption>Forward-fall recovery demonstration</figcaption></figure>
<figure><img src="/assets/img/portfolio/humanoid-getup-back.gif" alt="Backward-fall recovery demonstration" loading="lazy"/><figcaption>Backward-fall recovery demonstration</figcaption></figure>
<figure><img src="/legacy/images/bez.png" alt="Robot model retained from the original portfolio" loading="lazy"/><figcaption>Robot model retained from the original portfolio</figcaption></figure>
</div>

The paper investigates where morphology-blind policies generalize and where they still fail.
