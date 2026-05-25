Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper presents an end-to-end pipeline for real-time adaptive stimulation of latent neural dynamics. The key components are: (1) streaming latent space construction (including a novel streaming jPCA variant), (2) a nonparametric kernel-regression model for learning stimulus-response mappings that accommodates temporal discounting and delayed responses, and (3) a constrained optimization framework for designing high-dimensional stimuli that push latent states in desired directions while respecting experimental constraints (non-negativity, sparsity, power limits). The method is validated on synthetic data with non-stationary dynamics and on two real neural recording modalities (calcium imaging, electrophysiology), with algorithm runtimes under 10ms on average.

## Strengths

- **Novel end-to-end pipeline for a timely problem**: The paper addresses the important and under-explored challenge of designing closed-loop stimulations that target latent dynamical states. The integration of streaming dimensionality reduction, adaptive response learning, and constrained optimization into a single real-time framework is a first-of-its-kind contribution.

- **Nonparametric kernel regression with temporal discounting for stimulus-response learning (Eq. 7)**: The use of a product of three RBF kernels (on latent state, stimulus, and sample age) allows the model to handle nonlinear response mappings and adapt to non-stationarities. Figure 2e provides concrete evidence: after a 180° flip in the ground-truth mapping at t=25s, the model recovers within ~15s, while a blind comparison method does not. The continuous drift experiment further demonstrates adaptive tracking.

- **Optimization framework with realistic experimental constraints**: Equation (8) formulates stimulus design as a differentiable optimization problem that respects non-negativity, box constraints ([0,1]^N), and (intended) sparsity—all directly relevant to holographic optogenetics and multi-electrode stimulation. The paper validates against infeasible targets (Figure 4b: "Negative" inhibition and "Dense" blanket excitation) and confirms the constraints are properly enforced.

- **Demonstrated real-time capability**: The entire pipeline runs at <10ms average (under 100ms worst-case) on standard hardware (Section 3), making it genuinely compatible with in vivo closed-loop experiments.

- **Quantified reliability of optimization predictions**: Figure 4c demonstrates that the predicted misalignment angle serves as a loose lower bound on the observed misalignment, with <6% of non-Negative optimizations violating this bound—a practically useful diagnostic for experimenters.

- **Explicit handling of delayed stimulus responses**: The model incorporates a fixed delay d between stimulus delivery and its effect (Section 2.3), which is critical for realistic applications (e.g., the calcium imaging example uses 0.26s delay) and correctly attributes the response to the appropriate stimulus time.

## Weaknesses

### Major

- **The sparsity penalty formulation in Eq. (8) is unclear and likely incorrect as written.** The term $\|u\|_0^{\max} - \|u\|_1$ is problematic: (i) the notation $\|u\|_0^{\max}$ is never defined in the paper; (ii) for $u \in [0,1]^N$, minimizing this term encourages $\|u\|_1$ to be large (i.e., all entries close to 1), which is the *opposite* of the claimed sparsity constraint. The surrounding text says "we use an $L_1$ constraint on $u$ offset by $N$ to encourage a solution with the number of non-zero elements close to $n$," but the equation does not match this description. This is not a minor typo—it is the central optimization mechanism for stimulus design. The experimental results (e.g., "Dense" being flagged as infeasible, "Feasible" using <30 neurons) suggest that the *implementation* may produce sparse solutions despite the equation's apparent sign error, creating an unexplained inconsistency between the paper's mathematics and its empirical outcomes. The authors must clarify the intended formulation, define $\|u\|_0^{\max}$, correct the sign or provide the correctly specified objective, and reconcile the equation with the experimental evidence.

- **The "real neural data" experiments use simulated stimulation responses, not real biological responses.** For both the calcium imaging and electrophysiology datasets, the effect of stimulation is synthesized via a first-order autoregressive model: $a_t = 0.8 a_{t-1} + u_t$, $y_t = r_t + a_t$. This is a linear, low-dimensional, stationary additive perturbation. The abstract's phrasing "demonstrate our approach on... real neural data (calcium fluorescence images, intracortical electrophysiological recordings)" is misleading without explicit qualification that the stimulation *effects* are entirely synthetic. While the paper does transparently describe this procedure in the text, the evidential gap is significant: the method's core component—learning the stimulus-response mapping $\hat{S}$ from actual stimulation outcomes—is never tested under conditions where the response function is unknown, nonlinear, state-dependent, or biologically realistic. The toy model (Figure 2) does test non-stationarity but remains a fully synthetic system. This limits confidence that the approach would transfer to genuine experimental settings.

- **No comparison against any existing stimulus design method.** The optimization-derived stimuli are compared only to trivial baselines (random single neurons, random groups, shuffled versions of designed stimuli). The introduction cites prior work on active learning, Bayesian optimization, and input-output modeling for stimulation design (Minai et al., 2024; Wagenmaker et al., 2024; Yang et al., 2021; Draelos & Pearson, 2020), yet none are implemented as baselines. Without evidence that the method outperforms or differs meaningfully from existing approaches, the added complexity of the proposed pipeline is not justified.

### Minor

- **sjPCA and the parallel model-selection scheme are introduced as contributions but not used in the main validation.** The novel streaming jPCA (Section 2.1) and the adaptive selection among multiple latent representations (Section 2.2) are interesting, but the stimulation experiments (Figures 3–5) rely entirely on proSVD and a Kalman filter. sjPCA is validated only in Figure 1a on a synthetic toy. This fragmentation weakens the paper's coherence and leaves the practical value of these components undemonstrated.

- **No analysis of the kernel estimator's sample complexity or sensitivity to input dimension.** The kernel $K_2(u, U_i)$ operates on the full stimulus space $u \in [0,1]^N$ (up to $N=592$). With "roughly 10–20 total stimulations" available for learning, the effective sample size in a 592-dimensional space is extremely small. The paper does not discuss the curse of dimensionality, regularization, or how the kernel bandwidth is chosen relative to $N$. The sparsity constraint may mitigate this (only a few $u_i$ are nonzero), but this is not analyzed.

- **Several implementation details are underspecified.** The "stochastic coordinate descent" for tuning kernel scaling constants is mentioned but not described (initialization, convergence, computational cost). The selection of the latent dimension $k$ is not discussed or justified for the main experiments.

- **The optimization results lack statistical rigor.** The violin plots in Figure 4 are reported without numerical means, confidence intervals, or statistical tests. The closed-loop results in Figure 5 are presented without error bars, making it difficult to assess the variability or significance of the improvement over open-loop.

### Trivial

- The notation $\|u\|_0^{\max}$ is used without definition (addressed already in Major weaknesses).
- The text says "close to $n$" but $n$ is not defined; it may be a typo for $N$, but $N$ has a different meaning.

## Nice-to-Haves

- **Compare against at least one existing stimulus design method** (e.g., Bayesian optimization as in Minai et al., 2024, or random search with a sparsity constraint) to establish a performance baseline.
- **Test the response learning component on a more challenging response function**, such as one with nonlinear interactions, state-dependent gain, or spatial structure that cannot be captured by a simple additive AR(1) perturbation. A study on synthetic data varying $N$ and sample size would also clarify the estimator's practical operating regime.
- **Integrate sjPCA or the parallel model selection into at least one stimulation experiment** to demonstrate their utility, or explicitly separate them into a distinct contribution with independent validation.
- **Add numerical summaries (means, standard deviations, confidence intervals) to the Figure 4 and Figure 5 results**, and perform statistical tests for the comparisons.

## Removed Points

- **"The calcium imaging experiment uses only two stimulation events"**: This misreads Figure 3. The paper illustrates two example stimulations in panels (a) and (b), but panel (c) shows the error over the full 600s recording with many stimulations. The critic's claim is not accurate.
- **"The blind model is deliberately handicapped"**: The blind model is a valid baseline—it demonstrates what happens when stimulation effects are ignored. The comparison is informative and standard.
- **"The sjPCA description is too brief to be reproducible"** and similar reproducibility nitpicks about undisclosed implementation details: these are standard for a conference paper with appendix space limitations and do not constitute substantive weaknesses.
- **General area-of-concern sweeps** (e.g., "the evaluation lacks rigor," "could the metric be measuring a proxy?") that lack a concrete anchor in the paper.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a tension that is worth noting: the paper simultaneously introduces multiple novel components (sjPCA, parallel model selection, nonparametric response learning, constrained optimization) but validates only a subset in the main pipeline. This creates an unusual dynamic where the paper reads more like a "system design blueprint" than a tightly focused empirical contribution. The optimization formulation issue (sign of the sparsity penalty) is particularly striking because the experimental results appear to contradict the mathematics as written—suggesting either a gap between the paper's equations and its implementation, or that the alignment objective and box constraints alone produce sparse solutions through some other mechanism. Resolving this inconsistency would significantly strengthen the paper.

## Suggestions

1. **Fix the optimization formulation**: Define $\|u\|_0^{\max}$, correct the sign of the sparsity penalty to match the stated goal, and verify that the corrected objective produces the same empirical behavior as the current results. Alternatively, if the current formulation does induce sparsity through some other mechanism (e.g., interaction with the alignment objective), explain this clearly.
2. **Qualify the abstract and claims**: Explicitly state that the stimulation responses on real neural data are simulated with an AR(1) model, and reframe the evidential claims to reflect what was actually tested.
3. **Add existing-method baselines**: Implement at least one prior stimulus design method (e.g., random search with a budget constraint, or Bayesian optimization) to contextualize the method's performance.
4. **Address the kernel's curse of dimensionality**: Either provide analysis showing that the sparsity constraint effectively reduces the input dimension, or add dimensionality reduction/regularization on the stimulus space.
5. **Add statistical reporting**: Include numerical means, confidence intervals, and sample sizes for the main quantitative results.

## Score and Decision

The paper tackles an important problem with a well-motivated pipeline and several genuinely novel components. The real-time feasibility demonstration and the nonparametric response learning with temporal discounting are strong contributions. However, the optimization formulation contains a mathematically questionable sparsity penalty, the validation on "real neural data" uses entirely synthetic stimulation responses, and no comparison against existing methods is provided. These issues are addressable in revision but are substantive as the paper stands.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>