Now I have enough information to synthesize the final review. Let me write it.

## Summary

This paper proposes **PatternWatermark**, the first watermarking framework designed specifically for order-agnostic LMs (e.g., ProteinMPNN for protein generation, CMLM for machine translation). The approach uses a Markov chain to generate a key sequence, maps tokens to keys via a fixed vocabulary partition, and detects the watermark by counting pattern occurrences against a null distribution computed via dynamic programming. Experiments show very large TPR margins over adapted baselines (Soft watermark, Multikey, Unigram) at comparable or better generation quality.

## Strengths

- **First principled watermark for order-agnostic LMs.** The paper identifies a genuine gap (Section 3's discussion explains convincingly why existing watermarks fail in non-sequential generation) and proposes a method that addresses the unique constraints of this setting — a novel and valuable contribution.

- **Detection efficiency far exceeds all adapted baselines.** On protein generation (Table 1), at δ=1.5 the method achieves 99.87% TPR@0.1% FPR, versus 85.14% for the next-best baseline (Unigram) and near-zero for Soft watermark. On machine translation (Table 2), at δ=5 the method achieves 98.01% TPR@0.1% FPR versus Unigram's 95.41%. These margins are large and consistent.

- **Better quality–detectability trade-off than all baselines.** Figure 2 shows that at matched quality levels, the method's TPR is substantially higher than all baselines — e.g., at pLDDT ≈84.5, TPR ≈96% (δ=1.25) vs. Unigram's ≈85% at lower pLDDT (83.6). This is a concrete and practical advantage.

- **Strong robustness under token-modification and paraphrase attacks.** Under a 30% random-token modification (Table 3), the method (δ=1.5) maintains 65.73% TPR@0.1% FPR vs. Unigram's 54.08% and Soft's 0.00%. Under a 30% ChatGPT paraphrase (Table 4), it achieves 89.53% TPR vs. Unigram's 64.01%.

- **Ablation study empirically guides design choices.** Section 5.4 systematically evaluates pattern length (finding optimal m=4–5) and transition-matrix parameter a₁₁ (showing quality is nearly independent, justifying use of the strongest signal a₁₁=0).

## Weaknesses

### Fatal
None.

### Major

- **Null distribution assumption is unjustified, and empirical FPR validation is absent.** The detection test (Alg. 2–3) assumes that under the null hypothesis (unwatermarked text), the recovered key sequence follows a Markov chain with *uniform* transition probabilities (line 174). This assumption is stated without justification. The recovered key at each position depends on which vocabulary partition the LM's token falls into, and unless the partition is carefully balanced, the key distribution will reflect the LM's token probabilities — not uniform. The paper provides no description of how the vocabulary is partitioned (line 113 mentions partitioning but gives no strategy), so the reader cannot assess whether the uniform assumption is reasonable. Worse, the paper **never reports empirical false positive rates** on unwatermarked text. The "No Watermark" rows in Tables 1–2 show only dashes, yet empirical FPR calibration is a standard requirement in watermarking papers. Without this, the claimed "guaranteed controlled theoretical false positive rate" (line 16) is unsubstantiated. This is the paper's most serious weakness. *Evidence: lines 16, 113, 174, Tables 1–2 "No Watermark" rows.*

- **Baseline adaptations are not described.** The paper states that Soft watermark, Multikey, and Unigram are "adapted from existing approaches" (line 258) because "there are generally no watermarking methods specifically designed for order-agnostic LMs." Yet Section 3 (lines 63–64) explicitly explains why Soft watermark *cannot* be applied to order-agnostic LMs (the context-dependent key is unrecoverable). The adaptation procedure for each baseline is completely unspecified — e.g., what context (if any) was used for Soft and Multikey? Was a dummy context provided, a fixed key, or something else? Without this information, the reader cannot assess whether the baseline comparisons are fair or whether they represent strawman configurations. *Evidence: lines 63–64, 258.*

### Minor

- **Vocabulary partition strategy is not specified.** The method requires partitioning the vocabulary V into l parts V₁,…,Vₗ corresponding to the l keys (line 113). The choice of partition directly affects both the watermark's strength (what tokens get promoted) and the null distribution (what keys are recovered). The paper does not describe how this partition is constructed — randomly, by frequency balancing, by optimization, or otherwise. This limits reproducibility. *Evidence: line 113.*

- **The empirical results, while strong, rest on the unsupported FPR calibration.** The reported TPR numbers (e.g., 99.87% at 0.1% theoretical FPR) are computed as the fraction of watermarked texts whose p-value falls below the threshold. If the p-values are incorrect because the null distribution is misspecified, the TPR values may correspond to a much higher real FPR than claimed. This does not invalidate the comparison's internal consistency (all methods use the same theoretical thresholds), but it means the absolute TPR@FPR numbers should be interpreted with caution until FPR calibration is validated.

### Trivial

- The computational complexity O(n²l^m) is claimed but not derived (line 198). The derivation is straightforward from the algorithm description, so this is a minor clarity issue.

## Nice-to-Haves

- A discussion of how larger key spaces (l > 2) would affect detection power and quality would strengthen the paper, but is not required for its core contribution.
- Analysis of how sequence length affects statistical power is welcome but outside the paper's stated scope.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing appendix algorithm reference (Alg. "alg:practice algorithm" on line 262).** The harsh critic notes this algorithm is referenced but not present in the provided text. Per the review guidelines, appendix content is stripped by the parser and exists in the original submission. REMOVED.
- **"The paper should justify why alternation is optimal or preferred."** The paper does justify this: Section 5.4 (line 338) shows that quality is consistent across a₁₁ values, so a₁₁=0 (alternation) is chosen as the strongest watermark signal without quality loss. The harsh critic's claim is incorrect. REMOVED.
- **"The detection framework as specified cannot guarantee calibrated hypothesis tests… this is not a fixable-with-more-experiments issue."** This characterization as unfixable is too strong. The issue can be addressed by: (a) describing a balanced vocabulary partition strategy that justifies the uniform null, (b) reporting empirical FPR on unwatermarked text, and/or (c) deriving the correct null distribution. The core approach is not fundamentally broken. Downgraded from "fatal" to "Major."
- **Strength Finder's claim about "rigorous statistical control."** This conflicts with the verified weakness about the unjustified null distribution. Per the review guidelines, when a strength and verified weakness disagree, the weakness wins. The strength is replaced above with a more accurate claim about the method's novelty.
- **Requests for analysis of sequence length effects on detection power.** This asks for experiments beyond the paper's stated scope and the paper already provides extensive ablations. REMOVED as scope creep.

## Novel Insights

The harsh critic identifies a genuine statistical gap that escaped the paper's own characterization of its contribution as providing "guaranteed" FPR control. The pattern-based detection approach is creative and the empirical results are dramatic, but the conflation of "theoretical" FPR (computed under an assumed null) with "guaranteed" FPR (which would require the null assumption to be correct) is a meaningful distinction. The paper would benefit from either deriving the correct null from the actual key distribution or providing empirical calibration. Beyond this, the core observation — that patterns in a Markov-chain key sequence can survive order-agnostic generation because the key-to-token mapping is position-invariant — is a genuinely clever contribution.

## Suggestions

1. **Describe the vocabulary partition strategy** in detail. If tokens are assigned randomly or to balance total probability mass across partitions, state this explicitly. If the partition is frequency-balanced (each V_i has roughly equal total probability under the LM), the uniform null assumption becomes more defensible.
2. **Report empirical false positive rates** on unwaterheld text for each theoretical FPR threshold. This is the most direct way to demonstrate calibration and would address the core weakness.
3. **Specify exactly how each baseline was adapted** for the order-agnostic setting — what context was used for Soft and Multikey, and how the red/green lists were constructed for Unigram.
4. If the uniform null assumption cannot be justified, consider replacing the theoretical p-value computation with a permutation or bootstrap-based test that does not require distributional assumptions.

## Score and Decision

The paper addresses a genuine, previously unexplored problem and presents a clever, well-motivated framework with striking empirical results. However, a central statistical claim — guaranteed false positive rate control — is not adequately supported: the null distribution assumption is unjustified, no empirical FPR calibration is provided, and baseline adaptations are underspecified. These are substantial but fixable issues. The contribution is real, but the paper needs revision before it can be accepted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>