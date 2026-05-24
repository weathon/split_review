Now I have all the information needed. Let me produce the final consolidated review.

## Summary
This paper introduces the problem of Long-Form Spatio-Temporal Video Grounding (LF-STVG) — localizing a target in both space and time from videos lasting 1-5 minutes rather than the typical <1 minute. The authors propose ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks and selective memory retrieval, plus a cascaded spatio-temporal decoder that uses spatial predictions to inform temporal localization. On extended versions of HCSTVG-v2 (1-5 minutes), ART-STVG consistently outperforms prior methods (TubeDETR, STCAT, CG-STVG, TA-STVG), with margins growing from ~1% on 1-minute videos to ~7% on 5-minute videos. The method also achieves competitive results on short-form STVG.

## Strengths
- **First work to systematically study long-form STVG and propose a dedicated architecture.** The paper clearly identifies the scalability limitation of existing methods that process all frames at once, and the autoregressive streaming design is a well-motivated alternative for longer videos. The introduction of extended LF-STVG benchmarks (1-5 minutes) from original YouTube source videos fills an existing gap in the evaluation landscape.
- **ART-STVG consistently and substantially outperforms prior methods across all long-video settings.** Table 1 shows ART-STVG achieving 39.1% vs. 38.4% (TA-STVG) on 1-minute videos, and the gap widens to 23.0% vs. 14.2% (CG-STVG) on 3-minute videos and 15.0% vs. 8.1% on 5-minute videos. Figure 2 shows the gap grows monotonically with video length, supporting the claim that the autoregressive design is better suited to long-form processing.
- **Ablation studies cleanly isolate the contribution of each component.** Table 2 shows selective temporal memory raising m.tIoU from 9.6% to 23.0% (13.4 ppt gain) compared to using all memories. Table 3 shows spatial memory selection adding 0.9% beyond using all spatial memories. Table 4 shows the cascaded decoder design outperforming a parallel design (23.0% vs. 21.5% m.tIoU). These controlled experiments directly validate the design choices.
- **Competitive short-form STVG results despite the autoregressive architecture.** Table 7 shows ART-STVG at 59.2% m.tIoU on HCSTVG-v2, outperforming most existing methods and trailing only TA-STVG (60.4%) by 1.2%. This demonstrates that the autoregressive design does not sacrifice performance on the standard short-video benchmark.

## Weaknesses

### Fatal
None. The issues raised by the harsh critic are documentation gaps and experimental underspecifications, not fundamental flaws that invalidate the core claims.

### Major
- **The extended LF-STVG evaluation protocol is critically underspecified.** The paper extends HCSTVG-v2 validation clips to 1-5 minutes using original YouTube source videos (lines 254-258) but never states how ground-truth spatio-temporal tubes are obtained for the extended portions. The original HCSTVG-v2 annotations cover only 20-second clips. Since the annotations for the extended parts of the video are essential for computing m.tIoU and m.vIoU, this omission makes the evaluation difficult to reproduce or verify independently. The likely interpretation is that the original 20-second ground truth is reused within the longer timeline (the event only occurs once), but this must be stated explicitly and the metric implications discussed.

- **The inference protocol for baseline methods on long videos is not described.** Current STVG methods (TubeDETR, STCAT, CG-STVG, TA-STVG) are designed to process all frames in one forward pass. At 3.2 FPS, a 5-minute video requires ~960 frames, which exceeds standard GPU memory for these models. The paper does not state whether baselines used sliding windows, frame subsampling, the same 64 training frames, or other adaptations. Without this information, the comparisons in Table 1 may reflect asymmetric temporal coverage rather than genuine architectural advantages. Table 6 (training on 40-second videos) partially mitigates this concern but does not address the 1-5 minute inference setting.

### Minor
- **Training / test length mismatch limits the scope of the main results.** All methods are trained exclusively on 20-second clips and tested on 1-5 minute videos (line 264). This evaluates generalization under distribution shift rather than trained LF-STVG capability. Table 6 provides a partial remedy (training on 40-second videos confirms ART-STVG's advantage), but full-length training on 1-5 minute videos would strengthen the central claim. The paper would benefit from acknowledging this scope limitation explicitly.
- **The "baseline" architecture is deferred to supplementary material.** While page limits make this understandable, the main text should give a brief architectural sketch of the baseline (ART-STVG without memory/selection) for self-contained reading.

### Trivial
None.

## Nice-to-Haves
- Report GPU memory usage of ART-STVG vs. baselines on long videos to quantitatively support the computational bottleneck motivation.
- Provide more qualitative results (e.g., failure cases, temporal boundary predictions) to build intuition about when memory selection works or fails.
- Include a discussion of limitations (e.g., what happens if the target event appears in multiple distinct segments).

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh critic's claim that missing GT annotation is "fatal" and "invalidates the paper's central experimental contribution" — this is an overstatement. The GT naturally transfers from the original 20-second clips within the longer YouTube videos. The evaluation is interpretable, just underspecified in documentation.
- Harsh critic's claim about "the low values suggest models are not locating the event well" — m.tIoU of 15% on 5-minute videos is a reasonable absolute performance level given the difficulty of the task; the relative comparison is what matters.
- Harsh critic's concern about "vIoU@R for frames outside the original 20 seconds" — this is speculation; spatial ground truth would only apply to frames within the annotated event interval.
- Strength Finder's mention of "only slightly trailing TA-STVG" on short-form STVG as a major strength — this is a real result but it's competitive rather than superior, and slightly overclaimed.
- Harsh critic's demand for "inter-rater agreement" and other detailed annotation statistics — the manual review process described is appropriate for a benchmark extension.
- Any criticism about missing appendix content, release status of code/models, or references — these are parser artifacts or outside the paper's scope.

## Novel Insights
The most informative observation from combining the reviews is that the paper's claimed performance advantage on LF-STVG is supported by two independent forms of evidence: the gap grows monotonically with video length (Table 1, Figure 2), and the ablation studies show that the gap is primarily driven by the memory selection mechanisms rather than just the autoregressive structure. The latter point is not made explicit in the paper but is strongly suggested by the baseline performance: the memory-free autoregressive baseline (30.1% on 1-min, 23.0% on 2-min, 16.7% on 3-min) actually underperforms TA-STVG (38.4%, 25.3%, 13.9%) on shorter lengths, while the full ART-STVG with memory selection outperforms TA-STVG across all lengths. This suggests the memory selection mechanisms — not autoregression alone — are the primary source of improvement.

## Suggestions
1. **Explicitly describe the ground-truth reuse for extended videos.** State that the original 20-second spatio-temporal annotations from HCSTVG-v2 are used as ground truth within the longer timelines, and clarify how metrics are computed (e.g., whether frames outside the annotated interval are penalized or ignored for spatial metrics).
2. **Specify the inference protocol for each baseline method on long videos.** Report how many frames each baseline processes, whether sliding windows or frame subsampling is used, how predictions are aggregated, and GPU memory consumption. This is essential for establishing fair comparison.
3. **Add a limitation section** acknowledging that the main evaluation measures generalization from short to long videos, and that full-length training experiments (beyond the 40-second setting in Table 6) would further strengthen the claims.
4. **Briefly describe the baseline architecture in the main text** rather than deferring entirely to the supplementary material, since the baseline comparison is central to the ablation story.

## Score and Decision

### Calibration Summary

**Round 1 (Bracketing):** I queried three bands:
- Query A (score < 3.5) returned papers avg 3.0–3.4 — these are withdrawn/rejected papers with major flaws. The paper under review is clearly stronger.
- Query B (score 3.5–7.5) returned papers avg 4.25–7.0 — these are mixed borderline-to-accept papers.
- Query C (score > 7.5) returned papers avg 7.6–8.0 — these are oral/spotlight papers. The paper under review is not at this level.

**Initial bracket: [4.0, 6.5]**

**Round 2 (Narrowing):** I focused on 4.5–6.5 and 3.5–5.5:
- ResidualViT (5.75, Reject): Scores 6,6,8,3. Solid efficiency contribution but rejected on novelty and experimental concerns. The paper under review has a clearer contribution (first to tackle LF-STVG) but more significant documentation gaps.
- Understanding Long Videos (5.67, Accept Poster): Scores 5,6,6. Training-free approach for long video QA with missing comparisons. Accepted despite limitations. The paper under review has stronger architectural novelty but weaker documentation.
- Grounded-VideoLLM (4.25, Withdrawn): Scores 3,5,3,6. Limited novelty despite decent experiments. The paper under review has stronger novelty.
- CinePile (5.33, Reject): Scores 5,5,6. Dataset contribution with robust creation pipeline but rejected.

The paper under review has clear architectural novelty (first LF-STVG method, memory selection, cascaded decoder), extensive ablations, and competitive results. However, the missing experimental documentation (GT annotation protocol, baseline inference setup) are significant gaps that would require clarification during review. The paper is comparable to the stronger anchors in the 5.0–5.5 range but below the accepted poster at 5.67 due to the documentation completeness issues.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>