Now I have a thorough understanding of the paper and can cross-check each reviewer claim against the actual paper content. Let me write the consolidated review.

## Summary

This paper establishes the Neural Network Gaussian Process (NNGP) correspondence for wide Neural ODEs at initialization, proving that as width → ∞, Neural ODEs converge to centered Gaussian processes with deterministic kernels. The key technical challenge is handling the coupled depth and width limits — Neural ODEs correspond to infinite-depth ResNets with shared weights, preventing direct application of existing SDE-based approaches. The paper overcomes this using random matrix theory (Lemma 4.1) to show the two limits commute. It further proves the limiting kernel is strictly positive definite for non-polynomial Lipschitz activations (Theorem 4.8), and provides a dynamic programming algorithm for computing the covariance matrix.

## Strengths

1. **Novel NNGP correspondence for shared-weights Neural ODEs**: Extending NNGP results to the infinite-depth, shared-parameter regime is non-trivial because existing techniques (SDE limits, Tensor Programs with independent weights) do not apply. The paper correctly identifies and tackles this gap, establishing that wide Neural ODEs converge to GPs with kernels that depend qualitatively on whether weights are shared (Theorem 4.5, Proposition 4.6). In the independent-weights case the limiting kernel collapses to that of a two-layer network; in the shared-weights case it involves an integral over the entire trajectory — a genuinely distinct architectural signature (Remark 4.3).

2. **Strict positive definiteness for the infinite-depth limit**: Theorem 4.8 proves the limiting kernel Σ* is strictly positive definite on the sphere for non-polynomial Lipschitz activations. This property is essential for global convergence guarantees and benign overfitting, and extending it from finite depth (Theorem 4.4) to the infinite-depth limit is non-trivial since strict positivity can be lost in the limit.

3. **Rigorous discretization error bound**: Proposition 4.1 quantifies how well the finite-depth ResNet approximates the Neural ODE, providing an explicit bound \(\|h^L(x)-h(x,T)\| \leq \frac{A}{B}(e^{BT}-1)\beta\) that vanishes as \(L\to\infty\).

4. **Efficient DP algorithm for covariance computation**: Algorithm 1 provides a method for computing the NNGP kernel matrix under shared weights, which is needed because the covariance recursion couples all previous layers (unlike standard feedforward NNGP).

## Weaknesses

### Fatal
None.

### Major
None that can be verified from the main text alone. The reviewer's most severe criticisms either (a) refer to logical steps that are deferred to the appendix (which is standard for conference papers) or (b) are factually incorrect upon closer inspection (see Removed Points).

### Minor

1. **The logical chain from Lemma 4.1 to Theorem 4.5 is sketchy in the main text.** Lemma 4.1 establishes that the two iterated limits of the *empirical covariance* \(\hat\Sigma_n^L\) exist and are equal. Theorem 4.2 establishes that for finite depth \(L\), the ResNet converges to a GP with kernel \(\Sigma^L\) as width → ∞. Theorem 4.5 then claims the Neural ODE (the \(L\to\infty\) limit) converges to a GP with kernel \(\Sigma^* = \lim_{L\to\infty}\Sigma^L\). The paper states "Building on this foundation, we establish the NNGP correspondence for Neural ODEs" but does not explain in the main text how the commuting of *empirical covariances* (Lemma 4.1) combines with the finite-depth GP convergence (Theorem 4.2) to yield the infinite-depth GP convergence. A short sketch of this step would make the main-text argument self-contained and more convincing. (The full proof is presumably in the appendix, referenced as Lemma A.3/A.2 and Theorem D.1.)

2. **The DP algorithm is incompletely described in the main text.** The quantity \(V_\phi\) in Algorithm 1 is used but never defined in the main body. The algorithm's update rule is given both in pseudocode and equation (17), but the reader cannot tell whether \(V_\phi\) is evaluated via closed-form formulas for specific activations or via Monte Carlo integration. A brief definition or reference to where it is specified would suffice.

3. **The experimental section is too brief for reproducibility.** Figure 3 reports "Test Accuracy using NNGP of Neural ODE" on MNIST, but the widths, depths, and training hyperparameters are not stated. While the paper is primarily theoretical, the experiments included should be reproducible from the information given.

### Trivial

- The constant \(C_1, C_2\) in Proposition 4.1 are stated as "\(C_i > 0\) are constants" without further characterization. This is standard for generic existence bounds but a note that they depend only on the Lipschitz constant of \(\phi\) would be clearer.
- Section 4.3's header is labeled "NEURAL ODE \(f_{\theta}\) AS GAUSSIAN PROCESS" (singular) but the paper covers two distinct processes (shared vs. independent weights).

## Nice-to-Haves

- A brief explanation (even 2–3 lines) of why RMT yields uniformity of depth convergence in width — sketching the lemma referenced from the appendix — would substantially strengthen the main text's credibility.
- A complexity analysis (FLOPs or memory) for Algorithm 1 would better support the claim that it is "efficient."
- Clarifying that Lipschitz activations are controllable (which the paper notes is "easy to show" per Yang (2019)) could be stated explicitly for completeness.

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

- **"The limiting kernel Σ* for the shared-weights case is not proved to exist"**: This criticism is factually incorrect. Lemma 4.1 explicitly proves that the double limit of the empirical covariances exists and defines Σ* as that common limit. Theorem 4.5 then defines Σ* via Σ*(x,x') = lim_{ℓ→∞} Σ^ℓ(x,x'), and since Σ^ℓ(x,x') = lim_{n→∞} Σ̂_n^ℓ(x,x') (Theorem 4.2), the existence follows from Lemma 4.1.
- **"Lemma 4.2 (isotropy) is not established in the main text"**: This is a criticism about a missing proof that belongs in the appendix. The main text states the lemma; the proof is deferred as is standard. Per the meta-review instructions, criticisms about missing appendix proofs are removed.
- **"The commuting-limits justification is insufficient — the paper does not explain how RMT yields uniformity"**: This is about the appendix's Lemma A.3/A.2 not being reproduced in the main text. The paper provides a sketch ("convergence of depth ℓ is uniform in widths n") and cites the appendix for the RMT details. Per meta-review instructions, this is removed as a missing-appendix-content criticism.
- **"Presentation quality issues (OCR artifacts, 'Proposition 4.', 'Se t')"**: These are parser/formatting artifacts, not author errors.
- **"The paper does not explain why previous SDE approaches cannot be adapted"**: The paper explicitly states on p.10 that Hayou & Yang (2023) "can't be directly applied... because their analysis relies on SDEs, which require independent weights at each layer." This is a clear explanation.
- **"No discussion of the activation function's controllability condition"**: The paper states on p.5 that "it is easy to show a Lipschitz continuous activation φ is controllable."
- **Missing related works**: Removed per meta-review instructions.

## Novel Insights

None beyond the paper's own contributions. The reviewer's observation that the transition from empirical covariance convergence to full GP convergence requires additional justification is correct as a matter of mathematical hygiene, but the paper's main text openly acknowledges it is building on the appendix for the complete argument.

## Suggestions

1. Add a 2–3 sentence sketch in Section 4.3 explaining how Lemma 4.1 (commuting empirical covariances) combines with Theorem 4.2 (finite-depth GP convergence) to yield Theorem 4.5 (infinite-depth GP convergence). For example: "Since for each finite L, the output converges to a GP with kernel Σ^L (Theorem 4.2), and Lemma 4.1 guarantees Σ^L → Σ* uniformly in the sense that the double limit of the empirical covariances exists, standard tightness arguments (detailed in Appendix [ref]) imply the corresponding GPs converge in distribution to a GP with kernel Σ*."
2. Define \(V_\phi\) explicitly in Section 4.5 or state where it is defined (e.g., "where \(V_\phi(\cdot,\cdot,\cdot)\) is defined in Appendix [ref] as the expectation operator for the kernel update").
3. Provide experimental hyperparameters (width, depth, optimizer, learning rate, number of Monte Carlo samples for the kernel computation) in a brief table or footnote.

## Score and Decision

This paper addresses a timely and genuinely open question — extending NNGP results to Neural ODEs with shared weights — using a plausible technical approach (RMT-based commuting limits argument). The contribution is novel and the claims, if correct, would be valuable to the community. The main weakness is that the main text's theoretical argument is sketchy in places, requiring heavy reliance on the appendix to verify the core logic. However, this level of main-text brevity is within the norm for theory papers at top conferences, and the remaining weaknesses (incomplete DP algorithm description, sparse experimental details) are addressable. On balance, the paper's novelty and the importance of the research question outweigh its presentational shortcomings.

**Originality**: Good — the shared-weights infinite-depth regime has not been covered by prior NNGP work.  
**Quality**: Adequate but depends on the appendix being complete.  
**Clarity**: Below average — several leaps in the logic are underspecified in the main text.  
**Significance**: Potentially high, if the proofs hold.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>