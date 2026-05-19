- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 3
Now I have a thorough understanding of the paper and both reviews. Let me produce the consolidated review.

## Summary

This paper addresses safe boundary control of PDEs with unknown dynamics. The authors propose a framework that combines (1) a neural boundary control barrier function (BCBF) enforcing finite-time convergence of the boundary output, and (2) a neural operator that learns the input-output boundary mapping, which together enable a linear condition on the control derivative solvable via quadratic programming. Experiments on hyperbolic, parabolic, and Navier-Stokes PDEs demonstrate improved constraint satisfaction over vanilla RL controllers.

## Strengths

1. **Novel combination of neural operators and CBFs for PDE boundary safety** — Theorem 3.2 and Equation (11) derive that the derivative of the boundary output can be expressed as \( \dot{Y}(t) = \Lambda_\theta(t) \dot{U}(t) + \mu_\theta(t) \), making the BCBF constraint affine in \( \dot{U} \). This enables QP-based safety filtering for PDE boundary control — a non-trivial extension from ODE-based CBF-QP, since the Markov property does not hold in PDE dynamics. The theoretical derivation connecting neural operator derivatives to a QP-solvable form is a genuine technical contribution.

2. **Introduction of boundary feasibility as an appropriate safety notion for PDEs** — Definition 2.1 tailors the safety concept to PDE boundary control by requiring the output to enter and stay within the safe set by the end of a finite horizon, rather than demanding forward invariance at every time step. Section 5 motivates this by noting that oscillatory PDE trajectories can violate forward invariance during transients while still converging appropriately. This adaptation is well-justified for the PDE setting.

3. **Consistent empirical improvements across diverse PDE environments** — Tables 1–3 show that safety filtering with BCBF improves feasible rate and average feasible steps over vanilla PPO and SAC across hyperbolic (transport), parabolic (reaction-diffusion), and 2D Navier-Stokes PDEs. For example, PPO with time-dependent BCBF achieves 49% feasible rate vs. 0% vanilla PPO (Table 1), and raises feasible rate from 0% to 21% in the Navier-Stokes task (Table 3). These results support the framework's practical value.

4. **Useful ablation studies** — The ablation on filtering threshold \( \eta \) (Figure 2) systematically characterizes the trade-off between reward and constraint satisfaction, and the comparison between asymptotic and finite-time feasibility (Table 4) validates that the finite-time convergence term in Theorem 3.1 improves actual performance, not just theory.

## Weaknesses

### Fatal
None.

### Major

1. **Conditional guarantee vs. practical heuristic — model mismatch gap** — Theorem 3.2 assumes "the neural operator \( \mathcal{G}_\theta \) as an exact map... without model mismatch." The paper acknowledges this does not hold and introduces a filtering threshold \( \eta \) (Equation 14) as a workaround: when the QP-suggested control deviates too much from the nominal control, the filter is disabled. As the paper states, this is "a workaround" (line 142). The title ("Guaranteed Neural PDE Boundary Control") and abstract claim ("guarantee the boundary output stays within the safe set") overstate what the method actually delivers. While conditional guarantees are common in learning-based safety, the gap between the theoretical claim (exact model) and practical mechanism (heuristic threshold with no formal safety link) is significant. The problem is explicitly flagged as future work, but it is a structural limitation that should be acknowledged more honestly in the paper's presentation of results.

2. **Derivative computation for neural operators is not addressed** — Equation (9) requires \( \partial\kappa^{(l)}(t,s)/\partial t \) and \( db_l(t)/dt \), the continuous-time derivatives of the integral kernel and bias function. The paper uses FNO as the default neural operator, but FNOs parameterize kernels in Fourier space — the continuous derivative \( \partial\kappa/\partial t \) is not naturally available from the trained operator. The paper does not explain how these quantities are computed in practice (e.g., via autograd on the discretized operator, or through an alternative parameterization). This creates a gap between the continuous-time theoretical derivation and the discrete-time implementation. The authors should describe how the derivatives in Equation (11) are obtained from the practical neural operator implementation and address any approximation errors introduced.

### Minor

3. **Limited baselines** — The only baselines are vanilla PPO and SAC without any safety mechanism. While the paper claims to be the first to study safe boundary control with unknown PDEs, a simple baseline (e.g., clipping the control to an empirically safe range, or a proportional controller that drives the output toward the safe set) would provide a meaningful lower bound and help justify the complexity of the BCBF+neural operator machinery. The improvement over an unsafe controller is expected; a comparison showing the method outperforms a trivial safety scheme would substantially strengthen the evaluation.

4. **Evaluation procedure is ambiguous regarding the PDE environment vs. neural operator** — The paper states "as the computation of QP is not yet real-time, it is not yet ready to interact with the real PDE dynamics. we adopt the predicted Y(t) from the neural operator after each filtering step instead of real PDE dynamics" (line 142). It is unclear whether the 100-episode evaluations (Tables 1–3) are run on the PDE simulator or purely on the neural operator's predictions. If the latter, the results would only measure predicted safety, not actual constraint satisfaction. The paper should clarify this explicitly.

5. **Missing reproducibility details** — Architecture specifications (layer widths for BCBF, number of Fourier modes for FNO, number of layers), hyperparameters \( \lambda_\mathcal{G}, \lambda_S, \lambda_{BF} \), training epochs, learning rates, and the dataset collection procedure (how the 50k trajectory pairs are generated from pre-trained RL models) are not provided. This makes the experiments difficult to reproduce.

### Trivial

6. **Equation (11) is garbled and difficult to parse** — The expression spanning lines 121–125 contains unclear notation (superscript \( N \) appears without definition, operator notation is confusing). While likely a parser artifact, this should be cleaned up.

## Nice-to-Haves
- Reporting maximum or cumulative boundary violation (in addition to feasible rate and average feasible steps) would allow readers to assess the severity of early violations before convergence.
- A discussion of the computational cost (QP solve time, training time for neural operator and BCBF) would help assess practical applicability.
- A sensitivity analysis for the safe set bounds \( \mathcal{S}_0 \) would strengthen the claims.

## Removed Points
- **Criticism that the paper "does not characterize or motivate" boundary feasibility (Critic's point #2)** — This is incorrect. Section 5 explicitly discusses why forward invariance is too strong for oscillatory PDE trajectories and motivates the relaxation to boundary feasibility. The paper does address this.
- **Criticism about "the paper does not explain how the C_α,T term is derived"** — The derivation follows directly from Garg & Panagou (2021b) as cited, and the paper is not required to re-derive standard finite-time CBF results.
- **Criticism that "vanilla PPO/SAC have 0% feasible rate suggesting the safe set is unrealistic or the RL controller was never trained to satisfy it"** — This is precisely why a safety filter is needed. The 0% baseline reinforces the need for safety filtering, not weakness.
- **Criticism demanding comparison to safe RL methods (Lagrangian, constrained MDP)** — The paper claims to be the first in this specific PDE setting, and these methods are designed for ODE dynamics with Markovian state. Requiring non-existent PDE-safe-RL baselines is scope creep.
- **Strength about "the paper addressed an important problem"** — Removed as generic/superficial. The concrete strengths are listed above.
- **Various formatting, parser-artifact, and missing-appendix comments** — Removed per hard rules.

## Novel Insights
The reviews highlight an important tension that is implicitly present in the paper but not fully surfaced: the continuous-time theoretical framework (Theorem 3.2, Equation 11) relies on quantities \( (\partial\kappa^{(l)}/\partial t, \, db_l/dt) \) that standard neural operator architectures (FNO) do not natively expose, because these operators are trained and evaluated on discrete grids. This raises a deeper question about how "differentiable physics" assumptions transfer from the continuous operator theory to discrete neural implementations — a gap that extends beyond this paper. Additionally, the model mismatch problem is structurally harder in PDE boundary control than in ODE CBF-QP because the neural operator approximates a trajectory-to-trajectory map rather than a Markovian state transition, so prediction errors compound over time in a harder-to-characterize way. Neither the paper nor the reviews fully articulate this distinction, but it is an important insight for future work on neural-certificate-based PDE control.

## Suggestions
1. Re-title the paper to avoid overclaiming — replace "Guaranteed" with something like "Toward Safe" or "Safety Filtering for" to match the conditional nature of the guarantees.
2. Add a section or appendix explaining how the continuous-time derivatives in Equation (11) are computed from the trained neural operator in practice (e.g., autograd through the discretized operator, finite differences, or an alternative formulation).
3. Clarify in Section 4 whether the 100-episode evaluations are conducted on the PDE simulator or the neural operator. If on the neural operator, this is a major limitation that must be stated explicitly.
4. Add a simple baseline (e.g., clipping the control to a fixed safe range) to provide a meaningful comparison point for the method's complexity.
5. Include key hyperparameters and architecture details in the main paper or appendix for reproducibility.
