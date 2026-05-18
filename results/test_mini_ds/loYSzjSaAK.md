Now I have a thorough understanding of the paper and all the relevant anchors. Let me compose the final review.

## Summary

The paper introduces **submodular RL** (subRL), a framework for reinforcement learning where rewards are modeled by submodular set functions that capture diminishing returns as states are revisited. It proves a hardness-of-approximation result (Theorem 1) showing subRL cannot be approximated to any constant factor under standard complexity assumptions. The paper proposes **SubPO**, a policy gradient algorithm that decomposes the total submodular reward into a sum of marginal gains and uses this decomposition as the credit-assignment signal. Theoretical guarantees are provided under restrictive assumptions (ε-Bandit SMDPs, curvature bounds), and experiments are run on six domains ranging from grid-world item collection to continuous MuJoCo control.

## Strengths

1. **Hardness-of-approximation result (Theorem 1).** The paper proves that even deterministic submodular MDPs cannot be approximated within a factor better than Ω(log^{1-γ} OPT) unless NP ⊆ ZTIME(n^{polylog(n)}). This is a genuine theoretical contribution that establishes fundamental limits of the framework and is correctly proved via reduction from the submodular orienteering problem.

2. **Problem formulation and connection to related areas.** The paper coherently formalizes submodular rewards in RL, defines the submodular MDP (SMDP), draws connections to submodular orienteering, adaptive submodularity, convex RL, and submodular bandits (Section 2, Related Work). This framing is novel and may be useful for future work.

3. **Unbiased marginal-gain policy gradient estimator.** Equation (3) derives an unbiased gradient estimator that uses the marginal gain decomposition with a history-dependent baseline, incorporating causality. While the derivation is straightforward (standard policy gradient + marginal gain decomposition), the resulting estimator is clean and practically applicable.

## Weaknesses

### Major

1. **Insufficient empirical evaluation — only one strawman baseline.** The paper compares SubPO exclusively against "modular RL" (MRL), which treats the per-step reward as the singleton value F({s}) and sums additively. This baseline is expected to fail on every task by construction, since it ignores diminishing returns entirely. For each application studied (informative path planning, item collection, Bayesian experiment design, coverage), there exist established algorithms — greedy submodular orienteering (Chekuri and Pál, 2005), sequential greedy for sensor placement (Krause et al., 2008), adaptive submodular optimization (Golovin and Krause, 2011), and existing RL-based informative path planning methods — none of which are compared against. The paper's central empirical claim that SubPO is "effective" cannot be assessed from the evidence provided. This is the most critical weakness.

2. **Missing control ablation: marginal-gain decomposition vs. total submodular reward.** The paper attributes SubPO's performance to the marginal gain decomposition but never compares against running the same policy gradient algorithm using the total submodular reward F(τ) as the return (i.e., standard REINFORCE on this reward). This is the most basic control experiment needed to attribute results to the proposed mechanism. Without it, the reader cannot determine whether the marginal gain decomposition adds anything over a straightforward REINFORCE baseline.

3. **Theoretical guarantees do not connect to the practical algorithm.** 
   - The DR-submodularity result (Theorem 2, restateDRsub) requires the ε-Bandit SMDP assumption (Definition 9): a nearly deterministic MDP where each state has a unique action leading to it with probability 1−ε, and policies must be horizon-dependent (state-independent). This setting essentially reduces to a bandit and bears little resemblance to the structured environments used in experiments (grid worlds with sensors, continuous control).
   - The curvature result (Proposition 5, restateboundedC) states that "for the policy π obtained via SubPO, it holds that J(π) ≥ (1−c) J(π*)" but provides no argument that SubPO actually converges to such a policy. Since SubPO is a gradient-based method optimizing a non-convex objective, it may stop at any stationary point. The proposition does not connect the algorithm's behavior to the claimed bound — it asserts the bound holds for whatever policy SubPO produces, without algorithmic justification.

### Minor

4. **No statistical reporting in figures.** The paper states it runs "20 runs" on some experiments and "10 environments" to "compute statistical confidence," but the plots as described show only mean curves. Without error bands or confidence intervals, it is impossible to assess the variability or significance of the reported improvements.

5. **No discussion of computational cost of submodular reward evaluation.** Computing submodular functions like mutual information in the Bayesian experiment design task requires matrix operations that scale with the number of visited states. The paper does not discuss this cost, how it affects wall-clock time, or how it might limit scalability in large environments.

6. **Architecture details for non-Markovian policies are unspecified.** The paper mentions that "autoregressive policies (RNNs or transformers) can be used" (footnote p. 8) and refers to SubPOnm as using a non-Markovian policy, but does not specify what architecture was actually used in any of the six experiments. These details are relegated to the appendix.

### Trivial

None.

## Nice-to-Haves

- A comparison of SubPO against standard REINFORCE with total submodular reward F(τ) as return (the critical ablation mentioned above).
- Comparison against task-specific submodular optimization methods on each domain (e.g., greedy s-t orienteering for informative path planning, sequential greedy for Bayesian experiment design).
- Error bars / confidence shading on all experimental plots.
- Either remove or honestly caveat the theoretical claims that are not proven for the practical SubPO algorithm (particularly the curvature result, which appears to be a bound on the optimal modular policy rather than on SubPO's behavior).

## Removed Points

- **"Algorithmic novelty is overstated."** The harsh critic claims SubPO is just REINFORCE with a different reward decomposition. The paper presents itself as "a simple policy gradient-based algorithm" and does not claim algorithmic revolution. The marginal gain decomposition, while algebraically straightforward, is a legitimate design choice for the submodular reward setting. This criticism is overblown and removed.
- **"The connection to greedy is rhetorical, not algorithmic."** The paper acknowledges the connection is motivational ("This approach shares similarities with the greedy algorithm"), not a claim that SubPO performs greedy selection. Removed as misreading the paper's rhetorical framing.
- **Missing related works.** Removed per instructions (I cannot verify existence of unmentioned works).
- **Formatting/style nitpicks** (typos, missing theorem numbers, etc.). Removed per instructions (these are parser artifacts, not author errors).
- **Reproducibility concerns about hyperparameters/architecture details in appendix.** Removed per instructions (these sections are stripped by the parser).
- **"The paper claims sample efficiency and scalability without evidence."** The experiments do demonstrate scaling to continuous control tasks (Car Racing, MuJoCo Ant) and the plots show faster convergence in epochs vs MRL on some tasks. This is partial evidence; the claim is somewhat aspirational but not baseless. Downgraded to minor in the main evaluation.

## Novel Insights

The reviews surface that the paper's fundamental tension is between its two ambitions. First, establishing submodular RL as a theoretically grounded framework with provable hardness limits — which it succeeds at through Theorem 1. Second, demonstrating a practical algorithm that works well across diverse domains — which it fails to support because the experiments compare against only a strawman and omit the essential ablation. A genuinely interesting observation is that the building exploration experiment shows SubPOm (Markovian) getting stuck while SubPOnm (history-dependent) succeeds, which is a non-trivial finding about the limitations of Markovian policies under submodular rewards. This finding is undercut, however, by the lack of comparison to any non-learning baseline that could contextualize whether the gap is meaningful.

## Suggestions

1. **Add the standard REINFORCE control.** Compare SubPO against the same policy gradient algorithm using the total submodular reward F(τ) as return (no marginal gain decomposition). This is the single most important experiment to validate the method's claimed advantage.
2. **Add task-appropriate baselines.** For informative path planning, compare against the greedy s-t orienteering algorithm (Chekuri and Pál). For item collection, compare against cardinality-constrained greedy. For Bayesian experiment design, compare against sequential greedy. For coverage/exploration tasks, compare against intrinsic motivation methods (ICM, RND) that are standard in the RL exploration literature.
3. **Either connect the theory to the algorithm or be honest about the gap.** The curvature result (Proposition 5) should either be proved for the actual SubPO procedure or removed/downgraded to a statement about the optimal policy under bounded curvature (not about SubPO's output).
4. **Report error bars on all figures** and state whether runs are independent.
5. **Specify which architecture** (RNN, transformer, or other) was used for SubPOnm in each experiment.

## Score and Decision

**Round 1 bracket.** I queried for topically similar papers in three bands. The weak band (scores 0–3) returned papers like the dynamic pricing paper (3.00) and stability-guarantee RL (2.50), which are clearly weaker than the paper under review — the paper has at least a solid hardness result and a formulated framework. The mid band (4–7) returned the multi-agent submodular coordination paper (6.80), the mini-batch submodular paper (4.67), and the supermodular rank paper (5.00). The strong band (8+) returned papers like the policy gradient for confounded POMDPs (8.00) and the submodular file selection paper (8.00), which are clearly stronger (tight theory, proper baselines, full evaluation). **Initial bracket: [4.5, 6.0].**

**Round 2 narrowing.** I queried inside [4.0, 6.0] and [6.0, 7.5]. The most informative anchors in the [4.0, 6.0] range are the RL coverage path planning paper (4.75) and the general utility RL paper (4.50). The paper under review is slightly stronger than these — it has a more original problem formulation and a non-trivial hardness result — but it is notably weaker than the multi-agent submodular coordination paper (6.80), which has strong theoretical results, proper baseline comparisons, and cleaner experiments. **Final bracket: [4.5, 5.5].**

Positioning within the bracket: The paper's hardness result and problem formulation are genuine contributions that place it above papers that are purely incremental (like the general utility RL paper at 4.50). However, the experimental evaluation is fundamentally insufficient — comparing only against a made-to-fail baseline and missing the critical ablation — which prevents it from reaching the 6+ range where papers typically have at least adequate empirical validation. The paper is closer to the lower end of the bracket, comparable to papers whose theoretical contributions are balanced by weak experiments.

**Final score: 5.0.** The paper has a solid conceptual contribution (problem formulation + hardness result) but the experimental evidence is too weak to support the practical claims, and the theoretical guarantees are disconnected from the algorithm used in practice.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>