Now I have a clear picture of all the evidence. Let me write the final consolidated review.

## Summary

This paper proposes PATTERN-MARK, a watermarking framework for order-agnostic language models (LMs) — models that generate tokens in a non-sequential order (e.g., ProteinMPNN, CMLM). The approach uses a Markov chain to generate a key sequence whose alternating patterns (e.g., k₁ k₂ k₁…) are embedded by promoting different vocabulary partitions at each generation step. Detection recovers the key sequence from the final text by checking which vocabulary partition each token falls into, then counts how many of the high-frequency patterns occur, computing a p-value via a dynamic programming algorithm.

## Strengths

1. **Well-motivated problem.** The paper correctly identifies that existing watermarking methods for sequential LMs (which rely on preceding n-gram context) cannot be directly applied to order-agnostic LMs. To the best of my knowledge, this is the first work attempting to watermark order-agnostic LMs, which have important applications in protein design, machine translation, speech generation, and time-series forecasting.

2. **Technically sound sub-components in isolation.** The Markov-chain-based key generation (Algorithm 1 lines 2–4) and the exact dynamic programming computation of pattern-occurrence probabilities under the null hypothesis (Algorithm 3) are clearly described and technically correct as standalone methods.

3. **Clear exposition of why prior methods fail.** Section 3.1 provides a well-reasoned discussion of why existing watermarking schemes (Soft watermark, Multikey, distortion-free schemes) cannot be adapted to order-agnostic LMs, identifying the missing-context problem and the non-autoregressive joint-distribution problem.

## Weaknesses

### Fatal

1. **The detection mechanism does not account for the mismatch between generation order and final sequence order, invalidating the core claim.**

   This is the paper's central and most serious problem. I verified this directly from the algorithms in the paper:

   **Algorithm 1 (Generator):** Takes "generation order *o*" as input. The Markov chain produces keys *k*[1], *k*[2], …, *k*[*n*] in **generation-step order** (lines 2–4). Then each key *k*[*i*] is used to generate the token placed at final position *oᵢ* (lines 5–8). So the sequence of keys is embedded in *generation order*, not final position order.

   **Algorithm 2 (Detector):** Scans the final output sequence *x₁, …, xₙ* in **final position order** (line 4: "for i = 1, …, n") and recovers a key from each token based on which vocabulary partition *V_c* it belongs to (line 5).

   The recovered key sequence is *[k[o⁻¹(1)], k[o⁻¹(2)], …, k[o⁻¹(n)]]* — a permutation of the original key sequence *[k[1], …, k[n]]* under the inverse of the generation order. The Markov chain's alternating patterns (which are the entire basis of the statistical test) depend on adjacency in the **generation order**. Under any non-trivial permutation, these adjacencies are destroyed, and the pattern counts in the recovered sequence no longer follow the distribution computed by Algorithm 3.

   The paper itself acknowledges that "the detector does not know the order in which the tokens were generated" (Section 3.1). Yet the detection method implicitly assumes the generation order *is* the final order. No analysis, adjustment, or discussion of this permutation problem is provided. The method therefore does **not** solve the claimed problem — it only works when the generation order coincides with the final order (i.e., the sequential setting that the paper explicitly sets out to move beyond).

   This is not a missing ablation or a minor oversight. It is a structural flaw that means the proposed watermarking scheme, as described, cannot function as claimed for order-agnostic LMs with arbitrary generation orders.

### Major

2. **Experimental evaluation does not specify or control for generation order, making the results uninterpretable.**

   The paper reports strong detection results on ProteinMPNN and CMLM (e.g., 100% TPR at 1% FPR for protein generation). However, it does not state what generation order was used during watermarking, nor how the final sequence order relates to the generation order. For ProteinMPNN, the paper notes (Section 2, line 59–60) that "the decoding order is randomly sampled from the set of all possible permutations" — a setting where the detection method described in Algorithm 2 should fail entirely due to the flaw above. If the experiments instead used a fixed sequential order (left-to-right), they do not represent the order-agnostic setting. Without this information, the reported numbers cannot be interpreted as evidence that the method works for order-agnostic LMs.

### Minor

3. **Baseline adaptation details are insufficiently described.**

   The paper compares against Soft watermark, Multikey, and Unigram baselines "adapted from existing approaches" (Section 4.1), but provides no description of how these adaptations were made. For methods that rely on n-gram context (Soft, Multikey), the adaptation to order-agnostic generation is nontrivial and should be documented. Without this, it is unclear whether the reported baseline performance reflects inherent weakness of those methods or poor adaptation choices.

4. **The paper claims to handle CMLM, but CMLM generates tokens simultaneously in iterations, not one-at-a-time in any order.**

   CMLM (Mask-Predict) generates tokens in parallel during each refinement iteration; the notion of a sequential "generation order" (which Algorithm 1 requires as input *o*) does not naturally apply. The paper does not explain how the algorithm is adapted to this setting.

### Trivial

None beyond the standard formatting artifacts introduced by PDF extraction.

## Nice-to-Haves

- The paper would benefit from explicitly modeling the permutation between generation and final order and adjusting the null distribution accordingly, or from designing permutation-invariant detection (e.g., based on key multisets rather than adjacency patterns).
- An ablation showing what happens when the generation order is deliberately set to be very different from the final order would help clarify the scope of the method.

## Removed Points

- **Harsh critic's point 3 (baseline comparisons likely unfair):** While the adaptation details are insufficient (I kept this as a minor weakness), the harsh critic's stronger claim that the comparisons are "uninformative" and the soft watermark result "suggests the adaptation may have used a fixed or heuristic context" is speculative. The paper provides the numbers; the issue is insufficient description, not evidence of unfairness.
- **Strength Finder's points about superior detection efficiency, quality-detectability trade-off, and robustness (strengths 2–4):** These are contingent on the method working as claimed for order-agnostic LMs. Since the detection method has a verifiable structural flaw, these claimed empirical strengths cannot be relied upon as evidence. However, the attributed numbers are as reported; the issue is that they may reflect a different setting (sequential generation) than claimed.
- **Strength Finder's "first framework for order-agnostic LM watermarking":** This is factually true in terms of stated intent, but since the framework does not actually solve the claimed problem, it does not constitute a substantive strength.
- **Harsh critic's "Strengthening the Paper on Its Own Terms" section:** Contains good suggestions but these are speculative future directions, not weaknesses of the current submission.

## Novel Insights

The key insight that emerges from analyzing the reviews is that the paper's core algorithmic structure contains a subtle but devastating mismatch: the Markov chain patterns are generated over *generation steps* but detected over *final positions*, and in order-agnostic LMs these two orderings are related by an unknown permutation that the detection does not account for. This is qualitatively different from the missing-context problem that the paper correctly identifies for prior methods. The paper addresses one challenge of order-agnostic LMs (unavailable n-gram context) but overlooks another that is equally central (the permutation between generation and detection orderings).

## Suggestions

1. **Redesign the detection to be permutation-invariant.** The detection should not rely on adjacency patterns in the final-order key sequence, since these do not correspond to adjacency in the generation order. One viable direction: design watermarks based on *multisets* of keys (e.g., the proportion of k₁ vs. k₂ in the sequence) rather than adjacency patterns.

2. **Alternatively, formally characterize the relationship between generation-order and final-order key sequences.** If the null distribution of pattern counts after an unknown permutation can be derived, the detection could be calibrated accordingly. However, this requires knowing the distribution of the generation order, which the detector generally does not have.

3. **In any revision, report the generation order used in experiments explicitly.** State whether the generation order was left-to-right (sequential), random, or confidence-based, and show detection performance separately for each case.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Sampling-Based Watermark | eKGEsFdpin.md | 3.67 | 1, 2 | Proposed watermark for sequential LMs; incremental over Kirchenbauer. Current paper has a *more fundamental* structural flaw. |
| Word Importance | vfEqSWpMfj.md | 2.50 | 1 | Unrelated topic, low score due to weak claims. |
| CopyLens | Mez2No9lHj.md | 2.33 | 1 | Unrelated topic. |
| Outlier Paragraph Detection | B37UmlxsaP.md | 2.50 | 1 | Unrelated topic. |
| Entropy-Semantic Metric | z3DMFpaP6m.md | 3.00 | 1 | Unrelated topic. |
| SEAL Watermark (Theor+Prac) | LdIlnsePNt.md | 6.00 | 2 | Rigorous theory + practical method, but had unfair comparison concerns. Current paper is substantially weaker. |
| Codable Watermarking | JYu5Flqm9D.md | 5.75 | 2 | Accepted poster; solid incremental contribution. Current paper's structural flaw is more severe. |
| Mixed-Source Watermark Detection | dmDEhEHxix.md | 4.00 | 1, 2 | Tackled a well-defined subproblem with sound methodology. Current paper has a more fundamental issue. |
| EditMark | qGLzeD9GCX.md | 4.25 | 2 | Training-free model-editing watermark; limited novelty but no structural flaw. Current paper scores lower. |
| Multi-bit Watermark via Position Allocation | KOTsHW6mBI.md | 5.20 | 2 | Incremental but sound extension. Current paper's structural flaw makes it significantly weaker. |
| Unremovable Watermarks | 0SpkBUPjL3.md | 3.75 | 2 | Open-source model watermarking with theoretical guarantees. Current paper has a more severe flaw. |

**Round-1 bracket:** Between 2.5 and 4.5 (the paper is clearly weaker than the mid-range watermark papers at ~5.75 and has a more fundamental flaw than papers scoring ~4.0).

**Round-2 narrowing:** The paper is most comparable to the weakest watermark anchors (eKGEsFdpin at 3.67, qGLzeD9GCX at 4.25) but has a verifiable structural flaw that those papers do not. The flaw is not speculative — it follows directly from the algorithms as written in the paper. This places the paper below these anchors.

The problem is real and well-motivated, and the sub-components are technically sound in isolation. However, the central detection method has a verifiable flaw that means it does not solve the claimed problem. The experimental results, while seemingly strong, are uninterpretable without knowing the generation order used. The paper should not be accepted in its current form.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>