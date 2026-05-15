Now I have thoroughly analyzed the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

The paper introduces Reward Adaptation (RA), where an agent learns a target behavior by reusing source behaviors learned under different (but related) reward functions. Assuming the target reward is a positive-coefficient polynomial of source rewards, the authors propose Q-Manipulation: using source Q* and Q^μ values to compute upper/lower bounds on the target Q-function, then pruning actions whose upper bound falls below another action's lower bound. A reward-shaping step tightens the bounds via linear programming. The paper claims these bounds preserve optimality (Theorem 2) and that pruning yields guaranteed sample-complexity improvements. Experiments on grid-world domains (16–49 states) and auto-generated MDPs (up to 100 states) show 7.8–42.7% action pruning with faster convergence than Q-learning, Q-Decomposition, and reward-shaping baselines.

## Strengths

- **Well-posed problem formulation**: The paper provides clean mathematical definitions for Reward Adaptation (Definition 1) and its Q-variant version (Definition 2), carving out a distinctive niche at the intersection of transfer learning, modular RL, and multi-objective RL. The motivation (e.g., composing "fast" and "safe" driving behaviors) is clear and practically relevant.

- **Creative use of Q^μ**: The idea of leveraging both the optimal Q-function *and* the worst-case Q-function (Q^μ, linked to Q* under negated reward via Lemma 1) to obtain two-sided bounds is genuinely inventive. Most prior work uses only Q*.

- **Reward shaping for bound tightening**: The application of potential-based reward shaping (Lemma 5) to *reduce the distance between bounds*—rather than to guide exploration—is a clever technical twist. The linear programming formulation for choosing the shaping potential is sensible.

- **Honest discussion of limitations**: Section 5 openly acknowledges the linear programming bottleneck, the need for Q^μ during training, and the shared state-action space assumption. This transparency strengthens the paper's scientific rigor.

- **Empirical breadth**: The evaluation spans three simulation domains (Dollar-Euro, Frozen Lake, Race Track) plus six auto-generated MDPs, covering both linear and non-linear target reward forms, and an approximation-noise analysis (Figure 5). The convergence improvements are consistent across settings.

## Weaknesses

### Fatal

1. **The polynomial bounds (Lemmas 2, 3, Theorem 1) are not generally valid for stochastic MDPs, invalidating the optimality guarantee.**  

   Lemma 2 claims that for non-negative reward R and m ≥ 1:  
   **Q_R^{*m}(s,a) ≥ Q_{R^m}^*(s,a)**  
   where Q_R^*(s,a) = max_π E[∑ γ^t R(s_t,a_t) | s,a,π] and Q_R^{*m} = (Q_R^*)^m.

   **Why this fails**: The Q-value involves an expectation over stochastic trajectories. For a fixed policy π, by Jensen's inequality (x^m is convex for m≥1):  
   (E_π[∑ R_t])^m ≤ E_π[(∑ R_t)^m].  
   Meanwhile, Q_{R^m}^* corresponds to E_π[∑ R_t^m] (under the optimal policy for R^m).  
   For each trajectory, (∑ R_t)^m ≥ ∑ R_t^m holds (non-negative numbers), but this gives E_π[(∑ R_t)^m] ≥ E_π[∑ R_t^m].  
   These two inequalities point in opposite directions, and no general inequality guarantees (E_π[∑ R_t])^m ≥ E_π[∑ R_t^m].

   **Concrete counterexample** (within the paper's own MDP framework, R:S×A→ℝ deterministic, stochastic transitions):  
   From state s, under policy π₁: with probability 0.6 the trajectory yields rewards [4,0] (absorbing), with probability 0.4 yields [0,1] (absorbing). Under policy π₂: deterministically yields [3,0].  
   - Q_R^* = max(E[∑R|π₁], E[∑R|π₂]) = max(2.8, 3) = 3 (π₂ optimal for R).  
   - Q_R^{*2} = 3² = 9.  
   - Q_{R²}^* = max(E[∑R²|π₁], E[∑R²|π₂]) = max(10, 9) = 10 (π₁ optimal for R²).  
   - **9 < 10**, contradicting Q_R^{*2} ≥ Q_{R²}^*.  

   The paper's caveat ("assuming the influence of discounting can be safely ignored, e.g., when MDPs with absorbing states are considered") does not resolve this, as the counterexample uses no discounting (γ=1) and an absorbing MDP.

   **Consequences**:  
   - The "upper bound" ℚ_ℛ^* can be *lower* than the true Q_ℛ^*.  
   - The "lower bound" ℚ_ℛ^μ can be *higher* than the true Q_ℛ^μ.  
   - Action pruning may therefore remove optimal actions.  
   - Theorem 2's optimality proof depends on the correctness of these bounds (line 169: Q^μ ≥ ℚ^μ > ℚ^* ≥ Q^*), so it is unsupported.  
   - The claimed sample-complexity improvement is not guaranteed.

   *Note on the harsh critic's specific counterexample*: That example uses a stochastic reward at a given (s,a), which departs from the paper's definition R:S×A→ℝ (deterministic per-state-action reward). The counterexample above uses only deterministic per-step rewards with stochastic transitions, which is fully within the paper's framework, and demonstrates the same logical flaw. The mathematical issue is real.

   The linear case (Lemma 4) is not affected by this problem and remains correct.

### Major

2. **The evaluation never verifies that pruned actions are actually suboptimal under the target reward.**  
   The paper reports only the *percentage* of actions pruned and convergence speed. It never compares the final policy learned after pruning against the true optimal policy (obtained, e.g., by exhaustive Q-learning on the target domain). Given the theoretical flaw in the bounds (point 1), this empirical gap is critical: if optimal actions are being pruned, the convergence speedup is achieved at the cost of optimality, undermining the paper's central claim. The heat maps (Figures 2, 4) show *where* pruning occurs but not whether the pruned actions are *correctly* identified as suboptimal.

3. **Unfair comparison to baselines that lack the same prior information.**  
   Q-Manipulation has access to pre-trained Q* and Q^μ (or Q*_{-R}) for all source domains. The baselines (Q-learning, Q-Decomposition, reward shaping) receive no such pre-trained knowledge. A fair comparison would include baselines that also receive source Q values—for example, initializing target Q-learning with source Q values, or using successor features / transfer learning methods. Without this, the observed improvement cannot be cleanly attributed to the *pruning mechanism* itself; it may simply reflect the extra information Q-Manipulation receives. The paper acknowledges the cost of obtaining Q^μ but does not address this experimental confound.

### Minor

4. **The "discounting can be safely ignored" assumption is not formally justified.**  
   The paper states (line 73) that "the influence of discounting can be safely ignored, e.g., when MDPs with absorbing states are considered," but provides no formal argument or proof. Since the bounds' validity depends on this assumption, a rigorous treatment is needed—especially given that many practical MDPs do not satisfy it cleanly. (Note: even with this assumption, the bounds fail for stochastic MDPs, as shown above.)

5. **The domains used are very small (16–49 states for simulation, up to 100 for auto-generated).**  
   The paper itself flags the linear programming bottleneck as a limitation (Section 5), yet the evaluation never tests scalability beyond 100 states to demonstrate where the bottleneck actually becomes prohibitive. An experiment showing the wall-clock time of the LP step as state/action space grows would make the limitation concrete.

### Trivial
- None that survive the filtering rules.

## Nice-to-Haves

- Restricting the method to the provably correct linear case (Lemma 4) and presenting the polynomial extension as a heuristic with empirical validation (but without claiming guaranteed optimality).
- A baseline initialized with source Q values (e.g., Q-learning initialized with max or average of source Q*) to isolate the pruning benefit.
- Post-hoc verification that the final learned policy after pruning matches the true optimal policy for each evaluation domain.

## Removed Points

- **Harsh critic's counterexample using stochastic reward at a given (s,a)**: The paper defines R:S×A→ℝ as a deterministic function, so this specific example is outside the paper's framework. However, the *underlying mathematical issue* is real and is demonstrated above using a proper counterexample within the paper's framework (deterministic per-step rewards, stochastic transitions). The criticism is retained but corrected.
- **"Weakness" about missing comparison to other methods (e.g., successor features, transfer learning)**: The paper defines its scope and baselines clearly; demanding every possible comparison is scope creep. The unfair-baseline point above is narrower and more precise.
- **Strength about "Proof of optimality preservation (Theorem 2)" from the Strength Finder**: This depends on the flawed bounds and cannot be listed as a valid strength. The proof structure is logically coherent *conditional on the bounds*, but since the bounds are incorrect, the theorem is unsupported.
- **Strength about "Derivation of bounds for polynomial reward functions"**: The derivation is attempted, but the result is invalid for stochastic MDPs, so it is not a strength.
- **Strength Finder's point about "Empirical validation" being a core strength**: Partially retained above, but weakened because the experiments never verify the key claim (optimality retention) and use unfair baselines.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an important subtle point: the relationship between (E[∑ R_t])^m and E[∑ R_t^m] in stochastic MDPs is not governed by any simple inequality when m > 1, because Jensen's inequality (convex function) and the trajectory-wise inequality (∑ r_t)^m ≥ ∑ r_t^m pull in opposite directions. This means that bounding Q-functions under polynomial reward transformations via direct manipulation of scalar Q-values is fundamentally more difficult than the linear case (where linearity of expectation provides a clean bound). Future work on this problem would need to confront this difficulty head-on—perhaps by assuming deterministic MDPs, by working with the full return distribution rather than its expectation, or by bounding E[(∑ R_t)^m] instead of (E[∑ R_t])^m.

## Suggestions

1. **Fix or restrict the theory**: Either provide a correct proof of the polynomial bounds (possibly under stronger assumptions, such as deterministic MDPs) or restrict the method to the provably correct linear case (Lemma 4) and present the polynomial extension as a heuristic.
2. **Add a baseline with source knowledge**: Run Q-learning initialized with source Q* values to isolate the contribution of the pruning mechanism from the value of having pre-trained source knowledge.
3. **Verify optimality empirically**: For each evaluation domain, compare the policy learned *with pruning* against the true optimal policy to confirm that no optimal actions were incorrectly removed. This is especially important given the theoretical flaw.
4. **Scale up the evaluation**: Test on larger discrete MDPs (>100 states) to characterize the practical scalability of the linear programming formulation, which the paper itself flags as a bottleneck.

## Score and Decision

The paper introduces an interesting problem and a creative approach, but the core theoretical contribution—the polynomial bounds that underpin the optimality guarantee—is mathematically incorrect for stochastic MDPs. Because the bounds are wrong, Theorem 2's optimality proof is unsupported, and the method could prune optimal actions without detection. The experimental evaluation does not compensate for this gap (it never checks whether pruned actions are truly suboptimal) and uses baselines that confound the benefit of extra source information with the benefit of the pruning mechanism. The linear case (Lemma 4) remains correct, but the paper's claimed contributions extend well beyond it.

A major revision that either fixes the theory or honestly restricts the scope to the linear case (and adjusts claims accordingly) could make this a valuable contribution. In its current form, however, the paper cannot be accepted.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>