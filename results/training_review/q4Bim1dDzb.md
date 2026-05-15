Now I'll produce the final consolidated review.

---

## Summary

This paper proposes UniVoxel, a framework that accelerates inverse rendering by representing scene properties (geometry, materials, illumination) using explicit voxel grids rather than implicit neural fields. The key idea is to jointly voxelize an SDF field and a semantic field, from which geometry (normals, opacity), materials (albedo, roughness), and illumination (per-point Spherical Gaussians) are decoded by lightweight MLPs. The method achieves per-scene training times of 18 minutes on tested benchmarks (MII synthetic, NeRD real-world), a substantial speedup over prior work.

## Strengths

- **Significant optimization speedup**: The paper demonstrates per-scene training in 18 minutes on an RTX 3090, which is substantially faster than reported times for MII, Nvdiffrec-mc, TensoIR, and NeRFactor on the same hardware. The ablation studies further confirm the efficiency benefit of the proposed SG-based illumination model over environment-map alternatives (which take up to 2 hours).

- **Unified explicit voxelization framework**: Jointly voxelizing the SDF and semantic fields into a single explicit representation is a clean design that avoids the complexity of training separate deep MLPs for each scene property. Surface normals are derived directly from the SDF grid via finite differences, and materials/lighting are decoded by 3-layer MLPs — this architectural simplicity is the core enabler of the speed gains.

- **Per-point SG illumination avoids multi-bounce ray tracing**: Predicting per-position Spherical Gaussian parameters from the semantic field (Eq. 9) allows incident radiance to be queried without expensive ray tracing during training. The ablation study (Table `ablation_illum`) validates that this approach achieves competitive or better quality than environment-map and NeILF baselines while being significantly faster.

- **Extension to varying illumination**: The view-embedding mechanism (Eq. 10) is a simple yet effective way to handle scenes captured under different lighting conditions. Qualitative results on three NeRD scenes with varying illumination show plausible relighting where TensoIR fails, demonstrating practical value for real-world capture scenarios.

- **Comprehensive ablation on illumination models**: Table `ablation_illum` systematically compares the proposed SG-based illumination against environment maps (SG mixture and pixel-based), NeILF, and Spherical Harmonics, providing useful evidence for the efficiency-quality trade-offs of each design choice within the UniVoxel framework.

## Weaknesses

### Fatal

None.

### Major

1. **Overclaimed scope of the illumination model.** The paper repeatedly claims that per-point SGs "model the joint effects of direct lighting, indirect lighting and light visibility efficiently without expensive multi-bounce ray tracing" (abstract, introduction, Section 3.3). This is a non-trivial theoretical assertion: the SG parameters are predicted from *local* semantic features at point **x**, yet indirect lighting and visibility are inherently non-local phenomena requiring information about distant occluders and light paths. The method learns a per-position light field approximation that can capture scene-specific correlations but provides no mechanism for physically correct global illumination. The paper offers no analysis of when this approximation might fail (e.g., scenes with strong occlusions, small light sources, or significant multi-bounce interreflections), and the experiments are conducted on scenes with relatively simple lighting (MII synthetic, NeRD real-world). This overstatement of the illumination model's capability risks misleading readers about what the method actually achieves.

2. **Lack of quantitative geometry evaluation in the main paper.** Despite the availability of ground-truth geometry for the MII synthetic dataset, no quantitative geometry metrics (e.g., Chamfer distance, F-score, normal accuracy) are reported in the main text. The paper mentions experiments on the Shiny Blender dataset for geometry comparison (line 227–228), but these results are deferred to an appendix. For an inverse rendering paper that claims "favorable reconstruction quality," the absence of any geometry metric in the main evaluation body is a significant omission that weakens the core contribution.

3. **Potential inconsistency in the headline speedup claim.** The abstract and introduction claim "40× faster than MII and over 12× faster than Nvdiffrec-mc." Per the reviewer's report, Table 1 shows MII at 360 minutes and UniVoxel at 18 minutes, giving a 20× (not 40×) speedup. While I cannot independently verify the table data (the input files are not available in the extracted text), the 40× claim in the introduction should be consistent with the actual numbers reported in the paper's own table. (Note: the "over 12× faster than Nvdiffrec-mc" claim is not contradicted — if the actual speedup is ~22×, then "over 12×" is a true, if conservative, statement.) The authors should verify and correct this discrepancy.

### Minor

1. **Real-world varying-illumination comparison is limited.** On the three NeRD scenes with varying illumination, the paper compares only against TensoIR, which is known to use fixed environment maps and would be expected to struggle in this setting. While demonstrating that UniVoxel succeeds where TensoIR fails is informative, additional comparisons against methods designed for varying illumination (or an adapted baseline) would better substantiate the claim of handling complex real-world illumination.

2. **Marginal benefit of the SG regularization loss.** The ablation study (Table `ablation_loss`) shows that the L_sg regularization improves albedo PSNR marginally (26.56 → 26.62) while slightly degrading NVS and roughness metrics. The paper states it "improves the quality of albedo," which is technically true but overstates the practical significance of such a small gain. The narrative should be more measured.

3. **UniVoxel vs. UniVoxel(Hash) distinction could be clearer.** The paper describes both a dense voxel grid (96^3 → 160^3) and a multi-resolution hash encoding variant, but does not clearly state which configuration achieves the 18-minute result or how the two variants compare in terms of memory and speed. The relationship is mentioned in passing (line 260–261), but explicit attribution of the headline time to a specific configuration would improve transparency.

### Trivial

None.

## Nice-to-Haves

- **Test on scenes with genuine global illumination effects** (e.g., sharp shadows, occluded light sources, color bleeding) to validate whether the per-point SG field can actually approximate indirect lighting, as claimed. The current datasets (MII, NeRD) have relatively simple lighting.
- **Visualize learned SG lobes** (direction, sharpness, color) at different positions to provide insight into what the illumination representation captures.
- **Cite and discuss relevant recent work** on explicit representations for inverse rendering (GS-IR, Relightable 3D Gaussian, Neural-PBIR) that the paper already references but does not compare against quantitatively (Section 2 mentions them but experiments omit them).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the "12× claim is contradicted by the authors' own table"** — The critic claims 390/18 ≈ 21.7× contradicts "over 12×." This is incorrect: 21.7× is greater than 12×, so "over 12×" is a true (conservative) statement. Removed as factually wrong.
- **Criticism about missing section references ("presented in Sec.")** — These incomplete references (lines 228, 232) are almost certainly parser artifacts where LaTeX cross-references (`\cref{...}`) were stripped. Per instructions, such artifacts should not be treated as author errors. Removed.
- **Complaint about the relationship between coarse and fine stages and the 18-minute timing** — The paper clearly states 10k iterations in both stages (20k total, line 232). The critic's request for clarification is already answered by the text. Removed.
- **Formatting/style nitpicks and speculative "missing" criticisms** — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the method that the authors themselves have not already articulated.

## Suggestions

1. **Correct the speedup numbers** if they are inconsistent with Table 1. If the 40× claim is relative to the MII paper's originally reported time (e.g., ~12 hours) rather than the re-run time in the table, state this explicitly.
2. **Add quantitative geometry metrics** (Chamfer distance, F-score, or normal accuracy) to the main paper's evaluation, either from the MII synthetic dataset or from the Shiny Blender results currently deferred to the appendix.
3. **Tone down the claims about the illumination model** "modeling" global illumination. The paper should explicitly discuss that per-point SGs learn an approximation of the incident light field that captures scene-specific correlations, and acknowledge that the method has not been tested on scenes requiring physically correct global illumination.
4. **Add a discussion of limitations** covering when the method might fail (complex shadows, scenes with strong indirect lighting, small light sources) — this is standard practice that would strengthen the paper.
5. **Clarify which variant achieves 18 minutes** (dense grid vs. hash encoding) and provide memory footprint comparisons.

## Score and Decision

The paper presents a well-motivated approach with clear practical merit (substantial speed improvements on standard benchmarks). The core contribution — unified explicit voxelization with per-point SG illumination — is solid, and the ablations provide useful evidence. However, the paper suffers from three significant issues: (1) overclaimed theoretical scope of the illumination model, (2) missing quantitative geometry evaluation in the main paper, and (3) a potential inconsistency in the headline speedup figure. These are addressable in revision but non-trivial. On balance, the paper represents a useful contribution to the inverse rendering community, but the overstatements and omissions prevent acceptance in its current form.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>