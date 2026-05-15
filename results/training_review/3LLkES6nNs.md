Now I have a thorough understanding of the paper content and all the claims. Let me produce the final consolidated review.

## Summary

This paper establishes the Neural Network Gaussian Process (NNGP) correspondence for Neural ODEs by viewing them as infinitely deep ResNets with shared weights. Using random matrix theory, the authors argue that the depth and width limits commute (Lemma 4.1), enabling them to show that wide Neural ODEs converge to Gaussian processes. The paper derives distinct limiting kernels for shared-weights vs. independent-weights cases (a novel finding), proves strict positive definiteness of the limiting kernel, and provides a dynamic programming algorithm for computing the covariance matrix efficiently.

## Strengths

- **Novel distinction between shared- and independent-weights NNGP kernels.** Theorem 4.2 and Remark 4.3 show that skip connections cause weight sharing to affect the NNGP kernel structure — a departure from feed-forward, convolutional, and recurrent networks where sharing does not alter the kernel. This is a genuine theoretical insight that correctly identifies why standard techniques (SDE-based, Hayou & Yang 2023) cannot be directly applied to Neural ODEs.

- **Identification of the fundamental challenge.** The paper clearly articulates (Sec. 4.3) why the double limit (depth and width) does not trivially commute, citing known results about log-Gaussian behavior (Li et al., 2021) and diffusion limits (Peluchetti & Favaro, 2020). It correctly identifies that prior SDE-based approaches (Hayou & Yang, 2023) require independent weights per layer and thus cannot handle the shared-weights case.

- **Strict positive definiteness analysis for finite depth (Theorem 4.4).** This result is cleanly stated and provides a foundation for understanding the infinite-depth case. The experimental validation (Figure 3, smallest eigenvalues remaining positive as width/depth increase) offers supporting evidence.

- **Dynamic programming algorithm.** The paper identifies a genuine computational challenge: under shared weights, the NNGP covariance computation requires tracking correlations across all layers (not just forward propagating through one layer at a time). Algorithm 1 addresses this need, which prior NNGP software (e.g., Neural Tangents) does not support for the shared-weights case.

## Weaknesses

### Fatal

None. The core claims — that wide Neural ODEs converge to GPs and that the limiting kernel is strictly positive definite — are well-motivated and likely correct, even though the presentation of some proofs is incomplete in the main text. There is no error that invalidates the paper's central thesis.

### Major

- **The strict positive definiteness argument for the shared-weights limiting kernel (Theorem 4.8) has a logical gap in the main text.** The paper invokes Jacot et al. (2018, Theorem 3) and Hermitian expansions of the dual activation — these tools apply to *dot-product kernels* on the sphere (kernels that depend only on ⟨x, x'⟩). Lemma 4.2 only establishes that the diagonal entries Σ*(x,x) are constant across the sphere; it does **not** prove that Σ*(x,x') is a function of ⟨x, x'⟩ alone. For the independent-weights case, this follows from standard NNGP reasoning (the kernel recursively preserves dot-product structure), but for the shared-weights case the covariance involves double integrals of covariances of z-processes (Proposition 4.6(ii)), and the paper provides no argument that isotropy is preserved under this more complex dynamics. The claim in the main text — "by leveraging these properties, we can derive its Hermitian expansion" (line 224) — is insufficient. If the appendix contains the missing argument, it should be cited more explicitly in the main text. If not, this is a genuine gap. **This does not undermine the paper's core contributions** (the NNGP correspondence itself does not depend on strict positive definiteness), but it weakens a claimed result that the paper highlights as important for convergence guarantees.

- **The commuting-limits argument (Lemma 4.1) is only sketched in the main text.** Given the well-known subtlety in this area — where different depth/width scaling ratios produce different limit distributions (Gaussian, log-Gaussian, or diffusion) — and the fact that prior work (Hayou & Yang, 2023) required a specific 1/√L scaling and *independent weights* to obtain commuting limits, the paper's claim that 1/L scaling with *shared weights* yields commuting limits via RMT is a strong one. The main text says only that the proof uses "Lemma A.3 or A.2" and that "convergence of depth is uniform in width" — without even a sketch of why 1/L scaling suffices where 1/√L was previously required. The connection between the empirical Gram matrix Σ̂_n^L and the NNGP kernel Σ^ℓ is not explicitly justified, and the existence of the limit lim_{ℓ→∞} Σ^ℓ (on which Theorem 4.5 depends) is asserted without analysis of the fixed-point structure of the covariance recursion. These issues are likely resolved in the appendix, but they represent significant weight on deferred material for the paper's central claim.

### Minor

- **Experiments are purely qualitative.** The experimental section reports no error bars, no multiple seeds, no quantitative error metrics (e.g., relative Frobenius error between empirical and theoretical covariances). The NNGP training comparison shows a single test accuracy curve without comparing against finite-width Neural ODE training at multiple widths to verify convergence. For a theory paper, experiments are primarily illustrative, but the paper's own claim to "support our theoretical findings" (abstract) would be strengthened by even basic quantitative validation.

- **The relationship between Σ̂_n^L (Lemma 4.1) and Σ^ℓ (Theorem 4.2) is not clearly explained.** Lemma 4.1 defines Σ̂_n^L as an empirical Gram matrix of hidden features, while Theorem 4.2 defines Σ^{ℓ+1} as a theoretical NNGP kernel for the output. The paper asserts they are connected (both converge to Σ*) without explicitly writing the limiting relationship. A reader is left to infer that lim_{n→∞} Σ̂_n^L = (1/σ_w²) × Σ^{L+1} (up to the σ_v² output scaling). Making this explicit would improve clarity.

- **Theorem 4.2 has a notational imprecision.** It states that the output functions f^L_θ,k have covariance Σ^{L+1}, but Σ^{ℓ+1} is defined as σ_w² E[φ(u^ℓ) φ(u^ℓ)] without the σ_v² factor from the output layer V. Line 245 suggests the actual output covariance includes σ_v². This inconsistency should be resolved.

- **The DP algorithm (Section 4.5) claims efficiency without complexity analysis.** The algorithm description is also partially garbled by parser artifacts, but the underlying recurrence appears to require O(L²N²) storage and O(L³N²) computation. The paper should state the complexity explicitly and ideally provide a runtime comparison to Monte Carlo estimation for a representative problem size.

### Trivial

None.

## Nice-to-Haves

- Provide a brief sketch in the main text of why the RMT-based argument gives commuting limits with 1/L scaling and shared weights, even informally. This would help readers assess the plausibility of the deferred proof.
- State explicitly that the NNGP kernel for the shared-weights case is a dot-product kernel on the sphere (or provide a brief inductive argument), to close the gap in the strict positive definiteness proof.
- Include error bars in Figures 1–3 and report a quantitative convergence metric (e.g., ||Σ̂_n^L − Σ*||_F / ||Σ*||_F) for a few (width, depth) pairs.

## Removed Points

These points are flagged to be removed — treat them with caution as they stem from reviewer misreading or the review instructions.

1. **"Lemma 4.1 is stated without proof — references Lemmas A.2/A.3 in the appendix but text gives no indication of a rigorous argument"** → The appendix exists in the original submission; the parser strips appendices from all papers. The criticism that proofs are missing from the main text is a reviewer-knowledge gap, not an author error. Per the hard rules, this is removed. *(However, the substantive concern about the commuting limits being a non-trivial claim is preserved above as a major weakness.)*

2. **"Proposition 4.6(i) is not justified and contradicts the recursive structure... the paper does not discuss this degeneracy"** → The paper *does* discuss this degeneracy in Remark 4.7, which states that independent-weights ResNets with 1/L scaling "behave akin to a shallow or two-layer network." The reviewer missed this remark. The criticism is factually wrong about omission.

3. **"The DP algorithm description is unreadable — garbled pseudocode"** → Parser artifact. The original submission does not have this issue.

4. **"Missing appendix, missing proofs in appendix"** → Multiple variations of this complaint. The parser strips appendices; they exist in the original submission.

5. **"Pure formatting/style nitpicks"** about notation, capitalization, etc. → These are parser artifacts or style preferences that do not affect correctness.

6. **Multiple requested experiments (commuting limits verification, scalability analysis, failure modes)** → These are suggestions for future work that go beyond what is expected in a theory paper, especially one whose main contributions are theoretical.

7. **"No standard deviations, no multiple seeds"** → This is standard for a theory paper's illustrative experiments. Mentioned as a minor weakness above rather than a major flaw, consistent with softening for illustrative experiments.

## Novel Insights

The most striking observation in the reviewer commentary is that the harsh critic's own analysis of Proposition 4.6(i) actually *confirms* the paper's claim (the reviewer derives the same result and concludes "This argument is plausible") while simultaneously calling the result unjustified — effectively proving the paper is correct to a first approximation. More substantively, the insight that skip connections *change* whether weight sharing affects the NNGP kernel (Remark 4.3) is a genuinely novel observation that distinguishes Neural ODEs from MLPs and RNNs. Prior NNGP theory assumed weight sharing was irrelevant to the kernel; this paper shows it matters when skip connections are present, which is a meaningful conceptual advance.

## Suggestions

1. **Close the isotropy gap for Theorem 4.8 in the main text.** Add a brief inductive argument: since Σ^0(x,x') = σ_u²⟨x,x'⟩/n_in depends only on the inner product, and each Σ^{ℓ+1} is an expectation over Gaussian variables whose covariance is a function of the inner product, all Σ^ℓ and hence Σ* are dot-product kernels on the sphere. This is a standard observation in NNGP theory and needs only a sentence or two.

2. **Explicitly connect Lemma 4.1 to Theorem 4.5.** Write the relationship: lim_{n→∞} Σ̂_n^L = (1/σ_w²) × (limiting hidden-feature covariance), and show how this yields Σ* = lim_{L→∞} Σ^{L+1} (with the appropriate σ_v² scaling).

3. **Add a brief note about the existence of lim_{ℓ→∞} Σ^ℓ.** Even a sentence noting that the covariance sequence is monotone or bounded under the given assumptions would help.

4. **Report at least one quantitative convergence metric in the experiments** (e.g., Frobenius norm error between predicted and empirical covariances for a few (width, depth) combinations).

## Score and Decision

The paper makes genuine theoretical contributions: it identifies the correct framework for studying Neural ODE NNGP correspondence, pinpoints why prior SDE-based methods fail, derives distinct kernels for shared vs. independent weights, and provides a computational method. The two major weaknesses — the incomplete justification for isotropy in the strict positive definiteness proof and the reliance on deferred appendix material for the commuting limits argument — are significant but not fatal. Both are fixable: the isotropy point needs only a few lines of clarification in the main text, and the commuting-limits proof presumably exists in the appendix. The experiments are weak but acceptable for a theoretical paper. Overall, this is a solid contribution that advances our understanding of Neural ODEs at initialization, and the main results are likely correct.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>