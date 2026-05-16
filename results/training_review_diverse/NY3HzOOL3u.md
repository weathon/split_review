Now I have verified everything against the paper. Let me construct the final consolidated review.

## Summary

The paper proposes Plan4MC, a hierarchical framework that converts open-world long-horizon tasks in Minecraft into a combination of fine-grained basic skills learned with RL and planning over a skill graph built using LLM prior knowledge. The key ideas are: (1) decomposing skills into Finding, Manipulation, and Crafting types to make RL tractable without demonstrations; (2) a hierarchical Finding-skill that explores the world to provide good initialization for other skills; and (3) using an LLM to construct a skill graph offline, then applying DFS search for interactive planning, avoiding online LLM planning errors. Experiments on 40 diverse Minecraft tasks show consistent improvement over multiple baselines.

## Strengths

- **Fine-grained skill decomposition makes demonstration-free RL viable for open-world tasks.** Table 1 shows that with better initialization (which Finding-skills provide), RL success rates jump from near-zero to competitive levels (e.g., milk bucket: 0.40→0.99, log: 0.00→0.44). This directly supports the core claim that decomposing skills enables RL to learn without demonstrations.

- **The Finding-skill provides a measurable and dramatic improvement in manipulation skill success.** Table 3 demonstrates that manipulation skills executed with Finding-skills drastically outperform those without (e.g., milk bucket: 0.71 vs 0.07, log: 0.33 vs 0.05, cobblestone: 0.26 vs 0.06). The ablation Plan4MC w/o Find-skill consistently underperforms Plan4MC on all four task sets in Table 2, isolating this contribution.

- **Skill graph + DFS search outperforms online LLM planning, especially on long-horizon tasks.** Table 2 shows Plan4MC substantially outperforms Interactive LLM on Mine-Stones (0.293 vs 0.067) and Mine-Ores (0.267 vs 0.030). The Zero-shot ablation performs poorly across the board, confirming that interactive DFS on the pre-built graph provides more reliable planning than LLM-based methods.

- **Comprehensive evaluation with multiple baselines and ablations.** The experiments span 40 tasks across four task sets, comparing against MineAgent (end-to-end RL), Interactive LLM, and three ablations (w/o Find-skill, Zero-shot, 1/2-steps). The success rate curves per planning step (Figure 2) and conditional success rate analysis further substantiate the design choices.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims — that skill decomposition + Finding-skill enables demonstration-free RL for open-world tasks, and that graph-based planning outperforms online LLM planning — are all supported by evidence.

### Minor

- **The sample-efficiency claim (7M steps vs DreamerV3's 10M+) is directional rather than a controlled comparison.** The paper states Plan4MC "is the most sample-efficient demonstration-free RL method to solve Minecraft Tech Tree tasks." However, DreamerV3's 10M+ steps were for a single sub-task (harvest cobblestone with additional game-speed modifications), while Plan4MC's 7M steps aggregate training across all skills, many learned in easier conditions (targets initialized close to the agent, line 164: "for simplicity, we specify the environment that initializes target mobs or resources close to the agent"). The comparison is useful context but does not constitute a controlled apples-to-apples measurement. A direct comparison on a shared canonical task would substantiate the claim.

- **Tables 2 and 3 report success rates without variance or confidence intervals.** While Table 1 includes standard deviations over 3 seeds, the primary result tables (Tables 2, 3) present point estimates from 30 episodes each with no measure of dispersion. Given the stochasticity of RL in open-world environments, the reader cannot assess whether observed differences (e.g., Plan4MC 0.417 vs. Plan4MC 1/2-steps 0.337 on Cut-Trees) are statistically meaningful. Adding standard deviations or confidence intervals would strengthen the evidence.

- **Finding-skill training details are underspecified for full reproducibility.** The hierarchical policy for Finding-skills involves pre-training a low-level policy with DQN on randomly generated goals, then training the high-level policy with PPO. The paper omits: (i) the number of training steps for each phase, (ii) the total world size (the surface is divided into 10×10 grids, but the grid count is unstated), (iii) reward scaling for the high-level "state count" reward, and (iv) how the goal location (x,y)^g is communicated to the low-level policy (e.g., concatenated to visual features, or as an additional input channel). The paper promises code release, but the method description alone is insufficient for independent reproduction.

### Trivial
None.

## Nice-to-Haves

- Quantify the LLM-generated skill graph: number of nodes, how many required manual correction (if any), and the success rate of the DFS planner alone (given perfect skill execution) to isolate planning from execution errors.
- Report API cost or number of queries to ChatGPT for graph construction.
- On Interact-Mobs, where MineAgent's 0.171 is closer to Plan4MC's 0.320 than on other sets, a brief discussion of what makes those tasks easier (e.g., shorter horizon, fewer planning steps) is already present in the paper but could be expanded.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Reliance on human correction should be acknowledged more explicitly"** — The reviewer criticized the paper for not acknowledging human correction of LLM mistakes. However, the only mention of human correction is in a LaTeX comment (`%We find that ChatGPT makes few mistakes...`, line 146) that does not appear in the published text. The paper does not claim human correction is used. This criticism is based on a commented-out line.

- **"BC comparison in Table 1 is not entirely fair"** — The reviewer argued that the comparison between RL and behavior cloning (from Goal-Aware Learning) is incomplete because the BC results are from a different paper and some cells are empty. However, the paper transparently cites the source and uses this comparison only to motivate the need for better initialization, not as a rigorous benchmark. The skills with empty BC cells (milk bucket, wool) still show that RL with better init. achieves strong results (0.99, 0.81). This is a standard use of existing results for context, not a methodological flaw.

- **"Paper does not discuss why MineAgent's advantage is smaller on Interact-Mobs"** — The paper explicitly addresses this: "MineAgent achieves performance comparable to Plan4MC's on some easier tasks ... in Interact-Mobs, which requires fewer environmental steps and planning steps" (line 203) and "Interactive LLM has comparable performance to Plan4MC on the task set of Interact-Mobs, where most tasks require less than 10 planning steps" (line 246). The reviewer missed this discussion.

## Novel Insights

None beyond the paper's own contributions. The reviews offer useful suggestions for strengthening the evidence but do not surface a novel interpretation of the paper's findings.

## Suggestions

1. **Clarify the sample-efficiency claim.** Replace the qualitative comparison to DreamerV3 with a controlled experiment on a shared task (e.g., harvest cobblestone), or soften the claim to accurately reflect the comparison's directional nature.
2. **Add error bars to Tables 2 and 3.** Standard deviations or confidence intervals over the 30 evaluation episodes would allow readers to assess the reliability of reported differences.
3. **Expand Finding-skill training details.** Add a table or paragraph specifying: total world size, number of DQN/PPO steps for each phase, reward scaling, and how the goal location is fed into the low-level policy's input representation.

## Score and Decision

The paper makes a genuine contribution: it demonstrates that decomposing open-world tasks into fine-grained skills with a dedicated Finding-skill makes RL tractable without demonstrations, and that combining this with an LLM-constructed skill graph and DFS planning substantially outperforms both end-to-end RL and online LLM planning. The evaluation is thorough (40 tasks, multiple baselines and ablations). The weaknesses are real but minor and fixable — none threatens the core claims. I recommend acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>