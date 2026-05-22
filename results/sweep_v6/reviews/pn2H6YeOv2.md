Now I have all the information needed. Let me synthesize the final review.

## Summary

The paper proposes Pi-CCA, a replay-free continual learning framework for vision-language models that preserves cross-modal alignment geometry via a compact CCA certificate capturing canonical correlations and subspaces. The approach uses sketched projectors for constant-memory storage, EMA-based streaming updates, and prompt-invariance regularization. The method is evaluated across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL) showing modest but consistent improvements over prior replay-free methods.

## Strengths

- **Principled conceptual reframing of forgetting.** Treating forgetting in VL-CL as drift of cross-modal alignment geometry (canonical correlations and subspaces) rather than as mismatch of proxy signals is a clean and principled insight. The paper formalizes this through the whitened cross-covariance (Eq. 2) and builds a loss that directly constrains spectral and subspace invariants.

- **Compact, constant-memory certificate.** The use of random orthonormal sketches (h×k independent of d_v, d_t) enables a practical, replay-free solution with memory independent of model dimensionality. Figure 2 provides a Pareto analysis over k and h, identifying a broad efficient frontier, which confirms that "small yet sufficient" summaries are viable under peak memory and step-time constraints.

- **Component-wise ablation isolating each loss term.** Table 3 cleanly decomposes the contribution of each component: removing the spectral term (λ₁=0) drops MTIL Avg by 2.5 p.p., removing the subspace term (λ₂=0) drops it by 2.2 p.p., and removing prompt invariance (λ₃=0) drops it by 1.5 p.p. This granular evidence supports the claim that each certificate constraint is independently necessary.

- **Consistent SOTA across four benchmarks.** Tables 1–2 show Pi-CCA achieving the best results among replay-free methods on all four evaluation tracks, including surpassing a synthetic-replay method (GIFT) on VLCL I2T R@1 (48.6 vs. 47.3) without storing or generating data.

- **Prompt invariance mechanism is empirically validated.** Figure 4 shows that the ℒ_pi component flattens the degradation slope under increasing prompt perturbation strength, with a +2.44 p.p. R@1 improvement at s=1.0 under ID prompts. This provides direct evidence that the explicit invariance mechanism works as intended.

## Weaknesses

### Fatal
None. The core claims are supported by multiple lines of evidence (ablation, main results, robustness analysis) even though individual pieces have issues.

### Major

1. **Perfect correlations in Figure 3 (r=1.00, ρ=1.00) are unexplained in the main text.** The paper reports Pearson r=1.00 and Spearman ρ=1.00 for three of four scatter plots, with r=0.99 for the fourth. For data described as coming from "realistic perturbations" across multiple independent hyperparameter dimensions (certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type), exact linear fits are effectively impossible under standard empirical noise. The paper references §A.4 for a "theoretical explanation," but the main text frames this as *empirical correlation evidence* supporting the causal claim that geometry preservation predicts retention. If the relationship is deterministic (mathematically derived), it should be presented as such rather than as an empirical finding requiring correlation statistics. If it is genuinely empirical, the r=1.00 values raise serious doubt about the data collection or plotting pipeline. This figure cannot bear the weight the paper places on it as "direct evidence" without full clarification.

2. **No confidence intervals for the main classification results (Table 1).** Table 1 reports MTIL and X-TAIL results with no error bars or significance tests for any method (including Pi-CCA), while Table 2 includes confidence intervals for Pi-CCA and some baselines. The improvements over the next-best method are modest (e.g., MTIL Avg 76.8 vs. 75.2; X-TAIL Transfer 64.7 vs. 63.8). Without variance estimates, it is impossible to assess whether these differences are statistically significant. This is particularly important because the main "SOTA" claim rests on these numbers.

3. **The initial certificate construction is underspecified.** The paper introduces reference (pre-continual) CCA quantities ρ*_{1:k}, U*_k, V*_k "from Eq. 2" and states the certificate is "constructed from a diverse anchor prompt set" (line 102). It never specifies what data produces these initial quantities — whether it is the first task's mini-batch, a held-out validation set, the pre-training corpus, or something else. This is not a minor implementation detail: it determines whether the method requires initial data access, which would contradict the replay-free framing, and it directly affects reproducibility.

### Minor

1. **Unvalidated subspace-angle surrogate.** The subspace-angle loss ℒ_sub uses a Frobenius distance between sketched projectors as a surrogate for the true principal-angle distance. The paper states it "preserves order/angles under near-isometric sketches" without providing a bound or empirical comparison between the surrogate and the true distance. While Table 3 indirectly supports the sketch quality (Gaussian vs. SRHT give similar results), the paper would benefit from a direct validation that the sketched surrogate correlates well with the full-dimensional distance.

2. **No controlled baseline re-implementation.** The paper does not specify whether baseline numbers are taken from original papers or re-implemented under identical conditions (same backbone, LoRA configuration, optimizer, training schedule). Since different methods may use different backbone sizes, adapter settings, and training regimes, a direct numerical comparison without controlling for these factors makes it difficult to attribute gains to the proposed method. This is a common limitation in the field but should be acknowledged explicitly.

3. **Modest gains and limited scope of claims.** The improvements over strong baselines are in the 1–3 p.p. range. For X-TAIL Transfer, Pi-CCA at 64.7 is only 0.9 p.p. above DIKI (63.8). The paper's terminology ("directly controlling the alignment object") slightly oversells what the losses actually do — they act on spectral and subspace summaries derived from the alignment object, not on the alignment objective itself.

4. **No ablation of the whitening step.** The paper uses whitened cross-covariance (Eq. 2) as the foundation, but never ablates whether the canonical correlation formulation is essential or whether simpler spectral alignment of raw embeddings would suffice. This would help isolate whether the CCA machinery is the critical ingredient.

### Trivial

- Figure 2's 3D Pareto plot uses a color axis (AF) that is difficult to interpret in grayscale.
- The perturbation strength *s* in Figure 4 is not defined in the main text (referenced to appendix).
- "ID" vs. "OOD" templates in Figure 4 are not explained in the main text.
- The paper states "top performance among replay-free methods" when Table 2 includes GIFT (synthetic replay) as a comparison, which is fine but the phrasing could be tighter.

## Nice-to-Haves

- Adding error bars to Table 1 and Table 3 (at least 3 seeds) to enable significance assessment.
- A synthetic-data experiment validating that the sketched subspace surrogate correlates with the full-dimensional principal-angle distance.
- Sensitivity analysis of the prompt-invariance component to the number of perturbations *M*.
- Qualitative examples of retrieval results under different prompt templates comparing Pi-CCA with and without ℒ_pi.
- A trajectory plot of canonical correlations across the task sequence to visually demonstrate certificate maintenance.
- Comparison to a replay-based method under the same memory budget to contextualize the cost of replay.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper does not correspond to currently available systems / cannot be independently verified / code not released"** — removed per hard rule: reproducibility concern about code availability during review is standard. The paper clearly states code will be released upon acceptance.

2. **"Missing appendix content / missing proofs"** — removed per hard rule: the parser strips appendix sections; they exist in the original submission.

3. **"Missing related work"** — removed per hard rule: as the meta-reviewer I cannot verify claimed missing references.

4. **"Pure formatting/style nitpicks"** (typos, figure rendering, spacing) — removed per hard rule.

5. **Strength Finder's claim that Figure 3 is "direct empirical validation"** — removed because it conflicts with the verified weakness about Figure 3's perfect correlations (weakness wins).

6. **Criticism about "the introduction oversells novelty" / "the comparison with prior work is overstated"** — weakened and subsumed into Minor Weakness #3 as a more precise version.

7. **"Averaging projectors and then taking eigenvectors is not justified"** — the paper does provide justification: "Averaging projectors eliminates sign/rotation ambiguity within the canonical subspace (no Procrustes alignment needed)." This is a reasonable justification; the criticism is not substantive enough to stand.

8. **"The orth() step in EMA breaks the linear EMA property"** — this is a recognized engineering trade-off (re-orthonormalization) that is standard practice in streaming SVD/subspace tracking. The criticism does not identify a concrete failure mode.

## Novel Insights

The reviews surface a genuine tension in the paper: the conceptual contribution (geometry-first framing) is clearly strong and principled, but the main empirical exhibit (Figure 3) undercuts rather than supports the narrative. The near-perfect correlations suggest either a deterministic relationship that should be presented as a mathematical derivation, or a flawed empirical pipeline. A more revealing experiment — perhaps plotting the trajectory of canonical correlations over task sequences for Pi-CCA vs. a baseline — would actually visualize the "alignment geometry drift" mechanism that the paper claims to control. The reviews collectively suggest that the paper's strongest evidence is the ablation study (Table 3) rather than the correlation analysis, which is a missed opportunity to reframe the paper's evidentiary centerpiece.

## Suggestions

1. **Clarify Figure 3.** Either (a) state explicitly that the relationship is theoretical/mathematical (not empirical) and remove the "correlation" framing, or (b) if it is empirical, explain why r=1.00 is obtained and add error/noise to the plot to make it credible as an empirical observation.

2. **Add error bars to Table 1** (at least 3 seeds) to make the SOTA claim statistically grounded.

3. **Specify how the initial certificate is constructed** — what data produces the reference CCA quantities ρ*_{1:k}, U*_k, V*_k.

4. **Acknowledge the baseline comparison confound** explicitly — state which numbers are re-implemented vs. cited, and note the limitations of direct cross-paper comparison.

5. **Add a direct validation of the sketched subspace surrogate** — show that ℒ_sub (sketched) correlates with the true principal-angle loss on a small-scale experiment.

6. **Ablate the whitening step** (Eq. 2) to show whether the CCA formulation is essential.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/sb7qHFYwBc.md (C-CLIP) | 6.50 | Similar VL-CL topic. C-CLIP has larger performance gains (7-10 p.p.) but less technical novelty; Pi-CCA has stronger conceptual foundation but weaker experimental rigor. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/k9NYnsC4Mq.md (PROOF) | 5.67 | Similar VL-CL topic, comparable technical depth. Both papers have strengths in framing but suffer from experimental gaps (no std dev, unclear contributions). Pi-CCA has broader benchmark coverage. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/TLADT8Wrhn.md (TiC-CLIP) | 6.25 | Benchmark contribution with extensive analysis. Pi-CCA has more novel methodology but less rigorous evaluation. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/9aZ2ixiYGd.md (LEAPGen) | 5.00 | Prompt-based CL method with high variance in reviews (8,6,3,3). Pi-CCA has stronger mathematical foundations. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/G9Ea7mlqGO.md (SIT-CLIP) | 3.80 | Online CL for CLIP; weaker technical depth. Pi-CCA is substantially stronger in conceptual framing and technical execution. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/A1JdcLawSu.md (Hyperspherical Replay) | 3.00 | Weak CL paper with uniform low scores. Pi-CCA is far stronger across all dimensions. |

The paper makes a genuinely novel conceptual contribution (geometry-first VL-CL) with a mathematically principled framework and broad evaluation. However, the experimental validation has several gaps — the suspicious Figure 3 correlations, missing error bars in Table 1, and underspecified baselines — that prevent the paper from making a fully convincing case. Positioned relative to the anchors, the paper is stronger than the 3–4 range papers and comparable to the 5–6 range papers in overall quality, though its ceiling is capped by the experimental issues. Score reflects solid conceptual contribution tempered by incomplete empirical support.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>