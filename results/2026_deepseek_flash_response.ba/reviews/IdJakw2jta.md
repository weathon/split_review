Now I have enough calibration context. Let me synthesize the final review.

## Summary
This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending the standard STVG setting to videos of 1–5 minutes, and proposes ART-STVG, an autoregressive transformer that processes frames sequentially with selective spatial/temporal memory banks and a cascaded decoder design. On extended HCSTVG-v2 benchmarks (1–5 minutes), ART-STVG substantially outperforms existing methods (TubeDETR, STCAT, CG-STVG, TA-STVG), with gaps widening as videos grow longer.

## Strengths
- **Autoregressive design avoids the all-frames-at-once bottleneck.** Prior STVG methods process all frames simultaneously, which becomes prohibitive for long videos. ART-STVG's frame-by-frame processing is a principled solution to this scaling issue. Table 1 shows that on LF-STVG-5min, existing methods collapse to 7.7–8.1% m.tIoU while ART-STVG achieves 15.0%, with the gap growing monotonically from 1 min to 5 min.
- **Memory selection is shown to be non-obviously essential.** Table 2 reveals that using *all* temporal memories *hurts* performance relative to no memory (9.6% vs. 16.7% m.tIoU), and only the proposed selection mechanism recovers and exceeds both (23.0%). This provides strong evidence that naive memory aggregation fails for multi-event long videos, and the paper's boundary-detection-based selection addresses a real problem.
- **Cascaded decoder design is cleanly ablated.** Table 4 isolates the cascaded spatial→temporal design from the parallel alternative, showing consistent gains (+1.5% m.tIoU, +1.4% m.vIoU), confirming that fine-grained spatial cues help temporal localization in long videos.
- **Systematic ablations covering all key design dimensions.** Tables 2–6 individually ablate temporal memory selection, spatial memory selection, decoder architecture, number of selected memories, and training video length. Each experiment isolates a single variable while keeping others fixed.
- **Creation of five multi-duration benchmarks** (LF-STVG-1min through 5min) from authentic YouTube source videos, enabling direct measurement of how each method degrades with temporal extent.

## Weaknesses

### Major
- **Evaluation protocol for baselines on long videos is unspecified.** The paper's central comparison (Table 1) pits ART-STVG against TubeDETR, STCAT, CG-STVG, and TA-STVG on 1–5 minute videos (~960 frames at 3.2 FPS). All four baselines are transformer architectures with quadratic self-attention that cannot process 960 frames at full resolution in a single forward pass. The paper provides no description of how these baselines were deployed: How many frames did each baseline actually process? Was subsampling used, and if so what strategy? Were architectural modifications or memory optimizations applied? If baselines subsampled to, say, 64 frames while ART-STVG processed all 960, the reported gaps conflate architecture with frame access. The paper's central claim—that ART-STVG's design is responsible for the large gains on long videos—cannot be fully evaluated without this information. This is the single most important gap.

### Minor
- **No inference cost analysis.** The paper motivates ART-STVG partly by the computational bottleneck of full-video processing, yet provides no comparison of FLOPs, inference time, or memory consumption between ART-STVG and baselines. An autoregressive model processing 960 frames one-by-one may be slower than a subsampled parallel method, and this trade-off should be quantified.
- **Key architectural parameters missing from main text.** The number of decoder blocks *K* is never stated. The spatial memory selection uses "similarity" without specifying the metric (cosine? dot product?). The temporal boundary detection algorithm (threshold or selection criterion) is not described. The memory bank is said to grow "without removing any existing memories" (line 148), which appears to imply unbounded growth—how this is bounded in practice for long videos is unclear.
- **Loss function entirely deferred to supplementary material.** Section 3.5 sends the reader to supplementary for the loss function. A high-level description of the loss terms would improve readability.
- **SF-STVG performance slightly below SOTA.** ART-STVG underperforms TA-STVG by 1.2/1.0 points on short-form HCSTVG-v2 (Table 7). The paper describes this as "competitive," which is fair, but the trade-off should be more explicitly discussed.
- **Limited evaluation scope.** Results are reported on a single extended dataset (HCSTVG-v2 validation set only, 2,000 samples per length variant). The paper explains that only HCSTVG-v2 provides source videos for extension, which is a valid practical constraint but limits confidence in generalization.
- **Absolute performance on long videos is low.** ART-STVG achieves only 15.0% m.tIoU on LF-STVG-5min. While relative improvements over baselines are large (often 2×), the paper does not discuss what these absolute numbers mean practically, what the failure modes are, or what the upper bound might be given that models are trained only on 20-second clips.

### Trivial
- The notation in Equation (1) uses the same label "[f_i^1, f_i^2, ..., f_i^{H×W}]" for both appearance and motion features—this appears to be a formatting artifact (the conceptual description is clear).

## Nice-to-Haves
- A more complete decomposition showing the cumulative effect of each component (autoregressive baseline → +cascaded → +spatial memory → +temporal memory → full model) would sharpen the contribution story.
- Qualitative analysis on long videos (e.g., attention maps over the temporal dimension, failure case breakdown) would strengthen the claim that the model "handles" long-form videos.
- The related work discussion of long-term video understanding methods is brief and does not deeply differentiate ART-STVG's memory from memory-augmented video QA models beyond a single sentence.

## Removed Points
- *Garbled notation in Equation (1)*: This is a parser artifact from PDF extraction; the conceptual description is clear. Removed.
- *Related work too brief*: This is a scope preference rather than a specific error. Moved to Nice-to-Haves.
- *Missing appendix details*: The supplementary material is stripped during PDF parsing; these details exist in the original submission. Removed.
- *Criticism about baseline architecture underspecification*: Partially overlaps with the evaluation protocol concern, but the phrase "similar architecture... without memory and memory selection modules" is reasonably clear. Removed as a standalone point; subsumed by the broader major weakness.

## Novel Insights
None beyond the paper's own contributions. The finding in Table 2 that using all temporal memories is worse than using none (9.6% vs. 16.7% m.tIoU) is itself an interesting insight that the paper surfaces and then resolves with selective memory—but this is already a contribution claimed by the paper.

## Suggestions
1. **Disclose the baseline evaluation protocol in full.** Describe how many frames each baseline processed on each LF-STVG variant, the subsampling strategy (if any), GPU hardware, and any architectural modifications. Ideally, include a controlled experiment where ART-STVG is limited to the same number of frames as baselines to isolate the benefit of processing density from architectural design.
2. **Add inference cost measurements.** Report wall-clock time, FLOPs, and peak GPU memory for ART-STVG and baselines on at least one long-video condition.
3. **Specify K, the memory selection similarity metric, and the temporal boundary detection criterion.** These are needed for reproducibility.
4. **Add qualitative examples on long videos.** Show what the model attends to over a 5-minute span, with failure case analysis.

## Score and Decision

**Bracket (Round 1):** 4.5–6.0  
The paper is stronger than Grounded-VideoLLM (4.25, Reject) which was criticized for limited technical novelty—ART-STVG has a clearer architectural contribution and cleaner ablations. It is comparable to CoSPaL (5.50, Accept) and Language Repository (5.50, Reject) in terms of contribution clarity and experimental rigor, though it has a more significant experimental documentation gap. It is weaker than ARLON (6.25, Accept), which was well-received for its integrated autoregressive+diffusion design and comprehensive evaluation.

**Narrowing (Round 2):**  
Compared to Streaming Video Understanding with StreamChat (5.80, Accept), which similarly introduces a new task+benchmark+method, our paper has a less comprehensive evaluation (single source dataset vs. multiple benchmarks) and a more consequential documentation gap. Compared to CoSPaL (5.50, Accept), our paper has cleaner ablations but shares a similar concern about comparison fairness. The Grounded-VideoLLM (4.25, Reject) anchor suggests the floor for rejection with novelty concerns; our paper's novelty is clearer, placing it above this anchor.

**Calibrated score: 5.0.** The paper proposes a well-motivated method for a genuinely new problem and provides systematic ablations. However, the incomplete documentation of how baselines were run on long videos undermines confidence in the headline comparison—a gap severe enough to prevent acceptance in its current form but addressable in revision.

**Decision: Reject** (in current form; requires major revision on evaluation protocol disclosure before resubmission).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>