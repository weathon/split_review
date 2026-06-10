## Summary

This paper proposes a unified framework for 4D (3D + time) human video stylization that simultaneously handles style transfer on original views, novel view synthesis, and human animation — a capability no prior method offers. It represents the dynamic human and static scene with two separate NeRFs using a geometry-guided tri-plane representation, and performs stylization in the rendered feature space via AdaAttN rather than on rendered RGB frames. The paper's core claim is that this unified feature-space approach achieves a better balance of stylized textures and temporal coherence than two-stage alternatives (NeRF reconstruction followed by 2D video stylization).

## Strengths

- **First unified framework enabling a genuinely new capability.** Tables 0(a) and 0(b) systematically show that no existing method — whether 2D video stylization (LST, AdaAttN, CCPL) or NeRF-based stylization (StylizedNeRF, Style3D, StyleRF) — can simultaneously handle stylized original views, novel views, and animated humans from a monocular video. This is a concrete and well-documented novelty.

- **Unified feature-space stylization consistently beats the two-stage pipeline.** Table 5 shows that stylizing in NeRF-rendered feature space (0.165/0.214) outperforms NeRF reconstruction followed by 2D video stylization from LST (0.185/0.248), AdaAttN (0.179/0.267), and CCPL (0.261/0.321) on both datasets. This directly supports the paper's central thesis and is its strongest experimental result.

- **Geometry-guided tri-plane provides a measurable improvement over vanilla tri-plane.** Table 6 reports 0.182 vs. 0.207 warping error, and Figure 2 visually demonstrates sharper background textures and contours. The improvement is modest but verifiable.

## Weaknesses

### Major

- **The quantitative evaluation measures only temporal consistency, leaving "stylized textures" — half of the claimed "superior balance" — unmeasured.** Every quantitative table (Tables 1–4) reports only warping error (masked LPIPS between flow-warped frames). There is no quantitative metric for style quality: no style loss against the target style image, no CLIP-based style similarity, no FID, no per-preference breakdown from the user study isolating style fidelity. A method could win on temporal consistency by producing blurry, under-stylized frames, and the current evaluation would not detect this. The paper's headline claim of a "superior balance between stylized textures and temporal coherence" (abstract, line 8; contributions, line 34) cannot be assessed from quantitative evidence that only addresses one of the two dimensions. Qualitative comparisons (Figure 3) partially compensate, but a quantifiable style quality metric is standard for style transfer papers and is conspicuously absent.

### Minor

- **Results on original-view stylization are mixed but the paper does not acknowledge this.** On "Our dataset" (Table 1), AdaAttN achieves better warping error (0.161) than the proposed method (0.165). The paper consistently frames its performance as superior, but the evidence on the task that 2D methods can actually do is equivocal. This should be explicitly discussed rather than glossed over.

- **The "~70% inference speedup" claim is unverifiable.** Line 255 states the tri-plane representation achieves "a speedup of approximately 70% at inference time" compared to "NeRF approaches that use MLPs." No specific baseline method is named, no absolute timings (seconds per frame at a given resolution) are reported, and no hardware or sampling configuration is given. This claim is too vague to evaluate or reproduce.

- **The user study lacks critical methodological details.** The paper reports "approximately 3000 votes" and "5000 votes" (Figures 7–8) but the bar charts are not visible in the text. No per-method breakdown, no confidence intervals, no description of how users were instructed to weigh style quality vs. flicker, and no statistical significance test are provided. The user study as reported supports the paper's claims in only an aggregate, unverifiable sense.

- **The geometry-guided tri-plane description is ambiguous at a critical architectural juncture.** The paper describes encoding voxel coordinates with positional encoding, projecting them onto three planes, aggregating via average pooling, and using "three encoders with 2D convolutional networks to represent the tri-plane features" (lines 114–119). However, it is not clear how the U-Net outputs relate to the tri-plane features used during point query — whether they ARE the plane features, modulate them, or serve as additional conditioning. In vanilla K-Planes, plane features are learnable parameter grids; here they appear to be generated from encoded coordinates. Without a clear diagram or tensor-flow specification, this component is not reproducible from the text alone.

- **No statistical significance or variance reported.** All warping-error results are point estimates without variance, confidence intervals, or significance tests. Given the small datasets (40–200 frames), results could be driven by a small number of frames.

### Trivial

- The stylization component (AdaAttN) is used off-the-shelf without modification. The paper should state this more explicitly early on rather than implying a novel stylization approach.

## Nice-to-Haves

- Comparison against a two-stage pipeline using a stronger dynamic NeRF backbone (e.g., HumanNeRF, MonoHuman) rather than the authors' own reconstruction network would strengthen the claim that the unified approach is inherently better, not just benefiting from a better reconstruction.
- Absolute inference timings (seconds/frame at a given resolution on specific hardware) would ground the speedup claim.
- Reporting the stylization losses (content and style losses) explicitly rather than referencing AdaAttN would improve self-containedness.

## Removed Points

*These points were flagged by the reviewers but are removed after verification:*

- **"Comparisons with 2D methods are structurally rigged"**: Table 2's caption explicitly states "The input of all methods are generated by the proposed method." The paper is transparent about what is being compared (unified vs. two-stage), and this comparison is presented in the correct context. The original-view comparison (Table 1) is the appropriate fairness check, and it shows mixed results — which I retain as a Minor weakness above.
- **"Missing related works on dynamic NeRFs"**: Per the filtering rules, missing related works should not be mentioned.
- **"No comparison with a method that does the same task"**: No existing method does this task, which is precisely the paper's stated contribution. Table 5 compares against the natural two-stage baseline.
- **"Objective functions from AdaAttN not specified"**: The paper references the original AdaAttN paper for these losses, which is standard practice.
- **"~70% speedup as a strength"**: This claim is too vague to function as a strength; the weakness version is retained.

## Novel Insights

The two reviewer inputs frame the paper's central tension differently: the harsh critic sees the missing style metrics as a potentially fatal gap that unmoors the "superior balance" claim, while the strength finder emphasizes the genuine novelty of the unified capability. The key insight from synthesis is that the paper's most defensible claim is not "superior balance" (which requires measuring both style and consistency) but rather "first unified framework" (which Table 0 convincingly establishes). The most informative experiment — Table 5 comparing unified vs. two-stage pipelines — directly supports the framework-level contribution without requiring side-by-side style quality comparisons. Re-centering the narrative and evaluation around this comparison, while adding even minimal quantitative style anchoring (e.g., measuring how well the style pattern is preserved), would substantially strengthen the paper.

## Suggestions

1. Add at least one quantitative style quality metric: style loss (Gram matrix distance to style image) or a perceptual metric comparing stylized outputs to the style reference.
2. Acknowledge and discuss the mixed results on original-view stylization (AdaAttN beating the proposed method on "Our dataset").
3. Provide absolute inference timings with hardware specifications to ground the speedup claim.
4. Clarify the geometry-guided tri-plane architecture: specify U-Net inputs/outputs and how processed features inform point queries.
5. Report per-method breakdowns with confidence intervals for the user study.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>