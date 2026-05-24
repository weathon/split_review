## Summary

This paper presents a novel data structure for Gaussian kernel density estimation (KDE) that leverages asymmetric locality-sensitive hashing (LSH) to achieve substantially improved query-time bounds. The key idea is to instantiate the KDE-to-ANN reduction framework of Charikar et al. (2020) with the asymmetric LSH of Andoni et al. (2017), which allows trading off space for query time. The main result is a KDE data structure with query time ≈ 1/μ^{0.051} (a factor-of-3.4 improvement over the prior best exponent of 0.173) at the cost of ≈ 1/μ^{4.15} space, along with the first general time-space tradeoff curve for KDE. The approach is well-motivated, technically sound, and represents a meaningful advance in the theory of high-dimensional KDE.

## Strengths

- **Significant quantitative improvement**: The query exponent of 0.051 improves on the previous best of 0.173 (Charikar et al., 2020) by a factor of 3.4. This follows directly from the optimization framework in Lemma 15 and Equation (10), with numerical evaluation confirming the constants.
- **First time-space tradeoffs for KDE**: Theorem 16 and Figure 1 provide a smooth tradeoff curve parameterized by δ, where increasing allowed space monotonically reduces query time. Prior work offered only point results (e.g., linear space with a single query exponent). This is genuinely new and well-substantiated.
- **Linear-space improvement with simpler analysis**: In the δ = 0 (linear space) regime, the query exponent of 0.1865 improves on the data-independent bound of 0.25 from Charikar et al. (2020) and nearly matches their data-dependent bound of 0.173, while relying on a simpler, data-independent construction.
- **Explicit, interpretable overhead formula**: Lemma 15 gives the query-time exponent ξ(δ, x) as a closed-form min-max expression (Equation 10) over LSH parameters ρ_q, ρ_s and intermediate distance scales y ∈ [x, 1]. This makes the tradeoff transparent and directly feeds the numerical optimization.
- **Insightful impossibility discussion**: Section 1.2 provides a clear quantitative explanation of why constant query time cannot be achieved under current ANN technology — the overhead from intermediate distance scales persists even with ρ_q = 0 — which explains the plateau in Figure 1.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Numerical optimization lacks methodological detail**: The headline exponents (0.051, 0.1865, 4.15) are obtained by numerically solving the min-max problem in Equation (10), yet the paper provides no description of the numerical method — no mention of grid resolution, search strategy, convergence checks, or how the o(1) terms are handled numerically. In a theory paper where the exact constants are the headline result, readers need enough detail to assess whether the numbers are trustworthy. This does not undermine the asymptotic improvement (any constant below 0.173 would still be an advance), but it weakens confidence in the specific reported digits.

- **Core technical lemma deferred to appendix**: Lemma 31, which provides the collision probability analysis underpinning the query-time bound, is stated only by reference to Appendix C. While this is standard practice in theory papers, the main body would benefit from at least stating the lemma's key collision probability expression, which would make the paper more self-contained for readers who do not immediately turn to the appendix.

### Trivial

- The informal claim that the construction is "much simpler" than Charikar et al. (2020)'s data-dependent scheme (Section 1.1) is reasonable given the data-independent nature of asymmetric LSH, but the analysis itself remains non-trivial. A slight softening of this language would improve accuracy without weakening the contribution.

## Nice-to-Haves

- A brief discussion of how the additive distortion O(1/(r log log n)) from the sphere reduction (Lemma 8) propagates through the collision probability analysis at intermediate distance scales would make the reduction more self-contained, though the paper's claim of n^{o(1)} overhead is standard and sufficient.
- Describing the numerical method (e.g., grid resolution, optimization routine) in a footnote or brief paragraph would add transparency to the headline numbers.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Lemma 31 is stated without proof — appendix unavailable for review."** The appendix is stripped by the parser; it exists in the original submission. This is a parser artifact, not an author error.
- **"p_j definition is garbled (min(1/2^{J+n}, 1))."** The garbled formula `\min(\frac{1}{2^{J+n}}, 1)` is clearly a PDF extraction artifact. The intended formula is given in Equation (3) as `(1/μ)^{1-x_j} · 1/n`. This does not reflect the original submission.
- **"d = Õ(1) seems inconsistent with high-dimensional ANN (d = n^{o(1)})."** These are consistent: Õ(1) means sub-polynomial in n, i.e., n^{o(1)}, which exactly matches the requirement in Theorem 7. The paper also cites the standard dimension-reduction justification from Charikar et al. (2020, Remark 1).
- **"Equation (6) presented as 'turns out to be' without derivation."** The full derivation of the collision probability expression is sketched in Sections 1.2 and 4 (culminating in Lemma 15 of Appendix C, as cited). The technical overview provides sufficient intuition for a theory paper.

## Novel Insights

The most interesting structural insight emerging from this work is that the KDE problem forces a fundamental decoupling of the space and query exponents across different distance scales: the scale x that dominates the space bound is *not* the scale that dominates the query time. This is precisely why asymmetric LSH — which allows ρ_s ≠ ρ_q — yields an improvement where symmetric LSH cannot. The explicit characterization of the plateau at ξ(δ) ≈ 0.05, derived from the max-over-y term in Equation (10), reveals an inherent barrier in the LSH-based KDE framework that was not visible in prior work.

## Suggestions

- State Lemma 31's central collision probability expression in the main body (even if only as a displayed equation), so readers can follow the derivation of Equation (10) without consulting the appendix.
- Add a footnote or short paragraph in Section 5 describing the numerical method used to solve Equation (10) (e.g., grid discretization of x and y, resolution used, confirmation that further refinement does not change the reported digits).
- Soften "much simpler" to "simpler" or "conceptually simpler" when comparing to the data-dependent scheme of Charikar et al. (2020), since the asymmetric LSH analysis is still technically involved.

## Score and Decision

**Calibration anchors used:**

Round 1 (bracketing):
- cSd8Eom8Zt (2.33) — DeepKDE, applied/empirical, much weaker contribution
- GOjr2Ms5ID (3.25) — Cascaded Learned Bloom filter, different domain
- tra8ktyk0E (5.50) — Dynamic KDE, partially overlapping but less significant theoretical contribution
- BvQkjCnXXr (4.50) — FastLSH, efficiency-focused, less theoretical depth
- wLnls9LS3x (7.00) — Kernel Matrix-Vector Multiplication, most comparable: theory paper using LSH for kernel computation, some experiments, solid but not breakthrough
- N4rYbQowE3 (7.00) — Learning-Augmented Search, different domain
- sbG8qhMjkZ (8.00) — SVGD convergence rates, strong pure theory paper with complete proofs

Round 1 bracket: **between 6.0 and 8.0**

Round 2 (narrowing):
- HMe5CJv9dQ (7.50) — DP KDE, theory + experiments, broader scope, strong contribution. Our paper has a more significant theoretical advance but no experiments; slightly below this.
- wLnls9LS3x (7.00) — Kernel Matrix-Vector Multiplication, theory paper using LSH for kernels, with some empirical validation. Our paper has a more dramatic theoretical improvement (3.4x factor) but no experiments. Comparable quality.
- Eh0Od2BJIM (6.33) — HyperAttention, mixed theory/experiments, less focused contribution. Our paper is clearly stronger.
- olOheQ0ZcK (5.75) — Distance Estimation, different domain, mixed reviews. Our paper is stronger.
- oRNus243R6 (5.67) — Diverse Graph-based NN, different domain. Our paper is stronger.

Comparing directly against wLnls9LS3x (7.00): both are theoretical kernel computation papers. The anchor has experiments validating its assumption on BERT, which our paper lacks entirely. However, our theoretical contribution is more significant — a factor-of-3.4 improvement on a well-known bound versus a new algorithm that works under a specific structural assumption. The anchor also received criticism for limited empirical validation. Our paper's theoretical advance is cleaner and more impactful. I judge the papers as comparable in overall quality.

Comparing against HMe5CJv9dQ (7.50): this anchor has both theory and experiments across multiple kernels/distance functions, with a broader scope. Our paper is more narrowly focused (Gaussian KDE only) but achieves a more dramatic quantitative improvement on its specific problem. The anchor's broader applicability and empirical grounding give it a slight edge. Our paper sits modestly below this.

**Final placement: 7.0.** The paper makes a genuinely significant theoretical contribution with a novel approach, clear exposition, and well-supported claims. The main weakness — lack of numerical method detail — is minor and does not undermine the asymptotic improvement, though it does reduce confidence in the specific reported digits. This is a solid accept for a theory venue.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>