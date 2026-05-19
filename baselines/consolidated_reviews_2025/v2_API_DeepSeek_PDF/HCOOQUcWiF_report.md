## Summary
# Final Review Report

## Summary

This paper presents a differentiable polygon-based approach to object instance segmentation, addressing two core challenges: (i) vertex alignment between fixed-K predicted polygons and variable-L ground-truth polygons, solved via PolygonAlign — a contour-length-fraction (CLF) sampling strategy that creates consistent vertex correspondence; and (ii) polygon parameterization via an affine-transformation-decoupled vertex regression method under the active contour framework, with a learnable initializer and one-step refinement. The method is evaluated on MS-COCO using the Sparse R-CNN pipeline, achieving 35.2 AP with ResNet-101 (24 epochs), outperforming prior contour-based methods including PolarMask++, E2EC, and PolySnake. An empirical upper-bound analysis demonstrates fitting capacity above 80% AP, suggesting room for further improvement.

**Overall assessment**: The paper addresses a genuine gap — bridging the simplicity of mask-based training with the output advantages of polygon representations. The core ideas (PolygonAlign via CLF sampling, affine-decoupled vertex regression) are technically sound and well-motivated. However, several issues weaken the submission: overclaimed comparisons between fitting capacity and practical performance, ambiguous formulation of the rotation matrix, a citation error (PointRend), insufficient ablation rigor (single-run variance), and a narrow limitations section. With targeted revisions and additional experiments, the paper could become a solid contribution.

## Strengths
1. **Well-motivated problem**: The paper correctly identifies that polygon-based instance segmentation lacks the simple differentiable loss functions available to mask-based methods. The goal of enabling a simple $\ell_2$ vertex loss via alignment is clearly articulated and practically relevant.

2. **Clean technical solution for alignment**: PolygonAlign via CLF-based vertex re-sampling is an intuitive and effective approach to establishing vertex correspondence between predicted and ground-truth polygons. The analogy to RoIAlign is appropriate and helps readers understand the design philosophy.

3. **Practical simplicity**: The affine-transformation-decoupled parameterization with a learnable initializer and one-step refiner is notably simpler than prior active contour variants that require iterative refinement, dynamic matching (Douglas-Peucker), or multi-stage training with multiple loss terms.

4. **Competitive empirical results**: The method achieves 35.2 AP on MS-COCO test-dev with ResNet-101 (24 epochs), outperforming existing contour-based methods. The efficiency advantage (24 vs 140/250 epochs for competitors) is an appealing practical benefit.

5. **Upper-bound analysis**: The direct polygon fitting experiments (Experiments I and II) provide useful insight into the parameterization's capacity, showing that the core regression formulation can achieve >80% AP in idealized settings — which helps isolate representation limitations from learning/feature extraction challenges.

6. **Detailed architectural specification**: The Settings subsection provides sufficient network architecture details (layer dimensions, activation functions) to enable reproduction, which is commendable.

## Weaknesses
1. **Misleading upper-bound comparison (Abstract, Conclusion)**: The claim that "empirical upper-bound performance is much higher than all existing instance segmentation methods" conflates per-instance fitting capacity (no generalization gap) with end-to-end learned performance. This comparison is not apples-to-apples and overstates the paper's practical advantage.

2. **Rotation matrix ambiguity (Method §2.2.1)**: The paper learns a $2\times2$ "rotation" matrix via unconstrained regression without enforcing orthogonality. A general $2\times2$ matrix can represent scaling, shear, and reflection — not just rotation. The claimed "decoupled" property is compromised.

3. **Incongruous ablation results (§3.3)**: The non-monotonic K experiment (K=50 > K=120) is attributed to possible "training noise" with single-run experiments, which undermines confidence in the ablation conclusions. Multi-seed variance reporting is needed.

4. **Citation error (Page 6)**: PointRend is cited as (Sitzmann et al., 2020), but the correct reference is Kirillov et al. (2020). The Sitzmann paper is about SIREN/INRs, not mask refinement.

5. **Backbone mismatch in comparisons (Table 1)**: The method uses ResNet-50/101, while E2EC and PolySnake use DLA-34. The 1.4% improvement over E2EC may partially reflect backbone strength, not methodological advantage. No controlled backbone experiment is reported.

6. **Missing variance/statistical significance**: All results are single-run. Given that performance differences between methods are often 1-2 AP, the absence of confidence intervals prevents judging whether improvements are statistically reliable.

7. **Narrow limitations section (§3.4)**: Only one limitation (upper-bound gap) is discussed. Missing: fixed-topology inefficiency for simple objects, single-dataset evaluation, computational cost of 250 vertices, and Sparse R-CNN dependency.

8. **Contribution (iii) is not a methodological contribution (Page 3)**: Listing "state-of-the-art performance" as a separate contribution inflates the contribution count. Performance is an outcome of contributions (i) and (ii), not a standalone contribution.

9. **Unclear CLF sampling anchor (Page 2)**: The "intersection point between the polygon and the x-axis" is ambiguous for polygons that do not intersect the image x-axis. The coordinate frame for sampling is not clearly defined.

10. **Grammar and writing issues**: Multiple grammatical errors ("progress have been made", "It also simplify", "there are a lot room", "investigated using to direct") reduce readability and professional polish.

## Key Issues
### Issue 1 (Critical): Misleading upper-bound comparison in Abstract and Conclusion
**Location**: Page 1 - Abstract, Page 10 - Conclusion  
**Evidence**: Abstract states "empirical upper-bound performance of the proposed method is much higher than all existing instance segmentation methods." The upper-bound (Exp I, ~83% AP) is obtained by directly optimizing FC as per-instance parameters on the training set, with no generalization gap.  
**Impact**: This conflates fitting capacity with practical performance, creating an unsupported comparative claim. Reviewers will flag this as an overstatement.  
**Fix**: Remove this sentence or rephrase to explicitly distinguish fitting capacity from end-to-end performance.

### Issue 2 (Major): Rotation matrix not constrained to be orthogonal
**Location**: Page 5 - §2.2.1, Eq. (3)  
**Evidence**: A $2\times2$ matrix predicted via unconstrained MLP regression (output dim 6) is called a "rotation" matrix. No orthogonality constraint is enforced.  
**Impact**: The matrix can represent scaling/shear/reflection, making the "decoupled" property ambiguous and the optimization less interpretable.  
**Fix**: Either construct R from a single predicted angle $\theta$, or rename to "affine transformation matrix" and discuss the implications.

### Issue 3 (Major): Citation error — PointRend attributed to wrong paper
**Location**: Page 6 - §2.2.2  
**Evidence**: "coarse mask guided point-based refinement has also found useful such as the PointRend method (Sitzmann et al., 2020)". PointRend is by Kirillov et al. (CVPR 2020); Sitzmann et al. 2020 is about implicit neural representations (SIREN).  
**Impact**: Scholarly error that reduces credibility.  
**Fix**: Correct the citation to Kirillov et al. (2020).

### Issue 4 (Major): Ablation results not statistically reliable
**Location**: Page 9 - §3.3, Table 3  
**Evidence**: The paper acknowledges the K=50 > K=120 anomaly "could be simply caused by the common performance variations due to different training noises since we compare them using just one round of experiments."  
**Impact**: The main conclusion (K=250 is best) is unsupported by statistical evidence.  
**Fix**: Run at least 3 seeds per configuration; report mean ± std.

### Issue 5 (Major): Backbone mismatch in main comparison (Table 1)
**Location**: Page 8 - Table 1  
**Evidence**: Proposed method uses ResNet-50/101; E2EC and PolySnake use DLA-34. The claimed 1.4% improvement over E2EC does not control for backbone strength.  
**Impact**: The "state-of-the-art" claim may not hold under matched-backbone comparison.  
**Fix**: Add an experiment with DLA-34 backbone, or explicitly acknowledge the limitation.

## Actionable Suggestions
### Suggestion 1 (Must): Revise abstract and conclusion upper-bound claims
**Location**: Page 1 (Abstract), Page 10 (Conclusion)  
**Action**: Replace the misleading comparison with a bounded statement.  
**Revised abstract sentence**: "We also analyze the empirical upper-bound fitting capacity of the proposed parameterization through direct polygon optimization, which reaches over 80% AP, highlighting headroom for improvement between fitting capacity and end-to-end performance."

### Suggestion 2 (Must): Fix the rotation matrix formulation
**Location**: Page 5, Eq. (3)  
**Action**: Enforce orthogonality by predicting a single angle $\theta$ and constructing $R = [[\cos\theta, -\sin\theta], [\sin\theta, \cos\theta]]$, or rename to "affine transformation matrix" and note the additional degrees of freedom.  
**Revised text**: "We predict a rotation angle $\theta = f_\theta(F_C; \theta_\theta)$ and construct the rotation matrix as $R_{2\times2} = [\cos\theta, -\sin\theta; \sin\theta, \cos\theta]$."

### Suggestion 3 (Must): Correct the PointRend citation
**Location**: Page 6, §2.2.2  
**Action**: Replace "(Sitzmann et al., 2020)" with "(Kirillov et al., 2020)" for the PointRend reference.  
**Revised text**: "...such as the PointRend method (Kirillov et al., 2020)."

### Suggestion 4 (Must): Add multi-seed variance to ablation studies
**Location**: Page 9, Table 3  
**Action**: Run K=50, 120, 250 experiments with at least 3 random seeds each. Report as mean ± std. If differences remain within noise, state that K=250 is chosen based on expressivity rather than empirical superiority.

### Suggestion 5 (Must): Add DLA-34 backbone experiment
**Location**: Page 8, Table 1  
**Action**: Conduct one additional experiment using DLA-34 backbone to enable direct comparison with E2EC and PolySnake under matched conditions.

### Suggestion 6 (Nice-to-have): Clarify CLF sampling anchor
**Location**: Page 2, §1  
**Action**: Define the starting vertex in a canonical RoI-aligned coordinate frame rather than the image x-axis.  
**Revised text**: "The starting vertex is defined as the point on the contour with the smallest angle relative to the positive x-axis in the RoI-normalized coordinate frame."

### Suggestion 7 (Nice-to-have): Expand limitations section
**Location**: Page 9, §3.4  
**Action**: Add limitations on fixed-topology inefficiency, single-dataset evaluation, computational cost, and detection pipeline dependency.  
**Revised text**: (see annotation on Page 9 for the full paragraph)

### Suggestion 8 (Nice-to-have): Fix Eq. (1) loss notation
**Location**: Page 4, Eq. (1)  
**Action**: Replace matrix 2-norm with squared Frobenius norm and clarify coordinate normalization.  
**Revised**: $\ell(V, V^*) = \frac{1}{K} \|V - V^*\|_F^2$

### Suggestion 9 (Nice-to-have): Restructure contributions
**Location**: Page 3, "Our Contributions"  
**Action**: Reduce to two methodological contributions (C1: PolygonAlign, C2: affine-decoupled parameterization + refiner). Move performance summary to a separate sentence.

### Suggestion 10 (Nice-to-have): Fix grammar errors
**Locations**: Pages 1, 3, 6, 9  
**Actions**: 
- "progress have been made" → "progress has been made" (Page 1)
- "It also simplify" → "It also simplifies" (Page 3)
- "has been found useful" → "has been found useful" (Page 6, grammar structure)
- "there are a lot room" → "there is a lot of room" (Page 9)
- "investigated using to direct" → "investigated through direct" (Page 10)

## Storyline Options + Writing Outlines
### Abstract Outline (complete)

The abstract should use this 5-sentence structure:

**S1 (Problem)**: "Differentiable polygon (contour-based) modeling for instance segmentation remains underexplored compared to dominant bit-mask methods, primarily due to the difficulty of defining a simple and differentiable loss between predicted and ground-truth polygons."

**S2 (Gap)**: "Two key challenges exist: (i) aligning a fixed-K-vertex predicted polygon with a variable-L-vertex ground-truth polygon, and (ii) parameterizing polygons to enable stable end-to-end regression."

**S3 (Method)**: "We address these with PolygonAlign — a contour-length-fraction (CLF) sampling strategy that creates consistent vertex correspondence enabling a simple MSE loss — and an affine-transformation-decoupled vertex regression method that serves as a learnable contour initializer with one-step refinement."

**S4 (Key Result)**: "On MS-COCO, our method achieves 35.2 AP with ResNet-101 (24 epochs), outperforming prior contour-based approaches while requiring fewer training iterations."

**S5 (Outlook)**: "An empirical upper-bound analysis reveals fitting capacity exceeding 80% AP, indicating substantial headroom for future improvements in end-to-end learning."

### Introduction Outline (complete)

The introduction should follow a 5-paragraph structure:

**Paragraph 1 — Motivation and practical stakes**  
*Role*: Establish why instance segmentation matters and where polygon representations are needed.  
*Key claim*: Polygon representations are essential for applications requiring exact boundaries (annotation, CAD, shape editing), yet deep learning has focused almost exclusively on masks.  
*Transition*: → "This disconnect motivates our core question."

**Paragraph 2 — Bit-mask vs polygon dichotomy**  
*Role*: Explain the representational divide — humans annotate with polygons, machines learn with masks.  
*Key claim*: Bit-mask methods succeed because of simple differentiable losses on fixed-resolution grids; polygon methods lack this convenience.  
*Transition*: → "The technical difficulty lies in two specific problems."

**Paragraph 3 — The two technical challenges**  
*Role*: Clearly state the two challenges (alignment + parameterization) with concrete examples.  
*Key claim*: (i) Vertex count mismatch between predicted (K) and ground-truth (L) polygons. (ii) No canonical vertex ordering, making direct regression ill-posed.  
*Transition*: → "This paper solves both with two technical innovations."

**Paragraph 4 — Proposed solution overview**  
*Role*: Brief method description with reference to Figures 1-3.  
*Key claim*: PolygonAlign via CLF sampling + affine-decoupled vertex regression + one-step refinement.  
*Transition*: → "In experiments..."

**Paragraph 5 — Contributions and results preview**  
*Role*: Summarize two methodological contributions + key results + upper-bound analysis.  
*Key claim*: SOTA among contour-based methods on COCO; fitting capacity >80% AP.  
*Transition*: → Method section.

## Priority Revision Plan
### P0 — Publication-Critical (Must fix before acceptance)

| Priority | Issue | Effort | Expected Impact |
|----------|-------|--------|-----------------|
| P0.1 | Revise abstract/conclusion upper-bound claims | Low (text edit) | High — removes misleading comparison |
| P0.2 | Fix rotation matrix orthogonality | Medium (code + text) | High — corrects technical formulation |
| P0.3 | Correct PointRend citation | Low (text edit) | Medium — fixes scholarly accuracy |
| P0.4 | Add multi-seed variance to ablation | Medium (experiments) | High — provides statistical reliability |
| P0.5 | Add DLA-34 backbone experiment | Medium (experiment) | High — enables fair comparison |

### P1 — High Priority (Should fix)

| Priority | Issue | Effort | Expected Impact |
|----------|-------|--------|-----------------|
| P1.1 | Clarify CLF sampling coordinate frame | Low (text + figure) | Medium — resolves ambiguity |
| P1.2 | Expand limitations section | Low (text) | Medium — improves completeness |
| P1.3 | Fix Eq. (1) loss notation | Low (text) | Medium — corrects math notation |
| P1.4 | Restructure contributions to two claims | Low (text) | Medium — improves framing |

### P2 — Quality Improvements (Nice to have)

| Priority | Issue | Effort | Expected Impact |
|----------|-------|--------|-----------------|
| P2.1 | Grammar fixes | Low (text) | Low — polish |

**Expected post-revision score range**: [5.5, 7.0]/10

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|--------------|-----------------|-------------------|
| Exp I (§3.1) | Fitting capacity of parameterization | 5000 train polygons, direct FC optimization, full batch, 300 iter | AP (same-set) | AP 81.9-83.2% (K=50-250) | Parameterization is expressive | No generalization; K=50 > K=250 unexplained |
| Exp II (§3.1) | Alternative latent space via encoder | 5000 train + 5000 val polygons, encoder from bit-mask, 300 epochs | AP (held-out) | AP 81.9-83.8% (K=50-250) | Learnable latent polygon space exists | Bit-mask input limits real-world applicability |
| Main (§3.2) | COCO instance segmentation | MS-COCO train/test-dev, Sparse R-CNN, Res-50/101, 12/24 epochs | AP, AP50, AP75 | Best: 35.2 AP (Res-101, 24ep) | Contour-based SOTA | Backbone mismatch with baselines |
| Ablation 1 (§3.3) | Effect of affine transformation | Res-50, 12ep, K=250, w/wo affine | APDet, AP, AP50, AP75 | +0.3 AP with affine | Affine helps marginally | Small gain; single-run |
| Ablation 2 (§3.3) | Number of vertices K | Res-50, 12ep, K=50/120/250 | AP, Resampling Quality | K=250 best (31.8 AP); K=50 > K=120 anomaly | More vertices beneficial overall | Non-monotonic; single-run variance |

### Research-Theme Gap Diagnosis

1. **Generalization gap**: The paper does not evaluate on any dataset beyond COCO. It is unknown whether the method generalizes to other domains (e.g., Cityscapes, LVIS, medical images).

2. **Backbone fairness**: No controlled experiment with DLA-34 backbone to match E2EC/PolySnake. The SOTA claim is weakened by this omission.

3. **Statistical reliability**: No multi-seed experiments. All comparisons lack confidence intervals.

4. **Ablation depth**: Only two ablations (affine transformation, K). Missing: effect of refiner module, effect of CLF vs alternative sampling, effect of circular convolution vs MLP refinement.

5. **Computational cost**: No runtime, memory, or FLOPs comparison with mask-based methods.

### Proposed Research Experiments (P0/P1/P2)

| Experiment | Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Est. Cost | Quality Gain |
|------------|-------------|------------|----------------|----------|---------|-------------------|-----------|--------------|
| **P0: Multi-seed K ablation** | Statistical reliability of K=250 | Differences are within noise | Run K=50/120/250 with 3 seeds each | Same Res-50, 12ep | Mean AP ± std | std < 0.3 AP; K=250 > others in mean | ~3 GPU-days | High — fixes unsupported ablation |
| **P0: DLA-34 backbone** | Fair comparison with E2EC/PolySnake | Our method still outperforms | Implement with DLA-34, 24ep | E2EC (DLA-34, 140ep) | AP, AP50, AP75 | Our AP > 34.5 (PolySnake) | ~2 GPU-days | High — validates SOTA fairly |
| **P1: Refiner ablation** | Refiner contributes positively | Removing refiner reduces AP | Compare w/ and w/o refiner in Sparse R-CNN | Res-50, 12ep, K=250 | AP drop | AP drop > 0.5 | ~1 GPU-day | Medium — validates design choice |
| **P1: CLF vs uniform vertex sampling** | CLF is better than alternatives | CLF preserves shape better | Compare CLF vs uniform arc-length vs random sampling | Res-50, 12ep, K=250 | AP + resampling quality | CLF achieves highest AP | ~2 GPU-days | Medium — justifies method choice |
| **P2: Cityscapes evaluation** | Generalization beyond COCO | Method transfers to street scenes | Fine-tune on Cityscapes train, eval val | Res-101, 24ep | AP (instance seg) | AP > published contour methods on Cityscapes | ~2 GPU-days | Medium — broadens contribution scope |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 5.5 / 10

*Rationale*: The paper addresses a relevant problem with a clean technical approach (PolygonAlign + affine-decoupled parameterization). The empirical results are competitive within the contour-based family. However, the paper is weakened by several issues that directly affect research value and novelty claims: (1) a misleading upper-bound comparison in the abstract that conflates fitting capacity with performance; (2) a technically ambiguous rotation matrix formulation; (3) missing statistical rigor in ablations; (4) a citation error; and (5) a comparatively narrow evaluation (single dataset, unmatched backbones). The core ideas have merit, but the current framing and evidence do not yet support the strongest claims.

**Post-Revision Target**: [6.5, 7.5] / 10

*Rationale*: If the authors address the P0 items (correct upper-bound claims, fix rotation matrix, add multi-seed variance, add DLA-34 comparison, correct citation), the paper would become a solid contribution with well-supported claims. The ceiling is constrained by the single-dataset evaluation and incremental nature of the contribution over existing contour-based methods.