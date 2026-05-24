Now I have a solid calibration. Let me write the final review.

## Summary

This paper presents a real-time framework for designing high-dimensional optogenetic-style stimulations to drive latent neural dynamics in desired directions. The framework combines streaming latent-space construction (including a novel streaming jPCA variant), dynamical models (Kalman filter, VJF, Bubblewrap), a kernel-regression-based nonparametric stimulus-response mapping with temporal discounting, and constrained optimization for stimulus design under sparsity and non-negativity constraints. The method is designed to run end-to-end in under 100ms.

## Strengths

- **Novel streaming jPCA with Orthogonal Procrustes stabilization (sjPCA).** Section 2.1 introduces a streaming extension of jPCA using Sherman–Morrison updates and an Orthogonal Procrustes step to stabilize each rotational plane independently. Figure 1a demonstrates that sjPCA converges to the same subspace as an offline fit within seconds. This is a concrete algorithmic contribution beyond a simple combination of existing pieces.

- **Full real-time pipeline from latent construction through constrained stimulus optimization.** The paper integrates streaming dimensionality reduction, dynamics modeling, nonparametric response learning, and box-constrained optimization into a single framework (Algorithm 1). The pipeline runs end-to-end at <100ms (Section 3), which is a necessary condition for closed-loop *in vivo* use.

- **Adaptive stimulus-response mapping that handles non-stationarity.** The kernel regression model (Equation 7) incorporates a temporal kernel that discounts old samples. Figure 2e shows that after a 180° flip in the response map at t=25s (simulating a probe shift), the model recovers within ~15s, while a blind model suffers sustained elevated error. This demonstrates a genuine capability that fixed-mapping approaches lack.

- **Optimization demonstrably finds stimulations aligned with arbitrary latent directions.** Figure 4a shows that the designed stimuli produce observed responses whose angular deviation from the target is much smaller than random alternatives (single-neuron, multi-neuron, shuffled versions). For feasible directions, >84% of optimizations yield <1° predicted misalignment (Figure 4b).

## Weaknesses

### Major

1. **"Real neural data" experiments use simulated, not real, stimulation effects.** Section 4.1 states: "For each of the real datasets, we simulated stimulations using an autoregressive function… $a_t = 0.8 \cdot a_{t-1} + u_t$." The background neural activity is real (calcium imaging and electrophysiology), but the stimulation-induced perturbation is synthetic — a simple linear AR(1) additive process. This means the stimulus-response model is only validated against this manufactured effect, not against actual biological responses to stimulation. The paper's framing — "demonstrate our approach on both simulated and real neural data" (abstract) — is technically correct but risks overstatement, as the "real data" experiments do not test the method's ability to handle the nonlinear, high-dimensional, and non-stationary stimulation effects that occur in genuine experiments. The Discussion acknowledges offline operation but does not flag the simulated nature of the stimulation effects as a limitation.

2. **No comparison against existing adaptive stimulation methods.** The only baselines are random stimulation patterns (single neurons, groups, shuffled versions) and a "blind" dynamical model that ignores stimulation. The paper cites Wagenmaker et al. (2024), Minai et al. (2024), and Draelos & Pearson (2020) as related work addressing adaptive stimulus selection, but makes no experimental comparison. While direct comparison may require significant adaptation (these methods target different problem settings), the paper does not explain why comparison is infeasible, nor does it benchmark against even simple alternatives such as greedy selection of neurons with largest loading in the target latent direction. Without this, it is unclear whether the complexity of the differentiable-kernel-plus-non-convex-optimization approach is justified over simpler baselines.

### Minor

3. **Optimization procedure underspecified.** Algorithm 1 line 19 states only "Solve with box constraints." The paper does not name the optimizer (L-BFGS-B? Adam with projection? SLSQP?), report convergence criteria, describe how the ℓ₁ penalty term is handled (proximal gradient? ADMM? smooth approximation?), or study sensitivity to the hyperparameter λ₁. This compromises reproducibility and prevents independent implementation.

4. **No ablation of kernel components.** The stimulus-response model (Equation 7) uses three kernels: K₁ (state), K₂ (stimulus), K₃ (time). It is unclear how much each contributes. For instance, does the temporal kernel K₃ do the heavy lifting in the non-stationarity experiments (Figure 2e), or is the state kernel K₁ critical? Without ablations, the necessity of each component is unclear.

5. **Effect of stimulation on streaming dimension reduction not discussed.** The latent space is updated continuously via streaming PCA/sjPCA, even during stimulations. If a large stimulation causes a transient in neural activity, the streaming subspace estimate could be transiently perturbed. The paper does not test or discuss this failure mode.

### Trivial

- None beyond standard presentation artifacts (parser-related, not substantive).

## Nice-to-Haves

- The optional β coefficients for multi-step delayed stimulation effects (Section 2.3) are introduced but never used in results. Either include them or remove the discussion.
- A sensitivity analysis of λ₁ would clarify how the sparsity constraint trades off against alignment error.
- Formal significance tests on the error comparisons (Figure 3) would strengthen the claims.

## Removed Points

- **"The method is learning the exact model used to generate the ground truth response"** — The harsh critic claimed the method learns the exact AR(1) generative model. This is incorrect: the method uses kernel regression (nonparametric), which is structurally different from the AR(1) process used to simulate the raw stimulation effect. The kernel regression must learn from the projected latent responses, not from the AR parameters. The broader concern about using a simple linear model for stimulation effects is valid and retained above, but this specific formulation is factually wrong.

- **"Missing related works"** — Removed per instructions: I have no external sources to confirm existence of unmentioned works.

- **"Formatting/typo/style nitpicks"** — Removed as parser artifacts.

- **"Could include more models/datasets"** — Generic suggestion that does not harm core claims.

## Novel Insights

The key tension this paper surfaces — that few neuroscience papers bridge the gap between streaming latent-space methods and real-time stimulation design — is well-articulated by the reviewers. The paper's own contribution framework is clear. Beyond what the paper states, the most notable observation from the review process is that the streaming jPCA contribution (Orthogonal Procrustes stabilization of each rotational plane independently) is a genuinely novel algorithmic idea that could have value even outside the stimulation context, but it is somewhat buried in Section 2.1 and under-validated (only shown on one simulated system). The paper would benefit from pulling this forward and evaluating it on additional dynamical regimes.

## Suggestions

1. **Clarify the evaluation status of the "real data" experiments** throughout the paper (abstract, conclusion) so it is unmistakable that stimulation effects are simulated. This is the single issue most likely to mislead or frustrate readers.

2. **Add a simple non-random baseline** — e.g., greedy selection of the top-k neurons with largest loading in the target latent direction. This would directly test whether the optimization complexity is worthwhile.

3. **Report the specific optimizer and convergence criteria** used for Equation (8), and include a λ₁ sensitivity analysis in the supplement.

4. **Add ablation experiments** removing one kernel at a time (K₁, K₂, K₃) to show which components are essential.

5. **Test the effect of large stimulations on streaming subspace stability** — e.g., inject a transient and measure the subspace angle deviation before/after.

## Final Score and Decision

**Round 1 — Bracketing:** 
Weak anchors (<3.5 avg): BBldjKEBlJ (3.00), NPzuN3Rxi8 (3.00), fnO5h1CFyh (3.00), 04RGjODVj3 (3.00) — all reject-level papers with fundamental flaws or thin evaluation.

Middle anchors (3.5–7.5): FwW3jqchtY iSSM (5.00), 4ltiMYgJo9 EEG closed-loop (5.75), LNp7KW33Cg HDA (5.00), eR1119aUlL MRINE (4.25).

Strong anchors (>7.5): cNmu0hZ4CL (8.00), RWJX5F5I9g (8.00) — top-tier theory/neuroscience papers.

**Initial bracket:** 4.0–5.5. The paper has genuine algorithmic novelty (sjPCA, full pipeline) that puts it above the 3.0 band, but the evaluation weaknesses (simulated stimulations on real data, no non-random baselines) keep it below the 5.75–6.0 band.

**Round 2 — Narrowing:** Compared against FwW3jqchtY iSSM (avg 5.00) — this paper also lacks proper baselines and has strong assumptions, but notably has real optogenetic/microstimulation intervention data and an identifiability proof. Our paper's evaluation is weaker on real-data validation but stronger on streaming/real-time engineering. Compared against eR1119aUlL MRINE (avg 4.25) — this paper was criticized for being a combination of existing techniques with limited novelty; our paper has more novel algorithmic contributions (sjPCA) but similar evaluation gaps. The paper sits between these two anchors.

**Final score:** 4.5. The framework is coherent and novel in its integration, and the sjPCA contribution is genuinely new. However, the evaluation does not establish effectiveness on real stimulation responses (only simulated), and the lack of non-random baselines leaves the optimization's added value unproven against simpler alternatives. A major revision with real stimulation data (or a more realistic forward model) and proper baselines could raise this substantially.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>