- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes Plan4MC, a hierarchical framework for solving diverse long-horizon tasks in Minecraft without human demonstrations. It decomposes tasks into three types of fine-grained basic skills (Finding, Manipulation, Crafting), trains these skills with RL using intrinsic rewards (including a novel Finding-skill that performs exploration via a hierarchical policy), and uses an LLM to construct a skill dependency graph over which a DFS search algorithm plans skill sequences. The method is evaluated on 40 diverse Minecraft tasks, consistently outperforming a PPO baseline (MineAgent) and an interactive LLM planner.

## Strengths

1. **Fine-grained skill decomposition makes RL viable for open-world tasks.** The paper breaks long-horizon tasks into atomic skill types and demonstrates (Table 1) that RL can learn these skills when target items are initialized nearby — e.g., RL with better initialization achieves 0.99 success on "milk a cow" vs. 0.40 without, and 0.44 vs. 0.00 on "harvest log". This directly supports the claim that decomposition reduces exploration difficulty.

2. **Finding-skill dramatically improves downstream manipulation success.** The target-free hierarchical exploration policy (Section 3.1, Figure 2) is trained to maximize area coverage. Table 3 (Table on line 217) shows test success rates for manipulation skills rise substantially when preceded by the Finding-skill vs. without it (e.g., "milk a cow": 0.71 vs. 0.07; "harvest log": 0.33 vs. 0.05). Figure 3 further visualizes the per-planning-step success curves where Plan4MC with Find consistently outperforms the w/o Find ablation.

3. **Skill graph + DFS planning outperforms interactive LLM planning on long-horizon tasks.** The offline LLM-generated skill graph combined with DFS search (Section 4) avoids online LLM mistakes. Table 2 shows Plan4MC achieves 0.293 on Mine-Stones vs. 0.067 for Interactive LLM, and 0.267 vs. 0.030 on Mine-Ores — tasks requiring many planning steps. The zero-shot ablation (0.000 on Mine-Stones and Mine-Ores) confirms that interactive replanning is critical, while the graph-based search is more reliable than an LLM-only planner.

4. **Evaluation across 40 diverse tasks with multiple ablations.** The benchmark includes four task groups with 10 tasks each (Cut-Trees, Mine-Stones, Mine-Ores, Interact-Mobs), and ablation studies isolate the contributions of the Finding-skill, re-planning, and episode length. The "Plan4MC 1/2-steps" ablation further tests robustness to tighter time budgets.

## Weaknesses

### Fatal
None.

### Major

1. **The "most sample-efficient demonstration-free RL method" claim is insufficiently supported.** The paper asserts superiority over DreamerV3 (lines 17, 168) by noting DreamerV3 takes >10M steps for a single cobblestone while Plan4MC uses 7M total to unlock the iron pickaxe. However, this is not a controlled comparison: DreamerV3 learns one task from scratch in its own evaluation setup, while Plan4MC trains many skills separately with privileged training setups (spawning items nearby, MineCLIP rewards, separate skill curricula). The paper does not run DreamerV3 — or any other strong single-task RL method (PPO with exploration bonuses, Go-Explore, etc.) — on its own 40-task suite. Without such a comparison, the claimed state-of-the-art sample efficiency among demonstration-free methods is not rigorously substantiated.

2. **The LLM-generated skill graph is not validated.** The entire planning approach depends on the correctness of the LLM-constructed skill dependency graph, yet the paper provides no quantitative analysis of graph quality — no precision/recall of dependencies against a ground truth, no human verification rate, no error analysis, and no discussion of how errors could propagate through the DFS planner. The paper reports only that ChatGPT was prompted with a few demonstrations (Section 4.1). Since the Interactive LLM baseline (which also uses ChatGPT) makes mistakes on long-horizon tasks, it is reasonable to question whether the graph itself contains errors, yet this is not addressed.

3. **Main results lack statistical rigor.** Table 2 reports only point estimates of success rates for each method-task-set combination, with no confidence intervals, standard deviations, or significance tests. While Table 1 (RL vs. imitation study) reports means with std. devs. over 3 seeds, the main evaluation results do not. The paper states 30 test episodes per task (line 173) but does not report per-task breakdowns — only aggregated averages over 10 tasks per set. This hides per-task variance (some tasks may be solved easily while others fail entirely) and makes it impossible to assess statistical reliability of the reported improvements.

### Minor

4. **"Demonstration-free" framing is somewhat overstated.** The paper explicitly says "without human demonstrations" (abstract) and "most sample-efficient demonstration-free RL method" (abstract, line 39). However, the method relies on MineCLIP (a large vision-language model pre-trained on internet video including Minecraft gameplay) to provide intrinsic rewards for all Manipulation skills, and on ChatGPT (trained on web data including game knowledge) to construct the skill graph. These are forms of human knowledge distilled into pre-trained models. While not action-level demonstrations, this dependence should be more transparently acknowledged and qualified in the central claims.

5. **The "Plan4MC w/o Find-skill" ablation conflates training and testing.** Manipulation skills in Plan4MC were still trained with close initialization (either via spawning items nearby or prior Finding-skill execution during training — Section 3.2). So the ablation removes Finding-skills only during test. This means it primarily tests the importance of re-finding items during evaluation, not the importance of learning to find during training. The contribution of the Finding-skill during training (providing better initialization for other skill learning) is not isolated.

6. **Finding-skill restricted to surface exploration.** The paper explicitly states "considering to explore on the world's surface only" (line 97) and notes the assumption that target items are "uniformly distributed on the world's surface" (line 99). Many important Minecraft tasks (e.g., mining diamonds, iron ore in caves) require underground exploration. The limitation section (line 271) mentions goal-awareness but does not discuss the surface-only scope as a limitation, despite the paper's claim that the method is "extendable to other open-world environments."

### Trivial

7. **The exact list of 40 tasks is not provided**, and training details (network architectures for the DQN low-level policy, exact hyperparameters, steps per individual skill, number of grids for finding) are given only at a high level, somewhat hindering reproducibility.

## Nice-to-Haves
- Comparing against a strong single-task RL baseline (e.g., DreamerV3, PPO with exploration bonuses) on a subset of the same tasks would directly test whether the hierarchical decomposition is beneficial relative to monolithic RL.
- Validating the LLM-generated graph via human verification on a subset of skill dependencies (precision/recall) would strengthen confidence in the planning component.
- Decomposing task failures (planning errors vs. Finding-skill failures vs. Manipulation-skill failures) would help identify bottlenecks and validate the design.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Table 1 motivation is circular"** (Harsh Critic point): The critic claimed that Table 1 "does not show that Finding-skills can actually provide such initialization reliably." This misreads the paper — Table 1 is used to *motivate* the Finding-skill, which is then independently evaluated in Table 3 and Figure 3. The paper does not use Table 1 as evidence that Finding-skills work; it uses subsequent experiments for that. **Removed** (misunderstands the paper).

- **"DFS algorithm is trivial"** (Harsh Critic point): The criticism that the DFS algorithm is trivial once the graph exists is an opinion about implementation complexity, not a weakness. The contribution is the overall framework design (graph generation + search), not the complexity of the search algorithm itself. **Removed** (not a substantive weakness).

- **"Interactive LLM baseline may be under-optimized"** (Harsh Critic point): The critic speculates that the Interactive LLM baseline's prompts may cause planning failures, making the comparison unfair. The paper describes a reasonable baseline with few-shot demonstrations, error-handling rules, and per-case feedback (Section 5). The concern about under-optimization is speculative without evidence. **Removed** (speculative; no evidence of unfairness).

- **Generic reproducibility nitpicks** (e.g., "hyperparameters absent," "code link truncated," "large artifacts"): The paper describes architectures (MineAgent-based, LSTM for high-level), training algorithms (DQN for low-level, PPO for high-level and manipulation), and total steps (7M). More detailed appendix content is stripped by the parser. **Removed** (parser artifacts and standard-level detail for a conference paper).

## Novel Insights

The harsh critic's frame of comparing Plan4MC against DreamerV3 raises an interesting tension: Plan4MC uses a divide-and-conquer approach that is *structurally* more sample-efficient because it breaks exploration into manageable pieces (the Finding-skill handles navigation, Manipulation handles interaction), but this efficiency comes at the cost of requiring privileged training setups (spawning items nearby, MineCLIP rewards, environment-specific initializations). The critic's unstated insight is that while Plan4MC's per-task sample efficiency is not directly comparable to DreamerV3's single-task efficiency, the paper's framing implies a comparison that the evaluation cannot support. A genuinely novel contribution here would be a methodology paper that systematically isolates *which* form of prior knowledge (MineCLIP, LLM graph, Finding-skill, close-initialization training) contributes how much to the overall efficiency gain — but the current paper does not provide this decomposition.

Beyond the paper's own contributions, no genuinely novel insight emerges from the reviews.

## Suggestions

1. Add confidence intervals or standard deviations to the main results table (Table 2) and report per-task success rates (perhaps in a supplementary table) to allow readers to assess variance.
2. Include a controlled comparison to at least one strong single-task RL method (e.g., DreamerV3 or PPO with exploration bonuses) on a representative subset of the 40 tasks to substantiate the sample-efficiency claim.
3. Provide a quantitative validation of the LLM-generated skill graph — e.g., human verification of dependencies for a sampled subset, or an ablation comparing the LLM graph to a manually constructed gold-standard graph.
4. Decompose failures (planning vs. Finding-skill vs. Manipulation-skill) for each task set to identify the bottleneck.
5. Acknowledge the dependence on MineCLIP and ChatGPT more transparently when making "demonstration-free" claims, and qualify "sample efficiency" comparisons to note differences in training setup (privileged initializations, separate skill training).
