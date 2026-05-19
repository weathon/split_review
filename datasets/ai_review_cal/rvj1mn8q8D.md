- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6
Now I have all the information I need. Let me compile the consolidated review.

## Summary
This paper introduces TextGenSHAP, a set of optimizations for computing Shapley-based explanations for LLM text generation with long documents. The method combines (i) a hierarchical Owen-value approach that prunes unimportant input regions, (ii) speculative decoding to reuse decoder outputs across perturbed samples, and (iii) architecture-specific speedups (Flash Attention, in-place encoder resampling). The paper demonstrates that these techniques reduce Shapley computation from 12–20 hours to under an hour for token-level explanations and to seconds for document-level explanations. It also shows downstream utility by using the resulting attribution scores to rerank retrieved passages and distill documents for QA readers, yielding modest accuracy improvements.

## Strengths

1. **Demonstrated order-of-magnitude speed improvements for Shapley computation.** The paper's central empirical claim — reducing token-level Shapley from 12–20 hours to under an hour (T5-XXL/T5-large, 100 permutations) and to ~5 minutes (10 permutations), and document-level from minutes to <10 seconds on T5-FiD — is clearly supported by the benchmarks in Figure 3. This directly addresses a primary barrier to using Shapley values with LLMs.

2. **Principled adaptation of Shapley to generative text via Shapley-Shubik and hierarchical Owen value.** The reformulation in Equation 2 (Section 3.2) replaces the standard log-probability value function with a probability-based formulation derived from voting theory, avoiding the need to enumerate the exponentially large output space. The hierarchical extension (Section 3.3) via the Owen value provides a natural framework for multi-granularity explanations (documents → sentences → tokens). The paper clearly distinguishes these adaptations from prior work that requires pre-specified candidate outputs.

3. **Downstream task utility demonstrated on long-document QA.** The Shapley-based reranking improves recall AUC on Natural Questions from 84.23 (baseline) to 88.53+ (Table 1), and reader top-1 accuracy from 50.54 to 52.72 (Table 2), outperforming attention-based and majority-vote baselines. These results show that the extracted attributions carry signal useful for improving system performance.

4. **Architecture-aware engineering contributions.** The application of speculative decoding to Shapley sampling (exploiting the fact that perturbed inputs produce similar decoded outputs) and the in-place encoder resampling for FiD-style models are non-trivial, well-motivated optimizations that the paper explains conceptually (Section 4).

## Weaknesses

### Fatal
None.

### Major

1. **No faithfulness evaluation.** The paper's abstract mentions "faithful explanations" and the introduction discusses faithfulness as a core criterion (lines 30–34), yet the experiments never directly measure explanation faithfulness. There is no correlation between approximate (hierarchical, pruned) Shapley values and true permutation-based Shapley values (even on a subsample where exact computation is feasible), no deletion/insertion tests, and no comparison to ground-truth rationales. Without this, the reader cannot assess whether the aggressive approximations (pruning, speculative decoding) preserve explanation quality or destroy it. Speed improvements alone do not validate an *explainability* method — they validate an *optimization* method. This is the single most significant gap in the paper's evaluation.

2. **No comparison to alternative explanation methods on the downstream tasks.** The paper compares only to an attention-aggregation baseline (Table 1) and to its own variants. It does not compare against other established post-hoc methods (e.g., gradient × input, LIME, input occlusion, leave-one-out) on the same reranking/distillation tasks. Since the AUC improvements over attention on NQ are small (88.35 vs. 88.53–88.74), it is unclear whether the additional complexity of Shapley-based explanations is justified over simpler alternatives. Without a broader comparison, the claim that "Shapley enhances systems" is undersupported.

3. **Bias from hierarchical pruning is unquantified.** The method uses an arbitrarily chosen threshold (10%/30%, Figure 3 caption) to prune documents after the first-level Shapley pass, then computes token-level Shapley only within retained documents. This means tokens in pruned documents are implicitly assigned zero importance. The paper never measures how often this approximation discards actually important tokens, nor does it report sensitivity to the threshold choice (e.g., how results change at 5%, 20%, 50%). The speed gains come largely from this pruning, but the trade-off between speed and approximation error is entirely uncharacterized.

4. **Speculative decoding is not properly characterized.** The paper states that "a large amount of total computation can be saved" (line 246) via speculative decoding, but reports no quantitative metric of its effectiveness — no acceptance rate, no average number of decoder calls saved, no ablation isolating the contribution of speculative decoding from the other optimizations. Figure 3 shows that speculative decoding (yellow bars) provides meaningful speedup over plain hierarchical (blue bars), but without acceptance rates and overhead measurements, the reader cannot assess whether the technique is working as claimed or is simply a minor contributor.

### Minor

1. **No statistical significance or variance reported.** Speed benchmarks (Figure 3) and all accuracy/recall results (Tables 1, 2, Figures 4, 5) are reported as point estimates with no confidence intervals, standard deviations, or significance tests. For a paper claiming practical utility, it is important to know whether the reported improvements (e.g., 50.54 → 52.72 top-1 accuracy) are stable.

2. **MIRACL results are mixed and the pseudo-label approach weakens the evidence.** On MIRACL with original labels (Table 1), two of the three Shapley variants underperform the baseline (77.33 and 78.19 vs. 80.18). Only the best variant (82.38) exceeds baseline. The paper then constructs pseudo-labels using the same T5-XXL model, which improves scores — but this acts as a soft circular validation (the label-expansion favors methods correlated with the pseudo-labeler's behavior). The paper appropriately hedges this as "preliminary evidence" (line 358), but it remains a weak link in the evaluation chain.

3. **"Real-time" claim is overstated for token-level explanations.** The abstract mentions "real-time Shapley values" but token-level explanations on T5-XXL still take 5 minutes (10 permutations) to over an hour (100 permutations). This is not real-time in any interactive sense. The document-level explanations on T5-FiD (<10 seconds) do fit a real-time framing, but the broader claim in the abstract is misleading.

### Trivial

1. **Notational ambiguity in Equation 2.** The paper defines $v_p(S) := f(x,1_S)$ where $f$ returns a *probability vector*, but then Equation 2 uses $[v_p(S+i) - v_p(S-i)]_+$ and claims this yields a scalar $\phi_i$ per token. It is clear from context that $v_p(S)$ is meant to be the probability of the *decoded* output (a scalar), consistent with the Shapley-Shubik formulation, but the notation as written suggests a vector operation. Clarifying this would improve reproducibility.

## Nice-to-Haves

- A direct comparison to at least one alternative explanation method (e.g., gradient saliency, LIME) on the reranking/distillation tasks would substantially strengthen the claim that Shapley's complexity is worthwhile.
- Reporting speculation acceptance rates and decoder-call savings would make the speculative decoding contribution transparent and reproducible.
- A sensitivity analysis of the hierarchical pruning threshold (e.g., 5%, 20%, 50%) would help users understand how to set this parameter.
- Reporting variance or confidence intervals on the key results would align with community standards for empirical ML papers.

## Removed Points

These points were identified by the reviewers but either misread the paper, reflect parser artifacts, or violate the filtering rules:

- *"Algorithm 1 is referenced but not described"* / *"The paper should be self-contained"* — Removed per rule: the parser strips appendix content from all papers; this material exists in the original submission.
- *"The paper's own method uses greedy decoding which is also prespecification"* — Removed: the method does not require the user to enumerate candidate outputs; greedy decoding is just the mechanism to obtain the model's actual output. The distinction from prior work (which requires specifying all possible outputs) is valid.
- *"The number of permutation samples (100) is low; typically thousands are needed"* — Removed: this is a speculative claim from the reviewer with no evidence that thousands are needed for this setting. The paper's choice is explicitly stated and reproducible.
- *"Should compare to FastSHAP, KernelSHAP approximations"* — Demoted from a weakness to not retained: the paper explains (Section 2) that these methods are designed for tabular/image data and require prespecification of candidates, making direct comparison non-straightforward. A comparison would be nice but is not a required omission.
- *"FlashAttention-specific speed comparisons are missing"* — Removed: FlashAttention is a system-level optimization integrated transparently; the paper's benchmarks reflect end-to-end times with all optimizations active. It is reasonable not to ablate a standard system-level optimization.
- Various pure presentation/style nitpicks removed per rules.

## Novel Insights

An interesting observation that emerges from the cross-section of reviews is that the paper's core strength (massive speed improvements) and its core weakness (no faithfulness evaluation) are two sides of the same coin: the speed gains come from approximations (hierarchical pruning, speculative decoding) whose impact on explanation quality is never measured. The paper would be significantly stronger if it quantified this speed-faithfulness trade-off directly — even on a small subsample — because that would let readers assess whether the engineering optimizations preserve the very property (faithfulness) that motivates using Shapley values in the first place. A secondary insight is that the downstream QA improvements, while real on NQ, are small enough (sub-1% AUC differences from attention on NQ) that the paper's claim "Shapley-based explanations enhance systems" needs broader comparative evidence before it can be accepted as a general finding rather than a dataset-specific observation.

## Suggestions

1. **Add a faithfulness experiment on a small subsample.** Compute exact permutation-based Shapley values for 20–50 examples on a small model (e.g., T5-small with short inputs) and report Spearman correlation with the approximate hierarchical/pruned values. Also report the drop after each optimization (hierarchical, speculative, in-place encoding). This single addition would transform the paper from an engineering report into a validated explainability method.

2. **Add at least one non-Shapley explanation baseline** (e.g., gradient × input, leave-one-out) to the reranking experiments in Table 1 and Figure 3. This directly tests whether Shapley's complexity buys anything over simpler alternatives.

3. **Report speculative decoding acceptance rates and average decoder-call savings** in a short table or inline.

4. **Add a threshold sensitivity analysis** showing how the hierarchical pruning threshold affects both speed and downstream accuracy.
