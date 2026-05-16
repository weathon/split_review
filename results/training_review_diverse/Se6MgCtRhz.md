Now I have a thorough understanding of the paper and all claims. Let me compose the consolidated review.

## Summary

This paper presents Herald, a pipeline for generating natural-language–formal-language (NL-FL) parallel data from Mathlib4 using structural information (dependency graphs, hierarchical translation order, RAG). The resulting Herald dataset contains 580k NL-FL statement pairs and 44k proof pairs. The authors fine-tune DeepSeek-Prover-Base 7B on this dataset to create the Herald translator, achieving 93.2% Pass@128 on miniF2F-test and 22.5% on an internal graduate-level dataset, outperforming TheoremLlama (50.1%) and InternLM2-Math-Plus-7B (73.0%). They also demonstrate autoformalization of a Stacks Project section.

## Strengths

- **Dependency-aware hierarchical translation order.** The paper identifies that missing NL annotations for dependent definitions cause translation errors and solves this by stratifying statements into dependency levels and translating them in order (Section 3.1.1). This is a genuine structural improvement over methods that translate theorems in isolation.

- **Tactic-based augmentation producing 580k valid statements.** By decomposing tactic proofs into intermediate subgoal states, the pipeline generates new, syntactically valid formal statements that are provable and semantically grounded (Section 3.2.1, Figure 3). This directly addresses data scarcity while preserving correctness.

- **State-of-the-art formalization accuracy.** The Herald translator achieves 93.2% Pass@128 on miniF2F-test and 22.5% on an internal graduate-level textbook dataset, substantially outperforming strong baselines including TheoremLlama (50.1%), InternLM2-Math-Plus-7B (73.0%), and Llama3-instruct (28.2%) (Table 1). These results are impressive regardless of attribution.

- **Multi-strategy informal augmentation.** Four augmentation strategies (logical equivalence rewriting, abstract concept substitution, omission of implicit conditions, multilingual translation) generate diverse NL statements that better mimic real mathematical language distributions (Section 3.2.2).

- **Expert human feedback iteration over six rounds.** Five PhD mathematicians in pure mathematics with Lean expertise provided iterative feedback, yielding over a dozen principles incorporated into prompts (Section 3.1.1). This level of human validation during pipeline development is a strength not present in most prior NL-FL dataset generation work.

- **End-to-end formalization of a graduate-level textbook section.** The pipeline successfully auto-formalized a section of the Stacks Project (Normal Extensions) with only two manual theorem modifications (Section 4.3), demonstrating practical viability beyond toy benchmarks.

## Weaknesses

### Fatal
None.

### Major

- **Missing base model ablation.** The Herald translator is fine-tuned from DeepSeek-Prover-Base 7B, a model extensively pre-trained on formal programming languages like Lean. The paper reports no comparison against DeepSeek-Prover-Base 7B *without* Herald fine-tuning on the same test sets. Without this control, it is impossible to determine how much of the 93.2% miniF2F performance is attributable to the Herald dataset vs. the base model's inherent capabilities. The comparison against TheoremLlama (also fine-tuned on NL-FL Lean data) is fair, but the marginal contribution of Herald over the base model is unknown. This is a structural gap in the evaluation that weakens the paper's central empirical claim. Adding a "DeepSeek-Prover-Base 7B (zero-shot)" row to Table 1 is essential.

### Minor

- **Internal test datasets poorly specified.** The Extract Theorem and College CoT datasets are described in only one sentence each (Section 4.1.3): the former as "theorems from advanced undergraduate-level textbooks using OCR" and the latter as "digital mathematics resources...filtered using an LLM." No details are given about which textbooks, the number of source documents, overlap analysis with Mathlib4 training data, or the specific filtering methodology. Since these datasets account for a large portion of the empirical contribution (22.5% vs 17.1% results), the lack of transparency makes these results difficult to interpret.

- **No systematic human evaluation of dataset quality.** The Herald dataset is presented as a primary contribution (580k statements), yet its quality is assessed only through a brief qualitative case study (Section 4.2) with summary-level observations ("notations are well-written or poorly copied from formal language"). The paper mentions five PhD student annotators who provided feedback during pipeline development, but no human evaluation of the *final dataset* — no sample-wise correctness rate, no inter-annotator agreement, no comparison with alternative NL annotations. The downstream formalization results provide indirect validation, but for a dataset paper, some direct human quality assessment would substantially strengthen the contribution.

- **Inconsistency in reported TheoremLlama scores.** The abstract (line 5) correctly reports TheoremLlama's miniF2F-test as 50.1% (matching Table 1), but the introduction body (line 22) and contribution bullets (line 29) report 55.0%, which corresponds to the validation set score (55.6%) rather than the test set. This inconsistency undermines trust in the paper's reporting precision.

- **Validation pipeline not calibrated against human judgment.** The evaluation pipeline (translation → compiler check → LLM back-translation → NLI check, Section 4.1.2) uses InternLM2-Math-Plus-7B and DeepSeek Chat v2.5 for the latter two stages, which themselves have error rates. The paper provides no human calibration — no false-positive/negative rate for the pipeline relative to human judgment — so the absolute accuracy numbers (93.2%, 22.5%) may be overestimates. Since the same pipeline is applied to all models, relative comparisons are more reliable than absolute numbers.

- **Missing methodological details for reproducibility.** The paper mentions "over a dozen principles" from human feedback but does not disclose them (Section 3.1.1). The retrieval embedding model and similarity function are not specified (Section 3.1.1). The quality control for LLM-based informal augmentation (what fraction of augmented statements contain errors?) is absent (Section 3.2.2). The deduplication step is described only as "randomly sample a subset" (Section 3.2.1). These gaps limit reproducibility.

- **OpenHermes2.5 mixing not ablated.** The training recipe mixes NL→FL, FL→NL, and 20% OpenHermes2.5 general-domain data (Section 4.1.1). The effect of this general-language data on formalization performance is not isolated. A small ablation removing it would clarify whether the improvement comes from the Herald data or from improved language modeling via the general corpus.

### Trivial
None.

## Nice-to-Haves

- A limitations section discussing dataset coverage gaps across mathematical subfields, potential stylistic biases in LLM-generated NL annotations, and the risk that the validation pipeline may reject correct but unconventionally phrased formalizations would strengthen the paper.
- The retrieval component (1,000 manually annotated examples) could be ablated to show its contribution to translation quality.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about ".5 \citep{deepseekproverv15}" being a garbled fragment (Section-by-Section Notes).** This appears to be a parser/formatting artifact from PDF extraction, not an author error. The instruction requires removing formatting artifact criticisms.
- **Claim that "baselines are evaluated without fine-tuning on analogous data."** TheoremLlama is itself a model fine-tuned on NL-FL Lean data, making the claim partially inaccurate for that baseline. However, the core concern about missing the DeepSeek-Prover-Base 7B ablation (above, under Major) is retained and valid.
- **Criticism about "the abstract misstates TheoremLlama (50.1% and 4.0%)" and the "second number is 2.9%, not 4.0%."** The abstract pairs miniF2F-test (50.1%) with Extract Theorem (4.0%) when comparing against Herald's 93.2% and 22.5%. This is a coherent comparison of the first two columns of Table 1; it does not claim 4.0% for College CoT. No misstatement.
- **Generic formatting/style nitpicks** (not present in the harsh review, but noting for completeness).
- **Criticism about "missing related works"** — not confirmed by available sources.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation about the work that the paper itself does not state.

## Suggestions

1. **Add the missing base model ablation.** Run DeepSeek-Prover-Base 7B (zero-shot, few-shot) on all three test sets and add it as a row in Table 1. This is the single most important improvement. If the gain from Herald fine-tuning is substantial (e.g., >15 percentage points on miniF2F), the paper's core claim is validated.

2. **Provide a human evaluation of dataset quality.** Sample 100–200 NL statements from the Herald dataset and have mathematicians rate (a) mathematical correctness, (b) naturalness of language, (c) faithfulness to the original formal statement. Report these statistics.

3. **Calibrate the validation pipeline.** On a subset of accepted translations, have a human check whether the formalization is actually correct. Report the pipeline's false-positive rate.

4. **Improve documentation of internal test sets.** Describe the source textbooks, number of samples per source, filtering methodology, and overlap analysis with Mathlib4 for Extract Theorem and College CoT.

5. **Resolve the TheoremLlama score inconsistency** (55.0% vs 50.1%) between the introduction and Table 1.

6. **Disclose key methodological details** — the embedding model used for retrieval, a representative sample of the human-feedback principles, and the specific LLM(s) used for informal augmentation.

## Score and Decision

The paper presents a novel pipeline with genuine structural innovations (dependency-aware hierarchical translation, tactic-based augmentation) and produces a large-scale dataset that achieves impressive SOTA results. The primary contributions are real and well-motivated. However, the evaluation has a significant gap: the missing base model ablation makes it impossible to disentangle the dataset's contribution from the base model's prior training. The internal test datasets are poorly documented, and the dataset quality lacks systematic human assessment. These weaknesses are addressable, and the underlying work has sufficient merit to warrant acceptance with the expectation that the authors will provide the base model ablation in the final version.

**Score:** 6.0

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>