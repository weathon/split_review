- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 8, 8, 6, 6
Now I have a complete understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper bridges conformal prediction with decision-focused machine learning by introducing methods to produce prediction sets that minimize a user-specified downstream decision loss while maintaining standard marginal coverage guarantees. Two families of algorithms are proposed: (1) a "penalized conformal" approach that augments the non-conformity score with a loss-dependent term controlled by a tunable hyperparameter λ, and (2) hyperparameter-free methods — a Neyman-Pearson-derived Separable Penalized Ratio for separable losses and a greedy optimization approach for non-separable losses. The paper provides finite-sample coverage guarantees (matching standard conformal bounds), evaluates methods across CIFAR-100, iNaturalist, ImageNet, and the Fitzpatrick dermatology dataset, reporting 60–75% decision loss reductions, and presents a clinically compelling case study where prediction sets align with diagnostic hierarchies.

## Strengths

- **Finite-sample coverage guarantees for all proposed methods**: Propositions 3 and 4 (lines 115–121, 153–159) prove coverage bounds of \(1-\alpha \leq P(y \in S_{f(X)}) \leq 1-\alpha + \frac{1}{n+1}\), showing that decision-focused conformalization does not sacrifice statistical validity.

- **Consistent and substantial empirical loss reductions**: Across all four datasets (CIFAR-100, iNaturalist, ImageNet, Fitzpatrick) and both separable/non-separable losses, the proposed methods achieve 60–75% reductions in decision loss relative to baseline conformal prediction (Section 4, Figure 3).

- **Real-world clinical applicability demonstrated**: The dermatology case study (Figure 1, Section 4) shows that the proposed method produces prediction sets with coherent clinical meaning (all labels within a malignant epidermal family), while standard conformal sets span benign, malignant, and non-neoplastic diagnoses — directly illustrating how alignment with domain hierarchies supports high-stakes decision-making.

- **Theoretical optimality result for separable losses**: Proposition 2 (lines 108–111) proves that the oracle solution \(H = \{(x,y): p(y|x)/\ell(y) \geq t_\alpha\}\) minimizes expected decision loss while satisfying coverage, providing rigorous justification for the Separable Penalized Ratio.

- **Hyperparameter-free variants**: The Separable Penalized Ratio (Section 3.1.1) and the greedy optimizer for non-separable losses (Section 3.2.1) require no hyperparameter tuning, making the framework more principled and usable than the penalized conformal family alone.

- **Robustness to noisy base classifiers**: The ablation study (Figure 4) shows the proposed methods outperform base conformal prediction at every accuracy level of the underlying classifier (from ~0.2 to ~0.5 on Fitzpatrick), demonstrating practical value with imperfect models.

## Weaknesses

### Fatal

None. The core contributions — the conceptual framework, the coverage guarantees, the hyperparameter-free methods — remain valid. No verified weakness fully invalidates the paper's central claims.

### Major

- **The greedy algorithm equation (Eq. 4, line 149) contains a constraint that is inconsistent with the stated optimization objective.** The plug-in optimization requires \(\sum_{y \in S_x} \hat{p}(y|x) \geq 1-\alpha\) (coverage ≥ 0.9 when α=0.1). However, the constraint in the greedy equation is \(\hat{p}(y|x) \leq \alpha - p(S^i)\), which with α=0.1 permits only very-low-probability labels and blocks all additions once cumulative probability exceeds 0.1 — far short of the required 0.9. This appears to be a sign/inequality-direction error (possibly should involve \(1-\alpha\) instead of α). Since the greedy ordering defines the non-conformity score used in the subsequent split conformal step, this error undermines reproducibility. **Why it matters**: A reader implementing the algorithm as written would obtain a different (and likely poorer) ordering than intended, making the reported empirical results for the greedy method irreproducible from the description alone. The coverage guarantee (Proposition 4) remains valid regardless of the ordering, but the claimed decision-loss optimality of the greedy ordering is unsupported by the published equation.

- **The λ selection procedure for the penalized conformal method is either methodologically flawed or ambiguously described (Section 3.1, lines 95–96).** The paper states: "split the data in three folds: a validation set, a test set, and a calibration set. For each value of λ in ℋ estimate the quantile on the val set. Then, we estimate the decision loss on the test set and then select the λ with the best test loss (λ̂)." Selecting λ based on test-set performance renders the reported test losses optimistically biased for the penalized method (the only method requiring this tuning). The paper does not clarify whether the final reported losses are from the same test set used for selection or from a separate held-out evaluation. This is either a methodological flaw that inflates the headline results for the penalized method, or a writing error that needs correction. **Why it matters**: The paper's claim that "penalized conformal methods, when appropriately tuned, tend to outperform the other methods" (line 191) depends on these potentially contaminated loss numbers. The hyperparameter-free methods are not affected by this issue, but the comparison between penalized and hyperparameter-free methods is unreliable under this protocol.

### Minor

- **No variance or uncertainty measures in experimental results.** All figures and tables report only point estimates (median of means over 10 runs) without error bars, confidence intervals, or standard deviations (lines 170, 183, 198). Given the complex multi-split procedure (calibration, validation, test), hyperparameter selection, and the 10-run repetition, readers cannot assess whether the reported 60–75% loss reductions are statistically significant or within noise range. This weakens the strength of the empirical conclusions but does not invalidate the overall direction of results.

- **Synthetic hierarchy generation for CIFAR-100 and ImageNet.** The paper generates hierarchies via hierarchical clustering on the classifier's own representations (line 172). While this is acknowledged and the bias likely affects all methods similarly, it weakens the external validity of the hierarchy-based loss experiments on these two datasets, since the "expert-defined" structure is derived from the same model being evaluated.

- **The "base conformal" baseline method is not precisely specified.** The paper mentions "adaptive prediction sets (APS)" as background (line 78) but does not state which score function defines the baseline in the experiments. A reader needs this detail to assess fair comparison.

### Trivial

- None to report beyond parser artifacts unrelated to the original submission.

## Nice-to-Haves

- A dedicated table reporting empirical coverage with standard errors for each method and dataset would help validate that coverage guarantees are satisfied in practice (Figure 2 shows one dataset's coverage; extending this to all datasets would be more informative).
- A brief note on the computational cost of the greedy method (which requires per-instance optimization) would help practitioners assess trade-offs.
- A limitations discussion — e.g., sensitivity to classifier miscalibration, or scenarios where the greedy linearization of non-separable losses may be far from optimal.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing conformal risk control baseline (Harsh Critic's Issue #3)**: Removed. The paper's objective is to **minimize** decision loss subject to coverage, which differs from conformal risk control's goal of **controlling** expected loss at a preset level. Moreover, the losses studied (sum of label costs, max pairwise distance, coverage loss) either increase with set size or are non-monotonic, so risk control's non-increasing loss requirement is not satisfied. The paper explicitly discusses the relationship to risk control in the related work (lines 42–43) and explains the distinction. This criticism is not applicable.

- **"Coverage validation missing" (Harsh Critic's Strengthening Section)**: The paper includes Figure 2 showing empirical coverage on iNaturalist data, and the text states "We see a similar behavior for all the other datasets" (line 63). The figure is present in the original PDF.

- **Formatting/reproducibility nitpicks**: The harsh critic's general concerns about reproducibility ("hidden repository," appendix availability) and formatting issues are parser artifacts. The paper's code availability statement (line 228) is standard for a double-blind submission.

- **Strength Finder's generic strengths**: Dropped several generic or sycophantic strengths (e.g., "this paper addresses an important problem") that lacked specific, concrete evidence or conflicted with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an insight that the paper itself fails to articulate.

## Suggestions

1. **Correct the greedy equation constraint (Eq. 4).** Replace the constraint \(\hat{p}(y|x) \leq \alpha - p(S^i)\) with one consistent with the coverage requirement \(\sum \hat{p}(y|x) \geq 1-\alpha\). If the constraint is meant to prevent exceeding the remaining probability budget, it should involve \(1-\alpha\) rather than α, and the inequality direction should be checked.

2. **Clarify and fix the λ selection protocol.** Either confirm that λ is selected on a held-out validation set (not the test set) and the test set is used only for final evaluation, or redesign the experimental protocol to use three independent splits: validation (λ selection and initial quantile estimation), calibration (final quantile estimation for the selected λ), and test (final evaluation, used exactly once).

3. **Add error bars or confidence intervals** (e.g., standard deviations across the 10 runs, or bootstrapped intervals) to all experimental figures and tables.

4. **Specify the exact baseline algorithm** (e.g., "baseline conformal uses the APS score \(\rho(x,y)\) with no loss penalty, i.e., λ=0") in the experimental setup.

5. **Report empirical coverage** for all methods and datasets in a dedicated table to complement the marginal guarantees.
