Now let me write the consolidated review.

## Summary

This paper revisits the idea of using an off-the-shelf prompted LLM as a guardrail against prompt injection — an approach previously dismissed as ineffective based on older, weaker models. With modern reasoning-capable LLMs (GPT-4o, GPT-4.1, Qwen3-32B), the authors show that PromptArmor achieves near-zero false positive and false negative rates on AgentDojo (<1% FPR and FNR) and strong performance on Open Prompt Injection and TensorTrust, while also removing injected prompts (rather than discarding inputs) so the agent can continue the intended task. The paper includes ablations on model size, reasoning, prompting strategies, adaptive attack robustness, and a memorization test.

## Strengths

1. **Near-perfect detection on the most challenging benchmark, with strong generalization across three diverse settings.** Table 1 shows PromptArmor with GPT-4o achieves FPR 0.07% and FNR 0.23% on AgentDojo and keeps both rates below 5% on Open Prompt Injection and TensorTrust. The evaluation spans agent environments, text classification, and access-control settings, demonstrating breadth.

2. **Dramatically reduces attack success compared to all existing defenses.** Table 2 reports PromptArmor-GPT-4.1 attains 0.00% ASR on AgentDojo, whereas the best existing defense (DataSentinel) still suffers 38.63% ASR. This stark contrast establishes PromptArmor as a substantially stronger guardrail than prior approaches that used smaller models or fine-tuning.

3. **Robustness against adaptive attacks is validated.** Table 4 shows that after red-teaming with AgentVigil, PromptArmor-GPT-4.1 maintains ASR of 0.00% and 0.16% against two attack sets, with FPR and FNR below 5%. This directly addresses the concern that the defense could be evaded once an attacker knows about it.

4. **Systematic evidence on the roles of reasoning and model size.** Figure 3 shows that Qwen3-32B achieves near-perfect detection (FPR ~1%, FNR ~1%) regardless of reasoning mode, while smaller models (8B) benefit from reasoning but still underperform, and the 0.6B model cannot balance utility and security. This provides concrete empirical evidence that sufficient model capacity is the primary driver, with reasoning offering secondary gains.

5. **Memorization is ruled out as an explanation.** Section 4.5 applies a membership-inference test (Carlini et al. 2021; Staab et al. 2023) to GPT-4.1 on AgentDojo, reporting average similarity 0.34 (threshold 0.6) with only 3.5% of samples above threshold. This eliminates a natural confound for the strong results.

## Weaknesses

### Major

1. **Model-size confound in the primary comparison table.** Table 2 compares PromptArmor (GPT-4o / GPT-4.1) against baselines including DataSentinel (Mistral-7B), Llama Prompt Guard 2, and Deberta — all substantially smaller models. This conflates the defense *strategy* (prompting) with model *capacity*. The Qwen3-32B results in Figure 3 show that a 32B prompted model also achieves near-perfect performance, which partially addresses this concern, but these results are not included in the main comparison table where a reader would naturally look for fair head-to-head comparisons. The claim that "prompting an off-the-shelf LLM should be regarded as a standard baseline" would be strengthened by including a model of comparable size to the fine-tuned baselines (e.g., Qwen3-32B or a similarly sized open model) directly in Table 2.

2. **Dataset-specific prompt tuning undermines the "standard baseline" claim.** Section 4.1 states "Given the varying settings of the benchmarks, we adjusted the detection prompt for each dataset." The paper does not describe the extent of these adjustments, whether a single prompt would suffice, or how much engineering effort is required to adapt to a new domain. This is consequential because the paper's core message is that PromptArmor should serve as an *easy-to-deploy standard baseline*. If the prompt needs per-dataset tuning, the deployment simplicity argument is weakened. The authors should provide the exact prompts used (currently deferred to Appendix C, which is not available in the main PDF) and ideally demonstrate that a single prompt (or minimal modifications) works across all three benchmarks.

### Minor

3. **Removal quality is never directly measured.** The paper emphasizes that PromptArmor *removes* injected prompts (rather than discarding inputs) as a key advantage over prior work. However, there is no direct evaluation of removal quality — e.g., what fraction of injections are fully extracted, how often benign content is accidentally removed, or whether the fuzzy-matching regex (which allows "arbitrary characters between words") ever over-removes or under-removes. The end-to-end metrics (UA, ASR) conflate detection, extraction, and removal, so they cannot reveal systematic failure modes in the removal step. An ablation comparing PromptArmor with removal vs. a version that simply discards detected samples would also quantify the benefit of the removal component.

4. **No per-attack breakdown of ASR.** The reported "combined ASR" counts an attack as successful if *any* of the four attacks succeeds for a given injection goal. This washes out differences across attack types (Ignore Previous, System Message, Important Messages, Tool Knowledge). Breaking down ASR by attack type would reveal which attacks are harder to defend against and whether the defense is uniformly effective — especially important since prior work found some attacks harder than others.

5. **Distribution of clean vs. contaminated samples not reported.** Knowing the class priors for each benchmark would help contextualize the reported FPR and FNR numbers, since the practical impact of a given error rate depends on how common attacks are in the evaluation.

6. **Sensitivity of the fuzzy-matching removal not explored.** The description allows "arbitrary characters between words" in the regex, but there is no parameter sweep or error analysis showing how robust removal is to extraction inaccuracies. The 0.6 similarity threshold for the memorization test is also stated without justification.

### Trivial

- The paper lacks a dedicated limitations paragraph (e.g., scenarios where the guardrail LLM might be attacked directly, or where computational overhead is prohibitive).
- The Qwen3-0.6B non-reasoning result (FPR 62.57%) is extreme but not commented on beyond noting the trade-off; a brief explanation of whether this is prompt misinterpretation or inherent model limitation would be helpful.

## Nice-to-Haves

- **Ablation of removal vs. detection-only.** Comparing PromptArmor with its removal step against a version that simply discards detected inputs would directly quantify the utility benefit of removal.
- **Practical cost discussion.** Approximate latency and token consumption per guardrail call would help practitioners weigh performance gains against overhead.
- **Per-attack ASR breakdown** as described in weakness 4 above.

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper:

- *"Tool Filter's low utility is noted but not explained."* — The paper *does* explain: "suggests it filters necessary tools required for normal user tasks" (Section 4.2). REMOVED (factually wrong).
- *"Ablation with GPT-3.5 not applied to GPT-4o/4.1."* — The paper explicitly explains that GPT-4o and GPT-4.1 "perform equally well across different prompting strategies," making the ablation uninformative for those models. REMOVED (paper's reasoning is reasonable).
- *"AgentVigil description is thin."* — The reviewer acknowledges it is "sufficient." Not a weakness. REMOVED.
- *"Missing related works."* — Cannot verify without external sources. REMOVED per policy.
- *"Model sizes of baselines not specified."* — The paper lists DataSentinel as using Mistral-7B and mentions Llama Prompt Guard 2. The sizes of other baselines are standard knowledge in the field. REMOVED.
- *Style/formatting nitpicks.* — REMOVED per policy.

## Novel Insights

The merger of the harsh and strength-focused reviews surfaces one insight that goes beyond the paper's own narrative: the paper's results simultaneously *establish* and *bound* the contribution. The very strong performance of prompted GPT-4o/4.1 raises the question of whether the field should redirect from training specialized detection models toward better prompting of general-purpose models — but the model-size dependency revealed by the Qwen3 sweep shows this is only viable when the guardrail LLM has sufficient capacity (~32B+ parameters with reasoning). Future work at smaller scales still needs training-based methods. This tension between "prompting works" and "only with large models" is a genuine open problem that the paper exposes but does not resolve.

## Suggestions

1. Include Qwen3-32B (or another similarly sized open model) directly in the main comparison table (Table 2) to address the model-capacity confound.
2. Provide the exact prompts used for each benchmark (already in Appendix C) and, ideally, demonstrate that a single prompt variant works across all three benchmarks, or document the minimal modifications needed.
3. Add a direct evaluation of removal quality: measure the proportion of injections fully extracted and the fraction of benign content accidentally removed, plus an ablation comparing removal vs. detection-only.
4. Add per-attack ASR breakdowns to the main results table.
5. Include a brief "Limitations" section addressing scenarios the current evaluation does not cover (e.g., attacker awareness of guardrail prompt, computational cost at scale, multi-turn injection vectors).

## Score and Decision

After reviewing the paper and calibrating against human-annotated anchors in the same topic area:

**Round 1 bracket:** [5.0–7.0]. Low-band papers on similar topics score ~3.0 but have unclear methodology or very weak results — this paper is clearly far stronger. Mid-band papers (4.25–5.75) like SPIN (5.50), PFT (4.25), and RA-LLM (5.33) have narrower evaluations, missing baselines, or weaker results — the paper under review is stronger on all these dimensions. High-band papers (7.5+) present deeper theoretical insights or broader contributions not present here.

**Round 2 narrowing:** Anchors in the 5.8–7.0 range (accepted papers like ASB at 6.25, Improved Jailbreaking Techniques at 6.25, Simple Adaptive Attacks at 6.14) represent quality benchmarks. The paper under review is comparable in empirical rigor and contribution significance to these, though the identified weaknesses (model comparison fairness, prompt tuning, removal evaluation) prevent it from reaching the top of this band.

**Final score:** 6.0 — the paper makes a clear, well-supported contribution with strong empirical evidence, but the model-capacity confound in the main comparison and the dataset-specific prompt tuning weaken the "standard baseline" claim, and the removal evaluation gap leaves one claimed advantage unvalidated.

### Anchors consulted

| Anchor | Score | Source | Comparison |
|--------|-------|--------|------------|
| Inverse Prompt Engineering (3MDmM0rMPQ) | 3.00 | round1-topic-low | Much weaker methodology and unclear results |
| Wildflare GuardRail (KjxZ4BdUdN) | 3.00 | round1-topic-low | Much weaker; unfocused contribution |
| DIESEL (fmHS8aBfuH) | 3.00 | round1-topic-low | Much weaker; lightweight inference guidance |
| Code-of-thought prompting (lUyYX9VFgA) | 3.00 | round1-topic-low | Much weaker; safety evaluation, not defense |
| RA-LLM (V01FPV3SNY) | 5.33 | round1-topic-mid | Narrower evaluation (2 models, 1 dataset), no adaptive attacks |
| VLMGuard (JwoCs9O3QL) | 5.00 | round1-topic-mid | Different modality (VLMs), less thorough evaluation |
| PFT (l3bUmPn6u5) | 4.25 | round1-topic-mid | Significantly weaker; unclear problem scope, missing baselines |
| SPIN (PNHGYziAsL) | 5.50 | round1-topic-mid | Similar topic but evaluated on only 7B models, threshold sensitivity issues |
| Booster (tTPHgb0EtV) | 8.00 | round1-topic-high | Stronger theoretical grounding and broader impact |
| Backtracking (Bo62NeU6VF) | 8.00 | round1-topic-high | Stronger; novel technique with thorough evaluation |
| Baseline Defenses (0VZP2Dr9KX) | 5.25 | round1-weakness-comparison | Similar "baseline" framing but less focused |
| Blind Baselines (BXMoS69LLR) | 4.50 | round1-weakness-comparison | Different domain (membership inference) |
| Prompt Injection Benchmark (MsRdq0ePTR) | 5.25 | round1-weakness-eval | Benchmark paper, different contribution type |
| ASB (V4y0CpX4hK) | 6.25 | round1-weakness-agent | Broader benchmark scope but accepted |
| AgentHarm (AC5n7xHuR1) | 6.75 | round1-weakness-agent | Stronger benchmark paper but different contribution type |
| JudgeRail (CEvGuwMum0) | 5.75 | round2-defense | Similar guardrail concept but mixed reviews |
| Improved Jailbreaking (e9yfCY7Q3U) | 6.25 | round2-narrow | Accepted, similar quality tier |
| Simple Adaptive Attacks (hXA8wqRdyV) | 6.14 | round2-narrow | Accepted, similar quality tier |
| Transferability Jailbreaking (asR9FVd4eL) | 6.00 | round2-narrow | Accepted, comparable empirical rigor |

**What did the low-band anchors fail at?** Low-band papers (score ~3.0) typically have unclear methodology, weak or non-comparative results, poor experimental design, or contributions that do not advance the state of knowledge. The paper under review shares none of these failure modes. **What did mid-band failures look like?** Mid-band papers (4.25–5.5) that were rejected typically had one or more of: too-narrow evaluation (1-2 small models), missing critical baselines, unclear problem definitions, or claims not supported by the evidence presented. The paper under review is notably stronger across all these dimensions, but it does share one failure pattern with the mid-band — the model-size confound in the main table is a fairness issue that several mid-band rejected papers were criticized for.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>