Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper introduces Ref-Gaussian, a Gaussian splatting framework for reconstructing and rendering reflective objects. The method combines physically based deferred rendering (using split-sum approximation of the rendering equation applied on pixel-level material maps) with an inter-reflection component (a learned view-dependent residual modulated by ray-traced visibility on a periodically extracted mesh). The framework also incorporates geometry-focused optimization, including 2D Gaussian primitives, material-aware normal propagation, and per-Gaussian shading initialization. Experiments on three reflective datasets (Shiny Blender, Glossy Synthetic, Ref-Real) show that Ref-Gaussian outperforms prior NeRF- and GS-based methods on quantitative metrics and visual quality while maintaining real-time rendering speeds.

## Strengths

- **Physically based deferred rendering in a Gaussian splatting pipeline.** The paper formulates pixel-level material aggregation (albedo, metallic, roughness, normal) via alpha-blending and applies the split-sum approximation (Eq. 8) to evaluate the rendering equation efficiently. This replaces the simplified shading functions used in prior GS inverse-rendering methods (e.g., 3DGS-DR, GaussianShader). Quantitative results in Table 1 confirm the benefit across reflective scenes, and the ablation in Table 4 shows that removing deferred rendering degrades all metrics.

- **Novel combination of ray-traced visibility with a learned indirect residual.** The method computes binary visibility via ray tracing on an extracted mesh and models the indirect component as an SH-based learned per-Gaussian color weighted by (1−V) (Eq. 9–10, Section 3.2). While this is an approximation rather than a physics-grounded inter-reflection integral, it contributes to noticeable qualitative improvements on scenes with occlusion in the specular direction (Figure 9), and the approach is more efficient than Monte Carlo sampling used by RelightableGaussian.

- **Geometry-focused optimization strategies.** The material-aware normal propagation (expanding Gaussians with high metallic / low roughness) and the initial per-Gaussian shading stage are well motivated and quantitatively ablated (Tables 3–4). The paper shows that removing either component degrades normal reconstruction and rendering quality (Figure 10), providing direct evidence of their effectiveness.

- **Strong empirical performance on reflective scenes.** On Shiny Blender and Glossy Synthetic, Ref-Gaussian achieves top PSNR/SSIM/LPIPS across the majority of scenes against six baselines, with particularly clear gains on the more challenging Glossy Synthetic dataset. The method also demonstrates real-time rendering (FPS reported in Table 2) and fast convergence.

## Weaknesses

### Major

- **Unsupported claim of "unified solution for both reflective and non-reflective scenes."** The abstract and contribution list (lines 4, 16) explicitly claim the method works for non-reflective scenes. However, *every* experiment is conducted on reflective datasets (Shiny Blender, Glossy Synthetic, Ref‑Real). No evaluation on standard non‑reflective benchmarks (e.g., Mip‑NeRF 360, DTU, Tanks‑and‑Temples) is provided. This claim therefore lacks evidential support and must either be removed or substantiated with experiments. This is the most significant flaw because it is a central assertion in the paper's framing.

- **Framing of the inter‑reflection component overstates its physical grounding.** The paper repeatedly claims to "realize the intricate inter-reflection function" and that this is done "for the very first time" in Gaussian splatting (lines 4, 14). In practice, the indirect component is a per‑Gaussian view‑dependent color represented by spherical harmonics that is alpha‑blended into an indirect lighting map and weighted by (1−V), where V is a binary visibility flag from ray tracing. This is a **learned residual** that can absorb any view‑dependent effect not captured by the direct specular term — it is not a physically integrated inter‑reflection. Moreover, RelightableGaussian (Gao et al., 2023) already models inter‑reflection effects in Gaussian splatting (acknowledged in lines 12, 29). While the authors' specific formulation (split‑sum + learned residual + mesh‑based visibility) has merit, the "first ever" claim is inaccurate, and the "inter‑reflection" framing should be adjusted to a learned approximation. This does not invalidate the empirical results but misrepresents their nature.

- **Mesh extraction from 2D Gaussians is underspecified.** The method relies on periodically extracting a surface mesh from the Gaussian representation for ray‑tracing visibility (Section 3.2, line 115): "we periodically extract the object's surface mesh using truncated signed distance function (TSDF) fusion." How the TSDF is constructed from 2D Gaussian primitives (e.g., rendering depth maps followed by volumetric fusion, or Poisson reconstruction from splat centers) is not described. This is a key component for reproducibility — without it, the visibility computation cannot be replicated, and the sensitivity to TSDF resolution and fusion parameters is unknown. A brief description of the pipeline would suffice.

### Minor

- **Material‑aware normal propagation thresholds are ad‑hoc and the "strong positive correlation" is unsubstantiated.** The paper sets thresholds of metallic ≥ 0.02 and roughness ≤ 0.1 (line 154) and claims "a strong positive correlation between normal accuracy and high metallic, low roughness properties" (line 129) without any quantitative correlation analysis. A sensitivity analysis over these thresholds would strengthen confidence.

- **Spherical harmonics substitution for integrated diffuse lighting is not justified.** The paper mentions in Implementation Details (line 154) that "spherical harmonics have a better fitting capability than the integrated diffuse lighting and we thereby use spherical harmonics to substitute it." This substitution affects the physical interpretability of the diffuse term but is not motivated, ablated, or discussed in the main method section. An ablation comparing SH vs. pre‑integrated diffuse would clarify the trade‑off.

- **No quantitative ablation of the inter‑reflection component.** The paper acknowledges that "inter-reflection is the minority in the glossy synthetic dataset. Its effect cannot be fully observed from Table 4" (line 199). While Figure 9 provides qualitative evidence, a quantitative comparison (even on a single scene where inter‑reflection is prominent) would strengthen the contribution claim.

- **Environment map evaluation procedure is underspecified.** The paper states that environment maps are "evaluated after re-scaling to eliminate ambiguity" (line 174) but does not describe the alignment procedure (e.g., rotation/scale/intensity optimization). Without this, the MSE numbers in Table 2 are difficult to interpret or reproduce.

- **No discussion of limitations.** The paper does not discuss scenarios where the method may fail (e.g., scenes with extremely detailed geometry causing mesh extraction failures, or inter‑reflection effects too complex for a low‑order SH residual to capture).

### Trivial

- The paper mentions resetting "all color and material attributes before the second stage" (line 154) but a brief explanation of why the geometry is retained while materials are reset would help clarify the design rationale.
- Figure references in the text could be more tightly coupled to the results being discussed.

## Nice-to-Haves

- A runtime breakdown (rasterization vs. ray tracing vs. other components) would clarify whether the reported FPS reflects sustained real-time performance under all conditions.
- Additional relighting/editing demonstrations beyond the two examples in Figure 11 would strengthen the applications section.
- A limitations paragraph in the main paper would improve completeness.

## Removed Points

These points are flagged for removal; treat them with caution.

- **"Straw‑man in the introduction about prior works not modeling inter‑reflection"** — The paper actually acknowledges RelightableGaussian (line 12, 29) and describes its approach and limitations. The framing is that prior methods lack a *proper* or *efficient* solution, which is a defensible position.
- **"Missing statistical significance / error bars"** — Single‑run evaluation is standard practice for large‑scale novel‑view synthesis benchmarks in this community. Requesting multi‑seed experiments with error bars goes beyond the field's normal standard.
- **"Some baselines missing from tables"** — The table images are not readable from the paper text; this claim cannot be verified.
- **"Missing failure cases"** — A reasonable suggestion but not a core weakness; good papers often focus on strengths.
- **"Pure formatting/style nitpicks"** — Removed per instructions.
- **"Typos/grammar"** — These are parser artifacts, not author errors.

## Novel Insights

The reviews collectively surface a key tension: the paper's engineering contributions (physically based deferred rendering in GS, learned indirect residual with mesh‑based visibility, geometry optimization strategies) are solid and produce strong empirical results, but the paper frames these contributions more ambitiously than the evidence supports. The "unified solution" claim and the "first inter‑reflection in GS" framing are both overstated. The most valuable lesson from this review is that a paper can have a real technical contribution yet still be undermined by framing that overreaches — the delta between what the method actually does and what the paper claims it does is where the most credible criticisms concentrate.

## Suggestions

1. **Remove or substantiate the "unified solution" claim.** Either add experiments on a non‑reflective dataset (e.g., DTU or Mip‑NeRF 360) or remove the claim from the abstract and contributions.
2. **Reframe the inter‑reflection component** as a "learned indirect lighting approximation" or "visibility‑aware specular residual" rather than a physically grounded inter‑reflection. Adjust "first time" language accordingly.
3. **Add a brief description of the TSDF mesh extraction pipeline** (e.g., render depth maps from Gaussians → TSDF fusion → Marching Cubes) to improve reproducibility.
4. **Add a quantitative ablation of the inter‑reflection component** on a scene where its effect is visible (e.g., Bell or Tbell).
5. **Justify or ablate the SH substitution for integrated diffuse lighting** in the main method section.

## Score and Decision

The paper makes real technical contributions — the combination of physically based deferred rendering with a learned indirect component in Gaussian splatting is competently engineered and produces state‑of‑the‑art results on reflective datasets. However, the central claims are overstated in two significant ways (the "unified solution" claim with zero supporting evidence, and the overblown framing of the inter‑reflection component as a "first" and physically rigorous contribution), and a key implementation detail for reproducibility is missing. These issues are fixable, but in their current form they undermine the paper's overall case. The paper is borderline and would benefit from a major revision to align claims with evidence.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>