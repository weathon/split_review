## Summary

This paper proposes Fleet-Merge (FedRebasin), an algorithm for merging RNN-parameterized control policies trained on distributed, heterogeneous datasets without centralizing the data. The method extends prior model-merging techniques (permutation alignment via soft permutations) from feedforward networks to recurrent neural networks in the control setting, and introduces a new Drake Tool-Use Benchmark for contact-rich manipulation. The core idea — aligning multiple RNN policies to a shared reference using local data only — is well-motivated and represents a sensible extension of the GitRebasin / Peña et al. lineage.

## Strengths

- **Formal characterization of RNN permutation invariance.** Proposition 1 and Equation 8 (lines 248–258) explicitly define how permutation symmetries act on both feedforward and recurrent weight matrices of Elman RNNs, and prove the invariance formally. Prior model-merging work (GitRebasin, REPAIR) only handled feedforward networks; extending this treatment to the recurrent case is a nontrivial and necessary generalization for partially-observed control tasks.

- **Algorithm uses only local datasets for alignment, eliminating the need for shared data.** In Algorithm 1 (Line 233), each agent updates its permutation using trajectories sampled only from its *local* dataset $\mathcal{D}_{\mathrm{local},i}$. This departs from Peña et al. (2022), which required a common dataset $\mathcal{D}$ for the aligning updates. In the fleet setting where data cannot be centralized or shared, this design is a concrete algorithmic advance.

- **Introduction of the Drake Tool-Use Benchmark.** The paper develops a benchmark with four task families (wrench, hammer, spatula, knife) in the Drake simulator with parameterized initial conditions (lines 313–316). This fills a gap in available benchmarks for evaluating policy merging in compositional, contact-rich manipulation.

## Weaknesses

### Fatal

None.

### Major

- **No numerical results reported anywhere in the text.** Every experimental finding is stated in qualitative, narrative terms. Section 5 (Linear Policy Merging) says averaging "can improve performance" and gradient-based methods "can outperform alternation-based methods" — but provides no success rates, no rewards, no loss values, no effect sizes. Section 6.1 (Drake Tool-Use) claims "almost zero performance barriers" and robustness to model count — again, no numbers. Section 6.2 (Meta-World) claims "the gradient-based algorithms achieve the best performance" and that a "simple multi-task learning agent can solve all 50 tasks" — but the best performance *how much better*, and *how many* of the 50 tasks reached what threshold, is never stated. There are zero tables, zero numerical callouts in the text, no standard deviations, and no number of seeds or trials reported. All results are deferred to figures, which is insufficient to support the paper's quantitative claims. For a paper that asserts a "50% improvement" over baselines, the reader must be able to find a specific table or sentence that anchors that number to a metric, baseline, and condition — and such a sentence does not exist.

- **The "over 50%" improvement claim is unsubstantiated.** Line 61 asserts that Fleet-Merge "outperforms baselines by over 50%." I searched the full text: no metric, no baseline, no experimental condition is ever identified for this number. It is stated as a contribution but never validated or even contextualized in the experiments. This is not a minor oversight — it is a central quantitative claim with zero supporting evidence in the paper as written.

- **Hyperparameter values for Algorithm 1 are entirely omitted.** The algorithm lists as inputs: epoch length $E$, inner iterations $T$, stepsize $\eta$, soft-projection parameter $\tau$, and the subset sampling $\mathcal{I} \subset [N]$. None of these values, nor the subset size or sampling distribution, are reported anywhere in the paper. Without these, the method cannot be reproduced.

### Minor

- **The Drake benchmark is described too thinly.** The four task families are introduced in a single paragraph (lines 315–316) with no per-task success criteria, observation/action specifications sufficient for independent implementation, or reference results from representative methods. A benchmark is only useful to the community if it comes with actionable baselines and sufficient specification for reproduction. In its current form, this contribution is incomplete.

- **No ablation studies.** The method has at least three design components that could be ablated: soft vs. hard permutations, gradient-based vs. LAP-based alignment, and one-shot vs. iterative merging. None are isolated to measure their individual contributions. While not fatal, this omission limits insight into what drives performance.

- **No discussion of computational cost.** The paper does not report training time, Sinkhorn iteration count, or how the algorithm scales with the number of models $N$.

### Trivial

None.

## Nice-to-Haves

- Adding confidence intervals or error bars (even from a single figure) would substantially strengthen the empirical claims.
- A table reporting the key numerical results across all three experimental settings (LQG, Drake, Meta-World) would be the single most impactful addition.
- A discussion of failure cases or boundary conditions (high task heterogeneity, very different architectures, extreme non-IID data) would improve credibility.

## Removed Points

These points were flagged by the reviewers but removed under the filtering rules. Treat them with caution:

- *"The benchmark is not released or specified in a reproducible way"* — Removed per Hard Rules: do not question release status of cited resources.
- *"The relationship to prior work could be clearer"* — Removed as vague; the paper adequately distinguishes its approach from prior work.
- *"No related works on X"* — Removed per Hard Rules: do not mention missing related works without external sources.
- *"Formatting/grammar issues"* — Removed as parser artifacts, not author errors.
- *"Strength: the problem is important"* — Removed as generic; not a concrete paper-specific strength.
- *"Strength: addresses an important problem"* — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the paper's content that the authors did not themselves make, except the severity of the evidentiary gap.

## Suggestions

1. **Add at least one comprehensive results table** reporting, for each experimental setting (LQG, Drake, Meta-World), the task success rate (or reward/error) for each method with variance estimates. Directly anchor the "50% improvement" claim to a specific table entry and explain which baseline and metric it refers to.

2. **Report all hyperparameter values** for Algorithm 1: $E, T, \eta, \tau$, subset size and sampling distribution, number of Sinkhorn iterations.

3. **Expand the Drake benchmark section** to include per-task success criteria, reference results from at least naive averaging and single-task training, and enough detail for independent reproduction.

4. **Include a limitation paragraph** — when does the method fail? Under task heterogeneity, architectural differences, or non-IID extremes, does merging still work?

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>