Now I have all the information I need. Let me compose the final review.

## Summary

This paper introduces **Submodular RL (SubRL)**, a framework for RL with non-additive, history-dependent rewards modelled via submodular set functions that capture diminishing returns. The authors propose **SubPO**, a policy-gradient algorithm that decomposes the trajectory reward into marginal gains and greedily maximizes them. They prove an inapproximability result (hardness up to logarithmic factors), show that under restrictive assumptions SubPO recovers constant-factor guarantees (connecting to DR-submodular optimization), and demonstrate empirical effectiveness across six environments spanning discrete and continuous control.

## Strengths

- **Novel problem formulation.** SubRL formalizes an important and underexplored class of RL problems — optimizing submodular set functions of visited states — that covers applications (coverage control, informative path planning, experiment design) that cannot be naturally expressed with additive Markovian rewards. This is a genuinely useful framing.

- **Clean algorithmic idea.** The marginal-gain decomposition of the trajectory reward (Eq. 13) and its use in a policy-gradient estimator is a simple but effective adaptation of standard REINFORCE to non-additive rewards. The decomposition into per-step marginal gains is well-motivated by the connection to greedy submodular maximization.

- **Empirical breadth across diverse domains.** The paper evaluates on six environments (discrete and continuous, from gorilla nest coverage to MuJoCo Ant locomotion), showing that SubPO outperforms a standard modular-RL baseline. The code and video release is commendable and supports reproducibility.

- **Sample efficiency of Markovian SubPO.** In several environments, the Markovian variant of SubPO matches the performance of the non-Markovian variant while being more sample-efficient — a practically useful finding.

- **Correctness of deterministic Markovian optimality claim.** Though the harsh critic questioned Proposition 2 (restatedetMDP), the claim is mathematically sound: with time-augmented states, the objective J(π) is linear in the policy at each individual state, so an extreme point (deterministic policy) achieves the optimum. The critic's concern about non-linearity of F does not invalidate this argument.

## Weaknesses

### Fatal
None.

### Major

- **Only one baseline in experiments.** The sole comparator is modular RL (standard REINFORCE with per-step reward F({s})), which is the weakest possible baseline and is expected to fail on non-modular objectives. The paper would be substantially stronger with comparisons to: (a) state augmentation (feasible on small discrete problems), (b) reward shaping with novelty bonuses, (c) intrinsic motivation methods, or (d) a variant of SubPO that uses the full trajectory return F(τ) directly instead of marginal gains (to isolate the benefit of the decomposition). Without such baselines, it is unclear whether the improvement comes from the marginal-gain decomposition specifically or simply from using a non-additive reward signal.

- **The ε-Bandit SMDP guarantee (Theorem 2) is on an extremely restrictive setting.** The assumption requires a nearly deterministic MDP where each state has a unique action leading to it with probability 1−ε, and the policy is restricted to be state-independent (only horizon-dependent). This effectively reduces the problem to a submodular bandit with a Markov chain — essentially removing the MDP structure. While the paper explicitly positions this as a "simplified setting," the result does not meaningfully support the claim that SubPO is principled for general SubRL.

- **The curvature bound (Proposition 3) is stated without an explanation of how the algorithm achieves it.** The proposition claims SubPO achieves a (1−c) approximation for tabular SMDPs with bounded curvature, but the main text provides no intuition or argument linking SubPO's marginal-gain updates to this bound. The proof is deferred to the appendix (which is standard), but even a sketch of the mechanism would help readers assess plausibility.

- **Overclaimed contributions.** The conclusion states "first-of-its-kind inapproximability result for SubRL." Given that the inapproximability result relies on a reduction to the submodular orienteering problem (whose proof is entirely in the appendix and could not be verified during review), this language overstates what has been demonstrated in the available text.

### Minor

- **The hardness result is stated as a theorem but only sketched.** The reduction from submodular orienteering to SubRL is described in a single paragraph; the structural mismatch between SOP (budget + goal constraint) and SubRL (fixed horizon, no goal constraint) is not addressed in the main text. While the full proof is in the appendix, a more detailed sketch in the main text would improve clarity.

- **The gradient estimator (Eq. 13), while unbiased, is a straightforward application of the score function to the decomposition F(τ) = Σ Δ(sⱼ₊₁|τ₀:ⱼ).** The "causality" justification is somewhat misleading because Δ(sⱼ₊₁|τ₀:ⱼ) depends on all past actions, so actions at step i affect marginal gains at step j>i through the state trajectory.

- **Building Exploration results show a clear failure of Markovian SubPO** (Figure 5a). The paper honestly acknowledges this, but it undermines the broader claim that marginal-gain optimization suffices with simple Markovian representations.

### Trivial
None.

## Nice-to-Haves

- Adding an ablation that compares SubPO against a variant that replaces marginal gains with the full trajectory return F(τ) would isolate whether the decomposition itself or just the non-additive reward drives performance.
- A sample complexity or convergence analysis for the ε-Bandit case connecting quantitatively to the submodular bandit literature would strengthen the theoretical contribution.
- Learning curves for the Building Exploration environment showing both SubPO variants from the start of training would clarify whether the Markovian version eventually converges or is stuck.

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

- **Harsh Critic's Point 1 (inapproximability reduction invalid):** Removed per hard rule about missing appendix proofs. The full proof is in the appendix (stripped by the parser); the main text cannot be expected to contain the complete reduction. The structural-mismatch concern (goal constraint vs. fixed horizon) is a substantive mathematical question that can only be evaluated with the appendix.
- **Harsh Critic's Point 2 (deterministic policy claim false):** Removed because it is factually incorrect. With time-augmented states, J(π) is linear in π(·|s) for each state s individually (the distribution over trajectories is multilinear, but when all other policy parameters are held fixed, the objective is a linear function of the action distribution at a single state). Thus there exists an optimal deterministic Markovian policy. The critic's argument that non-additive F breaks linearity ignores that expectation over trajectories linearizes the dependence on per-state policy parameters.
- **Harsh Critic's Point 3 (curvature bound missing mechanism):** Removed per hard rule about missing appendix proofs. The proof is in the appendix.
- **Harsh Critic's Section-by-section notes about additive rewards being sufficient:** Removed as this is a strawman — the paper explicitly argues why additive rewards cannot capture the saturation/coverage behavior shown in Figures 1 and 2.
- **Strength Finder's "unbiased policy gradient estimator":** Removed because Eq. 13 is a standard score-function estimator applied to the marginal-gain decomposition; not independently novel.
- **Strength Finder's "optimality of deterministic Markovian policies":** Kept in strengths above as verified correct.
- **Strength Finder's "extensive and reproducible experiments":** Generic; kept as part of the broader empirical breadth strength.

## Novel Insights

The paper's most interesting observation is the *connection between the greedy algorithm for submodular maximization and policy gradient*: by decomposing the trajectory return into marginal gains and using these as per-step "rewards" in a policy gradient estimator, the algorithm naturally inherits the greedy heuristic that drives success in classical submodular optimization. This bridges two previously disconnected literatures and suggests a general recipe for handling non-additive rewards in RL — decompose the reward into increments that respect diminishing returns, then apply standard policy gradient on those increments. The practical finding that Markovian policies augmented with marginal-gain rewards can often match fully history-dependent policies is also noteworthy.

## Suggestions

1. **Add at least two additional baselines** for the discrete environments: (a) state augmentation (binary vector of visited states), and (b) SubPO with the full trajectory return F(τ) rather than marginal gains. This would isolate whether the marginal-gain decomposition specifically is responsible for the improvement.
2. **Provide a sketch of the SOP→SubRL reduction in the main text** to address the structural mismatch concern, even if the full proof is in the appendix.
3. **Tone down the language around the inapproximability result** in the conclusion — the result is claimed as "first-of-its-kind" but cannot be fully verified from the main text alone.
4. **Include a discussion of when Markovian SubPO fails** (as in Building Exploration) and whether this is due to variance, exploration, or an irreducible limitation of Markovian policies for that task.
5. **Clarify the variance-reduction baseline** used in Eq. 13 and whether the modular RL baseline receives an analogous baseline.

## Score and Decision

### Calibration Anchors

- **i8dYPGdB1C** (Multi-Agent Submodular Coordination, avg 6.80, Accept): Stronger theory (tight approximation bounds, communication efficiency analysis) but narrower scope. The present paper has broader problem framing but weaker theoretical grounding.
- **tijmpS9Vy2** (BAMDP Shaping, avg 7.00, Accept): Cleaner theoretical framework with well-justified results. The present paper's theory is less self-contained and less rigorous.
- **S24zdyiWDT** (Inverse RL Hardness, avg 6.00, Reject): Strong sample complexity analysis but rejected due to presentation issues and questionable metrics. The present paper has better empirical validation but weaker theory.
- **Gi5aWK8tOx** (General Utility RL, avg 4.50, Reject): Limited novelty — the MLE occupancy estimation is a known idea. The present paper has more novel problem framing but incomplete validation.
- **1DEEVAl5QX** (Mini-batch Submodular, avg 4.67, Reject): Straightforward algorithmic extension of known techniques. The present paper proposes a more novel framework.
- **ZiF1bJ9K6B** (Learning Coverage Paths, avg 4.75, Reject): Empirical paper with domain-specific contributions. The present paper has broader theoretical and algorithmic scope.

Relative to these anchors, the paper proposes a genuinely novel problem formulation and a clean algorithm, but its theoretical results are either unverifiable (deferred to appendix) or extremely restrictive (ε-Bandit), and the experimental comparison is limited to a single weak baseline. This places it below the clear-accept bar (6.5+) but above papers rejected for limited novelty or trivial contributions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>