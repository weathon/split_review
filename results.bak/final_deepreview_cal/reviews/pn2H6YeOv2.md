Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper introduces Pi-CCA, a replay-free continual learning framework for vision-language models that preserves cross-modal alignment by directly tracking and constraining the canonical correlation structure (spectrum and subspaces) of image-text embeddings. The method stores a compact "CCA certificate" using random orthonormal sketches and enforces spectral/subspace consistency during adaptation via three auxiliary losses, plus a prompt-invariance loss. Experiments across MTIL, X-TAIL, VLCL, and ConStruct-VL benchmarks show SOTA results among replay-free methods, and ablation studies confirm each component's importance.

## Strengths

- **Genuinely novel geometry-first principle.** The paper recasts forgetting in VL-CL as alignment-geometry drift and directly preserves the canonical correlations and subspaces of the whitened cross-covariance, rather than regularizing proxy signals (logits, similarities, parameters). This is a principled departure from existing replay-free methods and is well-motivated.

- **Strong empirical results across four diverse benchmarks.** Tables 1–2 show Pi-CCA consistently outperforming a large set of recent replay-free baselines (ZSCL, Mod-X, C-CLIP, RAIL, etc.) on classification (MTIL Avg 76.8 vs. next best 75.2), retrieval (VLCL I2T R@1 48.6 vs. 46.1), and structured-concept tasks (ConStruct-VL AF 2.7 vs. 3.3). It even beats a synthetic-replay method (GIFT) without storing or generating data.

- **Thorough component ablation.** Table 3 systematically ablates each term (spectral, subspace, prompt invariance, certificate EMA, covariance EMA, spectral moments, pairing method, sketch type), showing clear drops when key components are removed. The largest drops come from removing the spectral term (MTIL Avg −2.5) and the subspace term (−2.2), confirming both are necessary.

- **Prompt-invariance mechanism is validated.** Figure 4 provides direct evidence that the prompt-invariance loss flattens degradation slopes under increasing perturbation strength, with measurable gains at s=1.0 (R@1 +2.44 p.p. ID, +2.51 p.p. OOD). The stress-test methodology is clear and the operating range (s ≤ 0.6) is discussed.

- **Task-order robustness and efficiency characterization.** Figure 5 shows narrow IQRs across 20 random task orders, and Figure 2 provides a Pareto analysis of certificate capacity vs. memory/time, identifying a broad efficient ridge with a knee at (k=64, h=256).

## Weaknesses

### Major

- **Near-perfect correlations in the geometry→performance analysis are insufficiently explained.** Figure 3 reports Pearson r=1.00 and Spearman ρ=1.00 for angle drift vs. ΔAvg and ΔR@1, and 0.99/1.00 for spectral drift. Such values are extraordinary in any realistic empirical setting with more than a handful of data points. The paper does not disclose (i) the number of configurations in these scatter plots, (ii) whether all points are visible or overplotted, or (iii) how the performance drops (ΔAvg, ΔR@1) are computed relative to the same baseline configuration — which could introduce spurious dependence with drift measures derived from the same checkpoints. While this analysis is presented as supporting evidence (not the core SOTA claim), the absence of this information undermines the paper's narrative that preserving CCA geometry "causally predicts retention." The authors should provide raw data points, number of configurations, and confirm the correlations are not artifacts of a deterministic relationship or very small sample sizes.

### Minor

- **Inconsistent reporting of variance across tables.** Table 1 (MTIL/X-TAIL) reports point estimates with no standard deviations, while Table 2 (VLCL/ConStruct-VL) includes ±1 std values. Figure 5 also notes "3 seeds." This inconsistency makes it impossible to assess the statistical significance of the classification results and whether the improvements over second-best methods are robust. The authors should provide confidence intervals or standard deviations for Table 1 as well.

- **Baseline tuning protocol is not disclosed.** The paper lists many recent baselines (ZSCL, Mod-X, C-CLIP, etc.) and claims to "follow their standard task orders," but does not state whether each baseline was retrained under identical LoRA settings, backbone initialization, and hyperparameter budgets, or whether published numbers are cited. Given Pi-CCA has many hyperparameters (λ₁, λ₂, λ₃, η, β, α, k, h, M, J, ξ, γ, etc.), clarifying the tuning protocol for each baseline would strengthen fairness claims. A brief disclosure of per-method search spaces or configuration files would suffice.

- **No explicit limitations discussion.** The paper is silent on when the method might fail (e.g., very long task sequences, extreme domain shifts where the canonical subspace fundamentally changes, sensitivity to the choice of k in the certificate). A limitations paragraph would improve completeness.

### Trivial

- The symbol use is slightly inconsistent: **P**^*_(_·_) defined in Eq. (3) is never used after that, while **Q**_v^* is used instead; "R_v^⊥/R_t^⊥" in the figure caption could be mistaken for residuals rather than sketch matrices.
- The prompt perturbation distribution P is mentioned (synonym swap, back-translation, template jitter) but their relative frequencies and exact operations are deferred to an appendix that was not accessible in the main text.

## Nice-to-Haves

- A systematic sweep over λ₁, λ₂, λ₃ weights (beyond setting each to zero) would reveal whether performance is robust or brittle to the balance between task loss and preservation losses.
- An explicit per-step FLOPs/memory breakdown for the key operations (covariance EMA update, whitening SVD, loss computation) would definitively resolve any ambiguity about computational costs, though for CLIP-scale embeddings (d~768) the cost is clearly manageable.

## Removed Points

These points were raised by a reviewer but are not included as weaknesses after cross-checking against the paper:

- **"Feasibility of streaming CCA under computational constraints"** — The harsh critic worried that maintaining full covariance EMAs (Σ_vv, Σ_tt, Σ_vt) would be "prohibitively expensive" at CLIP scale. For d_v=768, d_t=512, the stored matrices total ~1.2M floats (~9.6 MB), and O(d²) EMA updates are negligible compared to the backbone forward pass. The paper clearly describes these as running EMA updates of mini-batch covariances (Eq. 12), and the optional Newton–Schulz iteration provides a cheaper alternative to full eigendecomposition. This concern is overblown; the method as described is implementable at stated resource costs for CLIP-scale models.

- **"Missing proofs in appendix" / "Missing related works"** — These are either parser-stripped content that exists in the original submission or cannot be verified without external sources. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The observation that forgetting correlates with CCA subspace/spectral drift is a useful empirical finding, but the near-perfect correlation values need better explanation before the claim is fully credible.

## Suggestions

1. **Clean up the correlation analysis in Figure 3.** Report the number of data points, show raw scatter with all points visible, and explain whether near-perfect correlations arise from small sample sizes or a genuine deterministic relationship between drift and performance drop (which would actually strengthen the paper — but it must be transparent). Consider adding partial correlations or bootstrapped confidence intervals.

2. **Add standard deviations to Table 1** for consistency with Table 2 and to allow readers to assess the significance of the SOTA margins.

3. **Add a brief disclosure of baseline tuning protocol** — even a sentence noting whether numbers are cited from original papers or reproduced, and whether hyperparameters were tuned per method.

4. **Include a limitations paragraph** discussing potential failure modes and certificate sensitivity.

## Score and Decision

### Calibration

**Round 1 bracketing.** Three queries over the human-review corpus:
- **Weak (<3.5):** Topics "continual learning vision-language model CLIP replay-free" → anchors at 2.00–3.00 (weak, flawed papers). Pi-CCA is clearly above this band.
- **Middle (3.5–7.5):** Topics "continual learning multimodal vision-language foundation model" → anchors at 4.75 (Continual LLaVA, reject), 5.67 (Proof, reject), 6.50 (C-CLIP, accept), 7.00 (Adapting MLLM to Concept Drift, accept). Pi-CCA sits in this band.
- **High (>7.5):** CCA/geometry topics → anchors at 8.00–9.00 but on neuroscience/LLM-function-vector topics, not directly comparable.

**Round 2 narrowing (4.5–6.0 and 5.5–7.5).** Directly comparable papers:
- C-CLIP (6.50, accept): Most relevant anchor — same subfield (CLIP continual learning). Pi-CCA is more novel (geometry-first principle vs. LoRA+contrastive) and has more comprehensive evaluation, but has the correlation-analysis flaw that C-CLIP lacks. Roughly comparable overall.
- Proof (5.67, reject): Pi-CCA is clearly stronger — more novel, better evaluated, more thorough ablations.
- Continual LLaVA (4.75, reject): Pi-CCA is significantly stronger.
- Gramian Multimodal (7.00, accept): About alignment metrics, not CL. Not directly comparable.

**Final bracket: 6.0–6.5.** Pi-CCA sits above Proof (5.67) and below Gramian Multimodal (7.00), comparable to C-CLIP (6.50). The score of 6.5 reflects the genuine novelty and strong empirical results, tempered by the unexplained perfect correlations that need addressing in revision.

### Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>