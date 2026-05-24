Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces INFOTok, an adaptive discrete video tokenization framework that dynamically determines token length per video using an ELBO-based router and a transformer-based adaptive compressor. The method is grounded in Shannon information theory (the paper proves existing uniform routers are suboptimal and its own router is near-optimal under stated conditions) and builds on top of existing fixed-length tokenizers (specifically Cosmos). Experiments on two video reconstruction benchmarks show INFOTok saves ~20% tokens over Cosmos-DV at equivalent reconstruction quality, outperforms the prior adaptive method ElasticTok by 1.0–2.0 PSNR at the same compression rate, and requires only 1 additional network evaluation versus ElasticTok's 11.

## Strengths

1. **Significant practical improvement over the prior adaptive method.** At the same compression rate (BPP₁₆=0.56 on TokenBench), INFOTok achieves PSNR 29.27 vs. ElasticTok's 27.34 (Table 1), with FVD roughly 3× lower (70 vs. 194). At BPP₁₆=0.81 it matches Cosmos-DV's reconstruction quality while using 19% fewer tokens. These gains are substantial and clearly demonstrated.

2. **ELBO-based routing is shown to be near-optimal via exhaustive-search ablation.** Table 2 compares INFOTok's routing against an oracle that searches over all possible token lengths and solves a dataset-level optimization problem. At BPP₁₆=0.81, INFOTok-Flex (PSNR 29.86) is within 0.06 dB of this upper bound (PSNR 29.92). This is strong evidence that the routing mechanism works despite using the fixed-length tokenizer's ELBO as a proxy.

3. **Ablations isolate the contributions of individual components.** Table 3 (Left) compares three masking strategies for the compressor (R2L, Jump, and the proposed ELBO-based masking) under the same router, cleanly showing that ELBO-based token selection drives quality. Table 3 (Right) swaps adaptive mechanisms across two backbones, confirming that INFOTok's mechanism consistently beats ElasticTok's regardless of architecture.

4. **General and architecture-agnostic framework.** INFOTok wraps existing fixed-length tokenizers (encoder + decoder) with a plug-in router and compressor, and the ablation on a pure Vision Transformer backbone (Table 3 Right) shows the mechanism works beyond the Cosmos architecture used for the main results.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No ablation isolating adaptivity from added transformer capacity.** INFOTok adds an 8-layer transformer for the adaptive compressor/decompressor. There is no baseline that adds the same transformer capacity to Cosmos *without* adaptive token length selection (i.e., fixed length, no router/masking). Such a baseline would clarify how much of the gain comes from content-adaptive allocation vs. simply having more model capacity. The paper's central narrative attributes improvement to the information-theoretic routing, but this attribution would be stronger with this controlled comparison.

2. **No downstream task validation despite the stated motivation.** The paper motivates adaptive tokenization by its potential to improve "video-understanding or generation tasks" and "scalable multimodal models," but evaluates only reconstruction metrics. The paper transparently scopes this out (Section 4: "training a video generative model is extremely resource-consuming and is beyond our scope"; Section 6 acknowledges this as a limitation). This does not invalidate the tokenization contribution — reconstruction fidelity is the standard evaluation for tokenizer papers (VQGAN, Cosmos, etc.) — but a small-scale generation experiment (e.g., training a simple autoregressive model on INFOTok tokens) would substantially strengthen the paper's narrative.

3. **No error bars or statistical significance reported.** FVD in particular is known to be noisy; single-run point estimates (Table 1) make it difficult to assess whether observed differences are meaningful. Reporting confidence intervals or results over multiple seeds would improve reliability.

4. **Missing transparency on how ElasticTok's loss thresholds were selected** to match the two specific BPP values (0.81, 0.56). The paper states "we align our methods with their settings" but does not report what thresholds were used. This makes full reproduction and assessment of the comparison's fairness more difficult.

5. **The per-token ELBO masking in the compressor is heuristically motivated**, not derived from the source coding theorems. The theorems dictate the *total* token count per video, but the compressor selects *which* individual tokens to drop using per-token ELBO values. The ablation (Table 3 Left) shows it works, but a comparison against random masking at the same length (the null hypothesis for adaptivity within a video) is missing and would strengthen the justification.

### Trivial
- The introduction claims "approximately 50% tokens without loss of reconstruction quality" (line 49), which is more aggressive than the 20% figure supported by Table 1. At BPP₁₆=0.56 (~44% reduction vs. Cosmos-DV 1.00), PSNR drops from 30.01 to 29.27 and FVD rises from 49 to 70. The abstract's 20% claim is well-supported; the 50% claim in the introduction is overstated.

## Nice-to-Haves
- **Wall-clock latency comparison** alongside NFEs: the paper mentions "more details regarding wall-clock inference latency comparison can be found in Appendix D" (which is not available here), bringing this comparison into the main text would strengthen the efficiency claims.
- **Visualization of per-token ELBO maps** compared to reconstruction error heatmaps, to make the mechanism's behavior more interpretable.
- **Histogram of assigned token lengths** across a dataset for INFOTok-Flex at a fixed β, to directly demonstrate adaptivity in practice.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh critic claim that the 20% token savings claim is unsupported** — The critic asserts this is contradicted by Table 1 at BPP₁₆=0.56, but the 20% savings claim refers to the BPP₁₆=0.81 vs. 1.00 comparison (InfoTok PSNR 30.08 vs. Cosmos-DV 30.01, FVD 49 vs. 49). This is a factual misreading by the reviewer; the claim is well-supported.
- **Criticism that Theorem 2.2 is framed as a "fundamental limitation" when it is only a worst-case construction** — The paper explicitly frames it as demonstrating "the fundamental limitation of data-agnostic router for training" and provides an intuition paragraph with a concrete example. The framing is appropriate for a theoretical result of this type.
- **Criticism that Theorem 3.1's optimality condition is impossible** — The paper states "if the tokenizer manages to minimize the reconstruction loss" as a conditional; this is standard practice for theoretical bounds in ML papers, and the empirical validation (Table 2) shows the method works near-optimally despite the idealized condition.
- **Criticism about NFEs vs. wall-clock time** — The paper explicitly cites Appendix D for wall-clock details; this material existed in the original submission and was stripped by the parser.
- **Request for theoretical explanation of why fixed-length ELBO predicts adaptive optimal length** — The paper provides an explanation: ELBO is a lower bound on log-likelihood, and optimal token length is proportional to -log p(x). Table 2 validates this empirically. The request is already addressed.
- **Generic sweep concerns about "could the metric be measuring a proxy"** — These are speculative and not anchored to specific evidence in the paper.

## Novel Insights
None beyond the paper's own contributions. The innovative connection between ELBO (from VAE-style tokenizers) and the information-theoretic optimal token length via Shannon's source coding theorem is the paper's own contribution, not an insight from the reviews.

## Suggestions
1. **Run the controlled ablation**: Add the same 8-layer transformer capacity to Cosmos without adaptive routing/masking (fixed token length) and compare at the same BPP to isolate how much gain comes from adaptivity vs. model capacity.
2. **Report error bars** for all metrics (especially FVD), either over multiple seeds or via bootstrapping.
3. **Report ElasticTok's loss thresholds** used to obtain BPP₁₆ = 0.81 and 0.56 to improve reproducibility.
4. **Add a random-masking baseline** for the compressor (same token budget as INFOTok, but dropping random tokens instead of ELBO-selected ones) to confirm that the per-token selection scheme is driving the improvement.
5. **Consider a small-scale downstream experiment** (e.g., training an autoregressive transformer on INFOTok tokens and measuring generation FVD) to validate the claimed practical impact.

## Score and Decision

**Score**: 7.5

**Decision**: Accept

This is a well-executed paper with a principled motivation, clean ablations, and substantial empirical improvements over the prior adaptive baseline. The weaknesses (missing controlled ablation for adaptivity vs. capacity, no downstream validation, no error bars) are real but do not undermine the core contribution: a demonstrably better adaptive video tokenizer with strong empirical support. The theoretical framing is a genuine strength (it motivates the algorithm and the near-optimality of the routing is empirically validated) even if the gap between idealized theory and practical algorithm is not fully closed. The paper's limitations are honestly discussed. The contribution is solid and the paper merits acceptance.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>