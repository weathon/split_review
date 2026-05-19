- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 6, 5, 8
Now I have a thorough understanding of the paper and can carefully cross-reference the reviewer claims. Let me synthesize the final review.

---

## Summary

This paper introduces PolySketchFormer, a transformer architecture that replaces softmax attention with degree-4 polynomial attention approximated via polynomial sketches (Ahle et al., 2020). A block-based lower-triangular multiplication algorithm is proposed to apply causal masking without materializing the full attention matrix, reducing sequential dependence compared to Performer's cumulative sum algorithm. Experiments on Wiki-40B and PG-19 show that perplexity stays within 2–3 points of softmax while training throughput exceeds FlashAttention at context lengths ≥8k, with a 4.5× speedup at 32k.

## Strengths

- **Linear-time attention latency in practice.** Figure 1 shows that PolySketchFormer's attention latency per token stays nearly constant (~0.04–0.06 ms) as context length grows from 512 to 16k, while FlashAttention's grows linearly from ~0.02 ms to ~0.25 ms. This is a direct empirical demonstration of the linear-time advantage on hardware.

- **Large-margin speedup at long contexts.** At 32k context length, a 4-layer PolySketchFormer trains at 1.54 steps/sec vs. 0.34 steps/sec for FlashAttention — a 4.5× speedup (Section 5). This is a concrete, practically relevant result.

- **Perplexity close to softmax across context lengths.** Table 1 shows that on both Wiki-40B and PG-19, PolySketchFormer stays within 2–3 perplexity points of softmax attention across context lengths 512–4k. The gap is relatively stable, not widening at longer contexts.

- **Scalability to larger models.** A 730M-parameter, 24-layer PolySketchFormer achieves 14.6 perplexity vs. 14.4 for softmax on Wiki-40B (Section 5), showing the approach does not collapse when scaled up.

- **Principled solution to non-negativity.** Theorem 2.5 and the tensoring trick provably ensure all entries of the approximate attention matrix are nonnegative, which is necessary for the probability interpretation of attention weights. This is a clean theoretical fix to a known issue with sketch-based approximations.

## Weaknesses

### Fatal
None.

### Major
- **Performer baseline dropped without resolution.** The paper identifies a data-leak bug in the open-source Performer implementation (line 192) and decides not to report Performer results at all. Performer is the most directly related method — it also uses random feature maps with a cumulative-sum causal algorithm that the paper explicitly claims to improve upon ("block-based algorithm gives significant speedups over the cumulative sum algorithm used by Performer," lines 6–7, 69–70). Fixing the bug (or implementing the cumulative-sum algorithm from scratch for the paper's own sketch-based method) and reporting the results would directly substantiate this central algorithmic claim. Without this comparison, the claimed advantage over Performer's cumulative-sum approach remains unvalidated.

- **No ablation studies for key hyperparameters.** The paper fixes sketch size to 32, block size to 256, and degree to 4 (lines 163–167) without varying any of them. These parameters directly control the accuracy-efficiency trade-off: sketch size determines approximation quality and compute cost; block size controls the balance between sequential steps and FLOPs; degree governs model capacity. Without ablations, the reader cannot assess how sensitive the method is to these choices, and practitioners lack guidance for configuring the method in different settings. Degree is partly motivated by Figure 2 (exact polynomial attention), but the interaction of degree with sketching error is unexplored.

- **Missing comparison with other linear-time attention methods.** The paper evaluates against softmax, exact polynomial attention, and FlashAttention — but not against other linear-time transformer variants. Linformer (Wang et al., 2020), Linear Transformer (Katharopoulos et al., 2020), Performer (if fixed), and the mixed-chunk approach of Hua et al. (2022) are all discussed in the introduction but never empirically compared. For a paper titled "Fast Transformers via Sketches for Polynomial Kernels," the reader cannot assess whether PolySketchFormer offers a better quality-efficiency trade-off than existing linear-time alternatives. The comparison with FlashAttention (a quadratic-approximation method) is useful for the speed claim but does not fill this gap.

### Minor
- **No multiple seeds or confidence intervals.** All perplexity and speed results appear to come from single runs. For the main 110M-parameter comparisons, the gap between softmax and PolySketchFormer is 2–3 perplexity points (Table 1) — without variance estimates, it is unclear whether this gap is stable or within noise. While multi-seed training of 110M-parameter models is expensive, reporting even 2–3 seeds for the central comparison would substantially strengthen confidence in the results.

- **No direct measurement of sketch approximation quality.** The paper relies entirely on downstream perplexity to validate that the sketched polynomial attention approximates the exact polynomial attention. No direct error metric (e.g., Frobenius norm between exact and sketched attention matrices, or per-row KL divergence) is reported. Given the frank acknowledgment that "the sketch sizes we use in our implementations are not very good at preserving the dot products for vectors that have negative entries" (line 67), direct approximation error measurements on actual query/key vectors from a trained model would bridge the theoretical guarantee and the perplexity results, and clarify whether the gap is due to sketch error or model capacity.

- **No memory usage comparison.** The paper reports steps per second but not peak memory usage, which is often the binding constraint for long-context training. Reporting memory (or maximum context length before OOM) for each method would strengthen the practical claims.

### Trivial
None.

## Nice-to-Haves
- **Direct comparison of the block-based algorithm vs. the cumulative-sum algorithm.** The paper could implement the cumulative-sum algorithm for its own sketch-based matrices and compare latency directly, isolating the speedup attributable to blocking vs. the overall method.
- **Downstream task evaluation.** Perplexity is a useful diagnostic but evaluating on tasks that stress long-range dependencies (e.g., long-document classification, Scrolls, or multi-hop QA) would test whether the 2–3 perplexity gap translates to meaningful performance differences.
- **Theoretical guarantee for the normalized attention output.** The AMM guarantee (Definition 2.1) bounds error on the unnormalized product, but the attention output involves normalization. A brief discussion of whether the guarantee extends to the final output would strengthen the theoretical framing.
- **The claim about "recontextualizing chunk-based attention" (line 69) is stated but not elaborated.** A short discussion connecting the block algorithm to the mixed-chunk mechanism of Hua et al. (2022) would clarify the claimed relationship.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Theorem 2.5's conditions are not checked for the specific sketch construction."** The paper explicitly references Section 4 of Ahle et al. (2020) to assert that the construction satisfies the required JL-moment conditions (line 123). This is standard practice in theory papers — deferring verification to a cited reference is appropriate. The critic's concern about the gap between the theoretical sketch size and the practical choice of 32 is acknowledged but is an observation about theory-practice gap, not an error.
- **"Sequential dependency is not eliminated — O(n/b) steps may still be a bottleneck."** The paper already acknowledges this: "As we increase the block size used, we decrease the number of sequentially dependent steps" (line 140). The sequential dependency is *reduced*, which is the claimed contribution. Without evidence that 64 sequential steps are a bottleneck, this is speculation, not a concrete flaw.
- **"No evaluation on downstream tasks."** The paper's stated scope is language modeling perplexity and training throughput. Requesting downstream tasks is a reasonable extension but outside the paper's declared evaluation scope.
- **"The claim about recontextualizing chunk-based attention is not elaborated."** This is a brief remark in the introduction, not a central claim. Its lack of elaboration is a presentation choice, not a methodological weakness.
- **"Theoretical guarantee for attention output, not just matrix product."** This is a valid nuance but not a weakness — the paper uses the attention formulation that normalizes by the sum of weights (Section 4), and the error analysis of normalization is an open question, not a flaw in what the paper does address.

## Novel Insights
None beyond the paper's own contributions. The harsh critic and strength finder largely agree on the paper's substance; the key tension is between the paper's genuine theoretical/empirical contributions and the incompleteness of its evaluation. The reviews do not surface a novel insight that the paper itself misses.

## Suggestions

1. **Fix the Performer bug and add Performer results** to Table 1 and Table 2. This is the single most important addition, as it directly validates the claim about the block algorithm improving on the cumulative-sum approach. Alternatively, implement the cumulative-sum algorithm for the paper's own sketch-based matrices and compare it against the block-based version to isolate the algorithmic contribution.

2. **Add ablation studies** for at least sketch size (e.g., 16, 32, 64 → tensored to 256, 1024, 4096 columns) and block size (e.g., 128, 256, 512) on one setting (e.g., 4k context, 110M model). Report both perplexity and training steps/sec to illuminate the accuracy-efficiency trade-off.

3. **Report results from at least 2–3 random seeds** for the main comparisons in Tables 1 and 2. Even if computational constraints limit this to one representative context length (e.g., 4k), it would provide basic evidence of stability.

4. **Add a direct approximation-quality measurement:** compute the Frobenius norm error between the exact polynomial attention matrix and the sketched approximation on a held-out batch of query/key activations from a trained model. This would bridge the theoretical guarantees and the perplexity results.

5. **Include at least one other linear-time baseline** (e.g., Linear Transformer with a simple feature map, or a re-implemented Performer with corrected causal masking) in the speed and perplexity comparison.
