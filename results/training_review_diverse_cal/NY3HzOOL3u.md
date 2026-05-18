Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

Plan4MC tackles the challenge of learning long-horizon tasks in Minecraft without human demonstrations. The key idea is to decompose the problem into (a) learning three types of fine-grained basic skills (Finding, Manipulation, Crafting) with RL, where a novel hierarchical Finding-skill performs exploration to bring target items near the agent, and (b) planning over these skills using a skill dependency graph generated offline by an LLM, combined with DFS-based search. Evaluated on 40 diverse Minecraft tasks, Plan4MC consistently outperforms MineAgent, an ablation without Finding-skills, and an interactive LLM planning baseline, particularly on tasks requiring many planning steps.

## Strengths

- **Finding-skill dramatically improves RL sample efficiency and downstream skill success.** Table 1 (rl-vs-imitation) shows that RL with good initialization (targets nearby) achieves 0.99 success on `milk_bucket` vs. 0.40 without, and Table 3 (skill-success-rate) confirms that test success rates of Manipulation-skills collapse without the Finding-skill (e.g., `milk_bucket` drops from 0.71 to 0.07). This directly validates the paper's core hypothesis that exploration is the bottleneck for skill learning and that a dedicated Finding-skill addresses it.

- **Skill graph + DFS search outperforms interactive LLM planning on long-horizon tasks by a large margin.** Table 1 shows Plan4MC achieves 0.267 on Mine-Ores and 0.293 on Mine-Stones, while the Interactive LLM baseline reaches only 0.030 and 0.067 respectively. The gap is largest on tasks requiring many planning steps, confirming that offline graph construction with deterministic search avoids the compounding errors that plague online LLM planners.

- **Comprehensive evaluation with 40 tasks across four difficulty levels and multiple ablations.** The task suite covers diverse settings (Cut-Trees, Mine-Stones, Mine-Ores, Interact-Mobs) and includes ablations that isolate the contribution of the Finding-skill (w/o Find-skill), the interactive replanning mechanism (Zero-shot), and the episode budget (1/2-steps), providing systematic evidence for each design decision.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed sample-efficiency comparison without direct experimental evidence.** The paper claims to be "the most sample-efficient demonstration-free RL method" and states that Plan4MC "greatly outperforms" DreamerV3, citing a single number from a prior paper (10M steps for cobblestone) vs. the authors' 7M total training steps. No DreamerV3 (or any other demonstration-free RL method) is actually run on the same tasks. The iron pickaxe claim ("unlock the iron pickaxe in test") is stated without a quantified success rate or comparison baseline. A comparative claim of this strength requires direct, controlled experimental evidence.

- **Main results table lacks statistical reporting.** Table 1 reports success rates averaged over 30 episodes with no standard deviations or confidence intervals. Given the modest sample size and the high variance inherent in Minecraft environments (the paper's own rl-vs-imitation table shows ±0.20 or larger on several skills), it is impossible to assess whether the reported differences between methods are statistically meaningful. This is a significant methodological gap.

- **LLM-generated skill graph correctness is unvalidated.** The planning mechanism depends entirely on the correctness of the skill dependency graph produced by ChatGPT. The paper mentions only that "ChatGPT makes few mistakes" (in a commented-out line that may not appear in the PDF) and provides no quantitative data: number of skills generated, error rate, human verification effort, or comparison to a manually crafted gold-standard graph. Without this, the robustness of the planning component is unknown.

### Minor

- **Uneven sensor advantage for Finding-skills.** The Finding-skill uses lidar for target detection during exploration (line 101), while baselines lack this sensor. The paper acknowledges this and suggests vision models as an alternative (citing VLM detectors), but does not implement or ablate this alternative, leaving the extent of the advantage unmeasured.

- **Insufficient specification of the Interactive LLM baseline.** The prompts, few-shot demonstrations, and error-correction rules used for the Interactive LLM baseline are not provided. Given that this baseline achieves competitive results on Interact-Mobs (0.247 vs. 0.320), the lack of specification makes it difficult to assess the fairness of the comparison or reproduce the result.

- **Low individual skill success rates and unexplained domain gap limit practical applicability.** Many Manipulation-skills have test success rates below 0.5 (log: 0.33, cobblestone: 0.26, mutton: 0.16). The paper attributes this to a "domain gap" between training and test environments but provides no analysis of its cause (perception errors? motor failures? environment randomization?) or potential mitigations. Since complex tasks chain many skills, this is a significant practical bottleneck.

### Trivial
None.

## Nice-to-Haves

- Per-task success rates with standard deviations or confidence intervals for all methods, to enable readers to assess statistical reliability.
- Direct comparison to DreamerV3 (or another demonstration-free RL method) on a representative subset of the 40 tasks, using equivalent computational budget.
- Quantitative validation of the LLM-generated skill graph: number of nodes/edges, error rate, human correction time, or comparison against a manually constructed graph.
- Ablation of the lidar detection: replace it with a vision-based detector and report any performance change.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Critic's claim that "no standard deviations or confidence intervals are reported anywhere in the paper."* Factually inaccurate: the rl-vs-imitation table (lines 79–80) reports ± values. The valid concern (main results lack error bars) is retained in Major.
- *Critic's complaint about Minecraft-specific symbols (`\mclog`, etc.) not being defined until after the abstract.* These are LaTeX macro definitions that the parser stripped; they would render correctly in the original PDF. Parser artifact.
- *Strength Finder's claim that "Plan4MC unlocks the iron pickaxe with only 7M training steps, far more sample-efficient than prior RL methods."* This conflicts with the verified weakness that the sample-efficiency comparison is not directly tested. The weakness wins; this strength is removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface well-known methodological concerns (error bars, overclaiming, unvalidated components) but do not contribute new scientific insight beyond what the paper already presents.

## Suggestions

1. **Compensate for the lack of direct DreamerV3 comparison** by either: (a) running DreamerV3 on a representative subset of tasks (e.g., one from each of the four task sets) with the same evaluation protocol, or (b) substantially softening the comparative language to remove the "most sample-efficient" and "greatly outperforms" claims, replacing them with a more measured statement such as "Plan4MC demonstrates strong sample efficiency compared to published results of demonstration-free methods."
2. **Add error bars to Table 1** by reporting success rates over multiple seeds (at least 3) with standard deviations or confidence intervals.
3. **Validate the LLM skill graph** by reporting the number of skills/nodes generated, the error rate (e.g., incorrect dependency, missing edge), and the human effort required to verify/correct it.
4. **Run an ablation replacing lidar detection** with a vision-based detector (using the cited VLM models) to quantify the sensor advantage.
5. **Diagnose the domain gap for Manipulation-skills** by comparing success rates in matched (training-like) vs. actual test conditions, to distinguish perception errors from motor or environmental factors.

## Score and Decision

The paper makes a genuine contribution by demonstrating that fine-grained skill decomposition + a dedicated Finding-skill + offline LLM-generated skill graphs can make RL tractable for long-horizon open-world tasks. The core ideas are sound and the experimental patterns are consistent across 40 tasks and multiple ablations. However, the paper is undermined by three clear issues that weaken the claims: an overclaimed sample-efficiency comparison not backed by direct experimentation, missing error bars on the main results, and an unvalidated LLM component that the planning mechanism depends on. These are all addressable with additional experiments and more measured claims, but in the current form they prevent a strong recommendation.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>