## Summary

The paper proposes RoPE++, an extension to Rotary Position Embeddings (RoPE) that reincorporates the imaginary component of the complex-valued attention score that standard RoPE discards. The imaginary attention is computed by rotating the query by -π/2 before applying the standard RoPE procedure, yielding a sine-based distance kernel with slower decay than the cosine kernel of real attention. Two configurations are introduced: RoPE++_EH (equal heads, halved KV cache) and RoPE++_EC (equal cache, doubled heads). Experiments at 376M and 776M scales show that both variants outperform or match standard RoPE on short- and long-context benchmarks, with the EC variant showing particularly consistent long-context gains.

## Strengths

1. **Clean theoretical derivation of the imaginary extension (§3.1, Eqs. 1–4):** The paper formally derives what information is discarded when RoPE keeps only the real part of the complex-valued dot product and shows the imaginary component can be materialized via a simple -π/2 query rotation. This mathematical framing is precise and practically actionable.

2. **Noise ablation experiment provides causal evidence for the core claim (§5.2, Figure 5e/5j):** Adding Gaussian noise (σ=1.0) to the imaginary attention degrades RULER-4k scores by ~5 points (376M) and ~8 points (776M) more than the same perturbation of real attention. This clean intervention directly confirms that imaginary heads are the dominant mechanism for long-context modeling, going beyond correlational evidence.

3. **Consistent long-context gains for RoPE++_EC at equal KV cache cost (Table 2):** RoPE++_EC outperforms vanilla RoPE on RULER average by 6.2 points (25.0 vs. 18.8 at 376M) and 2.0 points (29.4 vs. 27.4 at 776M), and on BABILong by 5.1 and 1.3 points respectively. Gains are most pronounced at 64k extrapolation, where RoPE++_EC consistently achieves the best scores.

4. **Generalization across interpolation methods (§5.3, Table 3):** RoPE++ maintains its advantage when combined with Linear PI and YaRN, demonstrating the method is complementary to existing context-extension techniques rather than competing with them.

5. **Dual-configuration design with explicit trade-offs (§3.3, Figure 4):** The two variants (EH for efficiency, EC for performance) are clearly motivated, and the EH variant's practical memory/throughput benefits are empirically validated across context lengths up to 128k.

## Weaknesses

### Fatal
None.

### Major

1. **Resource-equity confound in RoPE++_EC vs. RoPE comparison (§3.3, Table 2):** RoPE++_EC uses a double-sized W_o and potentially larger W_q compared to baseline RoPE. The paper states this is "under the fixed QKV parameter budget" (Section 3.3) while also noting "W_o in RoPE++_EC is double-sized." The reported "376M and 776M model sizes" appear to be nominal — it is unclear whether total parameters are held exactly constant across configurations or whether RoPE++_EC has a parameter/compute advantage. Without an explicit equi-resource ablation (e.g., fixing total parameters and allocating some to imaginary heads vs. all to standard heads), the EC variant's gains cannot be cleanly attributed to the imaginary extension rather than to increased model capacity. This does not invalidate the method — the EH variant partly addresses this by showing gains with fewer resources — but it is a significant confound for the headline claim.

### Minor

2. **Overclaim for RoPE++_EH on one benchmark (§3.3, Table 2):** The paper claims RoPE++_EH achieves "comparable or even superior results" and "comparable performance with vanilla RoPE using half the cache." At 776M on BABILong (Table 2), RoPE++_EH scores 19.4 vs. vanilla RoPE 22.8 — a 3.4-point gap that contradicts "comparable." The EH variant does achieve comparable or better results in other settings (376M BABILong: 11.6 vs. 11.0; 776M RULER: 28.6 vs. 27.4), but the specific BABILong regression at 776M is unreconciled with the paper's narrative.

3. **No variance or statistical significance reported (Tables 1–3):** All results are single-run point estimates. Short-context margins are small (e.g., 376M Short: RoPE 40.1, RoPE++_EC 41.0 — a 0.9-point difference over 11 tasks). Without variance estimates, it is impossible to assess whether these differences are meaningful or noise. Multiple seeds at 50B tokens of training are expensive, which tempers this criticism, but it remains a limitation.

### Trivial

4. **Unsubstantiated FlashAttention integration claim (§3.3):** The paper asserts imaginary attention "plugs directly into MHA or GQA... in a single pass in FlashAttention" without empirical verification or discussion of whether existing kernels support query interleaving.

5. **Mild overstatement of "first identify" claim (Contributions):** The paper claims to "first identify the loss of imaginary information in standard RoPE." The complex representation of RoPE is well-known (Su et al., 2024); the novelty is in *using* the discarded imaginary component, not in *identifying* its existence.

## Nice-to-Haves

- Report FLOPs per forward pass for each configuration to support efficiency claims quantitatively.
- Provide architectural details (number of layers, hidden dimension, head counts) for each configuration in the main text, not just the appendix.
- Include at least 2 training seeds for a subset of experiments to bound variance.

## Removed Points

- **"Abstract framing is misleading" (HC):** The claim that standard RoPE "discards" the imaginary component is mathematically accurate (Eq. 1 shows only the real part is retained). This is factual, not rhetorical overreach.
- **"Per-task variation suggests advantage not uniform" (HC):** The paper's claim is about average performance, which is supported. Per-task variation is expected and does not undermine the claim.
- **"Methodology description is hard to follow" (HC):** Subjective; the prose and mathematical presentation are adequate.
- **"Missing architectural details in appendix" (HC):** Appendix C was stripped by the parser; this is a formatting artifact, not an author error.
- **Generic strengths from Strength Finder ("addressed an important problem", "targeted an interesting question"):** Dropped as generic/superficial.

## Novel Insights

The noise-ablation experiment (Figure 5e/5j) provides unusually clean causal evidence for the distinct functional roles of real vs. imaginary attention heads, showing that the imaginary component is not just a redundant computation but carries disproportionate responsibility for long-context performance. This experimental design — corrupting one component while leaving others intact — could serve as a template for future work on multi-component attention mechanisms.

## Suggestions

1. **Add an equi-resource ablation:** Fix total model parameters between RoPE and RoPE++_EC by slightly reducing other dimensions (e.g., fewer layers or smaller hidden size) to compensate for the larger W_o/W_q. This would cleanly separate the effect of the imaginary extension from increased capacity.
2. **Report actual parameter counts** for each configuration (RoPE, RoPE++_EC, RoPE++_EH) in the main text so readers can judge resource equity.
3. **Acknowledge the BABILong 776M EH regression explicitly** and discuss what might cause it (e.g., do imaginary heads interfere with the multi-hop reasoning that BABILong tests?).

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jp4pxKqCRW.md | 2.50 | R1 low | Much weaker (broken periodic extension paper) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/5dDYhvt6dY.md | 3.00 | R1 low | Much weaker (efficient transformer with RP, small scale) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/OvoCm1gGhN.md | 8.00 | R1 high | Much stronger (Diff Transformer, major architecture innovation) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/EytBpUGB1Z.md | 8.00 | R1 high | Much stronger (Retrieval Head, deep mechanistic analysis) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/GtvuNrk58a.md | 6.20 | R1 mid / R2 | Stronger (deeper RoPE analysis, larger model studied) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/eoln5WgrPx.md | 6.50 | R1 mid | Stronger (STRING, training-free method, 10+ pt gains on RULER) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/JO7k0SJ5V6.md | 5.00 | R1 mid / R2 | Weaker (theory-only, limited to perplexity evaluation) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/OhauMUNW8T.md | 5.25 | R1 mid / R2 | Weaker (wavelet PE, marginal empirical improvement) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/3Z1gxuAQrA.md | 6.00 | R2 | Stronger/similar (PoSE, practical context extension, real LLMs) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/sIGWTd1DcW.md | 5.25 | R2 | Slightly weaker (CoPE, novelty concerns, incomplete evaluation) |

**Round-1 bracket:** 4.0 – 7.0 (above weak reject-level papers, below high-impact papers)

**Round-2 narrowing:** The paper sits between the 5.00–5.25 level (weaker position embedding papers with marginal results or limited evaluation) and the 6.00–6.20 level (stronger RoPE analysis or practically impactful methods evaluated on real LLMs). The core idea is cleaner than the wavelet/CoPE papers, and the long-context empirical evidence is stronger, but the resource-equity confound and small-scale evaluation prevent it from reaching the 6.00 level.

### Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>