#!/usr/bin/env python3
"""Merge Wowchemy per-paper cite.bib files into a single al-folio papers.bib,
enriching each entry with al-folio custom fields (pdf, code, selected, abbr,
abstract, slides, poster) pulled from the publication's index.md front matter.
Synthesizes a BibTeX entry for publications that lack a cite.bib."""
import os, re, glob, sys

SRC = "/Users/p.pandey/sandbox/personal/personal_website/content/publication"
OUT = "/Users/p.pandey/sandbox/personal/personal_website_alfolio/_bibliography/papers.bib"

# Publications highlighted on the homepage (al-folio `selected={true}`). Edit freely.
SELECTED = {"sigmod26_aeris", "sigmod26_bread", "sigmod25",
            "sigmod23_iceberg", "sigmod17", "recomb18"}

# Awards on publications -> al-folio `award_name` (badge) + `award` (description).
AWARDS = {
    "alenex25": ("Best Artifact Award", "Best Artifact Award at ALENEX 2026."),
    "fast16":   ("Best Paper Award", "Best Paper Award at FAST 2016."),
    "fast15":   ("Best Paper Runner-Up", "Runner-Up to the Best Paper Award at FAST 2015."),
}

TYPE_MAP = {"1": "inproceedings", "2": "article", "3": "article",
            "4": "techreport", "5": "book", "6": "incollection",
            "7": "phdthesis", "8": "misc"}

def parse_front_matter(path):
    """Very small YAML-ish parser for the simple key: value front matter.
    Handles multi-line double-quoted scalars (e.g. titles wrapped over 2 lines)."""
    fm = {}
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    body = text[m.end():] if m else ""
    block = m.group(1) if m else text
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        i += 1
        if not line or line.lstrip().startswith("#"):
            continue
        mm = re.match(r"^([A-Za-z_][\w]*):\s?(.*)$", line)
        if not mm:
            continue
        key, val = mm.group(1), mm.group(2).strip()
        # multi-line double-quoted scalar: opening quote with no closing quote
        if val.startswith('"') and not (val.endswith('"') and len(val) > 1):
            while i < len(lines) and '"' not in lines[i]:
                val += " " + lines[i].strip(); i += 1
            if i < len(lines):
                val += " " + lines[i].strip(); i += 1
            fm[key] = val.strip().strip('"').strip()
        elif val.startswith("[") and val.endswith("]"):
            items = [x.strip().strip('"').strip("'") for x in val[1:-1].split(",")]
            fm[key] = [x for x in items if x]
        else:
            fm[key] = val.strip('"').strip("'")
    return fm, body.strip()

def norm_author(a):
    """Clean a single author token: drop leading 'and', map admin, 'Last, First'."""
    a = re.sub(r"^and\s+", "", a.strip())
    a = "Prashant Pandey" if a == "admin" else a
    parts = a.split()
    return f"{parts[-1]}, {' '.join(parts[:-1])}" if len(parts) > 1 else a

def derive_year(fm):
    """Use the front-matter `date` year -- this is what the live Wowchemy site
    displays and sorts by (it can differ from the DBLP journal/proceedings year)."""
    return (clean(fm.get("date")) or "")[:4]

def set_title(bibtext, title):
    """Replace the bib entry's title with the front-matter title (the live site
    renders index.md titles, not the DBLP cite.bib titles). Brace-balanced."""
    title = clean(title)
    if not title:
        return bibtext
    m = re.search(r"title\s*=\s*\{", bibtext)
    if not m:
        return bibtext
    j, depth = m.end(), 1
    while j < len(bibtext) and depth > 0:
        if bibtext[j] == "{":
            depth += 1
        elif bibtext[j] == "}":
            depth -= 1
        j += 1
    return bibtext[:m.start()] + f"title        = {{{title}}}" + bibtext[j:]

def set_year(bibtext, year):
    """Force the bib entry's year field to `year` (replace or insert)."""
    if not year:
        return bibtext
    if re.search(r"\byear\s*=", bibtext):
        return re.sub(r"(\byear\s*=\s*)\{?\d{4}\}?", r"\g<1>{%s}" % year, bibtext, count=1)
    m = re.search(r"(@\w+\s*\{[^,]+,)", bibtext)
    return bibtext[:m.end()] + f"\n  year         = {{{year}}}," + bibtext[m.end():]

def clean(v):
    return (v or "").strip().strip('"').strip("'")

def enrich_fields(fm, body):
    """Return list of (field, value) al-folio custom fields to inject."""
    out = []
    # Venue badge (al-folio `abbr`): prefer the short label, fall back to the
    # `publication` field (already short for most entries), then patent.
    abbr = clean(fm.get("publication_short")) or clean(fm.get("publication"))
    if not abbr and (fm.get("publication_types") or [""])[0] == "8":
        abbr = "US Patent"
    if abbr:
        out.append(("abbr", abbr))
    abstract = clean(fm.get("abstract")) or body
    if abstract:
        abstract = abstract.replace("\n", " ").strip()
        if abstract:
            out.append(("abstract", abstract))
    for src_key, bib_key in [("url_pdf", "pdf"), ("url_code", "code"),
                              ("url_slides", "slides"), ("url_poster", "poster"),
                              ("url_video", "video"), ("url_project", "website")]:
        v = clean(fm.get(src_key))
        if v:
            out.append((bib_key, v))
    if str(fm.get("featured")).lower() == "true":
        out.append(("selected", "true"))
    return out

def inject(bibtext, fields):
    """Insert custom fields right after the `@type{key,` opening line."""
    m = re.search(r"(@\w+\s*\{[^,]+,)", bibtext)
    if not m:
        return bibtext
    insert = "".join(f"\n  {k:<12}= {{{v}}}," for k, v in fields)
    return bibtext[:m.end()] + insert + bibtext[m.end():]

def synthesize(fm, key):
    ptype = (fm.get("publication_types") or ["0"])[0]
    btype = TYPE_MAP.get(ptype, "misc")
    authnames = [norm_author(a) for a in (fm.get("authors") or [])]
    year = derive_year(fm)
    lines = [f"@{btype}{{{key},",
             f"  title        = {{{clean(fm.get('title'))}}},",
             f"  author       = {{{' and '.join(authnames)}}},",
             f"  year         = {{{year}}},"]
    if clean(fm.get("publication")):
        if ptype == "8":
            venue = "howpublished"   # patent
        elif btype == "article":
            venue = "journal"
        else:
            venue = "booktitle"
        lines.append(f"  {venue:<12} = {{{clean(fm['publication']) or 'US Patent'}}},")
    doi = clean(fm.get("doi"))
    if doi.startswith("http"):           # patents store a Google Patents URL here
        lines.append(f"  html         = {{{doi}}},")
    elif doi:
        lines.append(f"  doi          = {{{doi}}},")
    lines.append("}")
    return "\n".join(lines)

entries, synthesized, enriched = [], 0, 0
for d in sorted(glob.glob(os.path.join(SRC, "*"))):
    idx = os.path.join(d, "index.md")
    if not os.path.isfile(idx):
        continue
    fm, body = parse_front_matter(idx)
    slug = os.path.basename(d)
    bibpath = os.path.join(d, "cite.bib")
    fields = enrich_fields(fm, body)
    if slug in SELECTED and ("selected", "true") not in fields:
        fields.append(("selected", "true"))
    if slug in AWARDS:
        name, desc = AWARDS[slug]
        fields += [("award_name", name), ("award", desc)]
    if os.path.isfile(bibpath):
        with open(bibpath, encoding="utf-8") as f:
            bibtext = f.read().strip()
        bibtext = set_title(bibtext, fm.get("title"))  # match the live site's index.md title
        bibtext = set_year(bibtext, derive_year(fm))    # match the live site's date-based year
        bibtext = inject(bibtext, fields)
        enriched += 1
    else:
        bibtext = synthesize(fm, slug)
        bibtext = inject(bibtext, fields)
        synthesized += 1
    entries.append((clean(fm.get("date")), bibtext))

entries.sort(key=lambda x: x[0], reverse=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("---\n---\n\n")
    f.write("\n\n".join(e[1] for e in entries) + "\n")

print(f"Wrote {len(entries)} entries -> {OUT}")
print(f"  from existing cite.bib: {enriched}")
print(f"  synthesized (no cite.bib): {synthesized}")
