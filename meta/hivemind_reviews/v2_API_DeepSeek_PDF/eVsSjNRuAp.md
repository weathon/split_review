## Summary
# Final Review Report

## Summary

This paper proposes **Predictive Differential Training (PDT)**, a plug-in training acceleration framework that combines Koopman operator theory with differential learning. The core idea is to use Dynamic Mode Decomposition (DMD) to predict weight trajectories, then selectively apply these predicted updates only to parameters whose predictions satisfy two quality criteria (quantity and direction). A rollback scheduler falls back to standard SGD when prediction quality is insufficient.

PDT is evaluated on FCN, AlexNet, ResNet-50, and ViT-Base across CIFAR-10 and ImageNet-1K, demonstrating 10-40% reduction in wall-clock time to reach baseline best loss while maintaining comparable accuracy. The masking strategy is validated through comparison with random selection baselines, showing that strategic selection based on training dynamics is critical. The framework integrates with SGD, momentum-SGD, and Adam optimizers.

**Overall assessment:** The paper introduces a well-motivated and technically sound integration of Koopman-based prediction into DNN training. The masking strategy addresses a genuine limitation of prior all-parameter predictive training approaches. However, several methodological concerns (criteria design, oracle toy example, per-epoch overhead understatement), missing ablations (isolating masking from scheduling), and reproducibility gaps (algorithm details) limit the current contribution strength. Novelty claims cannot be fully verified without external literature comparison (deferred due to retrieval limitations in this run).

## Strengths
1. **Novel problem framing.** The paper identifies a genuine limitation in prior Koopman-based predictive training approaches—the lack of adaptive mechanisms for per-parameter prediction quality—and proposes a concrete solution via masking. This reframing of "all-parameter prediction" as a problem to be solved by differential treatment is the paper's strongest conceptual contribution.

2. **Clear empirical demonstration of the failure mode.** Figure 2 convincingly shows that unselective Koopman prediction applied to all parameters leads to training divergence as network depth increases, establishing clear motivation for the proposed masking strategy.

3. **Comprehensive evaluation across architectures and optimizers.** The experiments cover multiple architectures (FCN, AlexNet, ResNet-50, ViT-Base), datasets (CIFAR-10, ImageNet-1K), and optimizers (SGD, momentum, Adam), demonstrating that PDT can be integrated as a plug-in. The 5-seed repetition is a good practice.

4. **Honest negative results.** The validation-loss-based scheduling experiment (Section 4.3) transparently shows when PDT's approach fails, which is rare and commendable in optimization papers. The non-i.i.d. experiment (Appendix A.6) further tests robustness under challenging data distribution settings.

5. **Computational complexity analysis.** Section 3.3 provides a clear O(N×h²) complexity analysis of the DMD computation, and Appendix A.4 validates this with FLOPs measurements, enabling readers to assess the practical overhead.

## Weaknesses
1. **Masking criteria have scale and strictness issues.** The quantity criterion (Eq. 8) compares a τ-step predicted change norm against a 1-step SGD change norm, creating a scale-dependent bias that makes the criterion more permissive for larger τ. The direction criterion (Eq. 9) requires every intermediate prediction step to align with the single SGD step direction, which is overly restrictive for curved trajectories.

2. **Toy example overpromises acceleration.** The toy example in Section 3.2 claims ~60% acceleration using oracle-based subset selection with 3× higher learning rates. PDT's actual acceleration (10-40%) is substantially lower, and the example's mechanism (increased LR) differs from PDT's mechanism (DMD-based weight prediction). This discrepancy is not discussed.

3. **Per-epoch overhead understated.** The claim "computational load... is comparable to that of batch-level updates" (Section 4.1) is not fully accurate given the measured 23-25% per-epoch overhead (69.71 vs 56.74 TFLOPs for AlexNet, and 541.42s vs 432.79s per epoch for ViT-Base). The paper does not transparently discuss the conditions under which PDT yields net compute savings.

4. **Masking vs. scheduling confound in key comparison.** The Figure 2 comparison between PDT and unselective Koopman prediction uses a fixed schedule (3 SGD + 5 prediction steps) for the baseline, while PDT's schedule is determined adaptively by the masking strategy. This confounds two variables: masking content and prediction frequency.

5. **Algorithm reproducibility gaps.** Algorithm 1 omits several critical implementation details: DMD variant (exact DMD vs. projected DMD, rank truncation parameter), weight assembly rule (replacement vs. additive), and history matrix update policy (sliding window vs. growing window).

6. **Missing ablation on masking criteria.** The paper validates masking vs. random selection (Section 4.2), but does not ablate the two criteria (quantity vs. direction) independently. It is unclear which criterion contributes more to PDT's success and whether one alone suffices.

7. **Novelty cannot be independently verified in this run.** Due to Retrieval-Disabled Mode, external literature comparison is unavailable. The paper builds on prior Koopman-based training works (Dogra & Redman 2020, Tano et al. 2020), but the novelty of the specific masking strategy relative to adaptive optimization literature cannot be assessed without external search.

## Key Issues
### Issue 1 (Major): Masking Criteria Design Flaws
**Location:** Page 5 - Section 3.1, Equations (8)-(9)

**Problem:** The quantity criterion (Eq. 8) compares a τ-step predicted weight change norm against a 1-step SGD change norm without normalizing for the prediction horizon. For τ > 1, even poor τ-step predictions will have larger norms than a single SGD step simply due to accumulation, making this criterion too permissive. The direction criterion (Eq. 9) requires all τ intermediate prediction steps to align with the single SGD direction, which is overly restrictive for curved training trajectories.

**Impact:** These design issues may cause the masking strategy to either accept too many poor predictions (quantity criterion) or reject too many good predictions (direction criterion), potentially limiting PDT's acceleration benefit.

**Action:** Replace the quantity criterion with a per-step normalized ratio: accept prediction if `∥w^pred_{i+τ} - w_i∥ / τ > γ · ∥w^opt_{i+1} - w_i∥` (with γ < 1). Relax the direction criterion to only require end-to-end direction consistency: `(w^pred_{i+τ} - w_i)·(w^opt_{i+1} - w_i) > 0`. Add an ablation study comparing strict vs. relaxed criteria.

### Issue 2 (Major): Toy Example Does Not Reflect PDT's Mechanism
**Location:** Page 5 - Section 3.2, toy example

**Problem:** The toy example demonstrates acceleration via hand-picked 3× higher learning rates for a subset of variables, achieving ~60% acceleration. PDT uses DMD-based weight prediction with automatic masking, achieving 10-40% acceleration. The example's mechanism (increased LR) differs fundamentally from PDT's (prediction-based update), and the gap between 60% and 10-40% is not explained.

**Impact:** Readers may overestimate PDT's expected acceleration. The example should be reframed as an upper-bound oracle scenario, not a representative result.

**Action:** Add a paragraph explicitly stating: "This toy example illustrates an idealized upper bound where the optimal subset is known in advance. In practice, PDT's automatic masking achieves lower but still meaningful acceleration (10-40%)." Also clarify that the example uses LR acceleration, not prediction-based acceleration.

### Issue 3 (Major): Validation-Loss Scheduler Comparison Needs Baseline
**Location:** Page 9 - Section 4.3, Figures 8

**Problem:** The experiment shows that validation-loss-based switching between prediction and SGD fails catastrophically. However, it does not show whether PDT's full method (masking + rollback) avoids this failure under the same experimental setup. Without this direct comparison, the reader cannot attribute PDT's stability specifically to the masking strategy.

**Action:** Add a controlled experiment comparing three conditions under identical settings: (a) validation-loss switching only, (b) PDT with masking + rollback, (c) PDT without masking (rollback only). State explicitly that (b) does not exhibit the failure shown in Figure 8, citing the relevant Figure 5 result.

### Issue 4 (Major): Per-Epoch Overhead and "Comparable" Framing
**Location:** Page 6 - Section 4.1, computational load statement

**Problem:** The paper states computational load is "comparable to that of batch-level updates," but reported data shows 23-25% per-epoch overhead (69.71 vs 56.74 TFLOPs for AlexNet; 541.42s vs 432.79s per epoch for ViT-Base). This overhead is not negligible.

**Action:** Replace the "comparable" claim with a transparent trade-off statement. Provide a threshold analysis: "PDT's per-epoch overhead is ~23-25%. If PDT reduces total epochs by more than this percentage, total compute is reduced. For ViT-Base on ImageNet, the 10.2% runtime reduction is lower than the per-epoch overhead, meaning net compute savings are modest in that setting."

### Issue 5 (Major): Algorithm Reproducibility Gaps
**Location:** Page 13 - Appendix A.2, Algorithm 1

**Problem:** Algorithm 1 omits several implementation details required for reproducibility: (1) DMD variant (exact DMD, projected DMD, rank truncation), (2) weight assembly rule after masking (element-wise replacement or additive), (3) history matrix update policy (FIFO sliding window or growing window).

**Action:** Add explicit specifications to Algorithm 1: (a) "Compute rank-r truncated SVD of W (r = 10)" or similar, (b) "Assemble w_j(t) = M_j * w^pred_j(t) + (1-M_j) * w^opt_j(t)", (c) "Update W by removing the oldest column and appending the latest weight vector."

## Actionable Suggestions
### S1 (Must): Revise Masking Criteria Design
**Location:** Page 5 - Section 3.1, Equations (8)-(9)

Revise the quantity criterion to control for prediction horizon:
- Replace Eq. (8) with `(1/τ) * ∥w^pred_{i+τ} - w_i∥ > γ * ∥w^opt_{i+1} - w_i∥`, where γ ∈ (0.5, 1.0) is a discount factor.
- Clarify that `∥·∥` denotes absolute value for scalar weights (per-parameter masking), or vector norm over parameter groups if group-wise masking is used.
- Relax Eq. (9) to only require end-to-end direction consistency: `(w^pred_{i+τ} - w_i) · (w^opt_{i+1} - w_i) > 0`.
- Add an ablation experiment comparing three masking criteria variants: (1) full strict criteria (current), (2) relaxed direction (end-to-end only), (3) relaxed quantity (per-step normalized). Report masking ratio and final convergence for each.

### S2 (Must): Reframe Toy Example and Disclose Gap
**Location:** Page 5 - Section 3.2

Add the following clarifying text after the toy example:
"The toy example demonstrates an oracle scenario where the optimal subset to accelerate is known. PDT achieves its acceleration without oracle knowledge, using the automatic masking strategy. The ~60% acceleration in the toy example represents an upper bound; PDT's practical acceleration (10–40%, Table 1) is lower due to the overhead of automatic selection and DMD computation."

### S3 (Must): Add Ablation Experiment on Masking vs. Scheduling
**Location:** Page 4 - Section 4.2 / Figure 2 comparison

Add a controlled experiment:
- Fix the prediction schedule (e.g., predict every 4 epochs for both methods).
- Compare: (a) unselective prediction (all parameters), (b) PDT masking, (c) random masking with same ratio.
- This isolates the effect of the masking strategy from any scheduling differences.

### S4 (Should): Provide Transparent Overhead Analysis
**Location:** Page 6 - Section 4.1

Replace the "comparable" claim with a frank paragraph:
"PDT increases per-epoch FLOPs by approximately 23-25% due to DMD computation. The net compute savings depend on the number of epochs saved. For AlexNet on CIFAR-10, PDT reduces total compute by 23.74% (2596.30 vs 3404.32 TFLOPs). For ViT-Base on ImageNet, the more modest 10.2% runtime reduction reflects the higher relative overhead of DMD for larger models. Practitioners should weigh the per-epoch overhead against expected epoch reductions."

### S5 (Should): Complete Algorithm 1 Specifications
**Location:** Page 13 - Appendix A.2

Add these implementation specifications to Algorithm 1:
- Step 6: "Compute rank-r truncated SVD of W (r = min(h, 10)) for numerical stability."
- Step 9: "For each parameter j: w_j(t) = M_j · w^pred_j(t) + (1 - M_j) · w^opt_j(t)"
- Step 16: "Maintain W as a FIFO queue: remove the oldest column, append the latest weight vector."

### S6 (Nice-to-have): Validate Masked Ratio Against Prediction Error
**Location:** Page 7 - Section 4.1

Add a scatter plot showing per-epoch masked ratio (x-axis) vs. actual DMD prediction error ∥w^pred - w^actual∥ (y-axis) for one representative run (e.g., AlexNet on CIFAR-10). A strong negative correlation would validate that the masking strategy correctly identifies genuinely good predictions. Also add a per-layer breakdown of masking ratio for ResNet-50 or ViT-Base.

### S7 (Nice-to-have): Non-i.i.d. Experiment — Add Final Accuracy Discussion
**Location:** Page 17-18 - Appendix A.6

The non-i.i.d. experiment shows both SGD and PDT suffer significant accuracy drops (from ~0.80 to ~0.71). Discuss whether PDT exacerbates or mitigates this distribution-shift vulnerability. If PDT relies on regular training dynamics for DMD prediction, non-i.i.d. data should degrade predictions; does the masking strategy degrade proportionate to the increased prediction error?

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

**Current structure (4-5 sentences):**

**S1 (Problem & Domain):** "Training deep neural networks can be viewed as a nonlinear dynamical system on the weight space, where Koopman operator theory enables data-driven prediction of weight trajectories."

**S2 (Prior Gap):** "Existing Koopman-based predictive training bypasses SGD iterations via weight prediction, but applying predictions uniformly to all parameters causes gradient explosion in large models."

**S3 (Proposed Method):** "This paper proposes Predictive Differential Training (PDT), which selectively applies DMD-predicted weight updates only to parameters whose predictions satisfy quality criteria derived from training dynamics."

**S4 (Key Results):** "Across FCN, AlexNet, ResNet-50, and ViT-Base, PDT reduces wall-clock time to reach baseline best loss by 10–40% while maintaining comparable accuracy, and integrates as a plug-in with SGD, momentum, and Adam."

**S5 (Bounded Implication):** "PDT demonstrates that per-parameter prediction quality assessment is critical for stable Koopman-based training acceleration, opening a new direction for data-driven optimization."

### Introduction Outline (Complete, 5 paragraphs)

**P1 — Stakes & Motivation (replaces current generic optimizer list):**
- Role: Establish the practical cost of training large DNNs and the unmet opportunity in weight-trajectory prediction.
- Claim: Training remains expensive despite optimizer advances; predicting weight updates could bypass gradient computation.
- Transition: "An emerging alternative models training as a dynamical system and uses Koopman theory for prediction, but this approach fails for large models."

**P2 — Prior Predictive Training & Its Limitation (merges current paragraphs 3-4):**
- Role: Introduce Koopman-based predictive training (Dogra & Redman, Tano et al.) and its uniform-all-parameter failure mode.
- Claim: All-parameter prediction causes gradient explosion in larger networks because different parameters exhibit different dynamics.
- Evidence: Reference Figure 2 as empirical demonstration.
- Transition: "This motivates the need for selective prediction based on per-parameter dynamics."

**P3 — PDT Proposal & Core Intuition (replaces current paragraph 5):**
- Role: Present PDT's core idea: per-parameter prediction quality assessment via masking.
- Claim: Two simple criteria (quantity and direction) identify weights with reliable predictions; only those receive predicted updates.
- Transition: "We now describe the masking strategy and acceleration scheduler."

**P4 — Contribution Summary:**
- Role: List three contributions (masking strategy, acceleration scheduler, plug-in compatibility).
- Keep current bullet points but bound language to avoid overclaiming.

**P5 — Paper Organization:**
- Role: Roadmap for remaining sections.
- Keep brief.

### Revised Title Candidates

**Current title:** "Predictive Differential Training Guided by Training Dynamics"
**Issues:** Does not communicate the specific problem (gradient explosion) or method (Koopman-based selective masking).

**Candidate A (Problem-Method-Effect):** "PDT: Preventing Gradient Explosion in Koopman-Based Predictive Training via Per-Parameter Prediction Quality Masking"

**Candidate B (Shorter, more focused):** "Selective Koopman Prediction for Stable Deep Learning Acceleration"

**Candidate C (Balanced, recommended):** "Predictive Differential Training: Per-Parameter Prediction Masks for Stable Koopman-Based Training Acceleration"

## Priority Revision Plan
### P0 — Critical (Must fix before resubmission)

| Priority | Issue | Location | Action | Expected Impact |
|----------|-------|----------|--------|-----------------|
| P0.1 | Masking criteria scale/strictness issues | Page 5, Eq. (8)-(9) | Normalize quantity criterion; relax direction criterion; add ablation | Criteria become theoretically sound and empirically validated |
| P0.2 | Algorithm reproducibility gaps | Page 13, Algorithm 1 | Specify DMD variant, assembly rule, window update policy | Enables independent reproduction |
| P0.3 | Toy example misalignment | Page 5, Sec 3.2 | Add clarifying text on oracle vs. automatic selection | Prevents overestimation of PDT gains |
| P0.4 | Per-epoch overhead understatement | Page 6, Sec 4.1 | Replace "comparable" with transparent trade-off analysis | Improves scientific honesty and practical guidance |

### P1 — High Priority (Should fix)

| Priority | Issue | Location | Action | Expected Impact |
|----------|-------|----------|--------|-----------------|
| P1.1 | Masking vs. scheduling confound | Page 4, Figure 2 | Add controlled experiment with fixed schedule | Isolates masking effect from scheduling |
| P1.2 | Validation-loss scheduler needs baseline | Page 9, Sec 4.3 | Add direct comparison: full PDT vs. val-loss scheduler | Validates masking as critical component |
| P1.3 | Abstract lacks quantitative anchors | Page 1, Abstract | Add bounded performance ranges (10-40% runtime reduction) | Improves reader expectations |
| P1.4 | "Compelling effectiveness" overclaim | Page 2, Introduction | Replace with quantitative reference to Table 1 | Eliminates promotional language |

### P2 — Nice-to-Have (Quality improvements)

| Priority | Issue | Location | Action | Expected Impact |
|----------|-------|----------|--------|-----------------|
| P2.1 | Masked ratio vs. prediction error validation | Page 7, Sec 4.1 | Add correlation analysis and per-layer breakdown | Strengthens masking strategy validation |
| P2.2 | Non-i.i.d. accuracy drop discussion | Page 17-18, Appendix A.6 | Add interpretation of accuracy degradation under non-i.i.d. | Adds practical deployment insight |
| P2.3 | Conclusion restructuring | Page 10, Sec 5 | Separate validated claims from future work | Improves narrative clarity |
| P2.4 | Title revision | Page 1 | Use Candidate C title | Better communicates contribution |

### Revision Effort Estimate

- P0 items: ~2 days (criteria re-derivation + ablation experiments + algorithm documentation + text revisions)
- P1 items: ~3 days (controlled experiments + additional baselines + text revisions)
- P2 items: ~2 days (analysis + minor text revisions)
- **Total estimated effort: ~7 days for a complete, high-quality revision**

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|-------------|-----------------|-------------------|
| E1 | Generalization: PDT accelerates training across architectures | FCN/AlexNet on CIFAR-10; ResNet-50/ViT-Base on ImageNet-1K; baselines=SGD/Momentum/Adam | Time to baseline best loss (s), runtime per epoch (s), runtime reduction (%) | 10-40% runtime reduction across models | C3 (plug-in compatibility) | Per-epoch overhead not isolated; ViT shows modest 10.2% gain |
| E2 | Masking strategy: comparison with random selection | AlexNet/CIFAR-10; random weight acceleration with matched ratio | Training loss curves, convergence stability | Random selection fails; PDT succeeds | C1 (masking strategy effectiveness) | Masks scheduling confound; no ablation of individual criteria |
| E3 | Masking strategy: comparison with random prediction masks | AlexNet/CIFAR-10; random Koopman prediction masks | Training loss curves, NaN occurrence | Random masks cause gradient explosion | C1 | Same schedule for both methods not explicitly controlled |
| E4 | Validation-loss scheduler as alternative | AlexNet/CIFAR-10; switch between DMD/SGD based on val loss | Train/val loss curves | Validation-loss scheduler fails catastrophically | Supports PDT's masking approach | Missing direct comparison: does full PDT avoid this failure? |
| E5 | Hyperparameter sensitivity | AlexNet/CIFAR-10; vary τ, Ti, T0, h | Train loss at convergence | Sensitivity curves provided | PDT robustness | No formal sensitivity analysis (e.g., one-at-a-time vs. factorial) |
| E6 | Learning rate / batch size sweep | AlexNet/CIFAR-10; lr∈[0.001,0.1], batch∈[32,512] | Final accuracy, best train loss, time to baseline best loss | PDT better at low LR; high LR unstable | Robustness | High LR instability not fully resolved |
| E7 | Cosine annealing LR scheduler | AlexNet/CIFAR-10; batch=256, CosineAnnealingLR | Same as E6 | Improved stability at high LR | Robustness improvement | One setting only (batch=256) |
| E8 | Optimizer compatibility | AlexNet/CIFAR-10; SGD/Momentum/Adam | Same as E6 | PDT works with all three | C3 | Varying learning rates across optimizers confounds comparison |
| E9 | FLOPs analysis | AlexNet/CIFAR-10; measure TFLOPs per epoch and total | TFLOPs | 23.74% total compute reduction | Computational efficiency claim | Only one architecture-dataset pair |
| E10 | Non-i.i.d. training data | AlexNet/CIFAR-10; same-class batching (non-i.i.d.) | Final accuracy, best train loss, runtime reduction | PDT still outperforms SGD under non-i.i.d. | Robustness | Both methods lose ~10% accuracy vs. i.i.d.; mechanism not analyzed |

### Research-Theme Gap Diagnosis

1. **New knowledge gap:** The paper establishes that per-parameter prediction quality assessment is important, but does not provide a theoretical understanding of *why* some parameters are easier to predict than others. The masked ratio observation (larger networks → lower ratio) is descriptive, not explanatory.

2. **Reproducibility gap:** Algorithm 1 lacks critical implementation details (DMD variant, assembly rule, window policy), reducing the community's ability to build on this work.

3. **Causal attribution gap:** Without isolated ablations (masking vs. scheduling, individual criteria), the paper cannot attribute PDT's gains specifically to its claimed mechanism. Alternative explanations (e.g., implicit regularization from intermittent SGD, effective learning rate variation) are not ruled out.

### Proposed Research Experiments (P0/P1/P2)

**P0 Exp A — Masking Criteria Ablation**
- **Target Claim:** C1 (masking strategy effectiveness)
- **Hypothesis:** Relaxed direction criterion (end-to-end only) preserves or improves PDT's acceleration
- **Minimal Design:** Run PDT on AlexNet/CIFAR-10 with three masking variants: (a) current strict criteria, (b) relaxed direction (end-to-end), (c) normalized quantity criterion
- **Controls:** Same prediction schedule (predict every 4 epochs), same hyperparameters
- **Metrics:** Training loss at epoch 60, runtime to baseline best loss, masking ratio over epochs
- **Success Criterion:** Variant (b) achieves ≥ similar runtime reduction with higher masking ratio
- **Estimated Cost/Time:** ~4 hours on single GPU
- **Expected Quality Gain:** Clarifies which criterion is essential; potentially improves PDT's acceleration

**P0 Exp B — Isolated Masking vs. Scheduling Control**
- **Target Claim:** C1 (masking strategy is the critical component)
- **Hypothesis:** With fixed prediction schedule, PDT-with-masking outperforms unselective prediction + PDT-without-masking
- **Minimal Design:** Fix schedule (e.g., predict every 4 epochs); compare: (a) unselective prediction, (b) PDT masking, (c) random masking with same ratio, (d) no prediction (SGD baseline)
- **Controls:** Same total epochs, learning rate schedule
- **Metrics:** Training/test loss, runtime, masking ratio
- **Success Criterion:** (b) outperforms (a) and (c) in both loss and stability
- **Estimated Cost/Time:** ~6 hours on single GPU
- **Expected Quality Gain:** Disentangles masking effect from scheduling; addresses the most significant confound in current experiments

**P1 Exp C — Full PDT vs. Validation-Loss Scheduler Direct Comparison**
- **Target Claim:** C1 + C2 (acceleration scheduler)
- **Hypothesis:** Under identical settings where validation-loss scheduler fails, full PDT (masking + rollback) maintains stable convergence
- **Minimal Design:** Same setup as Section 4.3 (AlexNet/CIFAR-10); compare: (a) validation-loss scheduler, (b) PDT full, (c) SGD baseline
- **Controls:** Identical random seed, data order, hyperparameters
- **Metrics:** Train/val loss curves, runtime to convergence, final accuracy
- **Success Criterion:** (b) avoids the catastrophic failure shown in Figure 8 for (a)
- **Estimated Cost/Time:** ~3 hours on single GPU
- **Expected Quality Gain:** Directly validates the masking strategy as essential

**P1 Exp D — Per-Layer Masking Ratio Analysis**
- **Target Claim:** C1 (masking strategy captures per-parameter dynamics)
- **Hypothesis:** Early layers and late layers exhibit different masking ratios
- **Minimal Design:** For ResNet-50 or ViT-Base training on ImageNet, record masking ratio per layer/residual block at each epoch
- **Controls:** Same hyperparameters as Figure 5
- **Metrics:** Per-layer masking ratio over epochs, correlation with layer depth
- **Success Criterion:** Statistically significant difference in masking ratio across layers
- **Estimated Cost/Time:** ~8 hours on multi-GPU (requires logging per-layer masks)
- **Expected Quality Gain:** Provides insight into which layers benefit most from prediction; guides future method design

**P2 Exp E — Prediction Error vs. Masking Ratio Correlation**
- **Target Claim:** C1 (masking strategy identifies "good" predictions)
- **Hypothesis:** Lower per-parameter prediction error correlates with higher masking probability
- **Minimal Design:** For one run, log both per-parameter DMD prediction error and mask decision. Compute correlation coefficient.
- **Controls:** Standard PDT settings
- **Metrics:** Pearson/Spearman correlation between prediction error and mask acceptance
- **Success Criterion:** Significant negative correlation (r < -0.3)
- **Estimated Cost/Time:** ~2 hours (analysis only, using existing run logs)
- **Expected Quality Gain:** Validates the masking strategy's core assumption

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 5.5 / 10

**Rationale:** The paper addresses an important problem (stabilizing Koopman-based predictive training) with a well-motivated solution (per-parameter prediction quality masking). The experimental evaluation is reasonably comprehensive across architectures and optimizers. However, the score is constrained by:

- **Research Value (6/10):** The core idea of selective prediction is sound, but the toy example confounds expectations (60% oracle vs. 10-40% actual), and the net compute savings are modest (10-40% runtime reduction with 23-25% per-epoch overhead). The practical value for large-scale training is not yet compelling.
- **Novelty (Unverifiable → 5/10):** External literature comparison is unavailable in this run. The method builds directly on prior Koopman-based training works (Dogra & Redman 2020, Tano et al. 2020). The masking strategy appears to be a new contribution, but its novelty relative to adaptive optimization literature cannot be assessed without external search. Marked as deferred.
- **Validity/Soundness (5/10):** Masking criteria have design issues (scale mismatch, overly restrictive direction criterion). The key comparison (Figure 2) confounds masking with scheduling. Algorithm reproducibility gaps exist.
- **Reproducibility (4/10):** Algorithm 1 omits critical implementation details (DMD variant, assembly rule, window policy). The current description is insufficient for independent reproduction.

**Post-Revision Target:** [6.5, 7.5] / 10

**Conditions for reaching target:**
- Fix masking criteria design issues (P0.1)
- Add controlled ablation experiments (P0.2, P1.1, P1.2)
- Complete algorithm documentation (P0.3)
- Provide transparent overhead analysis (P0.4)
- Address overclaiming language (P1.4)
- If external literature can verify novelty with concrete differentiation from prior work, the upper bound may increase.