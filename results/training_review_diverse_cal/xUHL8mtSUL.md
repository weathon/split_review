Now I have a thorough picture of the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes a scalable Gaussian process regression method that leverages the closed-form Mercer decomposition of the compact Matérn kernel (product sines on \([0,1]^r\)) to obtain a low-rank kernel approximation via the Hilbert–Schmidt singular value decomposition (HS-SVD). The key advantage is that the eigenfunctions and eigenvalues are known analytically, so the low-rank representation is obtained without expensive numerical decomposition, yielding \(O(n m^2)\) time and \(O(n m)\) space complexity. The method is compared against nine state-of-the-art scalable GP approaches on simulated large-scale data.

## Strengths

- **Simultaneous reduction of time and space complexity with no expensive low-rank computation.** The method achieves \(O(n m^2)\) time and \(O(n m)\) space by exploiting a kernel whose Mercer decomposition is known in closed form (§3.2–§3.3, Algorithm 3.4). The eigenfunctions \(\phi_l(x)=\sqrt{2}\sin(l\pi x)\) and eigenvalues \(\lambda_l=(\alpha^2+l^2\pi^2)^{-\beta}\) are independent of the data, so constructing \(\Phi_m\) requires no numerical decomposition or optimization. This is a genuinely clean and elegant approach to obtaining a low-rank representation.

- **The compact Matérn kernel is connected to the standard Matérn kernel via a differential operator.** Proposition 3.5 shows that the compact Matérn (on a bounded domain with zero boundary) and the standard Matérn (on \(\mathbb{R}^r\)) are both Green's functions of the modified Helmholtz operator \((-\Delta + \alpha^2 I)^\beta\) — the difference is only the domain and boundary conditions. This places the compact Matérn on theoretically solid ground and enables fair comparisons (e.g., \(\beta=3\) compact Matérn vs. \(\nu=3/2\) standard Matérn have the same smoothness).

- **Smoothness control is proven.** Theorem 3.3 establishes that the compact Matérn kernel is \(\beta-r-1\) times differentiable, matching the flexibility of the standard Matérn kernel's smoothness parameter.

- **Parameter estimation benefits from precomputation.** Because the eigenfunctions \(\phi_l\) do not depend on the kernel parameters, \(\Phi_m\) and \(\Phi_m^\top\Phi_m\) are computed once and reused during MLE optimization (§3.3, §3.4). This provides significant savings in repeated likelihood evaluations.

- **Numerical stability is enhanced by truncation.** Discarding near-zero eigenvalues removes ill-conditioning in the kernel matrix inverse and log-determinant computation (§3.3), a known practical bottleneck in dense GP regression.

## Weaknesses

### Fatal

None.

### Major

- **The claim that the domain can be "any closed interval or bounded region without loss of generality" (Section 3.1, line 160) is overbroad.** The sine eigenfunctions are eigenfunctions of the Helmholtz operator specifically on rectangular domains with Dirichlet boundary conditions. For irregular (non-rectangular) bounded domains, the Mercer expansion changes fundamentally and closed-form eigenfunctions are generally unavailable. The paper does not discuss this limitation or assess the distortion introduced by projecting non-rectangular data onto \([0,1]^r\). While the method works on hyperrectangles (which covers many practical cases after bounding-box scaling), the phrasing overstates the generality and should be corrected.

### Minor

- **The comparison with state-of-the-art methods is confounded by differing implementations and hardware.** HS-SVD is implemented in R on a single CPU core, NNGP uses 16 CPU threads, and the remaining methods use GPyTorch on GPU(s) (Section 4). While the paper is transparent about this setup, the runtime comparison is not a controlled algorithmic benchmark — differences could arise from implementation language, framework optimization quality, or hardware rather than the core method. This does not invalidate the results but weakens the claim that HS-SVD is "more efficient" as an algorithmic statement.

- **The paper mentions uncertainty quantification as a hallmark of GP (abstract, introduction) but does not evaluate it.** The only reported metrics are MSE, runtime, and memory. No prediction intervals, coverage probabilities, or log-likelihood values on test points are shown. Section 3.4 notes that posterior samples are "easily extended" because the inverse is efficiently computed, but no demonstration is provided. For a GP method claiming UQ as an advantage, this is a meaningful gap.

- **The "no preprocessing" claim is slightly overstated.** Computing \(\Phi\) (size \(n \times m\)) and the quantities \(\Phi^\top Y\) and \(\Phi^\top\Phi\) requires \(O(nm)\) and \(O(nm^2)\) work respectively. While this is far cheaper than the alternatives (e.g., Nyström or inducing-point optimization), calling it "for free" or "no preprocessing" (abstract, line 27) is imprecise — it is a one-time cost that is part of the method.

- **Only 1D and 2D simulations are demonstrated.** The paper acknowledges the curse of dimensionality in Section 5 (exponential growth of \(m\) with dimension \(r\)), and indeed all simulations are 1D or 2D (Section 4). While this does not undermine the paper's core contribution (which focuses on \(n\)-scalability), it means the practical applicability to higher-dimensional problems is severely limited.

### Trivial

- **Notation confusion in the pseudocode (Section 3.4, line 222).** The algorithm defines \(G \leftarrow (\hat{\sigma}^2\hat{\Lambda}^{-1} + \Phi^\top\Phi)^{-1}\) but then writes \(H \leftarrow \frac{1}{\sigma}(Y - \Phi C \Phi^\top Y)\) where \(C\) is undefined (presumably \(G\) was intended).

- **The paper assumes zero mean (§3.2) and states "the prior mean can be handled separately" without any discussion.** In large-scale spatial statistics, the mean is often modeled as a linear combination of covariates, which would require additional computations.

## Nice-to-Haves

- Evaluate prediction interval coverage and width on simulated data to substantiate the UQ claim.
- Apply the method to at least one real-world dataset on a (near-)rectangular domain (e.g., a 2D spatial environmental dataset) to demonstrate practical relevance.
- Provide guidance on how to choose \(m\) in practice (e.g., based on eigenvalue decay rate and a target truncation error tolerance).
- Consider running GPyTorch baselines on CPU as well to construct a more controlled runtime comparison, at least for a subset of experiments.
- Discuss how non-rectangular bounded domains could be handled (e.g., via an approximate Mercer decomposition, as mentioned in Section 5).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic Point 1 ("experimental results not presented"):** The paper contains Figure 1 (image placeholder at line 24) and references tables reporting MSE/runtime/memory (Section 4, line 235). These are embedded as images in the original PDF and stripped by text-only extraction. Per the meta-review instructions, this is a parser artifact, not an author error.

- **Harsh critic Point about missing appendix / proof of Theorem 3.3:** The paper states "details for the proof of Theorem 3.3 are located in [appendix]" (line 248). The appendix is stripped by the parser. Per instructions, this is a parser artifact.

- **Harsh critic Point about "no analysis of computational cost of computing \(\Phi\) and \(\Phi^\top\Phi\)":** The paper's Algorithm 3.4 explicitly lists these steps and the text in §3.2–§3.3 derives the complexity reductions. The cost is implicit in the design.

- **Strength Finder's claim about Figure 1 "showing HS-SVD on a single CPU runs faster than GPU-accelerated SKI and LOVE":** While the figure exists in the PDF, the strength claim itself is kept in the Strengths section above; the specific figure reference is treated as supported by the paper's own claims.

- **Harsh critic Point about the method "not scalable" due to curse of dimensionality:** The paper explicitly acknowledges this limitation (Section 5). The paper's contribution is scaling in \(n\) (sample size), not \(r\) (dimension). The title's "Scalable" refers primarily to sample-size scalability, which is achieved. The dimensionality limitation is real but already discussed by the authors.

## Novel Insights

None beyond the paper's own contributions. The connection between the compact Matérn and standard Matérn kernels via the modified Helmholtz operator (Proposition 3.5) is the most insightful theoretical contribution and is well-explained in the paper itself.

## Suggestions

1. **Correct the overbroad domain claim.** Replace "any closed interval or bounded region without loss of generality" with language that acknowledges the restriction to hyperrectangular domains (or domains that can be bijectively mapped to one). Note that a bounding-box embedding is possible but may distort distances.
2. **Add a UQ evaluation.** Even a simple figure showing prediction intervals with coverage on one simulation would meaningfully support the UQ claim in the abstract.
3. **Clarify the "no preprocessing" language.** Replace "no preprocessing" with something like "no expensive numerical decomposition — the eigenfunctions are known analytically, so the low-rank basis is obtained by direct evaluation."
4. **Fix the pseudocode notation.** Replace the undefined \(C\) with \(G\) in the algorithm step.
5. **Briefly address the non-zero mean case.** A few sentences or a citation on how covariates or a non-zero mean function could be incorporated would strengthen the practical contribution.

## Score and Decision

**Originality:** The core idea — exploiting the closed-form Mercer decomposition of the compact Matérn kernel for scalable GP — is genuinely novel and elegantly sidesteps expensive low-rank approximation.  

**Importance of research question:** Scalable GP regression is a well-established and active area; any method that simultaneously reduces time and space complexity while maintaining interpretability is of clear value.  

**Claims support:** The theoretical complexity claims are well-supported by the mathematical derivations. The empirical claims rely on figures/tables present in the PDF. The "any bounded region" claim is overstated and should be corrected.  

**Soundness of experiments:** The simulation design (10 replicates, 9 baselines, varying sample sizes up to 2M) is sound. The uncontrolled hardware/implementation comparison is a limitation but is transparently disclosed.  

**Clarity of writing:** Clear and well-structured. The theoretical development is logically organized. The pseudocode could be slightly cleaner.  

**Value to community:** The method is practical, easy to implement (closed-form basis, no GPU requirement), and has clear complexity advantages. It could become a useful baseline for large-scale GP applications on low-dimensional data.

**Overall:** This is a solid paper with a clean theoretical contribution, honest discussion of limitations, and a practical method. The weaknesses are addressable and do not undermine the core contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>