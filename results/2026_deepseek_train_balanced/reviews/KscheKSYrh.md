## Summary

FreqKV proposes compressing the KV cache in decoder-only LLMs by exploiting energy concentration in the low-frequency components of the Discrete Cosine Transform (DCT). The KV cache is iteratively compressed: DCT is applied along the sequence dimension, high-frequency components are discarded at a retaining ratio, and inverse DCT reconstructs a smaller set of vectors — all without adding parameters or modifying architecture. The method achieves competitive perplexity against full-cache methods on language modeling and outperforms inference-only compression baselines on LongBench.

## Strengths

1. **Genuinely novel compression direction.** Prior KV cache compression for decoder-only LLMs relied on eviction, merging, or learned compression modules. FreqKV is the first to operate in the frequency domain via DCT truncation — a clean approach that adds no parameters. (Section 4.2, lines 106–127; Section 2, line 34)

2. **Well-motivated by an empirical observation.** The premise — KV state energy concentrates in low-frequency components as computation progresses — is grounded in a power spectrum analysis across 1000 CNN/Daily Mail documents (Figure 1). This observation directly motivates the truncation strategy. (Section 4.1, lines 90–102)

3. **Competitive perplexity from a compressed cache.** On PG-19 at 8K context, FreqKV achieves perplexity comparable to Full FT and LongLoRA (both using full KV cache at inference) and outperforms LoCoCo (which uses learned convolutional compression modules). (Table 1, Section 5.2, line 178)

4. **Zero additional parameters and clean design.** Unlike Activation Beacon (~2B extra parameters for a 7B model) or LoCoCo (convolutional modules), FreqKV uses only DCT/IDCT. Section 6.2 further shows that models trained with FreqKV can switch to full KV cache at inference and perform *better*, confirming training does not corrupt the original attention. (Sections 2, 6.2)

5. **Informative ablations.** The retaining-ratio analysis (Table 4, Figure 4) quantitatively justifies γ=0.5 by mapping the FLOPs/inference-time trade-off. The rescaling ablation (Figure 6) identifies and fixes a subtle signal-processing issue (IDCT normalization amplification) that would cause training instability. (Sections 6.1, 6.3)

6. **Demonstrated efficiency gains.** Figure 3 shows decoding time growing approximately linearly with FreqKV versus quadratically for full cache. Complexity analysis shows compression cost is O(N log N) and negligible relative to quadratic self-attention. (Section 5.3, Section 6.1)

## Weaknesses

### Fatal
None.

### Major

1. **LongBench comparison is asymmetric, overstating the "SOTA" claim.** FreqKV undergoes supervised fine-tuning on LongAlpaca (6.28K QA samples, 5 epochs) before evaluation on LongBench (Section 5.1). The four baselines in Table 3 — LM-Infinite, LongHeads, SnapKV, PyramidKV — are inference-only methods receiving no training. The paper claims "FreqKV achieves SOTA" (line 192) based on this comparison, conflating the benefit of compression with the benefit of task-specific fine-tuning on long-context QA data. To substantiate the claim, the paper should either compare against other *training-based* methods (LongLoRA, LoCoCo, Activation Beacon — all discussed in Section 2) or evaluate FreqKV in an equivalent zero-shot setting alongside the inference-only baselines.

### Minor

1. **No analysis of cumulative degradation from iterative compression.** Early tokens undergo multiple rounds of DCT truncation → IDCT reconstruction (estimated ~14 rounds for a 32K sequence with N=4096, L=2046). The paper provides no analysis of whether reconstruction error compounds. Section 6.2 partially addresses this by showing the full-KV switch works, but a direct analysis (e.g., cosine similarity between original and iteratively compressed states, or perplexity as a function of compression rounds) would strengthen the paper.

2. **No variance reporting.** Perplexity and LongBench scores are reported as point estimates without standard errors or confidence intervals. Given that differences between methods are sometimes small, some measure of variance is needed to assess reliability.

3. **Sink token count (S=4) taken from prior work without validation.** No ablation studies the sensitivity of FreqKV to the number of sink tokens. Since sink tokens are the only ones that never undergo compression, their role is disproportionately important and should be validated within the FreqKV framework.

4. **Perplexity evaluated only up to 8K despite training up to 32K.** The model is trained on 8192, 16384, and 32768 sequence lengths (Section 5.2), but Table 1 reports perplexity only at 2048, 4096, and 8192. Reporting at 16K and 32K would directly demonstrate effectiveness at the maximum claimed context length.

5. **Rescaling factor derivation is brief.** The √(L/N) rescaling (Equation 8) is introduced with an intuitive justification. A short derivation showing it preserves a principled quantity (e.g., ℓ₂ norm) would improve exposition.

### Trivial
None.

## Nice-to-Haves

- A Pareto-style visualization (perplexity vs. inference time or memory at a given context length) would help readers directly assess the compression trade-off across methods.
- A brief mathematical note that the truncated DCT + IDCT + rescaling is equivalent to projecting the sequence onto a low-frequency subspace would clarify what the compressed vectors represent, though the empirical results already demonstrate the approach works.

## Removed Points

These points were flagged by reviewers but removed per filtering rules:

- *Harsh Critic's "semantic interpretation of compressed KV states is underspecified"* — The paper mathematically defines what the compressed vectors are (DCT truncation + IDCT + rescaling, Equation 8). Requesting a "semantic" interpretation of an intermediate representation is an exposition preference, not a genuine weakness.
- *Equation formatting / truncation complaints* — Parser artifacts from PDF extraction, not author errors.
- *Missing appendix/proofs* — The parser strips appendix content; these exist in the original submission.
- *Criticism about LoCoCo comparison "missing crucial context"* — The paper clearly states LoCoCo uses convolutional modules and reports comparable numbers. The framing that this is "missing crucial context" is not supported by the paper.
- *Strength Finder's "SOTA on LongBench" as a standalone strength* — This conflicts with the verified weakness about asymmetric comparison. The factual achievement (highest average score on the reported set) is noted contextually, but the "SOTA" framing is removed pending resolution of the asymmetry issue.

## Novel Insights

None beyond the paper's own contributions. The key insight — KV cache energy concentrates in low frequencies in decoder-only LLMs, enabling compression via DCT truncation — is the paper's own discovery and is well-articulated. The reviews do not surface a novel cross-connection the paper itself does not already present.

## Suggestions

1. **Address the LongBench asymmetry directly.** Compare against at least one training-based context extension method (LongLoRA, LoCoCo, or Activation Beacon) on the same benchmark, or provide a zero-shot evaluation of FreqKV alongside the inference-only baselines. Clearly separate the benefit of the compression strategy from the benefit of SFT when making comparative claims.
2. **Add iterative compression fidelity analysis.** Track reconstruction error (cosine similarity or MSE between original and compressed KV states) as a function of compression rounds, or report perplexity on early tokens undergoing repeated compression.
3. **Report variance** (standard errors or confidence intervals) for the main results in Tables 1 and 3.
4. **Include perplexity at 16K and 32K** in Table 1 to match the reported training lengths.
5. **Ablate the number of sink tokens** (e.g., S ∈ {0, 2, 4, 8}) to validate this design choice.

## Score and Decision

The paper presents a genuinely novel and well-motivated compression method with clean empirical support on language modeling. The core weakness is the overstated "SOTA" claim on LongBench due to an asymmetric comparison against inference-only methods. This is addressable and does not invalidate the method's overall contribution, but it does temper the headline result. With the asymmetry addressed and the missing analyses added, this paper would be substantially stronger.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>