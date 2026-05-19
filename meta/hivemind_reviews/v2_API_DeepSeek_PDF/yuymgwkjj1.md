## Summary
# Final Review Report

## Summary

This paper addresses the known complexity-likelihood bias in normalizing flows for out-of-distribution (OOD) detection. The authors propose a training-time correction method by introducing synthetic low-complexity outliers (via CutPaste/CutMix/MixUp augmentation + Gaussian blur for images, sentence truncation + synonym replacement for text) and a softplus-based adverse likelihood objective that penalizes high likelihood on OOD samples while preserving it on ID samples. The method is evaluated on benchmark image datasets (CIFAR-10/100, SVHN, LSUN, iSUN, CelebA), high-dimensional real-world datasets (Chest X-ray, RealBlur, KonIQ-10k), and text datasets (IMDb, Movie Reviews, AG News, SST-2, WikiText-2). The central claim is that synthetic outlier training corrects the bias and achieves performance comparable to using limited real outliers, while also increasing the local Lipschitz constant consistent with prior theoretical analysis.

**Core strengths:** (1) The problem is well-motivated — the complexity-likelihood bias is a known failure mode of normalizing flows, and training-time correction is a legitimate research direction. (2) The method is simple and practical, combining standard augmentations with a softplus loss that avoids manual thresholding. (3) The evaluation spans multiple modalities (images, text, medical, blur) and uses both AUROC and FPR95 metrics.

**Core weaknesses:** (1) Inconsistent empirical performance — on several OOD settings (e.g., CIFAR-10→CelebA), the method shows no improvement or degrades performance, but the paper's narrative claims universal "significant outperformance." (2) The Lipschitz constant analysis, presented as a core contribution, uses a flawed estimation method (max gradient norm over 1000 samples is not the true Lipschitz constant) and the claimed theoretical support is correlational rather than causal. (3) The loss formulation (Ltotal = LID + LOOD) lacks explicit batched formulation and balancing mechanism details. (4) The blurred-CIFAR10 appendix experiment is poorly designed for supporting the main claim. (5) The paper overclaims novelty of "synthetic outlier perspective" given the existence of SANFlow (Kim et al., 2023) which also uses synthetic outliers with normalizing flows.

**Verdict:** The paper presents a reasonable engineering contribution to a well-known problem, but the evaluation overstates results, and the theoretical framing via the Lipschitz constant is not rigorously supported. Major revisions in claim-bounding, experimental rigor, and experimental design are needed before acceptance.

## Strengths
**S1. Well-motivated problem.** The complexity-likelihood bias in normalizing flows is a well-documented failure mode (Serra et al. 2020, Osada et al. 2024), and the paper's goal of correcting this bias during training (rather than post-hoc scoring) is a legitimate and practically relevant direction.

**S2. Simple and practical synthetic outlier pipeline.** The image outlier generation combining standard augmentations (CutPaste, CutMix, MixUp) with Gaussian blur is straightforward to implement and computationally inexpensive. The text outlier pipeline using sentence truncation and WordNet synonym replacement is similarly simple.

**S3. Softplus-based OOD objective avoids manual thresholding.** Compared to prior work (Schmier et al. 2022) that requires a manually set threshold to clamp OOD loss, the softplus formulation provides a smooth, automatically bounded loss surface. This is a clean technical improvement.

**S4. Multi-modal evaluation.** The paper evaluates on both image and text datasets, including high-dimensional real-world data (Chest X-ray, RealBlur, KonIQ-10k) and MVTecAD, which broadens the scope beyond standard benchmarks.

**S5. Ablation study on blur radius.** Appendix E provides useful insight into the sensitivity of the method to the blur parameter, showing that moderate blurring yields optimal performance. This type of analysis is informative for practitioners.

**S6. Motivation-based connection to Lipschitz theory.** The attempt to connect empirical results to the theoretical framework of Osada et al. (2024) through the local Lipschitz constant is conceptually interesting, even if the execution has flaws (noted in Weaknesses).

## Weaknesses
**W1. Claim-evidence mismatch in empirical results (Critical).** The paper claims "significantly outperforms methods trained solely on ID data" but several OOD settings show no improvement or degradation. For CIFAR-10→CelebA, CCM+Gaussian achieves AUROC 76.1 vs MLE's 76.4 (Table 2). For CIFAR-100→CelebA, the full method (CCM+Gaussian) at 65.1 is worse than Gaussian-only at 71.1, suggesting the CCM augmentation hurts performance on this setting. No confidence intervals or standard deviations are reported, making statistical significance unverifiable.

**W2. Lipschitz constant estimation is methodologically flawed (Critical).** The paper estimates LA as max_i ||∇f(x_i)|| over 1000 random samples. This is not the true Lipschitz constant (which requires supremum over all input pairs). The estimate is a sample-based lower bound at best. Moreover, Hypothesis 1 refers to Lipschitz on latent subset A, but the gradient is computed in input space. The observed increase in gradient norm does not necessarily correspond to the LA referenced in the theory. The causal claim ("supports the hypothesis") conflates correlation with causation.

**W3. Missing explicit batched loss formulation (Major).** Ltotal = LID + LOOD is stated but not formulated per-batch. Since LID applies to ID samples and LOOD to OOD samples, the effective loss ratio depends on the mini-batch composition controlled by outlier sampling probability (p=0.5). The paper claims this is preferable to loss weighting but provides no ablation comparing the two approaches.

**W4. Overclaimed novelty of "synthetic outlier + normalizing flows" (Major).** SANFlow (Kim et al., 2023, NeurIPS) already incorporates synthetic outliers to train normalizing flows across multiple distributions. The paper cites SANFlow in the Introduction but does not clearly differentiate its contribution from SANFlow's. The Lipschitz-constant connection is potentially novel, but the fundamental idea of using synthetic outliers to regularize normalizing flow likelihoods is not.

**W5. Introduction structure lacks narrative clarity (Major).** The Introduction reads as a literature survey rather than a focused argument building toward the specific gap. The fourth paragraph (related work on outlier methods) reads like a Related Work section. The fifth paragraph states contributions but mixes grammatical errors ("Specially" for "Specifically", "Furtheremore", subject-verb disagreement) that reduce credibility.

**W6. Blurred CIFAR10 experiment is poorly designed (Major).** Appendix D tests blurred CIFAR10 (simple) as ID against unblurred CIFAR10 (complex) as OOD. This setting (ID simpler than OOD) is precisely where normalizing flows already work well without correction. The experiment does not test the method's intended use case.

**W7. Text outlier synthesis produces unnatural text (Minor).** The synonym replacement approach produces grammatically incorrect outputs ("The dwarf in this movie be screaming!!", "a incubus") that do not represent natural low-complexity text. The complexity gap between original and synthetic text (Table 9: 2.63 vs 3.21) is small relative to image gaps, which may explain limited text improvements.

**W8. No statistical significance testing (Minor).** No results are reported with standard deviations or confidence intervals. Given the small performance gaps on some settings, multi-seed experiments with significance tests are necessary to establish reliability.

**W9. Conclusion lacks limitations (Minor).** The Conclusion does not acknowledge settings where the method performed poorly (CelebA) or the correlational nature of the Lipschitz analysis. A limitations paragraph is needed.

## Key Issues
### Issue 1: Claim-evidence gap in empirical results (Critical)
The narrative claims universal improvement, but the data shows inconsistent results. On CIFAR-10→CelebA, the full method achieves AUROC 76.1 vs MLE 76.4 — essentially no improvement. On CIFAR-100→CelebA, CCM+Gaussian (65.1) underperforms Gaussian-only (71.1). These failure cases are not acknowledged in the Abstract, Conclusion, or result discussion. **Impact:** Overclaiming reduces scientific credibility and misleads readers about the method's scope.

### Issue 2: Flawed Lipschitz constant estimation (Critical)
LA is estimated as max gradient norm over 1000 samples, which is not the Lipschitz constant. The true Lipschitz constant requires the supremum of ||f(x)-f(y)||/||x-y|| over all pairs. What is measured is a sample-based lower bound on the maximum gradient norm. Moreover, the computation is in input space while Hypothesis 1 references the latent subset A. The claimed theoretical validation is therefore unsupported. **Impact:** A central paper contribution (Lipschitz analysis) is methodologically unsound.

### Issue 3: Loss formulation lacks batched specification (Major)
Ltotal = LID + LOOD is presented as a per-sample loss, but LID and LOOD apply to different samples. The per-batch loss is L_batch = (1/|B_ID|)*sum LID(x) + (1/|B_OOD|)*sum LOOD(x'), where |B_OOD| is controlled by a sampling probability. Without explicit formulation, the balancing mechanism is unclear and unreproducible. **Impact:** Reproducibility risk.

### Issue 4: Inadequate differentiation from SANFlow (Major)
SANFlow (Kim et al., 2023) also uses synthetic outliers with normalizing flows for anomaly detection. The paper cites it but does not clearly articulate what is new beyond SANFlow. The Lipschitz connection is the best differentiator, but it is insufficiently supported. **Impact:** Novelty perception risk.

### Issue 5: Weak experimental design in Appendix D (Major)
The blurred CIFAR10 experiment tests the setting where ID is simpler than OOD, which is already easy for normalizing flows. This does not test the method's claimed strength. **Impact:** Waste of experimental space; does not support the core claim.

## Actionable Suggestions
### Suggestion A (Must): Bound claims and acknowledge negative results
**Problem:** Abstract, Introduction, and Conclusion claim "significant outperformance" without acknowledging failure cases.
**Action:** Revise the Abstract to include a bounded claim, e.g., "Our method improves OOD detection on several benchmarks where ID data is more complex than OOD data, though gains vary across settings." Add a limitations paragraph to the Conclusion explicitly mentioning: (1) minimal improvement on CelebA, (2) sensitivity to blur parameters, (3) CCM augmentation sometimes hurts performance.

### Suggestion B (Must): Fix Lipschitz constant estimation and interpretation
**Problem:** The LA estimation is methodologically incorrect.
**Action:** (1) Rename the metric to "estimated gradient norm upper bound" rather than "Lipschitz constant." (2) Add a theoretical justification connecting input-space gradient norms to the local Lipschitz constant on the latent subset A. (3) Report the Lipschitz constant using a certified method (e.g., spectral norm of weight matrices for ReLU networks). (4) Rephrase causal claims: "Our results are consistent with the hypothesis that synthetic outlier training increases model sensitivity to low-complexity inputs, measured via gradient norms."

### Suggestion C (Must): Report statistical reliability
**Problem:** No variance or significance testing reported.
**Action:** Run all main experiments (Tables 2, 3, 5, 6) over at least 3 random seeds. Report mean ± std for AUROC and FPR95. Add a paired significance test (e.g., Wilcoxon signed-rank) comparing CCM+Gaussian vs MLE on the most competitive OOD benchmarks.

### Suggestion D (Must): Clarify loss formulation and balancing
**Problem:** Ltotal = LID + LOOD is underspecified.
**Action:** Add an explicit batched loss formulation:
$$L_{\text{batch}} = \frac{1}{|B_{\text{ID}}|} \sum_{x \in B_{\text{ID}}} -\log p_X(x) + \frac{1}{|B_{\text{OOD}}|} \sum_{x' \in B_{\text{OOD}}} \log(1 + p_X(x'))$$
where $B_{\text{OOD}}$ is determined by outlier probability $p_{\text{out}}$. Report $p_{\text{out}}$ for all experiments (image and text). Add an ablation comparing this sampling-ratio approach against explicit loss weighting.

### Suggestion E (Must): Differentiate from SANFlow
**Problem:** The contribution relative to SANFlow is unclear.
**Action:** Add a dedicated paragraph or table comparing with SANFlow along dimensions: (1) outlier generation method, (2) loss function, (3) whether complexity bias is explicitly addressed, (4) evaluation on the same benchmarks (MVTec, CIFAR, etc.). Explicitly state what the current paper adds beyond SANFlow.

### Suggestion F (Nice-to-have): Redesign blurred CIFAR10 experiment
**Action:** Replace Appendix D with an experiment where CIFAR-10 is used as complex ID, and synthetic outliers are *blurred versions of OOD datasets* (SVHN, LSUN). Test whether blur-based synthesis helps most where it is needed (complex ID → simple OOD).

### Suggestion G (Nice-to-have): Improve text outlier quality
**Action:** Instead of first-synonym WordNet replacement, use a more controlled simplification system (e.g., linguistic simplification rules or a learned paraphraser) to produce grammatically valid but lexically simpler text.

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis

The current Introduction has the following paragraph structure:
- **P1** (Page 1, lines 81-88): Generic OOD importance, does not connect to normalizing flow bias.
- **P2** (Page 1, lines 89-99): General survey of normalizing flows, reads like a shallow literature list.
- **P3** (Page 2, lines 56-61): Prior findings on likelihood bias, but does not synthesize into an open gap.
- **P4** (Page 2, lines 62-73): Related-work on outlier methods (reads like a Related Work section).
- **P5** (Page 2, lines 74-90): Contribution summary with grammatical errors.

**Key problems:** (a) No clear "gap" statement between P3 and the proposed solution. (b) P4 interrupts the flow between problem statement and solution. (c) The three alignment checks fail: the Introduction does not clearly map core concepts to method variables.

### Recommended Storyline: "Problem-Defined Solution"

This storyline keeps the paper's technical content but reorganizes for logical flow.

**Paragraph 1 (Motivation):** State the specific problem: normalizing flows assign misleadingly high likelihood to low-complexity OOD data. Give a concrete example from Table 1. This immediately establishes stakes.

**Paragraph 2 (Prior attempts and their limits):** Describe attempts to mitigate this bias: complexity-adjusted scoring (Serra 2020) and theoretical analysis (Osada 2024). These work at test time but do not correct the model during training.

**Paragraph 3 (Proposed solution intuition):** We propose to correct the bias at training time by exposing the model to synthetic low-complexity outliers, teaching it to assign lower likelihood to such inputs automatically. Briefly describe the generation method (augmentation + blur), the softplus objective, and the connection to Lipschitz theory.

**Paragraph 4 (Contributions):** Clearly list 3 contributions with scoped claims.

### Abstract Outline (5 sentences)

**S1 (Problem):** Normalizing flows for OOD detection are systematically biased: they assign higher likelihoods to low-complexity inputs, undermining detection when ID data is complex and OOD data is simple.

**S2 (Gap):** Existing corrections operate at test time (complexity-adjusted scoring) but do not address the bias during training.

**S3 (Proposed method):** We introduce synthetic low-complexity outliers during training with a softplus-based adverse likelihood objective that penalizes high likelihood on OOD samples while preserving ID likelihood.

**S4 (Evidence):** On several benchmarks (CIFAR→SVHN, iSUN→CIFAR, real-world datasets), our method improves AUROC over maximum-likelihood training, approaching models trained with limited real outliers.

**S5 (Bounded claim + limitation):** Gains are most consistent when ID data is more complex than OOD data; performance varies otherwise. We also observe increased gradient norms consistent with the theoretical framework linking complexity to flow sensitivity.

### Introduction Outline (4 paragraphs)

**P1 — Territory + Problem** (150 words)
Role: Define OOD detection with normalizing flows. State the complexity-likelihood bias.
Transition: "However, this bias is only corrected at test time by existing methods."
Evidence anchor: Table 1 (CIFAR-10→SVHN: 44.3 AUROC baseline).

**P2 — Gap** (120 words)
Role: Explain why test-time correction is insufficient. The bias is inherent to the training procedure.
Transition: "In this paper, we propose to correct the bias at its source — during training."
Evidence anchor: Cite Serra et al. 2020, Osada et al. 2024.

**P3 — Solution** (180 words)
Role: Intuition of synthetic outlier training + softplus objective. Brief method summary.
Transition: "We validate this approach through extensive experiments."
Evidence anchor: Eq. (2)-(3), Figure 2 (toy example).

**P4 — Contributions + Roadmap** (100 words)
Role: List 3 bounded contributions. Section roadmap.
Transition: "The remainder of this paper is organized as follows..."
Evidence anchor: None needed.

### Title Suggestion

Current: "CORRECTING THE BIAS OF NORMALIZING FLOWS BY SYNTHETIC OUTLIERS FOR IMPROVING OUT-OF-DISTRIBUTION DETECTION"

Improved: "Training-Time Bias Correction for Normalizing Flows in OOD Detection via Synthetic Low-Complexity Outliers"

This title is more scannable and specifies "low-complexity" (the key design principle) and "training-time" (the differentiator from existing test-time methods).

## Priority Revision Plan
### Ranked Error Board

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence | Effort |
|------|-------|----------|---------------|------------|------------|--------|
| 1 | Claim-evidence mismatch in empirical results | Critical | High | Easy | High | Low |
| 2 | Lipschitz constant estimation flawed | Critical | High | Moderate | High | Medium |
| 3 | Missing statistical significance testing | Major | Medium | Easy | High | Low |
| 4 | Loss formulation underspecified | Major | Medium | Easy | High | Low |
| 5 | Inadequate differentiation from SANFlow | Major | Medium | Moderate | Medium | Medium |
| 6 | Blurred CIFAR10 experiment design | Major | Low | Easy | High | Low |
| 7 | Introduction narrative clarity | Major | Low | Moderate | High | Low |
| 8 | Text outlier quality | Minor | Low | Moderate | Medium | Medium |
| 9 | Conclusion lacks limitations | Minor | Low | Easy | High | Low |

### Revision Order (P0 → P1 → P2)

**P0 (Submission-critical, before next submission):**
1. Fix claim-evidence mismatch: rewrite Abstract, Conclusion, and result discussion to bound claims. Add a limitations paragraph.
2. Fix Lipschitz constant estimation: rename metric, add theoretical justification, or replace with spectral-norm-based estimate.
3. Add statistical significance: run 3 seeds, report mean ± std, add significance tests.
4. Clarify loss formulation with explicit batched equation and outlier probabilities.

**P1 (High-priority improvement):**
5. Add SANFlow comparison table differentiating contribution.
6. Redesign blurred CIFAR10 experiment to test the hard case.
7. Rewrite Introduction following the recommended storyline.

**P2 (Quality-of-life):**
8. Improve text outlier quality with better simplification method.
9. Add limitations to Conclusion.

### Expected Impact After P0 Revisions

- **Validity:** The paper becomes defensible — claims match evidence, statistics support conclusions.
- **Novelty:** Better differentiated from SANFlow, though still partially overlapping.
- **Reproducibility:** Loss formulation and hyperparameters are fully specified.
- **Score improvement:** From current ~4.5/10 to a post-revision target of 6.0-7.0/10.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Benchmark image OOD (Table 2) | CIFAR-10/100 as ID, SVHN/LSUN/iSUN/CelebA as OOD | AUROC, FPR95 | CCM+Gaussian improves over MLE on most settings | C1 (synthetic outlier bias correction) | No variance; failure on CelebA not discussed |
| E2 | Benchmark image OOD with iSUN as ID (Table 3) | iSUN as ID, 5 OOD datasets | AUROC, FPR95 | Gains on SVHN, LSUN, CelebA; mixed on CIFAR-10/100 | C1 | Complex ID setting only partially tested |
| E3 | Lipschitz constant measurement (Table 4) | CIFAR-10/100, iSUN | LA estimate (max gradient norm) | 7x increase on CIFAR-10 | C3 (Lipschitz enhancement) | Flawed estimation method |
| E4 | High-dimensional real-world (Table 5) | Chest X-ray, RealBlur, KonIQ-10k | AUROC | CS-Flow and FastFlow improved with synthetic outliers | C1, C2 | CCM degrades FastFlow on Chest X-ray |
| E5 | MVTecAD anomaly detection (Table 10) | MVTecAD categories | AUROC | CCM+Gaussian improves mean from 98.6→98.7 (FastFlow) and 98.7→99.2 (CS-Flow) | C1 | Gains are marginal (+0.1 to +0.5) |
| E6 | Text OOD detection (Table 6) | IMDb as ID, 4 OOD datasets | AUROC, AUPR | Large gain on SST-2 (+35.1), small gain on Wiki (+1.8) | C1 | Text synthesis quality issues |
| E7 | Blurred CIFAR10 as ID (Table 11) | Blurred CIFAR-10 as ID, unblurred/SVHN/LSUN as OOD | AUROC, AUPR | Modest gains (SVHN +3.0, LSUN +8.9) | C1 | Poor design: tests easy setting |
| E8 | Blur ablation (Figure 6) | CIFAR-10/100 as ID, SVHN as OOD | AUROC | Moderate blur gives optimal results | C1 | Only tested on one OOD pair |

### Research-Theme Gap Diagnosis

**Gap 1 — Causal separation is not established:** The paper claims synthetic outlier training "corrects the bias" and "increases LA," but does not establish that the LA increase *causes* bias correction. This is a correlational claim.

**Gap 2 — Statistical reliability is unknown:** None of the experiments report variance. Given that some gains are small (e.g., MVTecAD mean +0.1 for FastFlow), the results may not be statistically significant.

**Gap 3 — No test for the most challenging setting:** The method is designed for complex-ID + simple-OOD, but the most controlled test (blurred CIFAR-10) tests the easy case. A direct test is missing.

**Gap 4 — Ablation of CCM components:** The paper uses CutPaste, CutMix, and MixUp randomly but does not ablate their individual contributions. It is unclear which augmentation is most responsible for gains.

### Proposed Research Experiments

#### Experiment P0 (Must): Multi-seed replication with statistical reporting
- **Target Claim:** C1 (synthetic outlier correction improves OOD detection)
- **Hypothesis:** Improvements over MLE are statistically significant
- **Minimal Design:** Run Tables 2 and 3 with 5 random seeds each
- **Controls/Baselines:** Same hyperparameters across seeds
- **Metrics:** Mean ± std AUROC, FPR95; paired Wilcoxon test vs MLE
- **Success Criterion:** p < 0.05 on at least 3 of 4 OOD settings for each ID dataset
- **Estimated Cost:** ~50 GPU-hours
- **Expected Paper-Quality Gain:** High — establishes statistical reliability

#### Experiment P1 (Should): Causal Lipschitz verification
- **Target Claim:** C3 (Lipschitz enhancement supports bias correction)
- **Hypothesis:** Certified Lipschitz bound (via spectral norm) correlates with OOD detection improvement
- **Minimal Design:** Compute spectral upper bound on Lipschitz constant of each coupling layer; compare LA_with vs LA_without for each model
- **Controls/Baselines:** Same architecture, training setup
- **Metrics:** Spectral Lipschitz bound, correlation with AUROC gain
- **Success Criterion:** Positive rank correlation between Lipschitz increase and AUROC gain
- **Estimated Cost:** Minimal (adds ~1 line of code per layer)
- **Expected Paper-Quality Gain:** High — converts correlational claim to falsifiable evidence

#### Experiment P2 (Should): Ablation of CCM components
- **Target Claim:** C1 (outlier generation method is effective)
- **Hypothesis:** Individual augmentations have different contributions
- **Minimal Design:** Compare CutPaste-only, CutMix-only, MixUp-only, and combinations on CIFAR-10 → SVHN
- **Controls/Baselines:** Same blur radius, same training budget
- **Metrics:** AUROC, FPR95
- **Success Criterion:** Identifies which augmentation drives gains
- **Estimated Cost:** ~20 GPU-hours
- **Expected Paper-Quality Gain:** Medium — improves understanding and practical guidance

#### ASCII Diagram — Experiment Upgrade Plan
```text
P0 (critical, before resubmission):
  [no variance reported] -> [5-seed replication + Wilcoxon test]
  -> [statistical reliability established]

P1 (high priority):
  [Lipschitz: max gradient norm] -> [spectral bound per layer]
  -> [causal correlation test]
  [CCM combined] -> [individual augmentation ablation]
  -> [identify key component]

P2 (nice-to-have):
  [blurred CIFAR experiment] -> [redesign for hard case]
  [text synthesis quality] -> [linguistic simplification system]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score (evidence-grounded, emphasizing novelty + research value):** 4.5 / 10

**Rationale:**
- **Research value (5/10):** The problem is well-motivated but the contribution is incremental. Synthetic outlier generation via standard augmentations + Gaussian blur is practical but not conceptually novel. The softplus objective is a clean engineering improvement but does not open a new research direction.
- **Novelty (4/10):** SANFlow (Kim et al., 2023) already uses synthetic outliers with normalizing flows. The Lipschitz connection is the most novel element but is methodologically flawed in its current form. Without rigorous validation, the novelty claim is weak.
- **Validity/Soundness (4/10):** The Lipschitz estimation is incorrect. Claim-evidence mismatch across multiple experiments (CelebA failure, CCM degradation). No statistical significance testing. These are fixable but currently reduce confidence.
- **Reproducibility (5/10):** The FrEIA-based implementation is reproducible in principle, but the batched loss formulation is underspecified, outlier probabilities are not reported for all experiments, and no code is provided.

**Post-Revision Target:** [6.0, 7.0] / 10

**Conditions for reaching target:**
- [ ] All P0 items completed: bounded claims, fixed Lipschitz estimation, statistical significance testing, clarified loss formulation.
- [ ] SANFlow comparison table added.
- [ ] Introduction rewritten for narrative clarity.
- [ ] Limitations explicitly discussed.
- [ ] At least one causal experiment linking Lipschitz increase to bias correction.

### Page Coverage Audit

| Page | Section | Annotation Count | Coverage Status | Skip Reason |
|------|---------|-----------------|-----------------|-------------|
| 1 | Title/Abstract/P1 Intro | 3 | Covered | - |
| 2 | Intro P3-P5, Related Work | 2 | Covered | - |
| 3 | Hypothesis, Motivation, Table 1 | 1 | Covered | - |
| 4 | Image/Text Outlier Synthesis | 2 | Covered | - |
| 5 | Learning Objective (Eq 2-3) | 1 | Covered | - |
| 6 | Loss balancing, OOD Scoring | 1 | Covered | - |
| 7 | Experiment Setup, Results discussion | 1 | Covered | - |
| 8-9 | Tables 2-4, Lipschitz est., High-dim datasets | 2 | Covered | - |
| 10 | Text datasets, Conclusion | 1 | Covered | - |
| 11-15 | References and Appendix (text) | 0 | Skipped | References only; appendix figures/tables are referenced via annotations on page 16 |
| 16 | Appendix C-D (MVTec, Blurred CIFAR) | 1 | Covered | - |
| 17-19 | Appendix E-F (Ablation, Synthetic samples) | 0 | Skipped | Visual results only; no substantive claims requiring annotation |

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Core Claim: Synthetic outlier training corrects complexity-likelihood bias in NF]
    |
    ├── C1: Synthetic outlier generation (C1)  
    │   ├── Evidence: Tables 2, 3, 5, 6 (AUROC/FPR95 gains)
    │   ├── Gap: Gains inconsistent (CelebA fails, CCM degrades)
    │   └── Risk: Overclaimed as universal improvement
    |
    ├── C2: Softplus loss objective (C2)
    │   ├── Evidence: Figure 1, Eq (3), Toy example Figure 2
    │   ├── Gap: No ablation vs weighted loss or manual threshold
    │   └── Risk: Incremental over Schmier et al. threshold
    |
    └── C3: Lipschitz constant increase (C3)
        ├── Evidence: Table 4 (7x increase in gradient norm)
        ├── Gap: Estimation is not true Lipschitz constant
        └── Risk: Correlational, not causal; not properly verified
```

### ASCII Diagram — Revision Strategy Roadmap

```text
[Current] -> [P0 Fixes] -> [P1 Fixes] -> [Target]
    |            |               |
    | Overclaimed results       | Differentiate from SANFlow
    | Flawed Lipschitz est.     | Redesign blur experiment
    | No variance reported      | Rewrite Introduction
    | Vague loss formulation    |
    v                            v
[Weak paper (4.5/10)] -> [Defensible (5.5/10)]
                               -> [Competent (6.0-7.0/10)]
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
OOD Detection for Normalizing Flows
├── Branch 1: Likelihood-based methods
│   ├── Leaf 1.1: Direct likelihood scoring [Nalisnick 2019]
│   └── Leaf 1.2: Likelihood ratio methods [Ren 2019]
├── Branch 2: Complexity-adjusted approaches
│   ├── Leaf 2.1: Input complexity scoring [Serra 2020]
│   └── Leaf 2.2: Theoretical complexity analysis [Osada 2024]
├── Branch 3: Outlier-based regularization
│   ├── Leaf 3.1: Real outlier exposure [Hendrycks 2018]
│   ├── Leaf 3.2: Virtual/synthetic outlier synthesis [Du 2022, SANFlow 2023]
│   └── Leaf 3.3: Distributional OOD sets [Wang 2023, Zheng 2023]
└── Branch 4: THIS PAPER — Training-time bias correction
    ├── Core: Synthetic low-complexity outliers + softplus objective
    ├── Novelty: Lipschitz-regularization perspective (partially supported)
    └── Overlap: Leaf 3.2 (SANFlow) shares synthetic outlier + NF approach
```