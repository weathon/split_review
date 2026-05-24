Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes E3D, a two-stage training strategy that leverages large multimodal models (FastSAM + SemanticSAM) to generate pseudo-labels for sparsely-supervised 3D object detection on KITTI. Three technical modules are introduced: CPST (boundary-constrained semantic transfer from 2D to 3D), DCPG (dynamic-radius clustering for pseudo-label generation), and DS score (unsupervised quality scoring for pseudo-labels). The first stage trains a detector on LMM-derived pseudo-labels without ground truth; the second fine-tunes with extremely limited human annotations (~2%). The paper claims significant improvements over CoIn++ and asserts zero-shot capabilities.

**Important caveat:** The extracted paper is truncated — Tables 1 and 2 are embedded as unreadable images, and content after approximately line 175 (likely including ablations, zero-shot experiments, and conclusion) is absent. This limits the verifiability of several claims from both the paper and the reviews.

## Strengths

- **Clear problem framing and well-structured pipeline.** The paper identifies two concrete challenges (edge noise in 2D→3D semantic transfer, incomplete foreground in pseudo-label fitting) and designs one module per challenge. CPST's boundary-constrained mask shrink (Eq. 3, Section 3.2) directly addresses calibration-induced boundary noise with a simple geometric operation. This transparent design is a genuine strength — each component maps to a specific, stated problem.

- **DS score provides an unsupervised alternative to IoU-based NMS.** Section 3.4 proposes scoring pseudo-label proposals by their fit to a distribution prior (point-to-boundary distances ~ Gaussian) and a class-specific shape prior (meta-shape via KL divergence), replacing the ground-truth-dependent IoU metric. This is a principled approach to quality filtering in the absence of labels and is a concrete technical contribution.

- **Evaluation across multiple detector architectures.** Table 2 (visible in structure, though numbers are in an image) evaluates E3D on VoxelRCNN, CenterPoint, and CasA — three architecturally distinct detectors. This cross-architecture evaluation strengthens the claim that the method provides generalizable feature enhancement, not just a single-detector artifact.

- **Extremely low annotation regime targeting.** The paper targets 0.1% and 2% annotation rates, which is genuinely challenging. The stated improvements (36.92% at 0.1%, 14.89% at 2% in the text) represent meaningful practical gains if verifiable.

## Weaknesses

### Fatal
None.

### Major

- **Zero-shot results are claimed but not visible in the extracted experiments.** The abstract states: "we have verified our E3D in the zero-shot setting, and the results demonstrate its performance exceeding that of the state-of-the-art methods." The contributions list (end of Section 1) repeats: "without fine-tuning on labeled data, our E3D has shown superior performance compared to zero-shot methods." However, Section 4 (Experiments) describes only the setup with fine-tuning on 2% (or 0.1%) annotations. No zero-shot experiment table or comparison against methods like SAM3D or CLIP2Scene (cited in Section 2.2) is present in the extracted text. While the paper is truncated and zero-shot results could reside in the missing portion, a central claim of the paper is unsubstantiated by the available evidence. This must be addressed in a complete version.

- **No ablation study or hyperparameter sensitivity analysis is present in the extracted text.** The pipeline introduces three modules with at least six hyperparameters: mask shrink factor γ (set to 0.3), initial cluster radius r_initial (set to 1), adjustment factor δ (set to 0.1), DS score weights λ1, λ2 (both 0.5), and the Gaussian prior parameters μ=0.8, σ=0.2 (from Luo et al. 2024). The paper reports no analysis isolating the contribution of each module, no sensitivity study for any hyperparameter, and no study of how these choices affect the method's behavior across object classes. For a pipeline with this many design choices, the absence of ablations makes it impossible to know which components drive the reported results or how robust the method is to parameter settings. This is a significant methodological gap.

- **The claimed comparison with cross-modal weakly-supervised methods (Qin et al., 2020; Liu et al., 2022b) is stated in the Baselines paragraph (line 156) but no such comparison table is visible.** The paper promises this comparison to position against 2D-assisted weakly-supervised detectors, but it does not appear in the extracted experiments.

### Minor

- **The DCPG radius update (Eq. 4) uses a linear schedule based on seed point index `t`, with limited geometric justification.** The function `update(t, r_initial) = r_initial * t / N^(k) + δ` increases the clustering radius with the index of the seed point being processed. The paper states this provides "multi-scale receptive fields" (line 119), which is a reasonable intuition. However, the ordering of seed points is not defined, and the radius growth is tied to an arbitrary index rather than to any local geometric property (e.g., point density, distance to nearest neighbor, or curvature). A simple fixed-radius baseline or density-adaptive baseline would clarify whether the dynamic schedule is beneficial beyond simpler alternatives. The absence of this comparison weakens the claimed contribution of DCPG.

- **DS score hyperparameters are cited from prior work without KITTI-specific validation.** The Gaussian prior (μ=0.8, σ=0.2) is attributed to Luo et al. 2024, and the meta-shape templates to Wu et al. 2024. KITTI LiDAR point clouds have different density, range, and occlusion characteristics than the datasets used in those prior works. The paper does not check whether these priors actually hold on KITTI data. If the Gaussian mean of 0.8 is calibrated on indoor or synthetic data, it may systematically penalize or favor certain KITTI object types. A simple empirical validation (e.g., plotting the distance-to-boundary distribution for ground-truth boxes on KITTI) would resolve this concern.

### Trivial
- The phrase "Ehanced 3D object Detection strategy" in the abstract and Section 3.1 has a typo in "Ehanced" (should be "Enhanced").
- Equation formatting is inconsistent (e.g., `$\begin{array}{r}{\gamma^{c}=}\end{array}$` in line 81 appears garbled — clearly a parser artifact, not the authors' fault).

## Nice-to-Haves
- An analysis of when the LMM pipeline (FastSAM + SemanticSAM + cosine similarity) fails: for small objects, under occlusion, or in dense scenes. This would help calibrate expectations for practitioners.
- Validation of the DS score priors on KITTI ground-truth data (e.g., histogram of point-to-boundary distances for each class).
- A fixed-radius or density-adaptive baseline for DCPG to substantiate the benefit of the dynamic radius schedule.
- Statistical significance or variance reporting for the main results, especially given the random 10% scene selection.

## Removed Points

- **Criticism that E3D "degrades Pedestrian and Cyclist" (Harsh Critic Point 1):** This is not verifiable from the extracted text. Table 1 is an embedded image that cannot be read. The paper text acknowledges only "a slight decrease in precision for the 'Easy' car category" (line 164) but does not discuss Pedestrian or Cyclist. Without access to the actual numbers in Table 1, this claim cannot be confirmed or refuted. If true, it would be a serious issue, but I cannot validate it from the available evidence. **Treated with caution — the authors should address this in their response.**

- **Criticism that the experimental setup is underspecified / confounded (Harsh Critic Point 5):** The paper describes the split procedure (10% of scenes, one annotation per scene = ~2%) in lines 152-153. While it does not explicitly state that baseline CoIn++ numbers use the same split, this is standard experimental practice and the paper states it "followed" CoIn. This concern is speculative rather than grounded in a concrete discrepancy visible in the text.

- **Criticism about "implicit embedding" advantage not supported (from Harsh Critic notes):** The paper explicitly contrasts its explicit transfer approach with implicit embedding (citing Vora et al. 2020, line 101) and states the motivation ("avoid potential semantic feature confusion"). The criticism that "no experiment supports the claimed advantage" is reasonable in principle but is a subset of the more general missing ablation problem already listed.

- **Strength Finder's generic praise about "importance of the problem":** Dropped; this is a generic strength that could apply to any paper in this area and carries no discriminatory value.

- **Strength Finder's claim about DCPG adapting to "object geometry":** While the method varies radius, it does so by index, not by geometry. The strength claim overstates what the paper demonstrates. The DCPG description is kept as a contribution but the overstrong characterization is removed.

## Novel Insights

The reviews surface a deeper tension not explicitly discussed in the paper: LMMs (FastSAM + SemanticSAM) are likely to produce much higher-quality masks for cars (large, rigid, well-represented in training data) than for pedestrians or cyclists (small, articulated, less common). This asymmetry may explain why the method could be effective for one class but counterproductive for others — if the pseudo-labels are good for cars but noisy for pedestrians, the first-stage training could imprint biased feature representations that fine-tuning struggles to correct. The paper's silence on class-specific analysis is thus a missed opportunity to tell a more nuanced and ultimately more credible story about where and why LMM-assisted sparsely-supervised detection works. A future revision that explicitly characterizes which classes benefit and why would transform the paper from a broad (and arguably overclaimed) enhancement claim into a sharper, more actionable contribution.

## Suggestions

1. **Provide the promised zero-shot results**, or remove the claim from the abstract and contributions. This is the single most damaging discrepancy between the paper's rhetoric and its presented evidence.
2. **Add a class-specific analysis (Car, Pedestrian, Cyclist) of each module's effect.** At minimum, show a table of AP with CPST only, CPST+DCPG, and full E3D for each of the three KITTI classes at both difficulty levels.
3. **Ablate hyperparameter sensitivity** for the three most important parameters: mask shrink factor γ (e.g., 0.1–0.7), initial clustering radius r_initial (e.g., 0.5–2.0m), and DS score weight λ1/λ2 ratio.
4. **Validate the DS score priors** by showing that the point-to-boundary distance distribution on KITTI ground truth is indeed well-approximated by N(0.8, 0.2) for each class.
5. **Compare DCPG's dynamic-radius clustering** against a fixed-radius baseline to demonstrate that the dynamic schedule provides a measurable benefit.

## Score and Decision

The paper addresses a timely problem and proposes a pipeline with clear, well-motivated components. The method is technically coherent, and the available evidence (though partially obscured by the paper being truncated in extraction) suggests genuine improvements in the extremely low annotation regime. However, two major gaps are verifiable even from the truncated text: (1) the zero-shot results claimed in the abstract and contributions do not appear in the experiments section, and (2) no ablation or sensitivity analysis is provided for any of the three modules or six hyperparameters. The paper also promises a cross-modal comparison that is not visibly delivered. These gaps are fixable but prevent the current submission from being a complete, self-contained contribution. With the missing experiments and analysis provided, a revised version could make a solid case.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>