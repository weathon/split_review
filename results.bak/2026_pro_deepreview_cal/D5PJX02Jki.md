Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

This paper proposes RoPE++, an extension to Rotary Position Embeddings that re-incorporates the imaginary component of the complex-valued attention score—which is discarded in standard RoPE—as a parallel group of attention heads. Two configurations are introduced: RoPE++_EC (equal KV cache, doubled attention heads) and RoPE++_EH (equal attention heads, halved KV cache and QKV parameters). Both preserve RoPE's unified absolute–relative position-embedding format. Pre-training experiments at 376M and 776M scales demonstrate consistent improvements over standard RoPE and other position embeddings on short-context benchmarks, with larger gains on long-context benchmarks (RULER, BABILong). A noise-perturbation experiment provides causal evidence that the imaginary attention heads are the primary driver of long-context performance.

## Strengths

- **Clean mathematical derivation**: The imaginary attention is derived in a form that can be expressed equivalently as either relative or absolute position embedding, requiring only a −π/2 rotation of the query before applying standard RoPE (Equations 3–4, Section 3.1). This preserves RoPE's key theoretical property seamlessly.

- **Consistent and significant long-context gains**: On RULER and BABILong (Table 2), RoPE++_EC substantially outperforms standard RoPE across all tested context lengths. For the 376M model with long-context training, RoPE++_EC achieves RULER average 25.0 vs. 18.8 and BABILong average 16.1 vs. 11.0.

- **Causal evidence for imaginary attention's role**: The noise-injection experiment (Figure 5, Section 5.2) shows that adding Gaussian noise to imaginary attention heads degrades RULER-4k performance significantly more than the same perturbation applied to real heads (8-point gap at σ=1.0 for 776M), directly confirming the imaginary heads are the dominant mechanism for long-context modeling.

- **Practical efficiency with RoPE++_EH**: RoPE++_EH matches or exceeds standard RoPE's performance while using half the KV cache and QKV parameters, with demonstrated memory reduction and decoding speedup that widens as context length grows (Figure 4).

- **No degradation on short-context tasks**: Table 1 shows RoPE++ variants achieve the best or near-best average scores across 11 short-context benchmarks at both model scales.

- **Compatibility with existing methods**: When combined with PI or YaRN for context extension (Table 3), RoPE++ consistently yields the best average scores, demonstrating orthogonality to existing techniques.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Parameter asymmetry in RoPE++_EC**: The paper acknowledges that RoPE++_EC doubles W_o relative to standard RoPE (line 110–111). While W_q/K/V are shared and the parameter increase from W_o alone is modest compared to total model size, the EC variant does have more parameters than the RoPE baseline. The RoPE++_EH results (half QKV parameters, matching performance) provide strong evidence that the imaginary component itself delivers value, but a parameter-matched baseline for EC (e.g., a wider RoPE model with comparable total parameters) would make the attribution more airtight.

- **Limited model scale**: Evaluations are conducted only at 376M and 776M parameter counts. While two sizes provide some evidence of consistency, the absence of results at 1B+ scale leaves uncertainty about whether the benefits of the imaginary component persist at the scales where long-context LLMs are typically deployed.

- **Long-context evaluation limited to synthetic benchmarks**: RULER and BABILong, while standard in the community, are synthetic retrieval/QA benchmarks. No real-world long-context tasks (e.g., long-document summarization, multi-document QA, book-level comprehension) are evaluated, which limits the practical significance claims.

- **Single training run per configuration**: All reported metrics are point estimates from single training runs. For short-context tasks where average gains are modest (e.g., 376M Short: RoPE++_EC avg 41.0 vs. RoPE 40.1), seed sensitivity is relevant to assessing robustness.

### Trivial

- **Figure 2 caption and Section 3.3 description could be clarified**: The caption for Figure 2b states "key heads are halved" and Figure 2c states "key heads are doubled," which may confuse readers about the actual mechanism (the key projection is shared; what changes is how query heads pair with key heads). The architectural description in Section 3.3 would benefit from explicit dimension formulas for each variant.

## Nice-to-Haves

- A RoPE baseline with increased width to match RoPE++_EC's parameter count would isolate the imaginary component's contribution from capacity effects.
- Evaluation on at least one real-world long-context task (e.g., LongBench, ∞Bench, or a long-document QA dataset) would strengthen practical significance.
- Scaling experiments at 1B+ to demonstrate the method's benefits persist at practical deployment scales.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Confounded evaluation — RoPE++_EC doubles query heads, increasing Q-projection parameters"**: The paper explicitly states that W_q is *shared* between real and imaginary attention (line 112–113: "Both RoPE++_EH and RoPE++_EC share W_q between the real and imaginary attention"). The QKV parameter budget is indeed fixed. The W_o increase is acknowledged separately. This criticism misreads the architecture.

- **"The statement that QKV budget is fixed is factually wrong"**: Removed for the same reason — the paper correctly notes Q is shared.

- **"Weak theoretical justification — the first frequency period is ~62,831, far exceeding the 4,000 training length"**: This objection only applies to the lowest-frequency dimension. For high-frequency RoPE dimensions (θ_n near 1), the period is ~6.28 tokens, well within the training length. The paper's claim is that *more* dimensions see the full range, and this holds for high-frequency dimensions. The theoretical argument is largely sound.

- **"'Discarded information' framing is misleading — standard RoPE doesn't lose information"**: This is a semantic debate about whether the imaginary part constitutes "discarded" vs. "alternative" information. The paper's framing is reasonable and does not affect the technical contribution.

- **"Noise experiment may be confounded by different magnitude distributions"**: This is speculative without evidence that the magnitude distributions actually differ. The experiment uses the same σ for both components, which is a reasonable default. Without measured evidence of distributional differences, this does not rise to the level of an identified weakness.

- **"Missing appendix, missing proofs, missing references"**: These reflect parser artifacts; the original submission contains the complete appendix.

## Novel Insights

The paper makes an interesting observation that goes beyond its core contribution: the real and imaginary attention components of RoPE can be understood as complementary signals with fundamentally different distance-decay profiles — the real part decays as a cosine integral (favoring semantic locality), while the imaginary part decays as a sine integral (retaining sensitivity to distant positions). This decomposition into two complementary attention channels sharing the same key-value representations, but with different positional sensitivity via a simple −π/2 query rotation, is a clean insight that could inspire other dual-channel attention designs.

## Suggestions

- Add a table explicitly listing parameter counts (Q, K, V, W_o, total) and KV cache sizes for standard RoPE, RoPE++_EC, and RoPE++_EH at each model size. This would resolve all ambiguity in Section 3.3.
- Consider reporting results from a RoPE baseline with the same total parameter count as RoPE++_EC (e.g., widening the FFN or attention dimensions proportionally) to isolate the imaginary component's contribution. Even reporting this as a single ablation at one model size would substantially strengthen the paper.
- Add at least one downstream long-context task beyond synthetic retrieval, such as a long-document QA benchmark from LongBench or ∞Bench.

---

This paper makes a genuine, well-executed contribution: re-incorporating the imaginary component of RoPE as a parallel attention channel is a simple, theoretically clean idea that demonstrably improves long-context performance while enabling practical efficiency gains through the EH variant. The mathematical derivation is sound, the two-configuration design is thoughtful, and the experimental evidence — spanning short-context, long-context, efficiency, causal perturbation, and compatibility experiments — provides converging support for the core claims. The main limitations are the small model scale (376M–776M) and the restriction of long-context evaluation to synthetic benchmarks, which temper confidence in the method's practical impact at deployment scale. These are addressable limitations rather than fundamental flaws, and the paper as it stands makes a solid contribution to the position-embedding literature.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>