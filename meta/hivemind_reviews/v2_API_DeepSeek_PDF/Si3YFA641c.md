## Summary
# Final Review Report

## Summary

This paper, published at ICLR 2024, identifies and relaxes two "nonessential settings" in Evidential Deep Learning (EDL) that the authors argue exacerbate over-confidence. First, the prior weight W (which controls the balance between evidence proportion and magnitude in computing projected probabilities) is fixed to the number of classes C in standard EDL; the paper proposes treating λ = W/C as a tunable hyperparameter. Second, the standard EDL loss includes a variance-minimization term Lvar that drives the Dirichlet distribution toward a Dirac delta; the paper removes this term, directly optimizing the expected Dirichlet probability toward the one-hot label. The resulting R-EDL method demonstrates consistent improvements over EDL and the recent I-EDL baseline across classical, few-shot, noisy, and video-modality settings in both confidence estimation and out-of-distribution detection tasks.

The paper is technically well-motivated, with clear identification of two specific weaknesses in a widely-used method. The mathematical exposition is rigorous, with careful derivations linking subjective logic theory to the proposed modifications. The empirical evaluation is broad (four settings, multiple datasets, comparison against six baselines). However, several aspects require attention: the derivation from generalized W to the concentration parameter lacks intermediate justification, the selection of λ using classification accuracy rather than uncertainty quality metrics introduces a potential bias, the statistical significance of improvements over I-EDL is not assessed, and the limitations section omits several important boundaries. External literature verification was not available in this run, so novelty and SOTA claims are marked as deferred manual verification.

## Strengths
**S1 — Clear and well-motivated problem identification.** The paper identifies two specific, well-defined weaknesses in the standard EDL framework: the rigid prior weight setting (W = C) and the variance-minimization regularization term (Lvar). Both are clearly explained with supporting analysis (the 100-class counter-example for prior weight and the Dirac delta characterization for Lvar). The paper correctly argues that these settings, while widely adopted, are not intrinsically mandated by subjective logic theory.

**S2 — Rigorous mathematical exposition.** The paper provides thorough derivations of the bijection between subjective opinions and Dirichlet PDFs (Theorem 1), the EDL optimization objective (Eq. 2), and the generalized R-EDL formulation. The proof of bijectivity in Appendix A.1 is complete and correctly structured. The derivations of uncertainty measures in Appendix B (expected entropy, mutual information, differential entropy) are well-documented.

**S3 — Broad and comprehensive experimental evaluation.** The paper evaluates R-EDL across four distinct experimental settings: classical (MNIST, CIFAR-10), few-shot (mini-ImageNet), noisy (CIFAR-10 with Gaussian noise), and video-modality (UCF-101). Multiple uncertainty metrics are used (AUPR, AUROC, ECE, Brier score), and results are averaged over multiple runs with standard deviations reported. The ablation study (Table 3) cleanly separates the contributions of each relaxation.

**S4 — Practical relevance and simplicity of the proposed modifications.** Both relaxations are straightforward to implement: introducing λ as a tunable hyperparameter and removing Lvar from the loss. This simplicity makes R-EDL easy to adopt and build upon. The paper demonstrates that these simple changes yield consistent improvements, which is a valuable finding for the uncertainty estimation community.

**S5 — Candid discussion of limitations.** The paper acknowledges that the optimal λ value is not theoretically derived and that the optimization objective is "somewhat coarse." This self-awareness about the method's limitations is commendable and provides clear directions for future work.

## Weaknesses
**W1 — Mathematical derivation gap in the generalized concentration parameter.** [Connected to Page 4 annotation] The transition from the generalized projected probability (Eq. 7) to the relaxed concentration parameter αX(x) = eX(x) + λ (Eq. 9) skips a critical intermediate step. The formulas for belief mass bX(x) and uncertainty mass uX in terms of eX(x) were originally derived assuming W = C. When W becomes a free parameter, one must re-derive bX(x) and uX from the bijection conditions before substituting into αX(x) = bX(x)W/uX + aX(x)W. The paper's leap from Eq. 7 to Eq. 9 without this derivation weakens the mathematical rigor of the core contribution.

**W2 — λ selection criterion is misaligned with the paper's primary objectives.** [Connected to Page 9 annotation] The hyperparameter λ = W/C is selected based on "best classification accuracy on the validation set." However, the paper's primary claims are about uncertainty estimation quality — OOD detection and confidence estimation — not classification accuracy. Using accuracy for λ selection may inadvertently choose values that optimize for sharp predictions at the expense of well-calibrated uncertainty. Since the ablation study shows λ=0.1 performs best, but the paper does not report whether λ chosen by OOD AUPR would differ, this introduces a potential confound.

**W3 — Statistical significance is not established for claimed improvements.** [Connected to Page 7 annotation] The paper reports absolute gains against EDL and I-EDL without statistical significance tests. For the CIFAR-10→SVHN OOD detection task, R-EDL achieves 85.00±1.22 vs I-EDL's 83.26±2.44 — the overlapping standard deviations suggest the gain may not be statistically significant. Without paired significance tests (e.g., Wilcoxon signed-rank across 5 runs), readers cannot assess whether the improvements are robust or due to random seed variation.

**W4 — No external literature verification for novelty and SOTA claims.** [Connected to Page 1 annotation] The abstract claims "SOTA performances" and the paper states it is "the first to consider relaxing the nonessential settings." Due to external paper search being unavailable in this run, these novelty claims cannot be verified against the broader literature. The paper's comparison set, while reasonable, is limited to 3-6 baselines and does not include the full landscape of uncertainty estimation methods. The claim of being "first" to relax these settings requires manual verification against prior work.

**W5 — The "average" composite metric in the noisy setting is not clearly defined.** [Connected to Page 8 annotation] Fig. 1(a) presents an "average of classification accuracy and AUPR score." These two metrics operate on different scales (~15-90% for accuracy, ~52-94% for AUPR). The paper does not specify whether metrics are normalized before averaging. If raw values are averaged, the composite is dominated by the larger-scale metric and is not interpretable. This undermines the claim of "superior performance" under noise.

**W6 — Limitations section omits important boundaries.** [Connected to Page 9 annotation] The Deficiencies section discusses λ optimal value theory and the coarse optimization objective, but omits: (a) the cost of λ tuning (added hyperparameter search), (b) settings where R-EDL does not outperform I-EDL (e.g., 5-way 5-shot classification accuracy: 81.85 vs 82.00 for I-EDL), (c) limited evaluation scale (only small-to-medium datasets and backbones), and (d) the interaction between the deprecated Lvar and the retained KL regularization term Lkl.

## Key Issues
### Issue 1: Insufficient mathematical justification for the generalized formulation (Severity: Major)
The paper introduces a generalized αX(x) = eX(x) + λ (Eq. 9) but does not fully derive how the belief mass bX(x) and uncertainty mass uX map to evidence eX(x) under the relaxed prior weight W. The derivation from Eq. 7 to Eq. 9 assumes the same functional form holds when C is replaced by W, without re-deriving from the bijection conditions. This gap, while not invalidating the approach, reduces the mathematical rigor of the core contribution.

**Root cause:** The authors implicitly rely on an unstated assumption that the relationship between evidence and Dirichlet parameters is invariant under changes to W, which is not mathematically trivial.

**Impact:** Reviewers and mathematically-oriented readers may question whether R-EDL strictly adheres to subjective logic theory as claimed.

### Issue 2: λ selection criterion creates a potential confound (Severity: Major)
The hyperparameter λ is selected by optimizing classification accuracy on a validation set, yet the paper's contributions target uncertainty estimation quality. This mismatch means the reported OOD detection and confidence estimation results may be suboptimal relative to what could be achieved with λ tuned for those metrics. More critically, it creates an unfair comparison advantage if baselines also tune their hyperparameters for different objectives.

**Root cause:** The paper does not provide a principled criterion for λ selection tied to uncertainty quality.

**Impact:** The uncertainty estimation gains could potentially be larger (or smaller) if λ were selected by an uncertainty-aware criterion, making current results unverifiable.

### Issue 3: Statistical significance of improvements is not established (Severity: Major)
The paper reports gains over I-EDL but does not provide statistical significance tests. For several comparisons, the standard deviations of R-EDL and I-EDL overlap substantially (e.g., CIFAR-10→SVHN OOD detection: R-EDL 85.00±1.22 vs I-EDL 83.26±2.44; 5-way 20-shot classification: R-EDL 88.74±0.05 vs I-EDL 88.12±0.05), making it difficult to assess whether improvements are robust.

**Root cause:** The paper evaluates significance indirectly through multi-run averaging and standard deviation, but does not conduct formal hypothesis tests.

**Impact:** Without significance testing, the claim of "SOTA performances" and "remarkable performances" is not statistically grounded.

### Issue 4: Limited novelty assessment due to missing literature verification (Severity: Minor)
External paper search was unavailable in this run, preventing verification of novelty claims. The paper's claim of being "the first to consider relaxing the nonessential settings" and its implicit SOTA claims require manual verification against the broader literature. The comparison set, while reasonable, covers only a subset of uncertainty estimation methods.

**Root cause:** External retrieval infrastructure unavailability.

**Impact:** Novelty and SOTA judgments are deferred to manual verification.

### Issue 5: Unclear composite metric in the noisy setting (Severity: Minor)
The noise robustness analysis uses an "average" of classification accuracy and OOD detection AUPR without specifying whether these metrics are normalized before averaging. Since the scales differ substantially, the composite metric is not interpretable without further clarification.

**Root cause:** The paper prioritizes visual conciseness over metric clarity.

**Impact:** The claim of superior noise robustness cannot be fully assessed without raw metric inspection (available in Table 11, but the main text relies on the averaged figure).

## Actionable Suggestions
### Suggestion 1: Complete the mathematical derivation of the generalized concentration parameter
**Location:** Page 4, Section 3.2, between Eq. 7 and Eq. 9

**Action:** Add two intermediate derivation steps showing how the generalized αX(x) = eX(x) + λ follows from the bijection when W is free.

**Implementation:**
1. Define the generalized belief mass and uncertainty mass as functions of evidence under free W:
   - bX(x) = eX(x) / (Σ eX(x') + W)
   - uX = W / (Σ eX(x') + W)
2. Substitute into αX(x) = bX(x)W/uX + aX(x)W with aX(x) = 1/C:
   - αX(x) = [eX(x)W/(Σ eX(x')+W)] / [W/(Σ eX(x')+W)] + W/C = eX(x) + W/C = eX(x) + λ
3. Show that this reduces to αX(x) = eX(x) + 1 when λ = 1 (i.e., W = C)

**Expected benefit:** Eliminates the derivation gap and strengthens mathematical rigor.

### Suggestion 2: Use uncertainty-aware criteria for λ selection
**Location:** Page 5, Section 3.2 and Page 9, Section 5.5

**Action:** Select λ using a validation metric directly tied to uncertainty quality (e.g., OOD detection AUPR on a held-out validation set) rather than classification accuracy. Report both accuracy-selected and uncertainty-selected λ values and compare results.

**Implementation:**
- Create a validation split with ID and OOD samples
- For each candidate λ ∈ {0.01, 0.05, 0.1, 0.2, 0.5, 1.0}, compute validation OOD AUPR
- Select λ with best AUPR
- Report how results differ from accuracy-selected λ

**Expected benefit:** Removes the confound between λ selection and the claimed uncertainty benefits.

### Suggestion 3: Add statistical significance tests for key comparisons
**Location:** Page 7, Section 5.2 (after Table 1 description)

**Action:** Add paired significance tests (e.g., Wilcoxon signed-rank or paired t-test) comparing R-EDL against EDL and I-EDL for the primary metrics (OOD detection AUPR, confidence estimation AUPR). Report p-values for the most important comparisons.

**Implementation:**
- For each of the 5 runs, compute the paired difference (R-EDL minus baseline)
- Apply Wilcoxon signed-rank test across the 5 differences
- Report p-values in a footnote or parenthetical
- For metrics with p > 0.05, acknowledge the improvement is not statistically significant

**Expected benefit:** Provides readers with confidence that improvements are robust and reproducible.

### Suggestion 4: Clarify the composite metric in the noisy setting
**Location:** Page 8, Section 5.4 and Fig. 1(a)

**Action:** Either (a) explicitly state that metrics are min-max normalized before averaging, or (b) replace the composite with separate accuracy and AUPR line plots, or (c) simply reference Table 11 in the main text.

**Implementation:** Replace "Fig. 1(a) clearly illustrates the superior performance of R-EDL in terms of the average of these two key metrics" with: "We evaluate each metric separately (Table 11 in Appendix D.3). R-EDL achieves the best or second-best accuracy at all noise levels up to σ=0.10 while maintaining competitive OOD detection AUPR. At higher noise levels (σ≥0.125), R-EDL substantially outperforms both baselines in OOD detection."

**Expected benefit:** Removes ambiguity in the evaluation and makes the noise robustness claims verifiable.

### Suggestion 5: Expand the Limitations section
**Location:** Page 9, Section 6 (Deficiencies and Future directions)

**Action:** Add three additional limitations: (a) λ must be tuned per dataset, adding hyperparameter search cost; (b) in some settings, R-EDL does not outperform I-EDL; (c) evaluation is limited to small-medium-scale benchmarks.

**Implementation:** See the Mentor Revised Version in the Page 9 - Conclusion annotation.

**Expected benefit:** More complete and honest characterization of the method's scope strengthens scientific credibility.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this arc:
1. P1: High-risk domains need reliable uncertainty, existing methods are costly
2. P2: EDL is a promising single-pass method
3. P3: Two nonessential settings in EDL cause over-confidence
4. Contribution list

This is functional but can be improved. The gap between establishing the need for uncertainty and identifying EDL's specific weaknesses is somewhat abrupt. The paper transitions from "Bayesian/ensemble methods are computationally expensive" to "EDL solves this but has two problems" without clearly stating what EDL specifically contributes and what specific gap in uncertainty quality it leaves open.

### Recommended Storyline Revision

**Keep the current structure but strengthen the narrative connections:**

**P1 (unchanged):** High-risk domains → poor calibration → existing solutions costly → need efficient uncertainty.

**P2 (revised):** Introduce EDL as a promising single-pass solution, but note its over-confidence problem. The key limitation: while EDL was designed to reduce over-confidence, its specific implementation choices (fixed prior weight, variance regularization) actually work against this goal in some settings. This creates a clear tension.

**P3 (revised):** Identify the two nonessential settings and how they contradict EDL's objective of reliable uncertainty. The prior weight W = C forces an unintuitive upper bound on projected probabilities, and the variance term Lvar drives toward Dirac delta. Both push against uncertainty.

**P4 (theoretical insight paragraph — NEW):** Brief intuition about why relaxing these helps — smaller λ allows evidence proportion to dominate, removing Lvar prevents forced determinism. This creates logical anticipation for Section 3.

### Abstract Outline (Complete)

**S1 (Problem):** Evidential Deep Learning (EDL) provides single-forward-pass uncertainty estimation, but its specific parameterization choices inadvertently exacerbate over-confidence.

**S2 (Gap):** Two settings — the prior weight fixed to the number of classes and a variance-minimization regularization term — are not mandated by subjective logic theory yet are universally adopted.

**S3 (Method):** R-EDL relaxes these settings by introducing λ = W/C as a tunable hyperparameter and directly optimizing the expected Dirichlet probability, deprecating the variance term.

**S4 (Evidence):** Across classical, few-shot, noisy, and video-modality benchmarks, R-EDL consistently improves OOD detection and confidence estimation over EDL and state-of-the-art I-EDL.

**S5 (Scope):** The relaxations strictly adhere to subjective logic, providing a generalized yet principled framework for evidential uncertainty estimation.

### Introduction Outline (Complete)

**Paragraph 1 — Establish stakes and identify the gap:**
Role: Set the practical importance of uncertainty estimation. Identify the computational bottleneck of Bayesian/ensemble methods. Create space for single-pass alternatives.
Key claim: Existing reliable uncertainty methods are computationally expensive.
Transition: "This computational barrier motivates single-forward-pass alternatives like Evidential Deep Learning."

**Paragraph 2 — Introduce EDL and identify its unresolved weakness:**
Role: Present EDL as the leading single-pass approach. Acknowledge its success but identify its over-confidence problem as the key unresolved challenge.
Key claim: EDL reduces over-confidence compared to standard softmax, but its specific implementation choices limit further improvement.
Evidence anchor: Reference the counter-intuitive 100-class example from Section 3.2.
Transition: "We identify two specific settings in EDL that, while widely adopted, are not required by subjective logic theory."

**Paragraph 3 — Present the two relaxations:**
Role: Explain concisely what the two nonessential settings are and why relaxing them helps.
Key claim 1: The prior weight W = C imposes an unnecessarily low upper bound on projected probability in high-class-count regimes.
Key claim 2: The Lvar term forces the Dirichlet toward a point estimate, defeating the purpose of second-order uncertainty.
Transition: "Both relaxations strictly adhere to subjective logic."

**Paragraph 4 — Contribution summary and paper roadmap:**
Role: List contributions and guide reader through the paper structure.
Key contribution bullets (revised to emphasize method over analysis):
1. Generalized Dirichlet formulation with tunable λ = W/C
2. Simplified optimization objective without Lvar
3. Comprehensive empirical validation across diverse settings
Closing: "Detailed derivations, proofs, and additional results are provided in the Appendix."

## Priority Revision Plan
### P0 — Must-fix before any further submission (publication-critical)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|----------------|--------|
| P0.1 | λ selection criterion misalignment (Issue 2) | Select λ by OOD AUPR on validation set; report both accuracy-selected and uncertainty-selected results | Removes confound between λ choice and uncertainty claims | Medium (adds ~5 training runs) |
| P0.2 | Derivation gap in generalized αX (Issue 1) | Add 2-3 lines showing the complete derivation from bijection to αX = eX + λ | Closes mathematical rigor gap | Low (text only) |
| P0.3 | Unclear composite metric (Issue 5) | Replace averaged metric with separate accuracy and AUPR reporting; reference Table 11 | Makes noise robustness claims verifiable | Low (text only) |

### P1 — High priority (significantly improves paper quality)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|----------------|--------|
| P1.1 | Statistical significance (Issue 3) | Add paired significance tests for key comparisons (CIFAR-10→SVHN OOD) | Validates improvement claims | Low (compute from existing 5 runs) |
| P1.2 | Expand Limitations (W6) | Add λ tuning cost, non-superior cases, and evaluation scope limits | Improves scientific candor | Low (text only) |
| P1.3 | Reframe contribution list | Replace "analysis of" with method-focused phrasing | Strengthens contribution perception | Low (text only) |

### P2 — Nice-to-have (quality improvements)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|----------------|--------|
| P2.1 | Noisy setting analysis | Add separate line plots for accuracy and AUPR instead of averaged composite | Improves clarity | Low (figure update) |
| P2.2 | Related-work restructuring | Add structured comparison of DBU methods along concrete axes | Strengthens positioning | Medium (text rewrite) |
| P2.3 | Lkl vs Lvar interaction | Discuss whether KL regularization partially substitutes for removed Lvar | Deepens theoretical analysis | Low-Medium (text + small experiment) |

### Revision Order

1. **Immediate (text revisions):** P0.2, P0.3, P1.2, P1.3 (~2 hours)
2. **Short-term (experiments):** P0.1, P1.1 (~1 day)
3. **Optional improvements:** P2.1, P2.2, P2.3 (~1-2 days)

### Expected Quality Gains After Revision

| Dimension | Before | After |
|-----------|--------|-------|
| Mathematical rigor | Gap in derivation | Complete chain from bijection to loss |
| Statistical validity | No significance tests | p-values for key comparisons |
| Claim-evidence alignment | λ chosen by accuracy | λ chosen by uncertainty AUPR |
| Limitations transparency | 2 issues discussed | 5+ issues discussed |
| Overall score potential | Current level | +0.5-1.0/10 after P0+P1 fixes |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|-------------|----------------|-------------------|
| E1 | Classical OOD detection and confidence estimation | MNIST→KMNIST/FMNIST, CIFAR-10→SVHN/CIFAR-100; ConvNet/VGG16 backbones; baselines: EDL, I-EDL, KL-PN, RKL-PN, PostN, MC Dropout, DUQ | AUPR (MP, UM, DE, MI), AUROC, classification accuracy | R-EDL outperforms baselines on most metrics | C1 (prior weight relaxation), C2 (Lvar removal) | No significance tests; λ chosen by accuracy, not uncertainty metric |
| E2 | Few-shot OOD detection and confidence estimation | mini-ImageNet→CUB; WideResNet-28-10 backbone; N-way K-shot (N=5,10; K=1,5,20); baselines: EDL, I-EDL | Top-1 accuracy, AUPR (MP, UM, DE, MI) | R-EDL achieves best OOD detection in most settings | C1, C2, C3 (empirical effectiveness) | In some settings (5-way 5-shot), R-EDL accuracy slightly below I-EDL |
| E3 | Robustness to Gaussian noise | CIFAR-10 with zero-mean Gaussian noise σ∈[0.025,0.200]; baselines: EDL, I-EDL | Classification accuracy, OOD detection AUPR | R-EDL achieves best or second-best accuracy at low noise; best OOD at high noise | C3 | Composite "average" metric is ill-defined |
| E4 | Video-modality open-set recognition | UCF-101→HMDB-51/MiT-v2; I3D backbone; baselines: OpenMax, MC Dropout, BNN SVI, SoftMax, RPL, DEAR | Open maF1, Open Set AUC | R-EDL improves over DEAR (EDL-based SOTA) | C3 | Single backbone; limited analysis of which video-specific factors matter |
| E5 | Ablation study | Isolates λ relaxation and Lvar removal effects on classical and few-shot settings | AUPR, accuracy, confidence estimation | Both relaxations contribute; joint application is best | C1, C2, C3 | Does not analyze Lkl interaction with removing Lvar |
| E6 | λ hyperparameter analysis | CIFAR-10, λ ∈ [0.01, 1.5] | Classification accuracy, confidence AUPR, OOD AUPR | λ=0.1 optimal for accuracy; smaller λ generally better than λ=1 | C1 | Selection by accuracy may not align with uncertainty objectives |

### Research-Theme Gap Diagnosis

**Gap 1 — Causal attribution of gains:** The paper claims that removing Lvar mitigates over-confidence, but the ablation study cannot fully separate the effect of Lvar removal from the interaction with the retained KL regularization term (Lkl). The paper does not analyze whether Lkl partially or fully compensates for Lvar.

**Gap 2 — Generalization to large-scale settings:** All experiments use relatively small datasets (MNIST, CIFAR-10, mini-ImageNet) and moderate backbones. Whether R-EDL's benefits hold on large-scale benchmarks (e.g., ImageNet-1K with ViT) or complex modalities (e.g., medical imaging, point clouds) is unknown.

**Gap 3 — Practical λ selection guidance:** While the paper shows λ matters, it does not provide practical guidelines for selecting λ without a validation OOD set. In real-world deployment, OOD data may not be available at validation time.

### Proposed Research Experiments (P0/P1/P2)

| Experiment ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Quality Gain |
|--------------|-------------|------------|----------------|-------------------|---------|-------------------|----------------|----------------------|
| P0-Exp1: λ by AUPR | C1: λ improves uncertainty quality | Selecting λ by validation OOD AUPR yields better OOD detection than λ selected by accuracy | Re-run CIFAR-10 experiments with λ ∈ {0.01, 0.05, 0.1, 0.2, 0.5, 1.0} selected by OOD AUPR on held-out validation set (SVHN subset) | Compare accuracy-selected vs AUPR-selected λ for each metric | OOD AUPR, accuracy, ECE | AUPR-selected λ achieves ≥ accuracy-selected λ on OOD metrics | Low (~5 additional training runs) | Removes confound; potentially stronger results |
| P0-Exp2: Significance testing | C2, C3: R-EDL significantly outperforms baselines | The 5-run results show statistically significant improvement over I-EDL on CIFAR-10→SVHN | Compute paired Wilcoxon signed-rank test across 5 seeds for (R-EDL vs I-EDL) on OOD AUPR | None (within-subject comparison) | p-value, effect size | p < 0.05 for at least one OOD setting | Low (compute from existing runs) | Validates empirical claims |
| P1-Exp1: Lkl + Lvar interaction | C2: Lvar removal is the key | The improvement from Lvar removal is not explained by Lkl alone | Compare: (a) EDL (both Lvar+Lkl), (b) R-EDL (no Lvar, has Lkl), (c) R-EDL without Lkl, (d) EDL without both | EDL, R-EDL | OOD AUPR, accuracy | (b) > (a) and (c) < (b) confirms Lvar removal matters beyond Lkl | Medium (~10 runs) | Completes theoretical picture |
| P2-Exp1: Large-scale evaluation | C3: R-EDL generalizes | R-EDL's benefits hold on ImageNet-1K with modern architectures | Apply R-EDL modifications to ViT-B/16 on ImageNet-1K; evaluate OOD on ImageNet-R, ImageNet-C | Standard EDL, I-EDL | Accuracy, OOD AUPR, ECE | R-EDL matches or exceeds I-EDL on all metrics | High (compute-intensive) | Significantly strengthens generalizability claims |

```text
ASCII Diagram — Experiment Upgrade Plan

Stage 1 (P0 — Must, ~1 day):
  ├── P0-Exp1: λ by OOD AUPR instead of accuracy
  │     → Removes selection confound
  └── P0-Exp2: Paired significance tests (Wilcoxon)
        → Validates improvement claims statistically

Stage 2 (P1 — High priority, ~2 days):
  └── P1-Exp1: Lkl + Lvar interaction study
        → Isolates the mechanism: 4-way comparison

Stage 3 (P2 — Nice-to-have, ~1 week):
  └── P2-Exp1: ImageNet-1K scale evaluation
        → Tests generalizability boundaries
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

**Scoring rationale:**

The paper has genuine strengths: it identifies two well-motivated weaknesses in a widely-used uncertainty method, proposes simple and practical fixes, and provides broad experimental validation. The mathematical exposition is generally rigorous, and the ablation study cleanly separates the two contributions.

However, several issues prevent a higher score:
- **Research value (6/10):** While identifying weaknesses in EDL is valuable, the modifications are conceptually simple (adding a tunable λ and removing a loss term). The core insight — that EDL's parameterization choices are not mandated by subjective logic — is important but the resulting method does not introduce fundamentally new uncertainty estimation mechanisms.
- **Novelty (6/10):** The relaxations are clearly presented as modifications to existing methodology rather than a new framework. The claim of being "first" to consider these relaxations could not be externally verified in this run.
- **Validity/Soundness (7/10):** The derivations are largely correct, but the mathematical gap in the generalized concentration parameter derivation, the use of accuracy-based λ selection for uncertainty claims, and the lack of statistical significance tests collectively reduce confidence in the results.
- **Reproducibility (7/10):** Implementation details are well-documented in the appendix, and source code is provided. However, λ values vary across settings without clear guidelines for choosing them in new applications.

If all P0 and P1 issues are addressed (particularly P0.1: λ selection by uncertainty metric, P0.2: derivation gap, and P1.1: significance testing), the paper would warrant a significantly higher score.

**Post-Revision Target: [7.5, 8.0]/10**

This target assumes:
1. P0 issues (derivation gap, λ selection, composite metric) are fully resolved
2. P1 issues (significance tests, expanded limitations, contribution reframing) are addressed
3. The empirical claims remain supported after λ is selected by uncertainty-aware criteria
4. Manual literature verification confirms the novelty claims are valid within the stated scope