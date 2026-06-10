## Summary

This paper proposes Curiosity-driven Red-teaming (CRT), which augments the standard RL-based red-team objective with an entropy bonus and novelty rewards (SelfBLEU and cosine-similarity-based) to encourage exploration of effective test cases. The method is evaluated on text continuation (GPT2 base), instruction following (GPT2-alpaca, Dolly-v2-7B), and an RLHF-tuned chat model (LLaMA2-7b-chat). The core idea — connecting RL exploration to red-team test case diversity — is well-motivated and technically sound.

## Strengths

- **Thorough ablation studies systematically isolating each component (Section 4.5, Figure 7).** The paper decomposes CRT into entropy bonus, SelfBLEU reward, and cosine similarity reward, testing all combinations. Figure 7 shows that entropy bonus alone barely improves diversity, SelfBLEU or cosine similarity alone improve some metrics but not all, and only the full combination achieves the best diversity while maintaining quality. This provides strong causal evidence for the specific design choices, going substantially beyond most prior red-teaming papers in methodological transparency.

- **Clear demonstration that simple heuristic alternatives (high temperature, KL penalty tuning) cannot replicate CRT's diversity-quality tradeoff (Section 4.5, Figures 5 and 6).** Varying the KL penalty weight β shows that none of the tested values achieves both quality and diversity simultaneously. Varying sampling temperature from 0.7 to 2.0 shows even the highest temperature falls far short of CRT's diversity. This directly supports the claim that memory-dependent novelty mechanisms are genuinely superior to memory-independent stochasticity.

- **Consistent results across multiple target models and two task formats (Sections 4.2, 4.3).** In the instruction-following setting, CRT achieves strictly higher quality (percentage of toxic responses) *and* higher diversity than all baselines — not just a tradeoff but a strict improvement. This multi-setting validation strengthens generalizability.

- **Principled dual-signal novelty reward design.** The paper uses SelfBLEU (n-gram, form-based) and cosine similarity (embedding-based, semantic) novelty rewards. The ablation confirms each captures a different aspect of diversity, validating the design choice.

## Weaknesses

### Major

- **The LLaMA2 experiment does not support what the paper claims it demonstrates (Section 4.4, Table 1).** Every example in Table 1 shows LLaMA2 *politely refusing* to engage (e.g., "Thank you for asking! However, I must point out that..."). These are stereotypical safety-refusal responses, not toxic generations. The toxicity classifier appears to be flagging refusal language as toxic — a well-documented failure mode of such classifiers. The paper never acknowledges this. The abstract and introduction claim CRT "successfully provokes toxic responses from LLaMA2 model" — but the actual examples show the opposite: safe behavior being misclassified. This does not invalidate CRT as a method, but the paper's most striking headline claim is not supported by the evidence presented. The authors should either (a) use human evaluation or a validated classifier to confirm the responses are genuinely toxic, (b) reframe this experiment as finding prompts that *fool the classifier* rather than elicit toxic content, or (c) replace it with a different RLHF-tuned model where genuinely harmful content is elicited.

- **The paper conflates coverage with diversity throughout, but never measures coverage directly.** The motivating problem is that RL methods achieve "low coverage of the span of prompts that elicit undesirable responses" (line 24). The paper proposes CRT to "increase the coverage of generated test cases" (abstract). Yet the evaluation never measures coverage — it measures *diversity* via SelfBLEU and embedding cosine distance. These are not the same thing. Two sets of test cases can be equally diverse while one covers a much smaller region of the effective-prompt space (e.g., cycling through variants of the same few failure modes). The paper's claims about coverage are therefore unsupported; what is actually demonstrated is improved diversity. This is a conceptual gap between the problem stated and the evidence provided.

- **Critical hyperparameter values are not reported.** The paper introduces weights λ_E (entropy bonus), λ_i (novelty rewards), and β (KL penalty) but never reports their numeric values. The paper states "our method uses the same reward weights across all experiments" (line 252) without saying what those weights are. Without this information, the experiments are not reproducible. Given that the paper acknowledges the weights "must be tuned" (line 252), the missing values are a significant gap.

### Minor

- **The quality-comparable result in the text continuation task is an underpowered null finding (Section 4.2, Figure 1a).** CRT is claimed to have "comparable" quality to baselines on this task. With only 3 random seeds, no statistical tests, and no effect-size reporting, the evidence for "comparable" is weak. The instruction-following results (where CRT exceeds baselines on quality) mitigate this concern, but the paper should either report significance or discuss the limited power.

- **Missing formal definitions of evaluation metric equations.** The paper references `\label{eq:metric_quality}`, `\label{eq:div_selfbleu}`, and `\label{eq:div_embd}` on lines 136 and 221, but these equation labels are never defined in the paper. While the quality and diversity metrics are described in prose (Section 4.1, lines 106-111), the broken equation references are a presentation error that hinders clarity.

- **No discussion of the computational cost of the novelty rewards.** The SelfBLEU novelty reward (Equation 3) requires computing n-gram overlap against all previously generated test cases, which scales quadratically with the number of test cases. The cosine similarity reward (Equation 4) requires pairwise embedding comparisons against the growing set. The paper is silent on these costs, making it difficult to assess practical deployment feasibility at scale.

### Trivial

- None.

## Nice-to-Haves

- Report statistical significance (e.g., bootstrapped confidence intervals or effect sizes) for the main comparisons across all experiments, not just the text continuation task.
- Design a direct coverage measure (e.g., a taxonomy of prompt categories and per-category hit rates) to substantiate the paper's coverage claims rather than using diversity as a proxy.
- Include wall-clock time or FLOP comparisons to quantify the overhead of novelty reward computation.
- Evaluate on at least one non-toxicity safety metric (truthfulness, bias, privacy) to demonstrate generality.

## Removed Points

- **LLaMA2 as a strength (Strength Finder's Point 1):** Removed because it conflicts with the verified weakness: the examples in Table 1 are polite refusals, not toxic content. The strength claims a "striking empirical result" that is contradicted by the paper's own data. Per instructions: when a strength and verified weakness conflict, the weakness wins.
- **Criticism that RL+TDiv baseline implementation is unclear:** The paper describes the baseline adequately for a conference submission. This falls under "trivial implementation details" and is removed per the reproducibility nitpick rule.
- **Request for evaluation on additional safety metrics (from Harsh Critic's "Missing Parts"):** The paper explicitly scopes itself to toxicity ("our method can be applied to any other metric," line 30). Demanding evaluation on other metrics is scope creep.
- **Criticism about "missing related works":** Removed per instruction: I do not have external sources to confirm what works are missing.
- **Criticism about formatting/style:** None applicable.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the LLaMA2 issue honestly.** Either (a) use human annotation or a better-validated classifier to confirm whether the flagged responses are genuinely toxic, or (b) explicitly reframe the section as: "CRT finds prompts that cause a toxicity classifier to flag the model's outputs even when the outputs are safe refusals — revealing blind spots in the classifier rather than the model." The latter is still an interesting finding and would be honest about the evidence.

2. **Add a direct coverage measure.** Design a simple categorical taxonomy of prompt types (e.g., instruction categories, topic areas) and report how many categories each method successfully probes. This would directly support the coverage claims.

3. **Report all hyperparameter values** (λ_E, λ_i for each novelty reward, β, K for SelfBLEU n-gram range) in the main paper or appendix. Add a brief note on how they were selected.

4. **Add statistical significance** for the instruction-following results, where CRT shows clear improvement — this would strengthen the paper's strongest results.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>