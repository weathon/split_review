Now I have all the information I need. Let me write the consolidated final review.

## Summary

The paper investigates why naive output matching underperforms in 1-bit post-training quantization (PTQ) of LLMs and identifies three challenges: (i) layer-wise output alignment does not guarantee block-level loss reduction, (ii) quantization errors accumulate across layers, and (iii) output alignment can distort attention/token-similarity structure. The authors propose a selective output-alignment strategy that applies the **Output Error** objective (matching against the true full-precision input rather than the quantized-layer input) only to the last fully connected layer of each transformer block, and introduce **Attention Matrix Preservation (AMP)** — a masking mechanism that prevents degradation of token-similarity structure during quantization. Experiments across OPT (1.3B–30B), LLaMA-2 (7B, 13B), and LLaMA-3 (8B) show consistent perplexity and accuracy improvements over ARB-RC, ARB-X, BiLLM, and PB-LLM, with ablation studies verifying the contribution of each component.

## Strengths

1. **Well-motivated problem diagnosis.** Section 3 provides concrete evidence for why naive output alignment (ARB-X) fails: Figure 1 shows that layer-wise ARB-X sometimes increases block-level loss relative to weight-only ARB; Figure 2 quantifies how the Activation-conditioned Error diverges from the true Output Error as depth increases; and the token-similarity analysis in Section 3.3 directly connects output-matching distortion to attention degradation. These empirical diagnostics are informative contributions in their own right.

2. **Consistent gains across model families and sizes.** Tables 1 and 2 show that the method outperforms all prior 1-bit PTQ methods on every OPT model size (1.3B–30B) and on every LLaMA model for perplexity on C4, WikiText-2, and average zero-shot QA accuracy. The improvements on OPT-1.3B (C4 perplexity 24.69 vs. ARB-RC's 27.70) and OPT-2.7B (19.90 vs. 21.46) are practically meaningful. The one acknowledged exception (PTB + LLaMA-2-7B) is discussed below.

3. **Clean ablation studies validate the two core design choices.** Table 4 confirms that replacing Activation-conditioned Error with Output Error yields a consistent 0.7–0.9 perplexity improvement. Table 3 shows that removing AMP degrades LLaMA-2-7B by over 9 perplexity points on C4, confirming that AMP is essential — particularly for architectures like LLaMA that use RMSNorm and are more sensitive to directional distortions.

4. **Closed-form derivations for quantized parameters.** Equations (5)–(8) provide analytical solutions for the scale factors and binary matrix, making the optimization efficient (solving via `torch.linalg.lstsq` rather than iterative backpropagation). The closed-form row-wise binarization in Eq. (6) follows principles from prior binarization literature but is cleanly extended to the 1-bit LLM PTQ setting.

## Weaknesses

### Major

1. **LLaMA-2-7B on PTB (perplexity 3166) contradicts the strongest performance claims.** The proposed method yields 3166 perplexity on PTB for LLaMA-2-7B, whereas ARB-RC (763.19) and ARB-X (681.24) perform substantially better. The paper acknowledges this exception and argues that "the large perplexity indicates that the metric cannot provide a meaningful evaluation." While it is true that all methods perform poorly on this benchmark (BiLLM scores 5243), the comparison between 3166 and ~680 is a meaningful qualitative difference — it shows the method can regress significantly relative to baselines in this setting. Combined with the abstract's claim that the method "consistently outperforms existing 1-bit PTQ methods," this creates a tension the authors should resolve. A concrete analysis of *why* the method fails on this particular combination (outlier calibration samples? numerical instability in the least-squares solve? a specific architectural sensitivity?) is needed.

2. **The selective "last layer per block" design choice is not empirically justified.** The paper restricts output alignment to "only the last fully connected layer of each block, since it has the most direct impact on the block loss" (Section 4.2), but provides no ablation or evidence supporting this claim. A systematic comparison — e.g., applying output alignment to (a) the attention output projection, (b) the first FFN layer, (c) the last FFN layer, (d) all layers — is missing. The generality of this choice across architectures (OPT vs. LLaMA, whose blocks differ) is also unclear.

### Minor

3. **Mathematical sloppiness in the AMP objective (Eq. 9).** The equation states:
   `max || (X̂ŴŴ^TX̂^T) ⊙ (XWW^TX^T) || = Tr[X̂ŴŴ^TX̂^T XWW^TX^T].`
   The left-hand side (Frobenius norm of the elementwise product) is not equivalent to the right-hand side (Frobenius inner product, i.e., trace of the matrix product). The trace form is a reasonable objective for maximizing alignment between the two similarity matrices, but the equality as written is technically incorrect. This does *not* invalidate the AMP mechanism — the gradient-based mask in Eq. (10)–(11) still encourages preservation of token-similarity structure — but the exposition should be corrected.

4. **No variance or multiple-run statistics.** All perplexity and accuracy numbers are reported as single points with no standard deviations, confidence intervals, or sensitivity to different calibration-set draws. Given that PTQ uses only 128 calibration samples, the results could be sensitive to the specific calibration subset. Many papers in this field share this limitation, but it still weakens the evidence, especially where improvements are small (e.g., 0.1–0.4 perplexity points on OPT-13B/30B).

### Trivial

5. **Missing per-dataset breakdown for zero-shot QA.** The paper reports only "AveQA" (average over 7 datasets). Per-dataset scores would allow readers to assess whether gains are concentrated on a few tasks or distributed broadly.

## Nice-to-Haves

- A direct attention-preservation metric (e.g., average cosine similarity or KL divergence between quantized and full-precision attention maps) would strengthen the AMP motivation beyond the proxy token-similarity matrices.
- Results on an additional model family (e.g., Falcon, Mistral, or Gemma) would strengthen generality claims beyond OPT and LLaMA.
- Calibration-time overhead (GPU-seconds, peak memory) relative to ARB-RC/ARB-X would help practitioners assess the practical trade-off.

## Removed Points

- **Criticism about missing appendix content** (overhead analysis, algorithm pseudocode, additional zero-shot results for LLaMA). The parser strips these sections from all papers; they exist in the original submission. Removed per Hard Rules.
- **Claim that AMP derivation is fundamentally flawed / undermines the method.** As noted under Weakness 3, the exposition is imprecise but the core idea (maximizing trace of the product of similarity matrices to preserve token structure) is mathematically valid. The incorrect equality in Eq. 9 is a presentation error, not a method error. Demoted from the harsh critic's "fatal/methodological gap" assessment to Minor.
- **Reproducibility complaints about hyperparameters or undisclosed details.** The algorithm and full procedure are in the (stripped) Appendix; the main text gives the core equations. Per Hard Rules, removed.
- **Criticism that the preliminary analysis "only on LLaMA-2-7B" is insufficient.** The paper uses this single model to *motivate* the approach, then validates across OPT and LLaMA families. This is standard practice.
- **Strength Finder's generic strengths** ("the paper addresses an important problem," "the paper is well-written") — these are not evidence-grounded. Removed.

## Novel Insights

None beyond the paper's own contributions, which are well-articulated: the formal identification of the three failure modes of output alignment (block-level mismatch, error accumulation, attention degradation) and the selective+AMP solution. A genuinely novel synthesis from the reviews is that the AMP mechanism essentially acts as a *data-dependent regularizer* that prevents the output-error minimization from over-optimizing magnitude at the expense of directional structure — this interpretation is implicit in the paper but not stated explicitly.

## Suggestions

1. **Fix the PTB outlier.** Either (a) diagnose why LLaMA-2-7B produces 3166 perplexity on PTB and fix the issue, or (b) provide a clear failure analysis documenting the root cause and remove the claim of "consistently outperforms across all benchmarks."
2. **Justify the last-layer selection with an ablation.** Run output alignment on different subsets of layers within a block and report block-level loss and final perplexity for both OPT-6.7B and LLaMA-2-7B.
3. **Correct Eq. 9.** The AMP objective should be written as maximizing the Frobenius inner product `Tr[A^T B]` (which is a standard measure of matrix alignment), not as a norm of the elementwise product.
4. **Add variance information** — at minimum, run the full quantization pipeline 3 times with different calibration subsets on the two smallest models (OPT-1.3B, LLaMA-2-7B) and report mean ± std for the main perplexity benchmarks.

## Score and Decision

### Round 1 — Bracketing

Three queries searched for similar LLM quantization papers across score bands:

| Band | Query topic | Result anchors (avg scores) |
|------|-------------|------|
| Weak (<3.5) | "1-bit post-training quantization of large language models" | EfficientQAT (3.0), PrefixQuant (3.0), CVXQ (3.0), QCR (3.0) |
| Mid (3.5–7.5) | "binary quantization LLM output alignment" | PB-LLM (6.75), ARB-LLM (7.0), OneQuantLLM (4.5), FlexBCQ (5.0) |
| Strong (>7.5) | "LLM quantization post-training compression" | CBQ (7.6), Scaling Laws for Precision (8.0), Spectra LLM (7.6), Cut Your Losses (8.5) |

**Round-1 bracket: 5.0 – 7.0.** The paper is clearly stronger than the 3.0 rejected papers and not as strong as the 7.6+ papers.

### Round 2 — Narrowing

Two queries targeting the (4.5, 7.5) range:

| Query topic | Anchors |
|-------------|---------|
| "1-bit LLM quantization output alignment attention preservation" (4.5–6.5) | SliM-LLM (5.40), Q-resafe (5.25), OmniQuant (6.40), LLM-QAT (5.0) |
| "post-training quantization LLM binary weight binarization ablation" (6.0–7.5) | PB-LLM (6.75), ARB-LLM (7.0), SpikeLLM (7.0), BinaryDM (6.67) |

Reading full reviews of SliM-LLM (5.40, rejected), OmniQuant (6.40, accepted), PB-LLM (6.75, accepted), and ARB-LLM (7.0, accepted) for calibration:

- **SliM-LLM (5.40)**: Had mathematical errors in core equations and inference slowdown. Our paper is *better* — cleaner math, more consistent results.
- **OmniQuant (6.40)**: Tackles 4-bit quantization (easier problem), limited novelty. Our paper tackles 1-bit (harder) with more analysis depth. *Comparable or slightly better.*
- **PB-LLM (6.75)**: Practical mixed-precision binarization, accepted with moderate evaluation scope. Our paper has broader evaluation but one outlier failure. *Comparable.*
- **ARB-LLM (7.0)**: Direct baseline that our paper claims to improve upon. Strong results including surpassing FP16. Our improvements over ARB-RC/ARB-X are moderate (0.2–2.2 PPL). *Slightly weaker than ARB-LLM.*

### Final Score

The paper makes a genuine contribution (identifying and addressing three failure modes in output-alignment-based 1-bit PTQ) with solid empirical validation across multiple model families. However, the unanalyzed PTB outlier, missing ablation for the last-layer selection, and imprecise AMP exposition prevent it from reaching the 6.5+ tier. Positioned between OmniQuant (6.4) and PB-LLM (6.75), slightly closer to OmniQuant due to the unresolved PTB concern.

**Score: 6.0**  
**Decision: Accept**

The paper's contributions are meaningful, the ablation evidence is strong, and the identified weaknesses are addressable in revision. The PTB outlier should be resolved or explicitly caveated, and the last-layer selection should be ablated, but these do not invalidate the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>