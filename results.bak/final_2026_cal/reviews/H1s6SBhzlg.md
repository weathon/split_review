Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper introduces two aggregation algorithms—Optimal Weight (OW) and Inverse Surprising Popularity (ISP)—for combining responses from multiple LLMs. OW achieves Bayesian-optimal aggregation when agent accuracies are known (Theorem 1), while ISP provably dominates majority voting using only second-order (pairwise-correlation) information (Theorem 2). The paper also provides practical label-free pipelines (OW-L, OW-I) that estimate accuracies from second-order information. Experiments on simulated data, UltraFeedback, MMLU, and a healthcare dataset (ARMMAN) show consistent improvements over majority voting.

## Strengths

- **Bayesian optimality of OW (Theorem 1).** The paper proves a clean, non-trivial result: a simple linear aggregator with sigmoid-inverse weights is Bayesian-optimal among *all* aggregation rules under conditional independence. This is a genuine theoretical advance that connects weighted voting to the Bradley-Terry model (Corollary 1) and clarifies when majority voting itself is optimal (Corollary 2, homogeneous agents).

- **Explicit expected-advantage formulas for ISP vs. MV vs. SP (Theorem 2).** The paper provides closed-form expressions for the gaps in expected advantage between ISP, MV, and SP, showing that ISP > MV > SP in expectation. The result is non-trivial and correctly notes the vanishing advantage as the number of options K grows.

- **Consistent outperformance across simulation and three real-world datasets (UltraFeedback, MMLU, ARMMAN).** Every proposed method (OW-L, OW-I, ISP) beats MV on all three datasets. On the subset where models disagree, absolute gains reach 2.78–3.36%. The per-question comparison (Table 4) and statistical significance tests further support the empirical claims.

- **Practical estimation pipelines without ground truth (OW-L, OW-I).** The paper addresses the key practical barrier to using OW (unknown accuracies) by estimating accuracies from second-order information alone. This makes the theory applicable to unsupervised settings.

## Weaknesses

### Major

- **No formal train/test split for second-order estimation.** The paper estimates the conditional probabilities $\hat{\mathbb{P}}(A_i|A_j)$ from the full dataset and uses these estimates to compute the ISP advantage and OW weights on the *same* dataset. While the estimated quantities are population-level parameters (not per-question features), and Theorem 3 provides a finite-sample bound that partially accounts for this reuse, a proper held-out split or cross-validation would be the standard practice. The concern is that for smaller datasets or highly heterogeneous questions, some information leakage could inflate the reported gains. This does not invalidate the results (Theorem 3 bounds the penalty to $\tilde{O}(\sqrt{1/M})$), but it weakens the empirical rigor.

- **No comparison to confidence-weighted aggregation baselines.** The related work (Section 1.1) directly cites Chen et al. (2023a) and Fu et al. (2025), who show that aggregation using LLM confidence scores (readily available as log probabilities) improves accuracy. Since these methods operate in the same unsupervised setting and require no ground truth, their omission from the experiments makes it hard to assess whether the proposed methods offer advantages over simpler alternatives.

### Minor

- **Modest absolute improvements.** Gains over MV are 0.54–1.45% on full datasets and 1.16–3.36% on the disagreement subset. While statistically significant and consistent, these are incremental rather than transformative.

- **Inconsistency in $\sigma_K$ definition.** The abstract defines $\sigma_K(x) = x^2/(K-1+x^2)$, while Section 3 (line 77) defines $\sigma_K(x) = e^x/(K-1+e^x)$. Corollary 1 uses the logistic function $e^x/(1+e^x)$, confirming the Section 3 version is correct. This inconsistency is confusing and should be fixed.

- **No explicit tie-breaking rule for MV on real data.** The simulation section specifies "ties are broken uniformly at random," but this is not stated for the real-data experiments (Table 3).

- **Statistical test choice.** A t-test on per-question accuracy (binary outcome) is used; McNemar's test or a proportion test would be more appropriate for paired binary outcomes.

- **No ablation on the number of agents $N$.** All experiments fix $N=4$. The authors could strengthen the paper by showing how ISP/OW performance scales with $N$.

### Trivial

- The notation $\sigma_K^{-1}(x_i)$ in Algorithm 1 (line 86) has a formatting issue: the $\arg\max$ expression is missing a closing delimiter.

## Nice-to-Haves

1. Include confidence-based aggregation (log-probability weighting) as a baseline to clarify where the proposed methods add value.
2. Use a held-out split or cross-validation for estimating second-order information to eliminate any data-leakage concern.
3. Discuss computational cost: estimating $N^2 K^2$ conditional probabilities scales as $O(M N^2 K^2)$, which is worth acknowledging.
4. Report effect sizes and confidence intervals alongside t-statistics.

## Removed Points

- **"Random shuffling claim insufficiently justified"**: The deferred justification to Appendix B.1 is standard practice; the main text provides enough intuition.
- **"MV tie-breaking unspecified for real data"**: Minor, moved to Minor.
- **"ARMMAN class imbalance"**: Speculative without evidence; the paper reports the metric standard for the domain.
- **"No discussion of computational cost"**: Moved to Nice-to-Haves.
- **"The gain is small"**: Moved from "fatal" framing to Minor, as the gains are consistent and statistically significant.
- **"The critical issue is fatal/structural"**: Downgraded from fatal to Major because Theorem 3 explicitly accounts for finite-sample estimation and the per-question leakage is $O(1/M)$; a train/test split would be better but the current approach is not invalid.
- **Strength Finder's generic strengths** (e.g., "the paper addresses an important problem"): Removed for lacking specificity. Only concrete, evidence-backed strengths are retained.

## Novel Insights

Beyond the paper's own contributions, the most striking observation is the precise characterization of when *second-order* methods can outperform simple majority voting and when they cannot: ISP's advantage over MV scales as $\Theta(1/K)$ and vanishes as the number of options grows. This provides a clear practical guideline—ISP is worth using when $K$ is small (e.g., binary preference tasks) but offers diminishing returns for multiple-choice tasks with many options. Additionally, the result that SP *underperforms* MV in the LLM setting (contrary to human-subject studies) is an interesting negative result that underscores how LLM systematic biases differ qualitatively from human biases.

## Suggestions

1. **Fix the $\sigma_K$ inconsistency** between the abstract and Section 3.
2. **Add a train/test split** (or leave-one-question-out evaluation) for second-order estimation to rule out data-leakage concerns.
3. **Include confidence-weighted baselines** (log-probability weighting or confidence-thresholded MV) to contextualize the improvements.
4. **Specify tie-breaking for MV in real data experiments** and use McNemar's test for binary outcomes.
5. **Report results with varying $N$** (number of agents) to demonstrate scalability.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing.** Queried three bands on LLM aggregation / information aggregation topics:

| Band | Anchors | Avg scores |
|------|---------|------------|
| Low (<3.5) | e95povsLp5, pkHaUX69ZN, viySlQiXEA, q9BK5v9wrJ | 2.0–3.0 |
| Mid (3.5–7.5) | VtN1z92lvu, 2LcxmMKURb, x85kiYqL4y, d1KDC56u5c | 4.0–6.67 |
| High (>7.5) | 9gw03JpKK4, VKGTGGcwl6, DM0Y0oL33T, kkBOIsrCXh | 8.0 |

**Round-1 bracket: 4.5–6.8.** The paper is clearly stronger than the <3.5 papers (which are mostly rejected) and clearly not at the 8.0 level (which are oral papers on different topics). It sits in the mid band.

**Round 2 — Narrowing.** Queried two bands: (4.5, 6.5) and (6.0, 7.5). Key anchors read in full:

| Anchor | Score | Comparison |
|--------|-------|------------|
| VtN1z92lvu — Decision Aggregation under Quantal Response | 6.67 | Similar topic (aggregation with theory + LLM experiments). Cleaner evaluation but less comprehensive experiments. Our paper has stronger theory (Bayesian optimality vs. minimax regret) but a weaker evaluation protocol. Comparable overall; our paper slightly weaker due to evaluation concern. |
| x85kiYqL4y — Optimal Aggregation of LLM and PRM Signals | 5.00 | Questionable assumptions, marginal gains. Our paper is clearly stronger (cleaner theory, broader experiments). |
| EUu8TILWpR — Context Learning for Multi-Agent Discussion | 6.50 | Different approach (learned context generators for discussion). Stronger empirical gains (20–50%) but less theoretical depth in aggregation. |

**Final calibration:** The paper sits between 5.5 and 6.5. Compared to the Decision Aggregation anchor (6.67), our paper has stronger theoretical contributions (Bayesian optimality, explicit advantage formulas) and more comprehensive experiments (4 datasets vs. 1), but is held back by the evaluation protocol concern and missing baselines. A score of **6.0** positions it as a solid paper with clear theoretical contributions and broad empirical validation, below the strongest anchor due to methodological gaps but above the weaker anchors.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>