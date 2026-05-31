## Summary

BuilderBench is a new benchmark for generalist agents centered on open-ended block-building. It pairs a hardware-accelerated physics simulator (MuJoCo + JAX) with a curated task-suite of 42 target structures designed to require diverse reasoning abilities—intuitive physics, geometry, long-horizon planning, and scaffolding. The paper introduces two evaluation protocols: a multi-task self-supervised protocol (agents explore freely, then are evaluated on unseen tasks) and a single-task supervised protocol ("training wheels"). Baseline results for six RL algorithms and two LLMs are reported.

## Strengths

- **Speed and accessibility.** The JAX-MuJoCo simulator runs 10–100× faster than comparable open-ended benchmarks (Crafter, Minecraft, NetHack), meaningfully lowering the barrier to academic research. Providing single-file implementations of six algorithms reinforces this.
- **Well-motivated and rich task design.** The five case-study tasks (T-Block, Four-Cube Packing, Hexagonal Portal, Leaning Tower, Maximum Overhang) convincingly demonstrate that a simple block-building setup generates genuinely hard reasoning problems involving scaffolding, counterweights, rotation heuristics, and simultaneous multi-block manipulation. The design principle of requiring *distinct* skills per task is thoughtfully articulated.
- **Dual-protocol design.** Separating the open-ended self-supervised protocol from the supervised "training wheels" protocol is pragmatic: it ensures the benchmark provides useful gradient signal for researchers even when algorithms fail on the hard protocol, which is essential for incremental progress.
- **Interesting negative results.** The observation that MEGA/SFL/PPO all fail to achieve non-zero success beyond 2-cube tasks, and that ChatGPT-5 and Gemini 2.5 Pro fail all five case-study tasks, constitutes genuine empirical knowledge about the state of the art, not merely a validation of easy tasks.
- **Comparison to ARC-AGI.** The framing of BuilderBench as an *embodied* analogue of ARC-AGI—where priors must be self-discovered through interaction rather than supplied through solved examples—is coherent and places the benchmark precisely in the research landscape.

## Weaknesses

### Fatal
None.

### Major

- **Near-total failure on the primary protocol limits actionable feedback.** All four self-supervised algorithms achieve essentially zero performance on 3-cube tasks after 1B steps. A benchmark where all baselines score near zero for the dominant protocol provides little gradient signal for research and leaves open whether the design of the exploration phase is fundamentally sound or whether 1B steps simply isn't enough. Some characterization of *how* algorithms fail—what behaviors do they learn, what do they explore—would substantially increase scientific value. As currently presented, the self-supervised results say little more than "existing algorithms fail entirely," which is not falsifiable enough to guide future algorithm design.

- **LLM evaluation is superficial.** The evaluation in Section 7.1 consists of a 5×2 binary table (all X's). There is no analysis of what reasoning errors the models make, what parts of the plan they get right, or whether chain-of-thought helps. This section is presented as an important result but does not provide enough detail to be informative.

- **Only a subset of tasks are benchmarked.** The 42-task suite is the advertised contribution, yet the supervised protocol experiments cover only 17 tasks and the self-supervised experiments only 12. Results on the remaining tasks (which by design include harder and unsolved ones) are absent. The claim that the benchmark spans "very easy to extremely hard" is illustrated by figures but not substantiated by systematic results.

### Minor

- The multi-task self-supervised protocol's task specification ( $\mathbb{R}^{34}$, i.e., up to 10 cubes × 3D positions) is mentioned but the dimensionality discrepancy with the evaluation tasks is not fully explained. If agents never observe the hand-designed task spec during training, the mechanism by which a zero-shot test-time policy receives and processes that spec deserves clearer treatment.
- Reporting only three seeds for billion-step runs with algorithms that vary substantially in outcome is thin; confidence intervals are not shown in the figures described.

### Trivial
- Some figure descriptions are redundant (the same figure caption appears three times due to parser behavior).

## Nice-to-Haves

- A qualitative analysis of agent trajectories on failed tasks (e.g., what does an agent that has 1B self-supervised steps do when asked to build a T-Block?) would help readers understand the gap.
- Including even one positive result where an algorithm trained self-supervised transfers non-trivially to a held-out task (perhaps on 1-cube tasks) would make the self-supervised protocol more than a negative demonstration.
- A more informative LLM evaluation (e.g., scoring partial correctness of plans, or providing the LLM with visual input) would strengthen Section 7.1.

## Novel Insights

The central insight that a physically simulated block-building environment with only five action dimensions and simple cube-shaped objects can generate tasks requiring counterweights, scaffolding, simultaneous multi-block manipulation, and maximum-overhang reasoning is genuinely valuable. The paper makes concrete that *embodied reasoning* of this kind—reasoning that is not reducible to text but must be discovered through physical interaction—is currently beyond both state-of-the-art RL algorithms and frontier language models. The analogy to ARC-AGI, in which embodied priors must be *self-discovered* rather than provided, is a useful conceptual framing that distinguishes this benchmark from prior work in a principled way.

## Suggestions

- Add a per-category breakdown (e.g., motor tasks vs. geometry vs. scaffolding) of results on the supervised protocol across all 42 tasks.
- Include at least qualitative visualizations of what self-supervised agents learn after 1B steps to motivate future algorithm design.
- Expand the LLM evaluation to include partial credit scoring, chain-of-thought traces, or multimodal input (images of the structure) to better characterize why current models fail.
- Clarify how task-conditioned evaluation works in the self-supervised setting: if agents never see the goal format during training, how does the task-conditioned policy process test-time goals?

## Score and Decision

BuilderBench is a well-motivated and technically solid benchmark paper that addresses a genuine gap: there is no existing open-ended, fast, physics-based benchmark with a diverse curated task suite for studying exploration and generalization in embodied agents. The simulator speed, dual protocol design, open-source implementations, and rich task diversity are meaningful contributions. The primary weakness—that the main self-supervised protocol yields near-complete failure with little diagnostic insight—limits the paper's immediate utility as a research tool, but does not invalidate the benchmark itself; it makes clear that algorithmic progress is needed.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>