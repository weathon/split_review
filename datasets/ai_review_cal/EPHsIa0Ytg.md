- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6
## Summary

This paper introduces the *k*-multilinear extension (Definition 2.4) for *k*-submodular functions — the first continuous relaxation tailored to this class — and uses it within a Frank–Wolfe-type two-stage framework to obtain improved approximation ratios. The key results are: an asymptotically optimal **1/2-approximation** for monotone objectives under *O*(1) knapsack constraints (improving the prior 1/3), and a **1/3-approximation** for non‑monotone objectives under knapsack or matroid constraints (improving the prior ~0.245). The framework unifies monotone/non‑monotone cases and handles matroid constraints, knapsack constraints, and their intersections.

## Strengths

- **Asymptotically optimal 1/2-approximation for monotone *k*-submodular maximization under knapsack constraints.** Theorem 1.1 and Table 1 show this matches the lower bound of *(k+1)/(2k)* (Iwata et al., 2016) and improves the previous combinatorial 1/3-approximation (Ha et al., 2024). The same ratio extends to *O*(1) knapsacks with no dependence on the number of knapsacks, unlike prior work.

- **Improved 1/3-approximation for non‑monotone *k*-submodular maximization.** Theorem 1.2 and Table 1 report a factor-1/3 for both single knapsack and single matroid constraints, improving on the prior ~0.245 (Ha et al., 2024) and eliminating dependence on the number of knapsacks.

- **Introduction of the *k*-multilinear extension (Definition 2.4) and its key analytic properties (Lemma C.1).** This extension provides the first continuous relaxation for *k*-submodular functions, enabling Frank–Wolfe-type methods. The listed properties — approximate linearity (Ineq. 4), element-wise non-positive Hessian (Ineq. 3), and pairwise monotonicity — are specifically used to overcome the closure and approximate-linearity challenges that arise in the *k*-submodular setting (Section 1.2).

- **Unified continuous framework handling multiple constraint types and both monotone/non‑monotone cases.** Algorithms 1 and 3 are designed for *O*(1) knapsacks, matroid constraints, and their intersection, and the analysis works for both monotone and non‑monotone objectives (Theorems 3.1 and F.1). This generality exceeds prior combinatorial methods that typically target a single constraint type.

- **Novel technique for handling lack of coordinate-wise closure in Δ_kⁿ.** The introduction of auxiliary points **o**(t) = **x**(t) + (1−t)**o**⋆ (linear combinations rather than coordinate-wise maxima) and the derivation of the core inequality *F*(**x**(t+δ))−*F*(**x**(t)) ≥ *F*(**o**(t))−*F*(**o**(t+δ))−3εMδ (Section 3.2) are the central technical contributions that drive the improved ratios.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Query complexity for knapsack constraints is stated without explicit exponents.** The complexity is given as *O*(*k*^{poly(1/ε)} *n*^{poly(1/ε)}) (Theorem 3.1, Lemma 3.2). While this notation is standard in the submodular maximization literature (Chekuri et al., 2014), omitting even a rough indication of the exponent (e.g., "the exponent is *O*(1/ε)") makes the complexity opaque. This is a transparency issue, not a correctness issue, and the paper already acknowledges that query complexity is larger than combinatorial alternatives (line 172).

- **The "pairwise monotonicity" property for the non‑monotone case is listed but not explained in the main text.** The property is mentioned (line 66, line 74) as a tool to reduce the non‑monotone case to the monotone one, but no intuition, example, or sketch is provided for how this reduction works in the main body. A brief illustrative explanation would improve readability without burdening page limits, given that this property is central to the non‑monotone analysis.

### Trivial
None.

## Nice-to-Haves
- A brief remark on the regime where the algorithm's guarantees would be meaningful (e.g., constant *k*, small ε) given the high polynomial exponents.
- A short forward-reference statement in Section 3 that the non‑monotone rounding follows the same structure (presently deferred entirely to Lemma F.3).

## Removed Points

These points were flagged by reviewers but are removed here with justification:

- **"The proofs are only sketched in the main text; soundness depends on the appendix."** This is a standard page-limit constraint for theoretical conference papers. The paper explicitly references the appendix for all full proofs, and the main-text sketches are coherent. Speculating about appendix correctness is not a specific, verifiable weakness. *Removed as a speculative/general concern.*

- **"Lemma 2.5 (gradient oracle) is stated without proof."** Again, this is standard — the proof is deferred to the appendix. The lemma's statement with its query complexity is what the main text needs. *Removed as a missing-appendix complaint.*

- **"The non‑monotone rounding case references Lemma F.3 but is not restated in the main text."** The paper provides a forward reference to the appendix lemma. This is standard cross-referencing practice. *Removed as a formatting/preference nitpick.*

- **"The comparison table (Table 1) is referenced but not visible in the parsed text."** This is a PDF-parser artifact; the table exists in the original submission. *Removed as a parser issue.*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. In the main text, add 1–2 sentences giving intuition for how "pairwise monotonicity" enables reducing the non‑monotone case to the monotone one.
2. Replace "poly(1/ε)" with a more informative expression (e.g., "the exponent is *O*(1/ε)") or at minimum add a footnote clarifying the rough degree, to help readers gauge practicality.
