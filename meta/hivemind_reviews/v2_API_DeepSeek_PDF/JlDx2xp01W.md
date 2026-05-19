## Summary
# Final Review Report

## Summary

This paper proposes SAMRefiner, a universal mask refinement framework that adapts the Segment Anything Model (SAM) for improving the quality of pre-existing coarse segmentation masks. The core technical contribution is a multi-prompt excavation strategy that generates three complementary prompt types from coarse masks — distance-guided points, context-aware elastic bounding boxes (CEBox), and Gaussian-style masks — which collaboratively mitigate diverse mask defects (false positives, false negatives, boundary errors). For semantic segmentation, a split-then-merge (STM) pipeline handles multi-object cases. An optional extension, SAMRefiner++, introduces a LoRA-based IoU adaption module trained with a ranking loss to improve mask selection accuracy without extra annotations.

The paper evaluates the framework extensively across instance segmentation (COCO), semantic segmentation (PASCAL VOC), and dedicated mask correction benchmarks (DAVIS-585), under unsupervised, weakly-supervised, and semi-supervised settings. Results show consistent improvements: e.g., +10.3% AP_mask on COCO WSSIS with 1% annotations, and 87.1 IoU on DAVIS-585, while running 5× faster than CascadePSP.

**Strengths:** The paper addresses a practically valuable problem, offers a systematic prompting framework for SAM adaptation, and demonstrates strong empirical gains across diverse settings. The self-boosted IoU adaption idea is clever and annotation-efficient.

**Key weaknesses:** (1) Missing statistical significance and variance reporting across all experiments — many gains could fall within noise. (2) Several mathematical formulations have clarity/reproducibility issues (CEBox feature similarity normalization, Gaussian mask denominator scaling). (3) The training-inference mismatch in IoU adaption (trained on single-prompt, tested on multi-prompt) lacks justification. (4) Time efficiency comparison is unfair (CRF with 16 workers vs. GPU methods with 1 GPU). (5) Novelty claims (e.g., "first SAM-based refinement solution") require careful scoping — related work documents SAM-enhanced pseudo labels, which partially overlap. Since Retrieval-Disabled Mode is active, novelty verification is deferred to manual check.

## Strengths
1. **Practical and well-motivated problem.** Mask refinement is a pressing need in segmentation pipelines where coarse pseudo masks are ubiquitous (WSSS, USS, semi-supervised learning). The paper correctly identifies that existing methods are task-specific, dataset-dependent, or inefficient, and positions SAMRefiner as a universal alternative.

2. **Systematic multi-prompt framework.** Rather than relying on a single prompt type (as in most SAM adaptation works), the paper introduces three complementary prompts that address different defect types: distance-guided points (mitigates boundary noise), CEBox (handles false-negative-induced box truncation), and Gaussian-style masks (provides soft spatial priors). This multi-prompt collaboration is technically sound and well-motivated by empirical failure analysis (Fig. 2).

3. **Extensive empirical evaluation.** The method is tested across 8+ benchmarks spanning instance segmentation, semantic segmentation, and dedicated mask correction under unsupervised, weakly-supervised, semi-supervised, and fully-supervised settings. This breadth convincingly demonstrates the method's claimed universality.

4. **Self-boosted IoU adaption.** The idea of using coarse mask IoU as a training signal to improve SAM's IoU prediction via a ranking loss (Eq. 4) is elegant and practical — it requires no extra annotations and addresses a genuine bottleneck in SAM's mask selection. Placing LoRA on the IoU head (rather than backbone) preserves SAM's generative capability.

5. **Efficiency advantage.** The ability to batch-process multiple masks per image (unlike prior instance-sequential methods) yields a genuine practical advantage, as demonstrated by the 5× speedup over CascadePSP on COCO train5K.

6. **Open and reproducible.** The paper commits to releasing code (SAMRefiner), which is important for the community adoption of this post-processing tool.

## Weaknesses
### W1. Missing statistical rigor (Major, Validity & Reproducibility)
All experimental results are reported as single runs without variance, standard deviations, or confidence intervals. Table 3 contains entries with gains as small as +0.6 AP_mask, which could fall within random variation. This undermines the reliability of comparative claims, especially against close baselines. **Root cause:** The paper prioritizes breadth of evaluation (many benchmarks) over depth (statistical verification per setting).

### W2. Unfair time efficiency comparison (Major, Fairness)
In Table 5, CRF is tested with "16 workers" (parallel CPU threads) while all GPU methods use "one 3090 GPU" without parallelization. This asymmetric comparison inflates SAMRefiner's relative speed advantage. If CascadePSP were run with 16 parallel instances, its wall-clock time would decrease substantially.

### W3. Mathematical clarity gaps in core formulas (Major, Reproducibility)
- **CEBox (Eq. 1-2):** The feature similarity computation lacks normalization specification. $F_{query} \cdot \hat{F}_{im}$ without L2 normalization produces unbounded values; a fixed threshold of 0.5 is not meaningful without normalization context.
- **Gaussian mask (Eq. 3):** The denominator $|\mathbb{1}_{M_{\text{coarse}}>0}| \cdot \gamma$ uses the absolute foreground pixel count, which couples Gaussian span to object size in an unintended way — large objects get nearly flat Gaussians, defeating the purpose.
- **STM merging (Algorithm 1):** The merging condition may paradoxically favor merging *distant* regions over nearby ones, as a larger merged bounding box makes the inequality easier to satisfy.

### W4. IoU adaption train-test mismatch (Major, Validity)
The LoRA adaptor is trained on single-prompt inputs but applied during inference to multi-prompt inputs (Section 3.3). The paper does not justify why this transfer should work, and Table 1 shows only marginal gains (0.2-2.5 IoU points) from SAMRefiner++ over SAMRefiner. The authors acknowledge that "coarse IoU performs poorly in multi-prompt cases" (Fig. 5c), which directly undermines the training signal used.

### W5. Missing error-type mechanistic analysis (Moderate, Depth)
The ablation (Table 1) shows that combining prompts works better than any single prompt, but there is no analysis of *which prompt addresses which defect type*. Without this analysis, the claimed "collaboration" remains a descriptive observation rather than a mechanistic understanding.

### W6. Limited failure-case analysis in main text (Moderate, Completeness)
Failure cases are only discussed in the appendix (Section C.6, D.3). The main text presents an overly optimistic picture. The conclusion does not mention any limitations.

### W7. Overclaim in novelty positioning (Moderate, Defensibility)
The contribution bullet "New Roadmap: SAMRefiner offers the first solution to address the mask refinement task based on SAM" is too strong. Appendix B.1 discusses SAM-based pseudo-label refinement (Chen et al. 2023), which is conceptually similar. The claim should be scoped to "first systematic multi-prompt excavation framework" rather than "first solution."

### W8. Related work as flat list (Minor, Presentation)
Section 2.2 lists methods chronologically rather than organizing them by comparison axes (training requirement, task scope, inference pattern), making it harder for readers to grasp the paper's positioning.

## Key Issues
### Issue 1: No variance/statistical reporting across all experiments (Critical, Affects all performance claims)
The paper does not report standard deviations, confidence intervals, or significance tests for any result. This is especially problematic for entries with <1 AP improvement (Table 3: +0.6 AP for PointWSSIS F10%). **Fix:** Run all main experiments with ≥3 seeds, report mean±std, and add paired significance tests for close baselines.

### Issue 2: Unfair time comparison inflates efficiency claim (Major, Affects practical contribution)
CRF uses 16 CPU workers while GPU methods use 1 GPU. **Fix:** Report all methods under matched conditions (single-worker GPU/CPU) and add a note about parallelizability.

### Issue 3: CEBox similarity computation is underspecified (Major, Affects reproducibility)
Eq. (1)-(2) lack L2 normalization details; feature similarity threshold 0.5 is arbitrary without normalization. **Fix:** Explicitly state cosine similarity with L2 normalization, or add learnable temperature.

### Issue 4: Gaussian mask span is object-size-coupled (Major, Affects design validity)
Eq. (3) uses absolute foreground pixel count in denominator, causing size-dependent Gaussian spread. **Fix:** Replace with $d_{\max}^2$ (squared maximum distance from center to any foreground pixel).

### Issue 5: IoU adaption train-test mismatch (Moderate, Affects claimed improvement)
Trained on single-prompt but tested on multi-prompt without justification. **Fix:** Add an ablation comparing single-prompt-trained vs. multi-prompt-trained (oracle) adaption to bound the gap.

### Issue 6: STM merging condition may cause counterintuitive over-merging (Moderate, Affects semantic seg quality)
Algorithm 1's condition may favor merging distant regions. **Fix:** Add centroid-distance penalty or IoU-based overlap check.

### Issue 7: "First SAM-based refinement" claim is over-scoped (Moderate, Affects novelty defensibility)
Overlaps with existing SAM-enhanced pseudo-label works. **Fix:** Rephrase to "first systematic multi-prompt excavation framework for SAM-based refinement."

### Issue 8: Conclusion lacks limitation discussion (Minor, Affects completeness)
No mention of documented failure modes. **Fix:** Restructure into validated findings, bounded limitations, and future work.

## Actionable Suggestions
### S1. Add statistical rigor (Must, Priority P0)
- Run all main experiments (Tables 3, 4, 5, 6) with 3 random seeds.
- Report mean ± std in all tables.
- For entries with improvement <1 AP, add a paired Wilcoxon signed-rank test or bootstrap confidence interval.
- In the narrative, distinguish "substantial improvements" (>5%) from "modest gains" (<2%).

### S2. Fix time comparison fairness (Must, P0)
- Re-run CRF with a single CPU thread and report time.
- Report GPU methods with both 1-GPU and multi-GPU settings (if applicable).
- Add a footnote explaining parallelization assumptions.

### S3. Clarify CEBox mathematical formulation (Must, P1)
- In Eq. (2), change to: $Sim = [\text{cosine}(F_{query}, \hat{F}_{im})]_{\ge 0.5}$.
- Add text: "Both $F_{query}$ and $\hat{F}_{im}$ are L2-normalized before computing the dot product."
- Specify the upsampling method: "$\hat{F}_{im}$ is obtained by bilinear interpolation from $F_{im}$ to resolution $H \times W$."

### S4. Fix Gaussian mask denominator (Must, P1)
- Replace Eq. (3) denominator $|\mathbb{1}_{M_{\text{coarse}}>0}| \cdot \gamma$ with $\gamma \cdot d_{\max}^2$ where $d_{\max} = \max_{(x,y) \in FG} \|(x,y) - (x_0,y_0)\|_2$.
- Re-run the $\omega,\gamma$ sensitivity analysis (Fig. 9a) with the corrected formulation.

### S5. Justify IoU adaption train-test gap (Must, P1)
- Add a controlled experiment: train LoRA adaptor on multi-prompt inputs using oracle IoU (GT-based) as supervision, and compare with single-prompt-trained variant. Report the gap as the "upper bound" of improvement.
- Discuss the modest gains (0.2-2.5 points) more explicitly.

### S6. Fix STM merging condition (Nice-to-have, P2)
- In Algorithm 1, line 9, change condition to:
  `if (a_box_i + a_box_j) / a_box_bar > mu AND centroid_distance < tau * sqrt(a_box_bar):`
- Add a distance threshold $\tau$ to prevent merging of spatially separated regions.

### S7. Add error-type ablation (Nice-to-have, P2)
- Categorize DAVIS-585 defects into false-positive, false-negative, and boundary-error subsets.
- Report per-prompt-type performance on each subset (Table 1 extended).
- Add a paragraph explaining which prompt addresses which defect type.

### S8. Restructure Conclusion (Nice-to-have, P2)
- Replace current conclusion with three-paragraph structure: validated findings (with numbers), bounded limitations (from Appendix D.3), and actionable next steps.
- Remove promotional phrasing like "holds significant potential to expedite."

### S9. Tone down novelty claims (Must, P0)
- Replace "first solution" with "first systematic multi-prompt excavation framework" in contribution bullet.
- In Section 2.3, acknowledge existing SAM-based refinement attempts and clarify the differentiation.

### S10. Add reproducibility checklist (Nice-to-have, P2)
- In Appendix A.2, add SAM inference hyperparameters (pred_iou_thresh, stability_score_thresh, box_nms_thresh).
- Report GPU memory usage for single-image and batch inference.

## Storyline Options + Writing Outlines
### Abstract Outline (Compact, 4-5 sentences)

**S1 — Problem & Domain:** "Image segmentation pseudo-masks generated under incomplete supervision are widely used to reduce annotation cost, but their quality is often degraded by noise and boundary errors, limiting downstream model performance."

**S2 — Prior Gap:** "Existing mask refinement methods are either task-specific, dataset-dependent, or inefficient, restricting their practical deployment across diverse segmentation settings."

**S3 — Proposed Method:** "We propose SAMRefiner, a universal mask refinement framework that adapts the Segment Anything Model (SAM) via a noise-tolerant multi-prompt excavation strategy, generating distance-guided points, context-aware elastic boxes, and Gaussian-style masks collaboratively from coarse masks."

**S4 — Key Result:** "On DAVIS-585, SAMRefiner achieves 87.1 IoU — a 5.7 point improvement over coarse masks — while running 5× faster than prior methods. It consistently improves pseudo-mask quality across 8+ benchmarks under unsupervised, weakly-supervised, and semi-supervised settings."

**S5 — Bounded Implication:** "SAMRefiner serves as an efficient plug-and-play post-processor for any segmentation pipeline, and its self-boosted variant (SAMRefiner++) further refines mask selection without extra annotations."

### Current Introduction Map & Diagnosis

The current introduction has 5 paragraphs with the following roles:
1. **P1 (Page 1):** Context — pseudo-labeling paradigm and its noise problem. 
2. **P2 (Page 1-2):** Gap — four drawbacks of existing refinement methods.
3. **P3 (Page 2):** SAM introduction — why SAM is relevant but adapting it is nontrivial.
4. **P4 (Page 2):** Challenge — naive prompting fails; need for noise-tolerant prompts.
5. **P5 (Page 2):** Solution overview — SAMRefiner framework components.
6. **Contribution list (Page 3):** Four bullet claims.

**Diagnosis:** The current storyline is functional but has two issues:
- P3 and P4 could be merged, as both address the SAM-prompting challenge.
- The contribution bullets overlap and mix novelty claims with performance claims.

### Recommended Storyline Candidate (Best)

**P1 — Problem & Stakes:** Same as current P1 but with quantitative anchor (e.g., "Pseudo masks from WSSS typically achieve 40-50 mIoU on VOC, leaving a 30+ point gap to fully-supervised performance"). 

**P2 — Prior Limitations (structured):** Same as current P2 but organized by training dependency (training-free vs dataset-specific foundation-model-based) rather than four isolated drawbacks.

**P3 — Why SAM? Why not trivial?** (Merged current P3+P4, shortened): "SAM's zero-shot capability makes it a natural candidate for mask refinement, but naive prompting fails: tight boxes from coarse masks are truncated by false negatives, raw mask prompts are incompatible with SAM's logit-based design, and points are ambiguous near boundaries."

**P4 — Our Approach (overview):** "We propose SAMRefiner with three key ideas: (i) multi-prompt excavation to generate robust prompts, (ii) split-then-merge for multi-object semantic segmentation, (iii) optional self-boosted IoU adaption for improved mask selection."

**P5 — Contribution summary (condensed to 3 bullets):** See revised bullets in annotation on Page 3.

### Introduction Paragraph-by-Paragraph Rewrite Plan

**P1 (Page 1, Lines 30-43):** Add a quantitative anchor at the end.
**Mentor Revised Version (last sentence add):**
"For instance, weakly-supervised pseudo masks on PASCAL VOC typically achieve only 40-50 mIoU, leaving a gap of over 30 points compared to fully supervised models — a gap that dedicated refinement could meaningfully close."

**P2 (Page 1-2, Lines 44-71):** Restructure into organized taxonomy.
**Mentor Revised Version (opening):**
"Existing mask refinement techniques fall into three categories: (1) training-free post-processing like CRF, which is universally applicable but lacks semantic context; (2) dataset-specific CNN-based methods like CascadePSP and CRM, which excel on semantic segmentation but generalize poorly to instance segmentation; and (3) instance-sequential methods like SegRefiner, which improve quality at the cost of throughput. In all cases, the refinement pipeline is tied to particular tasks or training protocols, limiting universality."

**P3 (Page 2, Lines 72-81):** Soften "unexplored" claim.
**Mentor Revised Version:**
"Recently, the Segment Anything Model (SAM) has shown remarkable zero-shot segmentation capability. Several works have explored SAM for mask generation and pseudo-label refinement, but a systematic framework for noise-tolerant prompting in the universal mask refinement setting remains absent."

**P4 (Page 2, Lines 82-91):** Keep largely as-is, but replace "terrible" with more precise academic language.
**Mentor Revised Version (replace "terrible" sentence):**
"we find that directly using the coarse mask as a prompt produces low-quality outputs, as SAM's pre-training treats mask prompts as iterative logits rather than discrete binary inputs."

**P5 (Page 2, Lines 92-100):** Keep as solution overview, but move "5× faster" claim to results section.

## Priority Revision Plan
### P0 — Must fix (Publication-critical)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0 (1) | **Missing statistical rigor** (W1) | Add ≥3 seed runs with std for all main tables | Converts qualitative claims to statistically grounded results | 2-3 GPU-days |
| P0 (2) | **Unfair time comparison** (W2) | Normalize compute configurations; add single-thread CRF baseline | Restores fairness of efficiency claim | <1 day |
| P0 (3) | **Novelty overclaim** (W7) | Rephrase "first solution" to "first systematic framework" | Reduces reviewer friction | <1 hour |
| P0 (4) | **CEBox normalization** (W3, Eq 1-2) | Add L2 normalization and specify upsampling method | Ensures reproducibility | <1 hour |
| P0 (5) | **Gaussian mask denominator** (W3, Eq 3) | Replace area-based denominator with $d_{max}^2$ | Fixes object-size-coupling flaw | <1 day + re-run Fig 9a |

### P1 — Should fix (Quality improvement)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P1 (6) | **IoU adaption mismatch** (W4) | Add oracle upper-bound experiment | Clarifies method's ceiling | 1-2 days |
| P1 (7) | **STM merging condition** (W3, Algo 1) | Add centroid-distance penalty | Prevents over-merging | <1 day |
| P1 (8) | **Missing error-type analysis** (W5) | Categorize DAVIS-585 defects; per-prompt breakdown | Strengthens mechanistic understanding | 2-3 days |
| P1 (9) | **Conclusion restructuring** (W8) | Add limitations and quantitative recap | Improves completeness | <1 day |

### P2 — Nice to have (Polish)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P2 (10) | **Related work restructuring** (W8) | Reorganize as training-dependency taxonomy | Better positioning | <1 day |
| P2 (11) | **SAM inference reproducibility** | Add inference hyperparameters to appendix | Reproducibility | <1 hour |
| P2 (12) | **Abstract number anchor** | Add one specific result to abstract | Self-contained abstract | <1 hour |

### Revision Roadmap ASCII Diagram

```text
[P0 Fixes — Must Do]
    |
    ├── Add statistical rigor (3-seed runs)
    ├── Normalize time comparison
    ├── Fix CEBox normalization + Gaussian denominator
    ├── Rephrase novelty claims
    |
    v
[P1 Fixes — Should Do]
    |
    ├── IoU adaption oracle experiment
    ├── STM merging condition fix
    ├── Error-type ablation analysis
    ├── Restructure conclusion
    |
    v
[P2 Fixes — Polish]
    |
    ├── Reorganize related work taxonomy
    ├── Add SAM inference details
    ├── Anchor abstract with number
    |
    v
[Expected Outcome: 5-6/10 -> 7-8/10 after revision]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (Data/Split/Protocol/Baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|-------------|-----------------|-------------------|
| E1 | Multi-prompt vs single-prompt comparison | DAVIS-585; compare Point/Box/Mask/All prompts | IoU, boundary IoU, Top-1 Acc | Multi-prompt (ALL) achieves 86.9 IoU, best single (Box+Mask) 84.6 | C2 (multi-prompt > single) | No error-type breakdown |
| E2 | CEBox vs tight box | PointWSSIS COCO; compare tight box vs CEBox | AP_box, AP_mask, AP_boundary | CEBox improves AP_box 36.7→38.2 | C2 (CEBox) | Small gain (1.5 AP_box) |
| E3 | STM effectiveness | MaskCLIP/CLIP-ES on VOC; w/ and w/o STM | mIoU | +6.2% for MaskCLIP, +0.2% for CLIP-ES | C2 (STM) | Diminishing returns on better masks |
| E4 | IoU adaption effect | DAVIS-585; SAMRefiner vs SAMRefiner++ with various prompts | IoU, bIoU, Top-1 Acc | Top-1 Acc improves 44.1→63.8 for ALL prompts | C3 (IoU adaption) | Marginal IoU gain (86.9→87.1) |
| E5 | Instance seg under incomplete supervision | COCO; CutLER (unsup), NB (semi-sup), PointWSSIS (weakly-semi) | AP_mask, AP_boundary | Consistent gains; +10.3 AP for PointWSSIS F1% | C1 (universality) | No variance/statistical testing |
| E6 | Semantic seg under incomplete supervision | VOC; MaskCLIP (unsup), BECO/CLIP-ES (weakly-sup) | mIoU (train), mIoU (val) | +9.5 mIoU for MaskCLIP, +8.5 for CLIP-ES | C1 (universality) | DeepLabV2 only — limited architecture scope |
| E7 | SOTA comparison | DAVIS-585, COCO, VOC; CRF, CascadePSP, CRM, SegRefiner | IoU, mIoU, AP | SAMRefiner best on all except VOC DeepLabV2 baseline | C1 (SOTA) | Unfair time comparison |
| E8 | HQ-SAM upgrade | DAVIS-585, COCO, VOC; SAM vs HQ-SAM | IoU, AP, mIoU | HQ-SAM improves DAVIS-585 (87.7→90.6) but not COCO | Extensibility | Limited to large/salient objects |
| E9 | Human annotation correction | COCO2017 val; refine COCO masks, evaluate with LVIS | AP_mask, AP_boundary | +3.2 AP_mask, +5.7 AP_boundary | C1 (practical value) | Qualitative only |

### Research-Theme Gap Diagnosis

**Gap 1 — New Knowledge:** The paper's primary new knowledge is the multi-prompt excavation framework. However, the *mechanism* by which different prompts collaborate (which prompt handles which defect) is not established, weakening the knowledge contribution.

**Gap 2 — Reproducibility:** Critical because several mathematical formulations (CEBox normalization, Gaussian span, STM merging condition) are underspecified or potentially incorrect. Without clarification, exact reproduction is not guaranteed.

**Gap 3 — Impact on Practice:** The practical value is clear (ready-to-use refinement tool), but the statistical robustness of gains needs verification before practitioners can rely on the performance numbers for production decisions.

### Proposed Research Experiments (P0/P1/P2)

| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|-------------|-----------|---------------|-------------------|---------|------------------|-----------|---------------|
| C1 (universality) | SAMRefiner gains are statistically significant | Run 3 seeds on Tables 3/4 main entries; compute std and p-value vs baseline | Same baselines as original | Mean AP ± std, p-value | p<0.05 for all >1% gain entries | 2-3 GPU-days | Statistical grounding for all claims |
| C2 (multi-prompt collaboration) | Different prompts address different defect types | Categorize DAVIS-585 into FP/FN/boundary subsets; compute per-prompt IoU per subset | Single-prompt baselines | Per-subset IoU | Each prompt excels on a different subset | 1 day | Mechanistic understanding |
| C3 (IoU adaption) | Multi-prompt training would close the gap to oracle | Train LoRA on multi-prompt with GT IoU; compare with current single-prompt-trained variant | SAMRefiner (no adaption), SAMRefiner++ (current) | Top-1 Acc, final IoU | Oracle upper bound > current by >2% Top-1 Acc | 1 day | Quantifies remaining gap |
| C1 (efficiency) | SAMRefiner is faster under fair comparison | Re-run CRF single-threaded; re-run CascadePSP with batch processing | SAMRefiner on same hardware | Wall-clock time | SAMRefiner still 2x faster under fair comparison | <1 day | Defensible efficiency claim |

### Experiment Upgrade Plan ASCII Diagram

```text
P0 Experiments (Must Do Before Resubmission)
│
├── Seed-variance runs (3 seeds for Tables 3,4,5,6)
│   └── Output: mean±std for all entries
│
├── Fair time comparison
│   └── Output: corrected Table 5 time row
│
P1 Experiments (Should Do)
│
├── Error-type ablation (DAVIS-585 subsets)
│   └── Output: per-prompt per-defect table
│
├── IoU adaption oracle experiment
│   └── Output: single-prompt vs multi-prompt vs oracle comparison
│
P2 Experiments (Nice to Have)
│
├── STM condition fix validation
├── Gaussian mask reformulation validation (re-run Fig 9a)
└── Ablation on more backbones (ResNet, Swin, etc.)
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Scoring Rationale

**Primary scoring dimensions:** Research value + Novelty first, then validity/soundness, then reproducibility.

**Strengths supporting the score:** The paper addresses a practically important problem (universal mask refinement) with a technically sound multi-prompt framework. The empirical breadth across 8+ benchmarks is impressive, and the consistent improvements under diverse supervision settings demonstrate genuine practical value. The IoU adaption idea (LoRA on the prediction head, not backbone) is elegant.

**Weaknesses constraining the score:**
- **Missing statistical rigor (W1):** Without variance reporting, the magnitude of many claimed improvements cannot be verified. This is a significant validity concern.
- **Mathematical clarity gaps (W3):** The CEBox normalization and Gaussian mask scaling issues affect reproducibility.
- **Unfair time comparison (W2):** The efficiency advantage may be overstated.
- **Novelty overclaim (W7):** The "first SAM-based refinement" claim needs tighter scoping.
- **Retrieval-Disabled Mode:** Novelty verification against external literature is deferred to manual check, adding uncertainty to the novelty score.

**Score assignment:** The paper's research value is moderately high (practical tool, broad evaluation), but the methodological and reproducibility issues lower the overall confidence. After P0/P1 fixes, the score could increase substantially.

**Final Score:** 6/10

**Post-Revision Target:** [7, 8]/10 — achievable if P0 items (statistical rigor, formula clarifications, fairness fixes) are fully addressed and P1 items (error-type analysis, IoU oracle experiment) are completed.