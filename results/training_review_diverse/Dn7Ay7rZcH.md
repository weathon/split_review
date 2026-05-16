Now I have all the information needed. Let me synthesize the final review.

## Summary

PLUM proposes an on-policy preference learning framework for code language models that uses automatically generated test cases (from GPT-4) to create preference labels from the model's own outputs, then trains with KTO or DPO — all without training a separate reward model. The paper evaluates across multiple code LMs (MagiCoder, CodeQwen, DeepSeek Coder, StarCoder2, etc.) and benchmarks (HumanEval, MBPP, LiveCodeBench), reporting pass@1 improvements of up to 4.8% on standard benchmarks and 11.8% on LiveCodeBench.

## Strengths

- **Consistent gains across diverse models and benchmarks**: PLUM improves pass@1 across six different code LMs spanning different base architectures and sizes (MagiCoder, OpenCodeInterpreter, CodeQwen, DeepSeek Coder, StarCoder2), and across three datasets (OSS-Instruct, EvolInstruct, ShareGPT). The improvements hold on both standard benchmarks and the harder LiveCodeBench, suggesting genuine capability gain rather than benchmark-specific fitting.

- **Ablation evidence supports the design choices**: The paper runs controlled ablations showing (a) using only un-runnable code as negatives does not consistently help (Figure 2), (b) synthetic negatives from AST mutations harm performance (Section 3.2), and (c) on-policy KTO outperforms off-policy KTO (Table 6). These experiments directly support the claim that natural, on-policy negatives labeled by test-case execution matter.

- **Scalable preference signal without reward model training**: The framework generates test cases via GPT-4 and labels preference pairs using execution results, bypassing the need to train a separate reward model. This is a practical contribution — it makes on-policy preference learning feasible at scale for code generation, where unit tests provide a natural ground-truth signal.

- **Iterative online alignment demonstrated**: Table 7 shows that iterative PLUM outperforms offline methods on the challenging LeetCode benchmark, providing preliminary evidence that the framework supports multi-round policy improvement without a reward model.

## Weaknesses

### Fatal
None.

### Major

- **On-policy vs. off-policy comparison confounds distribution with source-model capability**. The experiment in Table 6 compares on-policy KTO on CodeQwen-1.5B against off-policy data from *different* models (DeepSeek-Coder-1.3B, Qwen2.5-Coder-1.5B, CodeStral-22B, DeepSeek-Coder-33B). Because these models have different solution quality, the observed gap conflates distribution mismatch with data quality differences. (Notably, the off-policy set includes models *larger* than the target — 22B and 33B — whose solutions may be higher quality, meaning the confound does not trivially favor the on-policy condition. But the experiment still cannot isolate whether "on-policy *per se*" drives the improvement.) A cleaner control would use the same model at different training checkpoints.

- **Missing training hyperparameters and reproducibility details**. The paper reports no learning rate, batch size, number of epochs, optimizer, hardware, or training runtime. This is a serious reproducibility gap for an empirical systems paper. Standard training configurations (these are not "trivial details") must be reported for the results to be verifiable.

### Minor

- **No comparison to CodeRL or RLTF as baselines**. The abstract claims PLUM "delivers substantial improvements over ... other execution-feedback-driven approaches," but CodeRL (Le et al., 2022, cited in Related Work §4) and RLTF (Liu et al., 2023a, in references) are not included in the experimental comparison. While the paper does compare against Reflexion, LeTI, and value-conditioning (all execution-feedback methods), CodeRL and RLTF represent the most directly related RL-based training paradigms. Including them (or explaining why they are not directly comparable) would strengthen the claim.

- **Iterative PLUM experiment lacks procedural detail**. Table 7 shows iterative PLUM results, but the paper does not specify the number of iterations, how test-case generation or data collection changed across rounds, or the computational cost. The statement "iterative preference learning ... outperforms offline methods" is not adequately substantiated without these details.

- **No analysis of test-case quality or noise**. The paper uses GPT-4-generated test cases as the preference signal but provides no analysis of their reliability (e.g., false-positive/false-negative rates, fraction of questions where generated tests are insufficient). Table 1 reports a "self-consistency pass rate" but is not discussed. Since the entire training signal depends on these test cases, their quality is a first-order concern.

- **No discussion of computational cost**. The paper does not report the number of GPT-4 API calls, the total training time, or the relative cost compared to baselines. This is important for practical adoption assessment.

### Trivial

- Some tables (2, 4, 5, 6, 7) are embedded as images with minimal textual description of key numbers; the text should report representative absolute pass rates so the reader can assess results without decoding figures.
- Figure 2's description uses "worse than PLUM in most cases" — "most" is vague; whether the gap is consistent or small is unclear without seeing the figure.

## Nice-to-Haves

- Run the on-policy vs. off-policy comparison using the *same model* at different training checkpoints (e.g., after 25%, 50%, 75% of SFT) to control for solution quality.
- Include standard deviations or confidence intervals for main results; many reported gains are modest (~3–5%), and without variance estimates their significance is unclear.
- A more detailed analysis of test-case quality (e.g., human evaluation of a random sample, or comparison against held-out oracle tests) would increase confidence in the preference signal.

## Removed Points

- **"Algorithm 1 is referenced but missing"**: The algorithm is likely present in the original submission as an image/table that was stripped by the PDF parser. Not a valid weakness.
- **"No comparison to execution-feedback RL methods" framed as if CodeRL is entirely absent from the paper**: CodeRL IS cited in Related Work §4 ("Code Generation with Large Language Models"), so the criticism that it is "omitted" from the paper is factually incorrect. The valid concern is its absence from baselines, which is kept above as a minor weakness.
- **"Results for rejection-sampling-based SFT and value-conditioning are not presented"**: The paper states these are in Table 2 and discusses them in the text (line 78–80). The table likely contains these results; the text description is sparse but the results exist.
- **"The paper does not release code or data"**: While this is stated by the reviewer, the paper is a conference submission and release decisions are typically made post-acceptance. This is a pre-publication expectation that is not standard to enforce at review time.
- **Strength Finder's claim that "Comprehensive comparison against multiple baselines"**: Overstated — the comparison is reasonably thorough but not comprehensive (missing CodeRL/RLTF). Merged into minor weakness above.
- **"The 'on-policy data is key' claim is not novel" (from Section-by-Section notes)**: This is a criticism about framing/novelty that does not identify a concrete flaw. The paper's contribution is the *method* for enabling on-policy preference learning at scale with test cases, not the claim that on-policy data matters in general.

## Novel Insights

The reviews surface an under-analyzed subtlety in the on-policy vs. off-policy experiment: the off-policy sources include models *larger* than the target (CodeStral-22B, DeepSeek-Coder-33B vs. CodeQwen-1.5B). This means the off-policy data is not necessarily lower-quality — if larger models produce better solutions, the confound could actually *favor* the off-policy condition. That on-policy training still wins despite potentially weaker candidate solutions is interesting but not directly interpretable from the current experiment design. A properly controlled study (same model, different checkpoints) would cleanly resolve this and could reveal whether distribution match or solution quality is the dominant factor.

## Suggestions

1. Add standard training hyperparameters (learning rate, batch size, optimizer, epochs, GPU type, training time) to a reproducibility section.
2. Run a controlled on-policy vs. off-policy experiment using the same model at different training stages to isolate the effect of distribution match.
3. Add a test-case quality analysis — either manual evaluation of a sample or comparison against held-out oracle tests — to quantify noise in the preference signal.
4. Include CodeRL or RLTF as baselines, or explicitly discuss why they are not directly comparable to the preference-learning paradigm.
5. Provide details on the iterative PLUM setup: number of rounds, how data changes, and whether performance saturates.
6. Report the GPT-4 API cost and total training wall-clock time.

## Score and Decision

The paper proposes a practical, well-motivated framework with consistent empirical improvements across diverse models and settings. The core idea — using test-case execution to create on-policy preference labels at scale — is solid and the ablations are informative. The main weaknesses are (a) the confounded on-policy vs. off-policy comparison, which partially undermines a central claim, and (b) missing training hyperparameters, which hinders reproducibility. These are addressable but non-trivial. The paper's contributions are real and the experiments demonstrate genuine utility, but the current evidence falls short of fully establishing that "on-policy *per se*" drives the gains. With stronger controls and additional details, this could be a solid paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>