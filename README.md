# Maintaining this website

This is your academic website built on **[al-folio](https://github.com/alshedivat/al-folio)** (a Jekyll theme). This guide covers everyday maintenance: adding and editing content, previewing locally, and deploying to **https://prashantpandey.github.io/**.

> **Key principle — this al-folio site is now the source of truth.**
> The old Hugo/Wowchemy site was imported once (see [`MIGRATION.md`](MIGRATION.md) and the `_migration/` scripts). From now on, **add and edit content here, directly**. Do **not** re-run the `_migration/*.py` scripts — they regenerate files from the old Hugo repo and would overwrite your edits (see [One-time import scripts](#one-time-import-scripts)).

---

## Table of contents
1. [One-time local setup](#one-time-local-setup)
2. [The everyday workflow](#the-everyday-workflow)
3. [Where everything lives](#where-everything-lives)
4. [Adding & editing content](#adding--editing-content)
   - [Publications](#publications)
   - [News / announcements](#news--announcements)
   - [Talks](#talks)
   - [Awards, Students, Teaching, Service (simple pages)](#simple-pages-awards-students-teaching-service)
   - [Lab photo gallery (students page)](#lab-photo-gallery-students-page)
   - [Projects](#projects)
   - [Homepage bio & interests](#homepage-bio--interests)
   - [CV](#cv)
   - [Social links, name, site settings](#social-links-name--site-settings)
   - [Navigation menu](#navigation-menu)
   - [Images & PDFs](#images--pdfs)
5. [Deploying to prashantpandey.github.io](#deploying-to-prashantpandeygithubio)
6. [Troubleshooting](#troubleshooting)
7. [One-time import scripts](#one-time-import-scripts)

---

## One-time local setup

al-folio needs **Ruby 3.x+**. macOS system Ruby (2.6) is too old, so we use Homebrew's Ruby.

```bash
# 1. Install a modern Ruby (once)
brew install ruby

# 2. Put Homebrew Ruby ahead of system Ruby for this shell
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
# (optional: add the line above to your ~/.zshrc so it's permanent)

# 3. Install the site's gems (once, and again whenever the Gemfile changes)
cd ~/sandbox/personal/personal_website_alfolio
gem install bundler
bundle config set --local path vendor/bundle
bundle install
```

> Note: image processing (`imagemagick`) is **disabled** locally (`imagemagick.enabled: false` in `_config.yml`) so you don't need ImageMagick to build. The deploy server (GitHub Actions) installs it automatically.

---

## The everyday workflow

```bash
# 0. one-time per terminal session
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
cd ~/sandbox/personal/personal_website_alfolio

# 1. Start a live preview (auto-rebuilds on save)
bundle exec jekyll serve --port 4001
# open http://localhost:4001  (Ctrl+C to stop)

# 2. Edit content (see sections below), watch it update in the browser

# 3. When happy, commit and push -> the site auto-deploys (see Deployment)
git add -A
git commit -m "Add SIGMOD 2026 paper and news"
git push
```

That's the whole loop: **edit → preview at localhost:4001 → commit → push**. Pushing to `main` triggers the deploy.

---

## Where everything lives

| Content | File / folder |
|---|---|
| Homepage (bio, interests, profile box) | `_pages/about.md` |
| **Publications** | `_bibliography/papers.bib` |
| **News / announcements** | `_news/` (one file per item) |
| **Talks** | `_talks/` (one file per talk) |
| Awards / grants / media | `_pages/awards.md` |
| Students & postdocs | `_pages/students.md` |
| Teaching | `_pages/teaching.md` |
| Academic service | `_pages/service.md` |
| Workshop page | `_pages/workshop.md` |
| Projects | `_projects/` (one file per project) |
| CV (structured) | `_data/cv.yml` · CV PDF: `assets/pdf/cv.pdf` |
| Social links (email, Scholar, GitHub…) | `_data/socials.yml` |
| Name, URL, analytics, features | `_config.yml` |
| Profile photo | `assets/img/prof_pic.jpg` |
| Paper / talk PDFs | `assets/pdf/` (and `assets/pdf/uploads/`) |

---

## Adding & editing content

### Publications

All publications live in **`_bibliography/papers.bib`** as BibTeX entries. The page at `/publications/` is generated automatically and grouped by year.

**To add a paper**, paste a BibTeX entry (DBLP or Google Scholar export works). Then add al-folio's optional fields to enrich it:

```bibtex
@inproceedings{my2027paper,
  title        = {A Great New Filter},
  author       = {Pandey, Prashant and Coauthor, Jane},
  booktitle    = {SIGMOD 2027},
  year         = {2027},
  abbr         = {SIGMOD 2027},                 % blue venue badge on the left
  pdf          = {uploads/my2027paper.pdf},     % file in assets/pdf/  OR a full URL
  code         = {https://github.com/...},      % "Code" link
  abstract     = {One-paragraph abstract...},   % expandable "Abs" button
  selected     = {true},                        % show on the homepage highlights
  award_name   = {Best Paper Award},            % award badge label (optional)
  award        = {Best Paper Award at SIGMOD 2027.}  % award description (optional)
}
```

Field cheat-sheet (all optional):

| Field | Effect |
|---|---|
| `abbr` | Blue venue badge on the left (e.g. `SIGMOD 2027`). **Add this to every paper** for consistency. |
| `pdf` | "PDF" link. A bare filename resolves to `assets/pdf/<file>`; a full `http…` URL links out. |
| `code` | "Code" link (GitHub, etc.) |
| `selected = {true}` | Includes the paper in the **Selected Publications** block on the homepage. |
| `award_name` + `award` | Award badge + description on the paper. |
| `abstract` | Expandable abstract. |
| `bibtex_show = {true}` | Adds a "Bib" button that reveals the BibTeX. |
| `html`, `slides`, `poster`, `video`, `website` | Extra labelled links. |

- **The year** comes from the `year` field and controls grouping/sorting. (During import we set this from the original site's display date — keep using a normal 4-digit year.)
- **The author name "Prashant Pandey" is auto-bolded** (configured via `scholar.last_name`/`first_name` in `_config.yml`).
- **PDFs**: drop the file in `assets/pdf/` and reference it as `pdf = {myfile.pdf}`.

**To edit a paper**, just edit its entry in `papers.bib`.

### News / announcements

Each news item is one Markdown file in **`_news/`**, named `YYYY-MM-DD-slug.md`. The homepage shows the 5 most recent; `/news/` shows all.

```markdown
---
layout: post
date: 2027-06-01 09:00:00-0400
inline: true            # true = one-line item (recommended)
related_posts: false
---
Three papers accepted to **SIGMOD 2027**! :tada:  [optional [link](https://...)]
```

For a longer, standalone news post, omit `inline: true` and add a `title:` — it becomes its own page.

### Talks

Each talk is one Markdown file in **`_talks/`**, named `YYYY-MM-DD-slug.md`. The `/talks/` page lists them grouped by year (most recent first).

```markdown
---
layout: page
title: "Filters and Adaptivity"
date: 2027-03-15
event: "SIGMOD 2027"
location: "Berlin, Germany"
slides: "/assets/pdf/uploads/mytalk.pdf"   # optional
video: "https://youtu.be/..."              # optional
---

Optional abstract / description in the body.
```

The homepage "Recent & Upcoming Talks" is **not** separate — talks only live in `_talks/`. (If you want a few on the homepage too, ask and we can wire that up.)

### Simple pages: Awards, Students, Teaching, Service

These are plain Markdown lists — just edit the file and save:

- **Awards / grants / media** → `_pages/awards.md` (sections `## Grants`, `## Awards`, `## Media`)
- **Students & postdocs** → `_pages/students.md`
- **Teaching** → `_pages/teaching.md`
- **Service** → `_pages/service.md`

Example (adding a student to `_pages/students.md`):

```markdown
- [New Student](https://their-site.com) — PhD (Started Fall 2027)
```

### Lab photo gallery (students page)

The bottom of `_pages/students.md` has a **"Lab life"** photo grid (hikes, runs, dinners). It's **data-driven**: the photo list lives in **`_data/lab_photos.yml`**, and the page loops over it **sorted by date, newest first**. You don't edit the page markup — only the YAML and the image files.

Each entry has three fields:

```yaml
- date: 2025-06                 # YYYY-MM — controls the sort order (newest first)
  image: assets/img/lab/lab-09.jpg
  caption: "SIGMOD 2025, Berlin, Germany w/ ..."   # quote it; commas/apostrophes are fine
```

The images themselves live in **`assets/img/lab/`**, named `lab-NN.jpg`.

**Before adding photos:** iPhone photos are usually **HEIC** (browsers can't display them) and several MB each. Convert and resize them to web JPEGs first. `sips` is built into macOS:

```bash
cd assets/img/lab
# convert + resize one photo (max 1600px on the long edge) to the next free number
sips -s format jpeg -Z 1600 ~/Desktop/IMG_1234.HEIC --out lab-15.jpg
```

**To add a photo:**
1. Convert/resize it into `assets/img/lab/` as the next `lab-NN.jpg` (step above).
2. Add an entry to `_data/lab_photos.yml` with its `date`, `image`, and `caption`. It auto-sorts into place by date — no need to position it manually.

**To remove a photo — do _both_:**
1. Delete its entry from `_data/lab_photos.yml`, **and**
2. Delete the image file from `assets/img/lab/`.

> The filename number is just a label; gallery order comes entirely from the `date` field. Numbering gaps (e.g. a missing `lab-08`) are harmless — no need to renumber.

> **Caching:** after deploying, an old photo may linger because of browser/CDN caching. Hard-refresh (`Cmd+Shift+R`) or use a private window to confirm the change; the CDN clears within a few minutes.

### Projects

Each project is one Markdown file in **`_projects/`** (`N_slug.md`, where `N` sets the order):

```markdown
---
layout: page
title: My Project
description: One-line summary.
img: assets/img/myproject.jpg
importance: 1
category: research
---

Body text, images, links.
```

Projects use `category: research` and show at `/projects/`. (Currently hidden from the top nav to match your old site — set `nav: true` in `_pages/projects.md` to expose it.)

### Homepage bio & interests

Edit **`_pages/about.md`**. The body (below the `---` front matter) is your biography. The `subtitle:` is the line under your name; the `profile.more_info` block is the contact box next to your photo. Research-interest keywords are woven into the bio paragraph (bold text).

### CV

Two parts:
- **The downloadable PDF**: replace `assets/pdf/cv.pdf` (the `/cv/` page's download button points here, and so does the CV social icon).
- **The on-page structured CV**: edit `_data/cv.yml` (Education, Experience, etc.). It's currently partial — fill it in or, if you only want the PDF, you can trim the YAML.

### Social links, name & site settings

- **Social icons** (email, X, Scholar, GitHub, CV): `_data/socials.yml`.
- **Your name, site title, URL, Google Analytics, dark mode, search**: `_config.yml` (top of file). The name-bolding in publications is `scholar.last_name` / `first_name` in the same file.
- **After editing `_config.yml`, restart `jekyll serve`** — config changes are not hot-reloaded.

### Navigation menu

The top nav is built from pages that have `nav: true` in their front matter, ordered by `nav_order`. Current order: News (1) · Awards (2) · Talks (3) · Publications (4) · Teaching (5) · Students (6) · Service (7). To add/remove/reorder, change `nav` / `nav_order` in the relevant `_pages/*.md`.

### Images & PDFs

- **Profile photo**: `assets/img/prof_pic.jpg`.
- **Other images** (projects, posts): put in `assets/img/` and reference as `assets/img/<file>`.
- **PDFs** (papers, slides, CV): put in `assets/pdf/` (paper PDFs imported from the old site are under `assets/pdf/uploads/`).

---

## Deploying to prashantpandey.github.io

Your live site is a **GitHub user page** served from the repository **`prashantpandey/prashantpandey.github.io`** (which currently holds the old Hugo site). al-folio ships a GitHub Actions workflow (`.github/workflows/deploy.yml`) that, on every push to `main`, builds the site and publishes it to a **`gh-pages`** branch.

### One-time switch-over

1. **Back up the current site.** The existing Hugo site is already in that repo's git history, so nothing is lost — but if you want a safety copy, branch it first:
   ```bash
   # in a clone of the existing prashantpandey.github.io repo
   git checkout -b hugo-backup && git push -u origin hugo-backup
   ```

2. **Put the al-folio site in that repo.** This directory is already a git repo, but its `origin` currently points at the upstream al-folio project (it was cloned from there). You have two options:

   **Option A — clean history (recommended).** Start a fresh history so al-folio's upstream commits aren't in your repo:
   ```bash
   cd ~/sandbox/personal/personal_website_alfolio
   rm -rf .git
   git init
   git add -A
   git commit -m "al-folio site"
   git branch -M main
   git remote add origin https://github.com/prashantpandey/prashantpandey.github.io.git
   git push -f origin main      # -f replaces the old Hugo content on main
   ```

   **Option B — keep the current (al-folio) history.** Just re-point the remote:
   ```bash
   cd ~/sandbox/personal/personal_website_alfolio
   git remote set-url origin https://github.com/prashantpandey/prashantpandey.github.io.git
   git add -A
   git commit -m "Switch site to al-folio"
   git push -f origin main
   ```

   Either way, the old Hugo site stays recoverable from that repo's history (and from the `hugo-backup` branch in step 1).

3. **Confirm the config is correct** (already set):
   - `url: https://prashantpandey.github.io`
   - `baseurl:` *(empty — site lives at the domain root)*

4. **Enable Actions write access.** Repo **Settings → Actions → General → Workflow permissions → "Read and write permissions"**. This lets the deploy action create/push the `gh-pages` branch.

5. **Wait for the build.** Check the **Actions** tab — the `deploy` workflow runs on the push and creates the `gh-pages` branch (takes ~2–4 min).

6. **Point GitHub Pages at the built branch.** Repo **Settings → Pages → Build and deployment → Source: "Deploy from a branch" → Branch: `gh-pages` / `(root)`** → Save.

7. **Visit https://prashantpandey.github.io/** — it should now serve the al-folio site. The first time can take a few minutes to propagate.

### Ongoing deploys

After the one-time switch, deployment is automatic: **commit and push to `main`**, and the Action rebuilds and republishes. No manual build needed.

```bash
git add -A && git commit -m "Add new paper" && git push
```

### Notes & gotchas
- The workflow only triggers on content paths (`**/*.md`, `**.bib`, `**.yml`, `assets/**`, `Gemfile`, …), which covers all normal edits.
- `imagemagick` is installed automatically in CI, so responsive images work in production even though it's disabled locally. (You can re-enable it locally with `brew install imagemagick` and `imagemagick.enabled: true`.)
- If CSS/JS doesn't load after the first deploy, make sure Pages is serving the **`gh-pages`** branch (step 6), not `main`.
- A custom domain (e.g. `pandey.dev`) is optional: add it under Settings → Pages → Custom domain and set `url:` accordingly.

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `jekyll: command not found` / old Ruby | Run `export PATH="/opt/homebrew/opt/ruby/bin:$PATH"` (and `bundle install` once). |
| Port 4001 busy | `pkill -f jekyll`, or use `--port 4002`. |
| Config edits not showing | Restart `jekyll serve` (config isn't hot-reloaded). |
| A paper/talk doesn't appear | Check the front matter / BibTeX is valid (no missing braces); check the date isn't malformed. |
| Build error mentioning `jupyter` or `imagemagick` | Those features are off locally; if you re-enable them, install the tool first. |
| Local build is fine but deploy fails | Check the **Actions** tab logs; usually a `.bib`/front-matter syntax error or missing Actions write permission. |

---

## One-time import scripts

`_migration/build_bib.py`, `build_talks.py`, and `build_projects.py` were used **once** to import content from the old Hugo site (`../personal_website/`). They also encode the curated **`SELECTED`** (homepage highlights) and **`AWARDS`** (paper award badges) lists.

- **Do not re-run them** during normal maintenance — they regenerate `papers.bib`, `_talks/`, and `_projects/` from the Hugo repo and will **overwrite** any edits you've made here.
- They're kept only for reference / a possible future re-import. If you ever do re-run `build_bib.py`, remember to re-apply edits, and note that `SELECTED`/`AWARDS` live at the top of that file.

See [`MIGRATION.md`](MIGRATION.md) for the full record of how the site was ported.
