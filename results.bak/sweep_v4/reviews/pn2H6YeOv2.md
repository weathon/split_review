Now I have all the information needed. Let me compose the final consolidated review.

## Summary

The paper introduces Pi-CCA, a replay-free continual learning framework for vision-language models that preserves cross-modal alignment geometry by storing a compact CCA certificate (canonical correlations + sketched subspaces) and matching it via mini-batch statistics. The method also incorporates prompt robustness via projector averaging over perturbations. Across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), Pi-CCA achieves state-of-the-art results among replay-free methods and even surpasses a synthetic-replay baseline.

## Strengths

- **Geometry-first approach to VL-CL is conceptually novel and well-motivated:** Instead of regularizing proxy signals (logits, similarities, parameters), Pi-CCA directly constrains the canonical subspaces and spectrum of the whitened image-text cross-covariance. This is a genuine conceptual shift from prior work like C-CLIP, Mod-X, and ZSCL, which act on surrogate objectives. The ablations in Table 3 confirm that both the spectral and subspace terms contribute meaningfully to performance.

- **Constant-memory certificate via random sketching is elegant and practically effective:** The certificate stores only sketched projectors S_v^* ∈ ℝ^{h×k} and  \bar{S}_t^* ∈ ℝ^{h×k} with h ≪ d_v,d_t, yielding memory independent of feature dimension. Figure 2 shows a clear Pareto frontier, with (k=64, h=256) near the knee. This demonstrates that the approach is both theoretically principled in its memory footprint and practically deployable.

- **Strong empirical results across four diverse benchmarks:** Pi-CCA achieves the top results among all replay-free methods on MTIL (Avg 76.8 vs. next-best 75.2), X-TAIL (Avg 68.1 vs. 67.4), VLCL (I2T R@1 48.6 vs. 47.3 for GIFT, which uses synthetic replay), and ConStruct-VL (FA 75.2, AF 2.7). The gains are consistent and non-trivial, suggesting the method genuinely improves retention.

- **Prompt-invariance mechanism is cleanly integrated and empirically validated:** The projector-averaging approach to prompt robustness (Eq. 5-6, 11) is a natural extension of the certificate framework. Figure 4 shows that at maximal perturbation (s=1.0), the full Pi-CCA model improves VLCL I2T R@1 by +2.44 p.p. and reduces AF by ~1.10 compared to the ablated version without L_pi.

- **Thorough robustness analysis:** Task-order sensitivity tested over 20 random permutations (Figure 5) shows narrow IQRs, and the ablation study in Table 3 systematically isolates each component. The certificate capacity Pareto analysis (Figure 2) demonstrates robustness to hyperparameter choices.

## Weaknesses

### Fatal
None.

### Major

- **The "original-space projectors" framing is geometrically imprecise, and the comparison across changing whitening lacks full theoretical justification.** The paper states at line 85 that P_v^* = U_k^* U_k^{*\top} are "original-space projectors," but U_k^* are obtained from the SVD of the whitened cross-covariance (Eq. 2), as the paper itself calls them "(whitened) canonical directions" at line 76. These are whitened-space projectors, not original-space projectors. Since the whitening matrices Σ_vv^{-1/2} and Σ_tt^{-1/2} evolve via EMA updates (Eq. 12), the metric in which the canonical directions are defined changes over time. Comparing U_k^* (from initial whitening) with Û_k (from current whitening) via a fixed sketch R_v is a well-defined matrix operation, but the geometric meaning of the Frobenius distance between their sketched projectors under different whitening stages is not fully justified in the paper. The empirical success in Tables 1-2 suggests the approximation works in practice, but the theoretical grounding needs to be strengthened — either by (a) back-transforming canonical directions to the original feature space, (b) providing a bound on how the subspace distance changes under evolving whitening, or (c) fixing the initial whitening. This does not invalidate the method given the strong empirical results, but it is a genuine gap in the paper's reasoning.

- **The reported correlation values (r=1.00, ρ=1.00) in Figure 3 are contradictory with the presence of scatter and 95% confidence intervals.** The figure caption reports Pearson r=1.00 in three of four panels and r=0.99 in the fourth, with Spearman ρ=1.00 across all four. Yet the caption also describes "realistic scatter" and "95% confidence interval shaded area." If there is visible scatter, Pearson r mathematically cannot be exactly 1.00. These values appear to come from a sweep over hyperparameters where both drift metrics and performance drops are computed relative to a single baseline configuration. It is plausible that the reported values are rounded (e.g., r≈0.9998 reported as 1.00), but the paper must clarify this. As presented, the numbers conflict with the visual description and erode confidence in the quantitative rigor. The authors should report raw r values to at least 4 decimal places or explain discretization/rounding.

### Minor

- **No "task loss only" baseline is shown.** The ablations in Table 3 remove one loss term at a time (λ_1=0, λ_2=0, λ_3=0) but never remove all regularization terms simultaneously (λ_1=λ_2=λ_3=0, i.e., fine-tuning LoRA with only L_task). While the individual ablation drops (2.2–2.7 p.p. on MTIL Avg) are informative, including this extreme case would quantify the total benefit of the CCA certificate over unregularized fine-tuning as a reference point for the community.

- **The claim of being "replay-free" is technically correct but the EMA statistics maintain persistent aggregate information about past data distributions.** The paper states "replay-free, constant-memory consolidation" (line 38) and "without storing past data" (line 36). The EMA-updated covariance matrices (Eq. 12) and certificate (Eq. 13) do summarize historical information, but this is qualitatively different from storing raw data — individual examples cannot be recovered. The framing is not misleading but would benefit from acknowledging that the approach relies on streaming sufficient statistics rather than being strictly "memory-free" at the level of individual data points.

### Trivial
- None.

## Nice-to-Haves
- A variant with frozen (initial) whitening would help disentangle whether the method's success depends on EMA-evolving whitening or whether the comparison would work even with fixed whitening, providing a cleaner theoretical story.
- Releasing anonymized correlation data (scatter plot source values) for Figure 3 would resolve the reproducibility concern around the r=1.00 values.

## Removed Points

The following points from the harsh critic were removed or downgraded after verification against the paper text:

- **"Geometric incoherence invalidates the mechanism" (downgraded from Fatal to Major):** The harsh critic's claim that "this invalidates the mechanism that the paper's entire claim rests on" is too strong. While the geometric framing is imprecise, the method is well-defined as a mathematical operation — R_v^T U_k is a valid matrix product regardless of which metric defines the subspace, and the empirical results in Tables 1-3 demonstrate the method works. The concern is real but not fatal; it calls for better theoretical justification, not rejection.

- **"EMA as functionally similar to replay buffer" (removed):** The EMA stores covariance statistics, not data. Individual examples cannot be reconstructed from Σ_vv or Σ_vt. The paper's claim of being "replay-free" is standard in the continual learning literature and refers to not storing raw data samples. This criticism reflects a semantic disagreement rather than a substantive weakness.

- **"Data fabrication" accusation regarding Figure 3 (downgraded):** The harsh critic states r=1.00 is "impossible under realistic experimental conditions and strongly suggests either a trivial analysis or data fabrication." This is unnecessarily strong. The values are more likely rounding artifacts (e.g., r=0.9998 reported as 1.00). It is a legitimate concern that needs clarification, but there is no evidence of fabrication. The figure description explicitly shows scatter and CI bands, which is inconsistent with r=1.00 — this is a reporting error, not fraud.

- **"Missing simple baselines" (kept as Minor but narrowed):** The harsh critic lists several missing baselines. The "task loss only" (all λ=0) baseline is indeed missing. EWC and standard knowledge distillation without data are partially covered by existing baselines (ZSCL uses distillation-like regularization). The critique about these being completely absent is overstated.

- **Section-by-section notes about "whitening-dependent geometry is never addressed" (merged into Major weakness above):** The paper does partially address this through the sketching justification (line 122-126) and the EMA certificate update (Eq. 13). The concern is about the completeness of the justification, not that it's entirely unaddressed.

- **"Frozen whitening experiment" and "task-agnostic strict replay-free" experiments (Nice-to-Haves):** These are reasonable suggestions for strengthening the paper but not required for acceptance given the already strong empirical validation.

- **"Code not released" (removed):** Per the hard rules, the paper states code cannot be released "due to ongoing commercial use." This is a policy concern, and the reproducibility statement provides a commitment for camera-ready release.

## Novel Insights

The harsh critic correctly identifies a subtle theoretical gap — the canonical directions from CCA are defined in a whitened space that evolves with the model, and comparing them across time-steps via fixed random projections lacks a clean geometric guarantee. What is genuinely interesting about this paper is that despite this imprecision, the method works empirically across four benchmarks. This suggests either (a) the EMA-smoothing of the certificate (Eq. 13) effectively anchors the comparison to a slowly-changing reference frame, making the whitening drift negligible in practice, or (b) the canonical subspaces are more robust to metric changes than the critic assumes. The paper would benefit from a formal analysis of which effect dominates. The prompt-invariance mechanism (averaging projectors over perturbations) is a technically clean solution to a practical problem and stands as a contribution independent of the whitening concern.

## Suggestions

1. **Clarify the geometric framing:** Acknowledge that U_k are directions in the whitened space and justify why comparing sketched projectors across different whitening stages is meaningful. One path: show that if whitening changes slowly relative to adaptation (enforced by the EMA rate β), the subspace comparison error is bounded by a function of ‖Σ_vv^{(t)} - Σ_vv^{(t-1)}‖.

2. **Report precise correlation values:** Provide unrounded Pearson and Spearman values (e.g., r=0.9997) for Figure 3, and reconcile the r=1.00 with the visible scatter in the plot. If the values are indeed exactly 1.00 due to the metric construction (e.g., both drift and performance drop are deterministic functions of the same hyperparameters), explain this explicitly.

3. **Add a "task loss only" ablation:** Report a row in Table 3 with λ_1=λ_2=λ_3=0 (no CCA regularization) to quantify the absolute benefit of the certificate.

4. **Release the correlation scatter data:** Even if the full code cannot be shared, providing anonymized CSV files for Figure 3 would resolve trust concerns.

## Score and Decision

Comparative score calibration against anchors:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| **C-CLIP** (sb7qHFYwBc.md) — VL-CL via LoRA+distillation | 6.50 (Accept) | Similar domain and evaluation scope; Pi-CCA has stronger conceptual novelty but less precise reporting on Figure 3 |
| **TiC-CLIP** (TLADT8Wrhn.md) — Continual training benchmarks | 6.25 (Accept) | Different contribution type (benchmark vs. method); Pi-CCA's methodological contribution is comparable in depth |
| **PROOF** (k9NYnsC4Mq.md) — VLM class-incremental learning | 5.67 (Reject) | Similar domain; Pi-CCA has more comprehensive evaluation and clearer contribution but also has notable concerns |
| **V+L Synergy** (9aZ2ixiYGd.md) — Rehearsal-free CL | 5.00 (Accept) | Pi-CCA's evaluation is more extensive across more benchmarks |
| **LVLM-CL** (JIlIYIHMuv.md) — Weak VL-CL method | 2.50 (Reject) | Pi-CCA is substantially stronger in all dimensions |
| **Projected Subnetworks** (WM5G2NWSYC.md) — Weak CL paper | 2.00 (Reject) | Pi-CCA is far more rigorous and complete |

Relative positioning: Pi-CCA is stronger than PROOF (5.67, rejected) in both contribution and empirical scope, broadly comparable to C-CLIP (6.50, accepted) in quality but with a notable reporting concern around Figure 3 that reduces confidence. Given the correlation evidence requires clarification and the geometric framing needs correction, the paper is slightly below the acceptance threshold in its current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>