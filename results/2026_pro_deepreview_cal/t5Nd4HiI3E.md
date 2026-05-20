Now I have a thorough understanding of both the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

This paper addresses the alignment of Large Reasoning Models (LRMs) with human preferences — an underexplored problem. The core challenge is that LRMs generate intermediate reasoning traces, and the standard DPO approximation (using a single sampled trace) produces high-variance gradients due to stochastic trace sampling. The authors propose BVPO, which mixes the high-variance trace-based gradient with a low-variance empty-trace gradient (conditioned on an empty reasoning trace) via a convex combination. They provide theoretical analysis framed through bias-variance optimization and MSE minimization, and demonstrate empirical improvements over DPO and SimPO on AlpacaEval 2, Arena-Hard, and math reasoning benchmarks across three LRMs.

## Strengths

- **Novel problem identification**: The paper correctly identifies that gradient variance from stochastic trace sampling is a genuine bottleneck for LRM alignment — an issue absent from standard LLM alignment literature, which was developed for models that don't externalize long reasoning traces. This is a real and timely problem as LRMs become increasingly deployed.

- **Simple, practical method**: BVPO is straightforward to implement — it augments standard DPO training with an additional loss term computed on empty-trace data, requiring no architectural changes or additional models. The empty-trace data is obtained by simply appending `