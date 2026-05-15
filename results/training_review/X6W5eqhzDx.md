Now I have a thorough understanding of the paper and can produce the final consolidated review, having verified the harsh critic's claims against the actual paper text.

---

## Summary

This paper introduces the concept of *reachability* to multi-task RL, defining reachable tasks (whose states overlap with training) vs. unreachable tasks (whose states do not). The authors argue that training on more reachable tasks acts as implicit data augmentation and improves generalization even to unreachable tasks. They propose **Explore-Go**, a simple method that prepends a pure-exploration phase to each training episode, thereby increasing the diversity of starting states the agent trains from. Experiments in Four Rooms (with PPO, DQN, SAC) and DeepMind Control Suite (Finger Turn, Reacher) show that Explore-Go improves test generalization while leaving training performance largely intact.

## Strengths

- **Clean conceptual vocabulary (reachable vs. unreachable tasks).** Definition 1 provides a principled way to think about multi-task generalization that goes beyond simple train-test distribution mismatch. It isolates why some test tasks benefit from exploration (reachable: you can encounter their states during training) and others may need a different explanation (unreachable: data augmentation through additional reachable tasks).

- **Explore-Go is simple, algorithm-agnostic, and empirically effective.** The method modifies only the rollout collection procedure (episode-start exploration phase) and demonstrably improves generalization across PPO, DQN, and SAC in Four Rooms (Figure 2), and with SAC/RAD in DMC (Figures 5-7). This practical versatility is a genuine contribution.

- **The TEE comparison yields a non-trivial empirical finding.** Despite TEE exploring more state-action pairs, maintaining a more diverse replay buffer, and achieving optimality in more reachable states (Figures 4a-d), Explore-Go still generalizes better to both reachable and unreachable test tasks (Figure 3). This cleanly demonstrates that "more exploration" is not the same as "better generalization" — an interesting and non-obvious result.

- **Scaling to continuous control with images.** Explore-Go improves performance in DMC environments with both state-based and image-based observations, showing the method is practical beyond discrete grid-worlds and compatible with modern data augmentation (RAD).

## Weaknesses

### Fatal
None.

### Major

- **The paper's central causal claim is supported only by indirect evidence.** The abstract states that training on more reachable tasks "and not the increased exploration, is responsible for the improved generalisation." However, the key experiment (TEE comparison, Figures 3-4) is an *elimination argument*: it shows that more exploration and state-optimality do *not* cause better generalization, and then infers that reachable-task count *must* be the cause. The hypothesized causal variable — the number of reachable starting states from which the agent can solve the task optimally — is never directly manipulated or measured. Concretely, Figure 4d measures per-state optimality, not per-starting-state (task-level) optimality, so even the diagnostic plot is slightly misaligned with the claimed variable. Without an experiment that systematically varies the number of reachable starting states (independent of exploration strategy) and shows a monotonic relationship with generalization, the mechanistic claim remains a well-motivated hypothesis rather than an established finding. The paper would be better served by hedging its language and presenting the mechanism as a plausible explanation supported by convergent indirect evidence.

### Minor

- **The TEE baseline is a simplified version of the method from Jiang et al. (2023).** The paper replaces ensembles+UCB with ε-greedy and different fixed ε values per worker. This is acknowledged in a footnote but limits how directly the results speak to the prior work's claims. A comparison with the original method (or a stronger exploration baseline) would be more conclusive.

- **The DMC experiments do not support the paper's reachability claims.** The paper notes "there appears to be no significant generalisation gap between training and testing in either environment" (line 189). Because both training and testing performance improve together, these results are consistent with Explore-Go simply aiding optimization rather than specifically providing data augmentation through reachable tasks. The DMC experiments demonstrate scalability and practical utility but do not engage with the paper's central theoretical distinction.

- **No verification that DMC test tasks are truly unreachable per Definition 1.** The paper asserts that certain DMC environments "test for unreachable generalisation" but does not verify that the test starting states cannot be reached from training starting states. For continuous control, different initial seeds often lead to overlapping state trajectories, so this should be checked or at least argued more carefully.

- **Missing ablation of the exploration-phase length $K$.** Only one value of $K$ is used per environment ($K=60$ in Four Rooms, $K=200$ in DMC). Since the paper argues that there is a "target accuracy" concern (Section 3.3) where too much exploration can provide incorrect targets, a sweep over $K$ would be informative about whether performance degrades past a certain point and whether the method is robust to this hyperparameter.

- **The ergodicity assumption for unreachable generalization (footnote 2) is not checked.** The paper assumes that unreachable test states cannot transition back into reachable training states, but does not verify this property in any of its environments. For tasks differing only in start states (as the paper assumes), this may often fail in practice.

### Trivial
- The on-policy compatibility argument (Section 4) is technically sound but could be expanded — a sentence or two deriving why a changed start-state distribution preserves the on-policy property would remove any doubt.

## Nice-to-Haves
- A direct experiment manipulating reachable-task count independently (e.g., pre-specifying varied subsets of start states without any exploration phase) would directly test the causal mechanism. This is the natural next step to substantiate the paper's core theoretical claim.
- An ablation of the uniform distribution over $[0, K]$ vs. other schedules (e.g., fixed $K$) would clarify whether the stochasticity matters.
- A brief discussion of when the data augmentation analogy might break down — e.g., when different reachable tasks have conflicting optimal actions — would strengthen the theoretical framing.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"The paper's framework collapses tasks to starting states, severely limiting its theoretical scope"** — REMOVED. The paper explicitly states this as an assumption on lines 40-43 ("To analyse which tasks can generalise to each other, we assume..."). This is a deliberate scope definition, not a hidden flaw. The critic incorrectly frames it as undisclosed.

- **"The justification for why Explore-Go is compatible with on-policy methods is weak"** — REMOVED. The paper's reasoning (line 121: changing the start-state distribution yields on-policy data for a modified MDP) is standard and correct in RL theory. This is not a genuine weakness.

- **"Test on environments where tasks differ beyond starting states"** — REMOVED. The paper explicitly scopes its framework to tasks differing only in starting states. Demanding evaluation outside this scope is not a valid criticism of the paper as written.

- **Several formatting/typo nitpicks** — REMOVED per hard rules (parser artifacts, not author errors).

## Novel Insights

The TEE comparison (Figures 3-4) yields an insight that is genuinely novel and somewhat independent of the paper's own causal narrative: that an agent can explore *more*, cover *more* states, be optimal in *more* reachable states, and yet generalize *worse* than an agent that explores less but structures its exploration at episode starts. This decoupling of exploration *quantity* from generalization *outcome* is non-trivial and suggests that the timing and structure of exploration — not merely its volume — is critical for multi-task generalization. The paper's framing of this as "reachable tasks vs. reachable states" provides a useful vocabulary for this distinction, even if the precise causal mechanism remains a hypothesis.

## Suggestions

1. **Tone down the causal language.** Replace "is responsible for" (abstract) with "is a key factor in" or "we hypothesize is responsible for." The paper's evidence supports a strong correlation and an elimination argument, not direct causation.
2. **Add a direct measure of task-level optimality.** Plot the fraction of starting states (tasks) from which each agent achieves the goal within a time limit, rather than just per-state action optimality. This would align the diagnostic with the claimed mechanism.
3. **Include a $K$ ablation study.** A sweep over different exploration-phase lengths (e.g., $K \in \{0, 20, 60, 100, 200\}$) would reveal whether longer exploration always helps, hurts beyond a point, or plateaus, directly informing the "target accuracy" discussion.
4. **Either verify reachability for DMC test tasks or acknowledge the limitation** that DMC results do not test the reachability theory — they merely demonstrate scalability.

## Score and Decision

The paper introduces a useful conceptual framework (reachable vs. unreachable tasks) and a practical method (Explore-Go) that consistently improves generalization across multiple algorithms and environments. The empirical demonstration is solid, and the TEE comparison yields an interesting finding. However, the paper overclaims on causal mechanism: the central claim that "training on more reachable tasks, not exploration per se, causes improved generalization" is supported only by an elimination argument, not by direct evidence. The paper's contributions (conceptual vocabulary, practical method, non-trivial empirical comparison) are genuine and valuable even if the mechanistic explanation remains a hypothesis. This is a solid paper with a useful method and framework, marred primarily by overclaiming on the causal narrative.

**Score: 6.0** (Clear accept: good paper with solid contributions, but the causal overclaim prevents it from being a top-tier paper. Minor revision can address the overstated claims.)

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>