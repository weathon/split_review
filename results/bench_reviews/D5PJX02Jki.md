Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper proposes RoPE++, which re-incorporates the previously discarded imaginary component of the complex-valued RoPE attention score as a parallel set of attention heads. The method comes in two configurations: RoPE++EC (doubled heads, equal KV cache) and RoPE++EH (equal heads, halved KV cache/QKV parameters). The authors derive a characteristic curve showing the imaginary attention favors long-range dependencies, and validate empirically at 376M–1.5B scales across short- and long-context benchmarks, with consistent gains over standard RoPE.

## Strengths

- **Elegant core idea with theoretical motivation**: The paper identifies a genuinely overlooked aspect of RoPE — the discarded imaginary component of the complex dot product — and shows through the characteristic curve (Eq. 5, Figure 1) that the imaginary attention has a slow-decaying profile favoring long-range dependencies. The derivation that imaginary attention reduces to a \(-\pi/2\) rotation of queries followed by standard RoPE is clean and principled.

- **Practical efficiency benefits (RoPE++EH)**: RoPE++EH halves KV cache and QKV parameters while matching or surpassing vanilla RoPE on short-context tasks (Table 1: e.g., 376M avg 40.3 vs 40.1 RoPE; 1.5B avg 43.6 vs 42.9 RoPE) and delivering measurable memory/throughput gains (Figure 4). This is an independently valuable contribution — even if the imaginary component were only a reparameterization trick, the compression result stands on its own.

- **Consistent long-context improvements for RoPE++EC**: On RULER and BABILong (Table 2), RoPE++EC delivers substantial gains at 376M (RULER avg 25.0 vs 18.8; BABILong avg 16.1 vs 11.0) and maintains advantages at 64k context lengths. These benefits persist across different extension methods (NTK, PI, YaRN; Table 3).

- **Generality and practical integration**: The method integrates with FlashAttention, works with standard long-context training recipes, and is validated at three model scales (376M, 776M, 1.5B) with training convergence checks (Appendix C, Tables 7–9). Code and checkpoints are publicly released.

## Weaknesses

### Fatal
None.

### Major

- **Missing capacity-matched baseline for RoPE++EC**: RoPE++EC doubles the number of attention heads (and the output projection size \(W_o\)) relative to standard RoPE, yet no experiment controls for this increase. A comparison against standard RoPE with \(2\times\) heads and independent query/key projections would isolate whether the gains stem from the imaginary formulation or simply from additional capacity. The RoPE++EH variant provides a partial control (equal heads, halved cache), but its long-context results are mixed (e.g., BABILong at 776M: 19.4 vs RoPE 22.8; 1.5B RULER: 31.0 vs 35.1), so it cannot fully carry the burden of proving the imaginary component drives the RoPE++EC gains. Without this baseline, the paper's central claim — that the imaginary part specifically improves long-context modeling — remains incompletely demonstrated.

### Minor

- **Short-context gains are small and of unclear reliability**: Many of the claimed improvements are 0.2–1.0 points averaged over 11 heterogeneous benchmarks (e.g., 376M Short: RoPE++EH 40.3 vs RoPE 40.1; 776M Short: RoPE++EH 42.5 vs RoPE 42.0). Results come from single training runs with no standard deviations or confidence intervals reported. While single-run evaluation is common in pretraining papers at this scale, the small margins make it difficult to distinguish signal from noise, especially given that some individual benchmark scores fluctuate substantially across configurations.

- **Noise-injection experiment provides only suggestive evidence (Section 5.2)**: The conclusion that imaginary attention plays "a more dominant role in long-context modeling" rests on observing larger RULER-4k score drops when Gaussian noise is added to imaginary vs. real heads. The experiment uses equal standard deviation across branches without normalizing for potential differences in attention-score magnitude or variance between the two branches. The finding is directionally interesting but the gap could partially reflect differing numeric sensitivity rather than a genuine difference in functional importance.

### Trivial

- The 1.5B BABILong result for RoPE++EC (22.9 vs RoPE 29.5, Table 6) is a noticeable exception to the otherwise positive long-context trend and is not discussed in the main text.

## Nice-to-Haves

- A controlled experiment replacing the imaginary heads with an alternative fixed rotation (e.g., \(+\pi/4\)) while keeping the same parameter-sharing architecture would help disentangle whether the benefits come from the specific \(\sin/\cos\) combination or from the general architectural pattern of doubled query transformations on shared keys.
- A per-subtask breakdown of RULER performance (e.g., needle-in-haystack at various depths, multi-hop composition) would provide finer insight into where and why imaginary attention helps.
- Validation at ≥7B scale would strengthen the practical relevance claim, though the current 376M–1.5B range is reasonable for an ICLR submission.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Missing head-count-equivalent baseline is fatal"** (Harsh Critic #1): The paper has RoPE++EH which partially controls for capacity (equal heads, halved cache) and shows comparable or better performance. This baseline does not fully resolve the concern, which is why a weakened version appears as a Major weakness above, but it is not fatal — the paper has independent value through the efficiency results and the theoretical analysis.

- **Absence of statistical evidence as a blocking issue** (Harsh Critic #2): Single-run evaluation with no error bars is noted as a Minor weakness above, but the consistency across 3 model scales, multiple benchmarks, and training stages provides implicit signal. This is standard practice in pretraining papers at small-to-medium scale and does not block acceptance.

- **Uncontrolled noise-injection experiment** (Harsh Critic #3): Kept as a Minor weakness with reduced force — the experiment provides suggestive evidence, and the equal-σ approach is a reasonable starting point for an ablation study, though it could be more rigorous.

- **"The claim that omitted phase information necessarily hurts performance is not established"** (Harsh Critic, Abstract/Introduction note): The paper does not claim necessity; it claims "potential loss" (line 18), which is appropriately hedged. The theoretical analysis in Section 3.2 provides a plausible mechanism, not a proof of necessity. Removed as a strawman.

- **"Characteristic curve analysis relies on strong distributional assumptions... does not connect to any actual mechanism"** (Harsh Critic, Section 3.2 note): The i.i.d. assumptions are explicitly stated and standard for this type of expectation-based analysis (following Su et al., 2024 and Su, 2024b). The expectation-based framework is a legitimate analytical tool for understanding average behavior of positional embeddings. The connection to long-context retrieval is theoretical motivation, not a proven mechanism — and the paper treats it as such ("helping LLM retrieve," line 458). Weakened substantially; the theoretical derivation is a genuine strength, not a weakness.

- **"Efficiency argument is only evidence for parameter-sharing, not for sin/cos swap"** (Harsh Critic, Section 3.3 note): The paper does not claim efficiency as evidence for the imaginary component specifically. Section 3.3 describes efficiency as a property of the architecture, and the paper treats efficiency and long-context improvements as separate contributions. The efficiency argument supports the practical value of the architecture design; it does not need to prove the imaginary component is uniquely responsible. Removed.

- **"The extrapolation argument is incremental... does not provide usable zero-shot extrapolation"** (Harsh Critic, Section 3.4 note): The paper explicitly acknowledges in Appendix D.2 that "RoPE++ cannot directly extrapolate like FoPE" — this is presented as a minor observation, not a core contribution. Removed as mischaracterizing the paper's claims.

- **"Not compared with simply reducing the number of KV heads"** (Harsh Critic, Section 5.1 note): RoPE++EH is compared against RoPE directly. The fact that reducing KV heads in standard RoPE would also save cache is a fair question but goes beyond what the paper sets out to evaluate. The paper demonstrates that RoPE++EH achieves comparable or better results with halved cache — this is a valid efficiency claim regardless of whether other methods could also save cache. Removed as scope creep.

- **Strength Finder claim that noise-ablation confirms dominant role** (Strength Finder, Supporting #1): Kept but weakened — the evidence is suggestive, not confirmatory (see Minor weakness above). The overstated claim is removed; the experiment itself is noted in the main review.

- **"The paper investigates a concrete aspect of RoPE that has received little attention"** (Harsh Critic strengths): Kept as part of the Elegant core idea strength above.

- **"RoPE++EH demonstrates... intriguing efficiency/accuracy trade-off"** (Harsh Critic strengths): Kept as the Practical efficiency benefits strength above.

## Novel Insights

The most genuinely novel insight is not just the re-incorporation of the imaginary component, but the architectural observation that imaginary attention can be computed as a \(-\pi/2\) rotation of queries followed by standard RoPE with shared keys — enabling either a cache-halving configuration (RoPE++EH) or a head-doubling configuration (RoPE++EC) with no additional KV overhead. The characteristic curve analysis showing the imaginary attention approximates a sine integral with slow long-range decay provides a clean theoretical motivation that is new relative to prior RoPE analyses.

## Suggestions

- Add a RoPE baseline with matched head count (e.g., \(2\times\) heads, independent Q/K projections) for at least one model size to isolate the contribution of the imaginary component from additional capacity. This is the single most impactful experiment for strengthening the paper's core claim.
- Report at least one measure of variance (e.g., std over the 11-benchmark average, or a bootstrap confidence interval) to contextualize the small-margin improvements.
- Discuss the 1.5B BABILong exception (Table 6) in the main text — it is a notable deviation from the otherwise consistent long-context pattern and readers will notice it.

## Score and Decision

**Anchor comparison:**

- **MrRoPE** (`1J63FJYJKg.md`, avg 6.50, Oral): Stronger — unifying theoretical framework, training-free, comprehensive evaluation at 7B+ scale, large consistent gains. RoPE++ is clearly below this level.

- **Frayed RoPE** (`W8ZXfNaqku.md`, avg 6.00, Poster): Comparable in spirit (RoPE modification, from-scratch training at 1B/3B, RULER evaluation). Frayed RoPE has a more developed theoretical story (geometric perspective on sink tokens) but similar experimental scale. RoPE++ has efficiency benefits Frayed RoPE lacks. Roughly comparable; RoPE++ slightly below due to the missing capacity baseline.

- **Frequency Bands in RoPE** (`PR1PPxvG9Q.md`, avg 5.20, Poster): Weaker — primarily analysis-focused, perplexity-based, less practical impact. RoPE++ is above this level.

- **TAPA** (`U1xQiqTnBp.md`, avg 4.00, Reject): Weaker — limited evaluation (no RULER), questionable computational overhead, similar scale. RoPE++ is clearly above.

- **DroPE** (`RlPVSeKjoc.md`, avg 3.50, Accept Poster): Weaker — simpler idea, less rigorous evaluation, less comprehensive benchmarks. RoPE++ is clearly above.

The paper makes a genuine contribution with a simple, well-motivated idea that yields practical efficiency benefits and long-context improvements. The missing capacity-matched baseline is a real gap that prevents the strongest form of the central claim, but the paper has independent value through RoPE++EH's efficiency results and the theoretical analysis. Positioned between Frequency Bands (5.20) and Frayed RoPE (6.00), the paper merits a borderline-accept score reflecting both its genuine strengths and the experimental gap.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>