Now I have a thorough understanding. Let me compose the final consolidated review.

---

## Summary

This paper proposes KVMerger, a KV cache compression method that merges similar key and value states instead of evicting them, targeting long-context LLM tasks. The method is motivated by an empirical observation that key states exhibit high localized cosine similarity within a sequence (explained via RoPE), and that the resulting layer-wise compression ratios are persistent across datasets. KVMerger consists of a greedy threshold-based grouping algorithm for merging set identification and a Gaussian-kernel weighted merging function. Experiments on LongBench and ZeroScrolls across Llama2-7B/13B and Mistral-7B show consistent improvements over H2O (eviction) and CaM (value merging) at 50% and 35% cache budgets.

## Strengths

- **Novel discovery of localized key-state similarity with theoretical grounding.** Section 3 provides clear visualization and analysis showing that key states exhibit high cosine similarity with adjacent tokens across layers and heads, unlike value states. The RoPE-based theoretical explanation (Lemmas 3.1–3.2) grounds why key states (but not value states) display this property — a genuine and well-motivated insight that opens the door for similarity-based KV cache merging.

- **Consistent and substantial outperformance over H2O and CaM on long-context benchmarks.** Tables 1–2 show KVMerger achieves the highest average score in 7 out of 9 model/budget combinations. On Mistral-7B at 35% budget, KVMerger scores 35.04 vs. H2O's catastrophic 13.48 and CaM's 28.27. On ZeroScrolls, KVMerger at 50% budget achieves 15.21, nearly matching the full-cache 15.30, while H2O drops to 14.36 and CaM to 14.24. Several individual task scores match or exceed the full-cache baseline, suggesting merging can be less destructive than eviction.

- **Well-designed ablation studies isolate design decisions.** Table 6 (σ sweep) and Table 7 (pivot selection) provide controlled experiments confirming that (a) σ≈5 performs best and aligns with the computed adaptive value, and (b) attention-score-based pivot selection substantially outperforms random selection (24.20 vs. 22.12 avg), validating both design choices.

- **Observation of persistent, dataset-independent KV cache sparsity.** Section 3.2 shows that layer-wise compression ratios from the merging set identification algorithm are nearly identical across different samples and tasks (Figure 3b). This finding is practically useful — it enables pre-determined layer-specific compression budgets without per-dataset tuning.

## Weaknesses

### Fatal
None.

### Major

- **The σ formula in Equation 4 (Gaussian kernel weights) is self-referential and underspecified.** The definition states σ = (∑𝐠_{pi}) / (√2|𝐒_k|), where 𝐠_{pi} = exp(-||𝐤_p−𝐤_i||² / 2σ²). Since σ appears on both sides — through the g terms — this is a fixed-point equation. The paper provides no explanation of how it is resolved (iteratively? closed-form approximation? different intended formula?). The text then says "We empirically define σ as the mean value of 𝐠_{pi}," which is the same circularity stated verbally. While the ablation shows that a fixed σ=5 works well (mitigating practical harm), **the algorithm as described cannot be replicated** without resolving this ambiguity. This is the most significant technical issue in the paper and requires a fix (either correct the formula or clarify the computation procedure).

- **Insufficient baseline comparison.** The experiments compare against only H2O (eviction) and CaM (value merging). The related work (Section 2.3) cites D2O, MiniCache, and FastGen as relevant prior compression methods, yet none are included in the experimental comparison. Given that KVMerger is also a merging method and D2O directly merges both key and value states, excluding it weakens the claim of "superior performance across tasks" (Abstract). The paper would be substantially strengthened by adding at least D2O and MiniCache under the same budgets.

### Minor

- **The formal problem definition (Section 2.4) is disconnected from the actual algorithm.** Definition 2.1 frames KV cache merging as minimizing compression ratio subject to an output perturbation bound ε. However, the algorithm does not check or enforce this ε constraint — the budget is fixed exogenously, and the threshold and proportions are tuned to match it. The formalization is conceptually ornamental and does not guide the method's design or evaluation. The paper should either remove it or connect it to the actual algorithm.

- **Overclaimed novelty.** The paper calls itself "one of the pioneering researches concerning KV cache merging for LLMs" and "the first one to consider KV cache problem independently," yet Section 2.3 cites three prior merging works (CaM, D2O, MiniCache) that already propose merging set identification and merging strategies. The observation of key-state similarity is indeed novel, but the overall framing should be adjusted to acknowledge prior art more accurately. The contribution is incremental (a new merging method with a better identification policy) rather than pioneering.

- **No sensitivity analysis for the cosine similarity threshold ε.** The threshold is set to 0.75 for both the 50% and 35% budgets without any analysis of how performance varies with this critical hyperparameter. Since this threshold directly controls merging set formation and thus compression patterns, a sensitivity study across a range (e.g., 0.65–0.95) is needed.

- **Needle-in-a-Haystack results lack quantitative metrics.** Figure 5 shows only heatmaps without reporting average retrieval success rates or similar summary statistics, making the claimed "highest retrieval performance" difficult to verify quantitatively.

- **Disproportionate proportion values not justified.** The recent-token and attention-score reservation proportions (0.17%, 0.12%, 0.08%, 0.02%) are stated without any explanation of how they were determined. If these are key to achieving the stated budgets, their selection should be documented.

### Trivial

- **Algorithm 1 pseudocode has an ambiguity:** on line "i = j," the variable `j` is a bound variable from the set comprehension in the preceding Group statement, making the assignment unclear. The algorithm is best understood as a greedy backward scan merging consecutive tokens whose cosine similarity exceeds ε, rather than a true AHC variant.

## Nice-to-Haves

- Reporting variance or running 2–3 random seeds on a subset of LongBench tasks would strengthen confidence that the reported improvements (often 1–2 points) are meaningful. (Note: single-run evaluation on established benchmarks is common practice in this area, so this is not a deficiency.)
- Extending the needle test to longer contexts (8K–16K tokens) would better demonstrate long-context capabilities.
- A qualitative example showing where eviction loses a critical token but merging preserves it would strengthen the narrative.

## Removed Points

- **Criticism about σ ablation being inconsistent** — the reviewer claims that the adaptive σ averaging to ~5 doesn't validate the adaptive formula because the average across variable per-set values doesn't equal using a global σ=5. This conflates "average σ across layers ≈ 5" with "individual per-set σ varies"; the authors reasonably claim alignment as empirical justification. Kept as minor but downgraded from the reviewer's stronger framing.
- **H2O catastrophic drop on Mistral-7B being abnormal** — the paper explicitly discusses this (Section 5.1) and attributes it to GQA adaptation, which is a reasonable explanation. The critic's suggestion that this indicates implementation problems is speculative without evidence.
- **The word "persistent" being too strong** — Figure 3(b) shows compression ratios are indeed consistent across samples; the evidence supports the claim adequately.
- **Missing related works** — I cannot independently verify whether specific works exist or are missing; per instructions, do not mention missing related works.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful tension: the paper's strongest empirical asset (the key-state similarity observation) is clean and well-supported, while its weakest technical component (the circular σ definition) is an artifact of the write-up rather than a fundamental flaw. The ablation showing fixed σ=5 works nearly as well as the adaptive formula suggests that the Gaussian kernel's bandwidth can be treated as a simple hyperparameter, and the "adaptive" framing adds complexity without demonstrated benefit. This is worth the authors noting.

## Suggestions

1. **Fix the σ definition.** Either: (a) clarify that σ is computed via a simple fixed-point iteration (and report convergence behavior), or (b) replace it with the mean of pairwise L2 distances within the merging set (which is likely what was intended), or (c) simplify to a fixed σ=5 across all merging sets, since the ablation shows it performs well and eliminates the circularity entirely.
2. **Expand the baseline set.** Add D2O and ideally MiniCache or FastGen under the same budgets to substantiate the "superior performance" claim.
3. **Add a sensitivity study** for the cosine similarity threshold ε (e.g., 0.65–0.95).
4. **Report quantitative needle-in-a-haystack metrics** (e.g., average accuracy) alongside the heatmaps.
5. **Tone down the novelty claims** to accurately reflect existence of prior merging works (CaM, D2O, MiniCache).

## Score and Decision

**Originality:** The key-state similarity observation is genuinely novel and well-supported. The merging method itself is a reasonable engineering contribution but not conceptually new — D2O already proposed weighted merging of both key and value states.  
**Importance of research question:** High — KV cache compression for long-context LLMs is practically important.  
**Claims well supported:** Partially. The empirical results are convincing, but the underspecified σ formula and limited baselines weaken the support.  
**Soundness of experiments:** Adequate but not thorough. Missing baselines, no sensitivity analysis for ε, no quantitative needle metrics.  
**Clarity of writing:** Generally clear. The σ formula and Algorithm 1 pseudocode have ambiguities.  
**Value to community:** Moderate — the key-state similarity observation and the pre-determined compression ratios are useful findings; the method itself is a solid baseline that others can improve upon.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>