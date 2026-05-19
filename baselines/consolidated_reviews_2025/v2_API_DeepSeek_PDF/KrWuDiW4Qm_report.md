## Summary
# Final Review Report

## Summary

This paper (MetaPhysiCa, published at ICLR 2024) tackles the challenge of out-of-distribution (OOD) robustness in physics-informed machine learning (PIML) for parametric ODE forecasting. The key idea is to combine causal structure discovery with meta-learning: the model learns a binary causal graph Φ (shared across tasks) indicating which basis functions causally influence each state derivative, while task-specific coefficients W(i) are adapted at test time from short initial observations. Experiments on three synthetic ODE benchmarks (damped pendulum, predator-prey, SIR epidemic) show that MetaPhysiCa achieves 2×–28× lower OOD normalized RMSE than existing PIML and deep learning baselines.

**Core contributions (C1–C3):**
- C1: Demonstrates that existing PIML methods fail under OOD initial conditions and/or ODE parameters, extending prior findings that were limited to deep-learning-only methods.
- C2: Proposes a meta-learning framework that separates causal structure (shared Φ) from task-specific parameters (W(i)), enabling knowledge transfer across diverse training trajectories.
- C3: Introduces a causal structure discovery method via ℓ1-regularized continuous optimization with a V-REx penalty that identifies the true ODE structure under certain identifiability conditions.

**Strengths:** Clean problem formulation, strong empirical results on standard synthetic benchmarks, thorough ablation analysis, and a theoretical identifiability guarantee (Theorem 1) under idealized assumptions.

**Weaknesses:** Experiments limited to synthetic data with known basis functions; the 2×–28× claim lacks statistical significance context; Theorem 1 assumes infinite data and known basis parameters (not matching experimental conditions); the derivative-based loss switch is not rigorously justified; the conclusion is too brief and lacks bounded limitations.

## Strengths
1. **Clean problem formulation and task decomposition.** The paper clearly identifies two distinct OOD failure modes (OOD initial conditions and OOD ODE parameters) and explains why different PIML families fail for different reasons. The transductive vs. inductive taxonomy (Section 3.2) is a useful conceptual contribution that helps readers understand the landscape.

2. **Strong empirical performance on synthetic benchmarks.** The core experimental results (Tables 1–3) show that MetaPhysiCa achieves substantially lower OOD NRMSE than all baselines (2×–28×) across three widely-used ODE benchmarks. The qualitative trajectory plots (Figures 3, 6, 7) convincingly demonstrate that baselines fail dramatically while MetaPhysiCa follows the true OOD dynamics.

3. **Thorough ablation analysis.** The paper evaluates each design component independently (Table 6: sparsity, test-time adaptation, V-REx), showing that ℓ1-regularization and test-time adaptation are critical, and that the V-REx penalty prevents learning incorrect structures (Table 7). This level of dissection strengthens the claim that each component is necessary.

4. **Theoretical identifiability guarantee.** Theorem 1 provides a formal proof that under certain conditions (infinite data, known basis parameters, no V-REx), the optimization recovers the true causal structure. This elevates the paper beyond pure empirical validation, even though the assumptions are strong.

5. **Good reproducibility practices.** Code is provided, hyperparameter search ranges are specified, and dataset generation is described in detail (Appendices B and C). The complexity analysis (O(mdMT)) is included.

## Weaknesses
1. **Limited to synthetic benchmarks with known basis functions (P1, fixable).** The evaluation is restricted to three synthetic ODE systems where the basis function library is pre-specified and sufficiently expressive. Real-world physical systems often have unknown governing equations, unknown relevant basis functions, and measurement noise beyond the 1%–10% tested. The paper's own experiment without sine/cosine basis (Appendix D.6) shows that OOD NRMSE degrades 2×–4× when the library is misspecified, and the method still outperforms baselines but is no longer qualitatively tracking the true dynamics. This limits real-world applicability.

2. **Strong statistical claims without proper uncertainty quantification (P1, fixable).** The headline "2× to 28× lower OOD errors" uses an extremely wide range without per-task breakdown and without significance tests. Standard deviations in Table 1 for MetaPhysiCa are up to 80% of the mean (e.g., OOD Xt0 and W*: 0.100 ± 0.080), suggesting high variability across test tasks. No confidence intervals or paired significance tests are reported. The claim "best baseline" is ambiguous across tasks and settings.

3. **Theory–experiment gap (P1, partially fixable).** Theorem 1 guarantees causal structure recovery under Assumption 1 (infinite observations per task, known basis parameters ξ, no V-REx penalty λ_REx=0). However, the experiments use finite trajectories (T=100), learn ξ jointly, and rely on V-REx as a "necessary" component (Page 7, line 15). The theorem does not cover the actual operating regime, weakening its practical relevance.

4. **Derivative-based loss is insufficiently justified (P2, fixable).** The switch from state-prediction loss R(i) to derivative-based loss eR(i) is a critical design choice (Page 6, lines 67–75) that is only supported by an informal empirical claim ("leads to a stable learning procedure"). The derivative estimation method is not specified in the main text, and the potential discrepancy between training (derivative MSE) and evaluation (state RMSE) is not discussed. A controlled comparison is missing.

5. **Conclusion is too brief and lacks synthesis (P2, fixable).** The conclusion (Section 6) essentially restates the abstract in 6 lines and does not synthesize findings, bound limitations concretely, or provide a clear roadmap for future work. The limitations are generic ("better optimization techniques") and do not specify conditions under which MetaPhysiCa would be expected to fail.

6. **Noise asymmetry across tasks (P3, minor).** The damped pendulum uses 1% noise while predator-prey and epidemic use 0% noise. While the stated purpose is to show OOD failure is not noise-related, this introduces a confound. A matched-noise experiment across all three tasks would be more systematic.

## Key Issues
### Issue 1 (Major): Statistical claims lack proper uncertainty quantification
**Evidence:** Page 9, Results paragraph: "MetaPhysiCa performs the best OOD across all datasets achieving 2× to 28× lower OOD NRMSE than the best baseline." Table 1 shows MetaPhysiCa OOD Xt0 and W* = 0.100 (0.080) for epidemic — std is 80% of mean. No significance test reported.
**Impact:** Without confidence intervals or significance tests, readers cannot assess whether the reported gains are statistically reliable. The wide 2×–28× range without per-task breakdown may overstate the average improvement.
**Fix:** Add paired significance tests (e.g., paired t-test or Wilcoxon) against the best baseline per setting. Report per-task improvement ratios with confidence intervals. Add a compact table showing: (Task, OOD scenario, MetaPhysiCa NRMSE, Best baseline NRMSE, Improvement factor, p-value).

### Issue 2 (Major): Theorem 1 does not match experimental conditions
**Evidence:** Page 7, Theorem 1 + Assumption 1 (Appendix A). Assumption requires T(i)→∞, known ξ, λ_REx=0. Page 7, line 15 states V-REx is "necessary to learn the true causal structure."
**Impact:** The theoretical guarantee covers a different regime (infinite data, no V-REx) than what is actually needed (finite data, V-REx on). This gap is not acknowledged, and the necessity of V-REx in experiments directly contradicts λ_REx=0 in the theorem.
**Fix:** Either extend the proof to cover the V-REx setting, or add an explicit statement that Theorem 1 applies to a simplified setting and discuss why V-REx is expected to improve finite-sample recovery. Add a finite-sample remark bounding ||ˆW(i)(Φ*) - W(i)*|| in terms of T.

### Issue 3 (Major): Derivative-based loss switching is a critical design choice without rigorous justification
**Evidence:** Page 6, lines 67–75: "In practice however, we found the squared loss directly between the predicted and estimated ground truth derivatives... leads to a stable learning procedure with better accuracy in-distribution and OOD."
**Impact:** This design choice changes what the model optimizes (derivative error vs. state error), yet the claim of superiority is only supported by informal empirical observation. Derivative estimation introduces noise, and the training-evaluation mismatch (derivative loss train vs. state RMSE test) is unexamined.
**Fix:** Add a controlled comparison of R(i) vs. eR(i) with identical hyperparameters on at least one task. Report ID and OOD NRMSE for both. Explain the mechanism (e.g., derivative loss provides per-step gradient without ODE solver backprop). Specify derivative estimation method in the main text.

### Issue 4 (Minor): Asymmetric noise across tasks is a potential confound
**Evidence:** Page 9, line 57: "We generate the damped pendulum dataset with 1% zero-mean Gaussian noise and the rest with no noise."
**Impact:** The claim that "OOD failure of baselines is unrelated to noise" is supported by the clean-data tasks (predator-prey, epidemic), but the noise asymmetry prevents systematic comparison of noise robustness across all three tasks.
**Fix:** Either add 1% noise to all three tasks for consistency, or clearly separate the claim into two parts: (a) OOD failure persists under clean data (predator-prey, epidemic), and (b) MetaPhysiCa handles mild noise (pendulum 1%). Add a matched-noise comparison.

### Issue 5 (Minor): Conclusion is too brief and lacks bounded limitations
**Evidence:** Page 9, Section 6: approximately 6 lines, restating the abstract.
**Impact:** Missed opportunity to synthesize findings, bound failure conditions, and provide a clear research roadmap. The "We believe" sentence adds no scientific content.
**Fix:** Restructure into three parts: (i) validated findings with scope, (ii) concrete limitations (basis function dependence, noise sensitivity, stiff ODEs with compositional SCMs), (iii) prioritized future directions.

## Actionable Suggestions
### S1 (Must) — Add statistical significance tests
**Target:** Page 9, Results paragraph; Tables 1–3.
**Action:** For each (task, OOD scenario) pair, report:
- Mean NRMSE ± std over M'=200 test tasks (already done).
- Paired t-test or Wilcoxon signed-rank test p-value against the best baseline.
- A compact improvement-factor table, e.g.: "(Pendulum, OOD Xt0): 8.4× vs DyAd (p<0.001); (Epidemic, OOD Xt0 and W*): 28× vs APHYNITY (p<0.01)."
**Expected benefit:** Validates that reported gains are not due to random variation. Increases reviewer confidence.

### S2 (Must) — Acknowledge and discuss theory–experiment gap
**Target:** Page 7, Theorem 1 paragraph.
**Action:** Add 2–3 sentences after Theorem 1:
"While Theorem 1 assumes infinite observations per task (T(i)→∞), known basis parameters ξ, and no V-REx penalty (λ_REx=0), the experimental setting involves finite trajectories, learned ξ, and active V-REx regularization. The finite-sample behavior of the estimator can be bounded using standard linear regression analysis: ||ˆW(i)(Φ*) - W(i)*|| ≤ O(1/√T) under appropriate conditions. We conjecture that the V-REx penalty improves structure recovery in the finite-sample regime by preventing rare but informative basis functions from being pruned, which we verify empirically in Table 7."
**Expected benefit:** Bridges theory and practice; prevents readers from over- or under-interpreting Theorem 1.

### S3 (Must) — Add controlled comparison of R(i) vs eR(i)
**Target:** Page 6, lines 67–75.
**Action:** Add a small table or paragraph in Appendix comparing R(i) and eR(i) on the damped pendulum task with identical hyperparameters (λΦ, λ_REx, learning rate, batch size). Report ID NRMSE, OOD Xt0 NRMSE, and convergence speed (epochs to reach validation loss within 5% of minimum).
**Expected benefit:** Validates the derivative-based loss choice. If eR(i) is indeed better, explains why (e.g., "eR(i) provides a per-timestep gradient that avoids ODE solver backprop, reducing gradient variance").

### S4 (Should) — Rewrite conclusion with bounded limitations
**Target:** Page 9, Section 6.
**Action:** Replace the current 6-line conclusion with a structured three-paragraph version:
1. **Validated findings** (1 sentence per task: what MetaPhysiCa achieves and under what conditions).
2. **Bounded limitations** (3 bullet points): (a) requires pre-specified basis functions, (b) degrades under >10% noise and misspecified libraries, (c) compositional extensions can produce stiff ODEs.
3. **Future work** (2–3 concrete directions): adaptive basis selection, finite-sample theory, PDE extension.
**Expected benefit:** A conclusion that tells readers exactly what is known, what is not known, and what to do next.

### S5 (Should) — Unify noise levels across all three tasks
**Target:** Page 9, dataset generation; Appendix D.3.
**Action:** Add a systematic noise experiment where all three tasks are evaluated at 0%, 1%, 5%, 10% noise with matched settings. Move the pendulum-only noise results to this unified table.
**Expected benefit:** Removes potential confound, strengthens the claim that OOD failure is noise-independent, and provides a comprehensive robustness profile.

### S6 (Nice-to-have) — Improve introduction narrative alignment
**Target:** Page 1, Introduction paragraphs.
**Action:** Restructure the introduction to follow: Big Picture → Gap (two distinct failure modes) → Solution (causal structure + meta-learning) → Evidence preview → Contribution list. The current version blends gap identification with method description, making it harder to track the argument. See Storyline Options section for a complete rewrite blueprint.

## Storyline Options + Writing Outlines
### Abstract Outline (4-sentence structure recommended for revision)

**Current abstract** has 3 sentences: problem → method → result. It is functional but could be tighter.

**Recommended revision (S1–S5):**

- **S1 (Problem):** "A fundamental challenge in physics-informed machine learning (PIML) is out-of-distribution (OOD) robustness when forecasting parametric ODE systems with unknown parameters and varying initial conditions."
- **S2 (Gap):** "Existing PIML methods either assume fixed ODE parameters across all tasks (transductive) or use neural network components that learn spurious correlations and fail under OOD shifts."
- **S3 (Solution):** "We propose MetaPhysiCa, which combines causal structure discovery with meta-learning to recover the true ODE dynamics by separating a globally shared causal graph from task-specific coefficients."
- **S4 (Result):** "On three synthetic ODE benchmarks (damped pendulum, predator-prey, SIR epidemic), MetaPhysiCa achieves 2×–28× lower normalized RMSE than existing PIML and deep learning methods under OOD initial conditions and ODE parameters."
- **S5 (Bound):** "The method assumes a pre-specified library of basis functions; performance degrades under misspecified libraries or high observation noise (>10%)."

### Introduction Outline (6-paragraph plan for revision)

**Current introduction issues:** The first paragraph blends background, gap, and motivation too densely. Contribution list is clear but generic for claim 2.

**Recommended structure:**

- **P1 (Establish territory):** "PIML has achieved strong in-distribution performance across biological, climate, and turbulence modeling. However, this success does not automatically extend to out-of-distribution (OOD) scenarios—a critical requirement for reliable forecasting in scientific applications." *(Sets stakes: OOD matters.)*

- **P2 (Identify gap):** "Two distinct OOD failure modes exist in parametric ODE forecasting: shifts in initial conditions and shifts in ODE parameters. Transductive PIML methods (e.g., SINDy) handle OOD initial conditions but cannot transfer across different parameters. Inductive methods (e.g., APHYNITY) adapt across parameters but use neural networks that fail under OOD initial states." *(Clear separation of the two gaps.)*

- **P3 (Root cause analysis):** "The common root cause is that existing PIML methods learn dataset-specific correlations rather than the causal structure of the underlying ODE. Standard neural network components extrapolate poorly (algorithmic alignment failure), and no current approach jointly addresses both OOD shifts." *(Explains why both failure modes persist.)*

- **P4 (Proposed solution intuition):** "We argue that OOD robustness requires two capabilities: (a) discovering the causal graph that determines which physical quantities influence each state derivative, and (b) adapting model parameters to each test task using only short initial observations. We propose MetaPhysiCa, which combines ℓ1-regularized causal structure discovery with meta-learning to achieve both." *(Bridges gap to method.)*

- **P5 (Contributions):** List C1–C3 as in the current paper, but with more specific wording for C2: "A meta-learning framework that decouples causal structure (shared binary matrix Φ) from task-specific coefficients W(i), enabling transfer across diverse trajectories while adapting at test time." *(Sharper than the current version.)*

- **P6 (Roadmap):** "We validate MetaPhysiCa on three synthetic ODE benchmarks with OOD initial conditions and parameters, showing 2×–28× improvement over baselines. Ablations confirm the necessity of each component, and a theoretical analysis (Theorem 1) provides identifiability guarantees under idealized conditions."

### Storyline Comparison

| Criterion | Current | Recommended | Improvement |
|---|---|---|---|
| Problem alignment | Good | Better (separates two gaps) | Stronger motivation |
| Variable alignment | Adequate | Φ and W(i) introduced earlier | Cleaner traceability |
| Contribution-evidence | Adequate | Explicit bound linking to experiments | Higher credibility |

## Priority Revision Plan
| Priority | Issue | Effort | Impact | Action |
|---|---|---|---|---|
| **P0** | Statistical claims without significance | Low (computational: recompute from existing test outputs) | High (validates core claim) | Add paired t-test p-values and per-task improvement table |
| **P0** | Theory–experiment gap in Theorem 1 | Low (text addition) | High (closes contradiction between theorem assumptions and empirical necessity of V-REx) | Add 2–3 sentences after Theorem 1 acknowledging the gap and conjecturing finite-sample benefit of V-REx |
| **P0** | Derivative-based loss justification | Low (one additional experiment + text) | High (validates critical design choice) | Add controlled R(i) vs eR(i) comparison in appendix with same hyperparameters |
| **P1** | Conclusion too brief | Low (text rewrite) | Medium (improves paper closure and reader understanding of limitations) | Rewrite as three-part structure (findings, limitations, future work) |
| **P1** | Noise asymmetry across tasks | Medium (3× additional experiment) | Medium (removes confound) | Run all three tasks at matched noise levels and create unified robustness table |
| **P2** | Introduction narrative alignment | Medium (text reorganization) | Medium (improves readability) | Restructure to follow P1–P6 outline in Storyline Options section |
| **P2** | Basis function assumption scope | Low (text addition) | Medium (clarifies applicability) | Add a paragraph in Section 4.1 discussing basis function selection and extension |
| **P3** | Stiff ODE issue with compositional SCMs | High (requires optimization research) | Low (niche extension) | Acknowledge as open challenge; no immediate experiment needed |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Problem: Statistical claim without significance tests]
    -> [P0: Add paired t-test + per-task improvement table]
    -> [Expected gain: Validated core claim, higher reviewer confidence]

[Problem: Theorem 1 contradicts V-REx necessity]
    -> [P0: Acknowledge gap + conjecture finite-sample benefit]
    -> [Expected gain: Theory matches experimental narrative]

[Problem: Derivative-based loss is unjustified]
    -> [P0: Add controlled R(i) vs eR(i) comparison]
    -> [Expected gain: Validates critical design choice]

[Problem: Conclusion lacks synthesis]
    -> [P1: Rewrite as findings + limitations + future work]
    -> [Expected gain: Clearer closure and bounded claims]

[Problem: Noise asymmetry across tasks]
    -> [P1: Unified noise robustness experiment]
    -> [Expected gain: Removes confound, strengthens generalizability]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | OOD robustness on damped pendulum | 1000 train tasks, 200 test; OOD Xt0 and OOD Xt0+W*; 1% noise | NRMSE (ID, OOD Xt0, OOD Xt0+W*) | 8.4×–28× improvement vs best baseline | C1, C2 | Synthetic only; no CIs or significance tests |
| E2 | OOD robustness on predator-prey | Same as E1; 0% noise | NRMSE | 2×–8× improvement | C1, C2 | 0% noise; no significance tests |
| E3 | OOD robustness on SIR epidemic | Same as E1; r=T/10 (shorter observation); 0% noise | NRMSE | 9×–28× improvement | C1, C2 | Short observation window may favor efficient adaptation |
| E4 | Causal structure recovery (Table 5) | Compare learnt Φ vs ground truth ODE | Φ matrix | Exact match for pendulum/prey; reparameterized for SIR | C3 | SIR shows reparameterization (not exact match) |
| E5 | Ablation: sparsity (Table 6) | Remove ℓ1 regularization | OOD Xt0 NRMSE | NaN* on 2/3 tasks | C3 | Shows necessity but no effect size |
| E6 | Ablation: test-time adaptation (Table 6) | Replace test-time adaptation with mean W(i) | OOD Xt0 NRMSE | 3×–17× degradation | C2 | Strong evidence of necessity |
| E7 | Ablation: V-REx (Table 7) | Remove V-REx; skewed training (1% damping tasks) | Learnt Φ + OOD NRMSE | Without V-REx: learns wrong structure; 24× worse OOD | C3 | Only tested on pendulum; skewed setting is synthetic |
| E8 | Noise robustness (Fig 8) | 0%, 1%, 5%, 10% Gaussian noise | OOD NRMSE | Comparable to baselines at 10%; robust ≤5% | None specific | Only two tasks; no unified threshold |
| E9 | Complex ODE (Table 8) | 2-layer compositional SCM on Chen (2020) ODE | NRMSE | 1.5×–1.7× improvement; stiff ODE in 2/5 folds | None specific | Stiff ODE failures limit reliability |
| E10 | Basis function count (Fig 9) | 7–32 basis functions | ||Φ||₁, training loss | Converges to true 3-term dynamics for all m | C3 | Slower convergence for larger m |

### Research-Theme Gap Diagnosis

Three research-value claims are weakly supported:

1. **Generalizability beyond synthetic ODEs:** No real-world physical system is evaluated. The method's reliance on a pre-specified basis function library is untested on systems where the governing equations are unknown.
2. **Statistical reliability of reported gains:** No confidence intervals or significance tests are provided for any of the 2×–28× improvement claims, making it impossible to assess whether the gains are systematic.
3. **Scalability and computational cost:** Only per-epoch complexity is reported (O(mdMT)). No wall-clock time, memory usage, or convergence comparison against baselines. The joint optimization is noted as 8.2× faster than bilevel (Appendix D.2.3), but absolute numbers are in CPU milliseconds and don't reflect GPU training.

### Proposed Research Experiments (P0/P1/P2)

| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| **P0: Statistical reliability** | Reported gains are statistically significant | Compute paired t-test and Wilcoxon p-values from existing 200 test-task outputs per setting | Best baseline per setting | p-value, effect size, 95% CI | p<0.01 for all settings | <1 hour (computational) | Validates core empirical claim |
| **P0: R(i) vs eR(i) comparison** | eR(i) improves training stability and OOD accuracy | Run MetaPhysiCa with R(i) (state MSE) on damped pendulum with same hyperparameters | eR(i) result from Table 2 | NRMSE (ID, OOD), convergence epochs | eR(i) achieves ≥1.5× better OOD NRMSE or 2× faster convergence | <2 hours (1 GPU) | Justifies critical design choice |
| **P1: Unified noise robustness** | OOD improvement persists at matched noise levels | Run all 3 tasks at 0%, 1%, 5%, 10% noise with TVR derivative estimation | NeuralODE, APHYNITY at same noise levels | NRMSE across all (task, noise, OOD scenario) combos | MetaPhysiCa outperforms baselines at ≤5% noise on all tasks | <4 hours (3 GPUs) | Removes confound; comprehensive robustness profile |
| **P2: Real-world ODE benchmark** | MetaPhysiCa improves OOD forecasting on real physical measurements | Select one real-world ODE dataset (e.g., lake temperature modeling, cardiac dynamics) with OOD time periods | NeuralODE, APHYNITY | NRMSE, forecast skill score | MetaPhysiCa outperforms baselines on at least 2 of 3 OOD periods | <1 week (data collection + experiments) | Demonstrates real-world applicability |

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 (This week):
  ┌─ Statistical tests on existing outputs
  ├─ R(i) vs eR(i) controlled comparison
  └─ Theory gap text revision

P1 (Before submission):
  ┌─ Unified noise robustness (all 3 tasks × 4 noise levels)
  ├─ Conclusion rewrite
  └─ Introduction narrative restructure

P2 (Next version):
  ┌─ Real-world ODE benchmark evaluation
  ├─ Adaptive basis function selection
  └─ Finite-sample theoretical bounds
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

**Rationale:** The paper addresses a well-motivated problem (OOD robustness in PIML) with a clean technical approach (causal structure discovery + meta-learning) and demonstrates strong empirical gains on synthetic benchmarks. However, the score is constrained by three factors:
1. **Statistical reliability**: The central empirical claim (2×–28× improvement) lacks significance tests and confidence intervals, making the reported gains unverifiable as systematic rather than random.
2. **Theory–experiment gap**: Theorem 1 assumes infinite data and no V-REx, while experiments rely on finite data and V-REx as "necessary"—this inconsistency reduces theoretical contribution impact.
3. **Limited scope**: Evaluation on three synthetic ODE systems with known basis functions limits evidence for real-world applicability.

The paper's strengths (clean problem decomposition, thorough ablations, theoretical identifiability) support a score above 5, but the above weaknesses prevent a score above 7.

**Post-Revision Target: [7.5, 8.5]/10**

If the authors address the P0 items (statistical significance tests, theory gap clarification, derivative loss justification) and P1 items (unified noise experiments, conclusion rewrite), the paper could reach 7.5–8.5/10. The upper bound is limited by the synthetic-only evaluation, which cannot be fully resolved without real-world validation. Achieving the target requires:
- Adding paired significance tests (p<0.01 for all settings) → +0.5
- Closing theory gap with explicit acknowledgment and finite-sample remark → +0.5
- Adding controlled R(i) vs eR(i) comparison → +0.3
- Unified noise robustness experiment → +0.3
- Rewriting conclusion with bounded limitations → +0.2
- Total potential improvement: ~+1.5–2.0 points