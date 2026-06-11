Now I have enough comparison points to calibrate. Let me finalize.

**Round 1 bracket: 4.25 – 5.75**

**Round 2 comparison:**
- **iSSM (5.00)**: causal SSM for neural perturbations, with identifiability proof, tested on real perturbation data. Weaknesses: strong assumptions, weak baselines, low reconstruction. Our paper has similar weak-baseline issues and a sign error in the optimization, but adds real-time streaming and more integrated framework. Comparable or slightly weaker.
- **FCCA (4.75)**: controllability analysis for neural dynamics. Novel idea but significant derivation issues, poor validation. Our paper is better validated but has its own issues.
- **MRINE (4.25)**: real-time multimodal neural decoding. Reviewers found limited novelty — "combination of existing techniques." Our paper has more methodological novelty.

**Final score: 4.5.** The paper has genuine contributions (temporal kernel regression, unified streaming framework, real-time feasibility), but three major weaknesses pull it below acceptance threshold: the optimization formulation has a sign issue that undermines the stated sparsity goal, baselines are trivial (random only), and the adaptive latent-space selection claim in the abstract is entirely unvalidated. These are substantive enough to warrant rejection, but the paper is clearly stronger than the 3.0-3.5 range and has enough novelty to exceed the "assembled from existing parts" criticism that anchored MRINE at 4.25.

## Summary
This paper presents a streaming framework for real-time neural stimulation design that integrates online latent space construction, nonparametric kernel regression for stimulus-response learning, and constrained optimization for selecting high-dimensional stimulation patterns that drive latent dynamics in desired directions. The method is tested on a toy dynamical system and two real neural datasets (calcium imaging, electrophysiology) with simulated stimulations, and runs in <10ms on average.

## Strengths
- **Unified real-time pipeline**: Algorithm 1 provides an end-to-end streaming framework that interleaves latent space updates, dynamics prediction, kernel regression updates, and stimulus optimization. This integration across all components into a single streaming loop is the paper's core architectural contribution.
- **Nonparametric stimulus-response estimator with temporal adaptation**: The kernel regression in Equation 7 simultaneously conditions on latent state, stimulus vector, and sample age. Figure 2e provides compelling evidence that the temporal kernel enables recovery from both a discontinuous flip (180° rotation at t=25s) and continuous drift (1 revolution/30s starting at t=45s) in the stimulus-response mapping. The model substantially outperforms a stimulus-blind baseline during stimulation periods.
- **Constrained optimization operating across high- and low-dimensional spaces**: Equation 8 formulates stimulus design as minimizing angular misalignment between desired and predicted latent perturbation, subject to realistic box constraints [0,1] and an L1-based feasibility term. Figure 4a shows designed stimuli achieve substantially lower angular error than random baselines.
- **Demonstrated real-time feasibility**: The paper reports end-to-end computation <100ms per timepoint, averaging <10ms (Section 3, line 154), faster than data acquisition rates for both modalities tested.
- **Validation on two real datasets from distinct modalities**: Calcium imaging (592 neurons, mouse V1, 15 Hz; Zong et al. 2022) and intracortical electrophysiology (130 units, NHP sensorimotor cortex, 30 Hz; O'Doherty 2024).
- **Closed-loop optimization advantage**: Figure 5b demonstrates that when the stimulus-response mapping is non-trivial, closed-loop optimization using the learned Ŝ produces stimuli with a larger proportion of their magnitude aligned with the target compared to open-loop optimization.

## Weaknesses

### Fatal
None.

### Major
- **Optimization formulation has a sign issue (Eq. 8)**: The penalty term is `λ₁(‖u‖₀ᵐᵃˣ − ‖u‖₁)`. Since `‖u‖₀ᵐᵃˣ` is a constant, minimizing this objective maximizes `‖u‖₁`. Under box constraints [0,1], this pushes all entries toward 1 — the opposite of encouraging sparsity. The paper claims this "encourages a solution with the number of non-zero elements close to n" (line 148-149), but the formulation as written does not encode this. A standard sparsity penalty would use `+λ₁‖u‖₁`. While the angular alignment term may still produce useful solutions in practice, the stated rationale for this term is incorrect, undermining the claimed contribution of the optimization framework.

- **Baselines are too weak to establish practical value**: The optimization experiments (Fig. 4a) compare against stimulating single random neurons, random groups, and shuffled versions of the designed stimulus. The paper cites Bayesian optimization, active learning, and Bayesian variational inference as prior approaches (Section 1) but does not compare against any of them — nor against simple principled alternatives like selecting the k neurons whose latent loading vectors (columns of Q) have the highest inner product with the target direction v. Beating random baselines is a low bar.

- **Adaptive latent-space selection is claimed but unvalidated**: The abstract prominently features "a novel streaming estimator to determine which representation is most predictive of ongoing neural dynamics at any timepoint" enabling "adaptive selection of stimulations to best distinguish amongst neural subspace hypotheses." In the body, this is treated purely descriptively: Figure 1c shows a heatmap of which space was the best predictor at each location, but there is no experiment testing whether adaptive switching between latent spaces actually improves stimulation outcomes, tracking accuracy, or hypothesis discrimination relative to using any single fixed space. A prominently claimed contribution receives no quantitative evaluation.

### Minor
- **Optimization solver is unspecified**: The objective in Eq. 8 embeds `s(u) = Ŝ(x_t, u, t)`, a kernel regression estimate, making it non-convex. The paper mentions leveraging differentiability (line 146) but never names the solver, discusses initialization strategy, or addresses convergence to local minima.

- **Streaming jPCA algorithmic details are missing**: The Sherman-Morrison application to solve Eq. 1 is mentioned (line 73) but not derived — what matrix is being recursively inverted, and how the skew-symmetric constraint `M = −M^⊤` is maintained in the streaming update, is not explained. The Orthogonal Procrustes stabilization (Eq. 2) is clear, but the core streaming mechanism is not.

- **Predictive error aggregation mechanism is unspecified**: Section 2.2 states that predictive error is "aggregated within a local region of the latent space" (line 108-109) but never defines what constitutes a local region or how error is smoothed, despite this underpinning the parallel-space-selection claim.

- **Real-data experiments use only simulated stimulations**: All results on real neural data add an autoregressive perturbation (`a_t = 0.8·a_{t-1} + u_t`) to recorded traces. This sidesteps genuine challenges the method is designed for (opsin expression variability, point-spread function imperfections, network-level recruitment). The paper acknowledges this in the Discussion (line 255-257) but the gap between the simulated-stimulation validation and the "in vivo applications" framing is substantial.

- **The delayed response model is not empirically isolated**: Section 2.3 describes a delayed response model with multiplicative βᵢ coefficients for persistent effects, but no experiment quantifies its benefit over the instantaneous model alone.

### Trivial
- **Figure 5 caption/text inconsistency**: The figure description (line 220) says panel (a) shows "difference between observed and predicted error over 100 stimuli," but the caption (line 222) describes it as showing "lower prediction error on new training samples, confirming the convergence of Ŝ." These describe different quantities.

## Nice-to-Haves
- A systematic closed-loop optimization experiment on the toy model quantifying how optimization quality improves as Ŝ learns over time.
- Comparison across the three dynamical models (KF, VJF, Bubblewrap) rather than reporting only KF results, to ground the claim of model flexibility.
- Testing sjPCA on real neural data to close the loop on that contribution, since all real-data results use proSVD.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **(Harsh Critic) "The gap is not conveyed honestly in the abstract or introduction"**: The abstract states the method is "compatible with future in vivo applications" and the introduction says "We anticipate that our adaptive method will enable the next generation of experiments" — both are forward-looking statements, not claims of having conducted in vivo experiments. The simulated-stimulation limitation is acknowledged in the Discussion. Removed as an overstatement.

- **(Harsh Critic) mmICA tested only on data matching its assumptions**: The paper explicitly states (line 91) that "mmICA is given a 6D system generated with Laplace random variables where the dimensions are jointly independent, to match the algorithm's assumptions." The paper is transparent about this. Removed as a strawman — the paper does not misrepresent this.

- **(Harsh Critic) Convergence metrics not directly comparable across methods**: The paper notes the different error metrics for proSVD/sjPCA (principal angles) vs. mmICA (Frobenius norm of demixing matrix) at lines 92-94, and the convergence plot is per-method. This is acknowledged in the text. Removed.

- **(Harsh Critic) Toy model only perturbs third dimension, making it too simple**: The toy model serves its purpose of testing the adaptive kernel regression. The paper doesn't overclaim from this. Removed as a nitpick.

- **(Harsh Critic) "The blind comparison model is a minimal baseline" for Section 4.1**: The stimulus-blind model is an appropriate baseline for testing whether the learned Ŝ improves prediction during stimulation periods — it isolates the contribution of the stimulus-response model. Removed.

- **(Strength Finder) "Parallel evaluation and adaptive selection across latent representations" as an unqualified strength**: Demoted because the adaptive selection claim is not quantitatively validated (see Major Weakness #3). The parallel evaluation is a framework capability, but the claimed benefit of adaptive switching remains untested.

## Novel Insights
The most interesting aspect of this work is the temporal kernel in Equation 7 that discounts old stimulus-response observations, enabling the model to track non-stationary mappings. Figure 2e's demonstration of recovery from both discontinuous flips and continuous drift is genuinely compelling and suggests that kernel regression with time-aware discounting could be broadly useful for any closed-loop neuroscience application where the stimulus-response function may change over the course of an experiment. This idea — treating sample age as a kernel feature rather than using a fixed-length sliding window — is clever and underappreciated.

## Suggestions
- Fix the sparsity penalty in Eq. 8 to actually encode the intended constraint: if the goal is k nonzero entries near 1, a term like `λ₁|‖u‖₁ − k|` or a simple `+λ₁‖u‖₁` with appropriate λ₁ would be more principled. Alternatively, explain and justify why the current formulation produces the intended behavior despite appearances.
- Add a loading-vector alignment baseline: select the k neurons whose columns in Q have highest absolute inner product with target v. This is simple, principled, and any optimization method should beat it to claim value.
- Either run an experiment showing that adaptive latent-space switching improves a downstream metric, or remove the claim from the abstract and reduce it to a descriptive capability in the body.
- Name the optimization solver, discuss initialization, and report convergence behavior across random restarts.
- Provide the Sherman-Morrison derivation for sjPCA (even if in an appendix) and explain how the skew-symmetric constraint is maintained.

## Calibration Anchor Comparison

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| MRINE (multimodal neural decoding) | 4.25 | R1 | Our paper has more methodological novelty; stronger. |
| FCCA (feedback controllability) | 4.75 | R2 | Similar level of novelty with validation gaps; comparable. |
| iSSM (interventional SSM) | 5.00 | R2 | Has identifiability theory; our paper has more empirical gaps (simulated stimulations, weak baselines). Slightly weaker. |
| Neural Manifold Regularization | 5.50 | R2 | Better validation; our paper weaker. |
| Zebrafish locomotion control | 5.75 | R1 | Better execution, comparable novelty; our paper weaker. |
| BRAID (input-driven neural dynamics) | 6.25 | R1 | Much stronger validation and baselines; our paper clearly weaker. |

**Round 1 bracket**: 4.25–5.75
**Round 2 narrowing**: Paper sits at ~4.5, between FCCA (4.75) and MRINE (4.25). Stronger than MRINE (more novelty) but comparable to FCCA (similar mix of novelty + execution gaps) and below iSSM (5.00, which has stronger theory and real perturbation data).

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>