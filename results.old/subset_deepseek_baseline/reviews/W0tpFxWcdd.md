## Summary

The paper proposes HINTS, a framework for incorporating human coaching into reinforcement learning by conditioning policies on programmatically generated cues derived from human-intuited hints. Instead of providing full demonstrations or explicit action supervision, a human identifies conceptual hints (e.g., "look far into the corner") that are grounded into sensory cues (e.g., road curvature) by a generator with access to ground-truth state information. The agent learns a policy conditioned on these cues using various conditioning schemes. Experiments in classic control, car racing, and locomotion show that hint-conditioned agents outperform vision-only baselines and approach state-based agents under limited training budgets.

## Strengths

- **Novel framework for human-in-the-loop RL**: The idea of using human-intuited cues as a form of coaching rather than direct supervision (demonstrations or action labels) is original and addresses an underexplored middle ground between full autonomy and full human control.
- **Systematic empirical evaluation**: The paper evaluates multiple conditioning schemes (LC, AC, FC, MC) across a diverse set of tasks (classic control, car racing, locomotion) and includes challenging deployment variations (hairpin corners, swing-to goals). The ablation of different hint types provides insight into which cues are most useful.
- **Clear performance gains over vision-only agents**: Across all tasks, hint-conditioned agents significantly outperform the vision-only PPO-RGB baseline, with improvements of +80% in classic control and +32% in challenging car racing variations. This supports the core claim that human coaching via cues improves sample efficiency.
- **Well-motivated and clearly written**: The paper motivates the problem of data-constrained visual control well, and the framework is described with sufficient detail to be reproducible (architecture, conditioning schemes, hint generator).

## Weaknesses

### Fatal
None.

### Major

1. **Hint generator requires ground-truth state information**: The generator \(G\) has access to the underlying environment state and dynamics to compute grounded cues. This is a critical limitation for real-world deployment where such ground truth is unavailable. The paper acknowledges this but provides no experiments or discussion on how to learn the generator from data or human feedback. Without addressing this, the practical applicability of HINTS is severely limited.

2. **Unfair comparison to baselines**: The paper compares HINTS agents (trained with a fixed, limited budget) to Expert PPO, DAGGER, and GAIL that are trained "until convergence" without specifying the budget. This is an apples-to-oranges comparison. The paper should either train all agents with the same budget or provide learning curves that show sample efficiency. Additionally, the paper does not compare to modern pixel-based RL methods (e.g., DreamerV2, DrQ-v2, CURL) that are designed for sample-efficient learning from images. The claim of "dominant performance over state-of-the-art baselines" is not supported when the baselines are limited to a simple PPO-RGB and state-based agents.

3. **Results do not consistently support the strongest claims**: In Table 2, for Acrobot, the best HINTS-FC agent (-302.24) is outperformed by PPO-x (-197.90), a state-based agent with the same limited budget. The paper claims +75% improvement over vision-only, but the comparison to state-based agents is mixed. The paper should clarify the scope of its claims and provide statistical tests (e.g., confidence intervals) to support the reported improvements.

4. **No comparison to random or less informative hints**: Hypothesis H2 states that "hinting with human-identified info increases performance over other types of info." However, the experiments only compare composite hints to full state information or individual cues. There is no baseline with random hints or hints that are not human-identified, so the claim that human intuition is the key factor is not directly supported.

5. **Lack of analysis on hint generator learning**: The paper relies on a programmatic generator with access to ground truth. There is no discussion or experiment on how to obtain the generator in settings where state information is not available, which is the primary motivation for using vision-based RL in the first place.

### Minor

- The paper uses "HINTs" and "HINTS" inconsistently (title vs. abstract/body).
- The figures (especially Figure 1) are described but the actual images are not visible in the extracted text, making it hard to assess the visual quality of the cues.
- The paper mentions "Appx Sec A.3" for details on agent architecture and hint generator, but the appendix is removed. While we are instructed not to penalize for missing appendix, the paper should be self-contained for the main claims.

### Trivial
None.

## Nice-to-Haves

- Include comparisons to modern pixel-based RL methods (e.g., DreamerV2, DrQ-v2) to contextualize the performance of HINTS within the broader sample-efficient RL literature.
- Provide experiments with a learned hint generator (e.g., trained from human demonstrations or weak supervision) to address the limitation of requiring ground-truth state.
- Add statistical significance tests (e.g., bootstrap confidence intervals) for the main performance claims.
- Include an ablation on the number of hints or hint dimensionality to understand the scaling properties of the framework.

## Novel Insights

The paper's core insight is that human-intuited cues can serve as a form of coaching that guides RL agents more effectively than direct supervision or full state information, especially under data constraints. The idea of conditioning on programmatically generated cues from human concepts is novel and could inspire future work on human-AI collaboration in RL. However, the reliance on ground-truth state for the generator limits the immediate impact of this insight.

## Suggestions

- Add comparisons to state-of-the-art pixel-based RL methods (e.g., DreamerV2, DrQ-v2) to demonstrate the advantage of HINTS over other sample-efficient approaches.
- Provide a more fair comparison by training all baselines with the same budget or by showing learning curves.
- Include experiments with learned hint generators (e.g., from human demonstrations or weak supervision) to address the limitation of requiring ground-truth state.
- Perform statistical tests (e.g., bootstrap confidence intervals) to support the claims of improvement.
- Clarify the results in Table 2 and 3, especially the comparison to state-based agents, and temper the claims accordingly.

## Score and Decision

The paper presents a novel and interesting framework with promising results. However, the major weaknesses—particularly the reliance on ground-truth state for the hint generator, the unfair comparison to baselines, and the lack of comparison to modern pixel-based methods—significantly limit the paper's impact and soundness. The core idea has merit, but the experimental validation is insufficient to support the strong claims made. I recommend rejection with the possibility of resubmission after addressing these issues.

MY FINAL SCORE: 4.5</score>
MY FINAL DECISION: Reject</decision>