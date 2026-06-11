## Summary
This paper proposes an integrated streaming framework for adaptive neural stimulation design, combining a novel streaming jPCA method (sjPCA) for online dimensionality reduction, nonparametric kernel regression for stimulus-response mapping, and constrained optimization for designing high-dimensional stimulation patterns to perturb low-dimensional latent neural dynamics. The framework is validated on a 3D toy model and two real neural datasets (calcium imaging, electrophysiology), with demonstrated end-to-end runtimes averaging <10ms per timestep.

## Strengths
- **Novel sjPCA with Orthogonal Procrustes stabilization**: The streaming jPCA formulation using Sherman-Morrison updates (Equation 1) with a per-plane Orthogonal Procrustes step (Equation 2) is a genuine methodological contribution to online subspace identification. Figure 1a demonstrates convergence to offline jPCA with N=10 runs and standard deviation shading.
- **Nonparametric kernel regression handles non-stationarity**: The three-kernel RBF estimator (Equation 7) with temporal discounting adapts to changing stimulus-response mappings. Figure 2e shows recovery within 15s after a 180° flip and continuous tracking under 1-revolution-per-30s rotation, outperforming a stimulation-blind comparison.
- **Real-time feasibility**: All experiments run under 100ms per timestep, averaging <10ms end-to-end on consumer hardware (Section 3), directly supporting the practical claim of compatibility with in vivo closed-loop experiments at 15–30 Hz.
- **Well-constrained optimization with realistic experimental constraints**: Equation 8 incorporates non-negativity (excitation-only), L₁ sparsity proxy, and box constraints [0,1]. Under open-loop mode, 517/600 "Feasible" and 508/600 "Q₀" target optimizations achieved <1° predicted misalignment (Section 4.2). Predicted error serves as a reliable lower bound on observed error (fewer than 6% exceeded predicted error for non-"Negative" targets).
- **Parallel latent space evaluation**: Running three dimensionality reduction methods and three dynamical models simultaneously with streaming predictive selection (Figure 1c) enables adaptive representation comparison — a novel capability for testing manifold hypotheses.
- **Validation across two neural modalities**: Testing on calcium imaging (592 neurons, 15 Hz) and electrophysiology (130 units, 30 Hz) demonstrates breadth across noise profiles and temporal resolutions.

## Weaknesses

### Fatal
None.

### Major
- **Real-data experiments use a trivially simple simulated stimulation model**: All real-data experiments simulate stimulations via `y_t = r_t + a_t`, `a_t = 0.8·a_{t-1} + u_t` (line 178) — neuron-uniform, state-independent, linear, and additive. This directly contradicts the paper's emphasis that real stimulation responses depend on "network structure and the state of the neural system" (line 112) and may not "involve the neurons that the stimulation intended to target" (line 21). The kernel regression Ŝ is asked to learn a known, trivially simple mapping on real data. The toy model tests more complex S functions (Equation 9 is state-dependent; Fig. 2d–e tests non-stationarity) but only in 3D. The paper's central claim — that this framework handles the complexities of real stimulation — is not supported by the real-data evaluation.

- **Optimization baselines are only random methods**: Figure 4a compares optimized stimuli only to random single-neuron stimulation, random multi-neuron stimulation, and shuffled versions of the optimized stimulus. The introduction cites Bayesian optimization (Minai et al., 2024), active learning (Wagenmaker et al., 2024), and variational inference (Draelos & Pearson, 2020) as existing approaches, but none are implemented. Without at least one non-trivial comparison, the marginal value of the proposed optimization cannot be assessed.

- **Full closed-loop pipeline not tested on real data**: The closed-loop comparison (Fig. 5) — where the learned Ŝ is used for stimulus design — is performed exclusively on the 3D toy model. Real-data experiments (Figs. 3, 4) use only open-loop mode with identity mapping S(u) = Q^T u (lines 228–229). The paper never demonstrates on real neural data the key advantage: using a learned stimulus-response mapping to design better stimulations than the identity mapping.

### Minor
- **No hyperparameter sensitivity analysis**: Kernel bandwidths in Ŝ, the λ₁ sparsity parameter, and the latent dimension k are not systematically analyzed. Practical deployment requires understanding sensitivity to these choices.
- **L₁ approximation quality unanalyzed**: The L₁ proxy for L₀ sparsity (Equation 8) could produce solutions distributing small values across many neurons rather than concentrating activation. The paper acknowledges this is approximate but doesn't characterize the approximation quality.

### Trivial
None.

## Nice-to-Haves
- Use more realistic simulated stimulation models on real data (state-dependent, neuron-specific, non-linear) to bridge the motivation-evaluation gap with minimal effort.
- Add at least one non-trivial optimization baseline (greedy neuron selection, random search with a budget).
- Test the full closed-loop pipeline on real data.
- Scaling analysis of kernel regression cost as neural population size grows.
- Demonstrate that parallel-space selection (Fig. 1c) improves downstream stimulation outcomes.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Results without error bars"** — Partially incorrect. Fig. 1a shows N=10 runs with std shading; Fig. 4 uses violin plots; Fig. 5 shows averages over 10 experiments. Individual demonstrations (Fig. 3c) show single runs, appropriate for demonstration purposes.
- **"Scaling analysis missing"** — Nice-to-have rather than a core flaw. The method is demonstrated at the scale of the target application (130–592 neurons).
- **"Multiple spaces claim unsupported"** — The paper demonstrates this with heatmaps (Fig. 1c) and claims adaptive representation selection, not improved stimulation outcomes.
- **"Kernel regression scalability concerns"** — The paper demonstrates real-time feasibility on the actual datasets, which is the relevant practical metric.

## Novel Insights
The paper's genuinely novel contributions are: (1) the Orthogonal Procrustes stabilization technique for streaming jPCA, a new contribution to online subspace identification that enables real-time rotational subspace tracking; (2) the demonstration that parallel streaming latent space evaluation reveals where different representations are most predictive in real neural data (Fig. 1c), suggesting potential for detecting task-dependent manifold switching; and (3) the finding that predicted stimulation error functions as a reliable lower bound on observed error (<6% of optimizations exceeded predictions for non-infeasible targets), a practically useful property for experimentalists designing stimulation protocols.

## Suggestions
- Use more realistic simulated stimulation models on real data (state-dependent, neuron-specific, non-linear responses) to directly address the main weakness.
- Add at least one non-trivial optimization baseline (e.g., greedy neuron selection or random search with a budget).
- Run the closed-loop pipeline (learned Ŝ + optimization) on real data, not just the toy model.
- Add systematic ablation of key hyperparameters (kernel bandwidths, λ₁, latent dimension k).

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| iSSM | FwW3jqchtY | 5.0 | 1,2 | Causal neural perturbation with SSM; rejected at 5.0. Paper under review has more novelty (sjPCA) but similarly incomplete real-data validation. |
| BRAID | 3usdM1AuI3 | 6.25 | 2 | Input-driven neural dynamics; accepted at 6.25. Comparable novelty, but BRAID has stronger real-data experiments despite unfair comparisons. |
| MR-SDS | WQwV7Y8qwa | 5.80 | 1,2 | State-dependent neural dynamics; accepted at 5.80. Paper under review has more novelty but weaker real-data validation. |
| Spectral learning | wCUw8t63vH | 6.80 | 1,2 | Shared dynamics; rejected at 6.80. Strong methodology rejected due to assumptions and lack of comparisons — similar issues. |
| FCCA | 4AlNpszv66 | 4.75 | 1,2 | Neural controllability; rejected at 4.75. Less novelty than paper under review. |
| Closed-loop EEG | 4ltiMYgJo9 | 5.75 | 1,2 | Closed-loop neural stimulation; rejected at 5.75. Similar topic, high reviewer variance. |
| Control locomotion | MFCjgEOLJT | 5.75 | 1 | Neuroscience control; accepted at 5.75. Less novelty, simpler methodology. |
| Dynamical modeling | eR1119aUlL | 4.25 | 1 | Real-time neural dynamics; rejected. Less complete framework. |
| QuantFormer | BBldjKEBlJ | 3.0 | 1 | Neural forecasting; rejected. Less relevant, lower quality. |
| TAVRNN | NPzuN3Rxi8 | 3.0 | 1 | Neuronal dynamics modeling; rejected. Less relevant. |
| Closed-loop diffusion | PiHGrTTnvb | 3.0 | 1 | Closed-loop control; accepted with high variance. Less relevant. |
| NMR | TVnkjz4MqV | 5.5 | 2 | Neural manifold regularization; rejected. Less novelty. |
| Generalist decoder | ONOe6cAE9I | 5.75 | 2 | Neural decoding; rejected. Different contribution type. |
| BrainPy | AU2gS9ut61 | 5.4 | 2 | Brain simulator; accepted. Different contribution type. |
| Optimal transport | cNmu0hZ4CL | 8.0 | 1 | Neural dynamics comparison; accepted. Higher quality, different scope. |
| Feedback Neural ODEs | cmfyMV45XO | 8.0 | 1 | Feedback for neural dynamics; accepted. Higher quality, different scope. |

**Round 1 bracket:** 5.0–6.5 (between iSSM at 5.0 Reject and spectral learning at 6.80 Reject).  
**Round 2 narrowing:** 5.5–6.25 (above MR-SDS at 5.80 Accept, below BRAID at 6.25 Accept given weaker real-data evaluation).  
**Final score:** 6.0 — The paper has genuine novelty (sjPCA, integrated framework, parallel space evaluation) that places it above the 5.0–5.5 rejected papers, but the evaluation gaps (simulated stimulations on real data, weak baselines, closed-loop only on toy model) prevent it from reaching the 6.25+ range of accepted papers like BRAID that had stronger real-data experiments.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>