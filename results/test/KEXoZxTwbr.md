Now I have a thorough understanding of the paper and can verify all claims. Let me compose the consolidated review.

## Summary

This paper presents MIRReS, a two-stage inverse rendering framework that jointly optimizes explicit triangle mesh geometry, spatially-varying materials, and environment lighting from multi-view images. The key technical components are: (1) two-stage mesh optimization (extracting a coarse mesh from a neural SDF, then refining it with trainable vertex offsets), (2) physically-based multi-bounce path tracing for indirect illumination estimation on the explicit mesh, and (3) reservoir-based spatiotemporal importance resampling (ReSTIR) for low-noise direct illumination. Experiments on the TensoIR and OWL datasets show strong quantitative results against TensoIR, GS-IR, and NVdiffrec-MC baselines.

## Strengths

1. **Stable mesh optimization via two-stage refinement.** The paper addresses a real problem in mesh-based inverse rendering: NVdiffrec-MC-style DMTet optimization suffers from topological instabilities that make multi-bounce path tracing intractable. By starting from a coarse mesh extracted from NeuS2 and refining it with trainable vertex offsets guided by both radiance-field and PBR losses, the method achieves stable geometry that supports path tracing. This is supported by the geometry metrics in Table 2 (best chamfer distance 0.0156 and normal MAE 0.217) and qualitative results in Figure 5.

2. **Integration of reservoir sampling for direct illumination in inverse rendering.** Applying spatiotemporal reservoir resampling to direct lighting estimation during inverse rendering optimization is a practical contribution that reduces rendering noise at low sample counts, enabling faster convergence. The ablation in Table 4 confirms its contribution (albedo PSNR drops from 27.24 to 26.12 when removed), and Figure 3 provides a visual demonstration of noise reduction.

3. **Strong empirical performance.** On the TensoIR dataset (Table 2), MIRReS achieves best or second-best scores across all metrics (albedo PSNR 30.02, relighting PSNR 29.70, novel view PSNR 36.15, chamfer distance 0.0156, normal MAE 0.217), consistently outperforming TensoIR, GS-IR, and NVdiffrec-MC. Results on the OWL dataset (Table 3) similarly show advantages in relighting and novel view synthesis.

4. **Explicit mesh output.** The method produces a refined triangular mesh with materials and lighting that can be directly imported into standard graphics pipelines, which is a practical advantage over implicit representations.

## Weaknesses

### Fatal
None.

### Major

1. **Gradient detachment for indirect rays (Section 4.2).** The paper states (line 243): "we detach the gradients of indirect rays due to the limited GPU memory." This means the multi-bounce path tracing for indirect illumination does **not** contribute gradients to the optimization of geometry, materials, or lighting — it is evaluated only in the forward pass. The paper's central claim is that multi-bounce path tracing improves the intrinsic decomposition. While the ablation (Table 4) does show an improvement when multi-bounce is enabled (albedo PSNR 27.24 vs 26.12 without), the mechanism of this improvement is unclear: it could come from more accurate forward-pass rendering providing a better training signal for direct-component gradients, or from secondary effects through the radiance field loss \( \mathcal{L}_{\mathrm{RF}} \). The paper does not discuss this limitation or analyze the mechanism, which weakens the attribution of benefit. This does **not** invalidate the overall results — the multi-bounce forward pass still prevents the optimization from baking shadows into albedo — but it means the paper overstates what the multi-bounce component actually contributes to optimization.

2. **Overclaim of novelty in multi-bounce path tracing (Section 2.2).** The paper states (line 107) that it is "the first inverse rendering framework that supports multi-bounce raytracing to estimate indirect lighting more accurately." However, the paper's own related work discussion (line 18) notes that TensoIR "enabl[es] explicit second-bounce ray marching online." TensoIR traces secondary rays for indirect illumination, albeit using radiance fields rather than physically-based rendering. The claim of being "first" is inaccurate. The actual novelty is better described as combining physically-based multi-bounce path tracing with stable mesh optimization — a narrower but defensible contribution. The paper also claims NVdiffrec-MC uses only "single-bounce raytracing" (Table 1), but NVdiffrec-MC's title ("Monte Carlo rendering and denoising") and the paper's own references to its path tracing indicate it can trace multiple bounces; the difference is in geometry representation stability, not the presence of multi-bounce tracing per se. These overclaims should be corrected.

3. **Temporal reuse in reservoir sampling without justification during optimization (Section 4.1).** The paper states (line 217) that it "exploit[s] spatial reuse and temporal reuse, incorporating samples from neighboring pixels and previous frames as candidates." ReSTIR's temporal reuse (Bitterli et al. 2020) was designed for static scenes or slowly varying direct lighting. During optimization, the environment map, material parameters, and mesh vertices all change every iteration. The paper does not address whether temporal reuse remains valid (unbiased) under this setting, or whether it introduces bias that could affect optimization quality. This is a significant methodological gap that needs clarification. If temporal reuse is disabled, the claimed benefit is reduced; if it is used, a justification is required.

### Minor

4. **Ablation study limited to albedo PSNR (Table 4).** The ablation examines only albedo PSNR. The effect of removing multi-bounce path tracing or reservoir sampling on geometry (normal MAE, chamfer distance), indirect lighting quality, and relighting is not reported. A more comprehensive ablation would strengthen the causal attribution.

5. **Uncontrolled initialization advantage.** The paper uses a two-stage initialization (InstantNGP + NeuS2) before the second-stage optimization. The baselines (TensoIR, GS-IR, NVdiffrec-MC) do not receive this initialization. While this is a legitimate part of the proposed pipeline, the paper does not isolate how much of the improvement comes from the initialization vs. the second-stage path tracing components (e.g., by running the second stage on a mesh from a different source). The "state-of-the-art" claim is plausible but not fully controlled.

6. **Missing discussion of scale ambiguity resolution.** The paper mentions using a global scalar scaling strategy for albedo (Section 5.1), following TensoIR, but does not discuss how the inherent scale ambiguity between albedo and lighting intensity is resolved during optimization, or whether the environment map is initialized from scratch vs. from an HDR capture.

7. **No ablation of bounce depth.** The paper limits tracing to three bounces but provides no ablation showing the marginal benefit of 1 vs. 2 vs. 3 bounces. This would help quantify the practical contribution of deeper tracing.

### Trivial

8. **Denoiser details are omitted.** The paper mentions an edge-avoiding à-trous wavelet transform denoiser (inspired by NVdiffrec-MC) and "directional clamping technique" but provides no specifics or ablation of the denoiser's impact.

9. **No runtime breakdown.** The paper claims "considerable acceleration" but provides no breakdown of per-component runtime or sample-count comparisons with baselines.

## Nice-to-Haves

- A discussion of failure modes: cases where Stage 1 produces a poor coarse mesh (e.g., highly specular or transparent objects) and how the method behaves under those conditions.
- Training time and sample count comparisons with baselines to substantiate the acceleration claim for reservoir sampling.
- A controlled experiment that isolates the two-stage initialization effect from the path tracing improvements.

## Removed Points

- *"Criticism about missing related works (Ref-NeuS, Neural-PIL, INV, Zhang et al. 2023)."* — The paper compares against three representative baselines across different representation categories; demanding an exhaustive list is scope creep and would make the paper broader rather than stronger.
- *"Reproducibility concerns about unreleased artifacts / undisclosed hyperparameters" and "missing appendix/proofs."* — The parser strips appendices; these are parser artifacts, not author omissions.
- *"LaTeX formatting artifacts in equations."* — These are parser extraction issues, not author errors.
- *"Typo/grammar/formatting nitpicks."* — Parser artifacts.
- *"The paper should also cover Y / domain Z / additional tasks."* — Scope creep beyond the paper's stated direction.
- *Strength Finder generic strengths without specific content.* — Dropped generic strengths that lacked specific citation or concrete content (e.g., "addressed an important problem").

## Novel Insights

The reviews surface an interesting tension: the multi-bounce path tracing improves decomposition results even with detached gradients. This suggests that the primary benefit of physically-accurate indirect illumination in inverse rendering may come from the forward pass providing a more faithful decomposition of observed radiance into direct and indirect components, preventing the optimization from baking shadows and inter-reflections into albedo or roughness — rather than from gradient signals flowing through indirect light paths. This distinction (forward-pass accuracy vs. backward-pass gradients) is worth making explicit and could guide future work: a method that only uses single-bounce with a learned indirect term might approximate the same benefit if the forward pass is sufficiently accurate, potentially at lower cost.

## Suggestions

- **Discuss the gradient detachment explicitly.** Acknowledge that indirect-ray gradients are detached and analyze why multi-bounce still helps (e.g., better forward-pass separation of direct/indirect components reduces material-lighting ambiguity). Consider showing optimization trajectories with and without detached gradients to confirm the benefit mechanism.
- **Correct the novelty claim.** Replace "first multi-bounce raytracing framework" with a precise description of what is new: stable mesh-based physically-accurate multi-bounce path tracing, or the specific combination of techniques.
- **Clarify or disable temporal reuse.** Either justify why temporal reuse remains approximately valid under optimization (e.g., slow parameter change, empirical bias analysis) or switch to spatial-only reuse and report the impact.
- **Add controlled ablations:** bounce depth (1 vs. 2 vs. 3), geometry metrics in the main ablation, the effect of the two-stage initialization vs. the path tracing components.
- **State whether the environment map is initialized** (from HDR capture?) or learned from scratch, and how albedo-lighting scale ambiguity is resolved.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>