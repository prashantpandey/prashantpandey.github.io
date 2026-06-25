---
layout: page
title: Fast and Space-Efficient In-Memory Indexes (Hash Tables, B-trees)
description: Cache- and space-efficient in-memory hash tables and ordered indexes for scalable systems.
img: assets/img/projects/inmemoryindexes.png
importance: 5
category: research
related_publications: true
---

In-memory indexes — hash tables and ordered structures like B-trees — sit on the critical path of modern data systems. This project designs indexes that are simultaneously fast, space-efficient, and concurrency-friendly.

We built IcebergHT {% cite DBLP:journals/pacmmod/0001BCFKTJ23 %}, a high-performance hash table with stability and low associativity, and Zombie Hashing {% cite DBLP:journals/pacmmod/ChesettiSPP25 %}, which reclaims the cost of tombstones in deletion-heavy workloads. For ordered data we designed the BP-tree {% cite DBLP:journals/pvldb/0001LWM023 %} and a locality-optimized, concurrent in-memory B-skiplist {% cite icpp25 %}, and we have studied how learned indexes perform for external-memory joins {% cite chesetti2025evaluating %}.
