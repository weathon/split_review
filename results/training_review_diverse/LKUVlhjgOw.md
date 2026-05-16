Now I have all the information I need. Let me synthesize the final review.

## Summary

The paper proposes a safety filtering framework for PDE boundary control when the PDE dynamics are unknown. It introduces a neural boundary control barrier function (BCBF) and uses a neural operator to learn the input-output mapping, proving that the BCBF derivative depends linearly on the control input derivative, enabling quadratic programming-based safety filtering for pre-trained RL controllers. Experiments on hyperbolic, parabolic, and Navier-Stokes PDEs show improved feasibility rates compared to vanilla PPO and SAC baselines.

## Strengths

- **First safe boundary control framework for unknown PDE dynamics**: The paper correctly claims priority on this problem. Prior safe PDE control methods (Krstic & Bement, 2006; Li & Krstic, 2020; Koga & Krstic, 2023) all assume known analytical PDE dynamics. This is a clear advance.

- **Novel integration of neural operator and BCBF enabling QP-based safety filtering**: Theorem 3.2 proves that the BCBF constraint is affine in ˙U(t) through the neural operator's differentiable structure (Equation 11), which is a non-trivial technical contribution. This circumvents the non-Markovian nature of PDE boundary control that prevents direct application of standard ODE CBFs.

- **New "boundary feasibility" notion tailored for PDE control**: Definition 2.1 (finite-time convergence-and-stay) is motivated by the fact that PDE trajectories can be highly oscillating and may temporarily leave the safe set early on. This is a principled adaptation of safety concepts to PDE dynamics.

- **Comprehensive ablation studies**: The paper examines the filtering threshold η (Figure 2), asymptotic vs. finite-time convergence (Table 4), and different neural operator architectures FNO vs. MNO (Table 5), providing insight into design choices.

- **Consistent feasibility improvements across environments**: The feasible rate and average feasible steps improve for all environments compared to vanilla RL baselines. For instance, on the 1D hyperbolic PDE, PPO with time-dependent BCBF filtering achieves feasible rate 0.95 (vs. 0.70 for vanilla PPO), and on 2D Navier-Stokes, PPO with filtering achieves 0.91 (vs. 0.61 for vanilla PPO).

## Weaknesses

### Fatal
None.

### Major

- **The "Guaranteed" title and framing overstate what is actually proven.** Theorem 3.2 explicitly assumes the neural operator is "an exact map... without model mismatch" (line 118), a condition never met in practice. While the paper acknowledges this as a limitation and introduces the filtering threshold η as a workaround (line 142), it provides no analysis of how large model mismatch can be before the guarantee breaks, nor any experiment measuring neural operator accuracy or relating it to safety violations. The conclusion also states "boundary feasibility is guaranteed by filtering the unsafe boundary conditions using the BCBF" (line 224), which conflates the theoretical guarantee (conditional on exact model) with the practical algorithm. This is a structural gap between the paper's advertised contribution and its evidence.

- **The safety filtering procedure is an offline trajectory modifier, not an online safety filter, but this is not clearly stated.** The paper says QP computation is "not yet real-time" and "we adopt the predicted Y(t) from the neural operator after each filtering step instead of real PDE dynamics" (line 142). This means the filter operates on the neural operator's predictions in a simulation loop, producing a pre-computed safe trajectory that is then deployed open-loop on the real PDE. This distinction from closed-loop safety filtering (which guarantees safety under the true dynamics via online intervention) should be explicitly clarified. The title and abstract should be adjusted to reflect that the safety filter works on the learned surrogate, with safety on the real PDE being approximate and dependent on model accuracy.

- **Statistical rigor is insufficient.** All results are reported from 100 episodes without variance, confidence intervals, or multiple random seeds. This makes it impossible to assess whether improvements are statistically significant or reproducible.

- **No safety-aware baselines are compared.** The paper only compares against vanilla RL controllers (PPO, SAC). Without comparison to any simple safety heuristic (e.g., output clipping, reward shaping for safety, or a naïvely applied CBF with a learned dynamics model), it is unclear whether the complexity of the BCBF + neural operator architecture is warranted. Given that the paper claims to be the first in this setting, it should at least include a reasonable non-neural baseline.

- **Safe set constraints differ between PPO and SAC for the same environment without justification.** For the hyperbolic PDE (Table 1), the constraint is Y<1 for PPO but Y<0 for SAC. For the parabolic PDE (Table 2), it is Y<0.6 for PPO but Y>-0.26 for SAC. No justification is given for why different constraints are used, raising concerns about post-hoc selection and making cross-controller comparison inconsistent.

### Minor

- **The "better general performance" claim in the abstract and contributions is overbroad.** Reward decreases after safety filtering in several cases: SAC on the hyperbolic PDE (0.58→0.57/0.55), both controllers on Navier-Stokes (PPO: 1.47→1.36/1.29, SAC: 39.59→35.98/37.30). The paper acknowledges some of these cases (e.g., "safety filtering for SAC models compromises the stabilization performance with lower reward" in Section 4.2), but the abstract-level claim should be tempered.

- **No evaluation of neural operator prediction accuracy is provided.** Without knowing how well the neural operator predicts the true Y(t) on held-out trajectories, it is impossible to assess the reliability of the derived QP constraints. A simple plot of predicted vs. true Y would be informative.

- **The joint training of the neural operator and BCBF (Equation 7) uses dG_θ(U)/dt in the BCBF loss, creating a dependency where the BCBF condition may appear satisfied on the model's output while being violated under the true dynamics.** This potential failure mode (the BCBF and operator could jointly "overfit" to satisfy the condition on training data) is not discussed.

- **No ablation of the loss function hyperparameters λ_G, λ_S, λ_BF** is provided, making it difficult to assess sensitivity to these weights.

- **The claim of being "first to study safe boundary control with unknown PDE dynamics"** would benefit from a more careful literature discussion in the related work, checking against alternatives such as robust MPC with learned models or other model-based safe control approaches that could handle PDEs without analytical forms.

- **The paper provides no runtime numbers** for the QP filtering step, even though it acknowledges that QP is "not yet real-time." This makes it difficult to gauge the gap between the current method and any potential online deployment.

### Trivial
- None that survive filtering per instructions.

## Nice-to-Haves

- An analysis relating the filtering threshold η to neural operator prediction error, showing what magnitude of error can be tolerated before safety violations occur.
- A simple baseline: e.g., proportional control that drives Y toward the safe set when near the boundary, or naive output clipping applied to the RL controller.
- Runtime analysis or discussion of how QP could be accelerated for potential online deployment.
- Code release for reproducibility.
- Multiple random seeds with standard deviations reported for all metrics.

## Removed Points

These points from the original harsh critique are removed for the following reasons:

- **Derivation of Cα,T not provided / Theorem 3.1 not proven**: The reviewer criticizes missing derivations. Conference papers commonly defer proofs to an appendix, which the parser strips. This is not a valid weakness to levy against the main paper text.
- **"The paper does not discuss how the integrals are discretized"**: Hyperparameters and implementation details that are impractical to exhaustively list in a conference paper. The paper's method description is at the appropriate level of detail.
- **"The paper does not discuss cases where the safe set is disconnected or more complex"**: Scope creep — the paper explicitly states it studies simple one-sided and two-sided sets, and notes complicated constraints as future work.
- **Criticism about missing related works**: Per instructions, I cannot confirm existence of missing references and must not mention them.
- **Pure formatting/style nitpicks**: Parser artifacts, not author errors.
- **Criticism about missing appendix content**: Stripped by the parser, present in original submission.
- **"No code release"**: Per instructions, reproducibility nitpicks about artifacts impractical for submission are removed; moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any fundamentally new observation about the approach that would reshape how the contribution is understood. The tension between the "guaranteed" framing and the conditional nature of the theory is the central issue, but this is an evaluation judgment rather than a novel insight.

## Suggestions

1. **Remove "Guaranteed" from the title** or add a qualifier (e.g., "Neural PDE Boundary Control with Neural Barrier Function Safety Filters"). The current title promises more than the theory delivers.

2. **Explicitly position the method as an offline trajectory modifier** (safety filtering applied to the neural operator surrogate, then deployed open-loop on the real PDE). Clarify what can and cannot be guaranteed under model mismatch.

3. **Add a simple figure or table showing neural operator prediction error** (predicted vs. true Y) on held-out trajectories, ideally correlated with safety outcomes.

4. **Add at least one non-RL baseline**: a simple heuristic (e.g., proportional control toward the safe set boundary) to calibrate whether the BCBF+neural operator complexity is justified.

5. **Report variance across multiple seeds** for all metrics. Single-seed 100-episode evaluations are insufficient.

6. **Justify why PPO and SAC have different safe set constraints** in the same PDE environment, or unify them.

7. **Temper the "better general performance" claim** in the abstract to reflect that reward can decrease when safety and control objectives conflict.

## Score and Decision

The paper tackles an interesting and underexplored problem — safe boundary control for unknown PDE dynamics — and proposes a technically novel combination of neural BCBF and neural operators. The proof that the BCBF constraint becomes affine in ˙U through the neural operator is a genuine contribution, and the empirical feasibility improvements are consistent.

However, the paper has several significant weaknesses that prevent acceptance in its current form. The "Guaranteed" framing is misleading given that the theoretical guarantee assumes an exact neural operator with no analysis of model mismatch. The safety filter is revealed to be an offline trajectory modifier (not an online safety filter), but this is not clearly articulated. The experimental evaluation lacks statistical rigor and safety-aware baselines. These are structural issues that go beyond presentation fixes.

The underlying approach has merit, but the paper needs major revisions to align its claims with its evidence before it can be accepted.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>