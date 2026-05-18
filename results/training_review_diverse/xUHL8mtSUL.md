Now I have a thorough understanding of the paper and can verify the reviewer's claims. Let me write the consolidated review.

## Summary

This paper proposes a scalable Gaussian process regression method based on the Hilbert-Schmidt Singular Value Decomposition (HS-SVD). By using the compact Matérn kernel — whose eigenfunctions (sine bases) and eigenvalues are known analytically and independent of kernel parameters — the method achieves a low-rank approximation of the kernel matrix with O(n m²) time and O(n m) space complexity without explicitly computing an expensive low-rank decomposition. The paper provides theoretical grounding by connecting the compact Matérn kernel to the modified Helmholtz operator, proves a smoothness theorem, and evaluates the method against nine baselines on simulated large-scale datasets.

## Strengths

- **Clean algorithmic approach with clear complexity advantages.** The method's key insight — leveraging known Mercer eigenfunctions that are independent of kernel parameters — is elegant. Because Φ and ΦᵀΦ are precomputed once and reused across MLE iterations, the method avoids recomputing the kernel matrix or its decomposition during optimization. This is a genuine practical advantage over methods that require recomputation at each gradient step.

- **Theoretical connection to the standard Matérn kernel via the modified Helmholtz operator (Proposition 3.5).** This provides a principled justification for using the compact Matérn as a drop-in replacement for the standard Matérn on bounded domains, and ensures that comparisons against methods using standard Matérn kernels are on equal footing in terms of smoothness.

- **CPU-only efficiency demonstrated against GPU-accelerated methods.** Figure 1 and the simulation results (though tables are not visible in the extracted text) indicate that HS-SVD on a single CPU core can outperform GPU-accelerated SKI and LOVE in runtime on datasets up to 2 million points. If these results hold, this is practically valuable for users without GPU access.

- **Smoothness theorem (Theorem 3.3) provides explicit control over kernel regularity**, analogous to the ν parameter in the standard Matérn family.

## Weaknesses

### Fatal
None.

### Major

- **The zero boundary condition of the compact Matérn kernel is acknowledged but its practical implications are not discussed or investigated.** The sine eigenfunctions φ_l(x) = √2 sin(lπx) vanish at the boundaries of [0,1]^r, meaning the GP prior forces predictions toward zero at the domain edges. Proposition 3.5 explicitly states this arises from the modified Helmholtz operator "with zero boundary condition." The paper then dismisses this by stating the domain can be replaced "with any closed interval or bounded region without loss of generality" — but the boundary condition remains zero regardless of which bounded region is chosen, because the eigenfunctions are tied to the Laplacian with Dirichlet boundary conditions. If the target function does not tend to zero at the boundaries, the prior will introduce bias near the edges that does not vanish asymptotically. The paper provides no experiments investigating boundary effects, no discussion of when this matters in practice, and no proposed remedy (e.g., centering the data, adding a parametric mean function, or using a basis with different boundary conditions). This is a first-order concern for practitioners evaluating whether the method suits their problem.

- **The simulation study is insufficiently specified for reproducibility or rigorous assessment.** The paper states that ∼100,000 samples are generated from "highly nonlinear functions" but does not specify the exact functions, the noise variance, the criterion for choosing m, or the hyperparameter ranges. The results (MSE, runtime, memory) are reported in tables that are not visible in the extracted text, and no individual simulation results are described in prose. While the authors state code is available, the paper alone does not provide enough detail to evaluate whether the method is tested under realistic challenges (e.g., non-zero boundary functions, non-stationary behavior). The paper also omits comparisons against random Fourier features and Nyström approximations — the most natural spectral low-rank baselines — while including nine other methods. This makes it difficult to attribute the method's advantage to the HS-SVD approach specifically versus the kernel choice or implementation.

- **No experiments on real-world data.** All empirical validation is on simulated data. For a methods paper presenting a practical GP approximation, evaluation on at least one real dataset (e.g., from a spatial statistics repository or UCI benchmark) is expected to demonstrate that the method works outside synthetic sine-construction-compatible settings, particularly given the boundary condition concern above.

### Minor

- **The claim of "no preprocessing overhead" / "for free" is overstated.** Constructing the n×m matrix Φ of sine evaluations and computing ΦᵀΦ is an O(n m²) operation. While far cheaper than O(n³) or O(n²), and while the paper correctly states the overall O(n m²) complexity, the framing of "no preprocessing overhead" implies zero cost. This is misleading: the method still requires evaluating m sine functions at n points, which is a one-time precomputation cost. The O(n m) memory for storing Φ is also not negligible for large n and moderate m (e.g., 8 GB for 10⁶×10³ in double precision).

- **No guidance is provided for choosing m in practice.** The paper describes m as "easy-to-tune" but offers no heuristic, no analysis of approximation error as a function of m, β, and r, and no discussion of how to select m in a data-driven way. The curse of dimensionality is mentioned in the Discussion (m grows exponentially with r), but this limitation should be part of the method's core description, not deferred to the final section.

### Trivial

- **Theorem 3.3 states the compact Matérn kernel is β−r−1 times differentiable**, but for β ≤ r this expression becomes ≤ −1, which is not meaningful for differentiability order. The proof is in the appendix (stripped), but the main-text statement should include the relevant constraint on β relative to r (or state the differentiability as max(0, β−r−1)).

## Nice-to-Haves

- A breakdown of wall-clock time (Φ construction vs. likelihood optimization vs. prediction) would help users understand where the method's time is spent.
- An analysis of the approximation error ‖K_XX − Φ_m Λ_m Φ_mᵀ‖ as a function of m, β, and r would strengthen the method's theoretical characterization.
- Discussion of how to handle non-gridded data with repeating coordinates, and the required preprocessing to rescale inputs to [0,1]^r.

## Removed Points

These points were raised by reviewers but are excluded from the main assessment for the following reasons:

- **"The algorithm contains an undefined variable C in 'H ← 1/σ (Y − ΦCΦᵀY)'."** The text shows a LaTeX rendering with C and a plain-text version with G concatenated — this is a parser artifact. Minor notation issues of this kind carry no weight in the evaluation.
- **"Truncating small eigenvalues for numerical stability is a general property, not specific to this method."** The paper is entitled to list this as a benefit of its approach; claiming it as a contribution would be overreach, but the paper presents it as a consequence, not a novelty.
- **"The paper does not report wall-clock times for the full pipeline in a table, only a single figure."** Figure 1 explicitly reports runtime. The tables (stripped) also contain timing information. This criticism is not supported by the paper.
- **"The theoretical contribution is thin — the core idea is a direct application of known results."** The paper is an algorithmic/empirical methods paper, not a theoretical paper. Its contribution is in the combination and application, not in new mathematical theory. Evaluating it against theoretical novelty expectations is a category error.
- **"The paper does not discuss how to handle discrete or non-gridded data with repeating coordinates."** The eigenfunctions are defined on [0,1]^r, which requires rescaling — a common preprocessing step for any method working on compact domains. This is a nice-to-have, not a core weakness.

## Novel Insights

The most interesting tension exposed across the reviews is between the method's mathematical elegance and its practical blind spots. The HS-SVD approach is genuinely clean: the compact Matérn's eigenfunctions are parameter-independent, which means Φ and ΦᵀΦ are computed once and reused throughout MLE — a structural advantage over methods that must recompute or re-factor during optimization. Yet the paper's evaluation strategy (simulated functions of unspecified form, no real data, no investigation of boundary effects) leaves the reader unable to assess whether this elegance translates to robust performance in practice. The boundary condition issue is particularly subtle: the standard Matérn on ℝʳ imposes no boundary behavior, so moving to [0,1]ʳ with Dirichlet conditions is not "without loss of generality" — it is a genuine modeling assumption that will matter whenever the response does not naturally return to zero at the domain edges. The paper would benefit from openly characterizing this trade-off rather than glossing over it.

## Suggestions

1. **Confront the boundary condition issue head-on.** Add an experiment where the true function has non-zero endpoints (e.g., a linear trend) and measure prediction error near boundaries. Discuss practical mitigations: centering the data, adding a parametric mean function, or extending to Neumann/Robin boundary conditions.
2. **Specify the exact simulation setup** (the true functions, noise variance, criterion for choosing m, hyperparameter ranges) in the paper text, not just in the supplementary code.
3. **Include comparisons against random Fourier features and Nyström approximations** as the most directly comparable spectral low-rank baselines.
4. **Replace "no preprocessing overhead"** with an honest accounting of the O(n m²) one-time cost and O(n m) memory for Φ.
5. **Add at least one real-world dataset** (e.g., from spatial statistics, UCI, or a GP benchmark repository).
6. **Provide practical guidance for choosing m**, both as a heuristic and via an error analysis showing how approximation quality varies with m, β, and r.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>