## Summary

This paper proposes a robust evaluation framework for heterogeneous treatment effect (HTE) estimators based on relative error. The key contribution is relaxing the consistency requirement for outcome regression models that limits prior work (Gao, 2025): the proposed estimator achieves $\sqrt{n}$-consistency and asymptotic normality with only a correctly specified propensity score (converging faster than $n^{-1/4}$), even if outcome models are misspecified. The authors derive moment conditions from a Taylor expansion, design a weighted least squares loss and balance regularizers that enforce these conditions, and embed them in a Dragonnet-style neural architecture. They also extend the framework to construct an enhanced HTE estimator by aggregating over pairs of candidate estimators. Experiments on IHDP and Twins show good coverage (94-96% for 90% CIs), high selection accuracy (80-94%), and strong HTE estimation performance.

## Strengths

- **Novel and well-motivated theoretical advance**: The paper identifies a genuine limitation of Gao (2025) — that Condition 2 requires consistency of outcome models — and provides a principled solution. The Taylor expansion analysis in Section 4.1 leading to the moment conditions in Eq. (4) is technically sound, and Theorem 1 formally shows that the proposed estimator remains $\sqrt{n}$-consistent and asymptotically normal when outcome models are misspecified, requiring only a correctly specified propensity score.

- **Loss functions directly derived from theory**: The weighted least squares loss $\mathcal{L}_{\text{wls}}$ and the balance regularizer $\mathcal{L}_{\text{const}}$ are derived from the first-order conditions in Eq. (4), which is a clean connection between theory and implementation. The ablation study (Table 5) empirically validates the importance of these components: the full loss achieves 80% selection accuracy on IHDP vs. 14% without $\mathcal{L}_{\text{const}}$, a dramatic difference.

- **Strong empirical performance on relative error evaluation**: The method achieves 96% coverage (vs. nominal 90%) and 80% selection accuracy on IHDP, and 94% coverage and 94% selection accuracy on Twins (Table 2, Figures 1-2). Compared to conventional nuisance estimators (linear regression, boosting) which achieve nominal coverage but much lower selection accuracy (as low as 44% on IHDP), the proposed method produces substantially tighter, practically useful confidence intervals.

- **Sensible engineering choices**: The soft-margin relaxation for the over-constrained propensity score optimization (using slack variables) is a well-motivated design, and the sensitivity analysis (Table 4) shows robustness to the hyperparameter $\lambda_2$ over a reasonable range.

## Weaknesses

### Fatal
None.

### Major

1. **Unclear data flow for the enhanced HTE estimator (Table 1)**: The paper does not specify which candidate estimators $\hat{\tau}_1, \dots, \hat{\tau}_K$ are used in the aggregation (Section 5) to produce the "Ours" results in Table 1, nor does it clarify which data split trains the neural network that produces $\hat{\mu}_0, \hat{\mu}_1$ for the enhanced estimator. Section 6.1 only states "We randomly split each dataset into training and test sets in a 2:1 ratio," without explaining how this split applies to the neural network training for the enhanced estimator versus the baselines. The reviewer's claim of "almost certainly" data leakage is speculative — there is no affirmative evidence the network is trained on the test set — but the omission makes Table 1 difficult to interpret. The paper must clarify: (a) what exact set of candidate estimators is used, (b) what data the neural network for the enhanced estimator is trained on, and (c) whether this is the same split used to train the baselines.

2. **Incomplete controlled comparison against Gao (2025)**: Table 2 compares the proposed method against two simple nuisance estimators (linear regression and gradient boosting). While the ablation study (Table 5) compares against a variant using $\mathcal{L}_{\text{wls}} \& \mathcal{L}_{\text{ce}}$ (without $\mathcal{L}_{\text{const}}$), this still uses the proposed weighted least squares loss $\mathcal{L}_{\text{wls}}$ rather than standard unweighted MSE. A cleaner baseline would be: the same neural architecture trained with *unweighted* MSE for outcomes + standard cross-entropy for propensity (i.e., replacing $\mathcal{L}_{\text{wls}}$ with $\mathcal{L}_{\text{MSE}}$ and removing $\mathcal{L}_{\text{const}}$). Without this control, the claimed improvement in selection accuracy (Table 2's 80% vs. 44-48%) is potentially confounded with the choice of neural network architecture rather than the novel losses.

3. **Lack of justification for no sample splitting**: The paper claims (Section 4.4) that sample splitting is not needed, unlike Gao (2025). However, the Theorem 1 conditions require $\hat{\gamma}, \hat{\beta}_0, \hat{\beta}_1$ to converge faster than $n^{-1/4}$. Standard DML results (Chernozhukov et al., 2018) show that without sample splitting (cross-fitting), even $\sqrt{n}$-consistent nuisance estimators can produce non-vanishing bias when flexible ML is used. The paper does not provide a theoretical argument or simulation evidence showing that the proposed framework avoids this issue. The claim "a variety of flexible machine learning methods can achieve the required convergence rates" cites DML references that *do* require sample splitting, creating a tension that is not resolved.

### Minor

1. **Unspecified candidate estimator set**: As noted above, the paper never lists which estimators form the candidate set $\mathcal{K}$ for the enhanced HTE estimator in Table 1. If the set includes the baselines being compared against (e.g., TARNet, Dragonnet, DCFR), this should be stated. If it includes only a subset, that should also be clarified. This is a straightforward clarity fix.

2. **Condition 2 characterization is slightly imprecise**: The paper states (Section 3) that Condition 2 "requires all nuisance parameter estimators to be consistent." Formally, Condition 2 is $\mathbb{E}[|\tilde{\mu}_a - \mu_a||\tilde{e} - e|] = o_p(n^{-1/2})$, and if one component is inconsistent (converges to a wrong constant), the condition could still be satisfied if the other component converges faster than $n^{-1/2}$. This is a technical nuance that doesn't undermine the paper's practical motivation — outcome models are indeed harder to get right than propensity scores — but the statement is technically imprecise.

3. **Ablation study's "Gao (2025)" label**: The paper labels the $\mathcal{L}_{\text{wls}} \& \mathcal{L}_{\text{ce}}$ ablation row as "a method of Gao (2025)" and states the network "degenerates to TARNet." However, this variant still uses the proposed weighted loss $\mathcal{L}_{\text{wls}}$ rather than standard MSE, so it doesn't correspond to an exact implementation described in Gao (2025). The paper should more carefully describe what this baseline represents.

### Trivial
None.

## Nice-to-Haves

- **Cross-fitting variant**: Even if the theory claims sample splitting is unnecessary, a cross-fitting variant would substantially increase confidence in the results, especially for practitioners familiar with DML.
- **Coverage calibration curve**: Showing coverage vs. nominal level across a range (e.g., 80%, 85%, 90%, 95%) for the proposed method vs. Gao-style baselines would strengthen the evidence.
- **Synthetic experiment with known misspecification**: A simulation where the outcome model is deliberately misspecified (e.g., linear working model with nonlinear true outcome) and the propensity score is correctly specified would directly test the claimed robustness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Data leakage claim (from Harsh Critic Issue 1)**: The claim that the enhanced HTE estimator "sees the test outcomes during training" is an assumption not stated in the paper. The paper is ambiguous about data usage, but there is no affirmative evidence of test-data leakage. This is a clarity issue, not evidence of a methodological flaw. Moved here because it's a speculation, not a verified problem.
  
- **"Condition 2 imprecision" (Harsh Critic's Section-by-Section Note 1)**: The reviewer claims Condition 2 "can be satisfied even if one of the two components is inconsistent." This is technically wrong for the standard interpretation — if a nuisance estimator is truly inconsistent (converging to a wrong limit), the deviation doesn't vanish, so the product can't be $o_p(n^{-1/2})$ unless the other converges at a super-fast rate that isn't achievable in practice. The paper's characterization is substantially correct. Moved here because the criticism is factually incorrect.

- **Taylor expansion variance concern (Harsh Critic's Section-by-Section Note 2)**: The concern about $1/\tilde{e}(x)$ causing variance inflation is addressed by the standard positivity assumption (Assumption 1). This is a known concern in all IPW-based methods and not specific to this paper. Moved here because it's generic and not a real weakness.

- **"Missing related works"**: Removed per instructions.

- **"Formatting/style nitpicks"**: Removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the enhanced HTE estimator's data flow**: Explicitly state (a) which candidate estimators form $\mathcal{K}$, (b) which data split trains the neural network for the enhanced estimator, and (c) whether this is consistent with how baselines are trained. A simple diagram or algorithm box in the main text would suffice.

2. **Add a controlled neural baseline for Gao (2025)**: Include a baseline where the same neural network from Section 4.3 is trained with standard unweighted MSE for outcomes + standard cross-entropy for propensity (no $\mathcal{L}_{\text{wls}}$, no $\mathcal{L}_{\text{const}}$). This would cleanly isolate the effect of the proposed losses versus the neural architecture.

3. **Address the sample splitting concern**: Either (a) provide a rigorous theoretical argument for why cross-fitting is unnecessary despite the DML literature's standard practice, or (b) run a version of the experiments with cross-fitting and show the results are essentially unchanged.

4. **Add a synthetic data experiment with known ground truth**: Generate data where the outcome model is deliberately misspecified (e.g., true outcome is nonlinear but working model is linear) and the propensity score is correctly specified. Compare bias, variance, and coverage of the proposed method against Gao-style baselines.

5. **Tone down the "degenerates to TARNet" claim**: The ablation baseline $\mathcal{L}_{\text{wls}} \& \mathcal{L}_{\text{ce}}$ still uses the proposed weighted loss, so it shouldn't be presented as equivalent to TARNet or as a direct implementation of Gao (2025).

## Score and Decision

**Anchors used for calibration:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/Ml8t8kQMUP.md` | 7.00 | Stronger paper: cleaner experiments, well-validated real-world case study, despite less theory. The current paper has more formal theory but less clean evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/0Xi3WDwd5w.md` | 7.00 | Stronger paper: Neyman-orthogonality theory is more fully developed, with comprehensive experiments and clear baselines. The current paper has a similar theory/experiment balance but weaker baseline comparisons. |
| `/home/wg25r/review_agent/human_reviews_2026/rxZdaKhu2I.md` | 6.00 | Comparable: clear theory with limited experiments but tight presentation. Current paper has more experiments but clarity issues. |
| `/home/wg25r/review_agent/human_reviews_2026/lGaZimFbss.md` | 5.00 | Comparable accepted poster: solid contribution with thorough experiments. Current paper has similar quality but some unresolved clarity issues. |
| `/home/wg25r/review_agent/human_reviews_2026/tB6fyc3sj8.md` | 3.50 | Weaker paper: unclear presentation, no baselines, no ablation. Current paper is substantially stronger across all dimensions. |
| `/home/wg25r/review_agent/human_reviews_2026/y1N4v2v5Xz.md` | 2.50 | Much weaker: fundamental issues with methodology framing. Not comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/hB6BzSgZwb.md` | 4.00 | Weaker: rejected paper with unclear contribution. Current paper has clearer contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/1qhNFRxORK.md` | 3.50 | Weaker: rejected paper with fundamental issues. Not comparable. |

The paper presents a genuine theoretical advance (relaxing outcome model consistency requirements) with a clean neural implementation. The experimental results are impressive, but the evaluation of the enhanced HTE estimator (Table 1) suffers from insufficient clarity about the data flow, and the comparison against Gao (2025) lacks a properly controlled baseline using the same architecture. These are addressable issues that don't invalidate the core contribution. The paper is comparable to or stronger than the accepted papers in the 5-6 range but falls short of the 7+ papers in experimental rigor.

**Score:** 5.0

**Decision:** Accept (Poster)

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>