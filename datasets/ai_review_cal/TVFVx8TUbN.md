- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3
I have thoroughly verified all claims against the paper. Here is the consolidated review.

---

## Summary

This paper introduces MHPP (Mostly Hard Python Problems), a human-curated dataset of 210 Python programming problems designed to address limitations of saturated benchmarks like HumanEval and MBPP. The dataset is organized around seven identified challenge types (Distraction, Redefinition, Shortcut, Commonsense, Cornercase, Complexity, Codesense), features rigorous contamination control (0% contamination reported), and is evaluated across 26 LLMs. The results show that MHPP reveals capability gaps that HumanEval fails to surface, particularly for open-source models and reasoning-heavy challenges.

## Strengths

1. **Empirically grounded challenge taxonomy.** The seven-category taxonomy is derived from a systematic error analysis of three strong LLMs (GPT-4, GPT-3.5, DeepSeekCoder) on HumanEval (Section 2.2, Figure 2). This taxonomy directly informs dataset construction and is not a post-hoc classification scheme.

2. **Demonstrated contamination-free construction with dual verification.** The paper reports 0% contamination for MHPP, achieved through both manual internet searches by meta-annotators and an automated contamination detector (Section 3.2). This is a concrete improvement over MBPP's 65.4% contamination rate (Section 2.1), which the paper verifies using the same detector.

3. **Empirical evidence that MHPP discriminates where HumanEval saturates.** The correlation analysis (Figure 5) and main results (Table 1) show that models like Llama 3.1 405B and DeepSeek-V2.5 nearly match GPT-4o on HumanEval but fall significantly behind on MHPP. This directly supports the claim that MHPP provides more discriminative evaluation of code-generation capability.

4. **Reliability validated through confidence interval analysis.** The paper reports narrow 95% confidence intervals for pass@1 and pass@5 scores across 10 rounds, with intervals for pass@k=1 being particularly tight (Section 5.1, Table 2). This quantitative validation of stability is a methodological strength rarely demonstrated in code generation benchmarks.

5. **Higher problem complexity quantified across multiple dimensions.** The paper reports concrete statistics: average of 167.6 words per description (vs. ~15.7 for MBPP), 14.9 lines of code per solution, and 14.0 test cases per problem (vs. 3.0 for MBPP, 7.2 for HumanEval). These metrics substantiate the claim that MHPP problems are systematically more complex.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Correlation claim between MHPP and HumanEval lacks quantitative support.** The paper states that "MHPP is closely correlated with HumanEval" (Section 4.3) and presents only a scatterplot (Figure 5) without reporting any correlation coefficient (Spearman's ρ, Pearson's r, or similar). The claim of *close* correlation is stronger than the visual evidence supports, especially given that GPT-4o appears as an outlier driving visible monotonicity. This does not undermine the core finding that MHPP is harder and more discriminating — that conclusion follows from the performance gap, not from the correlation — but it should be fixed. **Suggested fix:** report Spearman's ρ and soften the language to "substantially correlated" or similar.

2. **Construct validity of the seven challenge categories is not quantified.** The categories are derived from manual error analysis on HumanEval (Section 2.2) and guide dataset construction (Section 3.1), but the paper reports no inter-annotator agreement metric (Fleiss' κ, Cohen's κ) for the original error classification nor for validating that held-out MHPP problems are independently assignable to the intended categories. The quality assurance process (Section 3.2) involves meta-annotator review but provides no reliability statistic. The case studies (Section 5.2, Figure 7) are illustrative but do not substitute for systematic validation. **Suggested fix:** report a Kappa statistic from at least two independent annotators classifying a subset of problems.

3. **Inconsistency: claims data contamination for HumanEval but provides no evidence.** Line 98 states that "both MBPP and HumanEval face challenges concerning data contamination," yet only MBPP's contamination rate (65.4%) is reported and no analogous analysis is presented for HumanEval. If the contamination detector was applied to HumanEval, the results should be reported (even if they show 0% contamination); if not applied, the claim should be removed or softened. This is a factual inconsistency rather than a deep flaw, but it should be corrected.

### Trivial

1. **Number of samples for pass@5 in the main evaluation is not explicitly stated.** Section 4.1 mentions "sampling decoding with a temperature of 0.7, which are evaluated with unbiased versions of pass@1 and pass@5 scores" but does not state how many samples are drawn per problem. The CI analysis (Section 5.1) clarifies that 100 samples are generated (50 used per round), but it would improve reproducibility to state this explicitly in the main setup.

## Nice-to-Haves

- **Human performance baseline.** Reporting performance of expert Python programmers on a subset of MHPP would provide an upper bound and help calibrate model scores.
- **Positioning relative to APPS/CodeContests/LeetcodeHard.** A brief comparison of difficulty and coverage would clarify MHPP's novelty relative to existing hard benchmarks (the paper mentions them in Related Work but does not compare).
- **Controlled prompt ablation (optional).** Evaluating a few instruction-tuned models with the same simple prompt used for base models could help separate instruction-following from code-reasoning ability, though using model-native templates is standard practice in the field and not a flaw.

## Removed Points

These points were raised by reviewers but are removed after cross-checking against the paper:

- **"Variable prompting across instruction-tuned models is a confound."** Using each model's native instruction template is standard practice in this field; imposing a single simple prompt on instruction-tuned models would disadvantage them unfairly. This is not a valid weakness.
- **"Category guidelines are somewhat arbitrary."** Thresholds like "more than 200 words" for Distraction or "more than 3 operational steps" for Complexity are concrete annotation guidelines. While the specific numbers could be refined, their existence supports reproducibility and the reviewer provides no alternative standard to compare against.
- **"Extension to Java/C++ is mentioned without results."** Line 184 merely notes that the extension exists as future work; it is not a promised experiment. This is not a weakness.
- **"Contamination detection tool not described."** The tool (LiContan2023) is properly cited. Describing every cited tool's internals is not standard practice.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced no perspective that the paper's own analysis does not cover.

## Suggestions

1. Compute and report Spearman's rank correlation coefficient between HumanEval pass@1 and MHPP pass@1 (and ideally pass@5 as well). Qualify the "close correlation" language with the actual coefficient.
2. Report an inter-annotator agreement statistic (e.g., Fleiss' κ) from at least two annotators independently classifying a random subset of MHPP problems into the seven challenge categories.
3. Either apply the contamination detector to HumanEval and report the result, or remove the claim that HumanEval suffers from data contamination (currently asserted without evidence at line 98).
4. State the number of samples per problem for the pass@5 evaluation explicitly in Section 4.1.
