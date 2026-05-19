## Summary
This paper introduces Permute-and-Flip (PF) decoding as a new decoding method for LLMs, adapted from the differential privacy literature. PF decoding provably matches the perturbation-stability of softmax sampling while achieving up to 2× lower expected suboptimality and never being worse (Pareto-optimal among equally stable decoders). The paper further designs a PF watermarking scheme (via the Report-Noisy-Max interpretation) that yields a test score with known Gamma distribution under the null, enabling precise false positive rate control. Experiments on C4 and Alpaca datasets with Llama-2-7B show that PF decoding (and its watermarked variant) achieves lower perplexity than softmax sampling at the same temperature, and the PF watermark attains high detection accuracy.

## Strengths
- **Theorem 3.1 provides a clean, multi-faceted theoretical characterization of PF decoding.** The paper proves that PF has the same $(2/T)$-stability as softmax, is never worse (and up to 2× better) in expected utility, and is Pareto-optimal among all equally-stable decoders. These are genuine formal guarantees, properly attributed to McKenna & Sheldon (2020) but brought together in a unified presentation for LLM decoding.

- **Example 3.2 and Figure 1 give a concrete, analytically tractable case where PF strictly beats softmax.** In the two-token case with logits $[\Delta, 0]$, PF chooses the suboptimal token with probability $1/(2e^{\Delta/T})$ vs. softmax's $1/(1+e^{\Delta/T})$, and the advantage is shown to hold across all temperatures and gaps. This provides direct intuition for the "never worse" claim.

- **The PF watermark design (Algorithms 2 and 3, Theorem 4.3) is principled and leverages the Report-Noisy-Max equivalence.** The watermark inherits computational indistinguishability from the unwatermarked PF decoder, and the test score's Gamma null distribution enables exact FPR calibration. Figure 4 shows strong empirical alignment between theoretical and empirical FPRs across multiple datasets and keys.

- **Empirical results (Table 2, Figure 3b) show the PF watermark achieves a favorable perplexity-detectability tradeoff compared to baselines.** On C4, PF watermark attains the highest TPR (1.000 at 0.01 FPR) with the lowest PPL1 (6.38) compared to Gumbel WM (1.000 TPR, 7.20 PPL1) and KGW WM (0.195 TPR, 7.24 PPL1). The paper also reports results on a smaller model (TinyLlama-1.1B) and discusses robustness to paraphrasing and short texts.

## Weaknesses
### Major

- **Theorem 4.3's exact Gamma null relies on the "all m-grams are unique" condition, and the paper does not analyze its practical impact.** The theorem states that under the null, the test score follows Gamma$(n-m,1)$ only if all m-grams in the text are unique (line 276). The paper does not discuss how frequently this condition holds in real text, how the distribution degrades when it is violated, or whether the Gamma approximation remains robust under typical repetition patterns. While Figure 4 shows good empirical FPR alignment, it does not specifically test systematic violations (e.g., long repetitive text, common n-gram repetitions). This gap weakens the advertised claim of "precise control over false positive rates" because the conditions under which the guarantee holds exactly are stronger than what a reader might assume.

- **Critical experimental hyperparameters are not reported.** The temperature $T$ and watermark context length $m$ are never given numeric values, despite being central to the algorithms. The paper states "Using the same temperature" (line 339) without specifying what temperature was used. Without these numbers, the experiments cannot be independently reproduced or fairly compared against future work.

- **Reported metrics lack error bars or measures of variance.** Perplexity, TPR, and F1 scores are reported as point estimates without standard deviations or confidence intervals. Given the stochastic nature of LLM sampling and watermark keys, single-run estimates are insufficient for establishing the reliability of the results. The claim of "significantly lower perplexity" (line 339) is not backed by any statistical test.

### Minor

- **Abstract overstates the generality of the "never worse" claim.** The abstract says PF is "never worse than any other decoder" (line 4). Theorem 3.1 shows this is true relative to equally stable decoders (Pareto-optimality), not unconditionally for all decoders. The missing qualifier could mislead readers.

- **The decoder and watermark contributions are not disentangled in the main experiments.** Table 2 and Figure 3b compare PF watermark (with PF decoding) against Gumbel watermark (with softmax sampling) at the same temperature. Since PF decoding already yields lower perplexity than softmax, the PF watermark's perplexity advantage is partly inherited from the decoder, not purely a watermark property. The paper acknowledges this distinction in the theory (Figure 2b, lines 315-318) and includes a controlled comparison in the two-token case, but the main empirical results do not separate the effects. A direct control (e.g., applying Gumbel watermark to the PF distribution) would strengthen the claim.

- **The connection between stability and diversity is asserted without formal support.** The paper states "stability implies an intuitive notion of diversity" (line 55) but does not formalize or empirically validate this connection. Stability bounds how much log-probabilities can change under logit perturbations; diversity (e.g., low repetition rate) is a related but distinct concept. The claim is not critical to the paper's core contributions but is an unsubstantiated overreach.

### Trivial

- None that survive filtering (formatting artifacts in the extracted text are parser issues, not paper problems).

## Suggestions
1. **Explicitly state temperature $T$ and context length $m$ used in experiments.** These are essential for reproducibility.
2. **Add error bars or confidence intervals to all reported metrics.** Even single-variance reporting across several random seeds or keys would substantially strengthen the empirical claims.
3. **Discuss the practical scope of the "all m-grams unique" condition in Theorem 4.3.** Provide empirical evidence that the Gamma null distribution holds approximately even when the condition is violated, or characterize the deviation.
4. **Add a controlled experiment that applies the Gumbel watermark to the PF decoding distribution**, so the perplexity advantage can be attributed to the watermark design rather than the base decoder.
5. **Qualify the abstract's "never worse than any other decoder"** to specify "never worse than any other equally-stable decoder" for precision.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
