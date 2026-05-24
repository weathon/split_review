Now I have a thorough understanding of the paper and all the review claims. Let me compose the final review.

---

## Summary

This paper proposes an approach to produce smaller LLMs from larger pre-trained models via (1) **targeted structured pruning**, which prunes a source model to a pre-specified target architecture using Lagrange-multiplier-constrained optimization, and (2) **dynamic batch loading**, which adjusts domain sampling proportions during continued pre-training based on domain-specific loss gaps to a reference model. The method is instantiated as Sheared-LLaMA (1.3B and 2.7B) by pruning LLaMA2-7B. The resulting models match or outperform open-source small models (Pythia, OpenLLaMA, TinyLlama, INCITE) using only ~50B tokens of post-pruning compute, compared to the 300B–3T tokens used to train those baselines from scratch.

## Strengths

1. **Targeted structured pruning to arbitrary architectures is a genuine technical contribution.** The constrained-optimization formulation (Eq. 1, Lagrange multipliers on layers, heads, hidden/intermediate dimensions, lines 152–170) allows pruning to any pre-specified target architecture (e.g., Pythia-1.4B, INCITE-3B) rather than producing irregular shapes like prior work. The paper verifies that uniform architectures yield faster inference than non-uniform pruning at matched sparsity (Table 3).

2. **Dynamic batch loading is convincingly shown to reduce domain loss disparity and improve downstream performance.** Figure 3 shows that dynamic loading nearly equalizes loss gaps across domains (C4, GitHub, Book, etc.) compared to static data proportions, and Figure 4 confirms that this translates to better downstream task accuracy throughout continued pre-training. The ablation in Figure 4 directly isolates the contribution of this component.

3. **Strong empirical results against substantially more expensive baselines.** Sheared-LLaMA-2.7B outperforms OpenLLaMA-3B-v2, INCITE-Base-3B, and OpenLLaMA-3B-v1 on the majority of 11 evaluated tasks (Table 2), while using 50B tokens vs. 800B–1T tokens for those baselines. Sheared-LLaMA-1.3B outperforms TinyLlama-1.1B (3T tokens) and Pythia-1.4B (300B tokens). Instruction tuning win rates (GPT-4 evaluation, Figure 2) show further advantages.

4. **Practical ablation on pruning vs. continued pre-training budget allocation** (Table 5): systematically varies token allocation between stages within a fixed 5B-token budget, showing that more pruning tokens consistently improve perplexity. This provides actionable guidance for practitioners.

## Weaknesses

### Fatal

None.

### Major

1. **Lack of an internal scratch-training baseline on the same data and architecture.** All comparisons to "training from scratch" use external baselines (Pythia, OpenLLaMA, TinyLlama, INCITE) that were trained on different data mixtures (The Pile, RefinedWeb, etc.), with different hyperparameters, and often with substantially different architectures. While Sheared-LLaMA outperforms these models, the absence of a controlled ablation — training the target architecture from scratch on the same RedPajama data (both at 50B tokens and at a larger budget matched to the total compute including LLaMA2-7B pre-training) — means the reader cannot fully disentangle whether the gains come from the pruning initialization, the dynamic batch loading, or simply from using a better data recipe. The paper's core claim ("pruning + continued pre-training is more cost-effective than training from scratch") would be substantially strengthened by this control.

### Minor

1. **Pruning-method comparison is limited to early checkpoints without full downstream evaluation.** The comparison to CoFiPruning and LLM-Pruner (Section 5.2, Table 3) uses only 0.4B tokens and evaluates only perplexity and inference speed, not downstream task performance after the full 50B-token continued pre-training budget. The paper argues that targeted pruning's architectural regularity justifies a slight perplexity penalty (and estimates ~0.5B tokens to close the gap), but this remains an interpolation rather than a measured result. Running a competitor through the full pipeline would make the comparison conclusive. The paper acknowledges this as a computational constraint (line 357), but it remains a limitation on the evidence.

2. **No uncertainty quantification for any reported result.** All downstream task scores and win rates are presented as point estimates without standard errors, confidence intervals, or any discussion of evaluation variance. While single-run evaluation is common practice for LLM benchmarks, the absence is notable given the paper's aggregate claims ("outperforms across 10 of 11 tasks"), especially since GPT-4 win-rate evaluation is known to have variance.

3. **Reference loss source comparison deferred to appendix.** The choice between "scaling reference" (scaling-law estimate) and "source reference" (directly using the source model's loss) is an important practical decision — many users will only have access to a single source model. The paper states both work well but defers the comparison to the appendix (line 256–258). This comparison would merit a main-paper ablation since it affects the method's accessibility.

### Trivial

None.

## Nice-to-Haves

- An analysis of which layers/heads are consistently pruned across runs, and how pruning decisions vary by domain, would deepen understanding of the method's behavior.
- Extending the approach to larger source models (e.g., 70B → 7B) or different model families would test generality beyond LLaMA2-7B. The paper acknowledges this as future work.

## Removed Points

**These points were flagged during review but are removed after cross-checking against the paper. Treat them with caution if referenced elsewhere.**

1. **"The 3% compute claim is selectively framed / should include LLaMA2-7B training cost."** — The paper consistently compares against the cost of training *small models from scratch* (e.g., "only 1/32 of budget to achieve on-par performance with OpenLLaMA-3B-v2," Figure 1 caption). Under the stated scenario — leveraging an existing pre-trained LLM that is already available — the marginal compute comparison is the correct one. The critic's request to include the sunk cost of LLaMA2-7B's pre-training shifts the goalpost to a different research question (total cost of developing both large and small models).

2. **"Parameter count mismatch makes comparisons unfair (1.3B vs 1.4B, 2.7B vs 3B)."** — The asymmetry favors the *baselines* (they have more parameters), meaning the paper is proving a stronger point by comparing against larger models. Per the asymmetry rule, this criticism is removed.

3. **"Downstream performance trajectory is still improving, suggesting results are from an intermediate checkpoint."** — The paper explicitly acknowledges this: "the downstream performance trajectory suggests that further training the pruned model with more tokens would result in even greater gains" (line 84). This is transparent, not a hidden weakness.

4. **"Missing analysis of learned pruning masks."** — This is a nice-to-have, not a weakness. The paper's evaluation is already thorough; mask analysis would be a welcome addition but its absence does not undermine any claim.

5. **Generalized concerns about data mismatch across baselines.** — The paper transparently documents the training data for each baseline (Table 2 footnotes/table). Cross-dataset comparisons are the norm in LLM evaluation; this is not a specific identified flaw.

## Novel Insights

None beyond the paper's own contributions. The two reviewers largely agree on the paper's strengths and limitations, with the primary insight being that the paper's evaluation, while strong, would benefit from a controlled scratch-training ablation to tighten the causal attribution of gains to the pruning initialization specifically.

## Suggestions

1. **Add a controlled scratch-training baseline.** Train the target architecture (e.g., Pythia-1.4B configuration) from scratch on RedPajama with the same 50B token budget. Even at 50B tokens (where scratch-training will underperform), this directly quantifies the value of the pruning initialization. If compute allows, also train to a larger budget (e.g., 300B tokens) to match the total compute including LLaMA2-7B pre-training.

2. **Run one pruning competitor through the full 50B continued pre-training pipeline** and evaluate on the same downstream tasks. This would make the pruning comparison conclusive and address the main gap in Section 5.2.

3. **Provide variance estimates or at minimum note the stability** of the downstream evaluation numbers across random seeds or few-shot example permutations.

4. **Promote the reference-loss source comparison (scaling vs. source reference) to the main paper** or summarize its key finding in a sentence in Section 2.2.

## Score and Decision

**Originality:** 7/10 — Targeted structured pruning to arbitrary architectures is novel; dynamic batch loading is an adaptation of DoReMi with a practical simplification.  
**Importance of research question:** 8/10 — Cost-effective production of small LLMs is highly relevant.  
**Claims well-supported:** 6.5/10 — Empirical results are strong but lack a controlled scratch-training baseline and have limited pruning-method comparison.  
**Soundness of experiments:** 7/10 — Experiments are well-designed but have some gaps (no internal control, no uncertainty).  
**Clarity of writing:** 8/10 — Well-structured, clear motivation and method description.  
**Value to community:** 8/10 — Practical, actionable method; models have been released and used.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>