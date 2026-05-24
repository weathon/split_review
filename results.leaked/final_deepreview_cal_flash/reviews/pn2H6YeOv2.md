Now I have all the information needed. Let me construct the consolidated review.

## Summary

Pi-CCA introduces a replay-free continual learning framework for vision-language models that explicitly preserves the geometry of cross-modal alignment (canonical correlations and subspaces) via a compact sketched CCA certificate. The method adds prompt invariance through projector averaging over text perturbations. Across four standard VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), Pi-CCA achieves state-of-the-art results among replay-free methods, outperforming strong baselines including C-CLIP, RAIL, and even the synthetic-replay method GIFT.

## Strengths

- **State-of-the-art replay-free performance across diverse VL-CL tracks.** Pi-CCA achieves the highest numbers among replay-free methods on MTIL (Avg 76.8, Last 75.5, Transfer 73.2) and X-TAIL (Avg 68.1, Last 66.9, Transfer 64.7) in Table 1, and on VLCL I2T R@1 (48.6), T2I R@1 (37.4), and ConStruct-VL FA/AF in Table 2. These gains are consistent across four different benchmarks spanning classification, retrieval, and structured-concept matching.

- **Principled geometry-first innovation.** Rather than regularizing proxy signals (logits, similarities, parameters), the core idea directly constrains the canonical spectrum and subspaces of the whitened cross-covariance — the actual object underlying CLIP's retrieval and zero-shot behavior. Table 3 confirms that removing either the spectral term (ℒ_spec, λ₁=0) or the subspace term (ℒ_sub, λ₂=0) causes the largest performance drops (2.5 and 2.2 p.p. on MTIL Avg), indicating both invariants are essential and the method is indeed targeting alignment geometry, not a surrogate.

- **Prompt invariance mechanism is shown to be effective.** Figure 4 shows that ℒ_pi (Equation 11) flattens degradation slopes under both in-distribution and out-of-distribution prompt perturbations, improving R@1 by ~2.5 p.p. at s=1.0 and reducing ConStruct-VL AF by ~1.0. This provides direct evidence for improved prompt robustness.

- **Comprehensive and well-designed ablation study.** Table 3 systematically ablates each component (spectral term, subspace term, prompt invariance, certificate EMA, covariance EMA, spectral moments, pairing strategy, sketch type). Each removal hurts performance, demonstrating that all mechanisms are necessary. The sensitivity analyses (Figure 2, Figure 5) are thorough.

- **Replay-free and constant-memory by design.** The certificate uses random orthonormal sketches (h×k with h≪d_v, d_t), achieving constant storage independent of feature dimensions. Figure 2 shows an efficient Pareto frontier with a clear knee at (k=64, h=256).

## Weaknesses

### Fatal
None.

### Major

- **Suspiciously perfect correlation values in the geometry–performance analysis (Figure 3).** The figure reports Pearson r = 1.00 and Spearman ρ = 1.00 for the relationship between subspace-angle drift and performance drops (ΔAvg and ΔR@1), and r = 0.99 / ρ = 1.00 for spectral drift. A perfect linear correlation (r = 1.00) with no residual scatter is implausible when sweeping multiple independent hyperparameters (certificate size, EMA rates, invariance strength, whitening, pairing, LoRA capacity, learning rate, sketch type). The figure caption in the paper itself mentions "realistic scatter" but the annotated r = 1.00 contradicts this. While the values could be rounding artifacts (e.g., 0.9995 → 1.00 with two decimal places), the paper does not clarify the number of data points, show the raw scatter unambiguously, or explain why the relationship appears near-deterministic. This does **not** invalidate the paper's main empirical results (Tables 1–3), but it weakens the secondary claim that CCA geometry drift "directly and linearly explains" performance trends. The authors should clarify this in revision — show the actual scatter plot with raw points, report the number of configurations, and discuss whether the tightness is expected because drift is directly penalized during training.

### Minor

- **Backbone architecture not specified in the main text.** The paper never states which CLIP variant (e.g., ViT-B/32, ViT-L/14) is used for the vision and text encoders. The reproducibility statement promises these details in Appendix §A.2, but the main experimental setup section (4.1) should be self-contained for a quick reader. This is a transparency issue that makes it harder to verify that comparisons across baselines are controlled for backbone and adapter capacity.

- **Missing variability estimates in Table 1.** Table 2 (VLCL, ConStruct-VL) reports standard deviations (±), but Table 1 (MTIL, X-TAIL) does not. This inconsistency makes it difficult to assess the reliability of the reported gains on the classification tracks. Reporting variability (even from 3 seeds) would strengthen the empirical claims.

- **The paper treats the r=1.00 correlation as evidence for a causal claim without discussing possible confounding.** The geometry drift and downstream performance could both be driven by a third factor (e.g., the degree of distribution shift), rather than the drift itself causing the performance drop. A brief discussion of this — or a controlled experiment — would strengthen the causal interpretation. (This is related to the Major point above.)

### Trivial

- The method description is dense and could benefit from a more accessible high-level summary before the equations. Some notation (e.g., the distinction between P*, S*, Q*) requires careful tracking across Section 3.

## Nice-to-Haves

- Include a direct efficiency comparison with top baselines. The Pareto analysis in Figure 2 tunes Pi-CCA's internal hyperparameters but does not show where competing methods (e.g., C-CLIP, RAIL) lie on the same memory/performance trade-off. Adding a few external baselines would strengthen the claim that Pi-CCA is practical.

- Add a brief limitations paragraph in the main paper (the current conclusion defers everything to the appendix). Discussing when the CCA certificate might be less effective (e.g., tasks requiring large shifts in alignment, sensitivity to EMA parameters) would improve completeness.

- Clarify the number of data points and show raw scatter for Figure 3 (related to the Major weakness above).

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Strength #5 from Strength Finder** ("Strong geometry-performance correlation supporting the causal claim"): Dropped because it conflicts with the verified weakness about suspicious r=1.00 correlation values. The weakness questions the credibility of the evidence that the strength relies on. Per protocol, the weakness wins.

- **Harsh critic's point about computational cost not being discussed:** The Pareto analysis in Figure 2 *does* discuss computational cost (memory and step time) in the main text. This criticism is inaccurate; the paper does address overhead.

- **Harsh critic's "suspiciously perfect correlation" concern about invalidating results:** The harsh critic correctly identifies the issue but then says "this does not invalidate the paper's main results." This qualifies the point as Major not Fatal — already reflected above.

- **Strength Finder's generic/superficial strengths** (e.g., "addressed an important problem"): These were not present in the Strength Finder output; all listed strengths are specific and evidence-backed. No removal needed there.

- **Harsh critic's concern about fair comparison if baselines use different backbones:** This is speculative — there is no evidence that baselines use different backbones. The concern about unspecified backbone in main text is valid (kept as Minor), but the speculation about unfair comparison is removed.

## Novel Insights

Beyond the paper's own contributions, no genuinely novel synthesis emerged from the reviews. The core tension reviewers identified is between the paper's strong empirical results (Tables 1–3) and the suspiciously clean correlation values in Figure 3, which undermines the secondary claim but does not threaten the main contribution. The reviewers converge on the assessment that the method is principled, well-executed, and achieves clear SOTA — but the geometry→performance analysis needs better presentation.

## Suggestions

1. **Clarify Figure 3.** Report the number of configuration points, show raw scatter, and explain why the correlation appears so tight (e.g., rounding, or because drift is directly penalized during training — making the relationship near-deterministic by construction). Consider also showing results with visible noise to build credibility.
2. **Add backbone specification to Section 4.1.** A single sentence ("We use CLIP ViT-B/32 for all experiments") would make the main text self-contained.
3. **Add variability estimates to Table 1** (MTIL/X-TAIL), consistent with Table 2.
4. **Include external baselines on the Pareto plot (Figure 2)** to show where competing methods sit on the memory/performance frontier.
5. **Add a limitations paragraph** in the main text rather than deferring entirely to the appendix.

## Score and Decision

**Calibration anchors used:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| C-CLIP (sb7qHFYwBc) | 6.50 | R1/R2 | Directly comparable baseline; Pi-CCA outperforms it on every benchmark and has a more principled method |
| TiC-CLIP (TLADT8Wrhn) | 6.25 | R1/R2 | Benchmark-contribution paper; different contribution type, similar quality tier |
| RLCF (kIP0duasBb) | 6.67 | R2 | TTA paper; comparable quality but different setting |
| G9Ea7mlqGO (CLIP efficient online continual learner) | 3.80 | R1 | Lower quality, rejected paper; Pi-CCA far stronger |
| k9NYnsC4Mq (LwF for VLMs) | 5.67 | R1 | Reasonable but weaker than Pi-CCA |
| V6uxd8MEqw (Advancing Prompt-Based Methods) | 6.50 | R2 | Prompt-based CL paper; comparable quality |

**Round-1 bracket**: 3.5–7.5 (clearly above the weak band, plausibly in the upper half).

**Round-2 narrowing**: The paper is clearly stronger than C-CLIP (6.5) which it outperforms directly. It sits at a quality level comparable to or above the 6.5–6.7 anchors. The suspicious correlation issue (Figure 3) prevents it from reaching the 8+ tier. The score sits at 7.5 — above C-CLIP and the typical accept-level VL-CL papers, reflecting the principled method and strong results, but docked for the overstated correlation evidence.

**Final score**: 7.5

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>