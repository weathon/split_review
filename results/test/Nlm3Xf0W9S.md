Now I have all the information needed. Let me compose the consolidated final review.

## Summary

This paper proposes **PatternWatermark**, the first watermarking framework specifically designed for order-agnostic LMs (models that generate tokens non-sequentially, e.g., ProteinMPNN and CMLM). The method uses a Markov chain to generate key sequences with high-frequency alternating patterns. During generation, keys bias the token sampling toward specific vocabulary partitions; during detection, keys are recovered from the final token order and patterns are counted. Statistical significance is assessed via a dynamic programming algorithm that computes the exact pattern-count distribution under the null. Experiments on protein generation and machine translation show strong detection accuracy (e.g., 96.12% TPR@0.1% FPR for ProteinMPNN) with competitive generation quality.

## Strengths

- **First dedicated watermarking framework for order-agnostic LMs.** The paper correctly identifies that existing watermarks (Soft, Unigram, Multikey) rely on sequential context unavailable in order-agnostic settings, and proposes the first method to address this gap. The discussion in Section 3.1 explaining why prior schemes fail is clear and well-motivated.

- **Consistent empirical superiority over adapted baselines.** Across both domains (protein generation and machine translation), PatternWatermark outperforms all baselines at matched or superior generation quality. For example, at δ=1.25 (ProteinMPNN), it achieves 96.12% TPR@0.1% FPR with pLDDT 84.50 vs. Unigram's 85.14% TPR at pLDDT 83.58. The robustness experiments (Tables 3–4) show the method also withstands token modification and paraphrasing attacks better than baselines.

- **Principled statistical detection via dynamic programming.** Algorithm 3 computes the exact pattern-occurrence probability under i.i.d. uniform keys, enabling controlled theoretical false positive rates. The optimization reducing complexity from O(n²2^m) to O(n² m) for alternating patterns is a useful technical contribution.

- **Evaluation across two diverse domains with ablation studies.** The paper tests on both ProteinMPNN (protein design) and CMLM (machine translation), using domain-specific quality metrics (pLDDT, BLEU) and ablating pattern length m and transition matrix configuration. This breadth strengthens claims of generality.

## Weaknesses

### Major

1. **Undefined mapping from generation-order key sequence to final-order key sequence.** This is the paper's most critical gap. Algorithm 1 assigns keys to *generation steps* (key k[i] is used when generating the token at position o_i, where o is the generation order). Algorithm 2 recovers keys from the *final token order* (position by position). The recovered key sequence is therefore a permutation of the Markov chain output, governed by the inverse of the generation order o.

   The paper never explains under what conditions the Markov-chain pattern survives this permutation, nor does it specify what generation order o is used in the experiments. For the chosen transition matrix A=[[0,1],[1,0]] (perfect alternation), a random permutation of the alternating key sequence yields an expected pattern count essentially identical to the null hypothesis (i.i.d. uniform keys), making detection impossible in principle. Yet the experiments show strong detection — implying either that the generation order used is *not* random (contradicting the "order-agnostic" framing for ProteinMPNN, whose standard behavior is random-order decoding), or that there is an unstated mechanism. Without resolving this, the central claim of the paper — that the watermark is detectable in order-agnostic LMs — rests on an unverified premise.

   This is a major weakness because it affects the core contribution, but it is not necessarily fatal: the experimental results are strong and consistent, so a clarification (e.g., stating that a fixed left-to-right generation order was used, or explaining how CMLM's iterative refinement preserves the pattern) would likely resolve the issue.

### Minor

2. **Baseline adaptations are not described.** The paper states that Soft and Multikey watermarks were "adapted from existing approaches" but gives no details. The paper itself argues in Section 3.1 that Soft watermark cannot be applied to order-agnostic LMs because "some of the previous i tokens may not yet be generated." If the adaptation simply ignores unavailable context (e.g., falls back to a unigram hash), the comparison may evaluate a weakened form of the baseline. Without a description, the fairness of the comparison cannot be assessed. (Unigram is the exception — its adaptation is clear because it uses a fixed red–green list per token.)

3. **No empirical false positive rate validation.** The detector's null hypothesis assumes that the recovered key sequence under non-watermarked text is i.i.d. uniform. However, the key recovery is based on which vocabulary partition a token falls into; if the LM's token distribution is non-uniform across partitions without the watermark, the actual key distribution deviates from uniform and the theoretical FPR may not hold. The paper reports only TPR at theoretical FPR levels without validating that the empirical FPR matches. While this issue also affects the baselines, it weakens confidence in the reported TPR numbers.

4. **Underspecified experimental details.** Several implementation choices that affect reproducibility are not reported: (a) how the vocabulary is partitioned into l parts (random split? frequency-based?); (b) what generation order o is used for the experiments; (c) how CMLM's parallel/iterative refinement token generation is reconciled with the sequential key assignment in Algorithm 1. For CMLM, multiple tokens may be generated simultaneously in a single refinement iteration — it is unclear how a single key per generation step maps to this process.

### Trivial

- The explanation for why detection declines at large pattern lengths m (Figure 6) attributes the drop to "higher sensitivity to errors" but provides no analysis or simulation to support this.
- The effect of key recovery errors (not all tokens are promoted into the intended partition) on the DP-based p-value computation is not discussed.
- The claim that "distortion-free watermarking schemes cannot be adapted to order-agnostic LMs" (Section 3.1) is reasonable in essence but conflates the key generation mechanism with the distortion-free guarantee; it would be more precise to say existing distortion-free schemes require autoregressive decoding.

## Nice-to-Haves

- An empirical calibration plot showing actual vs. theoretical FPR on non-watermarked text would strengthen the detection claims.
- A simple simulation or theoretical argument showing how pattern frequencies behave under the specific generation orders used in the experiments (even if not perfectly random) would resolve the main ambiguity.
- A description of the vocabulary partitioning strategy and its impact on the null distribution would improve reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper fails to resolve how the Markov-chain pattern property transfers..."* — Retained as Major Weakness #1. This is a real issue, not a misunderstanding.
- *"The null hypothesis fails because the LM's token distribution is not uniform..."* — Retained as Minor Weakness #3, but downgraded from "critical" because (a) the concern is valid but (b) it affects baselines equally and many watermark papers operate with theoretical FPR.
- *"The adaptation of baseline methods is not described"* — Retained as Minor Weakness #2.
- *"Missing related works"* — Removed per instructions (cannot confirm existence of missing citations).
- *"Distortion-free claim is stated too strongly"* — Retained but moved to Trivial.
- *"Algorithm 3 optimization is useful"* — Not a weakness; acknowledged in Strengths.
- *"The paper should also cover Y / domain Z"* — No such demands in the review; not applicable.
- *Formatting/style nitpicks* — None identified in the harsh review.
- *Reproducibility nitpicks about undisclosed hyperparameters* — The reviewer asked for implementation details; these are retained as Minor Weakness #4 (underspecified details).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely new observation about the method that the paper itself does not discuss.

## Suggestions

1. **Clarify the generation-order / final-order mapping.** This is the single most important revision. State explicitly what generation order o was used in each experiment. If a fixed order (e.g., left-to-right) was used, say so and qualify the "order-agnostic" framing accordingly. If random generation order was used, explain how detectability is achieved (e.g., by showing that the specific patterns used are invariant under permutation, or by describing a different key-assignment mechanism).

2. **Describe the baseline adaptations.** Provide a few sentences explaining how Soft and Multikey watermarks were adapted to work without sequential context. This is essential for the reader to evaluate the fairness of comparison.

3. **Add empirical FPR calibration.** Report the empirical false positive rate on non-watermarked text for at least one representative setting to validate that the theoretical FPR matches practice.

4. **Report vocabulary partitioning strategy.** Describe how the vocabulary is split into l parts (random, frequency-balanced, or based on some other criterion).

## Score and Decision

**Originality:** High — first work to address watermarking for order-agnostic LMs.  
**Importance of research question:** High — order-agnostic LMs are increasingly used in protein design, machine translation, and other domains.  
**Claims support:** Partially — strong experimental results, but the core mapping ambiguity undermines confidence until resolved.  
**Soundness of experiments:** Adequate — results are consistent and well-reported, but missing details (generation order, baseline adaptations, empirical FPR) limit assessment.  
**Clarity of writing:** Mostly clear — algorithms are presented precisely, but the generation-order issue is a confusing omission in an otherwise well-structured paper.  
**Value to community:** Potentially high — if the mapping issue is resolved, this would be a useful tool for watermarking non-autoregressive models.

The paper has a genuine contribution and strong experimental evidence, but the unresolved ambiguity about the generation-order / final-order key mapping is a significant gap that needs to be clarified. The contribution is not fatally flawed — the experimental results are too consistent to dismiss — but the paper cannot be accepted in its current form without addressing this issue.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>