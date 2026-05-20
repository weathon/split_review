Now I have sufficient calibration. Let me write the final consolidated review.

## Summary

This paper introduces *submodular RL* (SubRL), a framework for reinforcement learning where rewards are modeled via submodular set functions that capture diminishing returns based on the history of visited states. The authors propose SubPO, a policy gradient algorithm that replaces additive per-state rewards with marginal gains in the gradient estimator. The paper contributes: (1) an inapproximability result (Theorem 1), showing SubRL is hard to approximate beyond logarithmic factors even for deterministic MDPs; (2) an unbiased gradient estimator using marginal gains (Theorem 2); (3) provable constant-factor guarantees under the ε-Bandit SMDP assumption (Theorem 3) and a curvature-based bound (Proposition 3); and (4) empirical results across six environments (discrete and continuous) demonstrating that SubPO learns effective policies where a naive modular baseline fails.

---

## Strengths

1. **Novel framework (SubRL) and clean algorithmic idea.** The paper is the first to formulate a general framework for RL with submodular reward functions. The core algorithmic idea — replacing additive rewards in the policy gradient with marginal gains of a submodular function (Theorem 2, Eq. 5) — is simple, principled, and well motivated by the success of greedy algorithms in submodular optimization. The gradient estimator is unbiased and accommodates baselines for variance reduction.

2. **Hardness result (Theorem 1).** The paper proves that SubRL is hard to approximate within \(\Omega(\log^{1-\gamma} \text{OPT})\) even for deterministic SMDPs, via a reduction to the submodular orienteering problem (Section 3). This establishes a fundamental theoretical boundary for the framework and justifies the need for approximation algorithms.

3. **Provable guarantees in structured settings.** Theorem 3 shows that under the ε-Bandit SMDP assumption (which generalizes the bandit setting), the objective \(J(\pi)\) becomes monotone DR-submodular, enabling constant-factor \((1-1/e)\) approximations via Frank-Wolfe (Section 5). This connects SubRL to the broader DR-submodular optimization literature and submodular bandits.

4. **Diverse empirical demonstration.** The paper evaluates SubPO across six environments spanning discrete (item collection, building exploration) and continuous (Car Racing, MuJoCo Ant) domains, including real-world motivated tasks (biodiversity monitoring, Bayesian experiment design). The results consistently show that SubPO (using marginal gains) outperforms the modular baseline MODPO (using per-state rewards), and that the Markovian variant SubPO-M often approaches the performance of the non-Markovian SubPO-NM (Figure 3, Figure 5).

---

## Weaknesses

### Fatal

None.

### Major

1. **Experimental baseline is too weak.** The only baseline compared against is MODPO, which uses the *same* policy gradient algorithm but with modular rewards \(F(\{s\})\) — a deliberately simple approach that is expected to fail on submodular tasks. No comparisons are made to standard RL algorithms (e.g., PPO) with reward shaping designed to encourage coverage, or to methods that augment the state with visit counts or other memory. Without such comparisons, the claims of "sample efficiency" and "scalability to high-dimensional state-action spaces" are not convincingly supported. The paper acknowledges that "it is possible to use alternative reward functions to train the car using standard RL" (car racing section) but does not include such baselines. This is the most significant evidential gap.

2. **Missing variance reporting on key experiments.** Figures 5b and 5c (Car Racing, MuJoCo Ant) show learning curves without any error bars, confidence intervals, or shaded regions, making it impossible to assess the statistical significance or variability of the reported improvements. In contrast, the discrete-environment experiments (Figures 3a–3c) do include error bars from 20 runs. The continuous-domain experiments are also the ones where sample efficiency and scalability are claimed, so the lack of variance information undermines those claims.

3. **Proposition 3's connection to SubPO needs clarification.** Proposition 3 states that for a tabular SMDP with bounded curvature \(c\), *the policy \(\pi\) obtained via SubPO* satisfies \(J(\pi) \ge (1-c)J(\pi^*)\). The curvature bound \((1-c)\) is a known approximation ratio for the greedy algorithm in submodular maximization (Conforti & Cornuéjols, 1984; Vondrák, 2010). However, SubPO is a policy gradient algorithm performing local search — it is not the greedy algorithm. The paper does not explain how SubPO's gradient-based updates (which can converge to stationary points) attain this guarantee. The proof is relegated to the appendix (which is stripped from the review copy), but even the main text should provide a high-level argument for why SubPO, rather than the optimal policy, achieves this bound. As written, the proposition appears to claim a global optimality guarantee for a local-search method without sufficient justification.

### Minor

4. **Gap between theory and empirical instantiation.** The provable guarantees (Section 5) are established for tabular policies and the ε-Bandit SMDP setting (a restricted, nearly deterministic MDP with state-independent policies). In contrast, all experiments use neural-network policies on general MDPs with continuous state/action spaces, and the ε-Bandit setting is never instantiated. This disconnect limits the theory's ability to explain the empirical success or guide hyperparameter choices. The paper is transparent about this being "simplified settings," but the gap remains large.

5. **No ablation of the gradient estimator.** The paper proposes the marginal-gain-based estimator (Eq. 5) as its core algorithmic contribution but does not ablate it against, e.g., a direct score-function estimator (Eq. 4) with the same baseline. Such an ablation would demonstrate that the marginal-gain decomposition itself (rather than just having a better baseline or more computation) is responsible for the improvement.

### Trivial

6. **Car Racing metric is not clearly defined.** The Y-axis of Figure 5b is labeled "normalized [0-start & 1-finish]" but the text does not clearly specify how this position-on-track metric is computed or normalized. The corresponding video link is helpful but the paper should define the metric explicitly.

7. **No discussion of computational cost of marginal gains.** The paper does not discuss the cost of evaluating \(F(s|\tau_{0:j})\) at each step. For Bayesian experiment design this requires matrix determinant updates; for coverage functions it requires union-size computation. A brief complexity note would be useful.

---

## Nice-to-Haves

- An ablation comparing SubPO's marginal-gain estimator to the raw score-function estimator (Eq. 4) on a simple environment, to isolate the effect of the decomposition.
- A comparison to an RL baseline with a shaped or count-based exploration bonus (e.g., PPO with a coverage bonus) on the Car Racing and MuJoCo Ant tasks.
- Adding error bars / confidence intervals for the continuous-domain experiments.
- A brief intuitive explanation in the main text of how Proposition 3 connects SubPO's gradient updates to the \((1-c)\) guarantee.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The ε-Bandit SMDP result follows directly from known properties; the novelty is limited."* — This is an opinion about the degree of novelty, not a concrete weakness. The paper's contribution is framing submodular bandits in the RL context; Theorem 3's proof (showing DR-submodularity under the ε-Bandit SMDP) is non-trivial technical work.
- *"Proposition 3 is likely incorrect as stated."* — The proof is in the appendix (stripped from the review copy). Calling it "likely incorrect" is speculation. I have kept a softened version as a Major weakness noting that the connection needs clarification.
- *"Section 3 (Hardness) routine reduction"* — An opinion about difficulty, not a weakness.
- *"No comparison to PPO with recurrent policy"* and *"Missing related works"* — Speculative claims about what the paper should have included.
- *"Code repository lacks permanent DOI"* — The paper provides a live GitHub URL and states the code will be made public. This is sufficient for a submission.
- *"The appendix may specify X but..."* — Speculation about content in a stripped appendix.
- *Formatting/style nitpicks* (typos, notation) — These are parser artifacts, not author errors.
- *Strength Finder strengths about "important problem" and "generic praise"* — Generic statements not backed by specific evidence of execution.

---

## Novel Insights

Beyond the paper's own contributions, the interplay of the two theoretical results (Theorem 1's hardness and Theorem 3's constant-factor guarantee under ε-Bandit SMDP) reveals an interesting phase transition: the difficulty of SubRL is driven not just by submodularity of the reward but by its interaction with the MDP transition structure. When transitions are sufficiently "forgetful" (controlled by ε), the problem becomes tractable with a \((1-1/e)\) guarantee; when transitions encode path constraints (as in the SOP reduction), the problem becomes inapproximable. This suggests that the practical hardness of SubRL instances depends on how much the MDP constrains the set of reachable trajectories — a dimension orthogonal to the reward's curvature — which is not explicitly discussed in the paper but emerges from comparing the results.

---

## Suggestions

1. **Add stronger baselines** — At minimum, compare SubPO-M to PPO with a shaped reward designed to encourage coverage (e.g., a count-based bonus or a distance-weighted coverage reward). On the discrete environments, compare to a Markovian policy with state augmented by a history vector (e.g., visited items). This would substantially strengthen the claim that SubPO's advantage comes from the marginal-gain decomposition rather than from having a reward function that happens to work better.

2. **Clarify Proposition 3** — Either (a) provide a sketch in the main text explaining how SubPO's gradient-based updates attain the \((1-c)\) guarantee (e.g., by connecting to the Frank-Wolfe or greedy algorithm under specific conditions on the tabular parameterization), or (b) explicitly state the additional assumptions required.

3. **Add error bars to all experiments**, especially the continuous-domain ones. Without variance information, the quantitative claims of sample efficiency and scalability are not interpretable.

4. **Include an ablation** comparing the marginal-gain estimator (Eq. 5) to the direct score-function estimator (Eq. 4) with the same baseline structure, on at least one environment.

---

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- *Weak band (avg < 3.5)*: "Action Shapley" (3.0), "Remote RL" (3.0), "Distributional Sobolev RL" (3.0), "Dynamic Pricing" (3.0) — These papers have fundamental flaws (missing baselines, unclear methodology, wrong assumptions). The SubRL paper is substantially stronger.
- *Middle band (3.5–7.5)*: "Multi-Agent Submodular Coordination" (6.8, Spotlight) — strong theory but weak experiments (no error bars, only 5 iterations); "Policy Gradient Subspaces" (6.5, Poster) — purely empirical with moderate novelty; "Combinatorial Online Prediction" (4.75, Reject) — limited by weak experiments.
- *Strong band (avg > 7.5)*: "Confounded POMDPs" (8.0, Poster), "Submodular File Selection" (8.0, Oral) — rigorous theory or extensive experiments with clear claims.

**Round 1 bracket: between 5.0 and 7.0.**

**Round 2 (Narrowing within bracket, scores 4.5–7.5):**
- "Integrating Planning and Deep RL" (6.25, Poster) — solid framework integrating planning and RL, comparisons to multiple baselines. The SubRL paper has more novelty but weaker baselines.
- "Policy-Gradient for Imperfect-Info Games" (6.25, Poster) — strong theoretical analysis of policy gradient in game settings. SubRL has broader empirical scope.
- "Learning Policy Committees" (5.75, Reject) — interesting problem but limited by weak experiments. SubRL has stronger empirical results.
- "Self-Adaptive Reward Shaping" (6.50, Poster) — practical algorithm with thorough experiments. SubRL has comparable empirical breadth but weaker baselines.

**Comparative Assessment:** The SubRL paper is most comparable to the Multi-Agent Submodular Coordination paper (6.8, Spotlight) in terms of combining submodular optimization theory with RL/bandits, but the experiments in SubRL are less rigorous (only one baseline, missing error bars on key plots). It is stronger than purely empirical papers (Policy Gradient Subspaces) and papers with fundamental methodological gaps (3-range papers). However, the weak baseline comparison and the unclarified Proposition 3 prevent it from reaching the 7+ range.

**Final Score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>