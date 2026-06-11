## Summary

This paper proposes a real-time algorithmic framework for closed-loop neural stimulation targeting latent dynamical states. The framework integrates streaming dimensionality reduction (including a novel streaming jPCA), dynamical modeling, nonparametric kernel regression for stimulus-response mapping with temporal adaptation, and constrained optimization to select high-dimensional stimulation patterns that produce desired perturbations in low-dimensional latent space. The method is tested on synthetic data and two real neural recording datasets with simulated stimulations, demonstrating sub-10ms runtime.

## Strengths

1. **Nonparametric kernel regression with temporal adaptation recovers from non-stationarity (Fig 2e).** The kernel regression estimator (Eq. 7) demonstrably recovers from both an abrupt 180° flip (recovery within ~15s) and continuous drift in the stimulus-response mapping. This is a concrete advance over approaches assuming static mappings.

2. **Constrained optimization (Eq. 8) produces stimulus alignment far better than random baselines (Fig 4).** For feasible random directions, 517/600 optimizations achieved <1° misalignment — a level of targeted control over arbitrary latent-space directions not previously demonstrated.

3. **End-to-end runtime <10ms average, <100ms worst-case benchmarked on real hardware (Section 3).** Wall-clock timing on a specified system (Ubuntu 22.04, i9 CPU, 3060 Ti GPU) confirms the full pipeline runs fast enough for closed-loop experiments at both 30 Hz and 15 Hz data rates.

4. **Streaming jPCA with Orthogonal Procrustes stabilization converges to offline fits (Fig 1a).** First streaming version of jPCA enabling real-time tracking of rotational dynamical structure.

5. **Parallel evaluation of multiple latent representations with adaptive selection (Fig 1c).** Simultaneously maintains sjPCA, proSVD, and mmICA spaces with multiple dynamical models, selecting the best performing representation — going beyond prior approaches committed to a single representation.

6. **Validation on two real neural data modalities** (calcium imaging at 15 Hz, 592 neurons; electrophysiology at 30 Hz, 130 units) with different timescales and noise characteristics.

## Weaknesses

### Major

1. **"Real data" experiments use simulated stimulations, not actual closed-loop stimulation.** All experiments on the two real neural datasets inject synthetic perturbations via an AR(1) process ($a_t = 0.8 a_{t-1} + u_t$) atop real baseline recordings. The method learns this known injected perturbation — not real biological responses with their full nonlinearity, variability, and state-dependence. The abstract says "We demonstrate our approach on both simulated and real neural data," which is technically true but misleading without qualifiers. The Discussion mentions this in a single sentence ("our real data experiments were performed offline, though in a realistic streaming setting"), but this is insufficient given how centrally the paper frames its claims of real-data validation. [Paper lines 178-179 confirm: "For each of the real datasets, we simulated stimulations using an autoregressive function..."]

2. **No comparison to any existing adaptive stimulation method.** The main comparison is a "blind" model that ignores stimulations entirely. For stimulus optimization (Fig 4), comparisons are against random single-neuron, random group, shuffled, and infeasible-direction baselines. The paper cites Bayesian optimization (Minai et al., 2024), active learning (Wagenmaker et al., 2024), and input-output modeling (Yang et al., 2021) — yet compares against none. Outperforming random baselines sets an extremely low bar and does not support claims of advancing the state of the art.

### Minor

3. **No ablation studies.** The framework has at least five interacting components (streaming dimensionality reduction, dynamical model, kernel regression, temporal weighting, optimization). Without ablations, the paper shows a complex pipeline can work but does not reveal which design choices matter or why.

4. **The "for the first time" claim (Discussion) is overstated** given the cited prior work on adaptive stimulation. The qualifier "that accounts for realistic experimental constraints" partially distinguishes it, but the framing exceeds the evidence.

5. **No evaluation of solution sparsity / L1 vs L0 constraint satisfaction.** The optimization replaces L0 with L1, but the paper does not analyze how often solutions actually satisfy the intended sparsity target.

6. **Adaptive kernel tuning not evaluated against fixed-length-scale variants.** The optional stochastic coordinate descent tuning of kernel length scales is mentioned but never empirically compared against fixed variants.

### Trivial

7. The "novel streaming estimator to determine which representation is most predictive" (abstract, Section 2.2) is straightforward model selection by tracking predictive error — effective but not a novel estimator.

## Nice-to-Haves
- Validation on an actual closed-loop stimulation experiment (proof-of-concept with e.g., optogenetics)
- Ablation studies isolating each component
- Comparison to at least one existing adaptive stimulation method
- Analysis of sparsity constraint satisfaction

## Removed Points
- **"sjPCA is incremental engineering adaptation"** — opinion, not a factual weakness; the paper demonstrates convergence and positions it as novel.
- **Criticism about not testing nonlinear latent spaces** — acknowledged as a limitation in the Discussion; scope is affine latent spaces.
- **"Could be slow without explicit analysis" for N=592** — runtime IS benchmarked as <10ms in Section 3; this criticism is factually incorrect.
- **Formatting/style nitpicks** — parser artifacts, not author errors.
- **Missing related works** — cannot verify; hard rule.
- **Requests for larger dataset or more models** — current datasets are adequate for scope.
- **180° flip being "only synthetic"** — this is a toy model experiment designed to validate non-stationarity handling; it serves its purpose.

## Novel Insights
The harsh critic correctly identifies that the most consequential limitation — real-data experiments using simulated stimulations — is structurally misaligned with the paper's framing. This is not a standard "more experiments needed" critique but a fundamental mismatch between claim and evidence. The strength finder correctly identifies that the temporal adaptation (Fig 2e) and runtime benchmarking are the paper's strongest concrete contributions. The disconnect suggests the paper would benefit from honest reframing as a realistic-simulation study with real neural substrates, rather than claiming validation on "real neural data."

## Suggestions
1. **Reframe honestly**: If only simulated stimulations are used, state clearly in the abstract and introduction that real neural recordings serve as the activity substrate but all stimulation effects are synthetic.
2. **Add at least one baseline from prior literature**: Implement Bayesian optimization for stimulus design (Minai et al., 2024) or another existing method as a comparison point.
3. **Add ablation studies**: Compare sjPCA vs proSVD vs mmICA in the full pipeline, test with vs without temporal kernel, and compare L1 vs hard sparsity constraint.

### Calibration Anchors

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| iSSM | FwW3jqchtY.md | 5.00 | 1, 2 | Real perturbation data + theory → this paper is weaker |
| EEG closed-loop | 4ltiMYgJo9.md | 5.75 | 1 | Actual closed-loop experiment → this paper is weaker |
| MRINE | eR1119aUlL.md | 4.25 | 1, 2 | Comparable validation strength, similar weaknesses |
| HDA domain adaptation | LNp7KW33Cg.md | 5.00 | 2 | Strong baselines + ablation → this paper is weaker |
| TiDeSPL-VAE | N83O2FcqzN.md | 5.00 | 2 | More baselines, ablation → comparable |
| Zebrafish locomotion | MFCjgEOLJT.md | 5.75 | 2 | More thorough evaluation → this paper is weaker |

**Round 1 bracket**: 3.5–5.5
**Round 2 narrowing**: Compared against iSSM (5.00, real perturbation data) and MRINE (4.25, similar real-time neural modeling), this paper is weaker than the former and comparable to the latter. The paper has genuine strengths (temporal adaptation, runtime benchmarking, constrained optimization) but its evaluation is fundamentally limited by simulated stimulations on real data and the absence of any comparison to existing methods. The two major weaknesses prevent the paper from supporting its central claims.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>