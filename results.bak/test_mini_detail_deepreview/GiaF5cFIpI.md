Now I have enough information. Let me produce the final consolidated review.

## Summary

This paper proposes a streaming framework for adaptive stimulation-response modeling of latent neural dynamics. It integrates three components: (1) streaming latent space construction including a novel streaming jPCA (sjPCA) with Orthogonal Procrustes stabilization, (2) a nonparametric kernel-regression model for the stimulus-response mapping that can handle nonstationarity via a time feature, and (3) a constrained optimization procedure for designing high-dimensional neural stimulation patterns to drive low-dimensional latent dynamics in a desired direction. The approach is evaluated on a toy circular dynamical system and two real neural datasets (calcium imaging from mouse visual cortex, electrophysiology from nonhuman primate sensorimotor cortex) with simulated stimulations, and demonstrates sub-100ms end-to-end runtime.

## Strengths

- **Novel streaming jPCA with Orthogonal Procrustes stabilization (Section 2.1, Equations 1–2, Figure 1a):** The sjPCA algorithm introduces a Sherman-Morrison update for online skew-symmetric matrix estimation and a novel per-plane Procrustes step to stabilize the identified rotational subspaces over time. Figure 1a shows convergence to the offline fit within a few seconds on a simulated circular system, which is a genuine algorithmic contribution over non-streaming jPCA (Churchland et al., 2012).

- **Nonparametric stimulus-response model that handles nonstationarity (Section 2.3, Equation 7, Figure 2e):** The product-kernel regression includes a time feature K₃(t, Tᵢ) that enables discounting old samples. Figure 2e demonstrates recovery after a 180° flip (within ~15s) and adaptation during continuous drift — an explicit handling of nonstationarity that prior stimulus-response models (typically assuming a fixed mapping) do not provide.

- **Constrained optimization for high-dimensional stimulation design (Section 2.4, Equation 8, Figure 4a):** The formulation jointly enforces nonnegativity, an L₁ sparsity surrogate, and box constraints, and is differentiable through the learned Ŝ. Figure 4a shows designed stimuli achieve significantly smaller angles between desired and observed latent responses compared to random baselines. This addresses a genuinely difficult search problem (10⁴⁵+ combinations).

- **Verified real-time runtime (Section 3):** The paper reports end-to-end runtimes averaging under 10ms and always below 100ms per timepoint, which is a concrete and important practical demonstration for closed-loop in vivo use.

- **Validation on two distinct real neural recording modalities (Sections 3 & 4.1, Figure 3):** The method is tested on both slow-rate (15 Hz calcium imaging, 592 neurons) and fast-rate (30 Hz electrophysiology, 130 units) data with realistic dynamics, showing the framework's flexibility across experimental preparations.

## Weaknesses

### Major

- **The high-dimensional kernel regression is not viable as described for the claimed data regime.** The stimulus-response estimator in Equation (7) uses a product of RBF kernels on the latent state x (low-dimensional, k~3–10), the stimulation vector u (N ≥ 130 for electrophysiology, N = 592 for calcium data), and time t. The paper claims to learn this mapping from "roughly 10–20 total stimulations" (Introduction). In a space of dimension >100, RBF kernel distances with 10–20 training points become nearly uniform — all pairwise distances converge to a constant, rendering K₂(u, Uᵢ) essentially uninformative. This means the model cannot learn stimulus-specific effects; the weighting reduces to being driven primarily by x and t, which alone cannot capture the stimulus-response mapping the paper claims. The paper provides no regularization analysis, no discussion of how kernel length scales are set for the u component, and no ablation showing that u actually contributes to predictions. The toy model (where this is tested) uses a 3D latent space with binary u, so the high-dimensional issue never arises in the central evidence.

- **All "real data" experiments use simulated (synthetic) stimulations, not real ones.** The paper states (Section 4.1): "For each of the real datasets, we simulated stimulations using an autoregressive function." This means the stimulus-response map Ŝ is never tested against genuine biological variability — opsin expression heterogeneity, state-dependent nonlinearities, or the nonstationarities that motivated the temporal kernel. The "real" component only provides background neural activity; the stimulus-response relationship is entirely synthetic. While the paper acknowledges this in the Discussion, the central claim of having developed a method that "learns stimulus-response mappings" is not validated under realistic conditions.

- **Baselines are too weak to support the claimed superiority.** The only comparator for stimulus-response modeling is a "blind" model that ignores stimulation entirely (Figures 2e, 3c) — this merely shows that modeling stimulation is better than not modeling it. For optimization, the comparison is against random single-neuron, random multi-neuron, and shuffled stimuli (Figure 4a). No comparison is made to Bayesian optimization (Minai et al., 2024, cited in the paper), active learning (Wagenmaker et al., 2024), or any other adaptive stimulation method. The evidence therefore does not establish that the proposed approach outperforms existing alternatives.

- **The optimization algorithm for stimulus design is underspecified.** Equation (8) defines a non-convex objective (cosine alignment + L₁ penalty) over a box domain with dimension N ≥ 130. Algorithm 1 says "Solve with box constraints" (line 19) but provides no detail on the solver, initialization strategy, gradient computation, convergence criteria, or handling of local optima. A runtime of "<10 ms on average" (claimed in the Introduction) for optimizing over hundreds of variables is hard to evaluate without specifying the algorithm. The gradient through the kernel regression (Equation 7) involves backpropagating through RBF derivatives summed over all training points — the paper does not explain how this is computed efficiently for real-time use.

- **The open-loop optimization experiments (Section 4.2, Figure 4) assume the stimulus-response mapping S is known and linear (S(u) = Qᵀu).** This removes the need to learn Ŝ entirely, which is the paper's central claimed contribution. The closed-loop results (Figure 5) use a non-trivial S but only on the toy model. The paper lacks a clean demonstration where Ŝ is learned and used for optimization on a realistic high-dimensional setup.

### Minor

- **sjPCA is only validated on a simulated circular system** (Figure 1a). The claim of convergence to an offline jPCA fit needs experimental support on real neural data with known rotational structure (e.g., preparatory reaching activity). Without this, it is unclear whether sjPCA works in practice.

- **Several components are described but never used or evaluated.** Three dynamical models are listed (KF, VJF, Bubblewrap) but only KF is actually used. The "adaptive switching between spaces" (Figure 1c, claimed in Section 2.2) is shown as a post-hoc heatmap but never demonstrated in an actual stimulation experiment. The delayed-response model and β coefficients (Section 2.3) are described but their effect is not evaluated.

- **No sensitivity analysis of key hyperparameters** (kernel length scales, penalty weight λ₁, maximum allowed non-zero elements ‖u‖₀^max). The results may depend critically on these values, and they are not reported.

- **The streaming jPCA description is sketchy.** How Ẋ is computed incrementally (needed for Equation 1) is not explained, and the cost of the per-time-step Orthogonal Procrustes solve (Equation 2) is not discussed.

### Trivial

- The notation ‖u‖₀^max in Equation (8) is used but never formally defined.

- Figure captions in the extracted text are duplicated and difficult to parse (parser artifact, not author error).

## Nice-to-Haves

- Replace or augment the high-dimensional kernel regression with a structured model that respects the dimensionality — e.g., assume the effect of u is linear in a low-rank projection, or use a sparse additive model. The current approach cannot learn meaningful stimulus-specific effects with 10–20 samples in >100 dimensions.
- Compare against at least one existing adaptive stimulation method (Bayesian optimization, active learning) under the same simulated conditions.
- Validate sjPCA on real neural data with known rotational structure against an offline jPCA fit.
- Test the full closed-loop pipeline (learned Ŝ + optimization) on a high-dimensional setup, not just the toy model.

## Removed Points

- **Criticism of missing reproducibility details (specific solver, hyperparameters, coordinate descent steps):** Partially valid but these details commonly appear in the supplementary appendix (which is stripped by the parser). The paper commits to code release (Section 7), so algorithmic reproducibility is achievable. Downgraded from Major to Minor or moved here.
- **"The paper provides no analysis of computational scalability of kernel regression":** The paper reports <10ms average runtime. For a streaming method, this concrete measurement is more informative than asymptotic analysis. Removed as a procedural complaint that the paper already addresses empirically.
- **Criticism that "only KF is used" from the strength finder:** The paper states "see Appendix C for comparison across all models" (Section 4.1), suggesting additional analysis exists in the stripped appendix. This is a parser limitation, not an author omission.
- **No ethics concerns about real stimulations:** Removed — speculative and not grounded in the paper as presented.
- **Strength about "reproducibility commitment":** Generic; code release commitments are standard, not a distinguishing strength. Moved here.
- **Strength about "delayed response model":** Described but never evaluated; a described-but-unvalidated feature is not a strength.

## Novel Insights

None beyond the paper's own contributions. The reviews highlight a genuine structural tension: the paper proposes a method that must learn from high-dimensional stimulation vectors with very few samples via nonparametric regression, but provides no analysis or remedy for the well-known failure mode of RBF kernels in high dimensions. This tension — between the ambition of the framework (which is commendable) and the statistical viability of its core learning component — is the central unresolved issue that the reviews surface but do not resolve.

## Suggestions

1. **Address the high-dimensional kernel regression issue directly.** Demonstrate with a controlled simulation that the u-component of the kernel is actually informative — e.g., by showing that shuffling u entries destroys prediction accuracy, or by comparing against a model that ignores u. Alternatively, adopt a structured model (e.g., linear-in-u with learned low-rank projection) that is statistically viable in the >100-dimension, few-sample regime.

2. **Run the method on data with real (not simulated) stimulations,** even in a reduced preparation. This is the decisive experiment for the paper's central claim. If infeasible, at minimum test on a simulated high-dimensional setup where u is not binary and the number of samples is varied systematically, with error curves showing that Ŝ actually leverages u.

3. **Add at least one meaningful baseline for both the learning and optimization components.** Compare against: (a) a linear regression of s on u (for learning), and (b) Bayesian optimization over u (for optimization). Without these, the paper cannot claim superiority over existing approaches.

4. **Specify the optimization algorithm concretely** — solver, initialization, iterations, and a convergence check (e.g., random restart comparison).

5. **Validate sjPCA on a real neural dataset** with known rotational dynamics (e.g., preparatory reaching) against offline jPCA.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Queried for papers on streaming/closed-loop neural dynamics and stimulation. Weak anchors (score < 3.5): QuantFormer (3.0, Reject), TAVRNN (3.0, Reject), DHTM (3.0, Reject). Middle anchors (3.5–7.5): iSSM (5.0, Reject), closed-loop EEG visual stimulation (5.75, Reject), MR-SDS (5.80, Accept), Parsing neural dynamics rSLDS (6.60, Accept). Strong anchors (> 7.5): Comparing noisy neural dynamics (8.0, Accept), Brain Bandit (8.0, Accept), Learning invariance manifolds (8.0, Accept). **Initial bracket: 3.5–6.0.**

**Round 2 (Narrowing):** Focused on 3.5–5.5 and 5.5–7.0 ranges. Lower-mid anchors: FCCA (4.75, Reject — controllability subspaces, interesting idea but flawed derivation), Nonparametric Covariance Regression (5.25, Reject — limited novelty), iSSM (5.0, Reject — interventional SSMs, similar domain). Upper-mid anchors: Parsing neural dynamics rSLDS (6.60, Accept — strong theory, real data validation).

**Comparison to anchors:**
- *iSSM (5.0, Reject):* Very similar domain (causal modeling of neural dynamics under perturbations). iSSM has a rigorous identifiability proof, tests on two real datasets with *actual* perturbations (photostimulation, microstimulation), and a clearer methodology. The paper under review has a more ambitious framework (streaming + nonparametric S + optimization) but no theoretical guarantees and weaker validation (simulated stimulations only). The paper is weaker than iSSM.
- *FCCA (4.75, Reject):* Interesting control-theoretic framing but serious derivation flaws. The paper under review has a more coherent overall framework but insufficient validation. Comparable quality — both have genuine ideas undermined by execution gaps.
- *Closed-loop EEG visual stimulation (5.75, Reject):* Similar "closed-loop stimulation" framing. That paper had unclear presentation and weak validation of individual components. The paper under review is slightly stronger in terms of algorithmic clarity.
- *Parsing neural dynamics rSLDS (6.60, Accept):* Strong theoretical contribution (infinite states, latent geometry), validated on real neural data with behavioral comparisons. The paper under review lacks comparable theoretical depth or experimental validation.

**Final score:** The paper's core weaknesses — the unaddressed high-dimensional kernel regression issue, simulated-only stimulations, and weak baselines — place it below the iSSM paper (5.0, Reject). The framework is conceptually coherent and addresses an important problem, but the gap between what is claimed and what is demonstrated is too wide for acceptance. Score: **4.0**.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>