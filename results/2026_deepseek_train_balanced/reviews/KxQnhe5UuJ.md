## Summary

This paper addresses a practical and underappreciated problem in continual learning (CL): most HPO in CL research uses an "end-of-training" framework that assumes multiple passes over the full data stream, which is unrealistic for deployment. The paper systematically compares five HPO frameworks (end-of-training, first-task, current-task, seen-tasks (Mem), seen-tasks (Val)) across five CL methods, four datasets, and two task settings. The central finding is that no HPO framework consistently outperforms the others on current benchmarks, leading the authors to recommend that practitioners select HPO frameworks based on secondary criteria like compute efficiency (favoring first-task HPO as the most efficient realistic option).

## Strengths

- **Comprehensive and systematic comparison.** The paper benchmarks 5 HPO frameworks × 5 CL methods × 4 datasets × 2 evaluation scenarios — the first such head-to-head comparison in the literature. Prior work proposed or used individual HPO frameworks in isolation without a controlled side-by-side evaluation, making this breadth a genuine contribution.

- **Rules out the trivial explanation.** Figure 3 shows that hyperparameter configurations produce a wide range of validation accuracies for DER++, confirming that the similarity across HPO frameworks is not because "any hyperparameter works." This tightens the argument: HPO matters, but which *framework* is used to select hyperparameters does not drive performance differences on these benchmarks.

- **Quantified compute-performance tradeoff for first-task HPO.** The paper reports concrete average gaps from end-of-training to first-task HPO (−0.39% to −0.91%), providing a specific empirical basis for the recommendation that first-task HPO sacrifices little accuracy for large compute savings.

- **Analytical complexity comparison in Table 1.** The paper provides a clear O(K·T) vs. O(K+T) breakdown of time complexity, which usefully formalizes the efficiency differences between frameworks even without wall-clock measurements.

## Weaknesses

### Fatal

None.

### Major

- **Insufficient statistical support for the central equivalence claim.** The paper's main finding — that no HPO framework is consistently better — is a negative/equivalence-type claim that requires strong evidence. However, experiments use only 3 seeds, and the analysis relies on an ad hoc +0.5% threshold for "noticing" differences rather than formal statistical testing (confidence intervals on differences, Bayesian equivalence tests, or rank-based aggregation). With 3 seeds and no inferential statistics, it is unclear whether the frameworks are genuinely similar or whether the experiment simply lacked sensitivity to detect real differences. The 0.5% threshold is introduced without justification (why 0.5% rather than 1% or 0.2%?) and is applied uniformly without reference to the standard error of each estimate. This does not invalidate the paper's contribution, but it weakens the confidence readers can place in the headline empirical finding.

### Minor

- **The "heterogeneous" task setting is not heterogeneous in a way that tests the paper's own hypothesis.** The heterogeneous setting divides the same image datasets (CIFAR-100, Tiny ImageNet) into more tasks (20 vs. 10) with uneven class counts, but all tasks are natural images from the same domain, using the same backbone and augmentations. The paper's own rationale for this setting is to "test whether dynamic HPO becomes more beneficial when tasks differ," but the tasks differ only in size and class count, not in domain, modality, or distribution. A genuinely heterogeneous stream (e.g., first task MNIST-style digits, later tasks natural images) would be needed to probe whether task-specific HPO adaptation matters. The paper's finding that dynamic HPO does not help in this setting is correspondingly less informative. (The paper does partially acknowledge this as an "open question" about benchmarks, which mitigates the severity.)

- **No quantitative compute measurements.** The paper explicitly recommends selecting HPO frameworks based on compute efficiency and identifies first-task HPO as the most efficient, but reports only analytical time complexity (Table 1). A practitioner deciding between frameworks needs actual runtime data (wall-clock time, GPU-hours, or comparable measurements on a representative setting) to calibrate the tradeoff. This is a concrete gap in the paper's own practical recommendation.

- **Consistent (albeit small) disadvantage of first-task HPO is underplayed.** The paper reports average gaps of −0.39% to −0.91% from end-of-training to first-task HPO, yet the overall framing emphasizes that "all frameworks perform similarly." In the tables, many first-task HPO entries are unbolded (meaning they are within 0.5% of the best), which supports similarity. But the consistent negative sign of the gap suggests a small but reliable penalty for first-task HPO that the "similar" framing elides. A more precise summary — "first-task HPO is slightly worse on average but much cheaper" — would better serve practitioners.

- **The hyperparameter configuration distribution analysis (Figure 3) is shown only for DER++.** The argument that hyperparameter choice matters (ruling out the trivial explanation) would be stronger if replicated for at least one or two more CL methods (e.g., ER, ESMER).

### Trivial

None.

## Nice-to-Haves

- **Analysis of which hyperparameters are selected by each framework.** Reporting the distribution of selected learning rates and regularization coefficients per framework could reveal whether frameworks converge to similar points or different points in HP space with similar accuracy — either finding would enrich the interpretation of equivalent average performance.

- **Ablation on validation split size.** The paper uses a fixed 10% validation split per task; results may depend on this choice, and a brief sensitivity analysis would strengthen the conclusions.

## Removed Points

These points were flagged by the reviewers but are removed from the main review for the following reasons:

- **The paper's introduction overstates the problem / CL research has different goals** — This is the reviewer's opinion about research priorities, not a factual weakness in the paper. The paper's motivation is clearly scoped to deployment-oriented HPO.
- **Prior HPO work discussion insufficiently critical** — A nice-to-have addition, not a weakness. The paper covers relevant prior work adequately.
- **Online CL setting not discussed** — The paper explicitly studies standard CL (offline CL); demanding a different setting is scope creep.
- **Seen-tasks (Val) memory cost not quantified** — The paper acknowledges this with an asterisk in Table 1; quantification would be nice but is a minor implementation detail.
- **Missing related works** — Automatically removed per instructions; no external confirmation available.
- **Formatting/style nitpicks** — Parser artifacts, not author errors.
- **"First-task HPO is slightly worse on average, not just similar"** — The paper already reports the numerical gaps (−0.39% to −0.91%) and frames the tradeoff in those terms. The critic's suggested reframing is close to what the paper already does; this is preserved in the minor weaknesses section as an underplayed framing issue rather than removed entirely. Actually, the paper does report the gaps, so this is largely addressed. I've kept a tempered version of this in "Minor."
- **The failure mode of first-task HPO is not tested** — The paper explicitly acknowledges this as an "open question." The harsh critic's framing implies the paper overclaims when it does not. However, the practical recommendation could be seen as overly broad, so I've kept a tempered version in Minor.

## Novel Insights

The most interesting observation from these reviews is the tension between the paper's two contributions: (1) the claim that no HPO framework is consistently better, and (2) the recommendation to use first-task HPO for efficiency. If the frameworks are truly equivalent *in performance*, the recommendation reduces to a purely practical one. But if the experiment simply lacked power to detect true differences, then the recommendation to use first-task HPO could be premature — the slightly worse average performance might signal a real gap that more runs would confirm. The paper's own reported numbers (−0.39% to −0.91%) lean toward a small but real gap, which would change the recommendation from "these are equivalent; pick by compute" to "you pay a small accuracy cost for first-task HPO; decide if it's worth it." This subtle distinction matters for practitioners, and the paper would benefit from explicitly addressing it.

## Suggestions

1. **Add formal statistical comparisons.** Report confidence intervals on pairwise differences between frameworks or a rank-based aggregation (e.g., average rank across all conditions). Even a simple sign test on which framework wins more often would be more informative than the binary bold/not-bold threshold.

2. **Report wall-clock time or GPU-hours** for at least one representative condition (e.g., DER++ on CIFAR-100) to provide the compute-efficiency evidence that the paper's own recommendation requires.

3. **Test the first-task failure mode explicitly.** Construct one CL stream where the first task is from a genuinely different distribution (e.g., first task contains only coarse-grained classes while later tasks are fine-grained) to establish boundary conditions on the first-task HPO recommendation.

4. **Increase the number of random seeds** from 3 to at least 5–10 for one key condition to verify that the equivalence finding is not an artifact of low statistical power.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>