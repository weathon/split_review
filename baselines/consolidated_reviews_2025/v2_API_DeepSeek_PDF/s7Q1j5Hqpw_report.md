## Summary
# Final Review Report

## Summary

This paper addresses Variable Subset Forecasting (VSF), a practical problem where only a subset of variables is available at test time while full variables are available during training. The authors propose Shift-Resilient Diffusive Imputation (SRDI), a diffusion-based imputation framework that tackles two types of distribution shift in VSF: inter-series shift (changing correlations across variables) and intra-series shift (distribution changes across time windows). SRDI uses a divide-conquer denoising strategy that disentangles invariant and variant patterns to handle inter-series shift, and a meta-learning framework where each time window is treated as a task to adapt to intra-series shift. Experiments on four datasets with four forecasting backbones show that SRDI consistently improves forecasting accuracy over partial baselines and outperforms several imputation methods.

**Overall Assessment:** The paper tackles a meaningful real-world problem with a technically plausible approach. The two-type shift taxonomy is a useful conceptual contribution. However, several substantive issues weaken the current version: (1) the "diffusion" model effectively operates as a single-step denoising autoencoder (R=1), which is not adequately justified; (2) the experimental evaluation has fairness concerns (Partial baseline is information-unfair, Oracle outperformance hints at possible leakage); (3) results are backbone-dependent with near-negligible gains on some configurations; (4) the method section has key technical ambiguities (tensor shapes, optimization scope, additive decomposition assumption). The paper would benefit from clearer experimental controls, broader ablations, and a more circumspect presentation of claims.

## Strengths
1. **Well-defined problem framing.** The VSF problem is practically important (sensor failures, cross-region deployment) and is clearly distinguished from standard time-series imputation. The two-type shift taxonomy (inter-series and intra-series) provides a clean conceptual framework for understanding why existing methods struggle.

2. **Technically grounded approach.** The combination of invariant-variant pattern disentanglement (for inter-series shift) with meta-learning (for intra-series shift) within a single diffusion-based imputation framework is a thoughtful design. The invariant-variant dispatcher with correlation disparity regularization is a principled attempt to enforce temporal stability in the invariant branch.

3. **Comprehensive backbone integration.** SRDI is evaluated with four different forecasting backbones (MTGNN, ASTGCN, MSTGCN, T-GCN) on four datasets, demonstrating that the imputation framework is backbone-agnostic and can be integrated with diverse architectures. This is a strength for practical applicability.

4. **Competitive empirical results on most configurations.** On 14 out of 16 (dataset, backbone) combinations, SRDI improves forecasting MAE by 11-45% over the partial (no imputation) baseline. The method also outperforms a wide range of imputation baselines (MICE, CSDI, PriSTI, FDW, SSGAN, etc.) on the reported metrics.

5. **Reproducibility effort.** The paper provides code via an anonymous repository and includes detailed hyperparameter settings (Appendix A.6), which aids reproducibility.

## Weaknesses
1. **"Diffusion" model with R=1 is effectively a single-step denoising autoencoder.** The hyperparameters set num_steps=1, meaning the forward and reverse diffusion processes each consist of a single step. Standard diffusion models require 50-1000 steps for gradual denoising. With R=1, the method is more accurately described as a conditional denoising autoencoder. This design choice is neither discussed nor justified in the paper, and the "diffusive imputation" framing may be misleading. (Annotation: Page 4, Section 4.1)

2. **Problem formulation has an off-by-one indexing error and optimization scope ambiguity.** The lookback window is defined as {x^N_{t-L-1}, ..., x^N_t}, which gives L+1 elements instead of L. Additionally, Eq. (1) minimizes only over Φ (imputation parameters), but Algorithm 1 also optimizes Θ (forecasting parameters), creating a mismatch between the formal objective and actual training procedure. (Annotation: Page 3, Section 3)

3. **Experimental comparison is information-unfair for the Partial baseline.** The Partial setting uses only the available S variables (15%) for forecasting (without imputation), while SRDI imputes all N-S missing variables from the S observed ones and then uses all N variables. This means SRDI has access to more information. A fairer baseline would compare SRDI against another imputation method using the same observed subset, which is partially done via the imputation method comparison, but the primary "Partial vs Oracle vs SRDI" table (Table 1) uses an unfair comparison. (Annotation: Page 8, Section 6.1-6.2)

4. **Oracle outperformance raises potential data leakage concerns.** The paper touts that SRDI sometimes beats the Oracle (forecasting with all variables ground truth). While denoising regularization could theoretically improve forecasting, the fact that the meta-learning fine-tuning step uses the test subset's available variables to adapt the model means there is a risk of information leakage from the test set. This risk is not discussed. (Annotation: Page 8, Section 6.2)

5. **Results are backbone-dependent with near-negligible gains on TRAFFIC.** For ASTGCN+TRAFFIC, improvement is only +2.27% MAE; for T-GCN+TRAFFIC, only +0.62%. These are far from the 20-45% gains claimed in the abstract and introduction. The paper's narrative of "consistent superiority" is contradicted by its own data. (Annotation: Page 9, Table 1)

6. **Ablation study is limited to a single dataset (ECG5000).** Since the method's effectiveness varies substantially across datasets, ablation results on one dataset may not generalize. Component-level design choice ablations (e.g., self-attention vs RNN, adaptive vs fixed GCN) are missing. (Annotation: Page 10, Section 6.3)

7. **Invariant-variant additive decomposition is not justified.** The dispatcher assumes invariant and variant patterns are linearly separable via residual subtraction (h^Var_m = h^Var_{m-1} - h^Inv_m). This strong assumption is not discussed or validated. (Annotation: Page 5, Section 4.2.1)

8. **Conclusion lacks limitations.** The conclusion makes unqualified claims about outperforming SOTA methods without acknowledging the backbone-dependent performance degradation, the single-step diffusion limitation, or any other boundary conditions. (Annotation: Page 10, Section 7)

9. **Related Work is organized as a list rather than around comparison axes.** The section reads as "method A -> method B -> our method is better" without explaining why VSF-specific methods like FDW fail at handling distribution shifts. This weakens the novelty positioning. (Annotation: Page 2, Section 2)

10. **Only one subset size (15%) is tested.** The sensitivity of SRDI to the percentage of observed variables is not explored. Practical VSF scenarios could have 5% or 50% of variables available, and the reported gains may not generalize. (Annotation: Page 8, Section 6.1)

## Key Issues
### Issue 1: R=1 diffusion — single-step denoising autoencoder mislabeled as "diffusion" [Severity: Major]
The hyperparameters (Appendix A.6) set `num steps: 1`. This means the forward process adds noise in one step and the reverse process denoises in one step. Standard diffusion requires gradual multi-step denoising (R=50-1000) for the generative capability to emerge. With R=1, the model is a conditional denoising autoencoder. The paper should either (a) justify why a single step suffices, with ablation across R values; (b) change terminology to "denoising-based imputation"; or (c) implement multi-step diffusion and report results. This affects the core identity claim of the method.

### Issue 2: Information-unfair Partial baseline and Oracle outperformance concerns [Severity: Major]
The main comparison (Table 1) contrasts SRDI (which imputes all N-S variables and forecasts with N variables) against Partial (which forecasts with only S variables without imputation). This is a 100-15=85 variable information advantage. The Oracle outperformance (SRDI beating the full-data forecast) is presented as a strength but could indicate test-set information leakage through the meta-learning fine-tuning step. Both issues need explicit discussion and additional controlled experiments.

### Issue 3: Backbone-dependent performance contradicts claimed consistency [Severity: Major]
On TRAFFIC with ASTGCN (2.27% MAE improvement) and T-GCN (0.62%), the gains are near-negligible. The paper's narrative of "consistent superiority" and the abstract's general claims are not supported by these results. The paper should analyze when SRDI helps vs when it does not, and bound its claims accordingly.

### Issue 4: Additive decomposition assumption is unvalidated [Severity: Major]
The invariant-variant dispatcher assumes h^Var_m = h^Var_{m-1} - h^Inv_m, which treats patterns as linearly separable. No analysis is provided on whether this assumption holds, what happens when it fails, or whether nonlinear alternatives (e.g., gated decomposition) would perform better.

### Issue 5: Ablation study is under-powered [Severity: Major]
Ablations are conducted on a single dataset (ECG5000) and test only complete module removal, not design alternatives. The meta-learning ablation (SRDI-M) removes the entire inner-outer loop structure — but this changes the entire training paradigm, not just the adaptation mechanism. A controlled comparison (same training, with/without fine-tuning) would be more informative.

## Actionable Suggestions
### S1: Address the R=1 Diffusion Issue [Must]
- **Problem:** The model uses num_steps=1, making it a single-step denoising autoencoder.
- **Action:** Run an ablation with R = {1, 5, 10, 50} on one dataset (ECG5000 with MTGNN) to show whether more diffusion steps improve imputation quality. If R=1 is optimal due to task characteristics, add a clear justification paragraph.
- **Expected benefit:** Either strengthens the diffusion claim (if more steps help) or provides an honest rationale for the single-step design.

### S2: Fix Problem Formulation Errors [Must]
- **Problem:** Eq. (1) minimizes over Φ only (not Θ); lookback window uses t-L-1 instead of t-L+1.
- **Action:** (a) Change Eq. (1) to min_{Φ,Θ} or add a note that Θ is pre-trained separately. (b) Fix index: replace t-L-1 with t-L+1.
- **Expected benefit:** Improves mathematical correctness and reproducibility.

### S3: Add Fairer Experimental Comparisons [Must]
- **Problem:** Partial baseline is information-unfair; Oracle outperformance is unexplained.
- **Action:** (a) Add a Fair-Impute baseline: use the same 15 observed variables with a simple imputer (e.g., mean imputation, linear interpolation) before forecasting. (b) Add a controlled experiment where the meta-learning fine-tuning step is disabled during testing to isolate its contribution. (c) Conduct a leakage analysis: report what fraction of the Oracle-beating cases are statistically significant.
- **Expected benefit:** Clarifies whether gains come from genuine shift-handling or from information advantage / leakage.

### S4: Analyze Backbone-Dependent Performance [Must]
- **Problem:** Near-zero gains on TRAFFIC with some backbones contradict "consistent superiority."
- **Action:** (a) Add a paragraph analyzing per-backbone, per-dataset results. (b) Discuss why TRAFFIC (862 variables) shows smaller gains. (c) Bound the conclusion claim to settings where gains are meaningful. (d) Add results for at least one additional subset size (e.g., 5%, 30%) to show robustness.
- **Expected benefit:** Strengthens the paper's credibility by demonstrating awareness of boundary conditions.

### S5: Justify Additive Decomposition [Nice-to-have]
- **Problem:** h^Var = h^Var_{m-1} - h^Inv_m assumes linear separability.
- **Action:** Add a brief theoretical justification or a controlled experiment comparing additive decomposition vs. a gated nonlinear decomposition.
- **Expected benefit:** Strengthens methodological rigor.

### S6: Expand Ablation Study [Nice-to-have]
- **Problem:** Single-dataset ablation; only complete module removal tested.
- **Action:** (a) Run ablations on at least METR-LA in addition to ECG5000. (b) Add component-level ablations: self-attention vs GRU/LSTM in Temporal Dynamic Unit; adaptive GCN vs fixed GCN in Spatial Dependency Unit.
- **Expected benefit:** Validates design choices more convincingly.

### S7: Restructure Related Work [Nice-to-have]
- **Problem:** Listed as method summaries rather than compared along axes.
- **Action:** Reorganize around three axes: (1) imputation strategy for missing variables, (2) distribution shift handling, (3) diffusion-based TS imputation conditioning mechanisms. For each axis, explicitly state where prior work falls short and why SRDI addresses it.
- **Expected benefit:** Strengthens novelty positioning.

### S8: Add Limitations and Future Work to Conclusion [Must]
- **Problem:** Conclusion lacks limitations and reads as a re-stated contribution list.
- **Action:** Restructure into: validated findings (bounded), limitations (backbone dependency, subset-size sensitivity, R=1 constraint), and 2-3 concrete future directions.
- **Expected benefit:** Meets standard academic writing expectations and improves paper completeness.

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis

The current narrative flows as: Problem definition (VSF) → Two types of shift → Proposed solution (SRDI with divide-conquer + meta-learning) → Contributions → Related Work → Method → Experiments → Conclusion. The main issues are: (1) the introduction does not clearly separate problem, gap, and solution into distinct paragraphs; (2) the gap (why existing imputation fails specifically at VSF shift) is asserted rather than demonstrated; (3) the "diffusive imputation" framing sets wrong expectations since R=1.

### Preferred Storyline: "Handling Distribution Shift in Variable Subset Forecasting via Invariant-Variant Decomposition and Meta-Learning"

**Narrative arc:** Real-world sensor failure → VSF problem → Two types of shift → Existing imputation methods fail because they don't model these shifts → Our insight: decompose inter-variable correlations into stable (invariant) and dynamic (variant) parts, then use meta-learning to handle cross-window distribution changes → SRDI integrates both in a denoising framework → Experiments show consistent but bounded improvements.

### Abstract Outline (5 sentences)

**S1 (Problem):** Variable Subset Forecasting (VSF) requires predicting future values when some sensors are entirely missing at test time, creating two types of distribution shift: inter-series (changing variable correlations) and intra-series (changing window distributions).

**S2 (Gap):** Existing impute-then-forecast pipelines for VSF do not model these shifts, causing systematic imputation errors that propagate to forecasting.

**S3 (Method):** We propose SRDI, which (i) disentangles invariant and variant inter-variable patterns through a divide-conquer denoising process to mitigate inter-series shift, and (ii) employs a meta-learning paradigm treating each time window as a task to adapt to intra-series shift.

**S4 (Result):** On four real-world benchmarks (METR-LA, TRAFFIC, SOLAR, ECG5000) with four forecasting backbones, SRDI improves forecasting MAE by 2-45% over forecasting with raw partial data, and outperforms 12 imputation baselines.

**S5 (Bounded implication):** These gains are largest on datasets with strong spatiotemporal structure (METR-LA, SOLAR) and more modest on high-dimensional settings (TRAFFIC), suggesting boundary conditions for deployment.

### Introduction Outline (4 paragraphs)

**P1 — The VSF problem and its practical importance [Role: Motivate + Define]**
- Sentence-level plan: (1) IoT sensor failures cause missing entire variable sequences. (2) This differs from standard missing data because complete variables are absent. (3) VSF task definition with example (air quality monitoring, cross-region deployment). (4) The concrete challenge: how to forecast when only a small subset S of the original N variables is available.
*Transition to P2:* "The standard solution path is impute-then-forecast, but this approach falters due to distribution shift."

**P2 — Why existing imputation methods fail in VSF [Role: Gap analysis]**
- Sentence-level plan: (1) Impute-then-forecast is the natural approach. (2) Two types of shift that harm imputation: inter-series (changing correlations, not covariate shift) and intra-series (window distributions). (3) Concrete explanation of why each shift type degrades imputation quality. (4) Existing methods (CSDI, PriSTI, FDW) each address one aspect but not the combined shift challenge.
*Transition to P3:* "To handle both shift types simultaneously, we design SRDI with two complementary mechanisms."

**P3 — SRDI intuition at a high level [Role: Solution preview]**
- Sentence-level plan: (1) For inter-series shift: decompose into invariant patterns (stable correlations) and variant patterns (dynamic correlations) via a denoising network; process separately and recombine. (2) For intra-series shift: treat windows as meta-learning tasks, enabling rapid adaptation. (3) Both components operate within a single imputation framework trained end-to-end.
*Transition to P4:* "We validate this approach on four real-world datasets."

**P4 — Contribution summary and roadmap [Role: Claims + Paper structure]**
- List contributions with bounded language. End with paper organization note.

### Alternative Storyline Option: "Shift-Resilient Imputation for VSF"

If the authors prefer to keep the current title, a middle ground is to strengthen the problem-gap-solution separation in the introduction while keeping the contribution bullets largely intact. Key changes: P1 focuses on VSF definition only; P2 provides a concrete gap table (which methods handle which shift types); P3 introduces SRDI; P4 summarizes contributions.

## Priority Revision Plan
### P0 (Critical — Must fix before resubmission)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0.1 | R=1 diffusion misrepresentation | Run ablation with R={1,5,10,50}; justify or rename method | Clarifies core method identity | Medium |
| P0.2 | Problem formulation errors (off-by-one, min over Φ only) | Fix indexing; align Eq. (1) with Algorithm 1 | Prevents reproducibility issues | Low |
| P0.3 | Unfair Partial baseline | Add matched-information imputation baseline (e.g., mean/linear) | Strengthens empirical rigor | Low |
| P0.4 | Missing limitations in Conclusion | Restructure into validated findings + limitations + future work | Meets academic standards | Low |
| P0.5 | Overclaiming "consistent superiority" | Add analysis paragraph on backbone-dependent results; bound claims | Improves scientific credibility | Low |

### P1 (High priority — Should fix)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P1.1 | Oracle outperformance unexplained | Add controlled experiment without fine-tuning; leakage analysis | Clarifies source of gains | Medium |
| P1.2 | Single-dataset ablation | Repeat ablation on METR-LA; add design-choice ablations | Generalizes ablation findings | Medium-High |
| P1.3 | Only one subset size (15%) tested | Add results for S = {5%, 15%, 30%, 50%} | Demonstrates robustness | Medium |
| P1.4 | Related Work is a list | Restructure around 3 comparison axes | Strengthens novelty positioning | Medium |

### P2 (Nice-to-have)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P2.1 | Additive decomposition unvalidated | Add gated decomposition comparison or theoretical justification | Methodological depth | High |
| P2.2 | Tensor shape ambiguity in TSR | Add explicit shapes for each transformation | Reproducibility | Low |
| P2.3 | Meta-learning asymmetry (Φ only in inner loop) | Discuss or test symmetric adaptation | Completeness | Low |
| P2.4 | Time complexity without actual runtime | Report wall-clock time and GPU memory | Practical assessment | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|----------------|-------------------|
| E1 | Overall VSF performance (Table 1) | 4 datasets × 4 backbones; S=15%; L=H=12; train/val/test=70/10/20 | MAE, RMSE | SRDI beats Partial in all 16 combos; beats Oracle in most | C1, C4 | Partial baseline is information-unfair; TRAFFIC gains negligible for ASTGCN/T-GCN |
| E2 | Imputation method comparison (Figs 2-3, 6-7) | 12 imputation baselines on ECG5000, METR-LA, TRAFFIC, SOLAR | MAE, RMSE | SRDI achieves best MAE/RMSE across all datasets | C4 | Only shown with MTGNN backbone; other backbones not tested |
| E3 | Ablation: spatiotemporal modules (Fig 4) | SRDI-TS, SRDI-T, SRDI-S variants on ECG5000 | MAE, RMSE | Full SRDI > all variants | C3 | Single dataset only |
| E4 | Ablation: invariant-variant dispatcher (Fig 4) | SRDI-IV (no dispatcher), SRDI-V (no variant) on ECG5000 | MAE, RMSE | SRDI > SRDI-IV > SRDI-V | C3 | No ablation for alternative decomposition mechanisms |
| E5 | Ablation: meta-learning (Fig 4) | SRDI-M (no meta-learning) on ECG5000 | MAE, RMSE | SRDI > SRDI-M | C3 | Removes entire inner-outer loop, not a controlled comparison |
| E6 | Dispatcher visualization (Fig 5, 8-10) | Adjacency matrix difference over time for invariant vs variant | Mean diff plot | Variant shows larger fluctuations | C3 | Qualitative only; no quantitative metric of disentanglement quality |
| E7 | Hyperparameter sensitivity (Table 2) | ϖ = {0, 0.0001, 0.0005, 0.001, 0.01, 0.1, 0.3} on ECG5000 | MAE, RMSE | Optimal ϖ = 0.0005 | C3 | Single dataset; only one hyperparameter tested |
| E8 | Complexity analysis (Appendix C) | O(max(K*R*N*T*T, K*R*N*N*T)) | Theoretical O | — | — | No actual runtime/memory numbers; excludes forecasting model |

### Research-Theme Gap Diagnosis

1. **New knowledge claim (C2: shift taxonomy):** The two-type shift categorization is useful but the paper does not empirically demonstrate that these shifts exist in the evaluated datasets or quantify their severity.
2. **Reproducibility:** Partially supported (code available, hyperparameters listed). However, tensor shape ambiguities (TSR module) and the R=1 choice without justification reduce full reproducibility.
3. **Impact on practice/understanding:** The paper shows empirical gains but does not provide deployment-relevant metrics (inference latency, memory, robustness to different missing ratios). The practical significance for IoT deployment is asserted but not quantified.

### Proposed Research Experiments (P0/P1/P2)

**P0-Exp A: Diffusion step ablation** [Target: C1 — diffusion identity]
- Hypothesis: More diffusion steps (R=5,10,50) will improve imputation quality but increase runtime.
- Design: Run SRDI with R={1,5,10,50} on ECG5000+MTGNN; report MAE, RMSE, and inference time.
- Success criterion: If R>1 improves MAE by >2%, the method should use more steps; if not, provide justification.
- Expected quality gain: Clarifies the "diffusion" framing — either validates the approach or triggers a rename.

**P0-Exp B: Controlled fine-tuning ablation** [Target: C1, C3 — meta-learning contribution]
- Hypothesis: The fine-tuning step is responsible for most of the gain on intra-series shift.
- Design: Compare (i) full SRDI, (ii) SRDI without fine-tuning (use meta-trained model directly), (iii) SRDI without meta-training (train on one window only, fine-tune on test). Report on all 4 datasets.
- Success criterion: Relative gain of (i) over (ii) quantifies fine-tuning contribution; gain of (ii) over (iii) quantifies meta-training contribution.
- Expected quality gain: Decomposes the meta-learning contribution; addresses the Oracle outperformance concern.

**P1-Exp C: Subset-size sensitivity** [Target: C1, C4 — practical robustness]
- Hypothesis: SRDI's advantage over Partial decreases as S increases (more observed variables = less need for imputation).
- Design: Repeat Table 1 with S={5%, 15%, 30%, 50%} on METR-LA and TRAFFIC with MTGNN backbone.
- Success criterion: Monotonic trend where SRDI's relative gain decreases with S; identification of the "break-even" S ratio.
- Expected quality gain: Establishes practical deployment boundaries.

**P1-Exp D: Cross-dataset ablation** [Target: C3 — ablation generality]
- Hypothesis: Ablation patterns on METR-LA will be similar to ECG5000.
- Design: Repeat E3, E4, E5 on METR-LA in addition to ECG5000.
- Success criterion: Same rank ordering (full SRDI > ablated variants) on both datasets.
- Expected quality gain: Generalizes ablation conclusions.

**P2-Exp E: Decomposition mechanism comparison** [Target: C3 — method validation]
- Hypothesis: Additive decomposition (h^Var_{m-1} - h^Inv_m) is a reasonable approximation.
- Design: Compare additive decomposition vs. gated nonlinear decomposition vs. no decomposition on ECG5000.
- Success criterion: Additive and gated decomposition perform similarly; or gated improves by >3%.
- Expected quality gain: Validates or improves the core decomposition assumption.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

**Rationale:** The paper addresses a practically relevant problem (VSF) with a technically thoughtful approach (invariant-variant decomposition + meta-learning). The two-type shift taxonomy is a useful conceptual contribution. However, the score is constrained by several significant issues:
- The "diffusion" model operates at R=1 (single-step), which undermines the core methodological claim and requires either justification or relabeling.
- The experimental evaluation has fairness concerns (Partial baseline information disadvantage; Oracle outperformance unexplained).
- Key results are backbone-dependent with near-negligible gains on some configurations (TRAFFIC: 0.62% improvement), contradicting the "consistent superiority" narrative.
- The problem formulation contains an off-by-one indexing error and optimization scope ambiguity.
- Ablation studies are limited to a single dataset.
- The conclusion lacks limitations and future work, which is below standard expectations for a conference submission.

**Primary scoring dimensions:**
- Research value/contribution: 5.5/10 (good problem framing, useful taxonomy, but method novelty unclear without external verification)
- Validity/soundness: 5.0/10 (formulation errors, experimental fairness concerns, R=1 issue)
- Novelty strength: Requires external literature verification (deferred — Retrieval-Disabled Mode); provisionally assessed as incremental based on in-manuscript evidence
- Reproducibility: 6.0/10 (code available, hyperparameters listed, but tensor shape ambiguities)

**Post-Revision Target: [7.0, 7.5]/10**

If the authors address all P0 items (fix formulation errors, run R ablation, add fair baseline, restructure conclusion, bound claims) and P1.1-P1.3 (controlled fine-tuning ablation, cross-dataset ablation, subset-size sensitivity), the paper could reach 7.0-7.5. This target assumes the core idea (invariant-variant decomposition for shift-handling in VSF) is validated by the additional experiments and that the R=1 issue is resolved (either by using more steps or by honestly relabeling the method). Achieving this target requires addressing experimental fairness and claim boundedness as the highest priority items.