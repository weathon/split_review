Now I have sufficient calibration context. Let me compile the final review.

## Summary

This paper identifies that standard RoPE implementations discard the imaginary component of the complex-valued attention score, and proposes RoPE++, which reincorporates this imaginary component as a separate group of attention heads. Two configurations are introduced: RoPE++\textsubscript{EH} (equal heads, halved KV cache) and RoPE++\textsubscript{EC} (equal cache, doubled heads). Theoretical analysis shows the imaginary attention's characteristic curve decays more slowly than real attention, enabling better long-context modeling. Experiments at 376M and 776M scales on short-context (11 benchmarks) and long-context (RULER, BABILong up to 64k) tasks demonstrate consistent improvements over vanilla RoPE, with the benefits widening at longer contexts.

## Strengths

- **Genuinely novel identification of an overlooked problem in RoPE**: The paper is the first to identify that standard RoPE discards the imaginary component of the complex-valued attention score, and to systematically analyze why recovering it helps long-context modeling. This is a principled architectural insight, not an incremental heuristic.

- **Theoretical analysis connecting imaginary attention to longer-range dependency capture**: Section 3.2 derives the characteristic curve of imaginary attention (sine integral, Equation 5) and shows it decays more slowly than the real attention's cosine integral (Figure 1). Section 3.4 further proves that imaginary attention exposes key dimensions to both negative and positive positional embedding values during pre-training, improving length extrapolation. This mathematical grounding goes beyond what typical position-encoding papers provide.

- **Strong and consistent empirical gains on long-context benchmarks**: RoPE++\textsubscript{EC} at 376M improves RULER average from 18.8 to 25.0 and BABILong average from 11.0 to 16.1 over vanilla RoPE (Table 2). At 776M, RULER average goes from 27.4 to 29.4. The gains are especially pronounced at 64k context (e.g., BABILong 376M: 12.8 vs 7.8). The improvement pattern is consistent across two model sizes, two benchmarks, and multiple context lengths.

- **Causal validation via attention perturbation**: The noise perturbation experiment (Figure 5) provides direct causal evidence — adding Gaussian noise to imaginary attention degrades RULER-4k scores by ~5 points (376M) and ~8 points (776M) more than the same noise applied to real attention — confirming that imaginary heads are functionally more important for long-context performance, not just correlated.

- **Generality across multiple context-extension techniques**: Table 3 shows RoPE++\textsubscript{EC} outperforms vanilla RoPE when combined with both Linear PI and YaRN (e.g., 776M YaRN RULER Avg: 34.4 vs 33.5), demonstrating the method's robustness beyond the NTK-based extension used in the main experiments.

## Weaknesses

### Major

- **RoPE++\textsubscript{EH} underperforms on several long-context settings, partially undercutting the "comparable performance" claim**: On 776M BABILong (Table 2), RoPE++\textsubscript{EH} averages 19.4 vs RoPE's 22.8 — a substantial 3.4-point drop. On 376M BABILong, EH (11.6) is only marginally better than RoPE (11.0). The paper claims EH "achieves comparable performance with vanilla RoPE using half the KV-cache," but this is not uniformly true for long-context tasks. The efficiency-performance trade-off should be stated more candidly.

- **Scale of evaluation is limited to 376M and 776M parameters**: While training from scratch at these sizes is reasonable, the community standard for position-encoding papers has shifted toward at least 1B+ validation. The STRING paper (6.5 avg score, ICLR) validated on 70B models; the "Round and Round" paper (6.2) on Gemma 7B. Without evidence that RoPE++ scales to 1B+, the practical impact of the method remains uncertain. The paper mentions "more analysis on larger model scale" is in Appendix C, but that appendix was stripped during extraction, so it cannot be evaluated.

- **Long-context evaluation only compares against RoPE, not against FoPE, Pythia, or ALiBi**: Table 2 (the main long-context results table) only includes RoPE as a baseline. The paper says "We highlight the comparison with RoPE in long-context training because RoPE is the position embedding currently most widely used," but this narrow comparison makes it impossible to assess whether RoPE++ is better than other PE alternatives in the long-context regime where it claims its main advantage.

### Minor

- **No discussion of the FLOPs cost for RoPE++\textsubscript{EC}**: While the EC configuration maintains equal KV cache size, it doubles the number of attention heads, which increases the FLOPs of attention computation proportionally. The paper discusses memory and TPOT (for EH) but does not quantify the training or inference FLOPs overhead for the higher-performing EC variant. A practitioner weighing the trade-off needs this information.

- **The characteristic curve analysis (Equation 5, Figure 1) assumes uniformly distributed query/key embeddings** and averages over frequencies. This is a standard simplification in the RoPE analysis literature, but the paper does not acknowledge this assumption's limitations — for example, it may not hold for trained models where embeddings learn task-specific distributions.

### Trivial

- None beyond typical parser artifacts.

## Nice-to-Haves

- Adding one experiment at the 1B–3B scale would substantially strengthen the paper's claims about scalability and practical relevance.
- Including FoPE and ALiBi in the long-context comparison (Table 2) would give a complete picture of where RoPE++ sits relative to the full PE landscape.
- Reporting standard deviations across multiple training runs would increase confidence in the reported improvements, especially for metrics where the gap is small (e.g., short-context averages).
- A brief analysis of where RoPE++ fails or underperforms would improve the paper's scientific rigor.

## Removed Points

The harsh critic did not provide any content. The Strength Finder's generic strengths (e.g., "this paper addressed an important problem") were removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Report the full long-context results with FoPE, Pythia, and ALiBi baselines in the main paper, not just in an appendix, to give readers a complete comparison.
- More clearly delineate where RoPE++\textsubscript{EH} loses versus vanilla RoPE (especially on BABILong 776M) and discuss the implications for practitioners choosing between EH and EC.
- Quantify the FLOPs overhead of RoPE++\textsubscript{EC} in the efficiency discussion, not just memory and latency.

## Score and Decision

**Round 1 bracket**: I queried three bands — weak (avg ≤ 3.5), middle (3.5–7.5), strong (≥ 7.5). The weak-band anchors (scores 2.5–3.0) are clearly worse than this paper. The strong-band anchors (all 8.0) are clearly better. This places the paper in the middle band.

**Round 2 narrowing**: I queried inside (5.0, 7.0) and examined anchors closely:
- STRING (6.5, ICLR Accept): Training-free, evaluated on 70B models, +10 points on RULER. More impactful empirically but less novel methodologically.
- PoSE (6.0, ICLR Accept): Training efficiency method, tested on LLaMA-scale models, clean contribution.
- "Round and Round" (6.2, ICLR Accept): Mixed reviews (8,5,8,5,5), strong analysis but weaker method contribution.
- Wavelet PE (5.25, ICLR Accept): Similar in being a novel PE design but marginal empirical gains.
- "Revisiting Positional Information" (6.33, Reject): Applied RoPE to vision with limited novelty.

**Comparison**: RoPE++ is stronger than the wavelet paper (5.25) in both theoretical depth and empirical magnitude. It is somewhat weaker than STRING (6.5) in terms of scale and immediate practical impact. It is roughly comparable to PoSE (6.0) — both have clear, novel contributions validated at moderate scale, with room for larger-scale confirmation. The paper's theoretical analysis and causal validation experiments are stronger than typical for this score range.

**Final score**: 6.0. The paper makes a genuinely novel contribution, provides solid theoretical grounding and empirical validation, but the limited scale of evaluation and the uneven performance of the EH configuration keep it from being a stronger paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>