## Summary

This paper proposes a multi-view deep learning pipeline for real-time Distance-to-Touchdown (DTD) estimation of approaching aircraft in digital tower environments. The system uses YOLOv7 detection with auto-segmentation (splitting high-resolution frames into tiles to preserve small-aircraft pixels), per-camera calibration networks trained with an adaptive algorithm and cross-view regularization, and an LSTM-based ensemble to fuse multi-view features. The pipeline achieves 0.18% MAPE on simulated Changi Airport data and 0.33% MAPE on real data (cloudy conditions, ≤7NM).

## Strengths

- **Auto-segmentation provides a clear, quantified detection-range improvement.** Splitting 1920×1280 frames into 640×640 tiles extends the maximum detection range from 6NM to 10NM and the effective range from 4NM to 8NM compared to naive downscaling (Table 2). This is a concrete engineering contribution with direct operational relevance.

- **Adaptive training algorithm with cross-view regularization is a practical solution to a real multi-view training problem.** The method of freezing the faster-converging calibration network until the slower one catches up (described in Section 4.1.2 and Figure 4) and the regularization term in Eq. 1 that enforces perspective-invariant features are sensible design choices that address genuine challenges in multi-camera setups.

- **The analysis of failure modes demonstrates genuine diagnostic thinking.** The explanation linking the accuracy dip around 7NM to Changi Airport's instrument approach chart (aircraft altitude adjustments between DME points at 4.4NM and 7.6NM making bounding boxes less discriminative) is insightful and domain-grounded (Section 5). This goes beyond simple metric reporting.

- **Robustness to detection failures is explicitly demonstrated.** The paper reports 15% of data points have miss-detections in at least one view (line 109), and the "Combination" setting (≥1 view detected) still achieves strong performance. The "Dual Exclusive" setting reduces errors by >30% (line 116), showing the system handles imperfect detection gracefully.

- **The weather/lighting analysis provides practical deployment insight.** Table 3 breaks down performance across four weather and five lighting conditions, with reasoned explanations for why cloudy conditions cause the highest error ("inconsistency of the sky" degrading bounding box accuracy) and why low-light conditions sometimes outperform high-light ones (glare and shadow effects).

## Weaknesses

### Fatal

None.

### Major

- **The central claim that multi-view fusion drives the performance gain is unsupported.** The only baseline is a hand-engineered geometric formula ("distance as a function of aircraft size and bounding box size," line 54), not a learned single-view variant of the proposed architecture. The reported 0.18% MAPE (67% reduction from 0.58%) therefore conflates two factors: (a) using a learned regressor vs. a geometric formula, and (b) using two views vs. one view. Without a single-view version of the same pipeline (same calibration network, LSTM, training procedure — but fed features from one camera), there is no way to attribute the improvement to the multi-view design. This is the most significant gap in the paper's experimental support for its core thesis.

- **The real-world case study cannot validate the multi-view advantage.** As the paper honestly reports (line 132), View 1 suffers a >90% miss-detection rate on real data due to small aircraft size and cloudy conditions, leaving the system operating effectively as a single-view pipeline. The real-world MAPE of 0.33% is therefore a single-view result under limited conditions (≤7NM, cloudy only). The paper's central architectural thesis — that combining multiple camera views improves accuracy and robustness — remains empirically untested on real-world video feeds.

- **The evaluation treats highly autocorrelated time-series data as independent samples.** The ~496k training samples are drawn from only 70 landing trajectories, each ~4 minutes long (line 50). Consecutive frames within each trajectory are nearly identical. The paper reports no trajectory-level evaluation, no cross-validation at the trajectory level, and no confidence intervals. The 30 test trajectories are independent, but the framing of 496k "data points" with a single MAPE figure almost certainly masks substantial variance across trajectories. This significantly overstates the apparent statistical reliability of the results.

### Minor

- **The LSTM's role and the architecture are under-specified.** The notation "[LSTM([256, 256],2)]" (line 50) does not clarify whether the LSTM processes temporal sequences across consecutive frames or simply treats the two camera-view feature vectors as a length-2 sequence. These are fundamentally different mechanisms. Similarly, the calibration network is described as "Linear([256,1])" but takes 4-dimensional bounding box inputs (x, y, w, h) — there must be hidden or embedding layers that are not documented. These omissions undermine reproducibility.

- **The regularization term in Eq. 1 is not ablated.** The cross-view prediction-consistency loss is described but never tested with/without. It is unclear whether it helps, hurts, or is neutral.

- **No per-trajectory error analysis is reported.** With 30 independent test trajectories, reporting per-trajectory MAPE (mean and variance) would be far more informative than the single aggregate MAPE.

- **Total pipeline latency is not fully reported.** The 28ms figure (line 77) covers YOLOv7 inference with TensorRT, but the auto-segmentation pipeline requires splitting the frame into 6 tiles plus a conditional second detection pass. The total per-frame latency (including tiling and the conditional second pass) is not given, making the "real-time" claim imprecise.

### Trivial

- None.

## Nice-to-Haves

- A comparison against a stereoscopic method would strengthen the framing, since the paper opens by critiquing stereoscopic approaches. This is outside the paper's stated scope but would make the motivation more self-contained.
- Ablating the LSTM against simpler fusion (concatenation, averaging) would clarify whether the sequential model adds value over straightforward alternatives.
- Testing on multiple aircraft types would strengthen generalizability claims.

## Removed Points

The following points from the inputs were filtered:
- The harsh critic's complaint that "Algorithm 1 cannot be evaluated because the parser stripped it" — removed per rule that parser-stripped content (appendices, algorithms) exists in the original submission.
- The critic's observation about "monoscopic model uses only bounding box size" being a weak baseline is superseded by the more precise articulation that no learned single-view baseline exists.
- No strengths were removed: all claimed strengths are concrete, specific, and backed by evidence in the paper.

## Novel Insights

None beyond the paper's own contributions. The two reviews confirm the paper's practical engineering merit while converging on the key gap: the multi-view advantage is asserted but not cleanly isolated experimentally.

## Suggestions

1. **Add a single-view learned baseline.** Train the same calibration network + LSTM architecture on features from only one camera. This is the single highest-leverage experiment and would directly test the paper's core architectural claim.

2. **Report trajectory-level statistics.** For the 30 test trajectories, report per-trajectory MAPE (mean, std, min, max). This would address the temporal-autocorrelation concern and provide a more honest assessment of generalization.

3. **Ablate the regularization term** and the LSTM fusion mechanism in separate experiments. The paper's design contains several interacting components, and the community would benefit from knowing which ones matter.

4. **Clarify the LSTM architecture explicitly.** State whether the LSTM processes temporal sequences (and over what window) or fuses the two camera views. Document the calibration network's full layer structure beyond the ambiguous "Linear([256,1])" notation.

5. **Report total end-to-end latency** including auto-segmentation overhead (tiling + conditional second pass), not just YOLOv7 inference time.

6. **Be more precise in the real-world conclusions.** The paper should explicitly acknowledge that the Changi case study validates single-view performance under limited conditions and that multi-view real-world validation remains future work.

## Score and Decision

**Score:** 4.5

**Decision:** Reject

**Rationale:** The paper addresses a practically relevant problem and contains several reasonable engineering ideas (auto-segmentation, adaptive calibration network training). However, the central claim — that multi-view fusion improves DTD estimation — is not adequately supported by the evidence. The sole baseline is a non-learned geometric formula, making it impossible to attribute the 67% MAPE reduction to the multi-view design. On real data, the multi-view system collapses to single-view operation. The evaluation also treats heavily autocorrelated trajectory frames as independent samples, with no trajectory-level statistics or confidence intervals. For ICLR, where papers are evaluated on the strength and clarity of their evidence for their core claims, these gaps are significant enough to warrant rejection. The engineering contributions are real but would need substantially stronger experimental support to be competitive at a top venue.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>