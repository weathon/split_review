- Decision: Reject
- Scores: 5, 6, 5

## Merged Review

### Summary
The paper addresses hyperparameter tuning for generalized linear contextual bandits, where theoretical hyperparameter choices (e.g., \(\alpha\) in OFUL) are often conservative and yield poor empirical performance. It proposes a double-layer bandit framework, CDT (Continuous Dynamic Tuning), that treats hyperparameter optimization as a non-stationary continuum-armed bandit. The top layer runs a Zooming Thompson Sampling algorithm with restarts to handle switching environments. The method tunes hyperparameters online without a pre-specified candidate set, achieves sublinear regret, and shows performance improvements on synthetic and real datasets.

### Strengths
- The problem is well motivated in practice – theoretically optimal hyperparameters are often useless in real-world bandit settings.
- The paper introduces a novel algorithm for tuning parameters in a *continuous* parameter space, along with a regret analysis that handles time‑switching Lipschitz bandits.
- Extensive experiments demonstrate performance improvements over existing methods.
- The framework successfully adjusts hyperparameters while maintaining theoretical guarantees (sublinear regret) and shows good empirical results.

### Weaknesses
1. **Missing key baselines** (both theoretical and experimental):  
   - Regret Bound Balancing and Elimination for Model Selection in Bandits and RL.  
   - Syndicated bandits: A framework for auto‑tuning hyper‑parameters in contextual bandit algorithms.  
   The regret bound of CDT is \(\Omega(T^{2/3})\), which is less favorable than the bound provided by Syndicated bandits, and the latter does not require stringent conditions on the problem.

2. **Questionable rationale for Eq.(2) decomposition**:  
   The assumption that “the bandit algorithm is likely to select similar arms if the hyperparameters are close” is not convincing. A non‑oblivious or oblivious adversary can present arms where hyperparameters are similar but the arm features differ considerably. The authors must specify the conditions under which Eq.(2) holds and provide a more plausible justification.

3. **Additional hyper‑parameters in Algorithm 1**:  
   The zooming algorithm introduces extra hyper‑parameters (e.g., epoch size) that are themselves unclear to tune. The suggestion to use an outer EXP3 layer to treat epoch‑size candidates as arms raises further questions about sensitivity to the EXP3 meta‑parameters. Moreover, if the outer EXP3 competes with base algorithms that perform poorly initially but improve later, those base algorithms may be discarded before they reach their good regime – a problem akin to corralling a band of bandits (see https://arxiv.org/abs/1612.06246). How is this addressed?

4. **Fixed‑length epochs vs. adaptive restart**:  
   The use of fixed‑length epochs between restarts seems unnatural; an adaptive schedule (more frequent restarts early, less frequent later) would be more practical. Additionally, why was the case of *piecewise* Lipschitz reward (the parameter space partitioned into clusters, each Lipschitz) not studied, given that discontinuities in the reward as a function of hyperparameters can occur?

5. **Dependence on prior knowledge and practical feasibility**:  
   The meta‑algorithm parameter \(H\) requires prior knowledge of the total horizon \(T\) and \(p_{z,*}\), which does not fully resolve the parameter tuning problem. In practice, \(T\) is often unknown, and adding a third layer of BOB would be needed – likely harming efficiency and imposing constraints (e.g., \(T\) larger than some threshold). Can such a three‑layer algorithm run efficiently and retain good performance?

6. **Theoretical sublinearity vs. experimental optimality**:  
   The theoretical result only provides sublinear regret and does not recover the optimal regret of the base algorithms (e.g., \(\tilde{O}(\sqrt{T})\)). Yet the experiments claim CDT is optimal. This discrepancy is not explained.

7. **Missing runtime comparisons**:  
   The paper claims the algorithm is efficient, but no running‑time comparisons are provided in the experiments. Runtime is crucial in bandit settings; the authors should add such comparisons.

8. **Minor typo**: In the notation, “\top” should be written as “T” (transpose).

**Reviewer disagreement**: Reviewer 2 is slightly more positive (score 6) than Reviewers 1 and 3 (both score 5), particularly recognizing the novelty of the regret analysis and the extensive experiments as clear strengths. The weaknesses above capture concerns raised by all three reviewers.