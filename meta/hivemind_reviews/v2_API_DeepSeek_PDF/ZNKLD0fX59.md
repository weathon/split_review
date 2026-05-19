## Summary
# Final Review Report

## Summary

This paper proposes CasualHDR, a unified framework for reconstructing high dynamic range (HDR) 3D scenes from casually captured videos with auto-exposure enabled, motion blur, and unknown varying exposure times. The method jointly optimizes four components through a differentiable physical imaging model: a continuous-time SE(3) camera trajectory (via cumulative B-spline), per-frame exposure time, per-channel camera response function (CRF), and a 3D Gaussian Splatting (3DGS) representation of the HDR scene. The key insight is that motion blur and image brightness are both coupled through exposure time, enabling joint optimization without ground-truth exposure metadata.

The paper contributes: (1) a joint optimization framework that handles exposure-varying, motion-blurred casual video input; (2) a small-scale benchmark dataset (4 synthetic + 6 real sequences) with exposure variation and ground-truth labels; (3) empirical results showing consistent improvements over prior methods (HDR-NeRF, HDR-Plenoxels, Gaussian-W, BAD-Gaussians) on novel-view synthesis, deblurring, and pose estimation tasks. Downstream applications include exposure editing and image deblurring.

**Overall Assessment:** The paper tackles a practically important and technically challenging problem — reconstructing HDR 3D scenes from imperfect casual video. The core idea (coupling exposure time, motion blur, and CRF via a unified imaging model) is sound and the engineering integration of continuous-time trajectory with 3DGS is novel in this context. However, the manuscript has several significant weaknesses: (a) missing statistical variance for all experimental results, (b) unclear train/test splits with potential selection bias in real-world evaluation, (c) reproducibility gaps in optimization hyperparameters, (d) unsupported SOTA claims without external literature verification, and (e) absence of limitations discussion. These issues reduce confidence in the reported gains but are fixable with additional experiments and writing revisions.

## Strengths
1. **Practically important problem formulation.** The paper targets a realistic and underexplored scenario: reconstructing HDR 3D scenes from casually captured video with auto-exposure, where exposure times are unknown and motion blur is present. This directly addresses a gap between controlled multi-exposure HDR reconstruction and everyday consumer-grade capture.

2. **Sound technical intuition.** The core idea — that motion blur and brightness are coupled through exposure time, so optimizing exposure from blur provides mutual constraints — is physically grounded and elegantly connects two previously separate research threads (HDR reconstruction and deblurring 3D reconstruction). The unified differentiable imaging model that jointly optimizes trajectory, exposure, CRF, and scene representation is technically coherent.

3. **Strong empirical results on comparative baselines.** Across 4 synthetic scenes and 6 real-world sequences, CasualHDR (both with random and ground-truth exposure initialization) consistently outperforms HDR-NeRF, HDR-Plenoxels, Gaussian-W, and BAD-Gaussians on PSNR, SSIM, and LPIPS for novel-view synthesis. The gains are often substantial (e.g., 5-10 dB PSNR improvement over baselines on synthetic datasets), suggesting the method captures meaningful signal beyond incremental improvements.

4. **Comprehensive evaluation across multiple tasks.** The paper evaluates not only novel-view synthesis quality but also image deblurring (PSNR/SSIM/LPIPS on synthetic, BRISQUE on ScanNet) and pose estimation accuracy (ATE on Vicon ground truth). This multi-task evaluation strengthens the claim that joint optimization benefits all three objectives simultaneously.

5. **Ablation study demonstrating component contributions.** Table 6 provides a component-wise ablation showing that each module (continuous trajectory, exposure optimization, CRF, deblur aggregation) contributes to overall performance. The ablation on spline control knot ratio (Table 5) adds practical guidance for balancing accuracy and computational cost.

## Weaknesses
1. **Missing statistical significance and variance reporting (Major).** All quantitative results (Tables 1-9) are reported as single-run point estimates without standard deviation or confidence intervals. For ATE results in Table 4, the standard deviations equal or exceed the mean values (e.g., Girls-vicon: 0.8294±0.8834 for CasualHDR-random), indicating high variability that makes reported improvements unreliable. Without multi-seed experiments and significance tests, the claimed "superior performance" cannot be distinguished from optimization noise or favorable initialization.

2. **Unclear evaluation protocol with potential selection bias (Major).** The paper selects "5 to 10 sharp images for each sequence to evaluate metric" (Page 7, Section 4.4) from real-world datasets. The criteria for "sharp" selection are subjective and not specified. If these images were part of the training set, the evaluation measures reconstruction rather than generalization. The train/test split is not clearly documented for any real-world sequence, making it difficult to interpret the reported novel-view synthesis metrics.

3. **Critical reproducibility gaps (Major).** The implementation details (Section 4.2) omit essential hyperparameters: (a) learning rates for CRF MLPs, exposure times, and trajectory control knots are not specified; (b) MCMC densification parameters differ from standard 3DGS adaptive density control but no details are given; (c) training iterations/convergence criteria are not stated; (d) the number of Gaussian primitives after optimization is not reported. These omissions prevent independent verification of results.

4. **Unsupported SOTA and generalization claims (Major).** The paper claims "state-of-the-art performance across all datasets" (Page 3, contribution list) without external literature verification. With Retrieval-Disabled Mode active, we cannot confirm whether the strongest baselines were included. The Abstract and Conclusion use "high robustness" and "superior performance" without bounding these claims to the specific tested conditions.

5. **Ablation percentage claims not precisely traceable (Major).** Section 4.6 states "24% improvement in PSNR" from continuous trajectory, "42% from jointly optimizing exposure time and CRF", and "9% from motion blur modeling." A direct verification against Table 6 shows these percentages do not cleanly map to any specific pairwise row comparison, making them potentially misleading.

6. **Conclusion lacks limitations discussion (Major).** The Conclusion does not discuss any failure cases, boundary conditions, or limitations of the proposed method. This is a significant omission — every paper should candidly discuss when and why the method might fail (e.g., rapid camera motion violating constant-velocity assumption, extreme dynamic range, low-light high-noise conditions).

7. **Related Work is a list rather than cumulative positioning (Moderate).** Sections 2.1-2.3 present three independent literature surveys organized chronologically rather than thematically. They do not build a cumulative argument about where the paper sits in the research landscape, and the gaps that motivate CasualHDR are stated weakly or at the end of paragraphs.

8. **Dataset scale is modest (Moderate).** The synthetic dataset contains 4 scenes × 77 frames each. The real dataset contains 6 sequences of varying lengths. While appropriate for a methods paper, the paper should acknowledge that broader generalization (e.g., to indoor/outdoor, dynamic scenes, different camera hardware) requires larger-scale evaluation.

## Key Issues
### K1: Statistical Under-Reporting (Severity: Major | Validity Risk: High)
No variance/confidence intervals are reported for any metric across the entire paper. The ATE results in Table 4 have standard deviations comparable to or exceeding the means (e.g., Girls-vicon: 0.8294±0.8834 for CasualHDR-random), making the reported improvements over baselines inconclusive without significance testing. This undermines the core claim that CasualHDR "outperforms" prior methods.

**Fix:** Run all experiments with ≥3 random seeds, report mean±std. Add paired significance tests between CasualHDR and the strongest baseline per dataset. For ATE, also report median and percentage of frames below a trajectory error threshold.

### K2: Evaluation Protocol Ambiguity (Severity: Major | Validity Risk: High)
The paper selects "5 to 10 sharp images" per real sequence for evaluation without specifying selection criteria or train/test splits. This introduces potential selection bias and makes the reported novel-view synthesis metrics unverifiable.

**Fix:** (a) Explicitly state train/test splits for every dataset. (b) Define objective sharpness criteria (e.g., Laplacian variance > threshold) if only sharp frames are used for testing. (c) Either evaluate on ALL held-out frames or justify why only sharp frames are appropriate and ensure they are excluded from training.

### K3: Reproducibility Gap (Severity: Major | Validity Risk: High)
Key optimization hyperparameters (learning rates for each parameter group, MCMC densification details, training iterations, convergence criteria) are not reported. Since joint optimization of heterogeneous quantities is sensitive to relative learning rates, this prevents reproduction and limits confidence in the results.

**Fix:** Add a dedicated hyperparameter table reporting LR for Gaussian primitives (subdivided by position/scale/rotation/opacity/SH), CRF MLPs, trajectory control knots, and exposure scalars. Report MCMC parameters (initial Gaussian count, densification interval, pruning threshold) and total training iterations.

### K4: Unsupported SOTA and Certainty Overclaim (Severity: Major | Novelty Risk: Moderate)
The contribution list claims "state-of-the-art performance across all datasets" without external literature verification. The Conclusion uses unqualified "high robustness and flexibility." These claims exceed the scope of evidence presented.

**Fix:** Replace "state-of-the-art" with "our method outperforms the compared baselines on the evaluated datasets." Replace "high robustness" with specific, bounded robustness claims (e.g., "robust to unknown exposure time and motion blur under the tested conditions").

### K5: Missing Limitations and Failure Mode Analysis (Severity: Major | Scientific Completeness)
The paper lacks any discussion of limitations, failure cases, or boundary conditions. This is a significant omission for a scientific publication and reduces the paper's value to the community.

**Fix:** Add a "Limitations" subsection to the Conclusion discussing: (a) constant-velocity assumption during exposure may fail under rapid camera motion; (b) B-spline trajectory adds memory overhead; (c) independent per-channel CRF MLPs may not enforce cross-channel consistency; (d) extreme dynamic range conditions remain untested.

### K6: Ablation Percentage Claims Not Traceable (Severity: Major | Factual Accuracy Risk)
The claimed improvements (24%, 42%, 9%) in Section 4.6 do not cleanly match specific pairwise comparisons in Table 6. The ablation also conflates multiple factors simultaneously rather than isolating single components.

**Fix:** For each claimed percentage, cite the exact row comparison (Row X vs Row Y). Add single-factor ablations where exactly one component is added while holding all others fixed. Add a "Delta" column to Table 6 showing improvement relative to a consistent baseline.

## Actionable Suggestions
### S1: Add Statistical Variance to All Reported Metrics (P0 — Must)
**Applies to:** Tables 1-9, Section 4.4, Section 4.5
**Action:** For every experiment, run with a minimum of 3 random seeds (different Gaussian initialization, different train/test split seeds where applicable). Report mean ± standard deviation. For the ATE metric (Table 4), add median ATE and percentage of frames below an error threshold (e.g., 0.5m). For PSNR/SSIM/LPIPS gains, add paired bootstrap confidence intervals or report p-values from a paired t-test against the strongest baseline.
**Expected impact:** Converts qualitative "consistently outperforms" into statistically validated claims. Without this, the core empirical contribution is not fully supported.

### S2: Clarify Evaluation Protocol and Train/Test Splits (P0 — Must)
**Applies to:** Section 4.1, Section 4.4
**Action:** 
(a) For every real-world sequence, specify: total frames, training frames, test frames, and which frames are excluded from training for novel-view synthesis evaluation.
(b) Define the sharpness selection criteria objectively (e.g., Laplacian variance > τ; report τ value).
(c) If sharp test frames were part of the training set, report results on truly held-out frames separately.
**Expected impact:** Resolves ambiguity about whether the paper measures reconstruction or generalization. This is critical for interpreting the results.

### S3: Add Optimization Hyperparameters (P0 — Must)
**Applies to:** Section 4.2
**Action:** Add a "Training Hyperparameters" paragraph or table that reports:
- Learning rates for each parameter group: Gaussian primitives (subdivided), CRF MLPs, trajectory control knots, exposure scalars
- Number of training iterations and convergence criterion (loss plateau threshold)
- MCMC densification parameters: initial count, densification interval, pruning threshold
- CRF MLP architecture: depth, width, activation function
- Warm-up schedule, if any
**Expected impact:** Enables reproducibility, which is a minimum bar for acceptance.

### S4: Rewrite Contribution Claims and SOTA Language (P0 — Must)
**Applies to:** Page 3 (contributions), Abstract, Conclusion
**Action:** 
Replace "state-of-the-art performance across all datasets" → "our method outperforms the compared baselines on the evaluated synthetic and real-world datasets."
Replace "high robustness" → "improved robustness to unknown exposure time and motion blur under the tested conditions."
**Expected impact:** Aligns claims with evidence, prevents reviewer pushback on overclaiming.

### S5: Add Limitations Subsection (P1 — Must)
**Applies to:** Conclusion (Section 5)
**Action:** Add 3-5 sentences discussing specific limitations: (a) constant-velocity assumption during exposure; (b) B-spline memory scaling with video length; (c) independent per-channel CRF; (d) untested extreme dynamic range conditions; (e) reliance on initial pose estimates from HLoc/DPV-SLAM.
**Expected impact:** Demonstrates scientific maturity and helps reviewers trust the paper's claims.

### S6: Improve Ablation Traceability (P1 — Must)
**Applies to:** Section 4.6, Table 6
**Action:** (a) In the text, cite exact row comparisons for each percentage (e.g., "Rows 1→3: continuous trajectory improves PSNR from 15.14 to 19.13 (+26%)"). (b) Add a "Δ vs Baseline" column. (c) Include single-factor ablations where exactly one component is toggled while others are held fixed.
**Expected impact:** Converts vague percentages into verifiable quantitative claims.

### S7: Restructure Related Work Around Thematic Axes (P2 — Nice-to-have)
**Applies to:** Section 2
**Action:** Reorganize into three thematic subsections: (1) HDR 3D reconstruction from controlled inputs (limitation: assumes known static exposures), (2) Deblurring 3D reconstruction (limitation: assumes consistent photometric response), (3) Appearance-robust NVS (limitation: LDR only, no HDR scene representation). Each subsection ends with one concrete gap that CasualHDR fills.
**Expected impact:** Stronger narrative positioning and clearer statement of intellectual contribution.

### S8: Add Sensitivity Analysis on λ_exp and N (P2 — Nice-to-have)
**Applies to:** Section 3.4, Section 4.2
**Action:** Add an ablation table showing PSNR/SSIM for λ_exp ∈ {0.05, 0.1, 0.25, 0.5, 1.0} and N ∈ {2, 5, 10, 20} on one synthetic scene.
**Expected impact:** Shows robustness to hyperparameter choices and justifies the chosen values.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current Introduction follows this structure:
- P1: Background (NeRF, 3DGS) → LDR limitation → HDR need
- P2: Prior work categories (RAW-based, multi-exposure LDR) → their limitations → key challenge
- P3: Auto-exposure opportunity → three challenges
- P4: Physical insight (blur-exposure coupling)
- P5: Proposed method (CasualHDR overview)
- P6: Experiment summary + contribution list

**Strengths:** The logical flow from background → gap → insight → solution is present. The three challenges of auto-exposure video (unknown exposure, brightness inconsistency, motion blur) are clearly articulated.

**Weaknesses:** 
1. P1 spends too much text on well-known NeRF/3DGS background (3 of 7 sentences).
2. The transition from "LDR is limited" to "HDR is needed" is abrupt and does not crisply define the specific unsolved problem.
3. The key insight paragraph (P4) is the most important but is placed late and undersells the contribution.
4. P5 (method overview) repeats information already in the Abstract.

### Recommended Storyline (Alternative A — Best Choice)

**Rationale:** This storyline prioritizes the problem formulation (casual video → HDR 3D reconstruction) as the entry point, reducing background exposition and front-loading the specific challenge.

**Abstract Outline (5 sentences):**
- S1: "Recovering high dynamic range (HDR) 3D scenes from multi-view images currently requires carefully captured multi-exposure image sets with known exposure times."
- S2: "We propose CasualHDR, a unified framework that reconstructs HDR 3D scenes directly from casually captured videos with auto-exposure, where exposure times are unknown and motion blur is present."
- S3: "Our method jointly optimizes a continuous-time SE(3) camera trajectory, per-frame exposure time, per-channel camera response function, and a 3D Gaussian Splatting HDR scene representation through a differentiable physical imaging model."
- S4: "On four synthetic scenes and six real-world sequences, CasualHDR achieves consistent improvements over prior HDR reconstruction and deblurring methods in novel-view synthesis, image deblurring, and pose estimation."
- S5: "Reconstructed HDR scenes also enable downstream applications including exposure editing and training-view deblurring."

**Introduction Outline (6 paragraphs):**

**P1 — Problem and Significance (3-4 sentences)**
*Role:* Define the practical stakes. Why should a reader care about HDR 3D reconstruction from casual video?
*Content:* "3D HDR reconstruction enables richer visual experiences in VR/AR, but current methods require controlled multi-exposure capture with professional equipment. Consumer-grade cameras with auto-exposure produce video with varying brightness and motion blur. Reconstructing HDR 3D scenes from such imperfect input would greatly expand the applicability of volumetric HDR content."
*Transition:* "However, existing approaches cannot handle this setting because..."

**P2 — Prior Work Gap (3-4 sentences)**
*Role:* Identify the precise gap in prior methods. 
*Content:* "Existing 3D HDR methods fall into two categories. RAW-based methods (RawNeRF, LE3D) require specialized sensors. Multi-exposure LDR methods (HDR-NeRF, HDR-Plenoxels, HDR-GS) require fixed-viewpoint image stacks with known exposure times. Neither category can process casually captured video where exposure varies automatically, motion blur degrades frames, and camera trajectories are continuous."
*Transition:* "A key obstacle is that..."

**P3 — Challenges of Auto-Exposure Video (3-4 sentences)**
*Role:* Articulate the three specific technical challenges.
*Content:* "Applying HDR reconstruction to auto-exposure video encounters three interrelated challenges: (1) exposure times are unknown and not stored in standard video metadata; (2) brightness fluctuations between frames break the photometric consistency assumed by structure-from-motion pipelines; (3) longer exposures in low light produce motion blur that violates the static-camera assumption of prior HDR methods."
*Transition:* "Our key observation is that these challenges are not independent..."

**P4 — Key Insight (2-3 sentences)**
*Role:* Present the core technical insight that drives the solution.
*Content:* "Crucially, motion blur and image brightness share a common cause: the exposure time. Longer exposure increases both the accumulated irradiance (brightness) and the camera displacement during integration (blur). This coupling means that the observed blur pattern carries information about the unknown exposure time, enabling joint estimation of exposure, camera motion, and scene radiance."
*Transition:* "Building on this insight, we propose CasualHDR..."

**P5 — Method Overview (3-4 sentences)**
*Role:* Describe the proposed framework at a high level.
*Content:* "CasualHDR unifies exposure time estimation, camera trajectory recovery, CRF calibration, and HDR scene reconstruction in a single differentiable optimization. A cumulative SE(3) B-spline parameterizes the continuous camera motion during each exposure window. The scene is represented as 3D Gaussians with HDR radiance values. A physical imaging model renders blurry LDR images by integrating the HDR scene along the trajectory and applying the learned CRF. All parameters are jointly optimized by minimizing a reconstruction loss against the input video frames."
*Transition:* "We validate this approach through extensive experiments..."

**P6 — Contributions and Results Preview (3-4 sentences)**
*Role:* Summarize contributions and key findings.
*Content:* "Our contributions are threefold: (1) a unified imaging model for HDR 3D reconstruction from casual video without exposure metadata; (2) a benchmark dataset with synthetic and real sequences for this task; (3) empirical results showing consistent gains over prior methods across novel-view synthesis, deblurring, and pose estimation on four synthetic and six real-world sequences."

## Priority Revision Plan
### Priority Matrix

```text
| Priority | Low Effort (~1-2 days)           | High Effort (~1-2 weeks)                    |
|----------|--------------------------------|---------------------------------------------|
| High Impact | P0: Rewrite contribution claims | P0: Add multi-seed experiments + variance   |
|            | P0: Add hyperparameter table    | P0: Clarify evaluation protocol/splits      |
|            | P0: Add limitations section     | P1: Single-factor ablations                 |
| Medium Impact | P1: Fix ablation percentages  | P2: λ_exp and N sensitivity analysis       |
|            | P1: Restructure Related Work    | P2: Bilateral grid comparison in main paper |
```

### Execution Order

**Stage 1 (Days 1-2): Claims, Hyperparameters, Limitations**
- Rewrite contribution list (remove SOTA claim → bounded wording)
- Add explicit training hyperparameters table (LR per group, MCMC params, iterations)
- Add Limitations subsection to Conclusion
- Fix typo ("impoving"), improve punctuation/capitalization

**Stage 2 (Days 3-7): Experimental Rigor**
- Run all main experiments with 3 random seeds; report mean±std
- Clarify train/test splits for all datasets; define objective sharpness criteria
- Add significance tests for key comparisons (CasualHDR vs best baseline per dataset)
- Add single-factor ablations and fix percentage claims with exact row references

**Stage 3 (Days 8-14): Completeness and Positioning**
- Add λ_exp and N sensitivity ablation
- Restructure Related Work around thematic axes
- Move bilateral grid comparison to main paper
- Add static frame figure from supplementary video
- Revise Introduction per recommended storyline

### Expected Outcomes After Revision
| Issue | Current State | Target State |
|-------|--------------|--------------|
| Statistical evidence | Single-run point estimates | mean±std over 3 seeds, significance tests |
| Evaluation protocol | Ambiguous train/test split, subjective "sharp" selection | Explicit splits, objective criteria |
| Reproducibility | Missing hyperparameters | Full hyperparameter table |
| Claim scope | "State-of-the-art", "high robustness" | Bounded to compared baselines and tested conditions |
| Scientific completeness | No limitations | Dedicated limitations subsection |
| Ablation traceability | Untraceable percentages | Exact row comparisons, single-factor ablations |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (Data/Protocol/Baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------|---------|-------------|----------------|-------------------|
| E1 | Novel-view synthesis on synthetic data | 4 Blender scenes (Factory, Pool, Trolley, Cozyroom), 77 frames each, vs HDR-NeRF, HDR-Plenoxels, Gaussian-W, BAD-GS, gsplat | PSNR↑, SSIM↑, LPIPS↓ | CasualHDR-gt best, CasualHDR-random 2nd, large margin over baselines | C1 (joint optimization works) | Single run, no variance |
| E2 | Novel-view synthesis on real data | 6 real sequences (CasualVideo: Yakitori, Toufu, Toufu-vicon, Girls-vicon, Fish, Building), vs same baselines | PSNR↑, SSIM↑, LPIPS↓ | CasualHDR consistently best | C1, C3 | Unclear train/test split, subjective "sharp" frame selection |
| E3 | Image deblurring (synthetic) | 4 Blender scenes, vs BAD-Gaussians | PSNR↑, SSIM↑, LPIPS↓ | CasualHDR significantly better (>7 dB on Factory) | C1 (deblur capability) | Only one deblur baseline |
| E4 | Image deblurring (ScanNet real) | 6 ScanNet sequences, vs BAD-Gaussians | BRISQUE↓ | CasualHDR better on avg (49.53 vs 55.94) | C1 (deblur on real) | BRISQUE is no-reference; content-dependent |
| E5 | Pose estimation | 2 RealSense sequences with Vicon GT, vs HLoc, DPV-SLAM, BAD-GS | ATE (cm) mean±std | CasualHDR-gt best, improvements small vs BAD-GS | C1 (trajectory recovery) | High std relative to mean; no significance test |
| E6 | Ablation: component analysis | Factory + Cozyroom, toggling Deblur/Exp.Opt/CRF/Conti.Traj | PSNR↑, SSIM↑, LPIPS↓ | Each component contributes; continuous trajectory most impactful (24%) | C1 (component necessity) | Percentages not traceable to specific row comparisons |
| E7 | Ablation: control knot ratio | Pool + Factory, ratio ∈ {0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0} | PSNR↑, SSIM↑, LPIPS↓ | Performance saturates at ratio=3.0 | Practical guidance | Only 2 scenes |
| E8 | Bilateral grid comparison (Appendix) | Smartphone + RealSense datasets, gsplat+bilagrid, BAD-GS+bilagrid | PSNR↑, SSIM↑, LPIPS↓ | Bilagrid helps appearance handling but cannot represent HDR | Differentiation from appearance-modeling methods | Only in appendix |
| E9 | HDR exposure editing (qualitative) | Various scenes, adjust exposure time post-reconstruction | Visual comparison | Exposure adjustment works | C1 (downstream task) | No quantitative HDR metric (e.g., HDR-VDP) |

### Research-Theme Gap Diagnosis

The paper makes three core research-value claims:
1. **New knowledge**: A unified imaging model that couples exposure time, motion blur, and CRF for casual video HDR reconstruction. **Assessment**: Partially supported. The technical integration is sound, but without statistical validation and clear evaluation protocols, the reliability of the empirical evidence is uncertain.
2. **Reproducibility/Reusability**: The proposed dataset and method implementation. **Assessment**: Weakly supported. Missing hyperparameters prevent reproduction; the gsplat+MCMC code is not clearly documented.
3. **Potential to change practice**: Enabling HDR 3D reconstruction from consumer-grade cameras. **Assessment**: Conceptually promising but practically unvalidated. No runtime/memory benchmarks, no ablation on varying camera hardware, no stress tests on extreme conditions.

### Proposed Research Experiments

**P0-EX1: Multi-Seed Statistical Validation**
- **Target Claim:** All quantitative comparisons (E1-E5)
- **Hypothesis:** CasualHDR consistently outperforms baselines with statistical significance
- **Minimal Design:** Run 3 seeds (different random init, same train/test split) for all methods in E1 and E2 on 2 synthetic + 2 real scenes
- **Controls/Baselines:** Same seed for all methods, same training budget
- **Metrics:** mean±std PSNR/SSIM/LPIPS; paired t-test p-value vs best baseline
- **Success Criterion:** p < 0.05 for at least 3 of 4 test scenes
- **Estimated Cost:** 2-3 GPU-days
- **Expected Quality Gain:** Converts qualitative outperformance into statistically validated evidence

**P0-EX2: Evaluation Protocol Clarification**
- **Target Claim:** Novel-view synthesis results (E2)
- **Hypothesis:** Current subjective "sharp frame" selection does not bias results
- **Minimal Design:** Run evaluation on two settings: (a) all held-out frames with no sharpness filter, (b) frames selected by Laplacian variance > τ. Report both.
- **Controls/Baselines:** Same split for all methods
- **Metrics:** PSNR/SSIM/LPIPS for both settings
- **Success Criterion:** Relative ranking of methods is consistent across both settings
- **Estimated Cost:** 1-2 GPU-days
- **Expected Quality Gain:** Eliminates selection bias concern

**P1-EX3: Single-Factor Ablation**
- **Target Claim:** Each component contributes independently (E6)
- **Hypothesis:** Isolating single factors clarifies each module's contribution
- **Minimal Design:** On Factory scene, run 6 configurations: (1) none, (2) +Conti.Traj only, (3) +Deblur only, (4) +Exp.Opt only, (5) +CRF only, (6) all
- **Controls/Baselines:** Same Gaussian init, same iterations
- **Metrics:** PSNR/SSIM, plus exposure time estimation error (|Δt_pred - Δt_gt| / Δt_gt)
- **Success Criterion:** Each single-factor addition shows measurable improvement
- **Estimated Cost:** 1 GPU-day
- **Expected Quality Gain:** Traceable contribution attribution

**P1-EX4: Exposure Time Estimation Accuracy**
- **Target Claim:** Exposure time optimization converges to true values
- **Hypothesis:** Optimized exposure times correlate with ground truth
- **Minimal Design:** On synthetic scenes (where Δt_gt is known), plot predicted Δt vs Δt_gt per frame. Compute mean absolute percentage error (MAPE)
- **Controls/Baselines:** Random initialization
- **Metrics:** MAPE, R² correlation
- **Success Criterion:** MAPE < 20%
- **Estimated Cost:** 0.5 GPU-day (reuses existing checkpoints)
- **Expected Quality Gain:** Direct validation of exposure optimization — a central claim

**P2-EX5: Robustness to Extreme Conditions**
- **Target Claim:** Robustness to challenging inputs
- **Hypothesis:** Method degrades gracefully under extreme dynamic range or rapid camera motion
- **Minimal Design:** On synthetic data, create two stress scenarios: (a) 3-stop exposure variation (vs ~1 stop in current data), (b) 2x faster camera motion. Compare CasualHDR vs best baseline.
- **Controls/Baselines:** Same stress conditions for all methods
- **Metrics:** PSNR/SSIM degradation relative to non-stress baseline
- **Success Criterion:** Degradation < 20% relative
- **Estimated Cost:** 1 GPU-day
- **Expected Quality Gain:** Demonstrates boundary conditions — essential for a "robustness" claim

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

The paper tackles a practically important and technically interesting problem (HDR 3D reconstruction from casual video) with a sound core idea (coupling motion blur and exposure time in a unified imaging model). The empirical results show consistent improvements over the compared baselines across multiple tasks and datasets.

However, the score is limited by several significant weaknesses:
- **Missing statistical validation** — no variance or significance testing for any metric (core empirical claim is not fully evidenced)
- **Unclear evaluation protocol** — potential selection bias from subjective "sharp frame" selection and undocumented train/test splits
- **Reproducibility gaps** — critical optimization hyperparameters not reported
- **Overclaiming** — "state-of-the-art" and "high robustness" claims exceed the evidence scope
- **No limitations discussion** — scientific completeness concern
- **Novelty verification deferred** — external literature verification unavailable in this run; SOTA claims cannot be confirmed

The paper's research value is real: enabling HDR 3D reconstruction from casually captured video would be useful, and the joint optimization insight is technically novel in this specific combination. But the current evidence base is insufficient to fully substantiate the claimed contributions.

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors complete the P0 revisions (multi-seed statistics, clear evaluation protocol, hyperparameter documentation, bounded claim language, limitations section), the paper could become a solid conference contribution. Key milestones for the target score:
- Statistical validation showing consistent significant improvements (p < 0.05) → +0.5
- Transparent evaluation protocol → +0.3
- Full reproducibility documentation → +0.3
- Claim bounding and limitations → +0.2
- Successful external novelty verification (deferred) → +0.5

The upper bound of 7.5 reflects the inherently incremental nature of combining existing components (3DGS, B-spline trajectory, CRF estimation) into a unified framework — the novelty is in the integration and the specific casual-video setting rather than any single algorithmic innovation.