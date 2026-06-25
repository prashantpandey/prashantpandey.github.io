---
layout: page
title: Scalable and Real-Time Stream Monitoring using External Memory
description: External-memory data structures for real-time monitoring of high-velocity data streams.
img: assets/img/projects/streaming.png
importance: 6
category: research
related_publications: true
---

Many monitoring tasks — finding heavy hitters, detecting events, flagging security anomalies — must keep up with high-velocity streams while retaining long histories that far exceed RAM. This project designs external-memory data structures that report results in real time without sacrificing throughput.

We developed external-memory structures for the timely reporting of heavy hitters {% cite DBLP:conf/sigmod/Pandey0BBFJKP20 %} and formalized the online event-detection problem {% cite DBLP:journals/corr/abs-1812-09824 %}. Building on SSD-aware sketches {% cite DBLP:conf/esa/GoswamiMMP18 %}, we applied these ideas to responsive, large-scale security monitoring {% cite vorobyeva2022using %}.
