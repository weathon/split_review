Now I have a thorough understanding of both the paper and the reviews. Let me construct the final consolidated review.

## Summary

The paper introduces the concept of *reachability* in multi-task RL to explain why exploration improves zero-shot generalization, and proposes **Explore-Go**, a simple method that inserts a pure-exploration phase at the start of each training episode to diversify starting states. The central claim is that generalization benefits come from training on more reachable *tasks* (via starting-state diversity), not from increased state-coverage exploration per se. Experiments in a Four Rooms grid world and two DMC environments show that Explore-Go outperforms standard baselines and a temporally equalized exploration (TEE) baseline that explores more states but generalizes worse.

## Strengths

1. **Reachability as a conceptual lens for multi-task RL generalization.** The paper formally distinguishes reachable from unreachable tasks (Definition 1) and argues, via an intuitive CMDP example (Figure 1) and a data-augmentation analogy (Section 3.3), that training on more reachable tasks—not indiscriminate state coverage—drives generalization. This provides useful vocabulary and framing for a growing area of research.

2. **Convincing empirical demonstration that Explore-Go (starting-state diversity) beats state-coverage exploration in Four Rooms.** The TEE comparison (Figures 4–6) is the paper's key evidence: DQN+TEE explores **more** state-action pairs, maintains **higher** buffer diversity, and is optimal on **more** reachable states, yet Explore-Go generalizes substantially better to both reachable and unreachable test tasks. This directly supports the paper's core claim about *when* vs *how much* exploration matters.

3. **Simple, broadly applicable procedure.** Explore-Go only modifies the episode start by prepending a uniform-random exploration phase, making it compatible with both on-policy and off-policy algorithms (PPO, DQN, SAC). The paper shows consistent improvement across all three in Four Rooms (Figure 3).

4. **Scales beyond discrete grid worlds.** Explore-Go shows positive results on continuous control tasks (Finger Turn, Reacher) from the DeepMind Control Suite with both state-based and image-based observations (Figures 7–8), demonstrating the method is not limited to tabular or discrete settings.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-experiment mismatch: the Four Rooms environment violates the modeling assumption underlying the reachability analysis.**  
   Section 3 assumes that tasks differ *only* in their starting-state distributions ("two tasks that *behave* the same are *represented* the same"). However, in the Four Rooms environment (Section 5.1), tasks differ in doorway positions and goal locations—i.e., they have different transition dynamics and reward functions. The paper does not acknowledge this gap or discuss how it affects the theoretical claims. A state (agent position) that is reachable under one doorway configuration may have entirely different dynamics or be impossible under another. The operational definition of reachability in this environment ("same doorway and goal configuration as a training task") is a reasonable heuristic but does not cleanly follow from Definition 1, which is defined in terms of states being reachable *within* a single CMDP. The paper would benefit from either (a) designing an experiment that respects its own assumptions, or (b) explicitly discussing how the theory extends to this setting.

2. **The central claim that "generalisation is about *when* you explore, not *how much*" rests on a single exploration baseline.**  
   The comparison to TEE (with α=0.1) is well-motivated as the most exploratory variant from Jiang et al. (2023), but it is still a single exploration algorithm. Other principled exploration methods—count-based bonuses, RND, ICM, ensemble-based UCB—might exhibit different relationships between state coverage and generalization. The paper frames the conclusion as a general principle but tests only one alternative to Explore-Go. This weakens the generality of the core claim.

3. **The operationalization of "unreachable" generalization in Four Rooms does not follow from the formal definition.**  
   Definition 1 defines unreachable generalization in terms of starting states having zero intersection with the reachable set *Sᵣ* of the training CMDP. But test tasks with different doorway positions have a different state space (the state includes doorways); their starting states are trivially not in the training CMDP's state space at all. The paper conflates two concepts: (i) states within the same MDP that cannot be reached from training starts, and (ii) states belonging to a different MDP (different dynamics). Only (i) fits Definition 1; (ii) requires a separate justification that the paper does not provide.

### Minor

4. **DMC evidence is incomplete and the results are modest.**  
   The paper lists 6 environments that "test for unreachable generalisation" (Reacher, Finger Turn, Manipulator, Stacker, Fish, Swimmer) but reports results for only 2. The paper acknowledges there is "no significant generalisation gap between training and testing" in these environments, making it unclear why they constitute a test of unreachable generalization. The reported gains are modest (Figures 7–8), and the paper does not explain *why* these specific environments test for unreachable generalization (i.e., why certain initial configurations are not reachable from others under the dynamics).

5. **No ablation on the pure exploration length *K*.**  
   The paper uses fixed values (K=60 for Four Rooms, K=200 for DMC) without exploring sensitivity. If K is too small, the method does nothing; if too large, the agent may waste episodes exploring far from the original task. A plot of generalization performance vs. K would significantly strengthen the paper.

6. **No direct task-level optimality metric.**  
   The paper's central distinction is between states and tasks, and the core claim is about solving more reachable *tasks* optimally. However, the optimality metric reported (Figure 6d) measures state-level optimality. A direct task-level metric (e.g., for each possible starting state, whether the policy is optimal from that start) would directly support the claimed distinction.

### Trivial
- The paper does not discuss or quantify the computational overhead of the additional exploration steps per episode.
- The pure exploration policy is always uniform random; the paper does not discuss settings where this may fail (e.g., dead ends, early termination).

## Nice-to-Haves
- Comparison to other principled exploration methods (RND, ICM, count-based bonuses) to strengthen the claim about "when vs. how much."
- Ablation on the pure exploration length *K*.
- Results for all 6 DMC environments listed as testing unreachable generalization, with analysis of why they are unreachable under Definition 1.
- Comparison to reset-controller approaches (Zhu et al., 2020) to isolate whether the benefit comes specifically from starting-state diversity.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *The critic claimed RAD's data augmentation is a confound for Explore-Go's proposed explanation.* This is incorrect: showing that Explore-Go improves on top of RAD (which already applies cropping augmentation) is a *stronger* test, not a confound. The paper's claim is that Explore-Go's starting-state diversity acts as a complementary form of data augmentation.
- *The critic's request for statistical significance tests beyond 95% confidence intervals.* Confidence intervals are standard and adequate for this paper's scope.
- *The critic's note about the paper not acknowledging the theory-experiment gap in the Section-by-Section notes.* This is a restatement of Major weakness #1, not a separate point.

## Novel Insights
None beyond the paper's own contributions. The key insight—that starting-state diversity (increasing reachable tasks) matters more for generalization than state-coverage exploration—is the paper's own contribution, and the reviews do not surface additional novel observations.

## Suggestions
1. **Acknowledge and discuss the theory-experiment gap explicitly.** Add a paragraph explaining that the Four Rooms environment violates the idealized assumption of Section 3, and discuss why the reachability analysis still provides useful intuition (or revise the assumptions to match the experiment).
2. **Add at least one more exploration baseline** (e.g., RND or count-based bonuses) in the Four Rooms comparison to support the claim that the finding generalizes beyond TEE.
3. **Include an ablation on *K*** showing how generalization performance varies with the maximum pure exploration steps.
4. **Either report results for all 6 DMC environments** that supposedly test unreachable generalization, or explicitly explain why only 2 are shown and what the other 4 would (or would not) demonstrate.
5. **Add a direct task-level optimality metric** in Four Rooms to support the state-vs-task distinction that is central to the paper's argument.

## Score and Decision

This paper introduces a clear conceptual framework and a simple, effective method that demonstrably improves multi-task RL generalization. The Four Rooms experiments are well-designed and provide compelling evidence for the core comparison (Explore-Go vs. TEE). However, the theoretical claims are weakened by a mismatch between the idealized assumptions and the actual experimental setup, the central "when vs. how much" claim rests on a single baseline, the DMC evidence is incomplete, and several important ablations are missing. The paper makes a genuine contribution but is not yet a complete package. On balance, the positive results and practical utility of Explore-Go warrant acceptance, with the understanding that the authors should address these gaps in a camera-ready revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>