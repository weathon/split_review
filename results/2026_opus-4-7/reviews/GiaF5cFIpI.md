## Summary
The paper proposes a streaming framework for real-time stimulus-response modeling and stimulus design to drive low-dimensional latent neural dynamics. Contributions are a streaming jPCA (sjPCA), a nonparametric kernel-regression stimulus-response model with a temporal kernel for non-stationarity, and a constrained optimization (cosine alignment to a target latent direction with non-negativity and L1-relaxed sparsity), all integrated end-to-end with sub-10ms per-step runtime.

## Strengths
- Coherent end-to-end real-time pipeline (Alg. 1) integrating streaming latent construction, dynamics tracking, kernel-regression response model, and constrained stimulus optimization.
- The sample-age kernel demonstrably tracks non-stationary stim-response mappings (Fig. 2e Flip and Rotate): the model recovers within ~15s from a 180° flip and tracks a 1 rev/30s rotation, with consistently lower 1-step error than a blind comparator.
- The constrained optimization (Eq. 8) formalizes biologically relevant constraints (non-negativity, neuron budget via L1 relaxation, magnitude cap) and is differentiable through the kernel response model.
- Fig. 5b shows that for non-trivial S, closed-loop optimization yields stimuli more aligned with the target direction than open-loop projection — directly supporting the necessity of a learned response model.
- Reported runtimes (<10ms avg, <100ms worst) are credibly compatible with both calcium imaging and electrophysiology data rates.

## Weaknesses

### Fatal
None.

### Major
- **All "real-data" stimulations are synthetic AR(1) additive injections.** Sec. 4.1: "y_t = r_t + a_t, a_t = 0.8 a_{t-1} + u_t". The kernel regressor is asked to recover a linear additive perturbation that the authors themselves placed into the data. The motivating regime in the introduction (unreliable responses, off-target excitation, state-dependence, plasticity) is never tested on real data — only on the toy circular system in Fig. 2c–e. This substantially narrows what the calcium-imaging and primate-motor results in Figs. 3–4 are actually evidence of.
- **The sole comparator is a "stimulation-blind" version of the authors' own model.** Related work explicitly cites stimulus-design / IO-dynamical methods (Draelos & Pearson 2020; Wagenmaker et al. 2024; Yang et al. 2021; Minai et al. 2024) but none appear as baselines. The headline gain (Figs. 2e, 3c) shows only that knowing-a-stim-happened beats not knowing — a low bar that cannot establish competitiveness with existing alternatives.
- **The strongest optimization result is on directions constructed to be reachable.** Fig. 4b's "Feasible" (517/600 < 1°) is, by Sec. 4.2's own description, drawn from vectors reachable using <30 excitatory neurons; "Negative" and "Dense" are infeasible by construction. The result that matters — closed-loop optimization on non-trivial S (Fig. 5b) — is a single curve with no solver-quality quantification and no alternative (e.g., greedy at small N).
- **A contribution emphasized in the abstract — adaptive selection across latent representations — never appears in the stimulation experiments.** Sec. 2.1 / Fig. 1c motivate running sjPCA/proSVD/mmICA in parallel to distinguish subspace hypotheses, but all Sec. 4 stimulation experiments use a single representation (proSVD Q0). Motivation and experiments diverge.

### Minor
- sjPCA is validated only against an offline jPCA fit on a circular linear system whose ground truth matches the algorithm's inductive bias (Fig. 1a). There is no downstream demonstration that sjPCA improves stimulation outcomes relative to plain proSVD.
- The L1 relaxation of the neuron-budget L0 is reasonable, but realized ||u*||_0 vs. the intended n is not reported. For biological feasibility this matters.
- Fig. 4b's "Negative" target is infeasible by construction (non-negativity of u); framing it as one of four optimization comparisons inflates the apparent rigor.
- Sec. 2.2 lists KF/VJF/Bubblewrap as parallel options but all main results use KF; consequences are deferred to appendix.

### Trivial
- The bandwidth-tuning rule for the sample-age kernel (K3) is only sketched in the main text despite driving the Fig. 2e Flip/Rotate recovery.

## Nice-to-Haves
- A head-to-head comparison with at least one cited stimulus-design baseline (e.g., Wagenmaker 2024 or Draelos & Pearson 2020) on the same synthetic-injection benchmark.
- A more realistic stimulation simulator (state-dependent miss rates, lag jitter, off-target excitation) matching the failure modes the introduction cites.
- At least one experiment in which the multi-representation adaptive selection actually drives a stimulation decision.
- Quantify solver quality (e.g., vs. greedy at small N) on closed-loop targets.

## Removed Points
These were considered but not retained; flagged with caution.
- (Generic) "Important problem" — too generic to count as a specific strength.
- (Strength) "Two recording modalities" — both modalities use the same authored AR(1) injection, so the modality breadth does not strengthen the central claim independently.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add at least one head-to-head with a cited stim-design baseline using identical synthetic-injection setups, then on a more failure-realistic simulator.
- Report realized neuron-count and magnitude budgets of u*.
- Demonstrate adaptive cross-representation selection actually driving stimulus design.
- Show whether sjPCA produces measurably better stimulus-design outcomes than proSVD alone.

## Calibration

Round 1 anchors retrieved:
- /datasets/deepreview_13k_calibration/PiHGrTTnvb.md (avg 3.00, round 1, low band) — closed-loop diffusion control, distinct domain; weaker than this paper.
- /datasets/deepreview_13k_calibration/NPzuN3Rxi8.md (avg 3.00, low band) — TAVRNN; weaker.
- /datasets/deepreview_13k_calibration/m9BiWVTJDx.md (avg 3.00, low band) — MRI control; weaker.
- /datasets/deepreview_13k_calibration/BBldjKEBlJ.md (avg 3.00, low band) — neural forecasting; weaker.
- /datasets/deepreview_13k_calibration/4ltiMYgJo9.md (avg 5.75, middle band) — closed-loop EEG visual stimulation, reject; closely comparable scope.
- /datasets/deepreview_13k_calibration/FwW3jqchtY.md (avg 5.00, middle band) — interventional SSM for neural perturbations; very close in scope and similar limitations (largely synthetic validation).
- /datasets/deepreview_13k_calibration/MFCjgEOLJT.md (avg 5.75) — locomotion control inputs; less comparable.
- /datasets/deepreview_13k_calibration/4AlNpszv66.md (avg 4.75) — feedback-controllable subspaces; close in spirit.
- /datasets/deepreview_13k_calibration/cNmu0hZ4CL.md (avg 8.00, high band) — OT distances for noisy dynamics; clearly stronger.
- /datasets/deepreview_13k_calibration/kbjJ9ZOakb.md (avg 8.00, high) — invariance manifolds; stronger.
- /datasets/deepreview_13k_calibration/Xo0Q1N7CGk.md (avg 8.00) — grid cells; stronger.
- /datasets/deepreview_13k_calibration/RWJX5F5I9g.md (avg 8.00) — Brain Bandit; stronger.

Round 1 bracket: 4–6. The paper has more engineering scope than FwW3jqchtY but the same core empirical limitation (largely synthetic validation, weak baselines), and is less polished than 4ltiMYgJo9 in baseline comparison.

Round 2 anchors:
- FwW3jqchtY (5.0), hyYP9MZeYn (4.75), BYUdBlaNqk (5.25), SyPrLti4PG (5.67), 4ltiMYgJo9 (5.75), TVnkjz4MqV (5.5), F5lcN7329a (6.0), 4AlNpszv66 (4.75).

Most relevant anchors are FwW3jqchtY (5.0) and 4ltiMYgJo9 (5.75). This paper sits close to FwW3jqchtY: ambitious systems framing, but the central claim (real-data stimulus design) is supported by author-injected perturbations and a strawman baseline. Compared to 4ltiMYgJo9, this paper has weaker baseline rigor and a contribution-experiment mismatch (adaptive selection unused). Slightly below FwW3jqchtY due to the larger gap between abstract claims and the realized experiments.

Final score lands at 4.5.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>