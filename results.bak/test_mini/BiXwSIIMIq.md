Good, I have all the evidence I need. Let me now write the final consolidated review.

## Summary

This paper proposes the AC-DC denoiser, a three-stage method (additive noise auto-correction, Langevin-based directional correction, and score-based denoising) that addresses manifold mismatch when integrating score-based denoisers into ADMM-based plug-and-play frameworks. It provides convergence analysis showing the denoiser is weakly nonexpansive (high-probability ball convergence under constant step size) and bounded (convergence under adaptive step sizes). Experiments across seven inverse problems on FFHQ and ImageNet show competitive or state-of-the-art results.

## Strengths

- **Novel AC-DC denoiser design targeting manifold mismatch in ADMM.** The paper identifies that dual variables in ADMM distort noise geometry of iterates, making naive score-based denoising ineffective. Algorithm 1's three-stage pipeline (AC → DC → Tweedie/ODE denoising) is a principled response to this problem that goes beyond prior noise-injection heuristics (DiffPIR, RED-diff). The DC stage using conditional Langevin dynamics is a distinctive addition that the ablation (Fig. 5) confirms improves reconstruction quality.

- **First convergence analysis for score-based denoisers within ADMM-PnP.** The paper adapts and extends prior ADMM-PnP fixed-point theory (Ryu et al., 2019; Chan et al., 2016) to score-based denoisers. Theorem 1 extends convergence from strictly contractive residuals to weakly nonexpansive ones, and Theorems 2-3 show the AC-DC denoiser satisfies these conditions with high probability. Theorem 3 further relaxes the strong convexity requirement, covering nonconvex losses like phase retrieval.

- **Comprehensive empirical evaluation across diverse inverse problems.** The method is tested on seven tasks (super-resolution, random/box inpainting, motion/Gaussian deblurring, phase retrieval, HDR) on two datasets (FFHQ, ImageNet) with nine baselines spanning sampling-based (DPS, DDRM), PnP (DiffPIR, RED-diff, DPIR, DCDP, PMC), and recent (DAPS) methods. Ours-tweedie/Ours-ode achieve best or second-best metrics in the majority of settings.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental schedules do not satisfy the asymptotic conditions required by the convergence theorems.** Theorem 2(b) requires $\lim_{k\to\infty} (\sigma^{(k)})^2 \nu_k = 0$; Theorem 3(b) requires $\lim_{k\to\infty} \sigma^{(k)} = 0$ and $\lim_{k\to\infty} \sigma_{s^{(k)}} = 0$. However, the experimental schedule sets $\sigma^{(k)} = \max(0.1, 10 - (10-0.1)\cdot k/W)$ (line 307), which decays to 0.1 and then remains constant — it never goes to zero. Similarly, $\sigma_{s^{(k)}} = 0.1/\sqrt{\sigma^{(k)}}$ is bounded below by ~0.316. Consequently, the convergence guarantees proven in Theorems 2(b) and 3(b) do **not** apply to the algorithm as implemented in the experiments. This is a fundamental disconnect between the theoretical claims and the empirical validation. The paper's title claims "A Convergent Plug-and-Play Framework," but the convergence is established only for parameter schedules that differ from those actually used.

2. **No computational cost comparison (runtime or NFEs) is provided.** The method solves each $\mathbf{x}$-subproblem with up to 1000 Adam iterations per outer ADMM iteration, plus 10 DC Langevin steps and additional score evaluations. This likely incurs substantially higher cost than baselines like DPS (~1000 NFEs total) or DiffPIR. Without runtime or NFE data, the reader cannot assess whether the modest PSNR improvements (typically 0.5–1 dB over the next best method) reflect algorithmic superiority or simply a larger compute budget. The limitations section acknowledges "each iteration of AC-DC denoiser needs multiple score evaluations," but the experiments do not quantify this cost, making the empirical comparisons difficult to evaluate.

### Minor

1. **The theory assumes the DC step reaches the stationary distribution** of the Langevin dynamics at each ADMM iteration (Theorems 2 and 3). The implementation uses $J=10$ Langevin steps, which is far from sufficient for mixing in high-dimensional image spaces. A footnote (line 217) points to Appendix E.2 for counterparts removing this assumption, and the main text cites this as "for notation conciseness." However, the central theoretical results in the main body are stated under an assumption the algorithm manifestly violates.

2. **Improvement margins are modest and not universal.** While Ours-tweedie/Ours-ode are often best, the PSNR gains over DAPS are typically 0.5–1.0 dB. On box inpainting (FFHQ), DCDP achieves higher PSNR (25.230 vs. 24.025). On several LPIPS metrics, DAPS matches or beats the proposed method. The claim of "consistent improvement" (Abstract, line 19) overstates the results.

3. **Limited ablation of the DC component.** The ablation study (Fig. 5) demonstrates the value of DC steps for phase retrieval, but this is only one task. Evidence across more inverse problems (e.g., deblurring, inpainting) would strengthen the claim that the DC stage is broadly beneficial.

4. **No statistical significance reported.** Metrics are averaged over 100 images without standard deviations or confidence intervals. Given the variability across images, this makes it difficult to assess whether differences between methods are meaningful.

### Trivial
None.

## Nice-to-Haves
- An ablation studying the sensitivity to the number of Adam iterations used to solve the $\mathbf{x}$-subproblem would be valuable. The paper uses up to 1000 iterations, but fewer might suffice, greatly reducing computational cost.
- A sensitivity analysis for key hyperparameters ($\eta^{(k)}$, $\sigma_{s^{(k)}}$ schedule, decay window $W$) would help practitioners apply the method to new problems.

## Removed Points
- **"Stationary distribution assumption is fatal"** — The paper explicitly points to Appendix E.2 (stripped by parser) for counterparts removing this assumption. This concern is partially addressed in the actual submission; retained as a minor weakness rather than a fatal one.
- **"The notation in Eq. (9) is garbled (self-referential)"** — This is a parser artifact from PDF extraction, not present in the original submission.
- **"Table 1 has duplicated rows (PMC appearing multiple times) and missing entries"** — Parser artifact from stripped sections.
- **"The proof is deferred to the appendix"** — Standard practice; not a weakness.
- **"Box missing region is large (128×128) — may favor methods that can hallucinate"** — Speculative concern without evidence.
- **"Weakly nonexpansive condition is central, proof deferred"** — Not a weakness; paper structure is appropriate.
- **"The improvement could reflect compute budget"** — Merged into Major weakness #2 (computational cost comparison).
- Various generic "strength" claims from the Strength Finder about problem importance — these are superficial.

## Novel Insights
None beyond the paper's own contributions. The synthesis of the two reviews surfaces the central tension: the paper makes a genuine algorithmic and theoretical contribution (the AC-DC denoiser, the convergence analysis), but the theory is presented for idealized conditions (stationary Langevin, vanishing noise schedules) that the actual algorithm in the experiments does not satisfy. This gap is the paper's defining weakness and is more clearly exposed by combining the reviewers' perspectives than by either alone.

## Suggestions
1. **Align theory with practice:** Revise the experimental noise schedules to satisfy the asymptotic conditions of the theorems (e.g., let $\sigma^{(k)} \to 0$ over iterations), or reframe the theoretical claims as "convergence guarantees under the following sufficient conditions, which provide intuition for why the method is stable in practice" rather than claiming a convergent framework that the experiments validate.
2. **Report computational cost:** Add a table comparing total NFEs or wall-clock time across all methods. If the method is more expensive, discuss the quality-efficiency trade-off explicitly.
3. **Acknowledge the theory-practice gap explicitly** in the main text, not just in the limitations section. The current framing ("convergent plug-and-play framework") over-claims relative to what is actually established.

## Score and Decision

**Calibration anchors:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| RISP | 8pQsiFyTQi.md | 6.00 | 1,2 | Score-based priors + convergence guarantees. Stronger theory (convergence rate) and better alignment between theory and experiments. Our paper is slightly weaker. |
| PnP-CM (CM+ADMM) | oJP8Geymcr.md | 4.00 | 1 | PnP-ADMM with score-like denoisers. Our paper has stronger theoretical contribution and broader experiments. Our paper is clearly stronger. |
| ReGuidance | VG5iE3rzLz.md | 5.00 | 2 | Diffusion inverse problem solver. Our paper has broader evaluation and more meaningful theory. Our paper is stronger. |
| FAST-DIPS | voMeZVAkKL.md | 6.00 | 2 | ADMM-style diffusion inverse solver with theory. Cleaner alignment between theory and practice. Our paper has wider experimental scope but a bigger theory-practice gap. Comparable, slightly weaker. |
| Non-Linear Null Space Priors | GK9yjjuyRT.md | 2.50 | 1 | Poorly regarded inverse problems paper. Our paper is much stronger. |

**Round 1 bracket:** Based on the initial bracketing, the paper sits between the weak anchors (avg ~2.5-3.0) and strong anchors (avg 8.0+), narrowing to the middle band (3.5-7.5). The most relevant anchors in this band are PnP-CM (4.0) on the lower side and RISP/FAST-DIPS (6.0) on the upper side.

**Round 2 narrowing:** Comparing against RISP (6.0) and FAST-DIPS (6.0), the paper has a broader experimental evaluation but a more significant theory-practice gap. Against ReGuidance (5.0) and PnP-CM (4.0), it is clearly stronger. The paper's theoretical contribution is genuine, but the disconnect between convergence conditions and experimental implementation is a concrete weakness that RISP and FAST-DIPS do not share to the same degree.

**Final score:** 5.0. The paper makes a meaningful contribution (novel AC-DC denoiser, first convergence analysis for score-based denoisers in ADMM, broad empirical evaluation), but the convergence theory is presented for conditions that the experimental protocol does not satisfy, and the missing computational cost comparison limits the strength of the empirical claims. The paper would benefit substantially from addressing these gaps before publication.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>