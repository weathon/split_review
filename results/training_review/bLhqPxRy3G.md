Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper studies gradient descent on the quadratic reparametrization \(x = u \circ u\) (a diagonal linear network) for solving the squared-residual feasibility problem \(\min_u \frac12\|A(u\circ u)-b\|_2^2\). It shows that the limit point solves an entropy-regularized linear program whose regularization strength is controlled by the initialization, and proves global linear convergence of the discrete-time dynamics under a constant stepsize. The results are connected to mirror descent and the Sinkhorn algorithm.

## Strengths

- **First discrete-time convergence analysis for reparametrized GD on general LPs.** The paper proves global linear convergence (Theorem 3) for gradient descent on a diagonal linear network under only strict feasibility and full row rank of \(A\) — assumptions milder than those in prior work, which typically required infinitesimal stepsizes or restrictive data conditions. The proof combines polyhedral decomposition, Lojasiewicz inequalities for polynomials, and careful bounding of multiplicative updates; this is a genuine technical contribution.

- **Clean characterization of initialization-dependent regularization in the continuous-time limit.** Theorem 1 shows that gradient flow with initialization \(\alpha\) converges to the solution of an entropy-regularized LP where the cost vector is determined by \(\alpha\). This is a crisp result that quantifies the trade-off between approximation accuracy (small \(\alpha\) gives better approximation of the original LP) and convergence speed, as confirmed by the experiments (Figure 2).

- **Explicit connections to mirror descent and Sinkhorn with empirical verification.** Sections 2.2 and 2.3 provide a clear discussion of how reparametrized GD relates to mirror descent (exact equivalence only in the infinitesimal-stepsize limit) and to the Sinkhorn algorithm for optimal transport (shared initialization structure but different update rules). Figure 1 empirically confirms the predicted behavior for small vs. large stepsizes.

## Weaknesses

### Fatal

None.

### Major

- **Experimental evaluation is too thin to support the claimed applications.** The experiments use a single synthetic dataset (\(300\times 3000\), Gaussian random) and compare only against mirror descent. There are no comparisons with standard LP solvers (simplex, interior-point), no basis pursuit recovery benchmarks (e.g., sparse signal recovery with \(\ell_1\)-magic or other solvers), and no numerical experiments for optimal transport whatsoever. The experiments validate the theoretical convergence behavior but do **not** demonstrate that the method is practically useful for the applications (basis pursuit, optimal transport) highlighted in the title and introduction.

- **Scope-claim mismatch.** The paper's framing — "solving linear programming problems using diagonal neural networks" — overstates what is actually established. The method solves the feasibility problem \(\min\|Ax-b\|_2^2\) under reparametrization, and its limit point solves an *entropy-regularized* LP (Theorem 1, Theorem 3), not the original LP. While the regularization can be made small by choosing a small initialization, this comes at the cost of slower convergence, and the general reduction (Remark 1) requires a big-M bound whose computation is not addressed for arbitrary LPs. The paper would benefit from upfront language clarifying that it solves a *regularized approximation* of the LP.

### Minor

- **The discrete-time limit characterization (Theorem 3) is less informative than the continuous-time one.** The perturbation vector \(w\) in the discrete characterization is defined in terms of the trajectory itself (\(w = (A^\top\nu - \log(x^\infty/x^0))/(\eta\log(1/\underline\alpha))\)), so the result is not an *a priori* characterization of the limit purely in terms of problem data. It shows that there exists some bounded perturbation such that the limit solves the perturbed problem, but the bound \(C(A,b,R)\) depends on various constants (Lojasiewicz parameters, Hoffman constant) that are not explicitly quantified. This is acknowledged in the paper (the error term vanishes as \(\eta\to0\)), but the characterization is less actionable than the gradient-flow result.

- **The linear convergence rate \(\rho\) is existential.** Theorem 3 proves that \(f(u^k) \le (1-\rho)^k f(u^0)\) for some \(\rho\in(0,1)\), but \(\rho = 2\mu\eta\sigma^2\) depends on \(\sigma\) (the lower bound on iterates), which itself depends on unquantified constants from the Lojasiewicz analysis. The rate is not explicit.

- **The big-M reduction (Remark 1) has limited practical guidance.** While mathematically valid, the remark does not discuss how to obtain \(M\) without already solving the LP. The statement "for many applications it can be easily computed" is not substantiated. This limits the practical applicability of the reduction for arbitrary LPs.

### Trivial

None worth listing beyond what has been noted above.

## Nice-to-Haves

- Comparison with standard LP solvers (e.g., simplex or interior-point) on a few small LP benchmarks (e.g., Netlib) would substantially strengthen the practical claims.
- Optimal transport experiments (e.g., on random cost matrices with comparison to Sinkhorn) would support the connection discussed in Section 2.3.
- An explicit bound on the discrete perturbation \(w\) in terms of only \(\eta\) and problem dimensions (rather than opaque constants \(C(A,b,R)\)) would make Theorem 3 more useful.

## Removed Points

- *"The paper does not actually solve linear programming problems"* — This is removed/weakened because the abstract accurately states "entropically regularized linear programming problems," and the paper is clear throughout that the limit solves a regularized problem. The framing is slightly overstated in one contribution sentence but not factually wrong.
- *"Connection to mirror descent is not novel"* — The paper explicitly cites prior work establishing this connection; presenting known connections for context is standard practice, not a flaw.
- *"Connection to Sinkhorn is descriptive but lacks analysis"* — It is labeled as a connections/discussion section, not an analytical contribution.
- *"Circularity concern in Lemma 5.5 (iteration-lb)"* — The critic speculates about a potential circularity without identifying a concrete gap. The paper's proof structure is: global-conv-detailed (independent of sublinear rate) → sublinear rate via Lojasiewicz → sum bound → lower bound on iterates → linear convergence. This sequence is logically coherent.
- *"Missing appendix, missing proofs"* — These are parser artifacts; the original submission contains the appendices.
- *Formatting nitpicks, typos, grammar issues* — These are parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the core strengths (the discrete-time convergence analysis is the main contribution) and agree that the experiments are thin.

## Suggestions

1. **Tone down the scope claims** in the title, abstract, and introduction to accurately reflect that the method solves an entropy-regularized LP rather than a general LP, or add a qualifier like "approximately solves."
2. **Add at least one additional experiment set:** either (a) a sparse recovery comparison (baseline: \(\ell_1\)-magic or CVX) on a standard basis pursuit test case, or (b) an optimal transport comparison against Sinkhorn on synthetic cost matrices.
3. **Discuss the big-M limitation** more honestly — acknowledge that the reduction requires knowledge of a bound \(M\) and that finding such a bound may itself be as hard as solving the LP, then either provide examples where \(M\) is easily obtained or restrict the claim to the \(c>0\) setting.
4. **Clarify the discrete characterization** (Theorem 3) by emphasizing that while \(w\) is trajectory-dependent, its norm is bounded and the extra term vanishes as \(\eta\to0\), recovering the gradient-flow characterization.

## Score and Decision

This paper makes a legitimate theoretical contribution — the first rigorous discrete-time linear convergence analysis for reparametrized GD diagonal linear networks solving viability/conic feasibility problems, with a clean characterization of initialization-dependent regularization. The proof techniques (polyhedral decomposition, Lojasiewicz inequalities for polynomials) are non-trivial. 

However, the experiments are minimal (one synthetic setting, no practical LP or OT benchmarks) and the framing overstates the scope (it solves an entropy-regularized approximation, not general LPs). The discrete-time limit characterization is less crisp than one would hope, and the big-M reduction for general LPs lacks practical guidance.

The paper is acceptably strong as a *theoretical* contribution to the implicit bias literature, provided the framing is corrected to match what is actually shown. For a broader venue (e.g., NeurIPS, ICML, COLT), the experimental validation and scope claims would need strengthening; for a more theory-focused venue, the current form is appropriate with minor revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>