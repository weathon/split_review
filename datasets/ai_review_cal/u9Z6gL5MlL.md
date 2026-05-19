- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3
Now I have all the information needed. Let me construct the consolidated review.

## Summary

This paper challenges the widespread practice of using artificial memorization (noisy labels/inputs) as a proxy for studying natural memorization in deep learning. The authors compute memorization scores (Feldman & Zhang, 2020) for real data points across VGG, ResNet, and ViT architectures on CIFAR-10, CIFAR-100, and Tiny ImageNet. They report that two well-known findings from artificial memorization—that over-parameterization increases memorization and that longer training increases memorization—are reversed for natural memorization. They also identify "transient memorization" (points memorized under some conditions but later generalized), report a strong correlation (Pearson 0.99) between memorization and train-test gap, and argue that memorization is not necessary for generalization.

## Strengths

1. **Direct measurement of natural memorization across multiple architectures and datasets**: The paper uses the Feldman & Zhang (2020) memorization score approximation (training 2,000 models per architecture) to identify naturally memorized points, rather than relying on artificial proxies. Experiments span three architecture families (VGG, ResNet, ViT) and three datasets (CIFAR-10, CIFAR-100, Tiny ImageNet), providing breadth of evidence.

2. **Clear demonstration that over-parameterization reduces natural memorization**: Figure 1 and Tables 1–2 show a consistent trend across all three architecture families: as parameter count increases within the same family (SmallVGG → VGG19, ResNet18 → ResNet50, ViT-Tiny → ViT-Small), the number of naturally memorized points decreases. This directly contradicts the artificial-memorization claim and is the paper's strongest result.

3. **Identification of non-monotonic memorization dynamics across training**: Figure 2 reveals three stages (no memorization → increasing → decreasing) across architectures and datasets. The finding that memorization can peak and then decline within a standard training regime (~100 epochs) is a novel observation that contrasts with the artificial-memorization claim that memorization monotonically increases with training.

4. **Characterization of transient memorization with memorization scores**: Section 4.3 quantifies that model-wise transient points have average memorization scores of 44.99% ± 15.02% and temporal-wise transient points have 35.71% ± 4.69%, both well above the dataset-wide average of 11.17% ± 19.13%. This provides concrete evidence that transiently memorized points belong to small but non-trivial subpopulations, consistent with the paper's explanation.

## Weaknesses

### Fatal
None.

### Major

1. **The subtraction method for counting transient memorized points assumes a superset relationship that is not justified.** The paper computes model-wise transient points as 8,375 − 4,111 = 4,264 (SmallVGG memorized minus ResNet50 memorized, Section 4.3) and similarly for temporal-wise (8,380 − 6,425 = 1,955). This arithmetic implicitly assumes that every point memorized by the larger model / later epoch is also memorized by the smaller model / earlier epoch. If some points are uniquely memorized by the larger model (a plausible scenario given the "memorization capacity" the paper itself discusses), the subtraction overcounts transient points. Without tracking individual point identities across models or epochs, the reported counts are potentially unreliable. This directly affects the central "transient memorization" claim.

### Minor

2. **No uncertainty quantification on epoch-wise memorization counts (Figure 2).** The three-stage pattern (no memorization → peak → decline) is presented as a single trajectory per model without error bars, confidence intervals, or variance estimates, despite 2,000 models being trained per architecture. The decline from ~8,300 to ~6,400 for LargeVGG on CIFAR-10 (23%) could be meaningful, but the stochasticity of the approximation process is not characterized. The ViT plots are described as "more subtle" without quantifying this difference. Error bars would substantially strengthen the paper's main temporal claim.

3. **The correlation claim (Pearson 0.99) is reported without adequate detail.** The paper does not state the number of data points in Figure 3, the per-dataset breakdown, or confidence intervals for the correlation coefficient. With roughly 8 model configurations per dataset (Tables 1–2), the total is ~20 points; a correlation of 0.99 on this many points is unusually high and could be driven by a few influential points or by both quantities collapsing to the same underlying capacity measure. The paper would benefit from per-dataset scatter plots with model labels, a reported p-value or confidence interval, and discussion of alternative interpretations.

4. **No sensitivity analysis of the 25% memorization threshold.** The paper adopts the 25% threshold from Feldman & Zhang (2020) without examining whether the reported trends (over-parameterization decreasing memorization, transient memorization) are stable under different thresholds (e.g., 20%, 30%). The definition of which points count as "memorized" depends on this choice, and results could shift.

5. **The claim that "memorization is not necessary for generalization" is somewhat overbroad for the evidence presented.** The paper shows that for many points, memorization is transient and resolved with more model capacity or training. However, the paper does not directly examine whether extreme outliers (memorization scores close to 100%, i.e., subpopulations of size one) still require memorization, nor does it measure test accuracy on the specific subpopulations corresponding to transiently memorized points. The claim is stated as a general principle (Abstract, Section 5) but the evidence is limited to three image classification datasets and the specific architectures tested.

### Trivial

6. **ViT models are pretrained while VGG/ResNet models are trained from scratch**, introducing a confound when comparing across architecture families. The authors acknowledge this (line 96: "due to the use-pretrained base models"), but it limits the strength of cross-architecture comparisons and could affect the training-iteration dynamics.

## Nice-to-Haves

- **Replicate a canonical artificial memorization result under the same experimental conditions** (e.g., injecting noisy labels or Gaussian inputs into the same training pipeline). This would directly validate the claimed mismatch rather than relying on literature comparison. This would elevate the paper from a critique into a clean empirical demonstration.
- **Track individual points** across epochs (or at least across model sizes) to support the "transient" claim directly, rather than inferring it from aggregate differences.
- **Report test accuracy for the specific subpopulations** corresponding to transiently memorized points, to strengthen the argument that generalization (not just point-level forgetting) is occurring.

## Removed Points

*These points were flagged by reviewers but are removed for the following reasons:*

- **"The central contrast with artificial memorization is inferred, not directly demonstrated"** — Removed as scope-creep. The paper's contribution is studying natural memorization and comparing findings to well-established results in the published literature. Requiring replication of prior work's experiments is beyond what is standard for a paper making this type of negative claim. The literature's findings are cited and the paper's results stand on their own as a study of natural memorization.

- **"Reason (3) about small subpopulations is consistent with Feldman & Zhang"** — Removed because the paper is not criticizing Feldman & Zhang. It is using the F&Z finding as part of its argument that artificial memorization (noisy labels/inputs) is a limited proxy because real memorization also occurs for correctly labeled small subpopulations.

- **"Paper conflates over-parameterization with model depth and architecture changes"** — Removed because varying depth and width within architecture families is a standard approach to studying over-parameterization. The paper also validates across three different architecture families.

- **"Missing related works"** — Removed per instruction; cannot verify existence from external sources.

- **"Typos, formatting, etc."** — Removed as parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface weaknesses in the transient memorization arithmetic and the need for uncertainty quantification, but do not identify fundamentally new observations about memorization beyond what the paper itself presents.

## Suggestions

- Track individual point identities across model sizes and epochs to directly verify the "transient" claim rather than using aggregate subtraction.
- Add error bars (bootstrap confidence intervals) to the epoch-wise memorization counts in Figure 2.
- Report the Pearson correlation with per-dataset breakdown, number of points, and confidence intervals; add a sensitivity analysis of the 25% memorization threshold.
- Narrow the "memorization is not necessary for generalization" claim to be dataset- and architecture-specific, or provide additional evidence (e.g., analysis of the high-score tail).
- Consider a small-scale artificial memorization control experiment to directly confirm the contrast.
