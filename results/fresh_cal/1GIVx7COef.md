Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces the first event-aided framework for spatially dense and temporally continuous point tracking. It proposes a streaming pipeline that estimates local B-spline curve trajectories from two consecutive frames and inter-frame events, then aggregates them via cross-attention and GRU-based fusion into global long-term trajectories. The method uses a self-supervised event consistency loss to exploit the continuous nature of events during training. Experiments on CVO, TAP-DAVIS, and DSEC benchmarks show consistent improvements over image-only baselines. Ablations confirm the contributions of event data, the curve representation, and the global aggregation strategy.

## Strengths

- **First integration of event data for dense continuous point tracking.** The paper introduces a genuinely new problem setup (event-aided temporally continuous dense tracking) and backs this with quantitative gains: 0.19 EPE_all improvement over DOT on the CVO extended set (Table 1) and 2.7 AJ improvement on TAP-DAVIS (Table 2). These are substantial margins on established benchmarks.

- **Multi-frame iterative streaming framework with explicit architecture validation.** The global motion aggregation via cross-attention and GRU (Sec. 3.2) is ablated in Table 5, where it outperforms direct flow accumulation ("post") and fixed-window fusion ("solo") on both CVO third and DAVIS quarter settings. This directly verifies the design choice.

- **Self-supervised event consistency loss with empirical support.** The event-to-trajectory consistency objective (Eq. 5) is ablated in Table 7, where adding it improves AJ from 0.653 to 0.681 on DAVIS quarter. The loss is principled (grounded in contrast maximization, a well-established event-processing framework) and well-motivated given the lack of continuous ground-truth annotations.

- **Systematic ablation of curve representation and control-point count.** Table 6 compares B-spline (N_c=4) against linear and quadratic motion assumptions, showing consistent gains. The choice N_c=4 is empirically justified by showing no further improvement with more control points.

- **Explicit handling of warping numerical error and occlusions.** The method includes a learned start-point offset (O_t) for compensating integer sampling errors and a learnable Fusion module for occluded points (Eq. 1). Ablation in Table 5 confirms that removing the offset degrades performance.

## Weaknesses

### Fatal

None.

### Major

- **The B-spline curve accumulation is mathematically underspecified at a critical point.** The method concatenates control points from local B-spline curves to form a global trajectory with (t−1)×N_c control points (Sec. 3.1). However, a B-spline's behavior is fundamentally determined by its knot vector and degree, neither of which is discussed for the global concatenated curve. The paper mentions "degree p" (line 48) but never specifies p's value. It does not state how the knot vector is extended when concatenating local curves, whether continuity constraints (C⁰, C¹, C²) are enforced at frame boundaries, or whether the global curve is still a valid B-spline of the same degree across the whole domain. The trajectory updates ΔT_t and Fusion module are described in functional terms but not in a way that clarifies how the curve parameters are adjusted. While the empirical results show the method works, this representation gap means the "principled" curve modeling claim is not fully supported by the exposition. The core idea is promising, but the paper needs to either formalize the accumulation or explicitly state that the network learns to compensate for any curve discontinuities, making the representation an architecture-driven approximation rather than a mathematically constructed one.

### Minor

- **No statistical uncertainty reported for any result.** All tables (Tables 1–4) report single numbers with no variance, confidence intervals, or multiple-seed evaluations. Training involves random initialization, data sampling, and event simulation. While single-run reporting is common in this area, the absence of any variance information makes it impossible to assess whether smaller margins (e.g., the 0.03 AJ gap between "w/ event" and "w/o event" on some settings in Table 7) are significant. Adding standard deviations over 3 seeds would substantially strengthen the paper's claims.

- **The continuous tracking comparison (Table 4) would benefit from directly placing the image-only ablation in the main table.** The paper compares against image-based methods that use linear interpolation for skipped frames, which the authors acknowledge "lack the ability to model inter-frame motion." The image-only variant of the authors' own method (from Table 7, ablation) does model continuous curves even without events and shows a more meaningful comparison. Including this row in Table 4 alongside CPFlow (the other curve-based method) would better isolate the benefit of events from the benefit of the curve accumulation itself. The ablation partially addresses this but is separated from the main comparison.

- **The motion extractor and event feature fusion are described at a high level without architectural specifics.** The paper states that "local correlations" are "augmented with event features" and processed by a "motion extractor" (line 70), but does not specify the architecture of these components (e.g., convolutional vs. transformer layers, number of refinements, how event features are injected into the correlation volume). Given that this is central to the local motion estimation, a short architectural description would improve reproducibility. This is a space-constraint issue and at most a minor gap.

### Trivial

- The degree p of the B-spline is mentioned but never specified numerically, even though N_c=4 is stated. This should be clarified for completeness.

## Nice-to-Haves

- The limitations section (line 185) is brief and focuses on speed and the lack of real event point tracking data. The paper could productively expand on what the current model fails at (e.g., fast rotational motion, heavy occlusion, scenes with very sparse events). This would help frame future work.

- The DSEC results (Table 3, two-frame optical flow) are tangential to the paper's main contribution (continuous point tracking). While they demonstrate adaptability, the "1st rank" framing could be softened since this is a different task. Adding a brief caveat would calibrate expectations.

## Removed Points

These points were identified in the inputs but have been removed with justifications:

1. **"CVO third and DAVIS quarter are never defined clearly"** — REMOVED because the paper explicitly defines these in Section 4.3 (line 167): "skip 1-frame (half) and 2-frames (one-third)" for CVO and "quarter at 3-frame intervals" for DAVIS. The critic's claim is factually incorrect.

2. **"Event grid representation is a reproducibility gap"** — REMOVED because the paper states "convert the raw event data into a dense grid representation (Rebecq et al., 2019)" (line 70), citing a standard published method. This is sufficient.

3. **"FE-TAP discussion is insufficient"** — REMOVED. The paper positions FE-TAP as "recover[ing] high-frame-rate point tracking from a fixed number of images and events... but does not take full advantage of the continuous nature of events" (line 41). This adequately explains the difference for a related work section.

4. **"DSEC table is garbled / unconvincing"** — REMOVED because the garbled table is a PDF parser artifact, not an author error. The claim of "1st rank" with specific EPE and AE numbers is a factual reporting of leaderboard results.

5. **"Missing appendix content / missing proofs"** — REMOVED because appendix content is stripped by the parser; these exist in the original submission.

6. **Formatting, typos, and presentation nitpicks** — REMOVED per policy (parser artifacts, not author errors).

7. **General area-of-concern sweeps** (e.g., "the evaluation lacks rigor" without concrete anchor) — REMOVED because they lack specific supporting evidence from the paper.

8. **Strength Finder generic strengths** (e.g., "this paper addresses an important problem") — REMOVED as they are generic/superficial and lack specific evidence beyond what is already captured in the retained strengths.

## Novel Insights

The review process surfaces a noteworthy tension: the paper's streaming curve accumulation is its most technically distinctive contribution, yet it is also its least formally specified component. The concatenation of local B-spline control points into a global curve without explicit knot vector management means the method is essentially learning to approximate a continuous global trajectory rather than constructing it from principled B-spline composition. This is not necessarily a flaw — the ablation in Table 6 validates that B-spline outperforms simpler motion assumptions — but it reframes the contribution: the real novelty may be in the learnable warping + offset + fusion mechanism (Eq. 1) that handles concatenation artifacts implicitly, rather than in the B-spline representation itself. This interplay between a theoretically motivated curve representation and a learned compensation for its composition gaps is an interesting design pattern that the paper does not explicitly acknowledge.

## Suggestions

1. **Clarify the B-spline accumulation.** Specify the degree p (e.g., p=3 as is standard for cubic B-splines). Describe whether the global trajectory is a single B-spline over the whole time domain or a piecewise concatenation. If it is a concatenation of independently defined local curves, state explicitly whether continuity (C⁰/C¹) at junctions is enforced by the architecture or learned.
2. **Report standard deviations.** Run the main evaluations (especially Tables 1, 2, and 4) with at least 3 seeds and report mean ± std.
3. **Move the image-only ablation into Table 4.** Place the "w/o event" row (currently in Table 7) into the main continuous tracking comparison table to directly isolate the benefit of events from the benefit of curve accumulation.
4. **Add a sentence on motion extractor architecture.** Specify whether it uses convolutional refinements, how many iterations, and how event features are fused with correlations.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>