Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

## Summary

This paper proposes a method for zero-shot continuous prompt transfer between different language models. The key idea is to encode a source model's continuous prompt into a relative representation using cosine similarities to shared anchor tokens, then search for target prompt embeddings that preserve this relative structure. The method is evaluated on LAMA-TREx factual probing across six target models (BERT, RoBERTa, ALBERT base/large variants). The core contribution is achieving prompt transfer without requiring task supervision or training a neural projector on the target model.

## Strengths

- **Novel application of relative representation to continuous prompt transfer.** Encoding prompts relative to anchor tokens from a shared vocabulary and aligning in that space is a clean, well-motivated idea. The encoding eliminates the need for model-pair-specific projectors or parallel prompts, a genuine advancement over Su et al. (2022).

- **Self-transfer experiment validates the pipeline.** Transferring from BERT_base to BERT_base (same model) achieves 49.82% accuracy, nearly recovering the direct-tuning upper bound of 50.56%. This demonstrates that the relative encoding/search pipeline can faithfully reconstruct original prompts when embedding spaces are identical, providing a strong sanity check.

- **Empirical correlation between matching loss and transfer accuracy.** Figure 3 shows that as the cosine matching loss in relative space decreases during search, validation accuracy on the target model monotonically increases across several source–target pairs. This provides direct evidence for the paper's core hypothesis.

- **Thorough model coverage.** The evaluation spans BERT (base/large), RoBERTa (base/large), and ALBERT (base/large) as targets, with multiple source combinations. Ablations on normalization (Figure 5), anchor count, and prompt length (Figure 6) give a reasonably comprehensive picture of the method's behavior.

- **Identifies and explains why larger source models transfer worse.** The paper notes (Section 4.3) that BERT_large and RoBERTa_large as sources yield lower transfer accuracy, consistent with prior findings about the expressiveness of deep model embeddings. This insight validates the practical scenario of tuning a small model and transferring to a larger one.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation is limited to a single task (factual probing).** All experiments use LAMA-TREx, which involves template-like single-token prediction. The paper frames the contribution as generalizing "task semantics" across models, which implies applicability to classification, generation, or QA. Without evidence on at least one additional task (e.g., SuperGLUE, MMLU), the generality of the method remains unsubstantiated. The success could be specific to this one narrow setting.

- **Multi-source transfer claim is overstated.** The paper claims in the abstract and conclusion that multi-source transfer "can further enhance" performance. However, Table 2 (main results) shows several cases where dual-source transfer performs *worse* than the best single source. For example, on RoBERTa_base target, BERT_base+RoBERTa_base dual-source achieves 43.83% vs. the RoBERTa_base single-source self-transfer of 45.17%. On ALBERT_base and ALBERT_large, BERT_base+BERT_large dual-source (23.67, 22.32) is actually *worse* than the best single source (RoBERTa_base → ALBERT_base: 26.11; RoBERTa_base → ALBERT_large: 24.72). The paper cherry-picks cases where multi-source helps (ALBERT targets with BERT_base+RoBERTa_base) while glossing over cases where it hurts. No statistical significance is reported. This central claim needs more careful qualification.

- **Neural projector baseline is a simplified version, not the strongest comparator.** The paper trains the neural projector on anchor words only, not on task-specific prompt pairs as in Su et al. (2022). While this comparison is understandable within the paper's zero-shot framing (no task data on target), the paper's phrasing "largely outperforming baseline approaches such as training neural projectors" (abstract) and "our method yields consistent improvement compared with the neural projector" (Section 4.3) could mislead readers into thinking the method outperforms Su et al.'s full approach, which uses more supervision. The paper should acknowledge this limitation explicitly and clarify the comparison is against a simplified variant.

### Minor

- **Normalization is decoupled from the search objective.** Equation 7 applies post-hoc normalization to match the target model's embedding distribution, but this transformation is not accounted for in the matching loss (Eqn. 5). Since cosine similarity is not invariant to mean-centering, there is a potential mismatch between the relative representation that is optimized and the one that is actually used. The paper does not discuss this inconsistency. While the ablation (Figure 5) shows it works empirically, the theoretical gap remains unaddressed.

- **Anchor selection is underspecified.** The paper says anchors are "shared tokens" (Section 3.2) and varies the number of anchors in ablation (Figure 6), but never describes *how* the subset of anchors is selected when k < total shared vocabulary (e.g., k=512 vs. the full 17,230). Are anchors chosen randomly? By frequency? The selection method could affect results, and its absence hurts reproducibility.

- **No variance or significance reporting.** All results are presented as single-point estimates with no error bars, confidence intervals, or multiple random seeds. Given the stochastic nature of gradient-based search, this makes it difficult to assess the reliability of the reported improvements, especially the small margins (e.g., 1–2 point gains in multi-source settings).

### Trivial
- The "zero-shot" terminology could be clarified: the method requires gradient-based search on the target model's embedding layer, which is not zero-shot in the sense of "no computation" — but the paper's usage (meaning "no task supervision on the target") is standard in the prompt-tuning literature. A brief clarification of the computational cost relative to direct tuning would help.

## Nice-to-Haves

- **Report per-relation accuracy.** The 41 relations in LAMA-TREx are diverse; micro-averaging could mask that the method works well on some relations and poorly on others. A per-relation breakdown (e.g., a table or scatter plot) would reveal where the method succeeds and fails.

- **Compare against few-shot prompt tuning on the target model.** Since the method requires gradient access to the target model anyway, a natural baseline is to tune the prompt with a small number of labeled examples on the target. This would contextualize the practical value of the "zero-shot (no task data)" claim.

- **Include source prompt performance.** The paper does not report the original source prompt's accuracy on the source model, making it hard to assess how much task semantics is preserved. Adding this would strengthen the analysis.

## Removed Points

- **"Not zero-shot" (gradient concern)**: The critic claimed the method "is not zero-shot in the common sense" because it requires gradient-based search on the target embedding layer. In the NLP prompt-tuning literature, "zero-shot transfer" standardly means *without task-labeled data on the target model*, not *without any computation*. The paper consistently uses the term in this standard sense (lines 20, 26). This criticism reflects a misunderstanding of field terminology. MOVED FROM REVIEW.

- **"Neural projector self-transfer poor → implementation is bad"**: The critic notes the neural projector's self-transfer numbers are low (e.g., BERT_base self → 26.82) and infers the implementation is poor. The low performance is expected and consistent with the paper's framing: training a projector on anchor words alone (without task-specific prompt pairs) is a weaker signal. The paper acknowledges this. This is not a weakness. REMOVED.

- **"LAMA has known biases"**: This is a generic criticism applicable to most work using LAMA, not specific to this paper's methodology. The paper follows standard practices from prior work. REMOVED.

- **Strength about "multi-source consistent improvement"**: The Strength Finder claimed multi-source yields "consistent improvement over the best single source." This conflicts with the verified weakness (many cases where dual-source underperforms the best single source). Per the meta-review rules, when a strength and verified weakness disagree, the weakness wins. MOVED FROM STRENGTHS.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation that synthesizes across the paper's results beyond what the authors already discuss.

## Suggestions

1. **Add at least one additional task domain** (e.g., SuperGLUE classification or MMLU multiple-choice) to demonstrate generalizability beyond factual probing.
2. **Qualify the multi-source claim** by acknowledging cases where it underperforms single-source transfer and reporting which conditions favor multi-source.
3. **Clarify the neural projector baseline** by explicitly stating it is a simplified variant trained on anchor words only, not the full Su et al. (2022) approach.
4. **Describe the anchor selection procedure** for subsets (k < total shared vocabulary) to improve reproducibility.
5. **Report results with error bars** across multiple random seeds for the search initialization.

## Score and Decision

This paper presents a novel and well-motivated idea — using relative representations for zero-shot prompt transfer. The self-transfer validation and the correlation between matching loss and accuracy provide reasonable evidence that the pipeline works. However, the experimental validation is too narrow to support the paper's general claims. Restricting evaluation to a single task (factual probing), overstating multi-source transfer, and comparing against a simplified neural projector baseline all limit the strength of the contribution. The core idea is promising, but the current evidence is insufficient for acceptance at a top-tier venue.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>