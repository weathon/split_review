Now I have a thorough understanding of the paper and can verify all claims. Let me produce the final review.

## Summary

This paper studies the Kernel Density Estimation (KDE) problem for the Gaussian kernel. Its main contribution is using **asymmetric LSH** (Andoni et al. 2017) — which supports separate space and query exponents — to obtain improved KDE data-structures. The headline results are: (1) query time ≈ (1/μ)^{0.05} with space ≈ (1/μ)^{4.15} (substantially improving over the previous best query exponent of 0.173), and (2) query time ≈ (1/μ)^{0.1865} with linear space (improving over the data-independent bound of 0.25 and nearly matching the data-dependent bound of 0.173 with a simpler analysis). More generally, the paper presents the **first explicit family of query-time vs. space tradeoffs** for KDE, parameterized by δ ≥ 0.

---

## Strengths

1. **Novel and significant improvement via asymmetric LSH.** The paper correctly identifies that in the KDE reduction, the bottleneck for query time and space occur at different distance scales, making asymmetric LSH (which decouples the two exponents) a natural fit. The resulting query exponent 0.05 is a genuine and large improvement over the prior best of 0.173. [Lines 77–81, Theorem 17]

2. **First explicit space-query tradeoff for KDE.** Theorem 16 provides, for any δ ≥ 0, a KDE data-structure with space exponent 1+δ and query exponent ξ(δ). Prior work only had specific points on this curve; the tradeoff family itself is new. [Theorem 16, lines 43–45]

3. **Cleaner analysis in the linear-space regime.** The paper achieves query exponent 0.1865 with linear space, beating the data-independent bound of 0.25 (Charikar et al. 2020) and coming within 0.0135 of the data-dependent 0.173, while the authors argue their analysis is substantially simpler than the data-dependent approach. [Line 105, Section 1.1]

4. **Analytic impossibility argument for constant query KDE.** Section 1.2 provides a self-contained argument showing why, even with ρ_q = 0, the query exponent cannot drop below ~0.09 under current ANN technology, and further optimization still plateaus near 0.05. This explains the plateau in Figure 1 and identifies a fundamental limitation. [Lines 87–103]

5. **Rigorous framing of the optimization problem.** The key optimization (Equation 10) is explicitly derived and stated: ξ(δ,x) = min_{ρ ≥ ρ_q(δ,x)} max_{y∈[x,1]} ... . While solved numerically, the problem itself is precisely defined, and the threshold function θ(δ) and parameter choices ρ_s(δ,x), ρ_q(δ,x) in Definition 14 are provided in closed form. [Definition 14, Lemma 15, Equation 10]

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Numerical optimization methodology is underspecified.** The paper reports specific numeric exponents (0.05, 0.1865, 4.1) that "follow by numerical evaluations" of the optimization problem in Equation 10, but does not describe the numerical method used, the error tolerances, or provide any certified bounds on the reported values. The paper states at line 81: "The exact optimum does not seem simple to obtain analytically, and we therefore resort to numerics." In a theoretical CS paper presenting precise exponent claims as formal theorems (Theorem 17), stronger justification is expected — at minimum, a description of the optimization procedure and some error analysis. While the o(1) terms in the theorem statements absorb small numerical errors, the lack of methodology detail is a gap in rigor.

2. **Inconsistency in the high-space exponent.** Theorem 1 (Informal, line 39) states the query exponent as 0.051 with space 4.15, while Theorem 17 (line 267) states query exponent 0.05 with space 4.1. The sources of this discrepancy are not explained, and it undermines confidence in the precision of the numerical results.

3. **Framing of the linear-space comparison could be more precise.** The abstract states the 0.1865 result "improves the non-adaptive KDE bound from Charikar et al. (2020) and nearly matching the bound of Charikar et al. (2020)." The latter ("the bound") refers to their data-dependent bound (0.173). Since 0.1865 is strictly worse than 0.173, calling it "nearly matching" is defensible but generous — the gap of 0.0135 in exponents translates to a factor of (1/μ)^{0.0135} in query time, which could be significant in the μ = n^{-Θ(1)} regime. The acknowledgments in Section 1.1 ("slightly worse") are clearer.

4. **No discussion of whether the high-space tradeoff is nontrivial.** The 0.05 exponent with space exponent 4.15 is the paper's headline result, but it is not compared against any baseline tradeoff (e.g., repeated independent random sampling, or a trivial scheme that uses more space to reduce query time). Is the point (space=4.15, query=0.05) on the tradeoff curve meaningfully better than what a naive approach would achieve at the same space? The paper would benefit from a brief discussion.

### Trivial
- The "nice range" constants c₀, c₁ are mentioned but the precise handling of x outside [c₀, 1-c₁] is deferred to the appendix. A brief qualitative statement about why these edge cases do not affect the asymptotic exponents would help.

---

## Nice-to-Haves

- **Empirical validation on synthetic data** (even at moderate n) would strengthen the paper for ICLR's audience, demonstrating that the theoretical exponents manifest in practice.
- **More detail on the numerical optimization**: describing the method (e.g., grid search, convex optimization), error control, and sensitivity analysis would address the rigor concern.
- **An explicit lower bound or impossibility result** (beyond the heuristic argument) for constant-query KDE would be a nice theoretical contribution.

---

## Removed Points

The following criticisms from the reviews are removed with justification:

1. **"Lemma 31 is in the stripped appendix, making the core proof unavailable"** — Removed per hard rule: missing appendix content is a parser artifact, not an author error. The paper states the lemma exists in the appendix, which is present in the original submission.

2. **"No high-level argument for why ANN extends to Level-j Recovery"** — Partially removed. Section 4 (lines 233–234) describes the query procedure: "apply the query procedure... but go over all points in the leaves" and states the analysis is formalized in Lemma 31. The high-level approach is described; the detailed derivation is appropriately deferred to the appendix.

3. **"Abstract does not clarify that 0.05 requires space 4.15"** — Factually incorrect. The abstract (line 13) states: "Our main result is a data-structure with significantly improved query time ≈ 1/μ^{0.05}, at the expense of somewhat higher space complexity of ≈ 1/μ^{4.15}."

4. **"Comparison to prior work is misleadingly framed"** — Overstated. The paper explicitly acknowledges at lines 105 and 270 that 0.1865 is "slightly worse" than 0.173. The abstract's "nearly matching" phrasing is retained as a minor weakness (see above).

5. **Several strengths from the Strength Finder** that were generic ("addressed an important problem") or duplicates are removed.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's formal theorem statements and the heuristic numerical optimization used to instantiate them — this is a genuine methodological point but the paper itself acknowledges it openly.

---

## Suggestions

1. **In a revision, dedicate a short paragraph to the numerical optimization method.** Even a brief description ("We solved min-max over ρ and y via a grid search on [0,1] with step size 10^{-4}, and verified the results using gradient descent from multiple starting points") and a statement about stability would resolve the rigor concern.

2. **Reconcile the exponent discrepancy** between Theorem 1 (0.051/4.15) and Theorem 17 (0.05/4.1), or explain the source of the difference (e.g., different rounding conventions, different δ values).

3. **Add a brief comparison** of the high-space tradeoff against a trivial baseline (e.g., "for comparison, using the symmetric LSH at space exponent 4.15 would yield a query exponent of X") to contextualize the improvement.

---

## Score and Decision

This is a solid theoretical paper with a clear contribution: it identifies that asymmetric LSH naturally fits the KDE problem's structure, obtains substantially better exponents, and provides the first tradeoff family. The weaknesses are minor and addressable — the numerical methodology could be better documented, and the exponent discrepancy needs reconciliation. The core ideas are sound and well communicated.

**Score: 7.5**  
**Decision: Accept**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>