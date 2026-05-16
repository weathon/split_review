Now I have all the evidence I need to compile the final review.

## Summary

This paper proposes KVMerger, a KV cache compression method for LLMs that merges similar key/value states rather than evicting them. It is motivated by two observations: (1) key states exhibit high localized cosine similarity within a sequence (explained via RoPE structure), and (2) the resulting sparsity pattern is persistent across datasets at the model level. The method identifies merging sets using a constrained agglomerative hierarchical clustering variant and merges states within each set using Gaussian kernel weighted merging with attention-score-based pivot selection. Experiments on LongBench and ZeroScrolls across Llama2-7B/13B-chat and Mistral-7B-Instruct show consistent improvements over H2O (eviction) and CaM (value merging), often approaching or matching full-cache performance.

## Strengths

1. **Novel empirical observation with theoretical grounding**: The paper is the first to identify and characterize high localized token-level similarity in key states (Section 3.1, Figure 2), and ties this phenomenon to the rotary structure of RoPE via Lemmas 3.1 and 3.2. This observation is well-supported by visualizations across layers and heads and provides clear motivation for merging over eviction.

2. **Consistent and strong empirical performance**: KVMerger outperforms H2O and CaM on nearly all LongBench tasks (Table 1) and all ZeroScrolls tasks (Table 2) at both 50% and 35% cache budgets across three model families. On several tasks it matches or exceeds full-cache performance (e.g., 2wikimqa: 32.99 vs 31.45 full cache). The needle-in-a-haystack results (Figure 5) further confirm robust retrieval.

3. **Principled merging framework**: The paper formalizes KV cache merging as a constrained clustering problem (Definition 4.1) with a locality constraint, and develops a practical greedy algorithm (Algorithm 1) to identify merging sets. The Gaussian kernel weighted merging function (Section 4.2) with attention-guided pivot selection is well-ablated (Tables 3 and 4), showing clear benefits over random pivot selection and average merging baselines.

4. **Demonstrated applicability beyond standard attention**: KVMerger maintains strong results on Mistral-7B-Instruct (Grouped-Query Attention), where H2O degrades sharply (Table 1), showing robustness to different attention architectures.

## Weaknesses

### Fatal
None.

### Major
None. All identified issues are minor or presentation-related; no weakness invalidates the paper's core claims or results.

### Minor

1. **The connection between formal clustering objective and Algorithm 1 is underdeveloped.** Definition 4.1 states a global objective (maximizing intra-cluster minus inter-cluster similarity), but Algorithm 1 greedily merges consecutive tokens whose cosine similarity exceeds a threshold ε. The paper does not show that the greedy procedure optimizes (or approximates) the formal objective. This does not invalidate the algorithm — it is a reasonable heuristic — but the presentation overstates the formalism.

2. **The definition of σ (Equation 4) is circular and the practical computation is unclear.** Equation 4 defines σ in terms of g_{pi}, which itself depends on σ. The ablation (Table 5) tests fixed integer σ values and finds σ=5 works best, with the paper noting that the "average value of computed σ for most layers fluctuates around 5." It is unclear whether σ is computed iteratively, set to a fixed global value (5), or determined some other way. This needs clarification.

3. **Missing comparison with directly relevant merging methods.** D2O and MiniCache are cited in Related Work (Section 2.3) but not evaluated experimentally. D2O is particularly relevant as it also merges both key and value states using weighted merging based on cosine similarity. The paper should justify why these are omitted or add comparisons on a subset of tasks.

4. **Evidence for "persistent KV cache sparsity at the model level" is based on a single model.** Figure 3(b) shows compression ratios only for Llama2-7B-chat (200 samples). The claim that sparsity is "independent of the dataset and remains persistent at the model level" would be substantially strengthened by showing analogous plots for Llama2-13B-chat and Mistral-7B-Instruct. The paper's main results provide indirect support (the method works across models), but the stated claim goes further than the direct evidence.

5. **No confidence intervals or statistical significance.** The reported improvements over baselines are often small (e.g., 35.02 vs 34.00 with H2O at 50% on LongBench average for Llama2-7B-chat). Without multiple seeds or significance testing, it is unclear whether these differences are consistent.

6. **Needle-in-a-Haystack results are only presented as heatmaps** with no numerical scores (e.g., average accuracy across depths/lengths), making quantitative comparison difficult. The visual improvements are evident but should be backed by numbers.

7. **The attention-score critique vs. usage is mildly inconsistent in framing.** The paper criticizes "attention-score-driven approaches" for being "biased" and risking "context damage" (Section 3.1), but then uses aggregated attention scores for both pivot selection (Section 4.2) and for excluding top-k states from merging (Section 4.1). The distinction is defensible — using attention scores for pivot selection does not discard information, unlike eviction — but the paper's wording creates an apparent contradiction that should be explicitly addressed.

8. **Value state weight normalization lacks justification.** The paper multiplies value state weights by |S_v| (line 230), making the weight sum equal to |S_v| instead of 1. The justification ("accurately reflect the number of value states") is vague and the impact of this scaling on attention outputs is not analyzed or ablated.

### Trivial

- The similarity threshold ε=0.75 is fixed across both budget scenarios with no sensitivity analysis.
- Lemma statements are labeled "Informal" and are simple properties of RoPE's 2D rotation structure; the paper should be clearer about their intended scope.
- The phrasing "effectively recovers the model's performance" in the conclusion is slightly overstated for cases where a non-trivial gap from full cache remains (e.g., ZeroScrolls 35%: 14.84 vs 15.30 full).

## Nice-to-Haves

- Ablation on the similarity threshold ε (e.g., sweep from 0.5 to 0.95) showing the trade-off between compression ratio and performance.
- Ablation on whether excluding top-k attention states from merging is necessary (i.e., setting preservation proportion to 0%).
- Comparison with simple average merging using proper weight normalization to isolate the contribution of the Gaussian kernel.
- Numerical scores for needle-in-a-haystack to complement the heatmaps.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Weight normalization of key states is "likely incorrect" (Critical Issue 1 - key states portion).** The reviewer claimed the merged key state is "not a convex combination" and "scaled upward" because the sum of weights exceeds 1. This is factually wrong. From Equation (5): w_p = 1/Σg, w_i = g_{pi}/Σg. Sum = (1 + Σ_{i≠p}g_{pi})/Σg = (g_{pp} + Σ_{i≠p}g_{pi})/Σg = Σg/Σg = 1. The key state merging is a valid convex combination. This criticism is removed as factually incorrect.

2. **"Contradiction in the role of attention scores" framed as a structural/fatal flaw (Critical Issue 2).** The reviewer claims this is a "fundamental inconsistency" and "contradiction." In reality, the paper critiques attention-score-based EVICTION (which discards low-attention tokens) and uses attention scores for PIVOT SELECTION (which preserves all tokens' information through weighted merging into the pivot). These are different operations with different consequences. The paper's critique is that "relying on attention-score alone can lead to context damage" because eviction loses information — merging does not. This is not a contradiction, and the severity is downgraded to a minor framing issue.

3. **Criticisms about lemma formality and value state analysis.** The reviewer faults the "informal" lemmas for not being "fully rigorous" proofs. The paper explicitly labels them as informal and uses them as suggestive analysis, not formal proof. The claim that the connection from RoPE to empirical similarity is "suggestive but not formally connected" — this is acknowledged by the paper's careful language. The criticism about value states lacking RoPE "should be verified or acknowledged as an assumption" — the paper does acknowledge this by noting value states lack RoPE, and the observation is presented as empirical, not as a theorem.

4. **"Lemma statements... are not fully rigorous."** The paper explicitly labels them "Informal" (twice). Criticizing informal lemmas for lacking rigor is a category error.

5. **Criticism that the paper should cover additional tasks/domains beyond its scope.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful observation about the sigma computation circularity and the value state weight scaling that the authors should address, but these are methodological clarifications rather than novel insights about the paper's contribution.

## Suggestions

1. **Fix the σ computation description.** Clarify whether σ is set to a fixed value (5) as the ablation suggests, or computed per-set via Equation 4. If the latter, explain the non-circular computation procedure (e.g., iterative estimation, or a two-step process using distances first).

2. **Add an explicit justification for the value state weight scaling (×|S_v|)** and ideally an ablation showing performance without the scaling factor.

3. **Add a brief sentence in Section 3.1 acknowledging that although attention scores are used for pivot selection, the key difference from eviction methods is that no token information is discarded — all tokens in a merging set contribute to the merged result. This would resolve the apparent contradiction cleanly.**

4. **Include comparisons with D2O on a subset of tasks**, or provide a clear justification for omission (e.g., different compression paradigm, implementation complexity).

5. **Add the persistent sparsity analysis for at least Llama2-13B-chat** to substantiate the "model-level" claim.

6. **Add numerical scores for needle-in-a-haystack** (e.g., average accuracy across all depth×length combinations).

## Score and Decision

The paper makes a solid contribution with a novel observation about key state similarity, a well-motivated merging framework, and consistent empirical improvements over strong baselines across multiple models and tasks. The identified weaknesses are minor — none threaten the core claims or require fundamental changes to the method. I recommend acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>