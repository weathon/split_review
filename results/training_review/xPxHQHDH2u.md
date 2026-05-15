Now I have a thorough understanding of the paper. Let me construct my final review.

**My analysis plan:**

1. **Critical Issue 1 (Overclaimed inter-reflection):** The paper's own text (line 12) acknowledges R3DG "traces rays across Gaussians for visibility inferring" — so the "first time" claim (lines 4, 14) is contradicted by their own citations. However, their approach (ray-tracing on extracted mesh + split-sum + learned indirect SH term) is a different and faster mechanism. The criticism about "not physical inter-reflection" is partially valid — the work defines indirect light as "perturbation caused by occlusion" (line 113), which is closer to occlusion-aware environment lighting than true light bouncing. I'll keep this as a major weakness about overclaiming.

2. **Critical Issue 2 (Ablation contradiction):** The paper acknowledges this issue directly (line 199). The data does show mixed results. This is a minor weakness — the inter-reflection component helps qualitatively (Figure 9) but not always quantitatively.

3. **Critical Issue 3 (Unified solution unsupported):** The paper claims this but tests only on reflective-heavy datasets. Valid weakness. I'll keep it.

Let me now write the final review.Now I'll construct the final consolidated review.

## Summary

This paper introduces Ref-Gaussian, a novel view synthesis framework that applies physically based deferred rendering with the split-sum approximation within a 2D Gaussian splatting (2DGS) pipeline. The method incorporates two main components: (1) pixel-level BRDF shading via deferred rendering after alpha-blending material properties, and (2) an occlusion-aware indirect lighting term that uses ray-tracing on a periodically extracted mesh to separate direct and indirect specular illumination. Additional geometry-focused optimizations — per-Gaussian shading initialization, material-aware normal propagation, and 2D Gaussian primitives — further improve reconstruction quality. The method achieves state-of-the-art quantitative results on reflective test scenes (Shiny Blender, Glossy Synthetic) and supports relighting and material editing.

## Strengths

- **State-of-the-art quantitative results on reflective-scene benchmarks.** Table 1 shows Ref-Gaussian achieving the highest PSNR (28.53 on Shiny Blender, 32.85 on Glossy Synthetic) and best SSIM/LPIPS across most scenes, outperforming 3DGS-DR, GaussianShader, R3DG, and NeRF-based methods. The gain on Shiny Blender is +1.64 dB PSNR over the strongest baseline (3DGS-DR), which is meaningful.

- **Physically based deferred rendering in a Gaussian splatting pipeline yields materially richer reconstructions.** The pixel-level BRDF shading (using albedo, metallic, roughness, normal maps aggregated via alpha-blending) demonstrably outperforms simplified shading functions. Ablations in Table 4 show removing PBR drops PSNR from 28.53 to 27.91 on Shiny Blender, and Figure 7 shows qualitatively better handling of material variations (e.g., the rough band on the sphere).

- **Efficient rendering compared to Monte Carlo approaches for inter-reflection.** By using split-sum approximation with pre-integrated environment maps and ray-tracing on an extracted mesh with BVH acceleration, the method achieves real-time rendering (185 FPS reported in Table 2) while modeling indirect illumination effects — substantially faster than R3DG's Monte Carlo approach (7.5 FPS).

- **Geometry optimization techniques show measurable benefit in ablations.** The combination of 2D Gaussian primitives, per-Gaussian shading initialization, and material-aware normal propagation collectively improve normal accuracy and rendering quality, as demonstrated in Tables 3-4 and Figure 10.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed novelty of the inter-reflection component.** The paper repeatedly states that it realizes inter-reflection "within a Gaussian splatting paradigm for the first time" (abstract, Section 1, Section 3). However, the paper's own related work section (line 12) acknowledges that **R3DG (RelightableGaussian)** already "traces rays across Gaussians for visibility inferring" within the Gaussian splatting paradigm. Moreover, the proposed mechanism — a per-Gaussian spherical harmonics color \(L_{\text{ind}}\) alpha-blended into an indirect lighting map — models occlusion-aware environment lighting rather than physical light bouncing between surfaces. The paper's framing of "inter-reflection" would be more accurately described as an occlusion-aware learned indirect specular residual. This overclaiming undermines the stated novelty of a core contribution.

- **Claim of "unified solution for both reflective and non-reflective scenes" is unsupported by experiments.** The abstract and contribution list (lines 4, 16) assert that Ref-Gaussian serves as a unified solution for reflective and non-reflective scenes. However, all three evaluation datasets (Shiny Blender, Glossy Synthetic, Ref-Real) are dominated by reflective objects. No experiments are conducted on standard non-reflective benchmarks (e.g., Mip-NeRF 360, DTU, or the original 3DGS scenes). This claim is speculative without supporting evidence.

### Minor

- **Ablation evidence for the inter-reflection component is mixed.** Table 4 shows that removing the inter-reflection component *improves* PSNR on Glossy Synthetic (32.83 vs. 32.67) and yields only a tiny gain on Shiny Blender (+0.21 dB). The paper acknowledges this limitation (line 199: "its effect cannot be fully observed from Table 4") and provides qualitative evidence (Figure 9) showing cases where the component helps. However, presenting inter-reflection as a central contribution is at odds with the quantitative ablation data, which at best shows marginal benefit on one of two test sets.

- **No error bars or statistical significance reported for any quantitative results.** All metrics in Tables 1-4 are reported as single values without variance estimates. Given the modest absolute gains over the strongest baseline (≈1-2 dB on Shiny Blender, <0.2 dB on Glossy Synthetic), the significance of these improvements is unclear.

- **Material-aware normal propagation thresholds are heuristic without sensitivity analysis.** The method uses hard thresholds (metallic ≥ 0.02, roughness ≤ 0.1) for scale increase. No analysis is provided on how sensitive results are to these values, or whether they generalize across different scene types.

- **Relighting and editing demonstrations are purely qualitative with no comparison to prior work.** While Section 4.3 showcases relighting and editing results (Figure 11), no quantitative metrics or comparisons against existing relighting methods are provided, making it difficult to assess the quality of the decomposed material and lighting.

### Trivial
- Table 4 caption mentions a typo ("Typo: Correction." in the caption) that should be cleaned up.
- The claim about "non-reflective scenes" in the contribution list is repeated despite no supporting experiments (see Major weakness above).

## Nice-to-Haves
- Evaluating Ref-Gaussian on standard non-reflective benchmarks (e.g., Mip-NeRF 360, DTU) would substantiate the "unified solution" claim.
- A controlled experiment replacing the learned SH indirect term \(L_{\text{ind}}\) with a standard view-dependent SH color (without visibility decomposition) would isolate the benefit of the ray-traced visibility mask.
- Sensitivity analysis for the material-aware normal propagation thresholds would strengthen the geometry optimization contribution.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"The inter-reflection component is not grounded in the Gaussian representation because visibility uses an external extracted mesh."** — The paper's pipeline uses ray-tracing on the extracted mesh for visibility, then maps visibility back to the Gaussian splatting framework via alpha-blending of the indirect term. This hybrid approach is a design choice, not a flaw. Many inverse rendering pipelines use explicit meshes for ray operations. This is a methodological preference, not a weakness.

- **"The per-Gaussian shading initialization is standard practice in many inverse rendering pipelines (e.g., NeRO) and not a novel contribution."** — Even if similar two-stage training is used elsewhere, the paper does not claim this specific sub-component as a primary novelty; it is presented as an engineering design to facilitate convergence. Criticizing it for not being novel is a strawman — the paper's core novelty lies in the overall pipeline integrating PBR deferred rendering with inter-reflection.

- **"FPS is lower than 3DGS-DR (141 vs 281), so compute efficiency advantage is questionable."** — 141 FPS is still real-time (>30 FPS). The method does more computation (BRDF shading, ray-tracing, inter-reflection) than 3DGS-DR's simplified shading, so a lower FPS is expected and acceptable. The more relevant comparison is against methods that also model inter-reflection (e.g., R3DG at 7.5 FPS), where Ref-Gaussian is far faster.

- **Pure formatting/style nitpicks** from the harsh critic's section-by-section notes are removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the inter-reflection contribution.** Replace "first Gaussian-grounded inter-reflection" with a more precise description such as "occlusion-aware indirect specular residual learned within a Gaussian splatting framework." Acknowledge R3DG as prior work on inter-reflection in the GS paradigm and clarify how the proposed approach differs (split-sum approximation + learned residual on extracted mesh vs. Monte Carlo ray-tracing across Gaussians).

2. **Either remove the "unified solution for non-reflective scenes" claim or support it with evaluation on standard non-reflective benchmarks** (e.g., Mip-NeRF 360, DTU). Without evidence, this claim should be scoped to reflective scenes.

3. **Provide variance estimates or error bars** for the main quantitative results, especially given the modest margins on Glossy Synthetic.

4. **Add a sensitivity analysis** for the material-aware normal propagation thresholds, or provide a rationale for why the chosen values are expected to generalize.

5. **Conduct the proposed controlled experiment**: replace \(L_{\text{ind}}\) with a view-dependent SH color without the visibility mask to formally demonstrate the benefit of the ray-traced decomposition.

## Score and Decision

The paper makes a genuine technical contribution by integrating physically based deferred rendering with split-sum approximation into the 2D Gaussian splatting framework, achieving strong results on reflective scenes. However, the core contribution is undermined by overclaiming on two fronts: (i) the inter-reflection novelty ("first time") is factually contradicted by the paper's own citation of R3DG, and the mechanism is better described as occlusion-aware indirect lighting rather than true inter-reflection; (ii) the "unified solution for both reflective and non-reflective scenes" claim has no supporting experiments. The ablation evidence for the inter-reflection component is mixed. The paper requires a major revision to align its claims with what is actually demonstrated. I recommend rejection in the current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>