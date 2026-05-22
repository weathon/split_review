Now I have a clear picture. Let me write the final consolidated review.

## Summary

ESS-Flow is a novel training-free method for controlled generation with flow-based models. The key insight is to perform Bayesian inference in the Gaussian source space using elliptical slice sampling (ESS), which avoids Jacobian and gradient computations entirely. The method only requires forward passes through the generative model and the potential function. Experiments on materials design (FlowMM) show large improvements over gradient-based baselines (D-Flow, PnP-Flow, DAPS) across four target properties, and a space-group task demonstrates feasibility on non-differentiable potentials where competing methods cannot be applied at all. A protein backbone prediction experiment using Chroma is also presented.

## Strengths

- **Novel and principled gradient-free approach**: ESS-Flow avoids the Jacobian computations that plague gradient-based source-space methods (D-Flow, HMC, Langevin) and handles non-differentiable potentials (space-group indicators, quantized atomic numbers) that break gradient-based approaches entirely. This is a genuinely new capability, not an incremental improvement.

- **Convergence guarantee**: Proposition 1 establishes geometric convergence of the ESS Markov chain to the target in total variation, adapting a result from Natarovskii et al. (2021). This rigor is absent from competing optimization-based methods like D-Flow and PnP-Flow, which offer no convergence guarantees to the posterior.

- **Strong empirical results on materials design**: Table 2 shows ESS-Flow achieving dramatically lower absolute errors (8.99 GPa bulk modulus, 10.53 GPa shear modulus, 1.85 eV band gap) versus the next best baseline DAPS (39.14 GPa, 84.33 GPa, 3.90 eV) — factors of 4–8× improvement. These are not marginal gains.

- **Clean demonstration on a non-differentiable problem**: The space-group task (Section 5.1) uses a binary indicator computed by an external program, where no gradient-based method can operate. ESS-Flow achieves 92.3% target space-group yield versus 2.5% for unconditional sampling. This directly validates the paper's core claim.

- **Honest limitation discussion**: The paper clearly states where ESS-Flow struggles (low-dimensional targets, sharp potentials for multi-fidelity) and does not overclaim on the multi-fidelity proof of concept.

## Weaknesses

### Major

None.

### Minor

- **Continuity assumption vs. discontinuous potentials**: ESS's finite-time termination guarantee (Murray et al., 2010) requires the pullback potential *g*∘*T*₀ to be continuous. The space-group binary indicator (Table 1: 1[*P_c* = *y*]) is discontinuous, yet the paper does not discuss whether the theoretical guarantee extends to this case or why ESS still works in practice (it does work, with 92.3% success). This gap between theory and practice should be addressed explicitly.

- **No comparison against gradient-based source-space MCMC**: The paper motivates gradient-free operation by noting that gradients are unavailable for certain problems (e.g., space group), which is valid. However, the review of related work positions ESS-Flow against gradient-based source-space methods (Purohit et al. 2025, Wang et al. 2025), and a comparison on a *differentiable* task would clarify whether the gradient-free advantage comes with a sample-efficiency cost or is purely beneficial. This is informative but not required for the core claim.

- **Protein experiment uses a modified Chroma prior**: Chroma is originally a diffusion model; the paper converts it to a deterministic ODE via the probability flow ODE and k-NN graph construction. This is standard practice (Song et al., 2021) and the paper acknowledges it. However, no validation is provided that unconditional samples from the modified model preserve Chroma's original quality. The reported unconditional ELBO (8.70) and clash count (10.1) in Table 4 are reasonable, but a direct comparison to the original Chroma would be reassuring.

- **Multi-fidelity proof of concept is weak**: The importance-weighting approach yields effective sample sizes of only 0.1% (band gap) and 1.0% (stability), which the paper honestly reports. This section would be better placed in an appendix, as it does not demonstrate a working approach and the paper's claims do not depend on it.

### Trivial

- The number of MCMC iterations and burn-in length are not reported for any experiment.
- Section 4.1 states that the Jacobian of *T*₀ is needed for Langevin/HMC in source space (since ∇_z g(T_θ(z)) = J_T_θ(z)^⊤ ∇_x g(x)), which is correct. This is worth keeping as context for readers.

## Nice-to-Haves

- A comparison against gradient-based source-space MCMC (HMC or Langevin) on a differentiable materials task would clarify whether ESS-Flow's exploration advantages come at a cost in mixing efficiency.
- Reporting ESS chain diagnostics (trace plots, effective sample sizes, acceptance rates) would strengthen the practical evaluation.
- The paper notes that Hyperparameter details are in the appendix (stripped by parser); these should be included in the main paper or a clearer repurposing of the appendix in the camera-ready.

## Removed Points

- **"Validity of protein experiment — Chroma modification is undocumented/substantial"**: Removed. Converting a diffusion model to a deterministic ODE via the probability flow ODE is standard practice established by Song et al. (2021) and widely used. The paper explicitly states this modification and generates samples with the probability flow ODE. The critic's claim that this is a "substantial architectural modification" that invalidates the prior is incorrect.

- **"Baseline hyperparameter tuning not documented"**: Removed. The paper states details are in the appendix. Since the parser strips the appendix, this criticism cannot be verified against the paper as presented.

- **"D-Flow is not a sampling method; comparison is unfair"**: Removed. D-Flow is included as a baseline in the same way the original D-Flow paper positions itself — as a method for controlled generation. The paper does not claim ESS-Flow "beats" D-Flow at sampling; it shows D-Flow fails on disconnected manifolds (Figure 2) and with quantization, which is an honest comparison illustrating ESS-Flow's advantages.

- **"Overclaiming on asymptotically exact"**: Demoted to minor. The paper's Proposition 1 states geometric convergence of the ESS chain to the target defined by the (discretized) transport map *T*₀, which is standard for MCMC. The discretization error of the ODE solver is a separate issue that affects all methods using flow-based models, not just ESS-Flow. The paper discusses discretization in Section 4.2.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors have not already made.

## Suggestions

- Discuss the continuity assumption for ESS termination in the context of the space-group binary indicator. Explain why ESS still works well in practice despite the potential being discontinuous.
- Add a validation column (e.g., unsupervised sample quality metrics) confirming that the modified Chroma prior (probability flow ODE + k-NN) produces samples of comparable quality to the original stochastic Chroma.
- Report MCMC diagnostics: number of iterations, burn-in, effective sample sizes, and acceptance rates for all experiments.
- Move the multi-fidelity evaluation (Section 5.1.1) to the appendix, as the results do not support a working approach and risk distracting from the paper's main contributions.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>