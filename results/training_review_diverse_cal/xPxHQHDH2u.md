Now I have verified all key claims from the paper. Let me synthesize the final review.

---

## Summary

This paper introduces Ref-Gaussian, a Gaussian splatting framework for high-quality, real-time rendering of reflective scenes. It combines (1) physically based deferred rendering with a split-sum approximation for pixel-level BRDF shading, and (2) Gaussian-grounded inter-reflection that computes indirect lighting via ray tracing on a mesh extracted from 2D Gaussians. The method also contributes material-aware normal propagation, a per-Gaussian shading initialization stage, and the use of 2D Gaussian primitives. On reflective benchmarks (Shiny Blender, Glossy Synthetic, Ref-Real), Ref-Gaussian achieves state-of-the-art quantitative results while supporting real-time rendering, relighting, and editing.

## Strengths

- **Physically based deferred rendering with split-sum approximation enables real-time, high-quality rendering of reflective surfaces.** Unlike prior Gaussian methods that use simplified per-Gaussian shading (GShader, 3DGS-DR) or expensive Monte Carlo sampling (R3DG), the paper formulates pixel-level BRDF shading via split-sum approximation (Section 3.1). This avoids Monte Carlo overhead while modeling complex material properties (albedo, metallic, roughness), as demonstrated by competitive FPS (82 FPS) and training time (2.1h) in Table 2.

- **Gaussian-grounded inter-reflection is realized for the first time within a Gaussian splatting paradigm.** The paper introduces a method to compute indirect lighting by ray tracing on an extracted mesh and assigning per-Gaussian spherical-harmonic-based indirect colors (Section 3.2). This component shows qualitative improvements on reflective objects (e.g., Tbell and Bell in Figure 9), a capability absent in prior Gaussian-based methods.

- **State-of-the-art quantitative results on reflective benchmarks.** Table 1 shows Ref-Gaussian outperforming 3DGS, Ref-NeRF, GShader, R3DG, and 3DGS-DR on most scenes across Shiny Blender and Glossy Synthetic datasets. The method also achieves the best normal map and environment map estimation (Table 2), and supports downstream applications including relighting and editing (Figure 11).

- **Material-aware normal propagation and per-Gaussian shading initialization improve geometry reconstruction.** Ablation studies (Tables 3 and 4) show that these components jointly improve normal map quality and rendering metrics. Figure 10 demonstrates that material-aware propagation prevents geometric collapse on smooth reflective surfaces. The initial per-Gaussian shading stage is shown to improve geometric convergence (Table 4 ablation).

## Weaknesses

### Fatal
None.

### Major

- **The claim of serving as a "unified solution for both reflective and non-reflective scenes" is unsupported by evidence.** The abstract and contribution list (items III) assert that Ref-Gaussian works for non-reflective scenes. However, the paper evaluates only on reflective datasets: Shiny Blender (synthetic reflective), Glossy Synthetic (synthetic reflective), and Ref-Real (real reflective scenes). No experiments are conducted on standard non-reflective benchmarks such as Mip-NeRF 360, Tanks and Temples, or DTU. Without such evaluation, the claim is speculative. Since the method includes components specifically designed for reflection (split-sum, inter-reflection, material-aware normals), there is a risk these could hurt performance on diffuse scenes. This overclaim should be removed or substantiated.

- **The inter-reflection component—a stated core contribution—lacks strong quantitative evidence of effectiveness.** The paper itself acknowledges this limitation: "inter-reflection is the minority in the glossy synthetic dataset. Its effect cannot be fully observed from Table 4." The Shiny Blender ablation shows a negligible PSNR difference (0.09 dB) when removing inter-reflection. While qualitative improvements are visible on specific objects (Figure 9, Tbell and Bell), the central claimed novelty is not convincingly demonstrated on the evaluated benchmarks. A dedicated experiment on a scene where inter-reflection is the dominant visual effect (e.g., concave reflectors, mutually reflecting objects) would be needed to properly validate this component.

### Minor

- **Quantitative gains over the simpler 3DGS-DR baseline are modest.** On Shiny Blender, Ref-Gaussian achieves ~32.42 PSNR vs. 32.07 for 3DGS-DR (~1% relative improvement). On Glossy Synthetic, the gap is 32.13 vs. 31.60 (~1.7%). No confidence intervals or multi-run statistics are reported, so the consistency of these improvements is unknown. Given that 3DGS-DR uses a much simpler shading function without inter-reflection or mesh extraction, the practical significance of these gains for the added complexity is unclear.

- **Per-Gaussian shading initialization discards learned material attributes with unclear mechanism.** The initial 18,000 steps of per-Gaussian shading are followed by a reset of all color and material attributes, retaining only geometry. The paper says this "help[s] the gradients to be more effectively transferred back to the Gaussian primitives," but no analysis of what geometric information is transferred is provided. The ablation shows it helps empirically, but the design rationale is under-explained.

- **Efficiency trade-off among Gaussian methods is not discussed.** Training time is 2.1h for Ref-Gaussian vs. 0.5h for 3DGS-DR and 0.8h for GShader (Table 2). The paper frames the result as "excels in optimization speed" but this is true only relative to NeRF methods; among Gaussian splatting methods the method is substantially slower to train with moderate rendering FPS (82 vs. 92 for 3DGS-DR). A breakdown of the overhead contributed by periodic TSDF mesh extraction would help evaluate the efficiency claims.

- **Substitution of spherical harmonics for physically integrated diffuse lighting is an unexplained departure from physical modeling.** Section 4 (Implementation details) notes: "we discovered that spherical harmonics have a better fitting capability than the integrated diffuse lighting and we thereby use spherical harmonics to substitute it." If the diffuse term is a learned SH fit rather than a physically integrated environment map, the decomposition into principled lighting and materials is weakened. This choice should be justified or its implications discussed.

- **No quantitative evaluation of relighting/editing.** Figure 11 shows relighting and editing results qualitatively, but no comparison against ground-truth renderings under known environment maps is provided. This limits the assessment of material decomposition quality.

- **No analysis of mesh quality for the extracted TSDF mesh.** Since inter-reflection depends on visibility computed via ray tracing on the extracted mesh, its accuracy directly affects the method. No quantitative mesh quality metrics (e.g., Chamfer distance, visibility accuracy) are reported.

### Trivial

- Fixed thresholds for material-aware normal propagation (metallic ≥ 0.02, roughness ≤ 0.1) are used without sensitivity analysis. The behavior of this heuristic under varying learned values is unclear.

## Nice-to-Haves

- A dedicated synthetic experiment where inter-reflection is the dominant visual effect (e.g., two reflective spheres reflecting each other, a concave reflector) would provide the strongest validation of the method's central claimed novelty.
- Report error bars or multiple-run statistics for the main quantitative comparisons.
- Tone down or remove the "unified solution for non-reflective scenes" claim unless non-reflective benchmark evaluations are added.
- Provide a training time breakdown showing the overhead of periodic mesh extraction and ray tracing.
- A sensitivity analysis for the metallic/roughness thresholds in material-aware normal propagation would strengthen the method.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Critic's claim that 2DGS substitution providing much of the improvement is a weakness.** The reviewer acknowledges "this is not a weakness per se." The paper's use of 2DGS is an architectural choice that is ablated and discussed; it does not constitute a flaw.
- **Critic's suggestion that confidence intervals are needed.** While desirable, the absence of multi-run statistics is common practice in graphics benchmarks where single-run evaluation is the norm. This is kept as a Minor weakness above (not removed entirely) but downgraded from the critic's framing.
- **Strength Finder's claim that Ref-Gaussian achieves SOTA on "non-reflective" scenes.** This conflicts with the verified weakness that no non-reflective evaluation exists. The strength is retained but scoped to reflective scenes only.

## Novel Insights

Beyond the paper's own contributions, the most interesting structural observation from the review process is the tension between the two core claims: the method is explicitly designed to handle inter-reflection (one of its two pillars), yet the evaluated datasets do not stress-test this capability. This suggests the community's reflective benchmarks may be saturating for direct specular reflection but do not adequately cover multi-bounce indirect reflection effects. A useful byproduct of this work would be a new benchmark specifically targeting inter-reflection-heavy scenes, which would allow proper evaluation of methods claiming this capability.

## Suggestions

1. **Remove or substantiate the "unified solution for non-reflective scenes" claim.** Either add experiments on standard non-reflective benchmarks (Mip-NeRF 360, DTU) showing competitive performance, or scope the claim to reflective scenes.
2. **Demonstrate inter-reflection quantitatively on a scene where it is dominant.** A simple controlled synthetic scene (e.g., two facing mirrors, a concave reflector) with ground truth would provide the most compelling evidence for this core contribution.
3. **Report multi-run statistics.** The modest PSNR gaps over 3DGS-DR (0.35-0.53 dB) need to be shown to be consistent to convince readers the improvement is systematic rather than due to run-to-run variance.
4. **Justify or discuss the SH substitution for diffuse lighting** as a deviation from physically based rendering. If the diffuse term is a learned SH fit, the decomposition's physical interpretability is reduced.
5. **Provide a training time breakdown** showing the fraction spent on mesh extraction vs. rendering optimization.

## Score and Decision

**Originality:** Good. The paper is the first to combine physically based deferred rendering with inter-reflection in a Gaussian splatting framework. Individual components build on existing work (split-sum approximation from NeRF methods, 2DGS, deferred shading from 3DGS-DR) but the combination is novel.

**Importance of research question:** High. Real-time high-quality rendering of reflective objects is an important open problem with applications in VR/AR, gaming, and e-commerce.

**Claims well-supported:** Partially. The PBR and overall SOTA claims are supported. The inter-reflection claim lacks strong quantitative evidence. The "unified solution" claim is unsupported.

**Soundness of experiments:** Adequate. Standard benchmarks and metrics are used, but missing multi-run statistics, non-reflective evaluations, and a dedicated inter-reflection experiment weaken the evidence.

**Clarity of writing:** Good. The method is well-described and the contributions are clearly stated, though some design choices could be better justified.

**Value to the research community:** Positive. The method advances the state of the art on reflective scenes, provides a useful real-time baseline, and opens the door for future work on inter-reflection in Gaussian splatting.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>