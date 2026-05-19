- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6
I have now thoroughly read and verified the paper against all reviewer claims. Here is my consolidated review.

---

## Summary

This paper proposes VE (Virtual Experiences), a goal-conditioned RL framework that addresses HER's limitation of restricting goal relabeling to within a single trajectory. VE expands goal relabeling across trajectories, filters virtual goals via a task-probability-density-based curriculum that gradually increases difficulty, and uses a self-supervised subgoal planning method (trained via an Advantage-Weighted Regression-style update) to guide policy learning through subgoal-conditioned imitation. Experiments on MuJoCo AntMaze, Sawyer, and Reacher tasks show substantial improvements over existing methods including PIG, HIGL, RIS, GCSL, and SAC+HER.

## Strengths

1. **Cross-trajectory goal relabeling with a principled curriculum.** The paper identifies that HER's within-trajectory limitation prevents knowledge integration across diverse tasks. The proposed task probability density (Figure 5) demonstrably tracks learning progress and selects increasingly difficult virtual goals, addressing a genuine limitation of prior work. The ablation in Figure 7 (left) showing that a 0.5:0.5 ratio of actual-to-virtual experiences is optimal — and that purely virtual experiences cause failure — confirms the curriculum's necessity.

2. **Self-supervised subgoal planning via an AWR-style update is a novel and validated component.** Applying Advantage-Weighted Regression to high-level policy learning (Section 4.2, Equations 7–8) — comparing the learned subgoal planner's distance against sampled subgoal distances as a self-supervised signal — is a clean design that avoids expensive graph search (unlike PIG/HIGL). The ablation in Figure 7 (right) confirms that learned subgoal planning outperforms random subgoal sampling, and the paper's analysis of why oracle subgoals don't help early in training shows thoughtful diagnostic reasoning.

3. **Compelling evidence for compositional skill integration.** The constrained AntMaze-U experiment (Figure 8) — where the agent trains only on same-side tasks but successfully solves cross-map (unseen) tasks — provides strong evidence that cross-trajectory virtual experiences enable skill composition. This is a nontrivial demonstration of the paper's core claim about integrating knowledge from diverse trajectories.

4. **Thorough ablation of key design choices.** The paper systematically ablates: the ratio of actual-to-virtual experiences, the task-probability-density curriculum vs. random virtual goals, learned subgoals vs. oracle/random subgoals, and the choice of prior policy for imitation learning (soft-updated historical policy). These ablations provide reasonable evidence that each component contributes to the overall performance.

5. **Strong empirical performance including on high-dimensional goal spaces.** VE achieves substantially higher success rates than all baselines across six environments (Figure 4). Notably, VE and RIS are the only methods evaluated on the full 31-dimensional state-space goal space in AntMaze, while PIG, HIGL, and GCSL use simplified 2D coordinate goals. VE also outperforms RIS on the hardest tasks (Figure 6) and succeeds on pixel-based Sawyer tasks where graph-based methods cannot operate.

## Weaknesses

### Fatal
None.

### Major

- **The main AntMaze comparisons use asymmetric goal spaces, weakening the controlled comparison.** The paper acknowledges (Section 5.2) that VE and RIS use a 31-dimensional full-state goal space in AntMaze while PIG, HIGL, and GCSL use simplified 2D coordinate goals. This means the baselines solve a different (arguably simpler-in-some-aspects) problem. While VE using a harder goal space and still outperforming baselines is suggestive, it is not a controlled test of method quality. The paper frames this asymmetry as "highlight[ing] the advantage of VE in handling high-dimensional goal spaces," which is a fair claim for VE's scalability, but the headline performance comparison in Figure 4 conflates the method's effectiveness with the goal-space design choice. A comparison where all methods use the same goal space (either 2D or 31D) would be needed to directly attribute the gains to the proposed algorithmic components.

### Minor

- **The task probability density estimation is underspecified for reproducibility.** Section 4.1 states that a "dedicated buffer B_l" records learned data and that the authors "approximate the learning frequency of tasks during training as their probability density," but the paper does not specify what density estimation technique is used (histogram bins? kernel density estimator? normalizing flow?), how many bins or what bandwidth, or how frequently the density estimate is updated. The filtering thresholds (0.8\bar{e}, 1.2\bar{e}) are described as empirical, and no sensitivity analysis is provided. This makes precise reproduction difficult without the codebase.

- **The ablation against random virtual goals (Figure 7, middle) does not control for filtering vs. curriculum.** The comparison contrasts "screening virtual targets based on task probability density versus randomly sampling virtual goals." If "randomly sampling" means uniform sampling from the replay buffer with no density filter (the most natural reading), then the comparison conflates "having any curriculum" with "using the specific task-probability-density curriculum." A cleaner control would use a different difficulty-based curriculum (e.g., based on goal distance) while still filtering, to isolate the benefit of density-based selection specifically.

- **No analysis of the stability of using the learned value function V for subgoal planning.** The high-level policy's loss (Equations 7–8) uses |V(s,g)| as a distance metric, yet V is the same critic being learned from data that includes virtual experiences whose quality depends on V's accuracy. This is not an unusual dependency in RL, but the paper provides no diagnostic (e.g., does the high-level policy's loss correlate with critic accuracy over time? does the method fail in settings where the critic is poor?). An analysis would build trust in the approach.

- **No algorithmic pseudocode.** Given the number of interacting components (density estimation, virtual goal filtering, high-level policy update with the AWR-style advantage computation, subgoal-conditioned imitation learning), a concise pseudocode listing would substantially improve clarity and reproducibility. The paper relies on textual description and equations that contain notational issues (e.g., the gradient in Equation (8) appears malformed).

### Trivial
- The gradient notation in Equation 8 contains formatting issues that make it hard to parse.
- Minor exposition notes: the target y_t in Equation (2) uses a subscript mismatch with Q_{\beta_k}.

## Nice-to-Haves
- A comparison where VE uses 2D coordinate goals (the baselines' setting) on AntMaze would directly confirm whether VE's advantage persists on an equal footing, strengthening the central empirical claim.
- Reporting wall-clock time or gradient steps per environment interaction would allow a fair cost-benefit comparison with graph-based methods like PIG, which the paper notes have high computational overhead.
- Sensitivity plots for the fixed threshold (0.8\bar{e} / 1.2\bar{e}) and for the number of subgoals k would be useful.

## Removed Points

* **Criticism that the "never experienced" claim is overstated (Critic's Section-by-Section):** Removed because it misreads the paper. The constrained AntMaze-U experiment (Figure 8) trains only on same-side tasks and the agent successfully solves cross-side tasks it never experienced during training — precisely the claimed capability. The critic's interpretation requiring "zero-shot generalization to completely novel task structures" exceeds what the paper asserts.

* **Criticism that the goal space asymmetry "could be driven entirely by this asymmetry" and is a fatal flaw:** Demoted from the critic's "fatal" classification to a Major weakness. The critic's framing that the gap "could be driven entirely by this asymmetry" is poorly reasoned — if anything, a 31D goal space is a harder problem than a 2D goal space (the agent must reach specific joint angles/velocities, not just an (x,y) position). Moreover, VE also outperforms RIS, which uses the same 31D goal space. However, the asymmetry remains a legitimate concern about controlled comparison, so it is retained as a Major weakness with accurate framing.

* **Criticism that the circular dependency in subgoal planning is "critical":** Demoted to Minor. Using the learned value function as a distance metric is standard practice in RL and not unique to this paper. The critic's comparison to RIS using a "separate, explicitly learned distance model" cannot be verified from the paper. The absence of stability analysis is a reasonable but minor concern.

* **Strength Finder claim that VE "substantially outperforms ... even oracle subgoals ('os') in later training stages":** Tempered. The paper states that oracle subgoals do not help much early because tasks are simple, and that "more precise subgoals can significantly expedite the learning." The paper does not explicitly claim that VE outperforms oracle subgoals in later stages, so this specific formulation is removed from the strengths.

* **Formatting/typo nitpicks, missing appendix references, trivial reproducibility concerns, and suggestions to add unrelated methods:** Removed per filtering rules.

## Novel Insights

A genuinely novel observation emerges from the cross-analysis of the two reviews: the paper's self-supervised subgoal planning method (Section 4.2) essentially treats subgoal generation as a form of contrastive learning over the learned value function — it randomly samples candidate subgoals and adjusts the high-level policy toward those that yield shorter value-predicted distances. This framing is not explicit in the paper but suggests an interesting connection to contrastive representation learning methods in RL, where the "positive examples" are implicitly defined by the relative advantage comparison. The paper could potentially strengthen its contribution by making this connection explicit and discussing how the self-supervised signal relates to other contrastive frameworks in the literature.

## Suggestions

1. **Run a controlled comparison on equal goal space.** Adapt VE to use 2D coordinate goals (following the baselines' setting) in AntMaze, or adapt the strongest baseline to 31D goal space with appropriate tuning. Either approach would directly quantify the contribution of the algorithmic components separate from the goal-space design choice.

2. **Specify the density estimation procedure precisely.** Report the exact method (e.g., KDE bandwidth, histogram bin count, or normalizing flow architecture), update schedule, and buffer size for B_l. Include a sensitivity plot for the filtering thresholds (0.8\bar{e}, 1.2\bar{e}).

3. **Add a cleaner ablation for the curriculum.** Compare task-probability-density-based filtering against an alternative curriculum (e.g., selecting virtual goals by increasing Euclidean distance from the state), keeping the filtering procedure otherwise identical. This would isolate the benefit of the density signal from the benefit of having any curriculum at all.

4. **Provide a stability diagnostic for the subgoal planning loop.** Plot the high-level policy's loss alongside the critic's accuracy over training to show whether the self-supervised signal degrades when the critic is inaccurate.

5. **Add a pseudocode algorithm listing.** A single-page algorithmic summary would greatly aid reproducibility given the framework's complexity.
