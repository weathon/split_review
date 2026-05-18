Now I have all the information needed to construct a thorough, verified review.

---

## Summary

This paper proposes UniVoxel, a unified voxelization framework for fast inverse rendering. It encodes a scene using two explicit voxel grids — an SDF field for geometry and a semantic field for materials/illumination — with lightweight MLPs for decoding. The key technical novelty is representing the incident light field via local Spherical Gaussians (SG) predicted from the semantic voxel grid, which avoids expensive multi-bounce ray tracing. On the MII synthetic dataset, UniVoxel reduces per-scene training time to 18 minutes (40× faster than MII, 12× faster than Nvdiffrec-mc) while achieving competitive or better PSNR/SSIM/LPIPS on novel view synthesis, albedo, roughness, and relighting.

## Strengths

1. **Dramatic optimization speedup with clear evidence.** The paper reports concrete training times: UniVoxel at 0.3 hours vs. 12 hours for MII and 4 hours for Nvdiffrec-mc (Table 1, with all baselines run on the same RTX 3090 as confirmed in Section 4.2). The 18-minute per-scene optimization is a genuine practical improvement over implicit and hybrid inverse rendering methods that require hours.

2. **Local SG illumination model eliminates multi-bounce ray tracing.** This is the paper's most novel component. By predicting SG parameters from the voxelized semantic field (Eq. 9, Section 3.4), UniVoxel jointly models direct lighting, indirect illumination, and light visibility without the expensive per-incident-direction visibility computation that prior explicit methods like TensoIR still require. The ablation study (Section 4.3) validates this design: the SG variant trains in 18 minutes while the environment map baseline takes up to 2 hours, and the SG model outperforms both Envmap and MLP (NeILF) variants on material quality.

3. **Competitive reconstruction quality across multiple benchmarks.** On the MII synthetic dataset, UniVoxel achieves leading or competitive numbers on NVS, albedo, roughness, and relighting (e.g., relighting PSNR 26.86 vs. 24.02 for TensoIR). Qualitative results (Figure 2) show high-frequency details preserved (text on balloons, nails on chair) where MII fails.

4. **Extension to varying illumination is clean and principled.** By adding a per-view learnable embedding to the SG prediction MLP (Eq. 11), the method naturally handles scenes with view-varying illumination. On the NeRD real-world dataset, UniVoxel produces plausible normals, albedo, and roughness where TensoIR fails due to environment-map limitations (Figure 4).

5. **Memory-efficient hash encoding variant strengthens the system.** UniVoxel(Hash) using multi-resolution hash grids achieves even higher relighting quality (27.72 vs. 26.86 PSNR) with modest additional computation (0.4 hours), demonstrating the framework's flexibility across memory/compute budgets (Section 3.3).

## Weaknesses

### Major

- **Missing quantitative comparison with Gaussian splatting–based inverse rendering methods (GS-IR, Relightable 3D Gaussian).** The paper mentions these methods in the related work (Section 2.2), dismissing them with a single sentence about "limited geometry quality," but provides no numerical or qualitative comparison on any dataset. Since these methods also achieve training times on the order of minutes and represent the most natural fast competitors, the paper's efficiency claims are unsubstantiated against the fastest alternatives in the literature. The omission is meaningful even though the paper's speed claims are specifically quantified against MII and Nvdiffrec-mc — the broader claim that UniVoxel achieves "favorable reconstruction quality compared to other state-of-the-art approaches" (abstract) requires validation against GS-based methods. The authors should include comparisons on at least the MII synthetic dataset, where ground truth is available, to show where UniVoxel stands relative to the current fastest alternatives.

- **No quantitative evaluation of geometry reconstruction on the main synthetic benchmark.** The paper reconstructs an SDF field as a core output and uses surface normals derived from it as a key input for rendering (Eq. 3, Section 3.2). Yet on the MII synthetic dataset — which has ground-truth geometry — the paper reports only appearance metrics (PSNR/SSIM/LPIPS for NVS, albedo, roughness, relighting) and no geometry metrics (e.g., Chamfer distance, F-score, normal angular error). While qualitative normal maps are shown and Shiny Blender results may exist in a stripped appendix section, the absence of geometry metrics on the primary benchmark means the "reconstruction quality" claim is evaluated only for appearance. Given the 160³ voxel resolution, it is important to verify that the geometry is not a bottleneck.

### Minor

- **The local SG illumination model lacks limitation analysis.** The paper uses 16 SG lobes per point (Section 4.2) but does not discuss under what conditions this might be insufficient (e.g., sharp shadows, concentrated indirect lighting, highly specular interreflections). The regularization losses (smoothing, white light penalty) are needed to mitigate material-lighting ambiguity, but no sensitivity analysis on the loss weights or number of SG lobes is provided. A dedicated discussion of failure cases — or a controlled experiment with known ground-truth illumination — would make the illumination contribution more credible. This is fixable and does not threaten the core claims.

- **The unified voxelization framework is presented as a core contribution but builds directly on established explicit representation designs (DVGO, NeuS).** The paper's first contribution — "unified voxelization of scene representation" — is essentially applying DVGO-style dense voxel grids (SDF field + semantic field) to inverse rendering, combined with NeuS-style SDF-based volume rendering. The novelty resides primarily in the local SG illumination model, not in the voxelization itself. The paper would benefit from sharper framing that acknowledges this and positions the contribution more precisely around the illumination modeling.

### Trivial

- The paper refers to Shiny Blender geometry results with a truncated section reference ("the results are presented in Sec." — line 227), suggesting a cross-reference to content that was not visible in the extracted text. If these results exist in the appendix, they should be referenced clearly in the main paper.

## Nice-to-Haves

- A sensitivity analysis on the number of Fibonacci-sampled incident directions (currently 128) and the number of SG lobes (currently 16) would strengthen the implementation section.
- Reporting quantitative novel-view-synthesis metrics alongside material metrics in the illumination ablation (Table 3) would provide a more complete picture — though this information may already exist in the stripped table.
- A formal limitations section at the end of the paper would improve credibility and is standard practice for this venue.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper does not state whether all baselines were run on the same hardware"* — **Removed.** The paper explicitly states at line 233: "We run all experiments on a single RTX 3090 GPU, and the training time of other baselines is measured on the same machine."
- *"Shiny Blender geometry results are missing"* — **Removed.** The paper states these results exist ("presented in Sec."); the content was likely in a section stripped during PDF-to-text extraction. Per policy, missing appendix/section content due to parsing is not a valid weakness.
- *"Would be informative to report PSNR/SSIM/LPIPS for novel view synthesis in the illumination ablation"* — **Removed.** The ablation table (`\input{tables/ablation_illum}`) was stripped during parsing and likely contains these metrics. This is a parser artifact, not an author omission.
- *Weaknesses about missing related work* — **Removed.** I cannot verify the existence of unmentioned related work without external sources.
- *Formatting/style nitpicks* — **Removed.** Parser artifacts are not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add quantitative comparisons with GS-IR and Relightable 3D Gaussian** on the MII synthetic dataset. This is the single most important improvement — without it, the efficiency claim is plausible but unverified against the most relevant fast competitors.
2. **Report geometry metrics (Chamfer distance, F-score, normal angular error)** on the MII synthetic dataset. The SDF field is a core component; its quality should be measured, not just visualized.
3. **Add a limitations paragraph** discussing when the 16-lobe SG model may be insufficient, the impact of regularization weights, and failure cases for the local illumination representation.
4. **Sharpen the framing** to acknowledge that the voxelization design follows DVGO-style explicit representations, and position the contribution as centered on the local SG illumination model integrated into explicit scene representations.

## Score and Decision

**Originality:** Moderate. The local SG illumination model integrated into an explicit voxel framework is novel. The unified voxelization itself is an engineering contribution building on established designs.

**Importance:** High. Fast inverse rendering is practically useful, and reducing training from hours to 18 minutes is a meaningful advance.

**Claims support:** Partially supported. The efficiency and appearance claims are well-supported, but the geometry quality claim lacks quantitative evidence, and the efficiency claim lacks comparison against GS-based methods.

**Soundness:** The methodology is sound. The ablation study is thorough. The main gaps are in evaluation breadth, not methodology correctness.

**Clarity:** The paper is clearly written and well-structured. Figures are informative.

**Value:** Good. The practical speedup and the illumination modeling approach are valuable contributions. The paper is on the border of accept strength due to the two major gaps, but both are fixable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>