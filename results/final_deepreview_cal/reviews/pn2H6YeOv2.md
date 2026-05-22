Now I have all the information needed. Let me produce the final consolidated review.

## Summary

PI-CCA proposes a replay-free continual learning framework for vision-language models that reframes catastrophic forgetting as alignment-geometry drift. Instead of regularizing proxy signals (logits, similarities), it preserves a compact "CCA certificate" — the top-*k* canonical correlations and sketched subspaces of the whitened cross-modal covariance — across tasks using only mini-batch statistics and exponential moving averages, with an added prompt-invariance mechanism. The method achieves state-of-the-art results among replay-free methods on MTIL, X-TAIL, VLCL, and ConStruct-VL benchmarks, supported by comprehensive ablations and analyses.

## Strengths

- **Conceptually novel reframing of forgetting as alignment-geometry drift.** Rather than matching logits, similarities, or parameters, PI-CCA directly preserves the canonical spectrum and subspaces of the whitened cross-covariance — the underlying object that drives CLIP's zero-shot retrieval and recognition. This geometry-first perspective is a principled departure from prior VL-CL methods that act on proxy signals. (Sec. 1, Sec. 2)

- **SOTA among replay-free methods across four benchmarks.** PI-CCA achieves the highest scores on MTIL (Avg 76.8 vs. next best 75.2), X-TAIL (Avg 68.1 vs. 67.4), VLCL retrieval (I2T R@1 48.6 vs. 47.3 of the synthetic-replay method GIFT), and ConStruct-VL (FA 75.2, AF 2.7). It even surpasses GIFT, which uses diffusion-generated synthetic replay, without storing or generating any data. (Tables 1, 2, Sec. 4.2)

- **Replay- and generator-free with constant memory.** The certificate stores only a sketched summary (spectrum + subspaces) whose size is independent of feature dimensions, using random orthonormal sketches. No exemplar buffers, generators, or task-specific metadata are required. (Sec. 3.2)

- **Thorough ablation isolating each component's contribution.** Table 3 cleanly shows that removing the spectral term or subspace term causes the largest drops (MTIL Avg −2.5 and −2.2 p.p.), confirming both are necessary. Ablations of covariance EMA, prompt invariance, certificate EMA, sketching type, and Hungarian vs. sorted pairing are all provided. (Sec. 4.3, Table 3)

- **Robustness to task order and certificate capacity.** 20 random task-order permutations show narrow IQRs (~0.5 p.p. for Avg), and the Pareto sweep over *k* and *h* (Fig. 2) reveals a broad robust ridge, confirming the method does not rely on a specific configuration or lucky ordering. (Fig. 2, Fig. 5, Sec. 4.3)

## Weaknesses

### Fatal
None.

### Major

1. **Implausible perfect correlations in the geometry–performance analysis (Fig. 3).** The paper reports Pearson *r* = 1.00 and Spearman *ρ* = 1.00 for the relationship between subspace-angle drift and accuracy drop, and *r* = 0.99 / *ρ* = 1.00 for spectral drift. These values are physically impossible on any real experimental data that exhibits the "realistic scatter" the caption itself describes — any measurement noise, rounding, or stochasticity would produce correlations strictly below 1.0. The figure caption also mentions a 95% confidence interval shaded area, which would be degenerate (zero width) at *r* = 1.00. This suggests either a rounding artifact (e.g., *r* = 0.9997 truncated to 1.00), a computation error, or that the data points are not as independently sampled as claimed. This does not invalidate the paper's core results (Tables 1–2) but undermines trust in the analysis section and must be corrected or explained. (Fig. 3, Sec. 4.3)

2. **Missing variance measures in the headline classification results (Table 1).** Table 1 reports MTIL and X-TAIL accuracies without any error bars or confidence intervals, while Table 2 provides ± intervals for retrieval and ConStruct-VL results. The paper mentions 3 random seeds only in the Fig. 5 caption but does not state that Table 1 values are averaged over multiple seeds or report their variance. Given that the gains over the next-best method are 0.7–1.6 points, variance reporting is essential to establish that these differences are statistically significant. This is a basic methodological requirement for a SOTA claim. (Table 1 vs. Table 2, Sec. 4.2)

### Minor

3. **The geometry drift measures are closely related to the losses being regularized, limiting their value as independent evidence.** D_ang (sum sin² θ_i) and ℒ_sub (Frobenius distance of sketched projectors) are different but closely related quantities; D_ρ (L2 norm of spectral difference) is the unsquared precursor of the first term in ℒ_spec. The correlation analysis in Fig. 3 therefore shows that when PI-CCA's own losses are better satisfied, performance is better — which is informative but not the independent corroboration the paper frames it as. A stronger test would correlate performance with a drift measure *not* explicitly regularized by PI-CCA (e.g., CKA distance, mutual information gap). (Sec. 4.3; compare D_ang/ℒ_sub definitions in Sec. 3.3)

4. **Gains over strong baselines are modest on some tracks.** On MTIL, the margin over C-CLIP is 1.6 points (Avg) / 1.7 points (Last); on X-TAIL, the margin over RAIL is 0.7 points (Avg). While consistent and in the right direction, these are incremental improvements. The paper acknowledges this implicitly but could be more transparent about the modest effect sizes on certain benchmarks. (Table 1)

### Trivial
None.

## Nice-to-Haves

- **Compare to a small-buffer replay baseline.** The paper positions itself as replay-free but does not quantify how much memory a small replay buffer (e.g., 200 samples per task) would require or how much PI-CCA closes the gap with such a baseline. A small comparison table would contextualize the replay-free claim.
- **Report raw zero-shot accuracy numbers.** The paper mentions *PD* (performance drop) on a held-out zero-shot suite but does not report the raw zero-shot accuracy values before and after continual learning — only relative PD in the prompt invariance stress test (Fig. 4). A table with absolute numbers would strengthen the zero-shot retention claim.
- **Specify which perturbation types are used for the main results.** The text mentions "synonym swap/back-translation/template jitter" for the stress test but does not clearly state which perturbation strategy is deployed in the main experiments (Sec. 4.2, Tables 1–2). This detail is likely in the appendix but should be explicit in the main text.

## Removed Points
- *"Overclaimed geometry–performance correlation (Fig. 3) ... D_ang and D_ρ are exactly the losses being optimized (ℒ_sub and ℒ_spec, up to constants)."* — Removed because D_ang measures principal angles in original space while ℒ_sub operates on sketched projectors, and D_ρ is an unsorted L2 norm while ℒ_spec uses sorted squared L2 plus a Ky-Fan term. They are related but not identical. The concern about circularity is retained in Minor #3 in a softened form. The valid concern about r=1.00 is retained as Major #1.
- *"Reproducibility of the full procedure — many interlocking components, relies heavily on appendix material (A.1, A.2, A.3, A.4)."* — Removed per hard rules: the appendix exists in the original submission and was stripped by the parser. The reproducibility statement details hyperparameters explicitly.
- *"No measure of variance appears for classification tasks. The paper claims 3 random seeds are used (stated in methods section)"* — The "3 seeds" mention only appears in Fig. 5's caption, not in the methods section. The core concern (missing variance in Table 1) is retained as Major #2; the inaccurate attribution is removed.
- *Strength: "Geometry‑performance correlation supporting the core hypothesis (Pearson r up to 1.00, Spearman ρ up to 1.00)."* — Removed as a strength because the r=1.00 values themselves indicate a computation issue that undermines this evidence.

## Novel Insights
The key insight that emerges from the interplay between the reviewer criticism and the paper's actual content is the tension between the paper's framing of the correlation analysis as "independent evidence" and the reality that the drift measures closely track the regularized losses. A genuinely stronger evidence design would compare PI-CCA's observed forgetting to a drift metric *not* part of its optimization — for instance, measuring how much the CKA or mutual information between modalities changes, and correlating that with performance. This design would separate the claim "preserving CCA geometry predicts retention" from the weaker claim "when PI-CCA works well, its own loss terms are small." The paper already has the experimental infrastructure to run such a test and would benefit from doing so.

## Suggestions

1. **Recompute or properly report the correlations in Fig. 3.** If the values are 0.9997 rounded to 1.00, report them to a precision that honestly reflects the scatter. If the computation is correct, explain how perfect correlations arise given the visible scatter and the 95% CI shaded area. If a bug exists, fix it and re-run.
2. **Add standard deviations or confidence intervals to Table 1** for the classification results, consistent with the reporting in Table 2.
3. **Add a brief discussion** acknowledging that D_ang/D_ρ are closely related to the regularized losses, and therefore the correlation analysis is not fully independent evidence. This would strengthen rather than weaken the paper by demonstrating self-awareness.
4. **Report absolute zero-shot accuracy** on the held-out suite before and after continual learning, not just PD.

## Score and Decision

**Calibration:**

Round 1 bracket: [3.5, 7.5]

Anchors retrieved and evaluated:
- C-CLIP (6.5, Accept) — Directly comparable VL-CL paper with SOTA results. PI-CCA has a more novel conceptual contribution but weaker analysis rigor (r=1.00 issue). Slightly below C-CLIP.
- TiC-CLIP (6.25, Accept) — CLIP continual training paper. PI-CCA has stronger methodological novelty but less comprehensive benchmarking scope.
- PROOF (5.67, Reject) — VLM class-incremental learning. PI-CCA is clearly more novel and better supported.
- Vision+Language Synergy (5.0, Accept) — Prompt-based CL with language guidance. PI-CCA has a stronger conceptual contribution and better-controlled experiments.
- LLaCA (5.33, Reject) — MLLM continual instruction tuning. PI-CCA demonstrates stronger methodological novelty.
- Incrementally Adapting Generative VLMs (4.67, Reject) — Task codebook approach. PI-CCA is clearly stronger.

Round 2 narrowing: PI-CCA sits above the 5.0–5.67 range but below C-CLIP (6.5). The conceptual novelty *and* strong empirical evaluation (four benchmarks, comprehensive ablations) place it closer to 6.0 than to 5.5, but the r=1.00 issue and missing Table 1 variance prevent it from reaching the C-CLIP level.

**Final score:** 6.0  
**Decision:** Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>