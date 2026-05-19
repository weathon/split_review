## Summary
# Final Review Report

## Summary

This paper, accepted at ICLR 2024, proposes a training-free CLIP adaptation method using Gaussian Discriminant Analysis (GDA). The core idea is to model CLIP visual features as class-conditional Gaussians with a shared covariance matrix, then construct a closed-form linear classifier from the estimated means and precision matrix (Eq. 3). This classifier is ensembled with CLIP's original zero-shot classifier (Eq. 5) to retain textual knowledge. The method is extended to base-to-new generalization via KNN-based data synthesis (Eq. 6) and to unsupervised learning via EM-based Gaussian mixture estimation (Eqs. 7-8).

The paper is well-executed empirically: it evaluates on 17 datasets across few-shot classification, imbalanced learning, out-of-distribution generalization, base-to-new generalization, and unsupervised learning. The method consistently outperforms prior training-free methods (by 2.82% on average over 11 datasets under 16-shot) and achieves competitive results with training-required methods (76.05% vs 75.83%). The ablation studies on precision matrix estimation (Table 6), ensemble effects (Figure 4), and architecture robustness (Table 9) are thorough.

However, the paper has several noteworthy weaknesses: (1) the Gaussian assumption for L2-normalized CLIP features is unexamined and potentially violated; (2) Eq. (4) for precision estimation lacks dimensional justification; (3) the EM covariance update (Eq. 8) uses non-standard equal class weights; (4) no variance/confidence intervals are reported despite running 3 seeds; (5) some comparative claims are over-extended (e.g., comparison to fully-trained models, p.9); (6) the conclusion adds unsupported future directions. Novelty/comparison conclusions are deferred due to Retrieval-Disabled Mode in this run.

## Strengths
**S1 — Clean, training-free methodology with strong empirical validation.** The core idea of applying GDA to CLIP adaptation is conceptually elegant: it replaces SGD-based optimization with closed-form parameter estimation from data statistics. The empirical validation is extensive (17 datasets, 5 task settings), and the method consistently outperforms prior training-free baselines across nearly all settings and architectures.

**S2 — Reproducibility-friendly design.** The method has no training hyperparameters beyond the ensemble coefficient α (searched coarsely), uses a standard shrinkage estimator for precision, and provides pseudocode (Algorithm 1). Training time is 1.6-3.6 seconds on a single RTX 3090, making it easy to reproduce and deploy.

**S3 — Strong ablation and analysis.** The paper includes thorough ablations: comparison of 6 precision estimation methods (Table 6), analysis of ensemble vs individual classifiers (Figure 4), scaling behavior with more data (Figure 3), and architecture robustness across 4 CLIP backbones (Table 9). These ablations support the design choices and clarify the method's behavior.

**S4 — Practical value for resource-constrained settings.** The training-free nature means the method can be deployed on devices without GPUs or with limited memory, using only a forward pass through CLIP and a small matrix inversion. The parameter storage is O(KD + D²) vs O(ND) for cache-based methods like Tip-Adapter.

## Weaknesses
**W1 [Core assumption gap] — Gaussian assumption for normalized CLIP features is unexamined.** The method models CLIP visual features as Gaussian-distributed with identical covariance across classes. However, CLIP features are typically L2-normalized, placing them on a unit hypersphere where Euclidean Gaussian assumptions are technically violated. The paper does not discuss or justify this assumption-feature mismatch anywhere. While empirical results are strong, the theoretical foundation has this gap that could affect interpretability and generalization to other feature spaces.

**W2 [Fairness of fully-trained comparison] — Table 7 comparison conflates pretraining scale.** The paper compares Ours (ViT-L/14 CLIP, pretrained on 400M image-text pairs) against ResNet-50/101 and DeiT trained only on ImageNet-1K. The "highest performance" claim is technically correct for the reported numbers but the comparison is not apples-to-apples due to vastly different pretraining data scales. A more appropriate comparison would be against linear probe on the same ViT-L/14 CLIP features with full training.

**W3 [Missing variance and significance] — No confidence intervals despite 3 runs.** The paper states it runs experiments with 3 seeds and averages results, but reports only point estimates without standard deviations or confidence intervals. Given that the margin over training-required methods is only +0.22% (76.05 vs 75.83), statistical significance cannot be assessed. The claim of "significantly" outperforming baselines (Section 4.2) is not statistically supported.

**W4 [EM covariance formulation] — Eq. (8) uses non-standard covariance weighting.** The M-step covariance update averages class covariances with equal weight (1/K) rather than responsibility-weighted averaging (N_k / total_N). This non-standard formulation could bias the covariance estimate when class responsibilities are imbalanced, potentially affecting convergence behavior.

**W5 [Conclusion overreach] — Unsupported future claims.** The conclusion adds "dense prediction tasks and other scenarios such as test-time adaptation" as future work without any evidence or even a conceptual sketch of how GDA would extend to these settings. Test-time adaptation, in particular, typically requires online single-sample estimation, which contradicts the batch-estimation premise of GDA.

**W6 [Incomplete failure analysis] — Weak cases not discussed.** The method underperforms on OxfordPets (vs Tip-X) and DTD (vs APE) in the 16-shot setting, but these cases are not analyzed. Understanding when the method fails (e.g., high intra-class variance, fine-grained textures) would strengthen the paper's scientific contribution.

**W7 [Novelty verification deferred] — Due to Retrieval-Disabled Mode in this run, all novelty and comparison conclusions are deferred. The paper's contribution claims relative to the literature cannot be independently verified without external paper search.**

**W8 [Writing style] — Some claims use overly promotional language** (e.g., "greatly outperforms," "significantly," "state-of-the-art") without precise statistical or comparative grounding. The phrase "hard-to-beat baseline" in the title is attention-grabbing but could be seen as overly confident.

## Key Issues
**Issue 1 (Severity: Major) — Gaussian assumption vs L2-normalized features (W1)**
The core of the method rests on an assumption (Gaussian features with identical covariance) that is likely violated by CLIP's L2-normalized embeddings. The authors should either (a) provide theoretical justification for why GDA works despite this mismatch, (b) add empirical diagnostics (e.g., normality tests on CLIP features, Q-Q plots, or eigenvalue analysis), or (c) discuss this as an explicit limitation. The current silence on this issue weakens the paper's theoretical rigor.

**Issue 2 (Severity: Major) — Missing variance reporting (W3)**
Despite averaging over 3 seeds, no standard deviations or confidence intervals are reported anywhere in the paper. Given that some improvements are small (e.g., +0.22% over training-required methods, +0.16% OOD average over Tip-Adapter-F), statistical significance is unclear. The claim of "significantly" outperforming baselines should be substantiated with error bars or significance tests.

**Issue 3 (Severity: Major) — Unclear precision estimator scaling in Eq. (4) (annotation Page 4)**
The formula $\widehat{\Sigma^{-1}} = D ((N-1)\hat{\Sigma} + \text{tr}(\hat{\Sigma}) I_D)^{-1}$ uses a scaling factor $D$ whose dimensional justification is unclear. This should be derived from the Kubokawa & Srivastava (2008) reference with explicit steps, or corrected if erroneous. The pseudocode (Algorithm 1) implements this literally, so any error in the formula would propagate to implementation.

**Issue 4 (Severity: Major) — EM covariance update uses non-standard weighting (W4)**
Equation (8) averages per-class covariance matrices with uniform weight $1/K$, while standard GMM uses responsibility-weighted averaging. This deviation should be justified or corrected. The equal-weight formulation could over-weight small, uncertain clusters and under-weight large, well-estimated ones, potentially degrading the shared covariance estimate.

**Issue 5 (Severity: Major) — Unfair comparison in Table 7 (W2)**
The comparison of Ours (ViT-L/14 CLIP, pretrained on 400M pairs) against ResNet/DeiT trained only on ImageNet-1K is informative but should be labeled as "different pretraining scale" rather than framed as "highest performance." A matched-scale baseline (e.g., linear probe on the same ViT-L/14 CLIP features) would be more appropriate.

**Issue 6 (Severity: Minor) — Conclusion overreach (W5)**
Adding dense prediction and test-time adaptation as future work without any feasibility evidence or conceptual sketch weakens the conclusion. These claims should be removed or grounded with a brief rationale.

**Issue 7 (Severity: Minor) — Failure case analysis missing (W6)**
The method underperforms on OxfordPets and DTD, but no analysis is provided. Understanding failure modes would strengthen scientific contribution.

**Issue 8 (Severity: Minor) — Title and language inflation**
The title "A Hard-to-Beat Baseline" and phrases like "greatly exceeds" (Section 4.2) and "state-of-the-art" (Conclusion) are promotional rather than precise. The title could be more informative (e.g., "Training-Free CLIP Adaptation via Gaussian Discriminant Analysis").

## Actionable Suggestions
**Suggestion A (Must) — Address Gaussian assumption for CLIP features (Issue 1)**
Add a paragraph in Section 3.1 or Section 5 (Conclusion/Limitations) discussing why GDA works despite CLIP features being L2-normalized. Suggested text: "We note that CLIP's visual features are L2-normalized to lie on a unit hypersphere, which technically violates the Euclidean Gaussian assumption. However, the resulting linear classifier remains effective because class-conditional means on the sphere still encode discriminative direction, and the shared covariance provides a regularized estimate of feature correlation structure. A formal analysis of this assumption mismatch is an interesting direction for future work."

**Suggestion B (Must) — Add variance reporting and significance (Issue 2)**
For the key results (Table 1, Table 3, Table 4), add standard deviations from the 3 seeds. For the claim of "comparable performance with training-required methods (76.05% vs 75.83%)", add a paired t-test or signed-rank test. If the improvement is not statistically significant, revise the wording to "our method achieves competitive performance without requiring training."

**Suggestion C (Must) — Justify or fix Eq. (4) precision estimator scaling (Issue 3)**
Provide a derivation or reference showing why scaling by $D$ is correct. Alternatively, adopt the standard Ledoit-Wolf or OAS shrinkage estimator which have well-understood theoretical properties. Add a note on the conditioning number of the resulting precision matrix.

**Suggestion D (Must) — Fix EM covariance update (Issue 4)**
Replace Eq. (8) with the standard GMM M-step: $\Sigma = \frac{1}{\sum_k N_k} \sum_k \sum_i \gamma_{ik} (x_i - \mu_k)(x_i - \mu_k)^T$ where $N_k = \sum_i \gamma_{ik}$. If the equal-weight formulation is intentional, provide justification and compare both versions in an ablation.

**Suggestion E (Must) — Reframe Table 7 comparison (Issue 5)**
Add a more direct baseline: linear probe on the same ViT-L/14 CLIP features trained on the full ImageNet training set. This is a natural "training-required" version of the same method. If the comparison to ResNet/DeiT is kept, clearly state "models trained from scratch on ImageNet only" vs "CLIP pretrained on 400M image-text pairs."

**Suggestion F (Recommended) — Analyze failure cases (Issue 6)**
Add a paragraph analyzing why the method underperforms on OxfordPets and DTD. Hypothesis: these datasets have high intra-class variance (different breeds, poses, textures) where the identical-covariance linear boundary is too restrictive. Add a t-SNE visualization of CLIP features for these datasets showing class-specific covariance structure.

**Suggestion G (Recommended) — Tone down promotional language (Issue 8)**
Replace "Greatly exceeds/outperforms" with "outperforms" or "achieves higher accuracy." Replace "hard-to-beat baseline" with a more descriptive title such as "Training-Free CLIP Adaptation via Gaussian Discriminant Analysis." Remove "state-of-the-art" where the comparison is limited to evaluated baselines.

**Suggestion H (Recommended) — Ground future work in evidence (Issue 5 continued)**
Remove or specifically ground future directions. For dense prediction: "GDA could be applied per-pixel using CLIP's dense features." For test-time adaptation: "TTA would require online estimation, which is beyond the current batch-estimation framework."

**Suggestion I (Recommended) — Add KNN label-noise analysis (annotation Page 2)**
Report the purity of KNN-retrieved neighbors for the base-to-new generalization setting. Add an ablation on k values showing performance vs. label noise trade-off.

## Storyline Options + Writing Outlines
### Abstract Outline (Revised)

Target: 5-sentence compact structure

- **S1 (Problem & Domain):** "Contrastive Language-Image Pretraining (CLIP) achieves strong zero-shot classification but adapting it to downstream tasks typically requires additional training, which is costly on resource-limited devices."
- **S2 (Prior Gap):** "Existing efficient adaptation methods — prompt learning, adapters, and cache models — still need gradient-based optimization, adding computational overhead and hyperparameter sensitivity."
- **S3 (Proposed Method):** "We revisit Gaussian Discriminant Analysis (GDA) as a training-free alternative: by modeling CLIP visual features as class-conditional Gaussians with a shared covariance, the Bayes-optimal classifier is obtained in closed form from the estimated means and precision matrix, then ensembled with CLIP's zero-shot classifier to retain textual knowledge."
- **S4 (Key Results):** "On 17 benchmarks, our method outperforms prior training-free methods by 2.82% on average and achieves competitive results with trained methods (76.05% vs 75.83%) on few-shot classification."
- **S5 (Scope & Availability):** "It also shows strong results on imbalanced learning, out-of-distribution generalization, base-to-new generalization, and unsupervised settings. Code is available at https://github.com/mrflogs/ICLR24."

### Introduction Outline (Revised)

**Current structure (5 paragraphs):**
P1: CLIP background (generic) → P2: Efficient fine-tuning methods + their cost → P3: Our GDA approach → P4: Extensions (KNN, EM) → P5: Result preview

**Weakness**: P1 spends too long on general CLIP background; P2 frames the limitation too narrowly as computational cost; P3 does not justify the Gaussian assumption.

**Revised structure (4 paragraphs, tighter narrative):**

- **P1 (Problem + CLIP context — 5 sentences):** "Deep learning success, but finetuning large models is expensive. CLIP provides strong zero-shot classification. However, zero-shot accuracy on downstream tasks lags behind supervised methods. This gap motivates efficient adaptation. Prior work (CoOp, CLIP-Adapter, Tip-Adapter) improves accuracy but still requires SGD training."
  *Transition sentence:* "This raises a natural question: can we match or exceed these adapted methods *without any training at all*?"

- **P2 (Gap + Our idea — 5 sentences):** "We observe that CLIP's visual encoder produces features that, while L2-normalized, exhibit class-conditional structure amenable to generative classification. We revisit Gaussian Discriminant Analysis (GDA), which constructs a linear classifier from class means and a shared covariance matrix — quantities estimable in closed form from few labeled examples. Our core innovation is to apply GDA to CLIP features and ensemble the resulting classifier with CLIP's original zero-shot classifier, combining visual and textual knowledge."
  *Transition sentence:* "This simple procedure requires no backpropagation, no hyperparameter tuning, and runs in seconds."

- **P3 (Extensions — 3 sentences):** "We further extend GDA to settings where labeled data is partially or fully unavailable. For base-to-new generalization, we synthesize new-class data via KNN retrieval from base classes using text embeddings. For unsupervised learning, we estimate the Gaussian mixture parameters via the EM algorithm initialized from CLIP's zero-shot predictions."

- **P4 (Contributions + Results — 4 sentences):** "Our contributions are: (1) a training-free CLIP adaptation method using GDA, (2) two simple extensions to base-to-new and unsupervised settings, and (3) extensive evaluation on 17 datasets. The method outperforms prior training-free approaches by 2.82% and matches training-required methods (76.05% vs 75.83%) on few-shot classification. On imbalanced learning, it surpasses fully fine-tuned baselines. The two variants also achieve competitive results on base-to-new generalization and unsupervised learning."

### Title Options
1. (Current) "A Hard-to-Beat Baseline for Training-Free CLIP-Based Adaptation"
2. "Training-Free CLIP Adaptation via Gaussian Discriminant Analysis"
3. "GDA-CLIP: Gaussian Discriminant Analysis for Training-Free CLIP Adaptation"

**Recommendation:** Option 2 or 3 is more descriptive and avoids promotional language while clearly communicating the method.

## Priority Revision Plan
```text
Priority Matrix:
| Priority | Low Effort (edits only)          | High Effort (new experiments)          |
|----------|----------------------------------|----------------------------------------|
| P0 (Must)| Eq.(4) justification,            | Add variance bars to Tables 1,3,4      |
|          | Conclusion toning down,          | EM covariance fix (Eq.8) + ablation    |
|          | Language toning down             |                                        |
| P1 (Should)| Gaussian assumption discussion, | KNN noise analysis (base-to-new)      |
|          | Failure case analysis text       |                                        |
| P2 (Nice) | Title revision option           | Additional OOD / domain-shift tests    |
|           | Related-work reorganization     |                                        |
```

### P0 Items (Must, before next submission)

1. **Justify Eq. (4) precision estimator scaling** — Add a derivation or reference showing why factor D is correct. This directly affects reproducibility.
2. **Fix EM covariance update** — Replace Eq. (8) with responsibility-weighted averaging. Run the unsupervised learning experiments again with the corrected formulation and report any changes.
3. **Add variance reporting** — Report standard deviations for all key tables (Table 1, 2, 3, 4, 5). For the key competitive claim (76.05 vs 75.83), run a statistical significance test.
4. **Tone down promotional language** — Remove "significantly" and "state-of-the-art" where not statistically justified. Replace with "our method outperforms" or "achieves higher accuracy."
5. **Remove or ground unsupported future claims** — Remove "dense prediction" and "test-time adaptation" or provide a concrete rationale.

### P1 Items (Should, before final version)

6. **Discuss Gaussian assumption** — Add a limitations paragraph in Section 5 acknowledging the L2-normalization / Gaussian mismatch.
7. **Add failure case analysis** — Discuss OxfordPets and DTD underperformance with visualization or hypothesis.
8. **Reframe Table 7 comparison** — Add a linear-probe baseline on the same ViT-L/14 CLIP features. Rephrase the comparison to acknowledge different pretraining scales.

### P2 Items (Recommended, quality improvement)

9. **Title revision** — Consider "Training-Free CLIP Adaptation via Gaussian Discriminant Analysis."
10. **Reorganize Related Work** — Restructure by adaptation mechanism (prompt tuning / adapter / cache / parametric) instead of chronological listing.
11. **Add KNN purity analysis** — Report what fraction of KNN-retrieved neighbors belong to the correct semantic class in the base-to-new setting.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|-------------|-----------------|-------------------|
| E1 | Few-shot classification | 11 datasets, 1/2/4/8/16 shots, RN50 CLIP, vs 5 training-free + 4 training-required methods | Top-1 accuracy | 76.05% avg (best training-free) | C1: training-free SOTA | No std reported; OxfordPets/DTD failure unanalyzed |
| E2 | Out-of-distribution generalization | ImageNet 16-shot -> 4 target datasets, ViT-B/16 | Top-1 accuracy | 60.37% avg (best overall) | C1: OOD robustness | Margin vs Tip-Adapter-F only +0.16% |
| E3 | Imbalanced learning | ImageNet-LT, Places-LT, RN101 CLIP, vs 9 baselines | Group acc, Overall, F1 | 62.34% Overall on IN-LT (best) | C1: imbalanced SOTA | Causal attribution conflates GDA + zero-shot ensemble |
| E4 | Base-to-new generalization | 11 datasets, half base / half new split, ViT-B/16, vs CLIP/CoOp/CoCoOp/KgCoOp | Base/New/H | 78.72 H (best) | C2: extension variant | KNN label noise not analyzed |
| E5 | Unsupervised learning | 11 datasets, no labels, EM-GMM, vs POUF/UPL | Top-1 accuracy | 63.46% avg (best on 7/11) | C2: extension variant | EM covariance weighting non-standard (Eq.8) |
| E6 | Precision matrix ablation | EuroSAT 1-16 shots, 6 estimators | Top-1 accuracy | KS estimator best (Table 6) | C3: KS estimator choice | Only on EuroSAT; generalizability unclear |
| E7 | Architecture robustness | 4 CLIP backbones (RN50, RN101, ViT-B/32, ViT-B/16), 16-shot, vs CoOp, Tip-Adapter | Top-1 accuracy | Ours best across all architectures | C3: architecture-agnostic | Comparison limited to one shot setting |
| E8 | Ensemble ablation | 11 datasets, 1-16 shots, zero-shot vs linear vs ensemble | Top-1 accuracy | Ensemble always best (Fig 4) | C3: ensemble effectiveness | — |
| E9 | Scaling behavior | ImageNet 1-64 shots | Top-1 accuracy | Linear in log(shots) (Fig 3) | C1: not limited to few-shot | Only ImageNet; other datasets unverified |

### Research-Theme Gap Diagnosis

1. **New Knowledge (partially supported):** The key insight — applying GDA to CLIP features — is novel in the CLIP adaptation literature. However, the paper does not theoretically investigate *why* GDA works on L2-normalized features, which would constitute deeper new knowledge.
2. **Reproducibility (well supported):** Pseudocode, code release, and simple method make this highly reproducible. However, the missing variance bars and unclear Eq. (4) create some ambiguity.
3. **Impact on Practice (partially supported):** The method's 1.6-second training time is genuinely useful for rapid deployment. However, the reliance on a full precision matrix (O(D²) storage) could be limiting for very high-dimensional features.

### Proposed Research Experiments

**P0 Experiment: EM Covariance Correction**
- **Target Claim:** Unsupervised learning performance (E5)
- **Hypothesis:** Correcting Eq. (8) to standard responsibility-weighted GMM will improve or maintain performance while being statistically principled.
- **Minimal Design:** Replace Eq. (8) as suggested, re-run Table 5 experiments on all 11 datasets.
- **Controls/Baselines:** Same as Table 5 (CLIP, POUF, UPL).
- **Metrics:** Top-1 accuracy, per-dataset delta.
- **Success Criterion:** Performance is not significantly degraded (within 0.5%) and the formulation is theoretically cleaner.
- **Estimated Cost/Time:** < 1 GPU-hour (single RTX 3090).
- **Expected Paper-Quality Gain:** Fixes a theoretical flaw; improves reproducibility and rigor.

**P1 Experiment: Variance Reporting + Significance**
- **Target Claim:** All performance comparisons
- **Hypothesis:** Some small margins (e.g., 76.05 vs 75.83) may not be statistically significant.
- **Minimal Design:** Compute std from existing 3 seed runs; run paired t-test for key comparisons.
- **Controls/Baselines:** N/A (post-hoc analysis).
- **Metrics:** Standard deviation, p-values.
- **Success Criterion:** Clear communication of which comparisons are statistically significant.
- **Estimated Cost/Time:** 0 GPU-hours (purely analytical).
- **Expected Paper-Quality Gain:** Substantially improves scientific credibility.

**P1 Experiment: KNN Purity Analysis for Base-to-New**
- **Target Claim:** Base-to-new generalization (E4)
- **Hypothesis:** The KNN-synthesized data for new classes has moderate label noise; performance correlates with neighbor purity.
- **Minimal Design:** For each dataset, measure the fraction of KNN-retrieved neighbors that share visual/semantic similarity with the new class. Compare per-dataset H-score with purity.
- **Controls/Baselines:** Vary k (16, 32, 64, 128).
- **Metrics:** Purity (%), H-score vs k.
- **Success Criterion:** Clear relationship between neighbor quality and performance; actionable guideline for choosing k.
- **Estimated Cost/Time:** < 2 GPU-hours.
- **Expected Paper-Quality Gain:** Addresses a key conceptual concern; provides practical guidance.

**P2 Experiment: Matched-Scale Linear Probe Baseline**
- **Target Claim:** Table 7 comparison to fully-trained methods
- **Hypothesis:** A linear probe on the same ViT-L/14 CLIP features, trained on full ImageNet, would achieve higher accuracy than the reported 80.0%.
- **Minimal Design:** Train a linear classifier (no GDA) on ViT-L/14 CLIP features using the full ImageNet training set. Compare with Ours (GDA, 3.6 sec) and with the reported ResNet/DeiT baselines.
- **Controls/Baselines:** Same as Table 7.
- **Metrics:** Top-1 accuracy, training time.
- **Success Criterion:** Transparent comparison showing the value added by GDA beyond simple linear probing.
- **Estimated Cost/Time:** < 3 GPU-hours.
- **Expected Paper-Quality Gain:** Fairer comparison; quantifies GDA's benefit over naive linear probe on the same features.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

**Rationale:** The paper has a clean, well-executed idea (GDA for training-free CLIP adaptation) with strong empirical validation across 17 datasets and 5 task settings. The method is practical, reproducible, and consistently outperforms prior training-free methods. However, the score is moderated by several factors:

- **Research Value (Primary dimension, weighted heavily):** The core idea is useful and the empirical demonstration is convincing. However, the theoretical foundation has gaps (Gaussian assumption for normalized CLIP features, unclear Eq. (4) derivation, non-standard EM weighting) that reduce the depth of new knowledge contributed.
- **Novelty:** Applying GDA to CLIP features is a simple but effective idea that appears novel in the CLIP adaptation literature. However, independent verification of novelty claims is deferred (Retrieval-Disabled Mode). The method's relationship to existing training-free cache models (Tip-Adapter, APE) could be more clearly delineated.
- **Validity/Soundness:** The experiments are extensive and the trends are consistent. The missing variance bars and lack of significance testing are notable gaps that prevent full confidence in the competitive claims (76.05 vs 75.83). Several formula-level issues (Eq. 4, Eq. 8) need clarification.
- **Reproducibility:** Good — code is released, pseudocode is provided, and the method requires minimal compute. The unclear precision estimator formula is a minor obstacle.

**Post-Revision Target: [7.5, 8.0]/10**

If the authors address the P0 and P1 items (Eq. (4) justification, EM covariance fix, variance reporting, Gaussian assumption discussion, failure case analysis, Table 7 reframing), the paper would be significantly strengthened. The core empirical contribution is solid and with these fixes to theoretical rigor and presentation, the paper would merit a higher score in the range of 7.5-8.0/10.