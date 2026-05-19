- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
I now have all the information needed. Let me compile the final consolidated review.

---

## Summary

This paper proposes a novel approach to evaluating and mitigating bias in image classification models based on continuous skin-tone nuance, avoiding the pitfalls of categorical grouping. The method converts skin-color pixels into ITA probability distributions, uses Wasserstein distance (relative to a randomly selected baseline image) to quantify differences, and fits a Bayesian polynomial regression to predict per-batch performance from that distance. A weighted loss function—applied only after ~30% of training epochs—then penalizes the model based on the inverse of predicted performance to reduce correlation between skin color and prediction quality. The approach is tested on three datasets (HAM, CelebA, UTKFace) with three architectures (VGG16, EfficientNet, ResNet50).

## Strengths

- **Novel continuous skin-color representation preserves within-group nuance.** Unlike prior work that averages skin pixels into a single ITA value or discretizes into categorical Fitzpatrick types, Algorithm 1 computes a per-pixel ITA distribution. This allows Wasserstein distance (Section 3.1.1) to capture fine-grained shifts in skin tone that categorical grouping would discard. Figure 2(C) demonstrates the approach empirically, showing three images all labeled "white" with visibly different ITA distributions.

- **Bayesian regression enables bias detection without skin-type annotations.** Section 3.2 fits a Bayesian polynomial regression that predicts per-batch F1/Accuracy from Wasserstein distance to a baseline. This requires no manual skin-type annotation—only the image itself. Figure 3 shows fitted regression curves revealing correlations between skin-color distance and performance for UTKFace and HAM datasets that group-level metrics would conceal.

- **Multi-dataset and multi-model evaluation provides breadth.** The method is tested on three diverse datasets (dermatoscopic images, facial attributes, facial demographics) with three pre-trained architectures (VGG16, EfficientNet, ResNet50), as described in Sections 4.1 and 4.2. This shows the approach is not tied to a single domain or model family.

- **Principled epoch scheduling aligns with CNN learning dynamics.** Algorithm 2 applies the weighted loss only after approximately 30% of training epochs. The paper justifies this by noting that CNNs focus on coarse features early in training (Section 3.3), so penalizing skin-color nuance prematurely would be counterproductive.

## Weaknesses

### Fatal

None.

### Major

- **No direct comparison of accuracy/F1 between unmitigated and mitigated models.** Table 3 reports pre- and post-mitigation *correlation* coefficients, and Table 4 (referenced in Section 4.2) shows "general performance" of the unmitigated models, but the paper never puts these side-by-side. The reader cannot assess whether the correlation reduction came at a substantial cost to overall accuracy or F1. Without this trade-off analysis, the claim that the method "mitigates" bias without degrading performance is unsubstantiated. At minimum, a table comparing accuracy/F1 for the unmitigated and mitigated conditions for every dataset/model combination is needed.

- **Random baseline selection introduces unexamined variance.** Section 3.1.1 states: "the baseline image, denoted by $x_0$, is selected randomly from the validation dataset." The entire pipeline—Wasserstein distances, Bayesian regression fit, and resulting loss weights—depends on this single arbitrary choice. The paper reports no analysis of stability across different random baseline selections, and the results tables (Tables 2–3) show no variance measures. This is a serious reproducibility concern: a different random baseline could yield different distance values and thus different loss weights and final model behavior. The authors should either justify a principled reference (e.g., the median skin distribution across the validation set) or run multiple trials with different baselines and report variance.

- **No confidence intervals or statistical significance for correlation results.** Table 3 reports correlation coefficients "before" and "after" mitigation for each dataset/model combination (e.g., HAM+EffNet: 0.40→0.06, UTKFace+ResNet: 0.02→0.00), but provides no confidence intervals or p-values. Given the small validation set sizes (especially HAM with ~49 validation images after the 60/20/20 split), the observed pre-mitigation correlations may not be statistically significant, which would render the "mitigation" effect meaningless. Bootstrapped confidence intervals or at minimum standard errors should be reported for all correlation values.

- **Several method details are under-specified, hindering reproducibility.** (a) **Polynomial degree selection** (Section 3.2): "The degree of the polynomial regression depends on the model and dataset and is determined from the prior distribution" is vague. How exactly is the degree determined? Cross-validation? Automatic relevance determination? (b) **Epoch threshold** (Section 6): The paper states the penalty is applied "about 30% of the total training epochs for most combinations" but does not describe how this was tuned across combinations or report sensitivity to this value. (c) **Batch size for Bayesian regression** (Section 3.2): Set to "1% of the validation dataset." For HAM (~49 validation images), 1% is less than a single image, making this description ambiguous or potentially non-sensical.

### Minor

- **Small dataset sizes after balancing undermine reliability.** After balancing class labels and skin-color groups, HAM has only 246 total images (Table 1), yielding ~147 training, ~49 validation, and ~49 test images. The Bayesian regression is fit on roughly 49 validation points. While pre-trained models mitigate some concerns about training, the small validation set makes the correlation estimates and their reductions potentially noisy. The paper should run multiple seeds or use cross-validation to demonstrate stability.

- **Loss function equation contains an error.** Section 3.3, Equation (line 162) shows $l_n = -w\{y_n \cdot \log x_n + (1-y_n) \cdot \log x_n\} \cdot \sigma \cdot \alpha$ where both terms are $\log x_n$. Standard binary cross-entropy requires $\log(1-x_n)$ in the second term. This appears to be a typo that should be corrected, though it may not affect implementation if the code is correct.

### Trivial

None.

## Nice-to-Haves

- **Stabilize the baseline reference:** Replace the random single-image baseline with a principled reference (e.g., median distribution across the validation set) to eliminate arbitrary variance.
- **Compare to a simpler continuous baseline:** A comparison using the mean ITA value as a scalar sensitive attribute (as done in tabular fairness) would isolate the benefit of using the full distribution and Wasserstein distance.
- **Report computational overhead:** The pipeline adds skin detection, per-pixel ITA computation, Wasserstein distance calculation, Bayesian regression fitting, and dynamic loss weighting. A brief discussion of training time overhead relative to standard training would help practitioners assess practicality.

## Removed Points

These points from the reviews are flagged to be removed; treat them with caution.

- **Missing individual fairness literature citations (Dwork et al., 2012, etc.):** Removed per rule against raising missing related works, as the reviewer cannot confirm coverage from external knowledge.
- **"Figure 1 referenced but algorithm list missing":** Removed as a parser artifact—embedded images are stripped by the extraction process.
- **"No discussion of computational cost":** Removed as scope creep; this is a nice-to-have, not a weakness.
- **Criticism about the claim "no research has achieved a fair model without annotations":** Removed as an opinion about related-work characterization rather than a concrete technical flaw in the paper.
- **Strength Finder's generic/superficial praise:** Some of the Strength Finder's strengths (e.g., commenting on the "importance of the problem") were dropped per instructions to keep only concrete, evidence-grounded strengths.

## Novel Insights

The intersection of the two reviews surfaces an interesting tension: the paper's core strength—treating skin color as a distribution rather than a scalar or category—is also the source of its most significant evaluation gaps. The Wasserstein-distance-based representation is genuinely novel and well-motivated, but the reliance on a single random baseline image undermines the claimed objectivity. Similarly, the Bayesian regression approach elegantly avoids needing annotations for bias detection, yet the lack of confidence intervals on the correlation estimates makes it impossible to distinguish genuine signal from noise on the small validation sets. This suggests that the paper's contribution would be substantially strengthened not by adding more datasets or models, but by a careful uncertainty analysis (bootstrapping the correlations, running multiple baselines, and comparing accuracy trade-offs) that matches the rigor of its theoretical framing.

## Suggestions

1. **Add an accuracy/F1 trade-off table** directly comparing unmitigated vs. mitigated models for every dataset/model combination, so readers can assess whether fairness gains come at a performance cost.
2. **Replace or robustify the random baseline.** Either use a principled reference (median distribution) or run multiple random baselines and report mean/variance of all metrics.
3. **Report confidence intervals** for all correlation coefficients in Table 3 (bootstrapped or otherwise) to establish statistical significance.
4. **Clarify the polynomial degree selection** procedure and the epoch threshold tuning method; report sensitivity to these hyperparameters.
5. **Fix the loss function typo** (both terms are $\log x_n$).
