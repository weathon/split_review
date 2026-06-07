## Summary

This paper proposes two methods — Truncated Sampling Models (TSM) and Iterative Refinement (IR) — to reduce the number of function evaluations (NFEs) required by diffusion models for physics-based fluid simulation surrogates. TSM restricts training to high-noise levels of the diffusion process and truncates the low-noise sampling steps, jumping directly to the denoised estimate via Tweedie's formula. IR samples a pre-trained DDPM by adding noise at selected levels and applying Tweedie's formula to refine an initial coarse estimate. Both methods are evaluated on three fluid dynamics benchmarks (incompressible and compressible turbulent flow, airfoil uncertainty) with NFE reductions of ×4–×20 while maintaining or improving accuracy over standard DDPM/DDIM/EDM baselines.

## Strengths

- **Domain-specific justification linking truncation to fluid data characteristics.** The paper identifies (line 128) that fluid datasets at coarse resolutions "inherently lack high-frequency details," and that their distributions are "predominantly unimodal," explaining why aggressive truncation of the reverse process does not lose meaningful information. This is a concrete, non-obvious connection between the method's design and the target domain that distinguishes TSM from generic truncation applied to natural images.

- **Quantitative demonstration that single-step TSM beats the ACDM benchmark on the Tra case.** Line 120 and Table 1 show that single-step TSM (NFE=1) achieves a ×20 speedup over the autoregressive conditional diffusion model of Kohl et al. (2024) while *outperforming* it in accuracy on the Tra dataset. This directly supports the paper's central claim that truncation can simultaneously improve speed and fidelity.

- **Clear three-axis differentiation of TSMs from the closest prior truncation work (TDPMs).** Line 101 provides three concrete distinctions: (i) which steps are truncated (TSM truncates the early reverse steps; TDPM truncates the late forward steps), (ii) TSMs require no auxiliary GAN generator, and (iii) TSMs enable one-step inference while TDPM quality degrades under large truncation.

- **Stride-conditioned autoregressive formulation enabling flexible prediction horizons.** Lines 65–73 describe conditioning the surrogate on a stride parameter *j*, allowing a single network to predict both next-step and intermediate future states. The paper explicitly contrasts this with DYffusion (Cachay et al., 2023), which requires separate forecaster and temporal interpolator networks.

- **Physics-relevant evaluation metrics beyond pixel-level accuracy.** The evaluation uses turbulent kinetic energy spectrum (TKE), domain-wide kinetic energy (DWKE), temporal correlation, and temporal stability (lines 116, 126, Fig. 2), which capture physically meaningful properties of fluid flows rather than only MSE.

## Weaknesses

### Fatal

None.

### Major

- **Missing critical ablation: TSM (restricted training) vs. standard DDPM + same truncation at sampling.** TSM's sole training modification is sampling t uniformly from {tₛ, …, T} rather than {1, …, T}. A standard DDPM trained on all noise levels can be sampled identically: start from x_T, run ancestral steps to x_{tₛ}, then estimate x₀ via Tweedie. Without this control experiment, the observed accuracy improvements cannot be attributed to the proposed training modification — they may simply come from the truncation + Tweedie heuristic at sampling time. This is the central empirical question about TSM, and the paper does not address it.

- **Misalignment between the central framing and the evaluation.** The paper states its objective is to "reduce the gap between DDPMs and deterministic single-step approaches" (abstract, line 16) and concludes by claiming to have "minimized the disparity between DDPMs and deterministic baselines" (line 170). Yet the evaluation compares only against other diffusion models (DDPM, DDIM, EDM, ACDM). The only deterministic baseline mentioned is "UNet_ut" (UNet with unrolled training) in Table 1's caption, but no results for it are discussed in the text. Standard deterministic surrogates for physics problems — FNO, DeepONet, standard UNet — are absent. The paper demonstrates improvements *within* the family of diffusion models, but this does not support the advertised claim about closing the gap to deterministic methods.

### Minor

- **Novelty of IR relative to PDErefiner is unclear.** IR adds noise to an initial state at selected levels from the diffusion schedule and applies Tweedie's formula to refine the estimate. This is conceptually similar to PDErefiner (Lippe et al., 2023), which refines PDE solutions through multistep denoising. The paper cites PDErefiner (line 80) but does not clearly articulate what distinguishes IR from it beyond "flexible choice of γ." The distinction needs to be substantiated.

- **IR's accuracy-NFE relationship is unpredictable.** The paper acknowledges (line 148) that "IR does not manifest a noticeable trend" between NFEs and accuracy and is "case-by-case tuned." While this is honest reporting, it is a practical limitation that means each application requires per-dataset hyperparameter sweeps to find the right γ schedule, and the same schedule does not transfer across problems.

- **The "deterministic mean prediction" concern for single-step TSM is not adequately addressed.** When s ≈ 1, TSM reduces to a single forward pass from pure noise — effectively an autoencoder rather than a sampling procedure. The paper attributes the success to unimodal distributions and coarse resolutions (line 128), which is a plausible foundation, but does not provide distributional evidence (e.g., per-sample variance across noise seeds, MMD, or coverage metrics) to show that single-step TSM is actually sampling from the distribution rather than producing a deterministic low-error mean estimate that happens to have low MSE.

### Trivial

- **Terminology describing what TSM truncates is ambiguous.** Line 93 says TSM truncates "the *last* steps of the reverse Markov chain," while line 101 says it "conversely truncates the *first* steps." The intended meaning (TSM focuses on high-noise levels and skips low-noise steps) can be inferred, but the forward/reverse direction switching is confusing and should be made consistent for reproducibility.

## Nice-to-Haves

- Include deterministic baselines (FNO, DeepONet, standard UNet) to substantiate the paper's central claim about reducing the gap to deterministic methods.
- Add per-sample variance across noise seeds for single-step (s≈1) TSM to demonstrate that the method preserves the generative/stochastic nature of diffusion models rather than collapsing to a deterministic estimate.
- Clarify what distinguishes IR from PDErefiner more explicitly.
- Report the results for UNet_ut (already listed in Table 1's caption) and discuss them in the text.
- Include statistical significance testing across seeds for the main comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **IR description is incompletely specified (critic's #1):** The critic claims Section 4.2 cuts off mid-sentence and is unreviewable. However, Algorithm 2 (referenced but an image stripped by the parser) is the primary specification, and the text (lines 105–109) adequately conveys the core concept: take an initial state, add noise at level γᵢ, apply Tweedie's formula to obtain a refined estimate, and repeat. The cut-off sentence at line 109 is a parser artifact. **REMOVED per parser artifact rule.**

- **Exclusion of consistency models and distillation methods from comparison (from section-by-section notes):** The critic notes that consistency models (Song et al., 2023) are omitted, weakening the SOTA claim. The paper justifies this on practical grounds (distillation offers "no significant accuracy improvements over the teacher"), and the paper explicitly scopes its comparison to methods that do not require extensive retraining. Criticizing this omission given the stated scope is scope-creep. **WEAKENED to nice-to-have and then REMOVED per soft rule on scope.**

## Novel Insights

The observations about when truncation works — (1) that fluid target distributions are predominantly unimodal, reducing Tweedie bias, and (2) that coarse-resolution data lacks the high-frequency details that low-noise levels would otherwise restore — are the most interesting findings. They suggest that the effectiveness of truncation-based sampling is domain-dependent rather than universal, which is a useful counterpoint to the generic "fewer steps = worse quality" narrative in the diffusion literature. The stride-conditioned formulation allowing a single network to handle multiple prediction horizons is also a practical contribution, though it builds on existing multi-parameter conditioning ideas.

## Suggestions

1. **Add the critical TSM control experiment:** Compare TSM (restricted training) against a standard DDPM trained on all noise levels but sampled with the same truncation and Tweedie jump. This single experiment determines whether the training modification has value. If TSM outperforms the standard DDPM + truncation, the paper's core claim is supported. If not, the contribution reduces to a known sampling heuristic.

2. **Align the evaluation with the framing:** Either include deterministic baselines (FNO, DeepONet, standard UNet) in the comparison to support the claim about "reducing the gap to deterministic approaches," or reframe the paper's contribution as "improving diffusion model efficiency for physics surrogates" without the deterministic-competition framing.

3. **Demonstrate that single-step TSM is genuinely sampling:** Provide per-sample variance across different noise seeds for the same input when s ≈ 1. Near-zero variance would indicate a deterministic mean estimate rather than sampling from a distribution.

4. **Clarify IR's relationship to PDErefiner:** A sentence explicitly stating what is novel about IR (e.g., the flexible γ schedule optimization, or the specific initialization strategy) would preempt novelty concerns.

5. **Report the UNet_ut results** already listed in Table 1's caption and briefly discuss them in the text.

## Score and Decision

The paper addresses a genuine problem — the computational cost of diffusion models as physics surrogates — and the TSM idea is intuitive and potentially useful. The results on the Tra dataset (single-step, ×20 speedup, beating the ACDM benchmark) are compelling within the family of diffusion-based methods. However, the paper has two substantiated major weaknesses: (1) the missing control experiment that would validate whether TSM's training modification contributes anything beyond truncation at sampling time, and (2) the misalignment between the central framing (closing the gap to deterministic methods) and the evaluation (which includes no deterministic baselines). These are fixable, but in the current form the core claims are not fully supported. TSM may simply be "standard DDPM + truncation + Tweedie" relabeled as a new method, and the paper's main advertised contribution cannot be evaluated without that control.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>