Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper develops a real-time streaming framework for modeling how high-dimensional neural stimulations affect low-dimensional latent dynamics, and for optimizing stimuli under realistic biological constraints (non-negativity, limited simultaneous targets, power limits). The framework integrates three components: (i) streaming latent space construction (including a novel streaming jPCA variant), (ii) a nonparametric kernel-regression stimulus-response model that adapts to non-stationarity, and (iii) constrained optimization to design stimuli that push latent activity along desired directions. Experiments are run on synthetic data and on real neural recordings (calcium imaging, electrophysiology) with simulated stimulation effects.

## Strengths

1. **Novel streaming sjPCA that converges to the offline rotational subspace.** Section 2.1 introduces sjPCA with an Orthogonal Procrustes stabilization step (Eq. 2). Figure 1a shows convergence to the true skew-symmetric rotation plane within ~2 s of simulated data, matching the offline jPCA baseline. This provides a capability — real-time tracking of rotational latent dynamics — not available in earlier streaming methods like proSVD.

2. **Nonparametric kernel-regression stimulus-response model that handles non-stationary mappings.** Equation (7) uses radial-basis kernels over latent state, stimulus, and sample age. Figure 2e demonstrates that after a 180° flip of the true mapping at 25 s, the model's prediction error spikes then recovers within ~15 s, while a blind model remains elevated. This is concrete evidence that the temporal kernel discounting mechanism works for both sudden discontinuities and continuous drift.

3. **Constrained optimization that designs stimuli aligning activity with latent directions, validated against multiple baselines.** Figure 4a shows that designed stimuli achieve a median angle of ~15° between observed and desired latent perturbation, while random single-neuron, random multi-neuron, and shuffled-designed stimuli all exceed 60°. 508/600 optimizations toward the first latent direction yield misalignment below 1°, confirming reliability under the non-negativity and sparsity constraints.

4. **End-to-end runtime below 10 ms per timepoint.** Section 3 reports all experiments average <10 ms per iteration and never exceed 100 ms on a workstation with an NVIDIA 3060 Ti GPU, meeting the real-time requirement for closed-loop in vivo applications — a threshold not demonstrated by prior optimization-based stimulation frameworks for latent dynamics.

5. **Validation on two real neural recording modalities.** The method is tested on calcium imaging data (Zong et al., 2022, 592 neurons) and electrophysiological recordings (O'Doherty, 2024, 130 units), demonstrating that the learned stimulus-response mapping reduces 1-step-ahead prediction error relative to a blind model on realistic data (Figure 3c, Appendix C).

## Weaknesses

### Fatal
None.

### Major

1. **The L₁ sparsity penalty in Eq. 8 is incorrectly formulated or underspecified.** The penalty term is λ₁(‖u‖₀^max – ‖u‖₁). For λ₁ > 0, minimizing this objective maximizes ‖u‖₁, which pushes all entries toward 1 (dense), the opposite of the stated goal of encouraging sparsity. The parameters ‖u‖₀^max and λ₁ are never defined or given default values; the text refers to "offset by N" and "non-zero elements close to n" using inconsistent notation (N vs. n vs. ‖u‖₀^max). While the experimental results (Fig 4) do show the method producing sparse stimulations in practice (14 out of 592 neurons in Fig 3a), the mathematical formulation as written does not match the stated intent. The paper needs to clarify whether the penalty is implemented differently during optimization, or reformulate Eq. 8 to correctly incentivize sparsity (e.g., a proper L₁ regularizer ‖u‖₁ with λ₁ > 0, or an explicit cardinality constraint via projected gradient).

2. **No comparison against existing stimulation design methods from the literature.** The paper cites active learning (Wagenmaker et al., 2024), Bayesian optimization (Minai et al., 2024), and Bayesian variational inference (Draelos & Pearson, 2020) as addressing parts of the same problem, but implements none of them as baselines. The only comparators are a "blind" model that ignores stimulation and random stimulation (single, multi, shuffled). Without comparing against any method that actively designs stimuli, the paper cannot support the claim that its approach is better or different from existing work. At minimum, a Bayesian optimization baseline using the same learned S-R model would establish the value of the specific optimization formulation in Eq. 8.

3. **Validation on "real neural data" uses simulated stimulation effects, limiting biological claims.** Section 4.1 states explicitly that stimulations were simulated: "we simulated stimulations using an autoregressive function" (y_t = r_t + a_t, a_t = 0.8·a_{t-1} + u_t). While the neural recordings themselves are real, the stimulation-response pairs are synthetic and generated by a linear AR(1) process that the model is well-suited to learn. This is not "circular" — the model must still learn the mapping from data — but it means the evaluation tests the model's ability to fit the chosen generative function rather than its ability to discover unknown biological response functions. The abstract's phrasing "demonstrate on both simulated and real neural data" is technically accurate (the neural data are real) but the stimulation effects are not, which readers may find misleading. A real closed-loop validation or test on a public dataset with actual optogenetic perturbations (e.g., Daie et al., 2021; O'Shea et al., 2022) would substantially strengthen the paper.

### Minor

4. **The parallel latent-space selection mechanism (Section 2.2, Fig 1c) is not tested in the stimulation pipeline.** The paper introduces sjPCA, proSVD, and mmICA as concurrent latent spaces with adaptive selection, and presents this as a contribution ("a novel streaming estimator to determine which representation is most predictive"). However, the stimulation experiments (Sections 4.1, 4.2) use only proSVD and KF, and never exercise the parallel selection mechanism in the context of stimulation design. The utility of this feature for improving stimulation outcomes is therefore unvalidated. The paper should either provide such experiments or scope the claim more modestly.

5. **sjPCA, a claimed novelty, is not evaluated in the main stimulation experiments.** The novel streaming jPCA (Section 2.1) is validated for subspace convergence in Figure 1a on simulated data only, but is never used in the stimulation-response modeling or optimization experiments. Its role in the pipeline and any benefit it provides over proSVD for stimulation design remain unclear.

6. **The optimization solver (algorithm, hyperparameters) for Eq. 8 is not described.** The paper specifies "argmin with box constraints" (Algorithm 1, line 19) but does not state the optimizer used (e.g., L-BFGS-B, projected gradient, Adam), learning rate, number of iterations, initialization strategy, or termination criteria. Combined with the unclear L₁ formulation, this makes the optimization procedure difficult to reproduce or assess.

### Trivial

- The notation in the text uses both N (total neurons) and n (target non-zero count) interchangeably; ‖u‖₀^max in Eq. 8 is never defined in the text.
- The toy model (Eq. 9) uses binary u ∈ {0,1}, while Eq. 8 allows u ∈ [0,1]^N — this inconsistency is never addressed.

## Nice-to-Haves

- A comparison against existing methods (Wagenmaker et al., Minai et al., Draelos & Pearson) would substantially strengthen the empirical evaluation.
- A closed-loop simulation or test on a real optogenetic perturbation dataset (e.g., Daie et al., O'Shea et al.) would bridge the gap to biological applicability.
- Ablation studies removing each component (no adaptation, no delay model, different latent spaces, different dynamical models) would clarify which components drive performance.
- A sensitivity analysis of the delay parameter d would address real-world applicability.
- Testing on a non-additive stimulation response model (e.g., multiplicative scaling) would test robustness to model misspecification.
- Providing example optimization trajectories showing the designed stimulus, resulting latent trajectory, and predicted trajectory would help diagnose sources of misalignment.

## Novel Insights

The harsh critic identifies a genuine mathematical issue with Eq. 8 that the neutral reviewer would likely miss in a quick read. However, the critic's framing that this is "fatal" and "invalidates the sparsity claim" is unsupported by the experimental evidence — the optimization clearly produces sparse stimuli in practice (Fig 3a: 14/592 neurons), suggesting either that the implemented objective differs from Eq. 8 or that the cosine-similarity term combined with box constraints implicitly enforces sparsity. The more fundamental insight from the reviews is a calibration observation: the paper's modular architecture (streaming latent space + nonparametric S-R mapping + constrained optimization) is a genuinely useful contribution, but the evaluation does not match the claim breadth. The method is tested on a pipeline where the S-R model must learn a known generative function from limited data — a necessary but not sufficient validation for the claimed goal of "enabling the next generation of experiments." The paper would benefit from narrowing its claims to match what is actually validated, or from substantially expanding the evaluation.

## Suggestions

1. **Fix Eq. 8** — Replace λ₁(‖u‖₀^max – ‖u‖₁) with a proper sparsity-inducing term (e.g., λ₁‖u‖₁ with λ₁ > 0; or a constraint ‖u‖₁ ≤ n combined with the box constraints; or a relaxation like λ₁(‖u‖₁ – τ)²). Define all notation explicitly and state the sign of λ₁.

2. **Implement at least one literature baseline** — A Bayesian optimization approach (using the same learned S-R model as the surrogate) would be the most natural comparison. At minimum, compare against uncertainty-guided active learning or optimal experimental design on the same stimulus selection task.

3. **Either validate the parallel selection mechanism in the stimulation loop or remove the claim** — If sjPCA and mmICA are not tested under stimulation, the claim about "adaptive selection of stimulations to best distinguish amongst neural subspace hypotheses" is unsupported.

4. **Specify the optimization solver** — State the exact optimizer, learning rate, iterations, initialization, and convergence criteria used for Eq. 8.

5. **Run a stronger biological validation** — Either use a public dataset with real optogenetic perturbations, or design a more realistic simulation where the true S function is nonlinear and unknown to the model (e.g., a spiking network model).

## Removed Points

These points were raised by reviewers but removed or demoted after cross-checking against the paper:

- **"Circular evaluation: model learns the same synthetic function that generates the data"** — Removed as overstated. The paper transparently states the stimulation is simulated. The model must still learn the AR(1) mapping from limited, noisy data — this is a valid test of the learning procedure, not a circular argument. Keeping it as a Major (weaker than
the critic intended) under point 3 above.
- **"mmICA uses proSVD as initial reduction, which may discard dimensions ICA needs"** — Removed. This is a standard design choice; the paper does not claim mmICA is optimal.
- **"Response model assumes additive effects (scope limitation)"** — Demoted to nice-to-have. The paper explicitly scopes to additive models and acknowledges nonlinear latent methods as a limitation. Scope-creep criticism.
- **"Toy model S is too simple"** — Demoted. The paper also tests on real data with more complex settings. The toy model is a controlled initial test.
- **"Runtime claim unsupported by concrete profiling"** — Removed. Section 3 reports concrete numbers (<10 ms average, <100 ms max). This is sufficient for the claim.
- **"No hyperparameter settings for reproducibility"** — Removed per rules (code promised in reproducibility statement; the optimizer details are a valid concern kept as minor weakness #6).
- **"Missing appendix content"** — Removed per rules (parser strips appendices from all submissions).
- **Formatting/style nitpicks and speculation about unreleased models/data** — Removed per rules.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>