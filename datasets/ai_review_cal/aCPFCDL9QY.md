- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

The paper proposes SELF-PARAM, a method that injects contextual knowledge into LLM parameters by minimizing the KL divergence between the original model's predictions (conditioned on context) and a target model's predictions (without context). The training uses GPT-4o-mini-generated QA pairs plus unrelated sentences from SlimPajama. Experiments cover single/batch/sequential context injection on PwC (QA-F1) and conversational recommendation on INSPIRED/REDIAL (Recall@1). The method requires zero additional storage at inference.

## Strengths

1. **Strong single and batch context injection results with zero storage overhead.** In Table 1, SELF-PARAM achieves QA-F1 of 0.4927 on OpenLLaMA-3B-v2 (single context), closely approaching the oracle (Base, C+Q: 0.5043) and far outperforming FT (S) at 0.2742. In Table 2 (batch injection), SELF-PARAM consistently beats DPR, BM25, InfLLM, and MemoryLLM across all three backbone sizes (3B/7B/8B) and both context counts (100/500), while requiring zero storage complexity (S=0) — these baselines require O(n) or O(1) storage.

2. **Well-motivated method with a clear intuition.** The paper defines context injection formally (Eq. 1–2) and provides an intuitive explanation (Section 3.3, "David likes apples" example) for why KL divergence is superior to next-word prediction loss for knowledge injection. The construction of the target sentence set with both context-related QA pairs and unrelated sentences is a practical design that balances injection and stability.

3. **Comprehensive evaluation across multiple tasks and model scales.** Experiments span single injection (3 models), batch injection (3 models × 2 context sizes), sequential injection (50 sequences × 20 steps), and conversational recommendation (2 datasets × 4 filtering scenarios). This breadth supports the paper's claims of generality.

## Weaknesses

### Fatal
None.

### Major

1. **SELF-PARAM exceeds the supposed upper bound (Base, C+Q) on OpenLLaMA-3B-v2 in batch injection.** In Table 2, for 100 contexts, SELF-PARAM achieves 0.5082 vs. Base C+Q at 0.5043; for 500 contexts, 0.5048 vs. 0.4869. The paper explicitly states that "Base, C+Q" (providing the model with the specific context containing the answer for each question) serves as the upper bound. If the C+Q condition indeed provides only the single relevant context per question, then SELF-PARAM should not beat it. This anomaly is not discussed. Possible explanations (e.g., context-length degradation in C+Q when many contexts are involved, or evaluation alignment differences) need to be ruled out or acknowledged. The fact that the anomaly is isolated to OpenLLaMA-3B-v2 (Mistral-7B and Llama3-8B stay below the oracle) suggests it may be explainable, but the paper's silence on the issue undermines confidence in the batch injection results.

2. **Sequential injection lacks any comparison baselines.** Figure 1 shows only SELF-PARAM's QA-F1 decaying from ~0.5 to ~0.3 over 20 sequential injections, compared to the base model at ~0.14. Without comparisons to FT (C), FT (S), model editing methods (MEND, ROME, MEMIT), or simple rehearsal-based approaches in the same sequential setting, the claim of "robust long-term retention" is unsupported. The 40% drop from peak is also difficult to evaluate without knowing what strong baselines achieve. This is the paper's own identified retention test, and the baseline gap is significant.

### Minor

3. **Fine-tuning baselines produce zero recall in conversational recommendation (Table 3), suggesting possible misconfiguration.** Both FT (C) and FT (Q) achieve 0.0000 Recall@1 across all scenarios on both INSPIRED and REDIAL. The paper's explanation ("divergent styles between recommendation conversations and the original instruct models") is plausible but unverified. Without sample outputs or diagnostic analysis confirming the fine-tuned models can still follow the instruction format, it is unclear whether these baselines are meaningful comparisons — any method producing non-zero output trivially beats them. Additionally, all methods (including SELF-PARAM) achieve very low absolute R@1 values (0.02–0.04), which raises questions about the practical significance of the task as set up.

4. **No variance or statistical significance reported.** All results in Tables 1–3 are single point estimates. Given that some differences are very small (e.g., Table 3 differences of 0.002–0.008), it is unclear which gaps are reliable. The OpenLLaMA anomaly (difference of 0.0039 for 100 contexts) could plausibly be within noise.

5. **No ablation on QA pair quantity or diversity.** The method's success depends on GPT-4o-mini-generated QA pairs. The paper does not analyze how the number of generated pairs per context, their diversity, or the ratio of QA pairs to unrelated sentences affects performance. Sensitivity to these choices is unknown.

6. **Token-level implementation of the KL objective is not specified.** Equation (2) states the KL divergence at the sentence level, but the practical implementation (token-level soft distillation vs. approximation) is not described. While a reader familiar with knowledge distillation can infer the standard practice, more precision would aid reproducibility.

### Trivial

- Notation inconsistency: Eq. (2) uses `P_θ(s|x)` but the Figure 1 caption uses `P(s|x+p, θ)`. The intended correspondence is clear but should be unified.

## Nice-to-Haves

- An ablation on the number of generated QA pairs per context and their diversity.
- Sequential injection comparisons to at least FT (C) and FT (S) in the same setting, and ideally model editing baselines.
- Variance estimates (error bars) across runs.
- Controlled experiments isolating context-length effects in the "Base, C+Q" oracle condition to explain the OpenLLaMA anomaly.
- A discussion of the cost/dependency on GPT-4o-mini for QA generation as a limitation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- The harsh critic's claim that "FT (S) and SELF-PARAM are the same method under different names." This is factually wrong. SELF-PARAM uses KL divergence between teacher and student distributions (Eq. 2), while FT (S) uses standard NWP/cross-entropy on the same data. These are different optimization objectives, and the paper explicitly discusses why KL divergence is preferable (Section 3.3).
- The harsh critic's claim that the notation "P_θ(s|x)" (Eq. 2) versus "P(s|x+p, θ)" (Figure 1) constitutes a structural inconsistency. This is a minor notational abbreviation — the figure caption and method description both make the intended meaning clear.
- The harsh critic's question "why should minimizing divergence on random sentences help answer questions about x" — the paper explicitly addresses this in Section 3.3 with the "David likes apples" example, explaining that KL divergence encourages generalization beyond surface forms.
- The harsh critic's claim that the method is "a form of distillation" and does not handle complex experiences better — the paper's comparison to prior distillation work (Section 2) focuses on the difference in data construction (generated QA pairs + unrelated text, not just factual statements/prompts), which is a verifiable distinction.
- The Strength Finder's generic strengths about "important problem" and "well-motivated training objective" — these are superficial and not specific enough to the paper's concrete contributions.

## Novel Insights

None beyond the paper's own contributions. The two reviewers largely validated the paper's stated claims and identified gaps the authors themselves should address; no latent insight or angle was surfaced that the paper does not already articulate.

## Suggestions

1. **Address the OpenLLaMA anomaly explicitly.** Either show that "Base, C+Q" in batch injection involves concatenating all contexts (leading to length-driven degradation), or acknowledge the issue and explain why SELF-PARAM might legitimately exceed this bound on smaller models. Including variance estimates would also help clarify whether the gap is meaningful.
2. **Add baselines to sequential injection.** At minimum, include FT (C) and FT (S) in the same sequential LoRA+merge setup. A rehearsal baseline (storing a small buffer of prior context) and a model editing baseline (e.g., MEMIT) would substantially strengthen the retention claim.
3. **Diagnose the zero-recall fine-tuning baselines in conversational recommendation.** Show sample outputs from FT (C)/FT (Q) to verify whether the model has catastrophically forgotten the task format or is generating empty/near-empty responses.
4. **Clarify the token-level implementation of the KL objective.** State whether token-level soft labels from the teacher are used, or whether an approximation is employed. This takes one sentence but substantially aids reproducibility.
