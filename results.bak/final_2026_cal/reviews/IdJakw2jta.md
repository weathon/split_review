Now I'll synthesize the final review.

## Summary
This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending the task from ~20-second clips to 1–5 minute videos. The authors propose ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks and a cascaded spatio-temporal decoder. The method is evaluated on extended HCSTVG-v2 benchmarks (LF-STVG-1min through 5min), showing large improvements over existing methods. The ablations convincingly demonstrate that the memory selection strategies and cascaded design are essential for the gains.

## Strengths
1. **Well-motivated problem and clean technical solution.** The paper identifies a genuine gap — all prior STVG work operates on videos <1 minute, and existing parallel-processing architectures cannot scale to longer videos. The autoregressive frame-by-frame design with memory banks is a natural and principled approach to long-form video, directly addressing the computational bottleneck of existing methods that "process all frames at once."

2. **Strong internal ablations validate each component.** Tables 2–5 convincingly show that: (a) using all temporal memories without selection *hurts* performance (9.6% m.tIoU) compared to no memory (16.7%), but selection recovers to 23.0% — a 13.4% gain; (b) spatial memory selection also improves performance; (c) the cascaded decoder design outperforms the parallel design by 1.5% m.tIoU; (d) the N_s=32 selection budget is optimal. These ablations are clean, controlled, and internally consistent.

3. **First benchmark suite for LF-STVG.** Extending HCSTVG-v2 validation to 1–5 minutes using original YouTube sources (not concatenated clips) with manual review provides a reproducible evaluation platform that was previously absent. This is a practical contribution that will enable future work.

4. **Competitive on short-form STVG despite long-form focus.** ART-STVG achieves 59.2 m.tIoU on HCSTVG-v2, trailing the SOTA TA-STVG by only 1.2 points while outperforming all other existing methods, demonstrating that the autoregressive design does not sacrifice short-video capability.

## Weaknesses

### Major

1. **Evaluation protocol for baseline methods on long videos is not disclosed.** This is the most significant weakness. The paper reports large improvements over TubeDETR, STCAT, CG-STVG, and TA-STVG on the LF-STVG benchmarks (Table 1), but never describes how these methods were evaluated on videos up to 5 minutes long. Existing STVG methods process all frames simultaneously and, as the paper itself notes (Section 1), suffer from "high GPU memory requirements" for long videos. A 5-minute video at 3.2 fps produces ~960 frames; the training uses N_f=64 frames. The paper does not state whether the baselines were given all 960 frames, subsampled frames, a sliding window, or some other adaptation. Without this detail, the central experimental claim — that ART-STVG significantly outperforms prior work on long videos — is difficult to verify independently. The paper states baselines were run using "provided source codes" (Table 6 caption), but the *inference* protocol (frame budget, GPU used, any subsampling/chunking strategy) must be specified to interpret the comparisons. The large gap (e.g., ART-STVG m.tIoU 15.0% vs TA-STVG 7.7% on 5-min videos) could partly reflect an unfair frame budget rather than genuine architectural superiority.

2. **LF-STVG dataset statistics are not reported.** The paper extends 2,000 HCSTVG-v2 validation samples to 1–5 minutes but does not report how many videos/queries exist per length category. Not all original YouTube videos may be long enough to extend to 5 minutes. Reporting the number of samples in each LF-STVG split, the average target event duration, and the distribution of lengths is essential for readers to assess the scale and difficulty of the benchmark.

### Minor

3. **Memory bank growth is not discussed.** The spatial memory bank stores one query per frame per decoder block (K partitions), growing linearly with video length without any retention or eviction policy. For a 5-minute video at 3.2 fps with K=6 blocks, this means ~5,760 stored items. While selection limits the cross-attention budget to N_s=32, the paper does not discuss the storage cost, whether pruning is ever applied, or whether unbounded growth would become problematic for hour-long videos. This is worth noting since the paper motivates the autoregressive design partly on computational grounds.

4. **No sliding-window or chunking baseline for long videos.** The "Baseline (ours)" row removes memory and selection modules, serving as an ablation control. But the paper does not include a natural non-autoregressive adaptation to long videos (e.g., running TubeDETR on chunks and merging predictions). Such a baseline would help isolate whether the improvements come from the autoregressive structure itself, the memory mechanism, or both. This is a nice-to-have but would strengthen the paper significantly.

5. **No confidence intervals or significance tests.** Given the variance inherent in long-video grounding (where only a small fraction of frames contain the target event), reporting standard deviations or significance tests across multiple runs for Table 1 would strengthen the conclusions.

### Trivial
- The paper states "all methods including ART-STVG are trained exclusively on the HCSTVG-v2 training set (average video length 20 seconds) for fair comparison" — a clarification on whether the *motion* backbone VidSwin (which uses previous frames as input) effectively sees temporally extended features even during training is worth noting, since this could partially mitigate the "trained on 20s" framing.

## Nice-to-Haves
- A wall-clock or GPU-memory comparison between ART-STVG and baselines on long videos, since the computational motivation is cited in the introduction.
- Qualitative failure analysis on very long videos, to contextualize the absolute performance numbers (15% m.tIoU on 5-min is low in absolute terms).
- A study of the temporal memory selection's sensitivity to the similarity threshold used for event boundary detection.

## Removed Points
- *"The evaluation of existing methods on long-form videos is likely unfair — baselines may have been subsampled."* This point is retained and upgraded to a Major weakness (see weakness #1), but the speculation that subsampling *must* have occurred is removed. The paper's failure to describe the protocol is the verifiable flaw, not the assumption of unfairness.
- *"The paper never states how these methods were evaluated on long videos."* Retained and merged with the major weakness.
- *"Missing related works."* Removed per policy — I cannot verify whether works are missing.
- *"Formatting/style nitpicks, typos, missing supplementary."* Removed per policy — these are parser artifacts or beyond verification.
- *"Reproducibility concerns about undisclosed hyperparameters."* Removed per policy — these are trivial implementation details.
- *Strawman about the baseline description being only in supplementary.* The paper does mention the baseline's architecture in the main text; the supplementary reference is just for extended detail.
- *Strength Finder strengths about "important problem" and "addressing gap."* Removed as generic/superficial. The retained strengths are concrete and evidence-backed.
- *"Competitive on short-form STVG despite being designed for long videos"* Retained — it is a specific, evidence-backed strength (Table 7).

## Novel Insights
None beyond the paper's own contributions. However, one observation emerges from reviewing the weaknesses: the paper's ablations (especially Table 2 showing that *all* temporal memories harm performance, delivering 9.6% vs 16.7% without any memory, while selection recovers to 23.0%) are actually more informative than the headline Table 1 results. These ablations make a clear cause-effect case for why the method works, independent of any evaluation-protocol ambiguities with the baselines. This suggests the paper would be better served by leading with this diagnostic evidence rather than relying primarily on the raw comparison numbers in Table 1.

## Suggestions
1. **Disclose the baseline inference protocol explicitly:** state how many frames were given to each baseline model at each LF-STVG length, whether any subsampling/chunking was used, the GPU hardware, and the total memory consumption.
2. **Add a sliding-window baseline** where existing methods process chunks of 64 frames and predictions are merged, as a more controlled comparison.
3. **Report full dataset statistics** for LF-STVG splits (number of videos per length category, target event duration distribution).
4. **Add confidence intervals** to the main results table, at minimum via bootstrap resampling or multiple runs.
5. **Acknowledge the memory growth issue** and optionally discuss pruning strategies for very long videos.

## Score and Decision

I calibrated this paper against the human-review corpus through two rounds of retrieval. 

**Round 1 (Bracketing):** Queried for STVG and long-video grounding papers in three bands. Weak-band anchors averaged 2.8–3.3 (e.g., "Temporal Grounding as a Learning Signal" at 2.80) and are clearly below this paper. Middle-band anchors averaged 4.0–6.0 (STVG-R1 at 4.67, Invert4TVG at 6.00). Strong-band anchors averaged 8.0 but are on different topics (3D generation, embodied navigation) and not comparable. This placed the initial bracket at approximately **4–6**.

**Round 2 (Narrowing):** Focused on the 4.5–6.0 range. Compared directly against:
- **STVG-R1 (4.67, Accept Poster)** — also tackles STVG with a new approach. ART-STVG has stronger technical novelty (autoregressive architecture designed for long video, not a wrapper on an existing VLM) and cleaner ablations, but shares a similar evaluation clarity gap. The paper is slightly stronger than this anchor.
- **VTG-Reasoner (4.00, Withdrawn)** — tackles long-video temporal grounding. ART-STVG is clearly stronger: it handles both spatial and temporal localization, has a more novel architecture, and better ablations.
- **Invert4TVG (6.00, Accept Poster)** — clean evaluation, incremental novelty. ART-STVG has more architectural novelty but a less transparent evaluation. Weaker than this anchor.
- **OmniSTVG (6.67, Accept Poster)** — new STVG sub-task with a large-scale benchmark and thorough evaluation. ART-STVG has a less extensive benchmark and a missing evaluation detail. Clearly weaker than this anchor.

After considering these comparisons, the final score is **5.0**. The paper has a genuine contribution (new problem formulation, principled method, strong internal ablations, useful benchmark extension), but the missing evaluation protocol for baselines is a significant gap that prevents full verification of the headline claim and keeps the paper below the 5.5–6.0 range.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>