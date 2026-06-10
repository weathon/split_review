## Summary

MuJoCo Manipulus is a simulation benchmark of 16 tool manipulation tasks (14 tools across 8 categories) built on MuJoCo with Gymnasium API integration. The paper provides baseline results from three model-free RL algorithms (CrossQ, SAC, PPO) across all tasks and identifies that current methods leave substantial room for improvement on tool manipulation. The benchmark fills a genuine gap: while general manipulation benchmarks exist, none specialize in tool manipulation at this scale.

## Strengths

- **First benchmark specialized for tool manipulation at meaningful scale**: The paper correctly identifies that existing benchmarks (ManiSkill2, Robosuite, RLBench) include some tool-adjacent tasks but none provide a dedicated, diverse suite of tool manipulation tasks. With 16 tasks across 8 categories using 14 tools, this substantially exceeds related work such as Wang et al. (2024) which provides only 4 tasks. The comparison in Table 1 and discussion in Section 2.2 make this case clearly.

- **Practical engineering that lowers the adoption barrier**: The Gymnasium API integration, single-file task implementations (Section 3.1, line 75), and fast wall-clock times (10 min for 100K steps, 30 min for 300K steps on RTX 4090, line 139) are genuine practical contributions that make the benchmark useful for rapid RL research iteration.

- **Generalized dense reward design across tool variants**: The paper designs reward functions using markers and goal positions that generalize across in-category tool variants (e.g., PourCup, PourMug, PourPan, PourPot, PourBowl all use the same reward structure despite different geometries) (Section 3.1, lines 76-77). This is a non-trivial engineering contribution.

- **Identifies a non-obvious failure mode**: The experiments reveal that CrossQ overfits to high-reward states encountered early in training while SAC and PPO avoid this on the same tasks (Section 4.2, line 138), providing concrete direction for future algorithm research.

## Weaknesses

### Fatal

None.

### Major

- **Title overclaims "generalizable" without any supporting evidence**: The paper is titled "A Robot Learning Benchmark for Generalizable Tool Manipulation" yet contains zero experiments on generalization. There is no evaluation on unseen tool variants, no domain randomization analysis, no cross-task transfer experiments, and no held-out tool testing. The only randomization is position randomization in environment resets, which tests robustness, not generalization. This is a clear mismatch between claim and evidence. The word "generalizable" should either be removed from the title or the paper should add experiments that test generalization.

- **RGB/vision observation support claimed as a key feature but entirely unvalidated**: The abstract (line 4) and contribution list (line 24) prominently state that the benchmark "supports both state-based and vision-based observation spaces" and "state, RGB, and state+RGB observation spaces." However, all reported experiments use only state-based inputs. No vision-based policy results are presented anywhere in the paper. A feature that is claimed but not demonstrated cannot be considered a validated contribution. At minimum, a single vision-based baseline on one task should be provided to demonstrate that the claimed functionality works.

### Minor

- **Only 3 model-free RL baselines from the same methodological family**: The benchmark evaluates only CrossQ, SAC, and PPO — all model-free actor-critic methods. No model-based RL, imitation learning, planning-based methods, or hierarchical RL are tested, despite all being relevant to tool manipulation. While this is not unusual for an initial benchmark release, it limits the paper's ability to demonstrate that the benchmark usefully discriminates between qualitatively different approaches. The paper's own identification of "hard" vs. "easy" tasks would be significantly strengthened by showing that methods from different families fail on different tasks.

- **Free-floating tool design limits relevance to real robot tool manipulation (though acknowledged)**: The agent directly controls the tool's pose via a MoCap body with no robot arm, gripper, kinematic chain, or grasping dynamics (line 17). The paper acknowledges this as a deliberate simplification, but the title and framing still call it a "robot learning benchmark." The core challenges that make tool manipulation hard for real robots — grasping affordances, force transmission through a gripper, kinematic constraints, contact stability — are entirely absent. This does not invalidate the benchmark for studying tool-centered motion planning, but the "robot learning" framing inflates the scope.

- **Different training horizons and frame skip values across tasks introduce experimenter degrees of freedom**: Some tasks use 100K training steps while Stacking and Scooping use 300K steps (line 136), and most tasks use frame skip of 12 while Ping-Pong uses 5 (line 139). The justification is empirical ("we found these tasks are more difficult"), which is reasonable but makes cross-task comparisons of sample efficiency impossible and creates concerns about experimenter degrees of freedom. A principled justification or a fixed protocol would strengthen the benchmark's validity.

- **The claim that existing benchmarks lack tool manipulation specialization could be concretely quantified**: The paper states that "none [of the existing benchmarks] specialize in tool manipulation" (line 54) and that they are "not ideal testbeds for studying the generalization to different tools" (line 12). While likely true, this argument would be stronger if the paper quantified how many tool tasks exist in ManiSkill2, Robosuite, and RLBench, and demonstrated concretely why those tasks are insufficient. Currently the differentiation relies on assertion rather than evidence.

### Trivial

None.

## Nice-to-Haves

- Adding a human performance baseline would help calibrate task difficulty and expected ceiling performance.
- An analysis of what makes tasks difficult (action space dimensionality, precision requirements, contact dynamics, reward sparsity) would make the benchmark more useful for method developers.
- Adding one model-based or planning baseline would demonstrate that the benchmark discriminates between qualitative method families.
- Multi-task or transfer experiments would directly support the "generalizable" framing if the authors choose to keep it.

## Removed Points

The following points from the input reviews are removed with justification:

- **"Table 1 is not readable from text extraction"** — Parser artifact; not a paper flaw.
- **"PourPlate uses 3 cube particles compared to 16"** — The paper explicitly documents this (line 96). It is a task feature, not a weakness.
- **"Stacking tasks as 'tool manipulation' is a stretch"** — The paper provides a reasonable justification (bowls/plates as food-carrying tools). This is a subjective framing preference, not a substantive weakness.
- **"No code or benchmark release verification"** — Standard for anonymous review submissions.
- **"The free-floating tool limitation is 'not acknowledged'"** — The paper explicitly acknowledges this (line 17: "This design allows future research to begin with simpler setups... before progressing to more complex variations where tool manipulation must integrate with a robot arm"). The claim that it is unacknowledged is factually incorrect.
- **"No human performance baseline"** — Not standard for first-release simulation RL benchmark papers. Demoted to Nice-to-Have.
- **"Section 2 comparison table..." notes about suggested additions** — These are speculative requests for content beyond the paper's stated scope, not verifiable weaknesses.

## Novel Insights

The most interesting finding to emerge across the reviews is that the benchmark's free-floating tool design, while a deliberate simplification, creates a fundamental tension between the paper's "robot learning benchmark" framing and its actual content. This tension is not resolved by the paper's brief acknowledgment of the limitation. A genuinely novel insight would be that the community might benefit from a clear taxonomy of tool manipulation tasks ranked by embodiment realism (free-floating → constrained end-effector → full arm with gripper → dexterous hand) rather than presenting one level as a complete benchmark. This synthesis emerges from the contrast between the paper's ambitious framing and the reviewers' skeptical readings, but goes beyond the paper's own analysis.

## Suggestions

1. **Remove "Generalizable" from the title** or add at least one generalization experiment (e.g., training on one tool variant and testing on a held-out variant within the same category).
2. **Add at least one vision-based baseline result** to validate the claim that the benchmark supports RGB observations. Even a single task with a CNN-based SAC would substantially strengthen this claim.
3. **Reframe the contribution honestly**: the benchmark tests tool-centered motion planning with free-floating tools. Replace or qualify "robot learning" in the title (e.g., "A Simulation Benchmark for Tool Manipulation").
4. **Provide a principled justification for training horizon and frame skip choices**, or adopt a uniform protocol.
5. **Quantify the gap with existing benchmarks** by stating how many tool-adjacent tasks ManiSkill2, Robosuite, and RLBench have, and what specific tool manipulation skills those tasks omit.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>