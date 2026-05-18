Now I have a thorough understanding of the paper and can cross-check all claims. Let me write the final review.

## Summary

This paper introduces Permute-and-Flip (PF) decoding for LLMs, adapted from a differential privacy mechanism (McKenna & Sheldon, 2020), and a corresponding PF watermarking scheme analogous to Aaronson's Gumbel watermark. The PF decoder is proven to have the same (2/T)-stability as softmax sampling while achieving strictly better expected utility (up to 2× smaller suboptimality) and a Pareto-optimal stability-perplexity tradeoff. The PF watermark provides provable false positive rate control (Gamma(n−m,1) under unique m-grams). Experiments on C4 and Alpaca with Llama-2-7B show PF decoding achieves lower perplexity than softmax sampling at the same temperature, and the watermarked system attains competitive detectability.

## Strengths

- **Rigorous theoretical framing connecting stability, utility, and watermarking.** Theorem 3.1 cleanly establishes that PF decoding is never worse than softmax sampling at the same temperature (Statement 3), is Pareto-optimal among all equally stable decoders (Statement 5), and can achieve up to 2× smaller suboptimality (Statement 4). This gives practitioners a principled reason to prefer PF over softmax.
- **Provable FPR control for the PF watermark.** Theorem 4.3 derives the exact null distribution of the test statistic (Gamma(n−m,1)) under unique m-grams, enabling precise Type-I error control without calibration data. Figure 4 validates this empirically across multiple datasets and keys — a genuine practical advantage over heuristics-based watermarks.
- **Clear presentation and intellectual honesty.** The paper explicitly states that the PF decoder comes from the DP literature (McKenna & Sheldon, 2020), that the theoretical results are direct translations of existing DP theorems, and that at the same temperature, PF watermark has lower detectability than Gumbel watermark (Figure 2a). This transparency is commendable.
- **The synthetic two-token analysis (Example 3.2, Figure 2b) provides an insightful equal-suboptimality comparison.** The paper acknowledges that comparing at equal temperature is misleading and presents a controlled comparison showing PF watermark can match or slightly beat Gumbel watermark when suboptimality is aligned.

## Weaknesses

### Fatal

None.

### Major

- **The experimental watermark comparison (Table 2, Figure 3b) compares PF watermark and Gumbel watermark at the same temperature, confounding decoder and watermark effects.** The paper's own analysis (Example 4.5, Figure 2a) shows that PF watermark has *lower* detectability than Gumbel watermark at the same temperature — and explains this is because PF is greedier, leaving less entropy for the watermark to exploit. When the paper then claims PF watermark "achieves the best balance of the highest detection accuracy and lowest perplexity" based on same-temperature experiments, the improvement in perplexity is entirely attributable to the PF decoder (which is known to have lower perplexity by Theorem 3.1), not to any property of the watermark. The paper provides the fair comparison (equal suboptimality) only in the synthetic two-token case (Figure 2b). The real-world experiments should match perplexity across methods before comparing detectability, or the claim should be moderated to "the PF *system* (decoder+watermark) achieves the best balance" with an explicit caveat about the confound.

- **The core algorithmic novelty is limited.** The PF decoder is a direct transplant from DP without modification; the paper cites McKenna & Sheldon (2020) for all its theoretical properties. The PF watermark is described as "an analog of Aaronson (2023)'s Gumbel-Watermark" — it replaces Gumbel noise with Exponential noise using the Report-Noisy-Max equivalence (Ding et al., 2021). While applying these ideas to LLM decoding is a legitimate contribution, the paper does not introduce new mechanisms, new algorithms, or solve a problem that prior methods could not address. The contribution is primarily an application/adaptation paper. This is not fatal (many such papers are valuable), but it limits the paper's significance.

### Minor

- **The abstract overstates the "never worse than any other decoder" claim.** The abstract reads: "provably up to 2× better in its quality-stability tradeoff than sampling and never worse than any other decoder." Theorem 3.1(3) only proves PF is never worse than *softmax sampling* at the same temperature. Theorem 3.1(5) proves Pareto-optimality among *equally stable* decoders. These are considerably narrower than "any other decoder." Greedy decoding achieves lower perplexity (though at the cost of stability and diversity), and decoders with different stability parameters are not covered. The abstract should qualify this claim.
- **The context length m for the pseudo-random function is not reported in the main experimental section.** This hyperparameter is critical for reproducibility and for assessing the unique m-gram assumption (Theorem 4.3, statement 2). The paper describes the watermark's dependence on m in Algorithms 2-3 but does not state what value was used in Table 2 / Figure 3.
- **The unique m-gram assumption for exact Gamma distribution (Theorem 4.3, statement 2) is not tested under violation.** For realistic text, repeated m-grams are common. The paper validates FPR empirically (Figure 4) but does not discuss what happens when m-grams repeat, whether the FPR control degrades, or provide guidance on choosing m to mitigate this issue.

### Trivial

- The paper uses perplexity as the primary quality metric but acknowledges (Section 2) that lower perplexity does not always imply better text. This tension is noted but not resolved.

## Nice-to-Haves

- An equal-perplexity comparison in the real-data experiments (vary temperature independently for PF and Gumbel watermark to match perplexity, then compare detectability) would directly support the synthetic insight from Figure 2b and strengthen the watermark claims substantially.
- Reporting the chosen value of m and studying its effect on detectability and FPR control would improve reproducibility.
- A brief discussion of computational overhead (PF via Report-Noisy-Max is O(|V|) like softmax) would complete the practical picture.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"The paper's core novel contribution is thin" as a fatal-level weakness** — This is a genuine limitation but the paper is transparent about it and the application to LLMs with watermark design is a reasonable contribution. Moved from "fatal" to "major" tier.
- **Criticism about missing appendix/proofs** — The parser strips these; they exist in the original submission.
- **"Computational efficiency" checkmark in Table 1 is misleading** — PF has the same O(|V|) complexity as softmax; the permutation step is a constant-factor overhead, not a fundamental efficiency problem. This is a nitpick.
- **"Stability is never used in experiments"** — Stability is a theoretical property used to prove the Pareto-optimality result (Theorem 3.1(5)); it does not need to be measured experimentally.
- **Various generic strengths from Strength Finder** — Claims about "the paper addressed an important problem" and other non-specific praise are removed.
- **Strength Finder's "Example 3.2 and Figure 1 give an explicit illustrative comparison"** — This is retained implicitly but as a minor supporting point, not a core strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Moderate the abstract's "never worse than any other decoder" claim** to reflect the precise scope: it applies to softmax sampling at the same temperature (Theorem 3.1(3)) and to decoders with equal stability in a Pareto sense (Theorem 3.1(5)).
2. **Add an equal-perplexity comparison** for the real-data watermark experiments: sweep temperature for both PF watermark and Gumbel watermark, match perplexity levels, then plot detectability. This would directly confirm whether the synthetic insight from Figure 2b holds in practice.
3. **Report the value of m** used in all watermark experiments and provide guidance on how it affects the unique m-gram assumption.
4. **Acknowledge the repeated m-gram limitation** of Theorem 4.3 statement 2 and discuss practical implications (e.g., how often m-grams repeat in natural text at different m values).

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ujpAYpFDEA.md` | 7.50 | **Better.** Novel task (imperceptibility detection), strong cross-model experiments. This paper has less novelty and narrower evaluation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/E4LAVLXAHW.md` | 7.00 | **Better.** First rigorous black-box detection of watermarks; novel task. This paper is an application/adaptation paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6p8lpe4MNf.md` | 5.50 | **Comparable.** Novel idea (semantic invariant watermark) but mixed experimental quality. This paper has cleaner theory but less novelty. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0KHW6yXdiZ.md` | 5.25 | **Comparable.** End-to-end logits watermarking with moderate experiments. This paper is somewhat cleaner theoretically but similar in overall contribution level. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eKGEsFdpin.md` | 3.67 | **Worse.** Similar method to KGW baseline with weak analysis. This paper has much stronger theoretical backing. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lNLVvdHyAw.md` | 5.00 | **Comparable.** Detecting LLM attacks with perplexity. Both are straightforward applications of existing ideas to LLMs. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gpKEDj9Dgg.md` | 2.00 | **Much worse.** Poorly executed LLM-ASR integration. This paper is far more rigorous. |

The paper is well-written and presents a clean application of existing DP mechanisms to LLM decoding, with a corresponding watermark. However, its core novelty is limited — the decoder is a direct transplant and the watermark is a direct analog. The headline watermark comparison in the real experiments is confounded (equal temperature rather than equal perplexity). The theoretical results are sound but pre-existing. Relative to the calibration anchors, this paper sits below the strong watermark papers (7.0–7.5) and is comparable to mid-range adaptation papers (5.0–5.5), but the unaddressed equal-perplexity confound in the main experimental claim pulls it down.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>