Now I have all the data I need. Let me synthesize the final review.

**Calibration summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Scaling Laws of RoPE-based Extrapolation | 5.00 | R1 | Our paper is stronger — has pre-training, comprehensive benchmarks, novel method |
| A Controlled Study on Long Context Extension | 5.75 | R2 | Our paper is stronger — has novel method with pre-training, not just a study |
| Round and Round We Go! (RoPE analysis) | 6.20 | R1 | Comparable — our empirical validation is stronger but mechanical insights less deep |
| STRING (Shifted Rotary Position Embedding) | 6.50 | R1/R2 | STRING has more impressive empirical results on large models; our contribution is more fundamental architecturally |
| What is Wrong with Perplexity | 6.80 | R2 | Different category (metrics), not directly comparable |

**Bracket:** 5.0–7.0 → narrowed to 5.75–6.50. Our paper sits above the 5.75 study paper and the 5.00 analysis paper, roughly comparable to the 6.20 "Round and Round" paper (stronger empirically, less deep mechanistically), and below the 6.50 STRING paper (smaller-scale validation, less dramatic gains). **Final score: 6.0.**

---

## Summary
This paper proposes RoPE++, which augments standard Rotary Position Embeddings by re-incorporating the imaginary component of the complex-valued attention score as a parallel set of attention heads. The key technical insight is that the imaginary attention can be computed by simply rotating query vectors by −π/2 and reusing the same cached keys, yielding two configurations: RoPE++_EC (doubled heads, equal KV cache) and RoPE++_EH (equal heads, halved KV cache). Pre-training experiments at 376M and 776M scales with 50B tokens show consistent long-context benchmark improvements, particularly for RoPE++_EC, with no regression on short-context tasks. The method is compatible with existing context-extension techniques (PI, YaRN).

## Strengths
- **Elegant architectural insight (Section 3.1, Equation 4):** The observation that the negative imaginary part of the complex RoPE dot product can be computed as a simple −π/2 rotation of q_t followed by standard RoPE, reusing cached keys with zero additional KV-cache overhead, is genuinely clever and practically useful. This yields two efficient configurations trading off head count against cache size.
- **Principled theoretical motivation (Section 3.2, Equation 5):** The paper derives the characteristic curve of imaginary attention as a sine integral function Si(Δt) that decays far more slowly than the cosine-based real attention curve, providing theoretical justification for why imaginary heads should better capture long-range dependencies.
- **Causal evidence from noise-perturbation experiments (Section 5.2, Figure 5):** Adding Gaussian noise separately to real and imaginary attention and measuring RULER-4k degradation shows that corrupting imaginary attention hurts performance by 5–8 points more than corrupting real attention (σ=1.0), establishing that the trained model relies on imaginary attention for long-context modeling.
- **Consistent long-context benchmark gains (Table 2):** RoPE++_EC outperforms vanilla RoPE on every single context-length setting across RULER and BABILong at both model scales (e.g., RULER avg 25.0 vs. 18.8 at 376M, 29.4 vs. 27.4 at 776M). RoPE++_EH achieves comparable performance with half the KV cache.
- **No short-context regression (Table 1):** RoPE++_EC achieves the best average score on the 11-task short-context suite at both 376M (41.0 vs. RoPE's 40.1) and 776M (42.8 vs. RoPE's 42.0), confirming the method does not trade off standard competency.
- **Robustness across context-extension techniques (Section 5.3, Table 3):** RoPE++ maintains its advantage when combined with both Linear PI and YaRN across four model-size × method combinations, demonstrating generality.
- **Length-extrapolation analysis provides secondary mechanism (Section 3.4, Figure 3):** The paper identifies that imaginary attention exposes selected query-key dimension pairs to both positive and negative positional embedding values during pre-training, giving a concrete, falsifiable explanation for improved extrapolation beyond the primary long-dependency mechanism.
- **Practical efficiency gains validated (Section 5.1, Figure 4):** RoPE++_EH consistently reduces memory cost and increases throughput, with the margin widening at longer contexts (up to 128k).

## Weaknesses

### Fatal
None.

### Major
- **Characteristic curve analysis relies on an unstated cross-term cancellation assumption (Section 3.2, Figure 1):** The derivation treats the real attention characteristic curve as purely cos-based — c_Re(Δt) = (2/d) Σ cos(10^(−n/d) Δt). However, Equation 1 shows that standard RoPE attention includes both cos-weighted diagonal terms and sin-weighted cross terms: (q^(2n)k^(2n) + q^(2n+1)k^(2n+1))cos(θΔt) + (q^(2n)k^(2n+1) − q^(2n+1)k^(2n))sin(θΔt). The reduction to a pure cosine curve is valid only under the expectation that the cross-term dot products vanish (a standard assumption in RoPE analysis, likely detailed in the stripped Appendix B), but this assumption is not stated in the main text. Without it, a reader sees two different curves in Figure 1 and may incorrectly conclude that real and imaginary attention are more distinct than they actually are. The paper should explicitly acknowledge when this assumption is expected to hold and when it might be violated.

### Minor
- **RoPE++_EC head-count confound partially unaddressed:** RoPE++_EC doubles the number of attention heads relative to standard RoPE (Section 3.3: "merely doubling the attention head group size"). While the paper is transparent about this and provides the EH variant (equal heads) as a cleaner comparison, the EC variant's larger gains are partially attributable to increased representational capacity. The EH results show mixed but roughly comparable performance (RULER avg 28.6 vs. 27.4 at 776M, 18.2 vs. 18.8 at 376M), which partially mitigates the concern but does not fully isolate the imaginary formulation's contribution for the EC variant. A head-count-controlled baseline or explicit discussion of this confound as a limitation would strengthen the paper.

- **Modest short-context gains:** The average improvement of RoPE++_EC over RoPE is 0.9 points at 376M and 0.8 points at 776M on the short-context suite (Table 1). While the direction is consistent and there is no regression, the small magnitude makes the practical significance of these gains uncertain, especially from single training runs.

### Trivial
- **Occasional overclaiming:** The statement "these dimensions no longer suffer from the length extrapolation problem" (Section 3.4) is too strong — Table 2 shows all methods still experience significant performance drops at 64k vs. 4k contexts, including RoPE++.

## Nice-to-Haves
- Multiple training seeds with standard deviations would help assess whether the modest short-context gains are statistically reliable (though single-run pre-training at 50B tokens is standard practice and multi-seed would be very expensive).
- Validation at larger model scales (e.g., 1B+) would strengthen the long-context claims, though the current 376M/776M scale is reasonable for a methods paper.
- A head-count-controlled baseline for RoPE++_EC (e.g., standard RoPE with matched parameter count and doubled heads) would isolate the contribution of the imaginary formulation.

## Removed Points
These points were flagged by reviewers but are removed from the final review with justification:

- **"The 'discarded information' framing is mathematically unsound — the imaginary part contains no new information about q and k" (Harsh Critic Point 1):** This claim is mathematically incorrect. The complex product yields two linearly independent equations: Re = α·cos + β·sin and Im = β·cos − α·sin (where α and β are the two q-k dot product combinations). Given only the real part, α and β cannot be individually recovered; the imaginary part provides the second independent equation. The imaginary part genuinely contains information not recoverable from the real part alone. The paper's framing of "recovering discarded information" is mathematically justified. (The characteristic curve oversimplification is addressed separately as a Major weakness.)

- **"The noise-perturbation experiment is confounded — it shows learned specialization, not inherent properties" (Harsh Critic Point 4):** The paper's claim is explicitly about the trained model's behavior ("confirming that imaginary attention plays a more dominant role in long context modeling"), not about inherent properties independent of training. The noise experiment directly tests this claim, and the finding is valid. The theoretical characteristic curve analysis separately addresses inherent properties.

- **"No error bars, variance estimates, or multiple seeds — fatal evidential gap" (Harsh Critic Point 3):** Single-run pre-training at 50B tokens is standard practice in this field. Moved to Nice-to-Haves per the soft rule about practices not standard in the field.

- **"Missing related work on complex-valued neural networks" (Harsh Critic, Missing Parts):** The paper does cite Wang et al. (2025) and Lee et al. (2022) in Section 2. We do not flag missing references per the hard rules. Removed.

- **"Parameter-count transparency needed, ablation on head-sharing needed, missing appendix" (Harsh Critic, various):** The paper already describes parameter relationships in Section 3.3. The appendix was stripped by the parser. Removed as nitpicks or parser artifacts.

- **"The method should be tested on larger datasets and larger models" (Harsh Critic / soft rule):** This is a generic one-size-fits-all criticism. Moved to Nice-to-Haves.

## Novel Insights
The key novel insight is the observation that the imaginary part of the complex RoPE dot product can be computed as a simple rotation of q by −π/2 followed by standard RoPE, reusing cached keys with zero additional KV-cache overhead. This yields a genuinely parameter-efficient mechanism for providing each attention head with two complementary positional views: one dominated by cosine modulation (emphasizing local semantic aggregation) and one dominated by sine modulation (with a sine-integral characteristic curve that decays slowly, favoring long-range dependencies). The theoretical connection between the sine-integral curve and long-range preference is clean and motivating. The length-extrapolation analysis (Section 3.4) provides a second, independent theoretical benefit: imaginary attention exposes dimensions to a wider range of positional embedding values, reducing OOD issues.

## Suggestions
- Add an explicit statement in Section 3.2 acknowledging that the real attention characteristic curve derivation assumes cross-term dot products have zero expectation, and briefly discuss robustness when this assumption fails.
- Either add a head-count-controlled baseline for RoPE++_EC or explicitly discuss the head-count confound as a limitation, making clear that the EH variant (equal heads, half cache) provides the cleanest comparison point.
- Tone down the claim about "no longer suffering" from length extrapolation — the method clearly helps but performance still degrades substantially at extrapolated lengths.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>