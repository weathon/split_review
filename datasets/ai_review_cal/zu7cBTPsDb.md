- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information I need. Let me compile the final review, carefully applying the filtering rules.

---

## Summary

MVTokenFlow proposes a pipeline for 4D content generation from a monocular video. It uses a pretrained multiview diffusion model (Era3D) to generate multiview images per frame, reconstructs a coarse dynamic 3D Gaussian field, then *regenerates* the multiview images by applying token propagation guided by rendered 2D flows from the coarse field, and finally refines the 4D field. The core idea — using rendered 2D flows from a coarse 4D field to guide token propagation in a multiview diffusion model — is clearly motivated and the approach consistently outperforms three existing baselines on a standard benchmark.

## Strengths

- **Token propagation guided by rendered 2D flows for multiview diffusion.** The paper extends 2D token flow (Geyer et al., 2023; Li et al., 2024c) from video editing to multiview 4D generation. After reconstructing a coarse dynamic 3D Gaussian field, the method renders 2D flow maps for *all* viewpoints and uses them to guide token propagation during regeneration (Sec. 3.3, Eq. 1). The ablation study (Table 3, "w/o flow propagation" row) shows this improves FVD, establishing a direct link between the innovation and the temporal consistency gain.

- **Consistent quantitative and qualitative improvement over strong baselines.** The method outperforms Consistent4D, SC4D, and STAG4D on all five metrics in Table 1 (PSNR, SSIM, LPIPS, CLIP, FVD). Qualitative comparisons (Fig. 3, Fig. 4) show visibly sharper motion and fewer artifacts, especially for complex real-world motions ("man turning his head") where prior methods fail.

- **Effective use of flow loss and normal loss for motion and geometry.** The flow loss (Sec. 3.2) explicitly supervises rendered 2D flows from the dynamic Gaussian field, decoupling motion and appearance learning. Ablation (Table 3) shows removing flow loss increases FVD from 73.8 to 79.7. The normal loss contributes to multi-view consistency (CLIP drops from 96.5 to 96.0). These design choices are well-motivated and empirically validated.

- **Leverages frozen pretrained models without expensive retraining.** The pipeline uses Era3D as-is, modifying only its inference via enlarged self-attention and token propagation (Sec. 3.1, 3.3). This avoids the computational burden of training a dedicated 4D diffusion model from scratch.

## Weaknesses

### Fatal
None.

### Major

- **Ablation terminology and missing quantitative component.** The ablation study (Sec. 4.3) suffers from confusing terminology. The text describes removing "flow loss" or skipping "regeneration and refinement phase" (Fig. 5), but Table 3 quantitatively ablates "flow propagation" and "normal loss" — a different set of components. "Flow loss" (a training loss on the 4D field, Sec. 3.2) and "flow propagation" (which appears to refer to the token propagation mechanism) are distinct things, yet the paper uses these terms as if interchangeable. Furthermore, the paper provides a qualitative comparison of the coarse field vs. the final result (Fig. 5b vs. 5c) showing that regeneration helps, but there is **no quantitative row in Table 3 for "w/o regeneration stage."** Without this, the reader cannot tell how much of the improvement in Table 3 comes from the regeneration stage as a whole versus the token-propagation component specifically. This undermines the paper's core empirical narrative.

- **Evaluation is confined to a single small dataset without statistical grounding.** All quantitative numbers (Tables 1–3) come from the Consistent4D dataset (24 videos). The paper mentions a "self-collected dataset" but provides only qualitative results on it. Metrics such as FVD are notoriously noisy with small video counts, yet no confidence intervals, error bars, or results from multiple seeds are reported. This makes it impossible to assess whether the reported advantages (e.g., LPIPS 0.08 vs. 0.11) are reliable or within the noise floor. Additionally, the number of viewpoints used in the evaluation metrics is not specified, raising the question of whether comparisons with baselines that generate different numbers of views are systematically biased.

### Minor

- **Key assumption about cross-view attention transferring temporal consistency is unverified.** The method only uses 2D flow on the front view for the coarse stage, relying on Era3D's cross-viewpoint attention layers to propagate temporal consistency to other views (Sec. 3.1, line 66). Cross-view attention is designed for *spatial* consistency across viewpoints, not temporal coherence. The paper provides no direct evidence that this mechanism successfully transfers temporal consistency; the claim rests entirely on the final results, which conflate multiple design choices.

- **Several methodological details are omitted.** (a) The paper does not explain how rendered 2D flow maps are converted into pixel correspondences for the token warp (bilinear interpolation? occlusion handling?). (b) The coarse 4D field is trained with flow loss *only on the front view* (via RAFT); rendered flows for other viewpoints come from a field never supervised on those views, but their quality is not discussed or measured. (c) The impact of RAFT noise on the flow loss is not discussed. (d) Hyperparameters (keyframe interval of 8, diffusion step threshold τ=20) are stated but not justified.

- **Incremental contribution relative to prior token-flow work.** The token propagation mechanism is directly adapted from prior video-editing work (Geyer et al., 2023; Li et al., 2024c). The main technical novelty is rendering flows from a coarse 4D field rather than estimating optical flow, and applying the mechanism per-viewpoint in multiview diffusion. This is a reasonable integration but not a fundamental advance. The paper also does not analyze how rendered flow quality affects regeneration, nor does it compare against a baseline using RAFT-estimated flows on all viewpoints.

- **Missing computational cost information.** The paper states experiments run on an A40 GPU but gives no training times. Readers cannot assess practicality.

- **Table 2 vs. Table 1 distinction is unclear.** The paper does not explain how Table 2 (novel view synthesis on synthetic objects) differs from Table 1 or what the metric in the table header is.

- **Available baselines do not include the very latest methods that use multiview diffusion models** (e.g., L4GM, 4D-fy). The chosen baselines (Consistent4D, SC4D, STAG4D) are reasonable but not fully up-to-date.

### Trivial

- The paper uses the term "token propagation" throughout the Method sections but switches to "flow propagation" in the ablation discussion (line 145). Since these likely refer to the same mechanism, the terminology should be consistent.

## Nice-to-Haves

- Reporting results on at least one additional dynamic dataset (e.g., RealEstate10K-derived dynamic subset) would address concerns about single-dataset evaluation.
- Reporting FVD on the input (reference) viewpoint would directly validate that the generated 4D video does not drift from the source video.
- Reporting task-specific variances (across 3 seeds) on the Consistent4D dataset would provide statistical grounding.
- Measuring rendered 2D flow quality (e.g., endpoint error against RAFT on the front view) would validate that the coarse field produces flows suitable for guiding token propagation.

## Removed Points

These points from the inputs were found to be invalid or non-substantive upon cross-checking with the paper:

1. **"SC4D struggles to model motion (in Sec. 2) is given as a claim without citation"** — This statement appears in Sec. 4.2 (Experiments, line 115), not in Sec. 2 (Related Work). It is an observation from the authors' own experimental comparison, not an uncited claim in a literature review. (Harsh Critic, Section-by-Section Notes)

2. **"The paper does not compare against an Era3D baseline without token propagation"** — Table 3 includes a "w/o flow propagation" ablation, which (by the paper's own description) removes the token propagation mechanism while keeping Era3D. This IS the Era3D-baseline-without-token-propagation comparison. The terminological sloppiness ("flow propagation" vs. "token propagation") is real, but the specific claim of a missing comparison is factually wrong. (Harsh Critic, Critical Issue 3)

3. **"Replacing Era3D with a simpler multiview method would isolate the contribution"** — This asks the paper to prove that Era3D is the right backbone, which is outside the paper's scope. The paper's claim is that token propagation on top of Era3D improves temporal consistency; the "w/o flow propagation" ablation within the Era3D pipeline properly tests this. (Harsh Critic, Critical Issue 3)

4. **"Images are small and hard to judge"** — This is a formatting/rendering artifact from PDF parsing, not an author issue. (Harsh Critic, Section-by-Section Notes)

5. **"The paper is an incremental integration... not a fundamental advance"** — Partially kept as a Minor weakness about novelty significance, but the harsh framing ("incremental integration") overstates the case. Extending token flow from 2D video editing to multiview 4D generation with rendered 2D flows is a non-trivial adaptation with demonstrated empirical benefit. (Harsh Critic, Critical Issue 4 — softened in the Minor section above)

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation about the paper that changes the interpretation of its results or suggests a direction not already evident from the paper itself. The main value provided by the meta-review is filtering noise and clarifying which specific criticisms are verifiable from the paper as written versus which stem from misreading or scope creep.

## Suggestions

1. **Unify the ablation narrative.** Add a quantitative row for "w/o regeneration stage" (i.e., coarse field only) to Table 3. Align the terminology between the Method section ("token propagation") and the ablation discussion. Clearly separate the Figure 5 ablation (flow loss, regeneration skip) from the Table 3 ablation (flow propagation, normal loss) and explain why different components are tested in each.

2. **Add variance/error bars** for all metrics on the Consistent4D dataset, reporting at least 3 independent runs.

3. **Clarify the evaluation protocol** — state explicitly how many viewpoints are used for each metric and verify that baselines use the same count.

4. **Provide additional implementation details** for the token propagation: how warped features are computed (e.g., bilinear interpolation, occlusion masking via flow confidence) and how the rendered 2D flow maps are used to establish pixel correspondences.

5. **Report computational cost** (training time in hours for each stage) to help readers assess practicality.
