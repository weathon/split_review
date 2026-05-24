Now I have sufficient context. Let me produce the final consolidated review.

## Summary

This paper explores Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new problem setting where target objects must be localized in videos spanning 1–5 minutes rather than the standard ~20 seconds. The authors propose ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks and a cascaded decoder design. On extended LF-STVG benchmarks derived from HCSTVG-v2, ART-STVG consistently outperforms prior STVG methods across all video lengths (1–5 min), with the margin growing as video length increases (e.g., m.tIoU=15.0% vs. best prior 8.1% on 5-minute videos). The method also achieves competitive results on short-form STVG (59.2% m.tIoU vs. SOTA 60.4%).

## Strengths

1. **Novel problem framing and architecture for LF-STVG.** The paper is the first to systematically study STVG at minute-long durations, correctly identifying that existing parallel-processing methods become infeasible for long videos. The autoregressive streaming design with separate spatial and temporal memory banks is a principled architectural choice for this setting. Table 1 shows ART-STVG outperforming all prior methods on every video length (1–5 min), with the advantage roughly doubling from 1min (39.1 vs. 38.4) to 5min (15.0 vs. 8.1).

2. **Memory selection strategies provide large and well-ablated gains.** Table 2 demonstrates that temporal memory selection raises m.tIoU from 9.6% (all memories) to 23.0% — a 13.4-point gain — while Table 3 shows spatial selection adds 0.9 points on top of using all spatial memories. The ablations are cleanly structured (no memory → all memories → selected memories) and the mechanism's behavior is visually supported by attention maps in Figure 5.

3. **Cascaded decoder design is validated with controlled comparison.** Table 4 directly compares cascaded vs. parallel decoding: cascaded improves m.tIoU by 1.5% (23.0 vs. 21.5) and m.vIoU by 1.4% (15.3 vs. 13.9), confirming that routing fine-grained spatial information to the temporal decoder provides a meaningful benefit for long-form localization.

4. **Competitive short-form performance despite being designed for long videos.** On the standard HCSTVG-v2 validation set (Table 7), ART-STVG achieves 59.2% m.tIoU, outperforming all methods except TA-STVG (60.4%) and substantially exceeding the autoregressive baseline without memory (46.2%). This shows the design does not sacrifice short-clip capability.

5. **Training with longer videos strengthens the empirical case.** Table 6 trains all methods on 40-second videos (vs. the default 20s): ART-STVG's m.tIoU rises to 28.3% on 3-minute evaluation, far ahead of TA-STVG (20.7%), confirming the approach exploits longer training sequences better than parallel methods.

## Weaknesses

### Fatal
None.

### Major

1. **Out-of-distribution evaluation limits the strength of the central claim.** All methods (including ART-STVG) are trained exclusively on 20-second videos but tested on 1–5 minute videos (Section 4.1, line 264: "all methods including ART-STVG are trained *exclusively* on the HCSTVG-v2 training set (average video length 20 seconds) for fair comparison."). This means every model faces a domain shift in video length at test time. The paper's core claim — that ART-STVG "can handle long-term videos effectively" — would be better supported by training on videos of the same length as the evaluation target. The 40-second training experiment (Table 6) partially mitigates this concern, but 40s → 3min still involves a 4.5× gap. Creating a proper long-form training set remains future work, and the current absolute numbers (15–39% m.tIoU) are quite low, reflecting the difficulty of the resulting out-of-distribution task.

2. **The temporal memory integration shows anomalously large degradation when all memories are used.** In Table 2, adding *all* temporal memories *reduces* m.tIoU from 16.7% (no memory) to 9.6%. The paper explains this as "irrelevant information" from multiple events. While the explanation is plausible, the magnitude of the drop (7.1 points) is unusual and suggests the query-insertion mechanism (adding the query without removal, line 206) may cause a specific failure mode — perhaps the unboundedly growing memory bank allows irrelevant event-level features to dominate cross-attention. The selection heuristic then compensates for this integration issue. An analysis of *why* all memories hurt so much (e.g., attention weight distributions, per-event memory interference) would strengthen the paper.

3. **The evaluation uses only one base dataset (HCSTVG-v2).** The datasets are extensions of HCSTVG-v2's validation set, which is the only available source with public video URLs (line 258). However, evaluating on a single source domain limits generalization claims. Testing on an additional long-video dataset (e.g., VidSTG if source videos are available, or a subset of Ego4D adapted for STVG) would substantially increase confidence in the method's generality.

### Minor

1. **Frame-level probabilities to segment-level prediction are not specified.** The temporal head produces per-frame start/end probabilities (h_i ∈ ℝ², line 182), but the paper does not describe how these are aggregated into a video-level temporal segment prediction (i.e., start time and end time). This detail is needed for reproducibility.

2. **The VidSwin clip length for 3D feature extraction is not reported.** The paper uses VidSwin for motion features and notes that "previous frames are also used as input" (line 136), but the exact temporal window / clip length is unspecified.

3. **The N_s ablation shows minimal sensitivity (range 22.5–23.0, Table 5),** which somewhat weakens the claim that the number of selected spatial memories is a critical design choice. The result is practically useful (performance is robust), but the paper presents it as validating the choice of N_s=32 without discussing this near-invariance.

4. **The memory bank grows unboundedly** (line 206: "adding the query as a new memory, without removing any existing memories"). For very long videos this is computationally problematic, and no scalability analysis (memory footprint vs. video length) is provided.

### Trivial
None.

## Nice-to-Haves
- A comparison with a simple sliding-window baseline (chunk a long video into 20-second clips, process each independently with a standard STVG method, then aggregate) would clarify the benefit of the autoregressive architecture over a much simpler alternative.
- Qualitative timeline visualizations showing predicted start/end probability curves for ART-STVG vs. baselines across different video lengths would help illustrate *why* the temporal memory selection improves boundary detection.
- Analysis of how N_s and the temporal selection threshold should scale with video length.

## Removed Points

- **"The improvements over baselines are not properly controlled for the chosen architecture"** (Harsh Critic #2): This criticism argues that comparisons against non-autoregressive prior methods are unfair because prior methods aren't designed for streaming. However, this is exactly the paper's point — the comparison demonstrates that the autoregressive paradigm is superior for long videos. The paper provides a controlled baseline (autoregressive without memory) that isolates the contribution of the memory modules. The suggestion to "adapt prior methods to process frames sequentially" would mean re-implementing the paper's core contribution in other methods, which is not a reasonable requirement. *Removed: invalid criticism.*

- **"The scarcity of experimental detail and reproducibility concerns"** about loss functions and architecture details deferred to supplementary material (Harsh Critic #4): The review template explicitly states that appendix content is stripped by the parser; these details exist in the original submission. *Removed: parser artifact.*

- **"The paper claims 'first to explore LF-STVG' but the dataset is extended from an existing one"**: The paper accurately and transparently describes that the LF-STVG benchmarks are extensions of HCSTVG-v2 because it is "the only dataset which provides available source videos" (line 258). Being the first to explore a problem and using extended existing data for evaluation are not contradictory. *Removed: not a valid weakness.*

- **Strength Finder claimed "Extension benchmarks are constructed from real long videos, not artificially concatenated clips"** as a supporting strength. This is factually correct and retained in Strengths.

- **Soft strengths from Strength Finder (#4 competitive short-form, #6 training with longer videos)**: Verified against the paper and retained.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the paper that the authors' own framing and analysis do not already cover.

## Suggestions

1. **Address the out-of-distribution evaluation more directly.** Either (a) create a long-form training set by extending a subset of HCSTVG-v2's training videos (acknowledging the annotation cost), or (b) reframe the paper's claims from "handles long-form STVG" to "is robust to temporal distribution shift for STVG" and discuss the practical implications of this different framing. The 40-second training experiment (Table 6) is a step in the right direction; extending to actual 1–5 minute training would be stronger.

2. **Analyze the "all memories hurt" phenomenon in Table 2.** Provide attention visualizations showing how irrelevant event memories interfere with the query, or ablate the query insertion mechanism (e.g., compare inserting vs. not inserting the query into the memory bank before selection). This would separate the quality of the selection heuristic from potential integration issues.

3. **Clarify the frame-to-segment conversion** — describe how per-frame start/end probabilities are aggregated into a single temporal interval prediction.

4. **Add a sliding-window baseline** that processes long videos in non-overlapping chunks with a standard STVG method and fuses results. This is a simple, practical alternative that would help justify the architectural complexity of ART-STVG.

5. **Report memory bank size growth** as a function of video length and discuss potential mitigation strategies (e.g., FIFO or attention-based eviction) for very long videos.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WOzffPgVjF.md` (TA-STVG) | 7.50 | Directly related STVG paper, accepted at ICLR. Stronger evaluation (3 standard benchmarks, in-distribution). This paper is somewhat weaker due to evaluation constraints. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8pusxkLEQO.md` (ARLON) | 6.25 | Long-video generation with autoregressive + diffusion. Similar level of architectural contribution and experimental evidence. Comparable quality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/le4IoZZHy1.md` (CG-Bench) | 6.20 | Benchmark paper for long video understanding. Accepted. This paper has a stronger technical contribution (novel architecture) but weaker evaluation breadth. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1DEHVMDBaO.md` (AMM) | 4.60 | Long-form video with memory augmentation. Rejected; had marginal improvements and weak baselines. This paper is substantially stronger in evidence and claims. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uHgVrGF2Wn.md` (LVBench) | 4.50 | Long video benchmark paper. Rejected; had quality concerns. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xYzOkOGD96.md` (Grounded Video Caption) | 3.83 | Rejected for limited evaluation and weak comparisons. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YGWxpOI6Y0.md` (VideoGPT+) | 3.40 | Rejected; scattered contributions, inadequate ablation. This paper is much more focused and coherent. |

The paper is weaker than the TA-STVG anchor (7.50) due to its constrained evaluation setup (single dataset, OOD training/test), but substantially stronger than the rejected papers (4.0–5.0 range). It is comparable to the accepted ARLON paper (6.25) and CG-Bench (6.20) in terms of contribution clarity and empirical support.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>