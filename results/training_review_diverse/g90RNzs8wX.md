Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper introduces UGOLD, the first unified benchmark that bridges unsupervised graph-level anomaly detection (GLAD) and unsupervised graph-level out-of-distribution detection (GLOD) under a common formulation of "generalized OOD detection." It compares 16 representative methods across 35 datasets spanning four practical scenarios (intrinsic anomaly, class-based anomaly, inter-dataset shift, intra-dataset shift) and analyzes them along four dimensions: effectiveness, generalizability, robustness, and efficiency. The paper's key findings include that near-OOD samples are consistently harder to detect than far-OOD, most methods degrade significantly under training-set contamination, and end-to-end methods generally outperform two-step pipelines.

## Strengths

- **First unified evaluation framework bridging GLAD and GLOD.** The paper defines a generalized graph-level OOD detection problem encompassing both tasks and assembles 35 datasets across four distinct scenarios to enable direct comparison of 16 methods that were previously evaluated in isolation (Section 3.1, Table 1). This addresses a genuine gap in the literature: researchers in each sub-area previously had no common ground for method comparison.

- **Multi-dimensional analysis beyond leaderboard rankings.** The benchmark evaluates methods across effectiveness (RQ1), generalizability to near- vs. far-OOD (RQ2), robustness to training-set contamination (RQ3), and computational efficiency (RQ4). This yields actionable insights — e.g., near-OOD awareness as a concrete research target, and the vulnerability of most methods to even 10–30% contamination — that go deeper than a single ranking table.

- **Empirically grounded challenges for the field.** Observations such as "no universally superior method" (Observation 183), "near-OOD samples are harder to detect" (Observation 186), and "performance degrades with increasing contamination" (Observation 188) are directly supported by the experimental design and provide clear motivation for future work. The paper also translates these findings into specific future directions (Section 5).

- **Evidence that end-to-end methods outperform two-step pipelines.** The benchmark shows that end-to-end methods achieve better average rankings and also deliver competitive or better time/memory efficiency (Observation 185, Fig. 5), giving practitioners a clear practical recommendation.

## Weaknesses

### Fatal

None.

### Major

- **Hyperparameter search conducted on the test set (Section 3.3).** The paper explicitly states: *"we conduct a random search to find the optimal hyperparameters w.r.t. their performance on the testing set"* (line 118). This is a significant methodological concern for a benchmark paper. Tuning on the test set leaks label information, produces optimistically biased results, and may favor methods with more flexible hyperparameter spaces (who can overfit more aggressively to test set noise). All quantitative results in Table 1 and the associated observations (182–185) are affected. The paper frames this as obtaining "upper bounds," which is a transparent justification, but for a benchmark that aims to provide reliable comparisons the community can build on, standard practice requires holding out a validation split from the training (ID) set for hyperparameter selection. The reported AUROC/AUPR/FPR95 numbers cannot be taken at face value as achievable performance estimates.

  That said, this flaw is not fatal because: (a) the authors are transparent about the procedure, (b) the key *qualitative* insights (near-OOD > far-OOD difficulty, vulnerability to contamination, no universal method) are relative comparisons that are unlikely to be reversed by proper validation, and (c) the relative rankings across methods, while possibly biased by differential hyperparameter flexibility, may still carry signal. However, the paper's central quantitative claims — the specific numbers in tables and the precise rankings — require re-running with a proper validation split before they can be trusted.

- **Ambiguity about hyperparameter selection in RQ2 (generalizability) and RQ3 (robustness).** The paper does not state whether hyperparameters were re-tuned for the near/far-OOD splits (RQ2, Section 4.2) or for each contamination level in the robustness study (RQ3, Section 4.3). If the test-set-tuned hyperparameters from RQ1 were reused, they may be suboptimal under different distribution shifts; if they were re-tuned on each new test set, the overfitting compounds; if default parameters were used, the conditions are inconsistent with RQ1. This ambiguity undermines the interpretability of these experiments.

### Minor

- **Inconsistency between hyperparameter strategies across research questions.** RQ1 uses test-set-tuned hyperparameters (framed as "upper bounds"), while RQ4 uses default hyperparameters (line 232). This makes it difficult to triangulate findings across dimensions — e.g., the claim that end-to-end methods are superior in *both* effectiveness and efficiency (Observation 190) rests on comparisons that used different hyperparameter selection strategies for each dimension.

- **No statistical significance analysis.** The paper's observations and rankings (e.g., "end-to-end methods have average rankings below 8, while 2-step methods rank above 8") are reported without any statistical test (e.g., paired Wilcoxon, Bayesian ranking). Given the variance across 35 datasets, some rankings may be fragile. This is addressable and would strengthen the conclusions.

- **The random search budget (20 trials or one day per method per dataset) may favor methods with fewer hyperparameters.** Methods with larger search spaces may not converge to good settings within 20 trials, while methods with smaller search spaces may fully explore theirs. This interacts with the test-set tuning issue to create additional unfairness. Reporting actual trial counts per method per dataset would help.

- **Lack of discussion about whether injected OOD samples in the robustness study (RQ3) are representative of real-world contamination.** The paper uses OOD data from the same splits as the main experiment; real contamination might come from different sources. This is a minor limitation worth acknowledging.

### Trivial

None (all formatting/typo issues are parser artifacts).

## Nice-to-Haves

- The paper would benefit from a recommended train/validation/test split protocol for future users of the codebase, with default hyperparameters for each method.
- A statistical significance analysis (e.g., paired Wilcoxon tests) over datasets would substantiate the ranking-based claims.
- Including a validation-set-tuning baseline alongside the test-set-tuned "upper bound" would give two practical reference points.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"No discussion of how the benchmark should be used by future researchers"* — Scope creep. The paper provides a unified codebase, explicit dataset splits, and outlines future directions. What constitutes "how to use" is subjective and the paper's deliverable (code + splits) is standard.
- *"Does not report how many hyperparameter trials were run per method per dataset"* — The paper already reports "20 times or for a maximum of one day per method per dataset" (line 118). The granularity the critic requests would be nice but is not absent.
- *"The paper should not be accepted in its current form ... the numbers must be regenerated"* — This conflates severity. The test-set tuning is a major issue requiring correction, but (1) the authors are transparent, (2) the qualitative findings are likely robust, and (3) calling it "fatal" overstates the case relative to the paper's actual contributions.
- *General formatting/style nitpicks and criticisms about missing appendix content* — Parser artifacts; the original submission does not have these issues.

## Novel Insights

The most interesting cross-cutting insight that emerges from the reviews is the tension between the paper's transparent-but-nonstandard methodology and its role as a benchmark. The authors openly state they tuned on the test set to obtain "upper bounds," and this honesty is commendable — but for a benchmark that aims to *set standards* for a field, methodological rigor in the evaluation protocol itself is part of the contribution. A benchmark that reports inflated numbers risks misleading the community even if relative rankings hold. The reviewers collectively highlight that the paper's value proposition (unifying GLAD and GLOD) is strong, but the execution of the evaluation protocol undermines the very trust a benchmark needs. This is a case where the contribution is real, the findings are probably directionally correct, but the paper needs to raise its own methodological bar to match the standards it implicitly asks the community to adopt.

## Suggestions

- **Rerun all effectiveness experiments (RQ1) using a proper validation split** drawn from the training (ID) set (e.g., 80/20 holdout) for hyperparameter selection, keeping the test set untouched until final evaluation. Report both default and validation-tuned results.
- **Clarify the hyperparameter selection protocol for RQ2 and RQ3** — state explicitly whether the same tuned hyperparameters from RQ1 were carried over, or whether hyperparameters were re-selected for each setting. Ideally, use the same validation-based protocol throughout for consistency.
- **Add statistical significance tests** (e.g., pairwise Wilcoxon signed-rank tests or critical difference diagrams) to support ranking-based claims and observations.
- **Report the actual number of successful hyperparameter trials** per method per dataset (some methods may not complete 20 trials within the one-day budget), so readers can assess fairness of the search budget.
- **Use the same hyperparameter selection strategy across all RQs** — or, at minimum, include a supplementary comparison showing how much the rankings change between default and tuned settings so readers can assess the impact.

## Score and Decision

This paper addresses a genuine gap and makes a useful contribution by unifying two previously separate evaluation tracks. The benchmark design (four scenarios, 35 datasets, 16 methods) is comprehensive, and the multi-dimensional analysis provides qualitatively valuable insights. However, the decision to tune hyperparameters on the test set is a significant methodological flaw for a benchmark paper — it inflates all reported numbers and undermines trust in the quantitative results. This is fixable by re-running with a proper validation split, but the paper cannot be accepted with the current numbers. The paper's core qualitative findings (near-OOD difficulty, contamination vulnerability, no universal method) are likely robust and valuable, but the benchmark's primary deliverable is reliable comparisons, and that standard is not currently met.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>