Now I have a complete understanding. Let me produce the authoritative consolidated review.

## Summary

This paper proposes ∫-noise (integral noise), a novel noise representation that reinterprets discrete Gaussian noise samples as integrals of an underlying infinite-resolution white noise field. The authors derive a noise transport equation with Jacobian rescaling for distribution-preserving warping of noise across video frames, and implement a practical algorithm via higher-resolution sub-pixel sampling, backward warping, triangulation, rasterization, and aggregation. The method is evaluated on four video tasks — appearance transfer (SDEdit), restoration/super-resolution (I²SB), pose-to-person video (PIDM), and fluid simulation super-resolution — showing improved temporal coherence over standard noise priors and interpolation baselines.

## Strengths

- **Mathematically rigorous distribution preservation via the Brownian bridge interpretation (Section 2.2, Equations 6–8, Figure 2b).** The paper provides a clean analytic proof: bilinear interpolation reduces noise variance (σ²_z = α² + (1−α)² < 1 for α∈(0,1)), whereas ∫-noise yields a conditional distribution whose stochastic component exactly compensates the lost variance (σ²_∞ = 1 − σ²_z). This directly validates the central claim that ∫-noise simultaneously preserves temporal correlation AND the original noise distribution — a non-obvious result.

- **Noise transport equation with Jacobian rescaling (Equation 4).** The continuous transport equation T(W)(A) = ∫_A (1/|∇τ(τ⁻¹(x))|^{1/2}) W(τ⁻¹(x)) dx is a theoretically grounded extension of white noise theory to the warping setting. The Jacobian determinant accounts for local stretching/compression, going well beyond the rudimentary interpolation or translation-only schemes in prior noise-prior work (Ge et al., 2023; Chen et al., 2023; Khachatryan et al., 2023).

- **Conditional white noise sampling derivation (Section 2.1, Equation 3).** The paper derives a closed-form conditional distribution for sub-pixel sampling (W(𝔸^k) | W(A⁰)=x) and provides a practical reparameterization (sample unconditionally, remove mean, add scaled pixel value) that connects the abstract white-noise formulation to a concrete, implementable algorithm.

- **Honest reporting of the LDM limitation (Section 4).** The paper explicitly reports that noise warping has "limited impact on temporal coherency in latent diffusion models" and explains why (low-resolution noise, high-frequency details offloaded to the decoder). This is a meaningful empirical finding that correctly bounds the method's scope, though it also limits practical applicability.

- **Ablation on the upsampling factor k (Section 4, inset plot).** The paper tests different k values on the fluid task, showing that k=1 already reduces undefined pixels and k=3 suffices for most cases. This provides practical guidance and demonstrates understanding of the approximation-cost trade-off.

## Weaknesses

### Fatal
None.

### Major

- **The SDEdit experiment confounds the ∫-noise contribution with cross-frame attention.** For the photorealistic appearance transfer task (lines 130–131), the paper states: "While our method also works without it, we use cross-frame attention in this specific application to better showcase the difference between the different noise priors." This means the results in Figure 1a and Table 1 for this task reflect the combined effect of ∫-noise + cross-frame attention, not ∫-noise alone. No ablation is provided isolating the ∫-noise contribution. The claim that "our method also works without it" is unsupported. A controlled experiment comparing (a) SDEdit + random noise, (b) SDEdit + cross-frame attention, (c) SDEdit + ∫-noise, (d) SDEdit + ∫-noise + cross-frame attention is needed to disentangle contributions.

- **The quantitative evaluation, while present in Table 1, lacks per-task specification in the text and is insufficiently rigorous for the paper's claims.** The text (line 144) states metrics include warping error, FID, Improved Precision, and/or LPIPS "whenever it makes sense" — but does not specify which metrics apply to which task, on which dataset, or under what conditions. For the fluid super-resolution task (the most challenging with "large motions and deformations"), the paper provides only qualitative x-t slices (Figure 5) and the text describes no quantitative results specific to that task beyond the omnibus Table 1. The paper's central claim — that ∫-noise improves temporal coherence in practical video tasks — relies heavily on visual inspection of figures and supplementary videos. Given that the differences between noise priors are subtle (especially in still frames from videos), systematic quantitative evaluation with per-task metric reporting and confidence intervals would substantially strengthen the paper.

- **The paper asserts a limitation of prior work without evidence.** In the Introduction (line 12), the paper states that cross-frame attention and feature warping "are not able to represent high frequencies patterns of the fine resolution image." This claim is made without citation or supporting analysis. The paper does not test whether cross-frame attention with a standard noise prior fails on the specific tasks used in the experiments. While the paper's contribution is orthogonal (it focuses on the noise prior itself), making an unsupported negative claim about competing approaches weakens the motivation.

### Minor

- **Computational cost is acknowledged but not quantified.** The paper says the method is "computationally less efficient than simpler techniques" and "remains comparable to DDIM inversion" (line 144) but provides no runtime measurements, wall-clock comparisons, or analysis of how cost scales with frame count, upsampling factor k, or optical flow complexity. The triangulation and rasterization steps are non-trivial, and readers cannot assess the practical trade-off without numbers.

- **PIDM motion estimation details are absent.** For the pose-to-person task (line 140), the paper says "We estimate a rough motion of the entire body from the pose sequence" without describing how this is done, what accuracy is needed, or whether errors in the estimated motion affect the noise warping quality.

- **No analysis of failure cases or long-sequence behavior.** The paper recommends warping back to the first frame via accumulated deformation fields for long sequences (line 100) but does not discuss the well-known problem of optical flow drift due to occlusions, disocclusions, and estimation errors over many frames. The fluid example has simple, smooth motion and is not a stress test. The paper footnotes disocclusion treatment but provides no analysis of how the method behaves under inaccurate flow or on long, complex videos.

- **Limited scope of the ablation studies.** The ablation on the upsampling factor k is limited to the fluid task. An ablation on the triangulation/rasterization resolution compared to simpler alternatives would be more informative. The LDM limitation is important but relegated to Section 4; given that latent diffusion models (Stable Video Diffusion, etc.) are the dominant paradigm for video generation, this scope restriction deserves more prominent placement.

### Trivial

- The limitations section's caveat that "the underlying assumption we made is that a more temporally-correlated noise prior would result in better temporal coherency... This assumption is not always guaranteed" is honest but somewhat undercuts the paper's framing. The paper would benefit from characterizing *when* the assumption holds rather than leaving it as a blanket caveat.

## Nice-to-Haves

- A comparison against a simple baseline of upsampling noise and correlating frames via latent interpolation (a natural approach practitioners might try).
- Runtime/scalability analysis across different k values and frame counts to help users assess the trade-off.
- An explicit diagnostic of what diffusion pipeline properties determine sensitivity to the noise prior — turning the acknowledged limitation into a design guideline.

## Removed Points

These were flagged as weaknesses by reviewers but are removed after verification against the paper:

- **"The evaluation does not establish practical value — no quantitative results for two tasks"**: The paper explicitly states (line 144–148) that all four tasks are quantitatively evaluated in Table 1, with warping error, FID, Improved Precision, and/or LPIPS. While the per-task specification in the text could be clearer, the claim that two tasks have "no quantitative results at all" is contradicted by the paper text. Demoted to the Major weakness above (insufficient per-task specification) rather than a categorical absence.

- **"Baselines are too weak — should compare against cross-frame attention, feature warping"**: This is scope creep. The paper explicitly focuses on *noise priors* as the object of study, and compares against the relevant noise-prior baselines (Random, Fixed, interpolation schemes, Ge et al., Chen et al.). Demanding comparison against architectural methods (cross-frame attention, temporal attention fine-tuning) asks the paper to solve a different problem. The paper's contribution is orthogonal to those methods; combining them is actually a strength (as done in the SDEdit experiment, albeit with confound issues).

- **"It's unclear whether the method actually uses conditional sampling"**: Line 73 explicitly states "we first compute the higher-resolution discrete ∫-noise W(𝔸^k), possibly from an a priori sample (Equation (3))." The method clearly uses conditional sampling. Removed as factually incorrect.

- **"Missing related works"**: Removed per rule (cannot verify existence of external sources).

- **Formatting/style complaints about the table being an image**: This is a parser artifact; the original submission contains a properly formatted table.

- **"The method is incompatible with latent diffusion models"**: The paper states "limited impact," not incompatibility. The distinction matters — the method can still be applied, it just has less effect. This is a real limitation (kept as Minor) but the critic's framing overstates it.

## Novel Insights

The harsh critic correctly identifies that the paper's strongest contribution is the mathematical framework (∫-noise representation and noise transport equation) rather than its empirical validation. A genuinely novel observation that emerges across the reviews is that the paper's core insight — that noise transport should preserve the *distribution* of the noise, not just its spatial correlation — reverses a common implicit assumption in the video diffusion literature. Most methods optimize for temporal coherence without considering whether the noise statistics are preserved; the paper shows these two objectives are connected and can be jointly satisfied through the Brownian bridge interpretation. This reframing has the potential to inform future work beyond the specific warping algorithm presented.

## Suggestions

1. **Disentangle the SDEdit experiment.** Add ablations comparing (a) SDEdit alone, (b) SDEdit + cross-frame attention, (c) SDEdit + ∫-noise, and (d) SDEdit + ∫-noise + cross-frame attention. This would cleanly separate the contribution of the noise prior from the attention mechanism.

2. **Provide per-task quantitative details in the text.** For each of the four tasks, explicitly state which metrics were computed, on which dataset, under what conditions, and report confidence intervals or standard deviations.

3. **Quantify computational cost** with wall-clock times for random noise, fixed noise, bilinear warping, DDIM inversion, and ∫-noise at varying k values and frame counts.

4. **Frontload the LDM limitation.** Given the dominance of latent diffusion models in video generation, the limited impact on LDMs should be stated in the abstract or introduction alongside the paper's claimed contributions.

5. **Add failure-case analysis** showing what happens when optical flow is inaccurate (e.g., on real-world video with occlusions and complex motion), and how the method handles disocclusions in practice.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>