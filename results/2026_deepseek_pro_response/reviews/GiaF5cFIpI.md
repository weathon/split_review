Now I have a clear picture. Let me compile my final calibrated review.

**Bracket from Round 1:** Between 4.5 and 6.5 — above iSSM (5.00) and FCCA (4.75), below the strong-band papers (8.00).

**Round 2 Narrowing:** Compared to iSSM (5.00, similar domain, rejected), our paper has a more complete integrated system but weaker validation (simulated vs. real stimulations). Compared to NMR (5.50, rejected), our paper has broader scope. Compared to MFCjgEOLJT (5.75, accepted), our paper is comparable in novelty depth with a harder problem. Compared to wCUw8t63vH (6.80, rejected), our paper is weaker on theory. 

Our paper lands around **5.5** — comparable to NMR and MFCjgEOLJT, better than iSSM/FCCA, but with distinguishable weaknesses (simulated stimulations, weak baselines, overclaiming) that pull it below the clear-accept threshold.

---

## Summary
This paper presents a streaming framework for real-time, closed-loop design of neural stimulations that perturb latent neural dynamics in targeted directions. The framework integrates (1) streaming latent space construction including a novel sjPCA algorithm, (2) a nonparametric kernel regression estimator \(\hat{S}\) that models stimulus-response mappings as a function of latent state, stimulus, and time, with temporal discounting for non-stationarity, and (3) a constrained optimization problem for designing high-dimensional stimulation patterns under non-negativity and sparsity constraints. The method is evaluated on a toy model and on two real neural datasets (calcium imaging and electrophysiology) with simulated stimulation effects, and demonstrates real-time feasibility (<10ms average, <100ms worst-case).

## Strengths
- **Non-stationarity-adaptive kernel regression for stimulus-response mapping.** The three-kernel estimator \(\hat{S}\) (Equation 7) uses temporal discounting via \(K_3(t, T_i)\) to handle non-stationary stimulus-response relationships. Figure 2e convincingly demonstrates recovery from both an abrupt 180° flip and continuous rotation of the underlying mapping, while the blind comparison model stays at elevated error. This temporal adaptability is a genuinely practical innovation for real experimental conditions where neural responses drift.

- **Constrained optimization produces highly aligned stimulations where feasible, and correctly identifies infeasible targets.** The optimization (Equation 8) with box constraints and L₁-relaxed sparsity achieves <1° misalignment in 517/600 trials for feasible directions and 508/600 for \(Q_0\)-directed stimulations (Figure 4b). The method correctly recognizes infeasible directions (blanket inhibition under non-negativity, blanket excitation under sparsity), producing appropriately high misalignment angles — a non-trivial sanity check that shows the optimization is doing something meaningful rather than blindly forcing a solution.

- **Streaming sjPCA converges rapidly to the offline solution.** Figure 1a shows sjPCA error dropping to near-offline levels within ~20 seconds of simulated data, with the Orthogonal Procrustes stabilization (Equation 2) providing practical per-plane alignment. While the contribution is modest (a streaming wrapper around existing jPCA), it is cleanly executed and serves the pipeline's real-time requirement.

- **Predicted error functions as a calibrated conservative lower bound on observed error.** For feasible targets, fewer than 6% of optimizations produced observed error lower than predicted error (Section 4.2). This property is practically useful: an experimenter can trust the optimization's self-assessment as a conservative estimate before delivering a stimulus.

- **Real-time computational feasibility is demonstrated.** End-to-end runtimes average <10ms per timepoint with worst-case <100ms, which is faster than both the 15Hz (67ms) and 30Hz (33ms) acquisition rates used. The hardware specifications are reported, supporting reproducibility.

## Weaknesses

### Fatal
None.

### Major
- **All real-data experiments use simulated stimulation effects, limiting evidence of real-world utility.** The paper applies an autoregressive model (\(a_t = 0.8 \cdot a_{t-1} + u_t\)) to add artificial stimulation responses onto real neural recordings from mouse V1 and NHP sensorimotor cortex (Section 4.1). While the underlying neural dynamics and the streaming pipeline operate on real data, the stimulation responses themselves are entirely synthetic — a single-parameter decay model that bears little resemblance to the complex, state-dependent, nonlinear effects of real optogenetic or electrical stimulation. The paper acknowledges this in the Discussion ("performed offline, though in a realistic streaming setting") but frames it as a minor caveat. The framework's core promise — enabling real-time closed-loop stimulation experiments — depends on handling actual neural responses to perturbations, which are shaped by network connectivity, opsin expression heterogeneity, point-spread function artifacts, and other biological factors not captured by this simulation. This gap limits how seriously the empirical results can be taken as evidence of real-world utility, though it does not invalidate the methodological contribution for a methods paper.

- **Baselines are weak and provide limited discrimination between alternative approaches.** For response modeling (Section 4.1), the only comparison is against a "blind" model that is identical to the proposed model but not informed of stimulation times — establishing only that modeling stimulations helps over ignoring them, which is a foregone conclusion. For optimization (Section 4.2), comparisons are against random single-neuron stimulation, random multi-neuron stimulation, and shuffled designed patterns — establishing only that optimization beats random selection. The paper cites several alternative approaches to related problems (Yang et al., 2021; Minai et al., 2024; Wagenmaker et al., 2024; Draelos & Pearson, 2020) but compares against none. Without at least one non-trivial baseline (e.g., linear regression for \(\hat{S}\), or a greedy neuron-selection heuristic for optimization), the paper cannot demonstrate that the specific design choices — kernel regression with RBF kernels and the particular constrained optimization formulation — matter relative to simpler alternatives.

- **The claim about "adaptive selection of stimulations to distinguish amongst neural subspace hypotheses" is never demonstrated.** The abstract prominently states this as a contribution: "the opportunity for adaptive selection of stimulations to best distinguish amongst neural subspace hypotheses." Figure 1c shows which latent space gives the best predictive probability at different locations, but no experiment shows stimulations being chosen to discriminate between competing subspace hypotheses, no metric quantifies discrimination success, and Algorithm 1 contains no step that selects stimulations based on subspace distinguishability. This is a significant gap between what is claimed and what is actually shown — the claim reads as aspirational rather than demonstrated.

### Minor
- **The optimization solver for Equation (8) is under-specified.** The paper does not specify what solver is used for the non-convex cosine-similarity objective with box constraints and L1 penalty, how it is initialized, or how many iterations are run. The statement that the approach "leverages the differentiability of our stimulus-response mapping" suggests gradient-based optimization, but the L1 penalty is non-smooth and RBF kernel gradients can vanish in high dimensions without careful bandwidth tuning. These details affect both reproducibility and credibility of the <10ms runtime claim for this component.

- **The kernel bandwidth tuning procedure is hand-waved.** The paper states bandwidths are "optionally tuned by stochastic coordinate descent at each new observation" but does not specify the number of parameters, the objective function, or the per-update computational cost. For a method whose headline claim is real-time feasibility, the tuning procedure for a core model component needs at least a summary of its computational footprint.

- **The convergence comparison in Figure 1a uses different generative models for different methods.** sjPCA and proSVD are tested on a circular linear dynamical system (matching their assumptions), while mmICA is tested on a 6D system with Laplace random variables (matching ICA assumptions). This makes cross-method convergence rate comparisons uninterpretable, though the within-method convergence to offline solutions is still informative.

### Trivial
None.

## Nice-to-Haves
- A non-trivial baseline for the response mapping (e.g., linear regression with state-dependent weights) would strengthen the evidence that the kernel regression approach is necessary.
- Demonstrating the full closed-loop cycle (estimate \(\hat{S}\) → optimize stimulus → deliver → observe response → update \(\hat{S}\)) as a clean end-to-end experiment would be the single most compelling piece of evidence.
- Either demonstrating the subspace discrimination claim with a concrete experiment, or removing it from the abstract and introduction.

## Removed Points
These points are flagged to be removed, treated with caution.

- **Harsh Critic claim that sjPCA is insufficiently explained (Sherman-Morrison details):** The paper states the approach and provides Equations (1)-(2). The level of detail is reasonable for a conference paper; the Sherman-Morrison application is a standard linear algebra technique and full implementation details would be in code/supplementary. Demoted from major concern.
- **Harsh Critic claim that "1-step-ahead prediction error conflates \(\hat{f}\) quality with \(\hat{S}\) quality":** The paper explicitly states that both the proposed model and the blind comparison use the same underlying dynamical model (KF), so the difference during stimulation periods isolates the \(\hat{S}\) contribution. The blind model comparison is valid for its purpose.
- **Harsh Critic claim about runtime analysis being completely deferred to supplementary:** The paper states the <10ms/<100ms claims in Section 3 and references benchmarking in supplementary materials. This is standard practice.
- **Harsh Critic claim about Figure 5 being "confusing":** The figure and caption clearly show (a) difference between observed and predicted error (tracking \(\hat{S}\) convergence) and (b) proportion of magnitude aligned with \(v\). The distinction between panels is adequately explained.
- **Harsh Critic claim that the gap is "structural" and "fatal":** While the simulated-stimulation issue is significant, calling it "structural/fatal" overstates the case for a methods paper that is transparent about its validation conditions and explicitly frames the work as enabling "future in vivo applications." Retained as Major rather than Fatal.
- **Strength Finder generic strengths about problem importance and motivation:** These are not specific to this paper. Removed.
- **Strength Finder claim about "opportunity for adaptive selection of stimulations to distinguish competing subspace hypotheses":** This is aspirational, not demonstrated. Moved to Major weakness.

## Novel Insights
The integration of temporal discounting into kernel regression for stimulus-response modeling is a practically motivated innovation: by making the estimator's memory of past observations tunable via a time kernel, the model can continuously track drifting stimulus-response relationships without explicit change-point detection. The flip-and-rotate experiments (Figure 2e) provide a clean demonstration. Separately, the observation that predicted error functions as a calibrated lower bound on observed error (<6% violation rate for feasible targets) is a property that could guide real experimental decision-making — an experimenter can trust the optimization's self-assessment before committing to deliver a stimulus.

## Suggestions
- Add at least one non-trivial baseline for the response mapping (e.g., linear regression \(s = Wu + b\)) and one for optimization (e.g., greedy neuron selection based on latent space projection alignment). These are straightforward to implement and would substantially strengthen the evidence that the specific design choices matter.
- Either demonstrate the subspace discrimination claim with a concrete experiment (e.g., select stimulations to maximize prediction divergence between two latent space hypotheses) or remove it from the abstract and introduction.
- Specify the optimization solver details (solver type, initialization strategy, typical iteration count) and kernel bandwidth tuning procedure (number of parameters, objective) in the main text or a prominent appendix.

---

## Anchor Comparison Summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `OcTUquFXfx` (global minima) | 2.60 | R1 | Our paper is substantially stronger — different domain, but clearly more complete |
| `PiHGrTTnvb` (closed-loop diffusion control) | 3.00 | R1 | Our paper is stronger — the diffusion paper had a single 3 dragging down otherwise high scores |
| `4AlNpszv66` (FCCA) | 4.75 | R1/R2 | Our paper is clearly better — FCCA had serious derivation issues and theoretical concerns |
| `FwW3jqchtY` (iSSM) | 5.00 | R1/R2 | Most comparable domain. iSSM has real interventional data + theory; our paper has more complete engineering pipeline. Our paper slightly better. |
| `LNp7KW33Cg` (stabilized neural dynamics) | 5.00 | R2 | Different topic (BCI). Our paper is stronger on technical contribution. |
| `TVnkjz4MqV` (NMR) | 5.50 | R1 | Comparable quality. NMR has more extensive experiments; our paper has broader scope and harder problem. |
| `SyPrLti4PG` (few-shot prediction) | 5.67 | R2 | Different topic. Our paper has more substantive contribution. |
| `4ltiMYgJo9` (closed-loop EEG) | 5.75 | R2 | Our paper is clearly better — the EEG paper had serious presentation and validation gaps. |
| `MFCjgEOLJT` (control inputs locomotion) | 5.75 | R2 | **Accepted.** Comparable novelty depth. Our paper addresses harder problem (high-dim stimulation design vs behavioral modeling) but has simulated-stimulation limitation. Comparable overall. |
| `WQwV7Y8qwa` (switching nonlinear DS) | 5.80 | R1/R2 | **Accepted.** Different topic. Our paper is comparable in quality. |
| `wCUw8t63vH` (spectral learning) | 6.80 | R2 | Our paper is weaker on theory but comparable on application relevance. |
| `cNmu0hZ4CL` (optimal transport) | 8.00 | R1 | Our paper is clearly below — less theoretical depth, weaker validation. |
| `kbjJ9ZOakb` (invariance manifolds) | 8.00 | R1 | Our paper is clearly below — less novelty, weaker validation. |

**Round 1 bracket:** 4.5–6.5. **Round 2 narrowing:** 5.0–6.0. Final score: **5.5**, positioned just above iSSM (5.00) and comparable to NMR (5.50) and MFCjgEOLJT (5.75, accepted). The simulated-stimulation validation gap, weak baselines, and undemonstrated subspace discrimination claim prevent a higher score despite genuine strengths in the kernel regression design and constrained optimization.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>