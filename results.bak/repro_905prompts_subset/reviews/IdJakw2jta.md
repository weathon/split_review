Now I have a solid calibration picture. Let me synthesize the final review.

---

## Summary

This paper introduces **Long-Form Spatio-Temporal Video Grounding (LF-STVG)** — extending STVG from short clips (~20s) to videos of 1–5 minutes — and proposes **ART-STVG**, an autoregressive transformer that processes frames one at a time with spatial and temporal memory banks and selective memory retrieval. A cascaded decoder design uses fine-grained spatial features to guide temporal localization. On five newly constructed benchmarks (LF-STVG-1min through 5min), ART-STVG substantially outperforms all prior STVG methods, with gaps widening as video length increases. The paper also shows competitive results on standard short-form STVG.

## Strengths

- **Consistent and growing improvements over prior methods on long videos.** Table 1 shows ART-STVG outperforming all four prior methods (TubeDETR, STCAT, CG-STVG, TA-STVG) across all five video lengths. The gap grows monotonically with video duration — e.g., on LF-STVG-3min ART-STVG achieves 23.0 m.tIoU vs. 13.9–14.2 for all competitors, and on LF-STVG-5min it achieves 15.0 m.tIoU vs. ≤8.1. This directly validates the core thesis that frame-by-frame autoregressive processing with memory is advantageous for long videos.

- **Memory selection strategies deliver large, well-controlled gains.** Ablations (Tables 2–3) show that using all temporal memories hurts performance (9.6 m.tIoU) vs. no memory (16.7), while the proposed selection raises it to 23.0 — a +13.4 point gain. Spatial memory selection adds a further 0.9 points. These controlled experiments cleanly isolate the contribution of selective memory, not just memory in general.

- **Cascaded decoder design yields clear benefits.** Table 4 compares parallel vs. cascaded spatio-temporal decoding; cascaded improves m.tIoU from 21.5 to 23.0 (+1.5) and m.vIoU from 13.9 to 15.3. The design is well-motivated and the ablation is clean.

- **Competitive on short-form STVG confirms generality.** On HCSTVG-v2 (short videos), ART-STVG achieves 59.2 m.tIoU / 39.2 m.vIoU, outperforming most prior dedicated short-form methods and falling only 1.2/1.0 points behind the top-performing TA-STVG (Table 7). This shows the autoregressive framework does not sacrifice short-video capability.

- **Multi-scale benchmark construction enables systematic analysis.** The extension of HCSTVG-v2's validation set to five distinct lengths (1 through 5 minutes) provides a controlled testbed that cleanly reveals how performance degrades for existing methods as video length increases, and how ART-STVG resists this degradation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Baseline evaluation protocol on long videos is underspecified.** The paper does not describe how existing methods (TubeDETR, STCAT, CG-STVG, TA-STVG) — all designed to process frames in one shot — were run on videos of 1–5 minutes. Whether they used subsampling, sliding windows, or full-frame processing is not stated. This does not invalidate the results (the consistent performance degradation with length is expected and the pattern is clear), but it is a reproducibility gap that should be filled. *(Found in Section 4.1, line 264: "all methods including ART-STVG are trained exclusively on the HCSTVG-v2 training set... for fair comparison" — the evaluation protocol itself is not described.)*

- **Temporal memory selection algorithm is underspecified.** The paper states that "points with lower similarities are considered as event boundaries" (Section 3.4) but provides no threshold, criterion for what counts as "lower," or precise mechanism for resolving "the event closest to current frame." While the conceptual idea is clear from Figure 4(b) and the TextTiling inspiration, the implementation is not reproducible as-is. *(Found in Section 3.4, lines 234–237.)*

- **Dataset annotation process for extended videos is sparse.** The paper states that the extended videos are "based on original YouTube videos, not concatenated clips" and were "manually reviewed to ensure quality," but does not describe how the ground-truth annotations (spatial tubes, temporal segments) were handled for the extended portions. Since the original videos are ~20s and the extensions are 1–5 min, it would be helpful to clarify whether the original annotations were simply kept (with the model needing to determine when the event occurs within the longer video) or whether new annotations were added. The former interpretation is reasonable and consistent with the task definition, but stating it explicitly would avoid ambiguity. *(Found in Section 4, lines 254–258.)*

- **No computational cost reporting.** The paper motivates ART-STVG partly by GPU memory constraints of full-video methods (Section 1), but never reports training/inference time, GPU memory consumption, or FLOPs for ART-STVG vs. baselines on long videos. Including such a comparison would quantitatively substantiate the computational motivation. *(Not reported anywhere in the main paper.)*

### Trivial
None that survive filtering (parser artifacts excluded).

## Nice-to-Haves

- A comparison to non-STVG long-video methods (e.g., memory-augmented transformers for action detection or video QA) adapted to STVG would further situate the work.
- An analysis of how spatial and temporal memory banks evolve over hundreds of frames — e.g., memory age vs. utilization, or whether early-frame memories are ever retrieved in long videos — would strengthen the intuition behind the memory design.

## Removed Points

- **Criticism about training–evaluation length mismatch (harsh critic point 2):** The paper trains all methods on 20s videos for fair comparison, then tests on longer videos. This is a standard evaluation paradigm for autoregressive/RNN-style models to test length generalization. Training all methods on the same data is the correct fairness baseline, and Table 6 separately investigates longer training. This is not a weakness.
- **Criticism about low absolute scores not being discussed:** Scores naturally drop for harder tasks (5-minute videos); the contribution is relative improvement, which is substantial and discussed.
- **Criticism about missing related work:** Cannot be verified and may be hallucinated.
- **Formatting/typo/style nitpicks:** Parser artifacts, not author errors.
- **Claim that the paper "should have retrained all methods on longer videos":** Already done in Table 6.

## Novel Insights

Beyond the paper's own contributions, the most striking finding is the *interaction* between memory selection and video length: using *all* temporal memories actually performs *worse* than using no memory at all (9.6 vs. 16.7 m.tIoU in Table 2), but the proposed selection strategy catapults performance to 23.0. This suggests that for long-video grounding, the challenge is not merely storing long-range information but *filtering out* irrelevant past information — a finding that could inform future work on memory-augmented video models regardless of architecture.

## Suggestions

- Specify how each baseline method was adapted to run on 1–5 minute videos (frame count, downsampling if any, GPU memory constraints). Even a brief one-sentence description per baseline would resolve the ambiguity.
- Provide the threshold or algorithm used for temporal event boundary detection in the memory selection mechanism, for reproducibility.
- State explicitly how ground-truth annotations were handled for the extended video portions — ideally confirming that the original event annotations were kept and the task is to localize that event within the longer video.
- Include a table or paragraph reporting inference time and GPU memory for ART-STVG vs. at least one baseline on the longest video setting.

## Score and Decision

**Round 1 bracket** (wide search): three queries on spatio-temporal video grounding across score bands. Weak anchors at ~3.0 (action recognition, anomaly detection — not directly relevant), middle anchors at 3.83–7.00 (ResidualViT at 5.75 Reject, Vinoground at 5.75 Reject, ARLON at 6.25 Accept, TRACE at 6.75 Accept, Autoregressive Video Imitators at 7.00 Accept), strong anchors at 7.75–8.50 (not closely comparable in topic). Initial bracket: **5.5–7.0**.

**Round 2 narrowing**: three queries inside the bracket. Compared against:
- ResidualViT (5.75, Reject) — underspecified training and evaluation, limited comparison. Current paper is clearly stronger.
- Vinoground (5.75, Reject) — benchmark-only, limited novelty. Current paper is stronger.
- ARLON (6.25, Accept) — similar use of autoregressive design for long video, but missing ablations. Current paper has more thorough experiments.
- AntGPT (6.25, Accept) — different task (action anticipation). Comparable contribution level.
- TRACE (6.75, Accept) — VTG with causal event modeling via LLMs. Current paper is comparable in thoroughness but lacks the LLM hook.

**Final score: 6.5**. The paper introduces a meaningful new task, proposes a clean method with thorough ablations, and shows convincing results. The underspecified baseline protocol and a few missing details prevent it from reaching the 7+ range but do not undermine its core claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>