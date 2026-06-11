Good. The Round 2 anchors confirm my bracket. The paper is clearly above the 5.0-5.25 RoPE papers (Wavelet PE, Scaling Laws) which had weaker evaluation and less clean motivation. It sits slightly below "Round and Round We Go!" (6.20, which analyzes RoPE at 7B scale) and clearly below "STRING" (6.50, which demonstrates 10+ point improvements on 70B models). The 6.5-8.0 papers are more foundational theoretical contributions. Final score: **6.0**.

Here is the final review:

---

## Summary
This paper proposes RoPE++, which re-incorporates the discarded imaginary component of RoPE's complex-valued attention score into the model. By rotating query vectors by −π/2 before applying standard RoPE, the method computes imaginary attention heads in parallel with standard real attention heads. Two variants are introduced: RoPE++_EC (equal cache, doubled heads) and RoPE++_EH (equal heads, halved KV cache/QKV parameters). Mathematical analysis shows imaginary attention has a sine-integral characteristic curve that decays more slowly than the cosine-integral curve of real attention, and experiments at 376M and 776M scales demonstrate improvements over RoPE on short- and long-context benchmarks.

## Strengths
- **Clean, novel observation with principled mathematical derivation**: The identification that standard RoPE discards the imaginary part of its complex dot product (Equation 1) and the derivation showing imaginary attention is equivalent to rotating q by −π/2 while preserving both relative and absolute PE formulations (Equations 3-4) is elegant and well-motivated. This is a genuinely under-explored observation in the RoPE literature.

- **Compelling causal evidence via noise injection**: Section 5.2 demonstrates that corrupting imaginary attention (σ=1.0) degrades RULER-4k by 5 points more (376M) and 8 points more (776M) than corrupting real attention, providing direct evidence that imaginary attention plays a dominant role in long-context modeling. This goes beyond correlation to establish causation.

- **Consistent long-context gains**: On RULER (Table 2), RoPE++_EC improves average from 18.8→25.0 at 376M and 27.4→29.4 at 776M; on BABILong, from 11.0→16.1 (376M) and 22.8→24.1 (776M). Margins are largest at the longest tested contexts (64k).

- **Practical cache-efficient variant with demonstrated efficiency gains**: RoPE++_EH halves KV cache and QKV parameters with measurable memory and throughput improvements (Figure 4). Even with half the cache, EH achieves comparable short-context scores to full-cache RoPE (Table 1: 40.3 vs 40.1 at 376M).

- **Modular compatibility with existing techniques**: Table 3 shows RoPE++ combined with both Position Interpolation and YaRN achieves the highest scores (e.g., RULER Avg 34.4 with YaRN at 776M vs 33.5 for RoPE).

## Weaknesses

### Fatal
None.

### Major
- **Incomplete parameter accounting for RoPE++_EC**: Line 99 states "The only cost of RoPE++_EC is an additional imaginary attention computed alongside the real one under the fixed QKV parameter budget," but line 101 acknowledges "W_o in RoPE++_EC is double-sized." Since EC doubles the number of attention heads, the output projection W_o (from head_dim × num_heads → model_dim) doubles in parameters. The paper never reports total parameter counts for any variant. A reader cannot determine whether EC's improvements come from the imaginary attention mechanism or simply from having a larger model. This is the most significant issue — the misleading framing combined with absent parameter counts makes the EC results hard to interpret fairly. The EH variant is less affected since W_o stays the same.

- **Limited experimental scale**: All main experiments are at 376M and 776M with 50B tokens. The paper references Appendix C for larger-scale analysis, but the main text evidence is at scales where attention patterns and scaling dynamics may differ from billion+ parameter models. For a method targeting long-context capability, validation at 1B+ scale would substantially strengthen the paper.

### Minor
- **Oscillatory characteristic curve under-discussed**: Section 3.2 claims imaginary attention "attends more to distant positions" because its sine-integral curve "declines very slowly." However, the sine integral oscillates around zero — at many distances the average imaginary attention weight is negative (anti-attending). The paper calls this "counter-intuitive" but doesn't analyze the practical implications. The empirical results validate the practical benefit, but the theoretical claim is incomplete without addressing oscillation.

- **EH underperformance on BABILong at 776M not acknowledged**: Table 2 shows EH achieves 19.4 average on BABILong at 776M vs RoPE's 22.8 — a 3.4-point gap. The paper claims "comparable performance" for EH (lines 27, 133), which is misleading for this configuration.

- **No variance or confidence intervals reported**: Short-context margins are often 0.1-0.5 points (Table 1), and without variance it is unclear whether these differences are statistically significant.

## Nice-to-Haves
- An ablation on the rotation angle (e.g., −π/4, −π/3) would clarify whether −π/2 is uniquely beneficial or any orthogonal transformation produces similar gains.
- A quantitative analysis of effective attention weight as a function of distance (accounting for oscillation) would make the long-range claim more concrete.
- Interaction between imaginary attention and softmax deserves analysis — imaginary scores can be negative, which could change post-softmax distributions.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **TPOT figure caption contradiction** ("higher TPOT" vs "speeds up decoding"): Likely a parser artifact in figure caption extraction.
- **Missing Appendix C content**: Appendix stripped by parser; larger-scale results cannot be verified from the parsed text.
- **Missing Appendix B preliminaries**: Parser strips appendix content.
- Any typos, formatting issues, or parser artifacts.

## Novel Insights
The observation that standard RoPE discards the imaginary part of its complex dot product is genuinely novel in the RoPE improvement literature. The insight that this imaginary part carries sine-based positional information with a fundamentally different decay characteristic (sine integral vs cosine integral) provides clean theoretical motivation. The noise injection experiment is a well-designed causal test that establishes imaginary attention's dominant role in long-context tasks.

## Suggestions
1. **Report total parameter counts and FLOPs** for all variants in a table — this is the single highest-leverage fix.
2. **Acknowledge the EH-BABILong underperformance** at 776M and discuss when EH is and isn't a good trade-off.
3. **Add a brief analysis of oscillation effects** — show that learned weights compensate or qualify the theoretical claim.
4. **Include variance across seeds** for short-context results where margins are small.

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Long-context Extrapolation via Periodic Extension | jp4pxKqCRW | 2.50 | 1 | Much weaker: poorly written, weak theory, limited experiments. Paper under review is clearly superior. |
| Efficient transformer with reinforced PE | 5dDYhvt6dY | 3.00 | 1 | Weaker: marginal gains, limited evaluation. Paper under review has cleaner theory. |
| Wavelet-based Positional Representation | OhauMUNW8T | 5.25 | 1 | Similar topic, weaker: marginal improvements, gaps in motivation. Paper under review has cleaner analysis. |
| Scaling Laws of RoPE-based Extrapolation | JO7k0SJ5V6 | 5.00 | 1 | Similar topic: strong theory but only ppl evaluation, one reviewer found it redundant with YaRN. Paper under review has more comprehensive benchmarks. |
| Contextual Position Encoding | sIGWTd1DcW | 5.25 | 1 | Similar topic: interesting but rejected. Paper under review has stronger empirical validation. |
| Learning positional encodings depends on initialization | fn0mjkZopf | 5.25 | 2 | Different focus (learned PE initialization). Less directly comparable. |
| Round and Round We Go! | GtvuNrk58a | 6.20 | 1, 2 | Closest: analyzes RoPE internals at 7B scale. Higher score due to larger-scale analysis, but paper under review has a practical method with more comprehensive benchmarks. Slightly above paper under review. |
| TAPE: Contextualized Equivariant PE | Us1RXG1Ji2 | 6.00 | 2 | Similar score range: novel PE framework with split reviews (5,8,3,8). Comparable quality but different approach. |
| Vocabulary In-Context Learning in Transformers | YE6N8htoFQ | 6.00 | 2 | Different focus (theoretical ICL analysis). Less comparable. |
| Why Does Effective Context Length Fall Short? | eoln5WgrPx | 6.50 | 1 | Stronger: training-free STRING method with 10+ point gains on 70B models. Paper under review needs training but offers a structural improvement. Below this anchor. |
| CLEX: Continuous Length Extrapolation | wXpSidPpc5 | 6.50 | 1 | Similar: RoPE-based extension with competitive LongBench results. Both have comparable quality. |
| Eliminating Position Bias (mechanistic) | fvkElsJOsN | 6.60 | 2 | Different focus (position bias mitigation, training-free). Less directly comparable. |

**Round 1 bracket: 5.5–7.0.** After Round 2: narrowed to 5.5–6.5. The paper is clearly above the 5.0–5.25 RoPE papers (cleaner theory, more comprehensive benchmarks), slightly below "Round and Round" (6.20) and clearly below STRING (6.50, validated at 70B scale). The parameter accounting issue and limited scale hold it back from 6.5. **Final score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>