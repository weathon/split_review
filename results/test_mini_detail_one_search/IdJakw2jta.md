Now I have a thorough understanding of the paper and all the calibration anchors. Let me produce the final consolidated review.

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new task formulation for localizing targets in videos spanning minutes rather than tens of seconds, and proposes ART-STVG, an autoregressive transformer framework. The key ideas are: (1) processing video frames one at a time as a streaming input, making the architecture naturally suited for arbitrary-length videos; (2) spatial and temporal memory banks with text-similarity-based (spatial) and event-boundary-based (temporal) selection mechanisms that filter relevant historical context; and (3) a cascaded spatio-temporal decoder that uses fine-grained spatial grounding information to assist temporal localization. The authors extend HCSTVG-v2 to create five LF-STVG benchmarks (1–5 minutes) and show that ART-STVG consistently outperforms existing STVG methods (TubeDETR, STCAT, CG-STVG, TA-STVG) with the performance gap growing as videos get longer (e.g., +9.1% m.tIoU on 3-minute videos, +7.3% on 5-minute), while remaining competitive on short-form STVG (59.2 vs. 60.4 m.tIoU of the best specialist).

## Strengths

- **Novel task formulation and benchmarks.** The paper is the first to systematically study LF-STVG, extending HCSTVG-v2 to 1–5 minute benchmarks using original YouTube videos (not concatenated clips). This is a practical and timely contribution given the gap between existing STVG research (≤35s) and real-world applications.
- **Architecturally principled design for long videos.** The autoregressive streaming approach (one frame at a time with memory banks) is a clean and well-motivated departure from existing methods that process all frames at once. The design eliminates the computational bottleneck of full-video processing and has clear advantages for streaming/online settings. The memory selection strategies are simple yet effective, with ablations showing dramatic gains (temporal selection: from 9.6% to 23.0% m.tIoU; spatial selection: from 22.1% to 23.0%).
- **Consistent and growing performance advantage.** ART-STVG outperforms all four baselines across all five video lengths on all metrics, with the margin generally increasing with video length (e.g., +0.7% m.tIoU on 1-min → +9.1% on 3-min → +7.3% on 5-min vs. TA-STVG). The 40-second training experiment (Table 6) further confirms that training on longer videos yields even larger gains.
- **Cascaded decoder design validated by ablation.** The cascaded spatio-temporal decoder beats the parallel counterpart by 1.5% m.tIoU and 1.4% m.vIoU (Table 4), providing clear evidence that spatial grounding information helps temporal localization in long videos.
- **Competitive on short-form STVG despite being designed for long videos.** ART-STVG achieves 59.2 m.tIoU on HCSTVG-v2, trailing the best short-form specialist (TA-STVG) by only 1.2%, demonstrating that the autoregressive approach does not sacrifice standard-benchmark performance.

## Weaknesses

### Fatal
None.

### Major

- **Baseline adaptation to long videos is undocumented.** All compared baselines (TubeDETR, STCAT, CG-STVG, TA-STVG) are designed to process an entire clip in one forward pass. For 1–5 minute videos at 3.2 FPS (192–960 frames), running these methods on all frames simultaneously would likely exceed GPU memory. The paper provides no description of how baselines were adapted — frame subsampling, sliding windows, gradient checkpointing, or reduced resolution. This omission makes the comparison opaque; the reader cannot assess whether ART-STVG's gains reflect architectural superiority or an asymmetric evaluation setup. Since the paper reports reasonable (if low) performance from baselines on long videos, some adaptation was clearly used, but it should be specified.
- **Central claim is framed as "handling long videos" but all models are trained on 20-second clips.** The paper states (Section 4.1) that "all methods including ART-STVG are trained exclusively on the HCSTVG-v2 training set (average video length 20 seconds) for fair comparison." The experiments therefore measure zero-shot generalization from short training to long test videos, not training on long-form data. While the autoregressive architecture is architecturally suited for long videos and this setup is transparent, the paper should explicitly characterize this as a training-test length generalization scenario rather than implying the method was trained for long-form STVG. The 40-second training experiment (Table 6) partially addresses this, but training on 1-minute+ clips would be a more direct test of the core claim.

### Minor

- **Training procedure of the autoregressive decoder is underspecified.** The paper does not clarify whether ground-truth bounding boxes are used during training as input for the next time step (teacher forcing) or whether predicted boxes are fed back (autoregressive training with exposure bias). The loss function is relegated to the supplementary material. These details are needed for reproducibility.
- **Temporal memory selection (event boundary detection) lacks quantitative validation.** The heuristic (cosine similarity of adjacent memory features to detect event boundaries, inspired by TextTiling) is only evaluated qualitatively in Figure 6. Precision/recall of the detected boundaries against ground-truth event segmentation would strengthen the claim that the selection finds meaningful structure, not coincidence.
- **No discussion of the low absolute performance on long videos.** The best m.tIoU on 5-minute videos is 15.0%. While this is expected for a new and challenging task, the paper does not contextualize what constitutes reasonable performance or discuss headroom for future work.
- **No confidence intervals or significance tests.** Given that the test sets may be relatively small (2,000 validation samples split across 5 lengths), statistical significance of the performance gaps would strengthen the results.

### Trivial
- The self-attention complexity of the multimodal encoder (concatenating 2×H×W appearance+motion tokens + N_t text tokens) is analyzed only briefly. A complexity table would be helpful but is not essential.

## Nice-to-Haves
- Train ART-STVG on longer training clips (e.g., 1 minute) and evaluate on LF-STVG-1min/…/5min. The 40-second experiment in Table 6 shows promising gains, and extending this would be the most direct validation of the long-form claim.
- Implement a sliding-window adaptation of an existing STVG method (e.g., run TubeDETR on 20-second windows with overlap) as an additional baseline. This would isolate whether the autoregressive architecture or the memory selection drives the gains.
- Analyze how performance and compute scale with video length and whether memory saturation eventually hurts for very long videos (e.g., 10+ minutes).
- Compare the fixed heuristic for temporal memory selection (cosine similarity threshold) to a learned alternative to assess whether the heuristic is sufficient or merely a placeholder.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"Using all memories is worse than no memory — this is a red flag" (Harsh Critic):** The paper explicitly explains this behavior: in long videos with multiple events, all memories introduce irrelevant information. The selection mechanism is designed specifically to solve this problem, and the ablation (Table 2, 9.6% → 23.0%) confirms it works as intended. This is a well-explained phenomenon, not a flaw.
- **"Complexity of concatenation in multimodal encoder" (Harsh Critic):** The concatenation produces 2×H×W + N_t tokens. Since this is per-frame (not over the full video), the complexity is standard for per-frame transformer encoders and does not constitute a meaningful weakness.
- **"Table 6 results are puzzling" (Harsh Critic):** The critic acknowledged this was a misreading — training on 40 seconds consistently helps ART-STVG (28.3 vs. 23.0), which is expected and supports the paper's claims.
- **"The paper hides the zero-shot nature" (Harsh Critic):** Section 4.1 explicitly states that all methods are trained on 20-second clips for fair comparison. The paper is transparent; the issue is about framing, not hiding.

## Novel Insights

The reviews reveal a useful tension: the harsh critic treats the 20-second-training-on-long-testing setup as a fatal flaw, while the paper's results actually tell a more nuanced and interesting story. **The most compelling evidence that this paper offers — but does not fully articulate — is that the performance gap between ART-STVG and all baselines grows monotonically with video length.** At 1 minute, the gap over TA-STVG is merely +0.7% m.tIoU; at 3 minutes it is +9.1%; at 5 minutes +7.3%. This trajectory is exactly what one would expect if the autoregressive streaming architecture genuinely handles temporal accumulation better than all-at-once methods. The fact that the gap exists at all despite all methods being trained on 20-second clips suggests that the architectural inductive bias (per-frame processing + selective memory) confers a structural advantage that does not depend on seeing long training data. The paper should lean into this narrative rather than letting it appear as an oversight.

## Suggestions

1. **Document baseline adaptation explicitly.** A single sentence in the experimental setup stating how each baseline was applied to long videos (e.g., "For videos exceeding N_f=64 frames, we uniformly subsample 64 frames for all-at-once methods; for ART-STVG we process all frames sequentially.") would eliminate the main methodological concern.
2. **Reframe the long-video evaluation as zero-shot generalization.** Explicitly state that the model is tested on longer videos than trained on, and position this as a stronger test of the architecture's long-video capabilities. Add a training-on-longer-videos experiment (≥1 minute) as the primary validation.
3. **Add precision/recall analysis for temporal event boundary detection** to quantitatively validate the temporal memory selection heuristic.
4. **Specify the training procedure (teacher forcing vs. autoregressive)** and move the loss function into the main paper or provide the supplementary appendix.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WOzffPgVjF.md` (TA-STVG) | 7.50 | Directly related short-form STVG method, accepted at ICLR. Stronger methodological completeness (trained and tested on same-length videos) but tackles an easier problem. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/14fFV0chUS.md` (TRACE) | 6.75 | Temporal grounding with video LLMs, accepted. Comparable completeness and novelty; fewer methodological gaps. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8pusxkLEQO.md` (ARLON) | 6.25 | Autoregressive+diffusion for long video generation, accepted. Comparable in quality; some evaluation gaps similar to this paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YCwN7wQA6W.md` (Grounded-VideoLLM) | 4.25 | Video temporal grounding with LLMs, rejected. Less novel framing and weaker empirical validation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xYzOkOGD96.md` (Grounded Video Caption) | 3.83 | Grounded captioning, rejected. Task novelty is reasonable but approach is less clean and baselines are weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hWlCc7Iksi.md` (ARVideo) | 3.40 | Autoregressive video pretraining, rejected. Limited contribution beyond straightforward application of existing ideas. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lvgsPjRtLM.md` (VideoDiT) | 2.50 | Video generation, rejected. Significant evaluation and novelty concerns. |

**Positioning:** This paper is stronger than the rejected anchors (3–5 range) due to its clear problem motivation, novel architecture, and strong empirical consistency. However, it is slightly weaker than top-tier anchors (7+) due to the undocumented baseline adaptation and the framing gap around training-test length mismatch. It aligns most closely with the mid-tier accepted papers (6.0–6.75) in terms of overall quality and contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>