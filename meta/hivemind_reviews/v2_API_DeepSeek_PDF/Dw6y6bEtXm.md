## Summary
# Final Review Report

## Summary

This paper introduces PICL (Physics-Informed Coarse-grained data Learning), a framework that integrates physics-informed losses into neural network training when only coarse-grained observations of PDE-governed dynamical systems are available. The core idea is to jointly train an encoding module (U-Net) that maps coarse observations to a learnable fine-grained latent state, and a transition module (FNO) that predicts the next fine-grained state. A two-stage fine-tuning strategy—first physics-tuning the transition module on unlabeled data, then data-tuning the encoding module—propagates PDE constraints through the model.

**Strengths:** The paper addresses a practically important problem (learning from coarse sensor measurements), proposes a coherent framework combining super-resolution and forecasting, and provides extensive ablation studies on three PDE benchmarks (wave equation, LSWE, NSWE) with additional results on Burgers and Navier-Stokes. The GitHub code availability supports reproducibility.

**Core Weaknesses:** (1) Missing statistical reliability—Table 1 reports only point estimates without variance or significance tests. (2) Loss function definition contains symbol inconsistency between F (defined on ground-truth ũ) and its use on learned û. (3) Baseline comparisons may favor PICL due to architectural asymmetry and encoder-tuning differences. (4) The two stated contributions are too generic; the genuine novelty (two-stage fine-tuning for propagating PDE constraints) is under-emphasized. (5) Multi-step prediction benefit is claimed but not mechanistically analyzed. (6) Novelty cannot be verified externally in this run due to retrieval constraints.

**Overall Assessment:** The paper has solid technical merit and the proposed approach is sensible. However, the current evidence is not yet sufficient to support the strength of several claims. With major revisions to statistical reporting, loss function clarity, baseline fairness, and claim bounding, the paper could become a valuable contribution to physics-informed machine learning.

## Strengths
1. **Practically relevant problem formulation:** The paper addresses a genuine and important challenge—learning physical system dynamics from coarse-grained observations without access to fine-grained ground truth. This setting is common in real-world applications (e.g., sparse ocean sensors, environmental monitoring) and existing PINN/neural-operator methods typically require finer-resolution data.

2. **Well-structured framework design:** PICL's decomposition into an encoding module (coarse-to-fine reconstruction) and a transition module (temporal forecasting) is conceptually clean. The two-stage fine-tuning strategy—physics-tuning the transition module on unlabeled data, then data-tuning the encoding module—is a clever mechanism for propagating PDE constraints through the model without requiring fine-grained labels.

3. **Comprehensive ablation studies:** The authors systematically investigate sensitivity to the physics loss weight (γ), length of consecutive input observations (n), fine-tuning steps (m1, m2), and gap period (q). The ablation on data quantity (labeled/unlabeled) and data quality (coarse-grid resolution) provides useful practical guidance for deploying PICL under varying data conditions.

4. **Multi-PDE validation:** Evaluation across five PDE families (wave equation, LSWE, NSWE, Burgers, Navier-Stokes) demonstrates the framework's applicability beyond a single equation type. The NSWE experiments with uneven bottom topography are particularly relevant for real-world shallow-water modeling.

5. **Reproducibility effort:** The authors provide the source code on GitHub and include detailed architecture specifications (Appendix A), hyperparameter tables (Table 2-3), and pseudocode (Algorithm 1-2), which is commendable for reproducibility.

6. **Zero-shot super-resolution demonstration:** The experiment in Appendix B showing PICL's ability to generalize to unseen coarse-grid resolutions (trained on 7×7, tested on 3×3, 5×5, 11×11) via a Transformer-based encoder is a noteworthy extension that suggests the framework could be adapted to flexible sensor configurations.

## Weaknesses
1. **Missing statistical significance (Major):** All experimental results in Table 1 are reported as single point estimates without standard deviations, confidence intervals, or significance tests. Given the small relative improvements (e.g., 4% on LSWE between PICL w/o fine-tune and PICL with fine-tune), it is impossible to assess whether these gains are statistically reliable or fall within run-to-run noise.

2. **Loss function symbol inconsistency (Major):** The RK4 residual function F is defined on the true fine-grained state ũ, but used to compute physics losses L_ep and L_tp on the learned fine-grained state û without explicitly stating the assumption that F can be meaningfully evaluated on û. This is a non-trivial assumption since û is a learned representation that may not satisfy the same discretization properties as ũ.

3. **Baseline fairness concerns (Major):** FNO* and PINO* use the same encoder architecture as PICL, but PICL's encoder additionally receives physics loss supervision (L_ep) which is not available to the baselines (γ=0 for FNO*). This means the comparison conflates two factors: (a) the benefit of the overall framework and (b) the benefit of the encoder receiving extra supervision. A controlled ablation keeping encoder supervision identical would be needed to isolate the framework's core contribution.

4. **Weak contribution framing (Moderate):** The two stated contributions are generic: proposing a framework and showing it improves predictive ability. The genuinely novel mechanism—the two-stage fine-tuning that propagates PDE information from the transition module to the encoding module—is described in the method but not elevated to a contribution. This framing weakens the paper's impact.

5. **Unsubstantiated multi-step claim (Moderate):** The claim that "the growth of cumulative error may slow down due to the model being constrained to meet the PDEs at each step" is offered as an explanation for PICL's multi-step performance but is not supported by any error decomposition analysis (e.g., per-step error vs. cumulative error, or comparison of error accumulation rates with/without physics constraints).

6. **Incomplete related-work comparison (Moderate):** The related work section is organized as a chronological list rather than comparative axes. The paper claims existing methods "cannot be applied to learn coarse-grained measured data directly" but does not provide concrete evidence from the cited works showing where or why they fail on coarse data.

7. **Novelty verification deferred (Moderate):** Due to retrieval constraints in this run, external literature verification was not possible. Claims involving "first" (in the SR paragraph) and "novel framework" should be treated as unverified and require manual literature checks.

8. **Conclusion too generic (Minor):** The conclusion section is only 4 sentences and reads as a compressed abstract. It does not enumerate validated findings, state limitations, or propose concrete next steps, which limits its usefulness as a standalone section.

## Key Issues
### Issue 1 — Missing variance and statistical testing in all experimental results
**Severity: Major | Validity Risk: High | Fixability: Easy**

**Evidence:** Table 1 (Page 7) reports L_d and ε as single values for each method/benchmark combination. The text reports "over 46% improvement" and "about 10% improvement" without confidence intervals. Fig. 2 and Fig. 3 also lack error bars.

**Mechanism:** Without multi-seed variance, the reader cannot distinguish genuine algorithmic improvement from run-to-run noise. This is especially problematic where improvements are small (e.g., LSWE: 2.54E-2 vs 2.44E-2 = 4% relative improvement).

**Impact:** The core claim of "superior predictive ability" lacks statistical grounding. A reviewer cannot recommend acceptance without knowing whether results are reproducible.

**Fix:** Re-run all experiments with ≥3 random seeds (different IC samples, weight initializations). Report mean ± std for all metrics in Table 1, Fig. 2, and Fig. 3. Add paired significance tests (e.g., Wilcoxon signed-rank) comparing PICL against FNO* on held-out test trajectories.

---

### Issue 2 — Loss function definition: F is defined on ũ but used on û without justification
**Severity: Major | Validity Risk: High | Fixability: Easy**

**Evidence:** Page 5, lines 24-27: "By expressing the 4th-order Runge-Kutta (RK4) formulae as F(ũ_t, ũ_{t+1}) = 0, we design two physics losses L_ep(θ) = F(û_t(θ), û_{t+1}(θ))^2 and L_tp(ω) = F(û_t, û_{t+1}(ω))^2."

**Mechanism:** The symbol ũ denotes the ground-truth fine-grained discretized state. The learned state û is a neural network output that may not lie in the same function space or satisfy the same discretization properties as ũ. Using F on û without explicit justification assumes that the PDE residual is well-defined for any learned representation at the same resolution, which is not guaranteed.

**Impact:** If û contains high-frequency artifacts or violates the PDE's regularity conditions, the physics loss may be computing a meaningless quantity.

**Fix:** Add an explicit sentence: "We assume that the learned fine-grained state û and the true discrete state ũ share the same spatial resolution (n×n grid) and that the RK4 residual F can be meaningfully evaluated on û. In practice, the PDE residual on û serves as a soft constraint that guides the learned representation toward physically consistent states." Additionally, verify with a simple test: compute F on random noise at the same resolution—if it produces non-zero residuals, then F(û) ≠ 0 is a meaningful loss.

---

### Issue 3 — Baseline construction favors PICL by design
**Severity: Major | Validity Risk: Medium | Fixability: Moderate**

**Evidence:** Page 6, lines 38-44: "FNO*: the same encoding module as PICL is attached ahead of FNO ... γ = 0 in loss function 4."

**Mechanism:** FNO* uses the same encoder as PICL but with γ=0 (no physics loss for the encoder). Thus PICL's encoder benefits from additional supervision (L_ep) that FNO*'s encoder does not receive. Any improvement from PICL over FNO* could be partly attributed to this extra supervision rather than the framework's core innovation.

**Impact:** Overstates the contribution of the two-stage fine-tuning framework relative to a fair baseline.

**Fix:** Add an additional baseline: "PICL-encoder-ablated" where the encoder is trained identically to FNO* (γ=0) but the two-stage fine-tuning is still applied. If this baseline still outperforms FNO*, the fine-tuning mechanism is validated. If not, the encoder supervision is the main driver.

---

### Issue 4 — Contribution framing is too generic and misses the actual novelty
**Severity: Moderate | Research Value Impact: Medium | Fixability: Easy**

**Evidence:** Page 2, lines 27-31: The two contributions are (1) proposing PICL and (2) demonstrating improvement. The two-stage fine-tuning strategy is described in the method but not listed as a contribution.

**Mechanism:** The paper's most distinctive mechanism is the alternating physics-tuning and data-tuning that propagates PDE information from the transition module to the encoding module. By not elevating this to a contribution, the paper undersells its novelty.

**Fix:** Restructure contributions to highlight the two-stage fine-tuning mechanism and its ability to learn from unlabeled coarse-grained data.

## Actionable Suggestions
### S1 — Add multi-seed statistics to all experiments [Must]
- **Action:** Re-run all methods (PICL variants and all baselines) on 3+ random seeds differing in weight initialization and training/validation split. Report mean ± std for L_d and ε in Table 1, add error bars to Fig. 2 and Fig. 3.
- **Location:** Table 1 (Page 7), Fig. 2 (Page 8), Fig. 3 (Page 9).
- **Expected benefit:** Provides statistical grounding for the "superior predictive ability" claim. Without this, the results are not verifiable.

### S2 — Clarify the F(ũ) → F(û) substitution in loss function [Must]
- **Action:** Add one sentence: "We assume that the learned fine-grained state û and the true discrete state ũ share the same spatial resolution and that the RK4 residual F can be meaningfully evaluated on û as a soft constraint." Also add a small epsilon to L_d denominator: L_d = ||ô_{t+1} - õ_{t+1}||₂ / (||õ_{t+1}||₂ + ε) to handle near-zero states.
- **Location:** Page 5, Section 4.2.2, around Equation (4).
- **Expected benefit:** Eliminates symbol confusion and improves reproducibility.

### S3 — Add a controlled baseline isolating the encoder physics loss [Must]
- **Action:** Add "PICL-encoder-ablated" where the encoder is trained with γ=0 (data loss only, like FNO*) but the rest of PICL (including two-stage fine-tuning) is retained. Compare against FNO* to show the benefit of the fine-tuning mechanism independent of encoder supervision.
- **Location:** Page 6, Section 5.1, add as a fifth baseline.
- **Expected benefit:** Disentangles the effect of encoder supervision from the two-stage fine-tuning innovation.

### S4 — Reframe contributions to highlight two-stage fine-tuning [Should]
- **Action:** Replace the generic contribution (2) with: "(2) We propose a two-stage fine-tuning strategy—physics-tuning of the transition module on unlabeled data followed by data-tuning of the encoding module—that propagates PDE constraints through the model, enabling semi-supervised learning from coarse-grained observations."
- **Location:** Page 2, Introduction, last paragraph.
- **Expected benefit:** Better communicates the paper's mechanistic novelty.

### S5 — Provide error decomposition analysis for multi-step prediction [Should]
- **Action:** Plot per-step error (ΔL_d(s) = L_d(s) - L_d(s-1)) in addition to cumulative L_d. If per-step error is constant across methods, the multi-step advantage is simply a consequence of lower one-step error. If per-step error decreases for PICL, the PDE constraint genuinely reduces error accumulation.
- **Location:** Page 8, Section 5.3 or as an appendix figure.
- **Expected benefit:** Substitutes speculation with evidence for the multi-step claim.

### S6 — Restructure related work around comparison axes [Should]
- **Action:** Organize the related work into three comparison axes: (1) Data requirement (full/partial/none), (2) Grid resolution dependency, (3) Physics integration method. For each axis, position existing works and then state PICL's position.
- **Location:** Page 2-3, Section 2.
- **Expected benefit:** Makes the comparison more informative and clarifies PICL's novelty.

### S7 — Expand conclusion with limitations and next steps [Nice-to-have]
- **Action:** Add a limitations paragraph covering: (a) dependence on regular grid and fixed architectures, (b) simulation-only validation, (c) assumption that PDE is known. Add a future-work sentence on irregular meshes and real-world sensor data.
- **Location:** Page 9, Section 6.
- **Expected benefit:** Improves completeness and helps readers understand the scope of the contribution.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction (Page 1-2) has a functional but improvable narrative: (1) broad motivation → (2) coarse-data challenge with ocean example → (3) PICL framework description → (4) contributions. **Missing element:** the concrete gap in existing methods is stated only abstractly ("many methods rely on fine-grained data"), and the link between the challenge and PICL's solution is not explicitly mapped.

### Recommended Storyline: Problem-Method-Evidence Arc

**Abstract Outline (4-5 sentences):**
- **S1 (Problem):** "Modeling PDE-governed physical systems from coarse-grained sensor measurements is challenging because existing physics-informed methods require fine-grained resolution to compute meaningful equation residuals."
- **S2 (Gap):** "Standard approaches either require expensive fine-grained data or fail when physics losses are computed on coarse grids due to large discretization errors."
- **S3 (Method):** "We propose PICL, which learns a fine-grained latent state representation from coarse observations via an encoding module, applies PDE constraints through RK4-based physics losses on this learned representation, and uses a two-stage fine-tuning strategy to propagate physics information through the model using unlabeled data."
- **S4 (Evidence):** "Across five PDE benchmarks—including wave equation, linear and nonlinear shallow water equations, Burgers equation, and Navier-Stokes equations—PICL reduces prediction error by 17-48% over data-driven baselines."
- **S5 (Implication):** "This work demonstrates that physics-informed learning is feasible with only coarse-grained observations, broadening the applicability of neural PDE solvers to real-world settings with sparse sensors."

**Introduction Outline (5 paragraphs):**
- **P1 — Big Picture:** "Neural network surrogates for PDE-governed physical systems have emerged as efficient alternatives to numerical solvers, but their training typically requires either dense high-resolution data or fine-grained grids for computing physics-informed losses. In many real-world applications—such as ocean monitoring, weather stations, and environmental sensing—measurements are inherently coarse-grained due to sensor sparsity." (Establishes stakes.)
- **P2 — Concrete Gap:** "Existing methods fall into two categories. Data-driven neural operators (FNO, DeepONet) require abundant high-resolution training data. Physics-informed methods (PINNs, PINO) compute PDE residuals on finely discretized grids, which is infeasible when only coarse observations are available because discretization errors dominate. A key open question is: can physics information be integrated when the available data is too coarse for direct PDE loss computation?" (Establishes gap and research question.)
- **P3 — Proposed Idea:** "We address this question with PICL, which learns a fine-grained latent state from coarse inputs via an encoder, applies PDE constraints in the latent space, and uses a two-stage fine-tuning strategy that first tunes the transition module with physics loss on unlabeled data, then tunes the encoding module with data loss, propagating PDE information through the model." (Solution intuition.)
- **P4 — Key Results Preview:** "In experiments on wave equation, shallow water equations, and Navier-Stokes equations, PICL achieves 17-48% lower prediction error than data-driven baselines while requiring only coarse-grained observations. The two-stage fine-tuning provides consistent additional improvements of 4-10% across benchmarks." (Evidence preview with specific numbers.)
- **P5 — Contributions:** Listed as three items: (1) framework, (2) two-stage fine-tuning mechanism, (3) experimental validation. (Explicit enumeration.)

### Title Options
**Current:** "PICL: Incorporating Coarse-Grained Data and Physics Information for Superior Physical Systems Modeling"
**Option A (recommended):** "PICL: Physics-Informed Coarse-Grained Learning for PDE Forecasting with Sparse Observations"
**Option B:** "Learning Physical System Dynamics from Coarse-Grained Observations via Latent Physics Constraints"
**Option C:** "Coarse-to-Fine Physics-Informed Neural Forecasting with Semi-Supervised Fine-Tuning"

## Priority Revision Plan
### P0 — Publication-Critical (Must fix before acceptance)

| # | Task | Location | Effort | Expected Impact |
|---|------|----------|--------|-----------------|
| P0.1 | Add multi-seed statistics (≥3 seeds) with mean±std for all tables and figures | Table 1, Fig 2-3 | 2-3 days compute | High: validates core claim |
| P0.2 | Clarify F(ũ)→F(û) substitution assumption and add ε to L_d denominator | Page 5, Eq. (4) | 30 min | High: resolves notation error |
| P0.3 | Add controlled baseline (PICL-encoder-ablated with γ=0) | Page 6, Section 5.1 | 1-2 days compute | High: fair comparison |
| P0.4 | Reframe contributions to highlight two-stage fine-tuning | Page 2, intro | 1 hour | Medium: better positioning |

### P1 — High Priority (Should fix before next submission)

| # | Task | Location | Effort | Expected Impact |
|---|------|----------|--------|-----------------|
| P1.1 | Add per-step error decomposition for multi-step claims | Page 8, Section 5.3 | 1 day | Medium: evidence for claim |
| P1.2 | Restructure related work around comparison axes | Page 2-3, Section 2 | 2-3 hours | Medium: clearer positioning |
| P1.3 | Report parameter counts for encoder vs transition modules | Appendix A | 30 min | Low: transparency |
| P1.4 | Expand conclusion with validated findings and limitations | Page 9, Section 6 | 1 hour | Medium: completeness |

### P2 — Nice-to-Have

| # | Task | Location | Effort | Expected Impact |
|---|------|----------|--------|-----------------|
| P2.1 | Add OOD coarseness generalization test (train on 7×7, test on unseen 4×4, 8×8) | Appendix or Section 5.5 | 1 day | Medium: robustness |
| P2.2 | Add Transformer encoder results to main text (currently only in appendix) | Main text Section 5 | 1 hour | Low: completeness |
| P2.3 | Replace "first" in SR paragraph with qualified statement | Page 3, Section 2 | 15 min | Low: accuracy |

### Revision Sequence (Recommended Order)
1. **Immediate (Day 1-2):** P0.2 (notation fix), P0.4 (reframe contributions), P1.3 (parameter counts), P2.3 (first claim)
2. **Compute-heavy (Day 3-7):** P0.1 (multi-seed runs), P0.3 (controlled baseline), P1.1 (error decomposition)
3. **Writing (Day 8-10):** P1.2 (restructure related work), P1.4 (expand conclusion), P2.1-2.2 (optional extensions)

### Expected Outcome After P0 Fixes
If the P0 items are addressed, the paper would have: (a) statistically grounded results, (b) a clearly defined loss function, (c) fair baseline comparisons, and (d) well-framed contributions. These are the minimum requirements for the paper's claims to be credible.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1: Wave Eqn. one-step | Test PICL on wave equation | Wave eqn. (5), coarse 9×9→fine 41×41, 4 baselines | L_d, ε | PICL fine-tune: L_d=2.64E-2 (17% vs FNO*) | C2 (improvement) | No std reported; ε uncalibrated |
| E2: LSWE one-step | Test PICL on linear SWE | LSWE (6), coarse 7×7→fine 32×32, 4 baselines | L_d, ε | PICL fine-tune: L_d=2.44E-2 (48% vs FNO*) | C2 | Same as E1 |
| E3: NSWE one-step | Test PICL on nonlinear SWE | NSWE (7), coarse 7×7→fine 32×32, 4 baselines | L_d, ε | PICL fine-tune: L_d=3.50E-2 (45% vs FNO*) | C2 | Same as E1 |
| E4: Multi-step pred. | Test PICL on 10-step rollout | All 3 benchmarks, 10 steps | L_d (per step, cumulative) | PICL consistently lowest across steps | C2 (multi-step) | No error decomposition |
| E5: Ablation - γ | Find optimal physics loss weight | NSWE, γ∈{0,1E-3,5E-2,1E-1,2E-1,1} | L_d | Optimal γ=0.1-0.2 | Framework sensitivity | Single benchmark |
| E6: Ablation - n | Find optimal input length | NSWE, n∈{1,2,4,6,8} | L_d | Optimal n=4 | Framework sensitivity | n=2 also competitive |
| E7: Ablation - m1,m2,q | Find optimal fine-tuning steps | NSWE, m1,m2∈{5,10,20}, q∈{50,100,200,500} | L_d | Optimal m1=m2=10, q=100 | Two-stage benefit | No analysis of why |
| E8: Data quantity - labeled | Test labeled data impact | NSWE, Nlab∈{50,...,350} | L_d | L_d decreases with more data | Data efficiency | Saturation not shown |
| E9: Data quantity - unlabeled | Test unlabeled data impact | NSWE, Nun∈{10,50,100,150} | L_d | Fine-tuning always helps | Semi-supervised benefit | Small benefit range |
| E10: Data quality | Test coarse-grid size impact | NSWE, xo×yo∈{3×3,...,11×11} | L_d | Larger coarse grids → better | Robustness | Non-monotonic at 11×11 |
| E11: Encoder architecture | Test U-Net vs Transformer | NSWE, U-Net vs ViT encoder | L_d | U-Net better than Transformer | Architecture flexibility | Small gap |
| E12: Zero-shot SR | Test generalization to unseen grids | NSWE, train 7×7, test 3×3,5×5,7×7,11×11 | ε | PICL fine-tune better than FNO* | Zero-shot capability | Uses nearest neighbor interpolation |
| E13: Fine-grained data | Test if FG data helps | NSWE, 0/1/2/all with FG labels | L_d | FG data helps both baselines and PICL | FG substitutability by physics | Not main setting |

### Research-Theme Gap Diagnosis

1. **New Knowledge:** The paper's core new knowledge is that physics-informed learning is feasible from coarse observations via learnable latent fine-grained states. However, this knowledge claim is weakened because the mechanism is not fully isolated from confounds (encoder supervision, architectural asymmetry).

2. **Reproducibility:** The paper provides code, architecture details, and hyperparameters. The main reproducibility gap is the absence of multi-seed statistics, which makes it impossible to verify whether the reported numbers are typical or cherry-picked.

3. **Impact on Practice/Understanding:** The paper would benefit from analyzing *when* PICL works and *when* it fails (failure-case analysis). Currently, only average performance is reported. Understanding the conditions under which the physics loss in latent space fails would significantly increase practical value.

### Proposed Research Experiments (P0/P1/P2)

**P0-Exp1: Multi-seed stability assessment**
- **Target Claim:** C2 (predictive improvement)
- **Hypothesis:** PICL consistently outperforms baselines across different random seeds
- **Minimal Design:** Run PICL w/o fine-tune, PICL with fine-tune, FNO*, FNO on NSWE with 5 seeds
- **Controls/Baselines:** Same data splits, same random seeds for all methods
- **Metrics:** L_d mean±std, min-max range, pairwise Wilcoxon p-value
- **Success Criterion:** PICL with fine-tune has L_d mean+1std < FNO* mean
- **Estimated Cost:** ~2-3 GPU-days
- **Expected Quality Gain:** Critical — without this, core claim is not statistically supported

**P0-Exp2: Encoder-supervision controlled ablation**
- **Target Claim:** C2 (framework benefit beyond encoder supervision)
- **Hypothesis:** The two-stage fine-tuning provides benefits even when the encoder receives no physics loss
- **Minimal Design:** Add "PICL-enc-ablated" (γ=0 for encoder during base-training, but fine-tuning unchanged) on NSWE
- **Controls/Baselines:** Compare vs FNO* and PICL w/o fine-tune
- **Metrics:** L_d, ε
- **Success Criterion:** PICL-enc-ablated > PICL w/o fine-tune (i.e., fine-tuning alone provides benefit)
- **Estimated Cost:** ~1 GPU-day
- **Expected Quality Gain:** High — separates framework contribution from auxiliary supervision

**P1-Exp3: Error accumulation analysis**
- **Target Claim:** Multi-step prediction benefit
- **Hypothesis:** Per-step error growth is lower for PICL than FNO* because PDE constraints regularize the learned dynamics
- **Minimal Design:** Compute ΔL_d(s) = L_d(s) - L_d(s-1) for each step s=1,...,10 on NSWE for PICL and FNO*
- **Controls/Baselines:** Compare ΔL_d curves
- **Metrics:** Per-step error ΔL_d, slope of cumulative error
- **Success Criterion:** ΔL_d slope is significantly lower for PICL than FNO*
- **Estimated Cost:** No extra compute (use existing rollout data)
- **Expected Quality Gain:** Medium — substitutes speculation with evidence

**P1-Exp4: Failure-case analysis**
- **Target Claim:** Framework generality
- **Hypothesis:** PICL failures occur at predictable PDE regimes (e.g., sharp gradients, high nonlinearity)
- **Minimal Design:** Collect all NSWE test trajectories where PICL L_d > 2× median. Analyze spatial gradients, nonlinear term magnitudes, and compare to success cases.
- **Controls/Baselines:** N/A (descriptive analysis)
- **Metrics:** Qualitative description, feature histograms for failure vs success
- **Success Criterion:** Identifiable boundary conditions or PDE regimes for failure
- **Estimated Cost:** ~0.5 day analysis
- **Expected Quality Gain:** Medium — strengthens understanding and practical usefulness

### ASCII Diagram — Experiment Upgrade Plan
```text
P0-Exp1: Multi-seed stability (NSWE, 5 seeds)
    └──> P0-Exp2: Controlled ablation (encoder-ablated PICL)
        └──> P1-Exp3: Error accumulation analysis (per-step ΔL_d)
            └──> P1-Exp4: Failure-case analysis (high-L_d trajectories)
                └──> All P0/P1 done → submit revision
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Rationale:** The paper addresses a relevant problem and proposes a technically coherent framework. However, the experimental validation lacks statistical rigor (no variance reporting, no significance tests), the loss function contains a symbol inconsistency that must be resolved, and the baseline comparisons are not fully controlled. The contributions are framed too broadly without highlighting the genuinely novel two-stage fine-tuning mechanism. The paper has solid potential but currently requires major revisions before the claims can be considered supported by the evidence.

**Score Breakdown:**
- Research Value / Contribution: 6/10 (practical problem, well-motivated, but novelty positioning needs work)
- Validity / Soundness: 4/10 (missing statistics, symbol inconsistency, baseline fairness concerns)
- Novelty: 5/10 (interesting combination of SR and physics-constrained forecasting, but externally unverifiable in this run)
- Reproducibility: 7/10 (code provided, architecture detailed, but missing seed-dependent variance)
- Presentation / Clarity: 5/10 (good structure, but contributions under-framed, conclusion too brief, related work too list-like)

**Post-Revision Target: [6.5, 7.5] / 10**

If the P0 items are addressed (multi-seed statistics, loss function clarification, controlled baseline, reframed contributions) and the paper undergoes careful rewriting of the introduction, related work, and conclusion sections, the score could rise to the 6.5-7.5 range. This assumes the experimental results hold with statistical significance and the framework's advantage over controlled baselines remains clear.