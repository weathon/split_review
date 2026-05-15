Now I have all the information needed. Let me construct the consolidated review.

---

## Summary

This paper studies learning hierarchical polynomials of the form \(h = g \circ p\) over Gaussian inputs using three-layer neural networks, where \(p\) is a degree-\(k\) polynomial feature and \(g\) is a degree-\(q\) polynomial link function. The main result (Theorem 3.1) proves that for a specific subclass of features \(p\) that decompose into many orthogonal, independent components, a layerwise-trained three-layer network achieves test error \(\widetilde O(d^{-\alpha})\) with sample complexity \(\widetilde O(d^k)\). For the special case of quadratic features (\(k=2\)), this yields the information-theoretically optimal \(\widetilde O(d^2)\) sample complexity, improving on the prior \(\widetilde\Theta(d^4)\) bound from Nichani et al. (2023). The key technical innovation is an "approximate Stein's Lemma" showing that the degree-\(k\) Hermite projection of \(h = g\circ p\) is approximately proportional to the feature \(p\) itself.

## Strengths

- **Optimal sample complexity for quadratic features (Corollary 4.2):** The paper achieves \(\widetilde O(d^2)\) samples when \(p\) is a quadratic satisfying \(\|A\|_F=1,\ \|A\|_{op}=O(1/\sqrt{d})\), which matches the information-theoretic lower bound. This is a strict and substantial improvement over the \(\widetilde\Theta(d^4)\) bound in Nichani et al. (2023). The explanation for the improvement (running many GD steps instead of a single large step to fully extract the feature) is clear and well-motivated.

- **Extension from quadratic to degree-\(k\) polynomial features:** Theorem 3.1 generalizes prior work (which was restricted to \(k=2\)) to arbitrary \(k\ge2\), showing that three-layer networks can learn \(h = g\circ p\) in \(\widetilde O(d^k)\) samples. The approximate Stein's Lemma (Lemma 4.3) is a genuine technical novelty that enables this generalization.

- **Sharp separation from kernel methods:** The \(\widetilde O(d^k)\) sample complexity for three-layer networks is contrasted with the \(\widetilde\Omega(d^{kq})\) lower bound for NTK methods, clearly demonstrating the advantage of feature learning over fixed-feature approaches. This exponential-in-\(q\) improvement is a clean and compelling result.

- **Rigorous two-stage analysis:** The proof cleanly decomposes into feature learning (stage 1, via kernel regression to fit the low-degree projection of \(h\)) and link function learning (stage 2, via 1D kernel regression). The analysis is mathematically sound and provides a concrete mechanism for how depth enables hierarchical learning.

## Weaknesses

### Fatal
None.

### Major
- **The feature class is quite restricted, limiting the breadth of the claimed contribution.** Assumption 3 requires \(p(x) = \frac{1}{\sqrt{L}}\sum_{i=1}^L \lambda_i \psi_i(x)\) where (i) each \(\psi_i\) depends on a separate orthogonal subspace of dimension \(\le k\), (ii) \(L = \Theta(d)\), (iii) the \(\lambda_i\) are balanced, and (iv) each \(\psi_i\) is a degree-\(k\) polynomial. This rules out many natural features: for instance, a low-rank quadratic \(p(x) = x^\top A x\) with \(A\) having \(o(d)\) nonzero eigenvalues fails the \(L=\Theta(d)\) condition. The proof of the approximate Stein's Lemma crucially depends on the CLT enabled by many independent summands — if \(L = o(d)\), the CLT error would degrade and potentially dominate the guarantee. While the paper notes that extending to \(L=\omega_d(1)\) is possible "at the expense of a worse error floor," it does not quantify this tradeoff. The two concrete examples given (orthogonally decomposable tensors and sparse parities) are indeed the only cases covered. The paper's framing of "a broad class" of hierarchical functions somewhat overstates what is actually a carefully engineered subclass.

- **The training algorithm is layerwise, non-standard, and requires knowledge of \(k\).** The activation \(\sigma_1\) is required to be a degree-\(k\) polynomial with \(\sigma_1^{(k)}(0)=\Theta(1)\), meaning the learner must know the degree of \(p\) to design the network architecture. The algorithm uses sample splitting (\(\mathcal{D}_1,\mathcal{D}_2\)), frozen parameters (\(a,b,s,V\) never trained), a specific weight decay schedule (\(\xi_1 = 2m_1/d^{k+\alpha}\)), and layerwise sequential updates. This is far from end-to-end gradient descent as used in practice. While the paper acknowledges this in the Discussion, noting that experiments (in the appendix) use "more standard training procedures," the theoretical result itself applies to a highly engineered training protocol. This weakens the paper's narrative that three-layer neural networks *as typically used* can efficiently learn hierarchical functions.

### Minor
- **The paper does not quantify how the error floor degrades when \(L \neq \Theta(d)\).** The remark that the result extends to \(L = \omega_d(1)\) "at the expense of a worse error floor" is too vague. The CLT error in Lemma 4.2 is \(O(d^{-1/2})\) because \(L=\Theta(d)\); if \(L = d^\gamma\) for \(\gamma<1\), the error would scale as \(O(L^{-1/2}) = O(d^{-\gamma/2})\), potentially dominating the \(\widetilde O(d^{-\alpha})\) guarantee. The paper should at least discuss this tradeoff.

- **The comparison to Nichani et al. is slightly asymmetric.** The paper's algorithm requires polynomial \(g\) with \(g'(0)=\Theta(1)\) (information exponent 1), while Nichani et al. handles 1-Lipschitz link functions and more general activations. The paper correctly acknowledges this in Section 5.1, but the abstract's claim of "generalizing" prior work to degree \(k\) does not mention the tradeoff in link function generality.

### Trivial
None.

## Nice-to-Haves
- A discussion of how the requirement of knowing \(k\) might be relaxed (e.g., via overparameterization or generic nonlinear activations with non-zero Hermite coefficients at all degrees) would strengthen the paper's practical relevance.
- Quantifying the dependence of the error on \(L\) (when \(L\) is not exactly \(\Theta(d)\)) would make the extension claim more concrete.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"No experimental evidence in main text"** — The reviewer criticized that experiments are absent from the main text and that the claimed empirical validation in the appendix "is not assessable." This is removed because the parser strips appendix sections from all papers. The paper states that experiments exist in the appendix; this is not a flaw in the paper's scientific content.

2. **"The approximate Stein's Lemma sketch relies on CLT/cumulant control that cannot be assessed without seeing the full proof"** — The paper provides a clear proof sketch (Section 4.3) and states the full proof is in the appendix. The parser strips the appendix. The sketch is sufficient for a main-text treatment, and the claim that the proof "cannot be assessed" is a formatting artifact, not a content issue.

3. **"The future work conjecture about extending to non-orthogonal features is too vague"** — This is a conjecture explicitly labeled as future work. Criticizing it for being speculative misunderstands the purpose of a future work section.

## Novel Insights

A genuinely novel observation emerges from comparing the reviewers' assessments: the paper's core mechanism — using the approximate Stein's Lemma to show that the low-degree Hermite projection of a composition \(g\circ p\) is approximately proportional to the inner feature \(p\) — is a genuinely new technical tool that may have broader applicability. The key insight is that when the feature \(p\) is a sum of many independent low-degree components, it becomes approximately Gaussian by the CLT, and thus an approximate version of Stein's lemma applies. This technique could potentially be used to analyze learning of other hierarchical functions where the inner feature satisfies a CLT-type concentration property. Both the harsh reviewer and the strength finder agree this is the paper's main technical contribution, and neither offers a refutation of its correctness.

## Suggestions

1. **Quantify the \(L\)-dependence explicitly.** The claim that results extend to \(L = \omega_d(1)\) "at the expense of a worse error floor" should be accompanied by a precise statement. If \(L = d^\gamma\), what is the error floor? This would significantly strengthen the paper's discussion of limitations.

2. **Add a small simulation in the main text.** While the appendix experiments cannot be assessed by the reviewer, adding a single simple figure (e.g., a 1D scatter plot showing \(g_{u,s,V}\) approximating \(p\) after stage 1) in the main text would make the empirical claim more credible to readers.

3. **Tone down the "broad class" language.** The paper's Assumption 3 is quite restrictive. Replacing phrases like "a broad class of hierarchical functions" with more precise language like "a class of features that decompose into many independent orthogonal terms" would more accurately reflect the scope.

## Score and Decision

**Overall assessment:** This is a solid theoretical contribution. The extension from quadratic to degree-\(k\) polynomial features is a genuine advance, and the optimal \(\widetilde O(d^2)\) sample complexity for quadratics is a clean result. The approximate Stein's Lemma is a novel technical tool. However, the restrictive feature class and non-standard training algorithm mean the paper's practical implications are more limited than the narrative suggests. The paper would be a clear accept at a theory-focused venue (COLT, ALT, NeurIPS theory track). The weaknesses are substantive but not fatal — they bound the scope rather than invalidating the core claims.

**Originality:** Good — extends a known line of work with a new technical tool (approximate Stein's Lemma) and non-trivial analysis.

**Importance of research question:** High — understanding how neural networks learn hierarchical features is a central question in deep learning theory.

**Claims well-supported:** Yes, for the stated assumptions. The claims are precise and the proofs are rigorous.

**Soundness of experiments:** Not assessable from the main text (appendix stripped), but this is a theory paper and the theoretical results are the primary contribution.

**Clarity of writing:** Good — well-structured, clear notation, transparent about assumptions.

**Value to community:** Positive — the approximate Stein's Lemma technique may find further applications, and the optimal quadratic result cleanly resolves a known gap.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>