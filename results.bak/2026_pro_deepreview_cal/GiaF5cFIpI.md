Now I have a comprehensive view of the anchor papers. Let me synthesize my final review.

---

## Summary

This paper presents a real-time streaming framework for closed-loop stimulation of latent neural dynamics. The core contributions include: (1) a novel streaming jPCA (sjPCA) method for online latent space construction, (2) an adaptive nonparametric kernel regression model for learning stimulus-response mappings that can handle non-stationarities, (3) a constrained optimization procedure for designing high-dimensional stimulation patterns to drive low-dimensional latent dynamics in desired directions, and (4) an integrated pipeline (Algorithm 1) that runs faster than real-time (<10 ms per timestep). The method is demonstrated on synthetic data and two real neural datasets (calcium imaging and electrophysiology), using simulated stimulations added to recorded traces.

## Strengths

- **Integrated real-time pipeline for adaptive stimulation:** The paper presents a complete framework (Algorithm 1) that interleaves streaming latent space construction, dynamical modelling, kernel-regression-based stimulus-response estimation, and constrained optimisation. On synthetic data, the estimator $\hat{S}$ learns the true mapping within ≈10-20 stimulations (Fig. 2c), and designed stimuli produce latent perturbations far better aligned with target directions than random approaches (Fig. 4a).

- **Adaptive, non-parametric stimulus-response mapping that handles non-stationarities:** The kernel-regression estimator $\hat{S}$ (Eq. 7) uses radial basis kernels over latent state, stimulus, and sample age. After a 180° flip or continuous rotation of the underlying mapping, the model recovers low prediction error — unlike a stimulation-blind baseline (Fig. 2d-e). This directly supports the claim of robustness to realistic experimental instabilities.

- **Novel streaming latent space construction (sjPCA):** The streaming jPCA uses a Sherman-Morrison update with an Orthogonal Procrustes stabilisation (Eq. 2) to track rotational subspaces in real time, converging to the same subspace as offline computation (Fig. 1a).

- **Computational efficiency permits real-time use:** All experiments averaged <10 ms per timestep and stayed below 100 ms (Section 3), meeting speed requirements for closed-loop in vivo experiments with calcium imaging (15 Hz) or electrophysiology (30 Hz).

- **Validation across diverse neural data modalities:** The method is tested on synthetic data, calcium imaging (592 neurons, 15 Hz; Zong et al., 2022), and intracortical electrophysiology (130 units, 30 Hz; O'Doherty, 2024), demonstrating applicability to both slow and fast recording regimes.

- **Handling of delayed stimulation effects:** The framework includes a fixed-delay response model (Section 2.3) and optional temporal spread coefficients, tested with a 0.2 s delay on calcium data (Fig. 3a-c). One-step-ahead prediction error remains lower than a blind model even when responses are not instantaneous.

## Weaknesses

### Fatal

None.

### Major

- **Real data experiments use only simulated stimulations; the difficult stimulus-response mapping problems are sidestepped.** The paper explicitly motivates the need to handle unknown opsin expression, spatial crosstalk, and state-dependent gain in real optogenetic experiments. Yet all evaluations on real neural data add *simulated* autoregressive perturbations to recorded traces. The stimulus-response mapping on real data is consequently trivial — it reduces to the identity mapping in the open-loop experiments (Fig. 3–4), where $S(u) = Q^\top u$. The closed-loop experiments with non-trivial mappings (Fig. 5) are conducted only on synthetic data. This means the core challenge the paper identifies — learning an unknown, non-trivial mapping from high-dimensional stimuli to latent effects — is never tested on real neural recordings. This substantially limits the evidence that the method would work under realistic in vivo conditions.

- **No comparison to any existing adaptive stimulation method.** The paper compares only against a "blind" model that ignores stimulations, and against random-unit/random-group/shuffled stimulation strategies. The literature includes closed-loop approaches based on Bayesian optimization (Minai et al., 2024, cited in the paper), active learning for stimulus selection (Wagenmaker et al., 2024, cited), and model-based control. Without even a simple baseline such as a rolling linear regression of stimulus effects, it is impossible to judge whether the non-parametric kernel regression and the specific optimization offer any advantage over simpler alternatives.

- **The multi-space and multi-model parallelism is never shown to benefit stimulation outcomes.** The paper introduces three streaming latent spaces (sjPCA, proSVD, mmICA), three dynamical models (KF, VJF, Bubblewrap), and adaptive model selection via prediction error. The adaptive selection is only illustrated as a static heatmap (Fig. 1c) showing which space was retrospectively best. The downstream stimulation experiments use a single latent space (proSVD). There is no experiment showing that switching between spaces or models improves stimulation design or closed-loop performance. This dilutes the contribution and leaves the reader uncertain which components are essential.

### Minor

- **Optimization procedure is underspecified.** The paper does not specify what solver is used for the optimization in Eq. (8), how gradients are computed through the kernel regression (which involves all training points), what initialization strategy is used, or what termination criteria are applied. The sparsity penalty notation $\|u\|_0^{\max}$ is introduced without formal definition (the text explains the intent but the formulation is imprecise). These omissions hinder reproducibility without being fatal to the core claims.

- **The optimization objective maximizes angular alignment but the evaluation of magnitude alignment is incomplete.** Equation (8) optimizes cosine similarity, ignoring whether the induced displacement is meaningfully large. Figure 5b attempts to address this by showing "proportion of magnitude aligned," but the definition of this metric is not provided in the paper body, and it is not shown whether the designed stimulations produce displacements that are large relative to ongoing dynamics. This leaves the practical utility of the designed stimuli somewhat unclear.

- **The sjPCA method description is sketchy.** The streaming solution to Eq. (1) is only described as "using the Sherman-Morrison formula" without explicit update equations. The kernel regression bandwidth tuning via "stochastic coordinate descent at each new observation" is mentioned but not specified. A reader would struggle to implement these components from the text alone.

### Trivial

- The sample size for Figure 5 experiments is stated as "10 experiments with over 100 stimulations each" but without the kind of statistical reporting (e.g., confidence intervals on final metrics) that would permit rigorous comparison.

## Nice-to-Haves

- Replacing simulated perturbations on real data with at least one public dataset that includes actual optogenetic or electrical stimulations, or a high-fidelity biophysical simulation with realistic opsin dynamics and optical crosstalk, would substantially strengthen the evidence.
- A comparison to at least one adaptive alternative (e.g., a linear-Gaussian model with a Kalman filter that jointly estimates dynamics and stimulation gain) would help calibrate the performance claims.
- Demonstrating that the designed stimulations produce a sustained displacement across multiple time steps (not just single-step alignment) would better support claims of practical utility for driving dynamics.
- Removing or de-emphasizing the multi-space/multi-model parallelism unless an experiment shows it improves stimulation outcomes.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Harsh Critic: "The central claim is unvalidated by real biological stimulation data (evidential, structural)"** — REMOVED as a fatal claim and DOWNGRADED to Major. The paper acknowledges this limitation in the Discussion ("a second limitation is that our real data experiments were performed offline" and "we demonstrated our method's capabilities on ... real experimental datasets with simulated effects"). The paper does not claim to have run in vivo experiments; it claims to have developed a method *compatible* with future in vivo use. The absence of real stimulation data is a significant limitation but not a fatal one for a methods paper. The closed-loop experiments with non-trivial mappings on synthetic data (Fig. 5) provide partial evidence. Retained as Major but not fatal.

- **Harsh Critic: "The optimization evaluation against an 'open loop' baseline is circular when the simulated mapping is the identity"** — PARTIALLY REMOVED. The paper is aware of this and separately tests closed-loop with non-trivial mappings (Fig. 5). The concern about the triviality of the real-data mapping is already captured under the Major weakness above.

- **Harsh Critic: "The L₁ surrogate ... does not enforce a bound on total stimulation power"** — DEMOTED. The box constraint $[0,1]^N$ does limit per-neuron power, and many experimental setups are limited per-neuron rather than by total power. Not a substantive flaw.

- **Harsh Critic: "The framework is overloaded with components whose synergy is never demonstrated, diluting the core contribution"** — RETAINED as Major, but the characterization as "diluting the core contribution" is the harsh critic's framing. The actual observation — that the multi-space/multi-model parallelism is not validated for stimulation — is correct.

- **Strength Finder: "Constrained optimisation finds feasible high-dimensional stimuli that align with desired latent perturbations"** — RETAINED but qualified. The 86% <1° result is for open-loop identity mapping on real data (or feasible targets where the mapping is known), which limits its evidentiary weight.

- **Strength Finder: "This paper addressed an important problem"** — REMOVED. Generic, not a substantive strength.

- **Strength Finder: "The method runs faster than real time and is validated on both calcium imaging and electrophysiological data, confirming its practical feasibility"** — RETAINED as a supporting strength. The feasibility claim is supported by the reported runtimes.

- **Harsh Critic: "Missing appendix, missing proofs in appendix"** — REMOVED per Hard Rules. The parser strips appendix sections; they exist in the original submission.

- **Harsh Critic: "Undisclosed hyperparameters, trivial implementation details"** — REMOVED per Hard Rules on reproducibility nitpicks.

- **Any concern about the existence or release status of cited models, tools, benchmarks, or datasets** — REMOVED per Hard Rules.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface insights that the paper itself does not already articulate.

## Suggestions

- The most impactful single improvement would be to include at least one experiment with a non-trivial stimulus-response mapping on real neural data. This could be achieved by defining a known nonlinear mapping (e.g., a sparse random projection with saturation) between the stimulus vector and its latent effect, and testing whether the kernel regression can recover it from real neural trajectories. This would bridge the gap between the synthetic closed-loop experiments (Fig. 5) and the real-data identity-mapping experiments (Fig. 3-4).
- Focus the paper on the core pipeline — streaming latent space construction, kernel regression for stimulus-response mapping, and constrained optimization. The multi-space/multi-model parallelism can be deferred to future work or the appendix unless an experiment shows it improves stimulation outcomes.
- Provide explicit update equations for sjPCA, specify the optimization solver and gradient computation, and report runtime scaling with the number of previous stimulations. These are relatively easy additions that would substantially improve reproducibility.

## Score and Decision

**Round-1 bracketing:** The paper was compared against three bands. Weak anchors (QuantFormer at 3.00, TAVRNN at 3.00) are clearly below this paper. Strong anchors (Feedback Neural ODEs at 8.00, Optimal Transport distances at 8.00) are clearly above. Initial bracket: **4.0–6.5**.

**Round-2 narrowing:** Anchors inside the bracket were examined:
- FwW3jqchtY (iSSM, 5.00, Reject): Uses actual stimulation data and has theoretical results, but limited comparisons and strong assumptions. Our paper has more technical components but weaker experimental validation (simulated stimulations only). Comparable overall.
- TVnkjz4MqV (NMR, 5.50, Reject): Contrastive learning for 2D latent dynamics. Good experiments but limited technical novelty and missing baselines. Our paper offers more methodological novelty but has a larger gap between claimed capability and experimental demonstration.
- 4ltiMYgJo9 (EEG closed-loop, 5.75, Reject): Closed-loop framework with offline surrogate validation. Similar validation limitations. Our paper has deeper technical contributions.
- MFCjgEOLJT (Control inputs locomotion, 5.75, Accept): Control-theoretic behavior modeling. More focused contribution but less novelty. Our paper is more ambitious but less thoroughly validated.
- wCUw8t63vH (Spectral learning shared dynamics, 6.80, Reject): Stronger than our paper — rigorous theory, clear validation. Our paper does not reach this level.

**Final calibration:** The paper lands between the iSSM paper (5.00) and the NMR paper (5.50). It has more technical novelty than both (sjPCA, integrated framework, optimization) but shares the NMR paper's issue of missing comparisons and shares the iSSM paper's limitation of experimental scope relative to claims. The simulated-stimulation-only validation on real data is the primary anchoring weakness. Score: **5.5**.

**Anchor papers summary:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| BBldjKEBlJ (QuantFormer) | 3.00 | R1 | Clearly weaker — poor baselines, unclear motivation |
| NPzuN3Rxi8 (TAVRNN) | 3.00 | R1 | Clearly weaker |
| eR1119aUlL (Nonlinear latent factors) | 4.25 | R1/R2 | Weaker — narrower contribution |
| FwW3jqchtY (iSSM) | 5.00 | R2 | Comparable — uses real stimulation data but simpler method |
| LNp7KW33Cg (HDA for BCI) | 5.00 | R2 | Weaker — less technical novelty |
| TVnkjz4MqV (NMR) | 5.50 | R2 | Most comparable — similar strengths and limitations |
| 4ltiMYgJo9 (EEG closed-loop) | 5.75 | R1/R2 | Slightly stronger in validation, weaker in technical depth |
| MFCjgEOLJT (Control inputs locomotion) | 5.75 | R2 | More focused and validated, less novel |
| WQwV7Y8qwa (Switching nonlinear DS) | 5.80 | R2 | Stronger — better validation and clearer contribution |
| wCUw8t63vH (Spectral shared dynamics) | 6.80 | R1/R2 | Clearly stronger — rigorous theory, clear validation |
| cmfyMV45XO (Feedback Neural ODEs) | 8.00 | R1 | Clearly stronger — theory + extensive experiments |
| cNmu0hZ4CL (Optimal transport distances) | 8.00 | R1 | Clearly stronger |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>