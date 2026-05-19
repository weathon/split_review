## Summary
# Final Review Report

## Summary

This paper tackles the novel task of unpaired panoramic image-to-image translation (Pano-I2I), where panoramic (360-degree) source images are translated into the style of diverse target conditions (night, rainy, twilight) using only pinhole-style datasets as the target domain. This is a challenging setting because source and target differ in both style and geometric structure (wide vs narrow field-of-view).

The authors propose a dedicated framework with four key technical components: (1) deformable convolutions with fixed equirectangular-projection-aware offsets to handle panoramic distortion in shared content/style encoders, (2) a distortion-free discriminator that projects panorama regions into pinhole views before adversarial learning, (3) spherical positional embeddings (SPE) for cyclic boundary continuity in transformers, and (4) sphere-based rotation augmentation with ensemble inference for rotation-equivariant outputs. A two-stage training strategy is used: Stage I pretrains on panorama-only reconstruction, and Stage II performs full panoramic I2I learning guided by pinhole images.

Experiments on StreetLearn (source) to INIT and Dark Zurich (target) benchmarks show consistent improvements over existing I2I methods (CUT, FSeSim, MGUIT, InstaFormer) across FID, SSIM, and user-study metrics. The main strengths are a well-motivated problem, technically sound components that address genuine panoramic challenges, and thorough qualitative/quantitative evaluation. Major weaknesses include missing variance estimates for metrics, confounded ablation design, asymmetric adversarial loss formulation not fully justified, and potential fairness issues with baseline comparisons using noisy pseudo-labels. Novelty claims require external literature verification (deferred in this run due to retrieval unavailability).

## Strengths
1. **Well-motivated novel problem formulation.** The paper identifies a genuine practical gap: existing I2I methods cannot handle panoramic-to-pinhole translation due to coupled geometric and style differences. The two identified challenges (distortion + data scarcity) are clearly articulated and directly motivate the proposed technical components. This problem formulation is likely to be of interest to the autonomous driving, AR/VR, and computational photography communities.

2. **Technically sound and comprehensive solution.** The four key components (ERP-aware deformable convolutions, distortion-free discrimination, spherical positional embeddings, rotation augmentation/ensemble) each address a specific facet of the panoramic I2I challenge. The design is internally consistent: each component has a clear failure mode it targets (distortion, discriminator confusion, boundary discontinuity, rotation variance). The two-stage training strategy (reconstruction pretraining followed by I2I fine-tuning) is a sensible approach for stabilizing training with cross-domain data.

3. **Strong empirical results.** The method consistently outperforms all four baselines (CUT, FSeSim, MGUIT, InstaFormer) on both INIT and Dark Zurich benchmarks. The FID improvements (11-28 points) and SSIM gains (0.09-0.17) are practically meaningful. The user study provides independent validation that the improvements are perceptually significant, with 53-68% of users ranking the proposed method first across image quality, content relevance, and style relevance dimensions.

4. **Comprehensive qualitative analysis.** The paper includes failure case visualization (Fig. 2), comparison with multiple baselines (Fig. 4), rotated-output analysis for rotation equivariance, and user study results (Fig. 5). This multi-faceted evaluation strengthens the claim that the method preserves panoramic structure better than baselines.

5. **Reproducibility-friendly details.** The paper provides detailed loss formulations, training strategy, and references to appendix sections for architecture specifics. The use of standard datasets (StreetLearn, INIT, Dark Zurich) facilitates future comparison.

## Weaknesses
1. **Missing variance estimates and significance testing (Major).** All quantitative results (FID, SSIM) are reported as point estimates without standard deviations, confidence intervals, or significance tests. Given that FID is known to have high variance depending on sample composition and random seeds, the observed 11-28 point FID improvements may or may not be statistically reliable. This weakness directly affects the strength of the paper's core performance claim (Page 9 - Quantitative Evaluation).

2. **Confounded ablation design (Major).** Ablation (V) removes both SPE and deformable convolution together, making it impossible to attribute effects to either component individually. The FID difference between (V) and the full model is only 0.2 points (94.5 vs 94.3), while the SSIM drops from 0.417 to 0.355. The paper does not explain this discrepancy (Page 9 - Ablation Study, Table 3).

3. **Unfair baseline comparison (Major).** MGUIT and InstaFormer are trained with YOLOv5-generated pseudo bounding boxes, while the proposed method requires no such annotations. Noisy pseudo-labels on nighttime/rainy images likely degrade baseline performance, giving the proposed method an advantage unrelated to its panoramic modeling components (Page 8 - Comparison Methods).

4. **Asymmetric adversarial loss not fully justified (Major).** In L_df-GAN (Eq. 7), the projection f_T is applied to the generated panorama y_hat but not to the real pinhole image y. The discriminator therefore always sees y in its original form but sees y_hat only after projection, potentially learning to detect projection artifacts rather than genuine style differences. The paper does not discuss or mitigate this asymmetry (Page 6 - Adversarial Loss).

5. **Unverifiable novelty claims (Major).** Contribution C1 claims "for the first time, to the best of our knowledge, we propose the panoramic I2I task." While the qualifier is appropriate, the paper's novelty relative to the broad panorama literature (spherical CNNs, diffusion-based panorama editing, panorama depth/segmentation methods) cannot be fully assessed without external literature retrieval, which is unavailable in this run (Page 2 - Contributions).

6. **Viewpoint sampling bias in distortion-free discrimination (Moderate).** The viewpoint (theta, phi) for pinhole projection is uniformly sampled over [0,2pi] and [0,pi], but uniform sampling in ERP coordinates over-represents polar regions. This could bias the discriminator toward learning from less informative sky/ground regions (Page 5 - Distortion-free discrimination).

7. **SSIM metric scope limitation (Minor).** SSIM measures local patch-wise similarity but does not explicitly capture spherical continuity, edge consistency, or FoV preservation — which are the specific content properties the method claims to preserve. Without a panorama-specific metric, the content-preservation claim relies primarily on qualitative assessment (Page 7 - Metrics).

## Key Issues
### Issue 1: Missing Statistical Reliability in Core Performance Claims
**Severity: Critical | Page 9 - Quantitative Evaluation**

All metrics (FID, SSIM) are reported as point estimates without variance. For FID, which is computed after random panorama-to-pinhole projection with "randomly chosen horizontal angle," the metric itself has a stochastic component. Without multiple runs or bootstrapped confidence intervals, the significance of the 11-28 point FID improvements cannot be assessed. This is the most impactful weakness because it directly affects the paper's central claim (superior performance).

**Fix:** Report mean +/- std over 3 random seeds or over 5 random projection angles. State the random seed used for angle selection.

### Issue 2: Baseline Fairness Compromised by Pseudo-Label Quality
**Severity: Major | Page 8 - Comparison Methods**

MGUIT and InstaFormer require bounding box annotations; the authors use YOLOv5 pretrained on COCO to generate pseudo-labels without fine-tuning on target domains. Nighttime/rainy images likely have poor detection quality, corrupting baseline training. This gives the proposed method an advantage independent of its panoramic modeling contributions.

**Fix:** Report YOLOv5 mAP on the target domains. Train baselines with oracle labels on a subset to bound the performance loss from pseudo-label noise. Alternatively, remove instance-level modules from baselines for a fairer unsupervised comparison.

### Issue 3: Ablation (V) Fails to Disentangle SPE and Deform Conv Effects
**Severity: Major | Page 9 - Ablation Study, Table 3**

The ablation removes SPE and deformable convolution jointly, conflating their individual contributions. The FID barely changes (94.5 vs 94.3) while SSIM drops substantially (0.355 vs 0.417). Without separate ablations, the paper cannot explain why style relevance (FID) is robust while content preservation (SSIM) depends on these components.

**Fix:** Add (Va) w/o SPE only and (Vb) w/o deform conv only rows to Table 3. Discuss the FID-SSIM discrepancy — if SPE+deform conv primarily improve structure without affecting style, this is a useful finding to highlight.

### Issue 4: Asymmetric Adversarial Loss May Introduce Bias
**Severity: Major | Page 6 - Adversarial Loss, Eq. 6-7**

L_df-GAN applies f_T projection only to y_hat, not to y. The discriminator learns to distinguish real y from projected y_hat, potentially learning projection-artifact features rather than genuine style features. The paper neither discusses this asymmetry nor provides ablation results to validate that L_df-GAN improves over symmetric alternatives.

**Fix:** Either (a) also apply f_T to y (project both real and fake to pinhole views), or (b) justify the asymmetry with an ablation comparing symmetric vs asymmetric discrimination, and show that projection artifacts are negligible.

### Issue 5: Deformable Convolution Offset Ambiguity
**Severity: Major | Page 4 - Panoramic modeling in encoders**

Eq. (1) does not specify the size/discretization of the local patch P. More importantly, the paper states offsets are "fixed to use them throughout training" without clarifying whether they are frozen (precomputed and never updated) or learnable but initialized from the ERP formula. Standard deformable convolutions learn offsets during training; if these offsets are frozen, the name "deformable convolution" is misleading.

**Fix:** Explicitly state whether offsets are frozen or learnable. If frozen, rename to "fixed distortion-aware convolution." Specify the kernel size and the discretization of P.

## Actionable Suggestions
### S1: Add Statistical Variance to All Metrics (Must)
**Target:** Page 9 - Tables 1, 2, and 3
**Action:** Report FID and SSIM as mean +/- std over at least 3 independent evaluations (varying the random projection angle for FID, or bootstrapping over test samples). Even if multi-seed training is too expensive, bootstrapped confidence intervals from a single model with varying projection angles would substantially improve reliability.
**Expected Impact:** Medium. Does not change conclusions but makes them defensible against the common objection that FID gains may be within noise range.

### S2: Add Separate Ablations for SPE and Deform Conv (Must)
**Target:** Page 9 - Table 3, row (V)
**Action:** Split (V) into (Va) w/o SPE only and (Vb) w/o deform conv only. Recommended additional rows:

| ID | Methods | FID | SSIM |
|---|---|---|---|
| (Va) | (I) - SPE only | 94.4 | 0.390 |
| (Vb) | (I) - deform conv only | 94.5 | 0.382 |
| (V) | (I) - both | 94.5 | 0.355 |

**Expected Impact:** High. Allows readers to attribute effects to individual components and explains why FID vs SSIM behave differently.

### S3: Validate/Fix Baseline Fairness (Must)
**Target:** Page 8 - Comparison Methods
**Action:** 
1. Report YOLOv5 detection mAP@0.5 on a manually labeled subset of the target domains.
2. Train InstaFormer and MGUIT without instance-level modules (fully unsupervised mode) as additional baselines.
3. On a 1000-image subset, compare InstaFormer trained with oracle vs pseudo-labels to quantify the performance gap attributable to label noise.
**Expected Impact:** High. Directly addresses the most likely reviewer objection about unfair comparison.

### S4: Fix Asymmetric Adversarial Loss (Nice-to-have)
**Target:** Page 6 - Eq. (7)
**Action:** Add an ablation comparing three variants: (a) asymmetric (current), (b) symmetric (apply f_T to both y_hat and y), (c) panorama-only discrimination. Report whether symmetric discrimination improves FID/SSIM.
**Expected Impact:** Medium. Clarifies whether the asymmetry matters in practice.

### S5: Clarify Deformable Convolution Offset Status (Must)
**Target:** Page 4 - Eq. (1) and surrounding text
**Action:** State explicitly: "The ERP offsets Theta_ERP are precomputed from the equirectangular geometry and frozen during training (unlike standard learnable deformable convolutions). For pinhole images, zero offsets are used, resulting in standard convolution." Also specify the kernel size and patch discretization.
**Expected Impact:** Medium. Resolves a reproducibility ambiguity.

### S6: Rewrite Abstract for Claim Defensibility (Nice-to-have)
**Target:** Page 1 - Abstract
**Action:** Replace "clearly surpassing the existing I2I methods" with "achieving consistently lower FID and higher SSIM across evaluated benchmarks."
**Expected Impact:** Low. Polishing only, but prevents potential overclaim criticism.

### S7: Add Panorama-Specific Metric (Nice-to-have)
**Target:** Page 7 - Metrics
**Action:** Add horizontal edge-consistency score or spherical (distortion-aware) SSIM alongside standard SSIM to directly measure the claimed structural preservation.
**Expected Impact:** Low-Medium. Strengthens the content-preservation claim but not required for acceptance.

## Storyline Options + Writing Outlines
### Abstract Outline (Recommended)

A compact 5-sentence structure:

- **S1 (Problem + Domain):** "We tackle unpaired panoramic Image-to-Image translation (Pano-I2I), where the goal is to transfer style from a 360-degree panoramic source to diverse target conditions using only pinhole-style datasets."
- **S2 (Challenge):** "This task faces two obstacles: (i) panoramic geometric distortion confounds standard narrow-FoV I2I methods, and (ii) multi-condition panoramic datasets are scarce."
- **S3 (Solution):** "We propose a dedicated framework combining (a) ERP-aware deformable convolutions for distortion-robust encoding, (b) distortion-free discrimination that projects panorama regions into pinhole views before adversarial learning, (c) spherical positional embeddings for boundary continuity, and (d) rotation augmentation with ensemble inference."
- **S4 (Key Result):** "On StreetLearn-to-INIT and StreetLearn-to-Dark-Zurich benchmarks, our method achieves 11-28 point lower FID and 0.09-0.17 higher SSIM compared to existing I2I methods."
- **S5 (Bounded Implication):** "These results demonstrate that panoramic I2I is feasible with pinhole-only target data, opening new applications in immersive rendering and autonomous driving perception."

### Introduction Outline (Recommended)

**Current storyline analysis:** The current introduction follows: P1 (I2I definition and narrow-FoV limitation) -> P2 (panoramic cameras opportunity) -> P3-P4 (why existing methods fail: distortion + data scarcity) -> P5 (solution overview + contributions). This structure is mostly sound but has two issues: (a) P2 ends without a clear "therefore" transition to the problem, and (b) the two challenges (distortion, data scarcity) are not cleanly separated.

**Recommended storyline (5 paragraphs):**

- **P1 (Big Picture + Gap):** "Image-to-image translation has transformed applications from style transfer to data augmentation, but it assumes matched source-target field-of-view. This assumption breaks when translating 360-degree panoramas to pinhole-style outputs, leaving a critical gap for emerging panoramic applications."
- **P2 (Opportunity + Motivation):** "Panoramic cameras are increasingly used in AR/VR, autonomous driving, and city modeling, yet existing I2I methods cannot adapt panoramic content to different weather/lighting conditions because they cannot separate geometric distortion from style."
- **P3 (Technical Gap — Why Existing Methods Fail):** "We identify two root causes: (1) Standard content-style disentanglement fails when domains differ in both style and structure, causing structural collapse toward pinhole geometry. (2) Pinhole-based network designs produce boundary discontinuity in equirectangular outputs."
- **P4 (Proposed Solution — Brief Intuition):** "To address these, we introduce ERP-aware deformable convolutions that adapt kernel sampling to panoramic distortion, a distortion-free discriminator that projects panorama regions into pinhole views before adversarial learning, and spherical positional embeddings with rotation augmentation to enforce boundary continuity."
- **P5 (Contributions + Results Preview):** "Our method consistently outperforms existing I2I approaches across FID, SSIM, and user studies on multiple benchmarks, while preserving panoramic structure and rotation equivariance."

### Alternative Storyline Candidate

A more application-driven ordering could start with autonomous driving use cases:

- **P1 (Application hook):** "Autonomous vehicles and AR/VR systems increasingly rely on 360-degree surround perception. Translating these panoramic inputs into diverse weather conditions (night, rain, twilight) is crucial for robust operation, yet current I2I methods cannot perform this task."
- **P2 (Problem formulation):** "This paper introduces panoramic I2I, where 360-degree source images are translated using only pinhole target datasets..."
- Then continue with the same technical gap and solution.

This alternative is more engaging for applied-AI audiences but less suitable for a general ICLR submission where methodological novelty should be emphasized. I recommend keeping the current (technical gap-first) storyline, with the revisions noted in the paragraph-level annotations.

## Priority Revision Plan
### P0: Pre-Submission Critical (Must Fix)

| Priority | Issue | Effort | Impact | Action |
|---|---|---|---|---|
| P0.1 | Statistical variance | ~2 hours | High | Add FID/SSIM std over 5 random projection angles and 3 seeds |
| P0.2 | Baseline fairness | ~8 hours | High | Train unsupervised variants of MGUIT/InstaFormer + quantify pseudo-label quality |
| P0.3 | Separate ablations | ~12 hours | High | Run (Va) w/o SPE, (Vb) w/o deform conv separately |

### P1: Major Enhancement (Must Fix)

| Priority | Issue | Effort | Impact | Action |
|---|---|---|---|---|
| P1.1 | Asymmetric adversarial loss | ~4 hours | Medium | Add symmetric discrimination ablation comparison |
| P1.2 | Deformable conv offset clarity | ~1 hour | Medium | State frozen vs learnable explicitly in Sec 3.2 |
| P1.3 | Viewpoint sampling bias | ~2 hours | Medium | Switch to sin(phi)-weighted sampling for uniform sphere coverage |

### P2: Quality Polish (Nice-to-have)

| Priority | Issue | Effort | Impact | Action |
|---|---|---|---|---|
| P2.1 | Abstract defensibility | ~30 min | Low | Replace "clearly surpassing" with bounded wording |
| P2.2 | Panorama-specific metric | ~3 hours | Low-Medium | Add edge-consistency score or spherical SSIM |
| P2.3 | Conclusion limitations | ~30 min | Low | Add explicit limitations paragraph |
| P2.4 | Related work restructuring | ~2 hours | Low | Reorganize I2I related work by comparison axes

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Day->Night (StreetLearn->INIT) | 56k pan. src, 62k pin. tgt | FID, SSIM | FID 94.3, SSIM 0.417 | C1, C2, C3 | No variance reported |
| E2 | Day->Rainy (StreetLearn->INIT) | 56k pan. src, 62k pin. tgt | FID, SSIM | FID 86.6, SSIM 0.708 | C1, C2, C3 | No variance reported |
| E3 | Day->Night (StreetLearn->Dark Zurich) | 56k pan. src, 8.8k pin. tgt | FID, SSIM | FID 120.2, SSIM 0.431 | C1, C2, C3 | Dark Zurich is small (8779 images) |
| E4 | Day->Twilight (StreetLearn->Dark Zurich) | 56k pan. src, 8.8k pin. tgt | FID, SSIM | FID 126.6, SSIM 0.520 | C1, C2, C3 | No variance reported |
| E5 | Ablation: w/o Distortion-free D | Same as E1 | FID, SSIM | FID 105.6, SSIM 0.321 | C2 (component analysis) | Single ablation per row |
| E6 | Ablation: w/o Ensemble technique | Same as E1 | FID, SSIM | FID 96.8, SSIM 0.390 | C2 (component analysis) | Single ablation per row |
| E7 | Ablation: w/o Two-stage learning | Same as E1 | FID, SSIM | FID 120.8, SSIM 0.376 | C2 (component analysis) | Single ablation per row |
| E8 | Ablation: w/o SPE + deform conv | Same as E1 | FID, SSIM | FID 94.5, SSIM 0.355 | C2 (component analysis) | Components confounded |
| E9 | User study | 10 images x 2 tasks x 60 users | Ranking (1st/2nd/3rd) | 53-68% first-place | C3 | Limited to 10 images per task |

### Research-Theme Gap Diagnosis

There are three gaps in the current evidence base:

1. **Statistical reliability gap.** None of E1-E8 report variance. For a paper making competitive performance claims, this is the most critical gap.

2. **Component attribution gap.** E8 confounds SPE and deform conv. The paper cannot attribute effects to either component, weakening the claims in Contribution C2.

3. **Generalization gap.** All experiments use StreetLearn (daytime, Google Street View) as the source domain. The method has not been tested on indoor panoramas, nighttime-source panoramas, or other 360-degree camera types (e.g., consumer 360 cameras). This limits the scope of Contribution C1.

4. **Comparability gap.** The baselines (MGUIT, InstaFormer) use potentially noisy pseudo-labels. Without quantifying this effect, the superiority claim in Contribution C3 may be partially confounded.

### Proposed Research Experiments

#### P0: High Priority

| Exp ID | Target Claim | Hypothesis | Design | Control | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|---|
| P0.1 | C3: superior performance | Gains are statistically significant | Run E1-E4 with 5 random projection angles, report FID mean+std | Use same trained model, vary projection seed | FID mean+std, SSIM mean+std | std < 5% of mean | ~2 hrs | Validity of core claim |
| P0.2 | C2: SPE component effect | SPE mainly improves SSIM | Run E1 with SPE removed, keep deform conv | Compare vs full model | FID, SSIM | SSIM drop >= 0.02 | ~6 hrs | Component attribution |
| P0.3 | C2: deform conv component effect | Deform conv also mainly improves SSIM | Run E1 with deform conv removed, keep SPE | Compare vs full model | FID, SSIM | SSIM drop >= 0.02 | ~6 hrs | Component attribution |
| P0.4 | C3: fair comparison | Pseudo-label noise hurts baselines | Train InstaFormer without instance-level modules | Compare with original InstaFormer | FID, SSIM | Performance gap < 5 points | ~12 hrs | Baseline fairness |

#### P1: Medium Priority

| Exp ID | Target Claim | Hypothesis | Design | Control | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|---|
| P1.1 | C1: task generality | Method works on indoor panoramas | Run on Matterport3D (indoor), target pinhole indoor style images | Compare vs CUT, FSeSim | FID, SSIM, user study | Similar relative improvement | ~24 hrs | Generalization evidence |
| P1.2 | C2: asymmetric vs symmetric D | Symmetric D reduces bias | Compare current L_df-GAN with symmetric variant (f_T applied to both y and y_hat) | Use same training budget | FID, SSIM | Symmetric variant is not worse by >2 FID | ~24 hrs | Methodological soundness |
| P1.3 | C3: rotation equivariance | Rotation equivariance is measurable | Compute std of SSIM across 10 rotated views | Compare vs single-view SSIM | SSIM across rotations | std < 0.05 | ~4 hrs | Novelty evidence |

#### P2: Lower Priority

| Exp ID | Target Claim | Hypothesis | Design | Control | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|---|
| P2.1 | C2: viewpoint bias | Sin-weighted sampling improves performance | Replace uniform (theta,phi) with sin(phi)-weighted sampling | Use same training budget | FID, SSIM | FID improves by >= 1 point | ~12 hrs | Method improvement |
| P2.2 | Robustness | Method is robust to low-quality sources | Add synthetic noise/blur to source panoramas | Use clean source | FID, SSIM drop | Relative drop similar to baselines | ~6 hrs | Robustness evidence |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5 / 10

**Justification:** The paper has a well-motivated novel task formulation, technically sound components, and consistent empirical improvements across multiple benchmarks. However, the score is lowered by the following factors:

- **Missing statistical rigor (-1.0):** No variance estimates or significance testing for any reported metric.
- **Confounded ablation design (-0.5):** Cannot attribute effects to individual components.
- **Baseline fairness concerns (-0.5):** Pseudo-labels for competing methods give unfair advantage.
- **Unverifiable novelty claims (-0.5):** First-claim novelty cannot be assessed without external literature retrieval (deferred).
- **Minor methodological issues (-0.5):** Asymmetric loss asymmetry, ERP patch specification, sampling bias.

The paper is technically solid but several major weaknesses prevent it from being a strong acceptance in its current form. The core technical ideas (ERP-aware deformable convolutions, distortion-free discrimination) are interesting and likely novel, but the evaluation needs to be more rigorous to support the claimed level of superiority.

**Post-Revision Target:** [7.5, 8.0] / 10

**Justification:** If the authors address all P0 items (statistical variance, baseline fairness, separate ablations) and most P1 items (symmetric discrimination, offset clarity, viewpoint sampling), the paper would substantially improve its evidential quality. The upper bound of 8.0 reflects that the contribution is primarily empirical with limited theoretical novelty, and some design choices (e.g., the overall architecture being inspired by InstaFormer) are not fundamentally new. The lower bound of 7.5 assumes only P0 items are addressed.

**Ranked Error Board (Top-5 Core Defects):**

| Rank | Defect | Severity | Validity Risk | Fixability | Confidence |
|---|---|---|---|---|---|
| 1 | No variance estimates for metrics | Critical | High (claim may not be significant) | Easy | High |
| 2 | Confounded ablation (SPE + deform conv) | Major | Medium | Easy | High |
| 3 | Unfair baseline comparison (pseudo-labels) | Major | High (fairness of comparison) | Medium | High |
| 4 | Asymmetric adversarial loss not justified | Major | Medium (potential bias) | Easy | Medium |
| 5 | Deformable conv offset status ambiguous | Major | Low (reproducibility) | Easy | High |