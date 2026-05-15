Now I have all the information needed to produce the consolidated review. Let me write it.

## Summary

This paper proposes **Significant-subspace Alignment (SAL)**, the first principled test-time adaptation method designed specifically for regression. The key insight is that regression features occupy a low-dimensional subspace — naive alignment of all feature dimensions (as done in classification TTA) is harmful. SAL detects the feature subspace via PCA on source features and performs KL-divergence alignment only within that subspace, with dimension weighting based on the linear regressor's sensitivity. Experiments on image and tabular regression tasks (UTKFace, Biwi Kinect, SVHN→MNIST, California Housing) show consistent gains over adapted classification TTA baselines.

## Strengths

- **First TTA method designed specifically for regression**, filling a clear gap in the literature. The paper correctly identifies that existing classification TTA methods (entropy minimization, naive feature alignment) are ineffective or harmful for regression.
- **Empirical observation directly drives method design**: the finding that regression features concentrate in a low-dimensional subspace (e.g., only ~53 valid dimensions out of 2048 for ResNet-50 on UTKFace) directly motivates subspace detection, rather than ad-hoc modifications of classification techniques.
- **Comprehensive and well-designed experiments** spanning image and tabular domains, multiple shift types (corruption, gender split, geographic split), and diverse regression tasks (age prediction, head pose, digit regression, housing price). The ablation study cleanly isolates the contributions of subspace detection and dimension weighting, showing that removing either degrades performance.
- **Mechanistic understanding via feature-space analysis**: reconstruction error analysis (Fig. 3) demonstrates that SAL preserves the source feature subspace while baselines degrade it, and the Gaussianization analysis (Fig. 5) with CLT reasoning supports the use of the Gaussian KL divergence in the projected subspace.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No regression-specific theoretical bound connecting feature alignment to target error.** The paper motivates the KL-divergence alignment by citing Nguyen (2022), which bounds target error by a distribution gap term in UDA, and mentions Cortes et al. (2011) for regression UDA theory in related work. However, it does not provide an explicit argument or bound connecting the moment-matching KL loss to regression risk. This is an evidential gap rather than a structural flaw — the experiments are strong — but the theoretical motivation could be sharper.

2. **Subspace drift dynamics are not analyzed.** The source subspace is computed once and never updated during TTA. While limiting updates to affine normalization parameters constrains feature shift, the paper does not quantify how much the target features can deviate from this fixed subspace before alignment becomes ineffective. The reconstruction-error analysis (Fig. 3) shows that SAL preserves the subspace *after* adaptation, but does not demonstrate that the subspace remains a valid basis *during* intermediate adaptation steps.

3. **Gaussian assumption only partially verified.** The claim that projected features are approximately Gaussian (justifying the diagonal Gaussian KL divergence) is supported by histograms of only three randomly selected dimensions and a CLT argument. A more systematic verification (e.g., normality tests across all projected dimensions, or a discussion of the diagonal independence assumption in the projected space) would strengthen this justification.

4. **Linear regressor limitation not discussed as a limitation.** The dimension weighting (Eq. 4) explicitly depends on the weight vector **w** of a linear regressor head. The paper defines the setting accordingly, but does not discuss how the method would need to change for non-linear regression heads (e.g., MLPs).

### Trivial
None.

## Nice-to-Haves

- A study of sensitivity to the number of source samples used for PCA subspace estimation.
- Visualization of how the projection of target features onto the first few PCA axes evolves during TTA steps.
- Discussion of failure cases or scenarios where the low-subspace assumption might break (e.g., extremely high-dimensional tasks with no simple manifold structure).
- An adaptive subspace update mechanism for handling larger or more complex shifts.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Oracle scores not visible in provided text"** — Parser artifact; the tables (included as `\input{tab/...}` files) are embedded in the original PDF and not rendered in the text extraction. Not a paper flaw.
2. **"Independence across projected dimensions is not discussed"** — Factually incorrect; the paper explicitly states the independence assumption when motivating the CLT argument (line 350: "Assuming that $a_{i,d}$ is independent of the feature dimension $d$...").
3. **Criticism that the theoretical motivation relies on a "classification UDA" bound** — The paper cites Nguyen (2022) for "unsupervised domain adaptation" generally and also cites Cortes et al. (2011) for regression UDA theory. The broader point about missing regression-specific theory is retained as a minor weakness above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a brief paragraph (or a note in the appendix) connecting the feature-alignment KL loss to regression risk, even informally via the existing theoretical framework of Cortes et al. (2011). This would strengthen the theoretical motivation without requiring a formal bound.
2. Include a systematic normality test (e.g., Shapiro-Wilk or Kolmogorov-Smirnov) on the projected feature dimensions to quantitatively substantiate the Gaussianization claim.
3. Explicitly note the linear-regressor assumption as a limitation and briefly discuss how non-linear heads would affect the dimension-weighting scheme.

## Score and Decision

The paper is a well-motivated, empirically solid contribution to an under-studied problem. The method is simple, principled, and convincingly outperforms baselines across diverse regression tasks with strong ablation and feature-space analysis. The weaknesses are minor and do not threaten the core claims. The paper makes a clear contribution to the community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>