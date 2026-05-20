## Summary

This paper introduces **Set-MI**, a method that improves membership inference (MI) for language models by aggregating per-document MI scores over sets of documents that share the same membership status (e.g., all arXiv papers from the same date). The key insight is that individual loss is a weak signal, but if documents can be grouped into sets where all members are either present in or absent from training data, averaging their scores amplifies the signal. The paper constructs five benchmarks (Wikipedia, Arxiv, Languages, License, Instructions), evaluates four MI methods (Loss Attack, LiRA, Min-K% PROB, zlib entropy), and demonstrates a mean AUROC improvement of 0.14. Extensive ablations examine model size, data deduplication, document length, set size, and robustness to violations of the set assumption.

## Strengths

- **Consistent and large AUROC improvement across methods and domains**: Table 2 shows Set-MI outperforms Individual-MI on 19 out of 20 benchmark–method pairs, with the average gain of 0.14 AUROC. The improvement is substantial in many settings (e.g., Arxiv Min-K% PROB rises from 0.590 to 0.954; Languages LiRA reaches 1.000). This directly supports the paper's central claim.

- **Robustness analysis validates the method under realistic, imperfect conditions**: Section 6 evaluates three aggregation strategies (MAX, MIN, FULL) under controlled simulated noise ratios up to 0.5 in both member and non-member sets. All three strategies maintain AUROC above 0.8 even with substantial noise, well above the Individual-MI baseline (~0.68). This is critical because the set assumption rarely holds perfectly in practice.

- **Diverse, practically motivated benchmarks**: Five benchmarks span real use cases — detecting copyrighted content (License), test-set contamination (Wikipedia, Arxiv), language inclusion decisions (Languages), and instruction-tuning data composition (Instructions). Each benchmark is grounded in explicit inclusion criteria from real training pipelines.

- **Useful ablations that provide actionable guidance**: The study of set size (Figure 4, right) shows that even sets as small as 3 documents yield substantial gains; the study of document length shows diminishing returns beyond 256 tokens; the deduplication analysis (Figure 3, right) confirms that deduplication reduces Set-MI's advantage more than Individual-MI's, aligning with known memorization findings.

## Weaknesses

### Fatal
None.

### Major
None. The method is sound, the experiments are extensive, and the core claims are well-supported.

### Minor
- **No variance or uncertainty estimates for any reported AUROC.** The paper uses random 1,024-token segments to represent documents and subsamples sets — both sources of randomness that could affect results. Without standard deviations, confidence intervals, or multiple trials, the reader cannot assess the stability of the reported gains. Since the headline improvement (0.14 average) is large and consistent across 19/20 settings, this does not invalidate the conclusions, but it is a notable gap in evidential rigor that would be straightforward to address.

- **The zlib + Instructions result (0.458 → 0.429) is unexplained.** This is the only case among 20 where Set-MI *decreases* performance. The paper reports it transparently in Table 2 but does not offer any explanation. While the decrease is small (0.029) and one cell out of twenty does not threaten the overall conclusion, the omission weakens internal coherence — understanding why aggregation occasionally hurts would deepen the analysis.

- **The 13-gram overlap proxy for "clean" Wikipedia membership is not discussed as a limitation.** The robustness experiment (Section 6) constructs ground-truth labels based on 13-gram overlap with the Pile. This is a reasonable proxy but can produce false positives/negatives. The paper does not acknowledge this caveat, though the controlled simulation design partially mitigates it.

### Trivial
- The paper notes that Set-MI performance plateaus beyond 256 tokens per document (Figure 4, left) but does not discuss why or what practical implication this carries for practitioners.

## Nice-to-Haves
- Error bars or bootstrapped confidence intervals for Table 2 would transform the evidence from plausible to strongly convincing.
- A brief discussion of the zlib+Instructions case (e.g., poor Individual-MI baselines can cause Set-MI to amplify noise) would improve completeness.

## Removed Points

- **"Overconfident tone about set assumption"** — The paper explicitly discusses violations (Section 3: "practical factors... might cause the set assumption to not hold") and dedicates Section 6 entirely to robustness. This criticism is not supported by the paper text.
- **"Instructions benchmark is too easy"** — The paper reports the data transparently (Min-K% PROB at 1.0); this is an observation about the benchmark, not a flaw in the paper's analysis or claims.
- **"Reference model choice for LiRA not specified"** — Details were deferred to the appendix, which was stripped by the parsing pipeline. Not an author error.
- **"Correlation analysis feels tacked on"** — Pure presentation/style nitpick without substantive content.
- **"No discussion of when set assumption fails"** — The paper discusses this in Section 3 and provides a full robustness analysis in Section 6. The criticism does not hold.

## Novel Insights

The human reviews converge on the same evaluation structure as my own: the method is simple and clearly effective, the experiments are broad, and the robustness analysis is a strong addition. The one consistent gap is the lack of uncertainty quantification — no reviewer flagged any fatal flaw or fundamental methodological error. The harsh critic's more speculative points (reference model availability, correlation presentation quality) were filtered out as not grounded in the paper's substance.

## Suggestions

1. **Add uncertainty estimates.** Report AUROC as the mean over (e.g.) 5 random token-segment draws with standard deviations or bootstrapped 95% CIs for Table 2. This one change would significantly strengthen the paper's evidential quality.
2. **Briefly explain the zlib+Instructions decrease.** Even one sentence noting that zlib entropy performs near-random on Instructions (0.458) and that averaging amplifies noisy signals would be sufficient.
3. **Acknowledge the 13-gram overlap limitation** and note that the controlled simulation design (where noise is injected knowingly) still provides valid insight into robustness.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Low band (<3.5): *On the Entropy of Language Models in Getting Semantic from Tokens* (3.0), *Language Models for Textual Data Valuation* (2.0), *CopyLens* (2.33), *Beyond Accuracy* (3.0) — all clearly weaker than Set-MI.
- Middle band (3.5–7.5): *User Inference Attacks on Large Language Models* (5.5, Reject), *Blind Baselines Beat Membership Inference Attacks* (4.5, Reject), *Evaluating Privacy Risks of PEFT* (5.8, Reject), *FLAT-Chat* (4.25, Reject).
- High band (>7.5): *Cheating Automatic LLM Benchmarks* (7.75, Oral), *How much of my dataset did you use?* (7.6, Oral), *Cybench* (8.67, Oral), *Privacy-Preserving ICL* (8.0, Poster).

**Round 2 (Narrowing within 5.5–7.5):**
- *Time Travel in LLMs: Tracing Data Contamination* (7.0, Spotlight, avg 7.0) — closely related topic (data contamination detection with instance→aggregation structure). Set-MI has more systematic evaluation (5 benchmarks, 4 methods, extensive ablations) but lacks the human validation and per-instance statistical testing that Time Travel includes. **Comparable; Set-MI is slightly better methodologically but slightly weaker on uncertainty quantification.**
- *Beyond Memorization: Violating Privacy via Inference* (7.2, Spotlight, avg 7.2) — different topic (personal attribute inference), very well received. Set-MI is less novel in its threat model but has cleaner experimental design. **Set-MI is slightly below this anchor in overall impact.**
- *Evaluating Privacy Risks of PEFT* (5.8, Reject, avg 5.8) — similar privacy evaluation scope but with limited benchmarks and weaker evaluation. **Set-MI is clearly stronger.**
- *Scalable Extraction of Training Data from Aligned, Production LMs* (6.67, Poster, avg 6.67) — strong empirical work on data extraction. The two papers have different scopes but similar rigor. **Comparable.**

**Initial bracket:** The paper sits between 5.5 and 7.5 — clearly above the 4–5 range (rejected papers with major flaws) and clearly below the 7.5+ range (Oral-level papers with breakthrough findings or exceptional rigor).

**Final score determination:** The paper is stronger than User Inference (5.5) and PEFT (5.8), comparable to Scalable Extraction (6.67) and Time Travel (7.0), but slightly below Time Travel due to the lack of uncertainty quantification. The core contribution is solid and well-supported, the weaknesses are minor and addressable. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>