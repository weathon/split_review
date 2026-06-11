## Summary

This paper proposes a streaming framework for adaptive stimulation of latent neural dynamics. It combines three components: (1) streaming latent space construction, including a novel streaming jPCA (sjPCA) with Orthogonal Procrustes plane stabilization, (2) an adaptive nonparametric stimulus-response mapping via product-of-kernels regression that handles non-stationary mappings through a temporal kernel, and (3) a constrained optimization procedure that designs high-dimensional stimulation patterns to perturb latent dynamics in desired directions. The method is evaluated on a toy model and two real neural recording modalities (calcium imaging from mouse visual cortex, electrophysiology from monkey sensorimotor cortex), with demonstrations of sub-10ms computation times.

## Strengths

1. **Novel framework integrating streaming latent dynamics, stimulus-response modeling, and sparsity-constrained stimulation optimization**: The paper formulates a differentiable optimization (Eq. 8) that maps from high-dimensional stimuli (with L1 sparsity and box constraints) to desired latent-space perturbation directions via a learned stimulus-response mapping. The core concept of bridging streaming latent-space methods with closed-loop stimulation design under realistic experimental constraints is novel. The optimization results in Section 4.2 show 508/600 optimizations achieving <1° misalignment between predicted and desired perturbation direction for the first latent dimension Q0, and 517/600 for random feasible directions.

2. **Adaptive nonparametric stimulus-response model capable of tracking non-stationary mappings**: The product-kernel estimator in Eq. 7 includes a temporal kernel K3(t, T_i) that discounts older observations. Figure 2e provides clear evidence of adaptation: when the mapping flips 180° at t=25s, the model recovers within ~15s; when the mapping continuously rotates starting at t=45s, the model tracks the drift. The "blind" comparison method (which withholds stimulation information) shows persistently higher error during and after stimulation periods, establishing that modeling stimulation effects matters.

3. **Streaming jPCA (sjPCA) with a principled alignment mechanism**: The paper extends offline jPCA to a streaming setting by adding an Orthogonal Procrustes step (Eq. 2) to stabilize each rotation plane independently. Figure 1a demonstrates convergence of sjPCA to the same subspace identified by offline jPCA, with error decreasing rapidly over time. This provides a useful algorithmic building block for the broader framework.

4. **Demonstrated real-time computational feasibility**: Section 3 reports end-to-end computation "averaged less than 10ms" per timepoint and stayed below 100ms on a standard desktop workstation (i9 CPU, 3060 Ti GPU). This is a concrete benchmark that supports the claim of compatibility with future in vivo applications.

5. **Parallel evaluation and adaptive selection across multiple latent representations**: The method runs three latent-space constructions (sjPCA, proSVD, mmICA) and three dynamical models (KF, VJF, Bubblewrap) in parallel, evaluating predictive error at each timepoint to determine which representation best predicts ongoing dynamics (Section 2.2, Figure 1c).

## Weaknesses

### Fatal
None.

### Major

1. **Real-data experiments use simulated stimulations with a simple additive model, not real neural responses to stimulation.** Line 178 states: "For each of the real datasets, we simulated stimulations using an autoregressive function to model a fast rise in neural activity of the perturbed neurons and a slower decay back to baseline levels." The generative model is a_t = 0.8·a_{t-1} + u_t — a linear AR(1) process. The ground-truth stimulus-response mapping S is entirely known and is a function the kernel regression is well-suited to learn. The abstract says the method was "demonstrate[d] on both simulated and real neural data," but the "real neural data" experiments are better described as simulated stimulations overlaid on real background activity. Real neural responses involve network effects, nonlinearities, off-target effects from optical point-spread functions, and state-dependent plasticity that are not tested here. The paper is transparent about this in the methods (line 178) and Discussion (line 252 mentions "simulated effects of arbitrary stimulations"), but the framing throughout overstates what is validated. This matters because the paper's core claim is about a method for real neural stimulation, and the validation addresses only a simplified proxy.

2. **No comparison against alternative stimulus-response modeling approaches.** The only baseline for the S mapping is a "blind" model that ignores stimulation entirely. The paper does not compare against simpler regressors (e.g., linear regression of stimulation effect onto [x, u], Gaussian process regression, or a neural network), which would test whether the kernel regression formulation provides benefits over alternatives. Similarly, no comparison against existing methods for related stimulation design problems (Minai et al. 2024, Wagenmaker et al. 2024, Yang et al. 2021) is provided. Without such comparisons, it is unclear whether the specific kernel regression formulation — which faces a high-dimensional input space — is necessary or advantageous compared to simpler approaches.

### Minor

1. **High-dimensional kernel regression generalization not empirically addressed.** The product kernel in Eq. 7 takes as input the full high-dimensional stimulation vector u (N=130 for electrophysiology, N=592 for calcium imaging). The real-data experiments use the open-loop identity mapping S(u) = Q^T u (line 228), which sidesteps the high-dimensional generalization challenge because the mapping is linear. The closed-loop experiments with a non-trivial learned S use a 3D toy model. The paper does not analyze how the kernel regression estimator degrades as the dimension of u increases, or demonstrate its effectiveness for nonlinear S in the high-dimensional regime it claims to handle.

2. **No ablation of the Orthogonal Procrustes alignment step.** sjPCA adds an Orthogonal Procrustes step (Eq. 2) to stabilize each jPCA plane. Figure 1a compares sjPCA against offline jPCA but not against a streaming baseline without the Procrustes step. An ablation is needed to establish that this design choice improves tracking quality.

3. **Optimization solver details are not provided.** The objective in Eq. 8 is non-convex (cosine similarity) with box constraints, but the paper states only "argmin with box constraints" (Algorithm 1 line 56). The solver, initialization strategy, convergence behavior, and stopping criteria are not described, affecting reproducibility.

4. **Regularization term notation in Eq. 8 is unclear.** The term λ1(‖u‖_0^max - ‖u‖_1) uses non-standard notation ‖u‖_0^max. The description "offset by N to encourage a solution with the number of non-zero elements close to n" would benefit from a clearer mathematical formulation of how this term relates to the desired sparsity level n.

### Trivial
None.

## Nice-to-Haves

- Ablation comparing sjPCA to a direct streaming jCPA without Procrustes alignment
- Analysis of kernel regression performance as a function of stimulation dimension u
- Comparison against a linear regressor for the S mapping
- Specification of the optimization solver (algorithm, initialization, convergence)
- Validation on data with real (not simulated) neural responses to stimulation, or at minimum a more realistic biophysical generative model

## Removed Points

These points were flagged for removal and are kept only for reference:

- "The Feasible case is essentially checking whether the optimization works when the target is known to be achievable" — This is a property of the experimental design, not a weakness. The paper also tests Random (not necessarily achievable) directions and Q0 as separate conditions, so the full set of experiments covers both achievable and potentially unachievable targets.
- "sjPCA contribution is modest" — Subjective opinion without specific anchor. The paper provides evidence of convergence to offline jPCA.
- "The blind model's error spikes during stimulations because it does not account for them" — This is the intended purpose of the comparison: to test whether modeling stimulation improves prediction. It is a valid first baseline.
- Generic strengths from Strength Finder about "addressing an important problem" — Not anchored to specific evidence; removed per filtering rules.

## Novel Insights

Synthesizing the reviews reveals that this paper's core tension is between its genuine technical contribution and its insufficient validation. The framework components (streaming latent spaces, adaptive kernel regression for S, constrained optimization) are individually reasonable and their integration is novel. However, the experimental design evaluates this integration against a bar that is too low for the claims made. The simulated stimulations on real data test the pipeline's ability to handle real background neural activity but not its ability to model real neural responses to stimulation. The baselines (blind model, random stimulation) establish that modeling and optimization help, but not that the specific methods chosen are effective compared to alternatives. The paper would be substantially stronger with either (a) validation on real neural responses to stimulation, or (b) a more honest re-framing as a proof-of-concept framework with explicit discussion of what remains to be validated empirically.

## Suggestions

1. The most impactful change would be to validate the method on data with real neural responses to stimulation, even if the stimulation is simple (e.g., single-site optogenetic or electrical). The paper's core claim is about a method for real neural stimulation, and the current validation addresses only a simulation-based proxy.
2. Compare kernel regression against simpler alternatives (linear regression, Gaussian process regression) for the S mapping, to establish whether the added complexity of high-dimensional kernel regression is justified.
3. Add an ablation of the Orthogonal Procrustes alignment to show it improves over a naive streaming jPCA.
4. Clarify the optimization solver (algorithm, initialization, convergence criteria) and the regularization term in Eq. 8.
5. Add an analysis of how kernel regression performance degrades with increasing u dimension, with the results on the real datasets (N=130, 592) as reference points.

## Score and Decision

**Calibration anchors used (all rounds):**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| A5utJ4xf27 (Brain object localization) | 2.33 | R1 | Much weaker; poor methodology, our paper is clearly better |
| hbon6Jbp9Q (Semantic representations) | 2.33 | R1 | Much weaker; our paper has more concrete contributions |
| eR1119aUlL (MRINE, real-time multimodal) | 4.25 | R1+R2 | Similar "combination of components" structure; our paper has similar validation strength |
| FwW3jqchtY (iSSM, interventional SSM) | 5.00 | R1+R2 | **Most similar**: real stimulation data (stronger validation), theoretical identifiability proof, but lacks baseline comparisons like our paper |
| N83O2FcqzN (TiDeSPL-VAE) | 5.00 | R2 | Mixed reviews (3,3,6,8); similar combination-of-components approach |
| 4ltiMYgJo9 (Closed-loop EEG) | 5.75 | R2 | Innovative framework but validation concerns similar to our paper |
| WQwV7Y8qwa (MR-SDS, switching NLDS) | 5.80 | R1+R2 | More comprehensive experiments, accepted; sets a higher bar |
| 3usdM1AuI3 (BRAID) | 6.25 | R1+R2 | More thorough evaluation, accepted; substantially stronger validation |
| wCUw8t63vH (Spectral learning) | 6.80 | R1 | Rejected but strong; more rigorous theoretical contribution |

**Round 1 bracket:** 4.0–5.5
**Round 2 narrowing:** The closest comparison is iSSM (5.0, rejected), which tests on real photostimulation/microstimulation data — a substantially stronger validation. Our paper has weaker validation (simulated stimulations on real background activity) but a broader framework. The MRINE paper (4.25) has a similar "combination of existing techniques" structure and was rejected. Our paper sits between these two anchors, closer to the lower end because the simulated-stimulation gap is the paper's most significant limitation.

**Final score: 4.5 — Reject**

The paper presents a genuinely novel framework with reasonable individual components, but the experimental validation does not support the central claim of being demonstrated on "real neural data" with respect to stimulation effects. The simulated stimulations via a simple AR(1) model, the lack of comparisons against alternative S-mapping approaches, and the unaddressed high-dimensional kernel regression concern collectively prevent acceptance at a top venue.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>