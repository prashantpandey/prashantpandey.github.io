---
layout: page
title: GPU-Accelerated Vector Indexes for Approximate Nearest-Neighbor Search
description: Compact, updatable vector indexes that exploit GPU parallelism for fast approximate nearest-neighbor search.
img: assets/img/projects/gpu.png
importance: 6
category: research
related_publications: true
---

Approximate nearest-neighbor search (ANNS) over high-dimensional vectors underpins modern retrieval, recommendation, and retrieval-augmented generation. Serving these workloads at scale demands indexes that are both fast and memory-efficient, yet most high-performance ANNS indexes are static and must be rebuilt to absorb new data. This project designs GPU-accelerated vector indexes that are compact enough to fit large datasets in GPU memory and dynamic enough to ingest updates in place.

We built Jasper {% cite arxiv26_jasper %}, a GPU-accelerated ANNS index that uses quantization to shrink the memory footprint while sustaining high query throughput, and supports in-place updates so the index can evolve with the data instead of being rebuilt. This work draws on our broader effort in compact and dynamic GPU data structures and the memory-management substrate they rely on.
