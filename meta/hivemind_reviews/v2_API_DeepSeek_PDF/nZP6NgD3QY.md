## Summary
# Final Review Report

## Summary

This paper (AdaMerging) addresses the problem of merging multiple independently fine-tuned models into a single multi-task learning (MTL) model without accessing their original training data. Building on the task-vector framework (Task Arithmetic, Ties-Merging), the authors identify that a single global merging coefficient λ limits performance because different tasks and layers contribute differently to the merged model. AdaMerging replaces the fixed λ with learnable per-task or per-layer coefficients, optimized via entropy minimization on unlabeled test samples. The method is evaluated on eight image classification datasets using CLIP-based ViT models (B/16, B/32, L/14).

The paper's core contribution is showing that entropy minimization correlates strongly (Spearman ρ=0.87) with cross-entropy loss on multi-task test data, enabling unsupervised coefficient optimization. Empirical results demonstrate 5-11% accuracy improvements over fixed-coefficient task-vector baselines, with additional evidence of generalization to unseen tasks and robustness to common corruptions.

However, several concerns limit the strength of the conclusions: (1) the evaluation is transductive — coefficients are optimized on the test distribution before evaluation on the same test set, creating an asymmetric comparison with baselines; (2) no variance or statistical significance is reported for any result; (3) the entropy-loss correlation analysis has methodological gaps; and (4) the method has unacknowledged limitations regarding architecture generality and evaluation protocol. The paper is technically sound and addresses a practically relevant problem, but claims require more rigorous empirical validation and bounded wording.

## Strengths
1. **Practically motivated problem:** The paper addresses a real and growing need in the foundation-model ecosystem: merging multiple fine-tuned models into one MTL model without access to original training data. This is relevant as model sharing without data disclosure becomes more common.

2. **Clean technical idea:** Replacing a single global merging coefficient with learnable per-task/per-layer coefficients is conceptually simple yet effective. The gradient-based optimization via entropy minimization avoids expensive grid search and scales to many tasks and layers (1,248 coefficients for 8 tasks × 156 layers).

3. **Empirically validated proxy objective:** The Spearman correlation analysis (ρ=0.87 between entropy and loss across eight tasks) provides a principled justification for using entropy minimization as a surrogate. The supervised-vs-unsupervised comparison (Table 10) further validates that the unsupervised version approaches the supervised upper bound.

4. **Comprehensive evaluation across three dimensions:** The experimental design covers performance (Tables 1-2), generalization to unseen tasks (Table 3), and robustness to distribution shifts (Table 4, Table 8) across three architectures (ViT-B/16, B/32, L/14), providing a thorough empirical picture.

5. **Low computational overhead:** The method adds only 8 (task-wise) or 1,248 (layer-wise) learnable parameters to 907M model parameters, and achieves meaningful gains within 7.5-50 minutes of additional training (Table 12), demonstrating practical efficiency.

6. **Multiple variants for broad applicability:** The paper presents four variants (Task-wise/Layer-wise × AdaMerging/AdaMerging++), allowing users to choose between simplicity (task-wise) and fine-grained control (layer-wise) depending on their compute budget and task diversity.

## Weaknesses
### W1. Transductive Evaluation Protocol (Major)
AdaMerging optimizes merging coefficients using unlabeled test samples via entropy minimization, then evaluates performance on the *same* test set. This creates a transductive setting that is fundamentally different from the inductive evaluation used by baselines (Task Arithmetic, Ties-Merging), which set λ via a separate validation process or default value. The asymmetric comparison inflates the reported gains relative to a fair inductive setup where test data is never used for any form of model selection.

### W2. Missing Variance and Significance Reporting (Major)
All experimental results (Tables 1-8) are reported as single-point estimates without standard deviations, confidence intervals, or statistical significance tests. Given that the optimization involves stochastic components (Adam optimizer, batch sampling), the stability of the learned coefficients and resulting performance is unknown. Several improvements are within the range that could be explained by optimization noise (e.g., Task-wise AdaMerging: 71.1% vs Task Arithmetic: 69.1% — a 2% gap without variance).

### W3. Entropy-Loss Correlation Analysis Has Gaps (Moderate)
The Spearman correlation (ρ=0.87) between entropy and loss is computed on the *initial* merged model (λ=0.3). While Appendix Fig. 10 tracks correlation across training stages, it only shows the aggregated correlation across all tasks — per-task correlation trajectories are not reported. If the correlation weakens for specific tasks during optimization, the proxy objective may drive coefficients in suboptimal directions for those tasks.

### W4. Limited Architecture and Task Scope (Moderate)
Experiments are confined to CLIP-based ViT models on image classification datasets. The paper does not test AdaMerging on other architectures (ResNet, BERT, LLMs) or task types (regression, segmentation, generation). Given that the method relies on entropy minimization for classification tasks, its applicability to non-classification settings is unclear.

### W5. Conclusion Lacks Limitations and Bounded Claims (Moderate)
The conclusion restates performance claims without acknowledging transductive evaluation, architecture limitations, or potential failure modes (e.g., the EuroSAT performance drop under noise observed in Appendix Table 8). Future work is stated generically ("different architectures") without specific technical challenges.

### W6. Ablation of Entropy Surrogate vs. Alternative Proxies (Minor)
The paper validates entropy minimization against cross-entropy (Table 10), but does not compare against other unsupervised proxy objectives (e.g., margin maximization, confidence maximization, consistency regularization). The choice of entropy is motivated by test-time adaptation literature, but the paper does not argue why entropy is specifically suited for coefficient optimization (as opposed to model parameter adaptation).

### W7. Unconstrained Coefficient Optimization (Minor)
The Task-wise and Layer-wise AdaMerging formulas do not specify constraints on λ coefficients. While empirically the learned coefficients stay within [0,1], there is no theoretical guarantee or explicit boundary enforcement. Negative coefficients or values >1 could theoretically produce degenerate models, and this possibility is not discussed.

## Key Issues
### Issue 1: Transductive Evaluation Creates Asymmetric Comparison (Severity: Major)
**Page 7 - Experiments Section.** The method optimizes coefficients on the test distribution (even without labels) before evaluating on that same test set. This is a transductive setup, whereas baselines use a fixed λ determined without any test-set information. The resulting performance gap conflates the benefit of adaptive coefficients with the advantage of test-set-specific adaptation. The paper does not acknowledge this asymmetry.

**Required fix:** Report an additional experiment where AdaMerging coefficients are optimized on a held-out subset of test samples and evaluated on the remaining held-in subset. Table 9 partially addresses this by varying test data percentage, but evaluation is still on the full test set after optimization on the same distribution.

### Issue 2: Absence of Variance and Significance Testing (Severity: Major)
**Page 7-9 - All Result Tables.** No standard deviations, confidence intervals, or significance tests are reported. The coefficient optimization involves stochasticity (batch sampling, optimizer noise), yet all numbers are presented as deterministic. For a method that claims "11% improvement," the reader cannot assess whether this is 11% ± 1% or 11% ± 5%.

**Required fix:** Run all experiments with ≥3 random seeds (different coefficient initialization seeds, batch orders), report mean ± std, and add paired significance tests for the key comparisons (AdaMerging vs. Ties-Merging).

### Issue 3: Entropy-Loss Correlation Evidence Is Incomplete (Severity: Moderate)
**Page 6 - Section 3.2.2.** The Spearman correlation (ρ=0.87) is computed on the initial merged model, not tracked per-task during optimization. Without per-task correlation trajectories, the paper cannot rule out that the proxy objective drives coefficients suboptimally for specific tasks during later optimization stages.

**Required fix:** Report per-task Spearman correlations at iterations 0, 100, 200, 300, 400, 500 in the main paper (moving beyond aggregated figures in the appendix).

### Issue 4: Overclaimed Generalization and Robustness (Severity: Moderate)
**Page 8 - Section 4.2.** The generalization experiment (Table 3) uses a setting where 6 tasks are merged and 2 unseen tasks are evaluated. However, the "unseen" tasks are from the same distribution as the training tasks (same datasets, just not merged). This evaluates knowledge transfer within the same benchmark suite, not generalization to truly out-of-distribution or novel task types. The wording "superior generalization capabilities" overstates the evidence.

**Required fix:** Replace "generalization to unseen downstream tasks" with "knowledge transfer to non-merged tasks within the same benchmark." Consider adding a true zero-shot generalization experiment (e.g., evaluate on a completely unseen dataset not in the 8-task set).

### Issue 5: Conclusion Omits Critical Limitations (Severity: Moderate)
**Page 9 - Conclusion.** The conclusion acknowledges zero limitations and makes unqualified claims ("superior to current SOTA"). This is inconsistent with the identified issues above and reduces scientific credibility.

**Required fix:** Add a limitations paragraph covering: (1) transductive evaluation, (2) architecture scope (CLIP ViT only), (3) classification-only tasks, (4) potential failure cases (EuroSAT noise drop), and (5) lack of theoretical convergence guarantees.

## Actionable Suggestions
### S1. Add Inductive Evaluation Protocol (Must)
**Target:** Page 7 - Experiments Section.
**Action:** Add an experiment where AdaMerging coefficients are optimized on a randomly sampled 50% subset of test samples, and evaluated on the remaining 50%. Report both the transductive (full-test optimization) and inductive (held-out evaluation) results side by side. This directly quantifies the gap caused by test-distribution adaptation and provides a fairer comparison with baselines.
**Expected benefit:** Clarifies how much of the reported gain comes from test-set-specific adaptation vs. the coefficient learning mechanism itself.

### S2. Report Multi-Seed Variance (Must)
**Target:** Tables 1-4, 6-8 (all result tables).
**Action:** Repeat all experiments with 3 random seeds (varying coefficient initialization and batch sampling order). Report mean ± std for Avg Acc and per-task accuracies. Add a paired bootstrap significance test comparing AdaMerging (Layer-wise) against Ties-Merging for the Avg Acc metric.
**Expected benefit:** Enables readers to assess whether reported improvements are statistically reliable or within noise range.

### S3. Rewrite Conclusion with Limitations (Must)
**Target:** Page 9 - Conclusion.
**Action:** Replace the current 5-sentence conclusion with a structured conclusion covering: (1) validated findings with bounded claims, (2) specific limitations (transductive evaluation, CLIP ViT only, classification-only), (3) concrete future work (architecture generality, theoretical convergence, alternative proxy objectives).

**Mentor Revised Version:**
"We have proposed AdaMerging, which learns per-task or per-layer merging coefficients via entropy minimization on unlabeled test samples, improving average accuracy by 5-11% over fixed-coefficient task-vector baselines on eight image classification tasks. The method also shows promising knowledge transfer to non-merged tasks and improved robustness to common corruptions. However, these results should be interpreted with two caveats: (i) our evaluation is transductive — coefficients are optimized on test samples before evaluation — which may overstate gains compared to purely inductive model selection; and (ii) experiments are limited to CLIP-based ViT models on classification tasks. Extending AdaMerging to other architectures (ResNet, LLMs) and task types (regression, generation) remains important future work, as does investigating theoretical convergence guarantees for the entropy surrogate and potential failure modes when the entropy-loss correlation degrades."

### S4. Strengthen Entropy-Loss Correlation Analysis (Nice-to-have)
**Target:** Page 6 - Section 3.2.2.
**Action:** In addition to the initial correlation, report per-task Spearman correlations at iterations 0, 100, 200, 300, 400, 500 as a table in the main paper. If any task shows decreasing correlation (e.g., drops below 0.6 during training), discuss the implication.
**Expected benefit:** Provides stronger evidence that the proxy objective remains valid throughout optimization, not only at initialization.

### S5. Reposition Generalization Claims (Must)
**Target:** Page 8 - Section 4.2 ("Substantially Improved Generalization").
**Action:** Replace "superior generalization capabilities when applied to unseen downstream tasks" with "improved knowledge transfer to tasks whose task vectors were not included in the merging process, within the same benchmark suite." Consider adding one truly out-of-distribution evaluation (e.g., evaluating on a corruption type not used during coefficient optimization).
**Expected benefit:** Aligns claim strength with evidence level, improving scientific credibility.

### S6. Discuss Negative Cases in Robustness (Nice-to-have)
**Target:** Page 8 - Robustness section, or Appendix discussion.
**Action:** Add 1-2 sentences discussing the EuroSAT performance drop under Impulse/Gaussian noise observed in Appendix Table 8. Acknowledge that the entropy surrogate may be less effective for certain task-noise type combinations.
**Expected benefit:** Shows scientific maturity by discussing failure modes rather than only highlighting positive results.

### S7. Add Coefficient Constraints or Discussion (Nice-to-have)
**Target:** Page 5 - Section 3.2.1.
**Action:** Add a sentence specifying whether λ_k is constrained (e.g., via sigmoid or clipping) or left unconstrained. If unconstrained, add a note that empirically coefficients remain in [0,1] and discuss why this is expected (e.g., gradient structure naturally bounds values).
**Expected benefit:** Improves reproducibility and clarifies implementation details for practitioners.

## Storyline Options + Writing Outlines
### Current Storyline Analysis
The current introduction follows: P1 (MTL background + foundation model challenges) -> P2 (Task arithmetic introduction + performance gap) -> P3 (Coefficient sensitivity problem) -> P4 (Proposed method + entropy intuition) -> P5 (Contributions). The main issue is that P1 is citation-heavy without a clear argument arc, and the gap is established too late (P2-P3).

### Alternative Storyline A (Recommended)
**Arc:** Practical Constraint -> Specific Gap -> Solution Intuition -> Key Validation -> Contributions.
- P1: Foundation models are independently fine-tuned and shared without training data. Traditional MTL is infeasible. Model merging is needed but current methods underperform.
- P2: Task-vector merging is promising but limited by a single coefficient λ. Show Fig. 1 data. Diagnose: different tasks and layers need different weights.
- P3: Gradient-based optimization of coefficients is natural, but we need a proxy objective since labels are unavailable. Key insight: entropy correlates with loss on MTL test data (ρ=0.87).
- P4: AdaMerging framework: learnable coefficients + entropy minimization. Two variants: task-wise and layer-wise.
- P5: Contributions listed with empirical scope.

### Alternative Storyline B
**Arc:** Technical Opportunity -> Method -> Evidence -> Impact.
- P1 (short): Task vectors provide a unique opportunity for data-free MTL.
- P2: But current single-λ approach is fragile. The open problem is automatic coefficient selection.
- P3: Our solution: make coefficients learnable, optimize via entropy (show correlation evidence upfront).
- P4: AdaMerging achieves 80.1% vs 72.4% (Ties-Merging) on 8-task benchmark.
- P5: Contributions.

### Abstract Outline (Complete)

**S1 (Problem):** Multi-task learning via model merging is increasingly important in the foundation-model era, but current task-vector methods use a single merging coefficient that limits performance.

**S2 (Gap):** Optimizing per-task or per-layer coefficients is infeasible via grid search for many tasks, and no principled unsupervised objective exists for coefficient selection.

**S3 (Method):** We propose AdaMerging, which learns task-wise or layer-wise merging coefficients via entropy minimization on unlabeled multi-task test samples.

**S4 (Evidence):** On eight image classification tasks with CLIP ViT models, AdaMerging improves average accuracy by 5-11% over fixed-coefficient baselines.

**S5 (Bounded claim):** Additional experiments suggest improved robustness to corruptions and knowledge transfer to non-merged tasks; variance and significance bounds are reported.

### Introduction Outline (Complete)

**P1 — Practical Need and Gap:**
- Role: Establish that model merging without training data is practically needed but current methods underperform.
- Key claim: Foundation models are fine-tuned and shared without data; traditional MTL is expensive; model merging is the alternative but has a performance gap.
- Transition: "The key limitation of current task-vector methods is their reliance on a single, globally-shared merging coefficient."

**P2 — Coefficient Sensitivity as the Core Problem:**
- Role: Diagnose why single-λ merging underperforms.
- Key claim: The merging coefficient critically determines average accuracy (cite Fig. 1). Different tasks and layers require different coefficients due to varying task conflict levels.
- Transition: "However, manually searching per-task or per-layer coefficients via grid search is intractable for large K and L."

**P3 — Proposed Solution Intuition:**
- Role: Introduce AdaMerging and its proxy objective.
- Key claim: We make coefficients learnable and optimize them via entropy minimization on unlabeled test data. Entropy correlates with loss (ρ=0.87) on MTL test data.
- Transition: "This leads to two adaptive merging schemes."

**P4 — Method Overview:**
- Role: Briefly describe Task-wise and Layer-wise variants.
- Key claim: Both variants optimize coefficients via gradient descent using the entropy surrogate without labels.
- Transition: "We evaluate these schemes on three dimensions."

**P5 — Contributions (explicit list):**
1. AdaMerging with learnable task-wise/layer-wise coefficients.
2. Empirical validation of entropy-loss correlation for MTL merging.
3. 5-11% improvement over fixed-coefficient baselines, plus generalization and robustness evidence.
4. Open-source implementation for reproducibility.

## Priority Revision Plan
### P0 Items (Critical — Must Address Before Resubmission)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P0.1 | Transductive evaluation (Issue 1) | Add inductive (held-out) evaluation + discuss protocol difference | Removes largest threat to validity; fair comparison with baselines |
| P0.2 | Missing variance + significance (Issue 2) | Run 3 seeds, report mean±std, add significance tests | Enables readers to assess reliability of claimed gains |
| P0.3 | Overclaimed generalization (Issue 4) | Tighten wording; consider true OOD evaluation | Aligns claim strength with evidence |
| P0.4 | Conclusion lacks limitations (Issue 5) | Rewrite per S3 | Improves scientific credibility and transparency |

### P1 Items (High Priority)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P1.1 | Entropy correlation analysis gaps (Issue 3) | Add per-task correlation trajectories across training | Strengthens proxy-objective validation |
| P1.2 | Negative case discussion (S6) | Add EuroSAT noise drop discussion | Shows scientific maturity |
| P1.3 | Coefficient constraint documentation (S7) | Add implementation detail on λ bounds | Improves reproducibility |

### P2 Items (Nice-to-Have)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P2.1 | Alternative proxy comparison | Compare entropy vs. margin maximization, confidence | Broadens contribution to method design space |
| P2.2 | Architecture generality | Add one non-ViT experiment (e.g., ResNet-50) | Expands applicability claims |
| P2.3 | Related-work reorganization | Restructure around comparison axes with table | Improves readability and positioning |

### Revision Order

```text
Phase 1 (Immediate): Claims + Disclosure
  - Tighten generalization/robustness wording
  - Add limitations to conclusion
  - Document coefficient constraints

Phase 2 (This Week): Experimental Rigor
  - Run 3-seed variance experiments
  - Add inductive (held-out) evaluation
  - Per-task entropy correlation tables

Phase 3 (Before Resubmission): Depth
  - Negative case discussion (EuroSAT)
  - Alternative proxy objective comparison
  - Architecture extension (ResNet)
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Multi-task performance (ViT-B/32) | 8 tasks, 13 methods, Avg Acc | Per-task accuracy, Avg Acc | Layer-wise AdaMerging: 80.1% (vs Ties-Merging: 72.4%) | C1 (adaptive coefficients improve performance) | No variance; single seed |
| E2 | Multi-task performance (ViT-L/14) | 8 tasks, 11 methods, Avg Acc | Per-task accuracy, Avg Acc | AdaMerging: 90.8% (vs Ties-Merging: 86.0%) | C1 | No variance; single seed |
| E3 | Multi-task performance (ViT-B/16) | 8 tasks, 8 methods, Avg Acc | Per-task accuracy, Avg Acc | Layer-wise AdaMerging: 84.9% (vs Ties-Merging: 77.0%) | C1 | Appendix only |
| E4 | Generalization to unseen tasks | 6 seen + 2 unseen, 2 settings | Avg Acc on seen and unseen | AdaMerging: 70.0% vs Ties-Merging: 59.6% (MNIST+EuroSAT) | C3 (generalization claim) | "Unseen" tasks from same benchmark; no true OOD |
| E5 | Robustness to corruptions (ViT-B/32) | 4 tasks, 7 corruptions | Per-task + Avg Acc under corruption | Avg improvement: 5.8-11.2% per corruption type | C3 (robustness claim) | EuroSAT drops under noise (Impulse/Gaussian) |
| E6 | Robustness to corruptions (ViT-B/16) | 4 tasks, 7 corruptions | Per-task + Avg Acc under corruption | Avg improvement: 6.8-12.4% per corruption type | C3 (robustness claim) | EuroSAT drops under noise |
| E7 | Learned coefficient analysis | Task-wise (Tab.5), Layer-wise (Fig.4) | Coefficient values | Coefficients differ across tasks and layers | C2 (correlation analysis) | No stability analysis across seeds |
| E8 | Data amount sensitivity | 0.1%/1%/5%/100% test data (Tab.9) | Avg Acc | 0.1% data: 74.0% (vs 69.1% baseline) | Practical applicability claim | Evaluation still on same test set |
| E9 | Supervised vs unsupervised | Compare entropy vs cross-entropy (Tab.10) | Avg Acc | Near-identical: 71.1% vs 71.3% (Task-wise) | C2 (proxy objective validation) | No explanation for near-identical results |
| E10 | Time cost analysis | Varying training duration (Tab.12) | Avg Acc over time | 7.5 min: +2%, 50 min: +8% | Practical efficiency claim | Single GPU, no scaling analysis |

### Research-Theme Gap Diagnosis

- **New Knowledge (Partial):** The entropy-loss correlation for MTL model merging is a novel empirical finding, but its investigation lacks depth (per-task trajectories, comparison with alternative proxies).
- **Reproducibility (Weak):** No code release with deterministic seeds, no variance reporting, implementation details (coefficient constraints, optimization bounds) are incomplete.
- **Impact on Practice/Understanding (Partial):** The idea of learnable merging coefficients via unsupervised optimization is practically valuable, but the transductive evaluation limits confidence in real-world applicability.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Quality Gain |
|--------|-------------|-----------|---------------|-------------------|---------|------------------|-----------|-------------|
| R1 (P0) | Fair evaluation | Held-out evaluation reduces but preserves gains | Optimize λ on 50% test samples, evaluate on other 50% | Full-test optimization, fixed-λ baselines | Avg Acc gap between transductive/inductive | Gap < 3% | 1 GPU-day | Removes validity threat |
| R2 (P0) | Statistical reliability | Gains are stable across seeds | 3 seeds with different init + batch order | Single-seed results, bootstrap CI | Mean±std, p-value vs Ties-Merging | std < 1.5%, p < 0.05 | 3 GPU-days | Enables reliable ranking |
| R3 (P1) | Proxy validity across training | Correlation persists per-task | Per-task Spearman ρ at iterations 0,100,...,500 | Aggregated correlation (current Fig.10) | Per-task ρ values | All per-task ρ > 0.6 at all stages | Compute-free (re-analysis) | Strengthens core contribution |
| R4 (P1) | Architecture generality | Method transfers beyond ViT | Apply AdaMerging to 4 ResNet-50 fine-tuned models on 4 subsets of 8 tasks | Task Arithmetic and Ties-Merging on ResNet | Avg Acc | AdaMerging > baselines by > 3% | 2 GPU-days | Expands applicability scope |
| R5 (P2) | Alternative proxy comparison | Entropy is competitive with other unsupervised proxies | Compare entropy vs. confidence-max, margin-max, consistency | Current entropy-based AdaMerging | Avg Acc, convergence speed | Entropy within 1% of best alternative | 1 GPU-day | Strengthens surrogate choice justification |

### ASCII Diagram — Experiment Upgrade Plan

```text
Current Experiment Set → Gap Analysis → Proposed Experiments
                                                
E1-E3 (Performance) ──→ No variance ──→ R2: Multi-seed reporting
E4 (Generalization) ──→ Weak OOD ──→   R1: Inductive evaluation
E5-E6 (Robustness) ──→ Negative cases ──→ Add discussion (no new expt)
E7-E9 (Analysis) ────→ Correlation gap ──→ R3: Per-task trajectories
E10 (Efficiency) ────→ Single arch ──→ R4: ResNet-50 experiment

P0: R1 + R2 (Validity-critical, do first)
P1: R3 + R4 (Depth, do next)
P2: R5 (Nice-to-have, if time permits)
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.0/10**

**Rationale:** The paper addresses a well-motivated practical problem with a clean technical idea (learnable merging coefficients via entropy minimization). The empirical results are promising and the proxy-objective validation is an interesting contribution. However, the score is constrained by three factors:

1. **Research value (moderate):** The incremental contribution over Task Arithmetic/Ties-Merging is meaningful but limited to introducing learnable coefficients and an entropy surrogate. The core task-vector framework is not new.
2. **Validity concerns (major):** The transductive evaluation (Issue 1) and missing variance (Issue 2) significantly limit confidence in the reported numbers. Without these addressed, the numerical claims cannot be fully trusted.
3. **Novelty (moderate):** In Retrieval-Disabled Mode, external novelty verification is deferred. Based on manuscript evidence, the contribution is solid but incremental — combining task vectors with test-time adaptation techniques.

**Post-Revision Target: [7.0, 7.5]/10**

If the authors address the P0 items (inductive evaluation, multi-seed variance, bounded claims, honest limitations), the paper would provide a validated, practically useful method. The upper bound is ~7.5 because the core technical novelty is moderate and the architecture/task scope remains limited.