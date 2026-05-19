Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes Part321, a method that recognizes 3D object parts from a single 2D image using only one annotated 3D mesh per category. It learns two types of correspondence—mesh-to-mesh (to share features across objects in a category) and mesh-to-image (to align 3D features with 2D image features)—and performs inference via gradient-based optimization of each part's 3D configuration using a render-and-compare approach. The method is evaluated on 2D part segmentation (against supervised segmentation baselines on three datasets) and on 3D part detection (without comparative baselines).

## Strengths

- **Novel and well-motivated problem formulation**: Recognizing 3D object parts from 2D images with minimal annotation (one 3D mesh per category) is a genuinely underexplored direction. The combination of mesh-to-mesh and mesh-to-image correspondence to build a category-level neural mesh is a creative and principled approach.

- **Method design is internally coherent and validated by ablation**: The two-level correspondence learning (mesh-to-mesh, Section 3.2; mesh-to-image, Section 3.3) and the gradient-based inference with geometry consistency (Section 3.4) form a complete pipeline. Table 5 provides ablation experiments showing that removing any component (part scaling, geometry consistency loss, part deformation) degrades performance on both 2D and 3D metrics, supporting the design choices.

- **Solid 2D segmentation results against reasonable baselines**: Part321 outperforms SegFormer (MiT-B2) and DeepLabV3+ (ResNet50), both with ImageNet-1K pretraining and pseudo-labeling from a domain adaptation method (Hoyer et al., 2022), across three datasets (VehiclePart3D, PartImageNet, UDA-Part). The improvement is substantial on fine-grained part definitions (Tables 1–3). The paper correctly notes this comparison is asymmetric (Part321 solves the harder 3D+2D task).

- **First quantitative demonstration of one-shot 3D part detection from a single image**: Table 4 reports 3D pose accuracy, Chamfer distance, and 3D bounding box IoU on the 3D DST dataset. While lacking baselines, this establishes feasibility for a task that previously had no quantitative results.

- **Contribution of a new benchmark (VehiclePart3D)**: The paper introduces a dataset with 279 real images, 47 CAD models, and part annotations across 5 categories, which can support future work on one-shot part segmentation.

## Weaknesses

### Fatal
None.

### Major
- **The "State-of-the-Art" claim for one-shot 2D part segmentation is not adequately supported**. The baselines (SegFormer, DeepLabV3+) are general segmentation architectures adapted to a one-shot training setup, not methods designed for few-shot/one-shot segmentation. No comparison is made to any few-shot segmentation approach (e.g., prototype-based or metric-learning methods) that could reasonably be adapted to part segmentation. The claim of "State-of-the-Art" implies a broader comparison than the paper provides. The paper can fix this by either adding such comparisons or tempering the claim to "strong performance in a data-constrained 2D part segmentation setting."

- **No comparative baselines for the 3D part detection task (the paper's central contribution).** Table 4 reports only Part321's own performance. The paper acknowledges this (line 116: "3D part detection from images using only one annotation lacks comparable baselines"), but this does not change the fact that the reader cannot calibrate whether the reported numbers (e.g., Chamfer distance, 3D IoU) are impressive or merely operational. A comparison to a simplified variant (e.g., a non-deformable template, or a method that predicts 3D bounding boxes per part from 2D segmentation) would meaningfully anchor the results.

### Minor

- **No discussion of failure modes or limitations.** The paper does not discuss where the approach breaks down. The method assumes category-level topological similarity (learned via mesh-to-mesh correspondence), which may fail for non-rigid or articulated categories (e.g., chairs, animals). Objects with missing/extra parts relative to the template are also not discussed. Adding a limitations paragraph would improve scientific rigor.

- **Inference runtime is not reported.** The inference involves 300-step gradient optimization per image (line 109), which is potentially expensive. No timing information is provided, which matters for real-world applicability.

- **No per-part IoU breakdown for 2D segmentation.** Reporting per-part IoU would reveal whether Part321 systematically fails on small, thin, or heavily occluded parts, and would help distinguish geometric errors from topological errors.

### Trivial
None.

## Nice-to-Haves

- Ablation on the number of CAD models used for training (e.g., 30 vs. 10 vs. 5) to test robustness to limited 3D data.
- Quantitative evaluation of mesh-to-mesh correspondence quality (e.g., semantic correspondence accuracy).
- Reporting per-category results rather than aggregates in Table 4.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The baseline comparison is unfair because it favors the author's method"**: Removed. The paper explicitly notes the asymmetry favors the *baselines* (line 116: "Note that this is an unfair comparison since our framework performs the extra task, which is more challenging than the purely 2D task"). The rule states to remove criticisms about unfair comparison when the asymmetry favors the baseline.

- **"The paper does not specify whether the PointNet++ encoder is trained on the category's meshes or a large corpus"**: Removed. The paper cites prior work (Sun et al., 2021) and states the encoder is trained "unsupervisedly from pointclouds" (line 43). The context makes clear it is trained on the category's meshes. This is a marginal implementation detail, not a substantive weakness.

- **"Missing appendix content, proofs, or references"**: Removed per the hard rule that the parser strips these sections from all papers; they exist in the original submission.

- **"The paper does not explain how the ground-truth offset is computed when correspondence is not one-to-one"**: Removed. The paper explains this clearly: argmax (Eq. 1) selects the best match, and the loss (Eq. 2) uses that correspondence. This is standard practice.

- **Strength Finder: "Outperforms strong 2D baselines"** — the "strong" qualifier is somewhat inflated given the baseline choice issue. However, the factual claim (outperforms) is correct, so I retain the underlying evidence but caveat the framing in weaknesses above.

- **Strength Finder generic strengths**: Removed strengths like "this paper addressed an important problem" or "this paper targets an interesting question" as generic/superficial. Only retained concrete evidence-backed strengths.

## Novel Insights

The two reviews collectively surface a useful tension that the paper itself does not fully acknowledge: the task being "pioneering" (3D part detection from a single image) and the desire to claim "state-of-the-art" (on 2D segmentation) are somewhat at odds. The truly novel contribution is the 3D pipeline, yet the paper front-loads the 2D SOTA framing, which sets expectations of comparisons the paper does not deliver. Conversely, the 3D results—the paper's most original part—are presented almost as an afterthought without comparative grounding. The insight from the cross-review analysis is that the paper would be stronger if it leaned into the 3D contribution as the primary claim and presented the 2D results as a convenient evaluation proxy (facilitated by the 3D-to-2D projection) rather than as a standalone SOTA claim.

## Suggestions

1. **Temper or properly qualify the "State-of-the-Art" claim.** Either add comparisons to few-shot/one-shot segmentation methods or rephrase to "strong performance on one-shot 2D part segmentation under a controlled data regime."
2. **Add at least one anchor for the 3D results.** A simple ablation (e.g., a fixed non-deformable part template, or a heuristic baseline using 2D segmentation lifted to 3D) would greatly strengthen the 3D evaluation.
3. **Add a Limitations section** discussing failure cases (non-rigid categories, missing parts, occlusion).
4. **Report inference time** and discuss the computational cost of the 300-step optimization.
5. **Include per-part IoU** in the 2D segmentation tables to reveal where errors occur.

## Score and Decision

**Originality**: High — the task formulation (one-shot 3D part detection from 2D images) and the two-correspondence approach are novel.  
**Importance of research question**: High — data-efficient part recognition has practical value.  
**Claims support**: Moderate — the 2D SOTA claim is oversold; the 3D results lack comparative context.  
**Soundness of experiments**: Moderate — the ablations are good, but baseline choices and the missing 3D comparison weaken the evidence.  
**Clarity**: Good — the method is described clearly, figures illustrate the pipeline well.  
**Value to community**: High — the task, method, and VehiclePart3D benchmark are useful contributions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>