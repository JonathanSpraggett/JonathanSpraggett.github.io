---
title: Flight-Tested Control & Vibration Filtering
description: Frequency-domain diagnosis, IMU filtering, stability margins and full-scale flight validation.
img: /assets/img/portfolio/fft.webp
img_alt: Raw versus filtered IMU vibration power
importance: 4
category: Flight controls
related_publications:
- spraggett2026digitalfilter
---

**AIAA SciTech 2026 · [Published paper (PDF)](/assets/pdf/aiaa2026_fft.pdf)**

Rotor vibration corrupted angular-rate feedback on a 250 kg coaxial eVTOL. I traced the dominant frequencies and evaluated **digital filtering without compromising loop stability**.

## Method

![Measurement filtering and closed-loop validation process](/assets/img/diagrams/filtering-pipeline.svg)

- **Diagnosis:** FFT/PSD analysis identified harmonics near 46 and 92 Hz.
- **Design:** 30 Hz low-pass and dual-notch filters.
- **Validation:** phase delay, gain/phase margins and hover telemetry.

## Physical validation

<div class="project-gallery">
<figure><img src="/assets/img/portfolio/flight-test.webp" alt="Aircraft used for flight experiments" loading="lazy"/><figcaption>Aircraft used for flight experiments</figcaption></figure>
<figure><img src="/legacy/images/mostavio.jpeg" alt="Original full-scale aircraft photo" loading="lazy"/><figcaption>Original full-scale aircraft photo</figcaption></figure>
</div>

**Outcome:** Substantially reduced vibration harmonics and throttle variation, with repeatable stable hover. Full quantitative results appear in the [paper](/assets/pdf/aiaa2026_fft.pdf).
