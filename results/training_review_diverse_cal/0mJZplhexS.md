Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper investigates how scaling up image classifiers interacts with sample difficulty and proposes Little-Big, a simple two-pass inference algorithm: a lightweight "Little" model screens all samples, and only low-confidence predictions are forwarded to a "Big" model. The core finding is that scaled-up models disproportionately correct low-confidence mistakes made by smaller models. The method achieves substantial MACs reductions (62–81%) without accuracy degradation across CNNs (EfficientNet), transformers (DeiT3, ViT), and hybrid models (EfficientViT, InternImage) on ImageNet-1K, and generalizes to ImageNet-ReaL and ImageNet-V2 with negligible accuracy loss.

## Strengths

1. **Simple, practical, model-agnostic method with strong empirical results**: Little-Big requires no retraining, architectural changes, or gradient access. It achieves 81% MACs reduction for EfficientNet-B7-600, 76% for EfficientViT-L3-384, 71% for DeiT3-L-384, and 62% for InternImage-G-512 while maintaining or exceeding baseline top-1 accuracy (Abstract, Table 1). These results span CNN, transformer, and hybrid families.

2. **Well-motivated by the scaling inefficiency analysis**: The paper quantitatively demonstrates that scaled-up models provide marginal accuracy gains at disproportionate compute cost (e.g., EfficientViT-L3-384: <2% improvement over L1-224 at 14× MACs). Section 3 bins predictions by Little model confidence and shows that >90% of correctable mistakes occur at low confidence (below 0.65/0.67/0.47 for three EfficientNet pairs), directly supporting the H2 hypothesis that scaling helps with hard samples.

3. **Robust generalization of the threshold selection**: The operating threshold T=0.24 selected on ImageNet-1K transfers to ImageNet-ReaL (0.04% drop) and ImageNet-V2 (0.07% drop). Warm-starting from the smaller V2 set (10K samples) produces a threshold yielding 78% speedup on ImageNet-1K (Section 4.2), showing the method is robust to distribution shift and limited calibration data.

4. **Favorable comparison to compression baselines**: The paper compares against pruning methods (WDPruning, X-Pruner, SPViT) and adaptive-compute methods (DynamicViT, A-ViT), showing that Little-Big achieves superior Pareto points on accuracy vs. MACs without the need for retraining or distillation (Table 2).

5. **Honest treatment of limitations**: The paper acknowledges storage overhead from the second model and discusses mitigation strategies (loading one model at a time, batching), grounding the method in real-world deployment considerations.

## Weaknesses

### Fatal

None.

### Major

1. **The decomposition analysis that motivates the core claim is shown for only one model family.** Section 3 presents the confidence-binned breakdown of correctable vs. non-correctable mistakes exclusively for EfficientNet (B0/B2/B4 paired with B7). The paper frames the claim that "scaling up helps with hard samples" (H2) as a general phenomenon, but the direct evidence for this is limited to one CNN family. The method does demonstrably work across other families (EfficientViT, DeiT3, ViT, InternImage) in terms of downstream MACs reductions, but the *analytical foundation* — showing that the Big model preferentially corrects low-confidence Little mistakes — is not extended to any transformer or hybrid pair. This weakens the paper's own narrative that the property is a general scaling phenomenon rather than something specific to EfficientNet's calibration behavior. Adding even one similar decomposition (e.g., an EfficientViT or DeiT3 pair) would significantly strengthen the paper's analytical grounding.

### Minor

2. **Accuracy-MACs trade-off curves are shown for only one Big model (EfficientNet-B7).** Section 4.2 provides detailed accuracy-MACs curves (Figure 4, bottom row) for EfficientNet-B7 with various Little companions. For other model families, only summary MACs reduction numbers are given in Table 1. The reader cannot visually inspect the shape of the trade-off or verify that the threshold selection method (leftmost intersection with target accuracy) applies cleanly for transformer-based families where calibration properties may differ. This is a presentation gap rather than a fatal flaw, since the summary results are clear.

3. **The fraction of non-correctable vs. correctable mistakes is not numerically reported.** Section 3 shows both categories in bar charts (Figure 3), but the paper never states what fraction of total Little mistakes are non-correctable (i.e., mistakes the Big model also gets wrong). This number bounds the best possible accuracy improvement from using the Big model at all and would sharpen the analysis. It is implicitly visible in the bar charts but not explicitly reported.

4. **The relationship between confidence thresholds for the decomposition analysis and the operating threshold for deployment is not fully explained.** Section 3 reports that 90% of correctable mistakes fall below confidence 0.65/0.67/0.47, while the operating threshold for lossless compression is T=0.24 (for B4+B7). These are different quantities — the former is a descriptive statistic about mistake distribution, the latter is determined from accuracy-MACs curves. A reader might reasonably wonder: if only 10% of correctable mistakes lie above 0.47, and the threshold is set at 0.24, then many correctable mistakes (those between 0.24 and 0.47) are passed to the Big model and corrected. The paper does not explicitly walk through this logic or quantify how the threshold affects which correctable mistakes are caught versus missed.

5. **Calibration mismatch between model families is not discussed.** The method relies on max softmax probability as a reliable proxy for hardness. ViTs are known to have different calibration properties from CNNs in some settings. While the empirical results confirm the method *works* for ViTs, the paper does not discuss whether the threshold selection or the correctable-mistake distribution would differ for ViT-based pairs. A brief discussion would strengthen the analysis.

### Trivial

None.

## Nice-to-Haves

- Extending the decomposition analysis (Figure 3 style) to at least one transformer or hybrid family (e.g., DeiT3-Small+Large or EfficientViT-L1+L3).
- Accuracy-MACs trade-off curves for a representative non-EfficientNet pair (e.g., ViT or DeiT3) in the main paper.
- Reporting the fraction of total Little mistakes that are non-correctable for each pair in Table 1.

## Removed Points

- **Criticism about missing comparison to cascade/early-exit methods**: The paper discusses early-exit mechanisms (dynamic token reduction, token halting) in Section 2.3 and compares against DynamicViT and A-ViT in Table 2. The claim that the paper does not compare to any cascades is factually incorrect. *Removed as factually wrong.*
- **Criticism that "no loss of accuracy" conflates two effects without analysis**: The paper's threshold selection method explicitly finds the leftmost intersection with the Big model's accuracy line, which by construction preserves accuracy. The specific mechanism (some correctable mistakes missed, but Big model compensates) is a natural consequence of the accuracy-matching design, not a flaw. *Removed as the paper already addresses the underlying concern through its method design.*

## Novel Insights

The most insightful observation from the reviews is that the paper's two key claims — (a) scaling helps with hard samples, and (b) the method works across families — are supported by evidence at different levels of directness. Claim (a) is supported by detailed decomposition for one CNN family; claim (b) is supported by downstream MACs numbers across families. While both claims are adequately supported to make the paper's contribution credible, closing this evidence gap would make the paper structurally tighter. The reviewers consistently identified this asymmetry, which is a genuine and correctable weakness rather than a misunderstanding.

## Suggestions

1. Add one decomposition figure (Figure 3 style) for a non-CNN pair — e.g., EfficientViT-L1 + EfficientViT-L3 or DeiT3-S + DeiT3-L — to directly demonstrate that the "scaling helps with hard samples" pattern holds beyond EfficientNet.
2. Include accuracy-MACs trade-off plots for at least one additional Big model (e.g., EfficientViT-L3 or DeiT3-L) so readers can visually verify the threshold selection procedure for a transformer-family model.
3. Add a brief discussion of calibration differences across model families (CNNs vs. ViTs) and whether they affect the threshold selection or the correctable-mistake distribution.

---

**Originality**: The paper offers a clean, simple insight (scaling inefficiency → two-pass filtering) that is surprisingly effective. The contribution is practical rather than theoretical.

**Quality of Research Question**: Well-motivated. The observation that scaled-up models waste compute on easy samples is simple but important.

**Claims Support**: The central claim (method achieves large speedups without accuracy loss) is well supported. The supporting claim (scaling helps with hard samples) has narrower direct evidence but is reasonable.

**Soundness**: Experiments are well-designed across multiple model families, scales, and datasets. The generalization tests (ImageNet-ReaL, ImageNet-V2, warm-start from small set) are a strong addition.

**Clarity**: Clearly written. The algorithm is simple and well-explained. The figures (where present) are effective.

**Value**: High practical value. The method is immediately usable with any off-the-shelf pretrained models.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>