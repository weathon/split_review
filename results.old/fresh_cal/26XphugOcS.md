Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes a zero-shot method for transferring continuous prompts between different language models. The approach encodes source prompt embeddings into a relative space defined by cosine similarities to shared anchor tokens, then searches for target embeddings that reconstruct those relative positions. The method is evaluated on LAMA factual probing across BERT, RoBERTa, and ALBERT models.

## Strengths

- **Novel encode-then-search strategy for zero-shot prompt transfer**: Sections 2.2–2.3 propose encoding source prompt embeddings into a relative space using shared anchor tokens, then searching for target embeddings that match these relative representations. Unlike prior neural projector methods (Su et al., 2022) that require parallel prompts or task supervision on the target model, this approach enables true zero-shot transfer without additional training — a clearly motivated and methodologically clean contribution.

- **Multi-source transfer improves generalization**: Section 2.4 introduces a multi-source objective (Eqn. 9) that maximizes similarity to relative representations from multiple source models. The main results table shows that dual-source BERT_base+RoBERTa_base achieves 27.13% on ALBERT_large, outperforming the best single source (RoBERTa_base 24.72%) by ~2.4 points, demonstrating that combining relative representations from multiple models enhances transferability.

- **Empirical link between relative-space matching and transfer accuracy**: Figure 1 shows a monotonic relationship across source-target pairs where decreasing matching loss corresponds to increasing validation accuracy, directly supporting the paper's core assumption that alignment in relative space captures transferable structure.

- **Normalization ablation validates cross-model adaptation**: Figure 2 demonstrates that the normalization treatment (Eqn. 7) provides substantial accuracy gains (often 10–20% absolute) when source and target models differ, while causing only minimal degradation in identical-model cases — confirming its necessity for effective transfer.

- **Robustness to hyperparameter choices**: Figure 3 shows that transfer accuracy varies smoothly with anchor count (512–17230) and prompt length (1–10), with clear trends and only modest degradation at extremes, indicating the method is not brittle to parameter selection.

## Weaknesses

### Fatal
None.

### Major

- **Scope-claim mismatch: title/abstract claims exceed experimental coverage.** The paper's title asserts "Generalizing Task Semantics Across Language Models" and the abstract claims that "task semantics in continuous prompts can be generalized across various language models." However, the entire experimental evaluation is conducted on a single task family — factual probing (LAMA-TREx, 41 relations). While the 41 subtasks provide reasonable breadth within factual probing, there is no evidence that the method transfers to other NLP task types (e.g., classification, NLI, generation). The method itself is task-agnostic in design, and results on factual probing are solid, but the broad narrative language ("task semantics," "across language models") implies generality that the experiments do not establish. The conclusion also claims that "smaller source models [can] act as effective 'soft prompt engineers' that perform better than manual prompting" — but this claim is not uniformly supported across all source-target pairs in the results (see Minor weakness below). The paper would be stronger by either (a) demonstrating transfer on at least one additional task type, or (b) explicitly scoping claims to factual probing.

### Minor

- **Claim of surpassing manual prompting is inconsistently supported.** The paper states (line 216) that "prompts transferred from the base models of BERT and RoBERTa surpass the manual prompting baseline." Cross-checking Table 5 against the manual baselines (Table 3): BERT_base surpasses manual on 2 of 6 target models (49.82 vs 30.64 for self-transfer, 20.83 vs 18.63 for ALBERT_base), but falls short on the other 4 (e.g., 31.40 vs 32.22 on BERT_large; 17.68 vs 20.48 on RoBERTa_base). RoBERTa_base surpasses manual on 4 of 6 (e.g., 25.09 vs 23.59 on RoBERTa_large; 26.11 vs 18.63 on ALBERT_base). The pattern is promising but not universal, and the blanket statement should be qualified.

- **No variance estimates reported.** The main results (Tables 3–5) are reported as single numbers. The search process in Eqn. (6) starts from randomly initialized target embeddings and uses gradient-based optimization, which may converge to different solutions across runs. Without multiple runs, standard deviations, or confidence intervals, it is difficult to assess the reliability of the reported improvements — particularly for small gains (e.g., 1–2 percentage points in multi-source settings). Adding error bars for at least the main comparisons would substantiate the results.

- **No limitations section.** The paper acknowledges no limitations of the proposed approach. Key limitations worth discussing include: (a) the method depends on a shared tokenizer/vocabulary and may fail when source and target models use very different tokenizations; (b) the search process requires access to the target model's embedding matrix and gradient computation, which is not entirely "parameter-free"; (c) experiments are limited to masked LMs — autoregressive models are not tested.

### Trivial
None.

## Nice-to-Haves

- A "nearest neighbor in relative space" baseline (matching averaged anchor similarities without gradient search) would be a useful sanity check to isolate the benefit of the search procedure from the relative encoding itself.
- The concluding remark about brain signals (line 287) is speculative and detracts from the otherwise technically focused paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about missing implementation details (optimizer, learning rate, steps for Eq. 6):** The paper states "randomly initialized" and "gradient descent." The parser strips appendix sections where such details may reside; this cannot be verified as an omission.
- **Criticism about the brain signals comment in the conclusion:** This is an editorial opinion about a single speculative sentence, not a substantive weakness in the paper's technical contribution. It does not affect evaluation.
- **Strength Finder's claim about "the single most important evidence":** The core claim is already captured under the first strength; that framing added no new information.
- **Generic scope-criticism ("the paper should test on more tasks" as a fatal flaw):** Retained as a Major weakness above but softened from "fatal" — the method is task-agnostic and the paper provides extensive evaluation within its chosen domain.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the work that the paper itself does not articulate.

## Suggestions

1. **Narrow the framing.** Revise the title, abstract, and conclusion to reflect that transfer is demonstrated on factual probing tasks. Replace "generalizing task semantics" with something like "zero-shot transfer of continuous prompts on factual probing" unless additional task domains are added.
2. **Add variance estimates.** Report results averaged over multiple runs (≥5) with standard deviations for at least the main comparisons in Table 5.
3. **Add a limitations section.** Acknowledge the shared-vocabulary requirement, the need for target-model access, and the scope of evaluation.
4. **Qualify the "surpass manual" claim.** State the specific source-target combinations where the method surpasses or approaches manual prompting, rather than making a blanket statement.
5. **Consider adding one more task type** (e.g., sentiment classification with prompt tuning) to substantiate the broader claim of task-semantic transfer — though this is a suggestion for strengthening, not a requirement for acceptance given the paper's current contributions.

## Score and Decision

This paper presents a novel and well-motivated method for zero-shot continuous prompt transfer. The encode-then-search strategy using relative representations is clean, the experimental setup is carefully constructed, and the analysis (correlation between matching loss and accuracy, normalization ablation, hyperparameter robustness) convincingly supports the internal validity of the approach. The method clearly outperforms the discretization and neural projector baselines across nearly all settings. However, the paper's framing overreaches the evidence: the broad title claim about "generalizing task semantics" is not matched by experiments limited to factual probing, and the claim of surpassing manual prompting is inconsistently supported. The absence of variance estimates is a secondary concern. The paper makes a genuine contribution to prompt transfer research — the core idea is sound and the factual-probing results are strong — but the presentation inflates the scope. This is a solid paper that should be accepted with substantive framing revisions.

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**