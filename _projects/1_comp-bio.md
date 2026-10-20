---
layout: page
title: Scalable, Real-Time, and Information-Rich Sequence Search Over SRA
description: Compact, exact, and incrementally updatable indexes for searching petabyte-scale sequencing data.
img: assets/img/projects/comp-bio.png
importance: 2
category: research
related_publications: true
---

The Sequence Read Archive (SRA) holds petabytes of raw sequencing data, but searching it for a given sequence has long been impractical at scale. This project builds compact, exact, and information-rich indexes that make large-scale sequence search fast and space-efficient.

Most recently, we enabled noise-robust DNA search at SRA scale via local-alignment embeddings with LOCALE {% cite biorxiv26_locale %}. We introduced Squeakr {% cite DBLP:journals/bioinformatics/PandeyBJP18 %} for fast and compact $k$-mer counting, and the Mantis system {% cite DBLP:conf/recomb/PandeyABFJP18 DBLP:conf/recomb/AlmodaresiPFJP19 %} for exact, large-scale sequence search. These build on succinct colored de Bruijn graph representations such as deBGR {% cite DBLP:journals/bioinformatics/PandeyBJP17 %} and Rainbowfish {% cite DBLP:conf/wabi/AlmodaresiPP17 %}. We made the search index incrementally updatable {% cite almodaresi2022incrementally %}, extended the approach to genomic variant search with VariantStore {% cite pandey2021variantstore %}, and scaled colored compacted de Bruijn graph construction to massive datasets with Cuttlefish 3 {% cite recomb26 %}. We continue to push toward faster and distributed search: accelerating streaming $k$-mer operations with a dynamic, concurrent, cache-efficient hash table {% cite biorxiv26_kachehash %} and balancing load across distributed genomic indices {% cite biodms26_loadbalance %}.
