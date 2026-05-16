Here is my consolidated final review.

---

## Summary

This paper introduces Kernel Banzhaf, a regression-based estimator for Banzhaf values inspired by KernelSHAP. The key contributions are: (1) establishing a linear regression formulation of Banzhaf values for general set functions (Theorem 3.2), (2) a practical algorithm using uniform subsampling with paired sampling, (3) theoretical guarantees on the sample complexity (Theorem 3.3, Corollary 3.4), and (4) extensive experiments showing superiority over Monte Carlo (MC) and Maximum Sample Reuse (MSR) baselines for Banzhaf estimation across eight datasets.

## Strengths

1. **Novel linear regression formulation for Banzhaf values (Theorem 3.2).** Prior work (Hammer & Holzman, 1992) only established this connection for simple set functions with binary, monotone outputs. The paper cleanly proves that Banzhaf values are the exact least-squares solution to \(\min_{\mathbf{x}}\|\mathbf{Ax}-\mathbf{b}\|_2\) for arbitrary set functions. The proof is concise (Observation 3.1 → Theorem 3.2) and correctly reasoned.

2. **Consistent and substantial empirical superiority over existing Banzhaf estimators.** Across all eight datasets in Figure 2, Kernel Banzhaf achieves lower \(\ell_2\)-norm error than MC and MSR at every sample size, with tighter interquartile ranges. The advantage is particularly pronounced on high-dimensional datasets (e.g., NHANES), where MSR errors go off the chart. This directly validates the paper's core claim of improved sample efficiency.

3. **Robustness to noise in the set function (Figure 3).** The noise-injection experiment is well-designed: Kernel Banzhaf maintains low error across noise levels \(\sigma\) while MC and MSR errors increase substantially. This is practically important because set functions in real explainability tasks are often approximated and noisy.

4. **Condition number analysis (Figure 5) provides an explanatory mechanism.** The paper shows that the matrix \(\mathbf{K}\) for Kernel Banzhaf has lower condition numbers than for KernelSHAP or Leverage SHAP at all sample sizes, explaining the improved numerical stability. This is a clean diagnostic that goes beyond just reporting error metrics.

## Weaknesses

### Fatal
None.

### Major

1. **The sample complexity bound's dependence on \(\delta\) is unusual and insufficiently justified.** Theorem 3.3 states \(m = O(n\log\frac{n}{\delta} + \frac{n}{\delta\epsilon})\). The \(\frac{n}{\delta\epsilon}\) term has an inverse (not logarithmic) dependence on \(\delta\), which is substantially worse than typical leverage-score guarantees (which have \(\log(1/\delta)\)). The paper acknowledges on line 159 that "the theorem can only be improved in the logarithmic factor and dependence on \(\delta\) and \(\epsilon\)," and on line 33 it claims near-optimality "up to log factors and the dependence on \(\epsilon\)." However, the \(1/\delta\) term is not typical for such bounds, the paper provides no lower bound showing this dependence is necessary, and the claim of near-optimality is ambiguous about whether it encompasses the \(\delta\) dependence. If the \(1/\delta\) term is an artifact of the paired sampling analysis, the paper should explain this; if it is real, it should be honestly contextualized as a limitation of the current analysis. This weakens the theoretical contribution.

2. **The comparison with Shapley estimators (Section 4.2) conflates algorithmic performance with semivalue properties.** Kernel Banzhaf (estimating Banzhaf values) is compared against Optimized KernelSHAP and Leverage SHAP (estimating Shapley values). Prior work (Karczmarz et al., 2022; Wang & Jia, 2023) has already established that Banzhaf values are inherently more robust to noise than Shapley values. The results in Figure 4 therefore primarily demonstrate this known semivalue property rather than an algorithmic advantage of Kernel Banzhaf. The paper acknowledges prior work on this robustness (line 249) and uses normalized error to improve fairness, but the framing ("Kernel Banzhaf consistently exhibits superior performance...") implies an algorithmic comparison that the experiment cannot cleanly support. The condition number analysis (Figure 5) is a cleaner algorithmic comparison and should be emphasized more; the error-based comparison in Figure 4 should be presented as a case study in semivalue properties, not as evidence of algorithmic superiority.

### Minor

1. **No empirical runtime/wall-clock comparisons.** The paper provides asymptotic complexity analysis (line 143) but no actual timing experiments. Since Kernel Banzhaf requires solving an \(m \times n\) least-squares problem, its computational cost relative to MC and MSR (which are simple averages) is a practical concern, especially when \(m\) is large. The trade-off between accuracy and computation time should be quantified.

2. **Main experiments use only XGBoost models.** While the paper mentions neural network experiments on smaller datasets (line 213), these are not shown in the main paper. For a method targeting general set functions in explainable AI, broader model validation would strengthen the claims. The noise robustness experiment partially addresses generalization concerns, but direct validation on neural network models would be more convincing.

3. **The benefit of paired sampling could be analyzed more systematically.** The ablation ("Kernel Banzhaf (Excluding Pairs)") is included in Figure 2, and the two variants perform similarly. The paper mentions that sampling without replacement shows no improvement (referencing Figure 10), but does not isolate the paired sampling step to show when or why it helps. A controlled experiment varying the fraction of paired samples would clarify the design choice and justify the additional complexity it introduces to the theoretical analysis.

### Trivial
None.

## Nice-to-Haves

- A controlled ablation study varying the proportion of paired vs. independent samples to clarify when paired sampling provides a benefit.
- Brief discussion of scalability concerns for very large \(n\) (e.g., \(n > 500\)) where the \(O(mn^2)\) least-squares solve may become a bottleneck.
- A limitations paragraph explicitly noting the bound's \(\delta\) dependence and scope of empirical validation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not comment on the \(\delta\) dependence"** (Harsh Critic): The paper does comment on line 159 ("can only be improved in the logarithmic factor and dependence on \(\delta\) and \(\epsilon\)"), though this acknowledgment is brief and could be more prominent. The substantive concern about \(1/\delta\) vs. \(\log(1/\delta)\) is kept in the major weaknesses above.
- **"Without access to the appendix, I cannot verify whether the bound is misreported"**: The appendix exists in the original submission. Per policy, criticisms about missing appendix content are removed. The bound itself (stated in the main text) is evaluated on its stated form.
- **"Figure 10 referenced, not visible"**: This is a parser artifact — the figure exists in the appendix of the original submission.
- **Strength: "Comparisons with state-of-the-art Shapley estimators"** (Strength Finder): This conflicts with the verified weakness that the comparison conflates semivalue differences with algorithmic differences. Per instructions, when a strength and weakness disagree, the weakness wins. The condition number analysis (Figure 5) is a genuine strength and is retained; the error-based comparison (Figure 4) is kept as a limited result with caveats.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension between the paper's theoretical claims and the stated bound, and between its framing of the Shapley comparison and what that experiment can actually resolve, but these are critiques of presentation and rigor rather than novel observations about the paper's substance.

## Suggestions

1. **Clarify the theoretical bound.** Either provide a justification for the \(1/\delta\) dependence (e.g., show it is unavoidable due to paired sampling) or replace it with a standard \(\log(1/\delta)\) bound. Remove or qualify the claim of near-optimality with respect to \(\delta\).

2. **Reframe Section 4.2.** Clearly separate the two claims: (a) Banzhaf values are more robust than Shapley values (confirming prior work), and (b) Kernel Banzhaf's regression subproblem is better conditioned (algorithmic contribution). The abstract and introduction should not claim that Kernel Banzhaf "outperforms Shapley estimators" without clarifying that this partly reflects semivalue differences.

3. **Add a runtime comparison.** A simple table or plot of wall-clock time vs. error would help practitioners evaluate the computational trade-off and strengthen the practical contribution.

4. **Include the neural network results** in the main paper (or add a clear statement that they are in the appendix and summarize the findings).

## Score and Decision

This paper makes a genuine contribution: a clean linear regression formulation for Banzhaf values, a well-motivated estimation algorithm, and strong empirical evidence that it outperforms existing Banzhaf-specific estimators (MC, MSR). The main weaknesses are (a) a theoretical bound whose \(\delta\) dependence is unusual and inadequately justified, (b) a cross-semivalue comparison that is framed too strongly, and (c) the absence of runtime experiments. None of these are fatal — the core Banzhaf estimation result is solid — but they collectively reduce the strength of the contribution. The paper is at the borderline between weak and accept, and with the suggested revisions (particularly clarification of the theory and reframing of the Shapley comparison) would be a solid addition to the literature on game-theoretic feature attribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>