Now I have sufficient calibration data. Let me write the consolidated review.

---

## Summary

This paper extends the theory of adaptive smoothness (previously developed for convex optimization) to the nonconvex setting, providing a unified convergence analysis for adaptive optimizers (AdaGrad, Adam, one-sided Shampoo) with general well-structured preconditioner sets. The key technical contribution is a novel matrix inequality (Lemma 3.3) that handles noncommutativity, enabling the first nonconvex analysis that goes beyond diagonal preconditioners. The paper also studies two benefits of adaptive geometry: (1) adaptive smoothness enables accelerated Õ(T⁻²) convergence with Nesterov momentum in the convex setting, and (2) adaptive gradient variance yields dimension-free convergence rates for NSD that are unattainable under standard variance.

## Strengths

- **First unified nonconvex convergence analysis for adaptive optimizers with general well-structured preconditioners.** The paper extends beyond the diagonal-only case (AdaGrad, Adam) to matrix-valued preconditioners (one-sided Shampoo/ASGO), overcoming noncommutativity via Lemma 3.3. This is a genuine technical advance that addresses a recognized open gap in the literature (lines 534–536).

- **Novel matrix inequality (Lemma 3.3) that handles noncommutativity in general preconditioner sets.** This technical result bounds the spectral norm of a sum involving differences of preconditioners via a novel relationship between matrix differences and logarithms (Lemma C.1). It subsumes the diagonal case and yields explicit bounds for general H. The technique is likely of independent interest for future adaptive optimization analyses (lines 599–601).

- **Clean geometric duality between supremum of primal norms and infimum of dual norms for well-structured preconditioner sets.** Lemma 2.2 and Figure 1 provide an intuitive geometric interpretation connecting Adam/SignGD, AdaGrad/NSD under the ℓ∞ norm, and generalized to arbitrary H. This formalizes the relationship between the two algorithm families elegantly.

- **Introduction of adaptive gradient variance (Definition 4.1) and demonstration of its payoff.** Theorem 4.5 shows NSD under adaptive variance achieves a dimension-free Õ(T⁻¹/⁴) rate (in the stochastic-dominated regime), while Theorem 4.7 provides a matching-dimension dependent lower bound under standard ℓ₁ variance. This highlights a genuine benefit of adaptive noise modeling.

## Weaknesses

### Fatal
None.

### Major

- **The acceleration "separation" claim (Section 4.2) is overstated.** The paper claims that adaptive smoothness "enables" acceleration while standard smoothness "fails," citing the Guzmán & Nemirovski (2015) lower bound for ℓ∞ smoothness. However, the paper's upper bound is under adaptive smoothness (a stronger condition), while the cited lower bound is under standard ℓ∞ smoothness (a weaker condition). The comparison shows that a stronger assumption leads to a better rate — which is true but not novel. The paper explicitly acknowledges the comparison is "for the specific case of ℓ∞ norm smoothness" (line 788), but then claims adaptive smoothness is "necessary" for acceleration (line 791), which conflates sufficiency with necessity. The claim should be qualified: adaptive smoothness is *sufficient* for acceleration in cases where standard smoothness is known to be insufficient, rather than claiming a general separation.

- **The variance comparison (Section 4.3) compares different assumptions rather than different algorithms under the same assumption.** Theorem 4.5 gives a dimension-free rate under adaptive variance σ_H, while Theorem 4.7 gives a dimension-dependent lower bound under standard ℓ₁ variance. As Proposition B.11 notes, adaptive variance can be up to d times larger than standard variance, so the gap could reflect the assumption strength mismatch rather than an algorithmic limitation. The paper acknowledges this mismatch but the narrative ("fundamental gap," lines 1010–1011) still reads as an apples-to-oranges comparison. To convincingly show that adaptive variance is the "right" notion for dimension-free rates, the paper would need a lower bound under adaptive variance itself, or a normalization showing the two variances are comparable.

### Minor

- **The nonconvex rates in Theorems 3.1 and D.2 contain terms depending on ∥S_T∥_op whose bound requires tracing through multiple layers of lemmas.** While the clean rate Õ(√(Δ₀Λ_H(f) log d)/T) emerges after optimizing η (Theorem 3.2), the intermediate dependence on ∥S_T∥_op makes the results less reader-friendly than they could be. A cleaner presentation of the final rate in Theorem 3.1 (analogous to Theorem 3.2) would improve accessibility.

- **The accelerated algorithm (Algorithm 2) requires evaluating gradients at convex combinations** (∇f_t^{α_t, x̄_t}(x_t) per Eq. 8), and the optimal learning rate η depends on the unknown parameter D = max_t ‖x_t − x*‖_H. While the projected variant (Algorithm 8, Theorem E.5) removes the need for prior knowledge of D, this comes at the cost of requiring knowledge of D as a projection radius. The practical implications of these requirements are not discussed.

- **The stochastic rate in Theorem 4.3 has four regime-dependent cases with different hyperparameter choices**, each depending on the unknown ratio a₀ = Δ₀ L_{‖·‖_H}(f)/σ_H. While such case analysis is common in optimization theory, its practical value is limited without guidance on how to estimate a₀ or adapt α and η online.

### Trivial

- The bound in Theorem 4.3 contains a term d√ε D / T² that, while present, reflects the effect of the stability parameter ε and is negligible for small ε.

## Nice-to-Haves

- A concrete synthetic example illustrating when adaptive smoothness Λ_H(f) differs substantially from standard smoothness L_{‖·‖_H}(f) (beyond the d factor) would help practitioners understand when the distinction matters in practice.
- While experiments are not expected for a theory paper, a small-scale numerical verification that the convergence rate scales with Λ_H(f) as predicted would strengthen the nonconvex claims.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

1. *"The central claimed separation — that adaptive smoothness enables acceleration while standard smoothness does not — is not properly established… The comparison as written is incoherent."* — The paper explicitly states the comparison is "for the specific case of ℓ∞ norm smoothness" (line 788). The comparison between different assumptions (adaptive vs. standard smoothness) is coherent as a study of what each assumption enables; it is not incoherent to compare what two different assumptions imply. Weakening is warranted (see Major weakness above), but the "incoherent" framing is too harsh.

2. *"The paper does not provide a clean, explicit rate" for nonconvex convergence.* — Theorem 3.2 gives a clean explicit rate: Õ(√(Δ₀·Λ_H(f)·log d)/T). The bound on ‖S_T‖_op is also stated explicitly (line 464).

3. *"The lower bound cited is for the specific norm ‖·‖_∞, but the paper's claim about adaptive smoothness applies to arbitrary well-structured preconditioner sets H."* — The paper says "for the specific case of ℓ∞ norm smoothness" (line 788). This is correctly qualified. The acceleration claim is made for the ℓ∞ case specifically.

4. *"The paper claims this 'duality' property holds for any well-structured preconditioner set, but the proof depends on the specific structure."* — Lemma 2.2 is stated and proven (via reference to Xie et al. 2025b) for any well-structured preconditioner set. This is a known property, not a claim that needs independent verification here.

5. *"The nonconvex rates are not properly instantiated for specific algorithms"* — The paper explicitly instantiates for AdaGrad, AdaGrad-Norm, one-sided Shampoo (lines 387–394). The bound on ‖S_T‖_op is given for general H (line 464) and improved for diagonal H (line 465).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Tone down the "necessary" claim** in the acceleration discussion. Replace "adaptive smoothness is necessary to achieve the acceleration" with "adaptive smoothness is sufficient for acceleration in settings where standard smoothness is known to preclude it" (or similar).

2. **In the variance comparison**, add a short discussion acknowledging that the upper and lower bounds operate under different variance notions, and clarify that the contribution is showing adaptive variance (despite being a potentially larger quantity) enables dimension-free rates — an *a priori* non-obvious result.

3. **Present the final nonconvex rate** in Theorem 3.1 in cleaned form (analogous to Theorem 3.2) so readers do not need to trace through ‖S_T‖_op to see the rate.

---

## Score and Decision

### Calibration Anchors

| Anchor | Avg Human Score | Comparison |
|--------|:-:|------------|
| `/home/wg25r/review_agent/human_reviews_2026/vPSiCA3CkD.md` (GRAAL acceleration) | 7.50 | Cleaner theoretical results and adaptivity, but the current paper covers nonconvex and general preconditioners — broader scope but slightly overclaimed narrative. |
| `/home/wg25r/review_agent/human_reviews_2026/XhXMzPJJ7J.md` (SGD with Adaptive Preconditioning) | 5.00 | Most directly comparable: similar unified analysis + acceleration framework. Current paper is technically stronger (nonconvex, general H) and more polished, but has similar framing concerns. |
| `/home/wg25r/review_agent/human_reviews_2026/9asuGOncOi.md` (Frank-Wolfe) | 6.00 | Comparable theoretical depth and rigor. Current paper has broader algorithmic coverage but lacks experiments (not expected here). |
| `/home/wg25r/review_agent/human_reviews_2026/yRtgZ1K8hO.md` (Polar Express) | 8.00 | More practical + theoretical combined. Not directly comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/0YDUJznwtX.md` (Adam sign-descent) | 2.00 | Significantly weaker paper with unreasonable assumptions. Current paper is far stronger technically. |
| `/home/wg25r/review_agent/human_reviews_2026/DwWorqSjwv.md` (AdaGrad robust) | 3.00 | Paper with serious technical flaws and misleading claims. Current paper is substantially sounder. |

The paper sits well above the 3–5 band (flawed/weak papers) and is comparable to or stronger than the 5–7 band anchors. Relative to the most comparable anchor (XhXMzPJJ7J at 5.0), the current paper extends the analysis to nonconvex objectives and general preconditioner sets, resolving the noncommutativity issue — a clear technical advance. The overclaim concerns in Sections 4.2–4.3 are real but not fatal and do not undermine the core contributions (Lemma 3.3, nonconvex analysis, geometric duality). Weighing the genuine technical contribution against the inflated narrative, the paper merits acceptance.

**Average anchor scores in the 5–7 band: ~5.5–6.0.** The current paper is at or slightly above the top of this band.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>