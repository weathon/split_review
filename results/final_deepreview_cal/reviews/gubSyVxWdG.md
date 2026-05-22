Now I have sufficient calibration. Let me construct the final review.

**Bracket from Round 1:** Between 5.5 and 8.0 (clearly above papers scoring 3-5, and below the very top tier papers that uniformly score 8.0 on different problem types).

**Round 2 narrowing:** Compared against anchors at 6.0 (CATE benchmark), 7.0 (doubly robust identification), 7.33 (continuous treatment effects). The current paper is stronger than the 6.0 benchmark paper (which had experimental design concerns) and comparable to the 7.0 papers. It is slightly below the 7.33 paper which tackled a genuinely novel problem setting (measurement error in continuous treatments).

---

## Summary

This paper proposes a framework for evaluating heterogeneous treatment effect (HTE) estimators using relative error, relaxing a key limitation of prior work (Gao, 2025). Specifically, while Gao's relative error estimator requires both the propensity score and outcome regression models to be consistent, the proposed method achieves √n-consistent, asymptotically normal estimates with valid confidence intervals requiring only a correctly specified propensity score — even when outcome models are misspecified. The framework introduces a weighted least squares loss whose first-order conditions automatically enforce the needed orthogonality conditions, combined with balance regularizers in a Dragonnet-inspired neural architecture. Experiments on IHDP, Twins, and Jobs demonstrate that the method achieves nominal coverage while producing substantially tighter confidence intervals (selection accuracy 0.80 vs. ≤0.48 for standard nuisances on IHDP). Beyond evaluation, the paper also proposes an HTE estimator derived from the learned nuisance parameters that achieves state-of-the-art performance on standard benchmarks.

## Strengths

- **Theoretically grounded relaxation of a known limitation.** Theorem 1 establishes √n-consistency and asymptotic normality of the relative error estimator requiring only a correctly specified propensity score, even when outcome regression models are misspecified. This directly addresses the acknowledged weakness of Gao (2025), where Condition 2 demands both nuisance components be consistent. The theory is clearly presented and the assumptions are stated precisely (Section 4.4).

- **Novel loss design with empirical verification of the mechanism.** The weighted least squares loss ℒ_wls (Section 4.2, Eq. 5) is designed so that its first-order conditions automatically enforce the population orthogonality condition needed for robustness. The ablation study (Table 5) cleanly validates this mechanism: removing ℒ_const collapses selection accuracy from 0.80 to 0.14 on IHDP and 0.94 to 0.14 on Twins, while removing only ℒ_ce causes a smaller drop — pinpointing the specific novel component responsible for the gains.

- **Convincing demonstration of practical value.** Table 2 provides a clean comparison: conventional nuisance estimators (linear regression, gradient boosting) plugged into Gao's framework achieve nominal coverage but selection accuracy ≤0.48 on IHDP — they are valid but uninformative. The proposed method achieves 0.96 coverage and 0.80 selection accuracy on the same data, showing the framework is both reliable and practically useful.

- **Thorough empirical evaluation.** Experiments span three datasets (IHDP, Twins, Jobs), include ablation studies, hyperparameter sensitivity analysis (λ₂ in Table 4, λ₁ and ρ in Appendix F.8), propensity score misspecification sensitivity (Table 6), runtime analysis (Table 3), and comparison against 11 HTE baselines (Table 1). The sensitivity analyses show the method is reasonably robust to hyperparameter choices and propensity score perturbations.

## Weaknesses

### Major
None.

### Minor

- **Gap between the exact theoretical constraints and the soft-relaxation implementation.** Theorem 1 assumes that the population-level conditions in Eq. (4) hold at the probability limits of the nuisance estimators. In practice, the second and third conditions are enforced through a soft relaxation (slack variables + penalty, Section 4.2), for which no theorem guarantees convergence to the exact constraints. The paper provides empirical evidence (Appendix F.4) that the relaxation works, but there is no formal bridging result showing that as ρ → ∞ the unconstrained solution recovers the asymptotic properties of Theorem 1. This limits the theoretical scope of the method. The weakness is acknowledged in the paper but not resolved.

- **Selection accuracy metric needs clarification.** The paper states: "we only pick the winner when the confidence interval for the relative error does not contain zero, otherwise, no selection will be made" (Section 6.1). It is unclear how selection accuracy is computed when no selection is made in some trials — are these trials excluded from the denominator, treated as incorrect selections, or treated differently? The current reporting could overstate accuracy if the method is conservative and only selects when the signal is very strong. Reporting the fraction of trials where a selection is made would resolve this.

- **Missing natural baseline for the HTE estimator.** Section 5's enhanced HTE estimator averages outcome model predictions from all pairs of candidate estimators. A natural baseline not included in Table 1 is a simple ensemble that averages the CATE predictions of the candidate estimators directly (without the learned outcome models). This would clarify whether the improvement comes from the learned outcome models ℒ_wls and ℒ_const, or simply from averaging multiple estimators.

### Trivial

- The conversion from the constrained optimization to the unconstrained loss ℒ_const (Section 4.2) could be presented more clearly, particularly how the slack variables ξ, η and the penalty parameter ρ interact.

## Nice-to-Haves

- Comparing against Gao (2025) with neural-network nuisance estimators (e.g., Dragonnet, TARNet) would sharpen the claim about robustness to outcome model misspecification. The ablation study partially addresses this (the ℒ_wls + ℒ_ce condition degenerates to TARNet-style estimation within Gao's framework), but a direct comparison running Gao's original estimator with neural network nuisances would be cleaner.
- A simple theoretical result for the Section 5 HTE estimator — even just consistency under mild conditions on the candidate estimators — would improve internal coherence. The paper acknowledges this limitation in the conclusion.
- Statistical significance tests (e.g., paired tests against the best baseline in Table 1) would strengthen the HTE estimation claims.

## Removed Points

These points were raised by the reviewers but are removed for the reasons stated:

1. *"Running time analysis not discussed in main text"* — **REMOVED (factually wrong).** The paper includes runtime analysis in Section 6.2 with Table 3 and accompanying discussion.
2. *"Incomplete comparison with Gao (2025): should compare with neural network nuisances"* — **REMOVED (addressed in ablation).** The ablation study explicitly states that the ℒ_wls + ℒ_ce condition "can be seen as a method of (Gao, 2025), where the proposed neural network degenerates to TARNet and serves as a conventional nuisance estimator." This is a fair proxy comparison that shows the proposed method significantly outperforms Gao with neural network nuisances.
3. *"Unclear conversion from constrained to unconstrained optimization"* — **DEMOTED to Trivial.** The conversion is clearly shown: the slack variables are introduced, the constraints are written explicitly, and then the Lagrangian-style penalty is defined. The derivation is standard and reproducible.
4. *"Hyperparameter selection details missing"* — **DEMOTED to Trivial.** The paper reports sensitivity analyses for λ₂ (Table 4) and for λ₁ and ρ (Appendix F.8), which is standard practice for an empirical methods paper. Full architecture details are in Appendix F.10.
5. *"Statistical significance in Table 1"* — **DEMOTED to Nice-to-Have.** The table reports standard deviations over multiple runs, which is the accepted norm for these benchmarks. Requesting formal hypothesis tests is a reasonable suggestion but not a weakness.
6. *"Missing related works"* — **REMOVED per hard rules.** I cannot verify the existence of un-cited works from within the paper.

## Novel Insights

None beyond the paper's own contributions. The core insight — that the orthogonality conditions needed for robustness to outcome model misspecification can be encoded directly into loss functions for nuisance estimation — is already the paper's main contribution. The calibration revealed no additional synthesis beyond what the authors present.

## Suggestions

1. Clarify the selection accuracy computation: report the fraction of trials where a selection is made alongside the conditional accuracy given selection.
2. Consider adding a formal proposition showing that the soft-relaxation solution converges to the exact-constraint solution as ρ → ∞ (or at least state this as a conjecture with empirical support).
3. Add the simple ensemble-of-candidate-estimators baseline to Table 1.
4. Either trim Section 5 or provide a minimal theoretical justification for the averaging scheme.

## Score and Decision

**My initial bracket (Round 1):** Between 5.5 and 8.0, clearly above papers scoring 3-5 and below the very top tier (8.0) of papers on tangentially related topics.

**Round 2 narrowing:** Compared against anchors at avg 6.00 (CATE benchmark paper), 7.00 (doubly robust identification), and 7.33 (continuous treatment effects with measurement error). The current paper is stronger than the 6.00 anchor (which had experimental design concerns) and comparable to the 7.00 anchors in terms of contribution clarity and experimental rigor. It is slightly below the 7.33 anchor, which tackled a genuinely novel and under-explored problem setting. Within the bracket, the paper sits near the top — the weaknesses present are non-fatal and either acknowledged or easily addressable.

**All anchors retrieved:**

| anchor_id | avg_score | round | comparison vs. this paper |
|---|---|---|---|
| tqHgSxRwiK | 3.00 | R1 | Substantially weaker — vague fairness testing, no theory |
| 5AJ8R4z5g0 | 3.25 | R1 | Much weaker — hidden confounders, limited evaluation |
| aoW5Sm8Op8 | 2.33 | R1 | Much weaker — survival benchmarking, no causal theory |
| jFox1iMWUa | 3.40 | R1 | Weaker — continuous treatment, limited theory and experiments |
| MqEQbvPvkE | 5.00 | R1 | Weaker — significant theoretical concerns (Donsker conditions) |
| QV6uB196cR | 4.75 | R1 | Weaker — narrower contribution, presentation issues |
| x2rZGCbRRd | 5.50 | R1 | Comparable — similar quality but different problem |
| TC9r8gsaoh | 6.00 | R1&R2 | Comparable in quality — both have theory+experiments |
| A3YUPeJTNR | 8.00 | R1 | Different problem type; higher impact topic |
| RvUVMjfp8i | 8.00 | R1 | Different problem (SSL evaluation); strong but unrelated |
| 3cuJwmPxXj | 8.00 | R1 | Different problem (representation identifiability) |
| UHPnqSTBPO | 8.00 | R1 | Different problem (LLM evaluation) |
| Q2bJ2qgcP1 | 6.00 | R2 | Weaker — experimental design concerns, overclaimed datasets |
| S46Knicu56 | 7.33 | R2 | Slightly stronger — more novel problem setting |
| 0iscEAo2xB | 6.75 | R2 | Comparable — similar level of rigor, applied problem |
| 9vTAkJ9Tik | 7.00 | R2 | Comparable — both have novel theory + thorough experiments |
| QGGNvKaoIU | 7.00 | R2 | Comparable — meta-learners for HTE over time |
| 6bDJ3CIm5w | 7.00 | R2 | Different topic (auction interference) |
| 1YPfmglNRU | 6.75 | R2 | Comparable — expertise-based HTE estimation |

The paper is a solid contribution to an important problem. It provides a clear theoretical advance over a known limitation in the literature, validates it thoroughly, and produces actionable improvements in estimator selection. The weaknesses are minor and do not undermine the core claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>