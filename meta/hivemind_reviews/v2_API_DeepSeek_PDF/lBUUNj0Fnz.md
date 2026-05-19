## Summary
# Final Review Report

## Summary

This paper proposes an active learning (AL) framework for semantic image segmentation that reduces human annotation effort by posing only binary (yes/no) queries about the presence or absence of semantic classes in images — rather than requiring pixel-level or region-level annotations. The authors formulate the selection of (image, class) pairs as a constrained optimization problem with an LP relaxation, balancing class-presence uncertainty (via Shannon entropy) and image diversity (via cosine similarity on deep features). Experiments on Flickr-Landscapes, Cityscapes, and PASCAL VOC12 using a DeepLabV3+ backbone show that the proposed method achieves 75-78% mIoU after 25 AL iterations — within 0.4-1.2 points of pixel-level baselines — while reducing estimated annotation time by 28-135x. A user study with 10 images and 3 annotators per dataset confirms that binary queries take only seconds versus minutes-to-hours for pixel-level annotation.

**Core strengths:** The binary-query paradigm is practically motivated and clearly described. The optimization framework combining uncertainty and diversity is sound. The empirical evaluation covers multiple datasets, backbones, and budgets with three-run averaging. The user study provides concrete annotation-time evidence.

**Key weaknesses:** (1) The spatial inference heuristic in the model-update procedure (Appendix F.1) is ad-hoc and unvalidated — the mechanism by which binary feedback translates to segmentation masks is the least rigorous part of the pipeline. (2) The comparison treats annotation protocol and selection algorithm as a single variable, conflating algorithmic merit with annotation efficiency. (3) The G matrix formulation (reciprocal entropy) creates an unbounded confidence score. (4) No statistical significance tests are reported, making "comparable" and "marginal" claims subjective. (5) The "first" claim cannot be verified without literature search (deferred due to Retrieval-Disabled Mode). (6) The conclusion lacks limitations discussion.

**Overall verdict:** The paper addresses a meaningful practical problem with a well-motivated approach. The main contribution — demonstrating that binary class-presence queries can guide effective segmentation model training — is valuable. However, the current manuscript has significant gaps in methodological rigor, particularly in how binary feedback updates the segmentation model spatially. The paper is publishable after major revision addressing the model-update mechanism validation, statistical rigor, and claim bounding.

## Strengths
**S1. Practically motivated problem framing.** The paper identifies a genuine bottleneck in deploying deep segmentation models: the high cost of pixel-level annotation. The proposed binary-query paradigm directly addresses this by reducing annotation to seconds per query rather than hours per image. This practical motivation is clearly articulated in the introduction and supported by a user study.

**S2. Sound optimization formulation.** The constrained optimization in Eq. (4) jointly considers class-presence uncertainty and image diversity, which are both relevant criteria for active learning. The LP relaxation proof (Theorem 1, Appendix A.1) is mathematically sound and allows efficient approximate solution. The two terms in the objective have clear interpretations and the ablation study (Appendix C, Fig. 5) confirms that both contribute to performance.

**S3. Comprehensive empirical evaluation.** The experiments cover three diverse datasets (Flickr-Landscapes, Cityscapes, PASCAL VOC12), two backbone variations (ResNet-101, ResNet-50, XceptionNet), multiple query budgets (200, 300, 400), and ablation studies. Results are averaged over 3 random splits. The comparison against a fully supervised baseline (Appendix H) provides a useful upper-bound reference. The backbone study (Section 4.7) shows robustness to architecture choice.

**S4. User study providing concrete annotation-time evidence.** The user study (Table 1) with actual annotation time measurements across pixel-level, region-level, and binary-level protocols is a valuable contribution. It grounds the paper's central efficiency claim in empirical data rather than speculation, showing binary queries take 2-4 seconds vs. 7.8-37.5 minutes for pixel-level annotation.

**S5. Clear writing and accessible presentation.** The paper is generally well-written with a logical flow. The core idea (binary queries) is intuitive and explained accessibly. Figure 1 effectively illustrates the contrast between conventional and proposed query mechanisms. The optimization framework is presented with sufficient mathematical detail for reproduction.

**S6. Meaningful annotation-effort quantification.** Table 3 and the associated analysis (Section 4.6) provide concrete annotation-time comparisons across all methods (binary: ~4-5.5 hours total vs. region-level: 225-300 hours vs. pixel-level: 156-750 hours). This quantification makes the practical impact tangible and supports the paper's main claim convincingly at the system level.

## Weaknesses
**W1. Ad-hoc spatial inference for binary-to-segmentation mapping (Critical).** The model-update procedure (Appendix F.1) relies on heuristics for converting binary feedback to segmentation mask updates. When a class is confirmed present but was predicted absent (Case 4), the method places it by "searching the boundaries of the dominant class" or "corners of the image." This heuristic has no theoretical grounding and was not quantitatively validated. For datasets with diverse scenes (e.g., Cityscapes where traffic lights, poles, and signs appear at varied locations), this heuristic may systematically misplace objects, degrading localization quality. Without ablation analysis isolating this component, the reader cannot assess how much performance depends on the heuristic vs. the binary feedback signal itself.

**W2. Annotation budget asymmetry conflates algorithm quality with protocol efficiency (Major).** The pixel-level baselines receive only 48 images/iteration (to exhaust the pool over 25 iterations), while binary methods receive 200 or 400 queries/iteration. The resulting comparison mixes two variables: the selection algorithm's effectiveness and the annotation protocol's efficiency. While this reflects real-world trade-offs, the paper presents the comparison as evidence of algorithmic merit ("our method outperforms RR and EE") without disentangling the selection algorithm from the annotation format. The ablation study (Appendix C) partially addresses this by ablating the uncertainty and redundancy terms, but a controlled experiment fixing the information budget would strengthen the algorithmic claims.

**W3. Missing statistical significance analysis (Major).** The paper claims RAL, Entropy, and Coreset "marginally outperform" the proposed method, but no statistical tests are reported. For Cityscapes, the gap is 78.5 vs. 79.4 mIoU with overlapping standard deviations. For PASCAL, the gap is even smaller (75.96 vs. 76.4). Without significance testing, the reader cannot determine whether these differences are meaningful or noise. This is particularly concerning given that only 3 random runs were used per configuration.

**W4. Unbounded confidence formulation in optimization (Major).** The G matrix defined in Eq. (2) uses the reciprocal of entropy: G(j,i) = α/H_ij. As H_ij → 0 (certain predictions), G → ∞, creating an unbounded confidence score. This makes the optimization potentially unstable and means the weight λ in Eq. (4) cannot be meaningfully interpreted without reference to the arbitrary scaling. The term "confidence" is also misleading, since the objective *minimizes* Tr(MG), meaning *low* confidence (high uncertainty) pairs are selected — the mathematics is consistent but the naming is confusing.

**W5. Incomplete rounding procedure specification (Major).** The rounding approach ("B highest entries in M are reconstructed as 1 and the other entries as 0, observing the constraints") is underspecified. If a row accumulates >Cmax top-B entries, the constraint-satisfaction mechanism is not described. Different implementations could produce different solutions, harming reproducibility.

**W6. Novelty claims unverifiable without literature search (Deferred).** The "first active learning framework for semantic image segmentation which poses only binary queries" claim cannot be fully evaluated without external literature search (deferred due to Retrieval-Disabled Mode in this review). Related binary-feedback methods in the AL literature (pairwise similarity, image-class membership queries) are discussed, but whether any prior work specifically combines class-presence binary queries with active selection for segmentation requires manual verification.

**W7. User study limitations (Minor).** The user study uses only 10 images per dataset and 3 annotators, providing limited statistical power for the time estimates. The ease ratings showing all binary queries as 10/10 may reflect the small annotator pool rather than universal preference. The time ratios (28-135x reduction) should be treated as approximate rather than precise.

**W8. Missing limitations discussion in conclusion (Minor).** The conclusion does not discuss any limitations of the proposed approach, reducing scientific credibility. Important limitations include: no spatial information in binary feedback, potential failure for small objects, computational scalability of the LP solver, and the heuristic spatial inference procedure.

## Key Issues
### Ranked Defect Board

| Rank | Issue | Severity | Validity Risk | Research-Value Impact | Fixability | Confidence |
|------|-------|----------|---------------|----------------------|------------|------------|
| 1 | Ad-hoc spatial inference in model update (W1) | Critical | High — the core internal mechanism is unvalidated | High — undermines the pipeline's credibility | Moderate — requires new analysis experiments | High |
| 2 | Budget asymmetry conflating algorithm vs. protocol (W2) | Major | Moderate — affects fairness of algorithmic comparison | Moderate — main claim still holds at system level | Easy — add equal-time comparison experiment | High |
| 3 | Unbounded G matrix formulation (W4) | Major | Moderate — affects numerical stability and interpretation | Low — fixable without changing results | Easy — replace with bounded formulation | High |
| 4 | Missing statistical significance testing (W3) | Major | Moderate — "comparable" and "marginal" claims are subjective | Low — would likely strengthen claims if tested | Easy — add paired t-tests | High |
| 5 | Incomplete rounding specification (W5) | Major | Low — affects reproducibility but not validity | Low — fixable with clearer pseudocode | Easy — add detailed pseudocode | High |

### Issue 1 (Critical): Unvalidated Spatial Inference Mechanism

**Location:** Page 19 — Appendix F.1, Cases (3) and (4)

**Problem:** The procedure for converting binary feedback to segmentation mask updates relies on heuristic spatial placement rules (dominant-class boundary search, corner placement). No validation or ablation of this critical component is provided.

**Why this is critical:** This heuristic is the bridge between the binary query signal and the segmentation output. If it systematically fails, the entire pipeline's performance degrades regardless of the AL selection algorithm's quality. The authors' claim that "over time...the classes adjust themselves appropriately" is anecdotal and unsupported.

**Recommended fix:** 
1. Add a quantitative analysis showing the fraction of Case (4) placements where the heuristic location matches ground truth.
2. Add an ablation comparing the heuristic vs. an oracle-location upper bound.
3. Discuss failure modes explicitly.

### Issue 2 (Major): Conflated Comparison

**Location:** Page 6 — Section 4.3, Page 8 — Tables 2-3

**Problem:** Pixel-level baselines use 48 images/iteration while binary methods use 200-400 queries/iteration. The paper attributes the efficiency gain to the binary query mechanism, but the comparison conflates algorithmic selection quality with annotation protocol efficiency.

**Recommended fix:** Add an experiment that fixes total annotation time (not query count) across all methods, or at minimum add a discussion parsing the contribution of each factor.

### Issue 3 (Major): Unbounded Confidence Score

**Location:** Page 4 — Equations (1)-(2)

**Problem:** G(j,i) = α/H_ij becomes unbounded as H_ij → 0, creating numerical and interpretability issues.

**Recommended fix:** Replace with G(j,i) = 1 - H_ij/log(2) (normalized to [0,1]) or G(j,i) = H_ij directly with maximization instead of minimization.

### Issue 4 (Major): No Statistical Testing

**Location:** Page 7-8 — Section 4.6

**Problem:** Claims of "marginal outperformance" are not statistically tested. Overlapping standard deviations suggest differences may not be significant.

**Recommended fix:** Add paired t-tests or report confidence intervals for the performance gap.

### Issue 5 (Major): Incomplete Rounding Specification

**Location:** Page 5 — Section 3.2

**Problem:** The rounding procedure ("B highest entries...observing the constraints") does not specify how constraint violations are resolved.

**Recommended fix:** Provide exact iterative rounding pseudocode with constraint projection.

## Actionable Suggestions
### Suggestion 1: Validate the spatial inference heuristic (Must)

**Target:** Page 19 — Appendix F.1, Cases (3) and (4)

The most critical gap in the paper is the unvalidated heuristic for converting binary feedback to segmentation mask updates. I recommend the following concrete actions:

1. **Quantify heuristic accuracy:** For each Case (4) occurrence (model predicted absent, oracle says present), record whether the heuristic placement (dominant-class boundary or corner) falls within the ground-truth mask of the newly confirmed class. Report this accuracy across all AL iterations and datasets.

2. **Oracle upper-bound ablation:** Simulate an oracle that places the confirmed class at its ground-truth location. Compare the mIoU trajectory with this oracle against the heuristic version. The gap quantifies the performance loss attributable to the heuristic.

3. **Alternative heuristic comparison:** Compare the current heuristic against alternatives (e.g., random placement within the image, class-conditional position priors learned from the initial training set).

**Expected impact:** Validates (or bounds the cost of) the least rigorous component of the pipeline. If the heuristic introduces substantial losses, the paper can explore learned spatial priors as a replacement.

### Suggestion 2: Add equal-annotation-time comparison (Must)

**Target:** Page 6 — Section 4.3

Add an experiment that fixes the *total annotation time budget* (not query count) across all methods. For example, if pixel-level methods spend 30 hours annotating 48 images (Cityscapes), give the proposed method the same 30 hours of binary queries. If the proposed method still achieves competitive mIoU under equal time, this provides a much cleaner test of the algorithmic contribution.

**Expected impact:** Separates selection algorithm quality from annotation protocol efficiency, strengthening the paper's central claim.

### Suggestion 3: Fix the G matrix formulation (Must)

**Target:** Page 4 — Equations (1)-(2)

Replace the reciprocal formulation G(j,i) = α/H_ij with a bounded alternative:

**Mentor Revised Version:**
"G(j,i) = 1 - H_ij / log(2), where H_ij ∈ [0, log 2] is the binary entropy. G(j,i) ∈ [0, 1], with G=0 for maximally uncertain (H=log 2) and G=1 for maximally certain (H=0). Minimizing Tr(MG) selects pairs with low G (high uncertainty), which is the desired behavior."

Or alternatively: Set G(j,i) = H_ij directly and change the objective to *maximize* Tr(MG), which is mathematically equivalent but avoids the unbounded reciprocal.

### Suggestion 4: Add statistical significance tests (Must)

**Target:** Page 7-8 — Section 4.6

For each dataset and AL iteration, report unpaired t-tests (or Welch's t-test for unequal variance) comparing the proposed method's mIoU against each baseline. Given the 3-run design, use a conservative threshold (p < 0.05). Report the p-values in a supplementary table or annotate Figure 2 with significance markers.

**Expected impact:** Either confirms that the proposed method is statistically indistinguishable from pixel-level baselines (which strengthens the paper) or identifies settings where gaps are genuine.

### Suggestion 5: Provide complete rounding pseudocode (Must)

**Target:** Page 5 — Section 3.2

**Mentor Revised Version:**
"Rounding procedure: (1) Sort all entries of the relaxed M in descending order. (2) Initialize M_int = 0^{N×C} and row_counts = 0^N, total = 0. (3) For each entry (i,j) in sorted order: if row_counts[i] < Cmax and total < B, set M_int[i,j] = 1, row_counts[i] += 1, total += 1. (4) Stop when total = B. This guarantees both the budget and per-image constraints."

### Suggestion 6: Add limitations discussion (Nice-to-have)

**Target:** Page 9 — Conclusion

Add a 3-4 sentence limitations paragraph before the future work section, covering: (a) lack of spatial information in binary feedback, (b) small-scale user study, (c) computational cost of LP solver.

### Suggestion 7: Add statistical power to user study (Nice-to-have)

**Target:** Page 7 — Section 4.5

Expand the user study to at least 30 images per dataset with 5+ annotators, or explicitly report confidence intervals for the time ratios and acknowledge the small sample limitation.

### Suggestion 8: Restructure Related Work around comparison axes (Nice-to-have)

**Target:** Page 2-3 — Section 2

Reorganize related work around two axes: annotation type (pixel/region/binary) and selection mechanism (uncertainty/diversity/coreset). This makes the novelty positioning clearer. See the annotation on Page 2 for a detailed rewrite.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows a standard three-paragraph structure:
- **P1:** Semantic segmentation is important; deep models are accurate but need lots of labeled data.
- **P2:** Active learning reduces annotation effort; it has been successful in many domains.
- **P3:** Segmentation is especially costly; we propose binary queries; contributions list.

**Diagnosis:** The current storyline is functional but generic. P2 reads as a general AL tutorial rather than building the specific case for binary queries in segmentation. The gap is not sharpened until the end of P3. The connection between "AL reduces annotation cost" and "binary queries are even cheaper" is intuitive but could be more tightly argued.

### Alternative Storyline Candidate (Recommended)

**P1 — Problem + Cost Hook:** Start with a concrete statistic: "A single Cityscapes image requires ~37.5 minutes for pixel-level annotation, making large-scale segmentation data collection prohibitively expensive." Then define the task and state the problem. This immediately establishes stakes.

**P2 — Prior Work Gap:** State that active learning reduces the *number* of samples to annotate, but existing AL methods for segmentation still require pixel-level or region-level annotation for each selected sample, so the per-sample cost remains high. This sharpens the gap: prior AL reduces *how many* samples, but not *how much* work per sample.

**P3 — Proposed Solution + Intuition:** Introduce the binary query paradigm as addressing the per-sample cost dimension. Explain the intuition: annotators answer yes/no questions about class presence, taking only seconds per query. Show Figure 1 and explain how the optimization framework selects informative (image, class) pairs.

**P4 — Contributions + Paper Roadmap:** List 3 contributions (not 4): (1) binary-query AL framework for segmentation, (2) LP-based optimization formulation, (3) empirical validation including user study.

### Abstract Outline

**S1 — Problem:** "Training deep segmentation models requires dense pixel-level annotations that are time-consuming and expensive to obtain."

**S2 — Prior Gap:** "Active learning reduces the number of samples requiring annotation, but existing methods still require pixel-level or region-level labeling of each selected sample."

**S3 — Proposed Method:** "We propose an active learning framework that poses only binary (yes/no) queries about the presence of semantic classes in images, reducing annotation effort to seconds per query. A linear programming relaxation jointly selects informative images and classes based on prediction uncertainty and image diversity."

**S4 — Key Result (bounded):** "On three benchmark datasets (Cityscapes, PASCAL VOC12, Flickr-Landscapes), our method achieves 75-78% mIoU — within 0.4-1.9 points of fully supervised training — while reducing annotation time by 28-135x compared to pixel-level alternatives."

**S5 — Implication (scoped):** "These results suggest that binary class-presence feedback can serve as a practical and efficient supervision signal for training segmentation models, though further validation of the spatial inference mechanism is needed."

### Introduction Outline (Revised)

**P1 — Problem and Cost Hook:**
- Role: Establish stakes with concrete numbers.
- Claim: Segmentation annotation is extremely expensive (cite user study times).
- Transition: "This cost has motivated active learning approaches."

**P2 — Gap Sharpening:**
- Role: Explain why existing AL methods are insufficient.
- Claim: AL reduces sample count but not per-sample cost (pixel/region labeling remains).
- Contrast: "What if we could reduce per-sample annotation to a simple yes/no question?"
- Transition: "We propose such a paradigm."

**P3 — Solution Intuition:**
- Role: Introduce binary queries and optimization framework intuitively.
- Claim: Binary queries dramatically reduce per-query effort (2-4 seconds).
- Mechanism overview: uncertainty + diversity → LP → (image, class) pairs.
- Transition: "Our contributions are three-fold."

**P4 — Contributions + Roadmap:**
- List 3 contributions (binary-query AL, LP formulation, empirical validation).
- Preview evaluation: datasets, baselines, metrics.
- Transition to method section.

### Title Suggestion

**Current:** "Active Learning for Image Segmentation with Binary User Feedback"

**Suggestion:** "Binary Query Active Learning for Semantic Segmentation: Reducing Annotation to Yes/No Questions"

Rationale: The revised title puts the core idea (binary queries) first, explicitly names the task (semantic segmentation), and adds a clarifying subtitle that explains what binary feedback means.

## Priority Revision Plan
### P0 — Must Fix (Publication-Critical)

| Priority | Defect | Action | Effort | Impact | Annotation Ref |
|----------|--------|--------|--------|--------|----------------|
| P0.1 | Unvalidated spatial inference heuristic (W1) | Add heuristic accuracy analysis + oracle upper-bound ablation | Moderate (2-3 weeks for experiments + analysis) | High — validates the core pipeline mechanism | Page 19 — App. F.1 |
| P0.2 | Missing rounding specification (W5) | Provide exact iterative rounding pseudocode | Low (1 hour) | High — enables reproducibility | Page 5 — Sec. 3.2 |
| P0.3 | Unbounded G matrix (W4) | Replace reciprocal entropy with normalized bounded formulation | Low (code fix + re-running experiments) | Moderate — improves numerical stability | Page 4 — Eq. (1)-(2) |

### P1 — Should Fix (Strongly Recommended)

| Priority | Defect | Action | Effort | Impact | Annotation Ref |
|----------|--------|--------|--------|--------|----------------|
| P1.1 | Budget asymmetry (W2) | Add equal-annotation-time comparison experiment | Moderate (requires user study time extrapolation) | High — cleans up comparison fairness | Page 6 — Sec. 4.3 |
| P1.2 | Missing significance tests (W3) | Add paired t-tests or confidence intervals for all main results | Low (1-2 hours) | Moderate — supports "comparable" claim | Page 7-8 — Sec. 4.6 |
| P1.3 | Missing limitations in conclusion | Add limitations paragraph | Low (1 hour) | Low — improves scientific completeness | Page 9 — Conclusion |

### P2 — Nice to Have (Quality Improvement)

| Priority | Defect | Action | Effort | Impact |
|----------|--------|--------|--------|--------|
| P2.1 | User study small sample | Expand to 30+ images and 5+ annotators per dataset | High (requires recruiting annotators) | Low-Moderate |
| P2.2 | Related Work restructuring | Reorganize around comparison axes | Moderate (rewriting) | Moderate — improves clarity |
| P2.3 | Introduction rewrite | Tighten per revised outline | Low-Moderate | Moderate — improves narrative |

### Revision Order (Recommended)

```text
ASCII Diagram — Revision Strategy Roadmap

Stage 1 (Week 1): Low-effort, high-impact fixes
  [Rounding pseudocode] → [Bounded G matrix] → [Statistical tests]
  → [Limitations paragraph]
  Expected gain: Reproducibility + rigor + scientific completeness

Stage 2 (Week 2-3): Moderate-effort, critical-fix
  [Validate spatial heuristic]
  └── [Heuristic accuracy analysis]
  └── [Oracle upper-bound ablation]
  └── [Failure mode documentation]
  Expected gain: Validates core pipeline mechanism

Stage 3 (Week 3-4): Comparison fairness
  [Equal-annotation-time experiment]
  → [Revised claims based on new evidence]
  Expected gain: Separates algorithmic merit from protocol efficiency

Stage 4 (Before resubmission): Polish
  [Related Work restructuring]
  [Introduction rewrite per outline]
  [Title revision]
  Expected gain: Readability + novelty positioning
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Main AL comparison (Fig 2) | 3 datasets, DeepLabV3+ ResNet101, 25 AL iterations, B=200/400 | mIoU | Proposed outperforms RR/EE; comparable to RAL/Entropy/Coreset | C1, C4 | Budget asymmetry; no significance tests |
| E2 | User study (Table 1) | 10 images/dataset, 3 annotators, LabelMe tool | Time (min/sec), Ease (1-10) | Binary: 2-4 sec, 10/10 ease; Pixel: 7.8-37.5 min | C3 | Small sample (10 images, 3 annotators) |
| E3 | Backbone study (Fig 3, Table 4) | Cityscapes, XceptionNet and ResNet50 backbones | mIoU | Proposed best for Xception; competitive for ResNet50 | C1, C4 | Only Cityscapes tested |
| E4 | Query budget study (Appendix B, Fig 4) | Flickr, B=200/300/400 | mIoU | Proposed outperforms RR/EE across all budgets | C1 | Gap increases at lower budgets |
| E5 | Ablation study (Appendix C, Fig 5) | Flickr, B=400, w/o redundancy, w/o uncertainty | mIoU | Both terms contribute to performance | C1, C2 | Only one dataset tested |
| E6 | Computation time analysis (Appendix D, Table 7) | All datasets, all methods | Minutes/iteration | Proposed ~25-28 min; faster than RAL, slower than EE/Entropy | — | LP solver overhead acknowledged |
| E7 | Cmax parameter study (Appendix E, Fig 6) | Flickr, B=200, Cmax=4/5/7/9 | mIoU | Cmax≤4 harms performance; robust otherwise | C1, C2 | Only one dataset |
| E8 | Initial training set size (Appendix G, Fig 11) | Cityscapes, 300 and 500 initial images | mIoU | Similar trends as main experiment | C1 | Lower absolute mIoU expected |
| E9 | Fully supervised comparison (Appendix H, Fig 12, Table 9) | All datasets, all methods vs. fully supervised | mIoU, effort reduction | Proposed within 0.74-1.87 mIoU of fully supervised; 28-135x reduction | C1, C3 | Small gap could be due to any method component |

### Research-Theme Gap Diagnosis

**Value claim 1 — New knowledge:** The paper's primary new knowledge claim is that binary (yes/no) class-presence queries can effectively train a segmentation model. This is partially supported: the experiments show competitive mIoU, but the mechanism by which binary signals translate to accurate spatial masks is not validated (the ad-hoc spatial heuristic). Without this validation, the *how* of the knowledge claim remains a black box.

**Value claim 2 — Reproducibility/reusability:** The paper provides adequate detail for reproducing the AL selection algorithm (equations, LP formulation, rounding). However, the model-update procedure (Appendix F.1) relies on underspecified heuristics that are difficult to reproduce exactly. The annotation-time numbers from the user study are useful for practitioners planning annotation budgets.

**Value claim 3 — Potential to change practice:** The core idea — binary queries for segmentation — has high potential for practical impact if validated. A practitioner could use this framework to obtain a usable segmentation model with only yes/no questions, which is dramatically cheaper than pixel annotation. However, the unvalidated spatial inference mechanism is a barrier to adoption.

### Proposed Research Experiments

| ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost/Time | Expected Quality Gain |
|----|-------------|-----------|---------------|-------------------|---------|-------------------|--------------------|---------------------|
| P0-E1 | W1: Spatial heuristic validation | The heuristic placement accuracy varies by class and dataset | For all Case (4) occurrences across one dataset, compute IoU between heuristic placement and ground-truth class mask | Oracle placement upper bound, random placement baseline | Heuristic accuracy (%), mIoU trajectory delta | Heuristic placement accuracy > 50% AND delta from oracle < 2 mIoU points | 1-2 weeks | Validates (or bounds) the core pipeline mechanism |
| P0-E2 | W2: Equal-time comparison | The proposed method maintains its advantage under equal annotation time budget | Fix annotation time budget to match pixel-level methods' cost; run AL with the proposed method under this budget | Pixel-level Entropy/Coreset under original setup | mIoU after 25 iterations | Proposed method mIoU remains within 1 point of pixel-level methods | 1-2 weeks | Separates algorithmic merit from protocol efficiency |
| P1-E1 | Statistical reliability | Performance gaps vs. baselines are not statistically significant | Compute paired t-tests for each dataset × AL iteration | All baselines | p-values, confidence intervals | Report p-values transparently regardless of significance | 1-2 hours | Supports or refutes "comparable" claims |
| P2-E1 | Robustness to annotation noise | The method remains effective when annotators make occasional mistakes | Introduce controlled label noise in binary feedback (5%, 10%, 20% flip rate) | Clean feedback version | mIoU degradation curve | Graceful degradation (≤3% mIoU drop at 10% noise) | 1 week | Addresses real-world deployment concerns |
| P2-E2 | Beyond semantic segmentation | The binary query paradigm extends to instance segmentation or panoptic segmentation | Adapt framework to COCO or a subset; compare to random binary queries | Random binary query baseline | Panoptic quality (PQ) or mask AP | Proposed outperforms random baseline | 3-4 weeks | Broader impact demonstration |

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Week 1-2): Core Validation
  [P0-E1: Spatial heuristic analysis] → [P0-E2: Equal-time comparison]
  ↓
  Decision gate: Does heuristic accuracy > 50% AND delta from oracle < 2 mIoU?
  ├── Yes → Proceed to P1-E1
  └── No → Develop learned spatial prior (alternative heuristic)

P1 (Week 1): Statistical Foundation
  [P1-E1: Significance tests for all main results]
  → Confidence intervals reported in Table 2

P2 (Week 3-4): Robustness & Generalization
  [P2-E1: Label noise robustness] → [P2-E2: Instance segmentation extension]
  ↓
  Final submission package
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.0 / 10**

**Rationale:** The paper addresses a practically important problem with a well-motivated and intuitively clear approach. The binary-query paradigm for segmentation has genuine potential for real-world impact. The empirical evaluation is reasonably comprehensive (3 datasets, multiple backbones, ablation studies, user study). However, the score is capped at 6.0 due to several critical and major weaknesses:

- **Research Value (6/10):** The core idea is valuable and practically relevant. The paper demonstrates that binary queries can yield competitive mIoU with dramatically less annotation effort — a non-obvious finding. However, the unvalidated spatial inference mechanism means the true research contribution (understanding *how* binary feedback enables segmentation) is incomplete.

- **Novelty (5/10):** The combination of binary queries with active learning for segmentation appears novel at the system level, but the "first" claim cannot be verified without literature search (deferred). The individual components (entropy-based uncertainty, cosine similarity diversity, LP relaxation) are standard. The model-update heuristic is the most novel component but is also the least validated.

- **Validity/Soundness (5/10):** The mathematical formulation is internally consistent, but three issues reduce confidence: (1) the unbounded G matrix raises numerical concerns, (2) the ad-hoc spatial heuristic is unvalidated, (3) missing statistical significance tests make "comparable" claims subjective.

- **Reproducibility (5/10):** The AL selection algorithm is adequately specified. The rounding procedure and model-update heuristic are underspecified, reducing exact reproducibility.

- **Clarity (7/10):** The paper is generally well-written and the core idea is communicated effectively. The introduction could be tightened and the related work could be more structured.

**Post-Revision Target: [7.0, 7.5] / 10**

If the following key issues are addressed in revision:
1. Validation of the spatial inference heuristic (P0-E1)
2. Equal-annotation-time comparison experiment (P0-E2)
3. Statistical significance testing (P1-E1)
4. Fixes to G matrix formulation and rounding specification
5. Addition of limitations section

...the paper would likely achieve a score in the 7.0-7.5 range, reflecting a solid contribution with clear practical value and adequate methodological rigor. Full resolution of all issues including broader generalization experiments (P2-E1, P2-E2) could push the score toward 8.0, but the current evidence base does not support a higher target.