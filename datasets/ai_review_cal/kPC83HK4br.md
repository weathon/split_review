- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

CHAMP introduces a sequence-to-sequence multi-hypothesis 3D human pose estimator that trains a diffusion-based denoiser jointly with a learned conformity scoring function via differentiable conformal prediction. The scoring function is used during inference to filter generated hypotheses before aggregation (mean, J-Agg, or J-Best), achieving state-of-the-art results on Human3.6M and MPI-INF-3DHP.

## Strengths

1. **End-to-end differentiable conformal scoring for multi-hypothesis pose selection.** The paper integrates a learned conformity score into training via a differentiable inefficiency loss (Section 4.2, Eq. 7-9), extending ConfTr from classification to structured 3D pose regression. The ablation (Section 5.4, Fig. 3) confirms that the end-to-end learned score outperforms both a separately trained score and a hand-designed function, demonstrating that the differentiable CP loop actively shapes the representations.

2. **State-of-the-art empirical results across multiple benchmarks.** On Human3.6M, CHAMP-Agg and CHAMP-Best improve over the base CHAMP-Naive by 1.7mm and 3.6mm MPJPE respectively (Section 5.1). On MPI-INF-3DHP, CHAMP-Agg achieves SOTA across MPJPE, PCK, and AUC (Section 5.2). These gains are consistent across datasets and aggregation strategies.

3. **Comprehensive ablation studies justifying design choices.** The paper ablates the conformity function (learned vs. hand-designed), the number of training/inference hypotheses, and the inefficiency loss weight λ (Section 5.4, Figs. 3-5). These experiments transparently support the chosen hyperparameters (H_train=20, H=80, λ=0.05) and confirm the learned score's advantage.

4. **Qualitative generalization to in-the-wild videos.** A model trained solely on Human3.6M applied to TikTok, YouTube, and 3DPW videos (Section 5.3, Fig. 1) shows the learned score generalizes beyond the training distribution and filters outlier hypotheses effectively.

## Weaknesses

### Fatal
None.

### Major

1. **Test-time conformity score mismatch invalidates the claimed CP coverage guarantee.** The conformity score φ_θ is defined and trained (Eq. 8) as φ_θ(ȳ^h, y_GT) — cosine similarity between embeddings of a hypothesis and the **ground-truth** 3D pose. At test time (Eq. 13, Section 4.3), the score becomes φ_θ(ỹ, y), where ỹ is the mean of 20 generated samples (a point estimate) and y is a candidate hypothesis. The ground-truth argument is replaced by a model-generated reference. The paper provides **no justification** that this substitution yields scores comparable to the calibration-time scores (which use the ground truth), nor does it explain why the CP coverage guarantee P(Y ∈ C(X)) ≥ 1-α would transfer. This is not a minor ambiguity — the abstract claims the method "inherits the probabilistic guarantees of conformal prediction," yet the test-time procedure as specified does not clearly support that claim. The method **functions** as a hypothesis filter (the empirical results demonstrate that), but the CP guarantee is not substantiated.

2. **Empirical coverage — absent despite being claimed.** Section 5.5 states "We also investigate the empirical coverage of our method in Human 3. Results suggest that we are able to inherit the coverage guarantee from CP with the learned conformity score even if the dataset is not fully exchangeable." No numerical results, table, or figure is provided. Given the test-time procedure concern above, empirical coverage rates for different α values are the most direct way to validate whether the CP guarantee actually holds. Their absence is a missing central piece of evidence.

### Minor

1. **No error bars or confidence intervals on any metric.** All reported numbers are point estimates. Given that improvements are on the order of 1-2 mm MPJPE (e.g., CHAMP vs. CHAMP-Naive), it is impossible to assess statistical significance.

2. **Missing ablation that isolates CP filtering from aggregation method.** The paper compares CHAMP-Naive (mean aggregation, no CP) to CHAMP (mean aggregation with CP), showing CP helps. But when CP is combined with J-Agg (CHAMP-Agg), there is no variant with the same backbone + J-Agg without CP filtering. A direct "backbone + J-Agg w/o CP" baseline would isolate the contribution of CP filtering from that of the aggregation method. Without it, the SOTA comparison to D3DP conflates these two factors.

3. **Training/test CP operational gap.** During training (following ConfTr), the differentiable CP simulates calibration by splitting **hypotheses from the same input** into calibration and prediction halves. During test-time calibration, the CP operates across **different (input, output) pairs**. The paper does not discuss whether a scoring function trained on within-input rankings generalizes to across-input score distributions. This is a methodological gap worth addressing.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment that computes empirical coverage (fraction of test examples where ground truth falls in the selected hypothesis set) for target 1-α values (e.g., 0.9, 0.95). This would directly validate the CP claim.
- Clarify whether the calibration step during inference computes scores as φ_θ(ỹ_i, y_GT_i) (mean prediction vs. ground truth) or in some other way, and justify why the resulting τ applies to test-time scores φ_θ(ỹ, y) (mean prediction vs. hypothesis).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The hand-designed score φ_peak requires ground truth at test time; the ablation is not informative."** The ablation (Section 5.4) compares scoring functions using **J-Best aggregation** (which itself is an oracle bounding method that requires ground truth). The purpose is to compare the quality of different scoring functions as ranking mechanisms under controlled conditions, not to demonstrate test-time applicability. This is a standard research comparison and not a weakness.

- **"The method as presented cannot function at test time."** The method does function — it produces filtered hypothesis sets and achieves strong empirical results. The issue is specifically with the CP coverage **guarantee**, not with whether the method works.

- **"No comparison with [specific missing baseline]."** The critic's "missing baseline" demands a variant that was not claimed in the scope. The paper compares CHAMP variants and prior SOTA methods; the CHAMP-Naive vs. CHAMP comparison already isolates the effect of CP filtering with mean aggregation.

- **Criticisms about missing appendix content, formatting, or reproducibility details** that cannot be verified from the paper as presented or that reflect parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally different interpretation of the results or an unforeseen implication that the paper itself fails to discuss.

## Suggestions

1. **Clarify the test-time conformity score.** Provide the exact formula for φ_θ at test time, specifying what each argument is (e.g., ỹ = mean of 20 generated samples, y = candidate hypothesis). Acknowledge the shift from the training-time usage and either (a) justify why the CP guarantee still applies, or (b) reframe the claim — e.g., describe the procedure as "learned hypothesis filtering inspired by CP" rather than claiming the formal CP guarantee. If the CP guarantee is to be retained, the calibration step must be described precisely and the coverage must be verified empirically.

2. **Report empirical coverage rates.** For at least one dataset (e.g., Human3.6M), report the fraction of test examples where the ground-truth pose is contained in the filtered hypothesis set C_θ(y, τ) for different target coverage levels (e.g., 1-α = 0.9, 0.95). Compare to a standard CP baseline with a hand-designed score to validate the learned score's coverage properties.

3. **Add error bars.** Report standard deviations over multiple runs or seeds for the main results.

4. **Add a "no CP" baseline with J-Agg.** Using the same trained backbone, apply J-Agg to all 80 hypotheses without CP filtering, and report the result alongside CHAMP-Agg. This cleanly separates the contribution of CP filtering from the aggregation method.
