---
layout: page
title: Data Systems for Efficient LLM Training and Inference
description: GPU-native data structures and algorithms for scalable LLM training data processing, long-context inference, and serving.
img: assets/img/projects/llm.jpg
importance: 7
category: research
related_publications: true
---

Large language models push data systems to their limits at every stage of their lifecycle: training corpora reach trillions of tokens, long-context decoding is dominated by attention over an ever-growing KV cache, and serving personalized models to many users strains GPU memory. This project applies ideas from compact, GPU-accelerated, and external-memory data structures to make LLM training and inference faster and more scalable.

On the training side, we built Cascade {% cite arxiv26_cascade %}, a GPU-accelerated, out-of-core suffix array construction algorithm that scales full-text indexing to LLM-sized corpora that far exceed GPU memory. On the inference side, Iceberg Attention {% cite preprint26_iceberg %} achieves sublinear long-context decoding by summarizing attention with a Mixture-of-Gaussians, and InferScale {% cite arxiv26_inferscale %} enables personalized LLM serving through GPU-native KV injection. This work draws on our broader effort in GPU data structures, memory management, and vector indexes.
