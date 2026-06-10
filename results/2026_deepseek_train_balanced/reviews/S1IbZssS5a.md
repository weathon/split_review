## Summary

This paper proposes Label-Noise-based Re-balancing (LNR), a data-level method that introduces asymmetric label noise—flipping only majority-class samples to minority classes with probability proportional to their estimated posterior—to correct decision boundaries biased by class imbalance. The paper provides theoretical analysis (Lemmas 2–3) linking the F1-optimal decision boundary to a boundary achievable via asymmetric label flipping, and validates the method on 32 KEEL binary datasets and long-tailed/step-wise CIFAR-10/100.

## Strengths

- **Lemma 2 provides a precise analytical form of the F1-optimal decision boundary** (Section 3.2): $S^{F1} = \{x_0 : P_1(x_0)/P_0(x_0) = \frac{\mathcal{F}1(x_0)}{2-\mathcal{F}1(x_0)}\frac{\pi_0}{\pi_1}\}$, formalizing how the boundary maximizing F1 deviates from the accuracy-optimal boundary by a factor involving both the attainable F1 score and the imbalance ratio. This gives the method a clear theoretical target.

- **Lemma 3 proves that asymmetric label noise can make the Bayesian boundary on noisy data coincide with the F1-optimal boundary on clean data** (Section 4.1): $S^* = \{x^* : \frac{P_1(x^*)}{P_0(x^*)} = [1-2\rho(x^*)]\frac{\pi_0}{\pi_1}\}$ with the condition $\frac{\mathcal{F}1(x^*)}{2-\mathcal{F}1(x^*)} = 1-2\rho(x^*)$. This directly motivates the LNR flipping strategy.

- **Top few-shot accuracy on long-tailed CIFAR-100** (Table 2): LNR achieves 30.72% few-shot accuracy vs. LDAM-DRW (27.23%) and RSG (29.80%), with LNR+GCL pushing to 31.06%. This validates the method on the hardest tail classes where sample scarcity is most acute.

- **Highest average relative ranking across 32 KEEL datasets for all three classifiers** (Figure 4): LNR achieves the closest-to-1 average ranking in F1 and G-mean for KNN, CART, and MLP, providing broad empirical support across diverse binary imbalanced problems.

- **Simple, classifier-agnostic design**: The method operates at the data level, requires no modification to the classifier being trained, and integrates with algorithm-level methods (shown via GCL combination). The multi-class extension avoids training a separate estimator by using the model's own softmax outputs.

## Weaknesses

### Fatal
None.

### Major

- **The flip-rate estimator's reliability under extreme imbalance is unexamined.** The method estimates $\rho(x) \propto \eta(x)$ by training $C_f$ on the original imbalanced data (Section 4.2, Step 1). The paper acknowledges this estimate is biased but asserts that "majority class samples with features similar to those of minority class samples still tend to exhibit relatively higher posterior probabilities" — an empirical claim that is never validated. The paper provides no experiment that isolates and tests whether the ranking of $\hat{\eta}(x)$ among majority samples is meaningful enough to drive beneficial flips, especially under extreme imbalance where $\hat{\eta}(x)$ may be near-zero for virtually all majority samples. While the aggregate KEEL results indirectly show the method works on average, the mechanism itself receives no direct scrutiny. This is the paper's most significant evidential gap.

- **The multi-class online label-flipping loop is analyzed for neither stability nor convergence.** Section 4.3 uses the model's own softmax outputs during training to determine which labels to flip, creating a feedback loop: the model's (biased) predictions determine the training labels, which then update the model. The deferred initiation ($T_D$ epochs) is borrowed from DRW, but DRW adjusts *loss weights*, not *labels* — reweighting cannot introduce consistent bias in the training signal, while relabeling can. The paper provides no analysis of when this loop converges to a better boundary versus when it reinforces the original bias. The sensitivity analysis (Section 5.2) covers only $t_{flip}$ for binary MLP on KEEL and says nothing about the multi-class setting or $T_D$.

### Minor

- **Sensitivity analysis is too thin to support claims of robustness.** Section 5.2 consists of three sentences describing the qualitative direction of $t_{flip}$ effects with no figures, no ablation grids, no analysis of $T_D$ in the multi-class setting, no study of the z-score normalization or tanh truncation choices, and no investigation of how the choice of flip-rate estimator $C_f$ affects results. The paper states $t_{flip}$ "can be selected by cross-validation" but provides no information on the range searched, whether it was per-dataset or global, or how sensitive the rankings are to the choice.

- **No statistical significance testing.** The KEEL evaluation (32 datasets, relative rankings in Figure 4) reports no statistical comparisons (e.g., Wilcoxon signed-rank test, critical difference diagrams). Given that performance differences between methods may be small, it is unclear whether LNR's top ranking is reliably distinguishable from the second-best method.

- **Missing comparisons with standard long-tailed learning baselines.** For multi-class experiments, the paper compares LNR against LDAM-DRW and RSG (and GCL as a combination). Contemporary baselines such as Balanced Softmax, logit adjustment, or BBN are absent. While the included comparisons are not weak, the omission makes it harder to calibrate LNR's position in the long-tailed learning landscape.

- **The multi-class algorithm pseudocode is difficult to parse.** Lines 155–162 contain unclear notation (`minMax`, `uni form`, `if U contains 1`) that would hinder reproduction without additional clarification.

### Trivial

- The claim that LNR avoids "information loss" (Abstract, Section 6) is slightly overstated: flipping a majority-class label to minority *does* discard the original label information. The more relevant contrast is that LNR avoids generative errors (synthetic samples) and retains all feature vectors, which is defensible and useful but should be phrased more precisely.

## Nice-to-Haves
- A synthetic experiment with known ground-truth $\eta(x)$ to directly validate whether the biased $\hat{\eta}(x)$ ranks boundary samples correctly.
- Deterministic vs. probabilistic flipping ablation to justify the probabilistic noise model.
- Tracking the number of flips per epoch and flip-set overlap in the multi-class setting to demonstrate stability.
- Computational cost discussion comparing the overhead of training $C_f$ vs. running SMOTE or other baselines.

## Removed Points
These points are flagged to be removed; treat them with caution:

1. **Criticism about tables being images** — This is a PDF-parser artifact, not a paper problem.
2. **Criticism about missing algorithm-level baselines in binary experiments** — LNR is a data-level method and the paper compares against a standard set of data-level baselines (SMOTE, ADASYN, Borderline, RUS, OSS, CC). RUS directly addresses the request for "straightforward majority-class downsampling." Asking for cost-sensitive or threshold-moving baselines in this context is scope creep.
3. **"Information loss is misleading" framed as a major weakness** — The paper's contrast is between label-flipping and *generative errors* from oversampling plus *information loss from undersampling*. Flipping preserves feature vectors and avoids synthetic samples; the framing is reasonable and the criticism is a semantic quibble, downgraded to Trivial above.
4. **Criticism about missing related works** — Rule prohibits mentioning missing references without external confirmation.
5. **Formatting/style nitpicks** — Parser artifacts, not paper errors.

## Novel Insights

None beyond the paper's own contributions. Both the Harsh Critic and Strength Finder converge on the same assessment: the theoretical connection between F1-optimal boundaries and asymmetric label noise is genuinely novel and well-motivated, but the empirical validation does not fully probe the fragile points of the method (estimator reliability under extreme bias, multi-class loop stability). The reviews add no insight beyond what the paper authors themselves would likely recognize as the natural next steps.

## Suggestions

1. Add a controlled synthetic experiment (e.g., Gaussian classes with known $\eta(x)$) that directly measures whether the biased $\hat{\eta}(x)$ from $C_f$ correctly identifies the majority-class samples that would benefit from label flipping. This would either confirm or bound the circular-dependency concern.
2. For the multi-class setting, include a stability analysis: track the number and identity of flipped samples across epochs, show that the flipped set stabilizes rather than oscillating, and demonstrate that performance does not collapse for a range of $T_D$ values.
3. Add sensitivity curves (at minimum, performance vs. $t_{flip}$ and vs. $T_D$) for at least one binary and one multi-class dataset.
4. Clarify the multi-class pseudocode (Algorithm 2) with standard notation and a worked example.

## Score and Decision

The paper introduces a genuinely novel approach to imbalanced learning with a clean theoretical motivation. The method is simple, classifier-agnostic, and delivers solid empirical results across two evaluation settings (32 KEEL binary datasets + long-tailed CIFAR-10/100). However, two structural concerns about the method's core mechanism—the reliability of the flip-rate estimator and the stability of the multi-class feedback loop—are acknowledged but not adequately analyzed. These gaps reduce confidence in the method's behavior in failure regimes but do not invalidate the demonstrated results. The paper makes a real contribution and the evidence in favor is stronger than the evidence against.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>