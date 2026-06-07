Now I have a well-calibrated view. Let me compile the final review.

**Bracket analysis:**

Round 1 bracket: **4.5–6.5** — ART-STVG sits between the Adaptive Memory Mechanism (4.60, memory bank for video but marginal gains, limited baselines) and TRACE (6.75, temporal grounding with causal modeling, complete method description, multiple benchmarks).

Round 2 narrowing: ART-STVG is comparable to WSTVG (5.50, accept, similar STVG domain with methodological gaps but genuine contributions), ResidualViT (5.75, reject, temporal video grounding with efficiency focus), and VAP (5.80, reject, long-form video understanding with novel frame selection). ART-STVG has stronger ablation studies than all of these but shares similar methodological description gaps. It is clearly below TRACE (6.75) and Norton (8.00).

Final score: **5.5**.

---

## Summary
This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG) — extending STVG to videos of 1–5 minutes — and proposes ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks and a cascaded decoder. The method outperforms existing STVG methods on extended LF-STVG benchmarks while remaining competitive on short-form STVG.

## Strengths
- **Clear identification of a genuine gap and well-scoped problem formulation**: The paper convincingly establishes that existing STVG methods target 20–35 second videos and fail on longer videos, both computationally and in accuracy. The LF-STVG formulation is well-motivated (Section 1, lines 15–31) and the paper is the first to address it.
- **Strong and consistent empirical superiority on LF-STVG**: ART-STVG consistently outperforms TubeDETR, STCAT, CG-STVG, and TA-STVG across all five extended benchmarks (1–5 min), with the performance gap widening as video length increases — e.g., 15.0 vs 7.7–8.1 m.tIoU at 5 min (Table 1e). The trend is clearly visualized in Fig. 2.
- **Compelling ablation demonstrating memory selection is essential**: Table 2 cleanly isolates the effect: using all temporal memories degrades performance from 16.7% to 9.6% m.tIoU (vs. no memory), while selective memory raises it to 23.0% — a 13.4-point swing that validates the core design.
- **Cascaded decoder yields measurable gains**: Table 4 shows the cascaded spatio-temporal design outperforms the parallel alternative by 1.5% m.tIoU and 1.4% m.vIoU, supporting the claim that spatial target cues assist temporal localization.
- **Competitive SF-STVG performance**: Despite the autoregressive design targeting long videos, ART-STVG achieves 59.2 m.tIoU on HCSTVG-v2, only 1.2 points behind the best existing method (TA-STVG at 60.4, Table 7), showing the method does not sacrifice short-form capability.

## Weaknesses

### Fatal
None.

### Major
- **Loss function and tube construction absent from the main paper (Section 3.5)**: Section 3.5 is two sentences and defers the entire loss function to supplementary material. The model outputs per-frame bounding boxes ($b_i$) and per-frame start/end probabilities ($h_i^s, h_i^e$), but the main paper never describes how per-frame predictions are supervised (what loss, what ground-truth alignment) or how they are aggregated into a spatio-temporal tube at inference time for computing m.tIoU/m.vIoU. This is central to evaluating whether the model actually solves STVG rather than a per-frame approximation of it.
- **Autoregressive temporal prediction is in structural tension with event boundary detection**: The model predicts per-frame start/end probabilities using only past information (causal constraint). Determining that a frame is the *end* of an event typically requires knowing the event does not continue — information only future frames provide. The temporal memory selection (adjacent-memory similarity for event boundaries, Section 3.4) partially mitigates this but operates on past information only. The paper neither acknowledges nor analyzes this limitation, and the low absolute m.tIoU scores (23.0% at 3min, 15.0% at 5min) may partly reflect this structural constraint.
- **How existing methods handle long videos at test time is unspecified**: TubeDETR, STCAT, CG-STVG, and TA-STVG were designed to process all frames simultaneously. For a 5-minute video at 3.2 FPS (~960 frames), this may exceed their architectural capacity. The paper does not describe whether frames were subsampled, whether a sliding window was used, or whether models ran out of memory. This makes the comparison partially uninterpretable as evidence for the autoregressive approach's superiority.
- **Benchmark extension methodology under-described**: The paper extends HCSTVG-v2 validation videos from 20 seconds to 1–5 minutes (Section 4, lines 196–200) but does not clarify how annotations are handled — does the annotation remain a 20-second target window embedded in a longer video, or are temporal boundaries re-annotated? The number of validation samples per extended benchmark is also not reported, nor whether the extended benchmarks will be released.

### Minor
- **Figure 2 uses undefined metrics**: Figure 2 displays m_Ap@1 and m_Ap@5, which are never defined in the main paper and differ from the metrics used in all tables (m.tIoU, m.vIoU, vIoU@R). The relationship between m_Ap and the table metrics is unexplained.
- **Inconsistent vIoU thresholds**: Table 1 reports vIoU@0.5 and vIoU@0.7, while Tables 2–6 report vIoU@0.3 and vIoU@0.5. This inconsistency across main results and ablations is confusing.
- **Deconcatenation rationale unexplained (Section 3.1)**: After fusing appearance, motion, and text features via self-attention, the model deconcatenates them back into separate features for different decoders (line 90). This seems to partially undo the fusion, yet the rationale is not discussed.
- **Computational advantage claimed without quantification**: The paper asserts that processing all frames at once causes "computational bottlenecks" and that ART-STVG "resolves the computational bottleneck" (Section 1, line 32), but no memory or latency measurements are provided.
- **No error bars or variance reported** for any result.
- **No limitation section**: The autoregressive constraint on temporal boundary detection, unbounded memory growth, and low absolute performance on long videos are not discussed as limitations.

## Nice-to-Haves
- An experiment comparing ART-STVG with a variant that has access to a limited future window (e.g., 1–2 seconds) would quantify how much the causal constraint costs in temporal localization accuracy.
- A plot of GPU memory / latency vs. video duration for ART-STVG and at least one existing method would substantiate the claimed computational advantage.
- Clarifying whether the extended benchmarks will be released alongside code and models.
- Describing the memory bank's scaling behavior — how inference time grows with video length.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic: "The paper cites VidSwin but the precise version and pretraining are not specified beyond 'tiny'"** — Removed. The paper specifies "VidSwin-tiny" (line 78, Section 4 Implementation), which is sufficient specification for a standard backbone.
- **Strength Finder: "The baseline ablation cleanly separates architectural contributions" and "Fair experimental protocol" and "Memory selection strategies are simple, principled"** — These are supporting details that are captured within the core strengths; not listed separately to avoid redundancy.
- **Strength Finder: "Fair experimental protocol for long-form evaluation"** — This is a supporting detail folded into the empirical results strength.

## Novel Insights
The autoregressive causal constraint is in fundamental tension with the event-boundary detection required for temporal grounding. The temporal memory selection mechanism (adjacent-memory similarity for event boundary detection, inspired by TextTiling) is a creative mitigation, but the paper's framing of low absolute scores as "strong" because they beat baselines obscures a potentially important limitation of autoregressive approaches to STVG. Quantifying this trade-off would be a valuable contribution to the community.

## Suggestions
- Move the loss function (even a compact equation) and a brief description of tube construction into the main paper.
- Acknowledge and discuss the autoregressive temporal prediction limitation explicitly in a limitations section.
- Describe exactly how existing methods were run on long videos at test time (subsampling? sliding window? full-frame?).
- Clarify the benchmark extension: how many samples per length, how annotations were handled, and whether the benchmarks will be released.
- Unify the vIoU thresholds across all tables or explain the rationale for different thresholds.
- Define m_Ap in the main paper or replace Figure 2 metrics with those used in the tables.

## Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| LVM-NET (bEvI30Hb2W) | 3.00 | R1 | Clearly weaker — limited evaluation, simpler method |
| ARVideo (hWlCc7Iksi) | 3.40 | R1 | Weaker — self-supervised pretraining, different task |
| Adaptive Memory Mechanism (1DEHVMDBaO) | 4.60 | R1 | Weaker — marginal improvements, limited baselines, missing SoTA |
| Motion-Grounded Video Reasoning (tEei1bolt3) | 5.00 | R2 | Weaker — similar new-task contribution but less developed evaluation |
| WSTVG CoSPaL (yHj6EunfVQ) | 5.50 | R2 | Comparable — similar STVG domain, methodological gaps, accepted |
| ResidualViT (QWDFOOoV3U) | 5.75 | R2 | Comparable — temporal grounding, efficiency focus, similar gaps |
| VAP (KtqZrNjvjd) | 5.80 | R2 | Comparable — long-form video, novel method, similar issues |
| CG-Bench (le4IoZZHy1) | 6.20 | R2 | Stronger — benchmark contribution, more thorough evaluation |
| TRACE (14fFV0chUS) | 6.75 | R1/R2 | Clearly stronger — complete method, multiple benchmarks, accept |
| Norton (9Cu8MRmhq2) | 8.00 | R1 | Much stronger — excellent presentation, multiple tasks, clear accept |

Round 1 bracket: **4.5–6.5**. Round 2 narrowed to **5.0–6.0**. ART-STVG is comparable to the WSTVG paper (5.50) and ResidualViT (5.75) — similar in contribution quality and methodological gaps — but the missing loss function from the main paper is a notable weakness that pulls it toward the lower end of this range.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>