## Summary
# Final Review Report

## Summary

This paper introduces Pseudo-Calibration (PseudoCal), a post-hoc framework for calibrating predictive uncertainty in unsupervised domain adaptation (UDA). The key idea is to reframe UDA calibration from a cross-domain covariate-shift problem into a target-domain-specific unsupervised problem, then use inference-stage mixup — grounded in the cluster assumption — to synthesize a labeled pseudo-target set whose correct-wrong statistics approximate those of real target data. Temperature scaling is then applied to this labeled pseudo-target set. The method is evaluated extensively across 5 UDA scenarios (closed-set, partial-set, source-free white-box, source-free black-box, semantic segmentation), covering 10 UDA methods and 5 calibration baselines.

**Strengths**: The conceptual reframing is elegant and clearly presented. The method is simple, post-hoc, requires no extra training, and works across diverse UDA settings without source data. The empirical validation is broad and the ablation study (Table 9) is comprehensive. The appendix analysis of sample-level correspondence (CRharmonic, Appendix D) is rigorous and transparent.

**Core weaknesses**: (1) The factorization claim (correct-wrong statistics → same temperature) has a logical gap — matching counts alone does not guarantee matching optimal temperatures without also matching per-sample confidence distributions. (2) No variance reporting or statistical significance testing accompanies any of the experimental results, making it impossible to assess whether improvements are reliable. (3) The segmentation experiments reveal a failure mode on GTA5→Cityscapes where PseudoCal underperforms both Ensemble and TempScal-src, but this is glossed over in the text. (4) The word "guarantees" in the abstract and contribution claims overstates what is an assumption-dependent empirical method. (5) The Conclusion introduces untested future claims (open-set UDA, object detection).

**Decision context**: The paper presents a useful calibration method with a novel conceptual angle and strong empirical breadth. However, the absence of variance/significance analysis and the overclaiming in key statements are significant weaknesses that should be addressed before acceptance.

## Strengths
1. **Conceptual reframing**: The paper shifts UDA calibration from the dominant covariate-shift + importance-weighting paradigm to a target-domain-specific unsupervised perspective. This reframing is clean, principled, and enables applicability to privacy-preserving (source-free) settings where prior methods cannot operate.

2. **Methodological simplicity**: PseudoCal is a post-hoc method requiring no additional training, no density estimation, and no source data access. With a single fixed hyperparameter (λ=0.65), it is straightforward to implement and deploy, as evidenced by the clear PyTorch pseudocode in Appendix A.

3. **Empirical breadth**: The evaluation spans 10 UDA methods × 5 scenarios × multiple benchmarks (Office-31, Office-Home, VisDA, DomainNet, Image-Sketch, Cityscapes). This is significantly broader than most UDA calibration papers, which typically evaluate on 2-3 methods.

4. **Ablation rigor**: Table 9 systematically compares PseudoCal's inference-stage mixup against 9 alternative pseudo-target synthesis strategies (PseudoCal-same, RandAug, CutMix, ManifoldMix, Pseudo-Label, Filtered-PL, etc.), cleanly demonstrating the importance of cross-cluster mixing.

5. **Transparent correspondence analysis**: Appendix D introduces four correspondence metrics (CRcorrect, CRwrong, CRarithmetic, CRharmonic) and honestly reports CRharmonic ≈ 60% across diverse UDA methods. This provides a quantitative foundation for understanding when and why PseudoCal works.

6. **Versatility**: PseudoCal works across closed-set, partial-set, source-free (white-box and black-box), and semantic segmentation settings, demonstrating broad applicability.

## Weaknesses
1. **Missing statistical significance (Major)**: All results are reported as point estimates averaged over 5 runs, without standard deviations, confidence intervals, or significance tests. Since ECE improvements are often 1-4% and ECE is known to be a noisy metric, readers cannot assess whether the reported gains are statistically reliable. This is the most significant technical weakness.

2. **Segmentation failure mode (Major)**: On GTA5→Cityscapes, PseudoCal (5.73% ECE) underperforms both Ensemble (2.66%) and TempScal-src (4.61%). The paper's claim that PseudoCal "performs the best on average" masks this failure, which is relevant for safety-critical applications.

3. **Overclaiming (language)**: The abstract uses "guarantees" regarding the pseudo-target set capturing real target structure. The method is assumption-dependent (cluster assumption) and empirical (CRharmonic ≈ 60%, not 100%). The word "guarantees" should be replaced.

4. **Factorization gap (Major)**: The core insight that "datasets with similar correct-wrong statistics share similar temperatures" (Page 2) is not fully proven. The NLL factorization in Eq 2 separates correct/wrong counts but does not account for per-sample confidence distributions, which also affect optimal temperature.

5. **Circularity in Eq 2 (Major)**: The sets Dc (correct) and Dw (wrong) are defined using the model's own predictions (argmax). If the temperature T changes during optimization, the partition of samples into Dc/Dw could also change, but the analysis treats them as fixed. This is not addressed.

6. **λ sensitivity claim undersupported (Minor)**: The paper states λ=0.65 works universally, but the sensitivity analysis covers only 4 out of 15+ method-scenario combinations. Different UDA methods may have different optimal λ.

7. **Table 1 oversimplification (Minor)**: MC-Dropout is marked ✗ for "no harm to accuracy" when it is a post-hoc method that does not change accuracy. Ensemble is marked ✓ for "label shift" without justification.

8. **Conclusion overreach (Minor)**: The conclusion introduces untested extensions (open-set UDA, object detection) as future work but frames the method as "versatile" based on these untested scenarios.

## Key Issues
### Issue 1: Missing variance and significance analysis (Severity: Major)
**Location**: Page 6 - Implementation Details; Page 6-8 Results Tables 2-7.
**Evidence**: The paper states "results are averaged over five random runs" but reports only point estimates (mean ECE) without standard deviations, confidence intervals, or significance tests in any table.
**Impact**: Since ECE improvements are often 1-4% and ECE is a noisy metric, the reader cannot determine if improvements are statistically significant or within random variation. This undermines the central empirical claim of "consistently and significantly outperforming all other calibration methods."
**Fix (Must)**: Add standard deviations (±std) to all ECE tables. Add a supplementary significance analysis (paired t-test or Wilcoxon signed-rank) comparing PseudoCal against the best baseline. Report per-seed results for at least one representative setting.

### Issue 2: Factorization argument has a logical gap (Severity: Major)
**Location**: Page 2 - Method Introduction; Page 4 - Section 3.1, Equations 1-2.
**Evidence**: The paper claims that "datasets with similar correct-wrong statistics should share similar temperatures." The factorization in Eq 2 separates NLL into correct/wrong terms but does not account for the distribution of confidence values within each group. Two datasets with identical correct/wrong counts can have very different optimal temperatures if their per-sample confidence distributions differ.
**Impact**: The theoretical motivation for the method is incomplete. The paper addresses this indirectly through empirical evidence (Figure 1b-c) but should explicitly acknowledge the gap.
**Fix (Must)**: Add a sentence acknowledging that matching correct-wrong statistics is necessary but may not be sufficient — the empirical validation confirms that inference-stage mixup also approximates confidence distributions.

### Issue 3: Dc/Dw partition circularity in Eq 2 (Severity: Major)
**Location**: Page 4 - Section 3.1, Equation 2.
**Evidence**: The sets Dc (correct predictions) and Dw (wrong predictions) are defined using the model's own predictions. If temperature T changes during optimization (as it does in TempScal), the argmax predictions may change, altering the composition of Dc and Dw. The equation treats Dc and Dw as fixed.
**Impact**: The factorization is technically incorrect as written because Dc/Dw should be functions of T, not constants. In practice, temperature scaling rarely changes argmax predictions for well-calibrable models, so this may have small practical effect, but the theoretical presentation is imprecise.
**Fix (Must)**: Add a note: "Dc and Dw are defined using the original (uncalibrated) predictions at T=1 and held fixed during optimization."

### Issue 4: Segmentation failure underreported (Severity: Major)
**Location**: Page 8 - Semantic Segmentation paragraph, Table 7.
**Evidence**: On GTA5→Cityscapes, PseudoCal (5.73%) underperforms Ensemble (2.66%) and TempScal-src (4.61%). The text says "PseudoCal performs the best on average," which is technically true (average of GTA5 and SYNTHIA) but hides a notable failure case.
**Impact**: Selective reporting reduces reader trust. The segmentation failure suggests PseudoCal's cluster assumption may be weaker for certain domain gaps or when the model is not adapted (source-only).
**Fix (Must)**: Discuss the GTA5 result explicitly, analyze why the cluster assumption might fail there, and suggest conditions under which PseudoCal should/should not be applied.

### Issue 5: Overclaiming language ("guarantees") (Severity: Major)
**Location**: Page 1 - Abstract.
**Evidence**: The abstract states that inference-stage mixup "guarantees that a synthesized labeled pseudo-target set captures the structure of the real unlabeled target data." Appendix D shows CRharmonic ≈ 60%, far from a guarantee.
**Impact**: Overstatement can mislead readers about the reliability of the method and invites skepticism from reviewers.
**Fix (Must)**: Replace "guarantees" with "enables" or "under the cluster assumption, ensures that."

## Actionable Suggestions
### S1 (Must): Add variance reporting and significance tests
Add standard deviations (±std) across the 5 random seeds to all ECE tables (Tables 2-7). Add a paired significance test (e.g., Wilcoxon signed-rank across all task-method combinations) comparing PseudoCal against the strongest baseline. Report per-seed results for at least one representative benchmark (e.g., Office-Home) in the appendix.

### S2 (Must): Replace "guarantees" with bounded language
Throughout the paper, replace "guarantees" and "successfully transforms" with phrasing that acknowledges the assumption-dependent nature. Examples: "enables," "under the cluster assumption, facilitates," "empirically demonstrates."

### S3 (Must): Clarify the Dc/Dw partition in Equation 2
Add a sentence after Equation 2: "Here Dc and Dw are determined using the model's uncalibrated predictions (T=1) and are held fixed during temperature optimization."

### S4 (Must): Discuss the GTA5 segmentation failure
In Section 4.3 or Section 5, add a paragraph analyzing why PseudoCal underperforms on GTA5→Cityscapes. Possible reasons: (a) source-only model may not satisfy the cluster assumption, (b) pixel-level mixing may not preserve semantic correspondence, (c) the domain gap may be larger. Suggest when practitioners should use alternatives.

### S5 (Must): Qualify the factorization insight
Add a sentence in Section 3.1: "While matching correct-wrong counts is important, the optimal temperature also depends on the distribution of confidence values within each group. Our empirical analysis in Section 4.3 shows that inference-stage mixup approximates both conditions."

### S6 (Nice-to-have): Extend λ sensitivity analysis
Add at least one source-free UDA method (SHOT or DINE) to the λ sensitivity analysis (Figure 3c-d). Consider testing λ=0.65 on segmentation to verify cross-task robustness.

### S7 (Nice-to-have): Add training-stage mixup with λ=0.65 as a control in Table 9
Add one row: "PseudoCal (train-stage, λ=0.65)" — using training-stage mixup with λ=0.65, then calibrate via TempScal-src. This isolates whether the improvement comes from the inference stage or the mix ratio.

### S8 (Nice-to-have): Revise Table 1 for accuracy
Either add footnotes clarifying that MC-Dropout is post-hoc (no accuracy harm) and Ensemble does not explicitly model label shift, or replace ✓/✗ with a more nuanced indicator.

### S9 (Nice-to-have): Restructure Conclusion
Replace the current conclusion with a three-part structure: (1) validated findings with bounded claims, (2) explicit limitations (assumption dependency, segmentation failure, variance not assessed), (3) conditional future work statement.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows: (P1) UDA background and accuracy focus → (P2) Calibration is important but under-explored in UDA → (P3) Existing importance-weighting methods have drawbacks → (P4) Our novel perspective and contributions. This is a functional structure but could be sharpened.

**Problem alignment check**: The stated problem is "poor calibration in UDA," and the solution (matching correct-wrong statistics via mixup) is well-aligned.
**Variable alignment check**: Core concepts (correct-wrong statistics, cluster assumption, pseudo-target synthesis) in introduction appear clearly in the Method section. ✓
**Contribution-evidence alignment check**: Contributions 1 (target-domain perspective) and 2 (PseudoCal) are well-supported; Contribution 3 (comprehensive evaluation) is supported but lacks variance analysis. Partial ✓.

### Recommended Storyline (Single Best)

**Abstract Outline (complete, copy-ready)**:

S1 (Problem & Domain): "Unsupervised domain adaptation (UDA) models frequently exhibit poorly calibrated predictive uncertainty on target data, a critical issue for safety-critical applications such as autonomous driving and medical diagnosis."

S2 (Challenge): "Two key challenges hinder UDA calibration: the absence of labeled target data, which prevents supervised calibration, and severe distribution shifts between source and target domains."

S3 (Prior Gap): "Existing approaches treat UDA calibration as a covariate-shift problem and use importance weighting with source data, but they require complex density estimation, fail under label shift, and cannot operate in source-free settings."

S4 (Method): "We propose Pseudo-Calibration (PseudoCal), a post-hoc framework that reframes UDA calibration as a target-domain unsupervised problem. By applying inference-stage mixup across predicted clusters and leveraging the cluster assumption, PseudoCal synthesizes a labeled pseudo-target set whose correct-wrong statistics approximate those of real target data, enabling direct application of temperature scaling."

S5 (Result & Boundary): "Extensive evaluation across 5 UDA scenarios and 10 UDA methods shows that PseudoCal consistently outperforms existing calibration methods on average, though its effectiveness depends on the cluster assumption holding for the given model, and variance analysis is needed to confirm statistical reliability."

### Introduction Outline (Paragraph-by-Paragraph)

**P1: Establish territory — UDA's accuracy focus and the overlooked calibration problem**
- Role: Set stakes; motivate calibration importance.
- Claim: UDA has made accuracy gains but calibration is equally crucial for safety-critical applications.
- Transition: "However, achieving reliable predictive uncertainty estimation is as crucial as high accuracy..."

**P2: Identify gap — Calibration in UDA is under-explored with unique challenges**
- Role: Define the two challenges (no target labels, distribution shift).
- Claim: Prior calibration methods fail due to these challenges.
- Evidence: Reference Wang et al. (2020) for accuracy-calibration trade-off; cite Figure 1(a) for illustration.
- Transition: Lead into criticism of existing approaches.

**P3: Critique existing solutions — Covariate-shift methods have limited scope**
- Role: Explain why importance-weighting is insufficient (label shift, complexity, source dependency).
- Claim: These methods are not general across UDA scenarios.
- Transition: "In contrast, we adopt a novel perspective..."

**P4: Present new perspective and contributions**
- Role: Introduce target-domain unsupervised framing, factorization insight, PseudoCal overview.
- Claim: Matching correct-wrong statistics enables source-free, post-hoc calibration.
- Evidence: Preview Figure 1(b)-(c) for correct-wrong statistics and reliability diagrams.
- Transition into Method section.

This structure tightens the narrative arc from "UDA accuracy focus → calibration gap → existing methods' limitations → our reframing → empirical validation of the reframing." The current paper largely follows this but could strengthen P2 by more clearly separating the two challenges and P3 by acknowledging PseudoCal's own dependency on the cluster assumption (for balanced critique).

## Priority Revision Plan
### P0 — Critical (Must fix before resubmission)

| # | Task | Location | Effort | Impact |
|---|------|----------|--------|--------|
| 1 | Add std/CI to all ECE tables | Tables 2-7 | Medium | High — establishes statistical reliability |
| 2 | Replace "guarantees" with bounded language | Abstract, Page 1 | Low | High — corrects overclaim |
| 3 | Clarify Dc/Dw fixed partition in Eq 2 | Page 4, Section 3.1 | Low | Medium — fixes theoretical precision |
| 4 | Discuss GTA5 segmentation failure | Page 8, Table 7 discussion | Low | Medium — honest reporting |
| 5 | Qualify factorization insight (confidence distributions matter) | Page 2, Page 4 | Low | Medium — completes theoretical motivation |

### P1 — Important (Recommended before submission)

| # | Task | Location | Effort | Impact |
|---|------|----------|--------|--------|
| 6 | Add training-stage mixup (λ=0.65) control to ablation | Table 9 | Low | Medium — cleaner causal isolation |
| 7 | Extend λ sensitivity to source-free methods | Figure 3 | Low | Medium — strengthens universality claim |
| 8 | Revise Conclusion to bounded claims | Page 9 | Low | Medium — defensible framing |

### P2 — Nice-to-have (Quality improvement)

| # | Task | Location | Effort | Impact |
|---|------|----------|--------|--------|
| 9 | Revise Table 1 for accuracy | Page 3 | Low | Low — minor correctness |
| 10 | Add per-seed results in appendix | Appendix | Medium | Low — supplementary transparency |

```text
ASCII Diagram — Revision Strategy Roadmap

[Overclaim in Abstract]
    → Fix: Replace "guarantees" with "enables"
    → Expected impact: Accurate scope boundaries, increased reviewer trust

[Missing variance in results]
    → Fix: Add ±std + significance test to all tables
    → Expected impact: Readers can assess reliability of reported gains
    
[Factorization gap in Eq 1→2]
    → Fix: Qualify confidence distribution dependency
    → Expected impact: Completes theoretical justification

[Dc/Dw circularity in Eq 2]
    → Fix: Clarify fixed partition at T=1
    → Expected impact: Theoretical correctness

[Segmentation failure underreported]
    → Fix: Explicit discussion of GTA5 underperformance
    → Expected impact: Honest scope boundaries, no selective reporting
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Closed-set UDA calibration | 6 UDA methods × 4 benchmarks (Office-Home, Office-31, VisDA, DomainNet) | ECE | PseudoCal achieves lowest avg ECE across benchmarks | C2 (PseudoCal effective), C3 (comprehensive evaluation) | No variance reported; λ sensitivity tested on only 2 method-benchmark combos |
| E2 | Partial-set UDA calibration | 3 UDA methods × Office-Home | ECE | PseudoCal outperforms second-best by 4.24% avg | C2, C3 | Only one benchmark; no significance test |
| E3 | Source-free UDA (white-box) | SHOT × DomainNet + Image-Sketch | ECE | PseudoCal avg 6.00% (vs Ensemble 14.87%) | C1 (works w/o source), C2 | No comparison to source-free-specific calibration methods |
| E4 | Source-free UDA (black-box) | DINE × DomainNet + Image-Sketch | ECE | PseudoCal avg 12.20% (vs Ensemble 18.22%) | C1, C2 | High ECE (47.76% on Sketch) vs Oracle 5.90% |
| E5 | Semantic segmentation | Source-only models: GTA5→Cityscapes, SYNTHIA→Cityscapes | ECE | PseudoCal avg 10.86% (best on avg) | C2 (versatility) | Underperforms Ensemble on GTA5 (5.73% vs 2.66%) |
| E6 | Ablation: pseudo-target synthesis | 9 strategies × 9 UDA method-task combos | ECE | Inference-stage mixup (ours) best among all alternatives | C2 (mixup design choice) | Missing control: train-stage mixup with same λ=0.65 |
| E7 | Mix ratio λ sensitivity | λ ∈ {0.51-0.9} × 4 method-task combos | ECE | Optimal λ ≈ 0.6-0.7 | C2 (λ robustness) | Only 4 combos tested; no segmentation |
| E8 | Backbone robustness | ViT-B on MCC C→S | ECE, NLL, BS | PseudoCal best across metrics | C2 (backbone-agnostic) | Single task, single backbone variant |
| E9 | Compatibility with post-hoc methods | MatrixScal, VectorScal, TempScal | ECE | TempScal best pairing with PseudoCal | C2 (framework flexibility) | Not central to main claim |

### Research-Theme Gap Diagnosis

**Gap 1 — Statistical reliability**: None of the experiments report variance or significance. This is the single weakest pillar of the empirical contribution. Without it, the central claim of "consistently and significantly outperforming" is not verifiable.

**Gap 2 — Causal isolation**: The ablation study (Table 9) convincingly shows that inference-stage mixup is the right design choice. However, it does not isolate whether the improvement comes from the inference stage or the specific λ value (0.65), since training-stage mixup baselines use standard Beta(0.3,0.3) ratios.

**Gap 3 — Failure mode analysis**: The paper identifies one limitation (small target samples) in the limitations section but does not analyze when/why the method fails. The GTA5 segmentation result is the clearest example — it is not discussed as a failure case.

### Proposed Research Experiments (P0/P1/P2)

**P0 Experiment: Variance and Significance Analysis**
- Target Claim: C3 (comprehensive evaluation demonstrates superior performance)
- Hypothesis: PseudoCal's ECE improvements are statistically significant vs. top-2 baselines.
- Minimal Design: Compute std across 5 seeds for all entries in Tables 2-7. Run paired Wilcoxon signed-rank test across all task-method pairs (N > 30).
- Controls/Baselines: TempScal-src, TransCal, Ensemble
- Metrics: Mean ECE ± std, p-value, Cohen's d effect size
- Success Criterion: p < 0.05 for the majority of benchmarks; effect size > 0.3.
- Estimated Cost/Time: Low (compute from existing seeds).
- Expected Gain: Allows unambiguous interpretation of reported improvements.

**P1 Experiment: Train-stage mixup with λ=0.65 control**
- Target Claim: C2 (inference-stage mixup is key design choice)
- Hypothesis: Training-stage mixup with λ=0.65 + TempScal-src yields higher ECE than PseudoCal.
- Minimal Design: Train UDA models with mixup λ=0.65, then calibrate on source. Compare to PseudoCal.
- Controls: Standard training-stage mixup (Beta(0.3,0.3)), PseudoCal
- Metrics: ECE
- Success Criterion: PseudoCal achieves lower ECE than both training-stage variants.
- Estimated Cost/Time: Medium (requires retraining UDA models).
- Expected Gain: Cleaner causal isolation of inference-stage advantage.

**P2 Experiment: Extended λ sensitivity**
- Target Claim: C2 (λ=0.65 works universally)
- Hypothesis: λ=0.65 is near-optimal for source-free (SHOT) and segmentation settings.
- Minimal Design: Sweep λ ∈ {0.51, 0.6, 0.65, 0.7, 0.8, 0.9} for SHOT on DomainNet and GTA5→Cityscapes.
- Controls: No-calibration baseline, Oracle
- Metrics: ECE
- Success Criterion: λ=0.65 yields ECE within 10% of optimal for each setting.
- Estimated Cost/Time: Low (inference-only).
- Expected Gain: Strengthens universality claim or reveals setting-dependent optimal λ.

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2)

Stage 1 (P0 — Before Resubmission):
    [Existing 5-run results] → Add ±std → Add significance test (paired Wilcoxon)
    Expected gain: Statistical reliability for all empirical claims

Stage 2 (P1 — Recommended):
    [Table 9 ablation] → Add training-stage λ=0.65 row
    Expected gain: Clean causal isolation of inference-stage advantage

Stage 3 (P2 — Nice-to-have):
    [Figure 3 sensitivity] → Extend to SHOT + segmentation
    Expected gain: Validate λ=0.65 universality or reveal boundary conditions
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Evidence-based rationale**: The paper has a genuinely novel conceptual reframing (target-domain unsupervised perspective for UDA calibration) that leads to a simple, elegant, and broadly applicable method. The empirical breadth is impressive (10 UDA methods, 5 scenarios). However, the score is constrained by several significant weaknesses:

- **Statistical reliability is not established** (no variance/significance, despite 5 runs). This is a fundamental gap when claiming "consistently and significantly outperforms."
- **Theoretical motivation has gaps** (Eq 2 overlooks confidence distributions and Dc/Dw circularity).
- **Language overclaims** ("guarantees") that, while fixable, indicate lack of defensive writing.
- **Failure cases underreported** (GTA5 segmentation).
- **Novelty can only be partially assessed** due to the absence of external literature comparison in this run.

These concerns are fixable, but as presented, the strength of evidence does not fully match the strength of claims.

**Post-Revision Target**: [7.0, 8.0] / 10

**Conditions for achieving 7.0+**: 
1. (Must) Add variance reporting and significance tests to all experimental results.
2. (Must) Fix overclaiming language and acknowledge the factorization gap.
3. (Must) Discuss the GTA5 segmentation failure and bound claims accordingly.
4. (Nice-to-have) Add the training-stage λ=0.65 control to the ablation.