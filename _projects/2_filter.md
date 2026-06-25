---
layout: page
title: Adaptive and High-performance Filters for Modern Workloads
description: Theoretically grounded, high-performance filters (approximate membership data structures) for modern workloads.
img: assets/img/projects/filter.jpg
importance: 2
category: research
related_publications: true
---

Filters — approximate membership data structures like the Bloom filter — are everywhere in storage systems, databases, networking, and computational biology. This project rethinks filter design to be simultaneously fast, space-efficient, feature-rich, and theoretically grounded.

We introduced the counting quotient filter {% cite DBLP:conf/sigmod/PandeyBJP17 %}, which packs more functionality into less space, and the vector quotient filter {% cite DBLP:conf/sigmod/PandeyCDBFJ21 %} for high throughput on modern hardware. More recent work makes filters adaptive to their workloads {% cite DBLP:journals/pacmmod/WenMTTBCFJP24 sigmod26_smart %}, strongly and monotonically adaptive over ranges {% cite sigmod26_aeris %}, and fully featured {% cite sigmod26_bread %}. We have also designed filters for similarity search over trajectories {% cite DBLP:conf/apocs/BhatC0023 %} and for GPUs {% cite DBLP:conf/ppopp/McCoyHY023 %}, and surveyed the emerging design space in a tutorial {% cite DBLP:conf/sigmod/0001FDZ24 %}.
