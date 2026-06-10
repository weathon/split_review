Here is my final consolidated review.

## Summary

This paper studies how model scale affects performance on large-scale multi-spectral remote sensing segmentation. It introduces a Spectral Dependency Module (SDM) — channel-wise self-attention over spectral bands — integrated into a Swin Transformer to form the Multi-Spectral Swin Transformer (MS-Swin). The paper evaluates four model families (ResNet, UNet++, Swin, MS-Swin) at sizes from ~1M to ~655M parameters on the Biological Valuation Map (BVM) of Flanders, a large densely-labeled Sentinel-2 dataset. The headline result is that MS-Swin at 655M parameters achieves >95% accuracy while UNet++ at 23M achieves <65% accuracy.

## Strengths

- **Clear formulation of the Spectral Dependency Module (SDM).** The module is precisely described (Equations 6–10, Figure 2). It computes C×C attention matrices across spectral bands for each spatial patch, enabling direct modeling of inter-band dependencies. The paper correctly distinguishes this from prior spectral-attention methods (Hang et al. 2021, Roy et al. 2021, Zhong et al. 2022) which use CNN-based sparse spectral correlation rather than token-to-band reformulation.

- **Empirical coverage across multiple model families and scales.** The paper systematically evaluates ResNet (1M–2800M params), UNet++, Swin Transformer, and MS-Swin variants across orders of magnitude in parameter count on a single large-scale multi-spectral dataset. This goes beyond the typical single-model-per-dataset paradigm in remote sensing (Section 2.2), and the results showing that small models saturate early while large models continue improving are informative.

- **Model-dataset size matching analysis.** Section 4.1 (Figure 7, Table 3) varies training data volume alongside model size, showing that small models perform comparably to large ones on limited data but saturate early, while large models realize their advantage only with sufficient data. This provides actionable guidance for practitioners.

## Weaknesses

### Major

- **Overall Accuracy (OA) is insufficient as the sole evaluation metric for land-cover segmentation.** The paper uses only OA (line 128), without reporting mIoU, F1-score, or per-class accuracy. For land-cover mapping with potentially imbalanced class distributions — which is the case for biological valuation maps — OA can be dominated by majority-class performance and may mask poor performance on rare but important classes. This is a standard concern in remote sensing (ISPRS Vaihingen, ISPRS Potsdam, LoveDA benchmarks all use mIoU as primary metric). Without per-class metrics, the headline claim that MS-Swin achieves >95% accuracy while UNet++ achieves <65% cannot be properly evaluated — the gap could be largely driven by differential performance on a single dominant class. This undermines the quantitative foundation of the paper's main result.

- **The scaling efficiency coefficient S is not properly defined.** The paper defines S = -1/log(G/(P×C)) (Equation 11) and names G as "Performance Gain Factor," P as "Parameter Count Scaling Factor," and C as "Computation Increase Factor" — but never specifies what baselines these factors are normalized against, how they are computed in practice, or what their numerical ranges are. Without this information, the reported scaling coefficients (used throughout Section 4 and Figure 6) are uninterpretable. The mathematical form also has the quirk that if G/(P×C) > 1 the log is positive and S becomes negative, while if the fraction < 1, S is positive — but the paper does not clarify which regime applies. This metric needs either a complete specification with examples or should be replaced with standard efficiency measures (accuracy/param, accuracy/FLOP).

- **Ablation of the Spectral Dependency Module is insufficient.** The only evidence for SDM's contribution is a single comparison: MSSwint (92.25%) vs. Swint (91.34%) — a 0.91% gap (line 217). This comparison is not a controlled ablation because the models have different parameter counts (SDM adds parameters). There is no comparison at matched parameter counts, no ablation testing SDM insertion at different stages (only stage 1 is tested), no comparison against existing spectral-attention methods (Hang et al., Roy et al., Zhong et al.), and no statistical significance or variance estimates. The 0.91% improvement could partially or fully reflect the additional parameters rather than the SDM mechanism itself.

### Minor

- **Training details insufficient for reproducibility.** The paper states optimizer (Adam) and hardware (4×A100-80G), but omits learning rate, learning rate schedule, weight decay, batch size, gradient accumulation steps, number of training epochs/iterations, patch size/grid size/sampling strategy, and data splits (train/val/test). These omissions make independent reproduction difficult.

- **UNet++ and ResNet multi-spectral adaptation is unspecified.** Sentinel-2 data has 13 spectral bands. The paper never states how these RGB-origin architectures (UNet++, ResNet) are adapted to handle multi-spectral input — whether the first convolution layer is modified to accept 13 input channels, or only 3 RGB-equivalent bands are used. This is essential for interpreting the cross-architecture comparison.

- **"Scaling laws" terminology is overclaimed.** The paper cites Kaplan et al. (2020) and calls itself a "scaling law study" but only tests a handful of model sizes at discrete points, without fitting parametric power-law relationships between compute/data/model size and performance. A more accurate description would be an "empirical scaling study" rather than a "scaling law" analysis.

- **Headline cross-architecture comparison conflates multiple factors.** The paper's headline result (UNet++ 23M @ <65% vs. MS-Swin 655M @ >95%) is presented as evidence that "models many orders of magnitude larger lead to substantial improvements." But this comparison varies architecture family (CNN vs. Transformer), parameter count (23M vs. 655M), and the presence of SDM simultaneously. While within-family scaling (Swin small→large, ResNet small→large) partially addresses this, the headline framing over-attributes the gap to scale alone.

### Trivial

None.

## Nice-to-Haves

- Reporting confidence intervals or standard deviations across multiple runs would strengthen the reliability of the comparisons.
- Testing SDM on additional large-scale multi-spectral datasets would improve generalizability beyond the Flanders region.
- Comparing against existing spectral-attention methods (Hang et al., Roy et al., Zhong et al.) under the same training setup would better establish SDM's contribution.

## Removed Points

These points from the inputs were removed with justification:

- *"Figures/images not extractable by parser"* — This is a PDF parsing artifact, not a paper issue. The original submission contains the figures.
- *"Missing appendix content"* — Appendices are stripped by the parser; they exist in the original submission.
- *"The SDM is straightforward and not novel"* — Simplicity is not a flaw. The SDM is a clean formulation of channel-wise attention; the claim that it's "not novel" is subjective and not a verifiable weakness.
- *"Missing related works"* — Not verifiable without external sources; the paper does cite relevant prior spectral-attention work.
- *"Scaling law study requires more sizes for power-law fitting"* — While the paper could have tested more sizes, the existing evaluation across orders of magnitude is substantial. This is subsumed into the "overclaimed terminology" minor weakness.
- *Strength Finder's "scaling efficiency coefficient" strength* — Removed because this conflicts with the verified weakness that S is ill-defined.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any perspective on the paper that goes beyond what the paper itself states.

## Suggestions

1. **Report mIoU and per-class accuracies** alongside or in place of OA. This is the single most impactful change — without it, the headline accuracy numbers cannot be trusted for land-cover segmentation.

2. **Fully specify the scaling coefficient S**: define the baselines and normalization for G, P, and C with concrete examples. Alternatively, replace S with standard efficiency metrics (accuracy/parameter, accuracy/FLOP) that readers can immediately interpret.

3. **Conduct a proper SDM ablation**: compare MS-Swin vs. vanilla Swin at identical parameter counts (by adjusting Swin's depth/width), with multiple random seeds. Test SDM at different insertion stages.

4. **Specify all training hyperparameters** (learning rate, schedule, weight decay, batch size, epochs, patch size, data splits) for reproducibility.

5. **Clarify how UNet++ and ResNet were adapted** to multi-spectral input (13-channel first convolution or 3-channel subset). If only RGB bands were used, acknowledge this as a limitation.

## Score and Decision

The paper addresses a relevant question and makes a reasonable architectural contribution in the SDM, while providing the most extensive empirical scaling study to date on a large multi-spectral remote sensing dataset. However, the evaluation is undermined by (a) the use of OA as the only metric, which is insufficient for land-cover segmentation, (b) an ill-defined scaling coefficient used throughout the results, and (c) an insufficiently controlled SDM ablation. These are structural issues that prevent the evidence from fully supporting the claims. The paper could be substantially strengthened with targeted revisions.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>