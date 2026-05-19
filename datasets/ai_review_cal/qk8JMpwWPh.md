- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3
Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces a new problem setting — few-shot inverse reinforcement learning with multi-task data — where an agent must learn a reward function and policy from too few target-task demonstrations by leveraging a larger offline multi-task demonstration dataset. The authors propose MPIRL, which decomposes the reward into two components: (1) a multi-task discriminator that generalizes expert behavior recognition across task variations, and (2) a proximity reward that estimates temporal distance to the expert state distribution to provide denser guidance. Experiments on Maze2D, Block Stacking, and seven FactorWorld manipulation tasks show MPIRL consistently outperforms GAIL, DVD, SQIL, and behavior cloning baselines.

## Strengths

1. **Novel and well-motivated problem formulation.** Section 3 clearly formalizes the few-shot IRL with multi-task dataset setting, distinguishing it from prior meta-IRL (which requires environment access during meta-training) and pure imitation learning (which cannot improve with online interaction). The household robot example in the introduction effectively motivates why this setting is practical.

2. **Two-part reward decomposition is validated as complementary.** The ablation study (Section 6.3, Figure 6a) shows that DISCRIMINATOR-ONLY and PROXIMITY-ONLY each underperform the full method. Qualitative visualizations in Figures 6b–c further demonstrate that the discriminator provides dense coverage across the state space while the proximity reward steers the policy away from unrecoverable regions. This directly supports the paper's central design hypothesis.

3. **Consistent empirical improvement across diverse tasks.** On nine tasks spanning navigation (Maze2D), precise manipulation (Block Stacking), and varied tabletop tasks (7 FactorWorld tasks), MPIRL achieves higher success rates than all baselines, with particularly large margins on challenging tasks (e.g., ~2× improvement over BC in Block Stacking). This breadth of evaluation strengthens the generality claim.

4. **Robustness to multi-task dataset composition.** Figure 5c shows that varying the similarity between multi-task tasks and the target task (SAME-PICK, DIFFERENT ALL, etc.) produces no significant performance difference. This is a practically important finding: the method does not require careful curation of task-aligned data.

5. **Practical pseudo-labeling strategy for proximity reward.** Section 4.2 identifies the degenerate training problem (P predicting itself from recursive relabeling) and proposes a random-sampling + backwards-relabeling solution to stabilize training. This is a non-trivial implementation contribution.

## Weaknesses

### Fatal
None.

### Major

1. **The headline "33% average improvement" claim is not clearly supported.** The abstract and conclusion state "an average 33% success rate improvement over the next best-performing method" without defining how this is computed (mean relative improvement? mean absolute percentage point difference? across which tasks?). The paper shows only three curves in Figure 4 — one aggregated FactorWorld curve instead of per-task results — making it impossible to verify the 33% figure from the reported data. This is the paper's central quantitative claim and it needs a clear definition, a per-task breakdown (in a table), and calculation methodology.

2. **The proximity reward pseudo-labeling mechanism is insufficiently validated.** The method relies on learning a proximity function P(s) that estimates temporal distance to expert states, using pseudo-labels derived from the discriminator and backwards relabeling — but there is no analysis of: (a) what happens during early training when the policy is random and the discriminator is unreliable (will the threshold condition D(s,a) > c_thresh rarely trigger, making pseudo-labels effectively uniform?); (b) sensitivity to the threshold c_thresh and scaling factor λ_prox; (c) whether the learned P(s) actually converges to correct temporal distances (e.g., by comparing against ground-truth distances in a simple environment like Maze2D). Without this verification, a core component of the method is a heuristic of uncertain reliability.

3. **The discriminator input representation is critically underspecified.** Section 4.1 states the discriminator takes "a task demonstration, the current state, and action" as input, but never specifies how a "task demonstration" is encoded — is it a one-hot task ID? A concatenated trajectory? A video? Since the environments are state-based (not pixel-based), the representation choice is non-obvious and directly affects how generalization across task variations works. This is a reproducibility-relevant detail that must be stated.

### Minor

4. **The GAIL baseline likely uses multi-task demonstrations in a disadvantageous way.** The paper states that for GAIL, multi-task demonstrations are used "as additional non-expert samples" (Section 5.2). If multi-task demos contain behaviors similar to the target task (common in multi-task settings), training the discriminator to classify them as "non-expert" weakens the GAIL baseline by pushing the reward landscape in the wrong direction. This may overstate MPIRL's relative advantage over GAIL. The paper should either use GAIL in a fairer configuration or discuss this confound.

5. **The different RL algorithms across baselines introduce a confound.** All online methods use PPO except SQIL which uses SAC (Section 5.2). The paper notes "SQIL converges more quickly and takes longer to run" but this is not a principled justification. RL algorithm choice can significantly affect sample efficiency and final performance, making the SQIL comparison difficult to interpret.

6. **No per-task results are shown for the 7 FactorWorld tasks.** Only an aggregated curve is presented in Figure 4. Individual task curves would enable readers to assess whether MPIRL's improvement is consistent or driven by a subset of tasks. The aggregation also obscures the variance underlying the 33% claim.

### Trivial
None.

## Nice-to-Haves
- A multi-task BC + RL fine-tune baseline (train a BC policy on all multi-task data, then fine-tune with sparse RL on the target task) would help isolate whether the reward function itself is the key contribution versus better policy initialization.
- Comparison against a version of MPIRL with a single-task discriminator (rather than multi-task) + proximity reward would isolate the benefit of multi-task data in the discriminator component.
- Validation of the proximity reward against ground-truth distances in Maze2D would substantially strengthen confidence in the pseudo-labeling mechanism.
- Learning curves for discriminator accuracy and proximity loss during training would help assess training stability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Meta-IRL comparison criticism** (Harsh Critic, Critical Issue 2): The critic claims meta-IRL methods could be applied directly if the multi-task data "has reward labels." However, the paper correctly identifies that meta-IRL methods "require access to multi-task environments or transition functions to train in" (line 38) — they need to interact with environments during meta-training, not just use a static dataset. The paper's setting only provides access to the target task environment. This criticism is factually incorrect about what meta-IRL requires; removed.

- **"DVD with online updates" comparison** (Harsh Critic, Critical Issue 2): The critic claims the paper does not compare against DVD with online updates. However, the ablation study (Section 6.3, DISCRIMINATOR ONLY) effectively does this, and the paper explicitly notes "the addition of an online adversarial objective (see Section 6.3) improves it significantly" (line 152). The distinction is partially addressed; moved here as the concern is overstated.

- **Generic "missing hyperparameters" and "no learning curves for discriminator/proximity loss"** (Harsh Critic, Missing Parts): These are standard requests for greater detail but do not threaten any core claim. The paper states code is submitted as supplementary material (lines 195-198), which would contain these details. Moved here as minor presentation issues rather than substantive weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already discuss.

## Suggestions

1. **Define and break down the 33% claim.** Specify whether this is relative or absolute improvement, list all 9 tasks with per-task success rates in a table, and show the computation. This single fix would substantially strengthen the paper.

2. **Add a validation experiment for the proximity reward.** In Maze2D, compute ground-truth temporal distances (via exhaustive search or simulation) and compare against the learned P(s) at various points during training. This would demonstrate whether the pseudo-labeling strategy converges to the correct quantity.

3. **Clarify the discriminator input representation.** State explicitly how a "task demonstration" is encoded — e.g., "we concatenate the first k=100 state-action pairs of a randomly sampled demonstration trajectory with the current (s,a) and pass the result through an MLP with [architecture]."

4. **Report per-task FactorWorld results.** Show individual success curves or a table of final success rates for all 7 tasks to allow readers to verify the aggregate 33% figure and assess consistency of improvement.

5. **Include a sensitivity analysis for c_thresh and λ_prox.** Even a brief ablation over a few values would help assess whether MPIRL is robust to these hyperparameter choices or fragile.
