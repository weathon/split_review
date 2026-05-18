Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces EquiJump, a model that applies two-sided stochastic interpolants to directly bridge consecutive all-atom protein MD simulation time steps, bypassing the need for a Gaussian prior. The model uses an SO(3)-equivariant neural architecture with four prediction heads (drift and noise for both features and coordinates), conditioned on a source protein conformation. On 12 fast-folding proteins, the authors train a single transferable model and evaluate it against the CG-MLFF force-field baseline and, for Protein G, against DDPM, Flow Matching, and one-sided interpolants. The results show substantially lower Jensen-Shannon divergence on slow dynamical observables and meaningful computational speedups.

## Strengths

- **Novel and well-motivated application of two-sided stochastic interpolants to MD step bridging.** Rather than transporting from a Gaussian prior (as in DDPM, flow matching, and one-sided interpolants), EquiJump transports directly between consecutive simulation frames. The controlled comparison on Protein G (Table 1) demonstrates that this design choice yields substantially more accurate long-run distributions (e.g., TIC1 JS=0.004 vs. 0.022 for the best one-sided interpolant, and vs. 0.049 for flow matching). This is the paper's strongest empirical evidence and cleanly isolates the benefit of the two-sided formulation.

- **SO(3)-equivariant all-atom model with strong transferability across 12 proteins.** The model operates on all heavy atoms via a tensor cloud representation with a four-track equivariant architecture. On the 12-protein benchmark, the largest EquiJump model (H=256) achieves substantially lower JS divergence than CG-MLFF across all observables (e.g., TIC1 JS: 0.03 vs. 0.30; RMSD % error: 15.2 vs. 34.7, Tables 2–3). Importantly, CG-MLFF is the only other published transferable model covering these 12 proteins, making this a meaningful advance for the setting.

- **Controlled comparison across generative frameworks under identical architecture.** The paper benchmarks EquiJump against DDPM, flow matching, and one-sided interpolants while keeping the network architecture fixed and only varying the transport formulation (Table 1). This clean ablation convincingly attributes the performance gain to the two-sided interpolant design rather than architectural choices.

- **Explicit analysis of the accuracy–speed tradeoff.** Table 4 and Figure 5 quantify both computational acceleration (3–34× over Amber24) and distributional accuracy, showing that EquiJump achieves JS < 0.1 on TIC components while providing 5–15× speedup. This helps practitioners understand practical deployment regimes.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Sign inconsistency in the noise prediction loss between Equation (6) and Algorithm 1.** Equation (6) (line 91) defines the noise loss as min E[½||\hat{η}||² + **Z·\hat{η}**] with a *positive* cross term. Algorithm 1 (line 142) instead uses `−∇(… + ½||\hat{η}|| − \hat{η}·Z^τ)` with a *negative* cross term, which matches the standard stochastic interpolant formulation from Albergo et al. The algorithm is consistent with the correct training objective, so the implementation is likely fine, but the theoretical equation is wrong. The authors should correct the sign in Equation (6) to `−Z·\hat{η}` (or equivalently `−\hat{η}·Z`). This is not a methodological flaw but a nontrivial presentation error that must be fixed.

- **The SOTA claim, while plausible, would benefit from broader baseline comparisons.** The claim "state-of-the-art results on dynamics simulation with a transferable model on all of the fast folding proteins" is supported against CG-MLFF, which the paper correctly identifies as the only other published multi-protein model on this benchmark. However, several recent deep-learning trajectory models cited in the paper (ITO, F³low, Timewarp, Arts et al. 2023) perform related next-step prediction tasks, though not necessarily as transferable models across 12 proteins. Including even a single-protein comparison against one of these methods would strengthen the claim and situate the work more clearly in the broader literature.

- **MSM convergence diagnostics are not reported.** The evaluation reweights observables using MSMs estimated from 500-step (50 ns) trajectories with lag times of 45–95 ns. The authors note that this reweighting "is extremely sensitive to the correct description of the transition states," but no implied timescale plots or Chapman-Kolmogorov tests are provided to assess MSM convergence. For fast-folding proteins whose slowest relaxation times may exceed 50 ns, this raises a concern about whether the reweighted distributions are trustworthy. Providing convergence diagnostics or reporting unreweighted (raw histogram) observables alongside the reweighted ones would address this.

- **Training-set reweighting details are underspecified.** The paper uses TICA + k-means clustering to reweight training transitions toward rare events, which is a potentially valuable contribution. However, the number of clusters, the method for determining cluster sampling weights, and sensitivity to these choices are not reported. The number of clusters is referenced only via a figure that is not available in the text.

### Trivial

- The norm in Algorithm 1 is written as `½||\hat{η}||` rather than `½||\hat{η}||²` (missing the square). This is a formatting issue.
- The paper does not include a limitations section. A brief discussion of the 100 ps step size, the lack of solvent, and the restriction to pre-computed training trajectories would improve completeness.

## Nice-to-Haves

- Compare EquiJump against at least one of the cited deep-learning trajectory models (ITO, F³low, Timewarp) on a single protein, even if only for raw (unreweighted) observables.
- Report unreweighted (histogram-based) JS divergences alongside the MSM-reweighted ones to provide a direct measure of per-step accuracy.
- Add implied timescale plots or Chapman-Kolmogorov tests for the MSMs used in reweighting.
- Quantify the contribution of solvent removal to the reported speedup (e.g., compare against implicit-solvent MD or a neural force field like MACE-OFF on the same system).
- Provide a clear limitations statement covering step size, solvent handling, and the offline training paradigm.

## Removed Points

These points were raised by reviewers but are removed or downgraded after verification against the paper:

1. **"The paper uses the term 'Two-Sided Stochastic Interpolants' but the setting is conditional, not the generic two-sided."** — Removed. The paper correctly defines ρ₀ = ρ(X^t) and ρ₁ = ρ(X^{t+1} | X^t), which is a valid two-sided setup where the source distribution is the (empirical) distribution of current steps and the target is the conditional distribution of the next step. This is not a limitation.

2. **"CG-MLFF comparison is not apples-to-apples due to different resolution and time steps."** — Demoted to Nice-to-Have. The paper explicitly acknowledges these differences (line 303) and explains why the comparison is still informative. The resolution and time-step differences are inherent properties of the compared methods, not flaws in the comparison design.

3. **"Acceleration estimates should quantify the solvent overhead contribution."** — Demoted to Nice-to-Have. The paper acknowledges that the reference simulation uses explicit solvent (lines 317–318) and compares against MACE-OFF as an all-atom baselines. Quantifying the solvent contribution would be informative but is not required.

4. **Strength Finder's claim about "rigorous evaluation of long-time dynamics via MSM reweighting"** is kept as a supporting strength, as the methodology is standard in the field despite the lack of convergence diagnostics (noted as a minor weakness above).

## Novel Insights

None beyond the paper's own contributions. The key insight — that transporting directly between consecutive MD steps via two-sided stochastic interpolants yields better long-run distributions than transporting from a Gaussian prior — is the paper's own contribution and is well supported by the controlled experiment on Protein G.

## Suggestions

1. **Fix the sign error in Equation (6).** Change "+ Z·\hat{η}" to "− Z·\hat{η}" (or equivalent) to match Algorithm 1 and the standard stochastic interpolant formulation.
2. **Add MSM convergence diagnostics** (implied timescale plots or Chapman-Kolmogorov tests) for the reweighting procedure, or report unreweighted JS divergences alongside the reweighted ones.
3. **Add a brief limitations section** covering the 100 ps step size, the absence of solvent, the offline training paradigm, and the restriction to equilibrium (not kinetic) evaluation.
4. **Strengthen the empirical comparison** by including results from at least one related deep-learning trajectory model (ITO, F³low) on a subset of the benchmark proteins, or clearly scope the SOTA claim to the "transferable model on the 12-protein benchmark" setting.

**Originality:** Good. The application of two-sided stochastic interpolants to direct MD step bridging is novel and the architectural design (four prediction heads with a shared conditioner) is clean.

**Quality:** Good. The experiments are well-designed with controlled comparisons (same architecture, varying transport) and systematic ablations of model capacity. The MSM-based evaluation is appropriate for the field, though missing convergence diagnostics.

**Clarity:** Generally clear. The main weakness is the sign inconsistency between Equation (6) and Algorithm 1, which must be corrected.

**Significance:** High for the computational biology / ML-for-molecular-simulation community. A single transferable model that can simulate 12 proteins at all-atom resolution with 100 ps steps and outperform force-field baselines is a meaningful step forward. The accuracy-speed tradeoff analysis is practically valuable.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>