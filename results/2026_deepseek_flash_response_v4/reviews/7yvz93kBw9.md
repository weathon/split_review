Now let me write the final consolidated review.

## Summary

This paper proposes D²GS, a method for sparse-view 3D Gaussian Splatting that addresses the observation that near-field regions tend to be overfit with too many Gaussians while far-field regions are underfit. Two complementary modules are introduced: DD-Drop (depth-and-density guided dropout) to suppress near-field overfitting, and DAFE (distance-aware fidelity enhancement) to boost far-field supervision using monocular depth masks. The paper also proposes an Inter-Model Robustness (IMR) metric to evaluate the stability of learned Gaussian distributions across independent training runs. Experiments on LLFF and Mip-NeRF360 show consistent improvements of 0.3–0.9 dB PSNR over strong baselines.

## Strengths

1. **Quantified diagnosis of spatial imbalance motivates the method.** Section 3.1 provides concrete numbers: near-field regions generate 11,450 Gaussians in the sparse-view model vs. 6,112 in the dense model (87% overshoot), while far-field regions produce only 3,082 vs. 5,224 (41% deficit). This directly supports the need for spatially adaptive dropout and far-field enhancement.

2. **Granular ablation isolates every component's contribution.** Table 4 decomposes the full 2.13 dB PSNR gain (19.22 → 21.35) into five incremental additions — density score alone with layering (+1.80), depth score alone with layering (+1.70), combined scores without layering (+1.88), combined scores with layering (+1.95), and finally DAFE (+0.18). All metrics (PSNR, SSIM, LPIPS, IMR) improve monotonically as components are added, confirming the improvements are complementary rather than from a single trick.

3. **Consistent SOTA results across datasets and metrics.** On LLFF 1/8 resolution, D²GS outperforms 11 prior methods on PSNR (21.35 vs. next-best 20.85), SSIM (0.746 vs. 0.717), LPIPS (0.179 vs. 0.196), and AVGE (0.087 vs. 0.092). On Mip-NeRF360, it leads on all four metrics as well (20.09 PSNR vs. next-best 19.74). The advantage holds at both 1/8 and 1/4 resolutions.

4. **Demonstrated robustness to choice of depth estimator.** Table 6 shows DAFE yields consistent improvements across three different monocular depth estimators (MiDas: 21.21 PSNR, DPT: 21.27, DepthAnything V2: 21.35), indicating the method is not brittlely dependent on a specific depth prior.

## Weaknesses

### Major

1. **IMR is presented as a core contribution but lacks basic validation.** The Inter-Model Robustness metric is listed as the paper's third main contribution (contribution 3 in Section 1), yet several concerns are unaddressed:

   - **No variance reported for a metric about variance.** Table 3 reports IMR as a point estimate (e.g., D²GS: 3.039 on 3-view), but since IMR measures dispersion across training runs, the uncertainty in the IMR estimate itself is critical. Without error bars, it is impossible to know whether the differences between methods (e.g., 3.039 vs. 3.136) are significant.
   - **Counterintuitive pattern not discussed.** For D²GS, IMR is *better* (lower) on 3-view (3.039) than on 6-view (3.109). The same holds for DropGaussian (3.205 vs. 3.143). More training views would generally be expected to increase stability, not decrease it. The paper offers no explanation.
   - **No correlation analysis with image-space metrics.** If IMR is proposed as a complementary evaluation tool, the paper should at minimum show that it captures something meaningful about rendering quality or stability that PSNR/SSIM/LPIPS miss, or that lower IMR corresponds to better rendering across runs.

   These issues do not invalidate the method itself, but they mean the IMR claim is not yet supportable as a core contribution. The paper would be stronger if it either validated IMR convincingly or presented it as a preliminary proposal rather than a headline contribution.

2. **Inconsistency between Figure 2 and the DAFE formulation.** The Figure 2 caption defines DAFE with three separate losses and three weights: **L_DAFE = λ_near L_near + λ_mid L_mid + λ_far L_far**. However, Section 3.3 (Eqs. 4–5) defines DAFE as a single binary-masked loss on far-field pixels only, with **no** λ_near, λ_mid, L_near, or L_mid anywhere in the equations. The total loss (Eq. 6) adds a single λ_DAFE·L_DAFE term. This discrepancy — between a three-region, three-loss formulation in the figure and a single binary-mask loss in the text — creates real confusion about what the method actually does.

3. **No error bars on any main results.** Tables 1 and 2 report all metrics as point estimates with no standard deviations or confidence intervals. The paper itself documents significant run-to-run instability in sparse-view 3DGS (Figure 3 left shows PSNR fluctuating from 14.62 to 18.63 across 10 runs of a prior method). Given this acknowledged variance, reporting main results without error bars undermines the reader's ability to assess the reliability of the claimed improvements.

### Minor

4. **Mip-NeRF360 view count is never specified.** The paper evaluates on Mip-NeRF360 (Table 2) but never states how many input views were used. The LLFF experiments explicitly use 3-view and 6-view settings; Mip-NeRF360 results are reported without this information, making them impossible to reproduce or contextualize.

5. **Several implementation details are missing.** The k-nearest-neighbors parameter *k* for density estimation (Section 3.2) is never reported. The depth thresholds D_near and D_middle are defined as "the first and second tertiles of the depth distribution" — it is unclear whether this refers to SfM point depths, Gaussian-to-camera distances, or something else. For the depth score d̃_i, which uses "Euclidean distance to the camera" — with multiple training cameras, it is not specified whether this is the distance to the nearest camera, the average, or some other aggregation.

6. **Baseline ambiguity in Table 4.** The baseline row (no components) reports 19.22 PSNR, which matches vanilla 3DGS from Table 1. Yet the paper states the implementation is "built on DropGaussian" (Section 4). It should clarify whether the baseline is vanilla 3DGS, DropGaussian with all modifications removed, or something else. The PSNR value suggests vanilla 3DGS, but this should be stated explicitly.

7. **No control for simple far-field L1 up-weighting without depth.** The DAFE module uses a monocular depth estimator to create a mask. A useful control experiment would be to compare against simply increasing the global L1 loss weight (without depth-based masking) to determine whether the depth estimation provides value beyond a loss-weighting adjustment.

### Trivial

- None.

## Nice-to-Haves

- Analyze whether DD-Drop and DAFE interact synergistically or interfere (e.g., removing near-field Gaussians could affect far-field rendering through projection overlap).
- Expand the diagnostic analysis (Section 3.1) beyond a single example scene to systematically show Gaussian count as a function of depth across all scenes.

## Removed Points

These points were considered but removed as non-substantive or factually incorrect:

- **"The first-order Taylor expansion of the Bures metric is unnecessary because 3×3 matrix square roots are cheap."** — Removed because the approximation is stated as also improving numerical stability, and for large numbers of Gaussian pairs the cumulative savings can be meaningful. The paper also defers the derivation to the appendix, which is standard practice.
- **"The IMR formula (Eq. 14) is ad-hoc without justification."** — Removed. The ratio of sum-of-squares to sum penalizes large pairwise distances more heavily, and the log makes the metric scale-invariant. This is a reasonable design choice even if not derived from first principles.
- **"The paper should compare against feed-forward methods like PixelSplat/MVSplat."** — Removed because the paper is in a different paradigm (per-scene optimization vs. feed-forward), as the reviewer themselves acknowledged.
- **"DAFE is just a per-pixel loss weighting, not a 'module'."** — Removed. The framing is standard for the field; many papers refer to loss modifications as "modules."
- **Strength: "Novel 3D-distribution-based robustness metric with evidence of diagnostic value"** — Removed because the IMR validation is incomplete (see Weakness 1), so claiming it as a strength overstates the evidence.
- **Strength: "Systematic hyperparameter exploration"** — Removed as the exploration is standard ablation practice without particular insight beyond the optimal values found.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses confirm the paper's core framing — that spatial imbalance in Gaussian distributions is a genuine problem and that the proposed two-component solution is reasonable and well-ablated — but raise valid concerns about overclaiming on the IMR metric and inconsistencies in presentation. No reviewer identified a previously unrecognized dimension of the problem or a connection the paper itself does not make.

## Suggestions

- **Either validate IMR properly or downgrade its status.** Specifically: (a) report IMR with error bars (bootstrapped or across runs); (b) show that IMR correlates with rendering quality variance across runs; (c) explain the counterintuitive 3-view vs. 6-view pattern; or (d) remove IMR from the core contribution claims and present it as a preliminary proposal.
- **Fix the Figure 2 vs. Section 3.3 discrepancy.** Either update the figure to match the binary-mask formulation or, if a three-region version was actually used, provide the correct equations.
- **Add error bars (standard deviations or confidence intervals) to all main quantitative results** (Tables 1, 2, 3), given the instability documented in Figure 3.
- **Explicitly state the view count for Mip-NeRF360** and clarify which depth distribution is used for the tertile thresholds.

## Score and Decision

**Calibration anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| I86z54CL2y (GeoGS3D) | 3.40 | 1 | Weak anchor — single-view 3D reconstruction, rejected. D²GS is clearly stronger. |
| rWIrdAo2xC | 2.83 | 1 | Weak anchor — monocular 3D human rendering, rejected. D²GS is clearly stronger. |
| AMVLOv30Qg (360-InpaintR) | 3.33 | 1 | Weak anchor — 3D inpainting, rejected. D²GS is clearly stronger. |
| P4o9akekdf (NoPoSplat) | 8.00 | 1 | Strong anchor — feed-forward unposed 3DGS, accepted. D²GS is less ambitious (per-scene optimization) and has overclaiming issues. D²GS is below this level. |
| vkj5ARRCeY (IBGS) | 5.75 | 1,2 | Middle anchor — geometry regularization for 3DGS, rejected. Similar pattern of solid method with overstated claims. D²GS has stronger empirical evidence (better ablation, clearer gains) and is slightly above this paper. |
| R9lgWYE508 (RAIN-GS) | 5.75 | 1,2 | Middle anchor — initialization relaxation for 3DGS, rejected. D²GS has clearer motivation and stronger results. D²GS is above this paper. |
| SBzIbJojs8 (HiSplat) | 6.00 | 2 | Strongest middle anchor — feed-forward hierarchical 3DGS for sparse views, accepted. D²GS is slightly below HiSplat due to less ambitious paradigm and overclaiming issues, but comparable overall quality given the thorough ablation. |

**Round 1 (bracketing):** The paper sits well above the weak anchors (2.83–3.40) and clearly below the strong anchors (7.60–8.00). The plausible range was [5.0, 7.0].

**Round 2 (narrowing):** Compared against 5.75-level papers (rejected) and the 6.0 HiSplat paper (accepted), D²GS sits between them — stronger than RAIN-GS/IBGS (5.75) in terms of empirical validation and clarity of motivation, but slightly weaker than HiSplat (6.0) due to the IMR overclaiming and presentation inconsistencies. The narrowing placed the paper at **6.0**.

**Final score: 6.0.** The core contribution — DD-Drop + DAFE for addressing spatial imbalance in sparse-view 3DGS — is sound, well-motivated, and consistently supported by ablation evidence. The method achieves genuine SOTA results on standard benchmarks. However, the paper overclaims in presenting the IMR metric as a core contribution without proper validation, and contains a notable inconsistency between Figure 2 and the DAFE equations. These issues are fixable and do not invalidate the method, but they weaken the paper's claim structure in its current form. **Decision: Accept** — the paper has a solid core contribution that the community would benefit from, and the identified issues are addressable during the revision process.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>