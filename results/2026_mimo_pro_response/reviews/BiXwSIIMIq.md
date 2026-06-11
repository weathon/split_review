Now I have enough calibration data. Let me finalize the review.

**Calibration Analysis:**

Key anchor papers retrieved:
- **HXjXPQU3yJ** (avg 6.25, Reject): "Prior Mismatch and Adaptation in PnP-ADMM" — Most topically similar. PnP-ADMM with convergence analysis, but narrower experiments (only SR/deblurring). Reviewed paper is stronger in method novelty and experimental breadth.
- **DsEhqQtfAG** (avg 6.50, Accept): "Decomposed Diffusion Sampler" — Diffusion for inverse problems with theoretical insight, accepted. Similar contribution level.
- **kRBQwlkFSP** (avg 6.75, Accept): "DiffStateGrad" — Diffusion for inverse problems with manifold projection. Similar experimental setup (FFHQ/ImageNet, 7 inverse problems). Has computational cost analysis the reviewed paper lacks.
- **x7d1qXEn1e** (avg 6.25, Accept): "A Restoration Network as an Implicit Prior" — Convergence analysis for inverse problems, accepted.
- **kNPcOaqC5r** (avg 5.75, Accept): "Learned Proximal Networks" — Convergence guarantees for PnP, accepted.
- **66arKkGiFy** (avg 5.75, Accept): "PnP Posterior Sampling under Mismatch" — PnP convergence, accepted.
- **Z9Odi09Rv9** (avg 4.75, Reject): "Fast and Noise-Robust Diffusion Solvers" — Diffusion for inverse problems, rejected.
- **9mX0AZVEet** (avg 6.00, Reject): "Improving Diffusion Models for Inverse Problems" — Diffusion for inverse problems, rejected.

**Round 1 bracket:** Between 5.75 and 7.0. The paper is clearly stronger than the 4.75 rejected paper and comparable to the 6.25-6.75 accepted papers. It has stronger method novelty and broader experiments than HXjXPQU3yJ (6.25 rejected) but has a significant computational cost gap.

**Final calibration:** The paper sits at approximately 6.5 — comparable to DsEhqQtfAG (6.50 accepted) and kRBQwlkFSP (6.75 accepted). It has a novel method, non-trivial convergence theory, and broad evaluation, offset by missing computational cost analysis and the W hyperparameter gap.

---

## Summary
This paper proposes the AC-DC denoiser — a three-stage score-based denoiser (Auto-Correction via additive Gaussian noise, Directional Correction via conditional Langevin dynamics, and standard score-based denoising) for integration into ADMM-based plug-and-play inverse problem solving. The paper provides convergence analysis showing fixed-point ball convergence under both fixed and adaptive step-size schemes, and demonstrates consistent improvements over baselines across 7 inverse problems on 2 datasets.

## Strengths
- **Well-motivated DC stage for manifold alignment**: The paper clearly identifies the manifold mismatch problem — ADMM iterates contaminated by dual variables do not lie on the noisy data manifolds where score functions are trained — and proposes a principled three-stage solution. The DC step uses conditional Langevin dynamics targeting p(z_σ|z_ac), whose support is provably contained in the noisy data manifold M_σ(k) (Section 3, Eq. 10, lines 129–135). This goes beyond prior noise-injection/purification methods that only perform the AC step.

- **Non-trivial convergence analysis extending prior ADMM-PnP theory**: The paper provides three theorems: Theorem 1 generalizes Ryu et al. (2019) from strictly contractive to weakly nonexpansive residuals (Assumption 1, Eq. 12); Theorem 2 proves the AC-DC denoiser satisfies this assumption with high probability (Eqs. 14–16); Theorem 3 removes strong convexity on ℓ and establishes convergence under an adaptive step-size schedule (lines 201–217). This is the first convergence analysis of ADMM-PnP with score-based denoisers.

- **Comprehensive evaluation across 7 inverse problems on 2 datasets**: Table 1 reports PSNR, SSIM, and LPIPS averaged over 100 images on FFHQ 256×256 and ImageNet 256×256 for super-resolution, Gaussian deblurring, motion deblurring, box inpainting, random inpainting, phase retrieval, and HDR. Both Ours-tweedie and Ours-ode achieve best or second-best in the large majority of settings, with notable margins (e.g., FFHQ random inpainting: 32.844 vs. 31.652 PSNR over DAPS; FFHQ phase retrieval: 27.944 vs. 26.707).

- **Framework flexibility through two denoiser variants**: Both Tweedie-based and ODE-based final denoising stages achieve strong results, demonstrating the AC-DC framework is agnostic to the specific denoising strategy.

- **Direct ablation evidence for DC contribution**: Figure 5 shows J=0 (AC-only) leaves severe artifacts on phase retrieval, while J=10 and J=20 progressively yield cleaner reconstructions (lines 287–291).

## Weaknesses

### Fatal
None

### Major

- **Missing computational cost analysis**: Each outer ADMM iteration involves solving the x-subproblem via Adam with up to 1000 gradient steps, J=10 Langevin DC steps each requiring a score evaluation, and one final score evaluation — totaling ~11 score evaluations and up to ~1000 loss gradient evaluations per iteration, across K=W+10 total iterations. By contrast, DiffPIR uses ~1-2 score evaluations per iteration. The paper acknowledges this in the Limitations (line 379: "each iteration of AC-DC denoiser needs multiple score evaluations. Reducing the required NFEs could significantly improve its efficiency") but provides no runtime data, no FLOP counts, and no wall-clock comparisons. Without this, it is impossible to assess whether the quality improvements (~0.5–1.5 dB over DAPS) justify the computational cost. This is a significant omission for a paper whose primary empirical claim is improved solution quality.

- **Key hyperparameter W is unspecified**: The hyperparameter settings section defines σ^{(k)} = max(0.1, 10 − (10 − 0.1)·k/W) and K = W + 10 (line 297), but never states the numerical value of W. This parameter controls the entire noise schedule, the number of outer iterations, and hence the algorithm's behavior and computational cost. Its absence hampers reproducibility.

- **Convergence theorems rely on practically violated assumption**: Theorems 2 and 3 both assume "the DC step reaches the stationary distribution for each k" (lines 183, 205). With only J=10 Langevin steps in 256×256×3 dimensions, this assumption is unlikely to hold. The paper points to Appendix E.2 for non-stationary versions (line 207), but the main theorems as presented do not directly apply to the implemented algorithm. The non-stationary convergence analysis should arguably be foregrounded in the main text since it describes the algorithm as actually run.

### Minor

- **No variance or statistical significance in results**: All metrics in Table 1 are single averages over 100 images with no standard deviations or confidence intervals. Given margins between methods are sometimes small (~0.9 dB for SR on FFHQ) and methods involve stochastic components, variance reporting would strengthen confidence.

- **Confusing duplicate/empty PMC rows in Table 1**: PMC appears multiple times per task with different values (e.g., Superresolution shows PMC at 27.761 and 23.774 for FFHQ, lines 324-325) and many empty cells. These should be labeled distinctly.

- **DCDP outperforms method on box inpainting without acknowledgment**: On FFHQ box inpainting, DCDP achieves PSNR 25.230 vs. 24.025 for Ours-tweedie (line 363). The text claims "in almost all of the inverse problems" (line 303) but should explicitly note where the method does not win.

### Trivial
- Minor naming inconsistency: baseline section says "DPIR" (line 295) but Table 1 uses "DiPIR" (line 321).

## Nice-to-Haves
- A quantitative ablation of DC step count J (PSNR/SSIM vs. J) would complement the visual-only ablation in Fig. 5.
- Empirical validation of the Gaussian approximation quality for p(z_ac|z_σ) used in the DC step (Eq. 10).
- Sensitivity analysis of the method to the σ schedule and W hyperparameter.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's speculative framing that computational cost is "orders of magnitude higher" than baselines — while the computational cost analysis is genuinely missing (kept as Major), the specific magnitude claim depends on information not available (e.g., convergence behavior of Adam, early stopping frequency).
- Strength about "the problem being important" — generic, not specific to this paper's evidence.

## Novel Insights
The paper's key novel insight is that noise injection alone (the AC step) is insufficient to align ADMM iterates with score-trained manifolds — directional correction via conditional Langevin dynamics is needed to actually steer iterates onto the manifold. This is grounded in the conditional score decomposition (Eq. 10) and the support argument (supp(z_σ|z_ac) ⊆ M_σ), providing theoretical grounding for why DC works beyond prior noise-injection approaches. The identification of dual-variable contamination as a distinct source of manifold mismatch in primal-dual methods (vs. primal-only PnP) is also a useful conceptual contribution.

## Suggestions
1. Report wall-clock runtime and NFEs for at least one task, comparing with DAPS and DiffPIR.
2. Move the non-stationary convergence analysis (Appendix E.2) to the main text, since J=10 does not reach stationarity.
3. State the numerical value of W and ideally include sensitivity analysis.
4. Add standard deviations across the 100 test images to Table 1.
5. Clean up duplicate/empty PMC rows in Table 1 with proper labels.

## Score and Decision

**Anchors retrieved across all rounds:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| HXjXPQU3yJ | 6.25 (Reject) | 1 | PnP-ADMM convergence, narrower experiments — reviewed paper is stronger |
| x7d1qXEn1e | 6.25 (Accept) | 1 | Restoration network prior with convergence — similar contribution level |
| kNPcOaqC5r | 5.75 (Accept) | 1 | Learned proximal networks — less empirically comprehensive |
| 66arKkGiFy | 5.75 (Accept) | 1 | PnP posterior sampling under mismatch — less empirically comprehensive |
| Z9Odi09Rv9 | 4.75 (Reject) | 1 | Diffusion solver, fairness concerns — reviewed paper is clearly stronger |
| DsEhqQtfAG | 6.50 (Accept) | 2 | Decomposed diffusion sampler — comparable contribution level |
| kRBQwlkFSP | 6.75 (Accept) | 2 | DiffStateGrad — similar experimental scope, has runtime analysis reviewed paper lacks |
| 9mX0AZVEet | 6.00 (Reject) | 2 | Diffusion for inverse problems — reviewed paper is stronger |
| h8GeqOxtd4 | 6.25 (Accept) | 2 | Score estimation theory — different focus |
| j8hdRqOUhN | 7.50 (Accept) | 2 | ReSample for latent diffusion — broader benchmark, higher score |

**Round 1 bracket:** 5.75–7.0. The paper is clearly stronger than the 4.75 reject (Z9Odi09Rv9) and comparable to or slightly above HXjXPQU3yJ (6.25 reject, similar topic but narrower experiments). It sits near DsEhqQtfAG (6.50 accept) and kRBQwlkFSP (6.75 accept).

**Final score:** 6.5. The paper has a genuinely novel method (AC-DC denoiser), non-trivial convergence theory (first for ADMM-PnP with score-based denoisers), and comprehensive empirical evaluation. The missing computational cost analysis and unspecified W hyperparameter are significant gaps that prevent a higher score, but the overall contribution is solid and above the acceptance threshold.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>