- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 5, 8, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me synthesize the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper studies quantum algorithms for minimizing the maximum of \(N\) convex, Lipschitz functions, a fundamental problem in optimization and machine learning. The authors propose a quantum algorithm with query complexity \(\tilde{O}(\sqrt{N}\varepsilon^{-5/3} + \varepsilon^{-8/3})\) and prove a lower bound \(\tilde{\Omega}(\sqrt{N}\varepsilon^{-2/3})\), establishing near-optimal dependence on \(N\). The upper bound adapts the classical ball-optimization framework (Carmon et al., 2021) and accelerates the softmax sampling bottleneck via quantum Gibbs sampling; the lower bound uses a quantum progress-control argument with a multi-round unstructured search construction.

## Strengths

1. **Quadratic quantum speedup in \(N\) over the classical state of the art.** Table 1 and Theorem 1 clearly show the improvement from the classical \(O(N\varepsilon^{-2/3} + \varepsilon^{-8/3})\) (Carmon et al., 2021) to this paper's \(\tilde{O}(\sqrt{N}\varepsilon^{-5/3} + \varepsilon^{-8/3})\). The improvement from \(N\) to \(\sqrt{N}\) in the leading term is the paper's central algorithmic contribution and is clearly stated.

2. **Matching quantum lower bound (up to polylog factors).** Theorem 4 gives a lower bound of \(\tilde{\Omega}(\sqrt{N}\varepsilon^{-2/3})\) queries, establishing that the algorithm's dependence on \(N\) is optimal. The abstract explicitly notes this near-optimality, which is a definitive theoretical contribution.

3. **Novel lower-bound technique extending quantum progress control to this problem.** The paper identifies a key obstacle — naive quantum progress control fails because a single unstructured search problem has polynomially small success probability — and overcomes it by introducing a multi-round unstructured search problem that forces adaptive queries, showing that any quantum algorithm making \(O(N)\) queries across rounds has only super-polynomially small success. This is a non-trivial extension of the Garg et al. framework.

4. **Quantum Gibbs sampling to replace the classical sampling bottleneck.** The paper correctly identifies that classical BROO implementation requires \(\Omega(N)\) queries to sample from the softmax distribution. Algorithm 2 and Lemma 4 show that their quantum subroutine produces \(K\) samples using \(O(\sqrt{NK}\log(1/\delta))\) queries, which drives the speedup. The concrete algorithm (Quantum-Epoch-SGD-Proj, Algorithm 1) and the quantum sampling subroutine (Algorithm 3) are clearly presented.

## Weaknesses

### Fatal
None.

### Major

- **Gradient estimation from a zeroth-order oracle requires clarification.** Proposition 4 (line 140-142) claims that a single query to the quantum zeroth-order oracle \(O_f\) suffices to "output the gradient \(\nabla f_i(x)\)." This builds on Jordan (2005, Lemma 2.2), which is a standard result, but the paper does not discuss the mapping from the quantum output to the classical stochastic gradient needed for SGD. Specifically:
  - The Epoch-SGD-Proj analysis (Lemma 5) requires unbiased stochastic gradient estimates with bounded variance. The paper asserts \(\mathbb{E}[\hat{g}_t] = \nabla\Gamma_{\varepsilon,\lambda}(x_t)\) (line 287), but does not explain how a single-query quantum procedure yields an unbiased gradient estimate (as opposed to an approximation or a quantum state that must be measured multiple times to extract classical values).
  - The dimension \(d\) is not discussed in the gradient estimation context — Jordan's algorithm gives one derivative per query in its basic form, and the number of oracle queries needed for a \(d\)-dimensional gradient is not \(O(1)\) in the straightforward application. While more sophisticated superposition-based approaches can achieve \(O(1)\) total queries, the paper provides no analysis or reference to support this for the specific setting of Lipschitz functions.
  
  This does **not** invalidate the paper's contribution — the result is recoverable with standard techniques from quantum gradient estimation — but the analysis is incomplete as written. The authors should either (a) clarify the gradient estimation procedure and justify unbiasedness and the \(O(1)\)-query claim for the \(d\)-dimensional setting, or (b) adopt a quantum first-order oracle (as in Chakrabarti et al. 2020) and note the change in model.

### Minor

- **The quantum sampling subroutine (Algorithm 2) defers key details to a stripped appendix.** The main text sketches the procedure (find top-\(K\) entries, approximate the remaining entries with a common value \(h\), construct an approximate state, apply amplitude amplification) and states Lemma 4's complexity claim. However, the derivation of the approximation error, the required size of \(K\) as a function of \(\varepsilon'\) and \(N\), and the amplitude amplification success probability analysis are all deferred to the appendix. While this is standard practice for theory papers, the main text would benefit from at least stating the required size of \(K\) and a brief justification for why the approximation does not degrade the BROO accuracy.

- **The proof of Theorem 3 references an unmotivated lemma.** The proof (line 287, 294) relies on "Lemma gammamax" to bound \(e^{(f_i^\lambda(x) - f_i^\lambda(\bar{x}))/\varepsilon'}\nabla f_i(x)\) by \(G = O(L_f)\) and to relate suboptimality of \(\Gamma_{\varepsilon,\lambda}\) to \(\mathcal{F}_{\max}^\lambda\). This lemma is not stated or even hinted at in the main text; it appears to reside in the appendix. A brief statement of the bound and its intuition would improve readability.

- **Proposition 2 (state preparation) assumes a classical procedure for partial sums without discussing its cost.** The proposition requires "a classical procedure that computes \(\sum_{l=i}^j w_j\) for all \(i\le j\)." In the quantum setting, constructing such a classical procedure from oracle queries has a cost that is not accounted for. This is a standard assumption in the quantum state preparation literature and is likely resolved by techniques using quantum arithmetic on queried values, but a brief note on feasibility would be useful.

### Trivial
None.

## Nice-to-Haves

- The lower bound statement (Theorem 5) assumes both Lipschitz and smooth (\(L_g\)-smooth) functions. A brief comment on whether the hard instance from Carmon et al. (2021) is already smooth or how it is smoothed would be helpful (the smoothing details are in the stripped appendix).
- The gradient estimation discussion could note that the result of Proposition 4 can be made unbiased with negligible overhead using standard Hadamard-test-based approaches, clarifying compatibility with the SGD analysis.

## Removed Points

These points are flagged to be removed, treat them with caution.

- *Harsh critic's claim that gradient estimation is a "structural issue" invalidating core claims:* The paper follows standard conventions in quantum optimization (citing Jordan 2005). The claim is not that the gradient is "exact" in an absolute sense (the paper never uses that word), but that a single oracle query suffices for a gradient estimate — a well-established quantum computing result. The concern is downgraded to Major above because the paper is incomplete on the unbiasedness and dimension aspects, not because the approach is fundamentally flawed.
- *Missing appendix details (Lemma gammamax, proof of Lemma 4, lower bound construction):* The instructions note that the parser strips appendix sections from all papers. Criticizing missing appendix content is invalid.
- *Missing related works:* Cannot be confirmed without external sources.
- *Formatting/style nitpicks (typos, grammar, etc.):* Per instructions, these are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation about the paper that the authors themselves do not make. The harsh critic correctly identifies that the gradient estimation step needs clarification, which is a fair technical point, but not a novel reading of the paper's structure.

## Suggestions

1. **Clarify the gradient estimation step.** Either (a) explain how Proposition 4 yields an unbiased stochastic gradient suitable for Epoch-SGD-Proj, including the dependence on dimension \(d\) and a justification that the one-query claim extends to \(d\)-dimensional Lipschitz functions with an explicit reference to Jordan (2005) or subsequent work, or (b) adopt a quantum first-order oracle model and note the change. This is the single change that would most strengthen the paper.

2. **State the required size of \(K\) and the approximation error of the softmax sampling in the main text.** A short statement (even a sentence) of how \(K\) is chosen relative to \(\varepsilon'\) and \(N\) to make the approximation in Algorithm 2 valid would make the main text significantly more self-contained.

3. **Briefly state the bound from Lemma gammamax** in the main text so the proof of Theorem 3 is readable without the appendix.

4. **Mention the feasibility of the partial-sum classical procedure** required by Proposition 2, perhaps with a brief note that it can be implemented via quantum arithmetic on oracle outputs without additional oracle queries.
