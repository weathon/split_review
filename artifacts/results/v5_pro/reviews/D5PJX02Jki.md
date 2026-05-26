Now I have a thorough understanding of the paper and the calibration anchors. Let me compose the final consolidated review.

---

## Summary

This paper proposes RoPE++, an extension to Rotary Position Embeddings that re-incorporates the imaginary component of the complex-valued attention score — which standard RoPE discards — as a second group of attention heads. The imaginary attention requires only a π/2 rotation of the query vector while preserving the unified absolute–relative positional encoding property. Two configurations are introduced: RoPE++_EC (equal cache, doubled attention heads) and RoPE++_EH (equal heads, halved KV cache). Pre-training experiments at 376M and 776M scales show that RoPE++_EC substantially outperforms standard RoPE on long-context benchmarks (e.g., RULER, BABILong), while RoPE++_EH matches RoPE performance with half the cache cost. Attention-pattern analysis and noise-injection experiments provide mechanistic evidence that imaginary heads play a dominant role in long-range context modeling.

## Strengths

- **Clean mathematical derivation with minimal architectural change**: The paper elegantly shows (Eqs. 2–4) that the imaginary attention reduces to a π/2 rotation of the query vector followed by the same RoPE operation, requiring no new parameters or architectural complexity beyond standard attention. This is a genuinely parsimonious idea.

- **Strong and consistent long-context gains for the EC variant**: Across two model scales, RoPE++_EC delivers substantial improvements on RULER and BABILong. For the 376M model, RULER average rises from 18.8 (RoPE) to 25.0, and BABILong from 11.0 to 16.1 (Table 2). The gains are largest at the longest context lengths (RULER 64k: 9.0 vs 5.5; BABILong 64k: 12.8 vs 7.8), directly validating the claimed long-context benefit.

- **Practical efficiency variant with maintained quality**: RoPE++_EH halves KV-cache and QKV parameters while achieving comparable or better performance than full-cache RoPE on most benchmarks (Tables 1–2). Measured memory and TPOT (Figure 4) confirm real efficiency gains that widen with context length.

- **Compelling mechanistic evidence**: The noise-injection experiment (Section 5.2) shows that corrupting imaginary attention degrades long-context performance by up to 8 points more than corrupting real attention, providing direct causal evidence that imaginary heads are critical for long-range modeling. The attention-pattern visualizations (Figure 5) further corroborate this by showing imaginary heads preferentially attend to initial/global positions.

- **Well-motivated theoretical analysis**: The characteristic curve for imaginary attention (Eq. 5, Figure 1) shows slower decay than the real attention curve, providing a clear theoretical motivation for why imaginary heads should help with long-range dependencies. The length-extrapolation analysis (Section 3.4) connecting sign exposure of sinusoidal functions to improved extrapolation is insightful.

## Weaknesses

### Fatal

None.

### Major

- **Single training run per configuration with no error quantification**: Every result in Tables 1–3 and Figure 4 comes from a single pre-training run per configuration. No error bars, confidence intervals, or multiple seeds are reported. The short-context gains are often under one percentage point (e.g., RoPE++_EC averages 41.0 vs RoPE 40.1 at 376M; 42.8 vs 42.0 at 776M). Without variance estimates, it is impossible to distinguish genuine improvement from sampling noise on these narrow margins. This is a significant gap for a paper that claims "consistent improvement" as a central finding. The long-context gains are larger and more robust-looking, but the same concern applies — particularly where RoPE++_EH occasionally underperforms RoPE (e.g., RULER-4k at 376M: 29.9 vs 31.6).

- **Modest experimental scale limits generality of claims**: The paper pre-trains models at only 376M and 776M parameters with 50B tokens. While this is a common scale for position-embedding ablations, the paper makes broad claims about RoPE++ as a general improvement over standard RoPE. No results at 1B+ scale or on existing open-weight models are provided, leaving open the question of whether the benefits persist at the scales where long-context LLMs are actually deployed. The short-context gains, in particular, may vanish or reverse at larger scales where the baseline already performs well.

### Minor

- **Configuration descriptions (EC/EH) are ambiguous**: The text in Section 3.3 and the visualization in Figure 2 are not fully aligned. The paper states RoPE++_EC "doubles the attention head group size" with "equal cache size," and Figure 2b is captioned as showing doubled query heads but halved key heads. It is unclear how key heads can be halved while maintaining equal cache without also adjusting per-head dimensions — and this adjustment is never explained explicitly. Similarly, the precise relationship between W_q, W_k, W_v, and W_o shapes across configurations requires the reader to infer rather than being stated. A small table specifying head count, per-head dimension, and parameter counts for a concrete architecture would resolve this completely.

- **No prefill/latency cost reported for RoPE++_EC**: The efficiency analysis (Figure 4) covers only RoPE++_EH, reporting memory and TPOT. RoPE++_EC, which doubles the number of attention heads, almost certainly incurs additional compute during prefill, yet no FLOPs analysis or prefill throughput is reported for either variant. The paper's efficiency claims would be stronger with a complete accounting.

- **Limited scope of mechanistic analysis**: The noise-injection experiment (Section 5.2) uses only two layers per model and one perturbation type (Gaussian noise). A cleaner ablation — e.g., training a RoPE++ model and then zeroing out the imaginary heads at inference, or training a variant with only imaginary heads — would more directly quantify the imaginary component's contribution. The current evidence is suggestive rather than dispositive.

- **Long-context baselines limited to RoPE**: Table 2 compares RoPE++ only against standard RoPE for long-context evaluation; FoPE, Pythia, and ALiBi are excluded. The paper acknowledges this is because those methods "lack an established extension mechanism," which is a reasonable justification, but it means the paper cannot claim RoPE++ outperforms those baselines in long-context settings.

- **"Information loss" framing is rhetorical rather than factual**: The paper states that standard RoPE "discards the imaginary part outright" and incurs "irreversible information loss" (Sec. 1). The real-valued dot product in RoPE is a design choice, not a lossy compression of a complex-valued computation. The imaginary part was never part of the defined operation. While the paper acknowledges that "taking the real part preserves the direct equivalence," the "information loss" framing overstates the case. This does not affect the method's validity but weakens the motivation's precision.

### Trivial

- The claim about extrapolation ("perplexity grows more slowly") is argued qualitatively in Section 3.4; a dedicated perplexity-vs-context-length plot for pure extrapolation (beyond the 64k benchmark in Table 2) would strengthen this point but is not essential given the long-context evaluation.

## Nice-to-Haves

- Training a RoPE++ model at 1B+ scale or fine-tuning an existing open-weight model with RoPE++ to show gains without from-scratch pre-training would substantially strengthen the paper's practical claims.
- Reporting hyperparameter sensitivity (e.g., whether the gains survive different learning rates, weight decay, or rotary base values) would address concerns about robustness.
- A dedicated perplexity-vs-context-length curve for pure length extrapolation would complement the theoretical argument in Section 3.4.
- Comparison with additional long-context baselines (even if limited to inference-only methods like SelfExtend or SnapKV) would strengthen the long-context narrative.

## Removed Points

These points from the harsh critic were considered but removed or demoted:

1. **"Figure 2b shows doubled query heads but halved key heads, which contradicts the caching claim"** → Partially removed as a contradiction claim. The configuration *is* under-specified, but the core logic (equal cache via halved per-head key dimension) is inferable. Retained the clarity concern at Minor level instead.

2. **"The statement that '75% imaginary vs. 25% real' is puzzling and suggests a misunderstanding"** → Removed. The paper's logic is actually coherent: since real and imaginary heads share W_q and differ only by a π/2 rotation, arbitrary proportions are structurally impossible. This is a correct observation, not a misunderstanding.

3. **"Missing reference to related complex-valued attention work / deeper discussion of how RoPE++ differs"** → Removed per rules against flagging missing related works.

4. **"Larger-scale validation needed / hyperparameter sensitivity / seed variance"** → Moved to Nice-to-Haves, as these are scope-expanding requests rather than core flaws given the paper's scale and focus.

5. **Demands for "multiple seeds" treated as a Major weakness rather than Fatal** → The single-run limitation is real but standard for position-embedding pre-training ablation papers at this scale. Kept as Major because the paper's central claim of "consistent improvement" requires variance estimation to be credible on short-context tasks.

## Novel Insights

The observation that the imaginary part of the RoPE complex product corresponds to an attention operation with a π/2-rotated query — and that this "imaginary attention" has a slower-decaying characteristic curve (Si function vs. cosine integral) — is genuinely novel and well-motivated. The practical consequence that this yields cache-efficient variants (EC and EH) through head-group doubling without extra parameters is an elegant connection between a mathematical curiosity and a practical engineering concern. The noise-injection experiment establishing a causal role for imaginary heads in long-context performance is a creative validation strategy that other position-embedding papers could adopt.

## Suggestions

- Add a small table specifying head count, per-head dimension, W_q/W_k/W_v/W_o shapes, and KV cache size for a concrete architecture under RoPE, RoPE++_EC, and RoPE++_EH. This would eliminate all ambiguity about the configurations in one place.
- Report prefill throughput or FLOPs for both EC and EH variants alongside the existing memory/TPOT curves (Figure 4).
- Consider a clean ablation: train a RoPE++_EC model, then at inference time zero out the imaginary attention heads and measure the performance drop. This would directly quantify the imaginary component's contribution without the confound of noise injection.
- If compute allows, report results from at least two seeds on the 376M configuration to give readers a sense of variance. Even two runs would substantially strengthen the credibility of the short-context claims.

## Score and Decision

**Anchor papers considered:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| jp4pxKqCRW | 2.50 | R1-topic-low | Much weaker: limited novelty, insufficient evaluation |
| 5dDYhvt6dY | 3.00 | R1-topic-low | Weaker: different domain, very limited eval |
| JO7k0SJ5V6 | 5.00 | R1-topic-mid, R2 | Comparable: similar RoPE extension with theory, but less diverse eval metrics |
| GtvuNrk58a | 6.20 | R1-topic-mid | Stronger: deeper mechanistic analysis on 7B model |
| eoln5WgrPx | 6.50 | R1-topic-mid | Stronger: results on 70B models, training-free method |
| Us1RXG1Ji2 | 6.00 | R1-topic-mid | Stronger novelty but mixed reviews; rejected |
| EytBpUGB1Z | 8.00 | R1-topic-high | Much stronger: extensive experiments, clear contribution |
| OvoCm1gGhN | 8.00 | R1-topic-high | Much stronger: similar dual-attention idea but with extensive validation |
| E2RyjrBMVZ | 4.17 | R1-weakness | Shares single-run limitation; our paper has this weakness |
| bmrYu2Ekdz | 6.50 | R1-weakness | Shows importance of multiple seeds for stable findings |
| xHMMt7r3GW | 5.33 | R2 | Comparable: RoPE extension with similar novelty level; rejected |
| sIGWTd1DcW | 5.25 | R2 | Comparable: novel PE approach with limited evaluation; rejected |
| 3Z1gxuAQrA | 6.00 | R2 | Stronger: more thorough evaluation, all reviewers scored 6 |
| t717joHHSc | 4.75 | R2 | Comparable quality, different approach; rejected |

**Round 1 bracket:** The paper sits clearly above the low-band anchors (2.5–3.0) — it has genuine novelty, clean methodology, and diverse evaluation that those papers lack. It sits below the high-band anchors (7.5–8.0), which have far more extensive experimental validation. Within the mid-band (3.5–7.5), the paper is most comparable to JO7k0SJ5V6 (5.00) and xHMMt7r3GW (5.33), both of which propose RoPE extensions with theoretical motivation but have evaluation limitations. The paper is clearly weaker than GtvuNrk58a (6.20) and eoln5WgrPx (6.50), which have stronger experimental validation and/or larger-scale results. Initial bracket: **4.5–5.5**.

**What did the low-band anchors fail at, and does the paper under review share any of those failures?** The low-band anchors (2.5–3.0) failed at insufficient novelty, poor or absent evaluation, and unclear methodology. The paper under review does NOT share these failures — it has clear novelty, a well-defined methodology, and diverse evaluation across short and long contexts. However, the paper does share the single-run/no-error-bar failure mode with weakness-anchored papers like E2RyjrBMVZ (4.17), which is significant: the paper claims "consistent improvement" but provides no variance estimates, and the short-context gains are narrow enough to be plausibly explained by noise.

**Round 2 narrowing:** The narrowed anchors (4.75–6.00) confirm the 4.5–5.5 bracket. The paper is comparable to JO7k0SJ5V6 (5.00, accepted with mixed reviews) in novelty and evaluation quality, but JO7k0SJ5V6 tested at larger scale (7B/13B). The paper is below 3Z1gxuAQrA (6.00, all 6s) which had more thorough evaluation. The single-run weakness and modest scale prevent the paper from reaching the 5.5–6.5 range occupied by papers with stronger validation.

**Final score: 5.0.** The paper presents a genuinely novel and elegant extension to RoPE with compelling long-context results. However, the single-run limitation means the "consistent improvement" claim on short-context tasks is not adequately supported, and the modest experimental scale (376M/776M) limits confidence that the findings generalize. The long-context gains for RoPE++_EC are the paper's strongest evidence and are substantial enough to be credible even with single-run data, but the overall evidential basis does not yet meet the standard for a strong accept.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>