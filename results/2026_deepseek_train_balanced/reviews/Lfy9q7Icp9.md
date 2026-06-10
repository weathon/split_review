Now I have a thorough understanding of both the paper and the reviewer inputs. Let me write the consolidated review.

---

## Summary

This paper introduces DiSK, a method that applies a series of progressively simplified Kalman filter updates to denoise privatized gradients in DP optimization. Starting from a full Kalman filter formulation (Algorithm 1) where the gradient is the state and the privatized gradient is the noisy observation, the authors apply four aggressive simplifications (identity observation matrix, finite-difference Hessian approximation, diagonal covariance, constant gain) to arrive at Algorithm 3, which is an exponential moving average of a linear combination of gradients evaluated at two points. DiSK adds at most 2× computation and 1.5–2× memory over baselines. The paper provides convergence theory showing a constant-factor improvement over DPSGD without additional assumptions, and reports empirical gains on CIFAR-10/100, ImageNet-1k, and GLUE.

## Strengths

- **Clean theoretical result with minimal assumptions.** Theorem 1 and Corollary 1 (lines 264–292) prove a constant-factor convergence improvement (√(1/C_κ)) over vanilla DPSGD under only L-smoothness, bounded variance, and bounded gradient — the same assumptions as DPSGD itself. The paper correctly notes (line 300, line 311) that prior works with convergence improvements require additional structural assumptions (e.g., gradient correlation for DOPPLER, Hessian trace for correlated-noise methods), making this genuinely novel.

- **Systematic simplification with explicit resource accounting.** Section 3.2 walks through the four simplifications (constant C_t, Hessian estimation via finite differences, diagonal covariance, constant gain) with clear justification. Section 3.3 (line 232) concretely quantifies overhead: at most 2× the computation of DPSGD, at most 2× memory of DPSGD, and 1.5× memory of DPAdam. This distinguishes DiSK from prior Kalman-filter-for-optimization approaches requiring O(d³)–O(d⁶) cost (line 126).

- **Novel unification of NAG and STORM.** Section 3.3 (lines 234–237) demonstrates that DiSK reduces to Nesterov Accelerated Gradient (when clipping is inactive and privacy noise is zero) and to STORM (with γ=-1, κ=α, B=1). This is a genuinely insightful connection that bridges acceleration and variance-reduction through a filtering lens.

- **Strong empirical gains across diverse tasks.** The from-scratch training results are substantial: 63% → 75% on CIFAR-10, 21% → 42% on CIFAR-100, and 32.4% → 36.9% on ImageNet-1k under ε=8. GLUE fine-tuning shows consistent 1–5 point improvements. These gains are large enough to signal a real algorithmic benefit.

## Weaknesses

### Major

- **Missing experimental comparison against DOPPLER, the most directly related method.** Section 3.3 ("Connection to DOPPLER") explicitly discusses DOPPLER (Zhang et al., 2024), notes that DiSK degenerates to first-order DOPPLER when evaluated at a single point, and argues DiSK is superior because DOPPLER requires prior knowledge of the gradient frequency spectrum. Yet the experiments compare DiSK only against DPSGD, DPAdam, and DPAdamW — not against DOPPLER, and not against DP-FTLR (also discussed in related work). The paper's SOTA claims (line 329) compare against published numbers from Bao et al. (2024) and De et al. (2022), which are not DOPPLER results. Without direct head-to-head comparison against the method the paper itself identifies as most closely related, the reader cannot assess whether DiSK's specific two-point gradient combination with EMA provides any benefit over a simpler first-order DOPPLER filter. This is the single most important evidential gap.

- **The Kalman filter framing overstates what the algorithm actually is.** After all simplifications are applied (identity observation matrix, diagonal time-invariant covariance, constant gain), Algorithm 3 is an exponential moving average of a linear combination of gradients evaluated at two points, with two free parameters (κ, γ). The adaptive covariance tracking that defines a Kalman filter — where the gain adapts based on estimated state uncertainty — is entirely absent. The paper is transparent about each simplification step in Section 3.2, but the framing throughout (title, abstract, contributions, Sections 1 and 3) consistently describes the method as "Kalman filtering" rather than as "a method motivated by Kalman filtering that reduces to a fixed-parameter EMA." The connection to NAG and STORM (Section 3.3) is actually a more honest and illuminating description of what the algorithm accomplishes. This is a framing problem: the contribution is still useful, but the reader is led to expect something more sophisticated than what is delivered.

### Minor

- **No error bars or variance estimates for any experimental result.** All results are reported as single accuracy numbers (Tables 1, Figures 2–3). DP training is inherently stochastic (subsampling noise + DP noise + SGD noise). The claimed improvements on CIFAR-10 (63%→75%) and CIFAR-100 (21%→42%) are large enough that one must wonder about hyperparameter sensitivity or luck in a single run. Even for expensive ImageNet-scale experiments, reporting variance over 2–3 seeds would substantially increase credibility. This is standard practice in the DP optimization literature.

- **The theoretical improvement is constant-factor and problem-dependent, with no empirical calibration.** The convergence bound improvement is √(1/C_κ) where C_κ = min{||∇F(x₀)||²/(2L(F(x₀)−F*)), 1}. When C_κ = 1, the bound shows no improvement over DPSGD. The paper notes (line 295) that for non-convex deep learning, L can be large and C_κ potentially small, but it never estimates C_κ empirically for any of the experimental settings. The connection between the theory and the observed empirical gains is therefore purely qualitative.

- **Theory assumes the regime where clipping is inactive.** Assumption 3 (bounded gradient, line 257–259) combined with the condition C ≥ (1+2(1−κ)/κ)G (Theorem 1) effectively means clipping is never active. The paper acknowledges this (line 261: "Since the impact of clipping is not the major focus of this paper, we follow this tradition"), and this is standard in DP convergence theory, but it means the theory covers a different operating regime than practical DP training where tight clipping is essential for privacy.

### Trivial

- The ablation study for hyperparameters κ and γ is relegated to the appendix. Given that these are the method's only tunable parameters beyond standard optimizer hyperparameters, at least a brief summary of their sensitivity should appear in the main text.

## Nice-to-Haves

- A dedicated limitations section would be helpful. The paper currently has no explicit discussion of limitations such as (a) the 2× computation overhead, (b) the two added hyperparameters, (c) the constant-factor (not order-improvement) nature of the theory. (The computation overhead is disclosed at line 232, but not framed as a limitation.)

- The privacy analysis could be made more explicit. The paper correctly notes that the privacy guarantee follows from the subsampled Gaussian mechanism (Section 4.2, lines 303–304), but since the per-sample quantity is now a linear combination of gradients at two points, explicitly stating the sensitivity bound for this combined quantity would strengthen the presentation.

- Estimating C_κ empirically for the experimental settings would connect the theory to the results and help the reader understand when the improvement is expected to be large or small.

## Removed Points

These points were flagged in reviewer input but are removed per filtering rules:

- **"The final algorithm is not a Kalman filter" framing as a fatal issue:** Downgraded to Major (above). The paper is transparent about the simplification chain in Section 3.2 and explicitly labels the result a "Simplified Kalman Filter." The criticism that it is not a Kalman filter at all is too strong given the clear documentation; the issue is more about overclaimed framing than dishonesty.

- **"Sweeping dismissal of prior methods" (line 18):** Removed. This is a subjective interpretation of the paper's characterization of existing work, not a verifiable weakness.

- **"Theoretical analysis's bounded gradient assumption":** This is acknowledged by the authors (line 261) and is standard practice. Retained only as Minor (above) with the acknowledgment.

- **"No limitations section":** Moved to Nice-to-Haves. The computation cost is actually disclosed (line 232), so the paper is not hiding this.

## Novel Insights

The most genuinely novel observation to emerge from the review is the tension between the paper's two framings. The Kalman-filter framing, while motivationally useful, masks the fact that DiSK is structurally an EMA of a two-point gradient combination that bridges NAG (acceleration) and STORM (variance reduction). The connection to STORM with γ=-1 is particularly underexploited in the paper: at γ=-1, DiSK's gradient combination looks like ∇f(x_t) − ∇f(x_t − γ d_{t-1}) (with γ=1), which is essentially a gradient difference approximating Hessian information — a known variance-reduction trick. The paper's theoretical corollary also selects γ=-1 (Corollary 1), but the empirical results use various γ values (γ=0.5 for CIFAR-10 results), suggesting the practical advantages of different γ regimes are not well-explained by the theory. This disconnect between the theoretically optimal γ=-1 and the empirically used γ values represents an underexplored gap.

## Suggestions

1. **Primarily: add DOPPLER as an experimental baseline.** Both on the vision benchmarks (CIFAR-10/100, ImageNet-1k) and the GLUE tasks. This is the single most important addition needed to support the claim that DiSK's specific mechanism (two-point gradient combination + EMA) outperforms a simpler first-order filter. If DOPPLER matches DiSK's performance, the paper's contribution reduces to the theoretical result and the NAG/STORM unification; if DiSK clearly outperforms, the empirical section becomes much stronger.

2. Report results with error bars (mean ± std over at least 3 seeds) for at least the smaller-scale experiments (CIFAR-10/100, GLUE).

3. Tone down the Kalman filter framing in the title/abstract, or add a clear sentence early on acknowledging that the final algorithm is a fixed-parameter filter that draws motivation from Kalman filtering but is not an adaptive Kalman filter.

4. Include at least a brief summary of κ, γ sensitivity in the main text (e.g., a small figure or a sentence describing the range of effective values).

5. Estimate C_κ for the CIFAR-10/100 setups to give a concrete sense of when the theory predicts improvement.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>