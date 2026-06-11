Now I have a clear picture from both rounds of anchoring. Let me synthesize and assign the final score.

**Round 1 bracket:** The paper sits between the iSSM paper (5.00, interventional models with theory but comparison gaps) and BRAID (6.25, more thorough experiments, accepted). Initial bracket: **4.5–6.0**.

**Round 2 narrowing:** After reading additional anchors in the 4.0–5.5 range, the paper is most comparable to iSSM (5.00) and PdZkfSttGK (5.25). Our paper lacks the theoretical contribution of iSSM but has a more integrated practical pipeline. It has similar evaluation gaps to both. I place it at **5.0**.

Key comparison: The iSSM paper (5.00) tested on *real* interventional data (photostimulation, microstimulation). Our paper only uses *simulated* stimulations on real recordings. This is a meaningful difference that prevents our paper from being scored above 5.0 despite its well-integrated framework.

---

## Summary
This paper proposes an integrated real-time framework for adaptive stimulation of latent neural dynamics. It combines streaming dimensionality reduction (including a novel streaming jPCA algorithm), nonparametric kernel regression to model stimulus-response mappings as a function of latent state, stimulus vector, and time, and a convex-relaxed optimization that designs high-dimensional stimulation patterns under experimental constraints (non-negativity, sparsity, bounded magnitude). The method is evaluated on synthetic data with complex response functions and on two real neural datasets (calcium imaging and electrophysiology) with simulated stimulations.

## Strengths
- **Novel streaming jPCA with principled stabilization**: The sjPCA algorithm (Section 2.1, Eqs 1-2) uses Sherman-Morrison for iterative updates and a per-plane Orthogonal Procrustes step to stabilize discovered rotational planes. Figure 1a shows sjPCA converges to the same subspace as offline jPCA within seconds.

- **Nonparametric kernel regression with temporal adaptability**: The estimator (Eq 7) uses three RBF kernels over latent state, stimulus, and sample age, enabling adaptation to non-stationarities. Figure 2e shows the model recovers within ~15s after a 180° mapping flip and tracks a continuously rotating mapping (1 rev/30s). This temporal adaptability is a genuinely useful feature for real experimental settings.

- **Convex-relaxed optimization with practical constraints**: Eq 8 formalizes stimulus design as alignment maximization subject to non-negativity, L1 sparsity, and box constraints. Figure 4b shows strong quantitative results: for feasible target directions, 517/600 optimizations achieve <1° misalignment between predicted and desired latent displacement, and the predicted error serves as a loose lower bound on observed error (Fig 4c).

- **End-to-end pipeline across modalities with real-time runtimes**: The method is evaluated on calcium imaging (Zong et al., 2022, 592 neurons, 15Hz) and electrophysiology (O'Doherty, 2024, 130 units, 30Hz). Runtimes average <10ms and stay <100ms, confirming real-time feasibility.

- **Closed-loop outperforms open-loop under non-trivial mappings**: Figure 5b demonstrates that when the stimulus-response mapping is non-trivial, closed-loop optimization through the learned mapping yields a higher proportion of observed response aligned with the target direction than open-loop optimization. This validates that learning the mapping adds value beyond naive projection.

## Weaknesses

### Fatal
None.

### Major
- **Simulated stimulations on real data use an overly simple model, creating a gap between motivation and validation.** The paper motivates the framework by citing real-world stimulation complexity (lines 112-113): neurons may lack opsin, point-spread functions cause off-target excitation, network structure produces non-intuitive responses, and mappings may drift. Yet when evaluated on real neural recordings, stimulations are injected via a trivial autoregressive model: y_t = r_t + a_t, a_t = 0.8·a_{t-1} + u_t (line 178). This is linear, additive, has no neuron-to-neuron interactions, no state-dependent gain modulation, and a fixed exponential decay. The toy model experiments (Fig 2) do test more complex response functions (position-dependent perturbation, flips, continuous rotation), but these use synthetic dynamics, not real neural data. The paper cannot fully claim to have demonstrated that its method handles real biological stimulation-response complexity when the real-data tests use a response model far simpler than what the method was designed to handle.

- **No comparisons against existing stimulation design methods, only random baselines.** The paper cites Bayesian optimization (Minai et al., 2024), active learning (Wagenmaker et al., 2024), and Bayesian variational inference (Draelos & Pearson, 2020) as prior approaches for designing neural stimulations. Yet the optimization results (Section 4.2, Fig 4a) compare the proposed method only against stimulating a single random neuron, stimulating random groups of neurons, and shuffling the designed stimulus weights. These are straw-man baselines. Beating random selection demonstrates the method does something informed, but does not establish that it advances the state of the art. Comparing against at least one existing method — or clearly explaining why such comparison is infeasible — would substantially strengthen the paper.

### Minor
- **Parallel latent space tracking is described but never connected to stimulation design in any experiment.** Section 2.2 and Figure 1c present a mechanism for running multiple latent space representations in parallel and adaptively determining which is most predictive. The abstract claims this enables "adaptive selection of stimulations to best distinguish amongst neural subspace hypotheses" (line 9). However, no experiment uses this adaptive selection to inform stimulation design. The capability is demonstrated (heatmaps in Fig 1c) but its utility for the paper's core contribution is never validated.

- **The non-trivial stimulus-response mapping in closed-loop experiments (Fig 5) is never specified in the main text.** Section 4.2 refers to "non-simple" and "non-trivial" mappings (lines 231-238) and references Appendix G for details, but the mapping should be characterized in the main paper so readers can assess the significance of the closed-loop vs. open-loop comparison.

- **The sparsity penalty formulation (Eq 8) could benefit from more explicit discussion.** The term λ₁(‖u‖₀^max - ‖u‖₁) with λ₁ > 0 in a minimization problem encourages entries toward 1 (maximum magnitude), since increasing ‖u‖₁ decreases the objective. With box constraints [0,1], this simultaneously encourages a target number of non-zero entries AND pushes those entries to full magnitude. The dual effect (sparsity + saturation) should be discussed more explicitly.

### Trivial
- The claim that the method learns a mapping "within roughly 10-20 total stimulations" (line 23) is tied to the toy model (Fig 2c) but not quantified for real-data experiments. The abstract should qualify this claim.
- The abstract's statement that the method "will enable the next generation of experiments" (line 23) overreaches relative to the evidence presented.

## Nice-to-Haves
- Hyperparameter sensitivity analysis for kernel regression lengthscales and the λ₁ sparsity parameter would strengthen practical guidance.
- Testing the kernel regression against more challenging simulated response functions on real neural data (e.g., with neuron-to-neuron interactions, state-dependent gain) would substantially close the evidence gap.
- Comparing optimization against at least one existing stimulation design method would better contextualize the contribution.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *"The electrophysiological data paragraph is misplaced"* — This is a parser/formatting artifact; the original submission does not have this issue.
- *"Hyperparameter sensitivity is never examined" as a major weakness* — Moved to Nice-to-Haves; this is a generic concern that applies to most methods papers and does not undermine core claims.
- *"The appendix may specify X but..."* — The parser strips appendices; this is not an author error.
- *"Adaptive selection among parallel latent-space hypotheses" as a standalone strength* — The capability is described but never validated as useful for stimulation design; it conflicts with the verified minor weakness and is insufficiently grounded to stand as a strength on its own.

## Novel Insights
None beyond the paper's own contributions. The integration of streaming latent-space construction, kernel regression with temporal adaptability, and constrained optimization for real-time stimulation design is a reasonably novel combination, though each component individually draws on established techniques.

## Suggestions
- Either validate the parallel latent-space selection experimentally (by showing it improves stimulation outcomes) or reduce its prominence from "contribution" to "infrastructure."
- Define the non-trivial stimulus-response mapping used in closed-loop experiments explicitly in the main text rather than deferring to the appendix.
- Add a discussion of what real-world challenges the current simulated-stimulation evaluation does and does not cover, to properly scope the claims.

## Anchor Comparison

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| eR1119aUlL (MRINE) | 4.25 | R1, R2 | Our paper has more novel contributions and better integration; clearly stronger |
| FwW3jqchtY (iSSM) | 5.00 | R1, R2 | Most comparable: iSSM has theory and real interventional data; our paper has better pipeline integration and real-time focus. Roughly equal. |
| LNp7KW33Cg (HDA) | 5.00 | R2 | Less relevant; our paper targets a more novel problem |
| PdZkfSttGK | 5.25 | R2 | Our paper has clearer contribution and better-integrated results; slightly weaker on validation breadth |
| TVnkjz4MqV (NMR) | 5.50 | R2 | NMR has more extensive experiments (68 sessions); our paper has similar novelty level but less thorough validation |
| WQwV7Y8qwa (MR-SDS) | 5.80 | R1 | More sophisticated modeling and theory; our paper is below this |
| 3usdM1AuI3 (BRAID) | 6.25 | R1 | More thorough experiments and baselines; our paper is clearly below this |

**Round 1 bracket:** 4.5–6.0. **Round 2 narrowing:** The paper is closest to iSSM (5.00) — comparable contributions with similar evaluation gaps. Final score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>