Now I have good calibration. Let me synthesize my final review.

**Round 1 Bracket:** Between 5.5 and 7.0. The paper is clearly stronger than PnP-Flow (5.50) and the variational RED-diff paper (5.50), comparable to but slightly different from the PnP-ADMM mismatch paper (6.25, rejected), and a bit below the unified diffusion convergence theory paper (6.50, accepted).

**Round 2 Narrowing:** The PnP-ADMM mismatch anchor (6.25, rejected) had cleaner theory but narrower experiments. Our paper has a novel method, broader experiments, but a theory-practice gap. The optimal covariance paper (6.00, rejected) had incremental novelty. Our paper lands at **6.0** — genuine contributions with notable but addressable gaps.

---

## Summary
This paper proposes ADMM-PnP with the AC-DC denoiser: a three-stage procedure (Auto-Correction via Gaussian noise, Directional Correction via conditional Langevin dynamics, and Denoising via Tweedie/ODE) embedded into ADMM for inverse problems. The key contributions are a principled mechanism for aligning ADMM iterates with the noisy manifolds on which score functions are trained, and convergence analysis establishing fixed-point ball convergence with high probability under both constant and adaptive step-size schedules.

## Strengths
- **Principled manifold alignment.** The AC-DC design has clear rationale: the AC stage pulls iterates toward noisy manifolds; the DC stage refines alignment via conditional Langevin dynamics targeting p(z_σ|z_ac) whose support lies on M_σ(k); the denoising stage then evaluates the score function within its effective operating regime (Section 3, Algorithm 1). This directly addresses a recognized gap in score-based PnP methods.
- **Convergence theory for score-based denoisers in ADMM.** Theorem 2 proves the AC-DC denoiser satisfies weak non-expansiveness with explicit parameterized ε_k² and δ_k² bounds (Eqs. 15-16) in terms of the noise schedules, score smoothness M, and dimension d. Theorem 3 removes the strong convexity requirement via an adaptive step-size scheme. These extend prior ADMM-PnP convergence results (Ryu et al., 2019; Chan et al., 2016) to score-based settings — a first in the literature.
- **Strong empirical performance.** Table 1 shows Ours-tweedie achieves best PSNR and SSIM on super-resolution, random inpainting, motion deblurring, Gaussian deblurring, and phase retrieval across both FFHQ and ImageNet, and Ours-ode consistently places second. The DC ablation (Figure 5) confirms the directional correction stage is essential: J=0 produces severe artifacts, while J=10 and J=20 progressively improve quality.
- **Honest limitations discussion.** Section 7 acknowledges the theoretical-practical gap (adaptive step sizes vs. constant, heuristic noise schedules), NFE cost, and the lack of recoverability analysis — providing useful context for the claims.

## Weaknesses

### Fatal
None.

### Major
- **Theory-practice gap on Langevin mixing.** Theorems 2 and 3 explicitly assume the DC Langevin dynamics "reaches the stationary distribution for each k." In practice, the algorithm uses J=10 Langevin steps (Section 6). The paper footnotes that relaxed versions removing this assumption exist in Appendix E.2, but the main-text theorems as presented describe an idealized algorithm rather than the one benchmarked. Additionally, the asymptotic scheduling condition lim σ^(k) = 0 (required by Theorem 2(b) and Theorem 3(b)) contradicts the practical schedule σ^(k) = max(0.1, ...), so the asymptotic theory does not describe the algorithm as actually run.
- **No empirical convergence evidence.** The paper's title announces a "convergent" framework and convergence analysis occupies roughly a third of the main text, yet the experiments contain no convergence diagnostics whatsoever: no PSNR vs. iteration plots, no residual norm decay, no dual variable norm trajectories. The reader cannot assess whether the algorithm converges in practice, at what rate, or whether the δ-ball radius matters.
- **Missing experimental results for claimed tasks.** The introduction (line 28) claims validation on high dynamic range (HDR) and the task description (Section 6, item g) lists nonlinear deblurring. Neither appears in Table 1 or any figure. The HDR claim in the introduction is unsupported.
- **Unreported computational budget.** The decay window W, which determines total ADMM iterations K = W + 10 and thus total NFE (roughly 11× score evaluations per ADMM iteration compared to single-pass denoisers like DiffPIR), is never given a numeric value. No NFE or runtime comparison with baselines is provided, making it impossible to judge whether performance gains reflect algorithmic improvement or simply more computation.

### Minor
- **Missing baseline results.** DPIR is listed as a baseline (line 295) but has zero entries in Table 1. DDRM appears for only 2 of 7 tasks. The DDPM entry in the Gaussian blur row is not listed among the baselines in Section 6.
- **Limited DC ablation.** The DC ablation (Figure 5) covers only phase retrieval with purely visual comparison — no quantitative metrics (PSNR/SSIM/LPIPS) vs. J are reported.
- **Untested generalization.** All experiments use a single pretrained score model from Chung et al. (2023), so results are tied to one specific score network architecture and training setup.
- **Gaussian approximation unverified.** The condition Var(s^(k))^(1/2) ≪ σ^(k) that justifies the Gaussian likelihood approximation in the DC step (Eq. 10) is never empirically validated.

### Trivial
- PMC appears multiple times in Table 1 with partially empty cells (likely a formatting artifact from parsing).
- "Qualitiative" vs. "Qualitative" header inconsistency in Section 6 (parsing artifact).

## Nice-to-Haves
- A controlled NFE-matched comparison to isolate whether the AC-DC mechanism itself improves results over spending more compute on existing methods.
- Convergence diagnostics (PSNR and residual norm vs. ADMM iteration) to directly support the central convergence claim.
- Problem-adaptive noise scheduling strategies to replace the heuristic linear schedule.
- Analysis of finite Langevin steps in the convergence theory rather than the idealized stationary-distribution assumption.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "The theoretical contribution is incremental."** This is a significance judgment, not a verifiable weakness. The paper makes a legitimate extension of existing theory to score-based denoisers and is upfront about its scope (line 221: "all theoretical results in this section focus on fixed-point convergence, which is not the strongest form of convergence guarantees").
- **Harsh Critic: "The relationship between δ̃² = δ²ε̄/ε in Theorem 1 appears under-defined."** The notation is fully defined in the theorem statement (line 167). Lack of motivation is a presentation nitpick, not a substantive issue.
- **Harsh Critic: "The S < ∞ condition is non-standard and its relationship to Assumption 3 (coercivity) should be clarified."** The paper already explains this at lines 219-220: "the condition S < ∞ ensures that there exists at least one point in X where the score norm is finite. This prevents pathological cases where the score diverges everywhere."
- **Harsh Critic: "The discussion of the Gaussian approximation needs more care — the relationship between DC step target and training manifolds is hand-wavy."** The paper explicitly acknowledges this is approximate ("Assume that the forward process used in training the score has sufficiently small time intervals, M_σ(k) is approximately contained in {M_σt}"). The approximation is transparent.
- **Harsh Critic: section-by-section technical nitpicks about ν_k interaction with scheduling, δ̃ motivation.** These are presentation refinements that do not undermine contributions.
- **Strength Finder: "Comprehensive experimental validation across seven inverse problems."** HDR and nonlinear deblurring results are missing; only 6 tasks appear in Table 1.

## Novel Insights
The combination of ADMM with score-based denoising reveals a structural tension that prior work has not systematically addressed: ADMM's dual variables distort the noise geometry of iterates, making naive score-function application unreliable. The AC-DC framework's insight is that the dual variable contribution can be treated as structured noise that the conditional Langevin dynamics step can partially correct — effectively decoupling the optimization geometry (handled by ADMM) from the data geometry (handled by the score function). This perspective may generalize to other primal-dual methods and provides a template for future score-based PnP convergence analyses.

## Suggestions
- Report W explicitly and provide NFE/runtime comparisons with baselines.
- Include convergence diagnostics (PSNR and residual norm vs. ADMM iteration) — this would directly support the paper's core claim and take relatively little experimental effort.
- Either include HDR and nonlinear deblurring results or remove the corresponding claims from the introduction and task description.
- Address the theory-practice gap: either demonstrate empirically that J=10 suffices for near-stationarity, or present the finite-step convergence results from Appendix E.2 in the main text.
- Clean up the baseline entries in Table 1 (DPIR, DDRM, PMC rows).

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| PnP-ADMM Mismatch & Adaptation | HXjXPQU3yJ | 6.25 | R1 | Very similar topic (PnP-ADMM convergence, mismatch). Cleaner theory, narrower experiments. Our paper has novel method + broader experiments + stronger results but theory-practice gap. Comparable overall — our paper slightly weaker on theory, stronger on empirics. |
| PnP Posterior Sampling Mismatch | 66arKkGiFy | 5.75 | R1 | PnP-ULA mismatch analysis. Our paper has method + convergence theory + broader experiments. Clearly stronger. |
| Unified Convergence for Score-Based Diffusion | HrdVqFSn1e | 6.50 | R1 | Pure convergence theory for diffusion samplers. Cleaner, more complete theory. Our paper adds practical method + experiments. Our paper slightly weaker overall due to theory gap. |
| PnP-Flow | 5AtHrq3B5R | 5.50 | R2 | PnP with flow matching. Our paper clearly stronger (better theory, broader comparisons, clearer method). |
| Variational Perspective on Diffusion IP | 1YO4EE3SPB | 5.50 | R2 | RED-diff. Our paper has more theory, broader experiments. Clearly stronger. |
| Optimal Posterior Covariance for Diffusion IP | 9mX0AZVEet | 6.00 | R2 | Incremental novelty (optimizing r_t²). Our paper has novel method design + convergence theory. Stronger. |
| Restoration Network as Implicit Prior | x7d1qXEn1e | 6.25 | R2 | PnP with restoration networks. Our paper more specifically targets score-based denoisers + ADMM. Comparable quality. |
| Score Estimation in Diffusion Models | h8GeqOxtd4 | 6.25 | R2 | Score estimation theory. Different focus. Our paper more applied. |

**Round 1 Bracket:** 5.5–7.0  
**Round 2 Narrowing:** The paper is stronger than the 5.50 anchors (PnP-Flow, variational RED-diff) and the 6.00 anchor (optimal covariance), comparable to the PnP-ADMM mismatch paper (6.25) but with a notable theory-practice gap, and below the unified diffusion convergence paper (6.50).  
**Final Score:** 6.0 — genuine contributions (novel method, first convergence theory for score-based PnP-ADMM, strong empirical results) weighed against addressable but significant gaps (theory-practice mismatch on Langevin mixing, missing convergence evidence and results, unreported computational budget).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>