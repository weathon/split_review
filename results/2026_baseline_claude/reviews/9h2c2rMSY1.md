## Summary

This paper addresses uncertainty quantification for surrogate models of time-dependent PDEs via conformal prediction (CP). The authors (1) prove that in function spaces, the total variation (TV) distance between PDE solution distributions at any two distinct time points is always maximal (= 1), ruling out exact CP guarantees in the infinite-dimensional setting; (2) show that working with discretized linear PDEs and Gaussian initial conditions yields analytically tractable Gaussian solution distributions at every time, enabling likelihood-weighted conformal prediction (WCP) with exact coverage guarantees; and (3) validate WCP empirically against naïve CP and LSCI on a parametric family of linear PDEs, demonstrating that WCP is the only method with consistent coverage.

---

## Strengths

- **Elegant two-level theory.** The duality between the negative result (mutual singularity in function space, Theorem 4.1) and the constructive positive result (exact Gaussians in finite dimensions, Theorem 4.2) is a compelling and clean theoretical story. The function-space singularity result is a non-trivial contribution that has direct implications for the neural operator literature that habitually reasons in infinite-dimensional spaces.
- **Exact, not approximate, guarantees.** WCP restores *exact* marginal coverage guarantees (not asymptotic ones) for the stated class of problems, while both baselines—naïve CP and LSCI—provide only informal or assumption-dependent coverage. The paper is careful to flag the difference between formal and informal guarantees throughout.
- **Computational efficiency.** WCP takes seconds versus ~40 minutes for LSCI on the same hardware. For real-time safety-critical applications, this is a practically significant advantage.
- **Systematic ablation.** The 3×3 grid of PDE parameters (varying instability and advection/reaction) is a thorough stress test. The comparison clearly shows when and why competing methods break down, and the relationship between the PDE's instability (parameter *a*) and the onset of infinite bands in WCP is well-illustrated.
- **Honest reporting.** The paper forthrightly reports when WCP resorts to infinite bands (e.g., 100% trivial bands for *a* = −0.01 at timestep 15 in Table 1), and frames this as a principled safety response rather than a failure—a reasonable position for safety-critical domains.

---

## Weaknesses

### Fatal
None.

### Major

1. **Restriction to linear PDEs.** The derivation of closed-form Gaussian distributions (Theorem 4.2) and thus the WCP weights (Equation 1) require linearity of the spatial operator. Nonlinear PDEs (Navier-Stokes, nonlinear wave equations, Burgers' equation) are explicitly left as future work. These are arguably the most practically relevant cases in scientific ML, and the paper's framing—"surrogate models for time-dependent physical systems"—is broader than what the method actually covers. No experiments or analysis address how far the linear approximation can be pushed, or what happens when one uses linearized dynamics around a trajectory.

2. **Practical utility lost in the high-instability regime.** For the most dynamically interesting cases (*a* = −0.01), WCP reaches 100% trivial (infinite) bands by timestep 15, providing zero useful uncertainty information for the remaining trajectory. While the paper argues this is preferable to undercoverage, the method essentially abstains at precisely the times when uncertainty information is most needed. No alternative strategy (adaptive recalibration, extrapolation using approximate weights, etc.) is proposed or even discussed, leaving a significant practical gap.

3. **Sensitivity to model knowledge.** WCP requires exact knowledge of the finite-difference matrix **A** and the initial distribution parameters (μ₀, Σ₀) to compute the density ratios. In practice these may be estimated from data or slightly misspecified. No robustness analysis is provided: it is unclear how sensitive coverage is to errors in **A** or in the estimated initial covariance Σ₀.

### Minor

1. **Undercoverage in WCP at moderate instability.** Table 1 shows WCP achieving 0.84–0.88 empirical coverage (against a 0.90 target) at timesteps 15–20 for *a* = −0.005 and *a* = −0.0075. The explanation (stochastic noise from small non-trivial sample size as n∞ rises) is plausible but not rigorously quantified. Given that formal guarantees are the paper's main selling point, these deviations deserve more careful finite-sample analysis.

2. **Naïve CP overcoverage is not explained.** For *a* = −0.005, naïve CP achieves 0.91–0.99 coverage across all timesteps (Table 1), exceeding the 90% target. The paper calls this a method with "no formal guarantees," but in this regime it empirically performs as well or better than WCP. Understanding when/why naïve CP overcoveres versus undercoveres would help practitioners assess when WCP is actually needed.

3. **Real-world validation is limited.** The only real-world experiment uses the heat equation (linear), which is the same PDE used in the theory. A real-world example that actually challenges the method (e.g., a weakly nonlinear system, or a case where the Gaussian assumption is only approximate) would more convincingly demonstrate practical scope.

### Trivial

None worth noting.

---

## Nice-to-Haves

- An experiment where the Gaussian or linearity assumptions are slightly violated (e.g., a nonlinearly perturbed heat equation) to characterize the method's degradation gracefully.
- A brief discussion of strategies for the infinite-bands regime (e.g., falling back to a looser approximate bound, flagging the sample, or triggering recalibration).
- Sensitivity analysis: how much does coverage degrade if Σ₀ is estimated from a finite sample or if **A** is computed from an approximate discretization?

---

## Novel Insights

The most genuinely novel insight is the theoretical juxtaposition between infinite- and finite-dimensional settings. The result that any two Gaussian measures on a function space induced by the heat equation at different times are mutually singular—making TV distance maximally equal to 1 regardless of how small the time gap δ is—is striking and underappreciated in the neural operator and conformal prediction communities. The implication is not merely that exchangeability fails, but that any method relying on approximate distributional similarity (including TV-based corrections) is provably powerless in the function-space limit. The constructive escape via finite-dimensional discretization is clean: discretization makes the measures absolutely continuous and exactly Gaussian, restoring tractability. This binary (singular vs. absolutely continuous) separating function-space from discretized analysis is a useful conceptual tool for future theoretical work in scientific ML.

---

## Suggestions

- Prove or empirically characterize a coverage degradation bound when **A** or Σ₀ are misspecified by ε, to give practitioners actionable guidance on how precisely the PDE parameters must be known.
- For the infinite-band regime, consider reporting an overall coverage metric that includes trivial bands (i.e., coverage = 1 for trivially covered samples), and separate this from non-trivial coverage, to give a more complete picture of method utility.
- Extend at least one experiment to a weakly nonlinear PDE (even as a negative/ablation result) to characterize the failure mode of WCP under nonlinearity.

---

## Score and Decision

WCP addresses a genuine and important gap—non-exchangeability in time-dependent PDE surrogate models—with clean theory, principled methodology, and honest empirical validation. The theoretical results (mutual singularity in function space; closed-form Gaussians under discretization) are genuinely novel and well-executed. The main limitation is the restriction to linear PDEs with known structure and Gaussian initial conditions, which is acknowledged but significantly narrows practical scope. The infinite-bands issue for highly unstable regimes is a practical concern without a proposed resolution. These are real limitations but do not invalidate the contribution within its stated scope.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>