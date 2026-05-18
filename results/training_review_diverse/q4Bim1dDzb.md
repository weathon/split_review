Now I have verified all claims against the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes UniVoxel, a unified voxelization framework for inverse rendering that jointly learns geometry (SDF), materials (albedo, roughness), and illumination by encoding a scene into explicit voxel grids with lightweight MLP decoders. The key innovation is using local Spherical Gaussians (SGs) to model incident light radiance per 3D position, which avoids expensive multi-bounce ray tracing and integrates seamlessly into the voxelized representation. The method reduces per-scene training from hours to 18 minutes (claiming 40× over MII and 12× over Nvdiffrec-mc) while achieving competitive reconstruction quality on synthetic and real-world benchmarks.

## Strengths

1. **Drastic training time reduction with clear quantitative support.** The paper reports that UniVoxel reduces per-scene training to 18 minutes, with specific speedup factors (40× vs. MII, 12× vs. Nvdiffrec-mc) stated in both the contributions list (Section 1) and the experimental results (Section 4.3). These claims are accompanied by quantitative metrics (PSNR, SSIM, LPIPS) on the MII synthetic dataset showing competitive or superior quality at a fraction of the training cost.

2. **Unified illumination modeling via local Spherical Gaussians eliminates multi-bounce ray tracing.** The method predicts per-point SG parameters from the voxelized semantic field using a lightweight MLP (Eq. 7), enabling efficient querying of incident radiance from any direction. This design directly addresses the computational bottleneck of prior methods that require environment-map-based visibility computation or multi-bounce ray tracing. The ablation study in Section 4.4 (Table 2) quantitatively confirms that the SG-based illumination model is both faster and higher-quality than environment-map, SH, and MLP-based NeILF alternatives.

3. **Competitive reconstruction quality across diverse benchmarks.** On the MII synthetic dataset, UniVoxel "outperforms other methods in most metrics" (Section 4.3). On the NeRD real-world dataset, it produces plausible normals, albedo, and roughness, with qualitative comparisons against NeRFactor, MII, Nvdiffrec-mc, and TensoIR (Figures 3–5). The method handles both fixed and varying illumination conditions, the latter via learnable view embeddings (Section 3.4).

4. **Comprehensive ablation studies that validate key design decisions.** The paper ablates the illumination model (SG vs. envmap vs. SH vs. NeILF MLP) in Table 2 and individual loss terms (reconstruction, smoothness, white-light regularization, SG regularization) in Table 3. These ablations demonstrate the necessity of each component and isolate the efficiency/quality contributions of the proposed design.

5. **Memory optimization via multi-resolution hash encoding.** The paper recognizes the memory cost of explicit voxel grids and provides a hash-encoded variant (UniVoxel(Hash)) that achieves higher relighting quality at the cost of a slight decrease in speed (Section 4.3), showing practical flexibility.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Ambiguity in training-time comparison methodology.** The paper's central efficiency claim (40× over MII, 12× over Nvdiffrec-mc) depends on knowing exactly what is included in each baseline's reported training time. The paper states only that "the training time of other baselines is measured on the same machine" (Section 4.2). Several baselines have multi-stage pipelines (e.g., MII involves NeRF pretraining, Nvdiffrec-mc uses Monte Carlo sampling, TensoIR has its own coarse-to-fine schedule). The paper does not specify whether it used each baseline's official implementation with default settings, whether the reported times include all stages end-to-end (including pretraining), or whether the timing reflects single-seed runs. This ambiguity weakens the central speedup claim and should be resolved in a revision.

2. **Ad-hoc roughness correction without analysis.** The paper applies a 1.5 power correction to the predicted roughness during relighting, noting "the optimization bias towards higher roughness values" (Section 4.2). This correction is a post-hoc fix applied to compensate for a known bias in the learned representation, yet the paper provides no analysis of this bias, no ablation showing relighting results without the correction, and no physical justification for the 1.5 exponent. While this does not invalidate the overall contribution, it undermines confidence that the material decomposition is fully disentangled and that the roughness estimates are physically meaningful rather than compensation artifacts.

3. **Missing quantitative results for varying-illumination NeRD scenes.** On the three NeRD scenes captured under varying illumination, the comparison against TensoIR is limited to qualitative figures (Figure 5). The paper states that "TensoIR fails to recover the geometry and materials" but provides no quantitative metrics for these scenes (PSNR, SSIM, LPIPS, or relighting-specific metrics). Since handling varying illumination is presented as a key capability enabled by the view-embedding extension (Section 3.4), quantitative validation on these scenes would substantially strengthen this claim.

### Trivial

- The coarse/fine stage iteration count (10k each, fixed) is not ablated. A learning curve showing when the method converges relative to baselines, or an ablation on iteration count, would clarify whether the schedule was tuned and how robust the method is to this hyperparameter.

## Nice-to-Haves

- An ablation comparing the SG-light-field *with* voxelization against an MLP that directly predicts SG parameters from coordinates (without the voxelized semantic field). This would isolate the benefit of the voxelized representation from the SG representation itself. The paper's existing MLP(NeILF) baseline does not fully serve this purpose since NeILF uses a different architecture and task.
- Reporting GPU memory usage for the voxel grids (with and without hash encoding), and comparing against TensoIR's tensor-factorized memory footprint.
- Visualizing learned SG lobes (amplitudes, sharpness) at selected surface points as evidence that the SGs capture indirect illumination patterns rather than just direct lighting plus learned visibility.
- Specifying the number of training images per scene for the NeRD real-world dataset.

## Removed Points

These points from the reviews are excluded per the guidelines:

- **Missing supplementary / appendix content** (references to "Sec. C", truncated "results are presented in Sec."): The parser strips supplementary sections from all papers; these exist in the original submission. Per hard rules, this criticism is removed.
- **Few-view generalization concern** ("Real-world NeRD scenes have only 8–16 images? ... Generalizing to few-view settings is an important challenge"): The paper does not claim few-view reconstruction; this is a request to expand the paper's scope beyond its intended contribution.
- **"Ethiopian Head" geometry robustness question** ("Could the authors comment on whether UniVoxel's SDF-based geometry is more robust to that scene?"): This is a discussion question, not a weakness.
- **Efficiency breakdown suggestion** (break total time into forward/backward/loss/visibility components): This is a nice-to-have analysis, not a weakness. Already covered in Nice-to-Haves section above.
- **SG lobe visualization suggestion** (visualize lobes as evidence of modeling indirect illumination): Already covered in Nice-to-Haves above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful clarifications and ablation requests but do not identify a fundamentally new angle that the paper itself misses.

## Suggestions

1. **Clarify training-time methodology explicitly.** Add a paragraph in the experimental setup stating: (a) whether official implementations were used for each baseline, (b) whether the reported times include all stages (pretraining + main training) end-to-end, and (c) whether multiple seeds were run and, if not, that single-seed results should be interpreted accordingly.

2. **Analyze the roughness correction.** Show relighting results without the 1.5 power correction, provide a quantitative comparison, and either justify the correction physically or replace it with a principled approach (e.g., adding a roughness regularization term that directly penalizes the bias during training).

3. **Add quantitative metrics for varying-illumination experiments.** For the three NeRD scenes with varying illumination (Figure 5), report PSNR/SSIM/LPIPS for novel view synthesis and, where ground truth relighting is available, relighting-specific metrics. Even if ground truth under novel illumination is unavailable for real-world scenes, quantitative NVS metrics would strengthen the claim.

## Score and Decision

The paper presents a technically sound and practically meaningful advance in inverse rendering efficiency. The unified voxelization design is well-motivated, the SG-based illumination model elegantly avoids multi-bounce ray tracing, and the experimental results demonstrate substantial speed gains with competitive quality. The weaknesses identified are fixable with clarifications and additional analysis — none threaten the core contribution. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>