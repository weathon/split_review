Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper introduces the problem of few-shot IRL with multi-task data, where an agent must learn a reward function and policy from only a few demonstrations of a target task (insufficient to cover all task variations) by leveraging a larger offline multi-task demonstration dataset. The proposed method, MPIRL, decomposes the reward into two learned components: (1) a multi-task discriminator trained adversarially to recognize expert behavior across task variations, and (2) a proximity reward that estimates temporal distance to the expert state distribution to provide shaping in non-expert states. Experiments on Maze2D, Block Stacking, and FactorWorld (7 tasks) show competitive results, with an advertised 33% average improvement over the best baseline.

## Strengths

- **Novel problem framing with realistic motivation.** The paper formally defines the few-shot IRL setting with an offline multi-task dataset — a practically motivated scenario (e.g., household robot learning new tasks from few demos while leveraging prior experience) that is not directly addressed by prior meta-IRL or imitation learning work. This framing is concretely described (Section 1) and shapes the method design.

- **Two-part reward decomposition with empirical evidence of complementarity.** The insight of decomposing the reward into a generalization component (discriminator) and a shaping component (proximity) is clean, and the ablation in Figure 6a directly shows that both components are necessary — each alone performs significantly worse than the full method. This is the strongest evidence that the decomposition is a meaningful algorithmic contribution.

- **Systematic analysis of data-condition sensitivity.** Figures 5a–5c study how MPIRL's performance varies with the number of target demos, the number of multi-task tasks, and the task similarity. The finding that performance saturates after ~10 tasks and is insensitive to task similarity (DIFFERENT ALL vs. SAME-PICK) provides practical guidance for data collection and demonstrates robustness.

- **Qualitative visualization of reward components.** Figures 6b and 6c provide visual insight into how the discriminator reward (dense over the maze) and proximity reward (shaped, penalizing hard-to-reach areas) offer complementary signals, supporting the paper's core intuition even when neither component is individually perfect.

## Weaknesses

### Major

**1. The proximity reward training procedure lacks principled justification and its convergence is unverified.**

The proximity function \(P(s)\) is trained via a pseudo-labeling scheme where the target labels are generated from the current \(P(s)\) itself. Specifically, the paper samples a random state \(s_t\) in a trajectory, uses the current network output \(P(s_t)\) as a base, and labels earlier states as \(P(s_t) - \gamma k\) (Section 4.2, Equation 3). The paper acknowledges that direct recursive relabeling leads to degenerate self-prediction, and the proposed fix — random sampling of anchor states — prevents the most obvious collapse. However, no analysis, diagnostic, or ablation is provided showing that this scheme actually converges to a meaningful measure of temporal distance to the expert distribution rather than drifting to a trivial solution. The paper's own admission that "directly relabelling each state recursively... results in degenerate training because the pseudo-labels become too similar to \(P(s)\), causing \(P(s)\) to predict itself" (line 76) confirms the severity of the stability problem, yet the fix is presented with no theoretical grounding or empirical validation that it actually resolves it. This matters because the proximity reward is a core component of the claimed contribution (a "well-shaped reward"), and if this component is not learning anything meaningful, the interpretation of the ablation results and the overall method's success is unclear.

**2. The multi-task discriminator's claimed generalization is asserted but not directly measured.**

A central claim is that the multi-task discriminator "generalizes across task variations" (Section 4.1, line 58). The only direct evidence is a single qualitative heatmap in Maze2D (Figure 6b) showing the discriminator reward is "dense over the entire maze." This does not demonstrate that the discriminator correctly identifies expert behavior on *unseen* task instances — it only shows the reward is not zero everywhere. The paper reports no quantitative evaluation of the discriminator's classification accuracy on held-out target-task variations (e.g., held-out starting positions in Maze2D), nor does it ablate the multi-task data by comparing against a discriminator trained *without* it. Without such evaluation, it is impossible to attribute the method's success to the discriminator's generalization rather than to other factors (e.g., the proximity reward doing most of the shaping work, or the online RL policy simply being robust). Given that the paper's motivation hinges on generalization beyond few target demos, this gap is significant.

**3. The headline "33% improvement" claim cannot be fully verified from the presented data.**

The abstract and conclusion state "an average 33% success rate improvement over the next best-performing method" across "nine tasks over three different simulated environments: Maze2D, Block Stacking, and seven tasks in FactorWorld" (line 139). However, the main results (Figure 4) show only 5 subplots (Maze2D, Block Stacking, and apparently 3 of the 7 FactorWorld tasks). Even for the tasks shown, the improvement is not uniform — in Maze2D, MPIRL and SQIL are essentially tied at convergence. Without seeing results for all 7 FactorWorld tasks (or at least a per-task breakdown), the aggregate 33% figure is unverifiable. This is not merely an appendix issue — the *main paper* does not present the full results that support its headline quantitative claim.

### Minor

- **The GAIL baseline may be disadvantaged by how multi-task data is used.** The paper states: "In our GAIL experiments, we use the multi-task demonstrations as additional non-expert samples" (line 120). Since these multi-task demonstrations are expert trajectories for *their own* tasks, labeling them globally as non-expert likely injects a confusing training signal into GAIL's discriminator. A fairer comparison would either ignore the multi-task data (standard GAIL) or use it in a multi-task-aware manner (as MPIRL does). This may inflate the apparent gap between MPIRL and GAIL.

- **No reporting of computational cost or hyperparameter sensitivity.** The method has multiple components (policy, discriminator, proximity network) trained iteratively, plus a threshold \(c_{thresh}\) and scaling factor \(\lambda_{prox}\). The paper does not report training time, sensitivity to these hyperparameters, or how they were chosen.

### Trivial

- **Terminology inconsistency with \(\gamma\).** The paper calls \(\gamma\) a "discount factor" set "proportional to the episode horizon" (line 67). This is actually a normalizing constant, not a discount factor in the RL sense. The framing is confusing and the variable serves two distinct roles (normalization in Equation 2, step-penalty in the recursive update) without clarification.

## Nice-to-Haves

- A TD-learning reframing of the proximity function as a value function for reward \(-1\) per step until an absorbing expert state (as the reviewer suggests) would be a more principled alternative to the current pseudo-labeling scheme and would connect to established theory.
- Measuring the discriminator's held-out classification accuracy (e.g., precision/recall on unseen variations in Maze2D starting positions) would directly validate the generalization claim.
- Reporting all 7 FactorWorld task results individually (even if deferred to an appendix that reviewers can access) would make the 33% claim verifiable.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic's concern about "the appendix was stripped by the parser" (Point 3):** Removed per the hard rule that the parser strips appendix sections from all papers; these exist in the original submission. However, the core concern about the main paper not showing all 7 FactorWorld results in Figure 4 remains valid and is kept as a Major weakness.
- **Strength Finder's "33% improvement" strength:** Removed because it conflicts with the verified weakness about incomplete result reporting — a headline claim that cannot be fully verified from the presented data should not be listed as a strength.
- **Harsh Critic's detailed "Strengthening the Paper on Its Own Terms" section:** These are constructive suggestions, not weaknesses, and are partly folded into Nice-to-Haves above.
- **Harsh Critic's "Missing Parts and Places to Improve" list items about the appendix:** Removed per the rule about missing appendix content being a parser artifact.
- **Strength Finder's generic phrasing about "addressed an important problem"** — none found; all listed strengths have specific content backing them.

## Novel Insights

None beyond the paper's own contributions. The reviews surface two structural concerns (unprincipled proximity training and unmeasured discriminator generalization) that are legitimate but do not add new analytical insight beyond what a careful reader of the paper would notice.

## Suggestions

1. Reframe the proximity reward training as TD(0) with reward \(-1\) per step and expert states as absorbing — this is theoretically sound and avoids the current circular pseudo-labeling concern. At minimum, provide diagnostic plots showing that \(P(s)\) converges to a meaningful distance metric.
2. Add a direct quantitative evaluation of the discriminator's generalization: train the multi-task discriminator (without proximity reward) and measure its classification accuracy on held-out target-task variations (e.g., held-out starting positions in Maze2D).
3. Present the per-task breakdown of all 7 FactorWorld results (either in the main paper or in an appendix that is accessible for review) so the 33% aggregate claim can be verified.
4. Revisit the GAIL baseline: either run it without multi-task data (standard GAIL) or clearly explain why the multi-task-as-negative setup is fair.

## Score and Decision

The paper tackles a meaningful problem and the two-part reward decomposition is a sensible design that ablation validates. However, three major weaknesses collectively undermine the paper's strongest claims: (a) the proximity reward training scheme is not justified and its convergence is unexamined, (b) the discriminator's claimed generalization is asserted without direct measurement, and (c) the headline 33% improvement claim is not fully verifiable from the data presented in the main paper. These are not fatal individually but together they leave the paper's core contributions inadequately supported. A substantially revised version addressing these issues — particularly the proximity learning scheme and discriminator evaluation — would be significantly stronger.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>