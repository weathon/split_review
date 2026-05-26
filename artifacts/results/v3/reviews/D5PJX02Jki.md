Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes RoPE++, which extends Rotary Position Embedding (RoPE) by re-introducing the imaginary component of the complex-valued attention score that standard RoPE discards. The imaginary attention is computed alongside the standard real attention in two configurations: RoPE++_EH (equal head count, halved KV cache) and RoPE++_EC (equal cache, doubled heads). Models at 376M and 776M are pre-trained on DCLM and evaluated on short- and long-context benchmarks.

## Strengths

1. **Clear mathematical identification of the discarded imaginary component.** The paper formally derives the imaginary attention (Equations 2–4), showing it is equivalent to applying a −π/2 rotation to the query before standard RoPE. This results in a principled dual-component attention mechanism rather than an ad-hoc modification.

2. **Consistent long-context improvement of RoPE++_EC over standard RoPE.** On long-context benchmarks (Table 2), RoPE++_EC outperforms RoPE at the same cache cost across both model sizes: e.g., 776M RULER average 29.4 vs. 27.4, BABILong average 24.1 vs. 22.8. The advantage is systematic across context lengths up to 64k.

3. **Efficiency advantage of RoPE++_EH with halved KV cache.** Figure 4 demonstrates measurable memory and decoding-time reductions for RoPE++_EH at both model sizes, with the gap widening as context length grows. This provides a practical efficiency-performance trade-off for long-context deployment.

4. **Theoretical explanation for improved length extrapolation (Section 3.4).** The analysis showing that combining real and imaginary attention exposes Q/K dimensions to a wider range of positional values (full cos/sin range) during training is insightful and provides a principled reason for why RoPE++ may extrapolate better.

5. **Compatibility with PI and YaRN (Table 3).** RoPE++_EC consistently improves upon the corresponding RoPE baselines under both Linear PI and YaRN interpolation, demonstrating that the benefit generalizes beyond a single training recipe.

## Weaknesses

### Major

1. **No ablation controlling for increased head count in RoPE++_EC.** RoPE++_EC doubles the number of attention heads relative to the RoPE baseline, while the paper attributes the improvement to the imaginary component itself. A proper ablation would compare RoPE++_EC (n real + n imaginary heads, shared QKV) against a variant with the same doubled head count but all heads using standard real RoPE (i.e., 2n real heads). Without this, it is impossible to tell whether the gains come from the −π/2 rotation or simply from having more attention heads. This confound undermines the core mechanistic claim that "imaginary attention plays a dominant role in long-context modeling."

2. **RoPE++_EH performance is inconsistent and the "comparable" claim is over-stated.** The paper states that RoPE++_EH "achieves comparable results with vanilla RoPE with half the cache." However, Table 2 shows RoPE++_EH underperforms RoPE on 776M BABILong by 3.4 points (22.8 vs. 19.4). Table 3 shows even larger gaps under YaRN/PI at 376M (e.g., RULER: 28.2 vs. 24.7; BABILong: 14.4 vs. 10.5). The paper does not discuss these failure cases or specify under what conditions EH's cache savings are worth the performance cost.

3. **Long-context evaluation lacks comparisons with other position embeddings on the same protocol.** The long-context experiments (Tables 2, 3) compare RoPE++ only against vanilla RoPE. FoPE, Pythia, and ALiBi—which were included in the short-context evaluation (Table 1)—are absent from the long-context benchmarks. Since the paper claims to "outperform vanilla RoPE and other position embeddings on average across short- and long-context benchmarks" (contribution list), the long-context half of the claim is only partially supported (vs. RoPE, not vs. other PEs). Adding at least ALiBi (which is designed for length extrapolation) would substantiate the claim.

### Minor

4. **Single-run results without variance or statistical significance.** All experiments appear to be single runs. The margins in Table 1 are often <1 point (e.g., 376M Avg: RoPE++_EC 41.0 vs. ALiBi 40.5), and without error bars or multiple seeds it is unclear whether these differences are meaningful. This is especially relevant given pre-training variance.

5. **Noise-injection experiment has methodological caveats.** The Gaussian noise experiment (Section 5.2) is a useful diagnostic, but (a) the scale of attention scores for real vs. imaginary heads is not reported, so equal σ may not be equally disruptive to both components; (b) the baseline (σ=0) score is only shown visually, not reported in text. These caveats weaken the claim that "imaginary attention plays a more dominant role."

6. **The theoretical claim about "imaginary attention assigning more weight to long context" needs qualification.** Section 3.2 states this based on the sine-integral characteristic curve, but the sine function oscillates rather than monotonically decaying. The claim would be stronger if framed as "on average across frequency bands, the envelope decays more slowly than the cosine curve," which the paper hints at but does not explicitly state.

### Trivial

7. **Figure 2 caption may cause confusion.** The caption for RoPE++_EH says "query heads are halved" while the text says "keeps equal attention head number." These are reconcilable but the discrepancy could mislead readers, especially given the complexity of the GQA configurations.

## Nice-to-Haves

- **Long-context perplexity curves** (e.g., PG-19 at varying context lengths) would directly support the Section 3.4 claim that "perplexity grows more slowly beyond the maximum supported context length," complementing the RULER/BABILong results.
- **Breakdown of RULER gains by subtask length** to show that the gap widens with longer contexts, which would strengthen the central narrative.
- **Clarify how 32k continued-training sequences are constructed** (contiguous chunks, same corpus as pre-training, batch size in tokens) for reproducibility.

## Removed Points

- *Missing architectural details (layers, heads, hidden dimensions)*: The paper states these are in Appendix C, which was stripped by the PDF parser. These are not missing in the original submission.
- *Unknown DCLM composition*: The paper cites Li et al. (2024) for the dataset. This is standard practice.
- *Reproducibility concern about non-released checkpoints/code*: The paper states they are publicly released. Per the hard rules, doubting the existence of cited artifacts is not permitted.
- *Missing related works*: Per the hard rules, this cannot be mentioned without external verification.
- *Missing warmup/decay details*: The paper explicitly provides these (0.5B tokens warmup, 5B tokens decay).

These points are removed because they either reflect parser artifacts, cite references the reviewer could check, or violate the hard rules about reproducibility nitpicks.

## Novel Insights

The key insight—that the imaginary part of the complex-valued RoPE attention score has a slower-decaying positional bias and can be recovered via a simple −π/2 query rotation—is genuine and well-derived. The connection between this imaginary component and improved length extrapolation through broader positional value coverage (Section 3.4) is a novel theoretical contribution beyond the empirical extension itself. The noise-perturbation experiment, despite its limitations, provides a creative approach to establishing causality in attention analysis.

## Suggestions

1. **Add the missing head-count ablation.** Compare RoPE++_EC against a RoPE baseline with the same doubled head count (2n heads, all real) at the same cache. This is the cleanest way to isolate the effect of the imaginary rotation from the effect of having more heads.
2. **Run long-context evaluation for at least one additional baseline** (ALiBi would be the most informative, given its design for length extrapolation).
3. **Acknowledge the settings where RoPE++_EH underperforms and discuss when the cache savings justify the cost.** Tables 2 and 3 provide the data; the paper should synthesize it.
4. **Report results from at least 2 seeds (or provide evidence of low variance) for the main benchmarks** to establish that the observed improvements are reliable.
5. **Fix the Figure 2 caption/description** to avoid confusion about head counts.

## Score and Decision

After synthesizing the review, I now need to calibrate the score against the anchors.

**Calibration anchor summary:**

| Anchor | Avg Score | Round & Query | Comparison to Paper |
|--------|-----------|---------------|---------------------|
| Scaling Laws of RoPE-based Extrapolation (JO7k0SJ5V6) | 5.00 | R1-topic-mid | Stronger theoretical framework, weaker evaluation (PPL only). Paper under review has better downstream evaluation but missing ablations. Roughly comparable quality. |
| Round and Round We Go (GtvuNrk58a) | 6.20 | R1-topic-mid | Stronger analysis of RoPE internals, more novel insight. Paper under review is weaker. |
| CLEX (wXpSidPpc5) | 6.50 | R1-topic-mid | More comprehensive evaluation, stronger baselines. Paper under review is weaker. |
| Wavelet-based Positional Rep (OhauMUNW8T) | 5.25 | R1-topic-mid | Similar-level contribution (alternative PE modification), similar evaluation gaps. Comparable. |
| Bias Learning (4GD7a9Bo9A) | 4.50 | R1-weakness | Rejected paper with missing evaluation, similar gap in completeness. Paper under review is slightly stronger (better evaluation). |
| Contextual Position Encoding (sIGWTd1DcW) | 5.25 | R2 | Rejected paper with novel idea but scalability concerns. Paper under review has similar quality. |
| Long-context Extrapolation via Periodic Extension (jp4pxKqCRW) | 2.50 | R1-topic-low | Fundamentally flawed. Paper under review is clearly stronger. |

**Round 1 bracket:** Between 4.0 and 5.5 (clearly above the 2-3 low-band, below the 6+ stronger papers).

**What did the low-band anchors fail at, and does the paper share any of those failures?**
Low-band anchors (2-3) had fundamentally incomplete evaluations (e.g., PPL-only, no downstream tasks), unclear methodology, or no empirical evidence supporting claims. The paper under review does **not** share these fundamental failures: it has a clear methodology, pre-trains models, and evaluates on multiple downstream benchmarks. However, it does share a milder version of "missing critical comparisons" (long-context baselines only vs. RoPE) and "confounded attribution" (no head-count ablation), which aligns it more with the mid-band papers that were scored 4-5.5.

**Final score:** 4.5 / 10.

The paper presents a mathematically sound and interesting extension of RoPE. However, the experimental evaluation has two significant gaps: (1) the missing head-count ablation confounds the attribution of improvement to the imaginary component, and (2) the RoPE++_EH's inconsistent performance is not honestly characterized. These issues are not fatal (the core RoPE++_EC results are clear and reproducible) but they prevent the paper from making a strong, well-supported case for its contribution. The idea has merit, but the evidence needs strengthening before publication.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>