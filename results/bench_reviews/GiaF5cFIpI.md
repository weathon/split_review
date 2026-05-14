Now I have all the material I need. Let me synthesize the final review.

## Summary

This paper presents an integrated real-time framework for learning how stimulations affect latent neural dynamics and designing stimulation patterns to drive those dynamics in user-specified directions. The pipeline combines streaming dimensionality reduction (including a novel streaming jPCA variant), a nonparametric kernel regression model of stimulus-response mappings that adapts to non-stationarities, and a constrained optimization procedure that respects sparsity and non-negativity limits on stimulation vectors. The components are benchmarked to run under 100 ms end-to-end, and experiments span toy models, real neural data (calcium imaging and electrophysiology) with simulated stimulations, and two real stimulation datasets.

## Strengths

- **First integrated real-time pipeline for closed-loop stimulation design in latent spaces.** The paper combines streaming dimensionality reduction, dynamical modeling, adaptive kernel regression, and constrained optimization into a single framework that runs under 100 ms. This goes beyond prior work that addressed isolated pieces. The parallel evaluation of multiple latent representations (proSVD, sjPCA, mmICA) with adaptive switching (Figure 1c) is a thoughtful design that allows real-time comparison of subspace hypotheses.

- **Nonparametric stimulus-response model with temporal adaptability.** The kernel regression in Equation (7) conditions on latent state, stimulus vector, and sample age, allowing the model to discount old observations. The flip and rotate tests (Figure 2d–e) convincingly demonstrate recovery within ~15 s after a 180° discontinuity and continuous tracking of a drifting mapping — capabilities that static linear models cannot provide.

- **Constrained optimization tailored to optogenetic feasibility.** The optimization problem (Equation 8) enforces non-negativity, sparsity (via L1 relaxation of L0), and box constraints, reflecting real limits on photostimulation. The method successfully distinguishes feasible targets (e.g., ~85% of feasible random directions achieve <1° misalignment) from infeasible ones (blanket inhibition, dense excitation), as shown in Figure 4b.

- **Convincing runtime benchmarks.** Appendix H shows that all components execute in under 10 ms on average and under 100 ms end-to-end, meeting the requirements for real-time in vivo deployment.

## Weaknesses

### Fatal
None.

### Major

1. **The primary evaluation uses simulated stimulations on real neural data, not real perturbations.** The central claim is a method for *driving* latent neural dynamics via designed stimulations. Yet Figures 3 and 4 — the main real-data results — simulate stimulations using an autoregressive function added to pre-recorded neural activity (lines 502–510). This means the stimulus-response mapping *Ŝ* is learned on simulated rather than real perturbations, and the optimization is validated against these simulated effects. The Discussion (line 700) acknowledges this: "our real data experiments were performed offline, though in a realistic streaming setting." While the paper positions itself as enabling *future* in vivo experiments, this gap between claim and validation is significant. The two real stimulation datasets in Appendix C (Daie et al., Draelos et al.) only validate the prediction model (comparing against a blind model), not the full closed-loop optimization — and even there the improvements are modest (1.84 vs 2.63, 4.63 vs 5.67) without error bars or statistical tests. The paper would be substantially stronger with even one real closed-loop validation.

2. **Weak comparison baselines.** The optimization evaluation (Figure 4a) compares only against random single-neuron, random multi-neuron, and shuffled versions of the method's own stimuli. While the paper cites several prior stimulation design approaches (Minai et al. 2024, Wagenmaker et al. 2024, Yang et al. 2021), none are used as baselines. Without comparison against any alternative method for designing stimuli toward latent targets, it is unclear whether the advantage comes from the optimization itself, the kernel regression model, or simply the problem formulation.

### Minor

3. **The sjPCA streaming formulation is presented at a sketch level.** The paper mentions using the Sherman-Morrison formula to update Equation (1) and an Orthogonal Procrustes step (Equation 2) to stabilize planes, but does not derive the update or show how it relates to the original batch jPCA. The convergence analysis (Figure 1a) uses only synthetic data, and the error metric (sum of absolute principal angles) is not validated on real neural recordings for sjPCA specifically. Since proSVD already provides online dimensionality reduction, the incremental contribution of sjPCA relative to a known offline method is unclear.

4. **No evaluation of how well the L1 relaxation approximates the L0 sparsity constraint.** The optimization replaces the L0 constraint with an L1 penalty offset by *N* (Equation 8). The paper never reports how many solutions actually satisfy the desired ∥u∥₀ ≤ max constraint, nor how this varies with λ₁. Given that sparsity is a key feasibility constraint, this omission weakens the optimization evaluation.

5. **The real stimulation datasets in Appendix C lack statistical rigor.** The improvements (1.84 vs 2.63 and 4.63 vs 5.67) are reported as point estimates without error bars, confidence intervals, or significance tests. Trial-by-trial variability is not shown. This makes it difficult to assess whether the improvements are robust.

### Trivial

6. The derivation of *Ŝ* (Section 2.3) would benefit from clarifying the handling of the delay parameter *d* and the conditions under which update rules fire.
7. Figure 3b shows "rightwards" push along *Q₀* with green arrows but provides no quantitative alignment measure for those specific trials.

## Nice-to-Haves

- An ablation study isolating which component (streaming dim reduction, kernel regression, or optimization) drives performance would strengthen the paper.
- Example optimized stimulation vectors *u\** for a few trials would build intuition (e.g., do they select neurons with high loadings in the target direction?).
- Learning curves for *Ŝ* on real data (as a function of number of stimulations, with variance across repeats) would substantiate the claim of learning within 10–20 stimulations.

## Removed Points

These points are flagged to be removed, treat them with caution:
- The harsh critic's objection to the "10⁴⁵ combinations" statement in the Introduction as "irrelevant" — this is a standard motivation for why brute-force is infeasible, not a claim about the solution method.
- The criticism that the toy model's binary stimulation (Equation 9) is "unrealistic" — this is a toy designed for controlled validation before moving to more realistic settings.
- The objection about Figure 4c (predicted vs observed error disagreement) — the paper explicitly discusses this, including the plausible explanation that infeasible targets lead the model to predict maximum error.
- Criticisms about the abstract "misleadingly" claiming "real neural data" — the abstract says "real neural data (calcium fluorescence images, intracortial electrophysiological recordings)," which is accurate; the data are real, the stimulations are simulated. This distinction is also clarified in the Discussion.
- Generic requests to add more comparison methods without specifying which are applicable — the paper's specific formulation (non-negative, sparse optimization with a learned nonparametric *Ŝ* on latent dynamics) is not directly comparable to most cited methods, which solve different optimization problems.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. The most impactful improvement would be to include one real closed-loop experiment (even on a simple preparation) that validates that the optimized stimuli produce the intended latent displacement. Without this, the paper's strongest claim remains unsupported.
2. Add at least one non-random baseline for stimulation design — e.g., selecting top-*k* neurons by absolute loading in the target direction, or a simple Bayesian optimization of the same objective.
3. For the real stimulation datasets in Appendix C, report error bars and statistical tests (even bootstrapped confidence intervals) to support the claimed improvements.
4. Evaluate the sparsity constraint satisfaction (what fraction of solutions meet ∥u∥₀ ≤ max?) and show how this varies with λ₁.

## Score and Decision

I calibrate against the following anchor papers from the human-review corpus:

| Anchor Path | Avg Human Score | Comparison |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/S4B7Iq7S3C.md` | 6.00 (Model-Guided Microstimulation) | Stronger in-vivo validation (real monkey experiments with behavior) but less comprehensive ML pipeline. Our paper is weaker on validation but comparable on methodology. |
| `/home/wg25r/review_agent/human_reviews_2026/kc5jbYHedw.md` | 4.50 (STEER plasticity inference) | Similar level: both have genuine methodological contributions but evaluation gaps relative to strongest claims. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/7jdmXx869Q.md` | 5.50 (MindPilot closed-loop EEG) | Has real human-subject validation but weaker ML methodology. Roughly comparable overall. |
| `/home/wg25r/review_agent/human_reviews_2026/2FrAvRz1E7.md` | 6.50 (InputDSA) | Cleaner theoretical framework with more convincing real-data experiments. Our paper is weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/iM4o9a83F7.md` | 7.33 (Dimensionality estimation) | Rigorous theoretical derivation validated across multiple real datasets. Our paper is substantially weaker in theoretical depth. |
| `/home/wg25r/review_agent/human_reviews_2026/IQIN8MwTWO.md` | 2.00 (DBS classifier) | Very weak validation with tiny sample. Our paper is substantially stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/wCBNxp1qWe.md` | 2.00 (Drosophila connectome model) | Overclaimed contributions relative to evidence. Our paper is stronger, though both have evaluation gaps. |

Relative to these anchors, the paper sits near the 4–5 range. It has genuine engineering contributions and the individual components are sensibly designed and benchmarked. However, the evaluation gap between the core claim ("driving latent neural dynamics") and the actual experiments (simulated stimulations on real data, with real stimulation datasets used only for prediction, not closed-loop control) is a significant weakness that prevents stronger acceptance. The paper would benefit from real closed-loop validation and stronger baselines.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>