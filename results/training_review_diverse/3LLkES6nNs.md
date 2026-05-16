Now I have all the information needed. Here is my consolidated final review.

## Summary

This paper establishes the Neural Network Gaussian Process (NNGP) correspondence for Neural ODEs, analyzing both autonomous (shared weights) and non-autonomous (independent weights) cases. The core contribution is proving that infinitely wide Neural ODEs converge to Gaussian processes with explicit, analytically characterized covariance kernels, and that these kernels are strictly positive definite for non-polynomial Lipschitz activations. The paper also provides a dynamic programming algorithm for computing these covariance matrices and conducts experiments illustrating the theoretical predictions.

## Strengths

- **Establishes NNGP correspondence for Neural ODEs with shared weights, a genuinely novel extension**: Prior NNGP results (Lee et al., Yang) applied to finite-depth networks with independent weights. This paper proves that even with shared weights across infinite depth, the Neural ODE output converges to a Gaussian process. The result is formalized in Theorem 4.5, deriving the explicit limiting covariance Σ* via a double-limit argument. This is a non-trivial extension because shared weights + skip connections create a non-Markovian structure absent in standard feed-forward or even independent-layer ResNet analyses.

- **Proves strict positive definiteness of the limiting NNGP kernel for non-polynomial activations**: This property (Theorem 4.8) is essential for global convergence guarantees in overparameterized regimes (Du et al., Arora et al.). The proof leverages Hermitian expansions and Lemma 4.2's verification that diagonal elements are equal and finite. Experimental validation (Figure 3) confirms positive smallest eigenvalues across varying width and depth.

- **Experimental validation of the core theoretical predictions**: Figures 1–3 provide supporting numerical evidence: output distributions of Neural ODE and ResNets are approximately Gaussian (Figure 1, top row), covariance matrices from simulation, dynamic programming, and ResNet match qualitatively (Figure 1, bottom row), and convergence of empirical covariance to Σ* as width and depth increase (Figure 2).

- **Clear framing and motivation of the double-limit problem**: Section 4.3 clearly explains why the depth and width limits do not automatically commute (citing Hayou & Yang, Li et al., Peluchetti & Favaro), and why the Neural ODE setting requires a dedicated analysis distinct from existing SDE-based approaches that assume independent weights.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theorem 4.2 contains a variance-parameter inconsistency**: The theorem states that the output functions converge to a GP with covariance Σ^{L+1}, where the recursion defines Σ^{ℓ+1} = σ_w² 𝔼[φ(u^ℓ)φ(u^ℓ)]. However, the actual output is f^L_θ(x) = V φ(h^L(x)), where V ~ N(0, σ_v²/n). By the law of large numbers, the output covariance should be σ_v² 𝔼[φ(u^L)φ(u^L)], not σ_w² 𝔼[φ(u^L)φ(u^L)]. This is confirmed by Proposition 4.6 (limiting covariance for the Neural ODE), which correctly uses σ_v². The inconsistency also appears in the computational section (line 245), which uses σ_v² for the output covariance. The error is in the theorem's definition — the recursion likely defines the *pre-activation* covariance, while the *output* covariance should include σ_v². The core idea remains correct, and the fix is straightforward (either redefine Σ^{L+1} with σ_v² or clarify the mapping), but as written the theorem statement is imprecise.

- **Algorithm 1 is incomplete: V_φ is never defined**: The dynamic programming recurrence (eq. 17) and Algorithm 1 both call the function V_φ(K^{ℓ-1,ℓ-1}, K^{ℓ-1,i}, K^{i,i}) without specifying what it computes. From context, this function likely evaluates an expectation of the form 𝔼[φ(z₁)φ(z₂)] under a trivariate Gaussian whose covariance is constructed from the three input matrices, but this is never stated. Without this definition, the algorithm — which the paper highlights as a contribution — cannot be implemented or reproduced. The garbled pseudocode is a parser artifact, but the missing definition is not.

- **Lemma 4.2 claims are stated without justification**: The lemma asserts that Cov(u^i(x), u^j(x)) = Cov(u^i(x'), u^j(x')) for all x, x' on the sphere. While this is a standard consequence of isotropic initialization (diagonal elements of the NNGP kernel depend only on input norm), the paper provides no argument, and the role of the activation function in potentially breaking isotropy (if φ is not odd) is not discussed. A brief inductive justification would resolve this.

- **Proposition 4.1 uses undefined constants C₁, C₂**: The Euler error bound includes constants C₁ > 0, C₂ > 0 that are never specified. While the key point (error → 0 as L → ∞) is clear, a proper statement would at minimum note that these are absolute constants depending only on the Lipschitz constant, or characterize their dependence. As written, the bound is not fully specified.

- **Experiments are primarily qualitative**: The experiments demonstrate Gaussian fits and covariance matrix visualizations, but lack quantitative validation (e.g., Kolmogorov–Smirnov tests for normality, Frobenius norm differences between theoretical and empirical covariance matrices, error bars for the MNIST accuracy curve). The MNIST experiment reports a single accuracy curve without comparison to the exact NNGP computed via their algorithm or to a finite-width baseline with error bars. The claim that "NNGP generally outperforms trained neural networks" is too strong given the evidence shown.

### Trivial
- Remark 4.7 notes that setting σ_w = 1/T mitigates instability; this practical note would benefit from a brief justification rather than being stated without analysis.
- The Section 4.5 reference to Algorithm 1 as providing an "efficient" O(L²) method could be made more precise with a complexity statement.

## Nice-to-Haves
- A discussion of limitations — e.g., the results hold at initialization only (no training dynamics), the analysis assumes specific Gaussian initialization scaling, the computational algorithm scales poorly with depth in practice — would strengthen the paper.
- Quantitative convergence metrics (e.g., relative Frobenius error of Σ^* vs. empirical covariance) in Figure 2 would strengthen the empirical validation.
- Error bars or multiple seeds for the MNIST NNGP accuracy curve.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that Lemma 4.1 is unsubstantiated / the RMT lemmas are absent**: The paper states that the proof relies on Lemma A.3/A.2 from the appendix. The appendix was stripped by the PDF parser and exists in the original submission. Per policy, criticisms about absent appendix content are removed.

- **Criticism that Proposition 4.1 "cannot be evaluated"**: The bound clearly shows the Euler error is O(1/L) and vanishes as L → ∞, which is the only property needed for the paper's arguments. The constants C₁, C₂ are not derived but their existence is sufficient for the asymptotic statement. This is a presentation imprecision, not a structural flaw.

- **Criticism that Theorem 4.2's recursion is "non-Markovian" and therefore the Tensor Program extension requires more justification**: The paper acknowledges this precisely in Remark 4.3, explaining that skip connections cause the covariance at layer ℓ+1 to depend on all previous layers, which is explicitly contrasted with the feed-forward case. The paper correctly handles this by defining u^ℓ = z⁰ + β Σᵢ₌₁^ℓ zⁱ and computing Σ^{ℓ+1} = σ_w² 𝔼[φ(u^ℓ)φ(u^ℓ)]. The reviewer's concern about circularity is unfounded — the system is well-defined recursively because Cov(zⁱ, zʲ) for i,j ≤ ℓ depends only on expectations involving u^{i-1}, u^{j-1}, which are already defined from earlier steps.

- **Criticism that the output functions should not be called i.i.d. due to shared weights**: The "i.i.d." refers to the n_out output neurons, which are independent because the rows of V are independent and identically distributed. This is standard in NNGP theory and is not affected by weight sharing in the hidden layers.

- **Criticism about the paper not proving convergence of the Σ^ℓ recursion as ℓ → ∞ for Theorem 4.5**: Theorem 4.5 defines Σ^* as lim_{ℓ→∞} Σ^ℓ, and Lemma 4.1 argues that the double limit exists. The convergence of the deterministic recurrence is part of what Lemma 4.1 establishes via the empirical covariance's a.s. convergence. The reviewer's demand for a separate proof of the recursion's convergence is addressed by the double-limit framework.

## Novel Insights

The key insight that is genuinely novel and goes beyond the paper's own claims is the structural observation (Remark 4.3) that skip connections — not weight sharing per se — are the mechanism driving the distinct NNGP behavior of Neural ODEs. In feed-forward networks with shared weights but no skip connections, the NNGP recursion factorizes in the standard way (depending only on the current layer's pre-activation). In ResNets/Neural ODEs, the skip connection introduces a cumulative sum over all past pre-activations, making the covariance non-Markovian and coupling all layers. This observation cleanly separates the effect of architecture (skip connections) from the effect of parameter tying, which is useful for understanding which architectural features drive qualitative differences in limiting kernel behavior. Beyond this, none beyond the paper's own contributions.

## Suggestions

1. **Fix the σ_v²/σ_w² inconsistency in Theorem 4.2**: Clarify whether Σ^{ℓ+1} as defined (with σ_w²) is the pre-activation covariance or the output covariance. If the former, state explicitly that the output covariance is σ_v² 𝔼[φ(u^L)φ(u^L)], and relate it to Σ^{L+1}. If the latter, replace σ_w² with σ_v² in the recursion's base case for ℓ = L (or adjust the definition throughout).

2. **Define V_φ in Algorithm 1 explicitly**: Specify that V_φ(K¹¹, K¹², K²²) computes 𝔼_{(z₁,z₂) ~ N(0, Σ)}[φ(z₁)φ(z₂)] where the 2×2 covariance Σ is constructed from the three input kernel matrices (e.g., the diagonal blocks K¹¹, K²² and the off-diagonal block K¹²). This is essential for reproducibility.

3. **Add quantitative metrics to the experiments**: Include Frobenius norm or relative error between theoretical and empirical covariance matrices, and add error bars or confidence intervals to the MNIST accuracy comparison.

## Score and Decision

The paper addresses an important and non-trivial theoretical question — the NNGP limit of Neural ODEs with shared weights — and makes a genuine contribution. The core theoretical framework is sound, the key results (NNGP correspondence for Neural ODEs, strict positive definiteness) are novel and valuable, and the experimental support, while primarily qualitative, is consistent with the theory.

The weaknesses are real but fixable: a variance-parameter error in Theorem 4.2 that does not invalidate the core idea, an underspecified function in the algorithm, and presentation imprecisions throughout. None of these are fatal or structural. A thorough revision addressing these points would produce a strong paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>