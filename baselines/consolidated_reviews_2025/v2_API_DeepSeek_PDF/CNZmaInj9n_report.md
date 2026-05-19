## Summary
# Final Review Report

## Summary

This paper proposes a unified perspective on stochastic Shapley value estimators and introduces SimSHAP, a simple amortized estimator. The authors show that existing estimators (semivalue, least squares value/KernelSHAP) can be expressed as linear transformations of importance-sampled subset values. They further unify amortized estimators (FastSHAP, etc.) as fitting problems with different metric matrices. Building on this framework, SimSHAP uses an identity metric matrix (M=I) with an unbiased l2 objective, eliminating the constrained optimization required by FastSHAP. Experiments on three tabular datasets and CIFAR-10 demonstrate that SimSHAP achieves comparable accuracy to FastSHAP with competitive inference speed.

The paper's main conceptual contribution is the unified perspective connecting disparate Shapley estimation strategies. SimSHAP itself is an incremental simplification of FastSHAP rather than a fundamentally new approach. The empirical evaluation is generally well-structured but has notable gaps in statistical rigor and analysis of trade-offs. The paper is clearly written and technically sound within its stated scope.

## Strengths
1. **Novel unified perspective.** The paper's primary contribution is a clean unifying framework showing that stochastic Shapley estimators (semivalue, least squares value) and amortized estimators share a common structure as linear transformations of sampled subset values. This framework is clearly presented through Definition 2 and Table 1, and successfully reveals the explicit connections between methods previously treated separately.

2. **Clear mathematical exposition.** The derivations linking semivalue, least squares value, and the proposed Sim-Semivalue are well-structured and logically sound. The equivalence proof between least squares value and semivalue (Proposition 1, Appendix A.1) is thorough, and the matrix-form derivation provides a compact, elegant representation.

3. **Simplicity-driven method design.** SimSHAP's design principle — removing the constrained optimization and post-hoc normalization required by FastSHAP — is well motivated. The unbiased fitting target (Eq. 14) and the use of an identity metric matrix represent genuine simplifications that could make amortized Shapley estimation more accessible.

4. **Comprehensive empirical scope.** The paper evaluates on both tabular (3 datasets with 12-96 features) and image (CIFAR-10) domains, comparing against multiple baselines including non-amortized methods (KernelSHAP variants, permutation sampling) and amortized alternatives (FastSHAP). Training/inference time comparisons are provided.

5. **Ablation studies in appendix.** Appendix A.6 provides useful hyperparameter sensitivity analyses (learning rate, batch size, epochs, model width/depth) that help readers understand SimSHAP's practical behavior.

## Weaknesses
1. **Incremental novelty of SimSHAP.** While the unified perspective is a genuine conceptual contribution, SimSHAP itself is an incremental simplification of FastSHAP — replacing the weighted least squares norm with an identity metric and removing the explicit efficiency constraint. The paper does not provide theoretical analysis showing why this simplification is preferable (e.g., convergence guarantees, variance reduction) beyond qualitative simplicity.

2. **Lack of statistical rigor in experiments.** Tabular experiments (Fig. 2) do not report variance, confidence intervals, or significance tests. Ground truth computation uses KernelSHAP "to convergence for a given threshold" but the threshold is unspecified. Image experiments show high variance for SimSHAP's Insertion AUC (std=0.117, highest among all methods) and a clear Insertion/Deletion trade-off that is not discussed.

3. **Incomplete limitation discussion.** The Discussion section (Page 9) acknowledges only one narrow limitation (amortized model design for CNNs/ViTs). Critical limitations — surrogate model approximation error, out-of-distribution artifacts from masked inputs, limited feature dimensionality in experiments, and architecture sensitivity — are omitted entirely.

4. **Overstated claim about "no substantial differences" (Page 2).** The paper states that stochastic estimators "exhibit no substantial differences," which is too strong. While they share structural commonalities, practical differences in sampling distributions, variance properties, and finite-sample behavior remain substantial.

5. **Higher training cost for image data.** SimSHAP requires 3.3x more training time than FastSHAP on CIFAR-10 (324 vs 98 minutes), which is acknowledged but under-emphasized. The practical advantage is primarily in inference speed, not overall efficiency.

6. **Unified perspective not fully leveraged.** The paper introduces the unified framework but does not use it to derive new theoretical insights (e.g., optimal sampling distributions, variance-minimizing transformations) or to improve existing methods. The framework remains primarily a descriptive taxonomy.

## Key Issues
### Issue 1 (Major): Statistical rigor gap in tabular experiments
**Location:** Page 7 - Section 4.1.2 Quantitative Experiments  
**Risk:** Readers cannot assess whether accuracy differences between methods are meaningful or within noise. Ground truth computation details (convergence threshold, number of samples) are not reported.  
**Fix:** Add standard deviations to Fig. 2, specify convergence threshold for ground truth, and add significance tests (e.g., paired t-test) for key comparisons.

### Issue 2 (Major): SimSHAP's metric choice (M=I) lacks theoretical justification
**Location:** Page 5 - Section 2.4 SimSHAP  
**Risk:** The core design difference from FastSHAP is presented as a simplicity-motivated heuristic without analysis of how the metric choice affects convergence, bias-variance trade-off, or noise sensitivity.  
**Fix:** Add theoretical or empirical analysis comparing M=I vs M=X^T W X — e.g., discuss the effect on gradient dynamics, condition number, and finite-sample behavior.

### Issue 3 (Major): Overstated claim about "no substantial differences" among estimators
**Location:** Page 2 - Introduction paragraph 3  
**Risk:** This absolute claim may trigger reviewer pushback since the unified form does not imply practical equivalence.  
**Fix:** Rephrase to acknowledge structural commonality alongside practical diversity in sampling distributions and finite-sample properties.

### Issue 4 (Major): Incomplete limitation discussion
**Location:** Page 9 - Section 5 Discussion  
**Risk:** Only one limitation acknowledged (amortized model design). Missing: surrogate model error, OOD masking artifacts, dimensionality scaling limits, architecture sensitivity.  
**Fix:** Expand to 4-5 substantive limitations with concrete scope boundaries.

### Issue 5 (Minor): Insertion/Deletion trade-off not discussed
**Location:** Page 9 - Section 4.2.3 Quantitative Experiments  
**Risk:** SimSHAP has best Insertion AUC but second-best Deletion AUC, with high variance. The narrative overstates advantages by selectively emphasizing Insertion AUC.  
**Fix:** Add explicit trade-off analysis, explain why methods differ across metrics, and report per-image variability.

### Issue 6 (Minor): Contribution C3 is performance-only
**Location:** Page 2 - Contribution list  
**Risk:** "Consistent efficiency improvement" describes experimental outcomes, not a conceptual contribution.  
**Fix:** Merge C3 into C2 or rephrase as an empirical validation claim.

## Actionable Suggestions
### S1 (Must) — Add statistical rigor to tabular experiments
**Target:** Page 7 - Section 4.1.2  
**Action:** 
- Report mean±std over at least 5 random seeds for all l1/l2 distance measurements in Fig. 2.
- Specify the exact convergence threshold for KernelSHAP ground truth (e.g., "l2 change < 0.01 over 2000 samples").
- Add a paired significance test (t-test or Wilcoxon) for SimSHAP vs FastSHAP on each dataset.  
**Expected benefit:** Readers can assess whether accuracy differences are statistically meaningful.

### S2 (Must) — Justify or analyze the identity metric choice
**Target:** Page 5 - Section 2.4  
**Action:** Add a paragraph comparing M=I vs M=X^T W X. At minimum:
- Discuss how M=I changes the loss landscape (gradients are in Shapley-value space vs subset-value space).
- Show whether M=I leads to different finite-sample bias or convergence rate.
- Empirical comparison: train SimSHAP with both M=I and M=X^T W X (FastSHAP's metric) and report accuracy.  
**Expected benefit:** Validates the core design choice and strengthens the paper's methodological contribution.

### S3 (Must) — Rephrase "no substantial differences" claim
**Target:** Page 2 - Introduction paragraph 3  
**Action:** Replace with: "We observe that these strategies share a common underlying structure..." Keep the unified perspective claim but acknowledge practical diversity.  
**Expected benefit:** Avoids reviewer pushback and presents a more defensible, nuanced contribution.

### S4 (Must) — Expand limitation discussion
**Target:** Page 9 - Section 5  
**Action:** Add at least 3 additional limitations: (1) surrogate model approximation error, (2) out-of-distribution artifacts from feature masking, (3) scaling limits to very high dimensions (>1000 features). For each, state one concrete scope boundary.  
**Expected benefit:** Strengthens scientific rigor and preempts reviewer criticism.

### S5 (Nice-to-have) — Rewrite qualitative evaluation section
**Target:** Page 8 - Section 4.2.2  
**Action:** Move qualitative discussion after quantitative results. Remove conclusive phrasing ("one may conclude that SimSHAP is a promising method") and present examples as illustrations, not evidence.  
**Expected benefit:** Separates anecdotal observation from rigorous evaluation.

### S6 (Nice-to-have) — Improve contribution structure
**Target:** Page 2 - Contribution list  
**Action:** Merge C3 into C2. Change to two contributions: (1) Unified perspective, (2) SimSHAP with unbiased l2 training + empirical validation.  
**Expected benefit:** Cleaner contribution narrative that focuses on conceptual novelty rather than experimental outcomes.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows a standard pattern: (P1) deep learning success + interpretability problem -> Shapley values as solution -> computational challenge, (P2) literature survey of acceleration methods, (P3) unified perspective + SimSHAP proposal + contribution list. This works but has room for improvement in narrative coherence and reader engagement.

### Proposed Abstract Outline (Complete)

**S1 (Problem):** "Shapley values provide axiomatically grounded feature attributions for black-box models but require summing over an exponential number of feature subsets, making exact computation intractable."

**S2 (Gap):** "Existing stochastic and amortized estimators — including ApproSemivalue, KernelSHAP, and FastSHAP — differ in their sampling and optimization strategies, but their structural relationships are not well understood, hindering systematic improvement and algorithm selection."

**S3 (Method):** "We show that all these estimators can be unified as linear transformations of importance-sampled subset values, and that amortized estimators correspond to metric-space fitting problems. Leveraging this insight, we propose SimSHAP, which minimizes an unbiased l2 objective in Euclidean space, eliminating the constrained optimization required by prior amortized methods."

**S4 (Result):** "Experiments on tabular datasets (12–96 features) and CIFAR-10 show that SimSHAP achieves accuracy comparable to FastSHAP with orders-of-magnitude faster inference than non-amortized methods."

**S5 (Bounded conclusion):** "Our results suggest that a simple identity-metric formulation suffices for amortized Shapley estimation, offering a practical and transparent alternative for real-time explanation."

### Proposed Introduction Outline (Complete)

**P1 (Stakes and problem):** "The lack of interpretability in deep neural networks limits their use in high-stakes domains. Shapley values provide a unique axiomatically-grounded attribution mechanism, but exact computation requires O(2^d) subset evaluations, making it prohibitive for high-dimensional inputs."

**P2 (Gap — what is missing):** "Numerous acceleration methods have been proposed, ranging from importance-sampled semivalues to amortized neural estimators like FastSHAP. However, the structural relationships among these methods remain unclear, making it difficult to identify which algorithmic components are essential and which are incidental."

**P3 (Solution — unified perspective):** "In this paper, we show that disparate stochastic estimators share a common structure: each can be expressed as a linear transformation T·E[a^S·v(S)] + b transformation of sampled subset values. Amortized estimators similarly differ only in their metric matrix M. This unified lens reveals that many design choices (e.g., constrained vs. unconstrained optimization) are incidental."

**P4 (SimSHAP and key evidence):** "Based on this understanding, we propose SimSHAP — the simplest instantiation of the unified framework, using M=I and an unbiased l2 objective. SimSHAP matches or exceeds FastSHAP accuracy on tabular and image benchmarks while requiring no post-hoc normalization."

**P5 (Contributions):** "Our contributions are: (1) a unified perspective connecting stochastic and amortized Shapley estimators through linear transformations and metric-space fitting; (2) SimSHAP, a minimal amortized estimator with unbiased l2 training-time efficiency gains; and (3) empirical validation across diverse data modalities."

### Alignment Check

| Check | Pass? | Notes |
|---|---|---|
| Problem alignment (challenge matches solution) | Yes | The unified perspective directly addresses the "lack of structural understanding" gap. |
| Variable alignment (intro concepts appear as method variables) | Yes | T, a^S, b, M all appear in Method section. |
| Contribution-evidence alignment (claims supported by experiments) | Partial | C1 (unified perspective) is conceptually supported; C2 (SimSHAP) is empirically validated but lacks metric-choice analysis; C3 (efficiency) conflates experiment with contribution. |

## Priority Revision Plan
### Ranked Error Board (Top 5)

| Rank | Issue | Severity | Research-Value Impact | Verifiability | Fixability | Confidence |
|------|-------|----------|----------------------|--------------|------------|------------|
| 1 | Statistical rigor gap in tabular experiments | Major | High — undermines reliability of empirical claims | High | Easy (add variance bars + significance tests) | High |
| 2 | Metric choice (M=I) lacks analysis | Major | Medium — weakens methodological contribution | High | Moderate (add analysis section) | High |
| 3 | Overstated "no substantial differences" claim | Major | Medium — reviewer pushback risk | High | Easy (rephrase) | High |
| 4 | Incomplete limitation discussion | Major | Medium — affects scientific completeness | High | Easy (expand text) | High |
| 5 | Insertion/Deletion trade-off not discussed | Minor | Low — affects interpretation but not validity | High | Easy (add discussion) | High |

### Revision Order and Expected Impact

**P0 (Must-do before next submission):**
1. Add statistical rigor to Fig. 2 and Table 3 (variance bars, significance tests) → closes Issue 1
2. Rephrase "no substantial differences" to "share a common structure" → closes Issue 3
3. Expand limitation section to 4-5 substantive points → closes Issue 4

**P1 (Should-do for strong revision):**
4. Add analysis of identity metric choice (M=I vs M=X^T W X) → closes Issue 2
5. Restructure contributions to 2 items (merge C3 into C2) → closes Issue 6

**P2 (Nice-to-have for polish):**
6. Rewrite qualitative evaluation as illustration rather than evidence → closes Issue 5
7. Improve abstract conciseness following the S1-S5 outline provided above

### Expected Quality Gains After P0 Revisions
- Scientific credibility: significantly improved (variance reporting + bounded claims)
- Novelty perception: improved (clearer unified perspective framing, less overclaim)
- Reviewer resistance: reduced (honest limitations + defensible language)
- Score uplift: approximately +1.5–2 points on a 10-point scale (from ~5.5 to ~7.0-7.5)

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|----------------|-------------------|
| E1 | Tabular accuracy (Census) | 12 features, LightGBM+MLP surrogate, M=64 samples | l1/l2 distance to KernelSHAP ground truth | SimSHAP ≈ FastSHAP accuracy | C2 | No variance bars, threshold not specified |
| E2 | Tabular accuracy (News) | 60 features, same setup | l1/l2 distance | SimSHAP ≈ FastSHAP accuracy | C2 | Same limitation |
| E3 | Tabular accuracy (Bankruptcy) | 96 features, same setup | l1/l2 distance | SimSHAP ≈ FastSHAP accuracy | C2 | Same limitation |
| E4 | Image Insertion AUC | CIFAR-10, ResNet-18, 8 samples, U-Net explainer | Insertion AUC (↑) | SimSHAP 0.757 (best) | C2 | High std (0.117); trade-off w/ Deletion not discussed |
| E5 | Image Deletion AUC | Same as E4 | Deletion AUC (↓) | SimSHAP -0.302 (2nd) | C2 | KernelSHAP better (-0.443); trade-off untested |
| E6 | Inference speed | All datasets | Inference time (s) | SimSHAP fastest (0.001-0.086s) | C2 | Gradient methods not applicable on tabular |
| E7 | Training speed | All datasets | Training time (min) | SimSHAP faster on tabular, 3.3x slower on CIFAR-10 | C2 | Cause not fully analyzed |
| E8 | Ablation: learning rate | Bankruptcy | l1/l2 distance | Best at 7e-4 | C2 | Single dataset only |
| E9 | Ablation: batch size | Bankruptcy | l1/l2 distance | Larger batch helps | C2 | Single dataset only |
| E10 | Ablation: model width/depth | Bankruptcy | l1/l2 distance | 3-layer MLP sufficient | C2 | Single dataset only |
| E11 | Limited data robustness | CIFAR-10 | Ins/Del AUC | Acceptable with 20% data | C2 | Lacks systematic data scaling analysis |

### Research-Theme Gap Diagnosis

1. **New knowledge gap**: The unified perspective (C1) offers conceptual novelty, but the paper does not extract actionable insights from it (e.g., optimal sampling distributions, variance bounds). The framework is descriptive rather than generative.

2. **Reproducibility gap**: Ground truth thresholds, random seed counts, and specific convergence criteria are not reported, making exact replication difficult.

3. **Robustness gap**: No out-of-distribution evaluation, no perturbation sensitivity analysis, no failure-case analysis. Robustness claims rely on single-dataset ablations.

### Proposed Research Experiments

**P0 Experiment: Statistical rigor addition**
- **Target Claim:** SimSHAP achieves comparable accuracy to FastSHAP.
- **Hypothesis:** Observed accuracy differences are within noise.
- **Design:** Run all tabular experiments with 10 random seeds, report mean±std, and conduct paired t-tests (SimSHAP vs FastSHAP per dataset).
- **Control:** Same surrogate model, same samples, matched seed sequences.
- **Metrics:** l1/l2 mean difference, p-value, effect size (Cohen's d).
- **Success Criterion:** p > 0.05 or effect size < 0.2 for all datasets.
- **Cost:** ~1 GPU-day (mostly re-runs).
- **Quality Gain:** High — directly closes the primary validity concern.

**P1 Experiment: Metric matrix comparison**
- **Target Claim:** M=I is a suitable choice for the amortized estimator.
- **Hypothesis:** M=I and M=X^T W X yield similar accuracy, but M=I trains faster.
- **Design:** Train SimSHAP with both M=I and M=X^T W X (keeping all else equal) on one tabular dataset (News, 60 features) and CIFAR-10. Compare accuracy, convergence speed, and variance.
- **Control:** Same explainer architecture, number of samples, optimizer, epochs.
- **Metrics:** l1/l2 distance, training loss curves, final Insertion/Deletion AUC.
- **Success Criterion:** M=I achieves within 5% of M=X^T W X accuracy with faster per-epoch training.
- **Cost:** ~2 GPU-days.
- **Quality Gain:** High — directly validates the core methodological contribution.

**P2 Experiment: Scaling to higher dimensions**
- **Target Claim:** SimSHAP works for moderate feature dimensions (≤96).
- **Hypothesis:** Performance degrades at very high dimensions (>500 features).
- **Design:** Evaluate on a high-dimensional tabular dataset (e.g., genomics with ~2000 features) comparing SimSHAP vs FastSHAP vs KernelSHAP with budget-matched samples.
- **Control:** Same surrogate architecture, same sample count, same evaluation protocol.
- **Metrics:** l1/l2 distance to reference (KernelSHAP at high sample count), training time, inference time.
- **Success Criterion:** Identifies practical dimension limit and characterizes degradation pattern.
- **Cost:** ~3 GPU-days.
- **Quality Gain:** Medium — establishes clear scope boundaries.

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 (Must): Statistical Rigor
  └── Add variance bars + significance tests to all tabular experiments
  └── Specify ground truth convergence threshold
  └── Expected: increased validity confidence

P1 (Should): Metric Choice Analysis
  └── Compare M=I vs M=X^T W X on News + CIFAR-10
  └── Convergence curves + final accuracy
  └── Expected: validates core design choice

P2 (Nice): Dimensionality Scaling
  └── Evaluate on high-dim dataset (>500 features)
  └── Identify practical limits
  └── Expected: clearer scope boundaries
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 5.5 / 10

**Rationale (research value + novelty prioritized):**

- **Research value (5/10):** The unified perspective connecting stochastic estimators is a useful conceptual contribution that clarifies relationships among Shapley estimation methods. However, the framework remains primarily descriptive — it does not yield new theoretical results, optimal sampling strategies, or variance bounds. The paper's practical contribution (SimSHAP) is an incremental simplification of FastSHAP without clear evidence of superiority beyond comparable accuracy.
  
- **Novelty (5/10):** The unified view is the strongest novelty element. SimSHAP's design (M=I, unconstrained optimization) is a straightforward simplification of existing amortized methods. External novelty verification is deferred due to retrieval constraints in this run, but the paper's own literature review suggests that similar amortized frameworks exist (Schwarzenberg et al., CoRTX), which the authors acknowledge in Appendix A.9.

- **Soundness (6/10):** The mathematical derivations are correct and well-structured. Experimental methodology is reasonable but lacks statistical rigor (no variance bars, no significance tests) and has notable gaps in analysis (metric choice justification, trade-off discussion). The code should be made available.

- **Reproducibility (5/10):** Key experimental details are provided (datasets, splits, model architectures, hyperparameters in appendix), but ground truth computation is incompletely specified, random seed count is not reported, and variance estimates are missing.

### Post-Revision Target: [7.0, 7.5] / 10

**Expected after P0 revisions (statistical rigor, bounded claims, expanded limitations):** 7.0/10  
**Expected after P0+P1 revisions (add metric analysis + P0 items):** 7.5/10

**Conditions for higher score (>7.5):** Achieving >7.5 would require either (a) extracting new theoretical insights from the unified framework (e.g., optimal sampling distributions), or (b) demonstrating clear empirical superiority of SimSHAP over FastSHAP (not just comparable accuracy) through more extensive evaluation including high-dimensional and OOD settings.