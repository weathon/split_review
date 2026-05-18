Now I have all the information I need. Let me write the consolidated review.

## Summary

The paper proposes a framework for incorporating downstream decision loss into conformal prediction, producing prediction sets that minimize expected decision loss while maintaining standard marginal coverage guarantees. Three methods are developed: (1) Penalized Conformal (tuning λ to weight decision loss against the nonconformity score), (2) Separable Penalized Ratio (hyperparameter-free, based on Neyman-Pearson for separable losses), and (3) a Greedy Optimization method (for non-separable losses). Experiments across five datasets show 60–75% reduction in decision loss over standard conformal prediction, with a dermatology case study illustrating clinically coherent sets.

## Strengths

1. **First principled integration of decision-focused loss into conformal prediction while preserving coverage guarantees.** The paper identifies a clear gap—prior conformal methods ignore downstream decisions, while decision-focused learning neglects uncertainty quantification—and bridges it with three algorithms, each proven to retain the standard conformal coverage guarantee (Propositions 2, 3, and the greedy method proposition).

2. **Handles both separable and non-separable decision losses, including non-monotonic losses.** Unlike conformal risk control (Angelopoulos et al., 2022), which requires losses that decrease with set size, the proposed framework imposes no such monotonicity restriction. This is demonstrated with coverage loss and maximum-distance loss on hierarchical label spaces.

3. **Theoretical finite-sample guarantee for hyperparameter selection (Proposition 1).** Provides a bound of \(2B\sqrt{\log(2|\mathcal{H}|/\delta)/(2n)}\) on excess risk when selecting λ via empirical risk minimization, showing the extra tuning step does not affect the \(O(1/\sqrt{n})\) rate.

4. **Robustness to noisy base classifiers demonstrated by controlled ablation (Figure 4).** On the Fitzpatrick dataset with artificially degraded classifiers, proposed methods consistently outperform standard conformal prediction across all accuracy levels, showing practical utility even with imperfect models.

5. **Significant and consistent empirical improvement across multiple datasets and loss functions.** Reductions in decision loss of 60–75% over standard conformal prediction across CIFAR-100, iNaturalist, ImageNet, and Fitzpatrick, with median-of-means over 10 runs.

## Weaknesses

### Fatal
None.

### Major

1. **Greedy algorithm constraint in Eq. 3 (line 149) is mathematically inconsistent with the coverage target.** The constraint reads:  
   `p̂(y|x) ≤ α - p(S^i_{f(x)})`,  
   where α = 0.1. Since p(S^i) is monotonic increasing and starts at 0, the RHS becomes negative after cumulative probability exceeds 0.1, making the feasible set empty long before the target 1−α = 0.9 is reached. This prevents the algorithm from producing meaningful sets under the stated goal. The intended constraint is almost certainly something involving (1−α) (e.g., `1−α − p(S^i)`). As written, the method is not executable as described, and readers cannot implement it without guessing the intended correction. This is the single most serious flaw in the paper. While it is plausible that the implementation used the correct constraint and only the equation contains a typo, the paper must be corrected and the corrected algorithm's results verified.

2. **Hyperparameter selection procedure (lines 93–97) as described violates standard evaluation principles.** The paper states: "split the data in three folds: a validation set, a test set, and a calibration set… estimate the decision loss on the test set and then select the λ with the best test loss." Using the test set for λ selection contaminates it as an unbiased estimator of generalization performance. The final reported losses may therefore be optimistically biased. The paper must clarify whether a separate held-out set was used for final evaluation or, if not, re-run with a proper train/validation/test split where the test set is used only for reporting.

### Minor

1. **Empirical coverage verification is provided for only one dataset (iNaturalist, Figure 2).** The paper states "We see a similar behavior for all the other datasets" without supporting evidence. While coverage is a provable property of the conformal procedure, providing coverage tables/plots for all datasets and loss configurations would strengthen confidence that the decision-focused optimization does not inadvertently break coverage in practice.

2. **The claim "our method imposes no restrictions on the type of losses that can be chosen" (line 42) is unqualified.** This claim refers to the absence of monotonicity restrictions (contrasting with conformal risk control), but for non-separable losses with no exploitable structure, the optimization step (greedy algorithm) lacks approximation guarantees. The paper should clarify that the statistical guarantee holds for any loss, but computational tractability depends on the loss having sufficient structure.

3. **The "base conformal method" used as baseline is not explicitly named.** While the paper earlier identifies adaptive prediction sets (APS, Romano et al., 2020) as the nonconformity score ρ, explicitly naming the baseline in the results section would improve clarity (this is correctly inferred from context but should be stated directly).

### Trivial
None.

## Nice-to-Haves

- A brief proof sketch for Proposition 2 (Neyman-Pearson optimality for separable losses) citing Sadinle 2019 for the uniform-cost special case — the paper already contains this citation but could add a sketch.
- Quantitative evaluation of "coherence" of prediction sets (e.g., average depth of common ancestor in the hierarchy) to support the qualitative improvement shown in Figure 1.
- Analysis of when each variant excels (penalized vs. ratio vs. greedy) with ablations varying calibration set size.

## Removed Points

These points were raised in the input reviews but are removed based on verification against the paper:

- **"Proposition 2 does not cite a standard reference"** — The paper explicitly cites Sadinle (2019) for the uniform-cost case (line 112) and states the general result follows from the Neyman-Pearson lemma. This is appropriately referenced.
- **"The paper should provide a proof or sketch of Proposition 2"** — The Neyman-Pearson lemma is a classical result; applying it to this setting is standard and a full proof would be a re-derivation. The paper's treatment is appropriate for a conference paper.
- **"The paper does not define the base conformal method"** — The paper identifies APS (Romano et al., 2020) as the nonconformity score ρ on line 78. The baseline is clearly identifiable and standard in the field.
- **"The paper should add Y / domain Z / additional tasks"** — These are scope-creep demands for breadth beyond the paper's own direction.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix Eq. 3.** The constraint in the greedy algorithm should be corrected (likely to involve 1−α instead of α) and the correction should be verified against the implementation. This is the most critical fix.
2. **Clarify the evaluation pipeline.** Specify whether λ selection and final reporting use the same or different held-out data. If the procedure described is incorrect, correct it and re-report results using a proper validation/test split.
3. **Add coverage results for all datasets** (a table in the appendix would suffice).
4. **Qualify the "no restrictions" claim** to distinguish statistical generality from computational tractability.

## Score and Decision

The paper addresses an important and timely problem—incorporating downstream decision loss into conformal prediction—with a clear motivation, principled algorithmic ideas, and extensive empirical evidence. However, two significant issues undermine the presentation: (1) the greedy algorithm's constraint (Eq. 3) is mathematically incorrect as written, and (2) the hyperparameter selection procedure as described violates standard evaluation methodology. Both are potentially fixable (the equation is likely a typo; the pipeline likely used a proper split in practice but was misdescribed), but until corrected, a reader cannot fully trust or reproduce the results. The paper's core contributions (penalized conformal methods, separable penalized ratio, coverage proofs) remain valuable and are not invalidated by these issues. With proper corrections, this would be a solid paper. In its current form, the errors are too significant to overlook.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>