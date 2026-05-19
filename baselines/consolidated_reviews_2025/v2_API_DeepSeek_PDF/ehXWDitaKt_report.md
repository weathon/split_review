## Summary
# Final Review Report

## Summary

This paper proposes **Newton Losses**, a method for improving the optimization of non-convex algorithmic losses (losses that embed differentiable algorithms like sorting or shortest-path computation) by incorporating second-order curvature information. The key idea is to split each training step into two substeps: (1) a Newton step on the loss function's output space, using either the Hessian or an empirical Fisher approximation, to produce a locally improved target; (2) a standard gradient descent step on the neural network parameters to regress toward this target. The method only replaces the loss function, keeping the network optimizer unchanged.

The paper provides two variants: a **Hessian-based** version (stronger but requires second derivatives) and an **empirical Fisher-based** version (widely applicable, using only gradients). Theoretical analysis (Lemmas 2–4 in the appendix) shows equivalence conditions between the split and standard optimization under idealized assumptions. Experimental evaluation spans eight differentiable algorithm methods across two tasks — multi-digit MNIST sorting and Warcraft shortest-path — showing consistent improvements, with the largest gains (up to >2× accuracy) on losses most affected by vanishing/exploding gradients. An ablation study on MNIST classification verifies that Newton Losses does not harm convex, well-behaved losses.

**Core strength:** The paper identifies a practical and well-motivated problem — hard-to-optimize algorithmic losses — and proposes a clean, general-purpose plug-in solution that is theoretically grounded and empirically validated across diverse methods. The two-variant design (Hessian/Fisher) appropriately handles practical constraints on Hessian availability.

**Core weaknesses:** (1) The empirical Fisher variant's limitations (unreliable curvature in few-sample regimes, sensitivity to gradient noise) are insufficiently characterized; (2) hyperparameter λ is selected per method from a single seed, raising selection-bias concerns for high-variance methods; (3) the theoretical convergence equivalence (Lemma 4) relies on an unrealistic surjectivity assumption (Y=R^{N×m}); (4) statistical significance reporting lacks p-values and confidence intervals despite overlapping standard deviations; (5) the ablation study includes a broken configuration (M4 sigmoid+SGD at chance level) that inflates the "no harm" claim.

## Strengths
1. **Well-motivated problem framing.** The paper identifies a genuine optimization challenge in weakly-supervised learning: algorithmic losses are non-convex, non-monotonic, and suffer from vanishing/exploding gradients. The motivation is clearly connected to the proposed solution — applying second-order optimization on the lower-dimensional loss space while keeping first-order updates on the network.

2. **Clean and general method design.** Newton Losses is architecture-agnostic and requires minimal changes to existing training pipelines. The two-variant approach (Hessian when available, empirical Fisher as fallback) is practical and well-justified. The InjectFisher implementation (Algorithm 2) elegantly modifies only the backward pass, making adoption straightforward.

3. **Broad empirical evaluation.** The evaluation covers eight different differentiable algorithm methods across two distinct benchmarks (ranking and shortest-path), including both analytical relaxations and stochastic methods. This breadth strengthens the claim that Newton Losses is a general-purpose improvement for hard-to-optimize losses.

4. **Significant improvements on difficult losses.** For NeuralSort, SoftSort, and Logistic DSNs — methods known to suffer from gradient pathology — Newton Losses achieves substantial gains (e.g., NeuralSort at n=10: 24.26% → 48.76% with Hessian variant). These improvements are practically meaningful.

5. **Theoretical analysis of the optimization split.** Lemmas 2-4 provide formal justification that the two-step split (Eq. 3a-3b) is equivalent to standard optimization under specified conditions, adding theoretical credibility to the method.

6. **Ablation study scope.** Testing 5 models × 2 optimizers = 20 settings with 20 seeds each on MNIST classification provides reasonable evidence that Newton Losses does not harm convex, well-behaved losses. The runtime analysis across all methods is thorough and shows that the Fisher variant adds negligible overhead.

7. **Open-science friendly implementation details.** The paper provides complete pseudo-code (Algorithms 1-2) with clear separation of Hessian and Fisher variants. The appendix includes Woodbury identity derivations for scalability and closed-form Newton losses for common standard losses.

## Weaknesses
1. **Empirical Fisher limitations under-characterized.** While the paper acknowledges that the empirical Fisher differs from the true Fisher, it does not analyze when the empirical Fisher provides reliable curvature for algorithmic losses. For losses with noisy gradient estimates (e.g., perturbed optimizers with few samples), the Fisher-based preconditioner can amplify noise rather than useful curvature, as seen in Table 3 (SS of loss with 3 samples: baseline 62.83% vs NL Fisher 58.80%). This failure mode is mentioned but not analyzed mechanistically.

2. **Hyperparameter λ selection methodology.** The Tikhonov regularization strength λ is selected per method based on a single seed (Appendix C), then used for all 10 evaluation seeds. For high-variance methods (Logistic DSN n=10: std up to 30.63%), this risks overfitting λ to one seed's noise pattern. The λ ablation (Figure 4) uses only 2 runs per setting ("will be updated to 10 runs for the camera-ready"), which is insufficient to demonstrate robustness.

3. **Statistical rigor gaps.** Significance claims (α=0.05) are stated but without reporting actual p-values, test types, or confidence intervals for the improvement deltas. Several methods show overlapping standard deviations between baseline and Newton Losses (e.g., Cauchy DSN n=5: 85.09±0.77 vs 85.11±0.78), making the significance claim questionable. The Fisher variant for Logistic DSN n=10 shows 25.72±27.42 — a standard deviation larger than the mean — which suggests extreme instability.

4. **Theoretical assumptions not grounded in practice.** Lemma 4's convergence-set equivalence requires the surjectivity assumption Y = R^{N×m}, which holds only for idealized infinite-capacity networks. The paper does not discuss the practical implications when this assumption is violated. Remark 1's generalization of Lemma 4 to Newton Losses vs standard training is therefore over-claimed.

5. **Ablation study includes a broken configuration.** Model M4 (LeNet-5 with sigmoid + SGD) achieves only 10.57% accuracy (random chance for 10-class MNIST), indicating a training configuration failure. Including this in the "indistinguishable to regular training" claim inflates the apparent agreement — both methods simply fail equally on this broken setup.

6. **InjectFisher scaling inconsistency.** Algorithm 2 computes `fisher = g.T @ g * g.shape[0]`, which yields N² times the empirical Fisher defined in Eq. (8). While λ can absorb this scaling, the mismatch between code and definition makes λ batch-size dependent, which is undocumented.

7. **Conclusion lacks specificity.** The concluding paragraph includes aspirational language ("unexplored territories of the space of differentiable relaxations") without concrete next-step research directions or a clear statement of the method's limitations.

## Key Issues
**Issue 1 (Major): Statistical evidence quality for core improvement claims**
- **Severity:** High — directly affects confidence in the main contribution
- **Evidence:** Table 1, Table 3 show overlapping std ranges between baseline and NL for multiple settings (Cauchy DSN n=5: 85.09±0.77 vs 85.11±0.78; Logistic DSN Fisher n=10: 25.72±27.42). Significance at α=0.05 is claimed without reporting p-values, test type, or effect-size CIs.
- **Impact:** Reviewers cannot assess whether improvements are statistically reliable. The high-variance settings (Logistic DSN, SS of algorithm with 3 samples) show NL performing worse than baseline in some runs.
- **Fix required:** Report paired t-test or Wilcoxon p-values for each baseline-vs-NL comparison. For high-variance settings, include median+IQR and discuss outlier effects. Add a table of deltas with 95% CIs.

**Issue 2 (Major): λ selection methodology risks overfitting**
- **Severity:** High — could inflate reported improvements
- **Evidence:** Appendix C states λ selected "based on one seed from the grid." λ varies from 0.001 to 1000 across methods (Tables 8-9), a range of 6 orders of magnitude. For Logistic DSN n=10 (baseline 12.31±10.22), even a single λ value can produce dramatically different results depending on seed.
- **Impact:** If λ is chosen to maximize improvement on one seed, the reported mean over 10 seeds may be optimistically biased. The λ ablation (Figure 4) uses only 2 runs per value, insufficient for robustness assessment.
- **Fix required:** (a) Select λ via cross-validation across seeds. (b) Report λ sensitivity with learning curves. (c) Update Figure 4 to 10 runs as promised. (d) Provide guidance for λ selection in practice.

**Issue 3 (Major): Broken ablation configuration inflates "no harm" claim**
- **Severity:** Medium-High — weakens the ablation's credibility
- **Evidence:** Page 9, Table 4, model M4 (LeNet-5 sigmoid + SGD) shows 10.57% accuracy — random chance for 10-class MNIST. This indicates a training failure (bad initialization, learning rate too low, or saturation), not valid comparison. Including it in the 9/20/7/1 counting distorts the conclusion.
- **Impact:** Readers cannot distinguish between "Newton Losses is harmless" and "both methods fail equally on broken configs." This undermines the ablation's otherwise careful design.
- **Fix required:** Diagnose and fix M4 configuration. If not fixable, exclude it and report separately with an explanation.

**Issue 4 (Major): Theoretical convergence equivalence relies on unrealistic assumption**
- **Severity:** Medium — affects theoretical contribution credibility
- **Evidence:** Lemma 4 (Appendix D.3) assumes Y = R^{N×m} (network can produce any output). Remark 1 extends equivalence to "Newton's method vs Newton Losses" without addressing the practical gap.
- **Impact:** The theoretical foundation is weaker than claimed. The method's empirical success may stem from effects other than the stationary-point equivalence (e.g., the preconditioning changes the optimization path, not just the convergence set).
- **Fix required:** Add a remark explicitly discussing the surjectivity assumption gap and its practical implications. Distinguish between "fixed points are equivalent under ideal conditions" and "optimization trajectories differ in practice."

**Issue 5 (Major): Empirical Fisher code-definition mismatch**
- **Severity:** Medium — affects reproducibility
- **Evidence:** Algorithm 2: `fisher = g.T @ g * g.shape[0]` vs Definition 2: (1/N)∑∇ℓ_i·∇ℓ_i^T. The code computes N² times the defined quantity.
- **Impact:** λ becomes batch-size-dependent without documentation. Practitioners porting the method to different batch sizes may get inconsistent results.
- **Fix required:** Either correct the implementation or explicitly document the scaling factor and its effect on λ transferability.

## Actionable Suggestions
### S1: Strengthen statistical evidence (Must)
For each baseline-vs-NL comparison in Tables 1-3, add:
- A column with the **improvement delta** and its 95% confidence interval
- The **p-value** from a paired t-test or Wilcoxon signed-rank test across the 10 seeds
- For high-variance settings (Logistic DSN, SS of algorithm with 3 samples), additionally report **median ± IQR** and the **percentage of seeds where NL improves** over baseline

### S2: Improve λ selection and sensitivity analysis (Must)
- Perform λ selection via **3-fold cross-validation across seeds** rather than a single seed
- Add a **λ sensitivity table** showing mean±std at λ = 0.1×, 1×, 10× the chosen value for each method
- Update Figure 4 to use **10 runs** (as the paper already promises in the caption: "will be updated to 10 runs for the camera-ready")
- Provide a **λ selection heuristic** (e.g., "set λ = c·Tr(F) where c ∈ [0.01, 1]" or cross-validate on a small validation set)

### S3: Fix ablation study configuration (Must)
- Diagnose the M4 (LeNet-5 sigmoid + SGD) failure: try **higher learning rate**, **Xavier/Glorot initialization**, or **batch normalization** to enable learning
- If M4 remains at chance level, **exclude it** from the summary statistics and report separately with an explanation
- Report the **effect sizes** (improvement delta per model) rather than only the count of "better/equal/worse"

### S4: Document empirical Fisher scaling and limitations (Must)
- **Correct or document** the scaling factor in Algorithm 2: either change to `fisher = (g.T @ g) / g.shape[0]` or add an explicit comment explaining the N² factor and its batch-size dependence
- Add a **limitation paragraph** on when the empirical Fisher is unreliable (few-sample regime, early training, multi-modal losses) as suggested in the Page 4 annotation

### S5: Tighten novelty claim in Related Work (Nice-to-have)
Rephrase "first work" to "first work — to our knowledge — applying second-order optimization on the loss output space rather than network parameters for algorithmic losses" to preempt reviewer challenges.

### S6: Strengthen conclusion with limitations and concrete next steps (Nice-to-have)
Replace the vague last sentence with three concrete directions:
- Custom Hessian implementations for structured prediction to reduce 1.1-2.6× overhead
- Theoretical convergence analysis under finite-network realistic assumptions
- Application to differentiable physics simulators and combinatorial optimization beyond shortest-paths

### S7: Add Woodbury forward-reference in main text (Nice-to-have)
Add a one-sentence forward reference in Section 3.3 to Appendix G for high-dimensional outputs, as suggested in the Page 21 annotation.

## Storyline Options + Writing Outlines
### Current Storyline Evaluation

The current introduction follows this structure:
- P1: Traditional losses are convex → weakly-supervised learning uses algorithmic losses → these are hard to optimize due to non-convexity/gradient issues
- P2: Literature survey of algorithmic loss applications (list of domains)
- P3: Second-order optimization of networks is expensive → we propose Newton Losses

**Problems:** P1 spends too long on traditional learning before stating the paper's actual focus. P2 is a citation list without conceptual organization. P3's logic (second-order is expensive on networks → apply it on loss) is sound but the transition is buried mid-paragraph across a page break.

### Recommended Storyline

**Option A (Recommended — Problem-to-Solution):**

- **P1:** "Algorithmic losses — loss functions that embed non-differentiable operators like sorting or shortest-path — arise naturally in weakly-supervised learning. Unlike standard convex losses, these losses are typically non-convex, non-monotonic, and exhibit vanishing or exploding gradients, making optimization the primary bottleneck in training."
- **P2:** "Existing solutions address this challenge by designing smoother relaxations (e.g., SoftSort, DSNs, AlgoVision, stochastic smoothing). While effective, each new relaxation requires custom design and analysis. This paper asks: can we improve training of *any* algorithmic loss by locally modifying its curvature, rather than redesigning the loss itself?"
- **P3:** "Second-order optimization can accelerate convergence but is impractical for large neural networks due to computational cost and generalization concerns. However, loss functions operate in lower-dimensional spaces than network parameters and are cheaper to evaluate. This suggests a split: apply second-order optimization locally on the loss output, while keeping first-order updates for the network."
- **P4:** "We formalize this split as Newton Losses — a plug-in replacement that replaces any loss ℓ with ℓ*(y) = ½‖z⋆ - y‖² where z⋆ is a Newton step of ℓ(y). We provide Hessian and empirical Fisher variants. Experiments on eight differentiable algorithm methods across sorting and shortest-path benchmarks show consistent improvements, with up to 2× accuracy gains on the hardest cases."

### Abstract Outline (Complete)

**S1 (Problem):** "In weakly-supervised learning, loss functions often embed differentiable algorithmic procedures such as sorting or shortest-path computation, leading to non-convex objectives that suffer from vanishing and exploding gradients."

**S2 (Challenge):** "These algorithmic losses are the primary optimization bottleneck, yet each new relaxation requires custom redesign to improve trainability."

**S3 (Gap):** "Existing second-order optimization methods accelerate training but are computationally prohibitive for large networks and may reduce generalization."

**S4 (Method):** "We propose Newton Losses, a plug-in method that locally approximates any algorithmic loss with a quadratic via its second-order information, then trains the network with standard gradient descent. The method is available in a Hessian variant (stronger, requires second derivatives) and an empirical Fisher variant (widely applicable, only needs gradients)."

**S5 (Result):** "On eight differentiable algorithm methods across the multi-digit MNIST sorting and Warcraft shortest-path benchmarks, Newton Losses consistently improves or matches baseline performance, with up to 2× accuracy gains on the most difficult losses."

### Introduction Outline (Complete)

**P1 (Stakes & Gap):**
- Role: Define the problem domain and why it matters
- Claim: Algorithmic losses are hard to optimize and this is the bottleneck
- Evidence: References [1], [2] on non-convex optimization challenges
- Transition: "This difficulty motivates a method that works with any algorithmic loss without redesign."

**P2 (Prior Work & Limitation):**
- Role: Survey existing differentiable algorithm relaxations (sorting, shortest-path, rendering) and identify that each requires custom design
- Claim: No existing approach provides a general-purpose loss-level fix
- Evidence: References [5]-[18], [33]-[42]
- Transition: "A different angle is to improve optimization of the loss itself using second-order information."

**P3 (Second-Order Motivation & Split Idea):**
- Role: Explain why second-order on loss is feasible when second-order on network is not
- Claim: Loss functions are cheap, low-dimensional → Newton step is tractable on loss
- Evidence: [26] on second-order limitations in networks, [29] on computational cost
- Transition: "This leads to the two-step split that defines Newton Losses."

**P4 (Method Summary & Contributions):**
- Role: State the proposed method and contributions
- Claim: Newton Losses is a general plug-in with two variants, evaluated across 8 methods
- Evidence: Preview of Table 1, Table 3 results
- Transition: [to Section 2, Related Work]

## Priority Revision Plan
### P0 Items (Must fix before acceptance)

| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| P0.1 | Statistical evidence gaps | 2-3 days | High | Add p-values, CIs, and median+IQR to Tables 1-3; clarify significance test type |
| P0.2 | λ selection methodology | 1-2 days | High | Cross-validate λ across seeds; add λ sensitivity table; update Figure 4 to 10 runs |
| P0.3 | Ablation M4 broken config | 1 day | Medium | Diagnose M4; fix or exclude with explanation |
| P0.4 | Algorithm 2 Fisher scaling documentation | 0.5 day | Medium | Add comment explaining N² factor and batch-size dependence; or correct to (g.T@g)/N |

### P1 Items (Should fix for strong resubmission)

| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| P1.1 | Empirical Fisher limitation discussion | 1 day | Medium | Add limitation paragraph on when empirical Fisher is unreliable |
| P1.2 | Lemma 4 surjectivity caveat | 0.5 day | Medium | Add Remark 2 discussing practical implications of finite networks |
| P1.3 | Conclusion rewrite | 1 day | Medium | Restructure into validated findings → limitations → concrete future work |
| P1.4 | Abstract scope bounding | 0.5 day | Medium | Add sentence about output-dimensionality constraint |

### P2 Items (Nice-to-have improvements)

| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| P2.1 | Introduction storyline revision | 1-2 days | Medium | Restructure per recommended Option A outline above |
| P2.2 | Woodbury forward-reference in main text | 0.5 day | Low | Add one-sentence pointer in Section 3.3 to Appendix G |
| P2.3 | "First work" claim scoping | 0.5 day | Low | Add "to our knowledge" qualifier and specify contribution niche |
| P2.4 | Notation clarity for Eq. (3a)-(3b) | 0.5 day | Low | Explicitly state "single-step" in main text |
| P2.5 | Expectation notation clarification in Appendix F | 0.5 day | Low | Define E[·] as empirical batch expectation |

### Revision Flow Diagram

```text
[P0.1: Add significance tests & CIs] ──→ [Tables 1-3 credibility ↑]
                                              │
[P0.2: Cross-validated λ + sensitivity] ──→ [Robustness evidence ↑]
                                              │
[P0.3: Fix M4 ablation] ──→ [Ablation conclusion reliability ↑]
                                              │
[P0.4: Document Fisher scaling] ──→ [Reproducibility ↑]
                                              │
                                              ▼
                                     [Resubmission ready]
                                              │
                ┌─────────────────────────────┼────────────────────────────┐
                ▼                             ▼                            ▼
        [P1.1-1.4: Empirical Fisher     [P1.1-1.4: Conclusion     [P2 items: Polish and
         limitation + theory caveat]      + abstract revision]       storyline revision]

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|-----------------|-------------------|
| E1 | Ranking supervision (Table 1) | 4-digit MNIST sorting; n∈{5,10}; NeuralSort, SoftSort, Logistic DSN, Cauchy DSN; 10 seeds | % rankings correct, % individual ranks correct | NL improves all baselines; up to 2× for hard cases | C3 (empirical gains) | λ selected per seed; significance unclear for high-variance methods |
| E2 | Shortest-path: Relaxed Bellman-Ford (Table 2) | 12×12 Warcraft; For/While × L1/L2²; 10 seeds | % perfect matches | Small improvements in 3/4 settings | C3 | Only Fisher variant; baseline already >94% |
| E3 | Shortest-path: Stochastic Smoothing (Table 3) | 12×12 Warcraft; SS of loss/algorithm; 3/10/30 samples; 10 seeds | % perfect matches | NL improves for ≥10 samples; poor at 3 samples | C3 | High variance at 3 samples; Fisher degrades performance |
| E4 | Shortest-path: Perturbed Optimizers FY (Table 3) | 12×12 Warcraft; 3/10/30 samples; 10 seeds | % perfect matches | Hessian NL improves >2%; Fisher equivalent | C3 | Fisher variant not meaningful for FY losses |
| E5 | Ablation: MNIST classification (Table 4) | 5 models × 2 optimizers; 20 seeds; 1 & 200 epochs | Accuracy (%) | NL indistinguishable from baseline | Safety verification | M4 config broken (10.57%); 1/20 significant by chance |
| E6 | Runtime analysis (Appendix B, Tables 5-7) | All above settings; single A6000 GPU | Training time (seconds) | Fisher NL ≈ Baseline; Hessian NL 1.1-2.6× overhead | Efficiency claim | Hessian overhead significant for DSNs (2.6×) |
| E7 | λ ablation (Figure 4) | NeuralSort & SoftSort n=5; 13 λ values; 2 runs | Individual rank accuracy | Method robust across λ orders of magnitude | Method robustness | Only 2 runs per λ (not 10); only 2 methods tested |

### Research-Theme Gap Diagnosis

1. **New knowledge gap:** The paper's core new knowledge is that local second-order preconditioning of the loss output space improves optimization of algorithmic losses. However, the theoretical foundation (Lemma 4) has an unrealistic surjectivity assumption, and the empirical evidence for the Fisher variant is mixed — it sometimes hurts (3-sample regime) while the mechanism for this failure is not analyzed.

2. **Reproducibility gap:** The code-paper mismatch in Algorithm 2's Fisher scaling and the λ selection methodology (single seed) create reproducibility risks. The M4 broken configuration in the ablation also undermines the "no harm" conclusion's reproducibility.

3. **Practical impact gap:** The method's practical value depends on whether practitioners can easily select λ and trust the Fisher variant. The current ablation (§4.3) only tests convex cross-entropy, not the more common case of a non-convex but moderately-well-behaved algorithmic loss where Newton Losses might help or hurt.

### Proposed Research Experiments

**P0 Experiment 1: λ cross-validation robustness**
- **Target Claim:** C3 (Newton Losses consistently improves baselines)
- **Hypothesis:** Improvement is not sensitive to λ selected on a single seed
- **Minimal Design:** For NeuralSort n=10 (high-variance case), select λ via 3-fold cross-validation over 10 seeds, compare to single-seed selection. Report mean±std improvement.
- **Controls:** Same optimizer, learning rate, and temperature as baseline
- **Metrics:** % rankings correct, p-value of improvement over baseline
- **Success Criterion:** Cross-validated λ yields improvement at least 80% of single-seed λ
- **Cost:** ~2 GPU-days
- **Expected Gain:** Robustness evidence for hyperparameter selection methodology

**P0 Experiment 2: Statistical significance table**
- **Target Claim:** C3 (improvements are statistically significant)
- **Hypothesis:** Improvements are significant under paired testing
- **Minimal Design:** For every setting in Tables 1-3, compute paired t-test p-values and 95% CI of the delta. Report in a supplementary table.
- **Controls:** Bonferroni correction for multiple comparisons across methods
- **Success Criterion:** At least 80% of claimed-significant comparisons survive correction
- **Cost:** ~0.5 day (computational only)
- **Expected Gain:** Credible, review-resistant significance statements

**P1 Experiment 3: Fisher variant failure-mode analysis**
- **Target Claim:** C3 (Fisher variant is a useful fallback)
- **Hypothesis:** Fisher degradation in 3-sample regime is due to noise amplification
- **Minimal Design:** For SS of loss with 3 samples, compare Fisher spectra (eigenvalue distribution) at epoch 1 vs epoch 50. Show that Fisher eigenvalues are dominated by sampling noise early and stabilize later.
- **Controls:** Hessian variant and baseline gradient norms
- **Metrics:** Condition number of Fisher matrix, gradient similarity (cosine) between NL-Fisher and NL-Hessian steps
- **Success Criterion:** Fisher has 10× higher condition number than Hessian at epoch 1
- **Cost:** ~1 GPU-day
- **Expected Gain:** Mechanistic understanding of Fisher failure; guidance for practitioners

**P1 Experiment 4: Ablation M4 diagnostic**
- **Target Claim:** Safety (NL does not harm convex losses)
- **Hypothesis:** M4 (LeNet-5 sigmoid+SGD) at 10.57% is a training failure unrelated to loss
- **Minimal Design:** Test M4 with (a) higher learning rate {0.01, 0.1}, (b) Adam instead of SGD, (c) proper weight initialization
- **Success Criterion:** Achieve >90% accuracy with any reconfiguration
- **Cost:** ~2 GPU-hours
- **Expected Gain:** Clean ablation; either valid "no harm" evidence or discovery of failure mode

### Experiment Upgrade Plan Diagram

```text
P0 Experiments (BEFORE resubmission)
├── P0.1: λ cross-validation (High priority) ──→ Confidence in hyperparameter selection
└── P0.2: Statistical significance table ──→ Review-resistant claims

P1 Experiments (IF time permits)
├── P1.1: Fisher failure-mode analysis ──→ Mechanistic understanding
└── P1.2: M4 ablation diagnostic ──→ Clean safety validation

P2 Experiments (NEXT submission)
├── P2.1: Non-convex but well-behaved loss test ──→ Broader safety coverage
└── P2.2: OOD/perturbation sensitivity ──→ Robustness evidence

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

*Rationale:* The paper presents a well-motivated, cleanly designed method that is empirically evaluated across diverse settings. The core idea (second-order preconditioning on the loss output space) is sound and practically useful. However, the score is constrained by the following factors:

- **Research Value (7/10):** The method is novel as a general plug-in for hard-to-optimize algorithmic losses. The two-variant design is practical. However, the incremental contribution per individual method is modest — Newton Losses is an engineering improvement on existing relaxations rather than a new algorithmic learning paradigm.
- **Validity/Soundness (6/10):** The statistical evidence is weaker than claimed (overlapping standard deviations, λ selection bias, no p-values). The ablation study includes a broken configuration that inflates the "no harm" claim. The theoretical analysis relies on an unrealistic surjectivity assumption without practical qualification.
- **Novelty (6.5/10):** The split-based optimization approach connects known ideas (proximal backpropagation, target propagation, Newton's method) in a new combination. Without external literature verification (this run is retrieval-disabled), the "first work" claim cannot be verified. The method's core mechanism — quadratic approximation + Tikhonov damping — is well-established; the novelty lies in applying it specifically to the loss output space for algorithmic losses.
- **Reproducibility (6/10):** Algorithms 1-2 provide clear pseudocode, but the Fisher scaling mismatch (page 5 annotation) and λ selection methodology create reproducibility risks. Runtime analysis is thorough.
- **Clarity/Presentation (7/10):** The method section is well-structured with clear definitions and derivations. The introduction storyline could be tightened (as recommended in the storylines section). The conclusion lacks specificity.

**Post-Revision Target: [7.5, 8.0] / 10**

If the following P0 items are addressed:
- P0.1: Statistical rigor (p-values, CIs, significance test details)
- P0.2: λ cross-validation and sensitivity analysis
- P0.3: M4 broken configuration fix
- P0.4: Algorithm 2 Fisher scaling documentation

...and P1 items are addressed (empirical Fisher limitation discussion, Lemma 4 caveat, conclusion rewrite), the paper would present a convincing, review-resistant contribution. The target range accounts for the inherent limitation that the theoretical analysis's surjectivity assumption cannot be fully resolved within a single revision, and that the Fisher variant's few-sample degradation is a structural limitation rather than a fixable bug.