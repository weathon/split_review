Now I have thoroughly verified all claims against the paper. Let me write the final consolidated review.

---

## Summary

MVTokenFlow proposes a pipeline for 4D content generation from monocular video. It first uses a pretrained multiview diffusion model (Era3D) to generate multiview images per timestep, reconstructs a coarse dynamic 3D Gaussian field from these images, then regenerates the multiview images by using 2D flows rendered from the coarse field to guide token propagation across all viewpoints, and finally refines the dynamic 3D Gaussian field with the regenerated images. The key technical ideas are (1) extending token flow from 2D video editing to multiview diffusion and (2) a coarse-to-fine pipeline where the coarse 4D field's rendered flows bootstrap temporally consistent regeneration for all viewpoints.

## Strengths

- **Novel coarse-to-fine pipeline for multi-view temporal consistency.** The paper introduces a two-stage approach where front-view token propagation (Section 3.1) produces a coarse 4D field, whose rendered 2D flows then guide token propagation on all viewpoints during regeneration (Section 3.3). This design breaks the dependency on single-view optical flow and enforces temporal consistency on unseen views without retraining a multiview diffusion model. The ablation (Table 3) shows that flow propagation reduces FVD from 220.4 to 208.4, and qualitative results (Figure 5b vs 5c) show regeneration significantly improves image sharpness.

- **Extension of token flow from 2D video editing to multiview diffusion for 4D generation.** The paper adapts the token merging/flow concept from prior video editing work (Geyer et al., 2023; Li et al., 2024c) to the multiview setting, using rendered 2D flows from a coarse dynamic 3D Gaussian field to warp features between keyframes and intermediate frames (Eq. 1, Section 3.1). Figure 6 demonstrates that without token propagation, generated multiview videos exhibit flickering and inconsistent pose/body shape across timesteps.

- **Flow loss and normal map supervision for dynamic 3D Gaussian field reconstruction.** The paper introduces a rendered 2D flow loss (minimizing difference between rendered optical flow from dynamic Gaussians and RAFT-estimated flow) and a normal map loss (from Era3D-generated normals) during reconstruction (Section 3.2). These losses provide explicit geometric and motion constraints. The ablation (Table 3) shows normal loss improves multi-view consistency (CLIP from 0.915 to 0.928), and Figure 5 demonstrates flow loss enhances extracted optical flow quality.

- **State-of-the-art quantitative results on the Consistent4D benchmark.** MVTokenFlow outperforms Consistent4D, SC4D, and STAG4D on all reported metrics (Table 1). LPIPS is reduced to 0.111 from 0.235 (Consistent4D) and 0.179 (STAG4D), indicating substantially better perceptual consistency. The method also shows strong qualitative improvements on complex motion cases (man turning head, Figure 3).

- **Avoids dependence on large-scale 4D training data.** Unlike methods that train temporally consistent multiview diffusion models from scratch on large 4D datasets, MVTokenFlow leverages a pretrained multiview diffusion model (Era3D) and enforces temporal consistency through token propagation guided by rendered 2D flows, without retraining or requiring 4D datasets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **FVD is absent from the main quantitative comparison (Table 1).** The paper claims temporal consistency as a core contribution and reports FVD only in the ablation study (Table 3). Including FVD in the main comparison against baselines would strengthen the claim that the method improves temporal consistency beyond what ablation alone can demonstrate.

- **The rendered 2D flow accuracy from the coarse 4D field is asserted but not quantitatively validated.** Section 3.3 states that "these coarse 3D Gaussian fields already produce a reasonable 3D flow field" without providing quantitative flow accuracy metrics (e.g., endpoint error against ground-truth flows on synthetic data). While the qualitative flow maps in Figure 5 are suggestive and the downstream improvement (FVD reduction) provides indirect validation, a direct flow accuracy evaluation would strengthen confidence in the core mechanism.

- **The token propagation feature injection is underspecified.** Section 3.1 describes obtaining self-attention features from keyframes, warping them via 2D flows, and interpolating them (Eq. 1) but does not state whether these propagated features replace the UNet latent features entirely, are used as keys/values in self-attention, or are injected through a different mechanism. While readers familiar with TokenFlow (Geyer et al., 2023) may infer the procedure, the description is insufficient for independent reproduction.

- **The main comparison (Table 1) does not isolate the contribution of Era3D from the proposed token flow.** The baselines (Consistent4D, SC4D, STAG4D) use SDS-based supervision or different backbones, so some of MVTokenFlow's improvements could stem from Era3D's multiview generation quality. The ablation in Table 3 partially addresses this by keeping Era3D constant and varying token propagation, but the main comparison would benefit from a controlled baseline that uses Era3D without token flow or the refinement stage.

### Trivial
- Section 3.1 uses the notation `\dot{\pi}(n\rightarrow\bar{n_m})` (line 58) which appears to be a rendering artifact; the bar over `n_m` seems misplaced.
- The two-stage description (front-view token flow in Section 3.1, all-view token flow in Section 3.3) is split across sections, making it mildly harder to follow the complete method in one pass.

## Nice-to-Haves
- A separate ablation of enlarged self-attention (Section 3.1) vs. token propagation to quantify each component's contribution to temporal consistency.
- Flow accuracy evaluation (e.g., EPE on synthetic data) to validate the coarse field's rendered flows.
- Compute runtime and training time comparisons with baselines.
- Discussion of failure cases beyond Era3D viewpoint limitations (e.g., where rendered flows are inaccurate due to occlusion or fast motion).

## Removed Points
These points are flagged to be removed, treat them with caution:
1. "The ablation (Table 3) leaves out the regeneration step (coarse vs. refined) as a separate condition" — **Factually incorrect.** Table 3 has a dedicated "Regeneration & Refinement" column comparing with and without this stage.
2. "Figure 5 shows qualitative improvement but the 'without flow loss' condition changes both flow loss and regeneration, conflating the two" — **Factually incorrect.** The paper ablates them separately: (c) is without regeneration, (d) is without flow loss, as described in the text.
3. "The paper does not ablate the impact of Era3D itself (e.g., by feeding baseline methods with Era3D-generated multiview images)" — This would require fundamentally modifying the baseline methods' pipelines and is not a standard controlled comparison. The ablation (Table 3) already keeps Era3D constant and isolates token flow's contribution.
4. Criticism about missing error bars / statistical significance on point estimates — This is standard practice for this benchmark/dataset size in the field.
5. Request for runtime and computational cost — A nice-to-have, not a weakness.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective on the method that the paper itself does not already articulate.

## Suggestions
1. Clarify in Section 3.1 exactly how the propagated features (Eq. 1) are used in the UNet denoising process — are they the latent features themselves, or are they injected as keys/values in self-attention?
2. Report FVD in the main comparison table alongside the baselines so that temporal consistency gains are directly benchmarked.
3. Add a quantitative evaluation of rendered 2D flow accuracy from the coarse field (e.g., endpoint error on synthetic data where ground-truth flow can be computed).
4. For the main comparison, consider including an ablated variant that uses Era3D without token flow or refinement to better decompose the source of improvements.
5. Merge the description of token propagation for all viewpoints (Sections 3.1 and 3.3) into a single coherent exposition to avoid reader confusion about the two-stage application.

## Score and Decision

The paper presents a novel and well-motivated pipeline that produces clearly improved 4D generation results over existing methods. The core ideas — extending token flow to multiview diffusion and using a coarse 4D field to bootstrap temporally consistent regeneration — are technically sound. The quantitative and qualitative evaluations demonstrate meaningful improvements on a standard benchmark. The weaknesses are real but minor (missing FVD in main comparison, flow accuracy not directly validated, feature injection underspecified) and do not threaten the paper's core contributions. The paper would benefit from the suggested clarifications and additional validation, but in its current form it makes a solid contribution to the field.

**Originality:** Good — extension of token flow to multiview diffusion is novel.  
**Importance of research question:** High — 4D generation from monocular video is an active and important problem.  
**Claims support:** Adequate — supported by ablation studies and comparisons, though some validation is indirect.  
**Soundness of experiments:** Moderate — standard benchmark used but missing FVD in main comparison and lacking direct flow accuracy validation.  
**Clarity of writing:** Adequate — the method description is mostly clear but the feature injection detail is underspecified and the two-stage exposition is fragmented.  
**Value to community:** Positive — the pipeline is practical and avoids expensive 4D training data.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>