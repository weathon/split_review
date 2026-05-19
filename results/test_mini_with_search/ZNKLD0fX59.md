Now I have sufficient calibration data. Let me write the final consolidated review.

---

## Summary

CasualHDR proposes a one-stage 3D Gaussian Splatting framework for reconstructing HDR 3D scenes from casually captured videos that exhibit auto-exposure variation, motion blur, and unknown exposure times. The core idea is a unified differentiable physical imaging model that jointly optimizes exposure time, camera response function (CRF), a continuous-time SE(3) camera trajectory, and the HDR 3DGS scene representation. The coupling between motion blur (which depends on exposure time) and brightness (which also depends on exposure time) provides mutual constraints that allow exposure time to be optimized without ground-truth values. Experiments on synthetic and real datasets show substantial improvements over baselines including HDR-NeRF, HDR-Plenoxels, Gaussian-W, BAD-Gaussians, and vanilla 3DGS.

## Strengths

1. **Well-motivated and practically important problem.** Addressing HDR 3D reconstruction from casually captured video (auto-exposure, motion blur, unknown exposure times) is a genuine gap. Existing HDR-3D methods require fixed multi-exposure setups with known exposure times, and existing deblurring methods don't handle exposure variation. The paper's key insight — that motion blur and brightness both depend on exposure time, providing a natural constraint for joint optimization — is physically sound and elegantly exploited.

2. **Strong empirical results with large margins over baselines.** The reported gains are substantial: CasualHDR (even with random exposure initialization) outperforms all baselines by large margins on both synthetic (e.g., 31.51 vs. 18.77 PSNR on Factory) and real datasets. The ablation study (Table 6) attributes specific contributions to each component: continuous trajectory (+24% PSNR), exposure+CRF (+42% PSNR), and deblur module (+9% PSNR). These are large, interpretable improvements.

3. **Methodologically sound unified formulation.** The coupling of continuous-time SE(3) B-spline trajectory (Section 3.2) with the physical imaging model (Section 3.3) is technically well-executed. Using cumulative B-splines for the global trajectory (rather than per-frame independent splines as in BAD-NeRF) allows cross-frame motion constraints, which is conceptually cleaner for video input. The ablation showing lower ATE than HLoc, DPV-SLAM, and BAD-Gaussians validates that the joint pose optimization actually improves trajectory estimation.

4. **Dataset contribution.** The CasualVideo dataset (RealSense + Smartphone subsets) with hardware-logged exposure times and Vicon ground-truth poses provides a useful benchmark. The synthetic Blender pipeline with controlled motion blur and exposure variation is also valuable for reproducible evaluation.

5. **Downstream applications demonstrated.** The method naturally supports deblurring (Table 3 shows clear gains over BAD-Gaussians) and HDR editing (Figure 3 shows adjustable exposure times post-reconstruction), going beyond standard NVS evaluation.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative HDR evaluation despite available ground truth.** The paper's central claim is HDR scene reconstruction, yet all quantitative metrics (PSNR, SSIM, LPIPS) are computed on tone-mapped LDR images. Two HDR scenes that differ in radiance can produce similar LDR outputs after tone mapping. The synthetic dataset has known HDR ground truth (the paper describes generating "sharp HDR images" before tone mapping — Section 4.1), so computing HDR-specific metrics (e.g., PU-PSNR, HDR-VDP-3) would be straightforward. Their absence weakens the core HDR claim. This gap is acknowledged in the HDR-NVS literature broadly (even strong papers like Mono4DGS-HDR received the same criticism), but given that the paper's headline contribution is HDR reconstruction, this needs to be addressed.

### Minor

2. **Exposure time optimization is claimed but not validated against ground truth.** The paper states (Section 3.3, line 111) that exposure time "will be gradually optimized to the actual value," and this is a key enabler of the method (allowing random initialization). However, no plot, table, or analysis compares optimized exposure times to the hardware-logged ground truth (which the paper explicitly states was collected — Section 4.1, line 145). The ablation (Table 6) combines exposure optimization with CRF learning into a single toggle, so the isolated effect of exposure time optimization is not quantified. Showing even a simple scatter plot of optimized vs. ground-truth exposure times for synthetic data or RealSense sequences would significantly strengthen the claim that the optimization is physically meaningful.

3. **Baseline input specification could be clearer.** While the paper describes its own initialization pipeline (HLoc for synthetic/RealSense, DPV-SLAM for ScanNet/Smartphone — Section 4.2), it does not explicitly state what inputs each baseline method received. In particular: did HDR-NeRF receive the measured exposure times (which were available — line 145) on real data before it "failed"? What pose initializations were used for each baseline? These details matter for interpreting the reported performance gaps. The ambiguity doesn't invalidate the results (the improvements are large enough to likely persist), but it makes fair comparison harder to assess.

4. **Ablation baseline not explicitly defined.** Table 6 reports percentage improvements from adding each module, but the "without" configuration is not formally defined. For example, the "Conti. Traj." ablation removes continuous trajectory — is the baseline using per-frame independent poses (vanilla 3DGS-style) or per-frame short splines (BAD-Gaussians-style)? The improvement is large (24%), but whether this comes from the global spline structure or simply from having more pose parameters is unclear without a clearer baseline specification. This is addressable with one sentence in the ablation text.

### Trivial

5. **No limitations section.** The paper would benefit from a brief discussion of: the constant-velocity assumption during exposure (mentioned in Section 3.3 but not discussed as a limitation), sensitivity to the number of virtual samples N, the fact that CRF is scene-specific and does not generalize across cameras, and scenarios with non-constant camera motion (acceleration, vibration).

## Nice-to-Haves

- Compare the global B-spline trajectory against per-frame short B-splines (as in BAD-Gaussians) in the ablation to better isolate the benefit of the global representation.
- Report training/rendering times relative to baselines to assess practicality.
- Add a brief comment on whether the mapping from (blur kernel, brightness, CRF) to (exposure time, trajectory) is identifiable — i.e., discuss the observability of exposure time given the model.

## Removed Points

- **"Baseline comparison fairness is insufficiently documented (structural/evidential)"** (harsh critic point 1, re: HDR-NeRF failure with/without exposure times): While the paper could be more explicit, it does state that ground-truth exposure times were extracted from hardware (line 145) and that HDR-NeRF "failed in all scenes on the real dataset" (line 168). The phrasing "Unlike HDR-NeRF, our method can learn ... without measured exposure times" strongly implies HDR-NeRF was run with measured times and still failed. The concern about pose initialization is partially addressed (Section 4.2 explains the initialization used). This is more of a reporting clarity issue than a structural flaw, so I demote it from the harsh critic's "structural" framing to the Minor weakness #3 above.

- **"Ablation design conflates multiple changes"** (harsh critic point 4, re: trajectory ablation not distinguishing global spline vs. per-frame poses): The natural baseline for "no continuous trajectory" is discrete per-frame poses, which is standard. The reviewer's request for per-frame short B-splines as a comparison is reasonable but not a core flaw — it is a nice-to-have refinement. I demote this to Minor weakness #4 above, as the percentage improvement reported is still informative even if the baseline could be better specified.

- **Strength Finder strengths about "importance of the research question" and "the paper addresses a clear gap"**: These are true but generic. I retain the concrete evidence-based strengths above and move these generic framings here.
- **Strength Finder strength about the method being "first to handle X"** — the paper does not claim to be the first to handle all of these simultaneously (it says "first one-stage method"), and concurrent work I²-SLAM exists. I have reframed this as a well-motivated problem rather than a "first" claim.
- Criticisms about missing appendix content (CRF MLP architecture, ScanNet results): The parser strips supplementary material. These cannot be evaluated.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is how the harsh critic's three main concerns (HDR metrics, exposure time validation, baseline documentation) all stem from the same root cause: the paper evaluates the *output* of the pipeline (LDR images) rather than the *internal variables* (HDR radiance, exposure time estimates). The method's strength is its physically grounded optimization; validating those physical quantities directly would not only address the evaluation gaps but also provide stronger evidence that the optimization converges to physically meaningful values rather than just fitting the data. This suggests a broader lesson for papers that couple physical model parameters with neural scene representations: when the model makes claims about latent physical quantities (exposure time, CRF), those quantities should be directly validated when ground truth is available, not just evaluated through the final rendered image quality.

## Suggestions

1. **On synthetic data** (where HDR ground truth exists), compute PU-PSNR or HDR-VDP-3 between recovered HDR radiance and ground truth. This directly validates the HDR claim.
2. **Plot optimized exposure times against ground truth** for the synthetic and RealSense sequences. A scatter plot with R² correlation would confirm the optimization recovers physically meaningful values.
3. **Add a table specifying per-baseline inputs**: exposure time provided (yes/no), pose initialization method, input image type (blurry/sharp). This resolves the fairness ambiguity.
4. **Frame the ablation baseline explicitly**: e.g., "The baseline in Table 6 removes the indicated component while keeping all others fixed. For Conti. Traj., the baseline uses per-frame independent poses."
5. **Add a limitations paragraph** discussing the constant-velocity assumption, scene-specific CRF, and sensitivity to initialization quality.

## Calibration Report

**Round 1 (Bracketing):** Queried for HDR 3D reconstruction + novel view synthesis topics. Low band (≤3.0) returned papers like "High-Fidelity 3D Scene Representation via HDR-Integrated Multi-Constraint Neural Rendering" (3.00, Reject) — papers with fundamentally flawed methodology or insufficient novelty. Middle band (4.0–7.0) returned HDR-4DGS (5.50, Accept Poster), HDR-NSFF (5.00, Accept Poster), Mono4DGS-HDR (7.00, Accept Poster), and Expo-GS (4.50, Reject). High band (≥8.0) returned text-to-3D and geometry learning papers (8.00–8.50) — clearly in a different tier. Initial bracket: 5.0–7.0.

**Round 2 (Narrowing):** Queried within [4.5, 6.0] and [6.0, 7.5] on "3D Gaussian splatting HDR reconstruction casual video motion blur." Retrieved USplat4D (5.00, Accept Poster), FAGS (5.50, Accept Poster), StreamSplat (6.67, Accept Poster), and revisited Mono4DGS-HDR (7.00, Accept Poster).

**Final placement:** CasualHDR is stronger than Expo-GS (4.50, Reject) which suffered from limited novelty and limited baselines. It is comparable to HDR-4DGS (5.50) — both have the same HDR metric gap — but CasualHDR addresses a more practical problem (casual video with blur vs. multi-view static LDR). It is weaker than Mono4DGS-HDR (7.00) which has more polished evaluation, a stronger "first-to-solve" narrative, and cleaner ablations. The main weaknesses (HDR metrics, exposure time validation, baseline clarity) are fixable evaluation gaps, not methodological flaws. Score: **5.5**, Decision: **Accept**.

### Anchors consulted

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Wt5CiB27af.md | 3.00 | R1 | Weaker — fundamental methodology issues |
| guUaZN0kyC.md | 2.50 | R1 | Weaker — different problem (image-to-3D) |
| 3dNKozB8U7.md | 3.00 | R1 | Weaker — feature consistency in 4DGS |
| imblpbUryY.md | 2.67 | R1 | Weaker — geometry rectification, not HDR |
| 10iBNwPtl2.md | 5.50 | R1,R2 | Similar — both have HDR metric gap, CasualHDR has more practical problem |
| MoRmmDiKAo.md | 5.00 | R1 | Slightly weaker — uses outdated NSFF, 10+hr training |
| 9ZrjgzlAuh.md | 7.00 | R1,R2 | Stronger — cleaner evaluation, two-stage pipeline |
| PxMtWs9bet.md | 4.50 | R1 | Weaker — limited novelty, limited baselines |
| m3rZ7Fdlst.md | 5.00 | R2 | Comparable — both have moderate evaluation gaps |
| UZ00ac4eqA.md | 5.50 | R2 | Comparable — similar tier of contribution |
| SaiDRQU7Ez.md | 6.67 | R2 | Stronger — feed-forward, real-time, more polished |
| 51JEkjP0gF.md | 6.00 | R2 | Stronger — broader theoretical contribution |

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>