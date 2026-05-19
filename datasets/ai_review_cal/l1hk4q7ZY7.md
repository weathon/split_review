- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6
Now I have a thorough understanding of the paper and all review claims. Let me produce the final consolidated review.

## Summary

This paper proposes RAPBO, a dueling Bayesian optimization method that augments pairwise preferences by clustering solutions, identifying a set of "similar solutions," and using directed hypergraphs to propagate preferential relations (e.g., if A and B are similar and A ≻ C, then B ≻ C). The goal is to close the performance gap between preference-based BO and function-value-based BO by making fuller use of the limited preference data. Experiments on six 10D synthetic functions and three real-world tasks (RobotPush, Sagas, Cassini1-MINLP) show consistent improvements over four dueling baselines and competitive/superior performance against GP-UCB under the same cost budget.

## Strengths

- **Consistent and substantial improvement over dueling baselines across all tasks.** In all six synthetic functions (Figure 2) and all three real-world tasks (Figure 3), RAPBO achieves better mean best-found function value than PBO, KSS, qEUBO, and COMP-UCB, often with narrower standard deviations. The ablation is clean: PBO is RAPBO without the preference propagation technique, so the gap directly measures the value added by the proposed augmentation.

- **First demonstration that a preference-only method can match or exceed function-value-based BO under cost budgets.** Figure 5 shows RAPBO matching GP-UCB on RobotPush and Cassini1-MINLP, and consistently outperforming GP-UCB on the 12D Sagas trajectory optimization task. Given the long-standing assumption that preference-based methods are strictly weaker, this empirical result is noteworthy.

- **Concrete and practical efficiency gain via directed hypergraph modeling.** Section 4.3 shows that using hyperedges reduces the relation-modeling complexity from O(n₁n₂ + n₂n₃) (full bipartite connections) to O(m) with m=2 hyperedges, making the propagation step computationally negligible relative to GP fitting.

- **Hyperparameter robustness demonstrated.** Section 5.4 reports that RAPBO outperforms the ablated PBO across different values of k (2, 3, 5) with no significant sensitivity, suggesting the method is not brittle.

## Weaknesses

### Fatal
None.

### Major

- **The accuracy metric for augmented preferences (Figure 4) is never explicitly defined.** The paper reports "mean accuracy of the augmented preferences" but does not state the ground-truth reference. For synthetic functions (Griewank), the natural interpretation is accuracy against the known objective function. For real-world tasks (RobotPush, Sagas, Cassini1-MINLP), which are benchmark datasets with available function values, accuracy is presumably also computed against ground truth. However, the paper should state this explicitly. Without this clarification, a reader cannot assess whether the reported "accuracy" measures agreement with ground truth (a meaningful validation) or something else. This is a reproducibility gap.

- **The comparison with GP-UCB (Figure 5) has an asymmetry that weakens the headline claim.** RAPBO is initialized with 30 duels (60 distinct solutions evaluated as pairs), while GP-UCB is initialized with only 15–20 function evaluations (15–20 solutions). The paper acknowledges this (line 203) and uses cost-based budgets to rationalize it, but the 3–4× difference in the number of distinct solutions seen at initialization gives RAPBO broader coverage of the search space before optimization begins. A controlled experiment matching the number of observed solutions (e.g., 15 duels / 30 solutions for RAPBO vs. 30 function evaluations for GP-UCB) would substantiate the claim that preference propagation, not just broader initial coverage, drives the competitive performance. As presented, the evidence for closing the gap with function-value-based BO is promising but not fully unambiguous.

### Minor

- **No statistical significance assessment.** The paper reports means and standard deviations from 20 repeats (standard practice in BO), but on several tasks the error bars overlap in later iterations (e.g., Griewank after ~70 iterations, RobotPush where multiple baselines cluster in a narrow band). Without confidence intervals, paired tests, or any significance measure, it is unclear which of the observed differences are robust versus noise. Given the strong claims made ("superiority," "for the first time"), at least bootstrapped confidence intervals would strengthen the evidence.

- **Preference generation details are underspecified.** The preference function in Eq. (1) uses the logistic function without a scaling/noise parameter τ (i.e., 1/(1 + e^-[f(x)-f(x')])). Without τ, the preference probabilities are nearly deterministic for any pair with a non-negligible function value gap. This affects both reproducibility and the simulated preference realism. The paper should specify how preferences were generated from function values in the experiments.

- **Clustering procedure details are missing.** The paper states it uses a Gaussian mixture model to partition solutions into k clusters and selects the one "with the highest intra-cluster similarity." It does not specify: (a) how the GMM is fitted (covariance type, initialization), (b) how "intra-cluster similarity" is precisely computed, (c) whether k is always the propagation parameter, and (d) what happens when no solution satisfies the conditions for forming the bad/similar/good sets. These affect reproducibility and the reader's ability to assess edge cases.

- **The paper only evaluates against methods that resample both solutions in a duel.** Section 3.2 identifies two families of dueling methods (fixed-solution and resampled-both) but only compares against the latter. The paper scopes to the second type (line 80: "we focus on the second type of methods"), which is a legitimate design choice. However, since the preference propagation technique uses similarity to the "current best"-like anchor (the similar-solutions set), it could plausibly transfer to the fixed-solution setting. Comparing with at least one fixed-solution method (HB or POP-BO) would strengthen the claim of broad superiority. As it stands, the claim should be read as "superiority over methods that resample both solutions."

- **On the RobotPush task, augmented preference accuracy hovers near 0.55 (barely above random) yet RAPBO still outperforms baselines.** The paper explains this by noting that propagation scope is narrow in this case. However, without an ablation that uses random augmentations of the same size, it is unclear whether the benefit comes from the augmented preferences themselves or from some other aspect of the procedure (e.g., the change in the acquisition function's posterior).

### Trivial

- **The O(2) complexity claim (Section 4.3) is technically correct for the modeling step but rhetorically inflated.** The overall algorithm cost is dominated by GP fitting and clustering (typically O(n³) for GP). The hypergraph's constant-time relation modeling is a minor efficiency within a larger-cost algorithm.
- A few grammatical issues (e.g., "a obvious" on line 14 should be "an obvious").

## Nice-to-Haves

- Formalize the assumption that "similar solutions have consistent preferences" as a Lipschitz-like condition on the preference function (e.g., if solutions are within ε in the GP-induced metric, their preference differences are bounded by δ). A brief theoretical statement would elevate the heuristic.
- Compare with at least one fixed-solution dueling method (HB, POP-BO) to demonstrate the technique is not limited to the resampling paradigm.
- Add a cross-validation experiment: hold out a subset of preferences, run propagation on the training set, and measure the accuracy of propagated preferences on the held-out set.

## Removed Points

These points from the reviews are flagged to be removed or demoted; treat them with caution:

- **"The accuracy validation is in-sample / circular"** (Harsh Critic Point 1, part). The critic claims the accuracy in Figure 4 is computed "on the same data that was used to define the clusters and generate the augmentations." This is not verifiable from the paper: for synthetic functions the ground-truth objective function is known, and for real-world tasks the benchmark datasets provide ground-truth function values. Accuracy is naturally interpreted as consistency with true function values, not with the original preference labels. The evaluation is likely an out-of-sample check (newly generated preference relations vs. independently known ground truth). However, the paper's failure to explicitly define the accuracy metric is a genuine weakness (kept above).
- **"Figure 6 is missing"** (Harsh Critic, Section 5.4). The paper's main text mentions hyperparameter analysis without referencing Figure 6. Any figure reference to 6 would be in the appendix (which is stripped from the PDF extraction). Per policy, criticisms about missing appendix content are removed.
- **"Excluding HB and POP-BO without justification"** → The paper explicitly scopes to one type of method (Section 3.2, line 80) and states this in the experiment description (Section 5, line 156). This is a justified scope choice, not an omission. The suggestion to also compare is moved to Nice-to-Haves.
- **"The related work section is puzzling"** → The related work adequately describes both method families and the paper clearly states which it addresses.
- Strengths from Strength Finder that are generic or unsupported (generic praise like "this paper addressed an important problem") have been dropped.

## Novel Insights

None beyond the paper's own contributions. The key technical idea — using clustering + hypergraphs to propagate preference relations — is novel within the dueling BO literature, and the empirical demonstration that preference-only methods can compete with function-value-based BO on real-world tasks is the paper's primary value-add.

## Suggestions

1. **Explicitly define the accuracy metric.** State in the caption of Figure 4 (or in Section 5.2) that "accuracy" is the fraction of augmented preferences consistent with the true objective function values (which are known for all benchmark tasks used).
2. **Add a controlled GP-UCB comparison** where the number of observed solutions is equalized (e.g., 15 duels / 30 solutions for RAPBO vs. 30 function evaluations for GP-UCB) to isolate the effect of the propagation technique from coverage differences.
3. **Report confidence intervals** (e.g., 90% bootstrapped) for the main comparisons in Figures 2, 3, and 5.
4. **Specify the logistic noise parameter** τ used for generating simulated preferences from function values.
5. **Provide clustering details** (GMM covariance type, intra-cluster similarity computation) in the main paper or appendix.
