Now I have thoroughly verified all claims against the paper. Let me produce the final consolidated review.

## Summary

This paper proposes a distributed scalable actor-critic algorithm for multi-objective multi-agent reinforcement learning (MOMARL). The key innovations are (1) a **graph-truncated Q-function** that approximates the global Q-function using only the κ-hop neighborhood state-action, (2) an **action-averaged Q-function** that further reduces the action dimension to each agent's local action while preserving the policy gradient (Proposition 1 proves equivalence), and (3) a **linear function approximation** that compresses the state to the κ-hop neighborhood. The paper claims 𝒪(1/T) convergence to an ε-Pareto-stationary solution and provides approximation error bounds (Theorem 1) showing exponential decay with κ. Experiments in a robot path planning environment compare against a centralized algorithm and a single-agent MORL baseline.

## Strengths

- **Novel graph-truncated and action-averaged Q-function constructions.** The paper clearly motivates and formalizes how to avoid the exponential explosion of the joint state-action space. The graph-truncated Q-function (Equation 12) limits the relevant information to the κ-hop neighborhood, and the action-averaged Q-function (Equation 16) further removes dependence on neighbor actions. Proposition 1 establishes that using the action-averaged Q-function is equivalent to using the graph-truncated one for policy gradient approximation — this is a genuinely non-trivial theoretical tool that enables fully distributed learning.

- **Rigorous approximation error bounds with exponential decay.** Lemma 3 and Theorem 1 provide explicit bounds of \(\frac{\sqrt{2}R}{(1-\gamma^m)^2}(\gamma^m)^{\kappa+1}\) on the policy-gradient approximation error, rigorously showing that the truncation error shrinks exponentially with the communication radius κ. This gives a principled trade-off between approximation quality and communication cost.

- **Fully distributed design with a clean theoretical framework.** Each agent operates using only its κ-hop neighborhood state and its own action \((s_{\mathcal{N}_i^\kappa}, a_i)\). The three-step design (graph-truncation → action-averaging → linear approximation) is clearly structured and well-motivated.

## Weaknesses

### Fatal
None.

### Major

- **Single-run results without error bars or statistical confidence.** The experimental results (Figures 2 and 3) show only a single trajectory per algorithm. Given the stochasticity of policy gradient methods, single runs provide no information about variance, reliability, or whether the observed advantage over baselines is significant. This is a fundamental gap in empirical methodology that undermines the paper's claims of superiority.

- **Insufficient baselines.** The paper compares against only two alternatives: (a) a centralized algorithm (Algorithm 3) that is too computationally expensive to be a practical competitor, and (b) the single-agent MORL algorithm of Zhou et al. (2024) naively applied to the multi-agent setting by treating all agents as one. No comparisons are made against standard multi-agent RL approaches — even simple baselines like independent Q-learning or independent actor-critic (each agent solving its own MORL problem with its own local reward) or the graph-based multi-agent methods that inspired the truncation approach (e.g., Qu et al., 2020). Without such comparisons, it is unclear whether the complexity of the proposed method is warranted relative to simpler decentralized alternatives.

- **No ablation studies on the core design choices.** The paper's main claims rest on the choice of the neighborhood radius κ, the action-averaged Q-function, and the linear feature approximation. Yet none of these are ablated: κ is fixed at 1 in all experiments, no baseline uses a different Q-function design (e.g., independent Q-learning), and the feature mapping φ_i is never described for the experiments. The reader cannot assess which component drives the reported performance.

### Minor

- **Convergence theorem not verifiable from the main text.** The paper states in the abstract and Section 4 that Algorithm 1 converges to Pareto-stationarity at rate 𝒪(1/T), but the main text contains no statement of the convergence theorem, no sketch of the proof structure, and no discussion of the key lemmas beyond the approximation error bounds. While the full proof is in the appendix (which was stripped by the parser), the main text should at minimum state the theorem and outline the proof architecture so reviewers can assess the claim.

- **Missing experimental details impair reproducibility.** No specific hyperparameter values are reported (learning rates η_w, η_λ, η_θ, batch size B, trajectory length H, number of iterations). The feature mapping φ_i for the linear approximation is not described. The exact size of the state and action spaces is not stated. These omissions make it difficult or impossible to reproduce the experiments.

- **The ξ weight in the graph-truncated Q-function (Equation 12) is defined but its computation is never explained.** The paper defines the graph-truncated Q-function using a conditional visitation distribution \(\xi_{\rho}^{\theta,m}(s_{-\mathcal{N}_i^\kappa}, a_{-\mathcal{N}_i^\kappa} \mid s_{\mathcal{N}_i^\kappa}, a_{\mathcal{N}_i^\kappa})\) that depends on the unknown stationary distribution. The paper then bypasses this via the action-averaged Q-function, but the transition from definition to practical computation should be clarified.

- **Assumption 1 (strictly positive visitation probability for all state-action pairs under any policy) is strong and its implications are not discussed.** The paper cites prior work that makes the same assumption, but for the MOMARL setting with decentralized policies and potentially large state spaces, this assumption is particularly restrictive.

- **Limited scale of experiments.** Experiments use only 6–10 agents in small acyclic networks. Scalability to larger networks (e.g., 50–100 agents) is not demonstrated, which is a concern given that the paper's primary motivation is scalability.

### Trivial

- The paper contains a few minor typographical errors (e.g., "shwn" instead of "shown" on line 293).

## Nice-to-Haves

- A comparison of the Pareto front or hypervolume achieved by the algorithm across multiple runs, rather than just the evolution of individual objective values.
- An analysis of communication cost or wall-clock time scaling with the number of agents, to substantiate the scalability claim quantitatively.
- Variation of the neighborhood radius κ (e.g., κ = 0, 1, 2) to demonstrate the trade-off between approximation error and computational cost, which directly validates the paper's core design principle.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"No comparison of Pareto-stationarity error against a baseline known to achieve it"** — The paper does compare against centralized Algorithm 3 in Figure 2(c), which is described as converging to 0-Pareto-stationarity. The reviewer missed this comparison.
- **"Abstract claim is not supported by small-network experiment"** — The abstract specifically says "as compared to the latest MORL algorithm." The small-network experiment compares against the centralized algorithm, not the MORL algorithm. The abstract's claim applies to the large-network experiment (Figure 3b) where it is supported.
- **"The paper does not discuss why the MORL baseline struggles"** — It does: "the policy gradient in the latest MORL algorithm deviates significantly from 0 due to the excessively large global state-action dimension" (line 305).
- **"The actor gradient is essentially a Monte Carlo estimate, not a critic-based estimate"** — The actor update uses \(\phi_i(s_{\mathcal{N}_i^\kappa,h}^b, a_{i,h}^b)^\top w_{i,t}^m\), which is the linear critic's output, not a Monte Carlo return. This is a standard actor-critic architecture.
- **"Algorithm pseudo-code is missing"** — The parser stripped the algorithm environment; it exists in the original submission as the paper states "given in Algorithm 1."
- **"Missing appendix/proof details"** / parser-stripped content — These are parser artifacts that exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any novel insight that the paper itself does not already articulate.

## Suggestions

1. **Add multiple random seeds (at least 5–10) with error bars or confidence bands** to all experimental figures. This is the single most impactful improvement for the empirical evaluation.
2. **Include at least one multi-agent baseline** that also uses local information — e.g., independent Q-learning where each agent treats its own reward vector with scalarization, or independent actor-critic with local critics. This would demonstrate the value of the graph-truncated and action-averaged design.
3. **Vary κ** (e.g., κ = 0, 1, 2) in at least one experiment to directly validate the exponential decay bound from Theorem 1.
4. **Report all hyperparameters** (learning rates, batch sizes, trajectory lengths, feature construction) in a table, and describe the feature mapping φ_i used in the experiments.
5. **Consider adding at least a paragraph outlining the convergence proof structure** in the main text — the key lemmas, the bias-variance decomposition, and how the MGDA λ-update interacts with the actor update to guarantee Pareto-stationarity.

## Score and Decision

The paper proposes a well-motivated theoretical framework with genuinely novel technical components (graph-truncated Q-function, action-averaged Q-function, equivalence result). The theoretical analysis, assuming correctness, represents a solid contribution to MOMARL. However, the empirical evaluation is substantially under-powered: single-run results without error bars, only two baselines (one impractical, one naively adapted), no ablation studies, and missing experimental details that prevent reproducibility. These are not fatal to the paper's core theoretical contribution, but they severely weaken the empirical claims of superiority. The paper would need significant additional experimental work to meet the bar for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>