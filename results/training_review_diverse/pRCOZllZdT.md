## Summary

This paper introduces Boltzmann Priors for Implicit Transfer Operators (BoPITO), a framework that incorporates a pre-trained Boltzmann Generator as an equilibrium prior into Implicit Transfer Operator (ITO) learning of transition densities. The method contributes three elements: (1) using the prior to seed many short MD trajectories for data generation, (2) decomposing the score into a fixed equilibrium term and a learned dynamic term with exponential decay ($\hat{\lambda}^N$), and (3) using this decay factor to interpolate between biased/off-equilibrium models and the equilibrium distribution, with the interpolation parameter fitted to match unbiased observables. Experiments on the Prinz potential and alanine dipeptide demonstrate improved sample efficiency (roughly 10× less transition-data to match ITO accuracy) and successful correction of biased dynamics via interpolation.

---

## Strengths

1. **Demonstrated order-of-magnitude improvement in sample efficiency.** Figure \ref{fig:long-term} shows that BoPITO achieves ITO-equivalent accuracy on long-time correlation functions with ~10× less transition-data on alanine dipeptide. The comparison is clean: same data, same architecture, only the score decomposition differs. The result is practically meaningful — it turns a data-intensive method into one viable in data-limited regimes.

2. **Principled score decomposition that separates equilibrium from dynamics.** The decomposition $s_{\boldsymbol{\theta}} = s_{\mathrm{eq}} + \hat{\lambda}^N s_{\mathrm{dyn}}$ (Eq. \ref{eq:bopito-score}) is a clear inductive bias grounded in the spectral decomposition of the transfer operator. Fixing $s_{\mathrm{eq}}$ and learning only $s_{\mathrm{dyn}}$ reduces the effective parameter count, which is the direct mechanism behind the sample-efficiency gain.

3. **Novel interpolation protocol for inverse problems with biased data.** The BoPITO interpolator (Section 3.3) allows recovery of approximate unbiased dynamics from models trained on deliberately biased simulations, by matching a tunable interpolation parameter to an unbiased dynamic observable. Figure \ref{fig:interpolation-correlation} demonstrates successful correction on alanine dipeptide. This is the first such capability for deep generative surrogates of transition densities.

4. **Clear motivation and thorough framing.** The paper clearly identifies a real bottleneck in ITO learning (data hunger), explains why equilibrium priors address it, and situates the contribution well against related work in MSM reweighting, Boltzmann generators, and latent-space simulators.

---

## Weaknesses

### Fatal
None.

### Major

- **Single-exponential approximation limits the generality of the interpolator.** The score decomposition (Eq. \ref{eq:bopito-score}) and interpolator (Eq. \ref{eq:bopito-int-score}) scale the entire learned dynamic component by $\hat{\lambda}^{N_{\text{int}}}$ — a single global exponential factor. Real molecular systems have a spectrum of relaxation rates, and $s_{\mathrm{dyn}}$ encodes contributions from multiple eigenfunctions decaying at different speeds. Scaling uniformly cannot, in general, reproduce the correct relative weighting of fast and slow processes at large lags. The success on alanine dipeptide may rely on it having a single dominant slow mode (the $\phi$ transition). The paper acknowledges this as a limitation (Section 6) but does not characterize the sensitivity to $\hat{\lambda}$ or test on a system with multiple distinct slow processes. This is a **structural limitation of the interpolation claim** — not fatal, but it narrows the conditions under which the approach is expected to work.

### Minor

- **The "order of magnitude" claim does not account for the cost of training the equilibrium prior.** The BoPITO pipeline requires first training $s_{\mathrm{eq}}$ (Section 3.2: "we first train $s_{\mathrm{eq}}$ (if not provided) using equilibrium data"). The headline "one order of magnitude reduction" refers only to the transition-density training phase. A reader could reasonably ask whether the total simulation budget (prior training + transition training) is similarly reduced. The paper would be strengthened by acknowledging this and discussing scenarios where a good prior can be obtained cheaply (e.g., from already-available biased simulations using reweighting, as noted in Section 2 under Boltzmann Generators). As written, the claim is technically accurate about the phase it describes, but the framing under-weights the prior's cost.

- **"Guarantees asymptotically unbiased equilibrium statistics" is stated too strongly.** The model converges to the distribution implied by $s_{\mathrm{eq}}$ as $N \to \infty$, not necessarily to the *true* Boltzmann distribution. If $s_{\mathrm{eq}}$ is imperfect (as all learned models are), the asymptotic distribution inherits those errors. The paper uses a near-perfect prior in experiments, so the results are not affected, but the abstract's phrasing ("guaranteeing asymptotically unbiased equilibrium statistics") and the introduction ("by construction, guarantees asymptotically unbiased equilibrium statistics") overstate the guarantee. The more precise language used in Section 3.2 — "asymptotically samples from an *available* equilibrium model" — is the correct framing and should be used consistently.

- **Time-scale split in Figure \ref{fig:long-term} is not defined.** The caption refers to "short, medium, and long time-scales" without specifying how these ranges are determined (e.g., number of eigenvalues, physical cutoffs). This makes the figure harder to interpret and the results harder to reproduce.

- **Interpolation sensitivity to $\hat{\lambda}$ is not characterized.** The interpolator depends on both $\hat{\lambda}$ (a free hyperparameter) and $N_{\text{int}}$ (fitted to data). The paper reports results for one fixed $\hat{\lambda}$ and does not show whether the optimal $N_{\text{int}}$ or the quality of the correction is robust to reasonable variations in $\hat{\lambda}$.

### Trivial
None.

---

## Nice-to-Haves

- Test interpolation on a system with multiple distinct slow processes (e.g., a small peptide with two dihedral transitions at different rates) to probe where the single-exponential scaling assumption holds or breaks.
- Add a brief discussion of how $\hat{\lambda}$ could be estimated from data (e.g., from the dominant eigenvalue of a Markov state model), rather than treated solely as a free hyperparameter.
- Discuss robustness of the observable-matching procedure to noise or sparsity in the reference observable $O^*_N$.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength Finder's "asymptotically unbiased guarantee" as an unqualified strength.** The strength finder claimed "no prior deep generative surrogate offers this theoretical guarantee" without caveat. Since the guarantee is modulo prior accuracy (per verified weakness #2 above), this claimed strength is kept but subsumed into Strength #1 (the sample-efficiency gain) and the principled score decomposition (Strength #2), with appropriate qualification in the main text.

- **Critic's suggestion to test interpolation on a multi-timescale system.** This is a valid suggestion but more appropriate as a Nice-to-Have than a weakness, since the paper's experiments already demonstrate the method working on a realistic system. Moved to Nice-to-Haves.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. In the abstract and introduction, replace "guarantees asymptotically unbiased equilibrium statistics" with "guarantees asymptotic convergence to the available equilibrium model" or similar language that makes the dependence on prior accuracy explicit.
2. Qualify the "order of magnitude" claim by noting it refers specifically to the transition-density training phase, and briefly discuss the total data budget (prior + transition) in a practical setting.
3. Add a definition of how "short, medium, and long" time-scales are determined in Figure \ref{fig:long-term} (caption or methods).
4. Characterize the sensitivity of the interpolator to $\hat{\lambda}$ — either by showing robustness across a range of values, or by providing guidance on how to estimate it.

---

## Score and Decision

**Originality:** The score decomposition with an equilibrium prior is novel within deep generative transition models. The interpolation protocol is also new.

**Importance:** The problem — reducing the data cost of learning surrogate dynamics — is well-motivated and practically relevant.

**Claims support:** The sample-efficiency claim is well-supported by experiments. The interpolation claim is supported on one system with acknowledged caveats. The "guarantee" language is slightly over-claimed but fixable.

**Soundness:** Experimental methodology is appropriate. Multiple replicates with confidence intervals. Comparisons are fair (same architecture, same data).

**Clarity:** The paper is well-written and clearly structured. The main ideas are communicated effectively.

**Value:** The method fills a real gap — no prior deep generative transition surrogate could leverage equilibrium priors. The 10× data reduction is practically significant.

**Overall:** A solid, well-motivated paper with a principled contribution and convincing empirical validation. The weaknesses are real but not fatal — the major limitation (single-exponential interpolation) is acknowledged, and the minor issues are addressable in revision.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>