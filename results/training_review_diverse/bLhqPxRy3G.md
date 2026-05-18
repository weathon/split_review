Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies gradient descent on diagonal linear networks (quadratic reparameterization \(x = u \circ u\)) for solving linear programs in standard form \(\min\{c^\top x : Ax=b, x\ge 0\}\) with \(c>0\). The key contributions are: (i) a proof of global linear convergence for discrete-time GD (Theorem 3), (ii) a precise characterization of the limit point as the solution of an entropy-regularized LP whose regularization strength depends on initialization and stepsize (Theorem 4), and (iii) connections drawn between reparameterized GD, mirror descent, and the Sinkhorn algorithm. The discrete-time analysis is the main technical advance over prior work that mostly considered gradient flow.

## Strengths

1. **First global linear convergence guarantee for discrete-time GD on diagonal linear networks solving LPs (Theorem 3).** The paper proves that under mild assumptions (full row rank of \(A\), strict feasibility, sufficiently small constant stepsize) the squared residual satisfies \(f(u^k) \le (1-\rho)^k f(u^0)\). This is a stronger result than prior analyses that focused on gradient flow or infinitesimal stepsizes, and the proof is technically nontrivial.

2. **Exact characterization of the limiting solution with explicit dependence on initialization and discretization (Theorem 4).** The limit point \(x^\infty\) is shown to solve \(\min_x c^\top x + \lambda\sum (x_i\log x_i - x_i) + \frac{\eta}{2}(\lambda+\bar c) w^\top x\) where \(w\) is a bounded nonnegative vector. This reveals the precise role of initialization \(\alpha\) and stepsize \(\eta\) in controlling regularization, extending the continuous-time result (Theorem 2) to capture discrete effects.

3. **Rigorous proof of iterate boundedness using a novel argument (Lemma 3).** Because the objective \(f(u)=\|A(u\circ u)-b\|_2^2\) can have unbounded level sets, standard boundedness arguments fail. The proof combines extreme-point decompositions of the feasible set with entropy inequalities — a nontrivial technical contribution.

4. **Empirical validation of the initialization–accuracy trade-off (Figure 2).** The left panel shows that smaller \(\alpha\) yields a better approximation to the LP solution, while the right panel shows that smaller \(\alpha\) slows convergence. This quantitatively illustrates the theory from Theorems 2 and 4.

## Weaknesses

### Fatal
None.

### Major

1. **The linear convergence rate depends on dimension through the Lojasiewicz exponent in a way that is not discussed, and the guarantee may be vacuous for problem sizes of interest.**  

   The linear rate \(\rho = 2\mu\eta\sigma^2\) (proof of Theorem 3, line 846) depends on \(\sigma\), which is built from constants involving the Lojasiewicz exponent \(\tau = 8\cdot 9^{-(n-1)}\) (Lemma 11, line 1298). For \(n=3000\) (the size used in experiments), \(\tau \approx 10^{-2860}\) — exponentially small in \(n\). This feeds into \(C_1\) and \(C_2\) in Lemma 9 (lines 778, 820), making the bound on \(\sum\|r^j\|_2^2\) from Corollary 6 (line 707) enormous and hence \(\sigma\) potentially astronomically small. The paper does not discuss this explicit \(n\)-dependence or its implications for the practical meaningfulness of the linear rate guarantee. While the rate is mathematically correct, its dependence on \(n\) means the theoretical guarantee can be extremely weak for moderate-sized problems, creating a significant gap between the claimed "linear convergence" and what the bound actually delivers.

   **The paper does state \(\tau = 8\cdot 9^{-(n-1)}\) in the proof of Lemma 11 (it is not hidden), but the implications for the rate constant, the bound on \(\sum\|r^j\|_2^2\), and consequently \(\sigma\) are never discussed in the main text. This is a gap between what the theorem claims and what it guarantees in practice.** (Note: the critic's description of this as "doubly exponential" is inaccurate; \(9^{-(n-1)}\) decays simply exponentially — but the core concern about extreme smallness for moderate \(n\) is valid.)

2. **Limited experimental validation relative to the breadth of claimed applications.**  

   The paper motivates the framework with basis pursuit and optimal transport, and the contributions list claims "supported by simulations" for comparisons with both mirror descent and the Sinkhorn algorithm (Section 1 bullet 3). However, the experiments (Section 4) only test a single random LP with \(c=1_n\) (\(m=300, n=3000\)). There are no experiments on actual basis pursuit (sparse regression) instances, no experiments on optimal transport problems, no comparison with the Sinkhorn algorithm, and no comparison with standard LP solvers (simplex, interior-point, Sinkhorn). The paper's broader claims about applicability to these domains rest entirely on theoretical connections, without empirical evidence that the method works competitively (or even correctly) on such problems. This is a significant overclaim relative to what the experiments support.

### Minor

1. **The reduction from general LPs to the \(c>0\) case (Remark 1) requires a valid big-\(M\) constant, which the paper does not construct in general.** The paper states that \(M\) "can be easily computed from \(\tilde A\) and \(\tilde b\) for many applications" but provides no general construction. For basis pursuit and optimal transport, such bounds are naturally available, but the claim that the framework applies to "general LP problems" is overstated without a practical method for obtaining \(M\) for arbitrary instances. This is a scope limitation rather than a technical error.

2. **The approximation error between reparameterized GD and mirror descent for finite stepsizes is not quantified.** Section 2.2 shows that the two algorithms match in the infinitesimal stepsize limit and differ for finite stepsizes, but the magnitude of the discrepancy (how large \(\eta\) can be before the difference becomes significant) is not bounded. A quantitative comparison would strengthen the connection.

3. **Section 5 ("A comparison with the general convergence theory of GD for nonconvex objectives") is oddly placed** after the experiments and before the proofs. It reads like an extended remark that would fit more naturally near the introduction or the convergence section. Minor organizational issue.

### Trivial
None.

## Nice-to-Haves
- An experiment on a basis pursuit instance (e.g., sparse recovery with \(X\beta = y\)) or an optimal transport problem (e.g., comparing with Sinkhorn on a uniform grid) would substantially strengthen the claimed practical relevance.
- A discussion of whether the Lojasiewicz exponent can be replaced by a dimension-independent bound under additional structure (e.g., strict complementarity) would address the main theoretical concern.
- A quantitative bound on how small \(\eta\) must be to achieve a given approximation accuracy in the limit (Theorem 4), and how this trades off with convergence speed, would be practically useful.

## Removed Points
- **"weakness" about the big-M reduction being "nontrivial in practice"** — kept as Minor (the paper acknowledges the limitation but overstates generality).
- **Critic's claim that \(\tau\) decays "doubly exponentially"** — this is factually wrong (\(9^{-(n-1)}\) decays exponentially, not doubly exponentially), but the underlying concern about the dimension dependence is valid and retained in Major weakness 1.
- **Critic's claim that "The authors treat \(\tau\) as a fixed constant independent of \(n\) throughout the paper"** — the paper does state \(\tau = 8\cdot 9^{-(n-1)}\) in Lemma 11's proof (line 1298), so this is partially inaccurate. However, the paper indeed never discusses the implications of this dependence in the main text, so the core criticism stands.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. In Theorem 3 and the surrounding text, explicitly state the dependence of \(\rho\) on \(n\) via the Lojasiewicz exponent and \(\sigma\), and discuss what this means for practical problem sizes. Even a caveat that the rate guarantee is a worst-case mathematical existence result whose practical tightness remains open would honestly delineate the theory's limitations.
2. Add at least one application-level experiment — either a small basis pursuit (sparse recovery) instance comparing recovery accuracy vs. \(\ell_1\)-norm minimization, or a simple optimal transport problem comparing with Sinkhorn — to ground the broader claims.
3. Soften the claim in the contributions list about "supported by simulations" for the Sinkhorn comparison, since no such simulations appear, or add them.

## Score and Decision

The paper presents a novel and technically rigorous theoretical analysis of discrete-time GD on diagonal linear networks for LP. The proofs of linear convergence and the limit characterization are genuine contributions that advance beyond the gradient-flow analyses in prior work. However, the theoretical linear rate guarantee has an unacknowledged exponential dependence on dimension that limits its practical import, and the experiments are too narrow to support the claimed breadth of applications (basis pursuit, optimal transport). The paper would be notably stronger if the authors addressed the dimension-dependence discussion and added application-level experiments. In its current form, the theoretical contribution is solid but the presentation overreaches.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>