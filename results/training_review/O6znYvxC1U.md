Now I have thoroughly verified every claim against the actual paper. Let me produce the final consolidated review.

## Summary

This paper aims to bridge kernel-theoretic and statistical-mechanics approaches to Bayesian neural networks (BNNs) by studying the spectral properties of the empirical kernel matrix in linear-width and sublinear-width regimes. The authors propose integral formulas (Theorem 3.4) for BNN predictor statistics based on the limiting spectral measure under the spectral universality assumption (SUA), and attempt to prove that the renormalisation theory of Li & Sompolinsky (2021) extends to nonlinear BNNs iff the SUA holds (Theorem 3.5). The paper also claims convergence of the empirical kernel matrix to a random matrix with independent eigenvalues (Theorem 3.3). Experiments compare the estimators to the renormalisation theory and variational inference.

## Strengths

- **Conceptual contribution linking SUA to BNN renormalisation.** The paper correctly identifies that the spectral universality assumption (SUA) from kernel theory can serve as a criterion for the applicability of renormalisation theory to nonlinear BNNs (Section 3.3). This connection between two previously separate research directions — random-matrix/kernel approaches and statistical-mechanics/renormalisation approaches — is a worthwhile conceptual step.

- **Identifies the sublinear-width regime as a gap in existing theory.** The paper rightly notes (Section 3.4) that the renormalisation theory breaks when α and α₀ are unbounded, and that new tools are needed for this regime. The observation that the integral estimators (setting aside their technical issues) could remain applicable through the strictly positive spectral support is a reasonable direction.

- **Attempts to provide a unified framework.** The ambition of treating linear and nonlinear BNNs, linear-width and sublinear-width regimes, and connecting kernel and renormalisation perspectives within a single framework is commendable and could, if properly executed, be a valuable contribution.

## Weaknesses

### Fatal

None. The paper does not contain outright fabrication or methodology that is fundamentally unsalvageable, though several issues are severe.

### Major

1. **The conditional likelihood is specified incorrectly (Section 2).** The paper states: `p(y|X,Θ,W^L) ∼ 𝒩(y, φ(Θ,X)^T W^L W^{L^T} φ(Θ,X))`. The mean is set to the observed data **y**, but a likelihood should have its mean equal to the model prediction `φ(Θ,X)^T W^L` (the network output). Moreover, the covariance is a rank-deficient P×P matrix rather than a standard noise covariance. This is not a parser artifact — the LaTeX clearly encodes this form. The paper appears to confuse the *conditional likelihood* (given parameters) with the *marginal likelihood* (integrated over parameters), where the latter can have mean y under the renormalisation theory. This error undermines the mathematical foundation of the entire BNN setup.

2. **Theorem 3.4 is not stated with sufficient mathematical precision.** Two concrete problems render it uninterpretable as written: (a) The "likelihood" is written as a joint distribution `p(y,Φ|Λ,X) ∼ 𝒩(Φ^T y, Λ)`, where the mean depends on the random variable **y** itself — this is circular and dimensionally inconsistent. The expression does not specify what it is a density over. (b) It describes `𝒟Φ` as a "standard Gaussian matrix measure" but then specifies entries as i.i.d. `N(μ_{K_Θ}, σ²_{K_Θ})`, which contradicts "standard" (typically zero-mean, unit-variance). These issues need to be resolved before the formulas can be used as claimed.

3. **Theorem 3.3 is not proved.** The proof sketch (≈10 lines) is insufficient to establish the claimed convergence in distribution over ℝ^{ℕ×ℕ}. The argument that "positive semi-definiteness ... suffices to characterise the kernel property" does not establish convergence of random matrices. The step invoking Baker (1977) to conclude the spectral measure limit assumes the very convergence that needs proof. The claim that eigenvalues can be sampled independently from the limiting spectral measure ignores the eigenvalue correlations inherent in finite random matrices — this would be a spectral universality result requiring substantial proof, not an immediate consequence. Because later results depend on this theorem, the theoretical framework is on weak footing.

4. **Theorem 3.5 is not rigorously proved.** The forward direction (SUA ⇒ renormalisation) relies on an unjustified step: "it suffices to consider the linear case and a new training dataset X̃ which exhibits the same covariance structure." No construction of such X̃ is given, and it is not obvious that one exists in general. The backward direction (renormalisation ⇒ SUA) is a non sequitur: the paper assumes the only way to obtain the Gaussian marginal likelihood form is through uniformity over the orthogonal group, but this is neither proved nor argued. The theorem claims "necessary and sufficient conditions on the data and the architecture" (Introduction), but the stated condition — existence of Θ achieving any orthogonal Φ — is not verifiable from data or architecture properties and thus provides no actionable criterion.

5. **The derivation that the limiting spectral measure in the linear-width regime is `ρ_{MP}^α ⊠^L ρ_{NNGP}^{α₀}` is not rigorous.** The paper claims this is "a direct corollary of Theorem 2 in El Harzli et al. (2024)" via "immediate induction." However, El Harzli et al. study the NNGP kernel matrix (where widths are already infinite), not the random feature kernel matrix `K_Θ^{P,N,N₀}(X,X)` where Θ itself has finite width. Extending their result to the latter setting requires additional arguments that are not provided. The induction step "successively applying the linear-width limit to the hidden-layer widths" is not explained.

### Minor

1. **Figure 1 validates consistency with the renormalisation formula, not with actual BNNs.** The comparison shows that the paper's estimator reproduces the renormalisation theory's predictions, but does not establish that either the estimator or the renormalisation formula accurately describes a trained BNN. No comparison against actual BNN posteriors (e.g., via HMC) is provided for the linear-width regime.

2. **Figure 2 provides only a qualitative comparison.** The sublinear-width experiment shows "reasonable matches" to variational inference, but no error bars, quantitative metrics (MSE, negative log-likelihood), or ablation of the SUA are given. The experimental setup uses eigenvalue shuffling (line 160) without theoretical justification.

3. **Section 3.4 (sublinear-width regime) is largely descriptive.** The paper acknowledges that the limiting spectral measure is unknown and renormalisation theory breaks, but offers no theoretical results for this regime. The suggestion to numerically estimate the positive spectral support is standard and does not require the paper's theoretical framework.

4. **The "if and only if" condition in Theorem 3.5 is not actionable.** The condition "there exists Θ such that φ(Θ,X)^T φ(Θ,X) = ΦΛΦ^T for every orthogonal Φ" cannot be checked for a given architecture and dataset, so the theorem does not provide a practical criterion despite the Introduction's promise.

### Trivial

- The notation `dρ(Λ)` where Λ is a diagonal matrix but ρ is defined as a measure over eigenvalues is sloppy; this is common in the literature but should be clarified.
- Calling `𝒟Φ` with `Φ_{i,j} ∼ N(μ,σ²)` a "standard Gaussian matrix measure" is inconsistent with standard terminology.

## Nice-to-Haves

- Compare the estimator against actual BNN posteriors (via HMC or exact enumeration for small P,N,N₀) in the linear-width regime, not just against the renormalisation formula.
- Test the estimator's degradation when the SUA is known to fail (e.g., spiked covariance data) to validate the claims about the SUA's role.
- Provide error bars on Figure 2 and quantitative metrics.
- Include an ablation showing how the predictor variance changes as the kernel matrix becomes degenerate with increasing α,α₀.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

- The critic's concern about the pseudo-inverse of Φ not being defined: Φ is P×M with finite M for any finite construction — the pseudo-inverse exists. The *limit* M→∞ needs care, but the pseudo-inverse itself is not ill-defined. **Reason: factually overstated.**

- "No comparison against actual trained BNNs is provided for the linear-width regime" and "the match is qualitative and no error bars" — these are kept in Minor above. The critic's phrasing that Figure 2 "only" provides qualitative comparison is fair; the more extreme claim that "no error bars or quantitative metrics" renders the experiment invalid would be overreach, so it is kept as a Minor issue.

- The criticism about Theorem 3.5 being "trivial or circular" — the theorem's **proof** is insufficient (kept as Major #4), but the *statement* of the theorem is not trivial; it genuinely connects SUA and renormalisation. The critic's "trivial or circular" label is too strong; the issue is insufficient proof, not that the result is trivial. **Reason: overclaimed; the issue is incomplete proof, not triviality.**

- The critic's "Missing Experiments" and "Deeper Analysis Needed" sections are suggestions for improvement, not weaknesses. These are moved to Nice-to-Haves.

- The critic's "Obvious Next Steps" suggestion to "Fix the likelihood definition" is valid but is a directive, not a weakness. The existence of the error is kept in Major #1.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core problem clearly: the paper has a promising conceptual framework (linking SUA to renormalisation theory) but the mathematical execution is not up to the standard required to substantiate the claims. The most insightful observation across the reviews is that the paper confuses the conditional likelihood with the marginal likelihood — this is a basic error that needs to be fixed before the remaining theorems can be properly assessed.

## Suggestions

1. **Correct the likelihood definition.** The conditional likelihood `p(y|X,Θ,W^L)` should have mean equal to the network output `φ(Θ,X)^T W^L`, not the observed data y. The covariance should be a scalar or simple diagonal noise term. Clarify how this relates to the marginal likelihood form `p(y|X) ∼ 𝒩(y, ...)` that appears in the renormalisation theory.

2. **Restructure Theorem 3.3 as an assumption or provide a real proof.** The current proof sketch does not establish the claimed convergence. If the result is essential, provide (a) a defined topology on ℝ^{ℕ×ℕ}, (b) a tightness argument, and (c) justification for independent eigenvalue sampling. Otherwise state it as a conjecture or condition.

3. **Rewrite Theorem 3.4 with precise notation.** Specify what `p(y,Φ|Λ,X)` means as a density, fix the dimensionally inconsistent expressions, and clarify the measure `𝒟Φ`. The formulas as written cannot be implemented or evaluated.

4. **Provide a rigorous proof for Theorem 3.5 or reframe it as a conjecture.** The forward direction needs a construction of X̃ or a different argument. The backward direction needs a proof that the Gaussian marginal form implies uniformity over the orthogonal group — or state it as a conjecture supported by intuition.

5. **Strengthen the experiments.** Add a comparison against actual BNN posteriors in the linear-width regime. Quantify the sublinear-width comparison (MSE, NLL) with error bars. Test the method's sensitivity to violations of the SUA.

---

## Score and Decision

The paper proposes an interesting conceptual connection between the spectral universality assumption and renormalisation theory for BNNs. However, the mathematical execution contains genuine errors (incorrect likelihood specification, incoherent density expressions, unsubstantiated proof sketches for all three main theorems) that prevent the paper from delivering on its claimed contributions. The experimental validation is too limited to compensate. A major revision fixing the mathematical foundation, clarifying the theorems, and providing more thorough empirical support would be needed before this work could be considered for publication.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>