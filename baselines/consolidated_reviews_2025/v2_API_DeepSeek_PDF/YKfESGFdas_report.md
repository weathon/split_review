## Summary
# Final Review Report

## Summary

This paper presents GeONet, a neural operator framework that learns the mapping from a pair of initial and terminal probability distributions (µ₀, µ₁) to the full Wasserstein geodesic {µₜ} connecting them. The core methodological idea is to reformulate the Benamou-Brenier dynamic optimal transport problem as a primal-dual PDE system (continuity equation + Hamilton-Jacobi equation) and train two coupled DeepONet-style networks to satisfy these PDE residuals via physics-informed losses, without requiring ground-truth geodesic data for training. The paper claims three main contributions: (C1) a physics-informed operator learning approach that learns geodesics without training on true geodesic data, (C2) mesh-invariant output enabling zero-shot super-resolution, and (C3) orders-of-magnitude inference speedup via amortized inference.

The technical approach is well-motivated and the combination of neural operators with OT optimality conditions is conceptually novel. However, the experimental evaluation has several significant weaknesses: (i) the speed comparison against POT uses very loose tolerances (threshold 10.0 for 2D) that may favor GeONet unfairly, (ii) the comparison against CFM/RF is methodologically asymmetric (density vs. particle outputs), (iii) the MNIST real-data experiment shows ambient-space L1 errors as high as 68%, questioning its practical utility, and (iv) key experimental details are deferred to appendices. The loss formulation's coupled PDE residual structure raises concerns about training stability and positivity constraints that are not addressed. Novelty and comparison conclusions are deferred due to external literature verification being unavailable in this run.

## Strengths
1. **Conceptually novel formulation.** Casting the Wasserstein geodesic computation as a neural operator learning problem over the primal-dual PDE system is a genuine conceptual contribution. This connects two previously separate fields (neural operators for PDEs and computational optimal transport) in a principled way, and the idea of training on only boundary pairs without geodesic supervision is elegant and well-motivated.

2. **Physics-informed training eliminates need for ground-truth geodesics.** The use of the KKT optimality conditions (continuity equation + Hamilton-Jacobi equation) as physics-informed loss is a key strength. It means the method can be trained solely on pairs of endpoint distributions, which are much easier to obtain than full geodesic data. This amortized inference paradigm is well-suited for applications requiring many repeated geodesic evaluations.

3. **Mesh-invariant output resolution.** The DeepONet-style architecture allows GeONet to predict the geodesic density at arbitrary space-time coordinates, enabling finer output resolution than the training grid without retraining. This is a genuine practical advantage over grid-based OT solvers that are bound to the discretization mesh.

4. **Competitive accuracy on Gaussian mixture benchmarks.** On 1D and 2D Gaussian mixtures, GeONet achieves L1 errors of ~5-8% for random pairings and ~7-8% for 2D problems, with reasonable standard deviations. These results demonstrate that the physics-informed training can learn meaningful geodesic approximations for continuous densities.

5. **Transparent limitations section.** The paper includes a dedicated limitations paragraph (Section 4.5) that honestly discusses the exponential scaling of branch network input with dimension, the need for predetermined evaluation points, and the open theoretical question of generalization bounds.

## Weaknesses
1. **Unfair runtime comparison (Major).** The speed comparison against POT (Section 4.4, Figure 6) uses a Sinkhorn stopping threshold of 10.0 for 2D, which is extremely loose. The claim of comparable accuracy at this threshold is unsupported by evidence (no POT error vs. threshold plot). The "orders of magnitude" speed advantage claimed in the abstract is therefore unreliable without matched-accuracy comparison.

2. **Asymmetric point-cloud comparison (Major).** Table 3 compares GeONet (which outputs densities) against CFM and RF (which output particle samples) using L1 error against a POT density reference. Converting samples to densities introduces discretization error, and CFM/RF were not designed for geodesic computation. The claim that "GeONet is the only framework... which encapsulates the geodesic behavior" overstates the evidence from an asymmetric evaluation.

3. **MNIST results are too weak to support real-data claims (Major).** Ambient-space L1 errors reach 68.1% at the geodesic midpoint (t=0.5) for random digit pairings, with standard deviations of 18.8%. The paper acknowledges that latent-space geodesics do not coincide with image-space geodesics, which fundamentally undermines the claim that GeONet works on real image data. The identity setting (same digit) already shows ~30% error, suggesting autoencoder distortion overwhelms the geodesic signal.

4. **Loss formulation has unaddressed technical vulnerabilities (Major).** The coupled PDE residual (Eq. 15-17) involves high-order mixed derivatives between Cϕ and Hψ, creating potential training instability. No positivity constraint ensures µ≥ 0 (the density output could become negative). Loss weights (α₁, α₂, β₀, β₁) are introduced without guidance on their selection. These issues are silently bypassed in the current manuscript.

5. **Input mesh-dependence vs. claimed mesh-invariance asymmetry (Moderate).** While the output is mesh-invariant, the branch networks require input distributions evaluated on a fixed equidistant grid. This restricts the method to gridded input data and limits applicability to irregularly sampled or multi-resolution input pairs.

6. **Incomplete reproducibility specifications (Moderate).** Key experimental parameters (training resolution m, number of distribution pairs n, DeepONet width p, training iterations, optimizer, loss weights) are deferred to appendices H-J. The collocation procedure's notation is ambiguous (N used for both batch size and collocation count). These omissions make independent reproduction difficult without extensive cross-referencing.

7. **Introduction narrative structure (Minor).** The introduction paragraphs do not clearly establish the specific research gap before presenting the solution. The transition from "OT must be recomputed per pair" to "operator learning perspective" lacks a logical bridge explaining why operator learning is the natural framework for this problem.

8. **"Zero-shot super-resolution" terminology overclaim (Minor).** The term implies a capability comparable to image super-resolution (e.g., 2x-8x upscaling), while the actual experiments show testing at 2x training resolution in 1D (100→200 points) with only ~1% error increase. The resolution gap and its significance are not clearly quantified in the main text.

## Key Issues
### Issue 1: Speed comparison lacks matched-accuracy evidence (Critical fixability)

**Location:** Page 9 - Section 4.4 (Runtime Comparison)

**Evidence:** The runtime comparison uses POT with stopping threshold 10.0 for 2D. The paper states "We found these choices were comparable to GeONet" without showing the error-threshold curve. A Sinkhorn tolerance of 10.0 on squared-Euclidean cost likely means the algorithm stops far from convergence, making POT artificially fast.

**Root cause:** The authors optimized for a runtime advantage without ensuring the baseline solver operates at the same accuracy level. The threshold selection rationale (0.5/10.0) is not empirically justified.

**Impact on research value:** If the core value proposition (orders-of-magnitude speedup) is based on an unfair comparison, the paper's main practical claim is unsupported. This can be fixed with additional experiments and more cautious claims.

**Fix:** Plot POT error vs. threshold; identify the threshold where POT matches GeONet's accuracy; then compare runtime at that threshold. Report training time and break-even analysis.

### Issue 2: CFM/RF comparison is methodologically asymmetric (Major)

**Location:** Page 8 - Section 4.2 (Point Clouds)

**Evidence:** GeONet produces continuous density fields on a grid (same format as POT reference), while CFM and RF produce particle samples. The conversion step (particles → density via binning) introduces quantization error that CFM/RF are not optimized for. Moreover, CFM and RF are generative flow models, not geodesic solvers — evaluating them on geodesic accuracy tests them outside their design scope.

**Root cause:** The authors selected baselines that are convenient for demonstrating superiority but not directly comparable in output modality.

**Impact on research value:** The claim that "GeONet is the only framework... which encapsulates geodesic behavior" is overstated and may mislead readers about the baseline capabilities.

**Fix:** (a) Use a density-estimation method (KDE) to convert CFM/RF samples to densities with bandwidth sensitivity analysis, or (b) compare all methods in sample space using distributional metrics (sliced Wasserstein distance, MMD), or (c) add amortized OT baselines (Meta OT) that directly predict OT plans.

### Issue 3: MNIST experiment does not support "real data" claim (Major)

**Location:** Page 8-9 - Section 4.3

**Evidence:** Ambient-space L1 errors reach 68.1% at geodesic midpoint (Table 4). The paper states geodesics in latent space and image space "do not coincide," meaning the autoencoder does not preserve OT geometry. Even identity pairings show ~30% error, indicating poor autoencoder reconstruction quality.

**Root cause:** The autoencoder's latent space does not inherit the Wasserstein geometry of the image space. Decoding the latent geodesic yields interpolations that are not Wasserstein geodesics in the original space.

**Impact on research value:** The paper's claim of demonstrating GeONet on "real data" is not supported. The experiment shows that a latent-space geodesic is not meaningful for image-space interpolation.

**Fix:** (a) Use an autoencoder trained with an OT-preserving regularization, or (b) apply GeONet directly to low-resolution images (e.g., 8×8 or 14×14) without autoencoder encoding, or (c) reframe the experiment as a proof-of-concept with explicit caveats about the geometry mismatch.

### Issue 4: Coupled PDE loss stability is unexamined (Major)

**Location:** Page 5 - Section 3, Eqs. (14)-(17)

**Evidence:** The loss couples two networks through a divergence-of-product term div(Cϕ ∇Hψ). No positivity constraint on Cϕ, no loss balancing discussion, and no training dynamics analysis are provided.

**Root cause:** The paper focuses on the mathematical formulation but does not examine the practical training challenges of coupled physics-informed neural operators.

**Impact on research value:** If the training is unstable or the two PDE residuals are not simultaneously minimized, the zero-duality-gap guarantee is violated and the method may not converge to the true geodesic.

**Fix:** (a) Add softplus activation on Cϕ output for positivity, (b) report separate training curves for Lcty and LHJ, (c) specify loss weight selection procedure, (d) add a synthetic test where the true geodesic is known to verify convergence.

## Actionable Suggestions
### S1 (Must): Fix the Runtime Comparison (Issue 1)
**Action:** Generate a figure showing POT error vs. stopping threshold (0.01, 0.1, 1.0, 5.0, 10.0) for the same test pairs used in Figure 6. Identify the threshold at which POT achieves the same L1 error as GeONet. Then report the runtime comparison at that matched-accuracy threshold. Separately, include a table with training time and inference time per geodesic (in milliseconds) so readers can compute the break-even point.

**Location:** Page 9 - Section 4.4

**Expected benefit:** Removes the most significant threat to the paper's core value claim.

### S2 (Must): Fix the CFM/RF Comparison (Issue 2)
**Action:** Either (a) use KDE with bandwidth selection to convert CFM/RF particles to densities, report KDE bandwidth and sensitivity, and re-compute L1 errors, or (b) convert all methods to sample-based comparison (GeONet density → particles via importance sampling) and use sliced Wasserstein distance, or (c) add Meta OT [Amos et al., 2023] as a baseline that also outputs OT plans directly. Remove or soften the claim that "GeONet is the only framework... which encapsulates the geodesic behavior."

**Location:** Page 8 - Section 4.2, Table 3

**Expected benefit:** Restores fairness to the baseline comparison and strengthens the paper's claims.

### S3 (Must): Strengthen or Reframe the MNIST Experiment (Issue 3)
**Action:** Add three analyses to the MNIST experiment:
(1) Report the autoencoder's reconstruction error (MSE/PSNR) to quantify geometric distortion.
(2) Decompose the ambient-space error into autoencoder error + GeONet approximation error.
(3) Show decoded geodesic images at all five time points for at least 6 representative digit pairs in a figure (not just the encoded space geodesics).
(4) If errors remain high (~60%+), reframe the experiment as a preliminary proof-of-concept with a call for future work on OT-preserving autoencoders.

**Location:** Page 8-9 - Section 4.3, Table 4

**Expected benefit:** Prevents overclaiming and provides readers with a clear understanding of where the method currently stands on real data.

### S4 (Should): Analyze Loss Formulation Stability (Issue 4)
**Action:** Add an ablation/analysis subsection (e.g., Section 4.2 or 4.6) that:
(1) Plots Lcty and LHJ training curves separately to show both PDE residuals decrease.
(2) Specifies how loss weights α₁, α₂, β₀, β₁ were selected (grid search, adaptive loss balancing [Wang et al., 2021], or fixed).
(3) Adds a positivity penalty or softplus activation on Cϕ's output.
(4) Tests on a synthetic problem with known closed-form geodesic (e.g., two Gaussians with known displacement interpolation) to verify the coupled PDE training converges to the correct solution.

**Location:** Page 5 - Section 3, Eqs. (15)-(16)

**Expected benefit:** Addresses training reproducibility and strengthens the methodological foundation.

### S5 (Should): Consolidate Experimental Parameters in Main Text
**Action:** Add a short "Experimental Setup" subsection at the beginning of Section 4 that lists in a compact table: n (training pairs), m (input grid resolution), p (DeepONet width), number of layers, optimizer, learning rate, training iterations, loss weights (α₁, α₂, β₀, β₁), hardware used, and wall-clock training time.

**Location:** Page 7 - before Section 4.1

**Expected benefit:** Makes the paper self-contained and reproducible without appendix navigation.

### S6 (Should): Tighten the Runtime Terminology
**Action:** Replace "orders of magnitude" in the abstract with a bounded claim: "[GeONet] achieves comparable testing accuracy to standard OT solvers on Gaussian mixture benchmarks, while reducing per-pair inference cost by 10-100× on fine grids when POT is run with loose tolerance; the speed-accuracy trade-off depends on the application." Add similar bounded language in the conclusion.

**Location:** Page 1 - Abstract; Page 9 - Section 4.4

**Expected benefit:** Prevents overclaiming and sets reader expectations appropriately.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows the structure: (1) OT overview and applications, (2) limitations of classical/ML OT solvers, (3) neural operators as a solution paradigm, (4) contribution list. The main weaknesses are: (a) the specific research gap (no existing method learns the geodesic operator across distribution pairs) is not clearly stated before the contribution paragraph, (b) the motivation for "operator learning" specifically (rather than another ML approach) is underdeveloped, (c) the contribution paragraph mixes multiple claims without a clear hierarchy.

### Abstract Outline (Revised — 5 sentences)

**S1 (Problem + Domain):** "Computing the Wasserstein geodesic between probability distributions typically requires solving a costly optimization problem per input pair, limiting its use in online and large-scale settings."

**S2 (Prior Gap):** "Existing amortized ML methods for optimal transport focus on static maps or single-pair geodesics, and do not learn a mapping from input distribution pairs to the full geodesic flow that generalizes to unseen pairs."

**S3 (Proposed Method):** "We propose GeONet, a neural operator that learns the mapping (µ₀, µ₁) → {µₜ} by enforcing the primal-dual optimality conditions of the dynamic OT problem — a coupled continuity/Hamilton-Jacobi PDE system — as physics-informed losses, requiring only the endpoint distributions for training."

**S4 (Key Results):** "On Gaussian mixture benchmarks, GeONet achieves L1 errors of 5-8% against reference geodesics computed by standard solvers, while reducing per-pair inference time by orders of magnitude on fine grids."

**S5 (Bounded Implication):** "The results demonstrate that amortized geodesic prediction is feasible for low-dimensional distributions; extension to higher-dimensional data remains an open challenge."

### Introduction Outline (Revised — 4 paragraphs)

**P1 (Big Picture + Gap):** 
*Role:* Establish Wasserstein geodesic as a useful but computationally expensive tool.
*Key claim:* Current OT solvers require per-pair recomputation.
*Transition:* "This per-pair cost becomes prohibitive when many geodesics are needed, motivating a fundamentally different approach."
*Evidence anchors:* Wasserstein-GAN, domain adaptation, Benamou-Brenier formulation.

**P2 (Prior Work Limitations):**
*Role:* Show that existing methods (classical solvers, entropic OT, ML geodesic methods) all share the limitation of per-pair computation.
*Key claim:* None learn a generalizable mapping from distribution pairs to geodesics.
*Transition:* "We therefore recast the problem as learning an operator between function spaces."
*Evidence anchors:* Hungarian method, Sinkhorn, Liu et al. 2021, Pooladian et al. 2023.

**P3 (Neural Operator Solution):**
*Role:* Explain why operator learning is the natural framework and how GeONet realizes it.
*Key claim:* DeepONet-style architecture with physics-informed primal-dual PDE losses enables geodesic learning from only boundary data.
*Transition:* "Our key idea is to train two coupled neural operators to satisfy the KKT conditions of the Benamou-Brenier problem."
*Evidence anchors:* DeepONet, PINO, KKT system (7).

**P4 (Contributions + Paper Roadmap):**
*Role:* State 3 contributions clearly and bounded.
*Key claims:* (C1) Physics-informed operator for geodesic without true geodesic data, (C2) mesh-invariant output, (C3) amortized inference speedup.
*Transition:* "The remainder of the paper is organized as follows..."
*Bounding note:* Replace "zero-shot super-resolution" with "mesh-invariant output resolution" and bound the speed claim.

### Selected Best Storyline: Option A (Problem → Gap → Solution → Evidence → Contribution)

I recommend the above 4-paragraph structure (Option A) because it:
1. Aligns problem (per-pair cost) directly with solution (operator learning amortization).
2. Clarifies why existing ML geodesic methods (Liu et al., 2021; Pooladian et al., 2023) are insufficient — they also solve per-pair problems.
3. Makes the operator learning motivation explicit: geodesic is a function-to-function mapping.
4. Bounds contributions to what is actually demonstrated.

## Priority Revision Plan
### P0 (Before Resubmission — Must Address)

| Priority | Action | Effort | Impact | Location |
|----------|--------|--------|--------|----------|
| P0.1 | Fix runtime comparison: plot POT error vs. threshold, compare at matched accuracy | Medium | Critical — core value claim | Section 4.4, Figure 6 |
| P0.2 | Fix CFM/RF comparison: add KDE conversion or use sample-space metrics | Medium | High — fairness of baseline eval | Section 4.2, Table 3 |
| P0.3 | Add autoencoder distortion analysis to MNIST; reframe claims if errors remain high | Medium | High — prevents overclaim | Section 4.3, Table 4 |
| P0.4 | Bound runtime claim in abstract and conclusion | Low | High — prevents overclaim | Abstract, Conclusion |

### P1 (Should Address for Strong Rebuttal)

| Priority | Action | Effort | Impact | Location |
|----------|--------|--------|--------|----------|
| P1.1 | Add positivity constraint (softplus) on Cϕ output | Low | Medium — training stability | Section 3, Eq. (12) |
| P1.2 | Report separate training curves for Lcty and LHJ | Low | Medium — training reproducibility | Section 3 or Appendix |
| P1.3 | Specify loss weight selection (α₁, α₂, β₀, β₁) | Low | Medium — methodology clarity | Section 3, Eq. (14)-(17) |
| P1.4 | Add experimental setup table in main text (m, n, p, optimizer, etc.) | Low | Medium — reproducibility | Section 4 intro |
| P1.5 | Test on synthetic known-geodesic problem for convergence validation | Medium | High — validates PDE coupling | Section 4.1 or Appendix |

### P2 (Nice-to-Have for Next Revision)

| Priority | Action | Effort | Impact | Location |
|----------|--------|--------|--------|----------|
| P2.1 | Restructure introduction narrative per revised outline | Medium | Medium — readability | Section 1 |
| P2.2 | Add amortized OT baselines (Meta OT) to comparison | High | Medium — completeness | Section 4.2 |
| P2.3 | Replace "zero-shot super-resolution" with "mesh-invariant output resolution" | Low | Low — terminology precision | Section 1, 4.1 |
| P2.4 | Add multi-seed results for all experiments | Low | Medium — statistical rigor | Section 4 |
| P2.5 | Clarify collocation procedure notation (N for pairs vs. collocation points) | Low | Low — clarity | Section 3 |

### Expected Outcome After P0+P1 Revisions

After addressing P0 and P1 items, the paper would have:
- A defensible runtime comparison with matched accuracy
- Fair baselines with appropriate output modality conversion
- Bounded claims that match the experimental evidence
- Reproducible experimental specifications in the main text
- Validated training stability with PDE residual monitoring
- A more focused narrative with a clear problem-gap-solution structure

This would strengthen the paper from a borderline submission to a solid acceptance candidate at a top venue.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|----------------|-------------------|
| E1 | 1D Gaussian mixture geodesic | Univariate GMMs, identity/random/OOD pairs | L1 error vs. POT at 5 time points | L1 ~3-6% (in-distribution), ~12-16% (OOD) | C1: accuracy on 1D densities | Training params deferred to appendix |
| E2 | 2D Gaussian mixture geodesic | Bivariate GMMs, identity/random/OOD/high-res | L1 error vs. POT at 5 time points | L1 ~6-8% (in-distribution), ~7-8% (OOD) | C1: accuracy on 2D densities | OOD error only slightly above random — unclear if OOD is truly out-of-distribution |
| E3 | High-resolution (super-res) geodesic | Higher grid resolution than training | L1 error vs. POT at finer grid | 1D: ~5-6%, 2D: ~6-8% | C2: mesh-invariant output | Training/test resolution gap not clearly specified in main text |
| E4 | Point cloud geodesic | 2D Gaussian particles → empirical densities | L1 error vs. POT | GeONet: ~23-30%, CFM: ~76-112%, RF: ~91-112% | C1: handles discrete data | Asymmetric comparison (density vs. particles); CFM/RF not designed for geodesics |
| E5 | MNIST geodesic (encoded space) | MNIST → autoencoder (32-dim latent) → GeONet | L1 error in encoded and ambient space | Encoded: ~1-3%, Ambient: ~25-68% | C3: real-data applicability | Latent-space geodesic ≠ image-space geodesic; very high ambient errors |
| E6 | Runtime comparison | POT vs. GeONet on 1D/2D grids | Wall-clock time vs. grid size | GeONet faster by orders of magnitude on fine grids | C3: amortized speedup | POT tolerance very loose (10.0 for 2D); accuracy not matched |

### Research-Theme Gap Diagnosis

1. **New Knowledge (partially addressed):** The paper introduces a novel formulation (operator learning for Wasserstein geodesic) but does not validate it on problems that cannot be solved by existing methods. All benchmarks have accessible POT references. To demonstrate new knowledge, the paper should show a problem where POT is infeasible (e.g., high resolution in 3D) and GeONet still produces a reasonable geodesic.

2. **Reproducibility/Reusability (weak):** The training procedure relies on many hyperparameters (loss weights, architecture sizes, collocation schedule) that are deferred to appendices. Without a clear specification of these choices in the main text, independent replication is unnecessarily difficult.

3. **Impact on Practice/Understanding (unclear):** The claimed speed advantage is the primary practical value. However, the unfair POT comparison (threshold 10.0) and the asymmetric CFM/RF comparison leave the magnitude of this advantage unclear. For practitioners considering GeONet, the key question — "how much faster for the same accuracy?" — remains unanswered.

### Proposed Research Experiments

**P0 Experiment — Matched-Accuracy Runtime Comparison**
- **Target Claim:** C3 (amortized inference speedup)
- **Hypothesis:** GeONet provides meaningful speedup at matched accuracy, but the margin depends on grid size and accuracy requirements.
- **Minimal Design:** Compute POT geodesics at 5 tolerance levels (0.01, 0.1, 1.0, 5.0, 10.0) on the same test pairs used in Figure 6. For each tolerance, compute L1 error vs. a high-accuracy POT reference (tolerance=0.001). Identify the tolerance where POT error matches GeONet's error. Plot runtime vs. grid size at this matched-accuracy point.
- **Controls:** Same test pairs, same hardware, same grid sizes.
- **Success Criterion:** GeONet is faster at matched accuracy for fine grids (≥200 points per dimension).
- **Estimated Cost/Time:** 1-2 days of computation.
- **Expected Gain:** Critical — validates or bounds the core practical claim.

**P1 Experiment — Synthetic Known-Geodesic Validation**
- **Target Claim:** C1 (PDE-coupled learning converges to true geodesic)
- **Hypothesis:** When the true geodesic between two Gaussian distributions is known in closed form (Wasserstein displacement interpolation), GeONet should recover it within the numerical error of the PDE residual discretization.
- **Minimal Design:** Train GeONet on pairs of Gaussian distributions with known displacement interpolation. Compare predicted geodesic to closed-form solution at 5 time points using L1, L2, and Wasserstein-2 distance.
- **Controls:** Same training parameters, compare against POT at fine resolution.
- **Success Criterion:** L1 error < 2% for the Gaussian-to-Gaussian case.
- **Estimated Cost/Time:** 1 day.
- **Expected Gain:** High — validates the mathematical foundation of the method.

**P2 Experiment — Ablation: Loss Weight Sensitivity**
- **Target Claim:** C1 (training formulation robustness)
- **Hypothesis:** The method is robust to a range of loss weight ratios (α₁/α₂, β₀/β₁) if both PDE residuals are monitored.
- **Minimal Design:** Run GeONet with 5 configurations of (α₁, α₂, β₀, β₁): (1,1,1,1), (10,1,1,1), (1,10,1,1), (1,1,10,10), (adaptive balancing). Report final L1 error and PDE residuals for each configuration.
- **Controls:** Same training data and architecture.
- **Success Criterion:** L1 error varies by less than 2% across configurations, or the optimal configuration is clearly identifiable.
- **Estimated Cost/Time:** 2-3 days.
- **Expected Gain:** Medium — improves reproducibility and provides practical guidance for users.

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Must): Matched-Accuracy Runtime Comparison
  ├── Compute POT at 5 tolerances (0.01 to 10.0)
  ├── Match error level with GeONet
  ├── Plot runtime at matched accuracy
  └── Bound speed claim accordingly

P1 (Should): Synthetic Known-Geodesic Validation
  ├── Select Gaussian pairs with closed-form geodesic
  ├── Train GeONet → predict geodesic
  ├── Compare against displacement interpolation
  └── Report L1/L2/W2 errors

P2 (Nice-to-Have): Loss Weight Sensitivity Ablation
  ├── Run 5 configurations of (α₁,α₂,β₀,β₁)
  ├── Compare final error and PDE residuals
  └── Provide practical weight selection guidance
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5/10**

**Rationale:** The paper presents a conceptually novel and well-motivated formulation connecting neural operators to Wasserstein geodesic computation. The core idea (learning the coupled PDE optimality conditions without geodesic supervision) is elegant. However, the experimental evaluation has significant methodological weaknesses that undermine the central claims. The runtime comparison uses an unjustifiably loose POT tolerance (10.0 for 2D), the baseline comparison against CFM/RF is methodologically asymmetric, and the MNIST real-data experiment shows ambient errors too high (up to 68%) to support the claim of successful real-data application. Additionally, the loss formulation's training stability and positivity constraints are unexamined, and key experimental parameters are deferred to appendices rather than presented in the main text. Novelty and comparison conclusions are deferred as external literature verification was unavailable in this run.

**Post-Revision Target: [6.5, 7.5]/10**

**Rationale:** After addressing P0 items (matched-accuracy runtime comparison, fair baseline comparison, MNIST reframing/analysis, bounded claims) and P1 items (positivity constraint, training curves, loss weight specification, reproducibility details), the paper would have a defensible empirical foundation. The remaining limitations (input-mesh dependence, curse-of-dimensionality in branch input, lack of theoretical generalization bounds) are inherent to the current approach but do not invalidate the core contribution. The post-revision score reflects a solid paper with clear contributions and honest limitations, suitable for a top conference in machine learning or computational mathematics.

---

### ASCII Diagrams

```text
ASCII Diagram — Paper Structure & Evidence Map

[Problem: OT geodesic requires per-pair recomputation]
    |
    v
[Gap: No existing method learns geodesic operator across pairs]
    |
    v
[Solution: GeONet — primal-dual PDE neural operator]
    |
    ├── C1: Physics-informed learning w/o geodesic data
    │       Evidence: Table 2 (Gaussian mixtures, L1 ~3-8%)
    │       Gap: No synthetic known-geodesic validation
    │
    ├── C2: Mesh-invariant output / super-resolution
    │       Evidence: Table 2 high-res rows (~4.8-7.9%)
    │       Gap: Input still mesh-dependent (fixed grid)
    │
    └── C3: Amortized inference speedup
            Evidence: Figure 6 (runtime vs. POT)
            Gap: POT tolerance too loose (10.0 for 2D)
    |
    v
[Weaknesses cluster]
    ├── Unfair POT comparison (tolerance 10.0 for 2D)
    ├── Asymmetric CFM/RF baseline (density vs. particles)
    ├── MNIST ambient error too high (68% at midpoint)
    └── Coupled PDE training stability unexamined
```

```text
ASCII Diagram — Revision Strategy Roadmap

[Problem: Claims not fully supported by evidence]
    |
    ├── Core value (speed) unverified
    │   └── Fix: Matched-accuracy runtime comparison (P0.1)
    │       └── Expected: Bounded, defensible speed claim
    │
    ├── Baseline comparison unfair
    │   └── Fix: KDE conversion or sample-space metrics (P0.2)
    │       └── Expected: Fair evaluation, stronger claims
    │
    ├── Real-data evidence weak
    │   └── Fix: Autoencoder analysis + reframing (P0.3)
    │       └── Expected: Honest assessment of limitations
    │
    ├── Training stability unclear
    │   └── Fix: Positivity constraint + loss curves (P1.1-1.2)
    │       └── Expected: Reproducible, stable training
    │
    └── Reproducibility insufficient
        └── Fix: Experimental setup table (P1.4)
            └── Expected: Self-contained main text
    |
    v
[Target: Paper with defensible claims, fair baselines, reproducible results]
```

```text
ASCII Diagram — Related-Work Taxonomy Tree (Layered)

Wasserstein Geodesic / OT Methods (Root)
├── Branch 1: Classical OT Solvers
│   ├── Leaf 1.1: Monge-Kantorovich (Hungarian, auction, simplex)
│   │   [Kuhn 1955; Bertsekas 1989; Luenberger 2015]
│   └── Leaf 1.2: Entropic Regularization (Sinkhorn)
│       [Cuturi 2013; Benamou et al. 2015; Altschuler et al. 2017]
│
├── Branch 2: ML-based Geodesic Methods
│   ├── Leaf 2.1: Per-pair geodesic solvers
│   │   [Liu et al. 2021, 2023; Pooladian et al. 2023; Tong et al. 2023]
│   └── Leaf 2.2: Amortized static OT maps
│       [Lacombe et al. 2023; Amos et al. 2023]
│
├── Branch 3: Neural Operators for PDEs
│   ├── Leaf 3.1: DeepONet family
│   │   [Lu et al. 2021; Tan and Chen 2022]
│   ├── Leaf 3.2: Fourier Neural Operators
│   │   [Li et al. 2020b]
│   └── Leaf 3.3: Physics-Informed Neural Operators (PINOs)
│       [Raissi et al. 2019; Li et al. 2021]
│
└── Branch 4: THIS PAPER — GeONet
    └── Neural Operator for OT Dynamics (primal-dual PDE coupling)
        [Novelty verification deferred — external literature search unavailable]
        Value contribution: First neural operator to learn Wasserstein geodesic
        from boundary pairs only, with mesh-invariant output and amortized inference
```

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Notes |
|------|-----------------|----------------|-------|
| 1 | 3 | Covered | Abstract + Introduction P1, P2 |
| 2 | 2 | Covered | Motivation paragraph, Contribution paragraph |
| 3 | 1 | Covered | Lagrangian derivation and KKT system |
| 4 | 1 | Covered | Neural operator background + Eq. (9) notation |
| 5 | 1 | Covered | Loss function formulation (Eq. 14-17) |
| 6 | 1 | Covered | Collocation training procedure |
| 7 | 1 | Covered | Gaussian mixture experiment setup |
| 8 | 1 | Covered | Point cloud comparison (Table 3) |
| 9 | 3 | Covered | MNIST results, Runtime comparison, Limitations |
| 10-13 | 0 | Skipped (references only) | No substantive content to annotate |

**Skipped paragraphs justification:** Pages 10-13 contain only the References section (bibliography entries). These are non-substantive for review purposes.