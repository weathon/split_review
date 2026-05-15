Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

The paper establishes a formal link between Out-of-Distribution (OOD) detection and Conformal Prediction (CP). Its first contribution is defining *conformal AUROC* and *conformal FPR@TPRβ* — applying the finite-sample corrections of Bates et al. (2022) to standard OOD evaluation metrics to produce conservative estimates with probabilistic guarantees, demonstrated on OpenOOD and ADBench. Its second contribution is exploring whether OOD scores (ReAct, Gram, KNN, Mahalanobis, ODIN) can serve as effective nonconformity scores for CP, finding that some (KNN, Mahalanobis) occasionally outperform traditional softmax-based scores.

## Strengths

- **Clear exposition of the FPR/p-value connection with compelling empirical evidence.** The paper carefully explains how the empirical FPR used in OOD evaluation is an approximate conformal p-value (Section 4.1), and the SVHN simulation (Section 4.3.1, Figure 1) is a well-designed experiment: 53 disjoint calibration folds of 10,000 points each, with the true FPR approximated using >520,000 held-out points, confirming the theoretical Beta distribution. This provides concrete, reproducible evidence that OOD metrics are subject to non-negligible finite-sample variability.

- **Practical demonstration on major benchmarks.** The correction is shown to reduce AUROC by ~1–2% on OpenOOD (Table 1, δ=0.01) and more variable, larger corrections on ADBench (Figure 3, δ=0.05), which has smaller dataset sizes. These results quantify the real-world trade-off between conservativeness and informativeness. The paper honestly notes that the correction does not invalidate the best OOD methods — it simply makes the evaluation more reliable.

- **Honest presentation of mixed results for the second contribution.** The paper forthrightly states "all OOD scores are inefficient for CP" and that Gram performs very poorly (Section 5). KNN and Mahalanobis sometimes beat softmax-based scores, but the results are not sweeping. The paper acknowledges this rather than over-interpreting the positive cases.

- **Remark 4.1 correctly clarifies that conformal metrics do not require extra validation data.** This addresses a natural practical concern.

## Weaknesses

### Fatal
None.

### Major
None. The core claims are logically sound and empirically supported, and no weakness threatens the paper's validity.

### Minor

1. **The transfer from the pointwise FPR guarantee to the integrated AUROC is not made explicit.** The paper states the Bates et al. guarantee (Eq. 11): ℙ[FPR(τ) ≤ \widehat{FPR}^+(τ), ∀τ ∈ ℝ] ≥ 1-δ. The "∀τ ∈ ℝ" makes this a *simultaneous* guarantee: with probability ≥ 1-δ, the corrected FPR dominates the true FPR at *every* threshold simultaneously. If this event holds, each point on the corrected ROC curve lies to the right of (or at the same position as) the corresponding true point, and the area under the corrected curve is ≤ the true AUROC. Therefore the guarantee *does* transfer to AUROC. However, the paper does not spell out this reasoning, relying on the looser claim that the metrics "use conservative estimates of the FPR." The paper would be strengthened by making this logical step explicit, rather than leaving readers to infer it. (Note: this is a presentation gap, not a logical error — the critic's characterization of the guarantee as merely "pointwise" misreads Eq. 11, which unambiguously quantifies over ∀τ ∈ ℝ.)

2. **The second contribution (OOD scores as nonconformity scores) is weakly supported.** The paper's own results show that three of the five OOD scores (Gram, ReAct, ODIN) perform poorly, and KNN/Mahalanobis only occasionally beat softmax by modest margins. The softmax-like transformation applied to convert class-dependent OOD scores into CP scores (Section 5) is presented without justification. The claim that this "unlocks a whole avenue for crafting CP nonconformity scores" (Conclusion) is too strong given the evidence — a more measured claim (e.g., "KNN and Mahalanobis are promising candidates worth further investigation") would better match the results.

3. **No comparison across the four correction functions (Simes, DKWM, Asymptotic, Monte Carlo).** The paper uses only the Monte Carlo correction (δ=0.01 for OpenOOD, δ=0.05 for ADBench). A comparison across corrections (at multiple δ values) would help practitioners understand the trade-offs between conservativeness and informativeness. The δ=0 results are mentioned but not shown.

4. **The monotonicity of the corrected FPR is not discussed.** The correction function h may or may not preserve the natural monotonicity of the empirical FPR as a function of the threshold. If the corrected FPR is not monotonic, the ROC curve could have non-standard behavior and the trapezoidal AUROC computation might need adjustment. This is a technical detail worth addressing.

### Trivial

- Only one calibration set size (n_cal=2000) and one backbone (ResNet18) are used in the CP experiments (Section 5). Sensitivity analysis would strengthen the results.
- The paper has a minor internal inconsistency: the table caption says "Table 2" (line 203) but the text on line 207 refers to "Table 5."

## Nice-to-Haves

- Validating the conformal AUROC against a ground-truth AUROC in a controlled simulation (e.g., using a very large held-out ID set to compute the true AUROC and checking how often the conformal version is ≤ the true value) would directly verify the claimed guarantee.
- Calibration size sensitivity analysis (e.g., n_val ∈ {100, 500, 2000, 10000}) for the gap between classical and conformal AUROC.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Conformal AUROC lacks a probabilistic guarantee (Structural)"** — The harsh critic claimed the Bates et al. guarantee applies "pointwise" to FPR at each threshold and does not transfer to AUROC. This is incorrect: Equation (11) states the guarantee holds simultaneously *for all τ ∈ ℝ*, which directly implies the conformal AUROC is a conservative lower bound on the true AUROC with probability ≥ 1-δ. The paper's claim is logically sound. (Removed as factually wrong about the nature of the guarantee.)

2. **"Novelty and significance of the first contribution are overstated (Structural)"** — The critic characterized the contribution as "at the level of a position piece." While the technique itself is a direct application of Bates et al., applying established CP corrections to the specific domain of OOD evaluation benchmarks — and demonstrating non-trivial practical impact (1–2% AUROC differences on established benchmarks) — is a valid applied contribution. The paper's title ("Exploring the Link," "Illustrations of Its Benefits") appropriately frames the scope. (Removed because the critic's standard for novelty is unreasonably high for what the paper claims.)

3. **"Section 4.5.2 ... the conclusion that 'no method is provably better than others' is already a known conclusion of ADBench; this experiment does not add new information"** — The paper is observing that the CP correction highlights variability in AD rankings, not claiming this as a novel discovery. The observation is contextually relevant. (Removed as scope creep.)

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the paper itself does not already articulate.

## Suggestions

1. In Section 4.4, add a brief argument: "Because the guarantee of Eq. (11) holds simultaneously for all τ, when the event occurs every point on the corrected ROC curve lies at or to the right of the corresponding true point, so the conformal AUROC ≤ true AUROC with probability ≥ 1-δ."
2. Tone down the "unlocking a whole avenue" claim in the Conclusion to match the mixed empirical results.
3. Add a small table or appendix comparing all four correction functions and at least two δ values.
4. Discuss the monotonicity of the corrected FPR with respect to the threshold, or at least note it as an implicit assumption.
5. Fix the Table 2 / Table 5 inconsistency.

## Score and Decision

The paper makes a clear, well-exposited conceptual contribution by bridging two active research communities. The first contribution (conformal OOD metrics) is sound and practically useful; the second (OOD scores for CP) is exploratory with mixed results but honestly presented. The paper's claims are appropriately scoped (it is an "exploring the link" paper, not a major methodological advance). The weaknesses are all minor — presentation gaps, limited experimental breadth, and somewhat overstated language in one place — none threaten the core claims.

**Score: 6.0**

**Decision: Accept**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>