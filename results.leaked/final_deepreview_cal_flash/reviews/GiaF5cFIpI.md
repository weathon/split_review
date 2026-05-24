Now I have sufficient calibration. Let me compose the final consolidated review.

## Summary

The paper presents an integrated real-time framework for designing high-dimensional neural stimuli that drive latent neural dynamics in desired directions. It combines streaming latent space construction (including a novel streaming variant of jPCA), nonparametric stimulus-response modeling via kernel regression with temporal adaptation, and constrained optimization that leverages differentiability to select stimuli under realistic experimental constraints. Experiments on simulated data and real neural recordings (calcium imaging, electrophysiology) with simulated stimulation effects show that the method learns response maps within tens of stimulations and finds stimuli whose latent effects align with target directions far better than random selection, all within real-time computational budgets (<100ms).

## Strengths

- **Adaptive nonparametric stimulus-response model.** The kernel regression estimator (Eq. 7) successfully learns stimulation effects from few examples and adapts to nonstationarities, demonstrated by recovery from a 180° flip and continuous rotation of the mapping (Fig. 2e). This directly supports the claim that the method can track changes in neural responses under stimulation, a critical requirement for real-world deployment.

- **Feasibility-constrained optimization demonstrably outperforms random baselines.** The optimization (Eq. 8) with L₁ sparsity and box constraints designs stimuli whose latent perturbations align with target directions significantly better than random single-neuron, multi-neuron, and shuffled stimuli (Fig. 4a,b). The method achieves <1° misalignment on >85% of feasible-direction trials (517/600), providing strong evidence for the optimization's efficacy under the assumed stimulus-response model.

- **Real-time runtime demonstrated.** The entire pipeline runs in <100ms and averages <10ms per timepoint (Section 3), meeting the speed requirements for closed-loop in vivo experimentation.

- **Novel streaming latent space construction.** The sjPCA method with Orthogonal Procrustes stabilization demonstrates convergence to offline jPCA (Fig. 1a), enabling real-time identification of latent spaces with rotational dynamics that can be used interchangeably in the framework.

- **Validation across recording modalities.** The method is tested on both calcium imaging (592 neurons, 15 Hz) and intracortical electrophysiology (130 units, 30 Hz) datasets, demonstrating applicability across different data rates and noise characteristics.

## Weaknesses

### Fatal
None.

### Major

- **The core optimization solver is critically underspecified.** The paper never states which algorithm solves Eq. (8) — no optimizer type (gradient descent, L‑BFGS, Adam?), step size, initialization scheme, number of restarts, or termination criteria. The kernel regression that provides gradients is non-convex and the stimulus dimension reaches N=592, making solver choices consequential for both solution quality and the reproducibility of all optimization results. Despite being central to the claimed contribution, this component is a black box.

- **No comparison to alternative stimulus-design methods.** Bayesian optimization (Minai et al., 2024) and active learning (Wagenmaker et al., 2024) are cited as related work but never compared against. Without such baselines, it is unclear whether the differentiable nonparametric model yields tangible improvements over simpler strategies such as random shooting or Bayesian quadrature, or whether the complexity of the pipeline is warranted. Every ablation compares against random or "blind" variants of the authors' own method.

- **Adaptive latent-space selection is described as a feature but never validated in the stimulation loop.** Section 2.2 and Fig. 1c present parallel latent-space tracking with adaptive selection of the most predictive representation. However, the stimulation experiments (Sections 4.1–4.2) use a fixed latent space (proSVD). Whether the adaptive switching improves stimulus design or dynamical prediction is never tested, leaving a claimed capability unsubstantiated.

### Minor

- **Real-data validation uses simulated, not real, stimulations.** All experiments on real neural data replace actual stimulation with a synthetic autoregressive additive model (the paper acknowledges this in Section 5). While this is a reasonable first step and the authors are transparent about it, the abstract and introduction frame the method as "compatible with future in vivo applications" without conveying the evidential gap. The learned stimulus-response mapping is thus tested against a tractable artificial target rather than the complex, state-dependent, and noisy effects of genuine optogenetic or electrical stimulation.

- **No analysis of kernel regression sensitivity in high dimensions.** The paper uses RBF kernels on stimuli u ∈ ℝ^{592} with very few data points. High-dimensional RBF kernels are known to concentrate distances and require careful length-scale tuning. The paper mentions "optional tuning" of scaling constants (Section 2.3) but provides no ablation, no default values, and no discussion of this well-known issue.

- **The open-loop optimization evaluation is near-tautological.** The open-loop setting (Section 4.2, S(u)=Qᵀu) uses exactly the mapping that the objective in Eq. (8) was designed to optimize against. Outperforming random selection under this mapping is expected. The closed-loop results (Fig. 5) with learned non-trivial mappings are more informative but still use a simulated target.

- **mmICA is not truly streaming.** The paper applies proSVD for streaming dimensionality reduction, then runs the batch mmICA algorithm on the reduced data (Section 2.1). This is a two-stage process with a batch component, not a fully streaming method as implied.

### Trivial
- The open-loop evaluation's "identity stimulus-response mapping" is described with slightly misleading framing in Section 4.2 — the comparison against random baselines is useful but the framing could overstate its contribution.

## Nice-to-Haves

- Sensitivity analysis of kernel length scales and the L₁ penalty λ₁. How robust are the optimization results to these hyperparameters?
- An ablation comparing the full differentiable optimization against a simpler random-shooting baseline (sample many candidate u, pick best predicted angle) to isolate the value of differentiability.
- Discussion of how continuous-valued u ∈ [0,1] solutions would be mapped to stimulation protocols in settings requiring binary on/off actuation.
- More detailed description of the optimization solver (projected gradient? clamped updates? etc.) — this is currently an underspecified major component.

## Removed Points

These points were flagged as removable by the filtering criteria and are listed here only for transparency:

- **"The sjPCA description is too brief to reproduce"** (Harsh Critic) — The paper provides sufficient mathematical description (Eq. 1–2) and demonstrates convergence empirically (Fig. 1a). While full reproducibility would benefit from released code, the description is at a level typical for conference papers. → REMOVED (strawman — the description is adequate for the paper's scope).

- **"Figures have captions that repeat the main text"** (Harsh Critic) — This is a minor formatting observation; not a scientific weakness. → REMOVED (formatting/style nitpick).

- **"The blind baseline is a very low bar"** (Harsh Critic) — The blind model (ignoring stimulation times) is a reasonable baseline for isolating the value of the response model. A stronger baseline would be nice but the blind model is not invalid. → DEMOTED from major to minor framing, but the core observation (baseline is weak) is retained in the Minor section under "open-loop evaluation" framing.

- **"The binary on/off issue"** (Harsh Critic) — The framework explicitly uses u ∈ [0,1]^N (which allows continuous, graded stimulation). Only the toy model uses binary stimulation. The critic assumed a binary requirement not stated in the paper. → REMOVED (factually wrong).

- **Strength Finder's "parallel representation evaluation" strength** — This claimed capability is not validated in the stimulation experiments. → REMOVED from Strengths (conflicts with verified weakness; moved here).

- **Strength Finder's "validation on real neural data"** — While the paper does use real recordings, the stimulations are simulated. This is a weaker form of validation than the strength description implies. However, the papers' use of real data from two modalities is still a strength worth noting (retained in Strengths with careful framing).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel perspective that the authors themselves missed.

## Suggestions

1. **Specify the optimization solver.** Describe the optimizer, step-size schedule, initialization strategy, number of restarts, and termination conditions used for Eq. (8). Include an ablation showing sensitivity to these choices.

2. **Add at least one alternative-method baseline.** Compare against Bayesian optimization (Minai et al., 2024) or a simple random-shooting approach (sample candidate stimuli, pick best predicted alignment). This would isolate the benefit of the differentiable nonparametric model.

3. **Either validate adaptive latent-space selection or de-emphasize it.** Run an experiment where the framework switches between sjPCA/proSVD/mmICA during stimulation and compare the resulting alignment against using a fixed space. If this is infeasible, revise the framing to match what is demonstrated.

4. **Provide kernel hyperparameter details.** Report default length scales, tuning procedure, and a sensitivity analysis. Discuss the issue of distance concentration in high-dimensional RBF kernels.

5. **Include a note on how the method would map to binary stimulations** if that is the intended deployment scenario, or clarify that continuous-valued stimulation (e.g., graded optogenetics) is the target.

---

## Score and Decision

### Calibration

**Round 1 (bracketing).** Three queries on "neural latent dynamics stimulation design" with score bands (−∞,3.5), (3.5,7.5), (7.5,∞). Weak anchors (band 1) averaged 2.5–3.0: papers that were clearly out of scope, incomprehensible, or trivial. Middle anchors (band 2) ranged 5.00–6.80: relevant papers on neural dynamics, interventions, and closed-loop stimulation. Strong anchors (band 3) averaged 8.0–9.0: top-tier papers with complete theoretical and empirical validations. The paper clearly falls in the middle band.

**Round 2 (narrowing within bracket).** Two queries in (4.5,6.5) and (5.5,7.5) on more specific topics. Retrieved anchors:

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| FwW3jqchtY — iSSM (Reject) | 5.00 | 2 | Similar topic (interventions in neural dynamics), has real perturbation data and theoretical identifiability proof, but was rejected due to strong assumptions and no baselines. This paper has a more practical framework but less rigorous evaluation. |
| 4ltiMYgJo9 — EEG closed-loop (Reject) | 5.75 | 2 | Similar goal (closed-loop stimulation design), but criticized for lack of validation and unclear methodology. This paper is comparable in scope but has somewhat better-specified components. |
| LNp7KW33Cg — Neural Domain Adaptation (Reject) | 5.00 | 2 | Different specific goal (BCI decoding, not stimulation); less directly comparable. |
| TVnkjz4MqV — Neural Manifold Regularization (Reject) | 5.50 | 2 | Neural latent dynamics focus, rejected despite clean experiments. This paper addresses a more difficult problem but has less rigorous validation. |
| SyPrLti4PG — Few-shot neural latents (Reject) | 5.67 | 2 | Different angle (latent evaluation, not stimulation); comparable score tier. |
| 3usdM1AuI3 — BRAID (Accept) | 6.25 | 2 | Input-driven neural dynamics with stronger baseline comparisons and real perturbation data. This paper has a less comprehensive evaluation. |
| wCUw8t63vH — Spectral learning (Reject) | 6.80 | 2 | Strong analytical contribution but lower practical relevance. |

**Bracket:** Round 1 placed the paper in (3.5,7.5). Round 2 narrowed to approximately (5.0, 6.0). The paper falls below BRAID (6.25) due to missing optimization details and lack of alternative-method comparisons. It is comparable to or slightly above iSSM (5.00) due to its more comprehensive framework, and comparable to the EEG closed-loop paper (5.75). **Final score: 5.5.**

### Decision

The paper addresses an important and timely problem — real-time causal manipulation of latent neural dynamics — with a conceptually coherent integrated pipeline. The adaptive nonparametric response model and constrained optimization produce meaningful results on realistic benchmarks. However, the evaluation has significant gaps: the optimization solver is completely underspecified (no algorithm, hyperparameters, or initialization), there is no comparison to any alternative stimulus-design method, and a claimed capability (adaptive latent-space selection) is never validated. These weaknesses are addressable in a major revision but collectively prevent acceptance in the current form.

**Score:** 5.5

**Decision:** Reject

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>