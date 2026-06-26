---
layout: page
title: A Compact, Dynamic, and Distributed GPU Data Structure Library
description: Compact, dynamic, and distributed data structures that exploit the massive parallelism of GPUs.
img: assets/img/projects/gpu.png
importance: 3
category: research
related_publications: true
---

GPUs offer enormous parallelism but are notoriously difficult to use for dynamic, pointer-based data structures. This project builds a library of compact and dynamic GPU data structures, together with the memory-management substrate they need.

We built Gallatin {% cite DBLP:conf/ppopp/McCoyP24 %}, a general-purpose GPU memory manager, and WarpSpeed {% cite alenex25 %}, a high-performance library of concurrent GPU hash tables. On top of these we have designed high-performance filters for GPUs {% cite DBLP:conf/ppopp/McCoyHY023 %} and distributed-memory $k$-mer counting on GPUs {% cite DBLP:conf/ipps/NisaPEOBY21 %}.
