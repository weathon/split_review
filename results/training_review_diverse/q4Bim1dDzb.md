Now I have a thorough understanding of both the paper and the reviews. Let me construct the final consolidated review.

---

## Summary

This paper proposes UniVoxel, a method for inverse rendering that encodes scene properties into two explicit voxel grids — one for a signed distance field (geometry) and one for a semantic field (materials and illumination). Illumination is modeled by predicting per-point Spherical Gaussian (SG) parameters from the semantic field via lightweight MLPs, avoiding expensive multi-bounce ray tracing. The central claim is that training takes 18 minutes per scene (40× faster than MII, 12× faster than Nvdiffrec-mc) while achieving competitive or better reconstruction quality on both synthetic and real-world benchmarks.

## Strengths

- **Dramatic training speedup (18 minutes per scene):** The paper demonstrates that UniVoxel reduces per-scene training to 18 minutes — 40× faster than MII and over 12× faster than Nvdiffrec-mc (Abstract, Section 1, Section 4.3). This directly supports the core efficiency claim and is a significant practical advance over implicit methods.

- **Competitive reconstruction quality despite the speedup:** On the MII synthetic dataset, UniVoxel outperforms or matches NeRFactor, MII, Nvdiffrec-mc, and TensoIR across most metrics (PSNR, SSIM, LPIPS) for novel view synthesis, albedo, and relighting (Table 1, Section 4.3). The paper also shows qualitative results on real-world NeRD scenes where the method produces plausible normals and albedo maps where environment-map-based TensoIR struggles (Figures 4, 5).

- **Novel SG-based illumination modeling eliminates multi-bounce ray tracing:** The method models local incident light radiance with per-point Spherical Gaussians (Section 3.4), learning SG parameters from the same semantic field used for materials. This design enables joint modeling of direct lighting, indirect lighting, and light visibility without the expensive multi-bounce ray tracing required by environment-map-based approaches. Ablation results confirm this SG approach achieves better quality and shorter training time than environment-map, SH, or NeILF alternatives (Table 2).

- **Memory-efficient via multi-resolution hash encoding:** UniVoxel can optionally adopt multi-resolution hash encoding (Section 3.3) to achieve higher effective resolution with low memory cost. The "UniVoxel(Hash)" variant achieves higher relighting quality at only a minor training-speed trade-off (Section 4.3), demonstrating practical flexibility.

- **Extension to varying illumination conditions:** The method incorporates per-view embeddings (Section 3.4) to handle scenes captured under changing illumination. On challenging NeRD scenes with varying lighting, UniVoxel produces plausible reconstructions where environment-map-based TensoIR fails (Figure 5), showing a generalization advantage of the unified SG approach.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Speed comparison against the most relevant explicit baseline (TensoIR) is not explicitly quantified in the text.** The paper prominently reports "40× faster than MII" and "over 12× faster than Nvdiffrec-mc" (Abstract, Section 1), but does not give an equivalent speed-up ratio for TensoIR, which is the closest explicit competitor. TensoIR already trains in ~1–2 hours, so the gap to 18 minutes (~3–6×) is still meaningful but smaller than the improvement over implicit methods. Not stating this explicitly weakens the efficiency narrative. The table presumably contains this information, but calling it out in the text would significantly help readers judge the practical significance.

2. **The white-light regularization (`L_white`) is insufficiently evaluated on real-world data with colored illumination.** The method introduces a regularization that penalizes color shifts in incident light (Section 3.5), effectively assuming nearly white illumination. While the ablation shows this helps on synthetic data, the NeRD real-world dataset includes scenes with colored/varying lighting where this prior could bias the material-lighting decomposition (absorbing color shifts into albedo rather than lighting). The paper provides qualitative results on these scenes but **no quantitative metrics for decomposed albedo or material quality under colored lighting**. Without this, the method's generalizability to strongly colored real-world illumination remains uncertain.

3. **No discussion of failure cases or limitations.** The paper lacks a section (or even a paragraph) discussing scenarios where the method might struggle — e.g., scenes with strong interreflections, highly specular surfaces, extreme non-white lighting, or fine geometric detail below the voxel resolution. While the paper's contributions are clear, including a brief limitations discussion would strengthen the presentation and help guide future work.

4. **The number of incident light samples is fixed at 128 with no ablation.** The sampling resolution for incident lights is set to 128 Fibonacci-sphere samples (Section 4.2). This is a key hyperparameter affecting both quality and speed; varying this (e.g., 64, 256) would strengthen the evaluation of the SG representation's efficiency claim. [Moved to Nice-to-Haves — see below.]

### Trivial
None.

## Nice-to-Haves

- An ablation varying the number of incident light samples (e.g., 64, 128, 256) would strengthen the evaluation of the SG illumination model's efficiency claims. If 128 is sufficient, that is good evidence; if fewer suffice, the speed advantage grows.
- An explicit limitations paragraph or failure-case analysis would strengthen the paper's completeness.
- Adding quantitative metrics (PSNR/SSIM/LPIPS) for albedo and relighting on the NeRD real-world scenes would solidify the real-world evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Tables are stripped by the PDF parser, so core evidence is missing"** — Removed per instructions: this is a parser artifact (LaTeX `\input` commands), not an author error. The tables exist in the original submission.

2. **"The incident light field should be evaluated at the surface point, not at every ray sample; the paper does not clarify how SG parameters are combined"** — Removed as factually incorrect. The paper explicitly states (lines 155–157): "Then we obtain the h(r) along the camera ray r by the volume rendering shown in Eq. 4 with κ_i replaced by h(x_i). Thus, we can efficiently query incident light radiance from an arbitrary direction at a surface point." The integration is clearly specified.

3. **"The hash-based variant should be the primary method"** — Removed as an opinion/presentation preference; the dense grid version is a defensible baseline design choice, and the hash variant is presented as a flexible option.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful practical concern (white-light prior evaluation on colored real-world data) but do not introduce fundamentally novel perspectives beyond what the paper already discusses.

## Suggestions

1. **Explicitly state the speed-up over TensoIR** (e.g., "3–6× faster than TensoIR") in the abstract and introduction alongside the MII and Nvdiffrec-mc comparisons. This addresses the most natural reader question about efficiency gains over the closest explicit competitor.

2. **Add quantitative metrics for albedo and relighting on the NeRD real-world scenes** (or at minimum a discussion of the white-light prior's impact on scenes with colored lighting). If the white-light prior distorts albedo on scenes with strongly colored illumination, acknowledge this as a limitation.

3. **Add a brief Limitations paragraph** in the conclusion or as a separate subsection, covering: (a) reliance on the white-light assumption, (b) voxel resolution constraints on fine geometry, (c) potential issues with strong interreflections or highly specular materials.

4. **Clarify the caption/title of the speed comparison**: ensure the training time for TensoIR is called out in the running text so readers can directly compare without parsing the table.

## Score and Decision

This paper makes a clear, well-motivated contribution: a unified voxelization framework that jointly learns geometry, materials, and illumination for inverse rendering, with a novel per-point SG illumination model that eliminates multi-bounce ray tracing. The 18-minute training time is a genuine practical advance. The method is technically sound, the ablations are informative, and the experiments cover appropriate benchmarks. The weaknesses are minor and addressable (explicit TensoIR speed comparison, deeper evaluation of the white-light prior on real-world colored lighting, and a limitations discussion). The paper is ready for acceptance with these revisions.

**Score:** 7.5

**Decision:** Accept

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>