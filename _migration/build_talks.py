#!/usr/bin/env python3
"""Convert Wowchemy content/event/*/index.md -> al-folio _talks/*.md"""
import os, re, glob

SRC = "/Users/p.pandey/sandbox/personal/personal_website/content/event"
OUT = "/Users/p.pandey/sandbox/personal/personal_website_alfolio/_talks"

def parse(path):
    fm = {}
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    body = text[m.end():].strip() if m else ""
    block = m.group(1) if m else ""
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip(); i += 1
        mm = re.match(r"^([A-Za-z_]\w*):\s?(.*)$", line)
        if not mm:
            continue
        k, v = mm.group(1), mm.group(2).strip()
        if v.startswith('"') and not (v.endswith('"') and len(v) > 1):
            while i < len(lines) and '"' not in lines[i]:
                v += " " + lines[i].strip(); i += 1
            if i < len(lines):
                v += " " + lines[i].strip(); i += 1
        fm[k] = v.strip().strip('"').strip("'")
    return fm, body

def clean(v):
    return (v or "").strip().strip('"').strip("'")

os.makedirs(OUT, exist_ok=True)
for f in glob.glob(os.path.join(OUT, "*.md")):
    os.remove(f)

n = 0
for d in sorted(glob.glob(os.path.join(SRC, "*"))):
    idx = os.path.join(d, "index.md")
    if not os.path.isfile(idx):
        continue
    fm, body = parse(idx)
    slug = os.path.basename(d)
    title = clean(fm.get("title")) or slug
    date = clean(fm.get("date"))[:10]   # YYYY-MM-DD
    if not date:
        continue
    n += 1
    out = ["---", "layout: page", f'title: "{title}"', f"date: {date}",
           f'event: "{clean(fm.get("event"))}"',
           f'location: "{clean(fm.get("location"))}"']
    for src, dst in [("event_url", "url"), ("url_slides", "slides"),
                     ("url_video", "video"), ("url_pdf", "pdf")]:
        val = clean(fm.get(src))
        if not val:
            continue
        if dst != "url" and not val.startswith("http"):
            val = "/assets/pdf/" + val.lstrip("/")   # local uploads PDF
        out.append(f'{dst}: "{val}"')
    out += ["---", "", clean(fm.get("abstract")) or clean(fm.get("summary")) or body or ""]
    with open(os.path.join(OUT, f"{date}-{slug}.md"), "w", encoding="utf-8") as fo:
        fo.write("\n".join(out).rstrip() + "\n")

print(f"Converted {n} talks -> {OUT}")
