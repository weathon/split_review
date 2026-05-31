Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper identifies a short-horizon bias in goal-conditioned RL methods (GCAC and GCWSL) that use hindsight relabeling, and proposes GCQS — an actor-critic framework that treats relabeled achieved goals as subgoals within a KL-regularized policy improvement scheme. The method generates subgoals without a separate discovery mechanism by using the same policy conditioned on achieved goals as a prior for the desired-goal policy. Empirical results across eight robotic manipulation tasks and four AntMaze tasks show GCQS outperforming or matching several baselines.

## Strengths

1. **Strong empirical demonstration of short-horizon bias.** Figure 2 provides clear histograms across four tasks (FetchReach, FetchPick, HandReach, BlockRotateZ) showing that DDPG+HER and WGCSL updates concentrate overwhelmingly on offsets of 0–10 timesteps, while trajectories reach 50–100 steps. This directly motivates the work and is well-supported.

2. **Novel and parsimonious subgoal generation from relabeled goals.** GCQS uses achieved goals from hindsight relabeling as subgoals without a separate subgoal discovery mechanism (Section 5.2, Equation 14). The prior policy π^prior(a|s,g) = E_{s_g~τ^g'}[π(a|s,s_g)] is a clean way to inject subgoal information into the policy. Figure 6 confirms that GCQS successes concentrate on longer trajectory horizons (e.g., 40–50 steps for FetchReach), directly addressing the identified bias.

3. **Substantial empirical gains across diverse tasks.** Figure 5 shows GCQS consistently achieving higher success rates and faster convergence than eight baselines across all eight robotic tasks. In FetchPick, GCQS reaches ~0.9 success by epoch 5 while DDPG+HER remains below 0.2. The ablation study (Figure 8) isolates the subgoal and Q-BC components, demonstrating that subgoals are the primary driver of gains.

4. **Competitive performance on AntMaze without specialized subgoal planning.** Figure 7 shows GCQS achieving ~0.9 on L-AntMaze (comparable to BEAG and PIG) and competitive results on U-AntMaze, S-AntMaze, and Pi-AntMaze, despite not using a separate subgoal-prediction algorithm.

## Weaknesses

### Fatal

None.

### Major

1. **The derivation of the Q-BC objective (Section 5.1) is mathematically incorrect.** Equation (11) states min D_KL(π∥π_relabel) = min E_{B_r}[log π(a|s,g')]. This is wrong on two counts: (i) D_KL(π∥π_relabel) = E_{a~π}[log π(a) − log π_relabel(a)], so minimizing KL does not reduce to merely maximizing E[log π] — the −log π_relabel term is dropped without justification; (ii) the expectation is taken under the buffer distribution B_r rather than under π's own distribution. The subsequent Lagrangian (12) then adds log π as a separate term to Q. While the resulting Q+log π objective is a known heuristic (properly cited to Fujimoto & Gu, 2021), presenting it as a *derivation* from constrained optimization is algebraically unsound. The paper would be stronger by presenting Q-BC as a heuristic combination of Q-maximization and behavior cloning and justifying it empirically, rather than claiming a principled derivation that does not hold.

2. **Missing SAC+HER baseline.** GCQS uses SAC as its underlying actor-critic ("GCQS integrates the SAC following GCAC," Section 5). The primary baselines (DDPG+HER, MHER, GCSL, WGCSL, GoFar, DWSL) use DDPG or supervised learning. SAC typically outperforms DDPG on continuous control tasks, especially on the MuJoCo/Fetch suite. The ablation study includes "No Subgoals" (SAC+Q-BC) and "No BC-Regularized Q" (SAC+subgoals), but neither is a plain SAC+HER baseline. Without this control, it is difficult to attribute the observed gains entirely to the subgoal or Q-BC components rather than the base-algorithm upgrade. The fact that "No Subgoals" (SAC+Q-BC) also achieves high success rates on several tasks (FetchReach, FetchPick, FetchPush) partially addresses this concern but does not resolve it — a SAC+HER baseline is needed to cleanly decompose the contributions.

### Minor

1. **Theorem 4.1 is a tautology.** The theorem states S(p(I+1)) ≤ S(p(I)) where S(x(K)) = Σ_{k≥K} x_k and p is the probability of selecting a future offset with horizon length i. This simply says the tail probability is non-increasing as the threshold increases — a property that holds for *any* probability distribution and proves nothing specific about GCAC/GCWSL. The empirical evidence in Figure 2 is legitimate and sufficient on its own; the theorem adds no theoretical support. The paper should either remove it or reframe it as a basic observation.

2. **Theorem 5.1's prior is self-referential.** The prior π^prior is defined as E_{s_g~τ^g'}[π(a|s,s_g)] — an expectation of the *same policy being trained*. The KL constraint in (15) therefore enforces that π(·|s,g) stays close to its own subgoal-conditioned average. This is a self-consistency condition rather than a constraint relative to a fixed, independent reference distribution. The bound's first term (R_max√(2η)/(1−γ)) depends on η, which can always be made trivially small by ensuring π doesn't vary with the goal. The bound is not vacuous (similar self-consistency arguments appear in the RL literature), but the paper oversells it as a "performance guarantee" without discussing the limitations of the circular definition.

3. **The novelty claim ("first to leverage relabeled goals as subgoals") is overstated.** The paper acknowledges Chane-Sane et al. (2021) as related work and notes a distinction (state=goal assumption). However, using future achieved goals as subgoals within a goal-conditioned framework is not as unprecedented as claimed. The contribution should be framed in terms of the specific mechanisms (Q-BC + KL-constrained integration) rather than asserting first-in-class status.

4. **Clarity of the phasic goal structure.** The practical implementation of the prior policy (Monte Carlo approximation, number of subgoal samples per update) is deferred to Appendix B.1 (which is not included in the main submission). Sections 5.2 could benefit from a concise pseudocode or a concrete example of how the prior is computed during training.

### Trivial

- Theorem 4.1's notation could be simplified: S(p(I)) is the tail probability; stating it directly would avoid the heavy notation for a trivial fact.
- The paper uses "off-policy actor-critic paradigm such as DQN, DDPG, TD3, and SAC" (Section 3.2) — DQN is not an actor-critic method.

## Nice-to-Haves

- An analysis of sensitivity to the KL hyperparameter β would improve reproducibility.
- A discussion of the computational overhead of the subgoal prior (additional forward passes per update) would be helpful.
- On AntMaze tasks, a comparison against flat SAC+HER (not just subgoal-based methods) would contextualize the results.

## Removed Points

- **Criticism that Theorem 5.1's proof cannot be verified because it is in the appendix.** — Removed per hard rules: the parser strips appendices from all submissions; the proof exists in the original.
- **Criticism about the paper not discussing how the approach differs from "simply averaging action distributions."** — The paper defines the prior explicitly in Equation 14 as the expectation of π(a|s,s_g) over achieved goals, and Equation 15 shows the KL constraint. The distinction is clear from the formalism.
- **Several generic statements from the harsh critic that certain sections "overstate novelty" without specific evidence of where the same mechanism appears in prior work.** — The paper acknowledges Chane-Sane et al. (2021) and explicitly contrasts the state=goal assumption; this is adequate for a conference paper scope claim.
- **Strength Finder strengths about "the problem being important" — generic/superficial.** — Moved here. The paper's value should be judged on its specific claims, not on the importance of the general topic.
- **Strength Finder's strength about Theorem 5.1 being a "theoretical performance guarantee" absent in prior work.** — This conflicts with the verified weakness that the prior is self-referential; weakness wins.
- **Reproducibility nitpicks about undisclosed hyperparameters or implementation details that are not standard to include.** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviewers' critiques align on the key structural issues (flawed derivation, missing baseline) but do not introduce novel analytical perspectives that reframe the work.

## Suggestions

1. **Fix Section 5.1.** Remove the flawed algebraic derivation. Present Q-BC as a heuristic combining Q-maximization with BC regularization on relabeled data, supported by the citation to Fujimoto & Gu (2021). This is honest and does not weaken the method.

2. **Add SAC+HER baseline** to all main experiments. This is non-negotiable to attribute gains to the subgoal and Q-BC components rather than the switch from DDPG to SAC.

3. **Reframe or remove Theorem 4.1.** It is a tautology as stated. The empirical evidence in Figure 2 is strong on its own.

4. **Tone down the novelty claim** regarding being "first" to use relabeled goals as subgoals. Focus on the specific technical novelties (Q-BC integration, KL-constrained subgoal prior) rather than the broad conceptual framing.

## Score and Decision

**Bracketing (Round 1):**
- Weak anchors (<3.5): Goal2FlowNet (3.0), LanGoal (2.0) — clearly weaker than GCQS
- Middle anchors (3.5–7.5): HPO (5.5), Merlin (4.5), SMORe (6.0) — relevant comparison set
- Strong anchors (>7.5): MaestroMotif (7.75), Privileged Sensing Scaffolds (8.5) — clearly stronger

Initial bracket: [4.5, 6.5]

**Narrowing (Round 2):**
- SMORe (6.0, all scores 6, Accept poster): Cleaner theory and execution. GCQS has stronger empirical breadth but flawed derivations and missing control baseline. → GCQS is weaker. Score ~5.0.
- Merlin (4.5, scores 5,3,5,5, Withdrawn/Reject): Weak theory, limited experiments. GCQS has stronger experiments but cleaner baselines. → GCQS is somewhat stronger, but Merlin's weaknesses are less verifiable.
- HPO (5.5, scores 3,6,8,5, Withdrawn/Reject): Similar tier — flawed problem formulation but interesting ideas. GCQS has broader experiments. → Roughly comparable, with HPO benefiting from a more theoretically grounded objective while GCQS has stronger empirical results.
- Integrating Planning (6.25, Accept poster): Cleaner framework but limited to gridworlds. GCQS tackles harder continuous control. → Hard direct comparison; the acceptance shows cleaner execution is rewarded.

Final bracket narrowed to [4.5, 5.5].

**Final score:** 5.0. The paper identifies a real problem and presents an effective solution with strong empirical validation. However, the flawed mathematical derivation in Section 5.1 and the missing SAC+HER baseline are significant weaknesses that, in combination, place the paper marginally below the acceptance threshold. The core idea is sound and the empirical evidence is strong across many tasks, but the presentation overreaches on theoretical rigor and experimental controls.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>