Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

PLUM introduces an on-policy preference learning framework for code language models that uses automatically generated test cases (via GPT-4) to label preference pairs from the model's own outputs, then trains with DPO/KTO without requiring a separate reward model. The framework is evaluated across multiple strong code LMs (Magicoder, OpenCodeInterpreter, CodeQwen, DeepSeek-Coder, StarCoder2) and benchmarks (HumanEval+, MBPP+, LiveCodeBench), reporting consistent pass@1 improvements of up to 4.8% on standard benchmarks and 11.8% on LiveCodeBench.

## Strengths

1. **Reward-model-free, on-policy preference learning for code**: PLUM bypasses reward model training by using test-case execution outcomes as the preference signal. The paper shows (Table 7, referenced) that this enables iterative online alignment without a separate reward model — a practical and cost-efficient contribution.

2. **Consistent and substantial improvements across diverse models and benchmarks**: The framework improves pass@1 across five different code LMs spanning three distinct SFT dataset distributions (OSS-Instruct, EvolInstruct, ShareGPT). The 11.8% improvement on LiveCodeBench (Table 5) is a non-trivial gain on a challenging, contamination-free benchmark, and the gains hold across models that are already strong SFT checkpoints.

3. **Careful empirical validation of the "on-policy matters" claim**: Table 6 directly compares on-policy vs. off-policy KTO training using preference data from models of varying sizes (1.3B to 33B). Off-policy data, including from larger models, consistently underperforms on-policy training. This directly supports the paper's central thesis and is a reproducible sanity check on claims from prior work (Tajwar et al., 2024; Guo et al., 2024b).

4. **Ablation isolates the value of functional correctness signals**: Figure 2 compares PLUM (test-case-based preference) against a variant using only non-executable code as negatives. The latter often fails to improve or hurts performance, while PLUM consistently enhances results. This cleanly separates the contribution of execution-based signal from mere runnability filtering.

5. **Scalable pipeline without manual annotation**: The paper generates ~60k preference pairs for OSS-Instruct/ShareGPT and ~120k for EvolInstruct using GPT-4-generated test cases, demonstrating practical scalability without human labeling.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Baseline zoo omits code-specific RL/RLHF methods that also use execution feedback.** CodeRL (Le et al., 2022) and RLTF (Liu et al., 2023a) are mentioned in Related Work but not included as experimental baselines. While these use a different paradigm (actor-critic RL with a learned reward model) and the paper's contribution is specifically about reward-model-free preference learning, comparing against them would strengthen the empirical positioning. This is a gap but not a fatal one — the included baselines (Reflexion, LeTI, value-conditioning, rejection-sampling SFT) are more directly comparable in the preference-learning setting.

2. **Test case quality is not independently assessed.** The paper reports downstream pass rates and mentions self-consistency pass rates (Table 1), but does not provide direct quality metrics for the generated test cases (e.g., branch coverage, fault detection rate, human evaluation). Since the entire preference signal depends on these test cases, some validation that they are non-trivial and discriminative would strengthen confidence. The risk of weak or overly easy test cases producing false preference labels is not addressed.

3. **KTO vs. DPO: observation without analysis.** The paper notes that PLUM-KTO outperforms PLUM-DPO, and that DPO "sometimes" harms performance. The explanation defers to prior work (Mitra et al., 2024; Yuan et al., 2024) on DPO instability. Given that this is one of the paper's reported empirical findings, some analysis specific to the code generation setting (e.g., are DPO-trained models over-conservative? do they overfit to false negatives?) would be valuable rather than simply citing external observations.

4. **No discussion of failure cases or limitations.** The paper does not address scenarios where PLUM might hurt performance (mentioned briefly for synthetic negatives and non-executable-code variants, but not for the main method). Types of problems where test-case-based preference may be unreliable (non-deterministic outputs, I/O-heavy problems, problems with ambiguous specifications) are not discussed. Similarly, potential overfitting to the GPT-4 test case generator is not considered.

### Trivial

- Training hyperparameters (learning rates, batch sizes, compute budget in GPU hours) and data sizes per experiment are not reported beyond the number of problems and sampled outputs, limiting fine-grained reproducibility.

## Nice-to-Haves

- A human evaluation or coverage analysis for the generated test cases.
- Analysis of DPO failure cases specific to the code generation setting (e.g., what kinds of problems degrade?).
- An ablation varying the number of generated test cases per problem to characterize the marginal value of more test signals.
- Discussion of potential overfitting to GPT-4's test case generation patterns and how this threat is mitigated.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Missing Methodology Section (Section 2).** The harsh critic claims the method section is absent. However, the parser stripped this section (the Introduction ends mid-sentence before Section 3 begins, and "Algorithm 1" is referenced in Table 7). The original submission contains this section. Removing as a parser artifact.

2. **Incomplete and Unverifiable Results Due to Parser Artifacts.** Tables/figures appear as image placeholders due to PDF extraction. Removing as a formatting artifact — the original submission has readable tables.

3. **"levitates" typo / stray characters like "tk .20".** These are parser corruption of the original text (e.g., "eliminates" rendered as "levitates"). Removing as formatting artifacts.

4. **Generic weakness about missing hyperparameters for reproducibility.** Requesting undisclosed hyperparameters and complete training logs is a standard nitpick; the rule says to remove such nitpicks. The paper provides reasonable methodological detail.

5. **"Weak" test-case filtering concern.** The paper explicitly states "before any filtering" (line 33), mentions self-consistency pass rate (Table 1), and shows pass ratio statistics (Figure 3). Some filtering criteria and quality metrics are present; the criticism overstates the gap.

6. **Baseline comparison complaint about unfair asymmetry.** The reviewer frames missing CodeRL/RLTF as undermining the claim of superiority, but these use a different paradigm (RL with reward models vs. preference learning). The included baselines are appropriate for the paper's category. This has been downgraded to a minor point above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no contradiction or unexpected finding that the paper itself does not already articulate. The consistent finding that on-policy outperforms even larger-model off-policy data (Table 6) is the paper's own most interesting result, not something newly revealed by the reviews.

## Suggestions

1. Add a brief validation of test case quality — even a small human annotation pass or a coverage metric on a sample of problems would substantially increase confidence in the preference signal.
2. Include CodeRL and/or RLTF as experimental baselines, or at minimum justify their exclusion based on paradigm differences (RL + reward model vs. preference learning without one).
3. Add a brief analysis of when/why DPO underperforms KTO in the code setting, perhaps by examining a few representative failure cases.
4. Add a limitations paragraph discussing threats to validity (GPT-4 test case patterns, non-deterministic problems, potential overfitting).
5. Report compute budget and key hyperparameters for reproducibility.

## Score and Decision

**Originality**: The combination of on-policy preference learning with automatic test-case-based labeling for code LMs is novel. (7/10)

**Importance**: Improving code generation without costly reward model training is practically significant. (8/10)

**Claims well-supported**: Yes — the core claims (on-policy > off-policy, test-case signals > non-executable negatives, consistent improvements across models) are supported by controlled experiments. (8/10)

**Soundness**: Experimental design is sound, with multiple ablations isolating specific contributions. Minor gaps in baseline comprehensiveness and test-case validation. (7/10)

**Clarity**: What is visible is clearly written. The missing Section 2 in the parsed version is a parser artifact. (7/10)

**Value to community**: High — the framework is straightforward to implement, does not require reward model training, and the on-policy finding has actionable implications. (8/10)

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>