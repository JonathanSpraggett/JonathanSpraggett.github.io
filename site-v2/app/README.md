# Jonathan Spraggett — Astro portfolio

This is the complete Astro application for the [personal robotics engineering and research portfolio](https://jonathanspraggett.github.io/), based on [dadangnh/as-folio](https://github.com/dadangnh/as-folio).

The current project lives in `site-v2/app` on the review branch. The existing Jekyll website remains the live production version until an explicit deployment.

## Run locally

```bash
corepack enable
yarn install --immutable
yarn dev
```

Production build: `yarn build`.

Edit the homepage in `src/pages/index.astro`, technical project stories in `src/content/projects`, publications in `src/data/papers.bib`, and the résumé in `src/data/cv.yml`.

Uploaded public-releasable media are in `public/assets/img/portfolio` and legacy originals in `public/legacy/images`.

**Privacy:** unreleased manuscripts are excluded from the public assets. Do not upload or link unreleased research PDFs in this project.

For migration and deployment instructions, see [site-v2/README.md](../README.md).
