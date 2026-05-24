Now I have strong calibration anchors. Let me write the consolidated review.

**Bracket analysis (Round 1):** The paper sits well above the weak band (avg 2.33–3.00) and clearly below the top band (avg 7.60–8.00). Initial narrowest plausible range: **5.0–7.5**.

**Round 2 anchoring:** The most comparable anchors are watermarking/decoding papers in the 5.25–6.33 range. The paper under review is stronger than JYu5Flqm9D (5.75), 9k0krNzvlV (5.75), and LdIlnsePNt (6.00) — it has cleaner theory, better presentation, and more rigorous guarantees. It's below mtSSFiqW6y (8.0, Oral). I'll place it around 6.5, which reflects a solid paper with meaningful contributions and some addressable weaknesses.

---

## Summary

This paper introduces the Permute-and-Flip (PF) decoder for LLMs, adapted from the differential privacy literature. PF decoding provably achieves the same stability as softmax sampling while never being worse and up to 2× better in expected suboptimality (Theorem 3.1). The paper also designs a PF watermark via the Report-Noisy-Max equivalence that provides exact false positive rate control (Theorem 4.3) and is computationally indistinguishable from the unwatermarked decoder. Experiments on Llama2-7B, Llama2-7B-Chat, and TinyLlama-1.1B across C4 and Alpaca datasets show that PF decoding (and its watermarked counterpart) achieves lower perplexity than softmax sampling and existing watermarking schemes at comparable detection accuracy.

## Strengths

1. **Pareto-optimal stability–perplexity tradeoff.** Theorem 3.1 proves that PF decoding is never worse than softmax sampling (point 3), up to 2× better in suboptimality (point 4), and Pareto-optimal among all 2/T-stable decoders (point 5). Example 3.2 and Figure 1 provide a concrete two-token case confirming PF's lower probability of selecting suboptimal tokens. This is a clean, non-trivial theoretical result directly supporting the paper's core claim.

2. **Exact, theory-driven false positive rate control.** Theorem 4.3 shows that under the null (key-independent text with unique m-grams), the PF watermark's test score follows a Gamma(n-m, 1) distribution, enabling exact FPR = α by setting τ = CDF⁻¹_Gamma(1-α). Figure 4 validates this empirically across multiple random keys on a log-log plot, demonstrating precise control that goes beyond heuristic thresholding.

3. **Favorable perplexity–detectability tradeoff in practice.** Table 2 and Figure 3b show that on C4 at T=1.0, PF watermark achieves PPL 8.33 (vs Gumbel WM 11.41, KGW WM 16.62) while maintaining TPR ≈ 0.984 at FPR=0.01. Across multiple temperature settings, PF watermark consistently attains the best combination of high TPR and low PPL among all compared schemes.

4. **Computationally indistinguishable watermark.** The PF watermark replaces i.i.d. exponential noise with a pseudo-random function of the key and preceding tokens (Algorithm 2). Under perfect pseudo-randomness, the watermarked distribution is computationally indistinguishable from the non-watermarked PF distribution, meaning the watermark does not alter the intended generation quality. This is theoretically grounded and empirically supported by the near-identical perplexity of PF and PF WM in Table 2.

5. **Evaluation across multiple models and datasets.** Experiments span Llama2-7B, Llama2-7B-Chat, and TinyLlama-1.1B-Chat on both open-ended generation (C4) and question-answering (Alpaca), demonstrating the generality of the approach.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Missing Top-p and Top-k baselines in experiments.** Table 1 lists Top-p and Top-k as decoding methods, and practitioners commonly use them for their favorable perplexity–diversity tradeoff. The experiments compare PF decoding only to greedy and softmax sampling. While the theoretical claim (Pareto-optimality among stable decoders) does not require these baselines since Top-p/k are not stable, the paper's broader practical claims (e.g., "a promising new approach for LLM decoding" in the abstract, "PF decoding produces significantly lower perplexity compared to sampling" in Section 5) would be strengthened by explicit comparison against these widely used methods. The paper does not need Top-p/k to support its core theoretical contribution, but including them would substantially bolster the practical relevance claims.

2. **No confidence intervals for detection metrics.** Table 2 reports TPR and AUC for watermark detection without uncertainty quantification. Standard errors for perplexity are reported but not for detection rates, making it difficult to assess whether differences between watermark methods (e.g., PF WM TPR 0.984 vs Gumbel WM TPR 0.988 at T=1.0) are statistically meaningful. This is important since these values are all near 1.0, and small differences could be noise.

3. **Inconsistency in Table 1: Greedy marked as watermarkable.** Table 1 marks Greedy with "✓" for Watermark, but Section 2 explicitly states that greedy decoding "is not watermarkable (at least not using existing techniques)." This is a clear internal contradiction that should be corrected.

4. **Gumbel WM perplexity anomaly.** In Table 2 (C4, T=1.0), Gumbel WM has perplexity 11.41 ± 0.27 versus non-watermarked softmax sampling at 12.47 ± 0.32. Since the Gumbel watermark is theoretically distribution-preserving, this gap (~2.5 SE) is notable and unexplained. The paper should either acknowledge this or provide an explanation (e.g., specific pseudo-random function behavior). This does not affect the paper's core claims (PF still outperforms both), but it raises a question about the baseline's correctness.

5. **MAUVE gap at T=0.8.** On C4 with T=0.8, PF decoding achieves MAUVE 0.92 vs sampling at 1.00. This non-trivial gap in distributional similarity to human text is not discussed. While PF decoding achieves lower perplexity, the paper should address whether this comes at a cost in distributional realism at lower temperatures.

### Trivial

- The paper should explicitly note that PF decoding via the Report-Noisy-Max formulation (Fact 4.2) is O(|V|) per token — the same as softmax sampling — since the permutation+coin-flip description might give the wrong impression about overhead.

## Nice-to-Haves

- An empirical validation of stability (e.g., robustness to logit perturbations or adversarial attacks) would directly demonstrate the practical value of the stability guarantee, beyond the theoretical proof in Theorem 3.1.
- A baseline applying the Gumbel watermark to PF decoding (or vice versa) would further isolate the contribution of the watermark algorithm from the decoder choice, though we note the paper's theory (Figure 2b) already addresses this at the analytical level for the two-token case.

## Removed Points

- **"Perplexity improvement not properly disentangled"** (Harsh Critic Point 2): The paper is transparent that PF WM = PF decoder + PF watermark, and the comparison is system-level (PF WM vs Gumbel WM). Section 4 explicitly states the PF watermark "enjoy[s] the performance boost that comes from replacing softmax sampling with PF." Figure 2b already includes the "Gumbel watermark on PF grid" baseline. No disentanglement issue exists given the paper's stated scope.
- **"Stability definition vs DP"**: The paper defines its own stability definition (Definition 2.1) and correctly cites known DP results for softmax and PF. No claim of equivalence to DP is made.
- **"Human evaluation / downstream task evaluation"**: This is outside the paper's scope; perplexity and MAUVE are standard evaluation metrics for decoding methods.
- **"Top-p/k missing" framed as a Major gap**: Downgraded to Minor since the core theoretical claims (Pareto-optimality among stable decoders) do not require them. The concern is only about practical relevance claims, which the paper can address.
- Various formatting nitpicks, speculations about unreleased items, and generic calls for more baselines without concrete justification were removed.

## Novel Insights

None beyond the paper's own contributions. However, a notable observation emerging from the reviews is that the paper's dual contribution — a provably Pareto-optimal decoder and a watermark with exact FPR control — creates a particularly clean pipeline where theory directly informs practice: the decoder optimization naturally leaves a statistical trace that the watermark exploits, and the same Report-Noisy-Max connection enables both the decoding guarantee and the watermark design. This tight coupling between the two contributions is an elegant structural feature that the paper could highlight more explicitly.

## Suggestions

1. **Fix Table 1**: Correct Greedy's Watermark entry from ✓ to ✗ to match the text in Section 2.
2. **Add Top-p sampling as a baseline** (at a few standard p values, e.g., 0.9, 0.95) for the text generation comparisons to strengthen the practical relevance claims.
3. **Include confidence intervals or standard errors** for TPR and AUC in Table 2.
4. **Briefly discuss** the Gumbel WM perplexity anomaly and the MAUVE gap at T=0.8, even if just to acknowledge the observations.
5. **Explicitly state** that PF decoding is O(|V|) per token via the Report-Noisy-Max equivalence.

## Score and Decision

**Round 1 bracket:** The paper is clearly above the weak anchor papers (avg 2.33–3.00 on LLM/watermarking topics) and clearly below the top-tier papers (avg 7.60–8.00). Plausible range: **5.0–7.5**.

**Round 2 narrowing:** Compared to:
- JYu5Flqm9D (5.75, Accept Poster): Codable Watermarking. Current paper has stronger theory (Pareto-optimality, exact FPR), better presentation, and comparable experiments. **Stronger.**
- 9k0krNzvlV (5.75, Accept Poster): Learnability of Watermarks. Limited novelty (distillation is well-known). Current paper has more original theoretical contributions. **Stronger.**
- LdIlnsePNt (6.00, Reject): Semantic-aware watermarking theory. Had unfair comparison issues and impractical assumptions. Current paper is more practical and better written. **Stronger.**
- vXf8KYTJmm (5.25, Reject): MAP decoding analysis. Had poor presentation and limited evaluations. Current paper is far stronger. **Much stronger.**
- mtSSFiqW6y (8.00, Accept Oral): Judge Decoding for speculative sampling. This paper had more impactful empirical results (9× speedup), broader implications, and was accepted as Oral. Current paper has stronger theory but weaker experimental scope. **Weaker.**

The paper is stronger than the 5.75–6.00 watermarking anchors but not at the level of the 8.00 oral paper. Its main weaknesses (missing practical baselines, minor presentation issues) are addressable and do not threaten its core contributions. Weighted against the calibration anchors, the appropriate score is **6.5**.

**Final score: 6.5/10 — a solid paper with clear theoretical contributions, a well-designed watermark, and addressable experimental gaps.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>