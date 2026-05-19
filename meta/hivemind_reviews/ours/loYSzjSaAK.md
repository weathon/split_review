## Summary
This paper introduces Submodular RL (SubRL), a framework for sequential decision-making under non-additive, history-dependent rewards with diminishing returns (submodular set functions). The contributions are: (i) an inapproximability result showing SubRL cannot be approximated within any constant factor in general (Theorem 1), (ii) a policy gradient algorithm (SubPO) that uses marginal gains instead of additive rewards, (iii) provable constant-factor guarantees under an ε-Bandit MDP assumption (DR-submodular reduction → (1−1/e) approximation) and under bounded curvature (Proposition 1), and (iv) experiments on six domains including coverage, experiment design, car racing, and MuJoCo Ant.

## Strengths
- **Hardness-of-approximation result (Theorem 1, Section 3).** The paper proves via reduction from submodular orienteering that SubRL cannot be approximated within a constant factor (only within Ω(log^{1−γ} OPT)) even for deterministic MDPs. This establishes fundamental limits and motivates why additional structure is needed for guarantees. This is a clean, non-trivial theoretical result.

- **DR-submodularity reduction for ε-Bandit MDPs (Theorem 2, Section 5).** Under the ε-Bandit SMDP assumption (Definition 1), the paper shows the SubRL objective J(π) becomes monotone DR-submodular over a convex polytope. This formally connects SubRL to continuous submodular optimization, enabling the use of Frank–Wolfe algorithms that achieve the optimal (1−1/e) approximation, and generalizing prior submodular bandit results to a broader class of MDPs.

- **Policy gradient theorem for submodular rewards (Section 4, Eq. 6).** The paper derives an unbiased gradient estimator using marginal gains Δ(s_{j+1}|τ_{0:j}) instead of per-step rewards. This is the first policy gradient formulation for general submodular functions and is the backbone of SubPO, making gradient-based optimization of non-additive objectives feasible. The use of a baseline for variance reduction is also incorporated.

- **Empirical validation across diverse domains.** Experiments span discrete and continuous state-action spaces, deterministic and stochastic dynamics, and tasks including informative path planning, item collection, Bayesian experiment design, building exploration, car racing, and MuJoCo Ant. The results consistently show SubPO outperforming the modular RL baseline, demonstrating the approach is applicable beyond toy settings. The comparison between Markovian and non-Markovian policy variants (SubPO-M vs. SubPO-NM) provides useful insight into when history dependence matters.

## Weaknesses
### Fatal
None.

### Major

- **The curvature-based guarantee (Proposition 1) is stated without sufficient justification linking it to the SubPO algorithm in the main text.** The proposition claims that for a tabular SMDP with bounded curvature c, "the policy π obtained via SubPO" satisfies J(π) ≥ (1−c)J(π*). Classic curvature guarantees (Conforti & Cornuéjols, 1984) apply to greedy algorithms on cardinality-constrained submodular maximization, not to gradient-based methods on MDPs. The proof is deferred to the appendix, and the main text does not sketch the mechanism by which a policy gradient method (Equation 4) — which converges to a stationary point, not necessarily a global optimum — achieves this bound. Without a clear explanation of how SubPO's gradient steps relate to the greedy algorithm whose guarantees depend on curvature, the claim as presented in the main paper appears unsubstantiated. This is the most significant concern about the paper's theoretical contributions. (The proof may be valid in the appendix, but the main text should at minimum sketch the reasoning.)

- **Experimental evaluation relies on a single baseline that is a known straw man.** The only baseline is "modular RL" (MRL), which uses F({s}) as an additive reward — a reduction that is expected to fail on tasks requiring coverage (and indeed does: MRL gets stuck in place in car racing and Ant, repeatedly visits high-density regions in Gorilla coverage). Showing SubPO outperforms MRL is a minimal sanity check, not a convincing validation against reasonable alternatives. Missing comparisons include: (a) a random policy, to establish a lower bound on absolute performance; (b) standard RL with a shaped reward that penalizes revisiting similar states (e.g., a negative reward for visiting states similar to previously visited ones); (c) for the deterministic planning tasks (Gorilla coverage, building exploration), a myopic greedy planner that iteratively selects the next state maximizing marginal gain; (d) for continuous control domains (Ant, Car Racing), PPO or SAC with a standard dense task reward to contextualize whether SubPO learns a reasonable policy in absolute terms. Without these, claims that SubPO "scales to high-dimensional domains" or is "sample efficient" are not adequately supported.

### Minor

- **Theory-experiment disconnect.** The DR-submodularity result (Theorem 2) relies on the ε-Bandit SMDP assumption (state-independent, horizon-dependent policies; near-deterministic transitions). None of the six experimental environments satisfy this assumption — they involve state-dependent dynamics, stochastic transitions, and high-dimensional continuous control. The curvature result (Proposition 1) is claimed for general tabular MDPs but is not empirically validated (no curvature measurement, no tabular experiment where the bound could be checked). Consequently, the theoretical guarantees and experimental settings operate in separate regimes and do not reinforce each other. An experiment on an ε-Bandit-like environment (e.g., a stochastic grid-world with action-specific transitions) validating the (1−1/e) or 1/2 bound would substantially strengthen the paper.

- **The DR-submodular optimization framework requires a down-closed constraint set, but the justification that the relaxed polytope P is down-closed is asserted without elaboration (line 219).** While P = {π^h(a) | 0 ≤ π^h(a) ≤ 1, 0 ≤ ∑_{j≠k} π^h(a_j) ≤ 1} likely is down-closed, a brief justification would improve clarity. Additionally, the paper transitions from this DR-submodular reduction (which uses tabular, horizon-dependent state-independent policies) to claiming that "any gradient-based optimizer can be used... and will result in a 1/2-optimal policy" via Hassani et al. (2017). It should be clarified whether the standard SubPO algorithm (with neural network parameterization and Adam) actually respects the constraints required for this guarantee, or whether the guarantee applies only to the specific Frank–Wolfe variant with tabular policies.

### Trivial
None.

## Suggestions
1. **Restructure the curvature result.** Either provide a sketch of the proof in the main text showing how SubPO's gradient steps achieve the (1−c) bound (e.g., by connecting to a Frank–Wolfe or greedy subroutine under tabular parameterization), or caveat the claim explicitly (e.g., "if SubPO converges to a stationary point, then the stationary point satisfies…").
2. **Add at least two stronger baselines** to the experimental evaluation: (i) a random policy, and (ii) standard RL (PPO) with a dense reward that captures the same objective (e.g., for coverage, a reward that is F({s}) with a small penalty for revisiting previously covered areas, tuned to match the difficulty). For the deterministic planning domains, add a greedy myopic planner baseline.
3. **Include one experiment that validates the DR-submodularity theory.** Design a simple ε-Bandit SMDP (e.g., a stochastic grid world where each action deterministically leads to a specific state with probability 1−ε, with a coverage reward) and compare SubPO's empirical approximation ratio to the predicted (1−1/e) or 1/2 bound.
4. **Clarify the constraint set P** and explicitly verify that it is down-closed. State whether the practical SubPO implementation (with neural network policies and Adam) satisfies the assumptions for the 1/2 guarantee from Hassani et al., or whether that guarantee only holds for the tabular Frank–Wolfe variant.

## Score and Decision

The paper introduces a novel framework with a solid hardness result, a meaningful DR-submodularity connection, and a practical algorithm. However, the paper in its current form has two significant weaknesses that undermine its overall contribution: (1) the curvature-based guarantee appears to claim more than the main text justifies, relying entirely on an appendix we cannot assess, and (2) the experimental evaluation is too weak to substantiate claims about scalability and effectiveness — only a single straw-man baseline is compared against. These issues are fixable with revisions, but in the current form the paper is not ready for acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
