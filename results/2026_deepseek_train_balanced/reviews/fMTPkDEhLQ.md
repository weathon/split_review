## Summary

This theoretical paper proves worst-case oracle complexity lower bounds for minimizing high-order Hölder smooth and uniformly convex functions under two asymmetric regimes: (1) \(q > p+\nu\) (higher uniform convexity degree than smoothness order), and (2) \(q < p+\nu\) (higher smoothness order than convexity degree). The paper claims matching lower bounds to the upper bounds of Song et al. (2021), using an \(\ell_\infty\)-ball-truncated Gaussian smoothing operator for the polynomial-rate case and Nesterov's hard function framework for the loglog case.

## Strengths

1. **Novel \(\ell_\infty\)-ball-truncated Gaussian smoothing operator (Section 4).** The operator is carefully designed to simultaneously achieve three properties — locality, dimension-free Lipschitz constant, and compounding smoothness constant under repeated application — that prior alternatives (\(\ell_2\)-ball smoothing, pure Gaussian, softmax, Moreau) fail to jointly satisfy. The systematic failure analysis of alternatives (lines 71–80) is clear and convincing. This is a genuine technical innovation.

2. **Sound construction and trajectory argument for the \(q > p+\nu\) case.** The polynomial-rate lower bound construction (Section 4) follows the Guzmán-Nemirovski framework with a well-structured trajectory indistinguishability argument (lines 166–186). The overall architecture extends prior work (Doikov et al. 2022, Thomsen et al. 2024) from \(p=1\) to general \(p\) with Hölder smoothness.

3. **Clear problem positioning.** The paper correctly identifies the gap between existing general upper bounds (Song et al. 2021) and the limited known lower bounds, which covered only special cases (e.g., \(p=1\) for uniformly convex, or \(p=2, q=2\) for strongly convex).

## Weaknesses

### Major

1. **The loglog-case derivation (Section 5) contains mathematical issues that prevent verification of the claimed bound.**
   - **T-dependent "constant".** The quantity \(c_{p,q,\nu}\) defined on line 320 contains the factor \((1/c_{p,\nu})^{q(p+\nu-1)((p+\nu-1)^T-1)/(p+\nu-2)}\), which depends on \(T\) through \(((p+\nu-1)^T-1)\). The combined \(T\)-dependency in the lower bound is therefore the product \((1/c_{p,\nu})^{q(p+\nu-1)((p+\nu-1)^T-1)/(p+\nu-2)} \cdot (p+\nu-1)^{-q(p+\nu-1)^T}\). On lines 321–323, this is absorbed into \(c_{p,q,\nu}\) and the constant is then treated as \(T\)-independent when solving for \(T\) via loglog. The derivation never checks whether the combined \(T\)-dependency actually yields a decaying bound (which requires an unstated condition on \(c_{p,\nu}\)) or correctly accounts for the \(T\)-dependency inside the "constant" when inverting the bound.
   - **Exponent inconsistency.** The derivation transitions from \(\sigma^{(p+\nu)/(p+\nu-q)} / L_p^{q/(p+\nu-q)}\) (line 318) to \(\sigma^{(p+q-1)/(p-1)} / L_p^{q/(p-1)}\) (line 323). These exponents are not equivalent under any natural substitution, and \(L_p\) (a non-Hölder smoothness parameter from Definition 1) appears where \(H\) (the Hölder parameter) should be. This is either an algebraic error or a serious notational failure. As presented, the derivation on lines 316–323 does not reliably establish the claimed \(\log\log\) rate.

2. **Undefined constant \(c_q\) in the polynomial-rate derivation (Section 4).** The constant \(c_q\) appears centrally in equations (205, 207, 210) that determine how \(H\) relates to \(\beta\), \(\sigma\), and \(T\) — i.e., the parameter setting that yields the final \(\Omega\) bound. It is never defined in the visible main text. Without knowing what \(c_q\) is, the reader cannot verify the algebraic steps from lines 202–210 or the final bound.

### Minor

1. **Bounded-domain restriction for \(q > p+\nu\).** The hard function \(F\) is guaranteed to be Hölder smooth only on a bounded domain \(\mathcal{Q} = \{\mathbf{x}: \|\mathbf{x}\|_2 \leq D\}\) with an explicit bound on \(D\) (footnote, line 134). This means the construction does not satisfy the *global* Hölder smoothness condition (Definition 2) that the matching upper bounds assume. The paper acknowledges this in a footnote but does not discuss whether the restriction is fundamental or can be removed by a scaling argument. This limits the generality of the lower bound relative to the claimed match with Song et al. (2021).

2. **Missing parameter regime condition in the loglog construction.** The derivation requires \(H \geq 2^{p+\nu+1}(p+\nu-1)!\,\sigma\) (line 301) so that \(\tilde{\sigma} \leq 1\). This is a restriction on the parameter space that should be explicitly flagged.

### Trivial

1. **Inconsistent range for \(\nu\).** Definition 2 restricts \(\nu \in (0,1]\), but the loglog construction (line 234) writes \(\nu \in [0,1]\). The \(\nu=0\) case corresponds to Lipschitz (not Hölder) continuity of the \(p\)-th derivative, which is a different setting.

## Nice-to-Haves

- A brief discussion of why the \(q = p+\nu\) case is more challenging than the two asymmetric cases would be more informative than simply flagging it as future work.
- A table summarizing which prior lower bounds are subsumed as special cases of the new results would aid readability.

## Removed Points

These points were flagged by the harsh critic but are removed with justification:

- *"The loglog-case bound requires \(c_{p,\nu} > (p+\nu-1)^{-(p+\nu-2)/(p+\nu-1)}\); this condition is unstated and if reversed the bound is vacuous."* → Subsumed into Major weakness #1. The specific numeric condition is a derived detail of the broader T-dependency issue. The core problem is that `c_{p,q,ν}` is treated as T-independent when solving for T, which is the mathematical gap.

- *"The empty gap-bound lemma (lem:Gap_bound) makes it hard to verify the final rate calculation."* → This is a parser artifact; the lemma content likely existed in the original submission. However, the missing definition of `c_q` (which would plausibly appear there) is a real issue and is kept as Major weakness #2.

- *"Dimensional restrictions \(T \geq \sqrt{d} - 1\) and \(T \leq d\) should be discussed more."* → These are standard in the Guzmán-Nemirovski framework and do not need elaboration.

- *"Gaussian smoothing (duchi2012randomized), softmax smoothing, Moreau smoothing..." (failure analysis)* → The strength finder noted this, but it is inherent to the paper's own contribution description and not an additional insight.

- *"The paper would benefit from a table summarizing previous lower bounds..."* → Moved to Nice-to-Haves.

- *General speculative criticisms* (e.g., "the evaluation lacks rigor" without a concrete anchor) → Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's ambition (matching lower bounds for both regimes) and the technical gaps in the loglog derivation, but do not add new conceptual observations beyond what the paper claims.

## Suggestions

1. Fix the T-dependency in \(c_{p,q,\nu}\) by separating the constant part from the T-dependent part. Show explicitly that the combined T-dependency yields a double-exponential decay (which requires stating and satisfying a condition on \(c_{p,\nu}\)).
2. Correct the exponent inconsistency on line 323 and replace \(L_p\) with \(H\) throughout Section 5.
3. Define \(c_q\) explicitly in the main text, not deferring it to a lemma that may be stripped.
4. Discuss whether the bounded-domain restriction in the \(q > p+\nu\) case is removable, and if not, state clearly what the lower bound implies under global assumptions.
5. Reconcile the range of \(\nu\) between Definition 2 (\(\nu \in (0,1]\)) and the loglog construction (\(\nu \in [0,1]\)). Define the overlap or clarify the distinction.

## Score and Decision

The paper makes real contributions — the \(\ell_\infty\)-truncated Gaussian smoothing operator is genuinely novel, and the Section 4 construction is largely sound. However, the Section 5 derivation (the \(q < p+\nu\) case) has verifiable mathematical issues — a T-dependent quantity treated as constant, and an exponent/notation inconsistency — that prevent reliable verification of the claimed \(\log\log\) bound. Since the paper's central claim is providing tight lower bounds for *both* asymmetric regimes, the unresolved problems in half the contribution substantially weaken the overall result. The paper needs major revision to Section 5 before it can be accepted.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>