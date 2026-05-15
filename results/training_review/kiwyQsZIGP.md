Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me synthesize the final review.

---

## Summary

This paper provides the first systematic investigation of task-level evaluation (TLE) and task-level model selection (TLMS) in few-shot learning. It evaluates four standard performance estimators (hold-out, cross-validation, leave-one-out CV, bootstrapping) across three datasets and five FSL algorithms, measuring their accuracy for per-episode performance estimation and their ranking quality for model selection. The key finding is that all existing estimators are unreliable for per-episode evaluation (≥50% chance of error >10% absolute), though 5-fold CV is the least bad option for estimation while resampling methods are better suited for model selection.

## Strengths

- **First systematic investigation of task-level evaluation in FSL.** The paper formally defines TLE and TLMS protocols, clearly distinguishing them from the standard aggregated evaluation (AE). This problem formulation is genuinely novel and addresses a neglected gap in the FSL literature. The paper is explicit that prior benchmarks focus on average-case algorithm comparison (Section 3, lines 36–38), while TLE addresses the fundamentally different question of per-episode validation needed for deployment.

- **Identifies a previously unrecognized failure mode of leave-one-out cross-validation in the few-shot regime.** The paper hypothesizes that LOO-CV's poor performance stems from induced class imbalance (one class has fewer training examples than others when a single sample is held out) and provides supporting evidence by varying the number of ways while keeping total support set size fixed (Figure 7 right, lines 220–222). This insight goes beyond the standard bias-variance trade-off reasoning and is concrete and testable.

- **Provides actionable, evidence-based recommendations for estimator choice.** Through extensive experiments across three benchmarks and five FSL algorithms, the paper concludes that 5-fold CV yields the lowest MAE for direct performance estimation (Table 2), while resampling methods (LOO-CV, bootstrapping) are better suited for model selection due to higher rank correlation with the oracle (Figure 5). These recommendations are concrete and backed by multiple tables and figures.

- **Rigorous multi-benchmark and multi-algorithm evaluation.** The experiments cover CIFAR-FS, miniImageNet, and Meta-Album (a cross-domain dataset), with five diverse FSL methods (Baseline, Baseline++, ProtoNet, MAML, R2D2). This breadth ensures findings are not specific to a single setting.

- **Demonstrates practical impact through hyperparameter tuning experiments (BaselineCV).** Showing that per-episode tuning of the ridge regularization parameter with 5-fold CV can improve aggregated accuracy over a fixed-hyperparameter baseline on 2 out of 3 datasets (Table 3) provides a concrete illustration that even imperfect estimators can yield gains at the task level.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the evidence presented. No single issue invalidates the conclusions.

### Minor

- **Missing baseline for the algorithm-selection experiment (Table 4).** The paper reports aggregated accuracy when using each estimator to select among FSL algorithms on a per-episode basis, but does not include a simple baseline: *always select the algorithm with the highest average oracle accuracy on the meta-validation set*. Adding this would clarify whether per-episode selection actually beats a fixed rule. The data is available in Table 1 (e.g., best single algorithm for CIFAR-FS: R2D2 at 72.06; best per-episode selection in Table 4: 73.44 with bootstrapping). On miniImageNet, the best single algorithm (ProtoNet at 66.12) actually outperforms all per-episode selection methods (best: LOO-CV at 64.34), which the paper does not discuss. Including this baseline would strengthen the paper's nuanced conclusion about model selection.

- **Oracle treated as ground truth without quantifying its own variance.** The oracle accuracy is computed from a finite query set (albeit much larger than the support set) and has sampling variance. The MAE and Spearman correlations treat the oracle as deterministic. While this is unlikely to change the qualitative findings (the query set is substantially larger than the support set), it overstates the measured error to some degree. The paper should at minimum discuss this limitation (lines 176–178 describe the oracle but do not address its variance).

- **MAML + LOO-CV collapse unexplained.** The extreme accuracy values for MAML with LOO-CV (16.79 on CIFAR-FS, 17.39 on miniImageNet, 15.24 on Meta-Album in Table 1) represent a dramatic failure that the paper does not investigate or explain. This is qualitatively different from the general pattern of underestimation and deserves at least a brief discussion (e.g., does MAML's inner-loop optimization collapse with imbalanced folds?).

- **BaselineCV drops on Meta-Album without discussion.** The paper states that "using 5-fold CV can provide a noticeable improvement over the aggregated accuracy of the standard Baseline" (line 227), but BaselineCV actually drops relative to Baseline on Meta-Album (59.36 → 58.46 in Table 3). This negative result weakens the claim that task-level tuning universally helps and should be acknowledged.

- **Class-imbalance experiment confounds number of ways with per-class sample size.** The experiment in lines 222–223 varies the number of ways while keeping total support set size fixed. This means reducing ways increases samples per class, which affects both class imbalance and model training quality. The paper frames this as a test of imbalance, but the two factors are confounded. A cleaner experiment would hold ways fixed and imbalance separately (e.g., by dropping samples from one class). The current evidence shows correlation but not causation.

### Trivial

- The MAE reported in Table 2 does not include confidence intervals, unlike the accuracy estimates in Table 1 (which report 95% CIs). Adding intervals would help readers assess the precision of the MAE estimates.

- The Spearman correlation results in Figure 5 report means without standard errors or confidence intervals. While the large number of episodes (10k+) means even small differences may be significant, reporting variance would aid interpretation.

- The reproducibility statement "We use the meta-training hyperparameters suggested in the documentation of this implementation" (line 173) is vague — no URL or reference to the codebase is provided.

## Nice-to-Haves

- A case study of individual "good" and "bad" episodes for the best estimator (5-fold CV) could help readers build intuition about when estimates fail (e.g., class separability, support set composition).

- Testing with additional fold values beyond the ones shown (e.g., k=3, 7, 15) would strengthen the claim that the optimal trade-off is around 5 folds.

- A concrete sketch of a Bayesian estimator that leverages meta-training data (mentioned as a future direction in line 275) would make the recommendations more actionable.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Overclaimed conclusions about benchmarks."** Removed because it misreads the paper. The paper explicitly distinguishes AE from TLE (Section 3, lines 44–48: "While such an experimental setup is sensible when assessing the 'average-case' performance...") and its claim is specifically that benchmarks are *not designed for task-level evaluation*, not that they fail at aggregated algorithm comparison. The abstract states "not designed in such a way that one can get a reliable picture of how effectively methods can be used on individual tasks," which is directly supported by the experiments showing estimator failure for TLE.

2. **"Figure 7 (left) lacks an x‑axis label."** Removed as a pure formatting/style nitpick. The figure caption says "MAE between k-fold CV estimates and the oracle estimates, as a function of k" which provides the necessary information. Without access to the rendered figure, this cannot be verified as a meaningful content issue.

3. **"The choice of k values tested should be stated explicitly."** The text says "we plot the error as a function of folds" and the figure key indicates the values. This is adequately described.

## Novel Insights

The reviews surface a productive tension that the paper itself does not fully exploit: the finding that per-episode model selection *underperforms* the best single algorithm on miniImageNet (64.34 vs. 66.12), even as the same approach *outperforms* it on CIFAR-FS (73.44 vs. 72.06). This suggests that the utility of per-episode selection depends on the diversity of relative algorithm strengths across episodes — a dataset where different algorithms dominate different episodes will benefit more from selection. The paper's class-imbalance analysis hints at one mechanism driving such diversity, but a broader investigation into the *episode-level variance of algorithm rankings* would be a natural next step. This could lead to a principled criterion for when per-episode selection is worth the computational overhead.

## Suggestions

1. Add the "best single algorithm" baseline to Table 4 (algorithm selection) and explicitly discuss when per-episode selection helps versus hurts.
2. Acknowledge the oracle's finite-sample variance as a limitation in the MAE analysis.
3. Add a brief discussion of the MAML+LOO-CV collapse — even a speculative explanation would help readers.
4. Acknowledge the Meta-Album negative result for BaselineCV and discuss possible reasons (e.g., domain shift, insufficient search range).
5. Disentangle the class-imbalance experiment by holding ways fixed and varying per-class sample counts independently, or at minimum flag the confound as a limitation.
6. Add error bars or confidence intervals to the MAE table and Spearman correlation figure to aid interpretation.

## Score and Decision

The paper tackles an important and genuinely neglected problem in FSL, provides a clear problem formulation, and backs its claims with extensive experiments across diverse settings. The weaknesses are all minor/nice-to-have — no issues threaten the paper's core conclusions. The missing baseline for algorithm selection and the unacknowledged negative result on Meta-Album are the most substantive concerns, but they are easily addressed and do not undermine the paper's overall contribution.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>