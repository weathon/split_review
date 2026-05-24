## Summary

This paper introduces SCaSML, a framework that improves pre-trained SciML surrogate models (PINNs, Gaussian Processes) for solving high-dimensional semi-linear parabolic PDEs at inference time, without retraining. The core idea is the "Structural-preserving Law of Defect" — deriving a new semi-linear PDE that exactly characterizes the error of the surrogate, which is then solved via Multilevel Picard (MLP) stochastic simulation. The authors prove that the final error is bounded by the *product* of surrogate and simulation errors (Theorem 2.5), yielding an improved convergence rate from \(O(m^{-\gamma})\) to \(O(m^{-\gamma-1/2})\). Experiments across 4 PDE families (linear convection-diffusion, viscous Burgers, HJB, diffusion-reaction) up to 160 dimensions demonstrate consistent 20–66% error reduction across both PINN and GP surrogates, with empirical validation of the accelerated scaling law.

## Strengths

- **Novel theoretical contribution — the Structural-preserving Law of Defect**: The derivation in Fact 2.3 that the error \(\tilde{u} = u - \hat{u}\) satisfies a semi-linear PDE preserving the structure of the original problem is genuinely original. This is not a straightforward application of classical defect correction, since neural network surrogates lack the asymptotic error expansions that classical methods rely on (Section 2.2 clearly contrasts this). The structural preservation is the key enabler for efficient Monte Carlo solution.

- **Provably accelerated convergence with product error bound**: Theorem 2.5 proves that the final error is the product of surrogate error and simulation error — a synergistic relationship where better surrogates directly reduce the inference cost. Corollary 2.6 formalizes the improved scaling law. The proof sketch (Section 2.4) provides clear intuition for why the convergence rate improves, and Figure 4 empirically validates the steeper log-log slope across dimensions 20–80 on the viscous Burgers equation.

- **Broad empirical validation**: Table 1 demonstrates consistent error reduction across 4 PDE families, dimensions from 10 to 160, and two fundamentally different surrogate types (PINNs and Gaussian Processes). The failure of naive MLP on the LQG problem (relative \(L^2\) error > 5) alongside SCaSML's success (error ~0.05–0.10) provides strong evidence that the hybrid approach succeeds where pure simulation fails. Figure 3a shows tightened pointwise error distributions, Figure 3b demonstrates effective inference-time scaling, and Appendix G.4 reports statistical significance at \(p \ll 0.001\).

- **Practical elastic compute paradigm**: The paper demonstrates that a smaller PINN with inference-time correction can outperform a larger PINN under equal total compute (Appendix G.7). This directly supports the "elastic compute" framing — users can trade inference time for accuracy on demand without retraining.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The "20–80%" error reduction range slightly overstates main-table results.** The largest reduction visible in Table 1 is VB-PINN at 20d (~66% relative \(L^2\) improvement). The 80% upper bound presumably comes from appendix results. This does not undermine the contribution, but abstract-level claims should be precisely anchored to reported data.

- **No direct empirical validation of the product error bound (Theorem 2.5).** The scaling-law experiment (Figure 4) validates the steeper slope, but does not explicitly show that the final error scales as the *product* of surrogate error and simulation error (e.g., by varying surrogate training budget and measuring both components). This would strengthen the theoretical-to-empirical link.

### Trivial

- The scaling-law plot (Figure 4) omits the surrogate-only and pure-MLP baselines on the same total-cost axis, which would make the efficiency gain visually sharper.
- No sensitivity analysis for the clipping threshold, which varies across problems (0.01 to 10). A brief check that results are robust to this hyperparameter would increase confidence.

## Nice-to-Haves

- A small ablation on the number of MLP levels and the basis sample size \(M\) would help characterize the cost-accuracy tradeoff of the inference step.
- Extending the comparison to a simple control-variate baseline (using the surrogate directly in the Feynman-Kac estimator without solving a separate defect PDE) would further isolate the value of the defect-PDE formulation — though the paper already frames the method as a control variate in the conclusion.

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **"Broader baseline (control variate approach)":** The harsh critic suggested adding a control-variate baseline. Removed because: (1) the paper explicitly frames SCaSML as a control variate in the conclusion (line 349); (2) the critic themselves noted this is "not required for a method paper"; (3) the defect PDE solves a fundamentally different problem than simple CV — it corrects the solution values, not just the estimator variance.

- **"Missing implementation details in main text":** The harsh critic noted MLP variant details are in the appendix. The paper does specify: 2-level simulation, \(M=10\), clipping thresholds per problem, and references the appendix for MLP preliminaries. The main text provides sufficient detail for understanding; additional details are appropriately in the appendix (which was stripped by the parser but exists in the original submission).

- **"Slope comparison for scaling law":** Moved from "Strengthening" to Trivial — this is a presentation improvement, not a weakness.

- **Formatting/style nitpicks:** None were raised by the harsh critic.

## Novel Insights

The paper makes a genuinely insightful connection: neural network surrogates exhibit *spectral bias* (learning low frequencies first), which means their residual error is predominantly high-frequency and irregular — precisely the regime where Monte Carlo methods thrive, since their convergence rate is independent of integrand smoothness. This explains *why* the surrogate + MC combination is particularly effective beyond just variance reduction, and why naive MLP alone fails on challenging problems (LQG). This insight about complementary error profiles (surrogate captures low-frequency structure, MC averages out high-frequency residual) is, to my knowledge, novel and practically important.

## Suggestions

- Consider adding a two-panel figure or table in the appendix that directly varies surrogate training budget and reports both surrogate error and final SCaSML error, validating the multiplicative relationship in Theorem 2.5.
- Add error bars or confidence intervals to the main table, since the paper already reports statistical significance tests in the appendix.
- Briefly discuss the sensitivity of results to the clipping threshold, perhaps as a footnote or appendix note.

**Originality:** High. The Structural-preserving Law of Defect is a novel derivation, and combining it with MLP for inference-time correction of neural surrogates is a fresh contribution to the SciML literature.

**Importance of research question:** High. Making neural PDE solvers trustworthy through principled error correction is a central challenge for deploying SciML in safety-critical applications.

**Claims well supported:** Yes. The theoretical bound (Theorem 2.5) is derived and empirically corroborated (Figure 4, Table 1). The experiments cover diverse PDEs and surrogate types.

**Soundness of experiments:** Good. Four PDE families, two surrogate types, dimensions up to 160, statistical significance tests, and inference-time scaling analysis. Minor gaps: no clipping sensitivity analysis, no direct product-bound verification.

**Clarity of writing:** Good. The paper is well-structured, the derivation is step-by-step, and the intuition sections (spectral bias, why Monte Carlo, training/inference separation) are effective. Some implementational details could be surfaced from the appendix into the main text.

**Value to the research community:** High. The framework is plug-and-play (works with any pre-trained surrogate), requires no retraining, and establishes a new paradigm for elastic compute in scientific ML. The defect-PDE approach may inspire similar correction schemes for other SciML methods.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| R5FzCFR5yU (Hybrid Numerical PINNs) | 3.33 | R1 | Far weaker: limited to 1D/2D, no theory, flawed methodology |
| wUaOVNv94O (Auto Neural Spatial Integration) | 4.00 | R2 | Similar spirit (NN as control variate for MC) but limited to 2D/3D Poisson/Laplace, no theory, poor experiments |
| 3ep9ZYMZS3 (HyPER) | 5.00 | R2 | RL-based correction for rollout, weaker theory, only 2D NS |
| Q9OGPWt0Rp (Real-time PINNs) | 5.25 | R1 | Different problem (parameterized PDEs), mixed reviews |
| wVADj7yKee (SINGER) | 6.33 | R2 | GNN evolution operator, theory + experiments, but narrower PDE class (up to 20d only) |
| 2DbVeuoa6a (Neural Spectral Methods) | 6.75 | R2 | Novel spectral loss, strong results but split reviews and narrower scope |
| x4ZmQaumRg (Active Learning for PDEs) | 7.00 | R2 | Solid benchmark paper, less theoretical novelty than SCaSML |
| D042vFwJAM (Physics-aligned field reconstruction) | 7.33 | R2 | Diffusion bridge for physics, strong but different problem |
| fU8H4lzkIm (PhyMPGN) | 8.00 | R1 | Exceptionally strong: thorough experiments, multiple benchmarks. SCaSML has stronger theory but narrower experimental breadth. |

**Round 1 bracket:** 4.0–8.0 based on topic-adjacent anchors.

**Round 2 narrowing:** The paper is clearly stronger than the 4.0–5.25 anchors and comparable to or stronger than the 6.33–7.00 anchors. It has more theoretical depth than SINGER (6.33) and more novelty than the AL benchmark (7.00). It is somewhat below PhyMPGN (8.00) in experimental breadth but comparable in contribution quality.

**Final score rationale:** The paper delivers a genuinely novel theoretical contribution (Structural-preserving Law of Defect), rigorous convergence analysis, and broad empirical validation across diverse high-dimensional PDEs. The weaknesses are minor and do not threaten the core claims. Positioned between the 7.00 Active Learning benchmark (less novel) and the 8.00 PhyMPGN (more exhaustive experiments), SCaSML lands at 7.0 — a strong accept with clear value to the community.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>