Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes a zero-shot method for transferring continuous prompts between different language models (e.g., BERT, RoBERTa, ALBERT) using relative representations. The approach encodes source prompt embeddings into a relative space defined by cosine similarities to shared anchor tokens, then searches for target prompt embeddings that preserve this relative structure. The method is evaluated on the LAMA-TREx factual probing benchmark (41 relation subtasks) and compared against discretization and neural projector baselines. The paper also explores multi-source transfer by combining prompts from multiple source models.

## Strengths

- **Zero-shot transfer outperforms trained baselines across diverse model pairs.** The encode-then-search method consistently beats the neural projector baseline (which requires training on target model data), often by large margins. For example, BERT_base → BERT_large yields 31.40% accuracy versus 12.49% for the neural projector (Table 3), and the method exceeds manual prompting on several target models. This is a genuinely novel capability.

- **Cross-architecture transfer works despite differing embedding dimensions.** The method successfully transfers prompts from BERT (d=768) to ALBERT (d=128) and other dimension-mismatched pairs where direct transfer is impossible. Table 3 shows consistent positive transfer to all ALBERT variants, validating the method's generality across architectures.

- **Multi-source transfer provides consistent (though modest) improvements on held-out architectures.** Combining BERT_base + RoBERTa_base as sources achieves the best results on ALBERT_base (27.13%) and ALBERT_large (26.54%), outperforming all single-source transfers. This provides proof-of-concept that multi-source integration can yield a more robust view of task semantics.

- **Ablation studies validate key design choices.** The analysis of anchor number and prompt length (Figure 4) shows monotonic improvement with more anchors up to a point, identifies 5 as the optimal prompt length, and demonstrates robustness to hyperparameter variation — providing concrete guidance for practitioners.

## Weaknesses

### Fatal

None.

### Major

- **Evaluation is restricted to a single task type (factual probing).** The entire experimental evaluation is conducted on LAMA-TREx, a factual knowledge benchmark involving single-entity prediction. While 41 relation subtasks provide diversity within this task, the paper's framing — "task semantics" and "generalizing task semantics across language models" — implies a broader scope. The method's effectiveness on other task types (e.g., sentiment classification, NLI, text generation) is entirely unknown, and the paper offers no argument that the relative-space approach should transfer to tasks with fundamentally different output structures. This does not invalidate the contribution, but it means the paper's central claim is narrower than the title and framing suggest. The authors should either restrict their claims to factual probing or demonstrate transfer on at least one additional task type.

### Minor

- **The gradient-based search procedure (Section 3.2) is underspecified for reproducibility.** Equation 5 (the core optimization) is described only as "can be accomplished by gradient descent," but the paper omits: learning rate, number of gradient steps, initialization scheme (beyond "randomly initialized"), optimizer choice, and stopping criterion. These are not trivial implementation details — they directly affect the quality of the transferred prompt. The paper should report these parameters.

- **No quantitative correlation measure is provided for the matching loss vs. accuracy relationship.** The paper claims the correlation between matching loss and validation accuracy is "highly consistent across all source–target combinations" and "convincingly" supports the core intuition, but provides only a qualitative figure (Figure 2) and no correlation coefficient. Given that the cross-model transfer accuracy changes appear small over the depicted loss range, a quantitative measure (Pearson/Spearman ρ) per source–target pair would meaningfully strengthen the claim or honestly calibrate it.

- **Multi-source gains on the most informative setting (cross-architecture) are small and unreported with statistical significance.** For ALBERT_base and ALBERT_large — the target models where neither source matches — the dual-source improvement over the best single source is only 1.0–1.8 percentage points (Table 3). No error bars, confidence intervals, or significance tests are reported anywhere in the paper. The gains may be real but could also fall within noise; the paper should acknowledge this limitation and report variance across the 41 subtasks.

- **The independent optimization of each prompt token ignores sequential structure.** The method optimizes each virtual token v_i^t independently (Eqn. 5, repeated for i=1,...,m) without considering joint interactions among prompt tokens. Continuous prompts are typically learned as a sequence whose joint effect matters for model behavior. The paper does not discuss this assumption, test whether joint optimization yields different results, or provide justification for token-wise independence.

- **Anchor selection procedure is not specified.** The paper uses "shared tokens" between source and target models as anchors, and selects 8,192 out of 17,230 shared tokens. However, it does not specify how shared tokens are identified across different tokenizers (exact string match? subword handling?) or how the 8,192 subset is chosen (random? most frequent?). These details affect reproducibility.

- **The neural projector baseline description is underspecified.** The paper trains "a two-layer projector to map the source embedding space to the target one based on anchor words" but does not clarify whether this projector was trained solely on anchor embeddings or also on paired prompt data, nor what training protocol was used. This affects the fairness of the comparison.

### Trivial

- The paper attributes lower transferability of large source models (BERT_large, RoBERTa_large) to "model specificity" and "high expressive power." While this explanation is supported by prior work, the paper provides no direct analysis (e.g., embedding norms, variance, reconstruction error) to substantiate the claim. This is a minor observation, not a flaw.

- The direct-transfer results (Table 1) are presented as a standalone experiment with the justification that they only apply when dimensions match. This is reasonable, but incorporating these into the main comparison framework would be cleaner.

## Nice-to-Haves

- Report per-relation breakdowns for representative source–target pairs to show the method works across diverse factual relations and is not driven by a few easy cases (these may already be in the appendix, which the parser strips).
- Provide a rough computational cost comparison (e.g., seconds per prompt per target model) to contextualize the claim that the method avoids "excessive gradient computations."
- Report the source model's own prompt tuning accuracy (e.g., BERT_base on LAMA with OptiPrompt) to give context for what "upper bound" the transfer is approaching.

## Removed Points

- **"Direct transfer should be in main table"** — The paper explicitly explains why direct transfer is presented separately: it is only feasible when source and target embedding dimensions match, so it does not fit the main comparison. This is a reasonable methodological decision, not an omission.
- **"Normalization formula is unusual and not well motivated"** — The paper clearly motivates the normalization (Eqn. 6) as addressing the magnitude insensitivity of cosine similarity, and provides an ablation study confirming its benefit. The reviewer's concern is not supported by the paper content.
- **Criticisms about missing appendix content or per-relation breakdowns** — The paper states "We provide additional results in the appendices." The parser strips appendix content; these likely exist in the original submission.
- **"Complaints about the paper not covering additional domains/tasks as core weaknesses"** — The single-task limitation is already captured in Major weaknesses; repeated demands for further breadth are scope creep.
- **Formatting/style nitpicks and claims about typos** — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel perspective on the method that the authors themselves have not already identified.

## Suggestions

1. Add at least one additional task type (e.g., sentiment classification on SST-2 or NLI on MNLI) to demonstrate cross-task generality. This is the single most impactful improvement.
2. Report quantitative correlation measures (Pearson/Spearman ρ) between matching loss and accuracy for each source–target pair in Figure 2.
3. Provide complete search hyperparameters: learning rate, number of steps, optimizer, initialization scheme, stopping criterion.
4. Add error bars or confidence intervals (e.g., standard deviation across 41 subtasks or multiple random seeds) for key results.
5. Clarify: (a) how shared tokens are identified across tokenizers, (b) how the 8,192 anchors are selected from the shared vocabulary, and (c) the training protocol for the neural projector baseline.
6. Test joint optimization of prompt tokens (backpropagating through all m tokens simultaneously) and compare to independent search, or at minimum discuss the independence assumption.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>