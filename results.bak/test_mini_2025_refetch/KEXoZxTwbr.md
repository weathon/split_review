Now let me write the final consolidated review.

## Summary

The paper presents MIRReS, a two-stage inverse rendering framework that reconstructs and optimizes explicit triangular meshes, PBR materials, and environment lighting from multi-view images. Its core contributions are (1) physically-based multi-bounce path tracing on a mesh for accurate indirect illumination estimation, and (2) reservoir-based resampled importance sampling (RIS) to reduce variance at low sample counts during direct lighting. The framework first extracts a coarse mesh from a neural SDF (NeuS2), then jointly refines geometry via trainable vertex offsets while optimizing materials and lighting through a differentiable PBR loop. Experiments on the TensorIR synthetic dataset and OWL real dataset show strong quantitative results, outperforming NVD-MC, TensorIR, and GS-IR across geometry, albedo, and relighting metrics.

## Strengths

1. **Multi-bounce path tracing for indirect illumination (Sections 4.2, Table 4).** The paper provides clear quantitative evidence that adding multi-bounce path tracing (without reservoir) raises albedo PSNR from 31.950 to 33.752 and relighting PSNR from 28.992 to 31.694. This is a genuine improvement over mesh-based methods like NVDiffrec-MC that do not model indirect illumination. Figure 4 visually demonstrates the indirect component decomposition.

2. **Reservoir sampling for variance reduction (Section 4.1, Figure 3, Table 4).** The use of reservoir-based RIS for direct lighting in an inverse rendering context is novel. Figure 3 shows that with only 1 sample per pixel, the reservoir-sampled rendering is nearly noise-free compared to standard MC. Table 4 confirms quantitative gains: adding reservoir sampling alone increases albedo PSNR from 31.950 to 32.529, and with multi-bounce from 33.752 to 34.348.

3. **State-of-the-art quantitative results (Tables 2 and 3).** On the TensorIR dataset, MIRReS achieves the best geometry (CD 0.056, N-MAE 3.305), albedo (PSNR 32.348, SSIM 0.970), and relighting (PSNR 32.363, SSIM 0.965). On the OWL dataset, it achieves the best relighting PSNR (28.827) and novel-view PSNR (38.223). The margins over TensorIR (the strongest baseline) are substantial — e.g., ~3 dB on albedo and ~3.8 dB on relighting on TensorIR.

4. **Stable mesh refinement via vertex offsets (Section 3.2).** Instead of DMTet (used by NVD-MC, which suffers from topological inconsistencies), the paper uses trainable vertex offsets that preserve mesh topology. This produces measurably better geometry: 23% lower Chamfer distance and 19% lower normal MAE relative to NVD-MC.

5. **Efficient training on a single GPU (Section 5.1).** The entire two-stage training completes in approximately 4.5 hours on a single RTX 4090, demonstrating practical feasibility despite multi-bounce path tracing.

## Weaknesses

### Major

- **Gradient detachment for indirect rays (Section 4.2, line 195).** The paper states: *"we detach the gradients of indirect rays due to the limited GPU memory."* This means the indirect illumination contributes to the rendering loss only as a fixed forward-pass term — parameters at secondary bounce points (materials, geometry) do not receive gradient signal through the multi-bounce pipeline. Consequently, the benefit of multi-bounce is primarily a better forward estimate of indirect light (reducing baked-in shadows) rather than end-to-end optimization of the full light transport. The ablation (Table 4) does not isolate whether the improvement comes from forward-pass accuracy or gradient-based learning. This is a significant limitation to the paper's central claim about multi-bounce enabling "more accurate intrinsic decomposition," and it is not discussed as a limitation in the paper.

### Minor

- **Reservoir sampling differentiability (Section 4.1).** The paper describes reservoir-based RIS (Eq. 9) but does not explain how gradients are propagated through the discrete resampling step. Standard implementations involve a non-differentiable selection; the paper mentions SLANG.D and custom CUDA kernels but gives no explanation of the mechanism (e.g., reparameterization, score-function estimator, or treating the resampling weights as detached). This leaves ambiguity about whether the direct lighting optimization is truly using the physical model in a gradient-correct manner.

- **Baseline configuration details not reported (Section 5.2).** The paper does not state whether baselines (NVD-MC, TensorIR, GS-IR) were run with their default settings or tuned for these datasets. Given that MIRReS benefits from a two-stage geometry initialization (NeuS2/InstantNGP), it is important to know whether baselines received comparable initialization or sufficient training. The large reported improvements make this a non-trivial concern.

- **Missing ablation on number of bounces (Section 4.2).** The paper uses three bounces by default but provides no analysis of how results change with 1, 2, or 3+ bounces. Such an ablation would directly inform the trade-off between computation and accuracy and validate the claim that multi-bounce beyond one bounce is beneficial.

- **NeuS vs NeuS2 inconsistency across datasets (Section 5.2).** For the OWL dataset, the paper uses NeuS (rather than NeuS2) for coarse mesh initialization, stating "we empirically find better quality." This means the coarse mesh quality is not uniformly controlled across datasets, and it suggests sensitivity to the first-stage initialization that is not discussed.

- **GS-IR performance on OWL is anomalously low (Table 3).** GS-IR's SSIM on OWL is 0.101 and PSNR is 18.761 — far below its TensorIR dataset performance (SSIM 0.941). While this may reflect a genuine limitation of GS-IR on this data, the extreme gap inflates the reported margin. At minimum, this should be acknowledged.

### Trivial

- The paper lacks a dedicated limitations section to discuss the gradient detachment, sensitivity to initialization, and memory footprint of multi-bounce path tracing.

## Nice-to-Haves

- A controlled experiment comparing training with and without detached indirect gradients (or comparing with a one-bounce indirect variant) would directly address whether the improvement from multi-bounce stems from forward-pass accuracy or genuine gradient-based learning.
- A training time breakdown (stage 1 vs stage 2) and comparison to baseline training times would be informative.
- Clarification on how GS-IR's normal MAE is computed if it "lacks mesh extraction."

## Removed Points

- *"First to support multi-bounce raytracing for indirect lighting is contestable"* — The paper's Table 1 clearly characterizes how prior methods handle indirect lighting. TensorIR uses second-bounce ray marching through radiance fields, not PBR path tracing. The paper's claim is appropriately scoped; Table 1 directly addresses this.
- *"If F_c is inaccurate, this could bias the mesh update"* — This is a generic concern applicable to any two-stage method and is not a specific identified flaw in the paper.
- *"Including a method that performs this poorly on one dataset inflates margin"* — Partially retained as a minor weakness above (GS-IR on OWL), but the harsh critic's framing as deliberate inflation is removed. The paper includes the metric honestly; the anomaly is worth noting but not a sign of bad faith.
- *"Pure formatting/style nitpicks"* — Removed as per instructions.
- Delusional strengths from Strength Finder — *"addressed an important problem"*, *"targeted an interesting question"* — These are generic and removed.

## Novel Insights

An interesting pattern across the two key findings is that the paper's strongest result — the multi-bounce indirect illumination — operates with detached gradients, meaning the improvement comes from a better *forward model* rather than backpropagation through indirect light transport. This is reminiscent of how differentiable rendering methods sometimes benefit more from low-variance forward estimates than from higher-order gradient terms. The reservoir sampling component similarly avoids the need for many Monte Carlo samples by using a learned proposal distribution. Taken together, the paper demonstrates that even without full end-to-end differentiation through indirect paths, explicit mesh-based path tracing with good forward estimators can substantially improve inverse rendering quality — a practically useful finding that is partially obscured by the paper's framing.

## Suggestions

1. **Acknowledge and analyze the gradient detachment limitation explicitly.** Add a dedicated discussion or ablation comparing detached vs. non-detached (or limited-bounce) variants. If detachment is imposed by memory constraints, state this and discuss potential remedies (e.g., gradient checkpointing, reducing sample count for indirect rays).

2. **Clarify how gradients flow through reservoir sampling.** A paragraph explaining the differentiable implementation (or noting that the resampling weights are treated as detached) would remove ambiguity about the direct-lighting optimization.

3. **Add an ablation on the number of bounces** (1, 2, 3) showing albedo PSNR, relighting PSNR, and training time for each setting.

4. **Report baseline configuration details** — whether default settings were used, whether comparable initialization was provided, and training durations.

5. **Add a limitations section** that transparently discusses gradient detachment, sensitivity to the first-stage initialization, and memory constraints.

## Score and Decision

**Round-1 bracket: 4.0–7.5.** The paper is clearly above weak-band papers (scores 2–3.4 on mesh-based inverse rendering topics) and below strong-band papers (scores 8+ on diffusion-based or large-model topics).

**Round-2 narrowing:** Six anchors in the 4.5–7.5 range were examined. The paper is comparable to Ref-Gaussian (6.5, Accept Poster) — both address indirect illumination for inverse rendering with similar contribution depth and evidence strength — and slightly below GI-GS (7.0, Accept Poster) because GI-GS does not have the gradient detachment limitation. The paper sits above UniVoxel (5.75, Reject) and Uni-IR (5.0, Withdrawn) in both technical contribution and experimental rigor.

**Final score: 6.5**

The paper has a genuine technical contribution (mesh-based multi-bounce + reservoir sampling) with strong empirical validation. The gradient detachment issue is a real limitation that tempers the central claim but does not invalidate the results — the forward-pass improvement alone is valuable. With transparent acknowledgment and an ablation addressing this, the paper would be a solid contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>