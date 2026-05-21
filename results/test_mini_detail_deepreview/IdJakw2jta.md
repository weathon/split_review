Now I have enough information. Let me write the consolidated review.

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending the task to videos of 1–5 minutes. It proposes ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks, selective memory retrieval mechanisms, and a cascaded spatio-temporal decoder design. The authors extend the HCSTVG-v2 validation set to create five LF-STVG benchmarks at different lengths. Results show ART-STVG substantially outperforms existing methods (TubeDETR, STCAT, CG-STVG, TA-STVG) on these benchmarks while remaining competitive on short-form STVG.

## Strengths

- **First systematic exploration of long-form STVG with a well-motivated autoregressive architecture.** The paper correctly identifies that existing STVG methods, which process all frames at once, face fundamental scalability problems on minute-scale videos. ART-STVG's frame-by-frame streaming design directly addresses this limitation. Table 1 shows ART-STVG outperforms all four prior methods on every metric across LF-STVG-1min through LF-STVG-5min, with the gap widening as video length increases (e.g., 15.0% vs. 8.1% m.tIoU on 5-min videos).

- **Memory selection strategies yield large, cleanly isolated gains.** Table 2 shows that selective temporal memory raises m.tIoU from 9.6% (all memories) to 23.0%, a 13.4 point gain. Table 3 shows selective spatial memory adds 0.9% over using all spatial memories, and 1.7% over no spatial memory. These ablations provide direct evidence for the retrieval mechanism described in Sections 3.3–3.4.

- **Cascaded spatio-temporal decoder is clearly better than a parallel design.** Table 4 reports 23.0% vs. 21.5% m.tIoU and 15.3% vs. 13.9% m.vIoU for cascaded vs. parallel designs, validating the claim that fine-grained spatial cues assist temporal localization in long videos.

- **Creation of LF-STVG benchmarks that expose the limitations of existing methods.** The extended datasets (LF-STVG-1min through -5min) are derived from original YouTube videos (not concatenated clips), are manually reviewed for quality, and reveal that prior methods degrade to near-chance performance on longer videos while ART-STVG maintains meaningful results.

- **Strong generalization from short-clip training, with supporting ablation on longer training.** All models in Table 1 are trained only on 20-second videos, yet ART-STVG still outperforms baselines on 1- to 5-minute test videos. Table 6 further confirms that training on 40-second videos improves both ART-STVG and baselines, with ART-STVG remaining substantially ahead (28.3% vs. 21.0% m.tIoU).

## Weaknesses

### Fatal
None.

### Major

- **Baseline inference protocol on long videos is underspecified.** The paper describes existing STVG methods as processing "all video frames at once" (Section 1) and argues this is infeasible for long videos due to GPU memory constraints. However, it never specifies *how* these baselines are actually run during inference on 1–5 minute videos. Key questions go unanswered: Do baselines process all frames (∼960 frames for a 5-min video at 3.2 fps)? If not, what subsampling or sliding-window strategy is used? Are modifications made to the baseline code to handle longer inputs? The paper notes in Table 6 that baselines are run "using their provided source codes," but this does not clarify the inference protocol. The very low vIoU@0.5 scores for baselines on 4 min/5 min videos (e.g., 0.0–0.3%) could indeed reflect a genuine limitation of one-shot processing, but without specifying the protocol the reader cannot assess whether the comparison is fair. This is the most impactful weakness and should be fully addressed.

### Minor

- **Limited dataset statistics for the extended benchmarks.** The paper states that LF-STVG-1min through -5min are created by extending the HCSTVG-v2 validation set's videos from 20 seconds to 1–5 minutes using original YouTube source videos. However, no basic statistics are reported: how many of the 2,000 validation samples are extended for each length? What is the average extended length within each benchmark? How does the query's temporal extent relate to the longer video segment? These details are important for reproducibility and for interpreting the difficulty of each benchmark.

- **Some implementation details are not specified.** The number of decoder blocks (K) is used throughout the method description but never given an explicit value. The temporal memory selection uses cosine similarity between adjacent memories and identifies "lower similarity" points as event boundaries, but no threshold or algorithm for detecting these boundaries is specified. These details would aid reproducibility.

- **Metric definitions for long-form evaluation could be clarified.** The paper references prior work for m.tIoU, m.vIoU, and vIoU@R definitions, which is standard practice. However, for the long-form setting, it would be helpful to clarify how metrics handle frames where the target is absent (e.g., whether m.vIoU is averaged over all frames or only frames within the predicted/ground-truth temporal window), and how the temporal predictions (h_i^s, h_i^e) are converted into start/end timestamps.

### Trivial
None.

## Nice-to-Haves

- Providing a sliding-window adaptation of an existing baseline (e.g., TubeDETR applied to non-overlapping 20s windows with result aggregation) would strengthen the comparison and isolate the benefit of the autoregressive design.
- Reporting GPU memory consumption and inference time for all methods on the longest videos would further validate the claimed efficiency advantage.
- A limitations section acknowledging the growing memory bank for very long videos and the heuristic nature of the temporal boundary detection would improve the paper's completeness.

## Removed Points

These points were flagged for removal; treat them with caution if citing:

- **"The dramatic drop from 'no memory' to 'all memories' (16.7→9.6 m.tIoU) is not explained"** — REMOVED. The paper explicitly explains this at lines 272–273: "This is because the long-term video often contains multiple events, and using all temporal memories may introduce irrelevant information." The critic missed this explanation.
- **"The evaluation protocol may have been severely disadvantageous to existing methods"** — REMOVED as speculative. The core concern (underspecified protocol) is kept as Major, but the jump to assuming unfairness is not verifiable from the paper.
- **Missing related works / missing appendix content** — REMOVED per instructions (stripped by parser, no external sources to verify).
- **Formatting/style nitpicks, typos, missing symbols** — REMOVED (parser artifacts or not substantive).
- **"The paper lacks a limitations section"** — REMOVED (this is a nice-to-have, not a weakness; moved to Nice-to-Haves).
- **Strength Finder's generic strengths about the problem being "important" or "meaningful"** — REMOVED; only concrete, evidence-backed strengths are retained.

## Novel Insights

Neither review surface genuinely novel insights beyond the paper's own contributions. The harsh critic's most useful observation is that the baseline inference protocol must be specified — this is a real gap, but it is a demand for clarification, not a new analytical insight about the method.

## Suggestions

1. **Specify the baseline inference protocol.** For each baseline method, state: (a) the number of input frames processed during inference on each LF-STVG benchmark, (b) whether the original codebase was modified, (c) if subsampling or a sliding window was used, and (d) peak GPU memory consumption. This single clarification would address the main weakness.
2. **Add dataset statistics tables** for LF-STVG-1min through -5min with at least: number of samples, mean/median video length, mean query length, and mean temporal extent of the target event relative to video duration.
3. **State the value of K** (number of decoder blocks) explicitly in the implementation section, and specify the algorithm or threshold used for event boundary detection in temporal memory selection.
4. **Clarify the metric computation** for long-form evaluation: how are frames outside the predicted event window handled in m.vIoU, and how are h_i^s/h_i^e converted to timestamps?

## Score and Decision

**Calibration:** I retrieved papers across three score bands using *spatio-temporal video grounding* and *long-form video grounding* queries.

*Round 1 (bracketing):*
- **Low band (<3.5):** VideoGPT+ (3.40), Spatio-temporal Diffusion Transformer (3.00), weakly supervised visual grounding (3.00). These have fundamental methodological issues or weak evaluations — the paper under review is clearly stronger.
- **Middle band (3.5–7.5):** TRACE (6.75, temporal grounding, accepted), ARLON (6.25, long video generation, accepted), Look Remember Reason (6.50, video reasoning, accepted), ResidualViT (5.75, temporal grounding, rejected), CoSPaL (5.50, weakly supervised STVG, accepted), Grounded-VideoLLM (4.25, temporal grounding, rejected), Adaptive Memory (4.60, long-form video, rejected), Language Repository (5.50, long video, rejected), Long Context Transfer (5.80, long video, rejected), TinyMem (4.67, long video action detection, rejected).
- **High band (>7.5):** Multi-granularity Correspondence (8.00), TANGO (8.50), Universal Visual Grounding (7.75), MovingParts (8.00) — these address different problem settings and none are topically close enough for direct comparison.

*Round 2 (narrowing within bracket):*
The paper is clearly above Adaptive Memory (4.60), TinyMem (4.67), and Grounded-VideoLLM (4.25), whose evaluation scope or novelty concerns are more severe. It is comparable to ARLON (6.25) and Look Remember Reason (6.50) in terms of contribution clarity and experimental depth, though all three papers have addressable weaknesses. It is slightly below TRACE (6.75) whose causal event modeling is a more distinctive conceptual framing. The paper's contribution — first to define and tackle LF-STVG with a clean autoregressive design and thorough ablations — is substantive, but the underspecified baseline inference protocol prevents a higher score.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>