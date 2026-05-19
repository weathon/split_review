- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 8, 3, 6, 3
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes a method for novel view synthesis (NVS) from a single image that combines two paradigms: it uses a pretrained 3D-based NVS model (Zero123++) to generate weak guidance images, then integrates these into a 3D-free inference-time optimization pipeline (HawkI-style). A regularization loss aligning the optimized embedding with a CLIP text embedding of the target angle is introduced to improve viewpoint consistency. The method is evaluated on complex indoor/outdoor scenes (HawkI-Syn and HawkI-Real) against Zero123++, Stable Zero123, and HawkI, and shows consistent improvements across multiple metrics.

## Strengths

1. **Effective fusion of complementary NVS paradigms.** The paper presents a clean architectural insight: 3D-based models (Zero123++) provide camera-angle guidance but struggle with complex scenes and backgrounds, while 3D-free methods (HawkI) handle in-the-wild scenes but lack camera control. The proposed pipeline stitches these together, achieving better results on complex scenes than either family alone. Evidence: Table 1 shows the method outperforms both Zero123++ and HawkI on nearly all metric-dataset-angle combinations (22 out of 28), e.g., HawkI-Real (30°,270°) CLIP score 30.55 vs. 29.05 (HawkI) and 27.52 (Zero123++).

2. **Regularization loss consistently improves results across ablations.** The viewpoint regularization term \(L_{reg} = \|e_{view} - e_{target}\|^2\) is ablated across two datasets and four viewpoints. Table 2 shows it improves or ties on 12 of 14 metric-rows (e.g., HawkI-Real (30°,270°) LPIPS 0.5868 vs. 0.6114 without regularization). Figure 5 provides qualitative support showing improved texture and style consistency.

3. **Diagnostic analysis motivates design choices.** Section 3 provides controlled experiments showing (a) CLIP alone cannot generate consistent camera-controlled viewpoints without a guidance image (Figure 2), and (b) incorrect guidance images dominate the output regardless of text input (Figure 3). These experiments give clear, evidence-based rationale for why both 3D-prior guidance and the regularization term are needed.

4. **Comprehensive evaluation across multiple dimensions.** The method is evaluated on seven metrics (LPIPS, CLIP, DINO, SSCD, CLIP-I, PSNR, SSIM) across two datasets and four distinct viewpoints, providing a broad assessment of both fidelity and semantic consistency.

## Weaknesses

### Fatal
None.

### Major
None that are truly major in the sense of invalidating the paper's core claims. The issues below are significant gaps in evidence but addressable.

### Minor

1. **View-CLIP score is listed as a metric but never reported.** The paper introduces the View-CLIP Score as a metric "focused specifically on the viewpoint" (line 177) and states it should be evaluated. However, it appears in none of the tables. Since the paper's core claim is about camera-controlled viewpoints, this is a missed opportunity to directly validate that claim. The CLIP score (which the paper notes assesses both content and viewpoint) is reported, providing partial evidence, but a dedicated viewpoint metric would substantially strengthen the camera-control claim.

2. **The relationship between the CLIP-analysis and the regularization loss needs clarification.** Section 3.1 states CLIP "falls short in grasping specific angles, like 30 degrees upward" and "cannot independently generate consistent viewpoints." While the paper does *not* claim CLIP has zero angle information—it says CLIP handles "general directions (such as up, down, left, and right)"—the transition from "CLIP alone is insufficient for camera control" to "using CLIP text embeddings as regularization targets" is underspecified. The paper would benefit from explaining what signal the text embedding of "View from an elevated angle of +30 degrees" actually carries and why aligning toward it (even if imperfect) helps. This is not a contradiction (the guidance image from Zero123++ is the primary control mechanism; the CLIP regularization is auxiliary), but the current framing invites confusion.

3. **No variance or error bars reported.** All quantitative results are single numbers without standard deviations. Given the stochasticity of diffusion inference and multi-step optimization, it is unclear whether small gaps (e.g., LPIPS 0.5661 vs. 0.5694, or DINO 0.3346 vs. 0.3315) are meaningful or within noise range. Reporting statistics over multiple runs would strengthen confidence.

4. **No runtime / computational cost reported.** The method requires four optimization stages per scene-viewpoint (text embedding optimization on \(I_{input}\), UNet fine-tuning, text embedding optimization on \(I_{view}\), and UNet fine-tuning with regularization), plus inference with mutual information guidance. Without any runtime characterization, readers cannot assess the practical trade-off between the quality gains and the inference cost. The paper acknowledges this is a limitation qualitatively (line 271) but provides no quantification.

5. **Limited angle range tested.** Due to Zero123++'s fixed-view design, the method is evaluated on only four predetermined view combinations. While this is an acknowledged limitation of the 3D prior model rather than the proposed pipeline, the paper's claims about "precise camera control" would be strengthened by demonstrating the approach on a denser or continuous range of angles.

### Trivial
- The "5.2× improvement" claim in the introduction (line 30) compares the paper's LPIPS gap against Zero123++'s self-reported gap from a different dataset. This framing is non-standard and the number cannot be verified from data presented in the paper. Consider simplifying this claim to the direct comparison against baselines shown in Table 1.

## Nice-to-Haves
- Including Free3D or another recent baseline for comparison breadth (mentioned in related work but not evaluated).
- A failure-mode analysis or discussion of cases where the method degrades below baselines.
- Ablating the use of Zero123++ versus a simpler init (e.g., using the input image directly) to isolate the contribution of the 3D prior versus the optimization framework itself.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Internal contradiction" about CLIP (harsh critic's Point 1, framed as critical):** The critic claims the paper contradicts itself by arguing CLIP cannot understand angles while using CLIP text embeddings for the regularization loss. However, the paper claims CLIP "falls short in grasping *specific* angles" and is "inadequate for generating camera-controlled views on *its own*" — a nuanced position about insufficient standalone precision, not a claim of zero signal. The regularization loss is an auxiliary signal within a pipeline whose primary control comes from the Zero123++ guidance image. The claimed "contradiction" overstates the paper's position. Demoted to Minor (point 2 above) with a softened framing.

- **"Comparison fairness" (harsh critic's Point 3):** The critic argues that comparing against Zero123++ is of "limited diagnostic value" because the method uses Zero123++ as a component. This is a standard concern for any method built on top of a baseline, but the paper addresses it through ablations (Table 2 isolates the regularization loss) and by comparing against *both* Zero123++ and HawkI separately. The comparison is standard practice and not unfair. Removed.

- **Missing related work comparisons (Free3D, MVDream):** The paper mentions Free3D in related work but does not compare against it. While additional baselines would strengthen the evaluation, requiring a comparison against every mentioned method is scope creep. The paper already evaluates against three strong baselines. Removed per soft rule on scope.

- **Several of the "Strengthening the Paper on Its Own Terms" suggestions:** These are speculative suggestions about how to reformulate the approach (e.g., "learn a lightweight mapping from angle parameters to CLIP space"), not weaknesses in the current paper. Moved here.

- **Strength Finder's claim that regularization "successfully injects 3D angle information into CLIP space":** This phrasing is somewhat speculative — the ablation shows metric improvements but doesn't directly prove angle information is being "injected" into CLIP space. The core observation (regularization helps) is retained in Strengths with more precise wording.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unexpected angle that changes the interpretation of the work.

## Suggestions

1. **Report View-CLIP scores.** Since this metric is already listed in the evaluation setup, populating the tables with it would directly support the camera-control claim at minimal cost.
2. **Clarify the role of the CLIP text-embedding regularization.** Add a sentence or two explaining that CLIP text embeddings capture coarse directional information (up/down/left/right), and the regularization nudges the optimized embedding toward this coarse directional signal — even if imprecise, this auxiliary signal improves consistency when combined with the guidance image.
3. **Add error bars or standard deviations** over at least 3 runs for the main quantitative comparison to establish that the reported gains are reproducible.
4. **Report inference time** per image (with breakdown across the four optimization steps) to help readers gauge practical applicability.
5. **Simplify the "5.2× improvement" claim** — the direct comparisons in Table 1 are more informative than this cross-paper gap comparison.
