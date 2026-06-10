Here is the final consolidated review.

---

## Summary

This paper proposes the first reinforcement learning algorithms for finite-space mean-field type games (MFTGs) with general dynamics and reward functions. MFTGs model Nash equilibria between large coalitions of cooperative agents. The paper makes three main contributions: (i) a theorem proving that MFTG solutions provide ε-Nash equilibria for finite-coalition games with an explicit O(1/√N) rate; (ii) a tabular Nash Q-learning algorithm with discretization error analysis; and (iii) a deep RL (DDPG-based) algorithm that scales to larger state spaces. Numerical experiments on up to 200-dimensional mean-field distributions demonstrate feasibility.

## Strengths

- **Theorem 1 provides an explicit convergence rate (O(1/√N))**
  connecting MFTG Nash equilibria to approximate Nash equilibria in finite-coalition games. This goes beyond prior asymptotic-only results (e.g., Saldi et al. 2018) and cleanly expresses the rate in terms of state/action cardinalities and coalition sizes.

- **Theorem 3 gives a non-trivial error decomposition for discretized Nash Q-learning**
  with closed-form constants C₁, C₂ separating the time-dependent learning error from the discretization errors ε_A and ε_S. This provides a principled understanding of how approximation quality depends on the grid fineness.

- **First RL algorithms for general finite-space MFTGs (beyond LQ settings)**
  Prior RL work on MFTGs (Carmona et al. 2020, Zaman et al. 2024) was restricted to linear-quadratic settings where policies have exact parametric representations. The paper addresses a genuine gap for general dynamics and rewards.

- **Scalability demonstrated to mean-field distributions of dimension 200**
  The four-room example (Example 2) operates at a scale that the tabular approach could not handle, providing concrete evidence that the deep method extends beyond toy problems.

- **Evaluation uses exploitability, a principled metric for equilibrium proximity**
  Rather than relying solely on reward curves, the paper computes exploitability by training best-response policies, providing a more direct measure of how close the learned policies are to a Nash equilibrium. This is used across all main experiments.

## Weaknesses

### Fatal

None.

### Major

- **Theorem 1's condition γ(1 + L_π + L_p) < 1 is restrictive and unexamined in experiments.**
  The discount factor γ and Lipschitz constants L_π (policy class) and L_p (transition) jointly determine whether the finite-coalition approximation guarantee holds. The paper never specifies or bounds L_π or L_p for any of the five experimental environments, nor does it discuss whether this condition holds in practice. If L_π + L_p is large, γ must be very small, potentially making the game effectively myopic. The Lipschitz condition on policies (Assumption 1c) is stated as a property of the policy class, which is verifiable in principle, but the numerical values are never contextualized.

- **Tabular convergence relies on the strong Hu-Wellman stage-game condition.**
  Assumption 3(c) requires every stage game to have a global optimal point or a saddle point — a structural condition that essentially assumes away the multi-agent equilibrium-finding difficulty. The paper states "it seems that in practice the algorithm works well even when this assumption does not hold" (line 246), but provides no evidence for this claim in the MFTG setting. Since the stage games involve continuous action spaces (distributions over agent actions), whether such points exist is non-trivial.

- **Baselines are too weak to fully support the empirical claims.**
  The two baselines (IL-MFTG and ablated DDPG) both withhold cross-coalition information; they test whether *having more information* helps, not whether the *specific algorithmic choices* (Nash Q-learning, centralized DDPG architecture) are superior to other methods that also use full information. For a paper claiming to propose effective learning algorithms for MFTGs, comparisons against approaches that also observe all coalitions' distributions but use different learning rules (e.g., independent PPO at the central-player level, or CTDE-based multi-agent RL) would be more informative. The "at least 30% improvement" claim (Appendix Table) lacks context about the metric, baseline, and whether this is averaged across environments.

- **Exploitability is computed via approximate best-response with uncalibrated error.**
  The exploitability metric — the paper's primary evidence that policies form a Nash equilibrium — requires training a DDPG-based best-response policy. The paper acknowledges (line 369) that deep RL "can only approximate the best response and cannot achieve it with absolute accuracy," but the magnitude of this approximation error is never quantified. In Example 3, exploitability fluctuates "between 0 and 100" (line 368-369) without any characterization of the reward scale or BR approximation quality. This makes it impossible to separate how far the profile is from equilibrium from how poor the BR approximation is.

### Minor

- **Stage-game solving complexity is not discussed for the tabular method.**
  At each iteration, the algorithm must compute a Nash equilibrium of a stage game with continuous action spaces (distributions over discretized agent actions). The complexity, accuracy, and algorithmic approach for this step are not described in the main text, making it difficult to assess the computational bottleneck of the tabular method.

- **No analysis of training cost or sample complexity.**
  The paper reports no wall-clock time, number of environment steps, or parameter counts for any method or baseline. This makes it hard to assess the practical cost of the claimed scalability improvements.

- **The deep method's convergence behavior is not analyzed beyond plotted curves.**
  While exploitability curves are shown, there is no discussion of whether exploitability decreases monotonically, whether performance plateaus, or whether variance across seeds decreases with training.

### Trivial

None.

## Nice-to-Haves

- Calibrating the exploitability BR approximation error on small problems (e.g., Example 1) where a tabular best-response could be computed exactly would significantly strengthen the evidence.
- A sensitivity analysis showing how Theorem 1's γ(1+L_π+L_p) < 1 condition maps to actual values in at least one environment would help readers gauge practical relevance.

## Removed Points

These points were considered but removed per the review guidelines:

- "The deep RL algorithm is underspecified in the main text" — This criticism targets content that resides in the appendix (Algorithms 1 and 2, architecture details, hyperparameters). The main text states the algorithm class (DDPG variant) and references the appendix. The hard rules require removing criticisms about missing appendix content that was stripped by the parser.
- "No variance estimates, confidence intervals, or statistical tests" — The figures show mean ± standard deviation / stddev (Figs. 1, 2, 3 captions). Error bars are present; the criticism is factually incorrect.
- "L_π appears in the condition but is itself a property of the learned policy — so it is not a condition that can be verified before learning" — Assumption 1(c) applies to the *policy class* (the set Π^i of admissible policies), not the specific learned policy. If the policy class is restricted to functions with Lipschitz constant ≤ L_π, the condition is verifiable before learning. The broader concern (restrictiveness of the condition) is retained above.
- "The paper should report effect sizes, not just relative improvements" — The improvement claim ("at least 30% in each game") is concrete and tied to a table in the appendix. The criticism is too vague to retain as a distinct point.
- "No training curves with error bars are shown" — Factually incorrect; the figures show mean ± stddev curves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Contextualize the γ(1+L_π+L_p) condition**: Provide estimates or bounds for L_π and L_p in at least one experimental environment, or discuss what classes of MFTGs naturally satisfy this condition without forcing a near-myopic γ.

2. **Augment baselines with full-information alternatives**: Add comparisons against methods that also observe all coalitions' distributions but use different learning rules (e.g., independent PPO with a centralized critic, or a multi-agent TD3 variant applied at the central-player level). This would test whether the *specific algorithmic design* matters, not just whether cross-coalition information is useful.

3. **Calibrate the exploitability approximation**: On small problems (Example 1), compare the DDPG-computed best response against an exact (tabular) best response to quantify the BR approximation error magnitude. Report exploitability both with and without this calibration.

4. **Report computational costs**: Include wall-clock time, number of environment steps, neural network parameter counts, and hardware specifications for both methods and baselines.

5. **Clarify the stage-game solver**: For the tabular method, describe how the Nash equilibrium of the discretized stage game is computed (algorithm used, computational complexity, effect on overall convergence).

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>