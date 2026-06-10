## Summary

This paper proposes a general framework for learning diffusion bridges with degenerate noise (where noise acts only in a subset of dimensions), enabling underdamped Langevin dynamics as a special case. The framework extends the Radon-Nikodym derivative (Proposition 2.3), derives an ELBO (Lemma 2.4), and proves equivalence between score-matching and likelihood maximization in the underdamped setting (Proposition 2.5). On the practical side, it introduces novel underdamped versions of DIS and DBS, employs splitting integrators (OBAB, BAOAB, OBABO), and uses end-to-end hyperparameter learning. Experiments across 9 benchmarks (up to d=1600) show strong empirical gains.

## Strengths

- **Proposition 2.3 extends the Radon-Nikodym derivative to degenerate noise (lines 95–99).** The paper derives a likelihood ratio between forward and reverse-time path measures for noise coefficients of the form η = (0, σ)ᵀ, using the pseudoinverse η⁺. This generalizes prior results (Vargas et al., 2024; Richter & Berner, 2024) that assumed non-degenerate noise.

- **Lemma 2.4 and Proposition 2.5 rigorously connect ELBO and score-matching for underdamped dynamics (lines 127–151).** Lemma 2.4 provides an ELBO for the log-likelihood in the degenerate-noise setting, and Proposition 2.5 proves that maximizing this ELBO (with v=0) is equivalent to minimizing a score-matching objective. This formalizes a connection previously suggested but not rigorously shown for the degenerate/underdamped case.

- **Remark 3.3 identifies a practical numerical advantage (lines 226–232):** The optimal controls u* and v* at terminal time T do not depend on ∇_x log p_target (the target score), only on the analytically known Gaussian velocity score. This is genuinely useful when the target is supported on a low-dimensional manifold where scores can be large.

- **Figure 4 provides systematic evidence that splitting integrators are crucial for underdamped controlled diffusions.** The paper compares Euler-Maruyama, OBAB, BAOAB, and OBABO across benchmarks, showing that splitting integrators offer substantial ESS improvements over EM at the same per-step cost (OBABO yields best results but at higher cost).

- **Figures 5 and 9 show that end-to-end hyperparameter learning works reliably.** Learning the mass matrix M, diffusion coefficient σ, terminal time T, and prior π yields substantial gains over fixed defaults for both N=64 and N=8 discretization steps, eliminating a practical tuning bottleneck.

- **Table 1 demonstrates strong empirical performance across diverse benchmarks.** Underdamped DBS achieves best results (across metrics Δ log 𝒵, ESS, Sinkhorn distance, log 𝒵 lower bound) on all 9 problems, including the high-dimensional LGCP (d=1600), often with far fewer discretization steps than competing methods.

## Weaknesses

### Major

- **Insufficient statistical characterization of main results.** All experimental results (Table 1, Figures 3–5) are reported as averages across four runs/seeds without any standard deviations, confidence intervals, or other measures of variability. With only 4 seeds, the claimed "state-of-the-art" results could be driven by a single advantageous seed. The paper makes strong comparative claims ("consistently outperforming other methods," "state-of-the-art performance"), but the reader cannot assess whether the reported differences are meaningful or within the noise of the evaluation. This gap is particularly problematic because the paper compares many methods across many benchmarks; without variance estimates, it is impossible to evaluate ranking stability.

### Minor

- **The comparison design may not fully disentangle the sources of improvement.** The paper's central claim is that underdamped dynamics bring benefits, but the proposed method differs from baselines along multiple axes simultaneously: the dynamics themselves (underdamped vs. overdamped), the splitting integrators (OBAB/BAOAB/OBABO vs. Euler-Maruyama), joint learning of both u and v, and end-to-end hyperparameter learning. While Figure 4 ablates the integrator choice and Figure 5 ablates the hyperparameter learning, the paper never isolates the effect of underdamped vs. overdamped *dynamics* holding all other factors (integrator, learning setup) fixed. The existing ablations are all within the underdamped DBS. A cleaner decomposition would strengthen the paper's attribution of gains to underdamped dynamics per se.

- **The paper acknowledges a tension between its convergence-rate motivation and the theoretical reality, but does not fully resolve it (lines 275–276).** The introduction motivates underdamped dynamics via improved convergence rates (from Õ(d/ε²) to Õ(√d/ε) for log-concave targets). The conclusion honestly notes that Chen et al. (2022) showed these improved rates do not carry over to the *learned* setting because the control u depends on Y as well as X. The three reconciliation bullet points are speculative ("we believe") and not supported by analysis in the paper. This does not invalidate the paper's empirical contributions, but the framing over-promises on the theoretical justification.

- **The baselines do not include existing underdamped variants of competing methods.** The paper acknowledges (line 59) that ULA→UHA, MCD→LDVI, and underdamped versions of CMCD and DDS exist in the literature. However, Table 1 compares primarily against the overdamped versions (ULA, MCD, CMCD). If the goal is to demonstrate that the *underdamped framework itself* is beneficial, comparing UD-DBS against UHA, LDVI, or underdamped CMCD would provide a fairer assessment. The paper mentions that "each of the previously existing methods brings some respective additional details" but does not explain why these variants were excluded or whether adapting them to the paper's framework changes the comparison.

### Trivial

- None.

## Nice-to-Haves

- **Verify the discrete-time ELBO claim empirically.** Remark 3.2 states that the paper's approach yields a guaranteed lower bound on log Z in discrete time, unlike previous divergence-based approaches. This is a strong claim and would benefit from at least a simple empirical verification on a problem where the exact log Z is known.

- **Include a computational cost comparison across methods.** The paper reports wallclock time for different integrators (Fig. 4) but does not compare total training cost between UD-DBS and competing methods. If UD-DBS requires more function evaluations per step, this matters for practitioners.

## Removed Points

These points were identified by the reviewers but are removed after verification against the paper:

- *"Equation (10) appears garbled"* — The rendering has minor parser artifacts but the equation content is clear and correct; this is a PDF extraction issue, not a paper flaw.
- *"Experimental setup details missing (architecture, optimizer, budget)"* — These details are deferred to the appendix (standard practice); the hard rules forbid penalizing content stripped by the parser.
- *"Missing limitations section"* — The conclusion discusses limitations and open questions (lines 275–276). No dedicated limitations section is required.
- *"Computational cost not compared"* — This is moved to Nice-to-Haves; the paper does provide wallclock time for integrator variants.
- *"The convergence theory tension is a structural/fatal issue"* — The paper openly acknowledges this tension in the conclusion. It is an honest limitation, not a fatal flaw. Retained as a minor weakness above.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the tension between convergence-rate motivation and learned-setting reality is correctly identified, but the paper already acknowledges this. The strength finder's catalog of contributions is accurate but does not reveal anything not stated in the paper itself.

## Suggestions

1. **Report standard deviations (or at least min/max ranges) for all main results (Table 1, Figures 3–5).** With only 4 seeds, this is essential for the reader to assess the reliability of the claimed improvements. Bootstrapped confidence intervals or pairwise significance tests would also be valuable.

2. **Disentangle the sources of improvement more cleanly.** At minimum, add a comparison: underdamped dynamics with Euler-Maruyama vs. overdamped dynamics with OBABO, to isolate whether the gains come from the dynamics or the integrator. This would directly address the paper's central question.

3. **Include underdamped variants of competing methods (UHA, LDVI, underdamped CMCD) as baselines.** If the goal is to show that the underdamped *framework* — not just UD-DBS specifically — is beneficial, comparing against existing underdamped methods would make the case stronger.

4. **Tone down the convergence-rate framing in the introduction** or expand the conclusion's reconciliation with supporting evidence. The current framing suggests the rates motivate the work, but the paper later acknowledges they do not apply in the learned setting. A more measured framing would avoid this tension.

5. **Empirically verify the Remark 3.2 claim** about the discrete-time Radon-Nikodym derivative yielding a guaranteed lower bound on log Z, at least on a toy problem.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>