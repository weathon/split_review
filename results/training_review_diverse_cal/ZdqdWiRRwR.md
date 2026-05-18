I have thoroughly cross-checked all claims against the paper. Here is my consolidated review.

---

## Summary

The paper proposes Recursive Metadata Normalization (R-MDN), a normalization layer that removes the influence of known confounding variables from intermediate DNN features via recursive least squares (RLS) regression. The key innovation is operating at the individual-example level (rather than requiring batch statistics like prior work MDN), which enables compatibility with vision transformers and true online/continual learning. The method is evaluated on synthetic data, ABCD sex classification (static), and HAM10000 skin lesion classification (continual), comparing against MDN, P-MDN, BR-Net, and standard continual learning baselines (EWC, LwF, PackNet).

## Strengths

1. **Individual-example-level operation directly addresses a real limitation of prior work.** Unlike MDN, which requires pre-computed batch-level covariance matrices and is incompatible with vision transformers, R-MDN uses the Sherman-Morrison rank-1 update to process each example independently within a minibatch (Section 3.2). This is validated on HAM10000 with a ViT backbone (Table 4), where MDN cannot be applied at all. This is a genuine architectural improvement that opens up confounder removal to modern architectures.

2. **Handles changing confounder distributions in continual learning without stage-specific networks.** R-MDN's internal state (regression coefficients + inverse covariance) is continuously updated across training stages, requiring only a single network. In the synthetic continual learning experiment, R-MDN achieves the best forward transfer distance (FWTd = 0.18, Table 3). On HAM10000 with ViT, R-MDN (C) achieves the highest average accuracy (0.70) and lowest dcor² (0.08) among all methods (Table 4).

3. **Consistently reduces feature–confounder correlation across all settings.** In ABCD sex classification, R-MDN drives squared distance correlation down to 0.08 ± 0.03 (boys) and 0.08 ± 0.02 (girls), substantially lower than the base model (0.31, 0.37) and lower than BR-Net and P-MDN (Table 2). It also achieves the smallest difference between TPR and TNR (0.00 ± 0.03), indicating equitable predictions across population groups — a direct fairness benefit.

4. **Robust generalization when confounders are absent at test time.** Figure 5 shows R-MDN maintains stable accuracy (~80%) across confounder intensity from fully present to fully absent, while the base model drops below 60% and both BR-Net and P-MDN degrade. This supports the claim that R-MDN relies on task-relevant features rather than spurious confounder correlations.

5. **Efficient online update.** The closed-form RLS derivation using the Sherman-Morrison formula (Section 3) avoids recomputing the full covariance inverse, making the approach computationally viable for streaming and minibatch learning. Complexity analysis is provided in the supplement.

## Weaknesses

### Fatal
None.

### Major

1. **The linearity assumption is the paper's central limitation, and its justification is inadequate.** R-MDN removes only *linear* dependencies between features and confounders. The paper's justification (Section 1, lines 19–20) offers two "key considerations": (1) nonlinear model decisions are hard to interpret, and (2) sufficiently powerful nonlinear models can extract arbitrary variables from features. Neither of these justifies why a *linear* model is sufficient to remove confounder influence from deep features. The method uses dcor² as its evaluation metric, which captures nonlinear dependence, and while R-MDN consistently reduces dcor², residual nonlinear dependence remains. **The paper should explicitly qualify what "removing the influence of confounders" means under this linearity assumption, discuss when linear removal is likely sufficient (e.g., monotonic confounder effects, low-complexity features), and provide a diagnostic for when residual nonlinear dependence might be problematic.** This does not invalidate the paper's contribution (which is structural — enabling ViT/continual learning via RLS), but it means the central claim is somewhat overstated relative to the evidence.

2. **The theoretical maximum accuracy (A_i) used in the continual learning metrics is not reported per stage for the synthetic experiments.** The BWTd and FWTd metrics (Eq. 1–2) require stage-specific theoretical maximum accuracies A_i. The paper defines A_i (line 157) but does not report the values for each of the 3 datasets × 5 stages. Since the distributions of σA change across stages (line 154), A_i changes accordingly. Without reporting these values, the reader cannot independently verify the BWTd/FWTd numbers. For HAM10000, no theoretical maximum exists, so BWTd/FWTd are not computed — the paper only reports stage-wise accuracies, which is appropriate but limits the generality of the continual learning evaluation.

### Minor

1. **Important method details are deferred to the supplement.** The regularization parameter λ ablation (central to adaptation speed vs. stability), computational/memory complexity analysis, and alternative layer placement studies are all in the supplement. A brief summary of λ sensitivity and a runtime comparison table in the main text would improve reproducibility and practical utility.

2. **Only single confounders are tested per experiment.** The paper uses one confounder per setting (σB, PDS score, age). R-MDN supports multiple confounders in principle (via the joint matrix X), but no experiment demonstrates this. A synthetic scenario with two confounders would strengthen the claim of general applicability.

3. **The t-SNE visualization (Figure 6) is qualitative.** The paper uses it to suggest that R-MDN's reduced feature separation is due to confounder removal rather than task-irrelevant information loss. Quantitative cluster metrics (e.g., silhouette score conditioned on confounder values) would provide more rigorous evidence for this interpretation.

### Trivial
None.

## Nice-to-Haves

- A nonlinear extension (e.g., kernel RLS or polynomial features of confounders) to directly measure how much additional confounder variance could be removed, even if the results show limited benefit.
- An ablation where a random (non-informative) confounder is used instead of the real one, to verify the benefit comes from removing the correct confounder rather than some other property of the RLS layer (e.g., regularization or feature decorrelation).
- Explicit reporting of stage-specific A_i values for each of the 3 synthetic continual learning datasets in the main text or supplement.

## Removed Points

These points were raised by reviewers but removed after cross-checking against the paper:

- **"R-MDN also projects out the label's linear influence from features"** — Removed because it is factually incorrect. The paper explicitly states (line 40): "We want to remove the influence of x̃ from z while preserving the variance related to the labels... obtain the residual r = z − x̃β̃_x; i.e., only with respect to β̃_x." The labels (y) are included in the regression matrix X only to improve the estimate of β̃_x via statistical control — a standard technique. Label information is preserved in the residual.

- **"Missing comparison against a feature-space OLS without recursive update"** — MDN *is* exactly this baseline. It pre-computes Σ⁻¹ over the training set and uses batch-level OLS. The recursive update is the paper's contribution. This comparison is already present.

- **"BWTd metric is circular"** — Removed because the metric is intentionally designed to measure deviation from an unbiased classifier's accuracy. Penalizing confounder use is the whole point. The paper correctly follows the standard formulation from Lopez-Paz & Ranzato (2017). The reviewer's observation that BWTd=0 can occur when both |R_{S,i}-A_i| and |R_{i,i}-A_i| are equally large is correct but describes a design feature of BWT-type metrics (they measure maintenance of behavior, not optimality), not a flaw.

## Novel Insights

None beyond the paper's own contributions. The core insight — using RLS with a Sherman-Morrison update for individual-example-level confounder removal — is clearly stated in the paper. The reviews surface no fundamentally new perspective on the work.

## Suggestions

1. **Qualify the linearity assumption and scope.** Add a paragraph explicitly stating that R-MDN removes linear confounder-feature dependencies and that residual nonlinear dependence may remain. Discuss when the linear assumption is reasonable and suggest diagnostics (e.g., comparing dcor² before and after residualization as already done).

2. **Report stage-specific A_i values** for the synthetic continual learning experiments, enabling independent verification of BWTd/FWTd.

3. **Move key ablation results to the main text** — at minimum a brief summary of the λ sensitivity analysis and a table of relative training time per batch for R-MDN vs. baselines with the ViT architecture.

4. **Add a multiple-confounder experiment** (e.g., synthetic data with two independent confounders) to demonstrate scalability of the approach.

## Score and Decision

The paper makes a solid, practical contribution: the RLS-based formulation enables confounder removal in settings where prior work (MDN, P-MDN) cannot operate (vision transformers, pure online/continual learning without look-ahead). The experiments are reasonably thorough across static and continual settings, and the fairness analysis (TPR/TNR balance) provides a concrete downstream benefit. The main weakness is that the linearity assumption is insufficiently bounded, but this is a limitation inherited from the broader literature (MDN shares it) and does not invalidate the structural contribution. The paper would be strengthened by more transparent discussion of residual confounding and by reporting a few deferred details in the main text. Overall, the contribution is real, novel, and well-validated within its scope.

**Originality:** Good — RLS for confounder removal in DNNs is novel.
**Importance:** Solid — addresses a real gap in ViT compatibility and continual learning.
**Claims support:** Good, with the caveat that the linearity assumption is under-scoped.
**Soundness:** Good — experiments are well-designed and use appropriate metrics (dcor²).
**Clarity:** Generally clear; methodology is well-explained.
**Value to community:** Positive — offers a practical tool for confounder removal in modern architectures.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>