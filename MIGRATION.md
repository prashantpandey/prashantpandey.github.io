# Migration: Wowchemy (Hugo) → al-folio (Jekyll)

This site is a prototype migration of the old Wowchemy/Hugo academic site
(`../personal_website/`) to [al-folio](https://github.com/alshedivat/al-folio).
The original Hugo site is untouched.

## Why we migrated

The Hugo site stopped building on modern Hugo: the pinned Wowchemy v5 theme
module uses the `getCSV` template function, **removed in Hugo v0.123.0**. The
theme is delivered as a fast-moving remote module (since renamed to Hugo Blox),
so upstream changes break local builds. al-folio is BibTeX-driven and far less
coupled to a churning mega-theme, which is the long-term maintenance win.

## Toolchain

- al-folio needs **Ruby 3.x+** (CI uses 3.3.5; this prototype built on Ruby 4.0
  via Homebrew). System Ruby 2.6 is too old.
- Setup:
  ```bash
  brew install ruby
  export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
  gem install bundler
  bundle config set --local path vendor/bundle
  bundle install
  bundle exec jekyll serve --port 4001   # http://localhost:4001
  ```
- `imagemagick.enabled` is set to **false** in `_config.yml` to avoid the
  ImageMagick system dependency for local builds. Re-enable (and `brew install
  imagemagick`) for responsive images in production.
- al-folio's demo Jupyter blog post was removed (it needs the `jupyter` CLI).

## What was converted (scripts in `_migration/`)

| Script | Source → Target | Notes |
|--------|-----------------|-------|
| `build_bib.py` | `content/publication/*/{index.md,cite.bib}` → `_bibliography/papers.bib` | 46 entries. 36 reuse the existing DBLP `cite.bib`; 10 are synthesized from front matter. Enriches each with `pdf`/`code`/`slides`/`selected`/`abstract`/`abbr`. |
| `build_projects.py` | `content/project/*/index.md` → `_projects/*.md` | 6 projects, `category: research`. |
| `build_talks.py` | `content/event/*/index.md` → `_talks/*.md` | 38 talks. `_talks` is a custom collection (registered in `_config.yml`), listed by `_pages/talks.md` grouped by year. |

PDFs were copied from `../personal_website/static/uploads/` to
`assets/pdf/uploads/` so `pdf = {uploads/...}` references and talk slide links
resolve. The CV PDF is wired into `_pages/cv.md` (`cv_pdf`).

To re-run any converter (paths are hardcoded to the sibling Hugo repo):
```bash
python3 _migration/build_bib.py
python3 _migration/build_projects.py
python3 _migration/build_talks.py
```

## Config / data wiring done by hand

- `_config.yml`: name, `url`, blank `baseurl` (root), `scholar.{first,last}_name`
  (bolds your name in the publication list), `talks` collection, imagemagick off.
- `_data/socials.yml`: email, Google Scholar id `VO62HkEAAAAJ`, GitHub, X.
- `_pages/about.md`: bio, Northeastern affiliation, profile box.
- `_pages/projects.md`: `display_categories: [research]` (default was `[work, fun]`,
  which is why projects showed empty at first).
- `_data/cv.yml`: replaced the default Einstein data.

## Full-site port (complete)

Every page of the live site (https://prashantpandey.github.io/) is ported, with
content verified against it:

> **Layout note:** the homepage was later restructured from a single Wowchemy-style
> scroll into a **lean al-folio about page** (bio + interests + News feed +
> Selected Publications + social). The long sections were moved to their own nav
> pages — `/awards/` (Grants/Awards/Media), `/students/`, `/teaching/`, `/service/`
> — which also makes the nav (News · Awards · Talks · Publications · Teaching ·
> Students · Service) match the live site's labels. Contact lives in the profile box.

| Live site | al-folio | Status |
|-----------|----------|--------|
| Homepage sections (Biography, Interests, Media & Awards, Talks, Publications, Teaching, Students, Contact) | `_pages/about.md` (lean) + `/awards/`, `/students/`, `/teaching/`, `/talks/`, `/publications/`, `/service/` | all content verified verbatim |
| — (al-folio addition) | News feed (`_news/`, homepage announcements + `/news/` archive) | 10 items seeded from awards/papers/talks |
| — (al-folio addition) | Selected Publications on homepage (`selected={true}`) | 6 curated papers (editable via `SELECTED` in `build_bib.py`) |
| — (al-folio addition) | Per-paper award badges (`award_name` + `award`) | ALENEX 2026 Best Artifact (WarpSpeed), FAST 2016 Best Paper, FAST 2015 Runner-Up — editable via `AWARDS` in `build_bib.py` |
| `/publication/` (46) | `/publications/` from `papers.bib` | 46 titles + year distribution match exactly |
| `/event/` (~38 talks) | `/talks/` (`_talks` collection) | 38 talks, grouped by year |
| `/teaching/` | `/teaching/` + homepage section | 7 courses |
| `/service/` | `/service/` | full year-by-year list |
| `/workshop/` | `/workshop/` | full agenda + speakers + videos |
| `/project/` (6) | `/projects/` | 6 projects (not in live nav; `nav: false`) |
| CV PDF | `/cv/` + CV social icon | links `assets/pdf/cv.pdf` |

Two corrections were applied in `build_bib.py` so the publications match the live
site exactly:
- **Year** is taken from each post's front-matter `date` (what Wowchemy displays
  and sorts by), not the DBLP journal year. This fixed e.g. Adaptive Quotient
  Filters (2024→2025), The Online Event-Detection Problem (2018→2019), Squeakr
  (2018→2017), Writes Wrought Right (2017→2016).
- **Title** is taken from the front-matter `title:` (not the DBLP `cite.bib`
  title), fixing capitalization/hyphenation differences.

### Known inherent difference (not a content error)
The live Wowchemy site renders publication authors with full first names
("Michael Bender"). al-folio uses `jekyll-scholar` with **APA** style, which
abbreviates to initials ("M. A. Bender"). The author *sets and order are
identical*; only the citation-string formatting differs. Changing this would
require a custom CSL/citation template — out of scope for the port.

### Skipped (boilerplate, not real content)
- `/post/getting-started/` — the Wowchemy demo post ("Welcome to Wowchemy").
- `/slides/example/` — demo slides.
- `privacy.md` / `terms.md` — `draft: true`, never published on the live site.

## Known cleanup / TODO before going live

- [x] Profile photo (`assets/img/prof_pic.jpg`) and CV PDF (`assets/pdf/cv.pdf`) — done.
- [x] `alenex25`/WarpSpeed year — confirmed **2026** on the live site; matches.
- [ ] **CV (`_data/cv.yml`)** — Education (PhD, Stony Brook 2018) + a placeholder
      Experience entry (not fabricated). Complete from your real CV, or rely on
      the linked PDF and trim the YAML sections. The CV download button already
      serves the real `cv.pdf`.
- [ ] **Author citation style** — see "Known inherent difference" above; optional
      CSL customization if you want full first names on the publications page.
- [ ] **Project images** — projects use a placeholder `assets/img/12.jpg`; drop
      in real images if desired (projects are not in the live nav anyway).
- [ ] **Talk detail pages** — abstracts/bodies are sparse (source events had
      little body text). Fine for the list; enrich if desired.
- [ ] **Long term**: as you add papers, just append a BibTeX entry to
      `_bibliography/papers.bib` (with optional `pdf`/`code`/`selected` fields) —
      no per-paper folders needed. This is the maintenance payoff.

## Pages

`/` · `/publications/` (46) · `/projects/` (6) · `/talks/` (38) · `/cv/`
