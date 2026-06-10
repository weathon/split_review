## Summary

This paper proposes Riemannian Flow Matching (RFM), a framework for training continuous normalizing flows on Riemannian manifolds. The key theoretical contribution is showing that any function satisfying three simple properties (non-negativity, positivity, non-degeneracy) — called a premetric — suffices to define a closed-form conditional vector field that transports a base distribution to a target (Theorem 1). On simple geometries with closed-form geodesics (spheres, tori, hyperbolic spaces), this yields simulation-free training. For general geometries (triangular meshes, manifolds with boundaries), spectral distances (biharmonic, diffusion) enable O(k) evaluation of the premetric after a one-time preprocessing cost. The paper demonstrates results on Earth/climate sphere datasets, protein/RNA torus datasets, and — for the first time — generative modeling on general mesh geometries and maze-shaped manifolds.

## Strengths

- **Clean theoretical framework via premetrics (Theorem 1).** The paper provides a general, mathematically clean method for constructing conditional vector fields on arbitrary Riemannian manifolds: any function satisfying non-negativity, positivity, and non-degeneracy yields a closed-form conditional flow (Equation 8). Theorem 1 proves that this is the minimal-norm solution satisfying the premetric scheduling constraint. This abstraction subsumes the Euclidean Flow Matching case and is the paper's strongest conceptual contribution.

- **First demonstration of continuous-time generative models on general geometries (meshes, manifolds with boundaries).** The paper presents results on triangular meshes (Stanford Bunny, Spot the Cow) and maze-shaped manifolds with boundaries — a genuinely novel capability. Quantitative NLL values are reported for the mesh experiments (Table 4) across multiple k values and spectral distance types, and the visualizations (Figures 5–6) show the model learning structured densities on these geometries.

- **Competitive empirical performance on several real-world datasets.** On the protein/RNA torus datasets (Table 2), RFM achieves the best NLL on 4 of 5 datasets, with a large margin on the 7D RNA dataset (-5.20 vs. next best -3.70). On the sphere datasets (Table 1), RFM wins on Volcano (-7.93 vs. -6.61) and Fire (-1.86 vs. -1.40) with substantial margins. The high-dimensional scaling experiment (Figure 7) shows RFM maintaining stable performance while baselines degrade.

- **Simulation-free on simple geometries with no divergence computation.** As summarized in Table 1 (tab:comparison), RFM is the only method among closely related approaches that simultaneously achieves simulation-free training on simple geometries, has a closed-form target vector field, and does not require divergence computation — avoiding the biased score approximations and expensive SDE simulation of prior Riemannian diffusion models.

## Weaknesses

### Fatal
None.

### Major

- **Maze experiment lacks quantitative evaluation.** The paper's claim about "first successful training of continuous-time deep generative models on … manifolds with non-trivial boundaries" (line 557) is supported only by visual inspection of sample trajectories (Figure 8, labeled fig:maze). No quantitative metric (NLL, Wasserstein distance, coverage, or any density-based measure) is reported. Given that this is presented as a key distinguishing capability (first-of-its-kind), the evidence is insufficient. The community cannot assess whether the model truly learns the target density or whether mass leaks through boundaries.

### Minor

- **Mixed SOTA results on sphere datasets are not discussed.** On Earth/climate sphere data (Table 1), RFM loses on Earthquake (-0.28 vs. -0.40 for Riemannian Diffusion Model) and Flood (0.42 vs. 0.25 for CNF Matching) — i.e., half the sphere datasets. The abstract claims "state-of-the-art performance on many real-world non-Euclidean datasets" and the main text does not discuss these losses or hypothesize why the method underperforms on more dispersed distributions. Acknowledging and analyzing these cases would strengthen the paper's credibility.

- **Mesh experiments lack reference baselines and contextualization.** The NLL values in Table 4 are reported for RFM alone without comparison to any baseline — the paper justifies this by being the first to train on such geometries, which is fair, but the numbers remain uninterpretable without a reference point. What is the NLL of a uniform distribution on these meshes? What about a simple kernel density estimate? The absence of any baseline or reference makes it impossible to gauge the difficulty of the task.

- **Potential circularity in mesh target construction.** The target distributions on meshes are constructed from eigenfunctions of the Laplace-Beltrami operator (following the setup of Moser Flow, Rozen et al. 2021), while the spectral distance premetric is also derived from the same eigen-decomposition. It is not discussed whether this creates any advantage (e.g., the metric may be better suited to representing eigenfunction-based targets than arbitrary real-world densities). While this follows standard practice from prior work, the paper would benefit from acknowledging this limitation.

- **Missing implementation details for general geometries.** The paper does not specify (i) what ODE solver is used to simulate the conditional flow $x_t$ on meshes and mazes, (ii) what step size or tolerance is used, (iii) how the gradient $\nabla \text{dist}(x,x_1)$ of the truncated spectral expansion is computed on discrete meshes, or (iv) how the computational cost of this ODE simulation compares to the training cost. These details matter for reproducibility, especially since the O(k) spectral distance evaluation is highlighted as a key advantage.

### Trivial
None.

## Nice-to-Haves

- **Ablation on the scheduler $\kappa(t)$.** Only $\kappa(t)=1-t$ is used. The theory allows other schedulers; an ablation would show the effect on sample quality and training stability.
- **Computational cost comparison.** A quantitative comparison of preprocessing cost, per-iteration cost, and total training time against Riemannian diffusion models would ground the claimed computational advantages.
- **Reference NLL values on mesh.** Reporting the NLL of a uniform distribution or a simple baseline on the mesh would contextualize the reported numbers.
- **Real-data mesh experiments.** The synthetic eigenfunction-based targets could be complemented with real measured scalar fields on anatomical or geological surfaces, if available, to strengthen the general-geometry evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about the "no bias" claim for finite-k truncated spectral distances being unsubstantiated.** The paper states (line 277) that finite k is sufficient for satisfying the premetric properties, with details deferred to the appendix. Per the review guidelines, criticisms about details deferred to an appendix that was stripped by the parsing process are not evaluated.
- **Criticism that the "simulation-free" framing is potentially misleading.** The paper consistently qualifies this statement with "on simple geometries" throughout (abstract, line 42, line 238, line 374). The distinction between simple and general geometries is made explicit.
- **Criticism about the early framing of "simulation-free" being potentially misleading.** The paper clearly defines simple geometries as those with closed-form geodesics (line 244) and states upfront that general geometries require ODE simulation (abstract, line 42).
- **Strength about "Strong empirical performance on real-world datasets"** — while partially supported, this strength is qualified by the mixed results on sphere datasets noted in weaknesses.

## Novel Insights

None beyond the paper's own contributions. The premetric-based abstraction for conditional flows on manifolds is the genuine novelty; the reviews do not surface an insight that the paper itself does not articulate.

## Suggestions

1. **Add quantitative evaluation to the maze experiment.** Report at minimum the NLL or Wasserstein distance between the learned and target distributions on the maze. This is essential to support the "first demonstration" claim.
2. **Acknowledge and discuss the mixed sphere results.** Add a paragraph explaining why RFM underperforms on Earthquake and Flood (e.g., are these datasets more dispersed, making the premetric schedule less suitable?) and what the limitations reveal.
3. **Provide reference NLL values for the mesh experiments** (uniform distribution baseline) so readers can interpret the reported numbers.
4. **Add implementation details for general geometries:** ODE solver type, step size / tolerance, and how $\nabla \text{dist}$ is computed from the truncated spectral expansion on meshes.
5. **Discuss the potential circularity in mesh target construction** as a limitation, even if briefly, so readers can assess the generality of those results.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>