Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper defines a class of random matrix distributions called "pseudoiid" (row/column-exchangeable, with moment and cross-correlation conditions mimicking i.i.d. behavior) and proves that deep fully connected and convolutional networks initialized with pseudoiid weights converge to Gaussian Processes in the infinite-width simultaneous limit. The result unifies and extends prior i.i.d.-only proofs (Matthews et al., 2018) and the orthogonal case (huang_2021), while also claiming applicability to computationally efficient architectures such as low-rank and structured sparse networks. The paper provides empirical validation at finite widths and discusses implications for Bayesian inference and Edge-of-Chaos analysis.

## Strengths

- **Unified generalization of the GP limit beyond i.i.d. weights.** The pseudoiid definition (Definition 3.2) cleanly abstracts the minimal conditions needed for the CLT argument to go through without requiring entrywise independence, and the main theorems (Theorems 3.3 and 4.2) provably extend the known i.i.d. GP limit to this broader class. This is a genuine theoretical advance.

- **Explicit handling of the first-layer restriction.** The paper clearly identifies why the first layer cannot be pseudoiid (only one dimension scales with n) and provides a precise resolution — i.i.d. Gaussian first-layer weights, with a footnote noting this can be further relaxed to row-i.i.d. This fills a gap left by prior work (huang_2021) that was "elusive on the treatment of the first layer."

- **Novel approach to orthogonal CNN filters.** The matricization strategy (reshaping the kernel into a tall matrix and enforcing column orthogonality scaled by 1/k², Eq. 6) is a sensible construction distinct from prior definitions, and the paper is transparent about its limitations (not claiming uniformity over all orthogonal kernels).

- **Empirical validation at finite width.** Figures 1–2 show clear convergence of preactivation histograms toward the predicted Gaussian and of joint distributions toward the bivariate Gaussian for multiple pseudoiid variants at widths as low as n=30, with convergence improving at n=300.

## Weaknesses

### Fatal

None.

### Major

- **Condition (iii) — the 8th-moment bound — is not verified for any concrete example.** For the low-rank case, the paper states that conditions (iii) and (iv) are "controlled by the choice of distribution 𝒟" without specifying 𝒟, computing any moment, or showing that such a 𝒟 exists while keeping the product CP in the pseudoiid class. For structured sparse weights, the paper merely says "for suitable choices of underlying distribution 𝒟, it satisfies the moment conditions." For orthogonal CNN filters, the phrase "the moment conditions are both straightforward to check" is followed only by a check of condition (iv), with condition (iii) unaddressed. Since the paper's practical reach (low-rank, structured sparse) depends on whether these distributions actually satisfy the pseudoiid conditions, the lack of concrete verification — even for a single canonical choice of 𝒟 — weakens the claim that these architectures fall under the GP limit. This is not fatal to the paper's theoretical contribution (the definition and theorem stand on their own), but it substantially reduces the evidential support for the claimed practical scope.

- **Unjustified application of Lemma 3 from huang_2021 to non-square matrices.** The paper invokes Lemma 3 of huang_2021 to compute the four-cross expectation in both the low-rank case (where C is an m×r Stiefel matrix, r < m) and the orthogonal CNN case (where Ũ is a c_out × k²c_in tall matrix). The lemma as stated applies to square Haar-distributed orthogonal matrices. The paper does not justify why it carries over to rectangular matrices with orthonormal columns (Stiefel manifold), nor does it discuss how the variance scaling (the 1/k² factor in Eq. 6) is incorporated. While the result likely extends, the argument as presented is technically incomplete.

### Minor

- **No quantitative convergence metric in the simulations.** The paper relies entirely on visual inspection of histograms and scatter plots. Reporting a simple metric (e.g., Wasserstein distance, Kolmogorov-Smirnov statistic, or the commented-out Wasserstein figure in the paper's own source) would strengthen the claim of GP convergence, especially for the structured sparse and low-rank cases where convergence is visually less rapid than for orthogonal weights at n=30.

- **The orthogonal CNN construction's random generation is underspecified.** The paper says kernels can be "drawn uniformly random with orthogonal columns" satisfying ŨᵗŨ = (1/k²)I, but does not specify how to uniformly sample from this set of matrices (e.g., the procedure on the Stiefel manifold). The caveat that the resulting U is not uniform over all orthogonal CNN kernels is transparent, but the practical reader is left without a concrete sampling algorithm.

### Trivial

None.

## Nice-to-Haves

- The paper could explicitly verify condition (iii) for at least one concrete choice of 𝒟 (e.g., Gaussian entries for P in the low-rank construction), perhaps as a short lemma.
- The EoC discussion in Section 4.2 could cite a self-contained computation for one pseudoiid example (rather than referencing Nait_2023) to make this implication more independently accessible.
- Adding quantitative deviation measures (Wasserstein distance, KS statistic) would make the empirical validation more precise.

## Removed Points

These points were raised by reviewers but are removed or downgraded per the review guidelines:

- **"The proof is not assessable from the main text"** — The full proof sketch and details are in the appendix (the commented-out subsection in the source), which was stripped by the parser. The main text references the Matthews et al. (2018) proof strategy, the Blum et al. (1956) exchangeable CLT, and the inductive argument. This is a standard organization for theoretical papers.
- **"Condition (iii) is insufficiently motivated"** — The paper does motivate condition (iii) in the paragraph following Definition 1 (line 65), explaining it ensures moments of dependent weights behave like independent ones, which the CLT argument requires. The paper also acknowledges the open question of whether conditions are redundant. The reviewer's concern about the condition being "strong" is noted, but this is a design choice the paper is transparent about.
- **"First-layer restriction is a practical limitation"** — The paper clearly states and justifies this restriction; it is not a hidden flaw.
- **"EoC contribution is indirect, citing unpublished work"** — The EoC is an implication of the GP limit, not the paper's core contribution. Citing Nait_2023 for the EoC calculation is appropriate; the reviewer's framing as a weakness would effectively require the paper to also compute the EoC itself, which is scope creep.
- **"The orthogonal CNN construction is confusing / Stiefel manifold not elaborated"** — The paper explicitly disclaims uniformity ("we do not claim the generated orthogonal convolutional kernel U is 'uniformly distributed'"), making this a design choice rather than an omission.
- **Formatting/style nitpicks, grammar/typo complaints** — These are parser artifacts, not author errors.

## Novel Insights

The most interesting observation that surfaces from these reviews is the tension between the paper's two contributions: (a) the abstract pseudoiid conditions that are necessary for the proof, and (b) the concrete examples that are claimed to satisfy them. The paper's theory is strongest as a unifying framework — giving a single set of sufficient conditions that subsumes i.i.d. and orthogonal cases under one roof. The examples are presented as beneficiaries of this unification, but the verification gap for condition (iii) means the paper is better described as *proposing a class that includes low-rank/structured sparse as hypothetical members* rather than *proving that these specific constructions belong to the class*. This distinction matters for the paper's marketing of itself. The core theoretical contribution (the pseudoiid definition and its proof of GP convergence) is solid; the applied reach is partially promissory.

## Suggestions

1. **Verify condition (iii) for at least one concrete example.** Even a short lemma in the main text or a clear reference to the appendix showing that Gaussian P entries with Haar-Stiefel C satisfy the 8th-moment bound would significantly strengthen the paper's practical claims.
2. **Justify the extension of Lemma 3 of huang_2021 to Stiefel matrices**, either by explicit derivation or by showing how a Stiefel matrix can be embedded in a square orthogonal matrix.
3. **Include a quantitative convergence metric** (e.g., Wasserstein distance across widths) in the simulations to replace or supplement visual inspection.
4. **Specify the sampling procedure** for the orthogonal CNN construction (e.g., draw a matrix with i.i.d. Gaussian entries, perform QR decomposition, rescale to satisfy ŨᵗŨ = (1/k²)I).

## Score and Decision

The paper makes a genuine theoretical contribution — the unified pseudoiid framework is a clean abstraction that extends the GP limit in a non-trivial way. The theorems appear sound (subject to the appendix containing the complete proof), and the paper is generally well-written and clearly motivated. 

However, the verification of the headline examples (low-rank, structured sparse) is incomplete in a way that undermines the claimed practical scope. The 8th-moment condition (iii) is not concretely verified for any example, and the application of Lemma 3 from huang_2021 to non-square matrices is unsubstantiated. These are fixable issues, but they reduce the paper's contribution from "we proved new architectures are GPs" to "we defined a class that would include new architectures if certain moment conditions are met, which we have not verified." A revision that fills these gaps would be significantly stronger.

The paper is a borderline accept: the theoretical definition and theorem are valuable, but the gap in example verification prevents the paper from fully delivering on its stated practical promises.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>