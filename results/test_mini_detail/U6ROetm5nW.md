## Summary

This paper presents new data structures for Gaussian Kernel Density Estimation that achieve improved query-time vs. space tradeoffs by leveraging asymmetric LSH constructions. The main result reduces the query exponent from the previous best of 0.173 to 0.05 (at higher space cost), and provides the first explicit space–time tradeoff curve for KDE. For the linear-space regime, the paper achieves a query exponent of 0.1865, beating the data-independent bound of 0.25 with a simpler analysis than the prior data-dependent approach.

## Strengths

- **Significant query-exponent improvement**: Theorem 17 reports a query exponent of 0.05 (with space exponent 4.1), improving substantially over the previous best data-dependent exponent of 0.173 (Charikar et al., 2020). The improvement is clearly visualized in Figure 1, where the tradeoff curve plateaus near 0.05.

- **First explicit space–query tradeoff for KDE**: Theorem 16 gives, for any δ ≥ 0, a KDE data-structure with space exponent 1+δ and query exponent ξ(δ). The paper states this is the first such tradeoff in the KDE literature, and the right plot of Figure 1 maps it explicitly.

- **Improved linear-space query exponent with simpler analysis**: For δ = 0 (linear space), the paper achieves query exponent 0.1865, beating the data-independent bound of 0.25 from Charikar et al. (2020) and coming within ≈0.013 of their data-dependent bound (0.173), while using a significantly simpler, data-independent analysis.

- **Clear analytic barrier for constant-query KDE**: Section 1.2 derives why even asymmetric LSH cannot yield arbitrarily small query exponents for KDE (Equation 7 and surrounding discussion), providing a well-justified limitation of the approach.

- **Well-structured reduction framework**: The reduction from KDE to Level-\(j\) Recovery to asymmetric ANN is clearly laid out, with explicit expressions for the threshold function θ(δ), the space/query exponents ρ_s(δ,x), ρ_q(δ,x), and the closed-form min-max optimization in Equation (10).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Numerical optimization not fully specified in the main text**: The claimed exponents (0.05, 4.15) are the output of a numerical optimization of Equation (10). The paper acknowledges the solution is numerical ("The exact optimum does not seem simple to obtain analytically, and we therefore resort to numerics"), but does not specify the optimization method used (e.g., convexity argument, grid search, analytic bounding) in the main text. The derivation from Equations (6–7) to the general form in Equation (10) is compressed, making it difficult for readers unfamiliar with Razenshteyn (2017) to follow the logical chain. While the appendix presumably fills this gap, the main text would benefit from a brief methodological remark.

- **Inconsistency in reported exponent values**: Theorem 1 (informal) states query exponent 0.051 and space exponent 4.15, while Theorem 17 states query exponent 0.05 and space exponent 4.1. The abstract uses 0.05 and 4.15, and the body text in Section 5 refers to space 4.15 when comparing with prior work. These slight numerical inconsistencies should be reconciled.

- **Dimension assumption d = Õ(1) not discussed as a limitation**: Definition 5 sets d = Õ(1) (polylogarithmic in n). While this follows the standard assumption in the LSH/ANN literature (and prior KDE work by Charikar et al.), the paper would benefit from a brief remark acknowledging that the tradeoffs are stated for this regime and that the hidden constants in Õ depend polynomially on d. This does not diminish the contribution but helps readers calibrate scope.

### Trivial

- The expression for ρ_q(δ,x) when x > θ(δ) in Definition 14 is stated without justification; a brief sentence explaining its origin (solving the ANN tradeoff constraint under the space budget) would improve readability.
- The additive error O(1/(r log log n)) from the sphere reduction (Lemma 8) is noted but its absorption into the o(1) terms or the approximation factor ε is not discussed.

## Nice-to-Haves

- Include a marker for the data-dependent bound (0.173) from Charikar et al. (2020) in the right plot of Figure 1, to directly contextualize the linear-space result.
- Provide a brief intuitive example (e.g., setting ρ_q = 0) in Section 1.2 to illustrate why the asymmetric tradeoff yields the improvement over symmetric LSH.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"The paper does not mention that Theorem 7's data structure is data-independent"* — **Removed because the paper already states this** immediately after Theorem 7 (line 145): "this data-structure is data-independent (see Razenshteyn (2017))."
2. *"The data-dependent bound (0.173) is mentioned only in the abstract"* — **Removed as factually incorrect**: the bound appears in the abstract AND in Sections 1.1 and 5.
3. *"Because the appendix was stripped from the extraction, I cannot verify this"* — **Removed per policy**: missing appendix content is a parser artifact, not an author error.
4. *"The 'o(1)' terms are not discussed"* — **Removed**: the paper uses o(1) in the standard asymptotic sense typical of theory papers; this is standard and does not require special discussion.
5. *"No discussion of extending to other kernels"* — **Removed as scope creep**: evaluating the paper on its stated scope (Gaussian kernel) is appropriate; extension to other kernels is a nice-to-have, not a weakness.

## Novel Insights
None beyond the paper's own contributions. The key conceptual insight — that different distance scales dominate the query time and space bottlenecks in the KDE reduction, allowing asymmetric LSH to exploit this imbalance — is already clearly articulated by the paper in Section 1.2.

## Suggestions

1. Reconcile the numerical inconsistency: make the query exponents (0.05 vs 0.051) and space exponents (4.1 vs 4.15) consistent across Theorem 1, Theorem 17, and the abstract.
2. Add a sentence in Section 4 or 5 specifying the optimization method used to evaluate Equation (10) (e.g., line search, convexity argument, grid refinement).
3. Explicitly note in Definition 5 or the discussion following it that the hidden constants in \(\tilde{O}\) are polynomial in d and that the results are stated for d = O(polylog n), consistent with prior work.
4. Add a marker for the Charikar et al. (2020) data-dependent bound (0.173) to the right plot of Figure 1 for completeness.

## Score and Decision

### Calibration Summary

**Round 1 — Bracketing:**
- Low band (avg < 3.5) on "KDE theory/algorithm": returned papers with avg scores 2.33–2.67 — fundamentally flawed or minimal contributions. The current paper is clearly above these.
- Middle band (3.5–7.5): returned papers with avg scores 4.5–6.75 — including "Optimal Sketching for Residual Error Estimation" (avg 6.75, accepted poster), "Beyond Worst-Case Dimensionality Reduction" (avg 6.5, accepted poster), and "HashOrder" (avg 5.5, rejected). 
- High band (avg > 7.5): returned papers scoring 7.75–8.0 — including "Streaming Algorithms For ℓ_p Flows" (spotlight, avg 8.0) and "Generalization error of spectral algorithms" (spotlight, avg 8.0).

**Initial bracket**: 4.5–7.5.

**Round 2 — Narrowing:**
- Lower-queries inside (4.5, 6.5): returned "Identify Dominators" (avg 4.8, rejected), "Clustering on Skewed Cost Distributions" (avg 5.6, rejected), "Adaptive Retrieval for k-NN" (avg 6.25, accepted poster).
- Upper-queries inside (6.5, 8.0): returned "Efficiently Computing Similarities to Private Datasets" (avg 7.5, accepted poster — DP KDE with theory + experiments), "Learning-Augmented Search Data Structures" (avg 7.0, poster), "Optimal Sketching" (avg 6.75, poster).

**Anchors read in full and compared:**
- **"Optimal Sketching for Residual Error Estimation"** (avg 6.75, poster): TCS paper with tight bounds; comparable theoretical depth. The current paper's KDE contribution (first tradeoff + substantial exponent improvement) is arguably more significant, but the numerical optimization reliance is a mild drawback. Roughly comparable.
- **"Beyond Worst-Case Dimensionality Reduction"** (avg 6.5, poster): Multiple lower/upper bounds for sparse vectors; moderate novelty concerns. The current paper is more focused with a clearer narrative. Slightly stronger.
- **"Efficiently Computing Similarities to Private Datasets"** (avg 7.5, poster): DP KDE with theory + experiments, broader scope. The current paper is narrower (purely theoretical) with minor presentation issues. Below this anchor.
- **"Streaming Algorithms For ℓ_p Flows"** (avg 8.0, spotlight): Initiated a new streaming model with matching bounds. More novel techniques. The current paper is a solid improvement within an established framework. Below this anchor.

**Round 3 — Final verification:**
- Inside (5.5, 7.5): returned "High-Dimensional Geometric Streaming" (avg 5.67, rejected) and "Clustering on Skewed Cost Distributions" (avg 5.6, rejected). The current paper is clearly stronger than both.

**Final determination**: The paper sits between the 6.5 and 6.75 anchors (comparable to or slightly above "Beyond Worst-Case" and "Optimal Sketching") and below the 7.5 anchor. Score 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>