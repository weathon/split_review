I now have a thorough understanding of the paper and have verified each claim from the reviews against the actual paper content. Let me produce the consolidated review.

## Summary

This paper studies the theoretical problem of learning hierarchical polynomials of the form \( h = g \circ p \) (where \(p\) is a degree-\(k\) polynomial feature and \(g\) is a degree-\(q\) polynomial link function) using three-layer neural networks trained with layerwise gradient descent. The main result (Theorem 3.1) shows that for a structured subclass of degree-\(k\) features \(p\) with orthogonal independent components, the network learns \(h\) with \(\widetilde O(d^k)\) samples — improving over kernel methods (\(\widetilde \Omega(d^{kq})\)) and over prior three-layer results that were restricted to quadratic features. The key technical innovation is an approximate Stein lemma (Lemma 3.2) showing that the degree-\(k\) Hermite projection of \(h\) is approximately proportional to \(p\), enabling the first training stage to extract the feature in \(d^k\) samples.

## Strengths

1. **Sample complexity improvement over kernel methods and prior three-layer guarantees** — The paper proves that three-layer networks achieve \(\widetilde O(d^k)\) sample complexity for learning \(h = g \circ p\) under the stated assumptions, whereas kernel methods require \(\widetilde \Omega(d^{kq})\) (citing Ghorbani et al., 2021). For the quadratic case \(k=2\), the paper achieves \(\widetilde O(d^2)\), a strict improvement over Nichani et al. (2023)'s \(\widetilde \Theta(d^4)\). This is a genuine advance in the theoretical understanding of feature learning in deeper networks.

2. **Extension to degree-\(k\) polynomial features beyond quadratics** — Prior work on three-layer networks (Nichani et al., 2023; Allen-Zhu & Li, 2019; Safran et al., 2022; Ren et al., 2023) was restricted to specific features (quadratics, norms, ball indicators). This paper extends provable guarantees to a broader class of degree-\(k\) polynomial features, including orthogonally decomposable tensors and sums of sparse parities (Remark 3.1). The technical machinery (approximate Stein lemma, multi-step GD analysis) is meaningfully more general than prior quadratic-only analyses.

3. **Approximate Stein lemma as a nontrivial technical innovation** — Lemma 3.2 shows that the degree-\(k\) projection of \(h = g \circ p\) is approximately \(\mathbb{E}[g'(z)]\, p\) up to \(O(d^{-1/2})\) error, and that lower-degree projections are negligible. This generalizes the classical Stein lemma beyond linear features and is the paper's core insight enabling feature recovery with only \(\widetilde O(d^k)\) samples.

4. **Clean two-stage analysis with transparent proof sketch** — The paper decomposes training into a feature-learning stage (kernel regression in \(d\)-dimensions to extract \(p\)) and a link-function-fitting stage (1D random feature model to learn \(g\)). The proof sketch in Section 4 is well-organized and clearly explains how the approximate Stein lemma bridges the two stages.

5. **Clear positioning against related work** — The paper carefully quantifies improvements over kernel methods (NTK), two-layer networks, and prior three-layer guarantees, including a detailed comparison with Nichani et al. (2023) explaining why multi-step GD improves sample complexity over single-step approaches (Section 5.1).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Unsupported claim of "information-theoretic optimality" for the quadratic case** — The abstract and Corollary 3.2 state that the \(\widetilde O(d^2)\) sample complexity for quadratics "matches the information-theoretically optimal sample complexity" / "matches the information-theoretic lower bound." However, the paper provides neither a proof nor a citation for such a lower bound for this specific function class (learning \(g(x^\top A x)\) with Gaussian data). The only lower bound cited (Ghorbani et al., 2021) is for NTK, a different comparison class. The claim is plausible (the matrix \(A\) has \(\Theta(d^2)\) degrees of freedom), but it is not substantiated. The language should either be softened to "matches the parametric rate for a quadratic feature" or backed by a cited/proved lower bound.

2. **Feature class requires orthogonal independent components — a genuine but transparent limitation** — The main assumption (Assumption 3.1) requires \(p = \frac{1}{\sqrt{L}} \sum_i \lambda_i \psi_i(x)\) where each \(\psi_i\) depends on orthogonal vectors and the \(\psi_i\) are thus independent under the Gaussian measure. This is a structural restriction: it excludes interactions between the components (e.g., a generic symmetric tensor with overlapping subspaces). The paper is quite upfront about this — the abstract says "a large subclass," the introduction says "a large class," the assumption section says "a restricted class," and the future-work section explicitly states that generalizing to all degree-\(k\) polynomials is open. Nonetheless, this means the main result covers a narrower class than the paper's overall framing ("a broad class of hierarchical functions") might suggest to a casual reader. A more precise characterization of where the orthogonal-components assumption sits relative to the space of all degree-\(k\) polynomials would strengthen the paper.

3. **Algorithmic specificity of the layerwise training procedure** — The analysis relies on a non-standard training procedure (Algorithm 1): layerwise gradient descent with sample splitting, frozen lower layers during stage 2, weight decay on \(u\), and a polynomial activation \(\sigma_1\). The paper acknowledges this (Section 5.2) and notes that experiments with standard end-to-end training are in the appendix. However, the gap between the analyzed algorithm and practical training is larger than in some related work. This is bounded but worth noting.

### Trivial

1. **The tunable parameter \(\alpha\) makes the concrete rate opaque** — Theorem 3.1 states error \(\widetilde O(d^{-\alpha})\) with sample complexity scaling as \(d^{k+3\alpha}\). To get a concrete error like \(d^{-1/2}\), one sets \(\alpha=1/2\) and needs \(n \approx d^{k+1.5}\). The presentation with a free parameter is flexible but somewhat obscures what rate is actually achievable. A short example (e.g., "setting \(\alpha=1/2\) gives error \(\widetilde O(d^{-1/2})\) with \(n = \widetilde O(d^{k+1.5})\)") would be helpful.

2. **The bias distribution assumption (polynomial tail, bounded 8th moment) is technical but not standard** — The Student's \(t\) example helps, but the tail parameter \(p\) appears in stage-2 error bounds, making the presentation heavier. If the proof permits Gaussian biases, that would be cleaner.

## Nice-to-Haves

- **A concrete example illustrating the approximate Stein lemma.** Section 4.3 provides a heuristic CLT argument. A worked computation for a simple case (e.g., \(k=2\), \(p(x) = \frac{1}{\sqrt{d}}\sum_i (x_i^2-1)\)) showing why \(\mathcal{P}_2(g\circ p) \approx \mathbb{E}[g']\,p\) would make the technical centerpiece more accessible and help readers gauge the lemma's generality.

- **A lower bound (even a simple degree-of-freedom count) for the general \(k\) case** would sharpen the contribution. The paper provides upper bounds and compares with baselines, but a lower bound contextualizing the \(\widetilde O(d^k)\) guarantee would elevate the work. This is not required but would be a valuable addition.

- **Clarify how the error propagates from stage 1 to stage 2.** Lemma 4.2 (stage 2) assumes an approximation \(\hat p\) satisfying a closeness condition. A brief note on how the stage-1 error feeds through to the final guarantee would improve the proof sketch's completeness.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Criticism about missing experimental figures in the main body** (Harsh Critic: "the main paper does not contain any experimental figures"): REMOVED. The paper states "simulations in Section \ref{app:experiments}" and has `\input{experiments}` at line 323. The appendix is stripped by the parser; the experiments exist in the original submission.

- **Criticism about the feature class being "narrow" and the paper not being "upfront about this gap"**: REMOVED. The paper is actually quite transparent. The abstract says "a large subclass," the introduction says "a large class," the assumption section begins with "a restricted class," and the future-work section explicitly identifies generalization to all degree-\(k\) polynomials as open. The paper cannot be faulted for insufficient disclosure.

- **Criticism about missing appendix, missing proofs in appendix**: REMOVED. The parser strips appendix sections from all papers; they exist in the original submission.

- **Criticism about "role of constant α is somewhat artificial" as a weakness**: DOWNGRADED to trivial. This is a presentation choice, not a substantive flaw.

- **Criticism that stage-2 "representational power... is assumed but not analyzed"**: REMOVED. Lemma 4.2 (stage 2) explicitly states the existence of \(c^*\) with error bounds. The analysis exists in the appendix.

- **Criticism about "no lower bound for the general case" as a weakness**: MOVED to Nice-to-Haves. Absence of a lower bound does not undermine the paper's positive result.

- **Criticism about initialization choices being "tailored to the Hermite expansion analysis"**: REMOVED. These are standard design choices in this line of theoretical work; no paper in this genre uses "untailored" initialization.

- **Criticism about bias distribution being "exotic"**: DOWNGRADED to trivial. The Student's \(t\) example is a concrete instantiation. This is a technical condition common in theory papers.

- **"The paper should also cover Y / domain Z / additional tasks" style criticisms**: REMOVED as scope creep. The paper's future-work section already acknowledges extensions.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: The key technical insight — that the approximate Stein lemma allows feature extraction in \(\widetilde O(d^k)\) samples regardless of the link function's degree \(q\) — is well-articulated by the Strength Finder. The contrast between multi-step GD (this paper) and single-step GD (Nichani et al., 2023) as the reason for the \(d^4 \to d^2\) improvement in the quadratic case is also a valuable point of comparison that the reviews correctly highlight. Otherwise, the reviews largely confirm the paper's own narrative rather than adding new perspectives.

## Suggestions

1. **Fix the optimality claim.** Either cite a known information-theoretic lower bound for learning \(g(x^\top A x)\) with Gaussian data, provide a brief argument (e.g., a degrees-of-freedom counting or Fano-type bound), or soften the language to "matches the sample complexity of learning a generic quadratic feature" or "is optimal among methods that do not exploit additional structure."

2. **Add a concrete worked example for the approximate Stein lemma**, even just a 1-paragraph computation for \(k=2\) with a simple quadratic feature. This would make the paper's core technical contribution more transparent without requiring full appendix access.

3. **Consider stating Theorem 3.1 with a concrete \(\alpha\)** (e.g., \(\alpha=1\)) and noting that other rates follow by adjusting hyperparameters. This would make the achievable error/sample trade-off clearer to the reader.

## Score and Decision

This is a solid theoretical paper with a genuine technical contribution (the approximate Stein lemma) and a clear improvement over prior work. The main weakness — an unsupported optimality claim — is minor and easily correctable. The feature class restriction is a genuine limitation but is transparently disclosed. The paper makes meaningful progress on an important problem in the theory of deep learning.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>