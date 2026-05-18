Now I have a thorough understanding of the paper and can write the consolidated review.

## Summary

This paper studies learning hierarchical polynomials of the form \(h = g \circ p\) (where \(p\) is degree-\(k\), \(g\) is degree-\(q\)) over Gaussian inputs using a three-layer neural network with a residual connection. The main result shows that for a structured subclass of degree-\(k\) polynomials \(p\) (satisfying an independent-components decomposition), a layerwise gradient-descent algorithm learns the target with \(\widetilde O(d^k)\) samples — a strict improvement over kernel methods which require \(\widetilde\Omega(d^{kq})\) samples. For the special case of quadratic features (\(k=2\)), the paper achieves \(\widetilde O(d^2)\) sample complexity, improving over prior work (Nichani et al., 2023) that required \(\widetilde\Theta(d^4)\). The key technical innovation is an "approximate Stein's lemma" showing that the degree-\(k\) Hermite projection of \(g \circ p\) is approximately proportional to \(p\) itself.

---

## Strengths

1. **Provable sample complexity improvement over kernel methods.** Theorem 3.1 shows that the three-layer network learns the target with \(\widetilde O(d^k)\) samples, whereas kernel methods require \(\widetilde\Omega(d^{kq})\) samples (a factor exponential in the degree of \(g\)). This improvement is clearly stated and directly supported by the theorem statement (lines 213–221) and the comparison to the cited lower bound of Ghorbani et al. (2021).

2. **Extension from quadratic features to degree-\(k\) polynomial features.** Prior theoretical work on three-layer networks (Nichani et al., 2023; Allen-Zhu & Li, 2019) was restricted to quadratic features or required the composition strength \(\alpha\) to be vanishingly small. This paper generalizes to arbitrary constant degree \(k\) while maintaining a \(\widetilde O(d^k)\) sample complexity. The extension is driven by the approximate Stein's lemma (Lemma 3.3), which is the paper's main theoretical contribution.

3. **Optimal sample complexity for quadratic features (Corollary 3.2).** When \(p\) is quadratic, the algorithm achieves \(\widetilde O(d^2)\) samples, which matches the parametric dimension of the quadratic feature and improves over the \(\widetilde\Theta(d^4)\) of the prior state of the art. The paper provides a clear explanation for why multiple gradient steps in stage 1 are the source of this improvement (Section 5.1).

4. **Two-stage feature-learning analysis.** The proof decomposes training into two interpretable stages: (i) kernel regression that recovers the feature \(p\) from the low-degree part of \(h\), and (ii) one-dimensional random-feature regression to fit the link function \(g\). This provides a concrete mechanistic explanation for how three-layer networks can exploit hierarchical structure that kernel methods cannot.

5. **Approximate Stein's lemma as a theoretical tool.** Lemma 3.3 is the paper's main technical contribution and is conceptually clean. It uses the Central Limit Theorem intuition that \(p\), being a sum of many independent components, is approximately Gaussian, so that Stein's lemma approximately applies. The result is a quantitative bound showing \(\|\mathcal{P}_k h - \mathbb{E}[g'(z)]\,p\| = O(d^{-1/2})\).

---

## Weaknesses

### Fatal
None.

### Major
None.

The paper's core claims are well-supported by the theoretical analysis. The weaknesses below are real but do not undermine the central findings.

### Minor

1. **Imprecise sample complexity framing in the abstract and summary statements.** The abstract and line 219 state that the target is learned in "\(\widetilde O(d^k)\) samples." However, Theorem 3.1 states that for any \(\alpha \in (0,1)\), the required sample size is \(n \ge d^{k+3\alpha}\) to achieve error \(\widetilde O(d^{-\alpha})\). Since \(\alpha\) is an absolute constant in \((0,1)\), the leading exponent is \(k+3\alpha\), not \(k\). The factor \(d^{3\alpha}\) is polynomial in \(d\) (up to \(d^3\)), not logarithmic. While one can reparameterize in terms of target error \(\varepsilon\) to recover an \(\widetilde O(d^k \cdot \text{poly}(1/\varepsilon))\) form, the current framing conflates this with a pure \(d^k\) dependence. The theorem itself is stated correctly and the imprecision is only in the summarizing language, but it is misleading enough that a reader could overestimate the tightness of the bound. **This affects the exposition, not the validity of the result.**

2. **"Information-theoretically optimal" claim for the quadratic case lacks a formal lower bound.** The paper states that the \(\widetilde O(d^2)\) sample complexity for \(k=2\) "matches the information-theoretically optimal sample complexity" (abstract, Corollary 3.2, line 338). However, no formal lower bound is stated, cited, or proved — not even a sketch. The heuristic justification (the quadratic \(p\) has \(\Theta(d^2)\) parameters) is plausible but does not account for the hierarchical structure \(g \circ p\) or the fact that the algorithm requires the extra constraint \(\|A\|_{op} = O(1/\sqrt{d})\). A cited lower bound or a brief information-theoretic argument would substantiate the claim. Without it, the optimality assertion is an informal observation rather than a proven result.

3. **The feature class (Assumption 2.2) is restrictive in ways that limit the scope of the generalization claim.** The assumption requires \(p\) to decompose as a sum of independent components \(\psi_i\) depending on orthogonal subspaces, with \(L = \Theta(d)\) balanced coefficients. While the paper provides two natural examples (orthogonally decomposable tensors and sums of sparse parities), the assumption excludes many degree-\(k\) polynomials. The paper states that the result applies to "a large subclass" but does not quantify how large this subclass is relative to all degree-\(k\) polynomials. The claim of generalizing prior work ("restricted to the case of \(p\) being a quadratic") is accurate in the sense of going from \(k=2\) to general \(k\), but both the current work and the prior quadratic-specific work impose structural restrictions on \(p\). The paper acknowledges this in the future work section but could more clearly calibrate reader expectations about the scope.

4. **The training algorithm is substantially engineered and departs from end-to-end training.** Algorithm 1 uses layerwise gradient descent with sample splitting (separate datasets for each stage), frozen random features \((a,b,s,V)\), weight decay, specific heavy-tailed bias initialization, and a degree-\(k\) polynomial activation \(\sigma_1\). Each of these choices is justified by the analysis, but together they make the gap between the algorithm studied and "three-layer neural networks trained via gradient descent" as used in practice quite wide. The paper acknowledges this (lines 347–348) and references experiments in the appendix using more standard procedures, but the main text does not summarize those experiments. **This is a common gap in theoretical ML papers and is not fatal**, but readers should calibrate what the result implies about practical training.

### Trivial

None.

---

## Nice-to-Haves

- **Clarify the error floor from Lemma 3.3.** The approximate Stein lemma gives an \(L^2\) error of \(O(d^{-1})\) (squared) between \(\mathcal{P}_k h\) and \(c p\). The theorem's error \(\widetilde O(d^{-\alpha})\) with \(\alpha < 1\) is always larger than \(d^{-1}\) asymptotically, so there is no contradiction, but stating this explicitly would be helpful.

- **Briefly discuss the information exponent assumption.** Assumption 2.3 requires \(\mathbb{E}[g'(z)] = \Theta(1)\) (information exponent 1). A remark connecting this to the single-index literature and explaining what changes if the information exponent is larger would improve the framing.

- **Include a short summary of the experiments in the main text.** The paper references experiments in the appendix but does not describe them in the main body. A 2–3 sentence summary of what was tested and how it validates the theory would strengthen the paper for readers who do not read the appendix.

- **Discuss the necessity of polynomial activation \(\sigma_1\).** The analysis relies on \(\sigma_1\) being exactly a degree-\(k\) polynomial. A remark on whether smooth non-polynomial activations (e.g., ReLU, erf) could be accommodated via polynomial approximation, and whether the results would degrade gracefully, would be useful.

---

## Removed Points

These points from the original reviews were flagged for removal with justification:

- **"The present work imposes an additional structural decomposition that was not required in the quadratic case of prior work."** — This is factually incorrect. Prior work on the quadratic case (Nichani et al., 2023) also imposes restrictions on \(p\) (e.g., specific spectral properties of \(A\)). The paper shows its assumption for \(k=2\) is equivalent to \(\|A\|_F = 1, \|A\|_{op} = O(1/\sqrt{d})\), which is analogous to the restrictions in prior work. The generalization claim is about moving from \(k=2\) to arbitrary degree \(k\), not about having weaker assumptions.

- **Comments about inability to verify appendix proofs / "cannot see the appendix."** — The appendix is not available in this extraction; the rules state that weaknesses about missing appendix content should be removed.

- **"The proof sketch for Lemma 3.3 is heuristic" as a weakness.** — Proof sketches are by design heuristic; the full proof is in the appendix. This is not a weakness of the paper.

---

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface framing and presentation issues rather than uncovering new observations about the results.

---

## Suggestions

1. Revise the abstract and introduction to say "\(\widetilde O(d^{k+o(1)})\) samples" or "\(\widetilde O(d^k \cdot \text{poly}(1/\varepsilon))\) for any target error \(\varepsilon\)" to accurately reflect the \(d^{3\alpha}\) factor in the theorem.

2. Either add a formal lower bound for the quadratic case (or cite an existing one) to substantiate the "information-theoretically optimal" claim, or downgrade the language to "matches the parametric dimension" / "is optimal up to logarithmic factors."

3. After stating Assumption 2.2, add an explicit sentence: "This is the main restriction of our work — we require \(p\) to be approximately Gaussian under \(\gamma\) via a CLT-type argument, which holds for polynomials decomposable into many independent components with orthogonal subspaces."

---

## Score and Decision

**Originality:** Good — the approximate Stein's lemma is a new technical tool, and extending the class of learnable hierarchical features from quadratic to arbitrary degree \(k\) is a meaningful advance.  
**Importance of question:** High — understanding feature learning in deep networks and the sample complexity advantage over kernels is a central problem in ML theory.  
**Claims supported:** Mostly — the main theorem is precise, but the summary language (\(\widetilde O(d^k)\)) is slightly loose, and the optimality claim is asserted without proof.  
**Soundness:** Appears sound based on the presented arguments; the core proofs are deferred to the appendix but the sketch is coherent.  
**Clarity:** Good — the paper is well-structured and the intuition is clearly conveyed.  
**Value to community:** Positive — a solid theoretical contribution that advances understanding of hierarchical feature learning.

None of the identified weaknesses are fatal or threaten the paper's core contributions. The paper is a meaningful advance over prior work and the analysis appears technically sound. The minor issues are addressable in a revision.

**Score:** 7.0

**Decision:** Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>