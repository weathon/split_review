Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies Bayesian neural networks in the linear-width (P ∝ N ∝ N₀) and sublinear-width (P ∝ N·N₀) regimes, aiming to bridge kernel-theoretic and statistical-mechanics perspectives. The main contributions are: (i) Theorem 3.3, claiming that the empirical kernel matrix converges in distribution to a matrix ΦΛΦ^T with independently sampled eigenvalues and eigenfunctions; (ii) Theorem 3.4, integral formulas for BNN predictor statistics under the spectral universality assumption (SUA); (iii) Theorem 3.5, a necessary and sufficient condition for extending renormalization theory to nonlinear BNNs; and (iv) a practical estimation method for the sublinear-width regime. The experiments provide illustrative validation on synthetic data and MNIST.

## Strengths

- **Conceptual bridge between Mercer eigenvalues and random matrix spectra (Theorem 3.3).** The paper makes a non-trivial connection between the Mercer decomposition of the random kernel and the limiting spectral distribution of the empirical kernel matrix, arguing that when the limiting spectral measure is nonrandom, the eigenvalue-eigenfunction correlations are asymptotically irrelevant. This reframes a key difficulty in BNN posterior computation.

- **Novel integral formulas connecting BNN predictors to spectral measures (Theorem 3.4).** The expressions for the predictor mean and variance in terms of the limiting spectral measure of the modified NNGP kernel, under the SUA, provide a unified framework covering both the linear-width and sublinear-width regimes. This offers a new way to think about BNN predictors that avoids sampling in weight space.

- **Connection between SUA and renormalization theory (Theorem 3.5).** The paper identifies a condition — that the random feature map can realize all orthogonal matrices — under which the renormalization theory of Li & Sompolinsky (2021) extends to nonlinear networks. This links two previously separate literatures and provides a criterion (even if hard to verify) for when the approximation should work.

- **Addressing the sublinear-width regime.** The paper identifies that existing renormalization theory breaks when P ∝ N·N₀, and proposes a finite-sample empirical spectral approach that goes beyond what existing theory can handle. The experiments suggest the method tracks variational inference predictions reasonably well in this regime.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 3.3's proof is inadequate for a central theoretical claim.** The paper's proof (lines 71–72) argues: the limiting spectral measure is nonrandom → "the eigenvalues can be sampled independently from the eigenfunctions" → the kernel matrix and ΦΛΦ^T converge to the same distribution. This jumps from "the marginal eigenvalue distribution is deterministic" to "eigenvalues and eigenfunctions are independent in the joint limit" without justification. Baker (1977) concerns convergence of eigenvalues for *fixed* kernels to Mercer eigenvalues, but here the kernel is random and the limiting argument requires controlling the joint distribution of eigenvalues and eigenfunctions. Because Theorem 3.3 underpins the entire subsequent framework (the integral formulas, SUA connection, and renormalization extension), the paper's main results rest on an unsubstantiated claim.

2. **Multi-layer spectral measure composition via "immediate induction" is unjustified.** The paper claims (line 77) that the limiting spectral measure in the linear-width regime is ρ_MP^α ⊠^L ρ_NNGP^α₀ by "immediate induction, successively applying the linear-width limit to the hidden-layer widths." The cited work (El Harzli et al., 2024) treats the case where interior widths are already infinite and the proportional limit applies only to the last-layer width. Extending this to all hidden layers simultaneously — or even sequentially — requires controlling the interaction of Marchenko–Pastur transformations at each depth, and ensuring that the spectral measure resulting from one MP transformation satisfies the structural conditions for the next. The paper does not address whether the composed spectrum admits the necessary factorization for each inductive step. The "immediate induction" glosses over a non-trivial technical hurdle.

3. **Theorem 3.5's "if and only if" is not properly proven.** The proof (lines 124–138) only sketches one direction: assuming the existence condition (SUA holds) → the Gaussian marginal likelihood follows by analogy with the linear case. The converse direction is argued in a single sentence: "if the SUA does not hold, the integral with respect to Φ does not span the space of orthogonal matrices, the identity equation 6 is no longer exact... nor is the renormalisation." This does *not* constitute a proof of the "only if" direction — it merely asserts the contrapositive without establishing why failure of the span implies failure of the Gaussian form. Moreover, the forward direction's argument ("it suffices to consider the linear case and a new training dataset X̃ which exhibits the same covariance structure") is itself heuristic rather than rigorous. An "if and only if" theorem demands justification for both directions.

4. **The integral formulas (Theorem 3.4) contain ambiguities and the derivation is absent from the main text.** The expressions shown (equations 2–3) raise several specific concerns that the paper does not resolve: (a) the term Φ^T Φ^T appears consecutively in equation 2 without clarification; (b) the inversion K⁻¹ = Φ Λ⁻¹ Φ^T requires Φ^T Φ = I exactly, but for finite P this orthonormality holds only approximately; (c) the integration measure DΦ is described as both a "standard Gaussian matrix measure" and as uniform over orthogonal matrices, with the claim that "in the limit of infinite dimensions, this space coincides with that of Gaussian matrices" — a heuristic that lacks quantified convergence. While some derivation details may reside in a stripped appendix, the formulas as typeset in the main text raise questions about correctness and scaling that the paper does not address.

5. **Experiments are too minimal to validate the theoretical claims.** The linear-width experiment (Figure 1) essentially recovers known renormalization theory results — it confirms consistency but does not test the paper's new claims. The sublinear-width experiment (Figure 2) covers a single dataset configuration (one synthetic setup with P=200, N₀=40) with no error bars, no comparison against ground-truth Bayesian inference (e.g., Hamiltonian Monte Carlo), and no assessment of sensitivity to the finite-sample approximations or the SUA accuracy. The paper attributes visible discrepancies to "finite-size effects" without quantifying them. For a paper that stakes a strong theoretical claim, this empirical support is insufficient.

### Minor

- **Sublinear-width regime is presented as a "novel technique" but the paper itself acknowledges the theory is incomplete.** The text (line 146) notes that "precisely characterising the asymptotic behavior of this Mercer's random spectral measure... is an interesting avenue for further research." This transparency is laudable but undercuts the claim in the abstract of "a novel technique for estimating the predictor statistics." The method is a numerical heuristic whose approximation quality is unknown.

- **SUA correlation structure is underspecified.** The paper states φ_i(x_j) ∼ N(μ_K, σ_K²) but does not specify the correlation structure across i and j, which matters for the joint distribution of Φ. The subsequent argument that Gaussian matrices approximate orthogonal matrices in high dimensions is cited without convergence rates.

- **Computational complexity is not discussed.** The proposed method requires diagonalizing kernel matrices multiple times and shuffling eigenvalues — the practical cost relative to variational inference or other baselines is not assessed.

### Trivial

- The likelihood specification $p(\mathbf{y},\Phi|\Lambda,\mathbf{X}) \sim \mathcal{N}(\Phi^T \mathbf{y}, \Lambda)$ in line 98 appears dimensionally mismatched ($\Phi^T \mathbf{y}$ is M-dimensional while Λ is M×M, but this is a product of P-dimensional and N-dimensional quantities that is not clearly defined without further explanation of the shapes).

## Nice-to-Haves

- Comparison against exact Bayesian inference (e.g., HMC) on small problems where ground truth can be computed.
- Error bars or confidence intervals on experimental results.
- A worked example or explicit computation of the Stieltjes transform fixed-point equation for a simple activation function.
- Discussion of computational complexity relative to alternative BNN inference methods.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing derivations of Theorems 3.3, 3.4, 3.5 in the main text":** Removed because full proof details likely resided in an appendix stripped by the parsing pipeline. The paper does provide proof sketches for Theorems 3.3 and 3.5 in the main text, and the existence of an appendix is standard.
- **"Mercer's eigenvalues for a random kernel concern":** The paper applies Mercer's theorem per realization of the random kernel, which is standard practice in the literature. The reviewer's concern about this point misinterprets the paper's approach.
- **"The paper does not give closed form of spectral measure":** The paper explicitly states it can be computed by solving the Marchenko–Pastur fixed-point equation numerically, which is sufficient for reproducibility.
- **"Pure formatting/style nitpicks":** Removed per instructions.
- **"Missing related works":** Removed per instructions (cannot verify existence of missing references).
- **Generic strength from Strength Finder about "important problem"**: Removed as insufficiently specific.

## Novel Insights

None beyond the paper's own contributions. The reviewer comments do not uncover observations that the paper itself does not already present or imply.

## Suggestions

1. **Strengthen Theorem 3.3** by providing a proper argument for why the limiting joint distribution of eigenvalues and eigenfunctions factorizes, or by weakening the claim to a construction that matches the limit (rather than claiming independence in the original process). Alternatively, derive the integral formulas without relying on this factorization.

2. **Provide a rigorous inductive argument** for the multi-layer spectral measure composition, either by establishing conditions under which sequential and simultaneous limits coincide, or by proving that the Marchenko–Pastur map of the NNGP spectral measure is itself a valid "population" covariance for the next layer.

3. **Restructure Theorem 3.5** as a one-directional claim ("if the SUA holds, then renormalization holds") unless the converse can be properly proven. An "if and only if" requires both directions.

4. **Clarify the integral formulas** — resolve the notational ambiguities, specify the exact scaling and finite-P corrections, and provide a clear derivation (or at minimum a rigorous outline in the main text) of how the posterior expectations reduce to the claimed expressions.

5. **Expand the experiments** to include: at least one comparison with exact Bayesian inference (HMC) on a small problem; error bars or multiple random seeds; a sensitivity analysis to the SUA approximation; and a check of whether the sublinear-width estimator degrades as the ratio γ increases.

## Score and Decision

The paper proposes an interesting conceptual framework connecting BNNs in proportional-width limits with kernel theory and renormalization, and it identifies a genuinely important problem (extending the theory beyond the linear-width regime). However, the theoretical development as presented is too sketchy to support the claimed contributions. The central Theorem 3.3 lacks a convincing proof, the multi-layer spectral composition is hand-waved, Theorem 3.5's "if and only if" is only partially argued, and the integral formulas contain unresolved ambiguities. The experiments are illustrative at best and do not compensate for the theoretical gaps. These are structural issues, not merely presentational.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>