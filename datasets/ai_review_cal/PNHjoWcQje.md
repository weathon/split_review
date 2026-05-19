- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

The paper proposes StepTool, a step-grained reinforcement learning framework for tool learning in LLMs. It introduces two components: (1) step-grained reward shaping that assigns rewards at each tool interaction step based on tool invocation success (SuccCalling) and contribution to overall task completion (Contribution), and (2) step-grained optimization using policy gradient methods (instantiated with PPO) to optimize multi-step decision-making. Experiments on StableToolBench across three open-source LLMs (ToolLlama, Llama3.1, Qwen2) and two decoding strategies (CoT, DFSDT) show consistent improvements over SFT and an RLHF-PPO baseline.

## Strengths

- **Step-grained reward design tailored to tool learning.** The paper formalizes tool learning as a multi-step MDP and designs rewards at each tool interaction step based on SuccCalling (format/content correctness), Contribution (relevance to task), and IsSolved (final task completion). This provides richer intermediate signals than final-reward-only approaches like RLHF, and is a genuinely novel application of step-level rewards to the tool-learning setting (Section 4.1).

- **Consistent empirical gains across three models and two decoding strategies.** Per the textual description (Table 2 content is in an \input file stripped by the parser), StepTool outperforms both SFT and RLHF-PPO baselines on ToolLlama, Llama3.1-8B, and Qwen2-7B under both CoT and DFSDT. Gains are larger on complex subsets (e.g., 5%–13% on I3 Ins.) compared to simpler ones (1%–4% on I1 Tool), which aligns with the claim that step-grained optimization helps most in multi-step scenarios (Section 5.2).

- **Ablation study confirming both components matter.** The two ablations—removing step-grained rewards (setting intermediate rewards to 0) and removing step-grained optimization (standard PPO on sub-trajectories)—both cause significant degradation, confirming that the combination of intermediate reward signals and step-level optimization is necessary for the observed gains (Section 5.4).

- **Tool invocation success rates improve.** Figure 4 shows that StepTool increases the average success rate of intermediate tool calls for both ToolLlama and Qwen2, providing direct evidence that step-grained optimization improves execution accuracy at intermediate steps (Section 5.5).

## Weaknesses

### Fatal
None.

### Major

- **The Contribution metric is underspecified.** The paper defines Contribution as $\mathrm{Contribution}(a_t, a_T)$ — "based on the relationship between the current action and the final task-solving action" — but provides no algorithm, heuristic, rule, or GPT-4 prompt for how it is computed. The reward acquisition section states annotations use "a combination of rule-based systems and GPT-4" without specifying what each component does or the prompt used. Since Contribution is central to the claimed novelty of step-grained reward shaping, the method is not reproducible without this specification. (Section 4.1, lines 159, 176)

- **Ambiguity in the training procedure: on-policy vs. off-policy not resolved.** The paper states that step-grained annotated data "can be used for offline reinforcement learning optimization or to train a reward model for online training" (line 177), without clarifying which variant was actually used in the experiments. The PPO instantiation (Eqs. 6–7) describes standard on-policy PPO with an old policy $\pi_{\theta'}$, but the data collection section describes static trajectory collection. It is unclear whether training involves (a) on-policy rollouts from the current policy with GPT-4 annotation at each step, (b) offline RL on a fixed set of pre-annotated trajectories, or (c) training a separate reward model and then doing online PPO. This ambiguity undermines reproducibility. (Section 4.2, lines 177, 225–246)

- **The RLHF-PPO baseline is underspecified and potentially a strawman.** The baseline is described only as "adapting RLHF to tool learning tasks, designed to handle single-step data" (line 285). No details are given about whether it uses the same reward annotations collapsed to a final signal, whether a separate reward model is trained, or how it handles multi-step trajectories. Without this specification, the reported improvements over RLHF-PPO cannot be properly interpreted. (Section 5.1, line 285)

- **No evaluation of generalization to held-out tasks or distributions.** The paper motivates the work by arguing that SFT's imitation of static trajectories "limits the model's ability to adapt to new tasks or environments" (line 17), yet all experiments are conducted on the same benchmark distribution (StableToolBench). There is no evaluation on tasks with unseen tool categories, different API domains, or out-of-distribution queries. The claimed generalization benefit is therefore unsubstantiated. (Sections 1, 5)

### Minor

- **Pass@k experiment is limited in scale and interpretability.** The Pass@k analysis (Section 5.3) uses only 20 tasks per subset (120 total) with no statistical significance testing. The paper's interpretation that improved Pass@k indicates "discovery of new knowledge" rather than "re-weighting prior knowledge" is not uniquely supported—improved sampling coverage from a better policy is also consistent with the data. The paper appropriately uses "suggest" (line 322), but the evidence is thin.

- **Exclusion of DPO-based baselines is weakly justified.** The paper excludes DPO because "constructing comparative data" differs from the authors' setup (line 287). However, DPO with final-task success as a preference signal or step-level DPO (as used in mathematical reasoning, cited in related work) would be natural and feasible comparisons. Including at least one such baseline would strengthen the evaluation.

- **No confidence intervals or significance tests on main results.** All main pass rate results are reported as point estimates without confidence intervals or significance tests. Given the modest improvements on some subsets (1–4%), it is unclear whether these differences are statistically reliable.

- **Missing PPO hyperparameters.** The paper reports learning rate, batch size, and KL coefficient, but omits other standard PPO hyperparameters such as clip epsilon, GAE lambda, number of PPO epochs per update, and value function loss coefficient. These would be needed for reproduction.

### Trivial
None.

## Nice-to-Haves

- Provide the GPT-4 prompts used for Contribution annotation, and ideally a validation study of annotation quality (e.g., human agreement rates).
- Discuss the cost of using GPT-4 as a reward annotator at scale (5,000 tasks × multiple trajectories) and potential failure modes.
- Clarify how the value function $V(s_t)$ is represented and trained in the tool-learning context (separate head on the LLM?).

## Removed Points

- **"The reward equation (Eq. 4) appears truncated/intermediate case missing"** — This is almost certainly a parser artifact. The equation as extracted only shows the $t=T$ case, but the mention of $\alpha$ "to balance the weight of each component" immediately after implies the intermediate case was present in the original. Per instructions, parser artifacts are not author errors.

- **"Improved Pass@k across all k is fully consistent with reweighting existing knowledge; authors' interpretation not justified"** — The paper uses cautious language ("suggest"; line 322). The reviewer's assertion that it's "fully consistent" with an alternative explanation is speculative, not a demonstrated error. The criticism adds no new information beyond the paper's own caveats.

- **"The w/o Step-grained Opt ablation is exactly the RLHF-PPO baseline"** — This is factually incorrect. The ablation uses *step-grained rewards* with standard PPO optimization, while RLHF-PPO uses final-task rewards. They differ in the reward signal used.

- **"Missing related works"** — Per instructions, I cannot verify the existence of missing references and must not mention this.

- **"Hyperparameter details missing / appendix missing"** — The paper reports learning rate, batch size, and KL coefficient; the missing PPO-specific hyperparameters are noted as a minor weakness above but claiming the paper is missing an "appendix" is inappropriate since appendices are stripped by the parser.

- **"No evidence of discovery of superior trajectories"** — The Pass@k analysis and the qualitative case study both provide evidence, albeit limited. The reviewer overstates the absence of evidence; the evidence is simply not definitive.

- **Miscellaneous formatting/style nitpicks** — Removed per instructions (parser artifacts, not author errors).

## Novel Insights

The harsh critic's detailed reading surfaces a genuine tension in the paper: the method relies heavily on GPT-4 as an oracle for intermediate rewards (particularly Contribution), yet the paper motivates RL over SFT by arguing that expert (GPT-4-generated) trajectories can be suboptimal. If GPT-4 is trusted enough to provide reward signals for RL optimization, why would GPT-4-generated expert trajectories for SFT be inherently suboptimal in a way that RL on GPT-4-annotated rewards would fix? This tension is not explicitly addressed and points to a deeper unexamined assumption in the reward design. The strength finder correctly identifies that the paper's core empirical showing—consistent gains across models and ablations—is genuine; the issue is not that the method fails but that its theoretical framing and reproducibility are weaker than the contributions warrant.

## Suggestions

1. **Specify the Contribution function concretely.** Provide the exact rules or GPT-4 prompt used to compute Contribution(a_t, a_T). Even a simple rubric (e.g., "Does the tool output contain information referenced in the final answer?") would substantially improve reproducibility and allow the community to assess whether the reward is reasonable.

2. **Resolve the on-policy/off-policy ambiguity.** Clearly state: (a) whether training uses online rollouts from the current policy or offline optimization on fixed trajectories; (b) if online, how GPT-4 annotations are obtained at each step during training without prohibitive cost; (c) whether a separate reward model is learned; and (d) how the value function V(s_t) is represented and trained.

3. **Add a held-out generalization experiment.** Evaluate on a set of tasks with entirely unseen tool categories or API domains to directly test whether step-grained RL improves generalization over SFT, as claimed in the motivation.

4. **Specify the RLHF-PPO baseline in detail.** Clarify whether it uses the same reward annotations (collapsed to final), a separate reward model, or some other adaptation. This is essential for the reader to interpret the comparison.

5. **Report confidence intervals for main results** (e.g., bootstrapped 95% CIs) to establish that reported gains are statistically reliable, especially on subsets with 1–4% improvements.
