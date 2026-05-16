Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces the first event-aided framework for spatially dense and temporally continuous point tracking. The core contribution is a streaming pipeline that estimates local curve trajectories from consecutive image-event pairs, then aggregates them into a global long-term trajectory via cross-attention and GRU-based motion representation fusion. The method achieves state-of-the-art results on the CVO and TAP-DAVIS benchmarks and ranks first on the DSEC optical flow leaderboard.

## Strengths

- **First integration of events for dense continuous point tracking.** The paper introduces a genuinely novel setup — using event data to recover continuous, parametric curve trajectories for every pixel over long video sequences. Prior image-only methods (DOT, SpatialTracker) operate at discrete frame intervals, while prior event-based methods (BFlow, CPFlow) are limited to a fixed small number of frames. The streaming accumulation of local curves into a global representation with arbitrary-length input is a clear advance.

- **Novel and well-motivated streaming architecture.** The global motion aggregation module (cross-attention + GRU between local and global motion representations, §3.2) is a principled way to fuse temporal information at the feature level rather than naively chaining optical flow fields. The ablation (Table 5) shows this outperforms both no temporal fusion (N/A) and post-processing aggregation (post) and short/long-term fusion (solo). The offset estimation and occlusion-aware warping (Eq. 1, §3.1) address real numerical challenges in curve accumulation.

- **Strong quantitative results across multiple benchmarks.** The method achieves the best reported results on CVO extended (0.19 EPE_all improvement over DOT), TAP-DAVIS (up to 2.7 AJ improvement), and ranks 1st on the DSEC optical flow leaderboard (0.05 EPE, 0.25 AE improvements). These gains are consistent across dense (CVO) and sparse (TAP-DAVIS) tracking settings, and across both simulated and real (DSEC) event data.

- **Self-supervised objectives using event and image consistency.** The event consistency loss (§3.3) that warps event chunks along estimated trajectories and enforces cross-chunk consistency is cleverly designed to exploit the continuous temporal signal in events. The ablation (Table 7) confirms it provides a meaningful improvement over discrete supervision alone.

## Weaknesses

### Fatal
None.

### Major

- **Missing baseline comparison with FE-TAP.** The paper cites FE-TAP (Liu et al., 2024) in §2.3 as a prior method that "recovers high-frame-rate point tracking from a fixed number of images and events" and acknowledges it as relevant work. Yet FE-TAP is never included in any experimental comparison (Tables 1, 2, 4, 5, 6, 7). Since FE-TAP is the closest existing method that also uses events for point tracking, its omission makes it impossible to determine whether the proposed global curve accumulation and streaming framework are necessary, or whether a simpler event-aided baseline would achieve similar gains. The paper's claim of being "the first event-aided point tracking framework" for dense tracking should be accompanied by a direct comparison or a concrete explanation (e.g., code not available, incompatible task definition) for why FE-TAP cannot be reasonably compared.

- **Continuous point tracking is validated only on simulated events; real-event validation is on a different task.** The paper's central thesis is that events enable *temporally continuous point tracking*, yet the continuous tracking evaluations (Tables 4–7, CVO and TAP-DAVIS) all use events simulated by vid2e. The real-captured event data (DSEC) is used only for two-frame optical flow — a fundamentally different and simpler task. The paper acknowledges this honestly in §4.4 ("Due to the lack of real captured event-based point tracking datasets ... we evaluate point tracking on standard video benchmarks with simulated events"), but the abstract and introduction present results on "simulated and real-world data" without clearly separating which claims are supported by real events. The disconnect undermines the strength of the contribution because the core benefit (events for continuous multi-frame tracking) is never demonstrated under real sensor noise, motion-dependent sparsity, and temporal correlations that simulators may not capture. Even a few qualitative curve trajectories on real event data (e.g., from DSEC) would partially address this.

### Minor

- **Event contribution in ablation is modest without statistical significance.** Table 7 shows that adding events improves EPE_all from 3.31 to 3.18 and OA from 0.905 to 0.916 on CVO third. These are small absolute gains, and no confidence intervals or multiple-seed runs are reported. Given that the event-aware method is substantially more complex than the image-only version, the reader cannot assess whether the improvement is statistically significant or within run-to-run variance. Reporting standard deviations across 3 seeds would significantly strengthen this claim.

- **Several architectural details are underspecified.** (a) How event features are fused with image features in the two-frame basis model (§3.2) is described only as "augment them with event features" — no fusion mechanism (concatenation, cross-attention, additive) is stated. (b) The cross-attention in §3.2 operates on motion representations with spatial dimensions, but the paper does not specify whether attention is computed globally over all pixel positions (prohibitively expensive) or at a lower resolution / with local windows. (c) The event consistency loss (§3.3) does not specify the number of chunks *B* or the range of random chunk intervals. (d) The "learnable module Fusion" for occluded points (Eq. 1) is described in a single sentence without architectural details. These omissions affect reproducibility and should be clarified.

- **No quantitative measure of trajectory continuity.** The paper claims "continuous" trajectories as a key advantage, but never directly measures temporal continuity (e.g., temporal smoothness of position derivatives, acceleration consistency, deviation from constant-velocity). The claim is supported only by the curve representation and the event consistency loss, but a direct metric would more convincingly demonstrate that the estimated trajectories are genuinely smoother or more physically plausible than linearly interpolated alternatives.

- **Continuous tracking ablations use short (third/quarter) settings only.** Tables 5–7 ablate on CVO third (2 of 7 frames skipped) and DAVIS quarter (3 of ~100 frames skipped), not on the full 48-frame CVO extended set. Since the global accumulation method is designed for long sequences, ablating on longer sequences would strengthen the validation.

- **Baseline results provenance is ambiguous.** The paper states experiments are "consistent with DOT" but does not explicitly state whether DOT and other baseline results are re-run under identical conditions or taken from original papers. Minor clarification needed.

### Trivial
None.

## Nice-to-Haves

- A comparison against FE-TAP (if code is available) or a more thorough discussion of why it is not comparable would resolve the most significant experimental gap.
- An evaluation on real event data for continuous (not just two-frame) tracking — even qualitative trajectory visualizations on DSEC or a custom capture — would directly support the paper's core claim.

## Removed Points

- *"The paper does not justify why linear is the appropriate default for interpolation"* — The paper states image-based baselines lack inter-frame motion modeling, making linear interpolation the natural default. This does not harm the paper's contribution and is standard practice. → Removed (not a genuine weakness).
- *"Batch size or training time per step not reported"* — 500k steps on 4×L40 GPUs with Adam optimizer and explicit learning rate schedule provides sufficient implementation detail for a conference paper. → Removed (trivial reproducibility nitpick beyond reasonable expectations).
- *"The claim 'first to enable...' is contestable given FE-TAP"* — The paper explicitly distinguishes itself from FE-TAP by noting FE-TAP uses a fixed number of images and does not model continuous inter-frame trajectories with parametric curves. The distinction is substantiated and reasonable. → Removed (strawman; the paper already addresses this).
- *"The complexity of the method makes reproducibility a concern"* — Generic reproducibility anxiety without specific missing details that the paper cannot reasonably include. → Removed.

## Novel Insights

The reviews reveal a key tension that is not fully resolved in the paper: the method's two main claimed advantages — (1) event-aided tracking and (2) streaming curve accumulation — are conflated in the experimental design. The ablation shows events help modestly, but the streaming curve framework itself (even without events, as the image-only ablation shows) may be the dominant source of improvement over DOT. The missing FE-TAP comparison is especially acute because FE-TAP, if re-implemented in a streaming fashion, could reveal whether events alone (without parametric curves) already solve most of the problem, or whether the curve representation is the critical enabler. The paper would benefit from explicitly disentangling these two axes of contribution.

## Suggestions

1. **Add FE-TAP as a baseline** in Tables 4 and 7, or provide a concrete, documented justification for why a fair comparison is infeasible (e.g., code unavailable, incompatible output format). If FE-TAP cannot be compared, state this clearly rather than leaving readers to infer the omission.

2. **Add a real-event continuous tracking experiment.** Even a qualitative evaluation — show curve trajectories on a few DSEC frames or a custom real event-camera capture — would greatly strengthen the central claim that events enable continuous tracking in practice, not only under simulation.

3. **Report statistical significance for the event ablation** (Table 7): run at least 3 seeds and report mean ± std for both image-only and event-aided settings. If the gain is within noise, hedge the claims about the "crucial role" of events.

4. **Specify architectural details** in a supplement or expanded paper: event-image fusion mechanism, spatial granularity of the cross-attention, chunking parameter *B* and interval ranges, and the architecture of the "Fusion" module for occluded points.

## Score and Decision

This paper tackles an important problem with a carefully designed framework and demonstrates consistent improvements over strong baselines. The streaming curve accumulation and global motion aggregation are genuine contributions. However, two issues prevent the evaluation from fully supporting the paper's stated claims: (1) the most relevant event-based baseline (FE-TAP) is never compared against, making it unclear whether the complexity of the proposed method is justified, and (2) the core claim of continuous tracking with events is validated only on simulated data. The paper is methodologically sound but incomplete in its current evaluation scope. With the missing baseline addressed, real-event validation added (or claims appropriately scoped), and the event ablation strengthened with error bars, this could be a strong contribution.

**Score:** 5.5

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>