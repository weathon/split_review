## Summary

This paper introduces a reachability framework for multi-task RL generalization, distinguishing between *reachable tasks* (whose states can be encountered during training) and *unreachable tasks* (whose states cannot). The authors argue that what improves generalization is not the *volume* of exploration but the number of *reachable tasks* the agent is trained on, via an implicit data augmentation effect. They propose Explore-Go, a simple method that prepends a pure-exploration phase (uniform random actions) at the start of each episode, shifting the agent's starting state distribution to cover more reachable tasks, then resumes normal learning. Experiments in Four Rooms (Minigrid) with PPO, DQN, and SAC, and two DeepMind Control Suite tasks (Finger Turn, Reacher) support the core claim.

## Strengths

- **Formal reachability framework with a testable dissociation.** The paper provides clear definitions of reachable/unreachable states and tasks (Definition 1, Section 3.1). This framework generates the specific, testable prediction that *when* exploration happens matters more than *how much*. The controlled experiment in Section 5.2 (Figures 3–4) directly tests this: TEE explores more states, maintains a more diverse replay buffer, and achieves optimality on more reachable states — yet generalizes *worse* than Explore-Go on both reachable and unreachable test sets. This is clean, compelling evidence for the paper's central claim.

- **Explore-Go works across three algorithm families with a principled on-policy justification.** The method is demonstrated with PPO (on-policy, policy-based), DQN (off-policy, value-based), and SAC (off-policy, policy-based) in Four Rooms (Figure 2). The paper provides a principled argument (Section 4, lines 121–122) for why on-policy methods remain valid: Explore-Go only modifies the starting-state distribution, so on-policy data remains on-policy for the modified MDP. This is a concrete advantage over prior TEE-based approaches noted to require off-policy algorithms.

- **Clean, well-controlled baseline comparison.** The TEE comparison uses α=0.1, selected via sweep as the most exploratory variant (line 142), making it a stringent upper-bound comparator. The additional diagnostic metrics (state-action coverage, buffer diversity, policy optimality on reachable states in Figure 4) provide mechanistic insight into *why* TEE underperforms despite exploring more — precisely supporting the paper's theoretical argument about correct targets (Section 3.2).

- **Scales beyond grid worlds.** The method is demonstrated on continuous control (DMC Finger Turn, Reacher) with both state-based and image-based observations (Figures 5–6), providing evidence that the approach is not limited to discrete environments.

## Weaknesses

### Major

- **The DMC experiments do not convincingly demonstrate improved generalization.** The paper acknowledges (line 189) that "there appears to be no significant generalisation gap between training and testing in either environment." When train and test performance track each other closely, improved test performance may reflect improved task performance that happens to transfer, rather than improved generalization to a meaningfully harder distribution. This weakens the claim that Explore-Go "scales" generalization improvement to more complex settings. The primary evidence for the paper's core claim therefore rests almost entirely on the Four Rooms grid world (one environment). While the DMC results are not harmful — they show the method works in continuous control — they do not strengthen the generalization argument.

### Minor

- **No ablation or sensitivity analysis of K (maximum exploration steps).** The paper uses K=60 for Four Rooms and K=200 for DMC without any study of how performance varies with K. Since the entire mechanism depends on shifting the starting-state distribution, the sensitivity to this shift magnitude is a natural and important question. This is the single most straightforward ablation that would strengthen the paper.

- **No empirical comparison to Zhu et al. (2020),** which learns a reset controller to increase start-state diversity for the same underlying purpose. The paper discusses this approach (line 243) but does not include it as a baseline. Given the close relationship (both methods increase start-state diversity; the difference is how the exploration is performed), this is a notable omission.

- **The reachability assumption limits the framework's scope.** The paper assumes (line 40) that tasks differ only in their starting-state distribution and that the representation φ maps behaviorally equivalent states to the same representation. This is a strong assumption that excludes many interesting generalization problems (e.g., sim-to-real with differing dynamics, visual domain adaptation, multi-goal RL with differing reward functions). While the paper is transparent about this assumption, it means the conceptual framework does not straightforwardly extend to the settings that many multi-task RL papers target.

- **The image-based DMC experiments compare only to RAD.** The image experiments (Figure 6) compare Explore-Go+RAD to RAD alone. Other standard image-based data augmentation baselines for DMC (DrQ, CURL, SODA) are not included. This limits the strength of the claim that Explore-Go improves generalization with images.

- **DMC experiment setup is underspecified.** The number of training seeds and test seeds used to define the ZSPT training set is not stated. The paper mentions six DMC environments that test unreachable generalization but only evaluates two (Finger Turn, Reacher), without explaining why the other four (Manipulator, Stacker, Fish, Swimmer) were excluded.

### Trivial

- None beyond standard formatting artifacts that are parser issues rather than author errors.

## Nice-to-Haves

- A controlled experiment equalizing the total number of exploratory steps between Explore-Go and a continuous-exploration baseline (or within Explore-Go itself) while varying only the *timing* of exploration would sharpen the "when vs. how much" claim beyond what the current TEE comparison provides.
- Testing on a benchmark with a known, large generalization gap (e.g., Procgen or a more challenging Minigrid configuration) would substantially strengthen the empirical case.

## Removed Points

These points are flagged per the filtering rules; they are removed from the main Weaknesses section with justification:

1. *"TEE comparison does not support the 'tasks vs. states' conclusion because both methods explore."* — **Removed: misreads the paper.** The paper's claim is precisely that *timing* (when) matters more than *quantity* (how much). The evidence (TEE explores more states, has higher buffer diversity, achieves optimality on more reachable states, but generalizes worse) directly supports this claim. The critic conflates "does more exploration" (measured empirically as state-action coverage, buffer diversity) with "the structure of exploration" — precisely the dissociation the paper establishes.

2. *"The conceptual contribution (reachability) is largely definitional and does not generate testable predictions."* — **Removed: opinion, not a concrete weakness.** The definitions generate specific testable predictions (e.g., TEE underperforms because exploratory states lack correct targets; training on more reachable tasks improves generalization via data augmentation). These predictions are tested in the experiments.

3. *"The paper claims to outperform 'the approach of Jiang et al.' but uses a simplified TEE reimplementation."* — **Removed: overstates the claim.** The paper explicitly states (line 138) that it uses ε-greedy instead of ensembles+distributional RL+UCB because ε-greedy works well in Four Rooms. It is comparing to the *idea* of temporally equalized exploration (continued exploration throughout training), not to the full system of Jiang et al.

4. *Various formatting, reproducibility nitpicks, speculation about missing appendix content.* — Removed per filtering rules (parser artifacts, missing appendix content assumed present in original submission).

## Novel Insights

None beyond the paper's own contributions. The key insight — that the timing of exploration and the number of reachable tasks solved optimally matters more than exploration volume — is already clearly stated and defended in the paper.

## Suggestions

1. Add an ablation of K (maximum exploration steps) in Four Rooms to show how the effect depends on the magnitude of the start-state distribution shift.
2. Include an empirical comparison to Zhu et al. (2020) (or a simple reset-controller baseline) to directly address the closest related method.
3. Add a sentence specifying the exact number of training and test seeds used in the DMC experiments.
4. Consider testing on an environment where the generalization gap between train and test is known to be large (e.g., Procgen or a harder Minigrid configuration) to strengthen the claim about generalization improvement.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>