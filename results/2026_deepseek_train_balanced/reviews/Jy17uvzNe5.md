Now let me produce the final consolidated review.

## Summary

This paper proposes JOBCD, a block coordinate descent framework for optimization under J-orthogonality constraints — a non-convex problem class arising in hyperbolic PCA, structural probes, and knowledge graph embeddings. Two variants are developed: GS-JOBCD (Gauss-Seidel, sequential) and VR-J-JOBCD (variance-reduced Jacobi, parallel). The paper provides convergence theory (oracle complexity under mild conditions, KL-based strong convergence) and derives a closed-form solver for the 2×2 J-orthogonal subproblem via hyperbolic CS decomposition and breakpoint search.

## Strengths

- **First BCD method for J-orthogonality constraints.** Prior methods (CSDM, ADMM, UMCM) are either hard to implement or only guarantee convergence to critical points. The paper shows that BCD is feasible here by reducing the 2×2 subproblem to a tractable 1D search via hyperbolic CS decomposition and a quartic equation solver (Lemma 2.2, Proposition 1). This is a genuine algorithmic contribution.

- **BS-points are provably stronger than critical points.** Theorem 4.2 proves that a block stationary point is always a critical point, but the converse does not hold. This provides a theoretical justification for why the proposed methods may escape poor local minima that trap existing approaches — and the experiments partially corroborate this.

- **Rigorous convergence theory.** The paper delivers oracle complexity bounds (O(Δ₀N/ε) for GS-JOBCD, O(nN + Δ₀√N/ε) for VR-J-JOBCD under PAGE-style variance reduction) and KL-based strong convergence with explicit rates distinguishing the linear-rate regime (σ∈(1/4,1/2]) from sub-linear (σ∈(1/2,1)). The KL analysis includes finite-length properties and bounds that reflect the Jacobi parallel strategy.

- **J-JOBCD achieves the best objective on 7 of 9 HEVP datasets.** In Table 1, J-JOBCD (the deterministic Jacobi variant) dominates across nearly all datasets, often by substantial margins (e.g., w1a: -9.32e+06 vs. CSDM's -5.72e+04). Constraint violations remain comparable, confirming the gains come from better optimization rather than constraint relaxation.

## Weaknesses

### Fatal
None.

### Major

- **VR-J-JOBCD results are completely absent from the experiments despite being a named contribution.** The paper lists VR-J-JOBCD as one of two main algorithmic variants (line 46: "We explore two specific variants"), states it "decrease[s] oracle complexity in the minimization of finite-sum functions," and claims on line 416 that "VR-J-JOBCD outperforms both J-JOBCD and CSDM when dealing with a large dataset." Yet Table 1 and all figures report only GS-JOBCD, J-JOBCD, and CSDM+GS-JOBCD — no VR-J-JOBCD anywhere. For HEVP where N=1, VR-J-JOBCD reverts to J-JOBCD, but HSPP has a clear finite-sum structure (a sum over m² terms) where VR-J-JOBCD would differ from J-JOBCD, yet only convergence curves without method labels are shown. The paper's central claim about its variance-reduced variant is empirically unsupported in the main body.

- **HSPP evaluation lacks any quantitative comparison.** Figure 2 shows convergence curves for HSPP on three datasets, but there is no table of final objective values, no wall-clock measurements, no comparison of constraint satisfaction, and no legend identifying which methods the curves correspond to. The y-axis is unlabeled. This makes it impossible for the reader to assess whether JOBCD actually outperforms baselines on this problem. The paper offers convergence curves as evidence of "efficiency and efficacy" but provides no extractable numbers.

- **The claim that "GS-JOBCD and J-JOBCD consistently deliver better performance" (line 416) is overstated for GS-JOBCD.** On CnnCal (Table 1), CSDM achieves -1.11e+03 while GS-JOBCD achieves -1.07e+03 — CSDM is better. On randn(1000-1000-500), CSDM achieves -1.93e+06 while GS-JOBCD achieves -1.22e+06 — CSDM is substantially better (58% higher objective). The claim is accurate for J-JOBCD (which dominates all baselines), but GS-JOBCD underperforms CSDM on 2 of 9 datasets. The paper should qualify this claim or explain the failure cases.

- **No multiple trials or statistical significance reported.** All results in Table 1 appear to come from a single run. For methods involving random block selection (GS-JOBCD) and random partitioning (VR-J-JOBCD), single-run evaluation does not establish robustness. Standard deviations or confidence intervals are needed to support claims of "consistent" superiority.

- **The w1a result for J-JOBCD is an unexplained outlier.** J-JOBCD achieves -9.32e+06 vs. GS-JOBCD's -9.21e+04 (a ~100× improvement) and CSDM's -5.72e+04 (~160×). This is by far the largest relative gap across all datasets. The paper does not discuss whether this represents a genuinely better solution or a numerical issue (e.g., the objective landscape having extremely deep but narrow valleys that only J-JOBCD finds). Given the constraint violation is also 1.1e-04 for all methods, this warrants explanation.

### Minor

- **The ε-BS-point definition for VR-J-JOBCD depends on algorithm randomness.** Definition 2 defines ℰ(X) for VR-J-JOBCD using an expectation over ιᵗ (the algorithm's internal randomness — block choices and minibatch samples). This means the stationarity criterion for a point depends on which algorithm produced it and its random seed, rather than being a property of X alone. In contrast, the GS-JOBCD criterion depends only on X and the problem data. While this may be a necessary modeling choice for the stochastic setting, it weakens the standard interpretation of the convergence guarantee.

- **The randn datasets are not described.** The paper lists "randn" as a synthetic dataset (line 362) but does not specify how it was generated (dimensions, distribution, random seed). This harms reproducibility.

- **The O(√N) complexity improvement for VR-J-JOBCD stems from a setting where b=N and p≈1/√N, meaning a full gradient is computed roughly every √N-th iteration.** The bound is valid, but the framing should more clearly acknowledge that the method periodically evaluates full gradients rather than being a pure stochastic method.

### Trivial
None.

## Nice-to-Haves

- A discussion of how to handle odd n (the even-n assumption for VR-J-JOBCD is explicit but restrictive — line 150).
- Hyperparameter sensitivity analysis for θ and ς (the Q-matrix scaling).

## Removed Points

The following criticisms were evaluated and removed per filtering rules:

- **Missing ultrahyperbolic knowledge graph embedding experiments from main body** — Removed per rule about parser-stripped appendix sections. The referenced section likely exists in the full submission.
- **Assumption A-i is idiosyncratic/stronger than smoothness** — Removed as factually incorrect: setting H = L_f·I recovers standard L-smoothness; the condition is equivalent to standard smoothness with a potentially structured majorization.
- **Typos/formatting criticisms** — Removed per hard rules (parser artifacts, not author errors).
- **"Hyperparameter guidance missing" framing as a weakness** — Downgraded to nice-to-have; most new methods do not include exhaustive sensitivity analysis.
- **Various speculative or generic criticisms** (e.g., "could the metric be measuring a proxy?") — Removed per filtering discipline.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add VR-J-JOBCD experimental results.** Report objective values, convergence behavior, and wall-clock time for VR-J-JOBCD on at least one finite-sum problem (HSPP is the natural candidate since it involves averaging over m² terms). This is necessary to support the paper's central claim about its variance-reduced variant.

2. **Provide a quantitative table for HSPP** with final objective values, constraint violations, and method identification, analogous to Table 1 for HEVP. Ensure the convergence curves have labeled axes and legends.

3. **Perform multiple random trials** (at least 5) with reporting of means and standard deviations for all randomized methods.

4. **Acknowledge and discuss the cases where GS-JOBCD underperforms CSDM** (CnnCal, randn(1000-1000-500)) and the w1a outlier for J-JOBCD. This strengthens rather than weakens the paper's credibility.

5. **Clarify the ε-BS-point definition** for VR-J-JOBCD — either justify why the expectation over algorithm randomness is necessary, or align it with the GS-JOBCD definition if possible.

6. **Describe how the randn synthetic datasets are generated** (distributions, dimensions, seeds) to enable reproduction.

## Score and Decision

This paper introduces a genuinely novel algorithmic framework for an under-studied problem class. The algorithmic design (reducing 2×2 J-orthogonal subproblems to closed-form via hyperbolic CS decomposition) is technically interesting, and the convergence theory is thorough. However, the experimental evaluation has significant gaps that undermine the paper's claims: VR-J-JOBCD results are entirely absent, the HSPP evaluation lacks quantitative data, claims of "consistent" superiority are not uniformly supported, and there are no multiple trials. The contribution is real but the evidence provided in the main body does not fully match the paper's advertised scope. With substantial experimental strengthening, this could be a strong paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>