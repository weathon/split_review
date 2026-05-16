Now I have a thorough understanding of the paper and can cross-check all reviewer claims against the actual text. Let me write the consolidated review.

## Summary

This paper introduces three methods that extend conformal prediction to produce prediction sets that minimize a user-specified downstream decision loss while maintaining standard coverage guarantees. The contributions are: (1) a penalized conformal predictor that augments the APS non-conformity score with a loss penalty weighted by a tuned hyperparameter, (2) a hyperparameter-free separable penalized ratio method (Neyman-Pearson-inspired plug-in thresholding plus conformalization), and (3) for non-separable losses, a greedy optimization-based meta-algorithm that linearizes the loss through marginal gains and conformalizes the resulting sets. The methods are validated on four datasets including a real-world dermatology case study, showing substantial reductions in decision loss over standard conformal prediction.

## Strengths

- **Novel problem formulation bridging decision-focused learning and conformal prediction**: The paper identifies a clear gap — standard conformal prediction provides coverage guarantees but ignores downstream utility, while decision-focused learning ignores uncertainty quantification. The paper defines a new objective (minimizing expected decision loss subject to coverage) and provides concrete algorithms to achieve it. This is well-motivated with practical examples (dermatology diagnosis).

- **Provable coverage guarantees for separable and non-separable losses**: Propositions 1–3 establish finite-sample marginal coverage guarantees matching standard conformal bounds. Proposition 2 shows 1−α ≤ P(Y∈S) ≤ 1−α+1/(n+1) for the separable penalized ratio; Proposition 3 extends this to the greedy-based non-separable method. The guarantees hold regardless of the quality of the base classifier.

- **Principled handling of non-separable decision losses**: The linearization of non-separable losses through marginal gains, followed by greedy optimization and conformalization, is a genuine innovation. This extends conformal prediction beyond the monotone-loss regime where conformal risk control applies, enabling losses such as hierarchy-coherence (coverage loss, maximum distance) that depend on set composition.

- **Substantial and consistent empirical improvements**: Across four datasets (CIFAR-100, iNaturalist, ImageNet, Fitzpatrick), all proposed methods achieve lower decision loss than standard conformal prediction. Reductions of 60–75% are reported. The improvements hold for both separable and non-separable losses and across datasets of varying size and difficulty.

- **Robustness to noisy base classifiers**: The ablation study on Fitzpatrick (Figure 4) demonstrates that the methods outperform standard conformal prediction even when the base classifier has low accuracy (0.2–0.4), showing practical value in settings where only imperfect models are available.

- **Modular, post-hoc, and model-agnostic**: The methods operate as a post-processing step on any classifier's predictions without retraining, preserving the modularity that makes conformal prediction attractive for deployment.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Experimental results lack measures of variability**: All figures report only median-of-means across 10 runs with no error bars, confidence intervals, or standard deviations (Figures 3, 4). With only 10 trials, random variation could affect the observed magnitudes. While the consistent direction of improvement across all datasets is reassuring, the absence of uncertainty quantification makes it impossible to assess the statistical significance of the claimed 60–75% reductions.

- **Greedy optimizer lacks analysis of approximation quality and computational cost**: For non-separable losses, the greedy algorithm (Eq. 3) is presented as a plausible heuristic, but the paper provides no analysis of its suboptimality gap, no discussion of conditions under which greedy is near-optimal (e.g., submodularity of the loss), and no empirical runtime measurements. For large label spaces (e.g., ImageNet with 1000 classes), evaluating the greedy criterion per test instance could be expensive, and the paper's claim that it is "lightweight" (Section 1) is unsupported. The connection between the greedy criterion (Eq. 3) and the loss being optimized is not formally justified.

- **No dedicated limitations discussion**: The paper lacks a limitations section. Important caveats are acknowledged only in passing or not at all: (a) the separable ratio method assumes the classifier's probability estimates are reasonable, (b) the greedy optimizer may be expensive for large label sets, (c) coverage guarantees are marginal and may not be informative for individual instances, (d) the penalized conformal method adds a hyperparameter that may be difficult to tune with limited data (though the paper notes this implicitly in Section 4.2).

- **Baseline comparison could be more explicit**: The paper repeatedly refers to "base conformal method" and "baseline conformal prediction sets" without explicitly naming the baseline. The context makes clear it is APS (Adaptive Prediction Sets, Romano et al. 2020) using score ρ(x,y), since all proposed scores build on ρ. However, explicitly stating "our baseline is APS with score ρ(x,y)" would improve clarity and reproducibility.

- **Synthetic hierarchies for CIFAR-100 and ImageNet may not capture meaningful decision structure**: The paper generates hierarchies via clustering of classifier representations (Section 4.1), which may not correspond to any real-world decision-relevant taxonomy. Only iNaturalist and Fitzpatrick use expert-defined hierarchies. While the paper is transparent about this, the empirical demonstration on synthetic hierarchies is weaker evidence that the methods would transfer to authentic domain-specific utility functions.

- **Random penalty assignment for separable loss not motivated**: The separable loss experiment uses penalties randomly sampled from {i/4 : i∈[4]} (Section 4.1). No rationale is given for this choice or why it represents a realistic cost structure. A more informative experiment would use costs reflecting actual decision-relevant differences (e.g., test costs, treatment costs, label acquisition costs).

### Trivial

- **Grid search parameters for the hyperparameter λ not reported**: The paper states λ is chosen via grid search (Section 3.1) but does not specify the grid size, range, or number of values tried. This makes the tuning burden opaque.

## Nice-to-Haves

- **Quantitative comparison to conformal risk control (CRC)**: The paper discusses CRC in related work (Section 3, approx. 3 sentences) and correctly notes that CRC controls expected loss for monotone-decreasing losses without guaranteeing coverage. However, a quantitative comparison on at least one loss where CRC is applicable (e.g., set size) would help position the contributions relative to the closest prior work and demonstrate the practical advantage of methods that guarantee coverage while minimizing loss.

- **More detailed distinction between this work and CRC**: The distinction — CRC controls expected loss at a preset level without coverage guarantees, while the proposed methods guarantee coverage and minimize loss — is critical and deserves more emphasis and formal comparison.

- **Runtime analysis of the greedy optimizer**: Reporting per-instance runtime for the greedy method (especially on ImageNet with 1000 classes) would help practitioners assess the computational trade-offs.

## Removed Points

These points are flagged per the instructions as invalid, misinformed, or out of scope. Treat them with caution.

- **Criticism about missing Tables** (\\ref{table: separable_vs_vanilla}, etc.): The reviewer noted these tables are missing from the extracted text. The parser strips tabular content; these tables exist in the original submission. Not a paper flaw.

- **Criticism that Proposition 1 "does not discuss how the bound degrades with the grid size"**: The bound in Proposition 1 explicitly contains the term log(2|H|/δ), which depends on |H| (the grid size). The reviewer missed this — the bound does capture grid size dependence.

- **Criticism about "no comparison to existing decision-aware methods" implying this is an evidential gap**: The paper discusses conformal risk control in the related work section and correctly identifies the different regime (monotone-decreasing losses only). The proposed methods explicitly handle losses that are not monotone, which CRC cannot. This is a scope difference, not a missing comparison.

- **Criticism that "the three tables that are supposed to contain numerical comparisons are missing from the extracted text entirely"**: Same as first point — parser artifact.

- **"The paper should state that CRC controls expected loss without guaranteeing coverage"**: The paper already states: "it does not directly optimize the expected value of the chosen function, and depending on such function, controlling for the expected value of the chosen loss can be at expense of statistical coverage." This adequately distinguishes the approaches.

- **Criticism about "synthetic hierarchies" being "questionable" and claiming results "may not transfer"**: The paper is transparent that CIFAR-100 and ImageNet use synthetic hierarchies. The results on these datasets still demonstrate that the algorithms work as intended. The primary validation datasets with expert hierarchies (iNaturalist, Fitzpatrick) show the same patterns. This is a scope consideration, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful suggestions for strengthening the empirical presentation but do not identify a structural gap or a different interpretation of the results that would change the paper's narrative.

## Suggestions

1. Add error bars (bootstrap CIs or standard deviations) to all quantitative figures and report the full result tables with variability measures.
2. Add a brief discussion of the greedy algorithm's approximation properties — even a note that losses satisfying submodularity would have known guarantees, and that in general the method is a heuristic.
3. Include a dedicated limitations paragraph in the conclusion.
4. Explicitly name the baseline (APS with score ρ(x,y)) and its parameters in the experiment setup.
5. Report the grid size and range used for λ tuning.
6. Add a comparison to conformal risk control on at least one monotone loss where CRC is applicable, to empirically demonstrate the trade-off.
7. Report empirical runtime of the greedy optimizer per instance, especially on ImageNet.

## Score and Decision

The paper makes a clear, well-motivated contribution to an important problem. The methods are novel, theoretically grounded (coverage guarantees are proven), and empirically validated across diverse settings including a real-world medical use case. Weaknesses are primarily in presentation quality — missing variability measures, incomplete reporting of implementation details, and lack of analysis of the greedy heuristic — rather than structural flaws. These are addressable and do not undermine the core contributions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>