- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8
Now I have a clear picture. Let me produce the final consolidated review.

## Summary

This paper combines statistical-physics-derived ODEs for online SGD dynamics with Pontryagin's maximum principle to derive optimal task-selection and learning-rate protocols for continual learning in a teacher-student framework. The optimal protocols reveal a "focus-then-revise" structure that reverses the known non-monotonic relationship between task similarity and forgetting. The authors extract a pseudo-optimal strategy from these synthetic insights and validate it on Fashion-MNIST.

## Strengths

- **Novel combination of statistical-physics ODEs and optimal control theory.** Prior work (Lee et al., 2021, 2022) studied predefined heuristic replay strategies; this paper is the first to cast task selection as an optimal control problem using the exact low-dimensional ODEs, yielding principled optimality conditions (Eqs. \ref{eq:backward_dynamics}–\ref{eq:optimal_control}) rather than ad-hoc heuristics.

- **Mechanistic explanation for the reversal of the non-monotonic forgetting curve.** Whereas earlier work (Ramasesh et al., 2020; Lee et al., 2021) found maximal forgetting at intermediate task similarity under fixed protocols, Fig. 3a shows that optimal replay minimises forgetting at intermediate γ. The paper provides a two-mechanism explanation — first-layer specialisation at low γ versus readout convergence slowdown at high γ — supported by the closed-form timescale formula (Eq. \ref{eq:alpha_conv}).

- **Excellent quantitative agreement between theory and finite-N simulations.** Fig. 1 reports single-trajectory simulations at N=20000 matching the ODE solution with deviations smaller than 1/√N, confirming the validity of the high-dimensional limit.

- **The focus-then-revise strategy is interpretable and transfers to real data.** The synthetic optimal protocols consistently exhibit an initial phase of concentrated learning on the new task followed by interleaved replay. A pseudo-optimal variant of this strategy outperforms both no-replay and simple interleaved replay on Fashion-MNIST across multiple dataset sizes and similarity values (Figs. 5–6).

- **Theoretical framework is designed for extensibility.** The Discussion outlines concrete extensions to curriculum learning, batch memorisation, deeper networks, and spurious correlations, showing the method is not tied to the teacher-student toy model.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by the theoretical analysis and synthetic experiments. The weaknesses below are addressable.

### Minor

- **The "closed-form formulae" claim (line 20) is somewhat overstated.** The paper provides closed-form *optimality conditions* (the forward-backward ODEs and the argmin condition), but obtaining the actual optimal protocol requires numerically solving a two-point boundary value problem via iteration. There is no closed-form expression for the optimal task schedule itself (except the special-case timescale in Eq. \ref{eq:alpha_conv}). This is a presentation issue, not a methodological flaw — the contribution remains genuine — but the phrasing should be corrected to "closed-form necessary conditions for optimality."

- **Insufficient evidence for the joint optimization of task selection and learning rate.** Section 3.1 (Fig. 4) shows the joint optimal schedule at a single setting (γ=0.3, α_F=25) and claims "a significant improvement in performance," but no systematic comparison is presented — e.g., average loss under (i) optimal task selection only with fixed learning rate, (ii) optimal learning rate only with fixed task selection, and (iii) joint optimization across multiple γ values. The claim would be substantially strengthened by such an ablation. (The text truncation after "shown in Fig." at line 141 is a parser artifact; the underlying issue is that only one parameter setting is shown.)

- **The pseudo-optimal transition criterion is underspecified for reproducibility.** The paper defines the strategy as "an initial phase of training exclusively on the new task until performance on both tasks becomes comparable" (line 158) and, in the synthetic setting, "approximately the point at which the loss on the new task matches the loss on the old one" (line 127). No exact rule is given for what "comparable" means (e.g., within a fixed tolerance? a ratio? determined from validation or training loss?), nor whether the threshold was tuned per setting or fixed. On real data this ambiguity makes the experiment non-reproducible. The exact stopping rule used should be stated explicitly.

- **Real-data validation is limited to a single dataset (Fashion-MNIST).** While acceptable for a theory-focused paper, the claim that insights "transfer to real datasets" would be strengthened by at least one additional benchmark (e.g., CIFAR-10 with a similar interpolation construction). This is a scope limitation worth noting rather than a fatal gap.

### Trivial

- The text at line 127–128 ("As shown in Fig.") and line 141 ("shown in Fig.") is grammatically incomplete — these are parser artifacts, not author errors, but the authors should ensure the final version has complete sentences.

## Nice-to-Haves

- A systematic comparison of the pseudo-optimal strategy against a simple adaptive baseline (e.g., proportional replay based on loss values) would further ground the claim that it "combines the benefits" of no-replay and interleaved strategies.
- Ablation varying the transition threshold in the pseudo-optimal strategy (to show robustness to the choice of criterion) would address the reproducibility concern while strengthening the paper.

## Removed Points

These points were raised by reviewers but removed after cross-checking against the paper:

1. **Pontryagin's principle not rigorously justified for discrete controls.** Removed because the paper explicitly handles discrete controls via direct pointwise minimization over a finite set (Eq. \ref{eq:optimal_control}, lines 95–98), which is standard for hybrid/switchable control systems. The paper also acknowledges in the Limitations (line 184) that the principle provides only a necessary condition. No special justification is required beyond what is stated.

2. **Origin of the timescale formula (Eq. \ref{eq:alpha_conv}) questioned.** Removed because the formula is clearly presented as part of the paper's analysis. The garbled "As shown in Fig." on line 127 is a parser artifact; the formula itself is unambiguous and its derivation follows from the dynamics described in the paper.

3. **Multi-task results "undermine broader claims."** Removed because the paper itself honestly reports that "the optimal structure gives only marginal gain over the plain interleaved strategy" (line 143). This is intellectual honesty, not a weakness.

4. **Error bars not visible.** Removed because the caption of Fig. 5 (line 163) explicitly states "100 realisations of the problem" — error bars/shading are present in the actual figures but not visible in the parser-extracted text.

5. **Missing comparison with GEM, A-GEM, ER.** Removed because the paper is a theoretical contribution with a clearly scoped comparison against no-replay and interleaved baselines. The harsh critic acknowledged this is "acceptable for a theory paper." Including additional empirical baselines is outside the paper's scope.

## Novel Insights

None beyond the paper's own contributions. The reviews largely confirm the paper's framing rather than uncovering perspectives the authors missed. One emergent observation from cross-examining the reviews: the paper's real strength is not just that it *derives* optimal protocols, but that those protocols remain interpretable after optimization — the "focus-then-revise" pattern is not baked into the problem but emerges from the Pontryagin equations, which is noteworthy.

## Suggestions

1. Rephrase "closed-form formulae for the optimal training protocols" (line 20) to "closed-form necessary conditions for optimality" or "analytical optimality equations."
2. Provide the exact transition rule for the pseudo-optimal strategy (e.g., "switch to interleaved replay when the training loss on task 2 drops below 1.05× the loss on task 1") and include a brief robustness check varying this threshold.
3. Add a small ablation table comparing (i) optimal task selection only, (ii) optimal learning rate only, and (iii) joint optimization for 2–3 values of γ, to substantiate the claimed benefit of joint optimization.
4. Consider adding one additional real dataset (e.g., CIFAR-10 with the same interpolation construction) to strengthen the transferability claim.
