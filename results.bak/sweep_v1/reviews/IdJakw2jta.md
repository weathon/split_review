Now I have sufficient calibration anchors. Let me produce the final consolidated review.

---

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG) as a new task and proposes ART-STVG, an autoregressive transformer that processes video frames sequentially (rather than all-at-once) with spatial and temporal memory banks and selective memory retrieval. The authors extend HCSTVG-v2's validation set from 20 seconds to 1–5 minutes (LF-STVG-1min through LF-STVG-5min). On these benchmarks, ART-STVG substantially outperforms existing STVG methods (e.g., +9.1 m.tIoU on 3-minute videos), and ablation studies isolate the contributions of each component. The paper also shows competitive results on short-form STVG.

## Strengths

1. **Large and consistent gains across all long-form video lengths.** Table 1 shows ART-STVG outperforms all four prior STVG methods (TubeDETR, STCAT, CG-STVG, TA-STVG) on all five LF-STVG benchmarks. The gap widens with video length (e.g., m.tIoU on LF-STVG-3min: 23.0 vs. 14.2 for the best prior method), consistent with the paper's claim that existing methods degrade in long videos.

2. **Ablations cleanly isolate each component's contribution.** Tables 2–3 show that removing either temporal or spatial memory selection degrades performance (temporal: 23.0 → 9.6 when using all memories; spatial: 23.0 → 21.3 without spatial memory). Table 4 shows the cascaded decoder design improves over parallel by +1.5 m.tIoU. These ablations provide controlled evidence that the specific proposed mechanisms are responsible for the gains.

3. **Structured extension of HCSTVG-v2 to long-form benchmarks.** The paper extends only the validation set from original YouTube videos (not concatenated clips), with manual quality review. This creates a reproducible evaluation setup for LF-STVG that the community can build on. The fact that all methods (including ART-STVG) are trained exclusively on 20-second videos and evaluated on 1–5 minute videos provides a clean test of generalization to longer videos.

4. **Clear visualization of the memory selection mechanism.** Figures 5 and 6 concretely show how spatial memory selection focuses attention on target regions and how temporal memory selection segments the video into events, providing intuitive support for the claimed mechanism.

## Weaknesses

### Major

1. **Missing details on how baselines were evaluated on long videos.** The paper compares against TubeDETR, STCAT, CG-STVG, and TA-STVG — all designed to process an entire video at once. For 1–5 minute videos at 3.2 FPS (192–960 frames), this would require prohibitive GPU memory. The paper states baselines were "trained exclusively on the HCSTVG-v2 training set" but does not specify the inference protocol: were frames subsampled? Was a sliding window used? Were the models truncated to a maximum frame count? Without this, readers cannot assess whether the reported baseline numbers reflect a fair deployment of these methods or a setup that inherently handicaps them. The paper should transparently describe the inference protocol for each baseline. *(Section 4, particularly the "Implementation" and "Datasets" paragraphs; Table 1)*

2. **Missing adapted baselines (e.g., sliding window).** The paper argues that existing STVG methods are "inapplicable" to long videos because they process all frames at once, but never tests whether a simple adaptation — e.g., sliding a 20-second window over the long video, running the baseline on each window, and merging predictions — would produce competitive results. This is the most obvious baseline and its absence weakens the claim that the autoregressive design is necessary rather than merely sufficient. Such an experiment would also clarify whether the observed performance gap is due to the autoregressive architecture per se or to the memory selection components. *(Section 1, Figure 1; Section 4.1)*

3. **Ground-truth annotation for extended videos not clarified.** The paper extends HCSTVG-v2 validation videos from 20 seconds to 1–5 minutes but does not explicitly state whether new ground-truth spatial bounding boxes and temporal event boundaries were annotated for the full duration, or whether evaluation uses only the original 20-second annotations. If the latter, predictions on frames/times outside the original annotation window have undefined ground truth, which would affect the interpretation of quantitative results. While all methods face the same evaluation (so the relative comparison is fair), the absolute numbers and the practical meaning of the metrics need clarification. *(Section 4, "Datasets" paragraph)*

### Minor

1. **No variance or statistical significance reported.** The validation set has 2,000 samples. The paper does not report standard deviations or confidence intervals for any metric. Given the large reported gaps (e.g., 23.0 vs. 14.2 m.tIoU on 3-minute videos), the core conclusions are unlikely to change, but the absence of variance estimates makes it impossible to assess which smaller differences (e.g., the 1.5% gain from cascaded vs. parallel decoder in Table 4) are significant. *(Section 4, Tables 1–7)*

2. **Absolute performance on long videos is modest.** ART-STVG achieves only 15.0% m.tIoU and 10.0% m.vIoU on 5-minute videos. While this is far better than baselines (~8% m.tIoU), the absolute numbers indicate that LF-STVG remains a very challenging task and the current approach captures only a fraction of the target events. The paper does not analyze what types of errors dominate (spatial mislocalization, temporal boundary errors, missed events, etc.). *(Table 1, rows for LF-STVG-5min)*

3. **Training on longer videos only explored up to 40 seconds.** The ablation in Table 6 extends training to 40-second videos, showing ART-STVG improves (28.3 vs. 23.0 m.tIoU on 3-minute evaluation). But this is still far from the 1–5 minute test setting. Training on genuinely long videos (minutes, not seconds) would directly validate whether ART-STVG benefits from longer training context — this is the most obvious next experiment and was not included. *(Section 4.2, Table 6)*

4. **Memory scalability not analyzed.** The memory bank grows linearly with video length (memories are added without removal). At 5 minutes and 3.2 FPS, this accumulates 960 frames × K memories per block. The paper does not report compute time, GPU memory footprint, or discuss potential saturation effects as video length increases further. *(Section 3)*

### Trivial

- None of substance beyond what is already noted as minor.

## Nice-to-Haves

- Running the baselines with a sliding-window adaptation would make the comparison irrefutable and is the single most impactful additional experiment.
- An oracle upper bound (ART-STVG trained on genuinely long videos, e.g., a subset of the extended data) would calibrate expectations about how much room for improvement remains.
- A failure analysis (spatial vs. temporal errors, per-video-length breakdowns) would help the community understand where LF-STVG methods fall short.
- Reporting inference time and memory usage as a function of video length would be valuable for practitioners.

## Removed Points

- **"Insufficient description of Baseline (ours)"** (Harsh Critic Critical Issue 3): The paper refers to supplementary material for the baseline architecture. The supplementary material was stripped by the parser and exists in the original submission. Per policy, missing-appendix criticisms are removed.
- **"Missing related works"**: Per policy, I cannot verify the existence of missing related works and must not introduce them.
- **Reproducibility nitpicks about undisclosed hyperparameters**: These are trivial implementation details that do not threaten reproducibility.
- **Formatting/style nitpicks**: Parser artifacts, not author errors.

## Novel Insights

The reviews surface an interesting tension: the paper's central claim — that autoregressive processing is crucial for long-video grounding — is supported by the large gap between ART-STVG and full-video baselines in Table 1, yet the paper never tests whether a simple non-autoregressive adaptation (e.g., sliding window) could close that gap. This means the evidence supports the *sufficiency* of the autoregressive + memory architecture but does not cleanly establish its *necessity*. A natural follow-up would be to compare ART-STVG against itself: an ART-STVG variant with memory but no autoregression (i.e., processing all frames in parallel with the memory banks) would disentangle the contributions of the two design choices. The reviewers did not note this specific experiment, but it emerges from combining their complementary concerns.

## Suggestions

1. **Clarify the evaluation protocol for all baselines.** State explicitly: (a) what maximum frame count each baseline implementation supports, (b) how longer videos were handled (frame sampling, truncation, sliding window, or full-video processing), and (c) whether any hyperparameters were adjusted for the longer videos.
2. **Clarify annotation coverage for the extended datasets.** State whether the ground-truth annotations cover the full 1–5 minute duration or only the original 20-second segment, and how metrics are computed for frames outside the annotated region.
3. **Add a sliding-window baseline.** The simplest adaptation of existing methods — run on 20-second windows with stride and merge predictions — would directly address the most natural question a skeptical reader would ask.
4. **Report variance** across multiple runs or seeds, at least for the main results (Table 1).
5. **Include an error analysis** on the 5-minute benchmark to inform the community about remaining challenges.

## Score and Decision

**Calibration anchors (retrieved from the human-review corpus):**

| Anchor | Avg Score | How it compares to this paper |
|--------|-----------|-------------------------------|
| TA-STVG (WOzffPgVjF) | 7.50 | Cleaner evaluation, tighter experiments, but solves a simpler (short-video) problem. This paper tackles a harder task with a more novel architecture but has evaluation protocol gaps. |
| Multi-granularity Correspondence (9Cu8MRmhq2) | 8.00 | More rigorous experimental design and stronger theoretical grounding. This paper is less polished and has more incomplete evaluation details. |
| Language Repository (O8FkMqNF1M) | 5.50 | Comparable average score range — both have interesting ideas but incomplete evaluations. This paper has cleaner ablations but similar evaluation protocol gaps. |
| LongViTU (4j9plQoOH1) | 4.75 | Weaker contribution (dataset-only, incremental). This paper has a stronger algorithmic contribution. |
| ARVideo (hWlCc7Iksi) | 3.40 | Much weaker — incremental method with marginal gains. This paper has a clearer problem formulation and larger improvements. |

The paper has a genuine contribution (first formulation of LF-STVG, novel autoregressive architecture with selective memory, strong empirical results across five extended benchmarks). The weaknesses are real but addressable: missing evaluation protocol details and a missing adapted baseline, not fatal theoretical errors. The core evidence (Table 1, ablation studies) supports the claims. Relative to the calibration anchors, this paper is substantially stronger than the Reject-level papers (avg 3.4–4.75) and weaker than the strongest Accept-level papers (avg 7.5–8.0) primarily due to incomplete evaluation specification rather than flawed methodology or weak results.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>