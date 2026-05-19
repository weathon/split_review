- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

The paper proposes Flow Score Distillation (FSD), a text-to-3D method that improves generation diversity by replacing the random noise in Score Distillation Sampling (SDS) with a deterministic noise schedule. The key insight is a theoretical derivation (Proposition 1) showing that the DDIM PF-ODE can be rewritten as an analogue of the SDS loss when the representation is the image directly — implying that SDS's random noise per step breaks consistency and causes mode-seeking. FSD restores this consistency. For 3D, the paper introduces a world-map noise function that provides coarsely correlated noise across views, and shows qualitative results demonstrating that FSD produces substantially more varied 3D assets than SDS without obvious quality degradation.

## Strengths

- **Theoretical connection between SDS and DDIM (Proposition 1, Section 3.1).** The paper proves that the PF-ODE (DDIM) can be written in a form that is structurally analogous to the SDS loss gradient, providing a formal mathematical framing for why SDS's noise strategy matters. This is a clean, non-obvious insight that goes beyond prior empirical analyses.

- **Identification of noise-sampling as a primary cause of diversity loss (Section 3.3, Figure 3).** The 2D analysis shows concretely that using different noise at each step makes the one-step denoised estimates inconsistent, forcing SDS toward an averaged output. This diagnosis is supported by visual evidence (Figure 3 showing how FSD's estimated ground-truth images remain consistent while SDS's vary greatly) and directly motivates the core design of FSD.

- **Clear qualitative evidence of diversity improvement in 3D (Section 5, Figure 5).** Across two backbone diffusion models (Stable Diffusion and MVDream), the paper shows that FSD produces substantially more varied 3D assets than SDS given different random seeds, while maintaining comparable quality. The MVDream comparison (Figure 5b) is particularly striking because SDS with MVDream yields nearly identical results across seeds, whereas FSD generates noticeably diverse content.

- **World-map noise function design (Section 4.2, Equation 6).** The paper identifies a real failure mode of the naive constant-noise design (surface holes, Figure 6) and proposes a principled solution: a spherical noise map that provides coarsely correlated noise across views while avoiding the texture-sticking problem. This is a practical contribution that makes the noise-scheduling idea workable for 3D.

## Weaknesses

### Fatal
None. The core idea is valid, the qualitative evidence supports the diversity claim, and the paper is honest about its limitations.

### Major

1. **No quantitative evaluation for the core 3D claim.** The paper's central contribution is a text-to-3D method that improves diversity without sacrificing quality, yet the entire 3D evaluation is qualitative — a handful of rendered samples for two prompts (one with each backbone), plus a single ablation figure. No quantitative metric is reported: no CLIP R-precision, no user study, no diversity measure (e.g., pairwise LPIPS), no comparison to any standard benchmark (e.g., T3Bench, DreamFusion prompts). The claims that FSD "substantially enhances generation diversity without compromising quality" are not substantiated with numbers. The section titled "Quantitative Results" (Section 5.3) contains only an ablation figure, not quantitative metrics. This is a significant evidential gap for the paper's main thesis.

2. **No 3D comparison to VSD or other diversity-targeting baselines.** The paper discusses Variational Score Distillation (VSD, from ProlificDreamer) extensively in the introduction and related work as the most prominent prior work addressing the same diversity limitation. It even includes VSD and NFSD in the 2D image-generation comparison (Figure 2). However, the 3D experiments compare FSD only to a vanilla SDS baseline. Since the paper argues that FSD "breaks free from the maximum-likelihood-seeking nature of SDS," it must be directly compared to existing methods that also target this limitation — particularly VSD. Without this comparison, a reader cannot judge whether FSD is actually better than alternatives.

### Minor

3. **Theoretical framing is oversold relative to what is proven.** Proposition 1 shows the DDIM PF-ODE can be rewritten as an SDS analogue *only when the representation is directly the image* (θ = x₀). The paper honestly acknowledges in the limitations that "we only found plausible theorems for FSD-guided 2D generation, and generalized FSD to 3D generation in an intuitive way." However, the abstract and introduction frame this as "a generalized DDIM generation process on 3D representations" without qualification. The disconnect between the ambitious framing and the actual scope of the theory should be corrected.

4. **The world-map noise function lacks thorough analysis.** The noise design in Equation 6 combines background noise, a patched world-map noise, and random noise. The ablation is limited to adjusting a single blending factor β (shown qualitatively for one prompt, Figure 7) and a brief mention of parameter Θ. For a method whose 3D contribution centers on this noise design, the lack of systematic analysis — e.g., effect on geometry metrics, sensitivity to world-map dimensions, comparison to alternative correlated noise strategies, or evaluation across multiple prompts — is a notable gap.

5. **"Several tricks" are never specified.** The paper states: "We apply several tricks that we found helpful to improve generation quality on both baselines and our method" (Section 5.1) without listing them. This hurts reproducibility and fairness — readers cannot know whether the baseline SDS is a strong or weak implementation. If these are standard tricks (e.g., timestep annealing, CFG scheduling), they should be stated explicitly.

### Trivial
None.

## Nice-to-Haves
- A more formal definition of the mapping from camera parameters (θ_cam, φ_cam) to world-map pixel coordinates, including interpolation scheme.
- Reporting wall-clock time or iteration count for FSD convergence relative to SDS and VSD.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Weakness about "what random seeds, what prompts, how many samples?" for the 2D comparison (Figure 2).** The paper states it uses "random seeds from 0 to 3 for each prompt by default" and shows 3 samples per method. This is sufficient for a qualitative illustration in a figure; the real gap is the lack of quantitative metrics, not the number of visual samples.
- **Weakness about the paper "cherry-picking" prompts for the Stable Diffusion experiment.** The paper directly acknowledges this limitation ("we manually pick some prompts on which SDS-like methods may not suffer from multi-face Janus problem") and explains why. This is an honest practice in a setting where the baseline method itself fails for most prompts. The concern is noted but already addressed by the authors.
- **Criticism about missing discussion of training cost relative to VSD.** The paper mentions that VSD's "training costs could grow linearly with the particle number" while FSD introduces "no extra training costs." A wall-clock comparison would be nice but its absence is not a weakness — the cost advantage is clearly stated and follows logically from the method design.
- **Strength about ablation on blending factor β being a "supporting strength."** While this is a valid supporting experiment, its limited scope (one prompt, qualitative only) means it is not a strong independent strength. However, it is not incorrect, so I retain it in milder form.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add a quantitative evaluation on a standard prompt set (e.g., 40 prompts from DreamFusion or T3Bench).** Report at minimum: (a) generation quality via CLIP R-precision or a user preference study, and (b) diversity via mean pairwise LPIPS between samples generated from different seeds for the same prompt. Report results for all seeds, not cherry-picked.
2. **Add a direct 3D comparison to VSD** using the same renderer, same number of optimization steps, reporting both quality and diversity metrics.
3. **Specify the "several tricks"** applied to both baselines and FSD in the implementation details.
4. **Ablate the world-map noise design more thoroughly:** show sensitivity to world-map dimensions, the effect of the blending factor β across multiple prompts, and comparison to alternative noise correlation strategies.
