Now I have enough information to write the final consolidated review. Let me compose it.

## Summary
2-3 sentence summary of the paper's contribution.

This paper introduces the AC-DC denoiser, a three-stage score-based denoiser (auto-correction via additive Gaussian noise, directional correction via Langevin dynamics, and Tweedie/ODE denoising) designed for integration into ADMM plug-and-play frameworks to solve inverse problems. The authors address the manifold mismatch between ADMM iterates and score function training manifolds, and provide convergence analysis showing the denoiser satisfies weak nonexpansiveness and boundedness properties under mild conditions. Empirical results on six inverse problems across two datasets show consistent improvements over eight baselines.

## Strengths

### 1. Novel AC-DC denoiser explicitly tackles the manifold-mismatch problem
The three-stage design (AC → DC → score denoising) is a principled attempt to align ADMM iterates with the noisy data manifolds where score functions are trained. The paper clearly identifies the challenge (Section 2) — that ADMM iterates, especially with dual variables, need not lie on these manifolds — and proposes a reasoned solution (Section 3, Algorithm 1). The Gaussian injection (AC) pulls iterates toward manifold neighborhoods, and the Langevin step (DC) refines alignment before score-based denoising. This goes beyond prior work that relies solely on noise injection (DiffPIR, RED-diff).

### 2. First convergence analysis for ADMM-PnP with score-based denoisers
The paper extends ADMM-PnP fixed-point convergence theory (Ryu et al., 2019; Chan et al., 2016) to score-based denoisers. Theorem 1 relaxes the standard contractive residual assumption to weak nonexpansiveness, establishing high-probability fixed-point ball convergence. Theorems 2–3 prove that the AC-DC denoiser satisfies the required properties with high probability under the stated assumptions (smooth log-density, coercivity). This is a genuine theoretical contribution that opens up analysis of score-based denoisers in primal-dual optimization.

### 3. Strong and consistent empirical performance
On six inverse problems (super-resolution, random/box inpainting, Gaussian/motion deblurring, phase retrieval) over two datasets (FFHQ 256×256, ImageNet 256×256), both Ours-tweedie and Ours-ode variants achieve best or second-best PSNR, SSIM, and LPIPS in nearly every case (Table 1). The margin over DAPS (the strongest baseline) is often 1–2 dB PSNR, and the qualitative results (Figures 2–4) show visibly cleaner reconstructions with fewer artifacts.

### 4. Comprehensive benchmarking and public code
The paper compares against eight baselines (DPS, DAPS, DDRM, DiffPIR, RED-diff, DPIR, DCDP, PMC), providing a thorough evaluation. The source code is publicly released, with hyperparameter schedules detailed in Section 6, supporting reproducibility.

## Weaknesses

### Major

**1. The convergence theory assumes the DC Langevin step reaches its stationary distribution, while the algorithm uses a finite J=10 steps.**  
Theorems 2 and 3 state "assume that the DC step reaches the stationary distribution for each k," but Algorithm 1 uses only J=10 Langevin iterations per ADMM outer iteration. Reaching the stationary distribution of a Langevin diffusion requires, in principle, an infinite number of steps. The paper references Appendix E.2 for results removing this assumption (footnote on p. 7), but the main text's theoretical guarantees therefore do not directly cover the executed algorithm. This gap between the theory's premise and the actual implementation is significant and should be discussed upfront rather than in a footnote.

**2. The empirical evaluation lacks standard deviations and confidence intervals.**  
All metrics in Table 1 are reported as single-point averages over 100 images. Without standard deviations or confidence intervals, it is impossible to determine whether the reported improvements (often 1–2 dB PSNR over DAPS) are statistically significant. This is a basic expectation for experimental rigor, especially when claiming consistent improvements.

**3. No computational cost comparison is provided.**  
The AC-DC denoiser requires multiple score function evaluations per ADMM iteration (J=10 Langevin steps plus the Tweedie/ODE denoising step). The paper never reports number of function evaluations (NFEs), wall-clock time, or relative computational cost against any baseline. Since several baselines (e.g., DiffPIR, DAPS) require fewer score evaluations per iteration, the practical trade-off of the method's gains versus its compute overhead is entirely unclear. The limitations section acknowledges this issue qualitatively but provides no quantification.

### Minor

**1. Limited ablation study.**  
The ablation (Figure 5) examines only the number of DC steps (J) and only on a single task (phase retrieval). The contribution of the AC stage is not isolated (e.g., "DC only" without AC), the effect of the denoising step (Tweedie vs. ODE) is not ablated systematically, and sensitivity to key hyperparameters (noise schedule σ⁽ᵏ⁾, step size η⁽ᵏ⁾, penalty parameter ρ) is not explored. While the ablation confirms that DC helps, it does not provide a comprehensive understanding of the design choices.

**2. The Gaussian approximation underlying the DC step is not validated.**  
The DC step relies on approximating the conditional score ∇log p(z_ac^(k) | z_σ^(k)) using a Gaussian likelihood (Equation 10 and the surrounding text), leading to the quadratic term in Algorithm 1 line 5. The paper asserts this holds "under proper scheduling of σ^(k) and mild regularity conditions" but provides no empirical or synthetic evidence that this approximation is reasonable for the iterate distributions encountered during ADMM. If the approximation is poor, the DC step may not steer iterates toward the intended manifold.

**3. The notation σ_{z_t} in Algorithm 1 line 5 is undefined.**  
The update uses 1/σ_{z_t}^2, but this quantity is not defined anywhere in the paper. This makes the algorithm description partially unclear.

**4. The number of ADMM iterations (W, the decay window size) is not specified.**  
The hyperparameter section (p. 9) describes the linear schedule for σ⁽ᵏ⁾ over a "decay window W" and sets the maximum iterations to K = W + 10, but never states the value of W used in experiments. This omission hinders reproducibility.

**5. Several baseline results raise concerns about fair comparison.**  
RED-diff performs anomalously poorly on some tasks (e.g., ~17 dB PSNR on FFHQ super-resolution, ~15 dB on ImageNet Gaussian deblur). While this could be due to inherent limitations of RED-diff with the chosen diffusion model, the paper does not state whether baselines were tuned or how their hyperparameters were selected. A brief statement about baseline tuning would put the comparisons on firmer ground.

### Trivial

- The notation "DiPIR" appears in Table 1 while the text refers to both "DiffPIR" and "DPIR" as separate baselines; this inconsistency should be resolved.
- "DDPM" appears as a baseline row in the Gaussian blur section of Table 1 but is not listed among the eight stated baselines; this should be clarified.

## Nice-to-Haves
- Provide an empirical validation of the Gaussian approximation used in the DC step, e.g., on a simple low-dimensional distribution or via diagnostic plots from the actual ADMM iterates.
- Include an analysis of the sensitivity to the number of ADMM iterations (W) and the noise schedule parameters.
- Report the gap between the stationary distribution assumption and finite-step Langevin dynamics, and summarize the Appendix E.2 results in the main text.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *Equation (9) appears garbled* — removed as likely parser artifact from PDF extraction.
- *Duplicate PMC rows, missing entries* — removed as potentially parser-induced artifacts from complex table extraction; the paper's table format is hard to verify from extracted text.
- *"ball radius r involves unquantified constants"* — removed because unquantified constants in convergence bounds are standard in this literature and do not threaten the paper's claims more than any other PnP convergence analysis.
- *"the paper does not explain why AC+DC is better than noise injection alone"* — the paper provides qualitative motivation (Section 3, Figure 1) and ablation evidence (Figure 5) for this; a formal comparison would strengthen but is not missing.
- *Claims about missing related works* — removed per instructions: I cannot verify presence/absence of related works.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a clear gap between theory (stationary-distribution assumption) and practice (finite-step Langevin), which is a genuinely useful observation for the authors to address. No other novel insight emerges that the paper itself does not already articulate.

## Suggestions
1. **Clarify what the convergence theory actually guarantees for the practical algorithm.** Reframe the main text to explicitly state that the theoretical results assume the DC step reaches stationarity, and summarize what the appendix provides without this assumption. Consider rephrasing "convergent" in the title and abstract to "stable" or "high-probability ball-convergent" to match the results more precisely.
2. **Add standard deviations or confidence intervals to all quantitative results.** Report per-method metrics with error bars (e.g., ± std over the 100 test images) so readers can assess statistical significance.
3. **Report the computational cost** in terms of NFEs or wall-clock time per test image for each method, alongside the quality metrics.
4. **Expand the ablation study** to cover (a) DC-only without AC, (b) varying σ⁽ᵏ⁾ schedule parameters, (c) multiple tasks rather than only phase retrieval, and (d) comparison of Tweedie vs. ODE denoising.
5. **Define all notation used in Algorithm 1** (especially σ_{z_t}) and specify the decay window size W.
6. **Validate the Gaussian approximation** in the DC step with a simple empirical check (e.g., on a toy distribution or by comparing the approximate Langevin update to a more exact Monte Carlo estimate).
7. **Include a brief statement** on how baselines were configured/tuned to ensure fair comparison.

## Score and Decision

I performed calibration in two rounds. Round 1 bracketed the paper between 4.0 and 7.5 by querying on relevant topics. The low band (<3.5) returned unrelated papers (FedADM 3.0, operator networks 2.33). The middle band (3.5–7.5) returned papers on diffusion-based inverse problem solvers (Variational Perspective 5.50, DiracDiffusion 5.50, Fast Noise-Robust 4.75, Monte Carlo guided 4.00). The high band (>7.5) returned strong diffusion model papers (all at 8.0) that this paper does not match in rigor. Round 2 narrowed within (4.0, 6.5), retrieving Prior Mismatch PnP-ADMM (6.25, reject), Variational Perspective (5.50, accept), DiracDiffusion (5.50, reject), and Fast Noise-Robust (4.75, reject).

**Round 1 bracket**: 4.0–6.5 (the paper is clearly stronger than the 2.3–3.0 weak anchors and weaker than the 8.0 strong anchors).  
**Round 2 narrowing**: Comparing against:
- *Variational Perspective (5.50, accept)* — this paper has comparable quality: both have novel methods and decent experiments, both have theory gaps. The current paper has more extensive experiments but weaker convergence guarantees relative to its framing. Similar score.
- *Prior Mismatch PnP-ADMM (6.25, reject)* — a stronger theoretical contribution (nonconvex analysis, explicit error bounds) but rejected partly due to limited experiments and unclear practical implications. The current paper has weaker theory but stronger experiments. Marginally lower score.
- *DiracDiffusion (5.50, reject)* — a diffusion-based method requiring per-task retraining with comparable experimental scope. The current paper's zero-shot approach and broader task coverage give it a slight edge.
- *Fast Noise-Robust (4.75, reject)* — had serious technical errors (incorrect use of Tweedie's formula, unfair comparisons). The current paper does not have such technical errors.

The paper sits between 5.0 and 6.0. The core contributions (novel AC-DC denoiser, first convergence analysis for score-based ADMM-PnP, strong empirical results) are solid, but the weaknesses — particularly the theory-practice gap from the stationary distribution assumption, missing error bars, and no computational cost comparison — prevent a higher score. A score of 5.5 reflects a paper with genuine contributions that also has clear, addressable weaknesses.

**List of anchors retrieved across all rounds:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| IsHWcsk4Fz (FedADM) | 3.00 | R1 | Much weaker; unrelated federated learning paper |
| xpmDc76RN2 (Operator Networks) | 2.33 | R1 | Much weaker; different subfield |
| Og7ZZd7hDm (Fed Composition) | 3.25 | R1 | Much weaker; different subfield |
| 1NYhrZynvC (Gradient Descent) | 2.50 | R1 | Much weaker; pure optimization |
| 1YO4EE3SPB (Variational Perspective) | 5.50 | R1/R2 | Comparable; similar level of contribution and weaknesses |
| Z9Odi09Rv9 (Fast Noise-Robust) | 4.75 | R1/R2 | Weaker; had technical errors this paper does not |
| bEDTZxwJjT (DiracDiffusion) | 5.50 | R1/R2 | Comparable; this paper slightly stronger (zero-shot vs retraining) |
| nHESwXvxWK (Monte Carlo guided) | 4.00 | R1/R2 | Weaker; polarizing reviews, limited experiments |
| 6EUtjXAvmj (Variational DPS) | 8.00 | R1 | Stronger; established research group, cleaner method |
| 6O3Q6AFUTu (NoiseDiffusion) | 8.00 | R1 | Stronger; more polished |
| fV0t65OBUu (Optimal Covariance) | 8.00 | R1 | Stronger; different subfield (diffusion training) |
| I5lcjmFmlc (Robust Classification) | 8.00 | R1 | Stronger; different subfield |
| HXjXPQU3yJ (Prior Mismatch PnP-ADMM) | 6.25 | R2 | Stronger theory but weaker experiments; rejected |
| x7d1qXEn1e (Restoration Network) | 6.25 | R2 | Stronger; cleaner method-theory connection |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>