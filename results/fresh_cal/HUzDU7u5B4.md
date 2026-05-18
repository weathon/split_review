Now I have thoroughly verified all claims against the paper. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
// Leave empty if none apply.

### Major
// Issues that a reviewer would weigh against acceptance.

### Minor
// Issues worth the authors' attention but unlikely to change an accept/reject decision.

### Trivial
// Small issues the authors should fix but that carry no weight in evaluation.

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Weaknesses that are flagged to be removed, treat them with caution

## Novel Insights
One paragraph synthesizing genuinely novel observations.

## Suggestions
- specific actionable suggestion

## Score and Decision

Here's my analysis of each issue:

**FactScore inconsistency** - verified. For RLFH HotpotQA: 13.05/(13.05+8.304)=0.611, reported 0.655. But the inconsistency exists across baselines too (e.g., Orca2: 20.04/(20.04+9.042)=0.689, reported 0.467). The fact that it affects ALL models in various ways, not just RLFH, and goes in BOTH directions, strongly suggests this is a property of the FactScore evaluation pipeline (perhaps per-response averaging vs aggregate ratio, or inclusion/exclusion of unverifiable facts) rather than selective manipulation. Still, the paper should explain the computation. → **Major**

**Refusal rate confound** - verified. RLFH answers 64.5% of HotpotQA vs FACT's 94.5%. The paper acknowledges this but does not provide a holistic metric. → **Major**

**Marginal improvement over FACT** - verified. +0.008, +0.007, +0.017. → **Major**

**Reward granularity ablation pattern** - verified but the critic's framing is too strong. The increase in #Inc is a natural consequence of generating more content. Score improves monotonically. → Downgraded to Minor.

**LCS reward assignment justification** - The paper describes the method but doesn't justify why only the last token gets the reward. Valid methodological question. → Minor.

**Missing hyperparameters (PPO)** - verified as missing. → Minor.

**No statistical significance** - verified. → Minor.

**"INI" typo** - The paper writes "INI" for what should be "ITI" (Inference-Time Intervention). Trivial.

Let me now construct the final review.

Actually, re-evaluating the severity: if the FactScore inconsistency is actually due to the FactScore pipeline's internal scoring (which is the standard FactScore metric from Min et al. 2023), then it's not so much a fatal flaw as a documentation gap. But it IS a problem because readers can't verify the numbers.

The refusal rate issue is serious because HotpotQA shows RLFH dropping from 94.5% to 64.5% response rate. That's a 30 percentage point drop. On the other two datasets, the drops are much smaller (98.4%→95.3% for SQuADv2, 73.6%→69.2% for Biography).

And the marginal improvement over FACT is a real concern for the significance of the contribution.

These three together (FactScore opacity + refusal confound + marginal gain) make the empirical case substantially weaker than it should be. However, the paper does have genuine contributions in terms of the method design and the ablation study on granularity.

Score: I'll go with 5.0, Decision: Reject (borderline).

Actually, let me think about the score more carefully. 

The paper's contributions:
1. On-policy fine-grained feedback framework - well-motivated
2. Token-level dense rewards - creative, ablation supports it
3. Automated fact assessment - useful
4. OOD generalization demonstrated
5. Behavioral analysis showing alignment with knowledge boundaries

Problems:
1. FactScore computation not transparent - major
2. Refusal rate confound - major
3. Marginal empirical gains - major
4. Missing implementation details - minor
5. No significance testing - minor

Given these, I think the paper is clearly below the acceptance threshold but has salvageable ideas. Score 4.5-5.0.

Let me set 5.0 and Reject.

Actually, I'll be more precise. Let me think about what score to assign as a meta-reviewer.

Score 5.0 = "Marginally below acceptance threshold" - this paper has interesting ideas but the evaluation is insufficient to support the strong claims. The FactScore inconsistency and refusal confound are significant issues.

Decision: Reject.

Let me also think about whether I'm being too harsh. The paper DID show RLFH outperforms all baselines on all three datasets. The improvement over Vicuna (the base model) is substantial. The improvement over FACT, while small, IS consistent across all three datasets. The ablation on granularity shows a clear trend. The behavioral analysis is thorough.

But the FactScore computation issue is real - if readers can't verify the numbers from the table, that's a serious transparency problem. And the refusal rate on HotpotQA (64.5%) is very concerning - it means the model is refusing more than a third of questions, compared to only 5.5% for FACT.

I'll go with 5.0 and Reject. This is a borderline paper that might be acceptable with major revisions to the evaluation (explain FactScore computation, provide holistic metric accounting for refusals, add significance testing).Now let me write the final consolidated review.

---

## Summary

This paper proposes RLFH (Reinforcement Learning for Hallucination), an online RL framework that mitigates LLM hallucination by providing fine-grained, token-level feedback. The method decomposes model responses into atomic facts, verifies each fact against external knowledge using an LLM-based fact assessment framework, and traces these judgments back to individual tokens to construct dense reward signals for PPO optimization. Experiments on HotpotQA, SQuADv2, and Biography show improvements over baselines including the base model Vicuna (+17.9% FactScore on average) and prior learning-based methods (+2.0% on average).

## Strengths

- **On-policy fine-grained feedback framework is well-motivated**: The paper clearly identifies the limitations of prior learning-based methods — off-policy data sampling causing distribution shifts and coarse-grained instance-level feedback causing imprecise signal (Section 1, paragraph 3). RLFH directly addresses both issues by enabling LLMs to explore using their current policy and providing statement-level feedback traced back to individual tokens. This motivation is coherent and the method design follows logically from the problem diagnosis.

- **Token-level dense rewards via atomic fact decomposition are validated by ablation**: The ablation study on reward granularity (Table 2, Section 4.4) provides direct causal evidence for the paper's core claim: statement-level rewards (0.655 FactScore) outperform both sentence-level (0.645) and response-level (0.639) rewards. The improvement is monotonic with granularity, and the mechanism — decomposing responses into atomic facts, classifying them into 5 truthfulness categories plus informativeness scores, and backtracing via LCS/LCS algorithms — is technically well-executed.

- **Automated LLM-based fact assessment enables online RL without human annotation**: The faithful reward model (Mixtral 8x7B) automatically extracts statements, verifies truthfulness against retrieved evidence, and assesses informativeness (Section 3.1). The annotation model ablation (Table 3) shows that even open-source 7B models provide useful supervision, suggesting practical viability of the pipeline beyond reliance on proprietary models.

- **Out-of-distribution generalization is demonstrated**: RLFH is trained only on HotpotQA but achieves the highest FactScore on SQuADv2 and Biography (Table 1), indicating the learned behavior (balancing knowledge usage) transfers across tasks.

- **Detailed behavioral analysis corroborates the intended mechanism**: Figures 2–5 show that after RLFH, the model shifts toward higher-accuracy responses, generates more statements in high-accuracy ranges, and selectively refuses questions it originally answered poorly — consistent with learning to align generation with internal knowledge boundaries.

## Weaknesses

### Major

- **FactScore computation is not transparent, and reported #Cor/#Inc/Score values are internally inconsistent**: The paper reports #Cor (correct facts), #Inc (inaccurate facts), and Score for each model in Table 1, but never defines how Score is derived from these counts. Simple division reveals systematic discrepancies: for RLFH on HotpotQA, #Cor/(#Cor+#Inc) = 13.05/21.354 = 0.611, but the reported Score is 0.655. Similarly, for Orca2 on HotpotQA the ratio is 0.689 vs. reported 0.467; for Vicuna it is 0.540 vs. reported 0.569. These inconsistencies affect most rows and go in both directions, suggesting Score is computed via a different aggregation (e.g., average of per-response FactScores rather than ratio of aggregates, or inclusion/exclusion of unverifiable facts) that the paper does not explain. This undermines the reader's ability to verify the central empirical claims from the presented data.

- **Increased refusal rate confounds direct FactScore comparison**: RLFH answers only 64.5% of HotpotQA prompts, compared to 94.5% for FACT (Table 1). Since FactScore is computed only on generated responses (refused prompts produce no response to evaluate), a more conservative model can inflate its score by selectively avoiding difficult questions. The paper acknowledges this qualitatively (Section 4.2, point 3) but provides no holistic metric that captures overall utility — e.g., correct facts per total prompt (counting refusals as zero). On HotpotQA, RLFH produces 13.05 correct facts per prompt on the 64.5% it answers, yielding ~8.42 correct facts per 100 total prompts, while FACT's 13.31 × 94.5% ≈ 12.58. Without such accounting, the reported FactScore gains (+0.008 on HotpotQA) could partially or fully reflect selection bias rather than superior hallucination mitigation.

- **Marginal improvement over the strongest baseline (FACT)**: The absolute FactScore gains over FACT are +0.008 (HotpotQA), +0.007 (SQuADv2), and +0.017 (Biography) — roughly 1 percentage point. Given the substantial increase in complexity (on-policy PPO with a separate Mixtral 8×7B reward model, online fact decomposition and verification during training), the practical benefit of this improvement is unclear. The paper frames this as "significant improvement," but the numbers do not warrant strong claims, especially when the refusal confound is considered.

### Minor

- **Reward assignment to only the final token of each statement is not justified**: The paper assigns the statement-level truthfulness reward exclusively to the last token of each statement via LCS/LCS matching (Section 3.2.1). No rationale is given for why concentrating the reward on a single token is preferable to distributing it across all tokens of the statement. This choice could affect PPO credit assignment and may partially explain the increase in incorrect facts observed in Table 2.

- **Increase in incorrect facts with finer granularity is not analyzed**: Table 2 shows that statement-level rewards increase #Inc from 6.453 (sentence-level) to 8.304, alongside an increase in #Cor from 11.17 to 13.05. The paper notes this briefly but does not analyze the mechanism — whether finer feedback causes the model to generate more content (including more errors) or specifically encourages riskier factual claims. Understanding this trade-off is important for interpreting the net benefit of fine-grained rewards.

- **No statistical significance or confidence intervals**: The reported improvements — especially the small gains over FACT — are presented without error bars, significance tests, or multi-seed results. Given the small effect sizes, it is unclear whether the observed differences are reliable or within the noise of the evaluation pipeline.

- **Missing implementation details for reproducibility**: PPO hyperparameters (learning rate, KL penalty coefficient, number of episodes, batch size, etc.) are not reported. The prompt templates for statement extraction and factual verification are also absent. These are needed for reproducing the method and interpreting training stability.

### Trivial

- The baseline "INI" appears to be a typo for "ITI" (Inference-Time Intervention, Li et al. 2023). The accompanying citation is correct for ITI, so this is a minor naming inconsistency.
- Table 3 (annotation model ablation) contains a LaTeX formatting artifact where a closing brace appears mid-row.

## Nice-to-Haves

- A computational cost comparison with FACT and other baselines would help readers assess practical viability, given RLFH's reliance on online LLM-based annotation during PPO training.
- The paper raises the tension between mitigating misleading/reckless hallucinations and increasing evasive ignorance (refusal) but does not formalize this trade-off. A cost model or user study weighing refusal against error would strengthen the practical contribution.

## Removed Points

These points were raised by reviewers but are removed from the main weakness list for the following reasons:

- **"The reward granularity ablation reveals a counterintuitive pattern that raises fatal questions" (from Harsh Critic)**: The increase in #Inc with finer granularity is a natural consequence of generating more content (statements per response increase from ~17.6 for paragraph-level to ~21.4 for statement-level). The key metric — Score — improves monotonically, and the paper briefly acknowledges the pattern. This is an observation worthy of deeper analysis but not a flaw.
- **"Cost analysis needed"**: Framed as a nice-to-have; not a weakness.
- **"Prompt templates for statement extraction and factual verification not provided"**: Partially subsumed under the reproducibility point above (Missing implementation details).
- **"The paper does not state whether FACT is also based on Vicuna-7b"**: The paper states "hallucination mitigation methods using the same initialize model" (Section 4.1), implying FACT shares the base model. This could be clearer but is stated.
- **"Detailed analysis should also show unconditional distributions (including refusals)"**: A valid suggestion for strengthening the analysis, but the paper's behavioral analysis on the answered subset is already informative and self-consistent.

## Novel Insights

A genuinely interesting observation emerges from synthesizing the refusal analysis (Figure 5) with the reward granularity ablation (Table 2): the model learns to trade off response rate for precision in a granularity-dependent way. As reward granularity increases from paragraph → sentence → statement, the response rate drops (0.867 → 0.715 → 0.645) while per-response statement count increases (from ~12.8 to ~21.4 total statements per answered prompt). This suggests that finer-grained feedback does not simply suppress low-confidence answers — it selectively encourages the model to elaborate more when it does answer, while becoming more selective about which questions to answer at all. This behavior is consistent with learning a sophisticated refusal-vs-elaboration strategy that simple coarse-grained rewards (positive/negative on the whole response) cannot produce. The paper presents this data but does not frame it as an emergent property of dense token-level rewards, which is a missed insight worth highlighting.

## Suggestions

1. **Clarify FactScore computation**: Provide the exact formula linking #Cor, #Inc, and Score, and explain any aggregation differences (e.g., per-response averaging vs. global ratio, handling of unverifiable facts). A worked example would resolve the apparent inconsistency.

2. **Report a holistic metric accounting for refusals**: Compute "correct facts per total prompt" (including refusals as zero) or a weighted F-measure that penalizes both incorrect facts and unnecessary refusals. This would directly test whether the RLFH's trade-off is beneficial overall.

3. **Add significance testing / multi-seed results**: Report means and standard deviations across at least 3 random seeds, especially for the comparison between RLFH and FACT where the gains are very small.

4. **Analyze the #Inc increase with finer granularity**: Explain whether the increase in incorrect facts at the statement level is due to more content generation, riskier generation, or a specific reward-shaping effect.

5. **Include PPO hyperparameters and prompt templates** in an appendix for reproducibility.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>