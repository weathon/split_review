Now I have a thorough understanding of the paper. Let me carefully verify each of the harsh critic's claims against the paper text before writing the consolidated review.

Key verifications:

**Theorem 1 notation**: Line 56 shows `\phi_{\mathbf{z}_j^{(\ell)}\mid \Sigma^{(\ell)}}(\mathbf{t})` — the notation explicitly conditions on Σ^(ℓ), contrary to the critic's claim of ambiguity.

**Algorithm sub-procedures**: Lines 91-95 reference `Algorithm~\ref{alg:s_given_s}` and `Algorithm~\ref{alg:s_given_y}` — these would be in the appendix (parser-stripped).

**Timing results**: Line 138 mentions "Supplementary Section~\ref{supp:timing_results}" — in the stripped appendix.

**Feature learning**: Proposition 2 (lines 106-113) contrasts α<2 vs α=2. For α=2 the kernel is deterministic and features do NOT depend on data — the critic's claim that "this is true for any non-degenerate prior" misses this contrast.

**DIWP training**: Line 128 "we train all the models using the same hyperparameters they use, with 8000 total steps" — the critic notes DIWP uses VI, not MCMC. This is a valid concern about comparability.

**α sensitivity**: Line 128 "α=1,δ=1" — fixed throughout, no variation explored.

Now I'll write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision## Summary

This paper develops a deep α-stable kernel process (Dα-KP) that arises as the infinite-width limit of a deep Bayesian neural network with elliptical infinite-variance priors on the weights. The authors show that the limiting process admits a conditionally Gaussian representation — Gaussian conditioned on positive α/2-stable scale variables — which enables a recursive formula (extending Cho & Saul 2009) for the stochastic covariance kernel across layers, avoiding the exponential-in-dimension complexity of prior work by Loria & Bhadra. Posterior inference is performed via MCMC, and experiments on discontinuous functions and UCI datasets demonstrate competitive predictive accuracy and superior uncertainty quantification compared to deep GP baselines and standard GPs.

## Strengths

1. **Novel theoretical framework bridging infinite-variance BNN limits to tractable deep kernel processes.** Theorem 1 establishes that under elliptical infinite-variance priors, the infinite-width limit yields an elliptical α-stable process with a conditionally-Gaussian representation. This is a genuine extension of the Neal/Cho–Saul line of work into the infinite-variance regime, and the recursive kernel formula (extending Cho & Saul 2009 to the conditional Gaussian structure) enables multi-layer architectures in the kernel space — a significant advance over Loria & Bhadra's shallow, feature-space approach with exponential complexity.

2. **Empirical advantages on discontinuous functions and real data.** On 1D/2D/10D jump functions (Table 1), Dα-KP substantially outperforms GP-based methods (DIWP, NNGP, GP Bayes, GP MLE) and is competitive with the Stable method (which becomes intractable above 2D). On UCI Energy and Yacht datasets (Table 2), Dα-KP achieves the best RMSE and MAE. Figures 2–3 further show that only the α-stable methods provide posterior intervals that correctly capture jump discontinuities, validating the practical motivation.

3. **Theoretical and numerical demonstration of stochastic kernels enabling feature learning.** Proposition 2 formally shows that the posterior of the features depends on the data for α<2 but not for α=2 (the Gaussian limit), providing a clean demarcation from deterministic-kernel deep GPs. Figure 4 (Boston data) confirms non-Gaussian feature posteriors via heavy-tailed marginals and q–q plots, corroborating the stochasticity of the kernel.

4. **Characterization of long-range dependence.** Figure 1 shows that conditional mutual information decays more slowly for smaller α, demonstrating that the deep α-stable process can capture distant relationships that GPs would treat as nearly independent — a property directly tied to the theoretical framework.

## Weaknesses

### Fatal
None.

### Major

1. **No sensitivity analysis for α, the defining parameter of the approach.** All experiments fix α=1 (and δ=1) without exploring other values. Since the entire contribution hinges on the difference between α<2 (heavy-tailed, stochastic kernel) and α=2 (Gaussian, deterministic kernel), the paper needs to show whether performance degrades gracefully as α approaches 2, or whether α=1 is a special sweet spot. Even one additional value (e.g., α=1.5 or 1.8) on a synthetic and one UCI dataset would materially strengthen the claims. The mutual information plot (Figure 1) is illustrative but does not substitute for predictive performance under varying α.

2. **No MCMC convergence diagnostics.** The paper reports results from 3000 MCMC iterations with 1000 burn‑in but provides no trace plots, effective sample sizes, or any assessment of mixing. For a methods paper proposing a new MCMC algorithm with non-standard scale variables whose posterior is coupled through the recursive kernel formula, the absence of diagnostics is a significant gap that prevents readers from assessing the reliability of the reported results.

### Minor

1. **The "feature learning" evidence is primarily qualitative.** The paper shows that features are heavy-tailed (Figure 4) and that their posterior depends on the data (Proposition 2), but does not quantitatively isolate whether the stochastic kernel posterior is *beneficial* for prediction. A natural control experiment would compare Dα-KP against a "plug-in" version where scales are fixed at their posterior means. If the stochastic kernel matters, the full posterior should outperform the plug-in on uncertainty quantification or data efficiency. The paper's predictive results are good overall, but they don't directly attribute the improvement to kernel stochasticity.

2. **No discussion of limitations or failure cases.** The paper mentions future directions (variational inference, inducing points) but does not discuss scenarios where Dα-KP might underperform — e.g., smooth functions where a GP is optimal, or very small sample sizes where the scale posterior may be highly uncertain. Acknowledging such cases would strengthen credibility.

3. **The DIWP baseline comparison is not fully apples-to-apples.** The paper states it trains DIWP "using the same hyperparameters they use, with 8000 total steps." DIWP uses variational inference (gradient-based optimization), while Dα‑KP uses MCMC. "Steps" means different things for the two methods, and the possibility that DIWP may not have converged in 8000 VI steps, or that Dα‑KP benefits from more thorough posterior exploration, is not discussed.

4. **The scalability of the proposed method for large n is not discussed.** The paper criticizes Loria & Bhadra's O(n^{I+2}) complexity but its own method involves O(n³) matrix inversions within MCMC iterations. For UCI datasets with n up to 769 and 3000 MCMC iterations this is plausible but not trivial, and the practical limits are not addressed.

### Trivial
None. (Formatting issues are parser artifacts, not author errors.)

## Nice-to-Haves

- A table or figure showing predictive performance across a range of α values (e.g., 1.0, 1.5, 1.8, 2.0) on at least one synthetic and one UCI dataset.
- MCMC convergence diagnostics (trace plots, effective sample sizes) for the scale variables.
- Wall-clock runtime comparisons alongside Tables 1–2 to substantiate the claimed computational advantage over the Stable method.
- A "plug-in" ablation experiment comparing full posterior vs. fixed posterior-mean scales to directly test whether the stochastic kernel improves predictions.

## Removed Points

These points from the Harsh Critic were flagged for removal; they are retained here for transparency but do not factor into the evaluation:

- **Theorem 1 "ambiguity" about conditioning.** The critic claimed the paper does not resolve whether the characteristic function is conditional or marginal. The paper's notation (line 56) reads `\phi_{\mathbf{z}_j^{(\ell)}\mid \Sigma^{(\ell)}}(\mathbf{t})`, which explicitly conditions on Σ^(ℓ). The presentation is clear on this point. **Removed (factually wrong).**

- **Missing MCMC sub‑procedures (Algorithm s_given_s, s_given_y).** These are referenced via `\ref{alg:s_given_s}` and `\ref{alg:s_given_y}`, which would be in the (parser‑stripped) appendix. **Removed (parser artifact).**

- **Missing timing comparisons.** The paper states timing results are in the supplementary (line 138: "highlight in Supplementary Section~\ref{supp:timing_results}"). **Removed (parser artifact).**

- **Recursive formula derivation "not justified."** The derivation is a direct application of the Cho & Saul (2009) result to the conditional Gaussian process at each layer; a sketch/proof would be in the appendix. The connection is conceptually clear from the theorem statement. **Removed (parser artifact; connection is direct).**

- **"Feature learning" criticism conflates α<2 with any non-degenerate prior.** The critic's claim that "this is true for any non-degenerate prior" is wrong in context — the proposition explicitly contrasts α<2 (stochastic kernel, features depend on data) with α=2 (deterministic kernel, features do not depend on data), a distinction specific to the paper's construction. **Removed (factually wrong).**

## Novel Insights

The Harsh Critic identifies a genuinely subtle point: the paper's joint limit construction (widths → ∞ while scales are fixed, then integrating over scales) is described but the precise ordering of limits is not formalized in the main text. This is a fair observation that goes beyond what is standard for this style of paper — most infinite-width limit papers in the Neal/Cho–Saul tradition do not formalize the limit ordering to this level of detail either — but it correctly identifies a place where an interested reader might want more rigor. However, this does not threaten the paper's core claims, as the conditionally Gaussian representation and the recursive kernel formula are well-defined at the level of the final hierarchical model regardless of the precise limit order.

## Suggestions

1. Add a sensitivity analysis for α across a range of values on at least one synthetic and one UCI dataset. This is the single most impactful addition the authors could make.

2. Include MCMC diagnostics (at minimum, trace plots for the log-posterior and a subset of scale variables, plus effective sample sizes) to support the reliability of the posterior inferences.

3. Add a brief ablation experiment comparing Dα-KP against a version with scales fixed at posterior means to directly demonstrate the benefit of the stochastic kernel.

4. Include a short discussion of limitations: where the method may struggle (smooth data, very small n, very large n), and how the computational cost (O(n³) per MCMC iteration) compares to alternatives.

5. Clarify the DIWP comparison by noting that DIWP uses variational inference while Dα-KP uses MCMC, and discuss how this difference may affect the comparison.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>