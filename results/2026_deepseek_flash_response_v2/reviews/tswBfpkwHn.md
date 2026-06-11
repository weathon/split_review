Now I have sufficient calibration data. Let me write the final consolidated review.

**Round 1 Bracket:** Based on the calibration search, papers in the low band (2.5-3.25) are applied ICL papers without theoretical analysis, while papers in the high band (8.0) are SSM papers not about ICL. The most topically similar papers — theoretical ICL analysis papers — cluster in the 4.5-7.5 band. The initial plausible bracket is 5.0-7.0.

**Round 2 Narrowing:** I read four anchors in full: two accepted theoretical ICL papers at 6.5-6.75 (vSh5ePa0ph, n7n8McETXw) and two rejected papers at 5.0-5.75 (Jwtpbhheoy, 2F7MFqATdo). The Mamba paper is clearly stronger than the rejected ones (which had fundamental theory-experiment gaps or originality concerns) and comparable to the accepted ones (which had similar minor issues like simplified architectures and strong data assumptions). The Mamba paper's theoretical contributions are solid and its weaknesses are addressable, placing it in the 6-7 range. I anchor at 6.5, comparable to n7n8McETXw (6.50).

Here is the final review:

## Summary

This paper provides the first theoretical analysis of the training dynamics and in-context learning (ICL) generalization of one-layer Mamba models on binary classification tasks when prompts contain additive outliers. It proves convergence and sample complexity bounds (Theorem 1), shows that trained Mamba generalizes to unseen tasks even when test prompts contain a large fraction of distribution-shifted outliers (Theorem 2), and decomposes the mechanism into linear attention for pattern selection and nonlinear gating for outlier suppression and local bias (Corollaries 1-2). Matching theorems for linear Transformers (Theorems 3-4) show they require α < 1/2 while Mamba can tolerate α → 1. Synthetic experiments validate the key predictions.

## Strengths

1. **First quantitative characterization of Mamba's ICL training dynamics.** The paper derives explicit convergence and sample complexity bounds for one-layer Mamba (Theorem 1, Equation 9) and proves that the trained model generalizes on unseen tasks with distribution-shifted outliers (Theorem 2). This goes beyond prior work (Li et al., 2024b; 2025b) that only analyzed global optima of Mamba-like models without addressing training dynamics or outlier robustness.

2. **Provable separation of Mamba vs. linear Transformers on the outlier-fraction threshold.** Theorem 2(c) shows Mamba can tolerate α up to min(1, p_a·l_tr/l_ts) which can approach 1, while Theorem 4(c) shows linear Transformers require α < 1/2. Figure 2 experimentally confirms this sharp threshold across three distinct outlier labeling functions: Mamba maintains error < 0.01 even at α = 0.8 while linear Transformers' error spikes at α > 0.5.

3. **Mechanistic decomposition into attention selection and gating suppression.** Corollary 1 proves the linear attention layer concentrates weight on context examples sharing the query's relevant pattern. Corollary 2 proves the gating layer suppresses outlier examples (G ≤ O(poly(M₁)⁻¹)) and imposes exponential decay with index distance (G ≥ Θ(1/2^{j-1})). Figures 3-4 verify both effects in 3-layer models, providing a precise account of how Mamba achieves robustness.

4. **Clean apples-to-apples comparison framework.** Linear Transformers are a special case of the Mamba formulation (G ≡ 1), and the matching theorem pairs (1↔3, 2↔4) isolate the nonlinear gating as the sole architectural difference, enabling clean attribution of robustness to gating.

5. **Honest accounting of Mamba's training costs.** The analysis does not hide disadvantages: Theorem 1 requires larger batch size, more iterations (T_M = Θ(l_tr)·T_T), and a lower bound on outlier magnitude, none of which are needed for linear Transformers (Theorem 3).

## Weaknesses

### Major
None.

### Minor

1. **Experiment/theory gap on the α bound.** Theorem 2(c) gives a sufficient condition α < min(1, p_a·l_tr/l_ts). In the experiments (p_a=0.6, l_tr=l_ts=20), this bound is α < 0.6, yet Figure 2 tests α up to 0.8 and reports Mamba maintaining error < 0.01. The paper says this is "consistent with Remark 5" but does not discuss why the bound is loose or what this implies about tightness of the sufficient condition. Since the conditions are sufficient (not necessary), the gap does not invalidate the theory, but it should be explicitly addressed.

2. **Abstract phrasing overstates the Transformer limitation.** The abstract states linear Transformers "can only in-context generalize effectively when the fraction of outlier-containing context examples is less than 1/2," which reads as a proven architectural bound. The paper clarifies in Section 3.4 that this is a comparison of sufficient conditions, and Remark 6 acknowledges that larger Transformers with proper training can achieve robustness. The abstract should reflect this nuance to avoid misleading readers.

3. **"With high probability" qualifiers are unquantified.** Corollaries 1 and 2 state their results hold "with a high probability" but never specify the probability level or the source of randomness. Given these corollaries constitute the paper's core mechanistic claim, readers need to know the confidence level.

4. **Strong modeling assumptions.** The orthogonal pattern assumption (μ_j ⟂ ν_k ⟂ v_s*), the fixed-A simplification (A=-I_m, eliminating Mamba's input-dependent selectivity), and the positive-cone constraint on test outliers (V') are strong modeling choices. While standard for theoretical analysis, their implications for real Mamba models should be discussed more prominently in the main text.

### Trivial
- None beyond the minor issues listed above.

## Nice-to-Haves
- Explicit discussion of the looseness of Theorem 2(c)'s sufficient condition relative to the experimental test range.
- Quantification of the "high probability" in Corollaries 1 and 2.

## Removed Points
These points were raised by the reviewers but are removed after cross-checking against the paper:

- **Harsh Critic Point 3 (V' constraint narrows scope):** The critic argued the test-time outlier generalization is narrower than claimed because V' requires positive linear combinations of training outliers. However, the paper *explicitly states this condition* — Theorem 2 condition (a) and the highlighted text in Section 3.1 ("but should contain a positive linear combination of outlier patterns seen during training"). The condition is not glossed over; it is part of the theorem statement. No removal needed since the paper is transparent about the scope.

- **Harsh Critic's "first theoretical analysis" contextualization concern:** The critic suggested the claim should be contextualized relative to Li et al. (2024b, 2025b). However, the paper explicitly distinguishes itself: it analyzes training *dynamics*, while Li et al. analyzed global minima. This distinction is stated in the related work section. The claim is accurate as written.

- **Harsh Critic's concern about upper bound on l_tr:** The critic questioned why Theorem 1 imposes an upper bound on prompt length. The paper addresses this in Remark 3 (ensuring the total number of outliers does not overwhelm clean examples). This is a reasoned modeling choice, not a flaw.

## Novel Insights

None beyond the paper's own contributions. The key insights — (1) Mamba's nonlinear gating enables robustness to outlier fractions approaching 1 while linear Transformers fail at α ≥ 1/2, (2) the mechanism decomposes into attention-based pattern selection and gating-based outlier suppression with exponential locality bias — are well-articulated by the authors themselves.

## Suggestions

1. Add a paragraph explicitly noting that Theorem 2's conditions are sufficient and may be loose, using the experimental finding at α=0.8 > 0.6 to illustrate the gap.
2. Soften the abstract's "can only" phrasing regarding the 1/2 threshold to "provably require α < 1/2 under the sufficient conditions derived here."
3. Quantify the probability statements in Corollaries 1 and 2 (even a brief note like "with probability at least 1-δ over the random draw of the prompt" would suffice).

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/B37UmlxsaP.md | 2.50 | 1 | Applied ICL paper; much less theoretical — this paper is stronger |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/EVg9lwHFJs.md | 3.00 | 1 | Applied ICL paper without theoretical analysis — this paper is stronger |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/gS0XOu0JKs.md | 3.00 | 1 | Uncertainty-aware ICL; no theory — this paper is stronger |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/4y3GDTFv70.md | 3.25 | 1 | Theoretical latent space theory; less specific to ICL dynamics — comparable rigor, different topic |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/aN4Jf6Cx69.md | 4.50 | 1 | ICL mechanistic basis with conflicting scores (1,1,8,8) — lower consensus |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/aKJr5NnN8U.md | 6.50 | 1,2 | ICL vs. IWL theory; accepted. Similar theoretical depth, slightly broader experiments — comparable |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jDsmB4o5S0.md | 6.00 | 1 | Dual process ICL learning; accepted. Similar scope — this paper has stronger theoretical novelty (Mamba is newer) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/YPIA7bgd5y.md | 6.50 | 1 | ICL label relationships; accepted empirical paper — this paper is more theoretical |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/v9Pguuamfp.md | 5.60 | 2 | ICL as kernel regression; rejected. Stronger assumptions, less direct experiments — this paper is stronger |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2PKLRmU7ne.md | 5.60 | 2 | ICL and Occam's razor; rejected. Less focused theoretical contribution — this paper is stronger |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Jwtpbhheoy.md | 5.00 | 2 | ICL uncertainty quantification; rejected. Narrower scope, weaker experiments — this paper is stronger |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2F7MFqATdo.md | 5.75 | 2 | Intention model for ICL; rejected. Overclaiming and weak experiments — this paper is stronger |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/vSh5ePa0ph.md | 6.75 | 2 | Pretraining task complexity for ICL; accepted. Cleaner theory but narrower setting (linear regression) — comparable, this paper covers more complex setting (outliers, nonlinear gating) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/n7n8McETXw.md | 6.50 | 2 | Training nonlinear Transformers for CoT; accepted. Very similar methodology and contribution style — this paper is comparable in quality |

**Round 1 Bracket:** 5.0–7.0 (clearly above applied papers at 3.0, below pure SSM architecture papers at 8.0).

**Round 2 Narrowing:** The paper is comparable to accepted theoretical ICL papers at 6.5–6.75. Its weaknesses (abstract overclaiming, experiment/theory gap on α bound, unquantified probability) are minor and addressable, similar to the accepted papers' own weaknesses. It is clearly above the rejected theoretical papers at 5.0–5.75 which had more fundamental theory-experiment mismatches or originality concerns.

**Final Score: 6.5** — The paper makes a solid theoretical contribution to understanding Mamba's ICL capabilities with rigorous convergence and generalization bounds, a clean comparison framework, and experimentally verified predictions. The weaknesses are minor and addressable in revision.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>