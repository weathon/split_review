## Summary
# Final Review Report

## Summary

This paper presents MUBEN, a benchmark evaluating eight uncertainty quantification (UQ) methods across four pre-trained molecular representation backbones (ChemBERTa, GROVER, Uni-Mol, DNN) and two supplementary backbones (TorchMD-NET, GIN) on 14 MoleculeNet property prediction tasks. The study covers both classification and regression, using scaffold splitting to create out-of-distribution test sets. The main findings are: (1) Deep Ensembles consistently improves both prediction and calibration but at high computational cost; (2) Temperature Scaling and MC Dropout are efficient alternatives for classification; (3) Bayesian methods (BBP, SGLD) show good regression NLL/CE but with caveats; (4) Uni-Mol achieves the best predictive accuracy but poorest calibration.

**Overall assessment:** The benchmark is timely and addresses a genuine gap in the literature. The experimental scope (4 primary backbones × 8 UQ methods × 14 datasets) is substantial. However, several methodological issues reduce confidence in the conclusions: (a) Uni-Mol's multi-conformer inference (11 representations/molecule) creates an unfair comparison advantage not controlled for; (b) no statistical significance testing is performed; (c) the "BBP/SGLD excel at regression" conclusion is undermined by contradictory evidence within the paper itself; (d) the backbone comparison confounds architecture, pre-training data, and inference strategy. With revisions, this could be a useful reference benchmark for the molecular ML community.

## Strengths
1. **Timely and relevant benchmark scope.** The paper addresses a genuine gap: how to select compatible UQ methods for modern pre-trained molecular representation models. With 4 primary backbones × 8 UQ methods × 14 datasets, the experimental coverage is substantial and useful for practitioners.

2. **Clear categorization of UQ methods.** The paper organizes UQ methods into four families (deterministic, Bayesian neural networks, post-hoc calibration, ensembles) and applies them consistently across backbones. This structured comparison allows readers to identify cross-cutting trends (e.g., Ensembles working well everywhere, Temperature Scaling being cost-effective for classification).

3. **Use of scaffold splitting.** The adoption of scaffold splitting (rather than random) creates a challenging out-of-distribution evaluation that better reflects real-world molecular discovery scenarios. This is a principled design choice that increases the practical relevance of the findings.

4. **Frozen backbone ablation.** The analysis of frozen backbone weights (Table 3) provides useful insight into whether pre-trained models serve primarily as feature extractors or require fine-tuning for UQ. The finding that frozen backbones improve regression calibration at the cost of accuracy is an interesting trade-off worth exploring further.

5. **Well-documented appendix.** The appendix provides extensive dataset statistics, implementation details, and full result tables, supporting reproducibility. The resource analysis table (Table 6) is particularly useful for practitioners choosing UQ methods under computational constraints.

6. **Multi-task and multi-domain coverage.** Including physiology, biophysics, physical chemistry, and quantum mechanics datasets allows testing whether UQ findings generalize across molecular property types — a strength over prior benchmarks that focused on narrower domains.

## Weaknesses
1. **Uni-Mol multi-conformer inference creates an unfair comparison (MAJOR).** Uni-Mol averages logits from 11 molecular representations (10 3D conformations + 1 2D graph) at inference time, while other backbones use single-pass inference. This is equivalent to an implicit ensemble and confounds any "superior representation capability" claim. The paper attributes Uni-Mol's performance to "large network size, various pre-training data and tasks, and integration of results from different conformations" but does not disentangle the last factor. A controlled ablation with single-conformer Uni-Mol inference is essential.

2. **No statistical significance testing.** All backbone-UQ comparisons are based on macro-averaged rankings without standard errors, confidence intervals, or significance tests. For close comparisons (e.g., GROVER vs ChemBERTa on several metrics), overlapping standard deviations from per-dataset tables (appendix) suggest many differences may not be statistically reliable. The paper's hierarchical ranking system compresses this uncertainty.

3. **BBP/SGLD regression claim is internally contradictory.** The paper states BBP and SGLD "deliver commendable performance in predicting regression uncertainty" while simultaneously reporting that (a) their RMSE/MAE do not consistently improve, (b) their predicted variances correlate poorly with actual error, and (c) their low NLL may result from variance inflation rather than meaningful calibration. The paper's own conclusion ("better suited for regression UQ") overstates what the evidence supports.

4. **Introduction relies on dense citation lists.** Multiple paragraphs in the introduction and related work (Page 1, lines 42-50; Page 2-3) present long citation lists without categorization, critical assessment, or connection to the paper's specific contributions. This reduces readability and weakens the gap-narrative.

5. **Abstract lacks concrete findings.** The abstract identifies the gap and introduces MUBEN but does not preview any quantitative results or actionable conclusions. For a benchmark paper, the abstract should communicate the main practical recommendations.

6. **Positioning against prior benchmarks is qualitative.** The related work section claims MUBEN "covers a more diverse suite of tasks, stronger pre-trained molecular representation models, and a more comprehensive set of UQ methods" than prior benchmarks. However, no comparison table is provided, and the claim is not quantitatively supported.

7. **Regression label normalization could have leakage risk.** The paper normalizes regression labels to standard Gaussian before training using "label mean and variance from the training set." The exact procedure is not fully specified — if dataset-level (including test) statistics are used, this would constitute data leakage. The ambiguity should be resolved.

8. **ToxCast's 617-task multi-task setup receives insufficient discussion.** Temperature Scaling assigns individual temperatures per task (617 parameters on a small validation set), and Deep Ensembles uses 617×M output heads. The paper does not discuss how extreme multi-task learning interacts with UQ evaluation, potentially biasing results on this dataset.

## Key Issues
### Issue 1 (Critical/Major): Uni-Mol multi-conformer inference confound

**Location:** Page 4 - Backbone Models paragraph (Uni-Mol description)

**Problem:** Uni-Mol uses 11 molecular representations per molecule at inference with logit averaging — an implicit ensemble not applied to any other backbone. The paper attributes Uni-Mol's superior performance to "molecular representation capability" but this cannot be disentangled from the ensembling effect.

**Evidence:** Page 4 text states Uni-Mol "generates 10 sets of 3D conformations... supplemented with an additional 2D molecular graph... For inference, we average the logits from all 11 representations."

**Impact:** Invalidates the claim that Uni-Mol has superior "representation capability" across all comparisons. The benchmark's primary finding about backbone ranking may be artifacts of unequal inference budgets.

**Fix requirement (Must):** Report Uni-Mol results with single-conformer inference. Add an ablation experiment comparing multi-conformer Uni-Mol vs single-conformer Uni-Mol vs other backbones with multi-view ensembling.

---

### Issue 2 (Major): No statistical significance testing

**Location:** Page 5-7 - Results and Analysis

**Problem:** All backbone-UQ rankings are based on macro-averaged ranks without confidence intervals or significance tests. Per-dataset tables in the appendix show overlapping standard deviations for many comparisons.

**Evidence:** Table 1 appendix Tables 9-16 show standard deviations overlapping across method comparisons on multiple datasets (e.g., BACE: DNN-Deterministic 0.8185±0.0164 vs DNN-MC Dropout 0.8168±0.0121).

**Impact:** The ranking-based narrative may overstate differences that are within noise. Readers cannot assess which comparisons are reliable.

**Fix requirement (Must):** Add paired significance tests (e.g., Wilcoxon signed-rank across datasets) or critical difference diagrams (Demšar, 2006) for the primary comparisons. Report effect sizes.

---

### Issue 3 (Major): BBP/SGLD regression conclusion overreaches evidence

**Location:** Page 8 - UQ Performance paragraph; Page 9 - Conclusion

**Problem:** The paper claims BBP and SGLD are "better suited for regression UQ" but the evidence is self-contradictory: they improve NLL/CE without improving RMSE/MAE, and their predicted variances do not correlate with error. Low NLL can be an artifact of variance inflation — a Gaussian with very large variance will always have low NLL because the squared error term $(y-\hat{y})^2/\hat{\sigma}^2$ is divided by a large number.

**Evidence:** Page 8 lines 74-78: "Yet, their inconsistent improvement of RMSE and MAE implies a greater influence on variance prediction than mean... we do not observe a better correlation between SGLD's error and variance."

**Impact:** Practitioners who follow this recommendation may end up with large-variance predictions that are not useful for decision-making under uncertainty.

**Fix requirement (Must):** Add variance-error correlation analysis (Spearman ρ between predicted σ and |error|). Revise conclusion to reflect the caveats. Consider reporting the "useful uncertainty" metrics like coverage of prediction intervals.

---

### Issue 4 (Major): Related-work positioning lacks quantitative evidence

**Location:** Page 3 - UQ Related Work paragraph

**Problem:** The paper claims MUBEN "covers a more diverse suite of tasks, stronger pre-trained molecular representation models, and a more comprehensive set of UQ methods" than prior benchmarks (Hirschfeld 2020, Scalia 2020, Wollschläger 2023). No comparison table supports this.

**Impact:** The novelty claim is unsubstantiated. The contribution as a "comprehensive benchmark" cannot be evaluated without understanding what prior benchmarks cover.

**Fix requirement (Nice-to-have):** Add a comparison table of existing UQ benchmarks: datasets, #backbones, #UQ methods, tasks, split strategy, evaluation metrics.

---

### Issue 5 (Major): Abstract lacks quantitative preview

**Location:** Page 1 - Abstract

**Problem:** The abstract ends with "offers insights for selecting UQ for backbone models" without previewing what those insights are.

**Impact:** Readers cannot quickly assess the benchmark's findings. The abstract should serve as a standalone summary of the paper's actionable conclusions.

**Fix requirement (Must):** Revise abstract to include 2-3 concrete findings (e.g., which UQ methods work best for which backbone/task type).

## Actionable Suggestions
### S1: Add Uni-Mol single-conformer ablation (P0 - Must)

**Problem:** The multi-conformer ensembling confound makes Uni-Mol's claimed superior "representation capability" unverifiable.

**Action:** Repeat the Uni-Mol experiments with single-conformer inference (randomly select one of the 11 representations at test time, or average over 3 instead of 11). Report the delta between single-conformer and multi-conformer Uni-Mol results.

**Location:** Section 4.1 (Backbone Models) and Section 5 (Results).

**Expected benefit:** Isolates the contribution of multi-conformer ensembling from backbone representation quality. If single-conformer Uni-Mol still outperforms other backbones, the claim is strengthened. If not, the paper must revise its conclusions about backbone ranking.

---

### S2: Add statistical significance analysis (P0 - Must)

**Problem:** No significance testing across the benchmark comparisons.

**Action:** Compute Wilcoxon signed-rank tests or paired bootstrap across datasets for the primary comparisons (Deep Ensembles vs deterministic, each UQ method vs baseline). Add a critical difference diagram (Demšar, 2006 style) for the main ranking tables. Report the proportion of datasets where each method is strictly better.

**Location:** Add to Section 5 (Results). Add a new subsection "Statistical Significance."

**Expected benefit:** Provides readers with confidence intervals on the rankings. Prevents over-interpretation of small differences.

---

### S3: Revise BBP/SGLD regression conclusion (P0 - Must)

**Problem:** The conclusion overstates evidence for BBP/SGLD in regression.

**Action:** 
(1) Add a variance-error correlation analysis: for each regression dataset, compute Spearman correlation between predicted $\hat{\sigma}$ and absolute error $|y-\hat{y}|$ for BBP, SGLD, Deterministic, and Ensembles. Report as a table.
(2) Add prediction interval coverage analysis: report what fraction of test points fall within the 50%, 80%, 95% predicted intervals.
(3) Revise the conclusion from "BBP and SGLD are better suited for regression UQ" to "BBP and SGLD achieve lower NLL and CE on regression tasks, but this owes primarily to variance inflation rather than improved mean prediction or variance-error correlation."

**Location:** Section 5 (UQ Performance) and Section 6 (Conclusion).

**Expected benefit:** Aligns claims with evidence. Prevents misleading practitioners.

---

### S4: Add prior benchmark comparison table (P1 - Nice-to-have)

**Problem:** Positioning claim (MUBEN covers "more") is qualitative and unverifiable.

**Action:** Add a comparison table: | Benchmark | # Datasets | # Backbones | # UQ Methods | Task Types | Split Strategy | Pretrained Models? |. Compare MUBEN with Hirschfeld 2020, Scalia 2020, Wollschläger 2023, Hwang 2020.

**Location:** Section 2 (Related Work).

**Expected benefit:** Substantive evidence for the benchmark's incremental contribution.

---

### S5: Clarify regression label normalization (P1 - Must)

**Problem:** Z-score normalization of regression labels could use dataset-level statistics if not carefully implemented.

**Action:** Add one sentence in Section 4.4 specifying "The z-score parameters $\mu$ and $\sigma$ are computed from the training split only: $\mu_{train} = \frac{1}{N_{train}}\sum_{n\in train} y_n$, and analogously for $\sigma_{train}$."

**Location:** Section 4.4 (Training and Evaluation Protocols).

**Expected benefit:** Resolves a critical reproducibility concern.

---

### S6: Discuss ToxCast multi-task effects (P1 - Nice-to-have)

**Problem:** 617 tasks on a small dataset creates multi-task learning dynamics that may affect UQ evaluation.

**Action:** Add a paragraph in Section 4.3 discussing: (a) how Temperature Scaling handles 617 independent temperatures; (b) whether per-task UQ metrics are reliable with few positive samples per task; (c) sensitivity analysis without ToxCast.

**Location:** Section 4.3 (Datasets) or Appendix.

**Expected benefit:** Provides confidence that benchmark results are not driven by a single extreme dataset.

---

### S7: Revise abstract to include concrete findings (P0 - Must)

**Action:** Replace the final generic sentence with 2-3 specific findings. See annotation on Page 1 for a complete revised version.

**Location:** Abstract.

**Expected benefit:** Makes the paper more discoverable and useful as a reference.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current storyline is: Molecular representation is important → Pre-trained models are powerful but overconfident → Prior UQ work has limitations → MUBEN fills the gap → Results show specific trends → Conclusion. This is functional but the introduction and abstract could better serve the reader by previewing concrete findings earlier.

### Abstract Outline (Revised)

**S1 (Problem + Domain):** Large molecular representation models pre-trained on unlabeled data achieve strong predictive performance but exhibit systematic overconfidence on out-of-distribution samples, motivating the use of uncertainty quantification (UQ).

**S2 (Gap):** While several UQ methods exist and prior studies have explored UQ for molecular property prediction, no comprehensive benchmark evaluates UQ across multiple pre-trained backbones with different molecular descriptors under consistent conditions.

**S3 (Solution):** We present MUBEN, a benchmark evaluating eight UQ methods (deterministic, BBP, SGLD, MC Dropout, SWAG, Temperature Scaling, Focal Loss, Deep Ensembles) on four pre-trained backbones (ChemBERTa, GROVER, Uni-Mol, DNN) across 14 MoleculeNet classification and regression tasks.

**S4 (Key Findings):** Deep Ensembles consistently improves both accuracy and calibration but incurs substantial computational cost. Temperature Scaling and MC Dropout are efficient alternatives for classification. BBP and SGLD achieve lower NLL on regression tasks, though this stems partly from variance inflation rather than improved mean prediction. Among backbones, Uni-Mol achieves the highest predictive accuracy but exhibits the poorest calibration.

**S5 (Implication):** These results provide practical guidance for selecting UQ methods in molecular property prediction and highlight the need for fairer backbone comparisons that control for inference-time ensembling.

### Introduction Outline (Revised)

**P1 — Motivation and Stakes:** Molecular property prediction accelerates drug discovery and materials design, but supervised learning requires expensive labels. Pre-trained molecular representation models offer a solution but introduce a new problem: systematic overconfidence on out-of-distribution data, which undermines their utility in high-stakes screening scenarios.

*Key claim: Accuracy alone is insufficient; calibrated uncertainty estimates are essential for reliable molecular property prediction.*

**P2 — Prior UQ Work and Its Limitations:** Prior work has applied UQ to molecular prediction (e.g., post-hoc calibration of MPNNs, evidential deep learning, Bayesian optimization). However, these studies share three limitations: limited UQ method variety, narrow task scope, and absence of modern pre-trained backbones.

*Key claim: A systematic evaluation of UQ across pre-trained backbones is lacking.*

**P3 — MUBEN and Contributions:** We present MUBEN, a unified benchmark covering 8 UQ methods × 4 primary backbones × 14 datasets. This allows us to answer: Which UQ methods work best for which backbone and task type? How does descriptor modality affect calibration? Are Bayesian methods truly beneficial for regression uncertainty?

*Transition: The benchmark design is described in Sections 3-4. Key findings are presented in Section 5 and synthesized in Section 6.*

**P4 — Structure of Paper:** The remainder of this paper is organized as follows. Section 2 reviews related work on molecular pre-training and UQ. Section 3 formalizes the problem. Section 4 details the experiment setup. Section 5 presents results and analysis. Section 6 concludes with limitations and future directions.

### Storyline Alternative: "Finding-First" Structure

An alternative structure that better suits a benchmark paper:

1. **Abstract + Introduction:** State findings first, then describe benchmark design.
2. **Section 2:** Direct comparison table with existing benchmarks (positioning).
3. **Section 3-4:** Design and methodology (compact).
4. **Section 5:** Results organized by research question, not UQ category:
   - RQ1: Which UQ methods are most effective overall?
   - RQ2: How does backbone choice interact with UQ effectiveness?
   - RQ3: Are Bayesian methods superior for regression uncertainty? (with caveats)
   - RQ4: What is the cost-performance trade-off?
5. **Section 6:** Practical recommendations + explicit limits of the benchmark.

This structure foregrounds the actionable information for practitioners.

## Priority Revision Plan
| Priority | Task | Effort | Impact | Section |
|----------|------|--------|--------|---------|
| **P0** | Add Uni-Mol single-conformer ablation | 3-5 GPU-days | Critical — resolves unfair comparison confound | §4.1, §5 |
| **P0** | Add statistical significance tests (Wilcoxon/CD diagram) | 1 day modeling | Major — validates ranking claims | §5 |
| **P0** | Revise BBP/SGLD regression conclusion + add variance-error correlation | 2 days modeling + writing | Major — aligns claims with evidence | §5, §6 |
| **P0** | Clarify regression z-score normalization procedure | 0.5 day writing | Medium — resolves reproducibility risk | §4.4 |
| **P0** | Revise abstract to include concrete findings | 0.5 day writing | Medium — improves discoverability | Abstract |
| **P1** | Add prior benchmark comparison table | 1 day writing | Medium — substantiates positioning | §2 |
| **P1** | Restructure Related Work (descriptor-based) with UQ implications | 1 day writing | Medium — improves relevance | §2 |
| **P1** | Discuss ToxCast 617-task multi-task effects | 0.5 day writing | Low — addresses outlier concern | §4.3 |
| **P2** | Add complete per-dataset result tables in appendix (already present) | N/A | Already done | Appendix |
| **P2** | Add hyperparameter sensitivity analysis for Temperature Scaling | 2 days | Low — nice-to-have | Appendix |

### Revision Flow

```text
Stage 1 (days 1-3): P0 experiments + writing
  [Uni-Mol ablation] -> [Significance tests] -> [BBP/SGLD revision] -> [Abstract rewrite]
  Expected: resolves core validity concerns

Stage 2 (days 4-5): P1 features
  [Benchmark comparison table] -> [Related Work restructure] -> [ToxCast discussion]
  Expected: substantiates novelty claims, improves readability

Stage 3 (days 6-7): P2 polish
  [Hyperparameter sensitivity] -> [Final proofreading]
  Expected: submission-ready manuscript
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|--------------|-----------------|-------------------|
| E1 | Evaluate UQ methods for classification (scaffold split) | 4 backbones × 8 UQ methods on 8 classification datasets | ROC-AUC, ECE, NLL, Brier Score | Deep Ensembles best overall; Temperature Scaling improves calibration | UQ comparison across backbones | No significance tests; Uni-Mol confound |
| E2 | Evaluate UQ methods for regression (scaffold split) | 4 backbones × 6 UQ methods on 6 regression datasets | RMSE, MAE, NLL, CE | BBP/SGLD best NLL/CE but not RMSE/MAE | BBP/SGLD for regression UQ | Variance-error correlation missing; BBP/SGLD claim may overstate |
| E3 | Frozen backbone weights | GROVER, Uni-Mol with fixed weights | Same as E1/E2 | Prediction degrades; regression CE improves | Backbones need fine-tuning | Only 2 backbones tested; massive accuracy loss makes CE improvement moot |
| E4 | Random vs scaffold split | 4 classification + 4 regression datasets | Same as E1/E2 | Random split improves scores; changes relative rankings | Split strategy affects conclusions | Subset of datasets only |
| E5 | TorchMD-NET and GIN supplementary | 2 backbones with Deep Ensembles | Same as E1/E2 | TorchMD-NET good on QM; GIN poor | Backbone modality specialization | Only best UQ method reported; limited comparison |
| E6 | Resource analysis | All UQ methods on BBBP | Additional training/inference cost | Temperature/MC Dropout cheapest; Ensembles most expensive | UQ cost-performance trade-off | Single dataset; coarse estimates |

### Research-Theme Gap Diagnosis

**New knowledge claim:** The paper claims to provide a "comprehensive evaluation" that offers "insights for selecting UQ for backbone models." This is partially supported: the ranking tables do provide comparative data. However, three critical gaps remain:

1. **Causal attribution gap:** The claim that "Uni-Mol's superior [backbone] performance" is due to "large network size, various pre-training data and tasks" is confounded by the multi-conformer inference strategy. Without disentangling these factors, the scientific contribution about *why* certain backbones perform better is weak.

2. **Practical guidance gap:** The "insights" (Deep Ensembles works, Temperature Scaling is cheap, BBP/SGLD for regression) are partially undermined by missing statistical evidence and contradictory findings for BBP/SGLD. The practical actionability for a practitioner choosing a UQ method is reduced.

3. **Reproducibility gap:** The regression label normalization ambiguity and the missing single-conformer ablation create traceability gaps. A third party cannot fully reproduce the benchmark claims without additional implementation details.

### Proposed Research Experiments

#### P0 Experiment: Uni-Mol Ablation — Single vs Multi-Conformer

- **Target Claim:** Uni-Mol "superior molecular representation capability"
- **Hypothesis:** The gap between Uni-Mol and other backbones is partly or fully attributable to multi-conformer ensembling (11 representations → average logits).
- **Minimal Design:** (1) Uni-Mol single-conformer: randomly select 1 conformation per molecule at inference. (2) Uni-Mol 3-conformer: average over 3 randomly selected conformations. (3) Other backbones with multi-view ensembling (e.g., ChemBERTa with 11 dropout passes or augmented SMILES).
- **Controls/Baselines:** Same random seeds, same hyperparameters, same training protocol.
- **Metrics:** ROC-AUC (classification), RMSE (regression), ECE/CE (calibration).
- **Success Criterion:** If single-conformer Uni-Mol still outperforms all other backbones on ≥70% of datasets, the representation claim is supported. Otherwise, the claim must be revised.
- **Estimated Cost:** 3-5 GPU-days (A100).
- **Expected Paper-Quality Gain:** Resolves the most critical methodological confound.

#### P0 Experiment: BBP/SGLD Variance-Error Correlation

- **Target Claim:** BBP and SGLD "better suited for regression UQ"
- **Hypothesis:** The low NLL of BBP/SGLD is an artifact of variance inflation; their predicted variances do not correlate meaningfully with prediction error.
- **Minimal Design:** Compute Spearman correlation between predicted $\hat{\sigma}$ and absolute error $|y-\hat{y}|$ for all regression datasets and methods. Also compute prediction interval coverage (50%, 80%, 95%).
- **Controls/Baselines:** Deterministic (using predicted $\hat{\sigma}$ from Gaussian NLL training), Deep Ensembles.
- **Metrics:** Spearman $\rho$, interval coverage gap (nominal - actual).
- **Success Criterion:** If BBP/SGLD Spearman $\rho$ is not significantly higher than Deterministic, the "better suited" claim should be weakened.
- **Estimated Cost:** 1-2 days (CPU analysis on existing predictions).
- **Expected Paper-Quality Gain:** Aligns the strongest conclusion with actual evidence.

#### P1 Experiment: Statistical Significance of Rankings

- **Target Claim:** All claims about relative method performance
- **Hypothesis:** Many ranking differences are within noise bounds.
- **Minimal Design:** Paired Wilcoxon signed-rank test for all primary comparisons (Deep Ensembles vs each method, across datasets). Report p-values and effect sizes. Generate critical difference diagrams.
- **Metrics:** Wilcoxon p, Cohen's d (or common language effect size).
- **Success Criterion:** Comparisons with p<0.05 are flagged as significant.
- **Estimated Cost:** 1 day modeling.
- **Expected Paper-Quality Gain:** Provides statistical rigor to the benchmark's main conclusions.

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Pre-Submission): Uni-Mol ablation + BBP/SGLD correlation + Significance tests
                      |
                      v
       [Uni-Mol claim fixed] [BBP/SGLD claim fixed] [Rankings validated]
                      |
P1 (Post-Acceptance): Prior benchmark table + ToxCast sensitivity
                      |
                      v
       [Positioning substantiated] [Extreme dataset concern addressed]
                      |
P2 (Future): Hyperparameter sensitivity + Additional UQ methods (conformal prediction, evidential deep learning)
                      |
                      v
       [Benchmark completeness improved]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

**Rationale:** The benchmark addresses a genuine and timely gap — UQ method selection for pre-trained molecular representation models. The experimental scope (4 primary backbones × 8 UQ methods × 14 datasets) is substantial and the scaffold-split design is principled. However, the score is constrained by three major issues:

1. **Novelty/Research Value (moderate):** The benchmark's contribution as a "comprehensive evaluation" is weakened by the Uni-Mol multi-conformer confound, which undermines the backbone comparison that is central to the paper's claims. Without resolving this, the practical value of the findings is reduced.

2. **Validity/Soundness (below threshold):** The absence of statistical significance testing, the contradictory BBP/SGLD evidence, and the uncontrolled Uni-Mol inference strategy all reduce confidence in the main conclusions. These are fixable, but in their current form they limit the paper's reliability as a reference benchmark.

3. **Reproducibility (adequate):** The appendix provides extensive implementation details and full result tables. The regression normalization ambiguity is a minor concern.

**Post-Revision Target: [6.5, 7.5]/10**

If the authors:
- Add single-conformer Uni-Mol ablation
- Provide statistical significance analysis
- Revise BBP/SGLD claims with correlation evidence
- Clarify normalization procedure
- Add benchmark comparison table

...the paper could become a solid contribution (7/10) that serves as a useful reference for the molecular ML community. The upper bound (7.5) requires resolving the core confounds convincingly.