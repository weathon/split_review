Now I have a thorough understanding of the paper content. Let me produce the consolidated review.

## Summary

This paper addresses the problem of achieving interventional fairness (a causal fairness notion based on Pearl's do-operator) when the underlying causal graph is only partially known, i.e., represented by a maximally partially directed acyclic graph (MPDAG). The authors make three main contributions: (1) they prove that modeling the predictor Ŷ as a function of all observed variables yields an augmented MPDAG, enabling formal causal inference (Theorem 1); (2) they provide a graphical necessary-and-sufficient condition for identifying the interventional fairness measure on an MPDAG, together with a constructive formula (Proposition 1); and (3) they formulate a constrained optimization problem that trades off accuracy against interventional unfairness, using Monte Carlo sampling of interventional distributions. Experiments on synthetic data and two real-world datasets (UCI Student, Credit Risk) demonstrate that the proposed ε-IFair method can achieve a tunable accuracy–fairness trade-off.

## Strengths

- **Theorem 1 (augmented-MPDAG property) is a genuinely novel theoretical contribution.** The paper proves that augmenting an MPDAG with a predictor node Ŷ (receiving edges from all observed variables) yields another MPDAG consistent with the same background knowledge. This is non-trivial and enables causal inference on the augmented graph — a result of independent interest beyond fairness. (Lines 212–216, Definition 4, Theorem 1)

- **Proposition 1 provides a clear, verifiable identification condition and formula.** The paper gives a necessary and sufficient graphical condition (no undirected edge between the intervention set S and V\S in the MPDAG) for identifying P(Ŷ|do(S=s)), together with a factorization formula in terms of the observational density. This gives practitioners a concrete check before applying the fairness constraint. (Lines 228–244, Proposition 1)

- **Experimental demonstration of a tunable accuracy–fairness trade-off.** On synthetic data (Figure 3) and the UCI Student dataset (Figure 5), the ε-IFair method shows that with appropriate λ it can simultaneously achieve unfairness as low as the IFair baseline and RMSE as low as the Full model — a concrete demonstration that the framework delivers on its central promise. (Lines 292–294, Figures 3 and 5)

- **Credit Risk experiment shows applicability where the IFair baseline is not viable.** Since Age has no non-descendants in the Credit Risk dataset, the IFair baseline is inapplicable (line 395). The proposed method still provides a meaningful fairness–accuracy trade-off, demonstrating value beyond what existing MPDAG-based approaches can offer. (Lines 373–396, Figure 7)

## Weaknesses

### Fatal

None.

### Major

- **Construction of MPDAGs for real-world datasets is not explained.** The paper states "Our experiments are carried out on the MPDAG G in Figure 5.1" (Student, line 345) and "based on the MPDAG G in Figure 5.2" (Credit, line 376), but provides no description of how these graphs were obtained. Were they learned from data (and if so, which causal discovery algorithm and hyperparameters were used)? Were they specified based on domain expertise? Without this information, the causal assumptions underlying the real-data experiments are unverifiable, and the results cannot be reproduced or assessed for correctness. This is a serious methodological gap since the entire framework depends on the MPDAG being a reasonable representation of the underlying causal structure.

- **The identification condition (Proposition 1) is restrictive, and its consequences are not empirically evaluated.** Proposition 1 requires that there be no undirected edge between nodes in S and nodes in V\S in the MPDAG. In many real-world scenarios, the MPDAG will contain such edges, leading to non-identifiability. The synthetic experiments are designed to avoid this condition (lines 284–287: background knowledge is sampled precisely to resolve undirected edges needed for identification), and the real-data experiments presumably satisfy it, but this cannot be checked because the MPDAGs are not described. The paper mentions averaging over orientations for non-identifiable cases (lines 249–250) but does not implement or test this strategy. The method's most practically challenging aspect — handling non-identifiability — is not evaluated, which limits the empirical support for the paper's claims about operating under partial knowledge.

### Minor

- **Fairness evaluation metric overlaps with the optimization penalty.** The paper uses MMD for the fairness penalty in optimization (Section 4.3, line 256: "Here, we employ MMD") and also evaluates unfairness using MMD (line 268: "assess interventional unfairness by MMD"). While this is not unusual in constrained optimization, it would strengthen the evaluation to show that the method also reduces unfairness measured by a different metric (e.g., difference in conditional means under interventions). The paper does partially address this through density plots (visual overlap of interventional distributions) and the Credit Risk experiment (which uses absolute difference in means for binary outcomes), but the primary evaluation is on the same quantity being penalized. This weakens — but does not invalidate — the empirical evidence.

- **Linear-Gaussian assumption in density estimation is not tested for robustness.** The paper estimates conditional densities using conditional multivariate normal distributions (line 256: "For convenience, we estimate f(vi|pa(vi,G)) using a conditional multivariate normal distribution"). The synthetic data are linear-Gaussian, matching this assumption. For real datasets, the data may be non-Gaussian or involve discrete variables (e.g., binary features in Credit Risk), and the paper does not discuss or test sensitivity to violations of this distributional assumption. While the paper notes other density estimation approaches could be used, the lack of robustness analysis is a gap.

- **No variability information in experimental results.** The synthetic results are averaged over 10 graphs per setting (line 293), but the trade-off plots show only point estimates without error bars, confidence intervals, or standard deviations. Without variability information, it is impossible to assess whether observed differences between methods (e.g., ε-IFair vs. Full at various λ) are statistically significant.

### Trivial

None.

## Nice-to-Haves

- **Sensitivity analysis for λ selection.** The paper uses λ values {0, 0.5, 5, 20, 60, 100} (line 290) without explaining the selection rationale. A finer-grained exploration of the trade-off curve would improve practical guidance.
- **Computational cost discussion.** The method requires Monte Carlo sampling from learned conditional densities at each training step; a brief discussion of runtime and scalability would help practitioners.
- **Testing on non-identifiable synthetic scenarios.** Implementing the averaging-over-orientations strategy mentioned in lines 249–250 and comparing performance on identifiable vs. non-identifiable cases would strengthen claims about handling partial knowledge.

## Removed Points

- *"The fairness metric is the same quantity being penalized during optimization — the absolute difference in Equation 3 vs. MMD in practice"* — Partially retained as Minor (see above). The critic's framing that the method "could simply shift predicted values downward" is speculative and not grounded in evidence from the paper. The concern is retained in weakened form as a valid point about evaluation overlap.

- *"The Credit dataset fairness metric inconsistency is not motivated"* — REMOVED. The paper explicitly motivates this (line 395: "Given that the target variable Loan_status is binary"). Its use of a different metric is actually a positive cross-validation signal, not a weakness.

- *"Section 4.4 should note path-specific fairness is also excluded"* — REMOVED. The paper already states "not applicable to path-specific causal fairness or counterfactual fairness" (line 261).

- *"Missing appendix / proofs"* — REMOVED per hard rules (parser strips appendices).

- *"Lack of comparison to prior work on fairness with unknown graphs"* — REMOVED. The paper mentions Zuo et al. (2022) and the IFair baseline from that work; the requested broader positioning is a nice-to-have, not a genuine weakness.

- *"The paper does not discuss computational cost"* — Moved to Nice-to-Haves.

- *"No sensitivity analysis for the choice of λ"* — Moved to Nice-to-Haves.

- Various formatting/style nitpicks — REMOVED per hard rules.

## Novel Insights

The reviews surface an important structural observation that goes beyond what the paper itself highlights: the paper's core theoretical contribution (Theorem 1 — the augmented-MPDAG property) is potentially separable from the fairness application and may be of independent interest to the broader causal inference community. However, the reviews also reveal that the paper's empirical strategy systematically sidesteps the hardest part of its own problem statement: the identification condition is restrictive, the synthetic data are designed to avoid non-identifiability, and the real-data MPDAGs are unverifiable. This creates a gap between the generality of the paper's framing ("partially known causal graphs") and the specificity of what is actually tested. The non-identification discussion (lines 249–250) hints at an averaging strategy that would address this, and evaluating it would significantly strengthen the contribution's scope and practical relevance.

## Suggestions

1. **Document the real-data MPDAGs fully.** For each real dataset, explicitly state how the MPDAG was obtained: which causal discovery algorithm was used (with hyperparameters), what background knowledge was incorporated, or whether domain expertise was consulted (with justification). If space is tight, provide this in the appendix. Without this, the real-data experiments are not interpretable.

2. **Test on a non-identifiable synthetic scenario.** Generate an MPDAG where the identification condition fails (undirected edges involving the sensitive attribute remain). Implement the averaging-over-orientations strategy mentioned in Section 4.2. Compare performance to the identifiable case. This would directly demonstrate how the method handles the partial-knowledge setting when the effect is not uniquely determined.

3. **Cross-validate fairness with an independent metric.** Show that the MMD penalty transfers to a different fairness measure (e.g., absolute difference in conditional expectations under interventions). The Credit dataset experiment partially does this — replicate this cross-validation on the synthetic and Student data.

4. **Add error bars or variance indicators** to the trade-off plots for the synthetic experiments (average over 10 graphs). A single sentence describing the spread would substantially improve the evidential value.

5. **Briefly discuss robustness to distributional assumptions.** If the method is robust to non-Gaussian data, a simple non-Gaussian synthetic experiment would demonstrate this. If not, acknowledge the limitation.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>