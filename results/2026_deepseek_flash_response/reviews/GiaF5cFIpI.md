Now I have a clear calibration picture. Let me write the final review.

**Round 1 bracket:** Based on the first calibration pass, the paper clearly sits above the 3.0-band (QuantFormer, TAVRNN) and below the 8.0-band (Comparing noisy neural dynamics, Brain Bandit). The relevant comparison is within the 4.5–7.0 range.

**Round 2 narrowing:** Reading Spectral Learning (6.80, rejected), BRAID (6.25, accepted), Interventional SSM (5.00, rejected), and Closed-loop EEG (5.75, rejected) provides sharper anchors. Our paper has stronger novel components than the iSSM paper but weaker baselines and a more pronounced validation gap than BRAID. It is comparable in structure to Spectral Learning (algorithmic paper with limited comparisons) but with broader scope.

**Final score:** 5.5 — the paper's algorithmic contributions are genuine and well-motivated, but the validation is insufficiently robust for a top venue. The framing overstates what is demonstrated.

---

## Summary

This paper presents a streaming framework for closed-loop neural stimulation design in latent spaces. It integrates three components: (1) streaming latent space construction including a novel streaming jPCA (sjPCA), (2) a nonparametric stimulus-response mapping via kernel regression with a temporal kernel to handle non-stationarity, and (3) a differentiable optimization procedure to design high-dimensional stimulation patterns under realistic constraints (non-negativity, sparsity, box constraints). The framework is evaluated on a toy model and two real neural datasets (calcium imaging, electrophysiology) where stimulation effects are synthetically superimposed.

## Strengths

1. **Novel streaming jPCA with Orthogonal Procrustes stabilization.** Section 2.1 introduces sjPCA, a streaming formulation of jPCA that solves the skew-symmetric optimization incrementally and stabilizes discovered rotational planes. Figure 1a demonstrates convergence to the offline fit within ~1-2 seconds. This enables real-time rotational subspace tracking, previously only available offline (Churchland et al., 2012).

2. **Nonparametric stimulus-response mapping with explicit temporal adaptation.** The kernel regression in Equation (7) uses three product kernels (latent state, stimulation vector, and sample age), where the temporal kernel K₃ allows discounting of old observations. Figure 2e validates this: the model recovers from an abrupt 180° flip within ~15s and tracks continuous drift (1 rev/30s), while a non-adaptive baseline suffers sustained error. This addresses non-stationarity that prior stimulation-response modeling work did not handle.

3. **Optimization framework searching the full high-dimensional space under realistic constraints.** Section 2.4 formulates a differentiable optimization (Equation 8) with box constraints, L₁ sparsity penalty, and non-negativity, operating directly in the N-dimensional neural space to produce a desired perturbation in the k-dimensional latent space. Figure 4a shows optimized stimuli achieve significantly better alignment with target directions than random baselines.

4. **Parallel evaluation across multiple latent representations.** Sections 2.1-2.2 describe running sjPCA, proSVD, and mmICA in parallel, with predictive error tracked to enable adaptive selection of the best representation at any timepoint (Figure 1c).

5. **Demonstrated real-time feasibility.** End-to-end runtimes averaging <10ms and below 100ms on standard workstation hardware (128GB RAM, i9 CPU, 3060 Ti GPU), making the framework compatible with future in vivo closed-loop experiments.

6. **Validation on two distinct neural data modalities.** Tested on both calcium imaging (mouse visual cortex, 15 Hz, 592 neurons) and intracortical electrophysiology (nonhuman primate, 30 Hz, 130 units), demonstrating generality across different temporal resolutions and noise characteristics.

## Weaknesses

### Major

1. **Validation gap between claims and evidence.** The paper's central claim is designing stimulations that perturb latent dynamics, yet all real-data experiments use **simulated** stimulations superimposed on real recordings via a simple AR(1) model (line 178: `a_t = 0.8·a_{t-1} + u_t`). The abstract states "We demonstrate our approach on both simulated and real neural data" — but the stimulations on real data are synthetic effects injected by the authors, not biological responses. The learned Ŝ is fitting a known synthetic model. The Discussion (lines 255-263) lists limitations including offline operation and nonlinear latent spaces but does **not** flag this as a limitation. This does not invalidate the algorithmic contribution — methods papers can reasonably test with simulated effects — but the framing significantly overstates the level of validation. Compare this to iSSM (FwW3jqchtY, avg 5.00, rejected) which was criticized for similar overclaims about real-data validation.

2. **Weak baselines relative to the cited literature.** The experiments compare against only: (a) a "blind" model ignoring stimulation, and (b) random neuron selection (single, multiple, shuffled). The paper's own introduction cites Bayesian optimization (Minai et al., 2024), active learning (Wagenmaker et al., 2024), Bayesian variational inference (Draelos & Pearson, 2020), and input-output dynamical modeling (Yang et al., 2021) as relevant prior work — yet none are used as comparators. Without comparisons to alternative stimulation-design methods, the relative value of the specific design choices (kernel regression, L₁-relaxed optimization) is unsubstantiated. This mirrors a weakness that led to the rejection of both Spectral Learning (6.80, rejected) and iSSM (5.00, rejected).

### Minor

3. **sjPCA is introduced as a contribution but not integrated into the stimulation pipeline.** sjPCA is validated for convergence (Fig 1a) but the real-data stimulation experiments (Figs. 3-5) use proSVD exclusively. The paper never demonstrates that jPCA-based latent spaces improve stimulation design, nor does the parallel latent space comparison (Fig 1c) explicitly inform stimulation selection. This leaves sjPCA as a decorative contribution relative to the paper's main claims.

4. **Underspecified implementation details for a methods paper.** The kernel regression mentions "each scaling constant is optionally tuned by stochastic coordinate descent at each new observation" (line 136) but provides no detail on this procedure or its cost. The O(N) growth of the kernel regression with each new observation is not discussed — no truncation, forgetting mechanism, or computational bound is given despite the method targeting real-time use. The optimization (Equation 8) provides no analysis of convergence properties, initialization strategies, or number of gradient steps needed.

5. **Near-perfect optimization results raise questions about evaluation difficulty.** The "Feasible" and "Q₀" cases achieve 517/600 and 508/600 trials with <1° error (Section 4.2). While this demonstrates the optimization works, such high success rates on the identity mapping (open-loop) case could indicate an underconstrained evaluation — the simple mapping `S(u) = Q^T u` makes the optimization nearly trivial.

6. **No variance or confidence intervals for key comparative claims.** The optimization results report point counts (517/600, 508/600) without measures of variability across independent runs. The runtime claims lack explicit specification of the exact problem dimensions used for the benchmark.

### Trivial

- The "shuffled" baseline is used but the shuffling procedure (permutation of which neurons? of the stimulation values?) is not specified.
- Figure 1 relies heavily on inline text descriptions rather than self-contained captions.

## Nice-to-Haves
- A comparison against at least one alternative method (e.g., Bayesian optimization on the toy model) would substantially strengthen the evaluation and is the most impactful single improvement.
- A discussion of kernel regression memory scaling (whether truncation, windowing, or sparsification is used for long recordings) would be valuable for a method targeting continuous operation.
- An ablation showing the contribution of the temporal kernel vs. a static kernel.

## Removed Points
- "Optimization evaluation conflates prediction and reality" — REMOVED: the dynamics model f is trained independently on non-stimulation data (Algorithm 1, lines 13 vs 10-11), so s_obs = x_t - \hat{x}_t is a standard residual-based approach in system identification, not circular.
- "Runtime benchmarks should be in main text" — REMOVED: the paper states runtimes in Abstract (line 9) and Section 3 (line 154); deferring full benchmarking to supplementary is standard.
- "Missing appendix/proofs" — REMOVED per rules: the appendix is stripped by the parser.
- "Missing related works" — REMOVED per rules.
- Formatting/style nitpicks — REMOVED per rules.
- "No comparison of sjPCA vs proSVD for stimulation task" — MERGED into Weakness 3 above.

## Novel Insights
None beyond the paper's own contributions. The reviews identify the core validation gap and weak baselines but do not surface a non-obvious insight that the authors missed.

## Suggestions
1. Add a comparison against at least one alternative stimulation-design method from the cited literature (Bayesian optimization or active learning) on the toy model. This is the single most impactful improvement.
2. Explicitly acknowledge the simulated-stimulation limitation in the Abstract and Discussion — do not let the framing overstate the validation level.
3. Either demonstrate sjPCA's benefit in the stimulation pipeline (e.g., show that stimulation design improves with jPCA latent spaces vs. PCA spaces) or reposition it as a secondary/standalone contribution.
4. Provide implementation details for kernel regression tuning and discuss memory/computation scaling for long recordings.
5. Report variability measures (error bars, confidence intervals) alongside point counts for optimization results.

## Score and Decision

**Anchors used:**
- QuantFormer (BBldjKEBlJ, avg 3.00, round 1, low band) — Much weaker paper; our paper is clearly stronger.
- Spectral Learning of Shared Dynamics (wCUw8t63vH, avg 6.80, round 1+2, middle band) — Comparable algorithmic ambition; rejected partly due to limited baselines and assumptions. Our paper has a similar profile but broader scope.
- BRAID (3usdM1AuI3, avg 6.25, accepted, round 2) — Stronger validation and baselines; accepted. Our paper's validation is weaker.
- Interventional SSM (FwW3jqchtY, avg 5.00, round 2) — Similar validation gap (real data with perturbations); rejected. Our paper has more components and better evaluation.
- Closed-loop EEG (4ltiMYgJo9, avg 5.75, rejected, round 2) — Similar closed-loop framework; rejected. Comparable quality.
- Dynamical Modeling Real-time (eR1119aUlL, avg 4.25, round 2) — Weaker paper.

**Round 1 bracket:** Between 4.0 and 7.0.
**Round 2 narrowing:** The paper is stronger than iSSM (5.00) and Dynamical Modeling (4.25) but weaker than BRAID (6.25) and Spectral Learning (6.80). It is comparable to Closed-loop EEG (5.75).
**Final position:** 5.5 — genuine algorithmic contributions undermined by a significant validation gap (simulated stimulations masquerading as real validation) and weak baselines.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>