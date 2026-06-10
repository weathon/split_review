## Summary

This paper introduces SEQUOIA, an algorithm that combines deep Q-learning with mixed-integer programming (MILP) to handle combinatorial action spaces in restless bandit planning. The Q-network takes the state-action pair as input and is embedded as a MILP whose optimization selects the best action without enumerating the exponential action space. The paper also contributes four new problem formulations (CORMABs) where actions are strongly coupled across arms. Empirically, SEQUOIA outperforms myopic heuristics and an ablated iterative-DQN baseline across these settings.

## Strengths

- **Novel MILP-embedding of a Q-network for combinatorial action selection (Section 4.1, Equations 4–5).** The paper provides a concrete mathematical encoding of a ReLU-activation neural network as a mixed-integer linear program, enabling the argmax over actions without enumerating an exponentially large space. This is the core technical enabler of the approach and is clearly described with references to established methods (Fischetti & Jo, 2018).

- **Four novel CORMAB problem formulations (Section 3, lines 60–84).** The paper introduces multiple interventions, schedule-constrained (bipartite matching), capacity-constrained, and path-constrained restless bandit problems. These are genuinely novel for the RMAB literature and concretely demonstrate settings where standard Whittle-index approaches break down due to coupled actions.

- **Consistent empirical outperformance with a single architecture across diverse settings (Section 5, Figure 3).** SEQUOIA achieves higher reward than all baselines across four problem settings at three scales (J=20,40,100 arms; N=5,10,20 actions), using the same network architecture and training procedure without per-domain tuning (line 164). The SAMPLING heuristic's degradation at scale (from near-myopic at 20 arms to far behind at 100 arms) directly illustrates the need for a structured approach.

- **Warm-starting strategies addressing the MILP computational bottleneck (Section 4.2, lines 135–139).** The paper identifies the computational challenge (640,000 MILP solves for a modest training instance) and proposes three concrete mitigations — myopic reward initialization, myopic-policy seeding, and perturbed/infeasible action diversity — plus memoization. This shows direct engagement with practical feasibility.

## Weaknesses

### Fatal
None.

### Major

- **The baseline comparison is too narrow to support the paper's strong claims.** SEQUOIA is compared against myopic heuristics (MYOPIC, SAMPLING, ITERATIVE MYOPIC), an ablated version of itself (ITERATIVE DQN), and random baselines. No method from the RL or planning literature that handles sequential decision-making with combinatorial action spaces is adapted as a baseline. MCTS-based planning (discussed in the paper's own related work: Silver et al., 2016; Raman et al., 2024) is a natural candidate: it handles sequential planning and can be combined with rollouts or learned value functions over combinatorial action spaces. While MCTS adaptation to CORMAB is non-trivial, its absence means the reader cannot calibrate whether SEQUOIA's gains come from the DQN+MILP idea itself or simply from not being myopic. Furthermore, the headline "28.3% improvement" (abstract) is stated without specifying the reference baseline — it is not clear whether this is relative to the best myopic baseline, the average over baselines, or ITERATIVE DQN — making the number uninterpretable as a general claim. **This does not invalidate the paper's contribution but materially weakens the empirical evidence for its central claim.**

- **No computational cost analysis despite identifying MILP solves as the critical bottleneck.** The paper repeatedly flags the MILP as "extremely expensive" and "the major computational bottleneck" (lines 133, 178), estimating 640,000 solves for a modest training instance. Yet not a single wall-clock time, training-time measurement, or per-step inference cost is reported anywhere. Without this, readers cannot assess the practical trade-off between SEQUOIA and the trivially cheap myopic baselines (which require no training). If SEQUOIA's 28.3% improvement comes at a 100× computational premium, the practical value is very different than if the overhead is modest. This omission is significant for a paper whose method's primary limitation is computational expense.

### Minor

- **No analysis of whether the MILP exploits approximation errors in the Q-network.** The MILP finds actions that *maximize the predicted Q-value*. If the Q-network is poorly calibrated in regions far from the training distribution, the MILP may exploit these errors to find actions that look good to the network but are actually poor — a known failure mode when learned models are used for optimization (optimization-induced distribution shift). The paper does not discuss this risk or provide any analysis (e.g., comparing predicted Q-values against actual returns for MILP-selected actions).

- **Missing details on the sigmoid piecewise linear approximation** (Section 3, line 78). The paper mentions using a piecewise linear approximation of the sigmoid link function for the multiple-interventions setting, but does not report the number of segments used or the approximation accuracy. This matters because the MILP solution quality depends on this approximation.

- **No discussion of MILP solve management.** There is no mention of whether Gurobi is given a time limit, an optimality gap threshold, or any termination criterion during training or inference. Real MILP solves for moderate-size problems may not terminate with the true optimum within reasonable time; how this affects the training signal or inference quality is not discussed.

- **Overclaimed priority on "first" sequential combinatorial setting** (line 23). The paper claims to consider "for the first time sequential combinatorial settings," but MCTS-based approaches (Silver et al., 2016; Raman et al., 2024) address sequential planning with combinatorial action spaces, even if in simpler constraint settings. The paper's contribution does not need this priority claim to stand — DQN+MILP for stochastic MDPs with combinatorial actions is a genuine extension — and overclaiming invites unnecessary scrutiny.

### Trivial
None.

## Nice-to-Haves

- An ablation of the three warm-starting components (myopic initialization, myopic seeding, random perturbation) to quantify each strategy's contribution.
- A table reporting mean rewards and standard errors (or confidence intervals) across the 30 seeds, complementing Figure 3.
- Brief discussion of how the method scales with larger J (e.g., J=500) — the action-input Q-network grows linearly in J, and the MILP size grows with the neural network depth, so a rough scaling estimate would help.

## Removed Points

*These points were raised in the raw reviews but are removed after filtering. They are included for completeness, not as valid criticisms.*

- **Whittle-index baseline suggestion:** The paper explicitly states (line 166) that Whittle relaxations "break down in strongly coupled action settings, our setting here." This suggestion misunderstands the paper's scope.
- **Missing hyperparameter details (learning rate, hidden units, epsilon schedule):** Removed per hard rules — these are nitpicks about reproducibility that do not threaten the core claims.
- **Notation typo in Equation (75):** Removed per hard rules about formatting and typographical artifacts potentially arising from PDF parsing.
- **IPOPT result "undercuts the rationale for using MILP":** The paper presents IPOPT as a future exploration for faster heuristic inference, not as a contradiction of the core method. This criticism over-interprets an exploratory result in the conclusion.
- **"Q-network takes full joint state as input" scaling concern:** This is an inherent property of the problem, not a weakness of the method. The paper does not claim otherwise.
- **Policy gradient with factorized action parameterization:** The critic's suggestion is vague and does not demonstrate a concrete adaptation path for the CORMAB setting with binary action vectors and strong coupling constraints.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear gap between the paper's claims and the evidence provided, and suggest specific remediations (stronger baselines, timing analysis), but do not contribute a novel technical insight beyond what the reviews' meta-assessment provides.

## Suggestions

1. **Add at least one strong baseline from the planning literature** — MCTS with rollouts (using the known transition dynamics) is the most credible candidate. Even if MCTS cannot fully match SEQUOIA's performance, quantifying the gap against a non-myopic planner would significantly strengthen the evaluation.
2. **Report wall-clock times** for both training (total and per-episode) and inference (per-timestep solve time) for SEQUOIA and each baseline, at each problem scale. This is essential for assessing practical viability.
3. **Clarify the 28.3% claim** by specifying the reference baseline and reporting per-setting improvements in a table with standard errors.
4. **Add an analysis of Q-network approximation quality:** compare the Q-value predicted by the network for the MILP-selected action against the Monte Carlo estimate of the actual discounted return from that action, across a set of test states.
5. **Report the number of segments used in the sigmoid piecewise linear approximation** and either its approximation error or a sensitivity analysis.

## Score and Decision

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**