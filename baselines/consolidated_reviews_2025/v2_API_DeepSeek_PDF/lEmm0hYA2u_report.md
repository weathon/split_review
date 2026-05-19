## Summary
This paper proposes **ZeroP**, a zero-shot quantization (ZSQ) framework that introduces publicly available **proxy data (PD)** as a direct input alongside synthetic data (SD) for fine-tuning quantized networks — departing from prior work that used PD only to guide SD generation. The authors conduct an extensive empirical study across **16 candidate PD datasets, 6 network architectures, and 3 benchmarks (CIFAR-10/100, ImageNet-1K)**. They also propose a lightweight **batch-normalization statistics (BNS) distance metric** for selecting effective PDs without exhaustive trial.

**Key Results:** At 4-bit quantization on ImageNet-1K, ZeroP+PD outperforms the best pure-SD methods by 0.84%–16.07% across architectures (ResNet-18, ResNet-50, MobileNetV1/V2, RegNet-600MF). For example, MobileNetV1 improves from 43.31% (SD-only) to 59.38% (+16.07%) using COCO as PD. The BNS distance shows Spearman rank correlations of 0.6–0.9 with downstream accuracy across architectures.

**Core Contributions (C1–C3):**
- **C1:** First systematic study of direct PD incorporation in ZSQ, challenging the SD-only paradigm.
- **C2:** BNS-distance-based PD selection method that is simple, cheap, and reasonably predictive.
- **C3:** Consistent empirical gains across diverse settings, with ZeroP achieving near-OD-method performance.

**Primary Weaknesses:** (1) No variance/statistical significance reporting; (2) BNS selection reliability is architecture-dependent and has known counterexamples; (3) Overclaim wording (e.g., "consistently outperforms all SOTA"); (4) No sensitivity analysis for key hyperparameters (mixing ratio λ, BNS sample count M); (5) Related Work is a flat list lacking structured comparison; (6) Novelty verification is deferred due to external-retrieval unavailability in this run.

## Strengths
1. **Practical motivation with broad applicability:** The paper addresses a real-world problem — the unavailability of original training data due to privacy/cost constraints — which affects many deployment scenarios. The proposed solution (using publicly available proxy data) is intuitive, easy to implement, and does not require changes to existing ZSQ pipelines.

2. **Extensive empirical characterization:** The evaluation across 16 candidate PD datasets is unusually comprehensive. This systematic sweep provides useful insights into which types of proxy data help (e.g., COCO, PASCAL VOC, DIV2K with small BNS distance) and which hurt (e.g., SVHN, MNIST with large BNS distance). The BNS distance correlation analysis (Fig. 4) is a practical contribution for practitioners.

3. **Plug-and-play compatibility:** ZeroP's data mixing strategy (Eq. 6) requires minimal modification to existing ZSQ methods. The ablation study (Table 3) shows consistent gains when PD is added to GDFQ, Qimera, IntraQ, and the authors' own baseline — demonstrating generalizability.

4. **Transparent limitations:** The authors explicitly discuss three limitations (PD availability, CNN-only evaluation, BN dependence), which is a good scientific practice and helps bound the scope of claims.

5. **Strong gains on difficult settings:** The 16.07% improvement on MobileNetV1 (4-bit) is particularly notable because MobileNetV1 is known to be challenging for quantization due to its depthwise separable convolutions and lack of residual connections.

## Weaknesses
### W1. Missing statistical rigor (Severity: High)
All results (Tables 1–3, Figure 3–4) are reported as single-point accuracy estimates without standard deviation, confidence intervals, or significance tests. Given that several improvements are small (0.15%–1.0%), readers cannot assess whether these gains are statistically reliable. This is the most impactful weakness because it undermines the core empirical claims.

### W2. Overclaiming and imprecise wording (Severity: High)
The paper states ZeroP "consistently outperforms all solely SD SOTA methods" (Page 8 — Performance Comparison), but Table 2 shows AIT achieves 71.96% vs ZeroP's 71.71% on MobileNetV2 5-bit — a direct counterexample. The phrase "new SOTA performance level" (Page 3 — Contributions) is also imprecise without specifying the comparison scope (architecture, bit-width, dataset).

### W3. BNS selection reliability is bounded (Severity: Medium-High)
The BNS distance metric shows strong correlation with accuracy (Spearman ρ ~0.6–0.9), but has known failures: CIFAR10 (BNS=82.14) outperforms Random Noise (BNS=78.09) despite having a larger distance. The paper notes this but does not analyze why. Additionally, the correlation varies substantially across architectures (ResNet-18 ~0.5 vs RegNet-600MF ~0.9 in 5-bit setting, per Fig. 4), limiting the metric's generalizability.

### W4. No sensitivity analysis for key hyperparameters (Severity: Medium)
Two critical hyperparameters — mixing ratio λ (Eq. 6) and BNS sample count M (Eq. 5) — are fixed at λ=0.5 and M=1024 without any sensitivity study. The λ selection could significantly impact results depending on PD quality, and the BNS distance estimate's stability with M=1024 is not validated.

### W5. Related Work lacks structured comparison (Severity: Medium)
Section 5 is a single chronological paragraph listing data-free KD and MS methods without organizing them by methodological axes. There is no explicit positioning of ZeroP against the strongest prior PD-using methods (KnockoffNet, DeGANs), and no comparison table summarizing task/PD-role/number-of-PDs-tested differences.

### W6. Technical depth of method contribution is limited (Severity: Medium)
The core methodological novelty is straightforward — mixing PD with SD in the input batch (Eq. 6) and using BNS distance for selection (Eq. 5). While the empirical characterization is extensive, the technical contribution is relatively shallow compared to papers that develop new SD generation techniques.

### W7. Conclusion and limitations lack forward-looking guidance (Severity: Low-Medium)
The Limitations section lists unresolved issues without suggesting mitigation paths. The Conclusion paragraph is too brief and introduces the claim "challenge the notion that relying solely on SD is necessary" without boundary conditions, but does not cover next steps or actionable future work.

### W8. Variance across architectures not analyzed (Severity: Low)
The gains vary dramatically across architectures — from 0.84% (ResNet-18) to 16.07% (MobileNetV1). The paper does not analyze why certain architectures benefit more from PD. This diagnostic gap limits transferability insights.

### W9. Novelty verification deferred (Severity: High — due to constraints)
Due to Retrieval-Disabled Mode in this review run, external literature comparison could not be performed. Novelty verdicts for C1–C3 are marked as deferred for manual verification.

## Key Issues
### Issue 1: Missing variance reporting invalidates reliability assessment (Critical)
**Location:** Page 6 (Table 1), Page 7 (Table 2), Page 8 (Table 3), Page 7 (Fig. 4)
**Evidence:** All accuracy numbers are single-point estimates. For example, Table 1 shows ResNet-18 gains as small as +0.15% (CIFAR10 PD) and +0.11% (MNIST PD). Table 2 shows ZeroP vs AIT on MobileNetV2 5-bit: 71.71% vs 71.96%.
**Impact:** Without standard deviation over multiple runs, these small differences cannot be distinguished from training noise. The claim that PD helps for small-gain cases is unverifiable.
**Fix:** Report mean±std over ≥3 seeds. Add a paired significance test (t-test or Wilcoxon) for the ZeroP-w/ vs ZeroP-w/o comparison.

### Issue 2: "Consistently outperforms all SOTA" contradicts Table 2 data (Major)
**Location:** Page 8 — Performance Comparison paragraph (right column)
**Evidence:** Text claims "ZeroP consistently outperforms all solely SD SOTA methods", but Table 2 shows AIT at 71.96% (MobileNetV2 5w5a) > ZeroP at 71.71%.
**Impact:** This factual overclaim directly reduces reviewer trust and may trigger rejection if not corrected.
**Fix:** Replace with "ZeroP achieves the best or second-best accuracy among pure-SD methods across all 8 evaluated settings." Acknowledge AIT's marginal advantage on MobileNetV2 5-bit.

### Issue 3: BNS selection metric has unanalyzed failure modes (Major)
**Location:** Page 6 (Table 1), Page 7 (Fig. 4 and Section 4.1.2 Results)
**Evidence:** CIFAR10 (BNS=82.14) outperforms Random Noise (BNS=78.09) despite larger distance. Correlation varies: ρ≈0.5 for ResNet-18 5-bit vs ρ≈0.9 for RegNet-600MF 5-bit.
**Impact:** The selection method's reliability is context-dependent. Practitioners cannot trust BNS distance without knowing when it works (and when it does not).
**Fix:** Add failure-mode analysis for the CIFAR10 case. Report per-architecture correlations with confidence intervals. Provide a practical decision rule (e.g., "use BNS as a first-pass filter, then validate top-3 candidates").

### Issue 4: Hyperparameter λ and M lack sensitivity validation (Major)
**Location:** Page 5 (Eq. 5-6), Page 7 (Section 4.1.2 Settings)
**Evidence:** λ=0.5 and M=1024 are fixed without ablation.
**Impact:** The reported gains could be sensitive to these choices. If λ optimization yields another 1-2% gain, the current results underreport potential. If λ=0.5 is suboptimal for some PDs, some gains may be underestimated.
**Fix:** Add λ sensitivity sweep (0.25/0.50/0.75) and M stability check (512/1024/2048) in appendix.

### Issue 5: Related Work does not fulfill "systematic understanding" promise (Moderate)
**Location:** Page 9 (Section 5)
**Evidence:** Single paragraph, chronological listing, no comparison table, no explicit differentiation from KnockoffNet/DeGANs.
**Impact:** The introduction claims contribution (1) is "provide a systematic understanding of the role of PDs in ZSQ", but the related work section does not deliver this systematic analysis.
**Fix:** Restructure as 2-3 thematic paragraphs or a comparison table. Add explicit "Difference from ZeroP" sentence for each cited method.

### Issue 6: Conclusion and Limitations lack specificity (Moderate)
**Location:** Page 9 (Sections 6 and 7)
**Evidence:** Limitations list 3 items without mitigation suggestions. Conclusion is 5 sentences repeating the abstract.
**Impact:** Weak closing reduces the paper's value as a reference for future work.
**Fix:** Add mitigation strategies for each limitation. Expand conclusion to include validated findings + bounded limitations + next steps.

## Actionable Suggestions
### S1 (Must): Add statistical significance testing across all main results
**Target:** Tables 1-3, Figures 3-4 (Pages 6-8)
**Action:** Run all experiments with ≥3 random seeds and report mean ± std. For the main comparison (ZeroP w/ vs ZeroP w/o, Table 2), add a paired bootstrap test or Wilcoxon signed-rank test and annotate significant gains (e.g., bold with *p<0.05).
**Expected benefit:** Converts unverifiable single-point claims into statistically grounded conclusions. This is the single highest-impact revision.

### S2 (Must): Fix overclaim in performance comparison paragraph
**Target:** Page 8 — Performance Comparison paragraph
**Current wording:** "ZeroP consistently outperforms all solely SD SOTA methods"
**Revised wording:** "ZeroP achieves the best or second-best accuracy among pure-SD methods in all 8 evaluated settings (4 architectures × 2 bit-widths). The only exception is MobileNetV2 5-bit, where AIT achieves 71.96% vs ZeroP's 71.71%."
**Expected benefit:** Eliminates a factual error that could trigger reviewer rejection.

### S3 (Must): Add hyperparameter sensitivity analysis for λ and M
**Target:** Page 5 (Eq. 5-6), Appendix
**Action:** 
- Sweep λ ∈ {0.25, 0.50, 0.75} on ResNet-18 + MobileNetV1 at 4-bit with COCO as PD. Report results in a small table.
- Vary M ∈ {256, 512, 1024, 2048} and show that BNS distance ranking (top-3 PDs) is stable for M ≥ 512.
**Expected benefit:** Demonstrates the method is robust to hyperparameter choice and that λ=0.5 is a reasonable default.

### S4 (Must): Analyze BNS distance counterexamples
**Target:** Page 7 — Section 4.1.2 Results
**Action:** Add 2-3 sentences analyzing why CIFAR10 (BNS=82.14) outperforms Random Noise (BNS=78.09) despite larger distance. Hypothesis: structured visual features in CIFAR10 provide useful gradient information that random noise lacks, even if BN statistics differ.
**Expected benefit:** Builds reviewer trust by showing the authors understand their method's limitations.

### S5 (Nice-to-have): Restructure Related Work as taxonomy
**Target:** Page 9 (Section 5)
**Action:** Organize into three blocks: (a) Data-free ZSQ methods, (b) Data-free KD methods, (c) Model stealing with PD. For each block, add a one-sentence contrast with ZeroP.
**Expected benefit:** Delivers on the "systematic understanding" promise from Contribution 1.

### S6 (Nice-to-have): Expand Conclusion with limitations and next steps
**Target:** Page 9 (Section 7)
**Action:** Restructure as: (1) validated findings (2 sentences), (2) bounded limitations (2 sentences), (3) concrete next steps (2 sentences — ViT extension, BN-free selection, other data-free tasks).
**Expected benefit:** Stronger closing that guides follow-up research.

### S7 (Nice-to-have): Improve abstract comparison specificity
**Target:** Page 1 (Abstract)
**Action:** Name the comparison baseline for the 7-16% claim and the 3.9% claim. Replace "opens up new avenues" with a concrete implication.
**Expected benefit:** Makes the abstract more informative and less promotional.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: Generic DL background → Quantization → OD difficulty → ZSQ
- P2: Two ZSQ approaches → SD limitation → "fundamental question"
- P3: Related tasks using PD → Direct PD question → Challenges
- P4: "To do this" paragraph → Roadmap → BNS method preview
- P5: Contribution summary paragraph

**Issue:** The narrative is **bottom-heavy** — the key insight (PD as direct input) is explained in P3-P4 after lengthy contextual buildup. The "fundamental question" in P2 is compelling but the answer is delayed.

### Recommended Storyline (Option A — Problem-First Arc)

**Target:** Restructure the introduction into a clean 4-paragraph arc:

**P1 — The Problem (Big Picture → Gap):**
"Network quantization enables efficient deployment, but fine-tuning requires original training data (OD) which is often inaccessible. Zero-shot quantization (ZSQ) addresses this but existing methods that rely solely on synthetic data (SD) suffer significant accuracy drops (e.g., 10-20% on MobileNetV1 at 4-bit)."

**P2 — Why SD is Insufficient (Gap Detail):**
"SD generation methods match OD statistics through limited loss terms (BNS, inter/intra-class loss). However, as we show, SD captures only a subset of OD's feature distribution (Fig. 2). This motivates searching for alternative data sources."

**P3 — The Solution (PD as Input → Key Idea):**
"Publicly available proxy data (PD) is a natural candidate. Unlike prior work that used PD only to guide SD generation, we propose using PD directly as input alongside SD. The challenges are: (a) PD may have mismatched distribution, (b) selecting good PD is costly. We address both."

**P4 — Contributions preview:**
(1) First systematic PD-in-ZSQ study, (2) BNS-distance selection, (3) Consistent SOTA-level gains.

### Abstract Outline (Complete)

**S1 (Problem):** "Zero-shot quantization (ZSQ) enables low-bit networks without access to original training data (OD), but performance degrades significantly when only synthetic data (SD) is available."

**S2 (Gap):** "Existing ZSQ methods rely exclusively on SD, which captures only limited aspects of OD's distribution."

**S3 (Method):** "We propose ZeroP, which directly incorporates publicly available proxy data (PD) as a complement to SD for quantization fine-tuning, along with a lightweight batch-normalization statistics (BNS) distance metric for selecting effective PD."

**S4 (Key Result 1):** "On ImageNet-1K 4-bit quantization, ZeroP improves accuracy by 7-16% over the best pure-SD baseline across architectures (e.g., MobileNetV1: 43.31% → 59.38%)."

**S5 (Key Result 2):** "ZeroP achieves 72.17% top-1 accuracy on ResNet-50 (4-bit), outperforming the leading pure-SD method by 3.9%, and approaches the performance of OD-based methods."

### Introduction Outline (Complete)

**P1 — Territory + Gap (Big Picture → Specific Problem):**
- Hook: Quantization + deployment need → OD scarcity (privacy/cost)
- Problem: ZSQ addresses this but works poorly
- Evidence: specific accuracy numbers
- Transition: "The core issue is that SD-only approaches..."

**P2 — SD Limitations (Why current approaches fall short):**
- SD methods: ZeroQ → GDFQ → Qimera → IntraQ
- Limitation: SD captures limited feature variability (Fig. 2)
- Key question: "Can we obtain OD-related information beyond SD?"
- Transition: "One underexplored resource is proxy data..."

**P3 — PD Opportunity + Challenges (Solution Preview):**
- Prior PD usage: only as SD guidance (KnockoffNet, DeGANs)
- Our novel angle: PD as direct input
- Two challenges: distribution mismatch + selection cost
- Transition (one sentence): bridge paragraph

**P4 — This Paper (Roadmap + Contributions):**
- Three steps: (1) direct PD baseline, (2) 16-PD evaluation, (3) BNS selection
- Three contributions (concrete, non-overlapping)
- Transition to Section 2

## Priority Revision Plan
### Revision Ranking (P0 = Must, P1 = Important, P2 = Nice-to-have)

| Priority | Issue | Action | Effort | Impact | Annotation IDs |
|----------|-------|--------|--------|--------|----------------|
| **P0** | Missing statistical rigor | Add 3-seed variance, significance tests | High (compute) | Very High — converts claims to evidence | #9 (Page 6) |
| **P0** | Overclaim "consistently outperforms all SOTA" | Correct wording to match Table 2 data | Low (text edit) | High — removes factual error | #11 (Page 8) |
| **P1** | No λ/M sensitivity analysis | Add ablation sweep for λ and M | Medium (compute) | Medium — demonstrates robustness | #8 (Page 5) |
| **P1** | BNS failure modes unanalyzed | Add analysis of CIFAR10 vs Random Noise case | Low (analysis + text) | Medium — builds trust in method | #10 (Page 7) |
| **P1** | Abstract lacks comparison specificity | Name baselines for all gain claims | Low (text edit) | Medium — improves first impression | #1 (Page 1) |
| **P1** | Related Work is flat list | Restructure as taxonomy + add contrast table | Low-Medium | Medium — supports C1 | #13 (Page 9) |
| **P2** | Conclusion too brief | Expand with limitations + next steps | Low (text) | Low-Medium | #15 (Page 9) |
| **P2** | Limitations lack mitigation | Add one mitigation per limitation | Low (text) | Medium | #14 (Page 9) |

### Revision Order (Recommended Execution Sequence)

**Phase A (Week 1-2):** P0 fixes — claim correction + statistical reruns.
1. Correct overclaim in Performance Comparison paragraph (Page 8).
2. Run main experiments with 3 seeds, compute mean/std, add significance annotations.
3. Update Abstract with specific baseline names.

**Phase B (Week 3-4):** P1 analyses — sensitivity studies + failure analysis.
4. Run λ sweep (0.25/0.50/0.75) on 2 architectures × 2 PDs.
5. Test M stability (256-2048) and confirm convergence.
6. Analyze CIFAR10 vs Random Noise counterexample.
7. Restructure Related Work section.

**Phase C (Before resubmission):** P2 polish.
8. Expand Conclusion with validated findings + bounded limitations + next steps.
9. Add mitigation suggestions to each limitation.
10. Final proofread for claim precision throughout.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup (Data/Model) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------------------|---------|-------------|----------------|-------------------|
| E1 | Evaluate 16 PDs on ImageNet-1K 4-bit | 4 architectures (RN18, MNV1, MNV2, RegNet), 16 PD datasets | Top-1 accuracy | COCO best (+1.4% to +16.07%); SVHN worst | C1 — PD improves ZSQ | Single seed, no variance |
| E2 | BNS distance correlation | Same as E1 + 5-bit | Spearman ρ, Pearson ρ | ρ=0.5-0.9 across archs | C2 — BNS predicts PD quality | ρ varies substantially; CIFAR10 counterexample |
| E3 | SOTA comparison (ImageNet) | 4 archs, 4-bit & 5-bit | Top-1 accuracy | ZeroP best in 7/8 settings | C3 — SOTA performance | AIT better on MNV2 5-bit; no variance |
| E4 | SOTA comparison (CIFAR) | ResNet-20, 3/4/5-bit | Top-1 accuracy | ZeroP+PD beats SD baselines | C3 — generalization | Only 1 architecture |
| E5 | Ablation: SD vs RN vs OD vs PD | 4 ZSQ methods × 3 datasets × 3 bit-widths | Top-1 accuracy | OD > PD > SD > RN pattern | C1 — PD transferable | RN>SD counterexample unexplained |
| E6 | BNS group analysis (Fig. 4) | 4 archs, 4 & 5-bit | Spearman ρ | BNS groups separate PD effectiveness | C2 — BNS as selection | Per-arch variation not analyzed |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Current Strength | Gap | Required Action |
|-------------------------|-----------------|-----|----------------|
| **New Knowledge** | First systematic PD evaluation in ZSQ (16 datasets) | No external literature comparison for novelty claims | Literature search (deferred) |
| **Reproducibility** | Public datasets, standard architectures | No multi-seed variance; λ and M fixed without analysis | Add variance + sensitivity studies |
| **Impact on Practice** | Simple plug-in to existing ZSQ pipelines | Use cases beyond classification not tested | Add segmentation/detection experiment |
| **Mechanism Understanding** | BNS distance correlates with performance | CIFAR10 vs RN counterexample unexplained | Add failure-mode analysis |

### Proposed Research Experiments (P0/P1/P2)

**P0-EXP1: Statistical robustness package**
| Field | Detail |
|-------|--------|
| **Target Claim** | C3 — ZeroP outperforms pure-SD methods |
| **Hypothesis** | Gains >1% are statistically significant at p<0.05 |
| **Minimal Design** | Run 3 seeds for ZeroP w/o and ZeroP w/ on 4 architectures (ImageNet 4-bit), compute mean/std |
| **Metrics** | Mean top-1 ± std, p-value from Wilcoxon signed-rank test |
| **Success Criterion** | Gains with p<0.05 for gains >1%; flag gains <1% as non-significant |
| **Cost** | ~3× current compute (assume 3 seeds) |
| **Quality Gain** | Converts all empirical claims from unverifiable to statistically grounded |

**P0-EXP2: Hyperparameter sensitivity — λ mixing ratio**
| Field | Detail |
|-------|--------|
| **Target Claim** | C1 — PD mixing strategy is robust |
| **Hypothesis** | λ=0.5 is near-optimal for PDs with small BNS distance |
| **Minimal Design** | Test λ ∈ {0.25, 0.50, 0.75} on ResNet-18 + MobileNetV1 with COCO PD at 4-bit |
| **Metrics** | Top-1 accuracy |
| **Success Criterion** | λ=0.5 is within 0.5% of the best λ |
| **Cost** | ~3 additional runs |
| **Quality Gain** | Removes concern about arbitrary hyperparameter choice |

**P1-EXP3: BNS distance counterexample analysis (CIFAR10)**
| Field | Detail |
|-------|--------|
| **Target Claim** | C2 — BNS distance predicts PD utility |
| **Hypothesis** | CIFAR10 outperforms RN because structured features help, despite BN stat mismatch |
| **Minimal Design** | Compute feature-space similarity (CKA) between CIFAR10 and ImageNet at different layers; compare with RN |
| **Metrics** | CKA similarity per layer |
| **Success Criterion** | CKA at mid/high layers is higher for CIFAR10 than RN, explaining the performance inversion |
| **Cost** | Low (no new quantization runs needed) |
| **Quality Gain** | Explains known failure case, strengthens BNS method credibility |

**P1-EXP4: Extend to segmentation/detection**
| Field | Detail |
|-------|--------|
| **Target Claim** | C1 — PD benefits general data-free tasks |
| **Hypothesis** | PD improves ZSQ for segmentation models on Cityscapes |
| **Minimal Design** | Quantize DeepLabV3 (Cityscapes) using PD (e.g., COCO, Mapillary), compare to SD-only baseline |
| **Metrics** | mIoU |
| **Success Criterion** | PD improves mIoU by ≥1% over SD-only |
| **Cost** | Medium (new task implementation) |
| **Quality Gain** | Demonstrates generality beyond image classification |

### ASCII Diagram — Experiment Upgrade Plan

```text
Phase A (Weeks 1-2): Statistical Validation
┌─────────────────────────────────────────────────────────────┐
│ P0-EXP1: 3-seed runs on all main comparisons (Tables 1-3)  │
│ └─> mean±std + significance tests                          │
│ P0-EXP2: λ sweep (0.25/0.50/0.75) on 2 archs              │
│ └─> confirm λ=0.5 robustness                               │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
Phase B (Weeks 3-4): Understanding + Generalization
┌─────────────────────────────────────────────────────────────┐
│ P1-EXP3: CKA analysis for CIFAR10 counterexample           │
│ └─> explain BNS distance failure mode                      │
│ P1-EXP4: Segmentation detection experiment                 │
│ └─> show PD benefit beyond classification                  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
Phase C (Before Resubmission): Writing + Positioning
┌─────────────────────────────────────────────────────────────┐
│ Fix overclaim wording (P0)                                  │
│ Restructure Related Work (P1)                               │
│ Expand Conclusion + Limitations (P2)                        │
│ Literature verification for novelty claims (deferred)      │
└─────────────────────────────────────────────────────────────┘
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Scoring Rationale

The paper demonstrates a practically motivated, empirically extensive study of proxy data for zero-shot quantization. Its strengths include the breadth of PD evaluation (16 datasets), plug-and-play compatibility with existing ZSQ methods, and strong gains on challenging architectures (MobileNetV1 +16%). However, several critical weaknesses limit the current score:

1. **Research Value (primary dimension):** The core idea (using PD as direct input) is intuitive but not technically deep. The paper's main value is the extensive empirical characterization rather than a new algorithmic principle. Score: 6/10.
2. **Novelty (primary dimension):** The concept of using proxy data in data-free tasks is not new (KnockoffNet, DeGANs). The novelty lies in (a) using PD as direct input (vs SD guidance) and (b) the systematic 16-dataset evaluation. However, external literature verification is deferred in this run, so novelty is conservatively assessed as moderate. Score: 5/10.
3. **Validity/Soundness:** The absence of statistical significance testing and the overclaim about "consistently outperforming all SOTA" (contradicted by Table 2 data) are serious concerns. Score: 5/10.
4. **Reproducibility:** Public datasets and standard architectures are used. Missing variance reporting and lack of λ/M sensitivity analysis reduce reproducibility. Score: 6/10.

### Final Score

**Final Score: 5.5 / 10**

*Interpretation: Marginally above the acceptance threshold for a top-tier conference. Major revisions addressing statistical rigor, claim precision, and hyperparameter sensitivity are required before the paper can be confidently accepted.*

### Post-Revision Target

**Post-Revision Target: [6.5, 7.5] / 10**

*If all P0 issues (statistical significance, overclaim correction) and P1 issues (λ/M sensitivity, BNS failure analysis, Related Work restructuring) are fully addressed, the paper could reach an 7/10 level — a solid acceptance at a top venue. The upper bound (7.5) requires convincing external literature verification (currently deferred) and a successful segmentation/detection generalization experiment.*