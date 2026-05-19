## Summary
# Final Review Report

## Summary

This paper introduces DPaI (Differentiable Pruning at Initialization), a method that converts the discrete Node-Path Balancing (NPB) principle into a differentiable optimization framework for neural network pruning at initialization. The key technical innovation is replacing NPB's per-layer discrete integer programming with a continuous gradient-based optimization over learnable score parameters, using Straight-Through Estimation (STE) through Top-K binarization to maximize the number of effective nodes, paths, and kernels under a sparsity constraint. DPaI is evaluated on CIFAR-10, CIFAR-100, Tiny-ImageNet, and ImageNet-1K across ResNet, VGG, and EfficientNet architectures, showing consistent accuracy improvements of 1-4.6% over prior PaI methods at high sparsity (96-99%) with comparable pruning time.

**Core strengths:** The differentiable formulation is a meaningful conceptual advance over discrete NPB, enabling global (rather than per-layer) mask optimization. The paper provides a thorough convergence analysis (under a single-edge-swap assumption) and extensive ablation on hyperparameter effects. The method is data-agnostic, which improves reusability across tasks. The pruning time is competitive and much more stable than PHEW or NPB across model sizes.

**Core weaknesses:** (1) The SOTA claims lack statistical rigor — main experimental results (Figure 1) do not report variance, and "significantly" is used without significance testing. (2) ImageNet-1K comparison only includes SynFlow (not NPB, the direct predecessor), weakening the key "differentiable vs discrete NPB" claim at scale. (3) The convergence analysis is limited to single-edge swaps while the actual algorithm performs simultaneous multi-edge updates. (4) The kernel-level pruning derivation has notation gaps (missing γ scaling, unclear 4D kernel → scalar mapping). (5) The conclusion introduces unsupported claims about NAS and sparse training applications. (6) Novelty claims ("first differentiable PaI method considering topology") cannot be verified without external literature comparison in this run.

## Strengths
1. **Conceptually clean differentiable formulation of NPB.** The core idea — converting the discrete NPB integer program into a continuous optimization over score parameters with Top-K binarization and STE — is elegant and directly addresses a genuine limitation of the prior NPB method. This enables global mask optimization rather than per-layer decomposition, which is a meaningful improvement over Pham et al. (2023).

2. **Extensive empirical evaluation across multiple architectures and sparsity levels.** The paper evaluates DPaI on three architectures (ResNet-20, ResNet-18, VGG-19) across four sparsity levels (68.38% to 99%) on three datasets (CIFAR-10, CIFAR-100, Tiny-ImageNet), plus ImageNet-1K on EfficientNet-B0 and ViT-B/16 experiments (limited scope). This breadth supports the generalizability claims.

3. **Competitive pruning time.** DPaI achieves pruning times of 70-90 seconds across model sizes, which is much more stable than PHEW (78-6928s) and NPB (20-430s). The time is also sparsity-independent, unlike iterative methods. This practical efficiency is a genuine advantage.

4. **Ablation study on tradeoffs.** Figure 2 and the analysis of effective nodes vs paths vs kernels provides useful insight into the multi-objective nature of the NPB principle. The Pareto front analysis and the "Effective Nodes Plus" metric (log RN + log RC) help users understand the method's behavior.

5. **Convergence analysis framework.** Despite assumptions, Section 3.3 provides a principled mathematical framework showing that single-edge updates toward the NPB objective monotonically increase effective paths and nodes. This theoretical grounding is more than most PaI methods provide.

6. **Data-agnostic property.** Because DPaI does not use training data or labels during pruning, the resulting mask can be transferred across datasets. The paper demonstrates this reusability trait, which is practical for deployment scenarios.

## Weaknesses
1. **Incomplete statistical reporting for main results.** The core empirical evidence (Figure 1, CIFAR-10/100/Tiny-ImageNet) is presented without variance, confidence intervals, or significance tests. The term "significantly outperforms" is used qualitatively, not statistically. Without seed variance, readers cannot assess whether the reported gains (1-4.6%) are reliable. (Page 8, Section 4.1)

2. **Insufficient baseline coverage on ImageNet-1K.** The large-scale ImageNet experiment (Table 1) compares DPaI only against SynFlow. NPB — the direct predecessor and main comparison point — is not evaluated at this scale. The 0.8% average improvement over SynFlow is modest, and without NPB comparison, the core claim ("differentiable NPB outperforms discrete NPB") remains unverified at scale. (Page 9, Table 1)

3. **Convergence analysis gap.** Section 3.3 proves monotonic improvement under a single-edge-swap assumption, but Algorithm 1 performs simultaneous multi-edge updates. The paper does not address this gap or discuss whether the theoretical guarantees extend to the practical algorithm. (Pages 5-7, Section 3.3)

4. **Potential inconsistency in objective derivatives (Eq. 7 vs Eq. 2).** The update rule in Eq. (7) (Page 5) uses δRP/δs, while the derivation in Eq. (2) computes δ log RP/δs. If Eq. (7) indeed uses the un-logged derivative, the path and node/kernel objectives are scaled inconsistently, potentially affecting optimization behavior. (Page 4-5, Eqs. 2, 7)

5. **Kernel/Connection objective notation gaps.** The RC derivation lacks γ scaling for tanh, unlike the RN objective where γ is explicit (Eq. 5 vs RC text). The mapping from 4D convolution kernels to scalar mask scores is not clearly specified. (Page 5, RC derivation)

6. **Hyperparameter sensitivity acknowledged but not mitigated.** The paper admits hyperparameter sensitivity as a "major drawback" but offers no practical guidance for selecting α and β beyond grid search (36 combinations per experiment). The cost of this tuning is not reported, reducing the claimed efficiency advantage. (Page 10, Section 4.2)

7. **Conclusion overclaims.** The conclusion introduces unsupported claims about DPaI's applicability to NAS and sparse training with no experimental evidence. "State-of-the-art" is used without scope qualification, despite identified weaknesses in comparison coverage. (Page 10, Section 5)

8. **Novelty claims deferred.** Contribution 1 ("first differentiable PaI method considering topology") and the general SOTA claim cannot be verified without external literature comparison, which was unavailable in this review run. These claims should be treated as provisional. (Page 2, Contribution list)

## Key Issues
Ranked by Severity | Research-Value Impact | Validity Risk | Fixability | Confidence:

**Issue 1 (Major) — Missing variance and significance for main experimental results.**
- **Severity:** Major | **Validity Risk:** High | **Fixability:** Easy
- **Evidence:** Page 8, Section 4.1. Figure 1 reports accuracy without standard deviations or number of seeds. The word "significantly" is used without statistical testing.
- **Impact:** Without variance, readers cannot assess whether accuracy improvements (1-4.6%) are statistically reliable or within noise, especially at high sparsity where absolute accuracy is low.
- **Fix:** Report mean±std over ≥3 seeds for all experiments in Figure 1. Add a table in Appendix with per-seed results. Replace "significantly" with quantitative ranges.

**Issue 2 (Major) — Insufficient baselines on ImageNet-1K.**
- **Severity:** Major | **Validity Risk:** High | **Fixability:** Medium
- **Evidence:** Page 9, Table 1. Only SynFlow is compared on ImageNet-1K.
- **Impact:** The core claim of "differentiable NPB outperforms discrete NPB" cannot be verified at scale because NPB itself is not included in the ImageNet comparison.
- **Fix:** Add NPB (and ideally at least one more baseline) on EfficientNet-B0/ImageNet-1K. If compute-constrained, run on a subset (e.g., ImageNet-100) with full baseline set.

**Issue 3 (Major) — Theory-practice gap in convergence analysis.**
- **Severity:** Major | **Validity Risk:** Medium | **Fixability:** Medium
- **Evidence:** Pages 5-7, Section 3.3 vs Algorithm 1. Single-edge-swap proof does not match multi-edge practical implementation.
- **Impact:** The convergence guarantees shown mathematically may not hold for the actual algorithm. This weakens the theoretical contribution.
- **Fix:** Either (a) extend the analysis to multi-edge case, or (b) explicitly acknowledge the gap and add empirical convergence evidence to bridge it.

**Issue 4 (Major) — Potential objective inconsistency (Eq. 7).**
- **Severity:** Major | **Validity Risk:** High | **Fixability:** Easy
- **Evidence:** Page 4-5, Eq. (2) computes δ log RP/δs, but Eq. (7) uses δRP/δs in the update rule. If this is not a typo, the path objective is not log-scaled in the gradient while node/kernel objectives are.
- **Impact:** Inconsistent scaling could cause one objective to dominate and produce suboptimal masks.
- **Fix:** Clarify whether Eq. (7) should use δ log RP/δs (consistent with Eq. 2) or δRP/δs (justify the difference).

**Issue 5 (Major) — Hyperparameter tuning cost not quantified.**
- **Severity:** Major | **Validity Risk:** Medium | **Fixability:** Easy
- **Evidence:** Page 10, Section 4.2 and Appendix A. Grid search over 36 (α,β) combinations. The cost of this search is not reported.
- **Impact:** If tuning requires multiple full 3000-step runs, the practical efficiency advantage of PaI (reduced training cost) is partially offset by tuning overhead.
- **Fix:** Report total tuning cost (GPU-hours) and propose a default (α,β) recommendation based on ablation trends.

**Issue 6 (Minor) — Conclusion overclaims and missing limitations.**
- **Severity:** Minor | **Validity Risk:** Low | **Fixability:** Easy
- **Evidence:** Page 10, Section 5. Claims about NAS and sparse training are unsupported. No limitations paragraph.
- **Fix:** Add a limitations paragraph covering hyperparameter sensitivity, convergence gap, and ViT scope restriction. Remove unsupported application claims.

## Actionable Suggestions
### Must-Fix Items (Publication-Critical)

1. **Report multi-seed variance for all main results (Page 8, Figure 1).**
   Run each experiment (ResNet-20/CIFAR-10, ResNet-18/Tiny-ImageNet, VGG-19/CIFAR-100) at all four sparsity levels with ≥3 random seeds. Report mean ± std in Figure 1 or an Appendix table. Add a sentence: "All results are reported as mean ± std over 3 seeds; full per-seed results are in Appendix [X]."

2. **Add NPB to ImageNet-1K comparison (Page 9, Table 1).**
   Run NPB under the same EfficientNet-B0/ImageNet-1K setup at sparsity 0.3. Report mean ± std over 3 seeds alongside DPaI and SynFlow. If compute is prohibitive, add a smaller-scale comparison (e.g., ImageNet-100 or a single ResNet-50 experiment at 90% sparsity) that includes NPB, SynFlow, and DPaI.

3. **Fix Eq. (7) gradient inconsistency (Page 5, Eq. 7).**
   Replace δRP/δs with δ log RP/δs to match Eq. (2) and keep all objectives consistently log-scaled. If the current Eq. (7) is correct, add a justification explaining why RP (unlogged) is used here while the rest of the derivation uses log RP.

4. **Add γ scaling to RC objective (Page 5, RC derivation).**
   Add γ factor in the tanh argument for RC: `tanh(γ * N(m(l)_i,j))`, consistent with Eq. (5) for RN. Also add a note on how 4D convolution kernels are mapped to scalar scores.

5. **Add limitations paragraph to Conclusion (Page 10, Section 5).**
   Include: (a) hyperparameter sensitivity, (b) convergence analysis assumes single-edge swaps, (c) ViT experiments cover only linear layers, (d) novelty claims need literature verification. Remove unsupported NAS/sparse training claims.

### Nice-to-Have Improvements

6. **Add empirical convergence plots for multi-edge updates (Page 7, Algorithm 1).**
   The paper has convergence plots in Appendix L (Figure 5) — cite them in Section 3.3 and add a note bridging the single-edge theory to observed multi-edge behavior.

7. **Clarify "data-agnostic" vs "score-initialization-dependent" distinction (Page 10, Section 4.2).**
   Replace "independent of initial weights" with "independent of network weights (pruning uses only randomly initialized score parameters, not trained weights)."

8. **Quantify convergence criterion (Page 7, Section 3.4).**
   Replace "does not change significantly" with a concrete threshold, e.g., `if |R_NPB(t) - R_NPB(t-τ)| / R_NPB(t-τ) < 1e-4 for τ=100 consecutive steps`.

9. **Fix NBP → NPB acronym (Page 2, contribution list).**
   The contribution bullet uses "NBP" instead of "NPB" — correct to "Node-Path Balancing (NPB)."

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows: LTH motivation → PaI methods & limitation → Topology importance (Frankle/Su) → NPB principle → DPaI solution → Contribution list. This is functional but has three issues: (a) the transition from LTH to PaI is abrupt, (b) the gap statement over-generalizes existing PaI methods, (c) the solution paragraph (Page 2, lines 8-16) is too dense and introduces "non-linear integer programs" before explaining the intuition.

### Recommended Abstract Outline (4-sentence structure)

S1 — Problem: "Pruning at Initialization (PaI) removes weights before training to reduce computational costs, but existing PaI methods rely on discrete per-layer optimization that yields sub-optimal network topologies at high sparsity."

S2 — Gap: "A recently identified principle — Node-Path Balancing (NPB) — shows that maximizing effective nodes and information paths improves sparse network trainability, yet it requires solving NP-hard discrete programs per layer."

S3 — Method: "This paper introduces DPaI, which converts NPB into a differentiable objective using learnable score parameters and Straight-Through Estimation, enabling global, gradient-based mask optimization without layer-wise decomposition."

S4 — Key Result: "On CIFAR-10, CIFAR-100, and Tiny-ImageNet, DPaI achieves 1-4.6% accuracy gains over prior PaI methods at sparsity levels above 96%, with competitive pruning time. The method is data-agnostic and the pruning mask can be reused across datasets."

### Recommended Introduction Outline (5 paragraphs)

**P1 — Motivation (revised):** Start with the practical challenge: training large neural networks is expensive; pruning reduces cost. Explain that pruning after training has been well-studied, but pruning before training (PaI) offers greater efficiency gains. Reference LTH briefly as motivation, not as the starting point. End with the research question: can we find good sparse masks at initialization without iterative pruning?

**P2 — Prior PaI and its limitation (revised):** Survey PaI methods (SNIP, SynFlow, PHEW) but avoid over-generalizing — acknowledge that SynFlow and PHEW do consider topology. State the precise gap: these methods optimize per-connection importance or local connectivity, not the global count of effective information paths and activated nodes jointly.

**P3 — NPB principle and its bottleneck:** Introduce NPB (Pham et al., 2023): the idea of maximizing effective nodes and paths. Explain its discrete optimization formulation. State the bottleneck: the NP-hard discrete program must be decomposed per-layer, producing sub-optimal global masks.

**P4 — Differentiable NPB (DPaI):** Explain the key insight — replace discrete masks with differentiable score parameters, use Top-K binarization with STE, and optimize the NPB objective directly via gradient ascent. Emphasize that this is the first method to make NPB differentiable, enabling global optimization.

**P5 — Contributions and evidence preview:** List three contributions (as currently, but bound the "first" claim with "to our knowledge" and fix NBP→NPB). Preview key results with concrete numbers. Mention data-agnostic advantage.

### Alternative Storyline Candidate

A stronger narrative arc would be:
**Big Picture:** Deep learning efficiency is limited by redundant parameters.
**Gap:** Existing pruning methods either prune after training (costly) or prune at initialization but produce poor topologies.
**Insight:** The key to good PaI is not individual weight importance but the global shape of the sparse network (number of effective paths vs nodes).
**Solution:** DPaI makes the shape objective differentiable, enabling gradient-based mask optimization.
**Evidence:** Strong gains at high sparsity, stable pruning time, data-agnostic reuse.

## Priority Revision Plan
### P0 — Immediate (Before Next Submission)

1. **Add variance to all main experiments** (Page 8, Figure 1). Report mean±std over ≥3 seeds. This is the single highest-impact fix — without it, the reported "significant" improvements cannot be evaluated statistically.

2. **Fix Eq. (7) gradient inconsistency** (Page 5). Verify whether δRP/δs or δ log RP/δs is intended and make consistent. This is a correctness issue that could affect optimization behavior.

3. **Add γ scaling to RC objective** (Page 5). Ensure all three objectives (RP, RN, RC) use consistent log-scale and γ-scaling.

4. **Add NPB comparison on ImageNet-1K** (Page 9, Table 1). Without this, the "differentiable vs discrete" claim remains unverified at scale.

### P1 — Within 1-2 Weeks

5. **Rewrite Conclusion (Section 5)** to include a limitations paragraph covering hyperparameter sensitivity, convergence gap, and ViT scope. Remove unsupported NAS/sparse training claims.

6. **Quantify convergence criterion** (Page 7, Algorithm 1). Replace vague "does not change significantly" with a concrete tolerance.

7. **Fix NBP → NPB acronym** (Page 2, contribution list) and bound the "first" claim with "to our knowledge" qualifier.

8. **Add theory-practice gap discussion** (Section 3.3). Acknowledge that convergence analysis assumes single-edge swaps while the algorithm performs multi-edge updates. Cite Appendix L's empirical convergence plots.

### P2 — Before Final Version

9. **Clarify kernel-to-scalar mapping** for convolutional layers (Page 5, RC section). Provide explicit tensor shape equations.

10. **Report grid search cost** (Appendix A) — total GPU-hours for hyperparameter tuning.

11. **Add data-agnostic caveat** (Page 10, Section 4.2): clarify that "independent of initial weights" refers to network weights, not score parameters.

### Expected Impact After Fixes

- **Validity:** Variance reporting + Eq. (7) fix + NPB on ImageNet will significantly improve rigor.
- **Novelty clarity:** Bound "first" claims and fix acronyms.
- **Practical utility:** Quantified convergence + tuning cost + limitations help practitioners adopt DPaI.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|-------------|----------------|-------------------|
| E1 | Accuracy comparison at multiple sparsity levels (Fig 1) | CIFAR-10/ResNet20, CIFAR-100/VGG19, Tiny-ImageNet/ResNet18; 4 sparsity levels; baselines: Random, SNIP, Iter-SNIP, SynFlow, PHEW, NPB | Top-1 accuracy, effective nodes, effective paths | DPaI best or second-best in most settings; 1-4.6% gains at 96-99% sparsity | C2 (superior sparse subnetworks) | No variance reported; single-baseline-per-setting; no significance tests |
| E2 | ImageNet-1K scale verification (Table 1) | EfficientNet-B0, sparsity 0.3, 3 seeds | Avg ± std accuracy | DPaI 72.2±0.25% vs SynFlow 71.4±0.29% | C2 (scalability) | Only SynFlow baseline; NPB absent; modest 0.8% gain |
| E3 | Hyperparameter ablation (Fig 2) | α,β grid search across all arch/dataset combos | Effective nodes, paths, kernels, test accuracy | α,β highly impact performance; Pareto front exists; best values tend to favor node/kernel objectives | C2 (ablation) | Tuning cost not reported; no automated selection method |
| E4 | Pruning time comparison (Fig 3, Tables 3-5) | All arch/sparsity combos | Wall-clock seconds, FLOPs | DPaI 70-90s consistent across settings; better than NPB/PHEW | Efficiency claim | Sequential implementation; parallelization not yet tested |
| E5 | Extreme sparsity (Table 8, Appendix E) | ResNet18/Tiny-ImageNet at 99.68%, 99.90%; 5 seeds | Effective nodes, log paths, test acc | DPaI outperforms NPB; large node std at 99.90% (±203) | C2 (extreme sparsity) | High variability; nodes-paths-accuracy relationship is non-monotonic |
| E6 | ViT-B/16 experiment (Table 9, Appendix G) | Tiny-ImageNet, 99% sparsity, linear layers only | Effective nodes, log paths, test acc | DPaI 35.61% vs SynFlow 29.55% vs Random 17.40% | C2 (transformer applicability) | Only linear layers pruned; self-attention not adapted |
| E7 | ERK vs Uniform layer-wise sparsity (Table 7, Appendix D) | ResNet18/Tiny-ImageNet at 99-99.9% sparsity | Layer-wise effective nodes, log paths, test acc | ERK prevents layer collapse; more balanced node distribution | Method design choice | Only tested on one arch/dataset |

### Research-Theme Gap Diagnosis

**Gap 1: Causal attribution of differentiable NPB advantage.** The paper claims that differentiable optimization produces better masks than discrete NPB, but does not run an apples-to-apples comparison where the same NPB objective is optimized via discrete vs continuous methods with matched compute budget.

**Gap 2: Generality of NPB principle.** The extreme sparsity results (Table 8) show that more effective paths do not always correlate with higher accuracy — NPB achieves 64.06 log paths vs DPaI's 49.96 at 99.90% sparsity, yet DPaI achieves higher accuracy (15.69% vs 11.73%). This counterexample is not discussed.

**Gap 3: Reproducibility — code and data dependency.** Code is provided (GitHub), but key hyperparameters (α,β) differ per experiment and are found via expensive grid search. A default configuration or automated selection method would improve reusability.

### Proposed Research Experiments (P0/P1/P2)

| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Cost | Expected Gain |
|-------------|-----------|---------------|-------------------|---------|------------------|------|--------------|
| **P0: Differentiable NPB > Discrete NPB** | DPaI's global optimization yields better masks than NPB's per-layer discrete solver | Use the same NPB objective, optimize via discrete (NPB) vs continuous (DPaI) with matched step budget on ResNet18/Tiny-ImageNet at 90%, 96.84%, 99% sparsity | Both methods use ERK; same sparsity targets; same initial score distribution | Effective nodes, paths, kernels; test accuracy; wall-clock time | DPaI achieves ≥1% accuracy improvement over NPB at all sparsity levels | Moderate (3 runs × 4 settings = 12 GPU-hours) | Directly validates core contribution |
| **P1: Statistical reliability** | DPaI gains are statistically significant | Run 5 seeds for Figure 1 experiments (ResNet20, VGG19, ResNet18 at all 4 sparsity levels) | Report mean±std; paired bootstrap test vs second-best baseline | p-value from paired bootstrap test | p < 0.05 for majority of settings | Moderate (5× existing runs) | Converts qualitative "significant" to statistical evidence |
| **P2: NPB principle boundary** | The nodes-paths-accuracy relationship has a tradeoff regime | Analyze the 99.90% sparsity case in Table 8: why does NPB have more paths but lower accuracy? Vary α,β systematically to trace the Pareto front | Sweep α in {0.01, 0.1, 0.5, 0.9, 0.99} at 99.90% sparsity; measure all three metrics | Accuracy vs (nodes, paths, kernels) scatter plot | Identify the regime where more paths reduce accuracy; provide guidance for α selection at extreme sparsity | Low (5 runs on existing setup) | Strengthens theoretical foundation of NPB principle |
| **P2: Automated hyperparameter selection** | Architecture statistics predict optimal α,β | Train a small predictor: use layer count, parameter count, ERK density profile to predict (α,β) values from Table 2 | Compare grid-search baseline vs predicted values | Accuracy gap between grid-search best and predicted | Gap < 0.5% across all settings | Low-Medium | Eliminates major practical barrier |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 6.5 / 10

**Rationale:** The paper presents a conceptually solid extension of NPB to differentiable optimization, with broad empirical evaluation. However, the score is constrained by:

- **Research value (7/10):** The differentiable NPB formulation is a genuine advance over discrete NPB, enabling global mask optimization. However, the value is incremental — it improves optimization of an existing principle rather than introducing a new principle. The ImageNet-scale verification is limited to one baseline.
- **Novelty (6/10):** The combination of Top-K + STE for PaI is a natural extension of existing techniques (used in post-training pruning). The "first" claim requires external verification (deferred in this run). The primary novelty is the application of differentiable optimization to the NPB objective, which is a well-defined but moderate contribution.
- **Validity/soundness (6/10):** Strong empirical results at multiple sparsity levels, but undermined by missing variance, insufficient ImageNet baselines, potential inconsistency in Eq. (7), and a theory-practice gap in convergence analysis.
- **Reproducibility (7/10):** Code provided, hyperparameters documented, training details clear. However, the α,β grid search cost is not reported, and the convergence criterion is vaguely defined.

### Post-Revision Target: [7.5, 8.0] / 10

If the following are addressed:
1. Multi-seed variance reporting for all experiments
2. NPB added to ImageNet-1K comparison
3. Eq. (7) gradient inconsistency fixed
4. Conclusion rewritten with limitations
5. Convergence gap acknowledged

The paper could reach 7.5-8.0, indicating a solid ICLR-level contribution with proper evidence. The core idea is promising and the experiments show clear improvements; the main work is in tightening the evidence and correcting notation issues.