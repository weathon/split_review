Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

PLUM proposes an on-policy preference learning framework for code language models that uses automatically generated test cases to create preference pairs, eliminating the need for separate reward model training. The framework operates in three stages: (1) automatic test case generation from natural language instructions, (2) preference data creation by evaluating candidate code solutions sampled from the policy against test cases, and (3) training the policy LM (primarily with the KTO objective). Evaluated across six code LMs on HumanEval(+), MBPP(+), and LiveCodeBench, PLUM reports consistent improvements (up to 4.8% average on standard benchmarks, 11.8% on LiveCodeBench).

## Strengths

- **Eliminates reward model training by leveraging automated test cases for on-policy preference learning.** The paper explicitly frames this as a core contribution (abstract L8: "PLUM levitates [eliminates] the need to train reward models, allowing for large scale on-policy and online preference data collation"). Figure 2's ablation confirms that using un-runnable code as negatives (without test-case-based correctness signals) fails to consistently improve performance, while PLUM's test-case-driven oracle produces robust gains (L71, L95).

- **Achieves consistent improvements across multiple code LMs and benchmarks.** The paper tests six diverse models (MagiCoder, OpenCodeInterpreter, CodeQwen, DeepSeek Coder, StarCoder2) and reports that PLUM "consistently improves the performance of a wide range of code language models across all three settings" (L63). The abstract quantifies average gains of ~4.8% on standard benchmarks and ~11.8% on LiveCodeBench (L10).

- **Demonstrates that on-policy preference data is strictly superior to off-policy alternatives.** Section 3.2 (L89) explicitly compares on-policy vs. off-policy training using models of varying sizes (1.3B to 33B) and finds that off-policy generally underperforms on-policy. The synthetic negatives ablation (L91) further confirms that AST-mutated negatives (off-policy by construction) can harm performance, underscoring the value of natural, on-policy negatives from test-case evaluation.

- **Enables iterative (online) preference learning without reward models.** Table 7 (referenced at L85, L97) shows that multiple iterations of PLUM further improve performance on LeetCode. This is a non-trivial extension since online RLHF typically requires a separate reward model, which PLUM bypasses via automated test-case evaluation.

- **Robust across preference objectives and dataset distributions.** PLUM works with both KTO and DPO (though KTO is more stable, L65), and generalizes across three diverse instruction-tuning datasets (OSS-Instruct, EvolInstruct, ShareGPT; Table 4, L29, L61).

## Weaknesses

### Fatal
None.

### Major
- **Reliance on GPT-4 for test case generation.** The paper uses GPT-4 to generate test cases for every evaluation question (L31). This introduces a dependency on a proprietary, costly API and raises reproducibility concerns — researchers without GPT-4 access cannot replicate the pipeline. While the paper mentions self-consistency pass rates for GPT-4-1106 (Table 1, L33), there is no evaluation of whether weaker/cheaper models suffice or how test case quality affects downstream preference learning. This is a genuine limitation of the approach, not a scope issue.

- **Limited baseline comparisons against other test-case-based training methods.** The paper compares against Reflexion (Shinn et al., 2023) and value-conditioning approaches (LeTI), but does not directly compare against other methods that also use execution/test-case signals during training, such as CodeRL (Le et al., 2022) or RLTF (Liu et al., 2023a), both cited in related work (L106, L156). While these methods differ in architecture (RL vs. preference learning), a head-to-head comparison would better contextualize PLUM's advantages.

### Minor
- **The KTO vs. DPO comparison is mentioned but not thoroughly analyzed.** The paper notes that "PLUM-KTO consistently out-performs the baseline, and that PLUM-DPO sometimes under-performs PLUM-KTO" (L65) and attributes this to DPO instability noted in prior work. However, no systematic analysis is provided (e.g., does DPO underperform on certain model sizes or data distributions?). This is a minor gap since the main claims do not depend on which preference objective is used.

- **No discussion of failure cases or limitations.** The paper paints a uniformly positive picture. There is no section discussing when PLUM might fail, how test case quality impacts results, or what kinds of programming problems resist improvement via this method. A brief limitations paragraph would strengthen the paper.

### Trivial
None (the extracted text has too many parser artifacts to assess presentation-level issues fairly).

## Nice-to-Haves
- Evaluate test case generation with open-weight or smaller models (e.g., DeepSeek-Coder) to reduce dependency on GPT-4 and improve reproducibility.
- Add a direct comparison with CodeRL or RLTF to quantify the benefits of preference learning over RL-based execution feedback.
- Provide a brief analysis of which types of programming problems (e.g., algorithmic vs. API-usage) benefit most from PLUM.

## Removed Points
The following points from the harsh critic were identified as invalid due to being parser artifacts, factually incorrect, or otherwise not valid weaknesses:

- **Missing entire method section (Section 2)**: The paper as extracted jumps from Section 1 (cut off mid-sentence at L19) to Section 3 (L24). However, this is a PDF extraction artifact — the introduction is clearly truncated (ends with "candidate solution to"), images are placeholder links, and text is garbled (e.g., "We tk .20" at L31). The three-stage method IS briefly described in the abstract (L6-8), and substantial implementation details appear throughout Section 3. The original submission would contain a complete Section 2. Per instructions, parser artifacts are not author errors.

- **Abstract ends abruptly / Introduction cuts off mid-sentence / Garbled text in Section 3**: These are all parser artifacts from PDF extraction (cut-off sentences, placeholder image references, "We tk .20" at L31). The original submission does not have these issues.

- **"No training hyperparameters, data splits, or evaluation protocols are clearly stated"**: Training details (temperature T=1, sample counts, KTO objective, dataset splits of 1K/400 instances) ARE stated in Section 3 (L31-33, L52, L59-61). The hyperparameters for preference learning (KTO objective, on-policy sampling) are described. This claim is factually incorrect for what is visible.

- **Generic/superficial strengths from Strength Finder**: Some strengths were dropped because they were generic (e.g., "robust across objectives and datasets" — this partially overlaps with the on-policy superiority claim and is already captured in verified strengths) or are restatements of the paper's own contributions rather than novel reviewer insights.

## Novel Insights
The reviews surface an interesting tension not explicitly discussed in the paper: PLUM's core claim is that test cases provide a "native and powerful" supervision signal for preference learning in code, yet the paper itself relies on GPT-4 to generate those test cases. This creates a circular dependency — to improve a code LM's correctness, you need access to a model (GPT-4) that is already capable of generating correct test cases from natural language. A deeper discussion of this dependency and whether the test-case generator can itself be a product of the same training loop (self-play for test case generation) would substantially strengthen the contribution. Additionally, the on-policy vs. off-policy comparison (Table 6) is the paper's strongest ablation — it directly addresses a known failure mode in preference learning and is well-designed, using models of varying sizes as off-policy generators.

## Suggestions
1. Replace GPT-4 test case generation with an open-weight model or provide a cost/quality analysis comparing different generators.
2. Add a direct comparison with RL-based execution feedback methods (e.g., CodeRL, RLTF) to substantiate claims about preference learning's advantages.
3. Include a limitations subsection discussing when test case quality degrades and how it affects PLUM's efficacy.
4. Report the specific numerical results from Tables 2/5 in the main text (in addition to the figures) to ensure they survive extraction.

## Score and Decision

The paper presents a clean, well-motivated framework with consistent empirical support across six models and three benchmarks. The core idea — using automated test cases as a proxy for preference signals in on-policy training — is timely and practical. The main weaknesses are (1) the GPT-4 dependency for test case generation, which limits reproducibility, and (2) the lack of comparison against RL-based execution feedback methods. Neither is fatal; the paper's claims are well-supported by the available evidence. The missing Section 2 in the extracted version is a parser artifact and does not reflect on the submission quality.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>