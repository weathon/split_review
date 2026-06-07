Here is my consolidated final review.

---

## Summary

This paper proposes Generalized Schrödinger Bridge Matching (GSBM), an alternating optimization algorithm that extends existing Schrödinger bridge matching methods (SBM, DSBM, rectified flow, flow matching) to incorporate task-specific state costs $V_t$ — the Generalized Schrödinger Bridge problem. The key technical contribution is reformulating Stage 2 of the alternation as a conditional stochastic optimal control (CondSOC) problem, which generalizes prior matching methods (which assume $V_t = 0$) and can be solved efficiently via a Gaussian path approximation parameterized by low-dimensional splines, optionally debiased via path integral resampling. GSBM is evaluated on crowd navigation, LiDAR surface navigation, opinion depolarization, and unpaired image translation.

## Strengths

- **CondSOC formulation (Proposition 2) that unifies prior matching algorithms as special cases.** The paper shows that Stage 2 of GSB optimization can be recast as a conditional stochastic optimal control problem (Eq. 6), and Table 1 demonstrates that when $V_t = 0$ this collapses to Brownian bridges (DSBM) and, with $\sigma \to 0$, straight lines (Rectified Flow). This is a genuine theoretical generalization and the paper's central intellectual contribution.

- **Feasibility preservation throughout training, with empirical evidence.** Figure 2 directly tracks $\mathcal{W}_2(p_1^\theta, \nu)$ during training on three crowd-navigation tasks. GSBM maintains near-zero Wasserstein distance to the target throughout, while DeepGSB shows large oscillations and occasional divergence. Figure 3 further illustrates this qualitatively. Theorems 5 and 6 provide theoretical grounding for this desirable behavior.

- **Computational efficiency of the spline-based approximate solver.** The spline parameterization uses $K \le 30$ control points, and runtime profiling on AFHQ (Table tb:runtime_perc) shows that solving CondSOC accounts for only 0.5% of total wallclock time. This contrasts favorably with DeepGSB, which requires caching entire discretized SDEs. On Stunnel, the explicit matching loss $\mathcal{L}_{\mathrm{exp}}$ is 2.76× faster than $\mathcal{L}_{\mathrm{imp}}$.

- **Closed-form analytic solution for quadratic $V_t$ (Lemma 3).** Lemma 3 derives exact coefficients for the optimal Gaussian path under quadratic $V(x) = \alpha \|\sigma x\|^2$, recovering Brownian bridges as $\alpha \to 0$ and straight lines as $\alpha, \sigma \to 0$. This provides a principled initialization and strengthens the connection to prior work.

- **Diverse experimental validation across distinct problem classes.** The paper evaluates on four qualitatively different tasks with distinct $V_t$ forms: mean-field interactions (crowd navigation), geometric manifold costs (LiDAR), latent-space semantics (AFHQ images), and high-dimensional opinion dynamics (1000-dim). Each tests a different aspect of the claims.

## Weaknesses

### Fatal

None.

### Major

- **The convergence theory (Theorems 5-6) is for exact subproblem solutions, while the algorithm uses approximations in both stages without analyzing whether guarantees are preserved.** Theorem 5's monotonic non-increasing property is stated generically, but in practice Stage 1 uses $\mathcal{L}_{\mathrm{exp}}$ which the paper itself notes "only upper-bounds the objective of Stage 1" (line 254), and Stage 2 uses the Gaussian path approximation (a variational approximation) rather than the exact CondSOC solution (except for quadratic $V_t$). The paper does not discuss whether the monotonicity or fixed-point properties are preserved under these combined approximations, nor does it provide empirical evidence tracking the GSB objective across iterations to verify monotonic decrease. This disconnect between the theory (exact subproblems) and practice (approximate solvers) is a significant gap that the authors should address in a rebuttal.

- **Most quantitative comparisons lack error bars, variance estimates, or statistical significance tests, weakening the empirical claims.** The FID comparison (Table tb:fid) reports single values (GSBM: 12.39, DSBM: 14.16) with no number of runs or variance. The LiDAR objective values (GSBM: 6209, DeepGSB: 7747) are single numbers. The opinion depolarization claim of "almost half the objective value" is given without numerical values for DeepGSB. Only the PI resampling ablation (Table tb:aba-pi) reports standard deviations over 5 trials. For a paper making strong empirical claims ("significantly improved scalability," "stable convergence"), the evidence would be substantially strengthened by error bars on all quantitative results.

### Minor

- **The CondSOC approximation quality is not characterized.** The Gaussian path approximation is the core of GSBM's practical advantage, yet the paper provides no experiments quantifying how close this approximation is to the true CondSOC solution for settings where it can be verified (e.g., quadratic $V_t$ where Lemma 3 gives the exact answer). While the PI resampling ablation partially addresses this, a direct comparison against known ground-truth solutions would help readers understand when the approximation is trustworthy and where it breaks down.

- **DeepGSB is excluded from the most realistic high-dimensional task (AFHQ).** The paper states "as the high dimensionality greatly impedes DeepGSB" (line 696), which is a fair practical limitation, but it means the most convincing high-dimensional application lacks a comparison against the primary baseline for the same problem class. While DSBM (a special case of GSBM) provides a meaningful baseline showing what $V_t$ buys, a direct comparison to an alternative GSB solver on this task would strengthen the evaluation.

- **The opinion depolarization result lacks concrete numerical values.** The paper claims GSBM achieves "almost half the objective value" relative to DeepGSB (line 744) but provides no numerical objective values for either method, only qualitative visualizations. This makes the claim difficult to assess quantitatively.

- **The FID comparison is described as "a measure of feasibility"** (line 712-713), but FID measures distributional similarity/generative quality rather than whether the boundary condition $p_1^\theta = \nu$ is satisfied. The Wasserstein distance $\mathcal{W}_2(p_1^\theta, \nu)$ used elsewhere is the more appropriate metric for feasibility.

### Trivial

None.

## Nice-to-Haves

- Empirically demonstrate the monotonic convergence property by tracking the GSB objective across alternating iterations.
- Provide a direct wallclock comparison (seconds per iteration) between GSBM and DSBM on the same hardware for the same task, rather than just percentage-based profiling.
- Include a synthetic experiment on a non-quadratic, non-convex $V_t$ with a known or analytically tractable CondSOC solution to characterize the approximation error.

## Removed Points

These points were raised by one or both reviewers but are removed after filtering:

- **"Convergence theory does not apply to the algorithm at all"** — The harsh critic framed this as a fatal disconnect. However, the paper does acknowledge the Stage 1 approximation (line 254, "only upper-bounds the objective"), and the theory-vs-practice gap is common in ML papers. This is retained as a **Major** weakness but not fatal.
- **"The specific form of V(x) in Lemma 3 is restrictive/unusual"** — The form $V(x) := \alpha\|\sigma x\|^2$ is not unusual; it's a standard quadratic form written in the paper's notation. This is a pure style nitpick and removed.
- **"Runtime overhead claim interpretation"** — The critic argued the 0.5% figure requires assuming other steps are identical between GSBM and DSBM. The paper states this clearly and the claim is reasonable. Removed as a nitpick.
- **"Missing related works"** — Removed per instructions.
- **"Pure formatting/style nitpicks"** — Removed per instructions.
- **"DeepGSB hyperparameter selection not specified"** — This level of implementation detail is standard to defer to the appendix. Removed per instructions (trivial implementation detail).
- **"The derivation of CondSOC factorization could be more explicit"** — This is a presentation preference, not a weakness. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews identify convergence-theory-vs-practice disconnect and missing error bars, which are common weaknesses rather than novel insights.

## Suggestions

1. Report standard deviations or confidence intervals for ALL quantitative results (FID, LiDAR objectives, opinion objectives) by running with multiple seeds. This is the single most impactful improvement for the empirical claims.

2. Add an experiment validating the CondSOC approximation quality: for a problem where the true CondSOC solution is known (e.g., quadratic $V_t$ from Lemma 3), compare the Gaussian path approximation against the ground truth, showing how the approximation error varies with $V_t$ complexity.

3. Track the GSB objective value across alternating iterations and visually demonstrate (approximate) monotonic decrease, connecting Theorem 5 to practice. If monotonicity is not observed, discuss why.

4. Provide direct numerical values for the opinion depolarization comparison (both methods' objective values) rather than only a relative claim.

5. Consider reporting the Wasserstein distance $\mathcal{W}_2(p_1^\theta, \nu)$ for the AFHQ task in addition to FID, for consistency with the feasibility framing and the crowd navigation experiments.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>