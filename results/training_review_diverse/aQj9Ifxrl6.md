Now I have all the information needed. Let me compile the final consolidated review.

## Summary

This paper proposes GSR (Group-robust Sample Reweighting), a two-stage method for improving model robustness to subpopulation shifts. The key idea is to use a small set of group-labeled data as a *target* to reweight a larger set of group-unlabeled training data via influence functions, rather than using group labels for direct training or model selection. By restricting the inner optimization to last-layer retraining (LLR), the objective becomes strongly convex, enabling exact gradient computation via the inverse Hessian (implicit differentiation) instead of the one-step truncated backpropagation used in prior work. The paper reports a 1.0% average absolute improvement in worst-group accuracy over DFR (the prior best method using the same amount of group labels), along with robustness to class-label noise in the held-out set.

## Strengths

1. **Principled use of influence functions for group-robust reweighting.** By restricting the inner loop to ℓ₂-regularized last-layer retraining, the inner objective is strongly convex (Assumption 3.1), making the Hessian invertible and the implicit gradient exact via Equation 6. This is a clean, well-motivated theoretical contribution that distinguishes GSR from the one-step truncated approximation used in MAPLE. The consistent degradation of GSR-HF (the Hessian-free variant) across all four benchmarks in Table 1 validates that the Hessian term matters.

2. **Consistent improvement over the strongest same-label-usage baseline.** GSR achieves a 1.0% average absolute improvement over DFR (which uses the same amount of group labels) across four standard benchmarks, with the largest gains on the harder datasets (CivilComments: +3.1%, MultiNLI: +0.8%). The improvement is not uniform—Waterbirds shows a slight regression (−0.3%)—but the consistency across datasets (GSR ranks at or near the top on all four) is itself a finding worth reporting, as many prior methods are less stable.

3. **Robustness to class-label noise in the held-out set.** Section 5.3 shows that GSR's worst-group accuracy degrades only minimally even with 40% random label flips in the held-out set. The weight distribution analysis (Figures 4b–4c) reveals that GSR automatically assigns near-zero weights to corrupted minority samples, effectively "cleaning" the training data. This is a practically useful property and is well-demonstrated.

4. **Informative weight-distribution analysis.** The paper goes beyond reporting aggregate results to show how weights evolve across groups (Figure 1) and their within-group distribution (Figure 2). These visualizations provide intuition for why the reweighting helps—minority-group weights increase, majority-group weights with spurious correlations decrease—and are a genuine strength of the exposition.

## Weaknesses

### Fatal

None.

### Major

None. While several issues below merit attention, none invalidate the paper's core claims or results.

### Minor

1. **The empirical gains are modest and partly dataset-dependent, and the framing slightly overstates them.** GSR's 1.0% average improvement over DFR is driven largely by CivilComments (+3.1%); on Waterbirds, GSR is *worse* than DFR (91.9 vs. 92.2), and on CelebA the gain is only +0.3%. The abstract states that GSR "even outperforms approaches that require significantly more group labels" without qualification. This is true on MultiNLI and CivilComments (where GSR beats Group DRO) but false on Waterbirds and CelebA (where Group DRO outperforms GSR by 0.7% and 0.5%, respectively). The paper does acknowledge "close-to-SoTA" on Waterbirds and CelebA in Section 5.1, but the unqualified abstract-level claim risks misleading a casual reader. The contribution is real but incremental in magnitude; the paper would benefit from more precise language about where and why the gains concentrate.

2. **The model selection criterion (Algorithm 1, line 17) uses average validation loss rather than worst-group validation loss.** The algorithm selects the last-layer parameters $\psi^{(t)}$ that minimize $\hat{\mathcal{R}}(\mathcal{D}^\mathrm{v}; (\phi^*, \psi^{(t)}))$—the *average* loss on the validation set—rather than the worst-group loss. Since the paper's goal is worst-group accuracy, this choice is surprising and is not justified. The validation set is split from the original validation set and is thus small, so per-group estimates may be noisy, but the paper should explain this design choice or show that using worst-group loss instead does not materially change results.

3. **The adaptive aggregation of influence scores (Algorithm 1, lines 7–14) is imported from Group DRO without ablation.** The paper notes that "only optimizing for the worst group in one step can be inefficient" (Section 3), but does not analyze whether the multiplicative update with temperature $\tau$ is crucial. An ablation comparing adaptive aggregation against simply using the worst-group influence each step would clarify whether this added complexity carries its weight.

4. **The GSR-HF ablation is suggestive but does not fully isolate the Hessian's benefit.** GSR-HF replaces the influence-function gradient with the MAPLE-style one-step approximation while keeping the LLR framework. The consistent gap in Table 1 supports the importance of the Hessian. However, both methods freeze the representation and only retrain the last layer, and the one-step approximation may interact differently with LLR than with full-network training. While the theoretical motivation for the Hessian is solid, the ablation is not perfectly controlled. This is a minor point—the empirical trend is clear—but worth noting.

5. **Mean (average) accuracy is not reported alongside worst-group accuracy.** The paper acknowledges in the conclusion that GSR "usually results in a decrease in mean performance" (Section 7) and that this is a known trade-off, but does not quantify the cost in the main results. Given that GSR is motivated by improving robustness, the magnitude of the average-accuracy penalty should be transparent (even if deferred to an appendix).

### Trivial

- The number of outer-loop iterations $T$ is listed as a hyperparameter in Algorithm 1 but never specified or analyzed. A brief statement of the values used would help reproducibility.
- The computational cost is described as "lightweight" and "inexpensive," but no runtime comparison to DFR (which trains the last layer once) is provided.

## Nice-to-Haves

- **Sensitivity analysis for the held-out fraction $\alpha$.** The paper uses 10% by default but does not study its impact. Since the held-out set is used for both reweighting and last-layer training, its size affects the trade-off between informativeness of the weights and remaining training data for representation learning.
- **Convergence characterization for the outer loop.** The outer objective is nonconvex due to adaptive aggregation and the dependence on $g^*$; a brief discussion of whether convergence to a stationary point is expected (or whether the algorithm is best viewed as a heuristic) would strengthen the "theoretically sound" claim beyond the exactness of the inner gradient.
- **Comparison of weight distributions between GSR and DFR failure cases.** On Waterbirds (where DFR slightly outperforms GSR), is GSR's weight assignment noisier? On CivilComments (where GSR gains most), what distinguishes the reweighting pattern? Such analysis would sharpen the paper's central argument about when the reweighting paradigm extracts more value from limited group labels.

## Removed Points

- **Criticism about the "annotation errors for group labels" claim being overstated (Harsh Critic, Other Observations, second bullet).** The paper states: "Since the group labels for the held-out sets are not used for retraining, GSR is not affected by the annotation errors for group labels." This is factually correct—GSR never consults group labels for the held-out set, so any errors in those labels are irrelevant. The red-box example in Figure 3 simply illustrates that a waterbird whose background arguably resembles land is correctly identified as a minority sample despite its background label being potentially debatable. The reviewer's claim that "no group-label errors exist in the Waterbirds held-out set (group labels are not used there)" misreads the paper's point: the paper is not asserting actual errors exist, it is demonstrating the method's principled *invariance* to such errors. Removed as a misunderstanding.
- **Strength Finder point about "State-of-the-art... superiority over methods requiring more labels" — weakened.** As noted in Weakness 1, this claim is true on 2 of 4 datasets but not on Waterbirds and CelebA. The strength is retained but calibrated.

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between the paper's two main technical ingredients. The influence function gives exact gradients *because* LLR makes the inner problem strongly convex—but LLR also limits the method to fixing only the last-layer classifier, not the representations. This means GSR inherits whatever biases exist in the ERM-learned features, which may explain why on Waterbirds (where representations are already good enough for DFR to work near-optimally) GSR's fine-grained reweighting adds little and can even hurt. Conversely, on CivilComments (where group imbalance is extreme and overlapping), the reweighting provides value precisely because the last-layer-only approach is already the bottleneck. This suggests the method's gains concentrate in settings where the representation is reasonable but the last-layer classifier needs careful per-sample calibration—an empirical hypothesis the paper could test more directly.

## Suggestions

1. Qualify the abstract-level claims to reflect where GSR outperforms Group DRO (MultiNLI, CivilComments) versus where it is close but behind (Waterbirds, CelebA).
2. Justify (or fix) the model selection criterion in Algorithm 1: if worst-group loss on the validation set is too noisy due to small sample size, state this explicitly.
3. Add an ablation removing the adaptive aggregation (lines 7–14) and using only the worst-group influence at each step.
4. Report mean (average) accuracy alongside worst-group accuracy, at least in supplementary material, so readers can assess the robustness-vs.-average trade-off quantitatively.
5. Include a sensitivity analysis for the held-out fraction $\alpha$ (used 10% by default) and report the number of outer-loop iterations $T$ used in practice.

## Score and Decision

This is a solid, well-motivated paper with a clean theoretical connection (influence functions + LLR), thorough experiments on four standard benchmarks, and informative weight-distribution analysis. The contribution is real but incremental: a ~1% average improvement over the strongest baseline, concentrated on harder datasets, with some overclaiming in the abstract. The core technical idea—using group labels as a target for reweighting rather than direct training—is sound, and the use of implicit differentiation via LLR is both principled and practical. The weaknesses identified are addressable and do not threaten the paper's central claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>