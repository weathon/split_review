- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6
Now I have a complete understanding of both the paper and the reviewer inputs. Let me carefully evaluate each claim against the paper text and produce the final consolidated review.

---

## Summary

This paper presents Ref-Gaussian, a Gaussian splatting framework for high-quality novel view synthesis of reflective objects. The method combines (1) physically based deferred rendering using the Disney BRDF with split-sum approximation to avoid expensive Monte Carlo sampling, (2) a Gaussian-grounded inter-reflection module that uses ray-traced visibility (via extracted mesh and BVH) to separate direct and indirect specular light, where indirect light is modeled as a learned per-Gaussian spherical harmonics function, and (3) geometry-focused optimizations including 2D Gaussian primitives, per-Gaussian shading initialization, and material-aware normal propagation. Experiments are reported on Shiny Blender, Glossy Synthetic, and Ref-Real datasets.

## Strengths

- **First integration of visibility-based inter-reflection within a Gaussian splatting framework.** Section 3.2 formulates inter-reflection by decomposing the specular term into direct and indirect light (Eq. 9), computing binary visibility via ray tracing on a periodically extracted mesh with BVH acceleration, and modeling indirect lighting with per-Gaussian spherical harmonics (Eq. 10). The qualitative ablation in Figure 9 shows that removing this component degrades rendered reflections on the Tbell and Bell scenes. While the indirect term is learned rather than physically simulated, the combination of ray-traced visibility with a learned indirect component is novel within Gaussian splatting.

- **Physically based deferred rendering with split-sum approximation.** Section 3.1 replaces the Monte Carlo sampling used by prior Gaussian methods (e.g., RelightableGaussian) with a split-sum approximation (Eq. 8) and precomputed 2D lookup textures / cubemap series. This enables full Disney BRDF shading at the pixel level (after alpha-blending), which the ablation in Table 4 (per text description: "all quality metrics drop significantly") confirms is important.

- **Geometry-focused optimization techniques** including material-aware normal propagation (periodically scaling metallic/low-roughness Gaussians to propagate accurate normals, shown in Figure 10), per-Gaussian shading initialization (first 18k steps), and adoption of 2D Gaussian primitives (from 2DGS). Section 3.3 describes these clearly, and the paper reports ablation results showing their individual contributions.

- **Demonstrated downstream applications.** Section 4.3 and Figure 11 show relighting and material editing results, supporting the claim that the decomposed representation is practically useful.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Inter-reflection claim would benefit from more precise framing.** The abstract and introduction state that the method "realizes the desired inter-reflection function within a Gaussian splatting paradigm for the first time." As described in Section 3.2, the indirect component is a learned per-Gaussian spherical harmonics function (Eq. 10), not a physically simulated multi-bounce light transport computation from geometry and materials. The method does model inter-reflection (it accounts for occlusion and learns what radiance should appear in occluded directions), and the visibility computation is grounded. However, the framing could more explicitly acknowledge that the indirect term is a learned data-driven approximation rather than a physically computed quantity. This does not invalidate the contribution but would improve clarity.

- **Inter-reflection contribution lacks dedicated quantitative evaluation.** The paper's own text acknowledges (Section 4.2, line 199) that "inter-reflection is the minority in the glossy synthetic dataset. Its effect cannot be fully observed from Table 4." The primary supporting evidence is the qualitative comparison in Figure 9. Given that the inter-reflection module is listed as a main contribution alongside physically based deferred rendering, a quantitative evaluation on scenes where inter-reflection is the dominant effect (e.g., multiple reflective objects in close proximity) would substantially strengthen the paper's evidence. The ablation also does not compare against a baseline that simply uses higher-order view-dependent SH for the entire reflected radiance (without the visibility-based separation), which would isolate the benefit of the proposed decomposition.

- **Mesh extraction and ray-tracing overhead is not quantified.** The paper states that the object's surface mesh is periodically extracted using TSDF fusion every 3000 steps over 58,000 total training steps (Section 3.2, line 115; Section 4 implementation details). The efficiency claims ("rapid convergence," "real-time rendering") are supported by training time and FPS reportedly included in Table 2, but the computational cost of the mesh extraction and BVH-accelerated ray tracing is not broken out separately. This makes it difficult to assess how much of the training budget is consumed by these operations versus the core Gaussian optimization.

- **No limitations or failure case discussion.** The paper does not include a limitations section. Discussing scenarios where the method might struggle (e.g., complex topology where mesh extraction fails, scenes where the binary visibility approximation is inadequate, or cases where the learned indirect term cannot disentangle from direct lighting) would strengthen the paper's scientific rigor and help guide future work.

### Trivial

- The paper's contribution list (Section 1, point I) states "We strive to realize real-time high-quality rendering" — this is aspirational language for a contribution statement rather than a specific technical contribution.
- The captions for Tables 2 and 3 are partially truncated in the extracted text (line 205: "Table 3: Ablation studand efficiency" — appears to be a formatting artifact).

## Nice-to-Haves

- A standalone comparison against a "2DGS + BRDF" baseline (deferred PBR without the inter-reflection module) would further isolate the benefit of each component.
- Reporting per-scene PSNR/SSIM/LPIPS in a readable text table in the main paper (in addition to the image-based presentation) would improve accessibility.
- Confidence intervals or variance across runs are not standard for these benchmarks but would add rigor.

## Removed Points

These points from the reviewers were evaluated and removed per the review guidelines:

- **"Tables are illegible/quantitative evidence is inaccessible"** — Tables in the submitted PDF are readable; their inaccessibility in the text extraction is a parser artifact. Per the instructions: "formatting artifacts are parser errors, not author errors — the original submission does not have these issues." **Removed.**

- **"NeRO, NeuS, NDE comparisons missing from Table 1"** — The paper states (line 150) that it "also compared with more NeRF-based models like NeRO, NeuS and NDE." Whether these appear in Table 1 cannot be verified from the extracted text (the table is an image). Asserting their absence is speculative. **Removed.**

- **"Statistical significance not reported"** — Single-run evaluation on standard benchmarks is the norm in this field; demanding confidence intervals is beyond standard practice. **Moved to Nice-to-Haves.**

- **"The indirect term is not inter-reflection"** — This mischaracterizes the paper. The method does model inter-reflection: it computes visibility via ray tracing and learns a function to approximate the radiance in occluded directions. The approach is data-driven rather than physically simulated, which is a legitimate design choice in a Gaussian splatting context. The weakness about framing is retained above as minor; the assertion that it "is not inter-reflection" is factually incorrect. **Removed.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add a brief clarification in Section 3.2 that the indirect lighting term is a learned approximation (parameterized by per-Gaussian SH) — a sentence such as "Note that this indirect term is learned from data rather than physically computed, enabling efficient approximation of multi-bounce effects within the Gaussian splatting framework" would resolve the ambiguity.
- Include a dedicated quantitative evaluation on scenes with prominent inter-reflection (e.g., Table 4 could include a subset of such scenes with per-scene metrics for the inter-reflection ablation).
- Report the fraction of training time spent on mesh extraction and ray tracing (e.g., "mesh extraction added X% overhead").
- Add a limitations paragraph discussing when the binary visibility approximation, mesh extraction, or learned indirect term may break down.
- Move the quantitative tables to text format (or add a text fallback) so they remain accessible after PDF-to-text conversion.
