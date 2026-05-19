## Summary
# Final Review Report

## Summary

This paper presents LRM (Large Reconstruction Model), a transformer-based encoder-decoder framework for single-image-to-3D reconstruction. LRM uses a pre-trained DINO ViT as image encoder and a 16-layer transformer decoder to project 2D image features onto a triplane NeRF representation via cross-attention and self-attention. The model contains 500M parameters and is trained end-to-end on approximately 1M objects from Objaverse (synthetic) and MVImgNet (real video) using only image reconstruction losses (MSE + LPIPS). At inference, LRM produces a 3D mesh from a single image in approximately 5 seconds.

**Strengths**: The paper demonstrates impressive reconstruction quality across diverse input types (real photos, generated images, rendered objects), with reasonable geometric consistency and texture detail. The feed-forward design avoids per-instance optimization, making inference fast. The training framework is conceptually clean—no 3D-aware regularizers or delicate hyperparameter tuning.

**Core Weaknesses**: (1) The "first large-scale 3D reconstruction model" claim conflicts with cited prior works (Point-E, Shap-E) that also operate at scale. (2) Inference relies on fixed camera parameters matched to training data, a strong assumption that limits real-world applicability and is under-emphasized in the abstract and introduction. (3) Quantitative evaluation is limited to 100 objects (50+50), which is small relative to the 1M training set. (4) Training requires massive compute (128 A100 GPUs for 3 days), limiting reproducibility. (5) The abstract overclaims generalization without adequately caveating the camera and Lambertian assumptions.

## Strengths
1. **Clean, scalable training framework**: LRM's design is elegantly simple—a transformer encoder-decoder trained with standard image reconstruction losses (MSE + LPIPS) on multi-view data. No 3D-aware regularization, GAN training, or distillation from diffusion models is needed. This conceptual clarity is a genuine strength that makes the framework extensible.

2. **Fast inference without per-instance optimization**: Unlike NeRF-based methods that require minutes to hours of per-shape optimization, LRM produces a 3D mesh in ~5 seconds via a single feed-forward pass. This is a meaningful practical advantage for downstream applications.

3. **Impressive qualitative generalization**: The visual results (Fig. 2, Appendix E) show high-quality reconstruction across diverse categories—animals, household objects, plants, generated images, and real photos. The model convincingly handles asymmetric objects (giraffe, penguin, bear) by inferring reasonable occluded geometry, demonstrating effective cross-shape priors.

4. **Thorough ablation and analysis (Appendix D)**: The paper provides extensive ablation studies on data composition (synthetic vs. real), number of training views, model depth, triplane resolution, camera pose normalization, rendering resolution, and LPIPS loss contribution. These analyses are valuable for understanding LRM's design decisions and for future research building on this work.

5. **Honest limitations section**: Sec. 4.3.2 identifies four concrete limitations (blurry occluded regions, fixed camera assumption, background dependence, Lambertian assumption) with reasonable explanations. This transparency is commendable and provides clear directions for improvement.

6. **Reproducibility commitment**: The paper specifies data sources (Objaverse, MVImgNet), pre-processing steps, architecture details, training hyperparameters, and software dependencies. The use of publicly available codebases (threestudio, x-transformers, DINO) further supports reproducibility.

## Weaknesses
1. **Overclaimed novelty positioning (Major)**: The paper claims LRM is "the first large-scale 3D reconstruction model" (Page 2) but later acknowledges in Appendix C that Point-E and Shap-E are large-scale models trained on millions of 3D assets with hundreds of millions of parameters. This internal contradiction weakens the novelty claim. The actual contribution—first large-scale *direct image-to-NeRF regression* model—is still significant and should be positioned honestly.

2. **Hidden camera assumption severely constrains real-world applicability (Major)**: Inference assumes fixed camera intrinsics and extrinsics matching Objaverse training data (Page 8). This is a critical deployment limitation that is only fully acknowledged in Sec. 4.3.2 (Limitations), not in the abstract or introduction. For in-the-wild images with unknown or different camera parameters, reconstruction quality can degrade substantially (Fig. 4).

3. **Insufficient quantitative evaluation breadth (Major)**: The main quantitative evaluation uses only 100 test objects (50 Objaverse + 50 MvImgNet). For a model trained on ~1M objects, this evaluation set is too small to robustly support strong generalization claims. The SOTA comparison (Appendix C) uses 100 GSO objects. Per-category breakdowns and larger-scale evaluation are needed.

4. **Extreme compute requirements limit reproducibility (Major)**: Training requires 128 A100 GPUs for 3 days (~9,216 GPU-hours). This is prohibitive for most academic labs and is not adequately disclosed in the main text. The smaller "baseline" model used for ablation (32 GPUs, 15 epochs) is still resource-intensive.

5. **Abstract overclaims generalization (Major)**: The abstract states the model is "highly generalizable" and "produces high-quality 3D reconstructions from various testing inputs, including real-world in-the-wild captures" without caveating the camera parameter assumption. This could mislead readers about deployment readiness.

6. **Missing variance/statistical reporting**: No standard deviations, confidence intervals, or significance tests are reported for any quantitative metric. Given that the PSNR differences between some ablations are small (e.g., 0.1-0.2 dB), statistical significance is unclear.

7. **Related work section is a literature list rather than structured comparison**: The related work (Sec. 2) reads as a chronological survey with paper-by-paper summaries rather than being organized around comparison axes (e.g., supervision type, representation, inference speed). This makes it harder for readers to quickly understand LRM's position relative to prior work.

## Key Issues
**Issue 1: "First large-scale 3D model" claim vs. cited evidence (Critical)**
- **Anchor**: Page 2 - Introduction paragraph 4; Page 20 - Appendix C
- **Problem**: The main paper claims LRM is "the first large-scale 3D reconstruction model" with 500M parameters and ~1M training objects. However, Appendix C explicitly discusses Point-E and Shap-E as having "hundreds of millions of learnable parameters" trained on "several million 3D assets." This creates a direct contradiction: either LRM is not the first, or the qualifier "large-scale" is defined differently from Point-E/Shap-E.
- **Impact**: If unresolved, this claim could be rejected by reviewers as overstatement or inaccurate positioning. It undermines trust in the paper's self-assessment.
- **Fix**: Reposition as "the first large-scale model to directly regress a triplane NeRF from a single image in an end-to-end manner" and explicitly acknowledge Point-E/Shap-E as prior large-scale 3D models with different objectives.

**Issue 2: Unconditional camera assumption at inference (Major)**
- **Anchor**: Page 8 - Inference paragraph; Page 9 - Sec. 4.3.2 Limitations
- **Problem**: The model assumes fixed camera parameters (matching Objaverse training data) for all inference inputs. This is a strong inductive bias that is not disclosed in the abstract, introduction, or contribution summary. Real-world images with different FoV, principal point, or camera distance will produce distorted reconstructions (Fig. 4).
- **Impact**: The paper's claims of "generalization to arbitrary in-the-wild images" are only valid under this camera assumption, which is rarely satisfied in practice.
- **Fix**: (a) Add camera assumption caveat to abstract and introduction. (b) Provide a sensitivity analysis showing reconstruction quality vs. camera parameter mismatch. (c) Discuss potential mitigation (e.g., incorporating camera pose estimation).

**Issue 3: Insufficient quantitative evaluation scale (Major)**
- **Anchor**: Page 6 - Evaluation paragraph; Page 20 - Appendix C
- **Problem**: The main analysis uses 50+50 test objects. The SOTA comparison uses 100 GSO objects. For a model trained on ~1M objects, this evaluation coverage (~0.01%) is too sparse to support strong generalization claims. No per-category breakdown or statistical significance testing is provided.
- **Impact**: The quantitative evidence is suggestive but not conclusive. Small evaluation sets may overstate or understate true generalization performance.
- **Fix**: Expand evaluation to at least 500-1000 objects with per-category analysis. Report standard deviations across multiple evaluation seeds.

**Issue 4: Training irreproducibility due to extreme compute (Major)**
- **Anchor**: Page 8 - Training paragraph
- **Problem**: Training requires 128 A100 GPUs for 3 days. This is an order of magnitude beyond what most academic labs can access. The paper does not discuss whether a smaller model can be trained with fewer resources while retaining meaningful performance.
- **Impact**: The work cannot be verified, built upon, or extended by most researchers in the field, limiting its scientific impact.
- **Fix**: (a) Provide a clear resource scaling analysis (performance vs. model size vs. compute). (b) Release pre-trained weights. (c) Report minimum resource requirements for meaningful training.

**Issue 5: Abstract/introduction overclaim without caveats (Major)**
- **Anchor**: Page 1 - Abstract; Page 1-2 - Introduction
- **Problem**: The abstract says "highly generalizable" and "high-quality 3D reconstructions from real-world in-the-wild captures" without qualifying the camera assumption, Lambertian material assumption, or background-removal requirement. The introduction similarly emphasizes generalization without bounded scope.
- **Impact**: Sets unrealistic reader expectations and is inconsistent with the limitations disclosed later.
- **Fix**: Replace unqualified "highly generalizable" with "generalizes across diverse object categories under assumed canonical camera parameters" or similar scoped language.

## Actionable Suggestions
### S1: Reposition the "first large-scale" claim (Must fix, P0)

**Current wording (Page 2, Introduction):**
"To the best of our knowledge, LRM is the first large-scale 3D reconstruction model"

**Problem:** Contradicts Appendix C discussion of Point-E and Shap-E as prior large-scale models.

**Revised wording:**
"To the best of our knowledge, LRM is the first large-scale model for direct single-image-to-NeRF regression, trained on approximately one million objects. While prior large-scale 3D models such as Point-E and Shap-E use diffusion on point cloud representations, LRM directly regresses a triplane NeRF in a single feed-forward pass, enabling fast end-to-end reconstruction without iterative refinement."

**Acceptance criteria:** The claim is scoped to "direct image-to-NeRF regression at scale" and explicitly acknowledges Point-E/Shap-E as prior large-scale 3D models.

### S2: Add camera sensitivity analysis (Must fix, P0)

**Current status:** The paper states the camera assumption as a limitation but provides no quantitative analysis of how reconstruction quality degrades with camera parameter mismatch.

**Action:** Add a new experiment varying FoV (±10%, ±20%, ±30%) and camera distance (±15%, ±30%) around the nominal Objaverse parameters, and report PSNR/LPIPS degradation curves. Include a table:

| Camera Perturbation | PSNR | LPIPS | Visual Quality |
|---|---|---|---|
| None (Objaverse default) | 20.1 | 0.160 | Good |
| FoV +10% | ... | ... | ... |
| FoV -10% | ... | ... | ... |
| Distance +30% | ... | ... | ... |

This quantifies the operating envelope and helps users decide when the method can be applied safely.

### S3: Expand quantitative evaluation (Must fix, P1)

**Action:** Evaluate on at least 500 held-out objects from Objaverse (stratified across categories) and 200 MvImgNet videos. Report per-category breakdown. Include standard deviations over 3 evaluation seeds.

**Expected outcome:** Stronger statistical support for generalization claims, and identification of categories where LRM performs poorly.

### S4: Disclose compute requirements in main text (Nice-to-have, P1)

**Action:** Add one sentence to the Training paragraph: "Total training cost is approximately 9,216 A100 GPU-hours. We will release pre-trained weights to facilitate reproduction and extension."

### S5: Add variance reporting to all quantitative results (Must fix, P1)

**Action:** For all tables reporting PSNR, SSIM, LPIPS, FID, and Chamfer Distance, include mean ± std over at least 3 evaluation runs (different seeds or different random subsets of test views).

### S6: Restructure Related Work (Nice-to-have, P2)

**Action:** Reorganize Sec. 2 around three comparison axes:
1. **By 3D representation**: point clouds, voxels, meshes, NeRF, triplane
2. **By supervision type**: category-specific, diffusion-guided, purely data-driven
3. **By inference speed**: per-shape optimization (slow) vs. feed-forward (fast)

For each axis, position LRM explicitly and state the concrete advantage.

### S7: Tighten Introduction narrative (Nice-to-have, P2)

**Action:** Rewrite Introduction using a clearer 4-paragraph structure:
- P1: Problem + prior gap (category-specific, diffusion-based, per-shape optimization)
- P2: Scaling lessons from NLP/Vision + unique 3D challenges
- P3: LRM approach overview (high-level: DINO encoder → transformer decoder → triplane NeRF)
- P4: Contributions (scoped, with explicit caveats about camera assumption)

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction has a reasonable arc but suffers from three issues:
1. **No explicit gap synthesis**: The first paragraph lists three prior limitations but does not synthesize them into a single, clear research gap.
2. **Delayed solution**: The NLP/Vision analogy paragraph (paragraph 2) delays the paper's own proposal until paragraph 3.
3. **Missing caveats**: The contribution paragraph (paragraph 4) makes a "first large-scale" claim without acknowledging Point-E/Shap-E.

### Recommended Storyline: "Data-Driven 3D at Scale"

**Rationale**: This storyline prioritizes the paper's strongest contribution—demonstrating that large-scale data + simple losses + transformer architecture can produce a generalizable 3D reconstructor—while honestly positioning it relative to prior large-scale 3D works.

**Abstract Outline (5 sentences):**
- S1 (Problem): Single-image 3D reconstruction is challenged by geometric ambiguity, with prior methods limited to narrow categories, slow per-shape optimization, or reliance on 2D diffusion priors.
- S2 (Gap): No existing method demonstrates that direct feed-forward regression from image to 3D can scale to diverse, in-the-wild objects.
- S3 (Method): We propose LRM, a 500M-parameter transformer encoder-decoder that directly regresses a triplane NeRF from a single image using only image reconstruction losses.
- S4 (Training): LRM is trained end-toend on ~1M multi-view objects (Objaverse + MVImgNet).
- S5 (Results + Caveat): LRM produces high-quality 3D shapes in 5 seconds from diverse inputs under assumed canonical camera parameters, with known limitations on occluded regions and non-Lambertian materials.

**Introduction Outline (4 paragraphs):**

- **P1 (Problem + Prior Gaps):** "Single-image 3D reconstruction remains challenging due to geometric ambiguity. Prior approaches fall into three paradigms: (a) category-specific methods that generalize poorly, (b) diffusion-guided methods requiring delicate tuning, and (c) per-shape optimization methods that are slow. All three fail to provide a fast, generalizable, and purely data-driven solution."

- **P2 (Scaling Inspiration + 3D Challenges):** "The success of large-scale models in NLP and vision suggests that scaling transformer architectures, data, and simple objectives can produce powerful general representations. However, 3D poses unique challenges: standardized representations are lacking, and multi-view supervision is harder to collect than text or image data."

- **P3 (LRM Approach):** "In this work, we investigate whether a generic 3D prior can be learned from ~1M multi-view objects using a simple feed-forward design. LRM uses a pre-trained DINO encoder and a transformer decoder to directly regress a triplane NeRF. The entire model is trained end-to-end with MSE and LPIPS losses—no 3D-aware regularizers or distillation needed."

- **P4 (Contributions, Scoped):** "We make three contributions: (1) We demonstrate that a 500M-parameter transformer can learn a generalizable image-to-3D mapping from multi-view data alone. (2) LRM achieves 5-second inference, two orders of magnitude faster than per-shape optimization methods. (3) We provide extensive ablations on data composition, model architecture, and supervision. Limitations include reliance on assumed camera parameters and Lambertian materials."

### Alternative Storyline: "Feed-Forward 3D without 2D Priors"

**Emphasis**: Highlight the contrast with diffusion-based methods (Zero-1-to-3, Make-It-3D, One-2-3-45). Structure: (a) Diffusion methods are powerful but slow and complex. (b) Direct regression is simpler and faster but needs large data. (c) LRM shows that direct regression works at scale. This storyline positions the contribution more competitively but risks over-emphasizing a negative comparison.

### Alignment Check

| Criterion | Current | Recommended |
|---|---|---|
| Problem alignment | Good but cluttered | Clearer hierarchy |
| Variable alignment | Terms match method | Same; improved transitions |
| Contribution-evidence | "First" claim overreaches | Scoped claim matches evidence |

## Priority Revision Plan
### P0 (Critical — Must fix before resubmission)

| # | Issue | Action | Expected Impact |
|---|---|---|---|
| 1 | "First large-scale 3D model" claim contradicts Appendix C | Reposition claim to "first large-scale direct NeRF regression model"; acknowledge Point-E/Shap-E | Resolves novelty overclaim; aligns main text with appendix |
| 2 | Abstract overclaims generalization | Add camera assumption caveat to abstract and introduction | Sets accurate reader expectations |
| 3 | Inference camera assumption hidden | Add sensitivity analysis; discuss in abstract/intro | Transparency about deployment constraints |
| 4 | Missing variance reporting | Add std/CI to all tables | Allows assessing statistical reliability |

### P1 (Major — High impact on paper quality)

| # | Issue | Action | Expected Impact |
|---|---|---|---|
| 5 | Small evaluation set | Expand to 500+ test objects; per-category breakdown | Stronger generalization evidence |
| 6 | Training compute disclosure | Add GPU-hour total + pre-trained weights release plan | Improves reproducibility assessment |
| 7 | Limitations need quantification | Add blur metric, FoV sensitivity range, Lambertian degradation | Turns generic list into operating envelope |
| 8 | Introduction narrative density | Restructure to 4 clear paragraphs (Problem → Scaling → Approach → Contributions) | Improved readability and narrative flow |

### P2 (Nice-to-have — Quality improvements)

| # | Issue | Action | Expected Impact |
|---|---|---|---|
| 9 | Related work is a literature list | Reorganize by comparison axes | Clearer positioning |
| 10 | Conclusion introduces new unsupported claims | Trim to validated findings only | Scientific discipline |
| 11 | DINO feature choice unablated | Add [CLS]-only vs all-patches ablation | Supports design justification |
| 12 | Loss function input view ambiguity | Clarify whether input view is included in V=4 total | Technical clarity |

### Revision Sequence (Recommended execution order)

```text
Stage 1 (immediate, 1-2 days):
  → Fix Issue 1: Reposition "first large-scale" claim
  → Fix Issue 2: Add camera caveat to abstract/intro
  → Fix Issue 4: Add std to all tables
  → Fix Issue 8: Restructure introduction narrative

Stage 2 (before submission, 1-2 weeks):
  → Fix Issue 3: Run camera sensitivity analysis
  → Fix Issue 5: Expand evaluation set (can reuse existing checkpoints)
  → Fix Issue 6: Compute total GPU-hours + prepare weights release
  → Fix Issue 7: Quantify each limitation

Stage 3 (polishing):
  → Fix Issue 9: Restructure Related Work
  → Fix Issue 10: Tighten conclusion
  → Fix Issue 11: Add [CLS] ablation
  → Fix Issue 12: Clarify loss formulation
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Main evaluation: novel view synthesis quality | 50 Objaverse + 50 MvImgNet; 5/15 views; PSNR/CLIP/SSIM/LPIPS | PSNR 20.1, CLIP 91.0, SSIM 79.7, LPIPS 0.160 | Strong reconstruction quality on held-out objects | Generalization claim | Small sample (100 total); no per-category breakdown |
| E2 | SOTA comparison (Appendix C) | 100 GSO objects; 20 ref views; 4 baselines | FID 31.44, PSNR 19.60, CD 0.053 | LRM outperforms Point-E/Shap-E/One-2-3-45 on all metrics | SOTA claim | GSO only; baselines may have been disadvantaged by background-removal pipeline |
| E3 | Synthetic vs. Real data (D.1) | Ablation baseline model; Objaverse/MvImgNet subsets | PSNR/LPIPS | Combining both datasets best; real data critical | Multi-source training helps | Baseline model much smaller; results may not fully transfer to full model |
| E4 | Number of training views (D.2) | 4/8/16/32+ views per shape | PSNR/LPIPS | 16 views sufficient; saturation beyond 16 | Data efficiency | Video data may have correlated frames |
| E5 | Decoder depth (D.3) | 6/16/24 cross-attn layers | PSNR/CLIP/LPIPS | Modest gains with deeper models | Deeper helps marginally | Small absolute gains (~0.1 PSNR) |
| E6 | NeRF MLP depth (D.3) | 2/6/12/14 MLP layers | PSNR/CLIP/SSIM/LPIPS | 2-4 layers optimal; deeper unnecessary | Triplane encodes information | Consistent with EG3D findings |
| E7 | Triplane resolution (D.3) | 32/64up/128up | PSNR/CLIP/SSIM/LPIPS | Higher resolution improves quality | Higher res beneficial | Uses upsampling; true high-res triplane may give larger gains |
| E8 | Camera pose normalization (D.4) | None/Random/Normalized | PSNR/LPIPS | Normalization crucial (19.0 vs 15.3 PSNR) | Pose normalization critical | Normalization limits real-world generalization |
| E9 | Side views count (D.5) | 1/2/3/4 side views | PSNR/LPIPS | More views improve quality | Multi-view supervision helps | Diminishing returns after 3 views |
| E10 | Rendering resolution (D.5) | 32/64/128 render res | PSNR/LPIPS | Higher resolution significantly improves | High-res training essential | Only tested up to 128px |
| E11 | LPIPS loss contribution (D.6) | With/without LPIPS | CLIP/SSIM/LPIPS | LPIPS loss critical (LPIPS 29.4→19.1) | Perceptual loss essential | Single ablation point |

### Research-Theme Gap Diagnosis

**Core claims with weak evidence support:**

1. **"Generalizes to arbitrary in-the-wild images"** — Supported only by qualitative examples (Fig. 2) and a small quantitative set (100 objects). Missing: large-scale stratified evaluation, OOD detection, and analysis of failure conditions.

2. **"First large-scale 3D reconstruction model"** — Contradicted by the paper's own appendix discussion of Point-E/Shap-E. The actual novel claim (first large-scale direct image-to-NeRF regression) is well supported but not positioned accurately.

3. **"Highly practical solution"** — Inference speed (5s) is indeed practical, but the camera assumption, background-removal requirement, and Lambertian material assumption significantly limit practical applicability scope.

### Proposed Research Experiments (P0/P1/P2)

**Exp-P0.1: Camera Sensitivity Analysis** (Priority: P0, 2-3 days)
- **Target Claim**: "LRM generalizes under assumed camera parameters"
- **Hypothesis**: Reconstruction quality degrades smoothly with FoV/distance mismatch
- **Minimal Design**: Vary FoV (±10%, ±20%, ±30%) and camera distance (±15%, ±30%) around nominal Objaverse parameters on 50 test objects. Report PSNR/LPIPS curves.
- **Controls**: Same test set, same checkpoint, same rendering pipeline
- **Success Criterion**: Report degradation envelope; identify "safe" operating range (e.g., <1dB PSNR drop)
- **Expected Gain**: Quantifies key limitation; provides practical guidance for users

**Exp-P0.2: Expanded Quantitative Evaluation** (Priority: P0, 3-5 days)
- **Target Claim**: "Generalizes across diverse object categories"
- **Hypothesis**: Quality varies by category but remains acceptable for most
- **Minimal Design**: Stratified sampling of 500 Objaverse objects across ≥10 categories + 200 MvImgNet videos. Report per-category PSNR/LPIPS. 3 evaluation seeds.
- **Controls**: Same checkpoint, same evaluation protocol as current paper
- **Success Criterion**: Mean PSNR within 0.5dB of current; identify bottom-3 categories with failure analysis
- **Expected Gain**: Robust statistical support for generalization claim; identifies improvement targets

**Exp-P1.1: Camera Pose Estimation Integration** (Priority: P1, 1-2 weeks)
- **Target Claim**: "Applicable to unconstrained real-world images"
- **Hypothesis**: Adding a camera pose estimation front-end (e.g., COLMAP or a learned pose regressor) removes the fixed-camera bottleneck
- **Minimal Design**: Integrate off-the-shelf camera pose estimator; evaluate on 100 phone-captured images with ground-truth camera parameters
- **Controls**: Compare against fixed-camera baseline on same test set
- **Success Criterion**: PSNR improvement of ≥1dB on phone-captured subset
- **Expected Gain**: Significantly extends practical applicability; addresses most important limitation

**Exp-P1.2: Pre-trained Weights Release + Reproducibility Guide** (Priority: P1, 1 day)
- **Target Claim**: "Reproducible and accessible"
- **Action**: Release checkpoint on GitHub/HuggingFace; provide inference-only Colab notebook
- **Expected Gain**: Enables community to verify, use, and build upon LRM without retraining

**Exp-P2.1: DINO [CLS]-only vs All-Patches Ablation** (Priority: P2, 1 day)
- **Target Claim**: "Patch-level DINO features are beneficial"
- **Design**: Train baseline model with [CLS]-only (1 token) vs all-patches (1025 tokens); compare PSNR/LPIPS
- **Expected Gain**: Empirical validation of design choice

```text
ASCII Diagram — Experiment Upgrade Plan

Stage P0 (before resubmission):
  ┌─────────────────────┐
  │ Camera Sensitivity  │──→ Quantify FoV/distance envelope
  │ Analysis (2-3 days) │──→ Figure + table for paper
  └─────────────────────┘
  ┌─────────────────────┐
  │ Expanded Eval Set   │──→ 500+ Objaverse + 200 MvImgNet
  │ (3-5 days)          │──→ Per-category breakdown table
  └─────────────────────┘

Stage P1 (before submission):
  ┌─────────────────────┐
  │ Camera Pose Est.    │──→ Remove fixed-camera bottleneck
  │ Integration (1-2wk) │──→ Real-world phone capture eval
  └─────────────────────┘
  ┌─────────────────────┐
  │ Release Weights +   │──→ HuggingFace + Colab demo
  │ Reproducibility     │──→ Community adoption enablement
  └─────────────────────┘

Stage P2 (polishing):
  ┌─────────────────────┐
  │ DINO [CLS] ablation │──→ Validate design choice
  │ (1 day)             │──→ Supporting ablation table
  └─────────────────────┘
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Rationale**: The paper demonstrates a technically solid and conceptually clean framework for single-image-to-3D reconstruction with impressive qualitative results. The main contributions—scaling direct NeRF regression to ~1M objects and achieving 5-second inference—are valuable. However, the score is constrained by:

- **Novelty (6/10)**: The "first large-scale" claim is contradicted by cited prior works (Point-E, Shap-E). The actual technical novelty (image-to-triplane transformer decoder with camera modulation) is meaningful but incremental over existing encoder-decoder frameworks (GINA-3D, MCC).
- **Research Value (7/10)**: The demonstration that simple reconstruction losses + scaling works for 3D is valuable for the community. The extensive ablation study is a strength. However, the camera assumption and compute requirements limit the practical impact.
- **Validity/Soundness (6/10)**: The method is sound, but the quantitative evaluation is under-powered (100 test objects, no variance reporting), and the camera assumption mismatch between training and inference is underexplored.
- **Reproducibility (5/10)**: Training requires 128 A100 GPUs for 3 days, which is beyond most academic labs' resources. The paper provides detailed architecture and data specs, supporting partial reproducibility.

**Post-Revision Target: [7.5, 8.0] / 10**

This target assumes all P0 and P1 fixes are implemented:
- Repositioned novelty claim
- Camera sensitivity analysis added
- Expanded quantitative evaluation with variance reporting
- Pre-trained weights released
- Abstract/introduction caveats added