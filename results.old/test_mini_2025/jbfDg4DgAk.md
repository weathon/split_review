Now I have good calibration. Let me finalize my review.

**Round 1 bracket**: Based on anchor inspection, I initially bracketed this paper between 4.5 and 6.5 — clearly stronger than the weak watermarking paper (eKGEsFdpin at 3.67) but potentially weaker than the accepted watermarking papers (JYu5Flqm9D at 5.75, 9k0krNzvlV at 5.75) due to missing experimental details.

**Round 2 narrowing**: After reading KRMSH1GxUK (5.80, Accept), RKQcJ1lXNT (5.50, Reject), and comparing to SpARK, I place SpARK at 5.5. It is roughly comparable to these anchors but on the lower side: its core idea is genuinely novel, but the missing specification of the semantic similarity metric and POS tagger weakens the evaluation's interpretability more than the comparable weaknesses in the 5.75 anchors. It is clearly stronger than eKGEsFdpin (3.67) and somewhat weaker than the 5.75+ Accept papers.

Now let me write the final review.

---

Let me double-check a few things before writing the final review. Let me verify that the paper really doesn't define the semantic similarity metric.

I already grepped for "semantic" and "similarity" and found no definition. The table captions just say "the semantic similarity of watermarked and non-watermarked text (Sem.)" — no model or metric specified. Confirmed.

Let me also verify the POS tagger claim. The paper mentions "Universal Part-of-Speech (POS) tags (Petrov et al., 2012)" but doesn't specify implementation. Confirmed.

Let me verify the robustness overclaim. The paper says in the conclusion: "maintains competitive robustness against both substitution and paraphrasing attacks." Let me check Table 3 again for substitution at 50% on Llama2-7b...

Table 3:
- SelfHash: 92.3 (best)
- Unigram: 91.4
- LeftHash: 83.9
- SpARK-Noun: 78.3
- SpARK-Verb: 72.4
- SpARK-Determiner: 67.6

For SpARK-Determiner vs SelfHash: 67.6 vs 92.3 = 24.7 point gap. "Competitive" is not accurate.

But for DIPPER 40L on Llama2-7b:
- SelfHash: 75.0
- SpARK-Determiner: 74.3
That IS competitive.

So the paper overstates substitution attack robustness but is accurate about DIPPER. The conclusion's blanket claim of "competitive robustness against both substitution and paraphrasing attacks" is too strong.

OK, I'm ready to write the review.## Summary

This paper introduces SpARK, a sparse LLM watermarking method that embeds watermarks only at tokens following words with specific Part-of-Speech (POS) tags (e.g., verb, noun, determiner), and detects watermarks by checking only those positions. The core idea is that watermarking fewer tokens reduces quality degradation while maintaining detectability by concentrating the statistical test on the watermarked subset. Experiments on Llama2-7b and Phi-3 across four datasets show that SpARK variants achieve substantially higher ROUGE-L scores and semantic similarity than comparable baselines (Hard, LeftHash, SelfHash, Unigram) while maintaining ≥99.5% TPR.

## Strengths

1. **The sparse watermarking approach anchored to POS tags is genuinely novel and well-motivated.** The paper identifies a real limitation of existing watermarking methods — that watermarking every token degrades quality — and proposes a clean solution: watermark only tokens after words with specific POS tags, then detect using only those positions. The design choice (anchoring to POS rather than random positions) is clever because it makes the watermark positions resilient to insertions/deletions and recoverable without a separate index.

2. **SpARK's quality advantage is clearly demonstrated on properly-defined metrics.** On Llama2-7b (Table 1), SpARK-Verb drops ROUGE-L by only 12.60% on Long-form QA, versus 22.37–47.06% for baselines, all at ≥99.5% TPR. On Phi-3 (Table 2) the gap is even larger: SpARK-Verb drops only 5.17% versus 13.75–65.77% for baselines. The perplexity results (Figure 3) further confirm that SpARK produces lower and more consistent perplexity. These metrics are standard and well-defined.

3. **The qualitative example (Table 4) provides compelling concrete evidence.** SpARK-Determiner produces semantically coherent text (Sem. 0.726) while SelfHash under the same prompt yields nearly incoherent text (Sem. 0.298), yet both achieve strong z-scores. This directly illustrates the paper's thesis that sparsity preserves quality without sacrificing detectability.

4. **The method is validated across two model families (Llama2-7b, Phi-3) and four datasets spanning two tasks (Long-form QA and Summarization).** The quality improvement is consistent across all settings, not cherry-picked.

5. **SpARK achieves genuinely competitive DIPPER robustness.** On Llama2-7b DIPPER 40L, SpARK-Determiner achieves 74.3% TPR versus SelfHash at 75.0% — within 0.7 percentage points — while using far fewer watermarked tokens and producing much higher-quality text.

## Weaknesses

### Fatal

None.

### Major

1. **The semantic similarity metric ("Sem.") is never defined.** The paper's quality evaluation relies heavily on the "Sem." column in Tables 1 and 2, and the qualitative example in Table 4 uses it as a key comparison. However, there is no description of which embedding model (e.g., BERT, SBERT), which similarity function (cosine? dot product?), or what reference text (the non-watermarked generation? the prompt?) is used. Without this definition, the semantic similarity numbers are not interpretable, and a central thread of the paper's evaluation is opaque. This is the most serious weakness because the paper explicitly highlights semantic similarity as evidence of quality preservation.

2. **The POS tagger implementation is not specified.** The method's behavior during both encoding (Algorithm 2 line 4) and detection (Algorithm 3 line 3) depends entirely on a POS tagger that is referenced only as "Universal Part-of-Speech (POS) tags (Petrov et al., 2012)." No specific implementation, model, training data, or library is named. Since POS tagger accuracy varies significantly across implementations (especially on LLM-generated text, which may have unusual syntactic patterns), this is a reproducibility failure: the core mechanism cannot be independently implemented or evaluated.

3. **Robustness claims are overstated for substitution attacks.** The paper describes SpARK's robustness as "competitive" against both substitution and paraphrasing attacks (conclusion). However, on Llama2-7b at 50% substitution (Table 3), SelfHash achieves 92.3% TPR while SpARK-Noun (the best SpARK variant) achieves 78.3% — a 14-point gap. SpARK-Determiner is at 67.6%, a 24.7-point gap. This is not competitive. The DIPPER results are genuinely competitive (74.3 vs 75.0), but the conclusion's blanket claim is misleading. The paper should honestly frame its contribution as: *SpARK trades substantial robustness against substitution attacks for much better text quality, while maintaining competitive robustness against paraphrasing.*

### Minor

4. **The zero-distortion watermarking methods (Christ et al., 2023; Kuditipudi et al., 2023) are discussed in related work but not included as baselines.** The paper's stated goal is to mitigate the quality-detectability tradeoff; these methods claim to avoid it entirely. The paper notes they struggle at low temperature (Piet et al., 2023) but does not specify the temperature used in its own experiments, making it impossible to assess whether this argument applies. Including them (or explaining more precisely why they are excluded) would strengthen the evaluation.

5. **The distribution of T (number of watermarked tokens) is not reported.** The z-test in Equation (1) uses only the watermarked positions. For datasets or text types where the target POS tag occurs infrequently, T could be very small, reducing statistical power. The paper does not report the average or minimum T across datasets, nor does it analyze the minimum text length needed for reliable detection. This limits practical guidance for deployment.

6. **Experimental results lack variance or significance estimates.** Tables 1–3 report single numbers without standard deviations, confidence intervals, or significance tests. Given that LLM generation is stochastic, this makes it difficult to assess whether observed differences are reliable.

7. **No analysis of false positives on human-written text.** The TNR is measured against unwatermarked LLM-generated text. Since the anchor is linguistic (POS) rather than random, human-written text might by chance have different statistical properties at positions following the target POS tags. This should be checked.

8. **The paper does not ablate sparsity rate directly.** Different POS tags yield different sparsity levels, but the paper does not systematically analyze the relationship between sparsity (fraction of tokens watermarked) and the quality-detectability tradeoff. Such an analysis would strengthen the central thesis.

### Trivial

None.

## Nice-to-Haves

- Report the distribution of T (watermarked token count) for each POS tag and dataset, including minimum values.
- Compare against zero-distortion baselines or explain more concretely the temperature settings that preclude their use.
- Analyze POS tagger accuracy on generated texts and its impact on false positive/negative rates.
- Include sparsity ablation (vary POS tag sets to produce different sparsity levels and measure quality vs. TPR).

## Removed Points

- "Cannot be weakened via soft bias" — This is a deliberate design choice of the method, not a weakness. The paper explains that hard restriction is used because sparse watermarking needs to utilize all available watermarked tokens.
- Figure 3 legend garbling — Parser artifact; the original submission does not have this issue.
- Missing appendix details — Parser strips appendix sections from all papers; these exist in the original submission.
- Missing related works — Per policy, cannot confirm whether a missing citation exists.
- Formatting/style nitpicks — Parser artifact, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Define the semantic similarity metric explicitly.** State which embedding model (e.g., all-MiniLM-L6-v2, text-embedding-3-small), which similarity function (cosine), and what the reference text is (the non-watermarked LLM output for the same prompt).
2. **Name the POS tagger implementation** (e.g., spaCy en_core_web_trf, NLTK's averaged perceptron tagger, Stanford POS tagger). Report its accuracy on a sample of the generated texts.
3. **Temper the robustness claims.** Replace "competitive" in the conclusion with a nuanced description: "SpARK achieves competitive robustness against paraphrasing attacks, but trails leading methods against high-rate substitution attacks — a tradeoff inherent to watermarking only a sparse subset of tokens."
4. **Report T statistics** (mean, min, 5th percentile) for each dataset and POS tag to help practitioners assess whether SpARK is appropriate for their text lengths.
5. **Add confidence intervals** to Tables 1–3, or at minimum report the number of independent runs.

## Score and Decision

**Calibration anchors** (all rounds):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| eKGEsFdpin | 3.67 | R1 | Sampling-based watermarking, Reject. SpARK is significantly stronger (more novel idea, better evaluation). |
| JYu5Flqm9D | 5.75 | R1/R2 | Codable watermarking, Accept poster. Comparable quality; both have fixable experimental gaps. |
| 9k0krNzvlV | 5.75 | R1/R2 | Learnability of watermarks, Accept poster. Comparable; SpARK has more novel core idea but less thorough evaluation. |
| KRMSH1GxUK | 5.80 | R2 | IP infringement detection, Accept poster. Comparable empirical quality. |
| RKQcJ1lXNT | 5.50 | R2 | Adaptive watermark attacks, Reject. SpARK has a stronger positive contribution. |
| KOTsHW6mBI | 5.20 | R2 | Multi-bit watermark, Withdrawn/Reject. SpARK is stronger. |
| 1ou5noWgHM | 5.40 | R1 | Source attribution, Reject. SpARK has more direct applicability. |

**Round 1 bracket:** 4.5 – 6.5 (clearly above the weak watermarking paper at 3.67, plausibly near the accepted watermarking papers at 5.75).

**Round 2 narrowing:** After reading KRMSH1GxUK (5.80) and RKQcJ1lXNT (5.50) in full alongside JYu5Flqm9D (5.75) and 9k0krNzvlV (5.75), I place SpARK at 5.5. The core idea is novel and well-supported, but the undefined semantic similarity metric and unspecified POS tagger are more consequential for interpretability than the comparable weaknesses in the 5.75 anchors. The paper is close to the acceptance margin — the missing details are fixable.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>