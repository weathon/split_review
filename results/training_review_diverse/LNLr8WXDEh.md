Now I have enough information to write the consolidated review. Let me compose it.

## Summary

This paper presents a systematic linear probing study of Stable Diffusion's internal representations across seven 3D scene properties: geometry (same/perpendicular plane), material, support relations, shadows, occlusion, and depth. Using a grid search over U-Net layers and diffusion timesteps with linear SVM classifiers, the authors find that decoder layers D₂/D₃ encode these properties well above chance, and that Stable Diffusion outperforms DINOv1/v2, OpenCLIP, and VQGAN on all properties tested.

## Strengths

- **Comprehensive and well-structured probing protocol across seven diverse 3D properties.** The paper defines a binary-question formulation for each property, repurposes five real-image datasets with ground-truth annotations (ScanNetv2, DMS, NYUv2, SOBA, Separated COCO), and applies a unified feature extraction and evaluation pipeline. This breadth is a genuine advance over prior work that typically probes one or two properties.

- **Actionable finding that optimal features consistently reside in the U-Net decoder (D₂/D₃ layers).** This is a practically useful insight: downstream tasks exploiting Stable Diffusion features can default to decoder layers rather than searching the full U-Net. The finding that material (a lower-level property) benefits from the nearer-to-output layer D₂ while properties requiring global reasoning favor D₃ is well-motivated and empirically supported.

- **Novel empirical result that Stable Diffusion's features encode support relations, shadows, and scene geometry with high AUC scores (e.g., 0.96 for support relations, 0.93 for shadows).** Even setting aside the comparative claims, the absolute performance of the linear probes on these tasks is notable and demonstrates that the model's representations carry substantial 3D physical information. The grid-search analysis (Table 2) revealing distinct optimal timesteps and layers per property is a genuine finding.

## Weaknesses

### Fatal
None.

### Major

- **The cross-model comparison (SD vs. DINO/CLIP/VQGAN) is underspecified to the point of being unverifiable.** Section 4.3 states that the protocol is applied "similar to Stable Diffusion" to ViT-based models, but it never describes how patch-level features from DINO/CLIP are processed for region pooling. For Stable Diffusion, the paper specifies: upsample dense U-Net features to image resolution with bilinear interpolation, then average-pool over region masks (Eq. 1–2). For ViT models, which produce a coarse grid of patch tokens (e.g., 14×14 or 16×16), it is unclear whether the authors (a) treat patch tokens as spatial features and upsample them similarly, (b) only use the CLS token, (c) interpolate attention maps, or (d) some other procedure. Because SD has much denser spatial features (the U-Net decoder produces feature maps at resolutions comparable to the input), any naive upsampling of ViT patch features would put DINO/CLIP at an inherent disadvantage — they literally cannot resolve region boundaries as finely. Without a transparent description of the feature extraction for each architecture, the central claim that "Stable Diffusion outperforms all the other models for all properties" (Section 4.4) rests on an incompletely documented methodology. This does not invalidate the SD-only results, but it substantially weakens the comparative conclusions.

- **No statistical uncertainty is reported for any result.** All AUC scores in Tables 2–4 are point estimates with no confidence intervals, standard deviations, or significance tests. Given that test sets vary in size (some capped at 1000 images) and the number of region pairs is not reported, it is impossible to assess whether observed differences (e.g., SD vs. DINOv1 on Shadow: 0.93 vs. 0.89) are reliable or within the noise of the evaluation. This is an evidential gap that reduces confidence in the quantitative comparisons that form a main contribution.

### Minor

- **Language overreach in framing.** The title asks "What Does Stable Diffusion Know about the 3D Scene?" and the paper frequently uses "understands" and "knowledge" (e.g., "Stable Diffusion can understand very well about scene geometry"). Linear probing measures whether a property is *linearly separable* in the representation space, not whether the model has causal understanding or uses this information during generation. While this is common framing in probing studies (and the abstract uses scare quotes around 'understands'), some claims could mislead readers into over-interpreting the results. Replacing "understands" with "encodes information about" or "linearly decodable" would better match the evidence.

- **Cross-property comparisons are confounded by different datasets and task formulations.** The "Occlusion" task (Separated COCO) is fundamentally harder than "Depth" (binary threshold on average depth) — the paper acknowledges this in passing in Section 5 but does not adjust interpretations when comparing AUC scores across properties. The claim that SD is "good at geometry, support, shadows, and depth but less performant at occlusion" could partly reflect dataset difficulty rather than the model's relative competence.

- **No low-level baseline for context.** The probing literature commonly includes a raw-pixel baseline (or shallow features like SIFT/HOG) to establish what performance is achievable from low-level image statistics alone. Without such a baseline, it is unclear how much of the probing performance reflects genuinely high-level 3D knowledge versus trivial cues (e.g., texture or color differences correlated with the property).

- **Region-pair counts not reported.** Table 1 shows only the number of images per split. Since each image yields many region pairs, the number of training/evaluation examples per property could vary substantially. Reporting pair counts and class balance (though the paper states it samples equally) would help readers interpret AUC scores.

### Trivial
- "Seperated COCO" (line 112) is a typo for "Separated COCO" (the dataset name).

## Nice-to-Haves
- A heatmap or compact table showing the full comparison across all properties and models in the main paper (Table 4 only shows 4 of 7 properties in the main text; the rest are deferred to the supplementary).
- An analysis of how performance varies across timesteps for a fixed layer (or vice versa) for key properties, to deepen understanding of why certain timesteps (e.g., 981 for Same Plane) work best.

## Removed Points

These points were flagged for removal; treat them with caution.

- *"The inpainting examples in Figure 1 are not connected to the probing experiments."* — The paper explicitly states (line 19) that these are "only for illustration and inpainting is not the objective of this paper." The probing experiments are a separate, systematic investigation; the illustrative examples are not claimed as evidence.
- *"The paper does not test whether using both symmetric and asymmetric inputs jointly would improve results."* — This is an experimental choice, not a weakness. The symmetric/asymmetric split is theoretically motivated (Section 3.3) and testing every combination is not required.
- *"The paper does not explore the worst layers or provide an ablation showing the range of performance across layers."* — The paper reports the best layer found via grid search, which is standard for probing studies. Reporting worst-case performance is not a standard requirement.

## Novel Insights

None beyond the paper's own contributions. The reviewers' concerns center on methodology transparency and statistical rigor rather than any conceptual reframing of the problem. The most useful insight from the review process is the recognition that probing comparisons across architectures with fundamentally different spatial resolutions (dense U-Net vs. patch-based ViT) require careful methodological alignment to ensure fair comparison — a consideration this paper currently treats too casually.

## Suggestions

1. **Describe the full feature extraction pipeline for all compared models in the main paper** — specifically how patch-level ViT features are pooled over region masks, whether upsampling is used, and at what resolution. If the supplementary already contains this detail, reference it clearly. Ideally, include a controlled experiment comparing SD features at ViT-comparable spatial resolution to isolate the effect of resolution from the effect of representation quality.

2. **Add bootstrapped 95% confidence intervals to all reported AUC scores**, or at minimum report results from multiple runs with standard deviations. This is essential for readers to assess whether the observed gaps between models are meaningful.

3. **Calibrate the language**: replace "understands" and "knows" with "encodes information about" or "is linearly decodable for" throughout, except where scare quotes or the title's rhetorical framing make the intent clear.

4. **Include a simple baseline** (e.g., raw RGB pixel differences with the same SVM protocol) to contextualize the probing results and demonstrate that the performance stems from high-level representation rather than low-level image statistics.

## Score and Decision

The paper makes a solid empirical contribution by systematically probing Stable Diffusion's representations across a broad set of 3D properties. The core findings — that decoder layers D₂/D₃ encode geometry, support relations, shadows, and depth well above chance, and that the optimal timestep/layer varies per property — are novel, well-supported, and practically useful. However, the comparative claim against DINO/CLIP/VQGAN is weakened by an underspecified methodology that does not describe how architectural differences in feature resolution were handled, and no statistical uncertainty is provided for any result. These weaknesses are fixable in revision and do not invalidate the paper's main contribution, but they must be addressed before the comparative conclusions can be trusted.

**Originality**: Good — applies probing methodology to diffusion models for 3D scene understanding at this breadth for the first time. **Importance**: High — understanding what generative models encode informs downstream usage. **Claims well supported**: Partially — the SD-only claims are well supported; the comparative claims are not due to underspecified methodology. **Soundness**: Adequate for the SD protocol, but the cross-model comparison needs proper documentation. **Clarity**: Generally clear, though the comparison methodology is vague. **Value to community**: Valuable — the probing protocol and findings about optimal layers/timesteps are directly usable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>