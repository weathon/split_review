## Summary
# Final Review Report

## Summary

This paper presents 4D Gaussian Splatting (4DGS), a method for real-time photorealistic novel view synthesis of dynamic scenes. The core idea is to extend 3D Gaussian Splatting (Kerbl et al., 2023) to the spatio-temporal domain by representing a dynamic scene as a collection of 4D Gaussian primitives with explicit geometry (full 4D covariance with 4D rotation) and a time-evolved appearance model (4D Spherindrical Harmonics). The rendering pipeline factorizes each 4D Gaussian into a conditional 3D Gaussian (projected to 2D for rasterization) and a marginal 1D temporal Gaussian, enabling end-to-end training and real-time rendering at 114 FPS on the Plenoptic Video benchmark.

The paper's key strengths are: (1) a conceptually clean formulation that treats space and time symmetrically via 4D Gaussian primitives; (2) impressive empirical results showing state-of-the-art rendering quality (32.01 PSNR on Plenoptic Video, +0.99 dB over the strongest prior method) at a significant speed advantage (114 FPS vs 36 FPS for Wu et al. 2023); and (3) extensive validation across monocular and multi-view, synthetic and real datasets.

The main weaknesses identified in this review include: (a) several overclaims ("first-ever," "outperforms all previous methods") that are not fully supported by the presented evidence or are contradicted by the paper's own cited baselines; (b) missing statistical rigor (no variance/confidence intervals in any experiment table, making the PSNR improvements of ~0.3-1.0 dB unverifiable); (c) insufficient quantitative validation of the motion-capture claim (optical flow analysis is qualitative only); (d) the 4DSH orthonormal basis uses only cosine terms without justification; and (e) the conclusion introduces unsupported claims. Since external literature retrieval is unavailable in this run, novelty verdicts are conservatively marked as deferred, but the paper's approach appears to be a sound extension of 3DGS with clear differentiation from deformation-based dynamic scene methods.

## Strengths
**S1. Novel and principled 4D primitive formulation.** Treating space and time as a unified 4D volume parameterized by anisotropic Gaussian primitives with full 4D covariance is a conceptually clean extension of 3D Gaussian Splatting. The use of double-quaternion 4D rotation enables the covariance matrix to capture correlations between spatial displacement and time, which is the mechanism behind the method's ability to model motion without explicit deformation tracking. This is a genuine conceptual contribution (C1).

**S2. Strong empirical performance.** The method achieves 32.01 PSNR on the Plenoptic Video benchmark, outperforming all compared baselines (HexPlane: 31.70, K-Planes-hybrid: 31.63, MixVoxels: 30.80) while simultaneously achieving 114 FPS—a 3x speedup over the fastest prior real-time method (Wu et al. 2023 4DGS at 36 FPS) and orders of magnitude faster than implicit methods (DyNeRF: 0.015 FPS). On the D-NeRF monocular benchmark, 4DGS achieves 34.09 PSNR, outperforming V4D (33.72) and Wu et al. (33.30). This combination of quality and speed is well-demonstrated.

**S3. 4D Spherindrical Harmonics (4DSH) as a compact temporal appearance model.** The extension of spherical harmonics with a Fourier temporal basis is a practical and interpretable way to model time-evolving view-dependent color without duplicating Gaussians per frame. This contribution (C2) is technically sound and avoids the redundancy of per-frame appearance models.

**S4. Comprehensive experimental scope.** The evaluation covers multi-view real scenes (Plenoptic Video), monocular synthetic scenes (D-NeRF), and outdoor urban scenes (Waymo Open Dataset), demonstrating versatility across different capture settings. The ablation studies isolate the effects of 4D rotation, 4DSH, and temporal densification.

**S5. Open and reproducible.** The authors provide a project website with code and video results, which supports reproducibility and community adoption.

**S6. Well-structured technical writing.** The method section is logically organized (3DGS preliminaries -> 4D formulation -> 4DSH -> training), and the mathematical derivations are accompanied by intuitive figure explanations (Figure 1, Figure 2).

## Weaknesses
**W1. Overclaiming and unsupported "first-ever" language.** The abstract, introduction, and conclusion contain unqualified "first-ever" and "outperforms all previous methods" claims. The paper's own Table 1 lists MixVoxels-L at 16.7 FPS and Wu et al. (2023) 4DGS at 36 FPS—both real-time capable. The "first-ever" claim is therefore factually inconsistent with the paper's own comparison table. The conclusion's "to the best of our knowledge, this work stands as the first ever method capable of real-time, high-fidelity video synthesis for complex, real-world dynamic scenes" is an overreach given the concurrent works cited by the authors. (Severity: Major)

**W2. Missing statistical evidence.** All experimental results are reported as point estimates without variance, confidence intervals, or multi-seed statistics. The PSNR improvements over the strongest baselines are modest (0.31 dB over HexPlane, 0.99 dB over Wu et al. 4DGS on Plenoptic Video; 0.37 dB over V4D on D-NeRF). Without standard deviations, the reader cannot determine whether these differences are statistically significant or within run-to-run noise. (Severity: Major)

**W3. Weak quantitative validation of the motion-capture claim.** Claim C1's core assertion is that 4D rotation enables motion modeling. The evidence is purely qualitative—rendered optical flow visualizations against estimated (not ground-truth) flow from VideoFlow. No quantitative metric (e.g., End-Point Error) is reported. The paper cites VideoFlow outputs as "GT Flow," which overstates the reliability of these references. (Severity: Major)

**W4. LPIPS incomparability across methods.** The LPIPS backbone differs between Plenoptic Video (AlexNet) and D-NeRF (VGGNet). More critically, Table 1 lists LPIPS for multiple baselines without specifying which backbone was used for each. If different backbones produced these numbers (as the diverse references suggest), the LPIPS column is not a valid cross-method comparison. (Severity: Major)

**W5. 4DSH orthonormal basis uses only cosine terms.** The 4D Spherindrical Harmonics defined in Eq. (11) use only the cosine Fourier basis. Claiming orthonormality for a cosine-only basis is incorrect unless the signal is assumed to be even in the time dimension. The paper does not justify this design choice or discuss its impact on representing asymmetric temporal color changes. (Severity: Minor)

**W6. Temporal flickering fix lacks rigorous analysis.** The paper acknowledges "temporal flickering and jitter" in some scenes and proposes batch temporal sampling as the fix, but provides no quantitative comparison against alternatives (random sampling, sequential sampling) and no residual artifact measurement. (Severity: Minor)

**W7. Missing comparison with deformation-based 4DGS on tracking metrics.** The related work section distinguishes this method from deformation-based approaches (Yang et al. 2023, Wu et al. 2023, Liang et al. 2023) by claiming that 4D primitives do not require tracking. However, no experiment measures tracking accuracy, correspondence quality, or the number of Gaussians needed—metrics that would directly validate this claimed advantage. (Severity: Minor)

**W8. Background reconstruction limitation is understated.** The Appendix Limitations section acknowledges that without initial points, the method cannot capture background geometry. This is described as a convenience limitation, but it is a fundamental constraint: the method cannot reconstruct regions not covered by the initial point cloud. This directly impacts the claim of handling "complex real-world dynamic scenes." (Severity: Minor)

**W9. Conclusion adds unsupported claims.** The conclusion introduces the new claim that the method "align[s] the rendering process with the imaging of such scenes," which was not tested or validated in the paper. This violates the principle of not introducing new claims in the conclusion. (Severity: Minor)

## Key Issues
### Issue 1: Statistical reliability of experimental claims (Critical)
**Location:** Page 7, Table 1; Page 8, Table 2; Page 9, Table 3
**Root cause:** All metrics are reported as point estimates without variance, confidence intervals, or multi-seed statistics. The PSNR gains over the strongest competitors are small (0.31 dB over HexPlane, 0.37 dB over V4D). Without variance reporting, these differences cannot be assessed for statistical significance.
**Risk:** The core empirical claim (contribution iii) is unverifiable. If the run-to-run variance is ~0.3 dB, the reported advantages could be within noise.
**Fix:** Report mean +/- std over >=3 seeds. Add paired significance tests for the strongest comparison.
**Priority:** P0 (Must fix before acceptance)

### Issue 2: Overclaim via "first-ever" and "outperforms all" language (Major)
**Location:** Page 1 - Abstract; Page 2 - Introduction (solution paragraph); Page 9 - Conclusion
**Root cause:** The paper claims "first-ever model supporting end-to-end training and real-time rendering" but its own Table 1 shows MixVoxels-L at 16.7 FPS and Wu et al. (2023) at 36 FPS—both real-time capable. The claim is internally inconsistent with the paper's evidence.
**Risk:** This overclaim invites immediate reviewer skepticism and can undermine trust in the entire paper.
**Fix:** Remove "first-ever" language. Replace with scoped wording: "to our knowledge, the first unified 4D primitive approach achieving state-of-the-art quality at real-time frame rates."
**Priority:** P0 (Must fix)

### Issue 3: Motion-capture claim lacks quantitative evidence (Major)
**Location:** Page 9 - Section 4.4, Figure 4
**Root cause:** The paper claims 4D Gaussians capture underlying 3D movement, but the evaluation is purely qualitative visual comparison of rendered optical flow. The "ground truth" flow comes from VideoFlow (another estimation method), not actual ground truth.
**Risk:** A core contribution (C1: motion modeling via 4D rotation) is supported only by subjective visual inspection.
**Fix:** Compute quantitative flow metrics (EPE, flow accuracy) on a subset of scenes. At minimum, report flow magnitude correlation against a reference method.
**Priority:** P1 (High priority)

### Issue 4: LPIPS incomparability across methods (Major)
**Location:** Page 7 - Table 1 footnotes, Page 7 - Implementation Details
**Root cause:** LPIPS is computed with AlexNet for Plenoptic Video and VGGNet for D-NeRF. The baselines in Table 1 may use different LPIPS backbones. This makes the LPIPS column non-comparable across methods.
**Risk:** The perceptual quality advantage claimed via LPIPS may be an artifact of backbone choice.
**Fix:** Use a single backbone (AlexNet, the community standard for LPIPS) for all evaluations and recompute.
**Priority:** P1 (High priority)

### Issue 5: 4DSH basis uses only cosine terms (Minor)
**Location:** Page 6 - Eq. (11)
**Root cause:** Z^m_{nl}(t,θ,φ) = cos(2πn/T t) · Y^m_l(θ,φ). Only cosine basis is used; orthonormality is claimed for a cosine-only basis, which is only valid for even signals.
**Risk:** May limit representation capacity for asymmetric temporal color changes; orthonormality claim is imprecise.
**Fix:** Clarify that only cosine basis is used for efficiency and justify sufficiency for the tested domain, or add sine terms.
**Priority:** P2

### Issue 6: Background reconstruction limitation understated (Minor)
**Location:** Page 12 - Appendix A
**Root cause:** The paper acknowledges that without point cloud initialization, background regions cannot be reconstructed and spherical initialization does not yield correct geometry. This is described as a convenience limitation rather than a fundamental constraint.
**Risk:** The claim of handling "complex, real-world dynamic scenes" is significantly qualified by this unreported failure mode.
**Fix:** Elevate this to a main-text limitation. Discuss practical impact for unbounded outdoor scenes or scenes where COLMAP fails.
**Priority:** P2

## Actionable Suggestions
### Suggestion 1: Add multi-seed variance reporting and significance tests (Must)
**Target:** Page 7 - Table 1, Page 8 - Table 2, Page 9 - Table 3
**Action:** Re-run all experiments with 3 random seeds. Report mean +/- std for PSNR, SSIM, LPIPS. Add a paired Wilcoxon signed-rank test or a matched-pairs bootstrap to compare against the strongest baseline (HexPlane for Plenoptic Video, V4D for D-NeRF). If the p-value exceeds 0.05, state the comparison as "not statistically significant" rather than claiming superiority.
**Expected benefit:** Transforms the empirical claims from unverifiable to statistically grounded. This single change addresses the most critical weakness.
**Effort:** Medium (re-running evaluations with seeds). The training pipeline is already implemented; only the seed loop needs to be added.

### Suggestion 2: Replace "first-ever" and "outperforms all" with bounded, defensible language (Must)
**Target:** Page 1 - Abstract, Page 2 - Introduction contribution paragraph, Page 9 - Conclusion
**Action:** 
- Abstract: Replace "first-ever model supporting end-to-end training and real-time rendering" with "achieves state-of-the-art rendering quality at real-time frame rates (114 FPS on Plenoptic Video)."
- Introduction contribution (iii): Replace "outperforms all previous methods" with "achieves superior visual quality and efficiency across synthetic and real, monocular and multi-view benchmarks."
- Conclusion: Replace "first ever method capable of real-time, high-fidelity video synthesis" with "to our knowledge, the first unified 4D Gaussian representation that achieves real-time rendering with state-of-the-art quality in this setting."
**Expected benefit:** Eliminates reviewer skepticism about overclaiming. Aligns claims with evidence in the paper's own tables.

### Suggestion 3: Quantify motion-capture evaluation (High priority)
**Target:** Page 9 - Section 4.4, Figure 4
**Action:** Add quantitative optical flow evaluation. For 2-3 representative scenes, compute average End-Point Error (EPE) between the rendered flow and a reference flow (from VideoFlow or RAFT). Report per-scene EPE for the Full model vs the No-4DRot ablation. Even a simple metric like "flow magnitude correlation coefficient" would provide objective evidence.
**Expected benefit:** Validates the core motion-modeling claim (C1) with objective evidence, significantly strengthening the paper.
**Effort:** Low-Medium. Optical flow estimation code is readily available; computing EPE requires ~100 lines of code.

### Suggestion 4: Standardize LPIPS backbone and recompute comparisons (High priority)
**Target:** Page 7 - Table 1, Page 7 - Implementation Details
**Action:** Use AlexNet backbone for all LPIPS computations across all datasets and baselines. Recompute baseline LPIPS values where necessary. Add a footnote specifying the backbone used.
**Expected benefit:** Makes LPIPS column comparable, increasing the credibility of perceptual quality comparisons.

### Suggestion 5: Add sine terms to 4DSH or justify cosine-only choice (Nice-to-have)
**Target:** Page 6 - Eq. (11), Section "4D Spherindrical Harmonics"
**Action:** Either (a) add sine terms to make the basis complete (doubling the coefficient count but ensuring true orthonormality), or (b) add an ablation showing that cosine-only achieves similar performance to a full Fourier basis on a representative scene. Also clarify that t in Eq. (11) represents t_render - mu_t (the offset from the Gaussian's mean time).
**Expected benefit:** Resolves the mathematical imprecision in the orthonormality claim and clarifies the temporal encoding.

### Suggestion 6: Expand Ablation Table 3 with temporal consistency metrics (Nice-to-have)
**Target:** Page 9 - Table 3
**Action:** Add a column for a temporal consistency metric (e.g., warped-frame PSNR, per-frame LPIPS variance, or temporal flicker score). This would directly evaluate the impact of 4D rotation and batch temporal sampling on temporal coherence.
**Expected benefit:** Addresses the temporal flickering concern with quantitative evidence.

### Suggestion 7: Merge contribution (iii) into (i) and (ii) (Must)
**Target:** Page 2 - Contribution list
**Action:** Contribution (iii) is a performance summary, not a conceptual contribution. Remove it as a standalone claim and merge its content into an empirical summary sentence at the end of the contribution list. This aligns with the constraint that pure metric improvements (without conceptual intervention) are not standalone contributions.
**Expected benefit:** Strengthens the contribution list by keeping only substantive conceptual claims.

### Suggestion 8: Move background limitation to main text (Nice-to-have)
**Target:** Page 12 - Appendix A -> Move to Section 5 (Conclusion) or add a new Limitations subsection
**Action:** Integrate the background reconstruction limitation into the main text conclusion. Add a concrete example (e.g., "On the Coffee Martini scene, removing spherical initialization causes a 2+ dB PSNR drop on background regions").
**Expected benefit:** Improves scientific honesty and helps readers understand the method's applicability scope.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current paper follows this narrative structure:
1. **Introduction P1:** Establish AR/VR importance, NeRF background, dynamic scene challenges
2. **Introduction P2:** Two-group taxonomy of dynamic NVS methods (implicit plenoptic vs deformation-based)
3. **Introduction P3:** Deformation-based group limitations
4. **Introduction P4 + Contributions:** Proposed 4D Gaussian solution + contribution list
5. **Related Work:** Static NVS -> Dynamic NVS -> Dynamic 3D Gaussians
6. **Method:** 3DGS preliminaries -> 4D formulation -> 4DSH -> Training
7. **Experiments:** Setup -> Results -> Ablation
8. **Conclusion**

**Strength of current storyline:** The paper follows a logical progression from problem to method to results. The two-group taxonomy in the introduction provides a clear framework.

**Weakness of current storyline:** 
- The introduction spends ~60% of its space on taxonomy/literature review before presenting the solution. The actual gap (space-time entanglement requiring joint modeling) appears only in the third paragraph.
- The contribution list mixes conceptual contributions (C1, C2) with a performance summary (C3), diluting novelty perception.
- The conclusion introduces a new "imaging alignment" claim not supported by experiments.

### Abstract Outline (Revised)

**Target:** 5-sentence structure, self-contained, no claims beyond evidence.

- **S1 (Problem):** Reconstructing dynamic 3D scenes from 2D images and synthesizing novel views over time is challenging due to scene complexity and temporal dynamics.
- **S2 (Gap):** Existing methods either learn 6D plenoptic functions without explicit motion modeling (leading to parameter coupling) or use deformation fields with restrictive topological priors.
- **S3 (Solution):** We propose to approximate the spatio-temporal 4D volume of a dynamic scene using a collection of 4D Gaussian primitives with full 4D covariance, where 4D rotation enables motion modeling without deformation tracking.
- **S4 (Technical highlight):** Appearance evolution over time is modeled via 4D Spherindrical Harmonics—a Fourier extension of spherical harmonics.
- **S5 (Result):** Experiments on monocular and multi-view benchmarks demonstrate state-of-the-art rendering quality (32.01 PSNR on Plenoptic Video) at real-time frame rates (114 FPS), outperforming prior methods in both fidelity and speed.

### Introduction Outline (Revised)

**P1 (Motivation + Gap):** Define the practical importance (AR/VR). State that while NeRF-based methods excel for static scenes, dynamic scenes introduce the fundamental challenge of jointly modeling spatial and temporal correlations. State the central difficulty: existing representations cannot simultaneously capture motion-correlated signal across frames while avoiding interference between dynamic and static regions. *(Replaces current abstract "central challenge" with an operational statement linked to the proposed solution.)*

**P2 (Prior work limitations):** Two-group taxonomy (plenoptic vs deformation) with explicit failure modes. Plenoptic methods struggle with "parameter coupling" between static and dynamic regions. Deformation methods assume topological invariance, limiting flexibility for objects entering/exiting or changing topology. *(Adds a concrete failure mode: topological change, which directly motivates the 4D primitive approach.)*

**P3 (Proposed idea + intuition):** We approach the problem from a different perspective—approximate the scene's 4D spatio-temporal volume directly with 4D Gaussians. Explain intuitively: a 4D Gaussian's conditional distribution mu_{xyz|t} shifts with time, capturing motion, while the marginal p(t) handles temporal visibility. This removes the need for explicit tracking or deformation fields. *(Bridges gap directly to the method.)*

**P4 (Technical components + contributions):** Two concrete contributions: (i) 4D Gaussian primitives with full 4D rotation for unbiased space-time modeling, (ii) 4D Spherindrical Harmonics for compact time-evolving appearance. Performance summary: achieves state-of-the-art quality at real-time frame rates on standard benchmarks. *(Removes the inflated "outperforms all" language; keeps contributions as conceptual claims with an empirical summary.)*

### Alternative Storyline Candidates

**Candidate A (Problem-first, clearer gap):** Start with a concrete failure scenario (e.g., "A monocular video of a flame salmon cooking—how can we render a novel view at any time with photorealistic quality? Current methods fail because..."). This engages readers immediately and makes the gap tangible.

**Candidate B (Method-first, for expert audience):** Lead with the 4D Gaussian insight: "We treat space and time symmetrically via 4D primitives." Then explain why existing methods cannot achieve this. This works for a technically-oriented audience but risks losing readers unfamiliar with the domain.

**Candidate C (Claim-focused):** Start with the result: "We present the first dynamic scene representation achieving real-time rendering (114 FPS) with state-of-the-art quality." Then unpack how. This is attention-grabbing but may be perceived as flashy. If chosen, all claims must be carefully bounded.

**Recommendation:** Adopt the Revised Outline described above (P1-P4), which combines the best elements of the current structure with clearer gap articulation and bounded claims. This is Option A (problem-first) integrated with a structured taxonomy. The concrete failure scenario can be added as an opening sentence in P1.

## Priority Revision Plan
The following revision actions are ranked by impact on paper quality and acceptance probability. Each item includes the expected benefit and estimated effort.

| Priority | Action | Key Issue Addressed | Effort | Expected Benefit |
|----------|--------|-------------------|--------|------------------|
| **P0** | Remove "first-ever" and "outperforms all" language; replace with bounded claims | W1, Issue 2 | Low | Eliminates overclaim risk; improves reviewer trust |
| **P0** | Add multi-seed variance and significance tests to all experiment tables | W2, Issue 1 | Medium | Transforms empirical claims from unverifiable to statistically grounded |
| **P0** | Merge contribution (iii) into empirical summary; keep only C1 and C2 as conceptual contributions | W1, Suggestion 7 | Low | Strengthens contribution list; aligns with review norms |
| **P1** | Add quantitative optical flow evaluation (EPE) to validate motion-capture claim | W3, Issue 3 | Medium | Validates core C1 motion-modeling claim with objective evidence |
| **P1** | Standardize LPIPS backbone (AlexNet) across all methods and recompute | W4, Issue 4 | Medium | Makes perceptual quality comparison valid |
| **P1** | Add temporal consistency metrics to ablation table | W6, Suggestion 6 | Medium | Provides quantitative evidence for temporal coherence |
| **P2** | Add sine terms to 4DSH or justify cosine-only with ablation | W5, Issue 5 | Medium | Resolves orthonormality imprecision |
| **P2** | Move background limitation to main text conclusion | W8, Issue 6 | Low | Improves scientific honesty and scope clarity |
| **P2** | Remove unsupported "imaging alignment" claim from conclusion | W9 | Low | Prevents new unsupported claims in conclusion |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Overclaim: "first-ever", "outperforms all"]
    -> P0 Fix: Replace with bounded wording
    -> Expected impact: Removes immediate reviewer skepticism

[Missing variance in experimental tables]
    -> P0 Fix: Add 3-seed std + significance tests
    -> Expected impact: Core empirical claim becomes verifiable

[Qualitative-only motion validation]
    -> P1 Fix: Compute EPE for rendered optical flow
    -> Expected impact: C1 motion claim gains quantitative support

[LPIPS backbone inconsistency]
    -> P1 Fix: Standardize to AlexNet, recompute baselines
    -> Expected impact: LPIPS column becomes comparable

[4DSH cosine-only basis]
    -> P2 Fix: Add sine terms or justify with ablation
    -> Expected impact: Mathematical precision improved

[Background limitation in appendix]
    -> P2 Fix: Move to main text
    -> Expected impact: Scope honesty improved
```

### Staged Execution Plan

**Stage 1 (Immediate - 1 day):** Implement P0 fixes - claim rewrites in Abstract/Introduction/Conclusion, contribution list restructuring, merge contribution (iii) into empirical summary.

**Stage 2 (Short-term - 3 days):** Run multi-seed experiments, compute variances, add significance tests, standardize LPIPS backbone. Add quantitative flow evaluation (EPE).

**Stage 3 (Medium-term - 1 week):** Ablate 4DSH with sine terms, add temporal consistency metrics, move limitations to main text.

**Stage 4 (Before resubmission):** Final proofread for remaining overclaims, ensure conclusion only contains validated claims.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Multi-view real scene rendering quality | Plenoptic Video (6 scenes, multi-view, real) | PSNR, DSSIM, LPIPS, FPS | 32.01 PSNR, 0.014 DSSIM, 0.055 LPIPS, 114 FPS | C3 (performance) | No variance; LPIPS backbone mismatch |
| E2 | Monocular dynamic scene rendering | D-NeRF (8 scenes, synthetic, monocular) | PSNR, SSIM, LPIPS | 34.09 PSNR, 0.98 SSIM, 0.02 LPIPS | C3 (performance) | No variance; LPIPS backbone mismatch |
| E3 | Ablation: 4D rotation (No-4DRot) | 2 scenes (flame salmon, cut beef) | PSNR, SSIM | Full: 31.62/0.97 vs No-4DRot: 30.79/0.96 | C1 (4D rotation enables motion) | Only 2 scenes; no motion-specific metric |
| E4 | Ablation: 4DSH (No-4DSH) | 2 scenes | PSNR, SSIM | Full: 31.62/0.97 vs No-4DSH: 31.38/0.97 | C2 (4DSH improves appearance) | Small gain (0.24 dB); only 2 scenes |
| E5 | Ablation: Time densification (No-Time split) | 2 scenes | PSNR, SSIM | Full: 31.62/0.97 vs No-Time: 30.25/0.97 | Temporal densification helps | Large gap but only 2 scenes |
| E6 | Optical flow visualization | All Plenoptic scenes | Qualitative | Visual similarity to VideoFlow flow | C1 (motion capture) | No quantitative metric (EPE) |
| E7 | Urban scene reconstruction | Waymo Open Dataset | Qualitative | High-fidelity renderings | Applicability | No quantitative metrics |

### Research-Theme Gap Diagnosis

**New knowledge gap:** The core insight—4D rotation enables motion modeling without deformation tracking—is conceptually novel but only qualitatively validated (E6). The paper lacks a controlled experiment that isolates the motion-capture capability from the rendering quality improvement.

**Reproducibility gap:** The reported results cannot be reproduced without knowing the random seed, the exact LPIPS backbone for each baseline, and the specific hyperparameter settings for the 10,000-iteration early stopping on Plenoptic scenes.

**Impact on practice/understanding gap:** The claim that 4D Gaussians are "friendly to long videos" is supported only by Figure 10 (Gaussian count at 10k iterations) but not by per-frame rendering time measurements across different video lengths.

### Proposed Research Experiments (P0/P1/P2)

**P0 Experiment: Multi-seed variance reporting (Critical)**
- **Target Claim:** All performance claims (C3)
- **Hypothesis:** The observed PSNR gains are statistically significant
- **Minimal Design:** Re-run main experiments (Plenoptic Video, D-NeRF) with 3 random seeds. Report mean +/- std for all metrics.
- **Controls/Baselines:** Same hyperparameters as original runs, only seed varies.
- **Metrics:** PSNR, SSIM, LPIPS (mean +/- std)
- **Success Criterion:** Standard deviation < 0.15 dB for PSNR; if std > 0.3 dB, interpret claims conservatively.
- **Estimated Cost/Time:** 3x GPU-hours per scene ~ 3 days on a single GPU.
- **Expected Quality Gain:** Transforms empirical evidence from Level 1 (descriptive) to Level 2 (quasi-experimental).

**P1 Experiment: Quantitative optical flow evaluation (High priority)**
- **Target Claim:** C1 (4D Gaussian captures underlying motion)
- **Hypothesis:** The rendered optical flow from 4DGS has lower EPE than the No-4DRot ablation
- **Minimal Design:** On 3 Plenoptic scenes, compute EPE between rendered flow and VideoFlow reference flow for Full vs No-4DRot models.
- **Controls/Baselines:** No-4DRot ablation as the baseline; VideoFlow as reference.
- **Metrics:** Average EPE, flow accuracy (percentage of pixels with EPE < threshold)
- **Success Criterion:** Full model achieves lower EPE than No-4DRot with a meaningful margin (>10% relative improvement).
- **Estimated Cost/Time:** 2 days (requires running inference, flow estimation, and evaluation code).
- **Expected Quality Gain:** Validates the core motion-capture claim with objective evidence.

**P1 Experiment: Temporal consistency metric (High priority)**
- **Target Claim:** Temporal stability (related to all claims)
- **Hypothesis:** Batch temporal sampling and full 4D rotation improve temporal consistency
- **Minimal Design:** Compute per-frame LPIPS variance and warped-frame PSNR for Full model vs No-4DRot and vs alternative sampling strategies.
- **Controls/Baselines:** Random frame sampling, sequential sampling.
- **Metrics:** Per-frame LPIPS variance (lower = more consistent), warped-frame PSNR (higher = better temporal coherence).
- **Success Criterion:** Full model shows lower LPIPS variance than alternatives.
- **Estimated Cost/Time:** 1 day.
- **Expected Quality Gain:** Provides quantitative evidence for the temporal flickering claim.

**P2 Experiment: 4DSH sine-term completeness (Nice-to-have)**
- **Target Claim:** C2 (4DSH orthonormality)
- **Hypothesis:** Adding sine terms improves or matches cosine-only performance
- **Minimal Design:** Compare cosine-only vs full Fourier (cosine + sine) 4DSH on 2 scenes.
- **Controls/Baselines:** Cosine-only as default.
- **Metrics:** PSNR, LPIPS.
- **Success Criterion:** Full Fourier < 0.1 dB improvement (justifying cosine-only choice); or > 0.3 dB improvement (requiring sine terms).
- **Estimated Cost/Time:** 1 day.
- **Expected Quality Gain:** Resolves the orthonormality imprecision and validates the 4DSH design.

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 (Must):
  [Multi-seed variance] -> [Statistical reliability] -> [Verifiable claims]
  
P1 (High):
  [Optical flow EPE] -> [Quantified motion capture] -> [C1 validated]
  [Temporal consistency] -> [Flicker quantification] -> [Temporal claims supported]
  
P2 (Nice-to-have):
  [4DSH sine ablation] -> [Basis completeness check] -> [C2 precision improved]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

**Score Rationale:** The paper presents a technically sound and conceptually clean extension of 3D Gaussian Splatting to dynamic scenes. The 4D Gaussian formulation with full 4D covariance and 4DSH is a genuine contribution. The empirical results are strong and the speed advantage is impressive. However, the score is constrained by the following factors:
- **Research value:** The core idea (4D primitives) is novel but the incremental improvement over existing methods (0.3-1.0 dB PSNR) is modest, and the motion-capture mechanism is only qualitatively validated (deduct -1.0).
- **Validity:** Missing statistical variance across all experiments means the main performance claims are not verifiable (deduct -1.0).
- **Objectivity:** Multiple overclaims ("first-ever," "outperforms all") that are inconsistent with the paper's own evidence damage credibility (deduct -0.5).
- **Reproducibility:** LPIPS backbone inconsistency and early stopping heuristics limit reproducibility (deduct -0.5).
- **Soundness:** The mathematical formulation is generally correct, though the 4DSH orthonormality claim needs clarification (minor deduction -0.5).

**Post-Revision Target:** [7.5, 8.5]/10

If all P0 fixes (claim rewrites, multi-seed variance, contribution restructuring) and P1 fixes (flow quantification, LPIPS standardization, temporal consistency metrics) are completed, the paper would address the most critical weaknesses. The ceiling is limited by the modest empirical margins and the fact that the core idea is an extension of 3DGS rather than a completely new paradigm. The upper bound of 8.5 assumes that the statistical evidence validates the observed gains and the motion-capture claim is quantitatively confirmed.

### ASCII Diagram — Paper Structure & Evidence Map

```text
Paper: 4D Gaussian Splatting (4DGS)

[Claim C1: 4D Gaussian primitives with 4D rotation enable motion modeling]
    -> Evidence: Eq (9) conditional mean shift; Table 3 (No-4DRot ablation); Fig 4 (optical flow)
    -> Gap: Optical flow evaluation is qualitative only (no EPE metric)
    -> Risk: Motion capture claim insufficiently supported

[Claim C2: 4D Spherindrical Harmonics model time-evolved appearance]
    -> Evidence: Table 3 (No-4DSH ablation); Eq (11)
    -> Gap: Cosine-only basis may not be complete; ablated on only 2 scenes
    -> Risk: Modest, 0.24 dB gain without orthonormality justification

[Claim C3: State-of-the-art quality and speed]
    -> Evidence: Table 1 (32.01 PSNR, 114 FPS); Table 2 (34.09 PSNR)
    -> Gap: No variance; LPIPS incomparable; PSNR gains are +0.31 to +0.99 dB
    -> Risk: Unverifiable without variance; overclaim language

[Reader path check:]
    Intro problem -> Method answer -> Results evidence -> Conclusion
    Check: PASS (loop is closed, but conclusion adds new unsupported claim)
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Dynamic Novel View Synthesis (Root)
├── Branch A: Implicit 6D Plenoptic Function (no explicit motion)
│   ├── Leaf A1: MLP-based (DyNeRF, NeRFPlayer)
│   ├── Leaf A2: Grid/Decomposition (HexPlane, K-Planes, MixVoxels)
│   └── Leaf A3: Ray-conditioned (HyperReel, StreamRF)
│   Limitation: Parameter coupling between static/dynamic regions
│
├── Branch B: Deformation-based (explicit motion modeling)
│   ├── Leaf B1: Canonical field (D-NeRF, TiNeuVox, V4D)
│   ├── Leaf B2: 3D Gaussian + deformation (Yang et al., Wu et al., Liang et al.)
│   └── Leaf B3: Tracking-based (Luiten et al., Kratimenos et al.)
│   Limitation: Assumes topological invariance; requires tracking
│
└── Branch C: Unified Spatio-Temporal Primitives (This paper - 4DGS)
    ├── Leaf C1: 4D Gaussian with full 4D covariance
    ├── Leaf C2: 4D Spherindrical Harmonics for temporal appearance
    └── Advantage: No explicit tracking/deformation needed; treats space-time symmetrically
    Unvalidated: Motion capture only qualitatively shown; tracking-free advantage not quantified
```

### Contribution-level Novelty Conclusion

This paper's central novelty lies in extending 3D Gaussian primitives to 4D with full covariance (C1) and introducing 4DSH for temporal appearance (C2). Since external literature retrieval is unavailable in this run, novelty verdicts are conservatively deferred to manual verification. However, based on manuscript-internal evidence: (a) the 4D rotation mechanism for motion modeling appears distinct from deformation-field approaches reviewed in Section 2, and (b) the 4DSH cosine-Fourier basis is a natural extension of SH that has not been used in prior dynamic scene rendering to the paper's acknowledgment. The paper's main risk is that concurrent 4DGS works (Wu et al. 2023, Yang et al. 2023) may have independently proposed similar ideas; the small (0.99 dB) PSNR gap and different technical routes suggest partial overlap rather than substantial overlap, but this cannot be confirmed without external verification.