Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes PointMIL, a framework that applies Multiple Instance Learning (MIL) to point cloud classification to obtain inherent local (point-level) interpretability without post-hoc methods. It introduces a contextual attention mechanism that smooths attention weights via k-nearest neighbors, evaluates four MIL pooling strategies, and demonstrates the approach across five point cloud backbones (PointNet, DGCNN, CurveNet, PointMLP, PointNeXt) plus a custom Transformer on four datasets (IntrA, RBC, ModelNet40, ShapeNetPart). The paper shows that PointMIL can improve both classification accuracy and interpretability over base backbones, with particularly strong results on biomedical datasets.

## Strengths

1. **Novel application of MIL for inherent local interpretability in point clouds.** The paper is the first to apply Multiple Instance Learning to point cloud classification for producing fine-grained, point-level, class-specific explanations as part of the model itself rather than through post-hoc methods. The related work section convincingly establishes the gap: existing inherently interpretable point cloud methods (XPCC, Interpretable3D) are global/prototype-based and do not provide point-level explanations.

2. **Contextual attention mechanism with demonstrated benefit.** The proposed neighbourhood-aware attention smoothing (Section 3.3) is simple yet effective. The ablation study (Figure 8) shows that including contextual attention consistently improves both classification metrics (F1, mACC) and interpretability metrics (AOPCR, NDCG@n) across pooling methods, with the best results at k=12. This is a clear technical contribution.

3. **Extensive evaluation across diverse backbones and datasets.** PointMIL is evaluated with five distinct backbones (PointNet, DGCNN, CurveNet, PointMLP, PointNeXt) plus a custom Transformer on four datasets spanning biomedical shapes and everyday objects (Tables 1-3). This breadth provides strong evidence of generality.

4. **Quantitative interpretability evaluation with established metrics.** Rather than relying only on qualitative visualizations, the paper uses AOPCR and NDCG@n to compare PointMIL's explanations against CLAIM and PSM across multiple backbones (Table 1), with perturbation curves providing complementary evidence (Figures 2, 5, 6).

5. **Segmentation validation as a faithfulness check.** Using point-level interpretations as segmentation masks and evaluating against ground-truth labels (Section 5.4, Table 3) provides a direct empirical test of whether the interpretations align with semantically meaningful point labels — an approach that directly addresses the well-known attention-faithfulness concern.

## Weaknesses

### Fatal
None.

### Major

1. **SOTA claim on IntrA and RBC is not substantiated against prior published results.** The paper claims "state-of-the-art" performance on IntrA (mACC 97.3%, F1 97.5%) but Table 2 compares only against generic point cloud backbones (PointNet, DGCNN, CurveNet, PointMLP, PointNeXt, PCT, 3DMedPT) and does not include results from the original IntrA paper (Yang et al., 2020) or any other prior work that has published classification numbers on these datasets. The original dataset paper is cited only for the dataset itself, not for its reported performance. Without comparison to existing published results on IntrA and RBC, the SOTA claim is unverifiable. The paper's contribution — improved interpretability with competitive or improved accuracy — does not depend on being SOTA, so this overclaim is a framing issue rather than a foundational flaw, but it is a significant one that needs correction.

2. **CLAIM and PSM adaptation details are underspecified, potentially affecting fairness of the interpretability comparison.** The paper compares PointMIL's interpretability against CLAIM and PSM on multiple backbones (Table 1) but does not describe how these post-hoc methods — originally designed for PointNet-style architectures — were adapted to work with DGCNN, CurveNet, PointNeXt, or the Transformer backbone. CLAIM relies on global average pooling (GAP) and projects classifier weights onto point features; PSM uses gradient-based saliency. How these operations work when the backbone uses different pooling strategies, downsampling, or concatenation of local/global features is not explained. This methodological gap makes the comparison difficult to reproduce and raises questions about fairness. The paper should detail any modifications made or acknowledge limitations of the adaptation.

### Minor

1. **Transformer backbone architecture is underspecified.** The paper states "we follow much of the Transformer block from Yu et al. (2021)" but does not provide specific architectural parameters (number of layers, embedding dimension, number of attention heads, MLP hidden dimensions, etc.). While citing the original architecture is a reasonable starting point, the paper's own claims of introducing "a new transformer-based model" (Contribution 2) require sufficient detail for independent implementation. The modifications from Yu et al. (2021) — removing point sampling and multi-graph reasoning — are described at a high level but the resulting architecture is not fully specified.

2. **No variance or confidence intervals reported.** The paper does not report standard deviations or multiple-run statistics for any experiment, including on small datasets (IntrA, RBC) where variance could be meaningful. This limits the ability to assess the reliability of the reported improvements, particularly for the interpretability metrics in Table 1.

3. **Segmentation claim about "not deteriorating" is overly broad.** The paper states "the segmentation results did not deteriorate and sometimes improved" but then immediately acknowledges that "the only exception was 3DMedPT on ShapeNetPart, where the original 3DMedPT outperformed POINTMIL with the transformer backbone by a relatively larger margin" (Cls. IoU 81.2 vs. 79.8, Inst. IoU 83.5 vs. 81.2). This is a clear and non-trivial deterioration that the paper should discuss more carefully rather than treating as a minor exception. The framing should be adjusted to accurately reflect the pattern of results.

4. **Perturbation analysis is qualitative.** The perturbation curves (Figures 2, 5, 6) are presented qualitatively without summarizing statistics (e.g., area under the perturbation curve, multiple runs). While the visual trend is informative, the analysis would benefit from quantitative aggregation.

5. **No discussion of why Conjunctive outperforms Additive pooling.** Both produce class-specific, attention-weighted point predictions, yet Conjunctive is recommended for interpretability. The paper speculates about independence of the attention and classification heads but provides no analysis (gradient flow, optimization landscape) explaining the performance gap.

### Trivial
None.

## Nice-to-Haves
- A code release commitment would significantly aid reproducibility given the underspecified architecture details.
- GPU runtime measurements for different k values in contextual attention would help readers assess the O(N²) time complexity trade-off mentioned in the ablation.
- An explicit statement of the number of classes in IntrA (two: Aneurysm vs. Normal) and that interpretability ground truth is available only for the Aneurysm class would aid readers (the annotation limitation is mentioned for segmentation but could be clearer for classification).
- Error analysis on why certain backbones (e.g., PointNet) produce worse interpretability, beyond the speculative explanation given.

## Removed Points
These points were raised by reviewers but are flagged to be removed or downgraded; treat them with caution:

- **"Adapted baseline for CurveNet/PointMLP not reported"** — Removed as factually incorrect. The paper states "Adapted architectures without farthest point sampling results are shown with a †" (Table 2 caption), confirming both original and adapted results are shown. The reviewer overlooked this.
- **"Paper does not mention IntrA has only two classes / annotation limitation"** — Removed as partially incorrect. The paper explicitly states "For IntrA, only the Aneurysm class contains annotations" (line 249).
- **"No comparison against global inherently interpretable methods (XPCC, Interpretable3D)"** — Removed as scope creep. The paper is about *local* interpretability. A quantitative comparison against global methods would not illuminate the paper's claims.
- **"ModelNet40 underperformance"** — Removed as mischaracterization. The paper explicitly acknowledges that POINTMIL is outperformed by SOTA methods on ModelNet40 ("While POINTMIL was outperformed by recent SOTA methods like PointMLP..."), and frames the "not harming" claim relative to the same backbone, not against SOTA. The paper is transparent about this.
- **"Missing code/data availability statement"** — Moved to Nice-to-Haves. This is valuable but not a core weakness.
- **"Comparison with additional post-hoc methods"** — Moved to Nice-to-Haves. The paper already compares against two established baselines; requesting more is a wishlist item.

## Novel Insights
The most interesting observation emerging from these reviews is that the segmentation validation (Section 5.4) is arguably the paper's strongest piece of interpretability evidence — stronger than the AOPCR/NDCG numbers against CLAIM/PSM — but it is not framed as such. By using point-level interpretations directly as segmentation masks and evaluating against ground-truth labels, the paper performs a direct faithfulness test of the kind that is rare in the interpretability literature and that directly addresses the attention-faithfulness critique (Jain & Wallace, 2019). The paper currently treats this as a secondary experiment ("segmentation results did not deteriorate") rather than as primary evidence for interpretation quality.

## Suggestions
1. In the revised version, either (a) compile and include prior published results on IntrA and RBC to substantiate the SOTA claim, or (b) remove the SOTA language and reframe the contribution as "competitive performance with state-of-the-art interpretability."
2. Provide a clear description of how CLAIM and PSM were adapted for each non-PointNet backbone, including any modifications to handle different pooling/architecture designs.
3. Specify the Transformer backbone architecture parameters (layers, dimensions, heads) in the main text or appendix.
4. Reframe the segmentation results: explicitly position them as a faithfulness test for the interpretations, report results on all backbones, and discuss the 3DMedPT exception honestly rather than as a parenthetical aside.
5. Report standard deviations across multiple runs (at least 3 seeds) for all main metrics, especially on the smaller biomedical datasets.

## Score and Decision

This paper makes a genuine contribution by adapting MIL to point cloud classification for inherent local interpretability, with a useful contextual attention mechanism and thorough empirical evaluation across backbones and datasets. The core novelty is real — the paper's claim of being first to apply MIL for this purpose is well-supported by the related work analysis — and the experimental evidence for improved interpretability (especially the segmentation faithfulness test) is compelling.

The two major weaknesses — the unsupported SOTA claim and underspecified CLAIM/PSM comparison — do not invalidate the paper's core contribution but do need to be addressed before publication. Both are fixable with additional comparisons and methodological clarifications rather than requiring new experiments. The minor issues (architecture specification, variance reporting, imprecise framing) are standard revision items.

Given the genuine novelty, the breadth of validation, and the fact that the major issues are addressable rather than structural, the paper merits acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>