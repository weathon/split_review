Now I have all the information I need. Let me synthesize the final review.

## Summary
This paper proposes a real-time streaming framework for designing neural stimulations that perturb latent dynamics in arbitrary directions. The framework integrates three components: (1) streaming dimensionality reduction (including a novel sjPCA method with Procrustes alignment), (2) adaptive nonparametric stimulus-response modeling via kernel regression with temporal discounting, and (3) constrained optimization to select high-dimensional stimulation patterns under sparsity and non-negativity constraints. The method is evaluated on simulated data and real neural recordings (calcium imaging and electrophysiology) with synthetically added stimulation effects.

## Strengths
1. **Adaptive kernel regression with temporal discounting handles non-stationary stimulus-response mappings (Fig. 2e).** The time feature \(K_3(t,T_i)\) in Eq. 7 allows old samples to be discounted, and Figure 2e demonstrates recovery from a 180° flip in the mapping within ~15 s and continuous adaptation during rotation. This goes beyond static input-output models and is a genuine methodological contribution.

2. **Constrained optimization framework for high-dimensional stimulus design under realistic constraints (Eq. 8, Fig. 4).** The paper formulates stimulus selection as minimizing angular misalignment with a desired latent direction, subject to non-negativity \(0 \le u \le 1\) and an \(\ell_1\) relaxation of the \(\ell_0\) sparsity constraint. Figure 4a shows that designed stimuli achieve a median angle of ~20° between observed and desired response, while all random baselines exceed 70°. This joint handling of excitation-only, per-neuron limits, and target-count constraints is new in this setting.

3. **Novel streaming jPCA (sjPCA) with Procrustes stabilization (Section 2.1, Fig. 1a).** The paper derives an online solution to the jPCA problem using the Sherman-Morrison formula and adds Orthogonal Procrustes steps to stabilize individually discovered rotation planes. Figure 1a shows convergence to the offline jPCA fit within ~5 s, enabling real-time tracking of rotational dynamics that was previously only possible offline.

4. **Parallel evaluation of multiple latent representations and dynamical models (Section 2.2, Fig. 1c).** The algorithm tracks predictive error for sjPCA, proSVD, and mmICA simultaneously and can adaptively select the best-performing representation at each timepoint. This is a practical capability for experiments where the appropriate latent structure may not be known in advance.

5. **Real-time computational efficiency (<10 ms average, <100 ms worst-case).** The runtime validation is explicit and verifiable, making the method plausibly compatible with closed-loop in vivo experiments.

## Weaknesses
### Fatal
None.

### Major
1. **The "real neural data" experiments use simulated, not real, stimulation effects.** Section 4 states: "For each of the real datasets, we simulated stimulations using an autoregressive function to model a fast rise in neural activity... \(a_t = 0.8 \cdot a_{t-1} + u_t\)." The stimulus-response function on real data is therefore a known, linear AR process — not an unknown, nonlinear, high-dimensional biological response. The paper is transparent about this, but the evaluation does not test the method's ability to handle the unmodeled complexity (state-dependence, cross-neuron interactions, network-wide side effects) that real stimulations would produce. The abstract states "demonstrate our approach on both simulated and real neural data" without qualifying that the stimulation effects on real data are synthetic, which could mislead readers. The method's practical value depends on handling real biological complexity, and the current evidence does not address this.

2. **No comparison to existing adaptive stimulation methods.** The introduction cites Yang et al. (2021), Minai et al. (2024), Wagenmaker et al. (2024), and Draelos & Pearson (2020) as relevant prior work, yet the experimental evaluation compares only against random baselines (single neurons, random groups, shuffled versions) and a blind model that ignores stimulation entirely. The reader cannot assess whether the kernel-regression-plus-optimization framework offers any advantage over, e.g., a Gaussian process-based Bayesian optimizer or an active learning scheme that explicitly balances exploration and exploitation. The marginal benefit of the proposed approach over existing alternatives is unquantified.

3. **The main optimization results (Fig. 4) assume an identity stimulus-response mapping.** The paper states: "The above experiments assumed that the result of a stimulation \(u\) was simply its projection into the latent space \(S(u) = Q^\top u\)." This sidesteps the core challenge the paper claims to address — learning unknown, potentially nonlinear stimulus-response mappings. While closed-loop results with learned mappings are presented in Figure 5, they are limited in scope: only 10 experiments with 100 stimulations each, and the "non-trivial" mapping is not described in the main text (the nature of this mapping is deferred to an appendix that is not available in the review copy). The claim that the non-trivial mapping is "about as easy to learn" as the simple one is itself suspicious and warrants more careful characterization.

### Minor
1. **The closed-loop evaluation is too limited to establish generalization.** Figure 5 uses only 10 experimental runs with ~100 stimulations each. The non-trivial mapping is not defined in the main paper, and the result that a simple (presumably linear) and non-trivial (presumably nonlinear) mapping are equally easy to learn for a nonparametric estimator needs more thorough investigation and explanation.

2. **The \(\ell_1\) relaxation of the sparsity constraint is acknowledged but not evaluated.** Equation 8 uses \(\lambda_1(\|u\|_0^{\max} - \|u\|_1)\) to encourage a target number of non-zeros, but the paper does not characterize how well this relaxation approximates the desired \(\ell_0\) constraint in practice. No histograms of the number of nonzero elements in designed stimuli are provided, and the parameter \(\|u\|_0^{\max}\) is defined in a notationally unclear way (appearing as \(n\) in the text and \(\|u\|_0^{\max}\) in the equation).

3. **The kernel regression's computational scaling with number of stored samples is not discussed.** The runtime benchmark (<10 ms) implies a small number of stored examples, but as observations accumulate, each prediction becomes \(O(N)\) in the number of stored samples. The time kernel can discount old samples, but the paper does not discuss mechanisms (e.g., forgetting, inducing points, or budgeted storage) that would maintain real-time performance over long experiments.

### Trivial
- The notation \(\|u\|_0^{\max}\) in Eq. 8 is not explicitly defined (the text mentions "\(n\)" as the target number of nonzeros).
- The "plane of highest rotation" for jPCA error measurement (Fig. 1a) is not a standard concept and could benefit from a brief definition.

## Nice-to-Haves
- A demonstration on a nonlinear dynamical system simulator (e.g., a rate model with network connectivity) where stimulations have biologically plausible effects (transient activation, activity spread, temporal delays) would substantially strengthen the core claim that the method works with unknown, nonlinear stimulus-response mappings.
- Comparison against at least one existing adaptive stimulation method from the cited prior work (e.g., a Bayesian optimization baseline).
- Learning curves over more stimulations with error bars across random seeds, and clearer characterization of the "non-trivial" closed-loop mapping.

## Removed Points
- **"The paper's own optimization is compared only to random selection."** — This is retained as Major weakness #2. The companion claim that "there is no comparison to existing adaptive stimulation methods" is factually correct and retained.
- **"This is not a test of whether the method can learn the true stimulus-response mapping in a real biological system"** — Retained as Major weakness #1, though softened from the harsh critic's "Structural/Fatal" framing since the paper is transparent about the simulation.
- **"The claim of demonstrating the method on real neural data is invalidated"** — The paper says "simulated stimulations" explicitly in the methods; "real neural data" in the abstract refers to real recordings, not real stimulations. This is a limitation, not an invalidation. Retained as Major.
- **Criticism of the sjPCA derivation being "sketchy"** — The Sherman-Morrison update and Procrustes alignment are described at a level appropriate for a main-text methods section, with more details presumably in the appendix (which the parser strips). Removed.
- **"The kernel length scales are tuned by stochastic coordinate descent... this may overfit"** — Speculative without evidence. The paper notes they are "optionally tuned," and coordinate descent on RBF length scales is standard practice. Removed.
- **"The 180° flip is an extreme change; most real nonstationarity is likely subtler"** — The paper also tests continuous rotation (a subtle drift scenario), so this criticism is inaccurate. Removed.
- **Pure formatting nitpicks** about missing appendix content or typos — removed per the hard rules.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the key tension: the paper presents a well-motivated, technically coherent framework with several novel components (sjPCA, temporally weighted kernel regression, parallel latent tracking), but the evaluation relies on simulated stimulation effects grafted onto real recordings, leaving the method's performance on genuine biological stimulus-response mappings untested. This gap — between the framework's ambition and its validation — is the central issue that the reviews correctly identify, though some individual criticisms overstate the severity.

## Suggestions
1. Either run a real closed-loop stimulation experiment (even a simple one) or replace the synthetic AR stimulation on real data with a more realistic nonlinear simulator (e.g., a network rate model) where the stimulus-response mapping is genuinely unknown, high-dimensional, and state-dependent.
2. Implement and compare against at least one existing method — a Gaussian process Bayesian optimizer (related to Minai et al. 2024) would be a natural baseline for the stimulus selection problem.
3. Expand the closed-loop evaluation: report learning curves over many more stimulations, show variation across random seeds, and clearly define the "non-trivial" stimulus-response mapping in the main text.
4. Include an analysis of the L1 relaxation's effectiveness: show histograms of the number of nonzero elements in designed stimuli and discuss how well the relaxation approximates the desired L0 constraint.

## Score and Decision

**Calibration anchors:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| uTJ7jlK4Op (SPIRE) | 2.80 | R1 | Weaker — poorly justified method for a different problem |
| kc5jbYHedw (STEER) | 4.50 | R1/R2 | Similar: both are framework papers with synthetic+real validation, but STEER has real DBS data; this paper has clearer presentation but weaker stimulation validation |
| HnPrgFlRww (BREM-NET) | 5.00 | R2 | Slightly stronger: more thorough evaluation with baselines |
| 7jdmXx869Q (MindPilot) | 5.50 | R1/R2 | Stronger: includes real human closed-loop experiments |
| S4B7Iq7S3C (Microstimulation) | 6.00 | R1 | Stronger: actual microstimulation in monkeys with behavioral readout |

**Round 1 bracket:** [3.5, 7.5] — the paper is clearly above the 1.0–3.33 cluster and clearly below the 8.0+ cluster.

**Round 2 narrowing:** The paper is most comparable to STEER (4.50) and weaker than MindPilot (5.50) and the Microstimulation paper (6.00). It has a solid framework contribution but the evaluation gaps (simulated stimulations, no method comparison, limited closed-loop) are significant enough to place it below the acceptance threshold.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>