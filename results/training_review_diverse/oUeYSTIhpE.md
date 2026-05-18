Now I have a complete understanding of the paper and all the claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes DisCo-DSO, a method that extends generative-model-based optimization (deep RL for combinatorial optimization) to jointly sample discrete tokens and their associated continuous parameters, rather than using the standard decoupled approach where a discrete skeleton is sampled first and continuous parameters are optimized separately via a black-box solver. The method is evaluated on a parameterized bitstring benchmark, symbolic regression, and decision tree policy learning for RL. The strongest empirical contribution is on the decision tree task, where DisCo-DSO outperforms existing specialized DT methods (evolutionary, cascading, differentiable DTs) across all four OpenAI Gym environments tested.

## Strengths

1. **Convincing decision tree results against specialized methods.** On all four Gym environments (MountainCar-v0, CartPole-v1, Acrobot-v1, LunarLander-v2), DisCo-DSO discovers univariate decision trees that outperform all compared baselines (evolutionary DTs, cascading DTs, differentiable DTs) in mean reward while maintaining comparable or lower parameter complexity (Figure 6). This is a clean empirical result that directly validates the practical value of joint discrete-continuous optimization.

2. **Clear pedagogical demonstration of sample efficiency.** The parameterized bitstring task (Section 4.1, Figure 2) provides a controlled setting where the advantage of joint optimization is cleanly demonstrated: DisCo-DSO achieves high reward with orders-of-magnitude fewer function evaluations than decoupled approaches. The design with known global optima, tunable difficulty (α weight, choice of f₁/f₂), and controlled comparison makes the efficiency argument transparent.

3. **Principled extension of deep RL to hybrid action spaces.** Section 3.2 formulates a joint autoregressive model emitting both discrete logits ψ⁽ⁱ⁾ and continuous distribution parameters φ⁽ⁱ⁾, enabling a unified risk-seeking policy gradient. The method does not require differentiability of the reward function and applies to any hybrid discrete-continuous optimization problem where the objective can be evaluated on complete solutions.

4. **Generalization advantage in symbolic regression.** Figure 3 shows DisCo-DSO achieves the best average test reward while using the fewest function evaluations, and avoids the overfitting/bloat problem that harms decoupled GP methods. This demonstrates that joint optimization learns useful priors from past samples rather than optimizing continuous parameters from scratch for each discrete skeleton.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Underspecified continuous parameter distribution.** The paper never states the distribution family for the continuous parameters in the general formulation or for the symbolic regression experiments. In Section 3.2, the method is described using a generic distribution D(βᵢ|lᵢ, φ⁽ⁱ⁾) emitted by the network, but the paper does not specify what φ⁽ⁱ⁾ contains (e.g., mean and variance of a normal? parameters of a truncated normal?) or how many output units correspond to each continuous-capable token. For the DT experiments, truncated normal distributions are mentioned (Section 4.3), but for the bitstring task and symbolic regression, the distribution family is not discussed at all. This is a reproducibility gap that should be addressed with a concrete specification — a simple table or algorithm block stating the distribution family, parameterization of φ, and how bounds are enforced would suffice.

2. **Per-skeleton optimization budget for decoupled baselines is not reported.** The central claim is that DisCo-DSO is more sample-efficient than decoupled approaches. The paper shows this advantage visually in Figures 2, 3, and 5, but never states how many function evaluations each downstream optimizer (L-BFGS-B, anneal, DE) is allowed per discrete skeleton. If the per-skeleton budget is too small, the decoupled methods might receive unfairly low rewards even for correct skeletons. While the structural advantage of 1 evaluation per complete solution versus many evaluations per skeleton is clear, the lack of this detail makes it harder for readers to assess whether the comparison is quantitatively fair. The paper should report the per-skeleton budget and ideally show that giving the downstream optimizer a much larger budget does not close the efficiency gap.

3. **Claim about avoiding bloat is asserted without analysis.** The paper states that DisCo-DSO "is able to avoid" the bloat problem in symbolic regression (Section 4.2), but offers no explanation or analysis of why joint optimization avoids overfitting where decoupled approaches do not. A brief discussion — e.g., showing that joint optimization reduces tree complexity, or that the risk-seeking objective implicitly penalizes unnecessary constants — would substantially strengthen this claim.

4. **Gradient formula is incompletely presented in the parsed text.** The gradient estimator (Eq. 14, line 94) appears truncated by the two-column format, showing only the discrete-token gradient term. The continuous-parameter gradient term is missing from the visible text. While this is a parser artifact and likely present correctly in the original submission, the current rendering makes the gradient computation impossible to verify from the provided text alone.

### Trivial

- The paper uses REINFORCE for both discrete and continuous actions. While this is a standard choice and the risk-seeking quantile baseline provides variance reduction, a brief comment acknowledging known variance concerns with score-function gradient estimators for continuous actions would be useful context.

## Nice-to-Haves

- An ablation comparing DisCo-DSO against a version where continuous parameters are learned by the generative model but sampled *after* the discrete skeleton is fixed (separate heads, no backprop through the discrete choice). This would isolate the benefit of joint exploration versus the benefit of learning a continuous distribution at all.
- A comparison against an SR method that tokenizes constants (e.g., Kamienny et al. 2022) on a standard benchmark would strengthen the generality argument for the SR setting, though the paper's main contribution is the general framework rather than a specific SR system.

## Removed Points

- **Missing comparison against published SR methods (Kamienny et al., Sahoo et al., etc.):** This paper is a general method paper for joint discrete-continuous optimization, not an SR benchmark paper. SR is one of three experimental domains. The decision tree results are the primary strength. Demanding head-to-head comparison against every SR method is scope creep. *Justification: The paper's contribution is the joint optimization framework, evaluated across multiple domains. The SR experiments are sufficient to demonstrate the approach's viability in a non-trivial hybrid space.*

- **REINFORCE variance as a critical issue:** The reviewer flags high variance of score-function gradients in continuous action spaces, but the paper uses a risk-seeking policy gradient (quantile-based baseline) which is a well-known variance reduction technique. The continuous parameter spaces tested are small (one or a few constants per token). This is a generic concern applicable to any REINFORCE-based method, not a specific weakness of this paper. *Justification: The paper already employs variance reduction via the risk-seeking objective; the concern is generic and not shown to be a practical problem in the experiments.*

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the paper's generality claim and the limited SR comparison set, but this is a standard scope constraint rather than a novel observation.

## Suggestions

1. **Add a concrete specification of the continuous parameter distribution.** Provide a table or algorithm block stating, for each experiment: (a) distribution family used (normal, truncated normal, uniform, etc.), (b) what φ contains (mean, variance, bounds), and (c) how output units map to distribution parameters for each token type. This is the single most impactful fix for reproducibility.

2. **Report the per-skeleton budget for all decoupled baselines.** State the number of function evaluations allowed per discrete skeleton for L-BFGS-B, simulated annealing, and differential evolution. Ideally, add a sensitivity analysis showing the effect of increasing the per-skeleton budget by an order of magnitude.

3. **Add a brief analysis of the bloat avoidance claim.** Even a paragraph showing comparative tree complexity or a qualitative explanation would turn an asserted observation into a supported claim.

4. **Clarify whether the entropy bonus for continuous distributions is computed analytically or via Monte Carlo estimation** for the truncated normal case, and provide the formula used.

## Score and Decision

This paper makes a genuine contribution: the joint discrete-continuous optimization framework is well-motivated, cleanly presented, and convincingly validated on the decision tree task where it outperforms all specialized baselines. The weaknesses are real but addressable — the distribution specification is the most important fix. None of the issues are fatal or invalidate the core claims. The paper merits acceptance with minor revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>