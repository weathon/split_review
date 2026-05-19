- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper systematically evaluates whether LLMs can improve their reasoning through self-correction without external feedback (intrinsic self-correction). Across three models (GPT-3.5, GPT-4, GPT-4-Turbo, Llama-2), four datasets (GSM8K, CommonSenseQA, HotpotQA, CommonGen-Hard), and multiple feedback prompts, the authors find consistent evidence that intrinsic self-correction degrades rather than improves reasoning performance. The paper further identifies three evaluation flaws in prior self-correction literature: (1) reliance on oracle labels to decide when to stop, (2) unfair comparisons that do not control for inference cost, and (3) prompt-design confounds where improvements come from under-specified initial prompts rather than correction itself.

## Strengths

- **Rigorous definition of intrinsic self-correction.** Section 2 clearly distinguishes self-correction without external feedback from methods that leverage oracle labels, tools, or human input. This clean isolation targets precisely the setting where self-correction claims are most overstated yet hardest to evaluate.

- **Systematic empirical demonstration of performance degradation.** Tables 3–5 and the extended prompt-variation tables show consistent accuracy drops across four models and three reasoning benchmarks. The degradation is large and unambiguous for most settings (e.g., Llama-2 on GSM8K: 62.0% → 36.5%), and even the smaller drops (GPT-4-Turbo) never show improvement.

- **Causal analysis of answer changes (Figure 1).** The paper quantifies the shift between correct/incorrect answers after self-correction, showing that models are systematically more likely to flip a correct answer to an incorrect one than vice versa. This provides direct empirical support for the paper's central explanation — that LLMs cannot reliably judge the correctness of their own reasoning.

- **Exposure of oracle-label reliance in prior work.** Table 2 reproduces the improvements from RCI and Reflexion when oracle labels are used, and Table 3 shows that performance collapses when those labels are removed. This cleanly identifies a fundamental flaw in how earlier evaluations were conducted.

- **Fair inference-cost comparison of multi-agent debate.** Table 6 compares debate against self-consistency at equal numbers of model responses (3, 6, 9) and shows debate never outperforms self-consistency — at 9 responses, self-consistency is 5.2% better. This demonstrates that debate's improvements stem from multiple sampling, not from correction.

- **Prompt-design artifact demonstration (CommonGen).** Table 7 shows that adding "include *ALL* concepts" to the initial prompt raises standard prompting from 44.0% to 81.8%, while the original Self-Refine pipeline on the weaker prompt only reaches 67.0%. This cleanly illustrates how under-specified initial prompts produce illusory self-correction gains.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claim — that current LLMs cannot improve reasoning through intrinsic self-correction — is well-supported by consistent evidence across models, datasets, and prompts. The weaknesses below are real but do not undermine the central contribution.

### Minor

1. **Multi-agent debate comparison limited in scope.** The claim that multi-agent debate "does not outperform self-consistency" (Section 4 title, and stated broadly in the conclusion) is tested on only one model (GPT-3.5) and one dataset (GSM8K). While this faithfully replicates the original debate paper, generalizing beyond that single setting requires more evidence. The rest of the paper's conclusions do not depend on this result, but the paper states it as a general finding.

2. **No error bars or confidence intervals for main results.** Results in Tables 3, 5, 6, and 7 are reported as point estimates without variance. For some settings where degradations are small (e.g., GPT-4-Turbo on GSM8K: 91.5 → 88.0 → 90.0), it is unclear whether the fluctuation is within noise. While most effects are large enough that intervals would not change the conclusion, their absence weakens the quantitative rigor, especially given that several datasets are evaluated on subsets of 200 or 100 examples.

3. **No deep analysis of why Llama-2 degrades catastrophically.** Llama-2 drops from 62.0% to 36.5% on GSM8K and 64.0% to 36.5% on CommonSenseQA. The paper notes that Llama-2 tends to change correct answers to incorrect ones but does not investigate *why* — e.g., calibration properties, confidence patterns, or whether the model is simply obeying the "review" instruction uncritically. The GPT-4/GPT-4-Turbo behavior (more likely to retain answers) presents a natural comparison that is not explored.

### Trivial

1. **Chain-of-thought usage not explicitly stated.** The paper says it uses prompts from prior work for initial generation but does not state whether these prompts involve chain-of-thought reasoning. For GSM8K and HotpotQA this matters for interpreting baseline scores, and it should be stated explicitly.

## Nice-to-Haves

- **Adaptive stopping protocol.** The paper forces a fixed two rounds of self-correction. An alternative protocol — letting the model decide when to stop and whether to accept its answer — could better reflect practical usage and might produce different results. Testing or discussing this would strengthen the analysis.

- **Expanded debate experiment.** Adding even one more dataset (e.g., CommonSenseQA) or model (e.g., GPT-4) to the multi-agent debate comparison would substantially increase confidence in the generalizability of that finding.

## Removed Points

These points were raised by reviewers but are removed with justification:

- **"A brief justification of the temperature choice would be helpful"** — *Removed*: The paper already states this justification: "to provide evaluation across different decoding algorithms" (line 83).

- **"The original task used a different model version for the CommonGen comparison"** — *Removed*: The paper's own replication (Standard Prompting* 53.0 → Self-Correct* 61.1 vs. Standard Prompting (ours) 81.8 → Self-Correct* 75.1) supports the same conclusion without cross-paper model differences.

- **"Missing appendix content / proofs"** — *Removed*: The parser strips appendices; the original submission contains them. The paper is an empirical critique, not a theoretical paper requiring proofs.

- **Generic strengths about importance of the problem** — *Removed*: The retained strengths are all specific and grounded in the paper's concrete contributions.

## Novel Insights

None beyond the paper's own contributions. The paper itself is the novel contribution — it provides a clear, well-evidenced negative result that challenges an overly optimistic narrative in the community. The key insight is that intrinsic self-correction fails not because of implementation details but because LLMs cannot reliably judge the correctness of their own reasoning, and this inability is structural rather than contingent on prompt engineering.

## Suggestions

1. Add confidence intervals (e.g., bootstrap) for the main accuracy tables to strengthen quantitative rigor.
2. Expand the multi-agent debate analysis to at least one additional dataset or model to support the general claim.
3. Add a brief analysis probing Llama-2's behavior — e.g., does it always change its answer when prompted to review, and is the model's confidence in the initial answer a predictor of whether it will flip?
4. Explicitly state whether chain-of-thought prompting is used for initial generation in each experimental setting.
5. Consider adding an experiment with adaptive stopping to address the "model decides when to stop" alternative protocol.
