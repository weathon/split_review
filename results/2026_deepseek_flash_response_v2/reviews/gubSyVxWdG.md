**Calibration Anchors Summary:**

**Round 1 (Bracketing):**
- *Low band (<3.5)*: 5AJ8R4z5g0 (3.25), p1b96KC6rj (2.17/4.40), tqHgSxRwiK (3.00), aoW5Sm8Op8 (2.33) — all Reject, weaker papers with limited contributions. Current paper significantly stronger.
- *Middle band (3.5–7.5)*: Q2bJ2qgcP1 (6.00, Accept) — CATE benchmark with Q statistic, comparable quality; x2rZGCbRRd (5.50, Reject) — post-treatment covariates, weaker theory; glgvpS1dD1 (4.50, Reject) — adversarial CATE, incremental; qsAckNdySL (4.25, Reject) — invariance-based causality.
- *High band (>7.5)*: 3cuJwmPxXj (8.00), A3YUPeJTNR (8.00), EUSkm2sVJ6 (7.60) — all on different topics (representation learning, prediction timing, data usage), significantly stronger contributions.

**Round 2 (Narrowing within bracket):**
- TC9r8gsaoh (6.00, Reject) — Nuisance-robust weighting. Comparable quality but had redundancy with existing methods. Current paper has clearer theoretical contribution.
- MqEQbvPvkE (5.00, Reject) — Exposure shifts with neural networks. Weaker theoretical validation.
- S46Knicu56 (7.33, Accept) — Continuous treatment with measurement error. Stronger, addresses genuinely new problem not previously studied.
- uwO71a8wET (6.50, Accept) — Bayesian neural CDE. Stronger on breadth but has latent variable concerns.

**Bracket**: Round 1 → [5, 7]. Round 2 → paper is comparable to the 6.00 anchors (NuNet, CATE Benchmark), below the 6.5+ anchors which address wider or more novel problem spaces. The core theoretical contribution is sound and well-motivated; the two major missing details (K not specified, selection rates not reported) are fixable and prevent a higher score but do not undermine the core contribution.

---

## Summary

This paper proposes a framework for evaluating Heterogeneous Treatment Effect (HTE) estimators using relative error. Its core theoretical contribution is proving that the proposed relative-error estimator is √n-consistent and asymptotically normal even when outcome regression models are misspecified — requiring only that the propensity score converges faster than n^{-1/4}, which relaxes stronger conditions in prior work (Gao, 2025). The paper derives moment conditions (Eq. 4) needed for this robustness, designs loss functions (L_wls, L_ce, L_const) that enforce them in a neural-network architecture, and tests the framework on IHDP, Twins, and Jobs datasets.

## Strengths

1. **Relaxing the outcome-regression consistency requirement**: Theorem 1 (Section 4.4) proves √n-consistency and asymptotic normality requiring only the propensity score to converge faster than n^{-1/4}, even if outcome regression models are misspecified. This is a concrete theoretical improvement over Gao (2025), which required all nuisance estimators to be consistent. The practical motivation is well-argued: outcome models rely on cross-group extrapolation and are prone to misspecification, while propensity scores are learned from the full dataset and more robust.

2. **Tight theoretical-to-algorithmic link**: The paper derives explicit moment conditions (Eq. 4, Section 4.1) via Taylor expansion and designs a weighted least squares loss (L_wls, Section 4.2) whose first-order conditions exactly match Eq. (4). The loss functions are derived from the robustness requirement rather than being ad-hoc, and the ablation study (Table 5) confirms both L_const and L_ce are necessary for the reported performance.

3. **Empirically tighter confidence intervals than prior approach**: Table 2 shows the proposed method achieves similar coverage (94–96% vs. 94–95%) but dramatically higher selection accuracy (0.80 vs. 0.44 on IHDP; 0.94 vs. 0.88 on Twins) compared to conventional nuisance estimators used within Gao's framework. This demonstrates the method produces narrower, practically useful CIs rather than wide but valid ones.

4. **Ablation study convincingly demonstrates component necessity**: Table 5 shows removing L_const drops selection accuracy from 0.80 to 0.71 on IHDP, and removing L_ce causes catastrophic collapse (√ePEHE jumps from 0.638 to 3.495). This provides clear evidence that the specific combination of losses drives the gains.

5. **Sensitivity analysis on propensity-score misspecification**: Table 6 shows coverage stays in 0.80–0.96 range across varying Gaussian noise injected into the propensity score, supporting the claim of reasonable robustness to propensity-score perturbations.

## Weaknesses

### Fatal
None.

### Major

1. **Candidate estimator set K for the HTE learning algorithm is not specified**: The enhanced HTE estimator in Section 5 averages over pairs of candidate estimators in a set K, and Table 1 reports "Ours" beating all baselines. However, the paper never states which specific estimators constituted K to produce the Table 1 results. Section 6.1 mentions using three estimators (Causal Forest, X-Learner, TARNet) for the *relative error* experiments but does not confirm these are the same K used for the HTE learner. Without this information, the reader cannot interpret whether "Ours" is an ensemble that had access to all strong baselines' information (making the comparison asymmetrical) or something more limited. This is an evidential gap that should be resolved by explicitly stating K. It does not undermine the paper's core evaluation framework contribution, but it undermines the interpretability of the HTE learning results in Table 1.

2. **Selection accuracy reported without selection rate**: Selection accuracy is defined (Section 6.1) as "the probability of correctly identifying the better estimator" conditional on the CI not containing zero. But the paper never reports the proportion of trials where a selection was actually made (i.e., how often the CI excluded zero). This is critical for interpreting Table 2: the proposed method achieves 0.80 selection accuracy vs. 0.44 (Regression) on IHDP, but if Gao's method rarely selects (e.g., only 50% of trials vs. 90% for the proposed method), the comparison tells an incomplete story. The paper itself criticizes Gao's CIs for "frequently includ[ing] zero" (Section 6.2), making this omission self-undermining. Without selection rates, the reader cannot distinguish between "our method selects often and accurately" vs. "both methods select rarely, but our method happens to be correct when it does."

### Minor

1. **Negative-weight issue in L_wls not discussed**: The weighted least squares loss L_wls (Section 4.2) includes the factor (τ̂₁(X_i) − τ̂₂(X_i)), which can be negative when the second estimator has a larger predicted effect. When negative, this term reverses the gradient direction — effectively pushing predictions away from observations rather than toward them. The population-level first-order conditions (Eq. 4) are sound, and the experiments suggest the optimization works, but the paper should acknowledge this finite-sample concern and discuss any stabilization techniques used.

2. **No discussion of overfitting despite claiming no sample splitting**: The paper emphasizes (Section 4.4) that unlike Gao (2025), the proposed method does not require sample splitting. However, the neural network simultaneously estimates nuisance parameters and evaluates relative error on the same data. Some discussion of why overfitting bias is not a concern in this setting would strengthen the paper.

3. **Jobs dataset results relegated to appendix**: Jobs is the only real-world observational dataset (with selection bias from non-experimental controls) in the experimental setup. While space constraints likely drove this decision, its omission from the main table (Table 1) is notable given the paper's framing around real-world applicability and outcome model extrapolation.

### Trivial
None.

## Nice-to-Haves
- Statistical significance tests (e.g., paired comparisons across replications) for Table 1 would strengthen the claims, though means and stds are standard in this literature.
- A brief justification or reference for why the specific neural network architecture achieves the n^{-1/4} convergence rate required by Theorem 1 would be helpful.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Criticism of "Gao's method" labeling** (Harsh Critic: "should be called 'conventional nuisance estimators within Gao's framework'"): The paper already acknowledges Gao does not prescribe specific nuisance estimators and describes the setup clearly. The ablation study explicitly labels L_wls+L_ce as "a method of Gao (2025)." Removed as the paper already addresses this.
- **Table 1 formatting/column garbling**: Parser artifact. Removed per instructions.
- **Theorem 1 "conflates consistency with convergence to probability limits"**: The paper correctly distinguishes between probability limits and true parameters; the text states "γ̂, β̂₀, β̂₁ converge to their probability limits" and separately discusses model misspecification. Removed as the critic slightly misreads the text.
- **"No formal comparison between methods in Table 1"** (demanding paired statistical tests): Moved to Nice-to-Have, as means and stds across repeated experiments are the standard reporting format in causal inference benchmarks.
- **Generic "missing related works"**: Removed per instructions about not mentioning missing related works.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Explicitly state which candidate estimators formed the set K** used to produce the Table 1 results, and consider adding an ensemble baseline that averages the same candidate estimators as a natural comparison.
2. **Report selection rates** (the proportion of trials where the CI excludes zero) alongside selection accuracy for all methods in Table 2 and Figures 1–2.
3. **Add a brief discussion** (even 1–2 sentences) of the sign-varying weight in L_wls and note whether any stabilization was used in practice.
4. **Add a brief discussion** of why the joint estimation of nuisance parameters and relative error on the same data does not introduce overfitting bias — or cite relevant theory if available.
5. **Consider moving Jobs results** to the main body or at minimum referencing them more prominently in the abstract/conclusion.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>