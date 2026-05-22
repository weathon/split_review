Now let me write the consolidated review.

## Summary
This paper develops a real-time framework for designing high-dimensional neural stimulations that perturb low-dimensional latent dynamics in desired directions. The method integrates streaming latent space construction (including a novel streaming jPCA with Orthogonal Procrustes stabilization), a nonparametric kernel regression model of the stimulus-response mapping that handles non-stationarity, and a constrained optimization procedure that solves for stimulation patterns under sparsity and non-negativity constraints. The framework is evaluated on simulated data and two real neural datasets (calcium imaging and electrophysiology) with simulated stimulation responses, demonstrating end-to-end runtimes below 100 ms.

## Strengths
1. **Novel streaming jPCA (sjPCA) with Orthogonal Procrustes stabilization**: The paper introduces a principled streaming variant of jPCA (Eq. 2) that identifies rotational planes in real time and converges to the offline fit within seconds (Fig. 1a). This is a genuinely useful contribution that fills a gap — prior methods could only identify rotational dynamics offline.

2. **Nonparametric stimulus-response mapping that handles non-stationarity**: The kernel regression model in Eq. (7) with a temporal kernel K₃ adaptively discounts old samples, and the paper demonstrates recovery from both a sudden 180° flip (Fig. 2e, "Flip") and continuous drift (Fig. 2e, "Rotate") within ~15 s. This addresses a real practical concern in closed-loop experiments that most prior models ignore.

3. **Constrained optimization for feasible high-dimensional stimulation design**: The optimization in Eq. (8) accounts for practical constraints (non-negativity for excitation-only opsins, approximate L₀ sparsity via L₁) and produces stimuli that reliably align with desired latent directions. Figure 4b shows 517/600 feasible directions achieve misalignment <1°, demonstrating that the framework can find effective stimuli despite severe constraints.

4. **Real-time feasibility and parallel latent space evaluation**: End-to-end runtimes average <10 ms per timepoint (Section 3), which is necessary for future in vivo use. The parallel evaluation of multiple latent spaces (proSVD, sjPCA, mmICA) with adaptive selection (Bubblewrap, Fig. 1c) is a pragmatic design choice for handling uncertainty about the "right" representation.

## Weaknesses

### Major

1. **Optimization objective formulation is ambiguous and potentially inconsistent with stated goals**: Equation (8) defines the objective ℒ(u) = −cos(v, s(u)) + λ₁(‖u‖₀^max − ‖u‖₁). The paper states this encourages sparsity (i.e., stimulating roughly n out of N neurons). However, minimizing λ₁(‖u‖₀^max − ‖u‖₁) penalizes *small* ‖u‖₁ and rewards *large* ‖u‖₁ — the opposite of a standard sparsity penalty. If ‖u‖₀^max = N (the total number of neurons), this term encourages maximally dense solutions. If ‖u‖₀^max is a small target number (like 30), the term still offers no upper bound: once ‖u‖₁ exceeds the target, further increases *reduce* the penalty. The paper needs to (a) define ‖u‖₀^max explicitly, (b) clarify whether the sign is correct or whether a standard L₁ penalty (+λ₁‖u‖₁) was intended, and (c) if the formulation is correct as written, explain why it does not steer solutions toward density. The empirical results show the method produces sparse solutions in practice, but the discrepancy between the equation and the stated intent undermines confidence.

2. **No real closed-loop stimulation experiments**: The evaluation on real neural data (calcium imaging and electrophysiology) uses *simulated* (injected) stimulation responses — an autoregressive function adds artificial effects to existing neural traces. The paper therefore demonstrates that the method can learn a hand‑crafted additive function, not that it can model or control real biological responses under stimulation (nonlinearities, state-dependent effects, opsin expression variability, cross‑talk, etc.). The paper acknowledges this limitation ("our real data experiments were performed offline") but the core contribution of the paper — closing the loop for stimulation design in live neural systems — is not empirically tested in any biological preparation. Even a test on a previously published optogenetic dataset with real stimulation (of which several exist) would substantially strengthen the evidence.

3. **Weak baselines for stimulation optimization**: The comparisons in Fig. 4a are against random single-neuron stimulation, random group stimulation, and shuffled versions of the authors' own optimized stimuli. These are strawman comparisons. Several methods for stimulus selection in neural systems (e.g., Bayesian optimization, active learning, greedy search over candidates) are cited in the introduction (Minai et al. 2024, Wagenmaker et al. 2024, Yang et al. 2021) but none are used as comparators. To establish that the proposed optimization offers an advantage over reasonable alternatives, the paper should compare against at least one non‑trivial baseline (e.g., greedy selection of top‑k neurons by their latent projection weight, or constrained optimization without the learned response model).

### Minor

1. **Missing solver details for the optimization**: The algorithm box says "Solve with box constraints" but does not specify the optimizer (gradient-based? subgradient? coordinate descent?), convergence criteria, or how non‑differentiability of the L₁ norm at zero is handled. The objective is non‑convex (cosine alignment term + sparsity term), so solver behavior matters for reproducibility.

2. **No statistical testing or confidence intervals**: Comparisons across violin plots (Fig. 4a) are reported qualitatively ("outperforms random methods") without significance tests, confidence intervals, or effect sizes. Given the variability visible in the plots, quantitative claims need statistical support.

3. **No ablation of the temporal kernel**: The paper claims the K₃ time kernel allows adaptation to non‑stationary S, but never compares against a version without the time feature. This would isolate the contribution of temporal adaptation from the base kernel regression.

### Trivial

1. The notation "offset by N" (Section 2.4) is confusing — it is unclear whether N refers to the total neuron count or some target sparsity level n. Clarify.

## Nice-to-Haves
- A synthetic closed-loop simulation where the true S is unknown to the algorithm and changes after the learning window (as in the toy model, Fig. 2) would better demonstrate that the learned mapping supports reliable perturbation, not just prediction.
- Reporting λ₁ values and kernel length scales would aid reproducibility.
- A comparison of performance across the three dynamical models (KF, VJF, Bubblewrap) in the stimulation setting (currently only KF results are shown).

## Removed Points
- *Criticism that the streaming convergence experiments are "trivial":* REMOVED — comparing a streaming method to its offline counterpart is standard and necessary validation; it is not a weakness.
- *Criticism about not testing nonlinear latent spaces (Discussion mentions this as a limitation):* REMOVED — the paper explicitly scopes this out and the framework is modular.
- *Criticism about the stimulation design selecting from a small set of pre-determined stimuli:* REMOVED — the paper is specifically about continuous optimization, not discrete selection.
- *"The real-time feasibility claim is overstated because it only shows runtime, not biological control":* WEAKENED — runtime is a necessary condition for real-time use; the real issue is the lack of real stimulation experiments, captured above as Major weakness #2.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Clarify the optimization objective in Eq. (8): define ‖u‖₀^max explicitly, verify the sign of the sparsity penalty, and explain why the formulation produces sparse solutions as claimed.
2. Add at least one non‑trivial baseline for stimulation optimization (e.g., greedy selection or constrained optimization without a learned model).
3. If real closed-loop experiments are infeasible for the revision, consider testing on a published optogenetic dataset where real stimulation was applied (several exist in the literature).
4. Report solver details (optimizer type, hyperparameters, convergence criteria) for reproducibility.
5. Add significance tests or confidence intervals to the main experimental comparisons.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor ID | Avg Score | Round | Comparison to this paper |
|-----------|-----------|-------|--------------------------|
| IQIN8MwTWO | 2.00 | R1 (low) | Much weaker — basic ML pipeline on EEG data with no real-time component |
| wCBNxp1qWe | 2.00 | R1 (low) | Much weaker — offline-only whole-brain fitting |
| Bf6wHMSBAz | 3.00 | R1 (low) | Weaker — Hebbian learning for BCI, more narrow scope |
| VlTHxRcP3A | 1.00 | R1 (low) | Much weaker — basic neural decoding with no stimulation |
| kc5jbYHedw | 4.50 | R1 (mid) / R2 | Comparable — STEER paper on plasticity inference under stimulation; similar depth but has real DBS data |
| S4B7Iq7S3C | 6.00 | R1 (mid) / R2 | Stronger — model-guided microstimulation with actual primate experiments and behavioral validation |
| 7dvYWzOiEu | 7.20 | R1 (mid) | Much stronger — deep kernel GP theory, rigorous |
| theeeNBSTG | 5.50 | R1 (mid) / R2 | Slightly stronger — CMLR has cleaner methodology and stronger baselines |
| tlA3GKpMHT | 4.00 | R2 (mid-low) | Weaker — DLFM withdrawn, overlaps with prior art |
| 6YktIxJTJr | 4.00 | R2 (mid-low) | Weaker — SYNAPSE is a simulation benchmark only |
| iM4o9a83F7 | 7.33 | R2 (mid-high) | Much stronger — rigorous dimensionality estimation theory |
| xZNoeX0z9f | 6.50 | R2 (mid-high) | Much stronger — Riemannian optimization, rigorous theory |

**Round 1 bracket:** Between 3.5 and 7.5 (clearly above the low-band rejects, clearly below the high-band theory/real-experiment papers).

**Round 2 narrowing:** Compared against comparable papers, this paper is below Model-Guided Microstimulation (6.00, has real experiments) and CMLR (5.50, cleaner baselines), comparable to STEER (4.50), and above DLFM/SYNAPSE (4.00). The weaknesses are real but fixable, and the contributions (sjPCA, nonparametric response model, constrained optimization framework) are genuine.

**Final score:** 5.0 — marginally above the acceptance threshold. The paper addresses an important problem with a well-motivated architecture and has genuine novel components, but the evaluation has substantial gaps (simulated stimulations only, weak baselines, ambiguous optimization formulation) that must be resolved before the claims can be fully supported.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>