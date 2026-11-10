# Jonathan Spraggett — robotics and autonomy portfolio (Astro / as-folio)

The working redesign is in **[site-v2/app](./app)**. The existing Jekyll site remains at the repository root on `master`. Nothing here is deployed to GitHub Pages.

## Local development

Requires Node.js 24+ and Corepack:

```bash
git switch redesign/as-folio-2026
cd site-v2/app
corepack enable
yarn install --immutable
yarn dev
```

For a production build, run `yarn build`. The root GitHub Actions workflow [asfolio-redesign-build.yml](../.github/workflows/asfolio-redesign-build.yml) runs the same build, validates routes and uploads compiled HTML for review.

## Site sections

- **Home:** a responsive editorial introduction, selected projects and publications, experience timeline and CV links
- **Projects:** technical case studies for eVTOL autonomy, flight controls, planning, estimation, applied perception, RoboCup and humanoid research
- **Technical deep dives:** archived original field-line processing and UKF algorithms, reformatted with diagrams and documentation
- **Earlier projects:** capstone-related foundations, university labs, hackathons and early hands-on robotics
- **Research:** AIAA SciTech 2026, RoboCup Symposium 2025, the 2023 undergraduate thesis, and NeurIPS 2021 workshop paper
- **CV:** web résumé and the redacted short public PDF, excluding unreleased manuscript information

Legacy project sources are retained under `app/legacy_jekyll_content/_portfolio` for traceability, and source media have been preserved under `app/public/legacy/images`. Overlapping legacy pages were incorporated into their canonical, expanded project stories instead of generating duplicate cards.

## Publication and image policy

Only released academic papers and the thesis are publicly downloadable. An unreleased research submission and its supporting figures are **intentionally excluded from this branch**. Do not reintroduce manuscript files or bundled artifacts when updating the site.

Company aircraft and security-system images should be checked for public-release approval before deployment.

## Deployment

This is a **review-only branch**. A production migration needs the Astro project moved to repository root (or a build config targeting `site-v2/app`) plus an explicitly configured GitHub Pages deploy workflow. Do not merge and expect the live Jekyll site to become Astro automatically.

## Attribution

Built on the MIT-licensed [as-folio Astro template](https://github.com/dadangnh/as-folio), with a custom homepage informed by editorial academic portfolio layouts, including [Ben Agro's site](https://benagro314.github.io/).
