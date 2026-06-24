#!/usr/bin/env python3
"""Convert Wowchemy content/project/*/index.md -> al-folio _projects/*.md"""
import os, re, glob

SRC = "/Users/p.pandey/sandbox/personal/personal_website/content/project"
OUT = "/Users/p.pandey/sandbox/personal/personal_website_alfolio/_projects"

def parse(path):
    fm = {}
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    body = text[m.end():].strip() if m else ""
    block = m.group(1) if m else ""
    cur = None
    for line in block.splitlines():
        mm = re.match(r"^([A-Za-z_]\w*):\s?(.*)$", line)
        if mm:
            cur = mm.group(1)
            fm[cur] = mm.group(2).strip().strip('"').strip("'")
        elif re.match(r"^\s*-\s", line) and cur:  # list item (e.g. tags, links)
            fm.setdefault(cur + "_list", []).append(line.strip()[1:].strip())
    return fm, body

# clear al-folio demo projects
for f in glob.glob(os.path.join(OUT, "*.md")):
    os.remove(f)

i = 0
for d in sorted(glob.glob(os.path.join(SRC, "*"))):
    idx = os.path.join(d, "index.md")
    if not os.path.isfile(idx):
        continue
    i += 1
    fm, body = parse(idx)
    slug = os.path.basename(d)
    title = fm.get("title", slug).strip()
    desc = fm.get("summary", "") or fm.get("image_caption", "")
    out = [f"---", "layout: page", f"title: {title}",
           f"description: {desc}", "img: assets/img/12.jpg",
           f"importance: {i}", "category: research", "---", "",
           body or f"{title}."]
    with open(os.path.join(OUT, f"{i}_{slug}.md"), "w", encoding="utf-8") as fo:
        fo.write("\n".join(out) + "\n")
    print(f"  {slug} -> {i}_{slug}.md   (title: {title[:50]})")

print(f"Converted {i} projects.")
