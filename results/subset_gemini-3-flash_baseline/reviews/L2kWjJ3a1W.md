## Summary
The paper introduces the Text-Guided Decision Transformer (TG-DT), an offline meta-reinforcement learning framework designed for zero-shot task adaptation. Unlike existing meta-RL methods that require task-specific demonstrations or online interactions at test time, TG-DT uses natural language task descriptions to specify goals. The core of the method is a dual alignment mechanism: Text-Behavior Contrastive (TBC) learning for cross-task distinction and Text-Behavior Matching (TBM) for fine-grained within-task quality distinction. The model conditions a Decision Transformer policy on these aligned embeddings. Experiments on MuJoCo and Meta-World benchmarks show that TG-DT achieves performance comparable to or better than state-of-the-art baselines that utilize more information (like test-time demonstrations).

## Strengths
- **Strong Motivation and Problem Setting**: The paper addresses a practical gap in offline meta-RL: the reliance on task-specific demonstrations at test time. Using language as a zero-shot task specifier is highly relevant for real-world robotics and human-agent interaction.
- **Dual Alignment Mechanism**: The combination of TBC (contrastive) and TBM (matching) is well-motivated. TBC helps separate distinct tasks, while TBM addresses the specific RL challenge of distinguishing trajectory quality (returns) within the same task, which standard contrastive losses often overlook.
- **Strong Empirical Results**: TG-DT outperforms or matches baselines like Prompt-DT and Meta-DT across several benchmarks (Cheetah, Ant, ML10, ML45). Notably, it achieves this without the test-time demonstrations that many of these baselines require.
- **Robustness Analysis**: The paper provides a thorough evaluation across different data quality levels (Medium, Mixed, Expert), demonstrating that the semantic grounding helps the model remain resilient to suboptimal or noisy offline data.

## Weaknesses
### Fatal
None.

### Major
- **Information Leakage in Test Prompts**: The paper notes in Section 4 and the Limitations that test-time prompts use "approximate statistics inferred from the training distribution" for fields like expected return and episode length. However, the performance of Decision Transformers is highly sensitive to the conditioning return-to-go. If the "approximate" return provided in the text prompt is too close to the oracle optimal return for a specific unseen task, the "zero-shot" claim is weakened, as the model is essentially being told the numerical solution via a text template.
- **Baseline Comparison Fairness**: Several baselines (Prompt-DT, Meta-DT) are marked with a dagger (†) indicating they require test-time demonstrations. While TG-DT's ability to work without them is a strength, the paper does not sufficiently discuss how much "privileged" information is contained in the text templates (e.g., task intent and expected returns) compared to the information extracted by baselines from a few demonstrations.

### Minor
- **Template Dependency**: The method relies heavily on a fixed template: "This is the [task_name], which targets [task_intent]...". The reliance on specific metadata (task name, intent) limits the "naturalness" of the language and suggests the model might be over-relying on keyword matching rather than semantic understanding.
- **Computational Overhead**: The architecture involves multiple encoders (Text, Behavior, Text-Behavior) and a decoder. There is little discussion on the training or inference latency compared to a standard DT.

### Trivial
- The t-SNE plots in Figure 4 show clusters, but the "progression" mentioned in the text for Cheetah-vel is difficult to discern visually without color-coding by target velocity.

## Nice-to-Haves
- An evaluation using "free-form" text or paraphrased instructions to test the robustness of the text encoder beyond the training templates.
- A comparison against a baseline where the DT is conditioned on a simple one-hot task ID or a non-aligned text embedding to further isolate the benefit of the TBC/TBM alignment.

## Novel Insights
The primary novel insight is the application of dual-objective alignment (contrastive + matching) specifically to the temporal and quality-sensitive nature of RL trajectories. While CLIP-like alignment is common in vision-language tasks, the authors correctly identify that RL requires "matching" to distinguish between a "good" and "bad" trajectory of the same task, which a standard contrastive loss might group together. Grounding the Decision Transformer in this aligned space effectively turns a sequence-modeling agent into a zero-shot instruction follower.

## Suggestions
- Clarify exactly how the "approximate statistics" for test prompts are calculated. For example, if the task is "Cheetah-vel" with a target velocity of 3.0 (unseen), and the prompt says "expected return of 6000" (based on training tasks), does this mismatch hurt the model?
- Include a sensitivity analysis on the text prompt. If the "expected return" value in the text is changed, does the agent's performance change accordingly? This would prove the model is actually "listening" to the text.

## Score and Decision
The paper presents a solid contribution to the growing field of language-conditioned offline RL. The methodology is sound, and the dual-alignment strategy is a clever adaptation of vision-language techniques to the specific constraints of RL (trajectory quality). The results are impressive, particularly the zero-shot performance on Meta-World ML45. While the reliance on templated prompts is a limitation, it is a standard starting point for this research area.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>