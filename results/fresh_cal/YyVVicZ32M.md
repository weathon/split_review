Now I have all the calibration data I need. Let me write the final consolidated review.

---

## Summary

This paper introduces Permute-and-Flip (PF) decoding for LLMs, a method adapted from differential privacy that matches the perturbation-stability of softmax sampling (2/T-stable) while achieving provably lower perplexity (up to 2× smaller expected suboptimality and never worse than softmax at the same temperature). The paper also designs a cryptographic watermark (PF watermark) for this decoder, analogous to Aaronson's Gumbel watermark, which provides exact false positive rate control via a Gamma(n−m,1) null distribution. Experiments on C4 and Alpaca datasets with Llama-2 show that PF decoding (and its watermarked variant) achieves significantly lower perplexity than softmax sampling while maintaining detectability.

## Strengths

1. **Provably optimal stability–perplexity tradeoff (Theorem 3.1).** The paper proves that PF decoding has the same stability as softmax sampling (2/T-stable), achieves strictly better expected utility (never worse, up to 2× smaller suboptimality), and is Pareto-optimal among all equally-stable decoders. These are clean, rigorous theoretical results correctly attributed to McKenna & Sheldon (2020) and cleanly translated into the LLM decoding setting.

2. **Exact false positive rate control for watermark detection (Theorem 4.3, Figure 4).** The PF watermark detection score under the null follows a Gamma(n−m,1) distribution, enabling precise calibration of the false positive rate. Figure 4 validates this empirically — the theoretical α and empirical FPR align tightly across multiple datasets and keys, which is strong evidence for practical reliability.

3. **Computationally indistinguishable watermarked decoder (Theorem 4.3, point 1).** The watermark construction replaces i.i.d. exponential noise with a pseudo-random function, guaranteeing that the watermarked PF decoder is computationally indistinguishable from the non-watermarked version. This is a clean property that avoids distributional distortion.

4. **Lower perplexity than softmax sampling at the same temperature (Table 2).** The experimental results show PF decoding achieves substantially lower perplexity (PPL1, PPL2) than softmax sampling on both C4 and Alpaca, while the PF watermark retains near-identical perplexity and achieves high detection rates.

## Weaknesses

### Major

1. **Confounded comparison of watermarking methods in the main experiments.** Table 2 and Figure 3b compare the PF watermark (applied to PF decoding) against the Gumbel watermark (applied to standard softmax sampling). Because PF decoding itself yields lower perplexity than softmax sampling, the PF watermark inherits this perplexity advantage regardless of the watermark mechanism. The reader cannot tell whether the PF watermarking scheme itself is superior or whether the gains are simply from the underlying decoder. The paper partially addresses this in Section 4 with a 2-token example and Figure 2b (varying temperature to match suboptimality), but this controlled comparison is not replicated on real data. An experiment applying both watermark schemes to the *same* base distribution (e.g., PF sampling with exponential vs. Gumbel noise) is needed to isolate the watermark contribution. As it stands, the headline claim that "PF watermark achieves the best balance of the highest detection accuracy and lowest perplexity" conflates decoder quality with watermark mechanism.

2. **Incomplete evaluation of text quality beyond perplexity.** The paper's central practical argument is that PF decoding achieves lower perplexity than softmax while maintaining stability. However, PF is explicitly described as "more greedy" than softmax, and the paper acknowledges that greedy decoding suffers from high repetition and low MAUVE. The paper reports MAUVE and seq-rep-5 scores but does not analyze whether PF increases repetition or degrades MAUVE relative to softmax — it only notes these metrics for greedy decoding. Since the stability property (Definition 2.1) does not guarantee diversity, and PF concentrates mass on high-probability tokens relative to softmax, the possibility that PF harms diversity is a real concern that must be explicitly addressed. Without this analysis, the claimed practical advantage is incomplete.

### Minor

1. **Overclaiming in the abstract.** The abstract states that PF decoding is "never worse than any other decoder." The actual result (Theorem 3.1, point 5) establishes Pareto-optimality *among decoders that are 2/T-stable* — it does not claim dominance over greedy decoding, beam search, or arbitrary decoders. Point 3 specifically says "never worse than Softmax-sampling" (same temperature). The abstract's unqualified wording is materially inaccurate and should be corrected.

2. **Shallow analysis of MAUVE and seq-rep-5 results.** Beyond the omission discussed above, the paper mentions MAUVE and seq-rep-5 in the evaluation setup but only comments on greedy's poor performance. The actual PF vs. softmax comparison on these metrics is not discussed in the text, leaving the reader to infer from the table (which is an image) what the numbers show. A brief textual comparison and discussion would significantly strengthen the paper.

### Trivial

None.

## Nice-to-Haves

- **Computational cost discussion.** Algorithm 1 shuffles the entire vocabulary O(|V|) per step. The paper should briefly note that PF decoding is O(|V|) per step (comparable to softmax) and that the Report-Noisy-Max equivalent used for watermarking avoids explicit permutation. A practitioner would benefit from this clarity.
- **Limitations section.** The paper would benefit from explicitly acknowledging: (a) PF decoding is more greedy and may reduce diversity in low-entropy settings; (b) theoretical guarantees are per-step, not sequence-level; (c) the "2× better" bound is worst-case; (d) the watermark's null distribution assumes unique m-grams (though Figure 4 suggests robustness).
- **Table 2 caption clarity.** The caption should explicitly state which baseline uses which decoder (e.g., "Gumbel WM applied to softmax sampling; KGW WM applied to softmax sampling").

## Removed Points

- *Critic's note about hyperparameters for baselines not stated in the main text.* This is a standard reproducibility detail that typically belongs in the appendix. The critic acknowledges "presumably they appear in the appendix." Not a substantive weakness.
- *Critic's request for a full limitations section.* Moved to "Nice-to-Haves" — a reasonable suggestion but not a flaw in the paper's current arguments.
- *Critic's request for computational cost discussion.* Moved to "Nice-to-Haves" — useful context, not a core weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective that the paper itself does not already articulate. However, the reviews collectively highlight a gap the paper could address: the tension between PF's "more greedy" nature and the resulting diversity implications. The paper's own analysis of this tradeoff in the watermarking context (Section 4, Figure 2b) is quite insightful and could be productively extended to the text-quality discussion.

## Suggestions

1. **Run a controlled watermark comparison on real data.** Apply the Gumbel watermark to PF sampling (via the Report-Noisy-Max equivalence) and compare against the PF watermark on the same PF-derived distribution. This isolates the watermark contribution and would directly address the confound.
2. **Explicitly compare PF vs. softmax on MAUVE and seq-rep-5.** Report these numbers and discuss whether PF increases repetition or reduces diversity. If it does, acknowledge the tradeoff and describe when PF is preferable (e.g., factual generation) vs. when softmax may be better (creative tasks).
3. **Correct the abstract.** Replace "never worse than any other decoder" with "never worse than any other equally-stable decoder" or "never worse than softmax sampling and Pareto-optimal among stable decoders."
4. **Add a brief limitations paragraph** covering the points in "Nice-to-Haves" above.

## Score and Decision

**Calibration anchors (from retrieval):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `ujpAYpFDEA.md` (Watermark imperceptibility) | 7.50 | More comprehensive experiments than the current paper; stronger empirical validation. Current paper is weaker on experimental breadth. |
| `KS8mIvetg2.md` (Test set contamination) | 7.50 | Tight experimental validation with clean theoretical framing. Current paper has comparable theory quality but less thorough experiments. |
| `kRoWeLTpL4.md` (Copyright-protected generation) | 7.50 | Solid empirical work. Current paper is comparable in theory but weaker on experiments. |
| `0KHW6yXdiZ.md` (End-to-end watermarking) | 5.25 | Training-based method with moderate results. Current paper has cleaner theoretical contributions and is less dependent on training artifacts. Slightly stronger overall. |
| `hTUrBJqECJ.md` (Unbiased watermark) | 5.50 | Similar mix of theory + experiments, but their experimental improvements over baselines were limited. Current paper has stronger theoretical grounding and clearer advantages. |
| `eKGEsFdpin.md` (Sampling-based watermark) | 3.67 | Limited novelty vs. prior work, no formal analysis. Current paper is substantially stronger in theory and empirical grounding. |
| `jbfDg4DgAk.md` (Sparse watermark) | 3.00 | Weak security analysis and limited contributions. Current paper is much stronger across all dimensions. |

The paper's theoretical contributions are solid and well above the typical watermark paper in rigor. However, the experimental evaluation has two meaningful gaps (confounded watermark comparison, incomplete text quality analysis) that prevent it from reaching the 7.5 tier. The core decoder contribution is well-supported; the watermark claims need additional controlled evidence.

**Score:** 6.0  
**Decision:** Accept

The core contributions — PF decoding as a provably stable, lower-perplexity alternative to softmax sampling, and its natural watermark extension with exact FPR control — are theoretically sound and practically relevant. The experimental gaps are significant but fixable, and do not undermine the paper's central theoretical claims. With the suggested revisions (particularly the controlled watermark ablation and the diversity analysis), this would be a strong paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>