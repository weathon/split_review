I now have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

Plan4MC proposes a hierarchical framework that decomposes long-horizon open-world Minecraft tasks into fine-grained basic skills (Finding, Manipulation, Crafting), trains these skills with RL and intrinsic rewards, and plans over them using a skill graph constructed offline via ChatGPT plus a DFS-based search algorithm. The key claims are that (1) a dedicated Finding-skill for exploration dramatically improves RL sample efficiency for downstream skills, and (2) the static LLM-generated skill graph with deterministic search yields more reliable long-horizon planning than interactive LLM planners. Experiments on 40 tasks show Plan4MC outperforming baselines and unlocking iron pickaxes with only 7M total training steps, far exceeding prior demonstration-free RL methods.

## Strengths

- **Fine-grained skill decomposition with a dedicated Finding-skill provides a genuine solution to open-world exploration for RL.** The paper correctly identifies that RL fails when task-relevant entities are far from the agent, and proposes a hierarchical exploration policy that maximizes area coverage. The ablation (Plan4MC w/o Find-skill) cleanly demonstrates this: Manipulation-skill test success rates drop from 0.16–0.71 to 0.02–0.07 when Finding-skills are removed (Table 3). The comparison in Table 1 further shows RL with better initialization (via Finding-skills) jumping from 0.00 to 0.44 for "log" and 0.04 to 0.16 for "cow."

- **The offline skill graph + deterministic search approach to planning is well-motivated and outperforms interactive LLM planners on long-horizon tasks.** Plan4MC achieves 0.293 vs 0.067 (Mine-Stones) and 0.267 vs 0.030 (Mine-Ores) over Interactive LLM, while being comparable on shorter Interact-Mobs tasks (0.320 vs 0.247). Using the LLM only for one-time graph construction rather than online prompting is a principled design choice that avoids LLM instability during execution.

- **Plan4MC demonstrates the most sample-efficient demonstration-free RL result on Minecraft Tech Tree tasks.** The paper shows that 7M total environmental steps suffice to unlock iron pickaxes, whereas prior work (DreamerV3) requires over 10M steps just for cobblestone. This is a concrete achievement.

- **Comprehensive ablation study.** The paper compares Plan4MC against MineAgent, Plan4MC w/o Find-skill, Interactive LLM, Plan4MC Zero-shot, and Plan4MC 1/2-steps, cleanly isolating the contributions of the Finding-skill, interactive planning, and the skill graph.

## Weaknesses

### Fatal
None.

### Major

1. **Missing variance estimates in main results (Table 2, tab:results).** The paper reports all main success rates as point estimates with no confidence intervals, standard deviations, or error bars. For evaluations averaged over 30 episodes per task (10 tasks per set → 300 episodes per condition), stochasticity from policy rollouts and environmental randomness is non-negligible. While many of the gaps between Plan4MC and MineAgent are large enough to be clearly meaningful (e.g., 0.417 vs 0.003, 0.293 vs 0.026), other comparisons are tighter: Plan4MC (0.267) vs Plan4MC w/o Find-skill (0.243) on Mine-Ores, and Plan4MC (0.320) vs Interactive LLM (0.247) on Interact-Mobs. Without variance, the reader cannot assess whether these differences are reliable. This weakens the evidential support for claims of "outperforming baselines by a large margin." Notably, the paper *does* report ± values in Table 1 (tab:rl-vs-imitation) for the training analysis, so the capacity exists — it is simply not applied to the main results.

2. **The LLM-generated skill graph is not validated.** The entire planning mechanism depends on the correctness of the skill graph built by ChatGPT. Yet the paper provides no analysis of the graph's accuracy: no error rates, no examples of mistakes, no description of manual corrections applied, no verification procedure (e.g., checking whether the graph supports reachability of key items like iron pickaxes from scratch). The paper mentions giving "a few demonstrations and explanations about the format" in the prompt (line 146), but offers no evidence that the resulting graph is correct or complete. This is a concrete evidential gap — without it, the reader cannot assess whether the method succeeds because the graph is correct or whether planning errors are masked by the interactive re-planning loop.

### Minor

1. **The Finding-skill itself is not directly evaluated.** The paper reports downstream success rates (how Finding-skills improve Manipulation-skill performance) but never directly measures the Finding-skill's own performance: area covered per training step, probability of finding a target within a fixed budget, average steps to first encounter of relevant items. The claim that the hierarchical policy "maximizes area traversed by the agent" (line 30) is never validated with coverage metrics. The downstream ablation (Plan4MC w/o Find-skill) partially compensates, but a direct evaluation would strengthen the contribution.

2. **Edge cases in the skill search algorithm are not discussed.** The paper alternates planning and execution with re-searching after skill failures (line 153), which handles many cases. However, the paper does not discuss what happens when the search algorithm itself fails to produce a plan (e.g., the target item is unreachable from current conditions due to gaps in the skill graph). The DFS-based search is described as producing a plan that is "ensured to be executable" (line 151), but this assurance depends on graph completeness, which is unvalidated. The lack of fallback for search failure is a methodological gap.

3. **The claim about being "the most sample-efficient demonstration-free RL method" is not fully contextualized.** The paper compares against DreamerV3 (a single-task model-based method) and VPT (which uses video pre-training). While the claim is likely true given the cited results, the paper does not discuss or compare against other multi-task RL methods or hierarchical RL approaches in Minecraft that also operate without demonstrations (e.g., H-DRLN, unsupervised skill discovery methods), which could provide more context for the efficiency claim.

### Trivial
None.

## Nice-to-Haves

- **A multi-task RL baseline.** Training a single RL agent across all 40 tasks simultaneously (with the same total 7M budget) would directly quantify the benefit of hierarchical decomposition beyond skill reuse. The current MineAgent baseline trains per-task for 7M each, which actually gives MineAgent substantially more total compute (280M vs 7M) — a comparison that already favors Plan4MC. A multi-task baseline would be informative but is not needed to support the paper's core claims.

- **Goal-conditioned Finding-skill.** The paper already acknowledges this limitation in the conclusion as future work. A goal-aware exploration policy would likely close remaining performance gaps.

## Removed Points

These points are flagged to be removed per our filtering rules; treat them with caution.

1. **"Unfair baseline construction: MineAgent gets 7M per task while Plan4MC uses 7M total."** — This asymmetry (more total compute for MineAgent) favors the baseline, not Plan4MC. If anything, it makes the comparison *conservative* for Plan4MC. Removed per the rule that criticisms about unfair comparison favoring the baseline should be removed. (However, the suggestion of a multi-task RL baseline is retained in Nice-to-Haves.)

2. **"The paper claims that ChatGPT makes few mistakes... but no data is provided."** — The sentence about "ChatGPT makes few mistakes" appears only in a LaTeX comment (line 146, preceded by %), not in the paper's visible text. The paper makes no explicit claim about error rates. The underlying concern about graph validation is legitimate and retained as Major weakness #2 above.

3. **"No mechanism to handle dead ends or re-plan from failure."** — The paper *does* describe re-planning: "we alternate skill planning and skill execution... After each skill execution, we update the agent's condition... and search for the next skill" (line 153). The remaining gap (search failure edge case) is retained as Minor weakness #2.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key empirical gap (missing variance) and the validation gap (LLM graph correctness) but do not reveal any insights beyond what the paper itself states about the value of the Finding-skill decomposition or the robustness of search-based planning over LLM-based planning.

## Suggestions

1. **Add variance estimates to Table 2.** Report standard deviations or confidence intervals across either (a) 30 episodes per task with bootstrapped CIs, or (b) multiple training seeds (even 3 seeds, as used in Table 1). This is the single most impactful fix.

2. **Validate the LLM skill graph.** Provide at minimum: (a) the number of nodes/edges in the graph, (b) a sample of the generated structured information, (c) an estimate of error rate (e.g., fraction of edges requiring correction), and (d) a verification that the graph supports reachability of key items (iron pickaxe, diamond items) from scratch.

3. **Directly evaluate the Finding-skill.** Report metrics such as: area covered per training step, fraction of episodes where target items are found within N steps, and average steps to first encounter of common items (logs, cows, etc.).

4. **Discuss edge cases in planning.** Clarify what happens when the search algorithm cannot find a path from current inventory to the target, and whether this occurred in any of the 40 tasks.

5. **Contextualize the efficiency claim.** Briefly compare against other demonstration-free methods in Minecraft beyond DreamerV3 and VPT, or explicitly scope the claim to "single-task model-based methods" if that is the intended comparison class.

## Score and Decision

The paper presents a well-motivated hierarchical framework with a genuinely useful contribution (the Finding-skill and offline LLM graph planning). The experimental evidence is strong in aggregate — many of the performance gaps are large and consistent across task sets. The two major weaknesses (missing variance and unvalidated LLM graph) are real but addressable; neither invalidates the core claims. The paper merits acceptance with revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>