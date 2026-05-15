Now I have all the information I need. Let me construct the final review.

---

## Summary

This paper addresses multi-step algorithmic recourse — providing paths of sequential changes for individuals who received negative decisions from an ML classifier. It makes two contributions: (1) a PAC learning framework for learning an optimal distance function and threshold that define feasible transitions from labeled examples, and (2) a data augmentation algorithm (Algorithm 2) that generates synthetic intermediate points to ensure every negatively classified individual receives a recourse path. Experiments on one synthetic and three real datasets (PIMA, Adult, HELOC) show that the method achieves validity = 1.0 (recourse for all) while baselines (FACE, counterfactual explanations) fail to provide paths for some individuals.

## Strengths

- **Formal PAC learning framework for distance/threshold selection.** The paper provides VC-dimension bounds (Theorems 2.2, 2.5) and efficient ERM algorithms (Theorems 2.3, 2.6) for learning feasible transition classifiers, with sample complexity guarantees (Theorems 2.4, 2.7). This formalizes a key gap in prior path-based methods that assumed fixed, unlearned distance functions.

- **Augmentation algorithm provides recourse coverage for all individuals.** The experimental results (Figure 2) convincingly show that across all four datasets, the proposed method achieves validity = 1.0, meaning every negatively affected individual receives a recourse path. In contrast, FACE validity drops as low as ~0.3 (synthetic) and ~0.2 (HELOC), demonstrating that the augmentation fills genuine coverage gaps.

- **Clear identification of the limitation in existing path-based methods.** The paper explicitly motivates the problem by showing (Figure 1) that a fixed distance threshold either permits infeasible transitions (too large) or denies recourse to some individuals (too small). This framing correctly identifies a real and important problem.

- **Model-agnostic and supports non-trivial constraints.** The method requires only prediction probabilities (not gradients), handles non-symmetric directional distance functions (Section 2.2.2), and can incorporate monotonicity constraints (Adult and HELOC experiments), making it applicable to practical settings where causal graphs or gradient access is unavailable.

## Weaknesses

### Fatal
None.

### Major

- **Feasibility labels are synthetic rules with no external validation.** The "ground truth" feasible transitions h* are generated using hand-crafted rule sets that vary arbitrarily across datasets (L1 distance below feature-wise standard deviation for PIMA; monotonicity + bounded variance for Adult and HELOC). The paper provides no evidence that these rules correspond to real-world feasibility, no human evaluation, and no domain-expert validation. This limits the external validity of the claims — the method learns to approximate an ad-hoc rule, not necessarily to capture realistic feasibility. While the paper acknowledges this limitation (Section 5: "future directions will include using human annotators"), it is structural to the current evaluation.

- **Only logistic regression classifiers tested.** The paper claims model-agnosticism (requiring only prediction probabilities) but conducts all experiments with logistic regression. No experiments with non-linear models (random forests, gradient boosting, MLPs) are provided. It is unclear whether the augmentation algorithm produces plausible points under complex decision boundaries or whether the Bayesian optimization solver handles non-convex landscapes effectively. This gap weakens the model-agnostic claim.

- **No validation that augmented (synthetic) points are realistic or achievable.** Algorithm 2 generates points by optimizing over the entire feature space subject only to d(x', y) ≤ τ, with no mechanism to ensure points respect feature ranges, causal dependencies, or distributional plausibility. The paper provides no case studies showing actual feature values at each step, no checks for whether augmented points lie within the data manifold, and no analysis of distributional shift. The claim of "feasible recourse" is only as strong as the guarantee that generated points correspond to achievable states.

- **Weak baseline selection; StEP is cited but not compared.** The paper cites StEP (Hamer et al., 2023) as a related path-based method but does not include it as a baseline. The only multi-step baseline is FACE, which is used with the same learned distance/threshold (advantageous as a controlled comparison but insufficient to establish state-of-the-art performance against existing methods). Single-step counterfactual explanations are included but are not a strong baseline for a path-based method.

### Minor

- **No statistical significance or uncertainty reported for main results.** Figure 2 reports point estimates for validity, average distance, and weight but provides no confidence intervals, error bars, or significance tests. Given the small sample (50 random individuals per dataset), results may be sensitive to the particular sample drawn.

- **HELOC has extreme class imbalance (0.444% feasible transitions) without discussion.** Learning a distance threshold from such an imbalanced binary labeling problem is questionable without discussing class imbalance handling, alternative thresholds, or undersampling techniques.

- **Theorem 2.8 convergence guarantee relies on strong assumptions.** The theorem requires that for all x there exists y satisfying f(y)-f(x) > λ / min w(a,b), and that the algorithm *only* chooses fresh points (the case it tries to avoid). The practical scenarios where this guarantee applies are not analyzed.

- **λ sensitivity is described but not systematically resolved.** Figure 3 shows that λ controls the trade-off between path ease and convergence, and that large λ can cause non-convergence (validity < 1 for PIMA). No systematic method for choosing λ is provided beyond "needs appropriate λ."

### Trivial
None.

## Nice-to-Haves

- A comparison with StEP or other path-based recourse methods.
- Case studies from real datasets showing feature values at each step of a recourse path, allowing qualitative assessment of path plausibility.
- Experiments with at least one non-linear classifier to support the model-agnostic claim.
- Validation of generated points via density estimation, feature range checks, or human evaluation.
- Statistical significance reporting for the main results in Figure 2.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Circular evaluation"** — The critic claimed the evaluation is circular because validity is checked against learned d,τ. This is a misunderstanding: the paper separately evaluates (a) how well d,τ approximates h* (Table 1, 0-1 error) and (b) whether the augmentation produces paths satisfying the learned constraints (Figure 2). The baselines also use the same d,τ, making the comparison fair. This is standard evaluation of a learned model, not circularity.

2. **"Age is mutable"** — The critic claimed age is allowed to change unrealistically. The paper enforces monotonicity constraints where age must *increase* (Adult dataset), which is factually correct (people age forward). This criticism is factually wrong.

3. **"PAC results are not novel"** — The critic called the theoretical results "straightforward applications of standard VC-dimension bounds." While the bounds are indeed standard, applying them to the recourse setting with distance functions and thresholds is a valid contribution that the paper does not oversell. This is a judgment about degree of novelty, not a factual error.

4. **"No comparison to methods using human-provided constraints"** — The paper explicitly scopes itself as a data-driven alternative (Discussion section) and acknowledges that human-provided constraints are a future direction. Demand-ing this comparison exceeds the paper's stated scope.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that the paper itself does not articulate.

## Suggestions

1. **Expand the classifier zoo.** Run experiments with at least one non-linear model (e.g., random forest, XGBoost) to demonstrate model-agnosticism and test augmentation robustness under complex decision boundaries.

2. **Validate augmented points qualitatively and quantitatively.** Provide 2–3 concrete case studies showing feature values at each path step, run density-based out-of-distribution checks on generated points, and if possible, conduct a small human evaluation or domain-expert plausibility check.

3. **Include StEP as a baseline** since it is already cited and is a natural competitor for path-based recourse.

4. **Add error bars or confidence intervals** to the main results in Figure 2.

5. **Be more precise about what "feasibility" means** in the paper's claims. The paper should state clearly that feasibility is defined with respect to learned distance constraints and that the quality of these constraints depends on the training labels.

## Score and Decision

The paper addresses an important problem and provides a sound framework with theoretical grounding. The core technical ideas — learning distance/threshold for recourse and augmenting to ensure coverage — are valuable. However, the experimental evaluation has significant gaps: only logistic regression is tested, the feasibility labels are arbitrary synthetic rules with no external validation, the augmented points are not validated for realism, and the baseline set is thin. These weaknesses weaken — but do not invalidate — the paper's contributions. The paper needs substantial additional experimental validation before it can be accepted.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>