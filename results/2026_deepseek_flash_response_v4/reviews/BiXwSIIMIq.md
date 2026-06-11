## Summary

The paper proposes AC-DC, a three-stage score-based denoiser (auto-correction via additive Gaussian noise, directional correction via conditional Langevin dynamics, and Tweedie/ODE score-based denoising) designed to mitigate the mismatch between ADMM iterates and the noisy data manifolds on which pretrained score functions operate. The paper provides convergence guarantees (weakly nonexpansive property → fixed-point ball convergence) for ADMM-PnP with the AC-DC denoiser, and validates the method across seven inverse problems on FFHQ and ImageNet, showing consistent improvements over baselines.

## Strengths

- **Novel AC-DC denoiser (Algorithm 1)** with a three-stage structure that explicitly addresses the manifold mismatch problem for score-based denoisers in ADMM. The ablation in Figure 5 directly validates that increasing DC steps (J=0→10→20) progressively reduces artifacts, isolating the effect of the DC component.

- **First convergence guarantees for ADMM-PnP with score-based denoisers.** Theorems 1–3 extend prior ADMM-PnP theory (Ryu et al., 2019; Chan et al., 2016) from contractive/bounded denoisers to the score-based setting, establishing weakly nonexpansive and boundedness properties — a meaningful step forward for the theory of score-based PnP methods.

- **Consistent empirical gains over 7 baselines across 14 task×dataset configurations.** Ours-tweedie/Ours-ode achieve best or second-best on nearly every metric, with margins of 0.4–1.4 dB PSNR over the strongest PnP competitor (DAPS) on most tasks, across super-resolution, random/box inpainting, motion/Gaussian deblurring, and phase retrieval.

- **Clear diagnosis of the primal-dual difficulty.** The paper identifies (lines 21–22, 117) that dual variables in ADMM further distort the noise geometry of the iterates relative to the score's training manifolds, explaining why prior score-based PnP work focused on primal algorithms and justifying the need for the proposed correction mechanism.

## Weaknesses

### Major

- **Theory-practice gap on convergence regimes:** Theorem 1–2 require ℓ to be μ-strongly convex and use constant ρ, while many experimental tasks (phase retrieval, inpainting) are not strongly convex. Theorem 3 removes convexity but requires adaptive ρ (the ρ-increasing rule), while experiments use constant ρ. The limitations section acknowledges this honestly ("it is therefore desirable to establish convergence guarantees for constant step sizes in such settings"), but the net result is that the theoretical results do not cover the experimental setup used, and vice versa. This weakens the paper's central claim of providing convergence guarantees for the method as actually deployed.

- **DC stationarity assumption:** Theorems 2 and 3 assume "the DC step reaches the stationary distribution for each k." In a 256×256 image space (~196k dimensions), achieving stationarity with Langevin dynamics would require a number of steps far exceeding the J=10 used in experiments. The paper references "counterparts removing this assumption" in Appendix E.2 (line 207), but the main-text theorems as presented assume a condition known not to hold at the scale and step count used in practice. This creates a gap between what the theory assumes and what the method actually implements.

- **Missing efficiency comparison:** The AC-DC denoiser is computationally expensive (up to 1000 Adam iterations per outer step × subproblem optimization, plus J=10 Langevin steps per outer iteration, plus denoising). No runtime, wall-clock time, or NFE comparisons are reported against baselines like DPS, DDRM, or DiffPIR, which are substantially cheaper one-shot diffusion samplers. The limitations section mentions this qualitatively but provides no quantitative data. This makes it impossible to assess whether the quality improvements justify the computational cost.

### Minor

- **Modest improvement margins:** Gains over DAPS are consistent but typically 0.4–1.4 dB. On box inpainting, DCDP has higher PSNR (25.23 vs 24.03 for Ours-tweedie), though Ours wins on SSIM and LPIPS. The improvements are real but modest relative to the method's complexity.

- **No ablation isolating the full pipeline from simpler alternatives:** Figure 5 compares J=0 (AC-only) vs J>0 (AC+DC), which validates the DC contribution. However, there is no comparison against a baseline that applies Tweedie denoising directly to the ADMM iterate without any AC or DC preprocessing (i.e., the plain score-based denoiser in the same ADMM framework). This makes it hard to attribute the gains specifically to the AC-DC mechanism versus the ADMM formulation and hyperparameter choices.

- **Unexplained notation:** The DC Langevin step (Algorithm 1, line 106) uses a term `1/σ_{z_t}²` that is not defined in the main text. It is likely related to the noise level but should be explicitly specified.

### Trivial

- Table 1 has minor formatting artifacts ("DiPIR" likely a parser artifact for DPIR; some empty PMC entries).

## Nice-to-Haves

- Runtime or NFE comparison with baselines to contextualize quality improvements against computational cost.
- Sensitivity analysis on the σ^{(k)} schedule parameters to connect the heuristic linear schedule to the theoretical rate conditions.
- A baseline that applies Tweedie denoising directly to ADMM iterates (without AC or DC) within the same framework.

## Removed Points

These points are flagged to be removed; treat them with caution:

- "SNORE is cited but not compared quantitatively" — REMOVED. The paper is not required to compare against every cited method; SNORE is a primal method, not designed for ADMM.
- "Phase retrieval on ImageNet PSNR 17.77 is very low" — REMOVED. Phase retrieval is intrinsically hard; the low PSNR reflects the problem difficulty and is not hidden by the paper.
- "Formatter issues in Table 1" — REMOVED as parser artifacts from the PDF extraction process.
- "Gaussian approximation in DC step is circular reasoning" — REMOVED. The paper states specific conditions ("under proper scheduling" and "mild regularity conditions"), which is standard for such approximations.
- "No AC ablation in Figure 5" — PARTIALLY REMOVED. Figure 5 does compare J=0 (AC-only) vs J>0 (AC+DC). However, a true "no processing" baseline (Tweedie directly on ADMM iterates without any AC or DC) is missing — kept as a Minor point above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the known tension between idealized theoretical assumptions and practical heuristics — a challenge common in the PnP literature. The paper's transparent acknowledgment of its own limitations in Section 7 is notably candid but does not resolve the underlying gaps.

## Suggestions

- Reframe the theoretical claims to clearly delineate which theorems apply to which experimental regimes, with explicit caveats where assumptions are not met by the experiments.
- Provide runtime or NFE comparisons to contextualize the quality improvements against computational cost.
- Include a simpler baseline within the ADMM framework that applies Tweedie denoising directly (without AC or DC preprocessing) to isolate the contribution of each pipeline component.
- Clarify the notation for σ_{z_t}² in Algorithm 1.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Prior Mismatch in PnP-ADMM (HXjXPQU3yJ) | 6.25 | R2 | Most comparable — PnP-ADMM + mismatch theory. Our paper has broader experiments and a more novel method, but a larger theory-practice gap. |
| Restoration Network as Implicit Prior (x7d1qXEn1e) | 6.25 | R2 | PnP extension with convergence theory. Comparable quality; our paper has more tasks but a more significant assumption gap. |
| Variational Perspective on Inverse Problems (1YO4EE3SPB) | 5.50 | R1 | Diffusion-based inverse problem solver with theory concerns. Our paper is stronger experimentally and has more novel method. |
| PnP-Flow (5AtHrq3B5R) | 5.50 | R2 | PnP + Flow Matching. Similar scope; our paper has more extensive experiments. |
| DiracDiffusion (bEDTZxwJjT) | 5.50 | R1 | Diffusion inverse problems, rejected. Our paper is theoretically and experimentally stronger. |
| Fast and Noise-Robust Diffusion Solvers (Z9Odi09Rv9) | 4.75 | R1 | Had technical math errors. Our paper is substantially stronger. |

**Round 1 bracket:** Between 4.5 and 7.0.

**Round 2 narrowing:** Closest comparison is the 6.25 PnP-ADMM anchor (HXjXPQU3yJ). Our paper matches it in theoretical ambition and exceeds it in experimental breadth, but has a larger theory-practice gap. The 5.50–5.75 anchors are weaker in experimental scope or method novelty. This places our paper slightly above the 5.50 tier but below a clean 7+.

**Final score: 6.0** — A solid paper with genuine contributions (novel denoiser design, first score-based ADMM-PnP convergence theory, extensive experiments) tempered by notable gaps between theoretical assumptions and practical deployment, and missing efficiency analysis.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>