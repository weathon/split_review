Now I have all the information needed. Let me construct the consolidated review.

## Summary

This paper identifies that standard RoPE implementations compute a complex-valued dot product but only retain the real part, discarding the imaginary component. The authors propose RoPE++, which re-introduces this imaginary part as a separate group of attention heads. Two configurations are presented: RoPE++<sub>EH</sub> (equal head count, halved KV cache) and RoPE++<sub>EC</sub> (equal cache, doubled heads). The imaginary attention can be implemented by a simple −π/2 rotation of the query before applying standard RoPE, making it architecturally clean. Experiments at 376M and 776M show improvements on short- and long-context benchmarks, with particularly large long-context gains for RoPE++<sub>EC</sub>.

## Strengths

1. **Clean and elegant architectural insight.** The observation that the imaginary part of the complex RoPE product corresponds to a −π/2 rotation of the query (Equation 4) is mathematically precise and practically attractive. It enables reuse of existing FlashAttention kernels and integration with GQA without custom CUDA code. This is a genuine contribution that goes beyond the typical RoPE interpolation/extension work.

2. **Demonstrated long-context improvements, especially at 376M.** On RULER and BABILong, RoPE++<sub>EC</sub> substantially outperforms vanilla RoPE at the 376M scale (RULER average 25.0 vs. 18.8; BABILong average 16.1 vs. 11.0). At 64k extrapolation, the margin is even wider (RULER 9.0 vs. 5.5). These are non-trivial gains on synthetic long-context benchmarks that directly probe the claimed ability.

3. **Practical KV-cache efficiency via RoPE++<sub>EH</sub>.** RoPE++<sub>EH</sub> halves the KV cache and QKV parameters while keeping the head count equal, producing lower memory costs and higher throughput (Figure 4). Average short-context performance is competitive with or better than vanilla RoPE (e.g., 40.3 vs. 40.1 at 376M, 42.5 vs. 42.0 at 776M), making this a practically useful trade-off for long-context deployment.

4. **Generalization across long-context extension methods.** Table 3 shows that RoPE++<sub>EC</sub> consistently improves over RoPE under both Linear PI and YaRN, indicating the benefit is orthogonal to existing interpolation-based context extension techniques.

5. **Attention pattern analysis provides mechanistic insight.** The qualitative attention heatmaps (Figure 5) show that imaginary heads attend more globally while real heads attend more locally, supporting the paper's core narrative. The noise-injection experiment (despite its limitations) provides quantitative evidence that imaginary heads are differentially important for long-context tasks.

## Weaknesses

### Major

- **RoPE++<sub>EC</sub>'s gains are confounded with increased head count.** RoPE++<sub>EC</sub> doubles the number of attention heads (and doubles the output projection W<sub>o</sub>) relative to vanilla RoPE while keeping KV cache equal. The observed gains on long-context benchmarks could partially—or entirely—derive from having more independent queries and a larger output projection, rather than from the *imaginary* nature of the added heads. The paper lacks a controlled baseline: "RoPE with 2× standard query heads and twice W<sub>o</sub> at equal KV cache." This is the most significant weakness because it directly threatens the attribution of the paper's central claim. RoPE++<sub>EH</sub> partially addresses this (same head count, still improves on average short-context tasks) but uses a different trade-off (halved QKV/cache), so it does not fully substitute for the missing control. The authors should either add this control or explicitly acknowledge that the EC configuration's advantage may reflect both the imaginary mechanism and increased representational capacity.

- **The theoretical analysis does not convincingly connect to actual model behavior.** Section 3.2 derives a characteristic curve for imaginary attention under the assumption of independent random query and key vectors. This is the same style of analysis used in prior RoPE literature, but it inherits the same limitations: attention is driven by *correlated* query-key pairs, so the average under independence need not reflect actual attention distributions. The sine-integral curve also becomes negative over some distance ranges; since softmax zeroes out negative logits, the "average" under the random-vector model does not correspond to actual post-softmax attention patterns. The paper does not quantify whether imaginary heads actually produce higher attention mass on distant tokens (e.g., via average attention distance metrics). The attention heatmaps provide qualitative support but are not systematic.

### Minor

- **The noise-injection experiment conflates position information with content importance.** Adding Gaussian noise to attention scores corrupts the entire content-based attention distribution, not just the positional component. The finding that corrupting imaginary attention hurts more could reflect that imaginary heads encode different semantic subspaces or are more important for the *content* of long-context retrieval, not specifically because of their position-encoding properties. This does not invalidate the experiment (it still shows imaginary heads are important for long context), but the paper over-attributes the effect to position encoding specifically.

- **Inconsistent results across model sizes and tasks.** At 776M, RoPE++<sub>EC</sub>'s gains on RULER are more modest (27.4 → 29.4) and RoPE++<sub>EH</sub> underperforms vanilla RoPE on BABILong (19.4 vs. 22.8). While the paper honestly reports these results, the inconsistency weakens the claim of general superiority. The "comparable" characterization for EH on long context is accurate for some settings but selective.

- **No statistical variance reported.** None of the tables report multiple seeds, confidence intervals, or variance estimates. While single-run pre-training at 50B tokens is expensive, at minimum the authors should acknowledge this limitation or provide variance for the key comparisons (e.g., the RULER 376M results where the claimed gains are largest).

- **Length extrapolation analysis is partially deferred.** The extrapolation benefit claimed in Section 3.4 relies on figures and analysis in Appendix D (not visible in the main paper body). The main paper would benefit from at least one extrapolation perplexity curve.

### Trivial

- None worth enumerating beyond what is captured above.

## Nice-to-Haves

- A controlled ablation: "Standard RoPE with 2× query heads and 2× W<sub>o</sub>" to isolate the imaginary mechanism from increased capacity in RoPE++<sub>EC</sub>.
- Quantitative metric of average attention distance for real vs. imaginary heads across layers, rather than purely qualitative heatmaps.
- Multi-seed variance for the key long-context comparisons.
- Evaluation at larger scale (e.g., 7B) to test whether the effects hold.

## Removed Points

The following criticisms from the harsh reviewer are **removed** (not incorporated into the assessment above):

1. *"The framing that standard RoPE 'discards imaginary information' is misleading / a straw man."* — **Removed.** This is factually incorrect. The complex multiplication in Equation 1 produces both real and imaginary components; taking only the real part does discard the imaginary part. This is standard complex arithmetic, not a straw man.

2. *"The real attention formula already includes both cos and sin terms, so the extrapolation benefit claim is vacuous."* — **Removed.** This misreads Section 3.4. The paper's argument is about which *specific dimensions* of q and k are coupled with which trigonometric functions, not about whether sin appears somewhere in the expression. The analysis of trained-vs-extrapolated embedding intervals in Figure 3 is a specific claim about dimension-wise coverage, not an aggregate claim.

3. *"The -π/2 rotation observation means this is just doubling query heads, not a new positional encoding."* — **Removed as redundant.** This point is subsumed by the confound weakness above, but the harsh critic presents it as undermining the entire contribution rather than as an ablation that would strengthen it. The architectural observation is precisely the paper's insight.

4. *"The theoretical analysis treats q and k as independent random vectors, which is the opposite of how attention works."* — **Weakened** from a fatal objection to a minor weakness. This style of random-vector analysis is standard in the RoPE literature (including the original RoPE paper's "long-context decay" analysis). The limitations are acknowledged and the relative comparison between real and imaginary curves remains informative even if the absolute values should not be over-interpreted.

5. *"Missing appendix content, references, proofs."* — **Removed.** The appendix was stripped by the PDF parser; these items exist in the original submission.

6. Generic strengths from the Strength Finder about "the problem being important" or "addressing an interesting question" — **Removed.** These add no paper-specific signal.

## Novel Insights

None beyond the paper's own contributions. The key observation—that the discarded imaginary part of RoPE can be recovered by a −π/2 query rotation and provides useful long-context information—is the paper's own contribution, not something synthesized from the reviews.

## Suggestions

1. **Add the controlled baseline for RoPE++<sub>EC</sub>.** Train a "RoPE-2×" variant with standard RoPE, twice the query heads, and twice W<sub>o</sub>, keeping KV cache equal. If the imaginary mechanism provides genuine additional value, RoPE++<sub>EC</sub> should still outperform RoPE-2×. If not, the paper's claims need reframing.

2. **Provide a quantitative attention-distance metric.** Compute the average attention distance (or attention mass on tokens beyond some threshold) for real vs. imaginary heads across layers and sequences. This directly tests the theoretical claim and would be more informative than the current qualitative heatmaps.

3. **Run a cleaner position-ablation experiment.** Instead of Gaussian noise on all attention logits, perturb only the positional component (e.g., zero out the sin terms in imaginary heads) to more cleanly attribute the effect to position encoding rather than content importance.

4. **Acknowledge the confound explicitly** and clarify that RoPE++<sub>EC</sub>'s advantage likely reflects a combination of the imaginary mechanism and increased query-head capacity, with the two configurations (EH and EC) offering different evidence for different aspects of the contribution.

5. **Add error bars or seeds** at least for the headline long-context comparisons at 376M where gains are largest, to establish statistical significance.

## Score and Decision

**Calibration anchors used** (all from the deepreview_13k_calibration set):

| Anchor | Avg Score | How it compares to this paper |
|--------|-----------|-------------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GtvuNrk58a.md` (Round and Round We Go — RoPE analysis) | 6.20 | Both study RoPE mechanisms. That paper has cleaner analysis but narrower experiments (one model, no pre-training). This paper has broader experiments but a confound in the main comparison. Comparable quality overall. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eoln5WgrPx.md` (STRING — shifted RoPE) | 6.50 | STRING has a simpler method and more striking empirical results (10+ point gains on large models). This paper has a more novel architectural insight but weaker causal attribution. This paper is somewhat weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JO7k0SJ5V6.md` (Scaling Laws of RoPE) | 5.00 | That paper provides useful theory but only perplexity experiments. This paper has broader evaluation but a confound. This paper is stronger in experimental scope. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OhauMUNW8T.md` (Wavelet Positional) | 5.25 | Both propose new position encodings. That paper had marginal improvements. This paper has clearer gains and more thorough benchmarking. This paper is stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jp4pxKqCRW.md` (Periodic Extension) | 2.50 | Poorly written, no real theory, limited experiments. This paper is substantially stronger in all dimensions. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FJFVmeXusW.md` (HeadKV compression) | 6.50 | A focused KV-cache compression paper with clear empirical wins. Different task but similar evaluation rigor. This paper is slightly weaker due to the confound concern. |

Positioned relative to these anchors: the paper has a genuinely novel observation, clean architecture, and solid experiments at two scales. The main weakness (confound of doubled heads in EC) is real but partially mitigated by EH results and does not invalidate the paper's contribution — it primarily limits the *attribution* of the improvement mechanism. On balance, the paper's contribution is above the threshold for acceptance but has a notable gap that should be addressed.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>