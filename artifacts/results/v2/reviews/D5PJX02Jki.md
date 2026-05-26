Now I'll compose the final consolidated review.

## Summary

This paper identifies that the standard RoPE-based attention discards the imaginary component of the complex-valued attention score, and proposes RoPE++, which re-introduces this imaginary component as a separate group of attention heads. Two configurations are introduced: RoPE++⸤EH⸥ (same number of heads, half KV cache/QKV params) and RoPE++⸤EC⸥ (same cache size, doubled heads with doubled W_o). The paper provides a theoretical analysis showing that the imaginary attention's characteristic sine-integral curve decays more slowly than the real attention's cosine curve, making it better suited for capturing long-context dependencies. Experiments at 376M and 776M scales show consistent improvements over vanilla RoPE on short-context (Table 1) and long-context benchmarks (RULER, BABILong — Tables 2–3), with RoPE++⸤EC⸥ showing the largest gains.

## Strengths

1. **Novel identification and principled theoretical analysis of the discarded imaginary component.** The paper identifies an overlooked information loss in standard RoPE and derives closed-form characteristic curves (Eq. 5, Figure 1) showing that imaginary attention (sine integral) decays more slowly than real attention (cosine integral), providing a clear theoretical rationale for why re-incorporating it benefits long-context modeling.

2. **Consistent empirical gains on long-context benchmarks across two model scales.** Table 2 shows RoPE++⸤EC⸥ improving over vanilla RoPE on RULER average by 6.2 points (376M: 25.0 vs. 18.8) and 2.0 points (776M: 29.4 vs. 27.4), with gains holding up to 64k context. BABILong improvements are similarly consistent.

3. **Practical efficiency configuration with real benefits.** RoPE++⸤EH⸥ achieves comparable or better average short-context performance (Table 1: 776M Avg 42.5 vs. RoPE 42.0) while halving KV cache size and QKV parameters, with memory and throughput gains documented in Figure 4.

4. **Compatibility with existing long-context extension methods.** Table 3 shows that RoPE++ combined with Linear PI or YaRN consistently outperforms vanilla RoPE with the same techniques (e.g., 776M YaRN RULER Avg: RoPE++⸤EC⸥ 34.4 vs. RoPE 33.5), demonstrating plug-and-play integration.

## Weaknesses

### Major

1. **RoPE++⸤EC⸥ has a confounded parameter increase that is not controlled for.** The paper states (Section 3.3) that W_o in RoPE++⸤EC⸥ is "double-sized" because the imaginary attention doubles the number of output heads. This means RoPE++⸤EC⸥ — which shows the largest gains — differs from vanilla RoPE in *two* respects: it introduces imaginary attention *and* it increases output projection capacity. No control experiment is run that isolates the effect of the imaginary mechanism by matching the total parameter budget (e.g., a version of standard RoPE with 2H heads and the same doubled W_o, but without the −π/2 rotation). RoPE++⸤EH⸥ partially addresses this concern since it has *fewer* total parameters than RoPE, but on the BABILong benchmark at 776M, RoPE++⸤EH⸥ underperforms vanilla RoPE (19.4 vs. 22.8 average), and even on RULER the advantage is modest (28.6 vs. 27.4). Until a proper capacity-controlled ablation is done, the core claim that the imaginary attention *itself* drives the long-context gains is not fully supported by the best-performing configuration.

### Minor

2. **Long-context benchmarks compared only against vanilla RoPE.** ALiBi, FoPE, and Pythia are evaluated only on short-context tasks (Table 1). While RoPE is the dominant position embedding in long-context LLMs and the paper's comparison strategy is defensible, the claim that "RoPE++ outperforms other position embeddings on long-context tasks" is not directly tested. A comparison against ALiBi (designed for length extrapolation) or FoPE on long-context benchmarks would strengthen the paper's conclusions.

3. **No uncertainty estimates or multiple seeds.** The margins on short-context tasks are small (averaging 0.5–0.9 pp). Without standard deviations or multiple seeds, it is impossible to assess whether these differences are statistically significant or within noise. While single-seed evaluation is common in LLM pre-training, the reported margins are small enough that this omission weakens confidence, especially for the short-context results.

4. **Noise-injection experiment (Figure 5e/5j) conflates sensitivity with scale.** Adding equal-σ Gaussian noise to real and imaginary attention scores and comparing the performance drop assumes the two score distributions have comparable scale. If imaginary scores are systematically larger (or smaller), equal noise would be proportionally more destructive to one component, making the conclusion that imaginary heads are "more dominant" premature. A head-ablation experiment (removing entire heads) or a normalized-noise experiment would be cleaner evidence.

5. **Experiments limited to 376M and 776M scales.** The paper claims relevance for "modern LLMs" but does not demonstrate the method at scales where long-context issues are most practically relevant (e.g., 1B+). A scaling discussion or a single experiment at 1B–2B would increase confidence.

### Trivial

6. Figure 2 caption and head-count descriptions are confusing on first read — the terms "halved" and "doubled" lack a clear reference point relative to the baseline GQA structure.

7. The negative sign for imaginary attention is justified in Section 3.2 but this justification is somewhat indirect and could be stated more clearly at first mention.

## Nice-to-Haves

- A controlled experiment comparing standard RoPE with 2H heads and a doubled W_o (matching RoPE++⸤EC⸥'s capacity) against RoPE++⸤EC⸥, to isolate the imaginary-attention effect.
- Training convergence plots (validation loss over training steps) for RoPE vs. RoPE++ to compare optimization dynamics.
- Wall-clock time measurements confirming the FlashAttention interleaving claim (Section 3.3).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about missing appendix content or references being absent.** The parser strips appendix sections; these exist in the original submission. (From harsh critic's "Missing Parts" and formatting-related complaints.)
- **Criticism that the method "cannot be independently verified" because models/tools are not released.** The paper states all code, checkpoints, and training configurations are publicly released (Reproducibility Statement). Per Hard Rules, we do not question the availability of cited/c claimed artifacts.
- **Criticism about typos, formatting, or "garbled text" issues.** These are parser artifacts, not author errors.
- **Criticism that "the paper's scope is too narrow" (studying only imaginary attention in RoPE).** This is the paper's stated contribution, not a scope violation.
- **Strength from Strength Finder about "the area is impactful" or "the problem is important".** These are generic and do not reference specific artifacts in the paper. Removed per filtering rules.
- **Strength from Strength Finder about "the method is principled" or "the framework is general".** Restatement of the paper's own claims without independent evidence.
- **Strength about "compatibility with FlashAttention" without empirical validation.** The strength cites a claim, not a demonstrated result. However, this appears to be the Strength Finder's error, so it is moved here.
- **Criticism that the paper "does not report error bars for long-context benchmarks."** This is covered in a retained weakness (point 3). The harsh critic's version about "multiple seeds needed" is retained; the specific phrasing about "large-scale benchmarks where single-run is the norm" is removed as it overstates the requirement.

## Novel Insights

The merged reviews surface one genuinely novel observation beyond the paper's own contributions: the attention-pattern analysis (Figure 5) showing that imaginary heads consistently attend globally while real heads focus locally provides mechanistic evidence for the claimed division of labor. The noise-injection experiment, though methodologically imperfect as noted, is a creative diagnostic that goes beyond standard ablation; with proper normalization it could be a broadly useful tool for analyzing whether a model component is functionally important.

The harsh critic correctly identifies that the W_o confound is the paper's most serious flaw, but the existence of the RoPE++⸤EH⸥ configuration — which delivers competitive results with *fewer* parameters — already provides *partial* evidence that the imaginary mechanism itself contributes. The unresolved question is exactly how much of the RoPE++⸤EC⸥ advantage comes from the extra capacity vs. the imaginary computation, which is a concrete and addressable experimental question.

## Suggestions

1. **Run a capacity-matched control:** Compare RoPE++⸤EC⸥ against standard RoPE with the same total head count (2H) and doubled W_o, but with all heads using real-only attention. If RoPE++⸤EC⸥ still wins, the imaginary-attention mechanism is cleanly validated.

2. **Add at least 2–3 seeds for the main comparisons** (Table 1 and Table 2) to provide error bars. Even a single additional seed would help assess variance.

3. **Normalize the noise-injection experiment** by measuring per-component score variance and scaling noise accordingly, or replace with a head-dropping ablation.

4. **Include ALiBi on at least the RULER benchmark** to calibrate whether the RoPE++ gains are meaningful relative to a fundamentally different position-embedding approach designed for length extrapolation.

5. **Provide training curves** (validation loss vs. tokens) for at least one model size to demonstrate that RoPE++ does not converge differently from RoPE.

## Calibration Anchors

| Path | Avg Score | Round/Query | Comparison |
|------|-----------|-------------|-----------|
| jp4pxKqCRW | 2.50 | R1-topic-low | Weak paper on RoPE extrapolation, rejected. Paper under review is substantially stronger. |
| ReccFdn4zE | 2.00 | R1-topic-low | Unrelated topic, very weak. Not comparable. |
| JO7k0SJ5V6 | 5.00 | R1-topic-mid | "Scaling Laws of RoPE-based Extrapolation" — similar topical proximity, accepted. Comparable quality: both have solid theoretical contributions but evaluation gaps. |
| GtvuNrk58a | 6.20 | R1-topic-mid | "Round and Round We Go" — stronger mechanistic analysis of RoPE on real 7B models. The paper under review is weaker on evaluation scale and rigor. |
| wXpSidPpc5 | 6.50 | R1-topic-mid | "CLEX" — strong experiments at larger scales (up to 7B). The paper under review is weaker on this dimension. |
| OhauMUNW8T | 5.25 | R1-topic-mid | "Wavelet-based Positional Representation" — accepted PE paper with similar scope and similar magnitude of empirical gains. Comparable overall. |
| eoln5WgrPx | 6.50 | R1-topic-mid | "Why Does Effective Context Length Fall Short?" — strong evaluation on models up to 70B. The paper under review has a more novel architectural contribution but smaller-scale experiments. |
| EytBpUGB1Z | 8.00 | R1-topic-high | "Retrieval Head Mechanistically Explains Long-Context Factuality" — exceptional paper. The paper under review is far from this tier. |
| VkqqZcofEu | 5.75 | R1-weakness-limited-baselines | "A Controlled Study on Long Context Extension" — controlled comparison of long-context methods. Similar issue of limited baselines but broader in scope. |
| E2RyjrBMVZ | 4.17 | R1-weakness-no-variance | Paper studying variance in benchmarks. The lack-of-variance weakness in the paper under review is recognized as a limitation that reduces score. |
| sIGWTd1DcW | 5.25 | R2 | "Contextual Position Encoding" — rejected despite decent scores. Novel PE idea with marginal improvements. Comparable to paper under review. |
| xHMMt7r3GW | 5.33 | R2 | "LieRE" — rejected PE extension for higher-dim inputs. Similar level of contribution. |

**Round 1 bracket:** The paper sits in the middle band (3.5–7.5), clearly above low-band papers with fundamental flaws but below top-band papers with exceptional evaluation.

**Narrowing:** Round 2 placed the paper solidly in the 4.5–5.5 range. The paper is comparable to "Scaling Laws of RoPE-based Extrapolation" (5.0, accepted) and "Wavelet-based Positional Representation" (5.25, accepted) in overall quality — novel contributions with clear limitations in evaluation completeness. The W_o confound is a real gap that prevents the paper from reaching the top of this band. The paper under review has stronger theoretical motivation than "Contextual Position Encoding" (5.25, rejected) and more comprehensive evaluation than "LieRE" (5.33, rejected), but its main confound is more severe than those in the accepted mid-band papers.

**What did the low-band anchors fail at, and does the paper share any of those failures?** The low-band anchors (scores 2–3) typically had fundamental methodological flaws, incoherent contributions, or evaluation protocols that could not support their claims. The paper under review does *not* share those failures — its core idea is coherent and theoretically grounded, and its evaluation design is sensible in most respects. The paper's main weakness (W_o confound) is a specific experimental gap rather than a fundamental flaw, which is why it sits in the mid-band rather than the low-band.

## Score and Decision

Based on the calibration anchors and the weaknesses identified, the paper is a solid mid-range submission with a genuinely novel idea and clean theory, but held back by a significant experimental confound (W_o in RoPE++⸤EC⸥) that undermines the strongest empirical claim. The paper would need to address this confound with a controlled experiment to be competitive for acceptance at a venue with a 5+ bar.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>