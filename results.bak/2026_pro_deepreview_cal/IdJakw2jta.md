Now I have thorough comparisons. Let me compile the final review.

**Calibration Summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| LVM-NET | 3.00 | R1 (low) | Weaker — limited benchmarks, marginal gains, rejected |
| ARVideo | 3.40 | R1 (low) | Weaker — methodology issues, rejected |
| AMViT | 4.60 | R1 (mid) | Weaker — marginal improvements, no SOTA, missing ablations |
| CoSPaL | 5.50 | R2 (mid-low) | Weaker — directly on STVG but unclear novelty, unfair comparison concerns |
| CG-Bench | 6.20 | R2 (mid) | Comparable — benchmark paper with documentation gaps, accepted |
| ARLON | 6.25 | R1+R2 (mid) | Comparable — good novelty, strong results, some documentation gaps, accepted |
| MotionAura | 7.33 | R2 (mid-high) | Stronger — more polished, multiple contributions, SOTA |
| Norton | 8.00 | R1 (high) | Stronger — thoroughly validated, no major gaps |

**Round 1 bracket:** 4.5–7.5. **Round 2 narrows to:** 5.5–6.5. The paper is comparable to ARLON (6.25) and CG-Bench (6.20) — good novelty and strong results with some evaluation documentation gaps. **Final score: 6.0**.

---

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new task that extends STVG to videos of several minutes, and proposes ART-STVG, an autoregressive transformer framework that processes frames sequentially using selective spatial and temporal memory banks with a cascaded decoder design. The authors extend the HCSTVG-v2 validation set to 1–5 minute videos and show ART-STVG substantially outperforms existing STVG methods, with performance gaps widening as video length increases. Comprehensive ablations validate each design choice.

## Strengths

- **Novel and well-motivated task formulation.** LF-STVG addresses a genuine gap between current STVG research (videos of 20–35 seconds) and real-world applications (minutes to hours). The paper provides clear motivation for why existing all-frames-at-once approaches fail for long videos (Sec. 1, Fig. 1–2).

- **Sound architectural design with validated components.** ART-STVG introduces three clearly motivated innovations: (1) autoregressive frame-by-frame processing to handle arbitrary video lengths, (2) selective spatial and temporal memory banks that filter relevant historical context (text-similarity selection for spatial memory, event-boundary detection for temporal memory), and (3) a cascaded decoder that routes fine-grained spatial predictions into temporal grounding. Each component is ablated (Tables 2–5) and shown to be causal to performance gains — e.g., temporal memory selection improves m.tIoU from 16.7% (no memory) to 23.0% on LF-STVG-3min.

- **Strong and consistent experimental results.** ART-STVG outperforms all baselines (TubeDETR, STCAT, CG-STVG, TA-STVG) across all five extended benchmarks (LF-STVG-1min through 5min) on all metrics (m.tIoU, m.vIoU, vIoU@0.5, vIoU@0.7). On LF-STVG-5min, ART-STVG achieves 15.0 m.tIoU vs. 8.1 (next best), a 6.9 point margin. The performance gap grows monotonically with video length (Fig. 2), directly validating the claim that the autoregressive design handles long videos better. The method also remains competitive on short-form STVG (59.2 m.tIoU vs. 60.4 SOTA on HCSTVG-v2).

- **Qualitative evidence supports the memory selection mechanisms.** Figure 5 shows spatial attention with selective memory focuses sharply on the described target while without it attention is diffuse; Figure 6 demonstrates temporal memory correctly segments videos into events and selects the event nearest to the current frame.

## Weaknesses

### Fatal
None.

### Major

- **Baseline inference protocol for long videos is not described.** The paper's central experimental claim — that ART-STVG handles long videos while existing methods fail — depends on the comparison in Table 1 and Figure 2. Yet the paper does not specify how existing all-frames-at-once models (TubeDETR, STCAT, CG-STVG, TA-STVG) were applied to videos of 1–5 minutes. At 3.2 fps, a 5-minute video contains ~960 frames; whether baselines processed all frames, were subsampled, or used a sliding-window protocol is unknown. This makes it impossible to assess whether the reported performance gaps reflect genuine architectural advantages or artifacts of how baselines were adapted to long inputs. The authors should describe the exact inference protocol for every baseline and ideally include a reasonable sliding-window baseline to show the gap is not due to length alone.

- **Temporal annotation alignment in the extended dataset is not explained.** The paper extends HCSTVG-v2 validation videos from ~20 seconds to 1–5 minutes using "original YouTube videos" but does not describe how the original temporal annotations (start/end times of target events) were positioned within the extended timeline. If the 20-second clip was simply padded, the temporal ground truth must have been shifted; the procedure for determining new start/end times and verifying correctness is absent. This is critical because tIoU and related temporal metrics depend directly on these annotations. The authors should clarify whether annotations were manually re-verified or mathematically shifted based on known clip positions in the source video.

### Minor

- **Loss function deferred to supplementary material.** Section 3.5 states the loss is described in supplementary material due to space. While acceptable in principle, understanding the optimization objective — particularly how temporal losses handle the full video vs. per-frame predictions — would strengthen the main-text presentation.

- **No runtime or memory measurements to support the "computational bottleneck" claim.** The paper argues that existing methods face "computational bottlenecks because of high GPU memory requirements" (Sec. 1) and that ART-STVG "resolves the computational bottleneck." No concrete measurements (peak GPU memory, inference time) are provided for any method on long videos. This claim is therefore asserted rather than demonstrated.

- **No discussion of autoregressive failure modes.** The autoregressive, memory-growing design could suffer from error accumulation or memory saturation over very long durations. The paper does not analyze whether performance degrades when the target event is temporally far from the current frame, or whether the memory-selection strategy has limits. Such discussion would demonstrate awareness of the method's boundaries.

### Trivial
None.

## Nice-to-Haves

- A sliding-window baseline for non-autoregressive methods would strengthen the fairness argument.
- Memory growth analysis (how many memories accumulate over a 5-minute video, and whether selection effectively controls this).
- Discussion of whether the cascaded design could propagate spatial errors into temporal predictions.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"GPU memory likely infeasible for baselines"** — The harsh critic speculated that processing ~960 frames in one forward pass is "likely infeasible" for baselines. This is speculative; the paper never reports attempting this and the critic does not have evidence. The real problem is the lack of protocol description, not a presumed failure. Removed as speculative.

- **"The temporal ground-truth alignment could invalidate all results"** — The harsh critic asserted this could "invalidate all results" and make them "meaningless." This is speculative catastrophizing. The paper uses original YouTube videos (not concatenated clips), suggesting clip positions in source videos are known. The issue is a documentation gap, not a demonstrated error. Removed as speculative escalation.

- **Strength Finder's generic strengths** — The strength finder included generic framings like "the idea is conceptually well motivated." These are already subsumed by the concrete strengths listed above.

- **Missing related work / missing appendix / formatting issues** — Standard parser artifacts or unsupported claims; removed per rules.

## Novel Insights

The paper reveals an important empirical pattern: autoregressive frame-by-frame processing with selective memory not only makes long-form STVG tractable but yields strictly better localization than all-frames-at-once processing, with the advantage growing as video length increases. This runs counter to the intuition that global context always helps — in long videos, the noise from irrelevant frames appears to overwhelm the signal, and selective temporal/spatial memory provides a better trade-off. This has implications beyond STVG for any video understanding task where the target event occupies a small fraction of the total duration.

## Suggestions

- Provide a complete account of how each baseline was run on long videos (frame sampling rate, whether all frames were used, any windowing or aggregation). If baselines cannot process all frames due to memory, describe the adaptation and justify its fairness.
- Clarify the temporal annotation alignment procedure for the extended dataset. If clip positions in source YouTube videos are known and annotations were mathematically shifted, state this explicitly. If manual re-annotation was performed, describe the procedure.
- Add a table reporting inference time and peak GPU memory for all methods on at least the 5-minute benchmark, to substantiate the computational bottleneck claim.
- Briefly discuss potential failure modes (error accumulation, memory saturation) to show awareness of limitations.

## Score and Decision

**Overall assessment:** This paper tackles a genuine and well-motivated extension of STVG to long-form videos and proposes a novel, carefully designed autoregressive framework. The methodological contributions (autoregressive processing, selective dual memory banks, cascaded decoder) are coherent and validated through thorough ablations. The experimental results are strong and consistent across five benchmarks of increasing difficulty. The two major weaknesses — undocumented baseline inference protocol and unexplained temporal annotation alignment — are documentation gaps that affect reproducibility and trust in the comparisons but do not appear to be errors. Both are addressable in a rebuttal. Compared to calibration anchors, this paper is comparable to ARLON (6.25) and CG-Bench (6.20) — solid contributions with some evaluation documentation gaps that were nonetheless accepted.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>