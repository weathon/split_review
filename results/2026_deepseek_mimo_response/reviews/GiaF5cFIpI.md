Now I have enough calibration data. Let me finalize the review.

**Calibration anchors summary:**

Round 1:
- Low (<3.5): QuantFormer (3.0), TAVRNN (3.0), DHTM (3.0), HyperEEGNet (3.0) — all rejects with limited novelty
- Middle (3.5-7.5): MRINE (4.25, reject), iSSM (5.0, reject), Spectral learning (6.8, reject), HDA (5.0, reject)
- High (>7.5): Causal OT (8.0, accept), Brain Bandit (8.0, accept), Feedback Neural ODEs (8.0, accept), ACSSM (8.0, accept)

Round 2:
- Nonparametric Covariance Regression (5.25, reject)
- MR-SDS (5.80, accept)
- Closed-loop EEG framework (5.75, reject)
- FCCA (4.75, reject)
- Multiregion dynamics (7.33, accept)
- Inverse decision-making (6.00, accept)

**Round-1 bracket: 4.5–6.5.** The paper has more novelty than the 4.x rejects but weaker real-data evaluation than the 6.x+ papers.

**Round-2 narrowing: 5.0–6.0.** The paper is clearly above FCCA (4.75) — it has a more complete system and stronger toy model validation. It's comparable to MR-SDS (5.80, accept) and the closed-loop EEG framework (5.75, reject) in ambition and evaluation quality. The paper's main differentiator from these anchors is the genuine novelty of sjPCA and the integrated streaming pipeline, balanced against the trivially simple stimulation model on real data. I'll place it at **5.5**.

## Summary
This paper proposes a real-time framework for designing neural stimulations that perturb latent neural dynamics in desired directions, integrating streaming dimensionality reduction (including a novel streaming jPCA method), nonparametric kernel regression for adaptive stimulus-response mapping, and a constrained optimization procedure for stimulation design. The method is validated on a toy model and two real neural datasets (calcium imaging, electrophysiology), with real-data stimulations simulated via a simple additive autoregressive process.

## Strengths
- **Novel streaming jPCA (sjPCA)** (Eqs. 1-2, Fig. 1a): The Sherman-Morrison-based streaming implementation of jPCA with per-plane Orthogonal Procrustes stabilization converges quickly to offline solutions, filling a genuine gap since prior jPCA was batch-only. This is a meaningful methodological contribution.
- **Adaptive stimulus-response mapping handles non-stationarities** (Eq. 7, Fig. 2e): The kernel regression estimator with a time kernel recovers within ~15s after a sudden 180° flip and continuously tracks under a rotating mapping, while a non-adaptive "blind" method fails — demonstrating the core adaptive capability on the toy model.
- **Stimulation optimization achieves sub-degree alignment under constraints** (Fig. 4b): 517/600 optimizations for feasible directions achieve <1° misalignment, and 508/600 for the first principal component direction, demonstrating the optimization reliably designs high-dimensional stimuli.
- **Model calibration** (Fig. 4c): For non-Negative targets, fewer than 6% of optimizations had observed error lower than predicted error, demonstrating that predicted error is a trustworthy lower bound.
- **Closed-loop outperforms open-loop for non-trivial maps** (Fig. 5b): Closed-loop stimuli (using learned Ŝ) have larger proportion of magnitude aligned with desired direction v than open-loop stimuli when S is non-trivial, demonstrating the value of adaptive feedback.
- **Real-time feasibility** (Section 3): End-to-end runtimes average <10ms with maximum <100ms per timepoint on commodity hardware.

## Weaknesses

### Fatal
None

### Major
- **Real-data evaluation uses trivially simple simulated stimulations that fail to test the paper's core claims.** The real-data experiments use $y_t = r_t + a_t$, $a_t = 0.8 \cdot a_{t-1} + u_t$ (line 178) — a linear, additive, deterministic, state-independent, time-invariant mapping. The paper's introduction and abstract heavily emphasize nonlinearity, state-dependence, unreliability, and temporal drift as the core challenges ("responses are driven by network structure and the state of the neural system," "we do not assume that the response to stimulation is robust"), but the real-data experiments test none of these properties. The comparison to the "blind" baseline is near-trivial when stimulation effects follow a simple additive AR process. The more interesting evaluations (discontinuity adaptation, rotating maps) appear only on the toy model (Fig. 2e). This is the most significant gap between the paper's claims and its demonstrated capabilities.

- **Closed-loop optimization with non-trivial response mapping demonstrated only on the toy model.** The optimization evaluation in Fig. 4 assumes the open-loop case $S(u) = Q^\top u$ (acknowledged at line 228), where the mapping is trivially linear. The closed-loop optimization using the learned non-trivial Ŝ (Fig. 5) is only demonstrated on the toy model. Thus the claim of "outperforms random methods in designing stimuli that produce our desired latent effects" (line 200) is not demonstrated against a challenging response function on real neural data.

### Minor
- **Multiple latent space switching proposed but not used in stimulation experiments.** Fig. 1c shows predictive probability heatmaps across spaces (proSVD, sjPCA, mmICA), and the abstract claims "adaptive selection of stimulations to best distinguish amongst neural subspace hypotheses." However, all stimulation experiments use a single latent space (proSVD for real data). Demonstrating switching during stimulation would validate this claim.
- **Optimization solver and hyperparameters unspecified.** The paper does not specify the optimizer algorithm used (gradient-based? which one?), the value of λ₁, or how the non-smooth objective is handled. Given the real-time constraint, this affects reproducibility.
- **Kernel regression tuning underspecified.** Bandwidths for RBF kernels are "optionally tuned by stochastic coordinate descent at each new observation" (line 136) with no details on the objective or convergence.
- **Main text real-data results use only KF for dynamics.** The paper claims comparison across dynamical models (KF, VJF, Bubblewrap), but Fig. 3 uses only KF, deferring others to Appendix C.

### Trivial
None

## Nice-to-Haves
- Use realistic simulated stimulation models on real data (state-dependent, unreliable, temporally variable) to stress-test the adaptive capabilities beyond the toy model.
- Demonstrate closed-loop optimization on real neural data with a learned non-trivial Ŝ.
- Show a stimulation experiment where the multiple-latent-space selection actually switches representations.
- Provide runtime breakdown by component (latent space update, kernel regression, optimization solve).

## Removed Points
These points are flagged to be removed, treat them with caution:
- Formatting/style nitpicks — parser artifacts, not paper problems.
- Missing appendix concerns — the parser strips appendices; they exist in the original.
- Concerns about "hardware description being overly specific" — this is a style preference, not a substantive issue.

## Novel Insights
The paper's novel insight is the integration of streaming dimensionality reduction, adaptive nonparametric stimulus-response modeling, and constrained optimization into a single real-time pipeline for neural stimulation design. The streaming jPCA method is a genuine contribution to the field. The kernel regression with time kernel for tracking non-stationary stimulus-response mappings is well-motivated and convincingly validated on the toy model. However, the gap between toy model demonstrations (strong) and real-data demonstrations (trivial stimulation simulation) limits the practical significance of the contribution as currently evaluated.

## Suggestions
- Replace the additive AR stimulation model on real data with more realistic simulations (nonlinear state-dependent effects, unreliable responses, temporal variability) to match the paper's framing about real experimental challenges.
- Extend the closed-loop optimization (Fig. 5) to real neural data with a non-trivial learned Ŝ.
- Specify the optimization solver, λ₁ value, and kernel tuning procedure.
- Demonstrate the multiple-latent-space switching during actual stimulation experiments.

## Score and Decision

**Anchors retrieved:**

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | BBldjKEBlJ (QuantFormer) | 3.0 | Less novelty than our paper; purely forecasting, not stimulation |
| 1 | NPzuN3Rxi8 (TAVRNN) | 3.0 | Graph-based neuronal dynamics; less complete system |
| 1 | fnO5h1CFyh (DHTM) | 3.0 | Temporal memory learning; different domain, less applicable |
| 1 | 04RGjODVj3 (HyperEEGNet) | 3.0 | BCI calibration; narrower contribution |
| 1 | eR1119aUlL (MRINE) | 4.25 | Real-time neural decoding; similar ambition, weaker novelty |
| 1 | FwW3jqchtY (iSSM) | 5.0 | Causal intervention modeling; similar importance, cleaner theory |
| 1 | wCUw8t63vH (Spectral learning) | 6.8 | Strong analytical contribution; more rigorous evaluation |
| 1 | LNp7KW33Cg (HDA) | 5.0 | BCI domain adaptation; less novel |
| 1 | cNmu0hZ4CL (Causal OT) | 8.0 | Novel metric, very well-validated; clearly stronger |
| 1 | RWJX5F5I9g (Brain Bandit) | 8.0 | Biologically grounded theory; clearly stronger |
| 1 | cmfyMV45XO (Feedback Neural ODEs) | 8.0 | Novel architecture with theory; clearly stronger |
| 1 | 8zJRon6k5v (ACSSM) | 8.0 | Amortized control; clearly stronger |
| 2 | PdZkfSttGK (Nonparametric Cov) | 5.25 | Nonparametric neural method; similar level, narrower scope |
| 2 | WQwV7Y8qwa (MR-SDS) | 5.80 | Switching nonlinear dynamics; accepted at 5.8, comparable ambition |
| 2 | 4ltiMYgJo9 (Closed-loop EEG) | 5.75 | Closed-loop stimulation; rejected at 5.75, very relevant |
| 2 | 4AlNpszv66 (FCCA) | 4.75 | Controllability analysis; rejected, our paper has more complete system |
| 2 | LbgIZpSUCe (Multiregion dynamics) | 7.33 | Strong modeling contribution; clearly stronger evaluation |
| 2 | APWIZgehDT (Perceptual boundaries) | 6.0 | Different domain; similar score range |
| 2 | zxO4WuVGns (Inverse decision-making) | 6.0 | Accepted at 6.0; stronger theoretical grounding |

**Round-1 bracket: 4.5–6.5.** Paper has more novelty than 4.x rejects but weaker real-data evaluation than 6.x+ papers.

**Round-2 narrowing: 5.0–6.0.** Paper is above FCCA (4.75, reject) due to more complete system and stronger toy validation. Comparable to MR-SDS (5.80, accept) and Closed-loop EEG (5.75, reject) in ambition. The trivial stimulation model on real data is the key differentiator holding the paper below the 6.0 accept threshold.

**Final score: 5.5.** The paper has genuine methodological contributions (sjPCA, integrated streaming framework) and strong toy model validation, but the real-data evaluation using a trivially simple additive AR stimulation model fails to test the paper's core claims about adapting to nonlinear, state-dependent, and unreliable stimulation effects. This evaluation gap is the primary factor limiting the score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>