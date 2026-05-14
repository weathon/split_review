Now I have all the information I need. Let me synthesize the final review.

## Summary
This paper proposes ZNet, a deep learning method that learns instrumental variable (IV) representations from observational data by decomposing observed covariates X into confounder (C) and instrument (Z) components. The method enforces the three standard IV assumptions—relevance, exclusion restriction, and unconfoundedness—through differentiable loss constraints (Pearson correlation and mutual information). ZNet outputs representations {C, Z} that can be plugged into any downstream two-stage IV estimator (TSLS, DeepIV, DFIV). The paper evaluates ZNet on eight semi-synthetic datasets with comprehensive comparisons against three variational IV-generation baselines (AutoIV, VIV, GIV).

## Strengths

- **Principled encoding of IV assumptions into a differentiable architecture**: ZNet is the first method to explicitly encode all three IV conditions—relevance, exclusion restriction, and unconfoundedness—directly into loss terms that can be optimized via gradient descent. The architecture cleanly mirrors the underlying structural causal model, and Lemma 1 provides a clever theoretical justification for the unconfoundedness constraint that handles cases where observed variables may be influenced by unobserved confounders (Section 5.1, Constraints 1–3).

- **Comprehensive empirical evaluation against strong baselines**: The paper tests ZNet with three downstream IV estimators (TSLS, DeepIV, DFIV) across eight semi-synthetic datasets spanning linear/nonlinear, disjoint/mixed/latent/no-candidate, and with/without unobserved confounding settings. The benchmarking covers AutoIV, VIV, GIV, TrueIV, and TARNet—making this arguably the most thorough evaluation of automatic IV generation to date (Table 1, Appendix Tables 3–4, 9–10).

- **Ablation studies validate the multi-loss design**: Systematic removal of each constraint (unconfoundedness, exclusion restriction, relevance) degrades instrument recovery, and ablating all constraints reduces correlation with true instruments to near zero (Figure 5c). This provides clear evidence that the composite loss is well-justified and each component contributes meaningfully.

- **Empirical recovery of both observed and latent instruments**: ZNet demonstrably recovers ground-truth instruments when they exist (high multivariate correlation with true instrument variables in Figure 5a,b) and reconstructs latent categorical instruments (Figure 4). These results validate that the method can discover known instrument structures from data.

## Weaknesses

### Major

- **No formal guarantee that learned Z satisfies IV conditions**: The paper claims that "solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument," but provides no identification proof. The constraints enforce pairwise *correlation* (e.g., Cov(Z,C)=0, Cov(Z,e_Y)=0), but the exclusion restriction and unconfoundedness require *conditional independence* (Z ⟂ Y | C,T and Z ⟂ e_Y | C). Zero covariance is necessary but not sufficient for independence, and the gap is not addressed. The paper acknowledges this limitation obliquely ("IV estimation in general is limited by a lack of theoretical guarantees") but the central claim of the method—that it *guarantees* IV validity—is not supported by theory. As the paper's core contribution rests on this claim, this is a significant gap.

- **Evaluation is entirely on semi-synthetic data that matches the method's assumptions**: Every experiment uses data generated to explicitly match the assumed SCM (Eq. 10–11) with clean separation of X→T, X→Y, X←U. This means the evaluation tests whether ZNet can recover a decomposition that was intentionally baked into the data. The paper's headline claim—that ZNet works "regardless of whether the assumption of unconfoundedness is satisfied" in "general observational settings"—is not supported by evidence from data that perfectly matches the method's structural assumptions. No real-world dataset with a known valid instrument (e.g., Mendelian randomization, distance-to-college) is tested, and no experiment examines robustness to SCM misspecification (e.g., where the true instrument is not a function of X, or where additive errors are violated).

- **Correlation-based constraints are a weak proxy for causal assumptions**: The entire loss framework uses Pearson correlation (and optionally MI) to enforce causal constraints, but the IV assumptions are fundamentally about causal independence, not associational uncorrelatedness. For exclusion restriction, the paper ensures Cov(Z,C)=0 but does not ensure that Z is conditionally independent of Y given C and T—the actual requirement. A Z that is uncorrelated with C could still have a direct causal path to Y, which would bias downstream IV estimates. The paper does not conduct any overidentification test (e.g., Sargan test) or placebo test to check whether learned Z behaves like a valid instrument.

### Minor

- **No confidence intervals or standard deviations reported for Table 1**: The paper reports mean ATE error over 50 bootstrap resamples but does not report standard deviations or confidence intervals. The significance stars (∗/∗∗) are defined relative to pairwise comparisons, but the reader cannot assess the variability of estimates. This makes it hard to judge whether ZNet's performance is statistically distinguishable from baselines in many settings.

- **TrueIV sometimes underperforms ZNet, raising questions about the evaluation**: In several settings (e.g., Linear Disjoint with TSLS: TrueIV -0.002 vs. ZNet 0.119; Linear Latent with DeepIV: TrueIV -0.317 vs. ZNet -0.136), the known ground-truth instrument underperforms ZNet's learned representation. This is not necessarily fatal—it can happen when the true instrument is weak for the particular estimator—but the paper does not discuss why, which undermines confidence in the evaluation design.

- **The additive error model assumption (Eq. 1) is inherited from Hartford et al. (2017) without discussion**: The SCM assumes unobserved confounders influence Y and T only additively. This is a strong parametric restriction that ZNet inherits. The paper does not discuss what happens when this assumption is violated (e.g., multiplicative confounding, or U influencing the treatment-covariate relationship).

- **Hyperparameter tuning is elaborate and may inflate reported performance**: The Bayesian optimization pipeline tunes loss weights, architecture choices, loss type (PC vs. MI), and gradient surgery decisions. While baselines were also tuned, the paper does not report how many trials were run, whether the selected parameters generalize across datasets, or the sensitivity of results to hyperparameter choices.

### Trivial

- Figure 4 shows a confusion matrix with axis labels reversed: row 1 (cluster 1) maps to column 0 (true label 0), indicating a relabeling step was applied but is not clearly explained in the caption.

## Nice-to-Haves
- A real-world case study applying ZNet to a dataset with a known valid instrument (e.g., genetic variants in Mendelian randomization, geographic proximity in economics) and comparing the ATE estimated using ZNet's learned Z versus the known instrument.
- Overidentification test (Sargan or placebo) on the learned Z in "No Candidate" settings to provide diagnostic evidence of instrument validity.
- An experiment with continuous treatments, since the paper claims ZNet supports them but evaluates only binary treatments.
- Sensitivity analysis showing ATE error as a function of key loss weights to assess whether performance is concentrated at a narrow hyperparameter peak.

## Removed Points
- "Confusion matrix shows perfect recovery, suggesting dataset is too simple": This is actually evidence of correct behavior in a clean setting and validates the method. The diagonal entries being 1.00 after K-Means+relabeling is expected when the latent instrument is perfectly recoverable.
- "Hyperparameter tuning leads to overfitting": The paper tunes both ZNet and baselines using the same Bayesian optimization framework, so any overfitting concern applies symmetrically.
- "No real-world experiment" is a valid concern but retained in Major; the specific phrasing "No Mendelian randomization or geographic variation test" is scope-creep since the paper never specifically claimed to evaluate those domains.
- "Missing confidence intervals" moved from Trivial to Minor since the bootstrap significance stars partially address this.

## Novel Insights
None beyond the paper's own contributions. The reviewer input does not synthesize observations that the paper itself does not already articulate or imply.

## Suggestions
1. **Tone down the scope claims**: Change "regardless of whether the assumption of unconfoundedness is satisfied" to something like "under the assumption that X can be decomposed into instrument and confounder components, the method reduces reliance on pre-specified instruments." The current language overpromises relative to what the evaluation demonstrates.
2. **Add a real-world validation experiment**: Apply ZNet to a dataset where a known valid instrument exists (e.g., a well-studied Mendelian randomization dataset) and compare estimates using ZNet's learned Z against the known instrument. Even one such experiment would significantly strengthen the empirical contribution.
3. **Report standard deviations or confidence intervals** alongside the mean ATE errors in Table 1.
4. **Add an overidentification test** (e.g., Sargan test) for the learned Z in No Candidate settings to provide diagnostic evidence.
5. **Discuss the identification gap explicitly**: Add a paragraph acknowledging that correlation-based constraints do not guarantee conditional independence, and discuss when the approximation is reasonable (e.g., linear Gaussian systems where zero partial correlation implies conditional independence).
6. **Add a robustness experiment**: Generate data where the true SCM violates ZNet's assumptions (e.g., non-additive confounding, instrument not a function of X) and show graceful degradation.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/s9eVX36UBl.md` | 2.50 | Much weaker: one-stage IV regression with toy experiments and limited novelty. ZNet is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/1qhNFRxORK.md` | 3.50 | ACTIVA: similarly limited to semi-synthetic data with overclaiming. ZNet has stronger empirical scope. |
| `/home/wg25r/review_agent/human_reviews_2026/j2D7VKS6Ob.md` | 4.00 | Contrastive learning for IV: comparable quality of idea, similar semi-synthetic scope. ZNet's evaluation is more comprehensive. |
| `/home/wg25r/review_agent/human_reviews_2026/1tTs2gZAJN.md` | 4.00 | CI-StoNet (Accepted Poster): had identification theory which ZNet lacks, but narrower experiments. Comparable overall. |
| `/home/wg25r/review_agent/human_reviews_2026/kvzW81UtyH.md` | 4.50 | Causality-inspired robustness: similar strength/weakness profile, semi-synthetic + some real data. Comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/ZPam0jRjTC.md` | 5.00 | Outcome-aware spectral features: stronger theory, same semi-synthetic limitation. ZNet has broader evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/dYaos1ITw4.md` | 6.00 | Topological causal effects (Accepted Poster): real-world experiments, rigorous theory. Stronger than ZNet. |

Positioned among these anchors, ZNet is clearly stronger than the 2.5 paper and comparable to the 3.5–5.0 papers. Its main deficit relative to the 5.0+ papers is the lack of any real-world validation and the absence of formal identification guarantees. Given the overclaiming in the abstract and Discussion relative to what is actually demonstrated, a score on the lower end of this band is warranted.

**Score**: 4.5 — A borderline paper that addresses an important problem with a clean architecture and thorough (albeit semi-synthetic-only) evaluation. The contribution is real but substantially weakened by overclaiming, the lack of theoretical guarantees for the central claim, and the absence of any real-world validation. The paper would benefit from a more measured presentation of its contributions and additional experiments demonstrating robustness outside the assumed SCM.

**Decision**: Reject — While the core idea has merit, the paper does not currently meet the bar for ICLR. The evaluation is entirely on data that matches the method's assumptions, and the central claim that ZNet produces valid instruments is not supported by theoretical guarantees or real-world evidence. A substantially revised version with real-world validation, formal analysis of when the correlation-based constraints suffice, and more measured claims could be competitive.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>