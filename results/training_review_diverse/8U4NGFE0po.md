Now I have a thorough understanding of the paper and can cross-check all reviewer claims. Let me synthesize the final review.

## Summary

This paper proposes PLHF (Prompt Learning from Few-shot Human Feedback), a framework for prompt optimization in LLMs when no well-defined metric exists for output quality (common in generative tasks). PLHF uses a duo-module design: a responder module that generates outputs, and an evaluator module (a prompt-optimized LLM) that learns human preference patterns from few-shot labeled data and serves as the scoring function for the responder. Experiments on three public datasets and one industrial SQL-QA dataset show PLHF outperforms existing scoring strategies including exact matching, embedding similarity, and using GPT-4o directly as the judge.

## Strengths

1. **Effective solution to the undefined-metric problem for generative tasks**: The paper directly addresses a practical limitation of existing prompt optimization frameworks (DSPy, TextGrad) that require well-defined metrics. PLHF's evaluator module, learned from few-shot human labels, enables optimization for tasks where output quality is subjective. Empirical results (Table 3) show PLHF (using GPT-3.5 as evaluator) consistently outperforms "PO with GPT-4o" across all four datasets under both DSPy and TextGrad backends, including relative improvements like +73.72% vs +44.11% on SGD with DSPy.

2. **Validation on real-world industrial data with actual human evaluation**: The SQL-QA dataset from a commercial product provides evaluation by actual human experts. PLHF achieves 24.21% improvement (TextGrad) over the base LLM versus 13.16% for the next best baseline (PO with GPT-4o), demonstrating practical applicability beyond controlled settings.

3. **Minimal human feedback requirement with clear algorithmic specification**: PLHF uses a single round of human-labeled data to train the evaluator, which then serves as the metric for the entire optimization process. Algorithm 1 clearly specifies the workflow, and Section 3.3 explains that the batch test setup stops at Line 16 (single round), avoiding iterative human queries. The optional augmentation loop (Lines 17–22) is explicitly marked as optional for incrementing-data scenarios.

4. **Detailed evaluator subtask analysis validates design choice**: Table 2 shows that prompt-optimized LLM-based evaluators dramatically outperform traditional ML methods (MLP, SVM) for scoring tasks—e.g., GPT-3.5 PO via TextGrad achieves RMSE of 1.62 vs MLP's 9.14 on AES-ASAP—supporting the paper's choice of using a prompt-optimized LLM as the evaluator.

5. **Performance analysis with few-shot sample sizes**: Figure 4 provides learning curves showing that both evaluator RMSE and responder output quality improve rapidly with few training samples (~50 on SGD), with shrinking standard deviations across 30 runs, supporting the few-shot claim.

## Weaknesses

### Fatal

None.

### Major

1. **Unvalidated pseudo-human judge for public datasets**: The paper's evaluation on public datasets (SGD, AES-ASAP, AES-2.0) relies on a "pseudo-human judge"—GPT-4o with DSPy prompt optimization trained on the same human-labeled samples used by PLHF. The paper does not provide any correlation or agreement statistics between this LLM-based judge and actual human ratings on a held-out set. While the SQL-QA dataset partially mitigates this with real human evaluation, the central claim about aligning with human preferences on the public benchmarks rests on an unvalidated proxy. The paper is transparent about this limitation (Section 4.3: "the original people who labeled the data are unavailable"), but this does not substitute for validation. The concern is not that the judge is circular (it uses a different, stronger model: GPT-4o vs GPT-3.5), but that its fidelity as a human proxy is simply assumed without evidence.

### Minor

2. **Unclear data splits and evaluation protocol**: The paper does not explicitly specify how each dataset is partitioned into training, validation, and test sets for either the evaluator or responder task. For Table 2 (evaluator subtask), it is not stated whether reported RMSE/Accuracy values are from a held-out test set. For Table 3 (responder subtask), the paper mentions "test queries" without describing how these are obtained or whether they are disjoint from the evaluator's training samples. The datasets have standard splits (e.g., AES-ASAP's training set), but the paper should explicitly state the protocol.

3. **Undefined responder output metric in Figure 4**: The y-axis for the responder curves in Figure 4 is labeled "output scores for R" without specifying what metric this represents. The caption and text mention "output quality score" but never define whether this is a specific score from the pseudo-human judge, the evaluator module, or some other metric. The figure's utility for independent assessment is limited without this definition.

4. **Missing experimental specification details**: (a) The trivial metric L (Accuracy or MAE) used per dataset is not stated. (b) Algorithm 1 says "while P_E' is not yet optimized (converged)" with no convergence criterion defined. (c) The "single round" claim needs explicit confirmation for the reported experiments—the optional augmentation loop (Lines 17–22) creates ambiguity about which version was used.

5. **No confidence intervals, significance tests, or cost analysis**: Table 3 reports relative improvements without confidence intervals or statistical significance. The SQL-QA result (100 queries) reports a single accuracy number with no error bounds. The paper discusses human feedback efficiency but reports no LLM call counts or API costs for PLHF vs baselines.

6. **Missing experimental comparisons**: The related work cites Lin et al. (2024) as a relevant approach using dueling bandits for prompt selection with human feedback, but provides no experimental comparison. The evaluator subtask (Table 2) does not include a GPT-4o baseline (direct use, without optimization), even though GPT-4o is employed elsewhere in the paper.

### Trivial

None.

## Nice-to-Haves

- Validating the pseudo-human judge against actual human raters on a held-out subset of outputs from all compared methods would substantially strengthen the paper's central claim.
- Including a GPT-4o baseline for the evaluator task (Table 2) would provide a more complete picture.
- Reporting convergence criteria for Algorithm 1 and the exact trivial metric L used per dataset would improve reproducibility.
- Adding confidence intervals or standard errors to Table 3 results.

## Removed Points

1. **Criticism that the pseudo-human judge "creates a fundamental tension with the paper's own motivation" is retained as a Major weakness** (see Major #1 above) but the reviewer's framing that "the improvement reflects better alignment with... a particular LLM judge" is somewhat overstated—the pseudo-human judge uses a different, stronger model (GPT-4o) than the evaluator (GPT-3.5), so the comparison is not circular. The SQL-QA dataset provides independent human validation where PLHF also wins. The criticism is kept but reframed more precisely.
2. **Criticism about "the paper does not include a baseline where GPT-4o is used directly as the evaluator (without optimization)"**: Retained as Minor #6 (down-graded from the reviewer's implied severity—it is a useful addition but not a structural flaw).
3. **Criticism about "the paper's own framing argues that metrics are hard to define; these baselines confirm that point"**: This is not a genuine weakness—it is the paper's motivation. Removed.
4. **Specific suggestion to include "a version where GPT-4o is also prompt-optimized (e.g., using DSPy or TextGrad) as the evaluator during optimization"**: Moved to Nice-to-Haves—this is a natural extension, not a flaw in the current paper.
5. **Criticism about iterative augmentation undermining the "single round" claim**: The paper explicitly clarifies (Section 3.3) that batch tests stop at Line 16, so the basic version uses a single round. The ambiguity about which version was used in experiments is a fair concern kept in Minor #4, but the reviewer's broader criticism is downgraded.

## Novel Insights

The most intriguing finding is that PLHF's evaluator learned from few-shot human labels (using GPT-3.5 as base LLM) outperforms using a much stronger model (GPT-4o) directly as a generic judge in the prompt optimization loop. This suggests that task-specific alignment—even with a weaker model and limited data—can dominate raw model capability when the evaluator needs domain-specific preference understanding. This echoes RLHF findings at the prompt level: quality of preference data matters more than scale of the base model for alignment. The SQL-QA industrial deployment provides rare real-world evidence consistent with this pattern.

## Suggestions

1. **Validate the pseudo-human judge**: Collect human judgments on a held-out subset of outputs from all methods on at least one public dataset, and report correlation/agreement statistics (e.g., Spearman ρ, Cohen's κ) between the pseudo-human judge and actual human raters. This single addition would resolve the paper's most significant weakness.

2. **Add a GPT-4o-as-evaluator baseline to Table 2** to show whether prompt optimization on GPT-3.5 truly bridges the gap to a stronger model for the scoring task itself.

3. **Clarify experimental setup**: Specify data splits, the trivial metric L used per dataset, convergence criteria, and confirm whether experiments used the single-round (Line 16 termination) version. Define the y-axis metric for the responder in Figure 4.

4. **Report statistical significance or confidence intervals** for the main results, particularly the SQL-QA human evaluation which is the strongest evidence.

## Score and Decision

Reviewer's assessment: The paper proposes a novel and practically motivated framework for prompt optimization with limited human feedback. The idea is clear, the algorithm is well-specified, and the industrial validation provides meaningful real-world evidence. The main weakness is the reliance on an unvalidated LLM-based judge for public dataset evaluations, but this is partially mitigated by the SQL-QA results and the paper's transparency. The contribution is solid and the paper is well-organized. The experimental clarity issues are fixable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>