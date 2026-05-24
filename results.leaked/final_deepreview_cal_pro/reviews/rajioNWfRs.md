Now I have all the information needed. Let me compile the final review.

---

## Summary

This paper introduces TNT, a two-stage training paradigm for deep memory RNNs (e.g., Titans) that decouples training efficiency from inference performance. Stage 1 uses a hierarchical memory architecture — a global memory with large chunks for long-range context plus multiple local memories with periodic state resets to enable context parallelism — achieving substantial training speedups. Stage 2 is a brief fine-tuning phase adapting local memories to small chunk sizes for high-resolution inference. The method achieves up to 17× training speedup over the Titans baseline while simultaneously improving perplexity and reasoning accuracy.

## Strengths

- **Clear problem identification and motivation.** The paper identifies three concrete challenges (Section 3): training inefficiency of deep memory modules, key–query domain mismatch, and chunk-size sensitivity. Figure 2 provides compelling empirical evidence for the train–test chunk-size mismatch, showing that a model pre-trained with C=64 degrades significantly when evaluated at any other chunk size.

- **Novel hierarchical memory with periodic resets enabling context parallelism.** The local memory reset mechanism (Eq. 6) is the key innovation: by resetting local states to a learned W_init every S_L tokens, sequential dependencies across segments are broken, enabling massive parallelization of non-linear recurrences — a long-standing challenge. The hierarchical design (global + local) ensures that global context is not lost.

- **Strong empirical results.** Table 1 shows up to 17.37× training speedup vs. Titans (1.12 hrs vs. 19.48 hrs). Table 2 shows TNT Stage 2 with four local memories achieves 23.09 average perplexity vs. Titans' best 25.07, and 40.9% average reasoning accuracy vs. 39.0%. Figure 4 demonstrates linear runtime scaling with sequence length, crossing over to outperform FlashAttention at 32K length.

- **Rigorous ablation study.** Table 3 cleanly isolates each component: removing global memory degrades PPL from 21.04 → 25.60; removing Q-K projection degrades to 22.01; incrementally adding local modules (1→4) reduces PPL from 23.53 → 20.15. These provide strong causal evidence for each design choice.

- **Practical contribution.** TNT removes a critical scalability bottleneck for deep memory RNNs, making them viable for long-context training at scale. The two-stage approach is architecture-agnostic and could apply to other deep memory modules beyond Titans.

## Weaknesses

### Fatal

None.

### Major

- **Missing key baseline: Titans with the two-stage curriculum but no hierarchical memory.** The paper's central claim is that the hierarchical design and reset mechanism overcome the train–inference chunk-size mismatch. A natural baseline — standard Titans pre-trained with a large chunk size then fine-tuned with small chunks (the same two-stage recipe, but without hierarchical memory) — is absent. The ablation (Table 3) removes global memory and Q-K projection, but never tests whether the two-stage schedule alone on a vanilla Titans model would already capture a meaningful portion of the benefit. Without this, the value of the hierarchical architecture specifically (vs. curriculum learning alone) is not fully isolated. This weakens the experimental case for the paper's primary contribution.

### Minor

- **Time-to-quality metric uses training loss rather than validation perplexity.** Table 1 uses "target training loss 3.20" as the quality threshold. Since training dynamics differ across architectures (particularly due to the reset mechanism), training loss is an imperfect proxy for generalization quality. The separately reported perplexity results in Table 2 validate model quality independently, so this does not undermine the core claim, but the speedup numbers in Table 1 should be interpreted with this caveat.

- **No analysis of the local segment length S_L.** The reset length S_L is introduced as a critical hyperparameter (Eq. 6) and set to 2048 or 4096 in experiments, but its effect on model quality and training speed is never analyzed. Understanding the sensitivity to this parameter would help readers assess the practical limits of the reset mechanism.

- **No inference-time cost reported.** The paper focuses on training speed but never reports memory footprint or per-token latency at inference. Since the method claims to establish a "practical foundation" for these models, inference efficiency is relevant.

- **No variance measures on reasoning benchmarks.** The accuracy differences among top models in Table 2 are relatively small (e.g., 41.0% vs. 39.7% average accuracy). The paper acknowledges that "downstream task accuracy can be subject to higher variance" but reports no standard deviations, confidence intervals, or multi-seed results. This limits the statistical strength of the accuracy comparisons.

### Trivial

- The main text (Eq. 7, Section 4.1.2) describes retrieval for a single local memory, while Table 2 reports configurations with up to four. The generalized formulation is deferred to Appendix E. While this is acknowledged, a brief sketch of how multiple local memory outputs are combined would improve the self-containedness of the main text.

## Nice-to-Haves

- Presenting validation perplexity vs. wall-clock time curves (rather than just the training-loss threshold in Table 1) would connect efficiency claims directly to model quality at a glance.
- Reporting exact parameter counts broken down by component (backbone, global memory, each local memory) for each row in the results tables would strengthen transparency, even though the total is stated as 150M.
- Adding the omitted two-stage Titans baseline would sharply strengthen the contribution claim.

## Removed Points

These points were flagged by the harsh critic but are removed or demoted after cross-checking against the paper:

- **"Parameter count never clarified"** → The paper explicitly states "150M parameter models" (Section 5.1) and "TNT (150M parameters)" in Table 2's header. While a component-level breakdown would be nice, the total is stated. Demoted from "structural" to minor/nice-to-have.

- **"Figure 4 compares TNT against Titans with C=16 only"** → Figure 4 is about runtime scaling with sequence length, not about absolute speedup. The full speedup range across chunk sizes is shown in Table 1. The comparison is appropriate for the scaling analysis.

- **"Abstract selects slowest Titans variant for 17× claim"** → The abstract says "up to 17× faster than the most accurate baseline configuration," which is accurate: the highest-accuracy Titans uses C=8, which is indeed slowest. This is standard reporting practice (compare against the best-quality baseline).

- **"Efficient-implementation appendix was stripped"** → The parser strips appendices; this is not an author error. Points depending on missing appendix content cannot be verified.

- **"ξ notation could be more precise"** → Notation nitpick; the definition is clear: ξ(i,j) = i - (i mod j).

- **"Challenge 1 conflates lack of efficient kernels with architectural limitation"** → The paper distinguishes between training inefficiency and poor hardware utilization clearly in Section 3. This is a matter of framing, not a factual error.

- **"Global memory architecture (depth, hidden size) never stated"** → The global memory follows the Titans architecture using CG=2048. The paper states it uses the 150M Titan configuration from Behrouz et al. (2025d). Architectural details are consistent with the base model.

- **"Whether global memory is frozen during Stage 2 is not stated"** → Section 4.2: "During this stage, only the local memory modules are adjusted to use smaller chunk sizes." This implies global memory is unchanged. The concern is overstated.

## Novel Insights

The paper's empirical finding that deep memory modules exhibit extreme sensitivity to chunk-size mismatch (Figure 2) — with a model trained at C=64 suffering >2.5× perplexity degradation when evaluated at C=8 — is a genuinely useful observation for the field. It reveals that these models do not simply benefit from finer-grained inference; they become specialized to their training resolution. This motivates the two-stage approach and may inform future work on memory-augmented architectures beyond this paper's specific solution.

## Suggestions

- Add the two-stage Titans baseline (Titans pre-trained with large C, fine-tuned with small C, no hierarchical memory) as a single-row addition to Table 2 or Table 3. This would cleanly isolate the hierarchical architecture's contribution from the curriculum effect and substantially strengthen the paper's central claim.
- Include a brief paragraph or diagram in the main text sketching how multiple local memory outputs are fused during autoregressive generation, rather than relying entirely on the appendix.
- Report standard deviations for reasoning task accuracies, even if only from 2–3 training seeds, to support the statistical claims.
- Consider adding S_L sensitivity analysis or at minimum a qualitative discussion of how reset frequency trades off parallelism against local context retention.

## Anchor Comparisons

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| JOBokGDcX0 | 2.50 | R1 | Much weaker — limited chunk overlap study, no scale |
| N581Nje6fH | 1.50 | R1 | Much weaker — unrelated domain, poor execution |
| 4ymHtDAlBv | 2.33 | R1 | Much weaker — small RNN for text classification |
| 1MHgMGoqsH | 3.00 | R1 | Weaker — MPC training framework, limited evaluation |
| GrmFFxGnOR | 5.00 | R1 | TNT stronger — minLSTM/minGRU rejected for scale/novelty; TNT has larger experiments, clearer novelty |
| E34AlVLN0v | 6.00 | R1 | TNT somewhat stronger — DEER has limited tasks and memory issues; TNT has more comprehensive empirical validation |
| GQGNLEHmdl | 6.33 | R1,R2 | Different domain (compiler), less comparable |
| UU9Icwbhin | 4.75 | R1 | TNT stronger — RetNet rejected, less empirical depth |
| GRMfXcAAFh | 8.00 | R1 | TNT below — LinOSS has strong theoretical depth TNT lacks |
| TvGPP8i18S | 6.25 | R2 | TNT comparable/slightly stronger — MELODI has similar hierarchical memory concept but TNT has more comprehensive experiments, speed measurements, and ablation |
| nrvoWOWcyg | 6.50 | R2 | TNT comparable — CD-LM has strong methodology but different domain; TNT has comparable empirical depth |
| pCEgna6Qco | 6.75 | R2 | TNT slightly below — stronger methodological analysis in the anchor |
| ZYDEJEvCbv | 6.80 | R2 | TNT slightly below — more complete experimental story |

**Round 1 bracket:** 6.0–7.5 (above DEER at 6.00, below LinOSS at 8.00).

**Round 2 narrowing:** TNT sits solidly in the 6.25–6.75 range. It is stronger than MELODI (6.25) due to more comprehensive experiments and clearer practical impact, but slightly below the 6.75–6.80 anchors which have more complete methodological analysis. The missing two-stage Titans baseline and the lack of inference-protocol detail in the main text prevent a higher score.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>