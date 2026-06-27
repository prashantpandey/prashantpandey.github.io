---
layout: page
title: students
permalink: /students/
description: Students & Postdocs
nav: true
nav_order: 7
---

- [Jamshed Khan](https://sites.google.com/view/jamshed/home) — Khoury Distinguished Postdoc (Started Fall 2025)
- [Hunter McCoy](https://huntermberkeley.github.io/) — PhD (Started Fall 2022)
- [Yuvraj Chesetti](https://droidkid.github.io/) — PhD (Started Fall 2023)
- [Zikun Wang](https://www.zikunw.com/) — PhD (Started Fall 2025)
- [Quynh Pham](https://www.linkedin.com/in/quynhdp/) — PhD (Starting Fall 2026)

## Lab life

Beyond research, we enjoy spending time together — hikes, runs, and dinners.

<!--
  Responsive photo grid (3 per row on desktop, fewer on mobile). Photos and
  captions live in _data/lab_photos.yml and are sorted by date (newest first).
  To add/remove a photo, edit that file (see README → "Lab photo gallery").
-->
{% assign lab_photos = site.data.lab_photos | sort: "date" | reverse %}
<div class="row row-cols-1 row-cols-md-3 g-3 mt-2">
  {% for photo in lab_photos %}
  <div class="col">
    {% include figure.liquid loading="eager" path=photo.image class="img-fluid rounded" caption=photo.caption %}
  </div>
  {% endfor %}
</div>
