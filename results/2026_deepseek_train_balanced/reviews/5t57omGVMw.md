## Summary

This paper studies the problem of sequentially tuning the relaxation parameter ω of SOR (and its symmetric variant SSOR) across a sequence of linear system instances, using only iteration-count feedback. The authors develop two complementary theoretical frameworks: (1) a near-asymptotic analysis that derives surrogate upper bounds on SOR cost, learnable via Tsallis-INF with Õ(T^{2/3}) regret that is dimension-independent; (2) a semi-stochastic analysis showing the expected SSOR cost is Lipschitz in ω via an anti-concentration technique, enabling a novel Chebyshev-regression-based contextual bandit (ChebCB) with Õ(T^{9/11}√n) regret against the instance-optimal policy. The paper provides the first end-to-end learning-theoretic guarantees for tuning an iterative linear system solver.

## Strengths

1. **First end-to-end regret guarantees for tuning SOR parameters.** The paper proves concrete sublinear regret bounds (Theorems 2.1, 3.1) for a bandit algorithm using only iteration-count feedback, covering the full pipeline. Prior theoretical work on data-driven linear solvers (Gupta et al. 2017, Bartlett et al. 2022, Balcan et al. 2022) did not provide such end-to-end guarantees. The near-asymptotic bound is dimension-independent, which is crucial for high-dimensional scientific computing.

2. **Novel technique for proving Lipschitz continuity of expected SSOR cost via anti-concentration.** Rather than using dispersion analysis or bounding predicate complexity, the paper proves Lipschitzness of the expected iteration count by combining (a) Lipschitzness of the error at each iteration and (b) anti-concentration to bound the probability that the residual lands near the tolerance threshold (Section 3.1). This is a genuinely new theoretical approach to handling discrete algorithmic costs.

3. **ChebCB algorithm with sublinear instance-optimal regret.** The paper introduces a novel contextual bandit method (Algorithm 2) combining Chebyshev polynomial regression with SquareCB, achieving Õ(T^{9/11}√n) regret relative to the instance-optimal ω for diagonally shifted systems (Theorem 3.2). This goes beyond prior work that only showed linear instance-adaptivity via convexity.

4. **Optimal Lipschitz-bandit rate achieved despite non-Lipschitz surrogate losses.** The surrogate upper bounds U_t(ω) are only semi-Lipschitz (non-Lipschitz near the optimal ω), yet Tsallis-INF still achieves the optimal Õ(T^{2/3}) Lipschitz-bandit rate by exploiting the monotonic structure (Section 2.3). This extends the applicability of existing bandit analyses.

5. **Extension to preconditioned conjugate gradient.** Section 2.5 shows that the near-asymptotic analysis extends to SOR-preconditioned CG, demonstrating the methodology is not limited to stationary iterative methods. The analysis maintains the same T-rate.

## Weaknesses

### Fatal
None.

### Major

1. **The near-asymptotic assumption (Assumption 1) is central to Section 2's results but lacks theoretical justification.** The assumption states that convergence occurs near the asymptotic regime — i.e., the effective convergence rate is bounded by ρ(C_ω) + τ(1−ρ(C_ω)). The paper characterizes this as "an assumption on ε and b" (line 181) and notes it requires ε to be small enough that the iteration matrix reaches its asymptotic regime before convergence. However, the sole empirical support is Figure 1 (right), showing one matrix dimension, one choice of b, and one measure of asymptocity. The paper provides no theoretical characterization of when the assumption provably holds for a broad class of matrices and right-hand sides. Since the entire surrogate loss framework of Section 2 depends on this assumption, this is a significant gap. If the assumption fails for practically relevant instances, the regret guarantees in Theorems 2.1 and 2.2 are about the wrong quantity. The paper would be much stronger with either a theorem establishing conditions under which the assumption holds, or an analysis of the penalty when it is violated.

2. **The algorithms require knowledge of spectral quantities that may be as expensive to compute as solving the system.** The bandit algorithms require knowing β_t = ρ(I_n − D_t^{-1}A_t), α_max, and ω_smax to set the grid size and parameters (lines 239–241). The paper acknowledges this and compares it to Chebyshev semi-iteration requiring similar estimates, but does not address how a practitioner would obtain these bounds without significant extra computation. Computing spectral radii is itself an expensive operation, which weakens the end-to-end claim that the learning overhead is "likely to be negligible in practice." Without a practical method for estimating these quantities cheaply (e.g., via Gershgorin disc bounds or incremental estimation), the algorithm has an oracle-like requirement.

### Minor

1. **The "head-to-head comparison" claim (Contribution 1, line 65) is overstated.** The paper states as a contribution "the first head-to-head comparison of two leading theoretical approaches to data-driven algorithms applied to the same problem." However, the two approaches are applied under different settings (deterministic vs. semi-stochastic, SOR vs. SSOR, surrogate bounds vs. expected cost) and produce qualitatively different guarantees. There is no dedicated passage that directly compares the guarantees on a shared example, analyzes the trade-offs systematically, or draws a conclusion about which approach is preferable under which conditions. The comparison is implicit in the structure rather than executed as claimed.

2. **The paper claims the procedures are "practical to deploy" (line 382) without empirical support.** The paper explicitly states upfront that it "does not seek to immediately improve the empirical state of the art" (line 36), which is a legitimate scope choice for a theory paper. However, the conclusion's claim of practicality is internally inconsistent with this scope. The reader cannot assess whether the regret bounds are tight enough to matter at realistic T (e.g., T=10^3–10^4), whether the spectral quantities can be estimated cheaply enough, or whether the overhead is actually negligible. A simple synthetic experiment (e.g., on 2D Laplacian systems with varying shifts) showing learning curves would resolve this tension.

3. **The semi-stochastic assumption (b_t i.i.d. from a truncated Gaussian) is strong and not justified for the motivating application.** In PDE simulations (the paper's primary motivation), right-hand sides at adjacent timesteps encode the evolving physical state and are highly correlated, not i.i.d. The paper asserts that convergence "depends more strongly on A_t" (line 50) but provides no evidence. If the b_t vectors correlate with the spectrum of C_ω in a way that anti-concentration fails, the Lipschitz argument collapses. This limits the practical scope of the Section 3 results.

4. **The CG extension (Section 2.5) is thin and acknowledged to be loose.** The analysis applies the same template using a condition-number-based convergence bound, with the acknowledgment that the bounds "match the shape of the true performance less exactly." The section contains no new algorithmic ideas and yields looser bounds, making it more of a remark than a substantive contribution.

5. **The Lipschitz condition in Lemma 1 has an odd restriction (τ ≥ 1/e² or β² ≥ 4/e²(1−1/e²)) that is not discussed.** The paper does not characterize how restrictive this condition is or whether it excludes practically relevant parameter regimes. A brief discussion would help the reader assess the generality of the Lipschitz result.

### Trivial
None.

## Nice-to-Haves

- A simple synthetic experiment (e.g., 2D Poisson equation with varying coefficients) showing learning curves for Tsallis-INF would dramatically strengthen the paper's credibility and resolve the tension between the "theory-only" scope and the "practical to deploy" claim.
- A theoretical characterization of when Assumption 1 provably holds (e.g., a bound on ‖C_ω^k‖₂^{1/k} − ρ(C_ω) in terms of the eigenstructure of C_ω and b) would replace the empirical hand-waving with rigor and elevate the Section 2 contribution significantly.
- Discussion of how to estimate β_t cheaply (e.g., via Gershgorin circle theorem bounds or power iteration with limited steps) would address the oracle-like requirement for spectral quantities.

## Removed Points

- **Weakness about regret bound constants being large/making bounds operationally weak**: The paper explicitly acknowledges this (lines 333, 371, 384) and frames the contribution as asymptotic. Large constants do not invalidate the theoretical contribution, which is the existence of sublinear regret and the technical machinery. The authors' own discussion is sufficient. Removed as the paper already addresses this.

- **Weakness about no experimental evaluation**: The paper explicitly scopes itself as not seeking to improve the empirical state of the art (line 36). For a theory paper at a top venue, lack of experiments is a legitimate scope choice. The "practical to deploy" claim in the conclusion is retained as a minor weakness. The broader "no experiments" criticism is removed as it demands the paper address problems outside its stated scope.

- **Weakness about CG analysis being thin**: Partially kept as Minor #4. The Harsh Critic's broader claim that this is a "missing part" is removed — the CG extension is presented as exactly what it is: a demonstration that the template extends.

- **Strength about dimension-independence from Strength Finder**: Merged into Strength #1. The dimension-independence is a supporting aspect of the main contribution.

- **Strength about head-to-head comparison from Strength Finder**: Removed as it conflicts with the verified weakness that the comparison is overstated. The paper does apply two frameworks to the same problem (which is valuable), but claiming a "head-to-head comparison" oversells what is actually executed.

## Novel Insights

The most incisive observation that emerges from examining the two approaches side-by-side is that the paper's two frameworks operate under fundamentally incompatible strengths: the near-asymptotic analysis yields dimension-independent, interpretable bounds but depends on an assumption that is hardest to satisfy for the very systems that would benefit most from adaptive tuning (those that converge quickly, where the asymptotic regime hasn't been reached). Meanwhile, the stochastic analysis removes this assumption but introduces dimension-dependence and the strong i.i.d. requirement on b_t. This suggests that bridging the gap between interpretable dimension-independence and rigorous cost-based guarantees is the central open challenge, and neither framework fully resolves it. The ChebCB algorithm is a step toward practical CB-based tuning but its Õ(T^{9/11}) rate is so slow that it raises the question of whether any sublinear rate can be tight enough to matter at realistic simulation horizons.

## Suggestions

1. Add a theoretical characterization of the near-asymptotic assumption: derive a bound on ‖C_ω^k‖₂^{1/k} − ρ(C_ω) in terms of the eigenstructure of C_ω and b, clarifying when the assumption provably holds.
2. Address the spectral knowledge requirement by discussing or proving how β_t can be bounded cheaply (e.g., via matrix norm inequalities or incremental estimation).
3. Add a simple synthetic experiment (e.g., 2D Laplacian with diagonal shifts) showing regret vs. T for Tsallis-INF compared to the best fixed ω and the instance-optimal ω. This would resolve the tension between the theory-only framing and the practicality claim.
4. Re-frame the "head-to-head comparison" claim to more accurately describe the relationship between the two frameworks — e.g., "we study the same problem under two complementary frameworks" rather than claiming an executed comparison.
5. Discuss the restrictiveness of the Lipschitz condition in Lemma 1 (τ ≥ 1/e² or β² ≥ 4/e²(1−1/e²)) to help readers assess the generality of the result.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>