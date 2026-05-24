Now I have all the information needed to produce the consolidated review. Let me construct it carefully.

---

## Summary

This paper argues that evaluating OOD robustness at a single (or very few) fixed degrees of distribution shift can produce misleading conclusions. Through controlled experiments on NoisyMNIST, RotatedMNIST, LowLightCIFAR10, and ImageNet-derived datasets, the authors demonstrate three phenomena: (1) models that excel under mild shifts can collapse under slightly stronger shifts of the same type; (2) training on strong shifts does not guarantee robustness to milder shifts and can even harm performance; (3) CLIP models adapted via linear probing are disproportionately brittle to downstream shifts that are rare in their pre-training data. The paper makes a useful methodological point about evaluation practice in OOD generalization.

## Strengths

- **Models that perform best under mild shifts collapse under slightly stronger shifts of the same type.** Figure 2 (left) and Table 1 quantify this systematically: e.g., on NoisyMNIST, the top-5 models at D₄ drop >10% at D₅ (only slightly more noise). VREx on ResNet-50 shows a 50.3% relative drop from D₄ to D₅. This provides direct evidence that robustness at one degree does not extrapolate to the next, a finding that single-degree benchmarks cannot surface.

- **Training on strong shifts can harm rather than help performance on milder shifts, and the effect is task-dependent.** Figure 3 shows that on RotatedMNIST, ERM trained on the clean domain plus the strongest rotation (0 & 10) performs *worse* on mild rotations than models trained only on clean data. On LowLightCIFAR10, training on the strongest shift degrades even clean-domain accuracy. This contradicts the intuitive assumption that extreme-shift exposure produces generally robust models.

- **The paper demonstrates the brittleness phenomenon across multiple datasets (NoisyMNIST, RotatedMNIST, LowLightCIFAR10, NoisyImageNet15, LR-ImageNet15), multiple architectures (4-layer CNN, ResNet-50, EfficientNet, ViT), and multiple DG algorithms (ERM, Mixup, CAD, VREx, IRM, etc.).** This breadth reduces the concern that the pattern is an artifact of a single setup.

- **GradCAM visualizations provide a mechanistic explanation for the brittleness.** They show that ERM relies on local features that degrade quickly under noise, while CAD uses more global structures that degrade more gradually, connecting the performance pattern to underlying feature use.

## Weaknesses

### Fatal
None.

### Major

- **The claim that findings "also hold for more general problems" (§3) is unsupported.** The paper's empirical evidence is entirely on synthetic or simulated shifts (Gaussian noise, rotation, brightness/shot-noise combinations, resolution reduction). While these controlled experiments cleanly demonstrate the brittleness phenomenon, no experiment involves a naturalistic, high-dimensional distribution shift (e.g., background change, style transfer, subpopulation shift). The paper's core methodological point — that single-degree evaluation can be misleading — is well-supported by the synthetic evidence, but the broad framing overstates the demonstrated scope. The paper would benefit from either (a) including at least one realistic shift benchmark with multiple severity levels, or (b) transparently scoping the claims to synthetic shifts and discussing generalizability as future work.

### Minor

- **The CLIP vs. randomly-initialized (RI) comparison on NoisyMNIST stacks multiple uncontrolled factors.** CLIP models are adapted via linear probing (frozen features, shallow classifier), while RI models are trained end-to-end from scratch on the full task. These differ in the amount of task-specific training, the optimization procedure, and the adaptation strategy. The paper's own commented-out paragraph (line 310–313) acknowledges that fine-tuning CLIP "significantly outperforms training from scratch and linear probing," but this result is not presented. Consequently, the claim that CLIP is "sensitive to minute shifts" is partly confounded with the linear probing adaptation method. The controlled comparison on NoisyImageNet15/LR-ImageNet15 is cleaner and should be foregrounded.

- **The left panel of Figure 2 selects the top-5 models that perform best on each specific domain independently.** This design shows that *different* models are best at different degrees (an interesting finding about model diversity), but it is weaker than the fixed-criterion evaluation in Table 1 and the right panel of Figure 2 for demonstrating that an *individual* model's robustness is brittle. The paper already provides the stronger evidence elsewhere, but the framing of the left panel could create confusion.

- **No explicit discussion of limitations.** The paper does not include a limitations section or discuss the extent to which the synthetic-shift results may or may not transfer to natural distribution shifts. Adding one would improve the paper's scientific rigor.

### Trivial
None.

## Nice-to-Haves

- Show full distributions of model performances (e.g., scatter plots or violin plots of accuracy at D₄ vs. D₅ for all trained models) rather than only top-k averages. This would reduce any selection-bias concern and strengthen reader confidence in the patterns.
- Include the fine-tuning results for CLIP (alluded to in the commented-out paragraph) to disentangle whether the brittleness is due to pre-training or the linear probing adaptation method.
- Add a realistic distribution-shift benchmark with multiple severity levels (e.g., an ImageNet variant with graded natural corruptions or a subpopulation shift with multiple confound strengths) to bridge the gap between synthetic demonstrations and real-world relevance.

## Removed Points

The following criticisms from the reviews were removed per policy:

- **Missing experimental details / reproducibility concerns (appendix content, CNN architecture specifics, complete list of 20 DG algorithms, hyperparameters):** These details were likely in the appendix, which is stripped by the parser. The original submission would contain them.
- **No statistical inference / confidence intervals / hypothesis tests:** Standard deviations are reported in Table 1. Requesting hypothesis tests for large-effect-size comparisons is a generic methodological preference, not a specific flaw.
- **Degree of shift not independently quantified:** The paper uses ordinal labeling, which the critic acknowledges is "acceptable for an empirical study." This is a non-criticism.
- **Pure formatting/style nitpicks:** Removed per policy.
- **Several generic "could this be a confound?" speculations** from the harsh critic's area sweep that lack specific anchoring to paper content.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface genuinely novel observations about the paper. The harsh critic's reading largely confirms the paper's findings while raising reasonable scope limitations. One insight worth noting: the contrast between NoisyMNIST (where training on strong shifts helps milder shifts) and RotatedMNIST (where it hurts) is a genuinely non-obvious finding that the paper documents well, and the reviewer correctly highlights this as particularly illuminating. The GradCAM-based mechanistic explanation linking local vs. global feature reliance to the brittleness pattern is also a distinctive contribution that goes beyond pure accuracy reporting.

## Suggestions

1. **Scope the claims more carefully.** Replace the unsupported statement that conclusions "also hold for more general problems" (§3) with a clear limitations paragraph that acknowledges the synthetic nature of the shifts and discusses which types of real-world shifts the pattern is likely (or unlikely) to transfer to.
2. **Foreground the NoisyImageNet15/LR-ImageNet15 results** in the CLIP discussion and either include the fine-tuning experiments or reframe the MNIST-based CLIP claim as a case study about domain mismatch between pre-training and downstream shifts.
3. **Add one realistic shift case study** (e.g., a natural corruption benchmark or a subpopulation shift with graded severity) if space permits; otherwise clearly bound the claims to controlled settings.

## Score and Decision

The paper makes a solid empirical contribution to an under-explored aspect of OOD evaluation. The core phenomenon is cleanly demonstrated, the experiments are well-designed (with multiple datasets, architectures, and algorithms), and the findings have clear implications for evaluation methodology. The main weaknesses are the scope of claims relative to evidence (minor-to-moderate overclaim) and the confounded CLIP comparison. These are addressable with revisions. The paper does not have fatal flaws.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>