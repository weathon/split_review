Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper studies learning hierarchical polynomials of the form \(h = g \circ p\) (where \(p\) is degree-\(k\), \(g\) is degree-\(q\)) using a three-layer neural network with a residual connection, trained via layerwise gradient descent. The main result shows that for a large subclass of degree-\(k\) features \(p\) (satisfying a CLT-type decomposition), the network learns the target with sample complexity \(\widetilde O(d^k)\) and polynomial time, improving over kernel methods which require \(\widetilde\Omega(d^{kq})\) samples. The key technical innovation is an "approximate Stein's lemma" showing that the degree-\(k\) Hermite projection of \(g\circ p\) is close to a constant multiple of \(p\) itself, enabling the first training stage to recover the hidden feature.

## Strengths

1. **Sample complexity improvement over kernel methods (verified).** Theorem 1 proves that the three-layer network learns \(h = g\circ p\) with \(\widetilde O(d^k)\) samples, whereas kernel methods require \(\widetilde\Omega(d^{kq})\) samples. This is a strict improvement by a factor of \(d^{q-1}\) and is the paper's central contribution. The separation is clean and well-motivated.

2. **Approximate Stein's lemma as a genuine technical innovation (verified).** Lemma 3.3 (lem:approximate_stein) shows that \(\|\mathcal{P}_k h - \mathbb{E}[g'] p\|_{L^2} = O(d^{-1/2})\) and \(\|\mathcal{P}_{<k} h\|_{L^2} = O(d^{-1/2})\), extending a prior quadratic-only result (Nichani et al. 2023) to degree-\(k\) polynomial features. This lemma is the key enabler for feature recovery in the first training stage and may be of independent interest.

3. **Explicit algorithm and modular proof structure (verified).** Algorithm 1 provides a concrete layerwise training procedure with specified hyperparameters. The proof decomposes cleanly into two convex stages (kernel-type regression in stage 1, random feature model in stage 2), making the analysis verifiable and modular.

4. **Concrete feature examples (verified).** The paper provides two explicit classes satisfying the feature decomposition (Assumption 3): orthogonally decomposable tensors (e.g., \(p(x) = \sum_i \lambda_i h_k(v_i^\top x)\)) and sums of sparse parities. These examples illustrate the scope of the results concretely.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Imprecise optimality claim for quadratic features.** The paper states (line 234, line 338) that for quadratic features the algorithm achieves \(\widetilde\Theta(d^2)\) sample complexity, "matching the information-theoretically optimal sample complexity." However, Corollary 1 requires \(n \geq d^{2+3\alpha}\) to achieve squared error \(\widetilde O(d^{-\alpha})\). The \(\widetilde O(d^2)\) phrasing is standard for hiding polylog factors, but \(d^{2+3\alpha}\) for any fixed \(\alpha>0\) is \(d^{2+\Omega(1)}\), which is more than just a polylog factor. The sample complexity for *vanishing* error is \(d^{2+o(1)}\) rather than exactly \(d^2\). The information-theoretic lower bound \(\Omega(d^2)\) is for learning a quadratic to *constant* error, not vanishing error. The improvement over prior work (\(\widetilde\Theta(d^4)\)) remains substantial, and the claim would be more precise as "nearly optimal" or with explicit qualification of the error tolerance. This does not affect the validity of Theorem 1 or Corollary 1.

2. **Restrictiveness of the feature class (Assumption 3).** The feature decomposition requires \(p = \frac{1}{\sqrt{L}}\sum_{i=1}^L \lambda_i \psi_i(x)\) with \(L = \Theta(d)\), orthogonal rank-\(\leq k\) subspaces, and independence across terms. As the paper notes (Remark after Assumption 3), this is essentially the condition that \(p\) is approximately Gaussian via the CLT. While the two examples given (orthogonal tensor, sparse parities) are natural, the paper does not quantify how large this subclass is among all degree-\(k\) polynomials. The paper acknowledges this scope (line 172: "Our results can easily be extended to any \(L = \omega_d(1)\)") and discusses generalizations in the future work section, so this is a known limitation rather than an oversight.

3. **Polynomial activation assumption (Assumption 4).** The analysis requires \(\sigma_1\) to be *exactly* a degree-\(k\) polynomial with leading coefficient \(\Theta(1)\). Prior work (e.g., Nichani et al. 2023; Ba et al. 2022) often only requires a non-zero \(k\)-th Hermite coefficient, which holds for many standard activations (ReLU, sigmoid, etc.). The paper does not discuss whether the result extends to activations with non-zero \(k\)-th Hermite coefficient but lower-degree terms. This limits the practical scope of the theory.

4. **Error bound not expressed directly as a function of \(n\).** Theorem 1 parameterizes the error as \(\widetilde O(d^{-\alpha})\) with sample size \(n \geq d^{k+3\alpha}\). This means the error is not directly expressed as a function of \(n\) in closed form. A statement like "for any \(\epsilon > 0\), with \(n \geq d^k \cdot \operatorname{poly}(1/\epsilon)\) samples, the algorithm achieves error \(\epsilon\)" would be more conventional and interpretable. The current parameterization by \(\alpha\) obscures the rate. This is a presentation choice, not a technical flaw.

5. **No explicit discussion of the computational complexity exponent.** While "polynomial time" is claimed, the runtime depends on \(T_1, T_2 = \operatorname{poly}(d, m_1, n)\) with \(m_1 = d^{k+\alpha}\) and \(n = d^{k+3\alpha}\), giving a runtime that could scale as \(d^{Ck}\) for an implicit constant \(C\). A brief comment on the exponent would help assess practical feasibility.

### Trivial
- The weight decay parameter \(\xi_1 = 2m_1/d^{k+\alpha}\) depends on \(k\) and \(\alpha\), which the modeler would not know in practice. The paper could note this is a theoretical choice, not a practical prescription.

## Nice-to-Haves
- A discussion of whether the result extends to activations with non-zero \(k\)-th Hermite coefficient (beyond exact degree-\(k\) polynomials) would broaden applicability.
- An explicit characterization of how many degree-\(k\) polynomials satisfy Assumption 3 (e.g., by counting parameters or showing random tensors satisfy it with high probability) would help readers assess scope.
- Expressing the error bound directly as a function of \(n\) (rather than via \(\alpha\)) would improve readability.

## Removed Points

The following points from the reviews were removed with justification:

1. **Harsh Critic's "Critical Issue 1" (inconsistency between Lemma 4 and Theorem 1).** The critic claims the final error cannot be better than \(\Omega(d^{-1/2})\) when \(\alpha > 1/2\), but this is based on a mathematical error. Lemma 4 gives bounds in **L2 norm** (\(O(d^{-1/2})\)), while Lemma 2 gives bounds in **squared L2 norm** (\(\widetilde O(d^{-\alpha})\), i.e., L2 norm \(\widetilde O(d^{-\alpha/2})\)). Properly combining them: \(\|h_\theta - \mathbb{E}[g']p\| \leq \widetilde O(d^{-\alpha/2}) + O(d^{-1/2})\). For \(\alpha \in (0,1)\), \(\alpha/2 \in (0, 0.5)\), so \(d^{-\alpha/2} > d^{-0.5}\), meaning the \(\widetilde O(d^{-\alpha/2})\) term **dominates** the \(O(d^{-1/2})\) floor, not the other way around. The squared error is thus \(\widetilde O(d^{-\alpha})\), consistent with Theorem 1. The critic's "\(\alpha > 1/2\) threshold" is an artifact of conflating squared and unsquared norms. **This is a factual error by the reviewer and is removed.**

2. **Criticism about missing appendix/content.** Removed per hard rules (parser strips appendices — they exist in the original submission).

3. **Generic formatting/style nitpicks and reproducibility complaints about undisclosed details.** Removed per hard rules.

4. **Strength Finder's claim about "information-theoretic optimal sample complexity" as an unqualified strength.** The "optimality" claim has the caveat described in Minor Weakness 1 above. This strength is retained but qualified.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface a genuinely novel insight that the paper itself does not already articulate. The approximate Stein's lemma and its consequences for feature learning are the paper's own contributions.

## Suggestions

1. Qualify the optimality claim for quadratic features: state the sample complexity as \(d^{2+o(1)}\) for vanishing error, and distinguish between achieving vanishing error vs. constant error when comparing to the information-theoretic lower bound.

2. Add a remark discussing whether the analysis extends to activations with non-zero \(k\)-th Hermite coefficient (not just exact degree-\(k\) polynomials), to broaden the practical scope.

3. Consider restating the error bound more directly as a function of \(n\) (e.g., "for any \(\epsilon > 0\), with \(n \geq d^k \cdot \operatorname{poly}(1/\epsilon)\) samples, the algorithm achieves error \(\epsilon\)").

4. Add a brief comment on the exponent of the polynomial runtime to help readers assess practical feasibility.

## Score and Decision

The paper studies a well-motivated and technically challenging problem, provides a genuine technical innovation (the approximate Stein's lemma for degree-\(k\) features), and proves a clear sample complexity improvement over kernel methods. The analysis is rigorous and the proof structure is modular and verifiable. The main technical claims are internally consistent (the harsh critic's central objection is based on a mathematical error involving norm conventions). The limitations are openly acknowledged by the authors and are reasonable for a theoretical paper of this scope. The weaknesses identified are minor and do not undermine the core contribution. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>