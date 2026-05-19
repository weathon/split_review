- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have a complete picture. Let me produce the consolidated review.

## Summary

This paper proposes a descent-based method for finding Nash equilibria in bilinear zero-sum games, exploiting the key observation that the duality gap is a convex function in this setting (Theorem 1). The method performs steepest descent on the duality gap: at each iteration it computes the direction minimizing the directional derivative, expressed in terms of the current best-response sets (Theorem 4), and takes a step. The paper claims a geometric convergence rate of O((1/ρ)·log(1/δ)) and presents experiments on random and block-structured games with up to 1000 strategies.

## Strengths

1. **Proof that the duality gap is convex for zero-sum games (Theorem 1).** This is the paper's core theoretical insight and is correctly proven. Prior descent-based approaches for general games (Tsaknakis & Spirakis 2008; Deligkas et al. 2017, 2023) used the non-convex maximum regret; the convexity observation directly justifies why a simple descent method suffices for zero-sum games, a fact that is not true for general-sum games. This is a genuine and non-obvious contribution.

2. **Closed-form directional derivative restricted to best-response sets (Theorem 4).** The directional derivative of V is expressed using only the current best-response sets, which enables the steepest-descent direction to be computed via a small LP (scaling with |BR| rather than n). This structural result is clean, well-derived, and is the computational enabler of the approach.

3. **Empirical evidence of sparse approximate best-response sets (Figures 2, 3).** The paper demonstrates that the ρ-best-response sets remain small (e.g., <10% of n for moderate δ), which supports the claim that per-iteration LPs are substantially smaller than the full game LP. This is a concrete, non-trivial empirical finding that justifies the method's design.

## Weaknesses

### Major

1. **The claimed geometric convergence is not established in the visible text.** The abstract and Section 1.1 assert that the algorithm "achieves a geometric decrease in the duality gap" and terminates in O((1/ρ)·log(1/δ)) iterations. However, the analysis in Section 4 stops at Lemmas 1–3, which bound the directional derivative from below by −δ. There is no descent lemma showing that taking a step along the minimizing direction reduces V by a multiplicative factor, no step-size analysis, no iteration-wise bound, and no convergence theorem. Given that V is piecewise-linear convex (not strongly convex), geometric convergence is not a standard consequence of the lemmas provided. This gap is verifiable from the paper as written — the analysis simply does not connect the directional derivative bounds to the claimed iteration complexity. If the proof was in a section stripped by the parser, the main text should at minimum outline the argument.

2. **The algorithm is not fully described in the visible text.** Section 4.1 is titled "THE ALGORITHM" but contains only the sentence "We now present our algorithm." before immediately transitioning to Section 5. "Algorithm 2" is referenced multiple times in the experiments and conclusion (e.g., "Size of LPs in Algorithm 2", "reuse the LP solutions we get in Algorithm 2") but is never presented. Key details necessary for reproducibility — how the direction-minimization LP is constructed, how the step size ε is chosen, the stopping criterion — are discussed only at a conceptual level scattered through the text. Even if pseudocode existed in a stripped appendix, the main body's section dedicated to the algorithm is essentially empty, which is an unusual presentation gap.

3. **No experimental comparison to zero-sum-specific iterative algorithms.** The experiments compare only against SciPy's general-purpose interior-point LP solver. The paper does not compare against methods designed specifically for zero-sum games that avoid LPs entirely: Multiplicative Weights Update (MWU), extra-gradient, optimistic gradient, or Nesterov's smoothing (Hoda et al. 2010; Gilpin et al. 2012), all of which are discussed in the related work. Since the paper's stated motivation includes "simpler algorithms" and improved complexity for zero-sum games, the absence of any comparison to these baselines makes it impossible to assess whether the proposed approach offers any practical advantage over existing iterative methods.

### Minor

4. **Unclear positioning relative to existing iterative methods.** The paper motivates the approach as providing "simpler algorithms" compared to solving a single LP, yet the proposed method solves an LP in every iteration (albeit a smaller one). The paper does not discuss the trade-off: when would solving many small LPs be preferable to solving one large LP, or to LP-free iterative methods? This weakens the paper's narrative about its contribution's significance, though it does not invalidate the technical content.

### Trivial

- None significant.

## Nice-to-Haves

- Provide convergence guarantees for a concrete step-size schedule (even a sublinear O(1/k) rate would be a verifiable result).
- Include wall-clock time comparisons against at least one of MWU, extra-gradient, or Nesterov smoothing in addition to the LP solver.
- Discuss variance/error bars for the experimental plots (Figures 1-3 show only averages).

## Removed Points

- **"Table 1 data is missing / absent from the paper."** The table exists in the original PDF as an embedded image (line 195). Its textual data was not extractable by the PDF parser. This is a formatting/parser artifact, not an author error. Per the Hard Rules, this criticism is removed.
- **"The paper claims geometric convergence in the abstract but it's not proven; the algorithm is not described."** These criticisms are kept as Major weaknesses above because they highlight genuine gaps in the visible text. However, it should be noted that if the convergence proof and algorithm pseudocode existed in sections stripped by the parser (as is common in this dataset format — the paper has no bibliography section, and Algorithm 2 is referenced without definition), the appearance of missing content may be partially attributable to extraction, not author omission. The criticisms are retained because Section 4.1 ("THE ALGORITHM") in the main body is essentially empty, which is atypical even for stripped content.
- **Strength: "Theoretical iteration complexity bound (Section 1.1)."** Removed because the bound is claimed but not supported by any visible proof. A claimed but unproven result is not a genuine strength.
- **Strength: "Experimental evidence of comparable running time to standard LP solvers (Table 1)."** The table data is in an image and its numerical content cannot be verified from the extracted text. Removed for lack of verifiable evidence in the extracted version, though the paper's text does reference such a comparison.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not identify any non-obvious implication of the work that the paper itself does not discuss.

## Suggestions

1. **If the convergence proof and algorithm pseudocode exist in the original submission (e.g., in a now-stripped appendix),** ensure they are present in the main body for any resubmission. The main text should contain at minimum: (a) a pseudocode listing of the algorithm, (b) a convergence theorem statement with a sketched proof, and (c) a clear specification of the step-size parameter ε and the stopping condition.

2. **Clarify the descent argument.** Show how the directional derivative bound (Lemma 3) translates into a per-iteration decrease in V. Even a sublinear O(1/k) convergence rate would be a meaningful, provable result; the paper should either prove the claimed geometric rate or drop that claim.

3. **Add comparisons to iterative zero-sum algorithms.** Running time and iteration count comparisons against MWU, extra-gradient, or Nesterov smoothing would significantly strengthen the evaluation. At minimum, acknowledge why these baselines are not included and discuss how the proposed method compares in terms of per-iteration cost and convergence guarantees.

4. **Discuss the LP-per-iteration trade-off explicitly.** Under what conditions (game size, structure, desired accuracy) would solving many small LPs be preferable to solving one large LP or using LP-free iterative methods?
