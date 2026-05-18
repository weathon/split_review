Now I have a thorough understanding of the paper and both reviews. Let me synthesize the final review.

---

## Summary

PLUM proposes a framework for on-policy preference learning for code language models that replaces human annotation or explicit reward models with automatically generated test cases. Given a code instruction, GPT-4 generates test cases; candidate solutions are sampled from the current model and evaluated against these test cases to produce preference pairs (passing = chosen, failing = rejected); the model is then trained with KTO or DPO. The paper evaluates on six code LMs across HumanEval, MBPP, EvalPlus, and LiveCodeBench, reporting consistent improvements.

## Strengths

- **Sound core idea with practical appeal**: Using automatically generated test cases to create on-policy preference pairs eliminates the need for separate reward model training or human annotation. This is well-motivated and addresses a real bottleneck in applying preference learning to code.

- **Consistent improvements across diverse models and challenging benchmarks**: PLUM is evaluated on six models (MagiCoder, OpenCodeInterpreter, CodeQwen, DeepSeek Coder, StarCoder2) and four benchmarks. Gains of up to ~4.8% on standard benchmarks and ~11.8% on LiveCodeBench are reported, and the trend is consistent across model families. This breadth strengthens the generalizability claim.

- **Systematic ablation evidence**: The paper validates its design choices through multiple controlled experiments: comparing on-policy vs. off-policy training (Table 6), testing synthetic negatives via AST manipulation, and ablating the test-case-based preference signal against using only un-runnable code as negatives (Figure 2). These experiments support the claim that natural, on-policy, test-case-grounded preference signals drive improvement.

- **Demonstration of iterative online alignment**: The paper shows that PLUM supports iterative preference learning without reward model retraining (Table 7), a practically relevant capability for continued improvement on harder problems.

## Weaknesses

### Fatal
None.

### Major

- **No dedicated method section (Section 2 is absent)**: The paper jumps from Section 1 (Introduction) directly to Section 3 (Experiments), with no separate exposition of the framework. Key procedural details — how test cases are generated (prompt format, acceptance criteria), how preference pairs are constructed from sampled solutions, how KTO/DPO are applied, and how iterative PLUM (Algorithm 1) works — are scattered across the abstract and experimental narrative rather than presented coherently. This structural gap makes the contribution harder to evaluate than it should be and is surprising for a method paper.

- **On-policy vs. off-policy comparison confounds model family**: Table 6 compares on-policy training (data from CodeQwen-1.5-Chat itself) against off-policy data from *different* model families and sizes (DeepSeek-Coder-1.3B, Qwen2.5-Coder-1.5B, CodeStral-22B, DeepSeek-Coder-33B). Because both model family and on/off-policy status vary simultaneously, the gap could partly reflect data-source differences rather than the on-policy principle. A cleaner comparison would use off-policy data from the *same* model at a different training stage.

- **Missing comparisons against execution-feedback RL methods**: The paper compares against Reflexion (prompting) and LeTI (value-conditioning), but does not experimentally compare against methods that use test outcomes with RL objectives (e.g., CodeRL, RLTF). While these methods differ in approach (explicit reward models vs. preference learning), comparing against them would better isolate the value of PLUM's design choice to avoid explicit reward models.

### Minor

- **Training hyperparameters not reported**: Learning rate, batch size, number of epochs, and KL penalty for KTO/DPO training are absent. This limits reproducibility.

- **Test case generation details missing**: The paper states that GPT-4 is used to generate test cases but does not provide the prompts used, the number of test cases generated per problem, or any quality filtering criteria beyond a self-consistency number (Table 1, not visible in extracted text).

- **No confidence intervals or significance measures**: Main results (Tables 2, 4, 5) are reported as point estimates without variance. Given that some reported improvements are very small (potentially 0.1–0.3% on MBPP for some models), it is unclear whether these gains are statistically reliable.

- **Data efficiency claim not validated with scaling**: The paper uses only 1K (OSS-Instruct) and 400 (EvolInstruct) instances and claims data efficiency, but does not show how performance changes with larger subsets or full datasets. The reader cannot assess whether the small-subset results are representative.

- **Value of on-policy negatives not fully disentangled from negative quality**: The on-policy vs. off-policy comparison varies model family, and the synthetic-negative ablation uses off-policy negatives. Because these confounds overlap, it remains unclear whether the benefit of "on-policy" data comes from being on-policy per se or from the higher quality of natural negatives produced by a capable model.

### Trivial

- **Typo**: "levitates the need to train reward models" (line 8) should be "eliminates."

## Nice-to-Haves

- Full-dataset experiments (or at least 2–3 data sizes) to substantiate the data efficiency claim.
- Providing the GPT-4 prompts used for test case generation, or releasing them as supplementary material.
- Error bars (e.g., bootstrapped confidence intervals) for the main benchmark results.
- A controlled on-policy vs. off-policy comparison where off-policy data comes from the same model (e.g., a frozen earlier checkpoint) to isolate the on-policy effect.
- A comparison against a simple reward-model baseline trained on the same test outcomes.

## Removed Points

- **"Missing related works (CodeRL, RLTF, SPoC, AlphaCode)"** — All four are cited in the paper (Related Works section or references). Factually incorrect; removed.
- **"Algorithm 1 is absent"** — The parser strips sections from all papers; Algorithm 1 likely existed in the original submission. Removed per hard rules on missing appendix/section content.
- **"Rejection-sampling SFT results never reported in main tables"** — The paper states it performed these experiments; table images are not visible in the parsed text and may contain these results. Cannot verify absence.
- **"Garbled text passages (e.g., 'We tk .20 ing temperature')"** — Parser artifact rather than author error. Removed per hard rules.
- **Several formatting/style nitpicks and generic observations** — Removed as they do not affect evaluation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a dedicated method section (Section 2)** that describes the three-stage pipeline coherently: test case generation (prompts, filtering criteria, quality checks), preference-pair construction from on-policy samples, and the KTO/DPO training objective with hyperparameters. Without this, the paper is structurally incomplete.

2. **Run a cleaner on-policy vs. off-policy comparison** using off-policy data from the *same* model (e.g., generations from an earlier training checkpoint) to isolate whether on-policy training itself drives improvement, independent of model family confounds.

3. **Report confidence intervals or standard deviations** for main results, especially where gains are small, so readers can assess statistical reliability.

4. **Include the test case generation prompts** (e.g., in supplementary material) and the hyperparameter configuration for all training runs to support reproducibility.

## Score and Decision

The paper tackles a relevant problem with a well-motivated approach and provides reasonably broad empirical validation across six models. The core idea — using auto-generated test cases for on-policy preference learning — is sound and the ablations are informative. However, the structural gap (absent method section), several important experimental confounds, and missing reproducibility details prevent the current manuscript from being publishable as-is. The paper would need a dedicated method section, a cleaner on-policy vs. off-policy experiment, and basic hyperparameter reporting to meet the bar for publication. The contributions are real but the presentation and evaluation are not yet rigorous enough.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>