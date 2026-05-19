- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 3, 8, 6
Now I have a complete picture of the paper. Let me construct the final review.

## Summary

PLUM proposes using automatically generated test cases from natural language instructions to construct on-policy preference data for code LMs, enabling preference learning (KTO/DPO) without training a separate reward model. The approach is evaluated on HumanEval+, MBPP+, and LiveCodeBench across five model families (MagiCoder, OpenCodeInterpreter, CodeQwen, DeepSeek Coder, StarCoder2), reporting consistent improvements over SFT baselines and ablations confirming the importance of on-policy data and execution-based preference signals.

## Strengths

1. **Consistent gains across diverse model families and benchmarks**: The paper demonstrates PLUM improves pass rates on standard benchmarks and LiveCodeBench across five different code LMs (MagiCoder, OpenCodeInterpreter, CodeQwen, DeepSeek Coder, StarCoder2). The abstract reports up to 4.8% average improvement on standard benchmarks and 11.8% on LiveCodeBench. The text (lines 63-64) emphasizes that improvements hold "regardless of the base models' performance" and applies to "a wide range of code language models across all three settings."

2. **On-policy vs. off-policy ablation (Table 6)**: The paper directly compares on-policy KTO against off-policy data sampled from four other models of varying sizes (DeepSeek-Coder-1.3B, Qwen2.5-Coder-1.5B, CodeStral-22B, DeepSeek-Coder-33B) and shows on-policy training consistently outperforms off-policy (lines 89-93). This isolates and confirms the central claim about on-policy data being key.

3. **Ablation on the importance of execution-based negatives (Figure 2)**: The paper shows that using non-executable/runnable code as negative instances does not consistently improve performance and can even hurt, whereas PLUM's execution-driven preference signals reliably enhance the model (lines 95-96). This distinguishes the approach from weaker alternatives.

4. **Demonstrates iterative online alignment without reward model training (Table 7)**: The paper shows that PLUM supports iterative preference learning (referencing Algorithm 1) without requiring a trained reward model, outperforming offline methods on the LeetCode benchmark (lines 97-98). This is a practical advantage for scaling.

## Weaknesses

### Fatal
None.

### Major

- **Comparison against execution-feedback training methods is incomplete**: The paper claims to outperform "other execution-feedback-driven approaches" but the baseline set is narrow. The experiments compare against Reflexion (a prompting method) and LeTI (a value-conditioning approach), but not against methods that also *train* models using execution feedback, such as CodeRL (Le et al., 2022) or RLTF (Liu et al., 2023a). The related works section (line 106) acknowledges these methods exist — "Reinforcement learning techniques, like those in CodeRL... and reward models used in DeepSeek-Coder-V2 also improve performance using test feedback" — but they are not included as experimental baselines. Without these comparisons, the claim that PLUM is superior to existing execution-feedback *training* approaches is not fully supported. This is a genuine gap, though CodeRL/RLTF use different RL paradigms (actor-critic) rather than preference learning.

### Minor

- **Test case quality is not analyzed**: The paper generates test cases using GPT-4 but does not analyze how often generated test cases are buggy, incomplete, or over-restrictive. The self-consistency pass rate for test generation is mentioned in a non-visible Table 1. Without understanding test case quality, it is difficult to assess whether performance gains are robust or depend on test case accuracy. The paper also does not discuss failure modes (e.g., open-ended programming tasks, domains requiring external libraries).

- **On-policy vs. off-policy ablation conflates multiple dimensions**: The off-policy condition uses data sampled from *other models'* outputs. As the harsh critic correctly notes, it would also be informative to compare against an off-policy variant where the model's *own* outputs are used with rewards evaluated differently (e.g., with an external reward model). This would better isolate the effect of "on-policy sampling" from "data source quality."

- **The "4.8% and 11.8% improvements" are not clearly stated as absolute or relative**: The abstract (line 10) and text (line 76) report pass rate improvements but it is ambiguous whether these are absolute percentage point gains or relative improvements. This should be clarified.

### Trivial
- The abstract ends mid-sentence ("We also demonstrate the benefits of on-policy and online preference learning" — line 10 continues with no period/end), and the introduction also cuts off mid-sentence (line 18). These are likely parser artifacts from PDF extraction but should be verified in the original.

## Nice-to-Haves

- **Expand baseline set to include training-based execution feedback methods** (CodeRL, RLTF) if computationally feasible, or add a discussion of why they are not compared.
- **Report variance** across multiple seeds for main results, given the stochasticity of on-policy sampling.
- **Break down LiveCodeBench results by difficulty level** — the paper asserts PLUM is "particularly beneficial for medium-level interview questions" (line 76) but provides no disaggregated evidence.
- **Disclose KTO/DPO hyperparameters** (β, learning rate, batch size, number of training steps) and the GPT-4 prompt template for test case generation.
- Add a limitations section discussing reliance on a powerful external LLM (GPT-4), computational cost of on-policy sampling, and scenarios where test cases may be insufficient.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Missing method section (critical issue #1 from harsh critic)**: The harsh critic argues the paper has no Section 2 (method description). However, the Introduction literally ends mid-sentence on line 18 ("test cases present as a native and powerful candidate solution to"), and there is a visible gap before Section 3 begins at line 24. The paper references "Algorithm 1" in Table 7. This is unambiguous evidence of PDF extraction truncation — the method section was present in the original submission but lost during parsing. Per the formatting-artifact removal rule, this criticism is invalid.

- **"Abstract ends abruptly mid-sentence" (section-by-section note)**: Same parser-truncation issue.

- **"Garbled text" complaints about "We tk .20 ing temperature T=1"**: Clearly a parser artifact from PDF — "We take temperature T=0.2" was likely intended.

- **"Missing numbers in tables due to parsing"**: Tables are embedded as images; missing numbers are parser artifacts. The text reports the key findings.

- **"No code or data release is mentioned"**: Code release is not a standard requirement, and the rule says to remove such reproducibility nitpicks.

- **Generic speculation-based criticisms**: The harsh critic's suggestions about "could the metric be measuring a proxy?" and similar area-of-concern sweeps without concrete anchors are removed.

- **Missing discussion of limitations/future work in Conclusion**: The paper's conclusion (lines 117-119) is indeed brief, but this is a minor presentation preference, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a reasonable gap in baseline comparison and raise helpful suggestions for strengthening the evaluation, but do not uncover contradictions or unexpected findings that meaningfully reframe the contribution.

## Suggestions

1. Add the missing baseline comparisons (CodeRL, RLTF, or similar training-based execution-feedback methods) or clearly explain why they are excluded.
2. Add a test case quality analysis (success rate per benchmark, failure modes, impact of self-consistency filtering).
3. Clarify whether reported improvements (% gains) are absolute or relative, and report variance across seeds.
4. Provide the KTO/DPO training hyperparameters and the GPT-4 test generation prompt in the main text or appendix.

## Evaluation

**Originality**: Moderate. Combining on-policy preference learning with automatically generated test cases for code LMs is novel in execution, though individual components (test generation, preference learning, on-policy sampling) are established. **Importance of research question**: High. Improving code LMs beyond SFT without expensive human annotation or reward model training is practically significant. **Claims support**: Adequate. Core claims (PLUM improves models, on-policy matters, execution-based negatives matter) are supported by experiments, though the baseline set is narrower than claimed. **Soundness of experiments**: Generally sound but limited by the narrow baseline comparison and lack of test case quality analysis. **Clarity**: The extracted text is heavily corrupted by parser artifacts; assuming the original submission is complete, the writing is clear and well-structured. **Value to community**: Potentially high — the framework is practical, scalable, and model-agnostic.
