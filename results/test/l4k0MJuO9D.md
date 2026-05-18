Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper addresses post-hoc calibration for unsupervised domain adaptation (UDA). The key insight is that existing importance-weighting methods for UDA calibration are ineffective because source accuracy remains roughly uniform across target-similarity percentiles (Figure 4), and source accuracy is systematically higher than target accuracy even after adaptation (Figure 2). The authors propose UTDC: estimate the adapted model's accuracy on the unlabeled target domain using a prior method (Deng & Zheng, 2021), then rescale per-bin source accuracy by the estimated target-to-source accuracy ratio, and minimize the resulting UDA-adaECE on target data to find calibration parameters. Experiments on Office-home and Office-31 across three UDA backbones show large and consistent reductions in adaECE compared to IW-based baselines (CPCS, TransCal), often approaching oracle-level calibration.

## Strengths

1. **Well-motivated diagnosis of IW calibration failure**: Figure 4 cleanly demonstrates that source accuracy is approximately uniform across target-similarity percentiles, directly contradicting the core premise of importance-weighting calibration methods. This explains why CPCS and TransCal fail to improve over source-only calibration and provides a clear rationale for the proposed approach.

2. **Large and consistent empirical gains**: Across all 18 Office-home tasks × 3 UDA backbones (DANN, DANN+E, CDAN+E), UTDC-TS reduces adaECE by wide margins compared to CPCS and TransCal. For example, on A→C with CDAN+E, UTDC achieves 2.2% adaECE versus TransCal's 11.8% and CPCS's 9.2%, closely matching the target-label oracle (1.8%). The same pattern holds on Office-31 (Table 3) and across multiple calibration metrics — ECE, NLL, Brier Score (Table 4).

3. **Robustness to accuracy estimation error**: Figure 3 shows that UTDC's adaECE remains low over a wide range of the correction ratio R, and the optimum is near both the true and estimated ratio. This demonstrates the method is not brittle to inaccuracies in the target-accuracy estimator, which partially mitigates concerns about relying on an external estimator.

4. **Clean, principled formulation**: The core idea — estimate target accuracy, rescale bin-wise source accuracy by the ratio, and minimize UDA-adaECE directly on target data — is simple, well-motivated, and applicable to any calibration method whose parameters can be found by minimizing adaECE.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient validation of the constant accuracy-ratio assumption across bins**: The method rescales all source-bin accuracies by the single global ratio R = A_target / A_source (Eq. 4). This assumes the accuracy ratio between source and target is approximately uniform across confidence quantile bins. The paper provides one validation (Figure 5, Office-home C→P) but does not show this holds across the diverse domain pairs and UDA methods tested. If this assumption systematically fails for some domain shifts, the estimated bin-wise accuracies would be biased. The sensitivity analysis (Figure 3) varies a global R but does not test per-bin ratio violations. Since this is a structural assumption baked into the method's core, the paper should demonstrate its validity across multiple representative domain pairs (e.g., by plotting per-bin accuracy ratios for several tasks from the evaluation suite, such as A→C, R→P, W→D where domain gaps differ substantially).

2. **Limited direct evaluation of the target accuracy estimator**: The entire pipeline depends on the accuracy estimate from (Deng & Zheng, 2021), yet the paper evaluates it only in aggregate (Figure 2 shows averages across tasks for three UDA methods, not per-task performance). Without seeing per-task estimated vs. true accuracy (e.g., a scatter plot with correlation across all 18 Office-home tasks), it is difficult to assess whether the estimator's errors are within the tolerance range shown in Figure 3 (which itself only covers one task, A→C). The sensitivity analysis partially addresses this, but the robustness margin could differ for other tasks where the estimator is less accurate.

### Minor

1. **Missing optimization details for Vector Scaling and Matrix Scaling variants**: The paper describes temperature selection via grid search (TS) but does not explain how the UDA-adaECE objective is minimized for VS (k parameters) and MS (k×k parameters). This omission makes the VS/MS results in Tables 2 and 3 unverifiable. Given that TS is the primary method and VS/MS are secondary, the authors should at minimum describe the optimizer, hyperparameters, and convergence criteria used.

2. **No measure of variability in calibration results**: The main results tables report point estimates without error bars or multiple runs. While UDA model training is often single-run in this literature, the calibration step's sensitivity to the accuracy estimate and binning could be characterized (e.g., bootstrap confidence intervals). Without variance estimates, some improvements could fall within noise for tasks where margins are smaller.

3. **Sensitivity analysis restricted to one task**: Figure 3 covers only Office-home A→C. The finding that the optimum is near both the true and estimated R should be verified for at least a few additional tasks with different domain gap magnitudes (e.g., a close domain pair like R→A and a distant one like C→A).

### Trivial
- Line 149: "shawed" → "showed" (parser artifact may have introduced this, but if present in original it is a typo).

## Nice-to-Haves
- For the constant-ratio assumption, the paper could compare the actual per-bin accuracy ratio across bins for several domain pairs and report the coefficient of variation, rather than just one visual plot.
- The accuracy estimator evaluation could include per-task absolute error in the global ratio R, with a scatter plot of estimated vs. true accuracy across all tasks.
- Could compare UTDC against a variant that uses fixed-interval bins (instead of adaptive/quantile bins) to test robustness to binning choice.

## Removed Points
- **Criticism about missing evaluation on VisDA-2017 / DomainNet**: Scope creep. The paper uses standard UDA benchmarks (Office-home, Office-31) consistent with the baseline literature it compares against. Demanding additional larger-scale datasets does not identify a flaw in the paper's existing evaluation.
- **Claim that the binning procedure is unclear**: The paper explicitly states that source and target data are each divided into M equal-size bins according to their confidence values (lines 67-68), and adaECE's adaptive binning is defined in lines 41-45. This is adequately described.
- **Criticism that the assumption requires comparable confidence levels across bins**: The reviewer characterizes the assumption as requiring bin indices to correspond to comparable confidence intervals. The paper's actual assumption (stated in lines 136-137) is that the *accuracy ratio* is similar across bins — not that confidence levels are comparable. The underlying concern (that different absolute confidence levels could produce different degradation) is legitimate but the reviewer's framing misattributes the paper's reasoning.

## Novel Insights

The diagnosis of IW calibration failure (Figure 4) is the most novel empirical insight in the paper and the reviews: it cleanly shows that source accuracy is near-uniform across target-similarity percentiles, which explains at a fundamental level why weighting source samples by similarity to the target cannot fix the accuracy-mismatch problem. This finding has implications beyond the paper's own method — it suggests that any calibration approach for UDA that relies on re-weighting source data will face fundamental limitations, and that direct estimation of target accuracy (as UTDC does) is a more promising direction.

## Suggestions

1. **Validate the constant bin-wise ratio assumption** across at least 4-6 representative domain pairs spanning close and distant gaps (e.g., R→A, A→C, C→P, A→W). Report the per-bin accuracy ratio and its variance across bins for each.
2. **Provide a per-task scatter plot** of estimated vs. true target accuracy for all task × UDA-method combinations, with correlation coefficient and mean absolute error. This would demonstrate the estimator's reliability in the specific settings tested.
3. **Describe the VS/MS optimization procedure** (optimizer, learning rate, convergence criteria) or, if space is constrained, focus the main paper on TS and relegate VS/MS details to supplemental materials.
4. **Extend the sensitivity analysis** (Figure 3) to at least 2-3 additional tasks with different domain gaps to verify the robustness margin generalizes.

## Score and Decision

The paper proposes a well-motivated, clean solution to an important problem (UDA calibration) and demonstrates large, consistent improvements across standard benchmarks. The two main weaknesses — incomplete validation of the per-bin constant-ratio assumption and thin evaluation of the accuracy estimator — are serious enough that they should be addressed, but neither invalidates the core contribution. The empirical results (e.g., UTDC achieving 2.2% adaECE vs. 11.8% for TransCal on A→C with CDAN+E) are too large and consistent to be explained away by these gaps alone. The paper would benefit from the suggested additional validation but is already a solid contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>