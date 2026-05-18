Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces RLFH (Reinforcement Learning for Hallucination), an online RL framework that mitigates hallucination in LLMs by constructing fine-grained, token-level reward signals. The key idea is to decompose model responses into atomic facts, assess their truthfulness and informativeness via an LLM-based automatic pipeline, trace these assessments back to individual tokens via longest-common-subsequence/string mapping, and use the resulting dense rewards in PPO. Experiments on HotpotQA, SQuADv2, and Biography show consistent FactScore improvements (+17.9% over base Vicuna, +2.0% over prior learning-based methods on average).

## Strengths

1. **Novel fine-grained token-level reward design for hallucination mitigation.** RLFH decomposes responses into atomic facts, evaluates each for truthfulness and informativeness, and traces signals back to individual tokens via LCS/LCS-string alignment (Section 3.2, Figure 3). This directly addresses the coarse-grained, instance-level feedback limitation of prior work (e.g., FACT) and enables precise credit assignment during online RL.

2. **LLM-based automatic fact assessment for on-policy reward collection.** The paper proposes a pipeline that uses Mixtral-8×7B-Instruct to extract atomic facts, verify them against external knowledge, and rate informativeness—all without human intervention and in real-time during RL training (Sections 3.1, 3.2). This makes the online RL optimization cycle feasible.

3. **Consistent empirical gains with generalization to out-of-distribution tasks.** RLFH achieves the highest FactScore on all three benchmarks (Table 1). Gains generalize to SQuADv2 and Biography despite training only on HotpotQA, suggesting the learned behavior is a meta-ability rather than dataset-specific overfitting.

4. **Detailed behavioral analysis supporting knowledge calibration.** The paper provides evidence (Figures 4–7) that after RLFH, the model increases correct statements while reducing incorrect ones, and deliberately refuses questions it originally answered poorly. This supports the claim that the model learns to calibrate generation to its internal knowledge rather than simply truncating output length.

## Weaknesses

### Fatal
None.

### Major

1. **The refusal-rate confound in FactScore is acknowledged but not fully resolved, weakening the headline claim.** RLFH refuses substantially more prompts than FACT (64.5% vs. 94.5% on HotpotQA). Because FactScore is computed only on answered questions, the reported improvement could be partially driven by selectivity. On HotpotQA, per-answered-question precision is actually slightly lower for RLFH (~0.61) than FACT (~0.64), yet FactScore is higher (0.655 vs. 0.647)—indicating the metric is influenced by response-length effects on the subset of easier questions RLFH selects. The paper discusses this (Section 4.2, "more conservative" bullet; Section 4.3, Figure 7 on refusal patterns) and provides informative analysis, but does **not** report any aggregate metric (e.g., correct facts per total prompt, or FactScore treating refusals as 0) that would enable a clean comparison of overall utility. Without this, a reader cannot determine whether RLFH is genuinely improving factuality or simply learning to decline hard questions while exploiting the per-response nature of FactScore on the remaining easy set. This is the paper's most significant weakness.

   *Mitigation note*: To the paper's credit, the picture is more nuanced than the critic's "driven entirely" framing—on SQuADv2 and Biography, RLFH also improves per-answered-question precision (SQuADv2: 0.681 vs. 0.670; Biography: 0.485 vs. 0.442), showing genuine gains beyond selectivity. But the HotpotQA numbers are ambiguous, and an aggregate metric across all datasets is needed.

2. **The "on-policy" advantage is asserted but not demonstrated.** The paper claims that on-policy sampling addresses distribution shift from off-policy data (Section 1, Sections 3.2), but no experiment compares RLFH against an off-policy variant of the same method. The reward model itself is fixed and not adapted to the changing policy distribution—the "on-policy" aspect is simply standard online RL sampling. Without a controlled ablation, the claimed benefit over off-policy alternatives is not empirically supported.

### Minor

1. **Reward-model sensitivity is documented but not analyzed for selection criteria.** Table 5 (tab:anno) shows that different annotation LLMs produce dramatically different behaviors: Vicuna-7b yields the highest FactScore (0.697) but with only ~6 statements per prompt, while Mixtral yields the most informative responses (~21 statements) with a lower FactScore (0.655). The paper acknowledges this ("at the cost of helpfulness") but provides no principled criterion for choosing among annotation models. If the goal is both truthfulness and informativeness, a joint metric or explicit selection rationale is needed.

2. **The token-level reward mapping via LCS is unevaluated.** The LCS/LCS-string alignment used to trace statement-level judgments back to individual tokens (Section 3.2.1) is described briefly but never validated for accuracy. Errors in decomposition or alignment would propagate directly into the RL reward signal. A small human evaluation or calibration analysis of this mapping step would substantially increase confidence in the method.

3. **Hyperparameter values (α, β, ε) are not reported.** The reward functions (Equations 1 and 2) depend on coefficients α, β, and ε whose values are not given in the main text. These are important for reproducibility. (The functions *f* and *g* are deferred to a table in the appendix, which is standard.)

### Trivial

- The paper would benefit from clarifying that the #Cor and #Inc values in tables are per-prompt averages (including refusals as zero), to avoid ambiguity in cross-checking per-answered metrics.

## Nice-to-Haves

- A comparison with DPO-based factuality methods or other recent RLHF-for-truthfulness approaches would better contextualize the benefit of online RL over preference-based alternatives.
- A small human evaluation (or comparison with GPT-4) of the fact-assessment pipeline's accuracy would boost confidence in the automated reward signals.
- An ablation comparing RLFH with a version of FACT augmented with a simple refusal rule (e.g., threshold on model confidence) would help separate the effect of learning to refuse from the effect of improving per-answer accuracy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the reward function details (functions *f* and *g*) are absent**: Table `\ref{tab:func}` exists in the appendix, which was stripped by the parser. The paper references it explicitly (line 167).
- **Criticism about missing comparison with DPO/factuality methods as a major omission**: While a useful addition, the paper's baseline set (ITI, DOLA, FACT) is defensible for its class. This is noted in Nice-to-Haves.
- **Criticism that the improvement is "driven entirely" by refusal selection**: Overstated—on SQuADv2 and Biography, RLFH also improves per-answered precision. The underlying concern about the metric confound is valid (kept as Major #1), but the "entirely" framing is not supported by the data.
- **Criticism about the reward model being larger than the policy model**: This is a practical observation, not a weakness. Many RLHF setups use larger reward models.
- **Criticism about missing KL penalty coefficient and reward normalization details**: These are standard PPO implementation details that can be inferred from the TRLX framework used.

## Novel Insights

The most interesting observation emerging from the review is that the refusal-behavior analysis (Figure 7) and the reward-model ablation (Table 5) jointly reveal an inherent tension: fine-grained token-level RL for hallucination inevitably shapes both *what* the model says and *whether* it says anything at all. The paper's documentation of this phenomenon (model becoming more conservative, refusing low-accuracy questions, and producing denser responses on answered questions) is actually one of its stronger contributions—it demonstrates that token-level factual rewards naturally induce a form of selective generation. The weakness is that the evaluation framework treats selectivity as a confound rather than as a potentially valuable capability that should be measured with a joint coverage-accuracy metric. An interesting follow-up would be to explicitly formulate the refusal threshold as a controllable parameter rather than an emergent side effect.

## Suggestions

1. **Report an aggregate metric that accounts for refusals.** The simplest fix: report average FactScore across *all* prompts, treating refusals as having 0 correct facts (or equivalently, report correct facts per total prompt). This would resolve the evaluation confound and allow a direct comparison showing whether RLFH improves overall utility or merely trades coverage for precision.

2. **Add an off-policy ablation.** Compare RLFH against the same method but with responses sampled from a fixed, pre-trained policy rather than the online policy, to empirically demonstrate the claimed on-policy advantage.

3. **Provide a joint metric for reward-model selection** (e.g., FactScore × response ratio, or correct facts per prompt) to justify the choice of Mixtral as the default annotation model over alternatives that achieve higher FactScore at the cost of informativeness.

4. **Validate the LCS-based token-level reward mapping** with a small-scale alignment accuracy study or a synthetic testbed.

## Score and Decision

The paper presents a novel and technically sound method for fine-grained hallucination mitigation via online RL. The core idea—decomposing responses into atomic facts and tracing token-level rewards back via LCS—is innovative and well-motivated. The experiments show consistent improvements across all three benchmarks, with the most compelling gains on out-of-distribution tasks where per-answered precision also improves. The behavioral analysis (Figures 4–7) provides meaningful insights into how the model learns to calibrate generation to internal knowledge.

However, the main evaluation is compromised by a refusal-rate confound that the paper acknowledges but does not fully resolve with appropriate metrics. The modest improvement over FACT (+2.0% on average) combined with the uncertainty about how much is driven by selectivity on HotpotQA prevents the paper from making a clean, unambiguous case for its claims. The missing empirical demonstration of the on-policy advantage and the unevaluated reward-mapping step further weaken the contribution in its current form.

The paper has a genuine contribution and the issues are addressable with reasonable revisions (aggregate metrics, one additional ablation, validation study). It is a solid borderline paper that would be strengthened by these additions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>