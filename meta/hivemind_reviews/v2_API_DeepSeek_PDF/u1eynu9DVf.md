## Summary
# Final Review Report

## Summary

This paper studies the problem of forecasting which upstream pre-training examples will be forgotten when a language model is updated to fix a specific error (model refinement). The authors formalize this as a binary classification task: given a pair of an online-learned example and an upstream pre-training example, predict whether the upstream example will be forgotten after the update. They propose three approaches: (1) a threshold-based baseline relying on forgetting frequency, (2) a partially interpretable logit-transfer model grounded in neural tangent kernel (NTK) theory that predicts how logit changes propagate between examples, and (3) a black-box representation-based model that learns an inner-product similarity between example encodings. Experiments on BART0 and FLAN-T5 (Large and 3B) across head-only, LoRA, and full fine-tuning setups show that the representation-based model achieves the best forecasting F1 (up to 79.3). Replaying examples predicted as forgotten reduces Exact Match drop — from 8.0% to 2.2% on BART0 in single-error setup, and from 5.5% to 0.3% in continual refinement of FLAN-T5. The paper also compares against a non-replay method (MEND) in the appendix.

**Overall assessment:** The paper addresses a well-motivated problem (catastrophic forgetting during model refinement) with clean problem formulation and thorough experimentation across multiple models and tuning regimes. The logit-transfer observation is scientifically interesting. However, several issues weaken the impact: (1) the NTK derivation relies on a single-step gradient approximation with an invertibility assumption that is not justified, (2) the trainable logit model fails on FLAN-T5 without a clear architectural explanation, (3) the experimental design confounds model architecture with evaluation dataset (BART0 on P3-Test, FLAN-T5 on MMLU), (4) the practical benefit over random replay is marginal in low-forgetting regimes (FLAN-T5 single-error), and (5) a non-replay method (MEND, appendix A) achieves lower forgetting than forecasting-based replay but is downplayed. Novelty comparison is deferred due to Retrieval-Disabled Mode.

## Strengths
**S1 — Well-motivated and clearly formulated problem.** The paper identifies a genuine, practical challenge in deploying LMs: when fixing a specific error via fine-tuning, it is unclear which upstream examples will be forgotten. The binary classification formulation (g: (xi, yi, xj, yj) -> {0,1}) is clean, testable, and directly applicable to replay-based mitigation. The definitions of Edit Success Rate and EM Drop Ratio are appropriate for the problem.

**S2 — Solid empirical breadth.** The experiments span two model families (BART0, FLAN-T5) with three sizes (400M, 840M, 3B), three tuning regimes (head-only, LoRA, full FT), and both single-error and continual refinement settings. This is more comprehensive than typical model-editing papers. The OOD generalization experiment (Table 2) and the hyperparameter analysis (Appendix E) add useful depth.

**S3 — Novel empirical observation of logit-change transfer.** The phenomenon documented in Figure 2(a) — that logit changes from an online-learned example partially transfer to an upstream example, causing prediction flips — is a genuine scientific contribution. The NTK-grounded derivation (Eq. 2) provides a theoretical scaffold for this observation, even if the practical simplified model has limitations.

**S4 — Clean computational efficiency analysis.** Table 5 and the FLOP analysis (Appendix D) clearly show that all forecasting methods are orders of magnitude cheaper than computing ground-truth forgetting via full inference on the upstream set. This makes the practical case for forecasting methods concrete.

**S5 — Reproducibility-friendly setup.** The paper uses publicly available models (BART0, FLAN-T5) and datasets (P3, MMLU), specifies hyperparameters, and commits to releasing code. The algorithmic pseudocode (Algorithms 1-4 in Appendix C) covers training and inference procedures in detail.

## Weaknesses
**W1 — NTK derivation has practical gaps.** The core theoretical derivation (Eq. 2) relies on a first-order Taylor expansion and assumes invertibility of the NTK matrix Θ(xi, xi) ∈ R^{T V × T V}. In practice, the model may have fewer parameters than T×V (e.g., head-only tuning with small heads), making the kernel rank-deficient. Moreover, the method uses K=30 or 100 gradient steps, but the derivation is exact only for a single step. These gaps are acknowledged but not analyzed — they explain the imperfect F1 and model-dependent performance.

**W2 — Simplified kernel approximation collapses informative structure.** The trainable logit-based model replaces the full kernel product Θ(xj, xi)Θ^{-1}(xi, xi) with a rank-d bilinear form h(xj)h(xi)^T, removing the vocabulary dimension entirely. This drastic simplification works on BART0 (where the NTK structure may be low-rank) but fails on FLAN-T5. The paper does not analyze the NTK rank or spectral properties that cause this discrepancy.

**W3 — Experimental confound between model architecture and evaluation dataset.** BART0 is evaluated on P3-Test, while FLAN-T5 uses MMLU, because P3 overlaps with FLAN-T5's pre-training. This means cross-model comparisons (e.g., "representation-based forecasting achieves 79.32 F1 on BART0 vs 67.81 on FLAN-T5") conflate architecture differences with task difficulty differences. It is unclear whether BART0's better forecasting results are due to its architecture or the easier P3-Test tasks.

**W4 — Practical benefit is marginal in low-forgetting regimes.** On FLAN-T5 in the single-error setup, Vanilla FT causes only 0.03%-0.15% EM drop. The improvement from random replay to representation-based forecasting is tiny (e.g., 0.068% to -0.026% on FLAN-T5 Large FT). The method provides substantial value only for high-forgetting regimes like BART0 Full FT (8% to 2.2% EM drop). The paper should explicitly bound when the method is worth adopting.

**W5 — Non-replay methods outperform in forgetting reduction but are downplayed.** Appendix A shows MEND achieves 0.060% EM Drop (vs 0.079% for representation-based replay) on FLAN-T5 Large LoRA, with the trade-off of lower edit success. This comparison is in an appendix, only on one setup, and its implications for the paper's third contribution claim are not adequately discussed in the main text.

**W6 — No statistical significance or variance reporting.** All F1 and EM drop numbers are reported as point estimates without confidence intervals, standard deviations, or significance tests. Given the highly skewed label distribution (0.03%-8% positive class), small F1 differences may not be statistically reliable.

**W7 — Representation-based model loses token-level interaction information.** The model sums over all T output positions before computing the inner product (Eq. 4), discarding the token-level correspondence that Figure 2(a) identifies as the mechanism of forgetting. No alternative pooling strategies are compared.

**W8 — Limitations section is too brief.** The paper lists only two limitations, omitting: (a) the one-time cost of obtaining ground-truth forgetting labels for training, (b) lack of validation on decoder-only LMs, (c) assumption of a fixed upstream dataset, and (d) the method not universally outperforming simpler baselines.

## Key Issues
**Issue 1 (Top Priority) — Inconsistent EM Drop Ratio definition.** The paper defines EM Drop Ratio as (EM_fi - EM_f0) / EM_f0, which yields negative values when forgetting occurs (since EM_fi < EM_f0). However, all tables report positive EM Drop % values. This mathematical inconsistency must be corrected by redefining the metric as (EM_f0 - EM_fi) / EM_f0 with positive values indicating forgetting. See annotation on Page 2 - Section 2 for full details.

**Issue 2 (Top Priority) — NTK invertibility and multi-step validity not addressed.** Eq. 2 requires inverting Θ(xi, xi) ∈ R^{T V × T V}, which can be rank-deficient (especially in head-only tuning where the parameter count may be < T×V). No damping or regularization is discussed. The derivation is also exact only for a single gradient step, yet experiments use K=30-100 steps. This undermines the theoretical foundation of the logit-based method. See annotation on Page 3 - Section 3.2.

**Issue 3 (High Priority) — Experimental confound prevents clean cross-model comparison.** BART0 is tested on P3-Test (diverse NLP tasks) while FLAN-T5 is tested on MMLU (multi-choice QA). Performance differences between models cannot be attributed to architecture alone. See annotation on Page 5 - Section 4.1.

**Issue 4 (High Priority) — MEND comparison undermines Contribution (C3) but is hidden in appendix.** Table 6 shows MEND achieving 0.060% EM Drop vs 0.079% for representation-based replay on FLAN-T5 Large LoRA. The paper's third contribution claims "reduced forgetting" as a practical utility, but MEND achieves lower forgetting with a different trade-off. This comparison must be moved to the main paper with an honest discussion of the trade-off. See annotation on Page 13 - Appendix A.

**Issue 5 (Medium Priority) — Simplified kernel collapses informative gradient structure.** The trainable logit-based model replaces a (T V × T V) NTK product with a (T × T) bilinear form h(xj)h(xi)^T. This eliminates vocabulary-level interactions that Figure 2(a) shows are critical. The failure on FLAN-T5 is attributed to "cannot be captured by a simplified kernel" without analyzing the NTK rank — this explanation is insufficient. See annotation on Page 4 - Section 3.2.

**Issue 6 (Medium Priority) — No statistical significance testing.** All F1 and EM drop results are point estimates without variance. Given the extreme class imbalance (0.03%-8% positive class), even ±1 F1 point could change method rankings. Bootstrapped confidence intervals or multi-seed experiments are needed. See annotation on Page 6 - Section 5.1.

**Issue 7 (Medium Priority) — Practical benefit is marginal in low-forgetting regimes.** On FLAN-T5 single-error setups (Tables 3), Vanilla FT already has <0.15% EM drop, and forecasting-based replay offers essentially no benefit over random replay. The paper should bound its applicability claims. See annotation on Page 7 - Section 5.2.

**Issue 8 (Low Priority) — Representation-based model loses token-level interaction signal.** Eq. 4 sums over output positions before the inner product, discarding token-to-token correspondence. An alternative per-token inner product could better capture the mechanism shown in Figure 2(a). See annotation on Page 5 - Section 3.3.

**Issue 9 (Low Priority) — Limitations section incomplete.** Only two limitations are listed. Missing: training cost of forecasting model, decoder-only LM generalization, fixed upstream dataset assumption, and inconsistent outperformance over simpler baselines. See annotation on Page 9 - Section 7.

## Actionable Suggestions
### Must-Fix (Publication-Critical)

**A1. Fix EM Drop Ratio definition (Issue 1).** Replace the current formula `(EM_DPT,fi - EM_DPT,f0) / EM_DPT,f0` with `(EM_DPT,f0 - EM_DPT,fi) / EM_DPT,f0` so that positive values consistently indicate forgetting. Update all tables accordingly. This is a mathematical error, not a stylistic choice.

**A2. Address NTK invertibility (Issue 2).** Add damping to the kernel inverse: replace Θ^{-1}(xi, xi) with (Θ(xi, xi) + λI)^{-1} where λ is a small positive constant. Report sensitivity to λ. Acknowledge that Eq. 2 is a first-order approximation and analyze F1 vs. number of gradient steps. Include: "The fixed logit method's performance degrades as K increases because the linear approximation in Eq. 2 holds only for a single step."

**A3. Move MEND comparison to main paper (Issue 4).** Add MEND results to Table 3 and add a paragraph in Section 5.2: "MEND achieves lower EM Drop (0.060%) than our best forecasting-based replay (0.079%) on FLAN-T5 Large with LoRA, but at the cost of reduced edit success (93.1% vs 95.7%). This trade-off highlights that forecasting-based replay prioritizes maintaining high edit accuracy while still substantially reducing forgetting, whereas MEND prioritizes forgetting reduction at the expense of edit reliability. The appropriate choice depends on application requirements."

**A4. Add variance reporting (Issue 6).** Report all main F1 and EM drop results as mean ± std over at least 3 random seeds (different D_R^train/D_R^test splits). Add a note: due to extreme class imbalance, small F1 differences (<2 points) may not be statistically significant.

**A5. Expand limitations section (Issue 9).** Add at least 4 concrete limitations (see annotation on Page 9 - Section 7). Required: training cost, decoder-only generalization, fixed upstream dataset, and non-universal outperformance.

### Nice-to-Have (Quality Improvement)

**A6. Control for dataset confound (Issue 3).** Run FLAN-T5 on a subset of P3-Test tasks confirmed to be outside its pre-training mixture. Alternatively, run BART0 on MMLU to enable direct comparison. Even a limited experiment (e.g., 5 tasks) would substantially strengthen cross-model claims.

**A7. Analyze NTK rank for BART vs T5 (Issue 5).** Compute the effective rank of the NTK matrix Θ(x, x) for both BART0 and FLAN-T5 on representative examples. Report whether rank(BART) > rank(T5) or vice versa, and how this relates to the simplified kernel's success on BART. This would explain why the trainable logit method works on one but not the other.

**A8. Compare pooling strategies for representation model (Issue 8).** Add ablation: sum-pooling (current), mean-pooling, per-token inner-product, and cross-attention. Report F1 for each on at least one setup (e.g., BART0 head-only). If the current design is optimal, explain why.

**A9. Bounded applicability statement.** In Section 5.2 or Conclusion, add: "The practical benefit of forecasting-based replay is most pronounced when baseline forgetting is substantial (EM drop >1%). When the model already exhibits low forgetting (<0.2% EM drop), simpler replay strategies are nearly as effective."

**A10. Precision-recall analysis for continual setup.** Add an analysis paragraph explaining why precision stays stable while recall drops (Figure 3). Include an experiment that re-estimates the frequency prior periodically during the continual sequence to test whether stale priors cause the recall drop.

## Storyline Options + Writing Outlines
### Abstract Outline (Revised)

Current abstract is dense and leads with a method failure narrative. Recommended rewritten abstract (S1-S5):

- **S1 (Problem):** "Language models deployed in the wild make errors; naively updating them with corrected instances causes catastrophic forgetting of upstream knowledge."
- **S2 (Gap):** "Existing replay-based mitigation samples upstream data blindly, lacking both interpretability and controllability."
- **S3 (Method):** "We formulate forecasting forgotten examples as a binary prediction task and propose two approaches — a partially interpretable logit-transfer model grounded in NTK theory, and a black-box model learning representation similarity between examples."
- **S4 (Key Result):** "The black-box method achieves up to 79.3 F1 across BART0 and FLAN-T5 under head-only, LoRA, and full fine-tuning. Using its forecasts for targeted replay reduces Exact Match drop from 8.0% to 2.2% on BART0, and from 5.5% to 0.3% in continual FLAN-T5 refinement."
- **S5 (Bounded Implication):** "Forecasting forgotten examples enables efficient, targeted forgetting mitigation without full upstream inference, with greatest benefit when baseline forgetting is substantial."

### Introduction Outline (Revised)

Current introduction has one overpacked paragraph (P1) and a too-brief goal paragraph (P2). Recommended restructure into three paragraphs:

**P1 (Problem + Motivation):** Begin with the practical stakes: LMs deployed in the wild make errors, and fixing them without full retraining (model refinement) is essential for usability. Establish catastrophic forgetting as the main obstacle. Briefly state why standard random replay is insufficient (lacks interpretability, poor controllability). Close with the key gap: prior work identifies examples prone to forgetting but does not explain *how interactions between two examples* cause forgetting of one when learning the other.

**P2 (Core Observation + Method Preview):** Introduce the logit-change transfer phenomenon (Figure 2a) as the key empirical finding. State: "When we fix an error on example xi, the logit changes on xi partially transfer to upstream example xj, potentially flipping its prediction." Then preview the two proposed approaches: (a) a partially interpretable model that learns how much logit change transfers based on example similarity, and (b) a black-box model that directly predicts forgetting from learned representations. Note that (a) works on BART but fails on T5, motivating (b).

**P3 (Contributions + Roadmap):** State three contributions cleanly:
"(1) A novel problem formulation for forecasting forgotten examples in model refinement.
(2) Two forecasting methods with complementary strengths: interpretable logit-transfer and accurate black-box.
(3) Empirical validation that forecasting-guided replay reduces catastrophic forgetting across architectures and tuning regimes, with head-to-head comparison against a non-replay baseline (MEND)."

### Title Suggestion

Current: "WHAT WILL MY MODEL FORGET? FORECASTING FORGOTTEN EXAMPLES IN LANGUAGE MODEL REFINEMENT"

The title is functional but could be more informative. Consider:
- "Forecasting Forgetting: Predicting Which Upstream Examples Will Be Forgotten During Language Model Refinement"
- "Anticipating Catastrophic Forgetting: Forecasting Forgotten Examples in LM Error Correction"

The key is to communicate both the *problem* (forecasting forgetting) and the *setting* (LM refinement) in the title. The current title emphasizes the question format, which is engaging but less specific than needed for search indexing.

### Storyline Alignment Check

| Check | Current | Revised |
|-------|---------|---------|
| Problem alignment | Good: paper clearly studies forecasting forgetting during model refinement | Retain |
| Variable alignment | Adequate: logit changes, representations, forgetting labels are consistent across sections | Improve by explicitly defining h(x) encoding earlier |
| Contribution-evidence alignment | Partial: C3 (replay algorithm) is not distinct from C2's downstream application | Reframe C3 as empirical demonstration, not separate algorithm |

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[Problem: EM Drop formula is sign-flipped]
    → [Fix: Redefine as (EM_f0 - EM_fi)/EM_f0]
    → [Expected: Consistent metric interpretation]

[Problem: NTK invertibility not addressed]
    → [Fix: Add damping λI to Θ^{-1}, discuss multi-step degradation]
    → [Expected: Theoretical rigor improved]

[Problem: MEND comparison hidden in appendix]
    → [Fix: Move to main paper Table 3, add trade-off discussion]
    → [Expected: Honest positioning of contributions]

[Problem: No variance/statistics reported]
    → [Fix: Add mean±std over ≥3 seeds, bootstrap CIs]
    → [Expected: Statistical reliability]

[Problem: Model-dataset confound]
    → [Fix: Add FLAN-T5 on P3 subset, or BART0 on MMLU]
    → [Expected: Clean cross-model comparison]

[Problem: Simplified kernel collapses NTK structure]
    → [Fix: Add NTK rank analysis for BART vs T5]
    → [Expected: Explain BART/T5 discrepancy]

[Problem: Limitations insufficient]
    → [Fix: Add 4+ concrete limitations]
    → [Expected: Scientific completeness]
```

### Priority Levels

| Priority | Action | Effort | Impact | Section Affected |
|----------|--------|--------|--------|-----------------|
| **P0** | Fix EM Drop Ratio definition | Low (text edit) | High (correctness) | Sec 2, Tables 3-4 |
| **P0** | Add NTK damping / multi-step discussion | Low (text edit) | High (theoretical rigor) | Sec 3.2 |
| **P0** | Move MEND comparison to main paper | Medium (restructure) | High (contribution integrity) | Sec 5.2, Table 3 |
| **P0** | Add variance reporting | Medium (re-run experiments) | High (statistical validity) | Tables 1-4 |
| **P0** | Expand limitations | Low (text edit) | High (scientific completeness) | Sec 7 |
| **P1** | Control for dataset confound | Medium (new experiments) | Medium (cross-model claims) | Sec 4.1, 5.1 |
| **P1** | NTK rank analysis (BART vs T5) | Medium (compute) | Medium (explain discrepancy) | Sec 3.2, Appendix |
| **P1** | Bound applicability statement | Low (text edit) | Medium (honest claims) | Sec 5.2, 7 |
| **P2** | Pooling strategy ablation | Low (re-train) | Low (method refinement) | Sec 3.3 |
| **P2** | Precision-recall analysis for continual | Low (analysis text) | Low (completeness) | Sec 5.3 |

### Revision Sequence

**Stage 1 (before re-submission, ~1-2 days):** P0 items — fix EM Drop formula, add damping discussion, move MEND to main text, expand limitations. These are primarily text edits that do not require new experiments.

**Stage 2 (before re-submission, ~1 week):** P1 items — run variance experiments, control experiment for dataset confound (FLAN-T5 on 5 P3 tasks), NTK rank computation. These require running models but are parallelizable.

**Stage 3 (optional):** P2 items — pooling ablation, precision-recall analysis. These improve depth but are not required for acceptance.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Single-error forgetting forecasting (Table 1) | BART0/FLAN-T5, head/LoRA/Full FT on P3-Test/MMLU | F1 | Rep-based best (79.3 BART0, 67.8 FLAN-T5) | C2 (forecasting methods) | No variance reported; BART vs T5 confounded with dataset |
| E2 | OOD generalization (Table 2) | BART0, P3-Test ID/OOD split | F1 | Rep improves OOD (50.12) over threshold (46.24) | C2 (generalization) | Only BART0 tested |
| E3 | Single-error refinement (Table 3) | BART0/FLAN-T5, Full FT/LoRA | Edit Success, EM Drop % | Rep reduces EM drop vs random replay | C3 (practical utility) | FLAN-T5 benefit marginal (<0.1% EM drop improvement) |
| E4 | Continual refinement (Table 4) | FLAN-T5 Large/3B, LoRA/Full FT, 40 steps | EM Drop % | Rep reduces EM drop from 5.5%→0.3% (Large LoRA) | C3 (continual setting) | Forecasting model not updated during stream |
| E5 | Computational efficiency (Table 5, Appendix D) | FLOP analysis across methods | FLOPs | Rep: 1.35e10, GT: 9.04e14 | C2 (efficiency) | Theoretical complexity only, not wall-clock |
| E6 | Hyperparameter: learning rate (Appendix E.1, Table 9) | FLAN-T5 Large Full FT, 3 LRs | Edit Success, EM Drop % | LR=1e-5 best trade-off | Robustness | Only one model/setup |
| E7 | Hyperparameter: replay batch count (Appendix E.2, Table 10) | FLAN-T5 Large Full FT, replay batches 3-30 | EM Drop % | More batches help in continual, hurt in single | Robustness | Only one model |
| E8 | MEND comparison (Appendix A, Table 6) | FLAN-T5 Large LoRA | Edit Success, EM Drop % | MEND: 93.1%/0.060%; Rep: 95.7%/0.079% | Contrastive | Only one setup; not in main paper |

### Research-Theme Gap Diagnosis

- **New Knowledge (gap):** The logit-change transfer phenomenon is genuinely novel, but its boundary conditions (why BART vs T5 differ) are not explained. The paper describes an observation without establishing *why* it holds or fails.
- **Reproducibility (adequate):** Models, datasets, and hyperparameters are clearly specified. Algorithms 1-4 provide enough detail for re-implementation.
- **Impact on Practice (partial):** The method is most impactful when forgetting is severe (BART0 Full FT: 8%→2.2% EM drop). In low-forgetting regimes (FLAN-T5 single-error), the practical advantage over random replay is negligible. The paper should explicitly clarify this applicability boundary.

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

P0 Experiments (pre-submission critical):
┌─────────────────────────────────────────────────────────────┐
│ E-R1: Variance Estimation                                   │
│ Target: All main results (Tables 1-4)                       │
│ Design: Run 3 seeds with different D_R splits               │
│ Metric: Mean±std F1 and EM Drop                             │
│ Cost: ~2 GPU-days (parallel on 3 seeds)                     │
│ Expected Gain: Statistical reliability for all claims       │
├─────────────────────────────────────────────────────────────┤
│ E-R2: Dataset Confound Control                              │
│ Target: Table 1 cross-model comparison                      │
│ Design: Run FLAN-T5 on 5 P3-Test tasks not in pretrain      │
│ Metric: F1, compare to BART0 results                        │
│ Cost: ~1 GPU-day                                            │
│ Expected Gain: Clean cross-model comparison                 │
└─────────────────────────────────────────────────────────────┘

P1 Experiments (high impact):
┌─────────────────────────────────────────────────────────────┐
│ E-R3: NTK Rank Analysis                                     │
│ Target: Explain BART/T5 discrepancy (Sec 3.2)               │
│ Design: Compute effective rank of Θ(x,x) for both models    │
│ Metric: Rank / (T V), rank vs forecasting F1 correlation    │
│ Cost: ~1 GPU-day (gradient computation)                     │
│ Expected Gain: Theoretical explanation of model dependency  │
├─────────────────────────────────────────────────────────────┤
│ E-R4: MEND Full Comparison                                  │
│ Target: C3 claim validation                                 │
│ Design: Run MEND on all setups from Table 3                 │
│ Metric: Edit Success, EM Drop %                             │
│ Cost: ~2 GPU-days (meta-model training)                     │
│ Expected Gain: Complete trade-off characterization          │
└─────────────────────────────────────────────────────────────┘

P2 Experiments (quality improvement):
┌─────────────────────────────────────────────────────────────┐
│ E-R5: Pooling Strategy Ablation                             │
│ Target: Eq. 4 design justification                          │
│ Design: Compare sum/mean/per-token/cross-attention pooling  │
│ Metric: F1 on BART0 head-only                               │
│ Cost: ~0.5 GPU-day                                          │
│ Expected Gain: Method design validation                     │
├─────────────────────────────────────────────────────────────┤
│ E-R6: Decoder-only LM Validation                            │
│ Target: Generalization beyond encoder-decoder               │
│ Design: Run on LLaMA-7B or GPT-2 with LoRA                  │
│ Metric: F1, EM Drop %                                       │
│ Cost: ~2 GPU-days                                           │
│ Expected Gain: Broader applicability claim                  │
└─────────────────────────────────────────────────────────────┘
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

The paper addresses a well-motivated problem with clean problem formulation and solid empirical breadth across models and tuning regimes. The logit-change transfer observation is a genuine scientific contribution, and the representation-based forecasting method shows practical utility in high-forgetting regimes. However, the score is constrained by:

- **Research Value (-1.0):** The practical benefit is marginal in low-forgetting regimes that cover most of the testbed (FLAN-T5 single-error). The method's main value is demonstrated primarily on BART0 Full FT.
- **Novelty (-0.5):** The problem formulation is novel, but the methods (frequency prior, representation similarity, logit approximation) are individually not new; their combination is the contribution. Novelty comparison is deferred due to Retrieval-Disabled Mode.
- **Validity/Soundness (-1.0):** The EM Drop formula inconsistency, unaddressed NTK invertibility issue, and experimental confound (model x dataset) weaken the paper's technical foundation.
- **Reproducibility (-0.5):** Good: public models/datasets, clear hyperparameters, algorithmic pseudocode. Minor gap: no variance reporting.
- **Presentation (-0.5):** Abstract leads with method failure; limitations too brief; MEND comparison buried in appendix.

**Post-Revision Target: [7.5, 8.0] / 10**

If the authors address the P0 items (EM Drop fix, NTK damping discussion, MEND in main text, variance reporting, expanded limitations) and the P1 items (dataset confound control, NTK rank analysis, bounded applicability statement), the paper would be a solid 7.5-8.0. The remaining P2 items (pooling ablation, decoder-only validation) would be nice-to-have but not required for acceptance.

### Rating Breakdown

| Dimension | Score (1-10) | Rationale |
|-----------|-------------|-----------|
| Research Value / Importance | 7 | Timely and practical problem; impact concentrated in high-forgetting regimes |
| Novelty / Originality | 6 | Problem formulation is novel; methods are combinations of known techniques |
| Technical Soundness | 6 | Clean empirical design but NTK derivation gaps and metric inconsistency |
| Reproducibility | 7 | Good transparency; missing variance reporting |
| Presentation / Clarity | 6 | Well-structured but abstract and limitations need improvement |
| **Overall** | **6.5** | Solid work with fixable weaknesses |