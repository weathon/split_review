- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 3, 3
Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper introduces Reward-Extended Differential (RED) reinforcement learning, a framework for solving multiple linear subtasks simultaneously in average-reward MDPs. The core idea is that by exploiting the structure of the average-reward Bellman equation, any subtask satisfying certain linearity/invertibility conditions can be updated using a constant fraction of the standard TD error. The paper proves the RED Theorem, proposes tabular RED TD-learning and RED Q-learning algorithms, and presents a case study on CVaR optimization with two empirical demonstrations.

## Strengths

- **The RED Theorem (Theorem 4.1) and the reward-extended TD error derivation are a genuine theoretical contribution.** The paper formally establishes that for linear subtask functions satisfying Definition 1, subtask estimates can be updated using a constant fraction of the TD error. The derivation from the Bellman equation (Equations 4.2–4.5) is clearly presented and constitutes the paper's main intellectual contribution. (Lines 161–228)

- **The formal definition of a "subtask" (Definition 1) provides principled scope and clarity.** By specifying the required properties (linearity, invertibility, state-action independence), the paper makes precise what kinds of objectives the framework can handle and where its limits lie. This is valuable for future work extending the approach. (Lines 139–146)

- **The CVaR update rule (Equation risk_RED_1) and the empirical demonstration on the two-state "red-pill blue-pill" task show that the framework can, in principle, learn a CVaR-optimizing policy without augmented state-space or bi-level optimization.** Figure 6.2's convergence plots across multiple initial guesses provide some evidence that the method is robust to initialization on this simple task. (Lines 304–312, Figure 6.2)

- **The paper honestly acknowledges its own limitations** in the Discussion section (linear subtask restriction, unichain/communicating assumptions, lack of testing on complex tasks with nonlinear function approximation), which is a mark of scientific integrity. (Lines 348–351)

## Weaknesses

### Major

- **The abstract claims "proven-convergent algorithms" but the proofs for Theorems 4.2 and 4.3 are empty.** The paper states that the RED TD-learning and RED Q-learning algorithms "converge, almost surely" to the correct quantities, but the proof environments at Lines 260–262 and 292–294 contain no content whatsoever. The RED Theorem (4.1) is proven, which establishes that the *update structure* is sound, but convergence of the coupled system (value function, average-reward estimate, and one or more subtask estimates all evolving simultaneously) is not demonstrated. Since the paper's primary methodological claim rests on these algorithms being proven-convergent, this omission is consequential. (Lines 255–262, 287–294)

- **The empirical evaluation is far too thin to support the paper's claims.** (a) No comparisons against any existing CVaR optimization method are provided — not even a simple baseline that discretizes VaR and solves multiple MDPs. The paper cites Xia et al. (2023) and Stanko et al. (2019) as prior work, but offers no quantitative comparison. (b) The two-state "red-pill blue-pill" task is a sanity check; it lacks validation against a ground-truth optimal CVaR policy computed by exhaustive search. (c) The inverted pendulum experiment is explicitly chosen so that the average-reward-optimal and CVaR-optimal policies are identical (Line 317), meaning it cannot differentiate the RED CVaR algorithm from standard Differential Q-learning. The only information this experiment provides is that the RED algorithm does not *prevent* learning a good policy — which is too weak to support claims of effectiveness or of risk-awareness. (d) The paper uses only linear function approximation; there is no evidence about how the method scales to nonlinear approximation or more complex domains. (Lines 315–317)

- **The piecewise-linear extension for CVaR is not rigorously justified.** The paper states that piecewise linear functions "can be handled by applying the above logic for each linear segment separately" (Line 227), but provides no formal proof or derivation. The VaR update rule (Equation risk_RED_1) is stated without a step-by-step derivation from the RED framework — it is presented as fact. Given that the CVaR case study is the paper's only demonstration, this gap in formal justification weakens the contribution. (Lines 227, 304–313)

### Minor

- **The paper demonstrates only one subtask application (CVaR).** While the authors acknowledge this limitation (Line 350), the RED framework's generality would be significantly strengthened by even one additional example (e.g., optimizing a linear combination of mean and variance). As it stands, readers cannot assess whether the framework is broadly applicable or only works for the CVaR case.

### Trivial

- None.

## Nice-to-Haves

- A comparison against a simple baseline that discretizes VaR and solves multiple MDPs, even on the two-state task, would give a meaningful efficiency comparison and demonstrate the advantage of the RED approach.
- An analysis of sensitivity to the step-size parameters η_r and η_{z_i} would improve practical guidance, particularly since the theory likely requires these to be in a specific range.
- Using an environment where the CVaR-optimal and average-reward-optimal policies genuinely conflict (e.g., a risky arm vs. a safe arm) would provide a much stronger test of the risk-awareness claim.

## Removed Points

- The harsh critic's claim that the RED Theorem's derivation "contains a subtle but important omission" (about pulling z_i out of the expectation) is addressed — the paper explicitly states "we used the fact that z_i is independent of the states and actions to pull it out of the expectation" (Line 207). The step is correct under the stated assumptions, and the critic acknowledges this.
- The claim that "no analysis of the sensitivity to the step-size parameters" is a weakness: moved to Nice-to-Haves, as it is not a core flaw.
- The strength finder's claim that "Convergence theorems (Theorems 4.2 and 4.3) establish theoretical rigor" is removed because the proofs are empty, directly contradicting the notion that rigor has been established.
- The strength finder's generic characterizations of the work were filtered; only concrete, evidence-anchored strengths are retained.

## Novel Insights

The reviews surface one observation not emphasized in the paper itself: the coupled dynamics of the RED algorithms (value function, average-reward estimate, and subtask estimates updating simultaneously from the same TD error) is genuinely more complex than the standard Differential TD/Q-learning setting from Wan et al. (2021). In Wan et al., the average-reward estimate directly tracks the TD error with a fixed target interpretation. In RED, the "extended reward" at each step depends on current subtask estimates, which in turn are updated using the same TD error. This creates a system of interdependent stochastic approximations whose convergence analysis is non-trivial. The paper's claim that building on Wan et al.'s proof technique is "sufficient" may be an oversimplification of the technical challenge.

## Suggestions

1. **Provide the convergence proofs for Theorems 4.2 and 4.3** — either in the main text or a clearly referenced appendix. Even a proof sketch would be far preferable to empty proof environments. If the proofs follow straightforwardly from Wan et al. (2021), that should be explained with a clear reduction argument.
2. **Add at least one non-trivial baseline comparison** for the CVaR case study. For the two-state task, a brute-force search over discretized VaR values (solving a standard MDP for each) would establish ground truth and allow comparison of solution quality and convergence speed.
3. **Redesign the second experiment** to use an environment where the CVaR-optimal and average-reward-optimal policies differ, so that the algorithm's risk-awareness can be directly verified.
4. **Provide a step-by-step derivation** of the VaR update rule (Equation risk_RED_1) from the general RED framework, clarifying how the piecewise linear extension is formally justified.
