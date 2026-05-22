Now I have all the information needed to synthesize the review. Let me write the final consolidated review.

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending STVG from short clips (~20 seconds) to videos of 1-5 minutes, and proposes ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks and selection mechanisms. The model uses cascaded spatio-temporal decoders (rather than parallel). Experiments on newly extended benchmarks show ART-STVG significantly outperforms existing short-form STVG methods on long videos, while remaining competitive on short-form STVG.

## Strengths

- **First work on LF-STVG with new extended benchmarks.** The paper identifies a genuine gap—existing STVG benchmarks are limited to <1 minute clips—and creates the first evaluation suite for long-form STVG by extending HCSTVG-v2 validation videos to 1-5 minutes using original YouTube sources. This provides a reproducible foundation for future work.

- **Consistent and large-margin outperformance on long videos.** In Table 1, ART-STVG surpasses all four prior methods (TubeDETR, STCAT, CG-STVG, TA-STVG) on every metric across all five video lengths. The gains grow with video length: on 3-minute videos, ART-STVG achieves 23.0% m.tIoU vs. the best prior 14.2% (a 62% relative improvement); on 5-minute videos, 15.0% vs. 8.1%.

- **Ablations validate memory selection and cascaded design.** Table 2 shows temporal memory selection improves m.tIoU from 16.7% (no memory) to 23.0% (selected). Table 4 shows the cascaded decoder design (spatial then temporal) outperforms parallel (23.0 vs. 21.5 m.tIoU). These ablations provide direct evidence that the proposed mechanisms contribute beyond the autoregressive baseline.

- **Competitive performance on short-form STVG.** Despite its autoregressive design, ART-STVG achieves 59.2% m.tIoU and 39.2% m.vIoU on HCSTVG-v2 (Table 7), trailing the SOTA TA-STVG by only 1.2%/1.0%. This demonstrates the autoregressive approach does not sacrifice short-video performance.

- **Qualitative analysis confirms memory selection effects.** Figure 5 shows attention maps where spatial memory selection focuses the query on the target region, while without selection the attention is diffused. This visual evidence supports the ablation results.

## Weaknesses

### Fatal
None.

### Major

1. **Training-test domain mismatch is not adequately addressed.** The model is trained exclusively on 20-second clips (64 frames at 3.2 FPS) from HCSTVG-v2 and evaluated on 1-5 minute videos. The memory banks accumulate information over hundreds of inference frames but were never trained under conditions requiring long-term storage and retrieval. The paper states this setup explicitly (Sec. 4.1: "all methods including ART-STVG are trained exclusively on the HCSTVG-v2 training set"), and all baselines share the same limitation. However, this means the claimed ability to "handle long-term videos effectively" is demonstrated under a distribution shift the paper does not analyze. There is no study of how memory bank size scales, whether early memories are overwritten or diluted, or how the selection mechanisms degrade as the bank grows. Table 6 (training on 40-second videos) partially addresses this by showing ART-STVG still outperforms baselines, but 40 seconds is still far short of 5 minutes. **Why it matters:** The core contribution hinges on long-video capability, but the evaluation does not cleanly separate generalization from short training data vs. genuine long-video understanding.

2. **Confounding factors in contribution attribution.** The simple autoregressive baseline (without memory) outperforms all prior methods on 3-5 minute videos (e.g., 16.7 vs. 13.9 m.tIoU on LF-STVG-3min). This strongly suggests the autoregressive frame-by-frame design itself—which avoids the GPU memory bottleneck of processing all frames at once—is a major source of improvement. The ablations do show that memory and selection add gains (16.7→23.0 for temporal, 21.3→23.0 for spatial), but without a non-autoregressive variant using the same backbone (e.g., a parallel decoder with the same encoder), it is impossible to isolate how much of the overall improvement over prior work comes from the autoregressive framework vs. the memory mechanisms. **Why it matters:** The paper's claimed contributions (memory selection, cascaded design) cannot be cleanly separated from the baseline autoregressive design, making the novelty attribution ambiguous.

3. **Absolute performance is very low on longer videos, with no failure analysis.** On 5-minute videos, ART-STVG achieves m.tIoU = 15.0%, m.vIoU = 10.0%, and vIoU@0.5 = 11.4%. While these exceed baselines (7.7-8.1%), they are near-floor in absolute terms. The paper does not discuss whether predictions at these thresholds are meaningful for any real application. No failure case analysis or qualitative prediction timelines on long videos are provided, making it hard to assess whether the model is learning meaningful grounding or exploiting shallow correlations. **Why it matters:** Without understanding failure modes, the reader cannot judge whether the method is a genuine step toward solving LF-STVG or merely less-bad-than-chance.

### Minor

1. **Spatial memory selection shows only modest gains.** Table 3 shows spatial memory selection improves m.tIoU from 21.3% (no memory) to 23.0% (selected), with selection contributing only 0.9 points beyond using all memories. Table 5 further shows the number of selected spatial memories (Ns=16/32/48) has minimal impact (range 0.5 m.tIoU). This weakens the claimed importance of the spatial selection mechanism.

2. **No statistical significance or variance reported.** All results are reported as single-run point estimates without error bars or confidence intervals. Given the low absolute numbers and likely high variance on long videos, this makes it difficult to assess whether differences are meaningful.

3. **The temporal memory ablation baseline ("all memories") is misleadingly bad.** In Table 2, using all temporal memories (9.6%) is substantially worse than no temporal memory (16.7%), likely because irrelevant event information overwhelms the decoder. The paper highlights the ❷→❸ gain (9.6→23.0, +13.4 points), but this comparison inflates the value of selection by contrasting against an artificially degraded configuration. The more meaningful gain is ❶→❸ (16.7→23.0, +6.3 points), which is still positive but smaller.

### Trivial
None.

## Nice-to-Haves

- A sliding-window baseline that applies a short-form STVG model (e.g., TA-STVG) on overlapping windows of ~20 seconds and merges predictions would test whether the autoregressive memory is actually better than a trivial extension of existing methods.
- Training and evaluation on videos of matching length (e.g., train on 3-min videos and test on held-out 3-min videos) would remove the distribution shift concern.
- Analysis of memory bank behavior over time—size growth, forgetting patterns, selection mechanism degradation—would strengthen the claim that the model truly handles long-term context.

## Removed Points

- **"No qualitative examples" (Harsh Critic):** The paper includes attention map visualizations in Figures 5 and 6. While there is no end-to-end prediction timeline on a full 5-minute video, the paper does provide qualitative evidence. **Reason:** Partially factually incorrect—the paper does have qualitative examples, though they are limited.
- **"No discussion of why extension not validated with metrics":** This is a minor point but reasonable to keep as a nice-to-have; moved to Nice-to-Haves. **Reason:** Scope creep for a first paper on this task.
- **Strength Finder claim about "13.4-point gain":** The 13.4-point gain is from comparing against the "all memories" baseline (❷), which is worse than "no memory" (❶). The gain from no memory to selected is 6.3 points, still substantial. **Reason:** The claim is factually correct but misleading in framing; demoted to note in Minor weakness #3.

## Novel Insights

The most interesting observation emerging from the reviews is that the simple autoregressive baseline (no memory) outperforms all prior non-autoregressive methods on videos longer than 2 minutes. This suggests that for long-form STVG, the bottleneck may not be sophisticated memory mechanisms but rather the fundamental inability of parallel frame-processing methods to handle many frames. If this holds, the main contribution of this paper may be less about memory selection and more about demonstrating the effectiveness of autoregressive design for long-video grounding—a point the paper itself does not fully emphasize. Future work should investigate whether even simpler streaming designs (e.g., per-frame detection with temporal smoothing) can match or exceed the memory-augmented approach.

## Suggestions

1. Train all methods (including ART-STVG and baselines) on 2-3 minute videos and evaluate on held-out long videos to eliminate the training-test length mismatch. This is the single most important experiment to validate the core claims.
2. Add a non-autoregressive variant of ART-STVG (same backbone, parallel decoder) to isolate the benefit of the autoregressive design from the memory mechanisms.
3. Include a sliding-window baseline that applies TA-STVG on 20-second windows.
4. Report error bars (at least 3 runs) for all main results.
5. Provide qualitative prediction timelines for a full 5-minute video with ground-truth comparisons and failure case analysis.

## Score and Decision

**Calibration anchors** (from retrieval batch):

| Anchor | Avg Score | Comparison to This Paper |
|--------|-----------|-------------------------|
| TA-STVG (WOzffPgVjF) | 7.50 | Stronger: clean evaluation, clear SOTA on standard benchmarks, no training-test mismatch |
| LangRepo (O8FkMqNF1M) | 5.50 | Comparable: both have evaluation concerns, this paper's relative improvements are larger but evaluation protocol is more questionable |
| Motion-Grounded Video (tEei1bolt3) | 5.00 | Comparable: both introduce new task+benchmark with reasonable but imperfect evaluation |
| AMViT (1DEHVMDBaO) | 4.60 | Slightly weaker: marginal gains vs. this paper's larger relative improvements |
| LVBench (uHgVrGF2Wn) | 4.50 | Comparable quality but different contribution type (pure benchmark vs. method+benchmark) |
| Grounded Video Caption (xYzOkOGD96) | 3.83 | Weaker: had severe novelty overclaim issues; this paper's contributions are more clearly scoped |
| ARVideo (hWlCc7Iksi) | 3.40 | Weaker: marginal improvements and limited novelty; this paper has clearer problem framing and larger gains |

This paper addresses a meaningful gap (first LF-STVG work, new benchmarks) and shows consistent relative improvements. However, the training-test domain mismatch and confounding factors in contribution attribution are significant concerns that prevent acceptance at the ICLR bar in current form. Positioned relative to anchors, the paper falls between medium-scored papers (~5.5) and lower-scored ones (~3.8-4.6)—closer to the former due to its genuine contributions but pulled down by the evaluation concerns.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>