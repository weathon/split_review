Now I have all the information I need. Let me construct the final review.

## Summary

The paper introduces the task of Free-Form HOI Generation (beyond grasping, including actions like pushing, poking, rotating) and proposes TOUCH, a three-stage framework: (1) CVAE-based contact map prediction on hand/object surfaces, (2) a multi-level conditioned diffusion model with coarse-to-fine text and geometric injection, and (3) a refinement stage with cycle-consistency and physical constraints. It also contributes WildO2, a dataset of 4.4k 3D HOI samples reconstructed from Something-Something V2 videos with multi-level semantic annotations.

## Strengths

1. **Task formulation and problem framing** — Moving HOI generation beyond the grasp-centric paradigm to include non-grasping actions (push, poke, rotate, etc.) with fine-grained text control is a meaningful and timely step. The paper clearly motivates why this requires new methodology and data.

2. **Well-designed multi-level conditioning architecture** — The coarse-to-fine injection of global SSC features and local DSC features via FiLM and cross-attention (Section 4.2) is cleanly motivated and convincingly ablated. Removing this multi-level design drops P-IoU from 0.728 to 0.525 (Table 2), demonstrating that the hierarchical conditioning is essential.

3. **Explicit contact modeling with fine-grained hand-part segmentation** — The CVAE-based contact prediction (Section 4.1) with 17-part hand segmentation provides spatial priors beyond grasping. Ablation (Table 2, "✗ hoc.") shows contact accuracy drops sharply (P-IoU from 0.728 to 0.492) when removed, confirming its value for free-form poses.

4. **Empirically demonstrated semantic controllability** — The model captures force-related nuances ("firmly" vs. "gently") producing measurably different contact geometries (22-25% contact area difference, Section 5.4.3, Fig. 9), and generalizes to out-of-domain Objaverse objects and unseen verbs (Section 5.4.2, Fig. 7).

## Weaknesses

### Fatal

None.

### Major

1. **Evaluation on self-generated ground truth with limited external validation.** The WildO2 ground truth is reconstructed by the authors' own pipeline (object reconstruction from a reference frame, hand estimation, camera alignment, refinement). The metrics (MPVPE, contact IoU, P-FID) compare generated poses to this same pipeline's output. With only a 55% reconstruction success rate and no quantitative validation against real motion capture or manually annotated 3D poses, it is unclear how much of the reported improvement reflects genuine physical plausibility versus learning to reproduce reconstruction artifacts. The paper shows qualitative comparisons to original 2D frames (Fig. 5) and uses manual inspection, but these are not a substitute for quantitative external validation.

2. **Insufficient baseline comparison for claimed state-of-the-art.** The evaluation compares only to ContactGen (2023) and Text2HOI (2024), both adapted from different settings. The paper states "existing methods have not explored fine-grained controlled HOI generation," which justifies some limitation, but the claim of state-of-the-art is fragile without comparison to contemporaneous methods that may handle non-grasping interactions (e.g., those cited from 2025 in related work). Even if those methods are grasp-centric, a quantitative demonstration of their failure on free-form tasks would strengthen the paper.

3. **Unspecified test-time optimization asymmetry.** The paper augments baselines with "an optimization-based post-processing module to correct hand poses" but does not specify whether this module is equivalent in iterations, loss functions, or computational budget to TOUCH's refinement stage (which includes a refiner network plus \(N_{\text{tta}}\) TTA iterations). While TOUCH(w/o TTA) results are reported (Table 2 and referenced in Table 1), the main comparison presumably uses full TOUCH with TTA, making the comparison asymmetric if baselines receive less optimization.

### Minor

4. **No independent evaluation of the contact map prediction module.** The CVAE-based contact predictors (Section 4.1) are never evaluated quantitatively in isolation. Since the entire diffusion pipeline relies on these predictions, reporting their accuracy against ground-truth contact maps on held-out data would be a valuable sanity check.

5. **Missing VLM evaluation details.** The "VLM assisted evaluation" (Table 1) does not specify which VLM was used, the prompt template, or how scores were computed. This makes the metric non-reproducible.

6. **No confidence intervals or error bars in Table 1.** With ~677 test samples, reporting variance would help assess the stability of the reported improvements.

7. **Force-semantic analysis lacks statistical rigor.** The 22-25% contact area difference (Section 5.4.3) is reported without variance or significance testing, and the sample size/selection criteria are not stated.

### Trivial

None.

## Nice-to-Haves

- A subset of WildO2 validated against real mocap or manually annotated 3D poses would substantially strengthen the evaluation.
- Training TOUCH on an existing grasp-only dataset (e.g., GRAB) and showing degradation on free-form interactions would isolate the contribution of the WildO2 data.
- Reporting failure cases (generated poses that are unrealistic) would provide a more balanced assessment of the method's limitations.

## Removed Points

These points were flagged for removal during consolidation; treat them with caution.

- **"First large-scale in-the-wild 3D HOI dataset is overstated"**: The harsh critic argued the dataset is from scripted tabletop actions (Something-Something V2), not truly "in-the-wild." This is a definitional quibble — relative to lab mocap datasets (GRAB, HOI4D, OakInk), Something-Something V2 is indeed "in-the-wild" (real environments, varied objects, diverse lighting/backgrounds). The term is used in the relative sense common in the field and is not misleading.

- **"4.4k samples is modest for large-scale"**: This is subjective. For 3D HOI data with 92 intents and 610 object categories, 4.4k is a meaningful contribution. The scale is appropriate for the claimed scope.

- **"Cycle-consistency loss should cite prior uses"**: The harsh critic noted the loss is standard. The paper cites no prior use but the loss design is a reasonable application, not claimed as a novel invention. This is not a substantive weakness.

- **Generic strength from Strength Finder about "addressing an important problem"**: Too generic. Not included as a strength.

- **Strength about "the formulation of free-form HOI as a meaningful step"**: This is stated in my own terms in the strengths section.

- **Penetration metrics reported despite being "deceptively low"**: The paper itself acknowledges this caveat (Section 5.3) and correctly argues contact metrics are primary. This is a presentation choice, not a weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a quantitative external validation study: on a small subset (50-100 samples), obtain pseudo-ground truth via manual annotation or a different reconstruction pipeline and report MPVPE/contact IoU on that subset. This would directly address the circular-evaluation concern.
2. Ensure all baselines receive exactly the same TTA budget as TOUCH's refinement, or alternatively, make the primary comparison TTA-free for all methods and relegate the full refinement to supplementary.
3. Add confidence intervals (e.g., bootstrapped 95% CIs) to Table 1 and report the variance of the force-semantic contact-area analysis.
4. Provide full VLM evaluation details (model name, prompt template, scoring protocol) for reproducibility.
5. Add a sanity-check evaluation of the contact map prediction CVAEs against held-out ground truth contacts.

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration set):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `ZYwLfi50GI.md` (HOI-Diff) | 5.25 | Similar topic (text-driven HOI). TOUCH has stronger dataset contribution and more thorough ablations, making it slightly stronger. |
| `nTNElfN4O5.md` (IHDiff) | 5.50 | Hand-interaction domain. Comparable quality; TOUCH's task formulation and dataset are more novel contributions. |
| `Cf8HBieRzL.md` (UniContact) | 3.50 | Robotic contact synthesis. TOUCH is substantially stronger in evaluation depth, clarity, and methodological contribution. |
| `J4D5WVoc5g.md` (ViTaM-D) | 4.50 | Hand-object reconstruction with tactile sensing. TOUCH is better organized and has stronger ablations. |
| `DrhZneqz4n.md` (Single Motion Diffusion) | 7.50 | Strong paper with clear writing, thorough evaluation, and convincing results. TOUCH is not at this level — the evaluation lacks external validation and strong baselines. |
| `sn7CYWyavh.md` (Whole-Song Hierarchical Generation) | 7.25 | Strong accepted paper. TOUCH's evaluation is comparatively weaker (self-generated GT, limited baselines). |
| `8QTpYC4smR.md` (Systematic Review of LLMs) | 1.00 | Very weak paper. TOUCH is far stronger in every dimension. |

The paper makes real contributions — a novel task formulation, a well-designed three-stage framework with clear ablations, and a practically constructed dataset. However, the evaluation has meaningful limitations: it relies on self-generated ground truth without external quantitative validation, compares against only two adapted baselines, and has unspecified test-time optimization asymmetry. These gaps prevent the evidence from fully supporting the claimed contributions at a top-venue standard.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>