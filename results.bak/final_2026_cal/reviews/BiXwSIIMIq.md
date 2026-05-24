Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces AC-DC, a three-stage denoiser (auto-correction via additive Gaussian noise, directional correction via conditional Langevin dynamics, and score-based denoising) designed for integration into the ADMM-PnP framework for solving inverse problems. The authors provide convergence guarantees showing that under proper AC-DC parameters, the ADMM iterates are weakly nonexpansive (enabling fixed-point ball convergence under constant step sizes) and that under relaxed conditions the denoiser is bounded (enabling convergence under adaptive step sizes). Experiments across super-resolution, inpainting, deblurring, and phase retrieval on FFHQ and ImageNet show consistent improvements over baselines including DPS, DiffPIR, DDRM, and RED-diff.

## Strengths

- **Novel three-stage AC-DC denoiser addressing the manifold mismatch problem in ADMM-PnP.** The paper identifies that the combination of ADMM iterates (especially the dual variable) and score-based denoising creates a geometry mismatch, since score functions are trained on specific noisy data manifolds. The AC stage injects Gaussian noise to push iterates toward those manifolds, the DC stage uses conditional Langevin dynamics to refine alignment, and only then applies score-based denoising (Tweedie's lemma or ODE). This is a principled solution to a recognized challenge that prior score-based PnP works (e.g., DiffPIR, RED-diff) do not fully address.

- **Extends ADMM-PnP convergence theory to score-based denoisers.** Prior ADMM-PnP convergence results (Ryu et al. 2019) required the denoiser residual to be strictly contractive. Theorem 2 relaxes this to weak nonexpansiveness (Assumption 1 with δ > 0), showing that the AC-DC denoiser satisfies this property with high probability under standard smoothness/coercivity assumptions. This represents a meaningful theoretical generalization that brings score-based denoisers under the ADMM-PnP umbrella.

- **Convergence analysis covers both strongly convex (Theorems 1–2) and nonconvex losses (Theorem 3).** While Theorem 1 requires ℓ to be μ-strongly convex, Theorem 3 removes this requirement (using bounded data domain and an adaptive ρ-schedule), providing a theoretical pathway for harder problems like phase retrieval where the forward model is not convex.

- **Consistent empirical improvement across diverse inverse problems.** Table 1 shows that Ours-tweedie and Ours-ode achieve the best or second-best scores on PSNR, SSIM, and LPIPS across seven tasks on two datasets (100 images each), including super-resolution, random/box inpainting, Gaussian/motion deblurring, and phase retrieval. Qualitative results (Figures 2–4) confirm that reconstructions are cleaner and more natural-looking than baselines.

- **Ablation validates the DC stage.** Figure 5 shows that increasing DC steps J from 0 (AC only) to 10 to 20 progressively reduces artifacts on phase retrieval, confirming that the Langevin-based directional correction is essential for effectiveness.

## Weaknesses

### Major

- **The convergence guarantees (Theorems 2 and 3) assume the DC Langevin dynamics reach the stationary distribution at each ADMM iteration, while the practical algorithm runs only J=10 Langevin steps.** The theorems explicitly state this assumption and a footnote points to Appendix E.2 for counterparts removing it. However, the abstract and introduction present the convergence results without this qualification, creating a misleading impression that the guarantees cover the evaluated algorithm. Even if the appendix relaxes this (which cannot be verified from the main text alone), the central theoretical contribution is proven under an idealization that is known not to hold in practice. This is the paper's most significant limitation and should be addressed by either: (a) providing convergence results for finite Langevin steps (e.g., via mixing-time bounds), or (b) reframing the theoretical claims to clearly separate the idealized analysis from the empirical method.

- **Theorem 3's convergence guarantee requires adaptive step sizes (p-increasing rule), but all experiments use a fixed step size.** The paper acknowledges this in the limitations section ("such schedules are arguably less appealing in practice… our experiments suggest that constant step sizes also perform well"). This means the nonconvex convergence result does not apply to the actual implementation evaluated in the paper — a theory-practice gap identical in structure to the stationary-distribution issue. An empirical demonstration that the adaptive schedule produces comparable results, or a convergence analysis for fixed step sizes under nonconvex losses, would be needed to close this gap.

### Minor

- **The Gaussian approximation used in the DC step is heuristic and unvalidated.** The DC step approximates the conditional score as ∇ log p(z_ac^(k) | z_σ^(k)) ≈ -(1/σ_ac^(k))(z_σ^(k) - z_ac^(k)), justified by "proper scheduling of σ^(k) and mild regularity conditions on s^(k), e.g., when Var(s^(k))^(1/2) ≪ σ^(k)." No empirical verification is provided that this condition holds for any of the tested problems, nor is the choice σ_{s^(k)} = 0.1/√(σ^(k)) derived from an analysis of this condition. While the ablation shows that more DC steps help (as any MCMC practitioner would expect), it does not validate the specific approximation.

- **The ablation study for DC steps is limited to one task (phase retrieval).** Figure 5 shows only the phase retrieval case. Demonstrating the effect of varying J on other tasks (e.g., Gaussian deblurring, box inpainting) would strengthen the evidence that the DC stage is broadly beneficial.

- **No runtime or NFE comparison with baselines.** The paper mentions that each iteration needs "multiple score evaluations," but does not report the total number of score function evaluations or wall-clock time per task. Since the AC-DC denoiser involves additional Langevin steps per ADMM iteration, this is a practical concern for reproducibility and deployment. The limitations section notes this, but quantification is missing.

- **Theorem 1's strong convexity requirement on ℓ excludes many problems of interest** (e.g., phase retrieval, compressed sensing with underdetermined systems). While Theorem 3 relaxes this, the tension with the adaptive-step-size issue (above) means that the fixed-step-size guarantee — the practically appealing setting — only applies to strongly convex problems.

### Trivial

- None beyond standard formatting artifacts introduced by the PDF parser.

## Nice-to-Haves

- A hyperparameter sensitivity study (varying the AC noise level, annealing rate, or DC step count across multiple tasks) would help gauge robustness.
- Comparing against a variant that uses the "exact" conditional score (if feasible via approximation) would isolate the effect of the Gaussian approximation.
- Reporting total NFEs and wall-clock time per reconstruction would clarify the practical cost of the additional DC steps.

## Removed Points

These points from the harsh critic are removed with justification:

- **"The appendix is not available for review" and claims about missing appendix content.** Per hard rules: the parser strips appendices from all papers; the original submission contains them.
- **"PMC rows appear multiple times" in Table 1.** This is a PDF-parser artifact, not an error in the original paper.
- **"No experiment isolates the effect of AC without DC."** Figure 5 explicitly shows J=0 (AC only) vs. J=10/20 (AC+DC), so this criticism is factually incorrect.
- **Reproducibility nitpicks about inner-loop convergence criteria.** The paper specifies max iterations (1000), convergence tolerance (Δ_tol=1e-3 over 3 iterations), and the optimizer. This is adequate detail.
- **Pure formatting/style criticisms.** Per hard rules, these are parser artifacts, not author errors.

## Novel Insights

The harsh critic raises the stationary-distribution and adaptive-step-size gaps as separate issues, but the review's own synthesis reveals a pattern: both gaps follow the same structure — the theory covers an idealized version of the algorithm while a heuristic approximation is used in practice. This recurring pattern is worth noting because it is common in this literature; the paper is transparent about both gaps (footnote + limitations section), which is more honest than many works in this space. The key takeaway is that the paper provides a theoretical scaffold (weak nonexpansiveness, boundedness) for score-based denoisers in ADMM, but the actual guarantees trail the implementation by one level of approximation. The practical value of the method rests more on the well-designed AC-DC architecture and the strong empirical results than on the theory as currently presented.

## Suggestions

1. **Align the abstract and introduction's theoretical claims with what is actually proven.** Add a qualifying phrase such as "under the idealization that the Langevin dynamics reach stationarity" so the reader can calibrate expectations from the start.
2. **Run an experiment with the adaptive ρ-schedule** required by Theorem 3 to demonstrate that the nonconvex convergence guarantee is practically realizable. Even if the fixed-step variant performs better, showing that the adaptive version also works would close the theory-practice gap.
3. **Provide a more granular ablation of DC steps** (J ∈ {1, 5, 50}) on at least one additional task (e.g., Gaussian deblurring) to show the trend is not specific to phase retrieval.
4. **Report total NFEs and runtime** per reconstruction for all methods. This is important because the AC-DC denoiser's DC steps add computational cost, and readers need to evaluate the efficiency trade-off.
5. **Empirically verify the Gaussian approximation condition** (Var(s^(k))^(1/2) ≪ σ^(k)) for at least one test problem to support the DC step's theoretical justification.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- Weak anchors (score < 3.5): Papers like "Consistency-Guided Reverse Sampling" (3.0), "Non-Linear Null Space Priors" (2.5) — typical reject papers with limited novelty or weak results.
- Middle anchors (3.5–7.5): "Consistency Models as PnP Priors" (4.0), "Provable Derivative-Free Inference" (4.5), "Noise-Adaptive Diffusion Sampling" (4.5), "Mode-seeking for inverse problems" (4.0) — mixed-acceptance papers on related topics.
- Strong anchors (> 7.5): The Polar Express (8.0), VIST3A (8.0) — topically unrelated (matrix methods, text-to-3D).

Initial bracket: The paper is clearly above the weak band (it has a novel method and strong experiments). It sits somewhere in the 4.5–7.5 range.

**Round 2 (Narrowing, 4.5–7.5):**
- "Provably Accelerated Imaging with RISP" (6.0, Poster, scores 6/4/6/8) — Score-based prior + convergence theory + inverse problems. Similar structure to the paper under review. RISP also assumes Lipschitz/Hessian conditions not verified, lacks a systematic ablation. **The paper under review is comparable in quality to RISP** (similar strengths in theory+experiments, similar weaknesses in assumptions-vs-practice).
- "Efficient Approximate Posterior Sampling" (6.0, Poster, scores 4/8/4/8) — Theoretical posterior sampling with score models. Strong theory, weak experiments. The paper under review has stronger empirical validation.
- FAST-DIPS (6.0, Poster) — ADMM-style splitting for diffusion priors.
- "Distributional Consistency Loss" (5.0, Poster) — Different approach, less closely related.

**Final anchor comparison:** The most topically similar anchor is RISP (6.0), which has a comparable profile: novel methodology, convergence guarantees under mild assumptions that are not fully verified, competitive experiments. The paper under review has a more novel denoiser design than RISP's contribution but shares similar theory-practice gaps. **Final score: 6.0**, matching the strongest relevant anchor.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>