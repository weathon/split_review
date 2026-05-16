Now I have all the information needed to produce the consolidated review. Let me verify each key claim against the paper text before finalizing.

---

## Summary

This paper provides the first rigorous sparsistency analysis for ℓ₁-regularized inverse optimal transport (iOT). It derives an irrepresentability-type condition (the "certificate") for support recovery of the ground cost, proves finite-sample complexity bounds (Theorem 1), and works out the Gaussian case in closed form, showing that iOT interpolates between the Lasso (ε → ∞) and the graphical Lasso (ε → 0). The theory is supported by numerical experiments on graph-structured costs.

## Strengths

1. **First sparsistency theory for ℓ₁-regularized iOT with sample complexity.** The paper proves that under a non-degenerate certificate condition, the ℓ₁-iOT estimator recovers the true support with sample complexity scaling as n^{-1/2} (Theorem 1). This goes substantially beyond prior iOT work (Dupuy & Galichon, Carlier et al.) that lacked finite-sample guarantees for sparse recovery in the continuous setting.

2. **Generalized irrepresentability condition for a non-quadratic, non-fixed-design loss.** The certificate in Definition 1 extends the Lasso irrepresentability condition to the iOT loss, whose Hessian depends on the full coupling structure rather than a fixed design matrix. The analysis via Proposition 2 (minimal-norm subgradient) and the implicit function theorem is non-trivial and yields a condition that is both sufficient for and (via the subdifferential) connected to necessity.

3. **Explicit connection between iOT, Lasso, and graphical Lasso in Gaussian limits.** Propositions 4 and 5 show that as ε → ∞ the iOT certificate converges to the Lasso certificate, and as ε → 0 (with symmetric positive-definite A and isotropic covariances) it converges to the graphical Lasso certificate. This is the first result linking inverse OT to graph estimation and provides interpretable insight into how the entropic penalty dictates which sparse structure is learned.

4. **Closed-form Hessian for Gaussian marginals (Lemma 3).** The paper provides an explicit formula for ∇²W(A) that extends Galichon's earlier result to a more general setting, enabling concrete computation of the certificate in the Gaussian case.

5. **Finite-sample analysis of dual certificates (Proposition 3).** The paper bounds the deviation between population and empirical certificates with explicit constants, providing the non-asymptotic foundation for Theorem 1. The numerical experiments in Section 6 validate that recovery failures align with certificate degeneracy, directly supporting the theory.

## Weaknesses

### Fatal

None.

### Major

1. **The exponential factor exp(C‖A_soln‖₁/ε) in Theorem 1 is presented without discussion of its source, implications, or whether it is improvable.**  
   The bound requires  
   \[
   \max\Big\{\frac{\exp(C\|A_{\text{soln}}\|_1/\epsilon)\sqrt{\log(1/\delta)}}{\lambda},\; \sqrt{\log(2s)}\Big\} \lesssim \sqrt{n},
   \]  
   which is the paper's central quantitative result. The factor exp(C‖A_soln‖₁/ε) is enormous when ε is small (the empirically relevant regime for OT) or when the true cost has large ℓ₁ norm, making the bound potentially vacuous. The paper never explains where this factor comes from (e.g., Lipschitz constants of the log-partition function, strong convexity modulus, or uniform concentration bounds), whether it is an artifact of the proof technique, or whether it could be tightened using local properties such as restricted strong convexity. The paper even acknowledges numerically that sparsistency fails for ε = 0.1, which is consistent with the bound becoming vacuous, but this connection is not discussed. Since this is the headline quantitative result, the reader deserves a clear statement of the limitation and its source. **(Evidential gap; fixable but meaningful — the bound's practical regime of validity is unclear without this discussion.)**

### Minor

1. **Lemma 3 (Gaussian Hessian formula) does not specify conditions under which the matrix inverses in the expression exist for non-invertible A.**  
   The paper claims (lines 276–277) that Lemma 3 generalizes Galichon's formula to the case where A is rectangular or rank-deficient. However, the stated formula involves inverses of (Σ_β − Σ^⊤ Σ_α^{−1} Σ) and (Σ_α − Σ Σ_β^{−1} Σ^⊤), and the lemma statement does not specify conditions for their invertibility when A is non-invertible. The "general formula" is presented without clarifying what assumptions are needed for the expression to be well-defined. This is a methodological gap in an otherwise clean technical contribution. **(The paper should either state precise conditions or qualify the claim.)**

2. **Proposition 5 (ε → 0 limit) requires A to be symmetric positive-definite and Σ_α = Σ_β = I, which is a significant specialization.**  
   The paper states these restrictions, but does not discuss how much they narrow the scope of the graphical Lasso connection. The original iOT problem does not require A to be symmetric or positive-definite, nor isotropic marginals. The reader would benefit from a brief note that this connection, while insightful, applies to a constrained version of iOT, and that relaxing symmetry would lead to a different limit.

### Trivial

1. **Figure 2 caption lacks experimental setup details.** The caption reports recovery performance vs. λ for three ε values, but does not state the number of samples N used, whether results are averaged over trials, or error bars. (The graph size n=80 is mentioned in the text, but the sample size is not clearly reported.)

2. **The scaling λ = λ₀ ε in Proposition 5 is non-obvious and the paper provides no derivation.** A one-sentence explanation of why this scaling yields a non-degenerate limit would improve readability.

## Nice-to-Haves

- A brief discussion of how λ could be chosen in practice given n (e.g., "λ must dominate the estimation error from Proposition 3 but be small enough that the population certificate condition holds").
- A simple non-Gaussian synthetic example (e.g., categorical distributions) demonstrating that the certificate is computable and sparsistency holds — this would strengthen the claim that the theory applies beyond Gaussians.
- A remark on the computational cost of verifying the irrepresentability condition a priori (it requires the Hessian of W, which itself requires solving an EOT problem).

## Removed Points

These points were removed (treated with caution):
- **Criticism that the paper does not verify centering preserves linear structure (Section 2).** This is a standard empirical demeaning operation that preserves linearity; the concern does not affect the paper's claims.
- **Claim that Proposition 5's symmetry constraint is not stated explicitly.** The paper *does* state "optimizing over symmetric positive semi-definite matrices" and "for symmetric A≻0." The criticism was partially inaccurate; the retained version above captures the substantive residue.
- **Request for more baselines or comparisons.** This is a theoretical analysis paper; benchmarking against other methods is not required for the core contribution.
- **Formatting/style nitpicks and missing appendix references.** These are parser artifacts or out-of-scope for the paper's contribution class.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the exponential factor exp(C‖A_soln‖₁/ε) in the sample complexity bound is not merely a technical constant — it creates a fundamental tension between the entropic regularization strength ε and the sparsity-inducing ℓ₁ regularization. Small ε (the "sharp" OT regime) makes the bound vacuous, which numerically manifests as sparsistency failure (ε=0.1). The paper implicitly demonstrates that sparsistency is practically achievable only in the large-ε regime, which is precisely when the connection to the standard Lasso emerges. Neither the harsh critic nor the strength finder explicitly draws this connection, but together they reveal that the paper provides a rigorous explanation for *why* one must choose between accurate OT coupling (small ε) and reliable cost recovery (large ε) — a trade-off that was previously understood heuristically at best.

## Suggestions

1. **Add a paragraph after Theorem 1 that identifies the source of exp(C‖A_soln‖₁/ε)** (e.g., uniform concentration bounds over the function class, or the Lipschitz constant of the log-partition function), discusses whether it can be refined via localized arguments (e.g., restricted strong convexity), and explicitly states that for small ε the bound becomes vacuous — consistent with the numerical observation that sparsistency fails in that regime.

2. **State precise conditions for Lemma 3** (e.g., when the matrices (Σ_β − Σ^⊤ Σ_α^{−1} Σ) and (Σ_α − Σ Σ_β^{−1} Σ^⊤) are invertible), or, if the formula holds in a generalized sense (e.g., via Moore–Penrose inverses), say so explicitly.

3. **Add a sentence justifying the scaling λ = λ₀ ε in Proposition 5** and note that the symmetry/positive-definiteness restriction, while needed for the graphical Lasso connection, is a genuine constraint on the original iOT problem.

## Score and Decision

**Originality:** High — first sparsistency theory for ℓ₁-iOT with novel connections to Lasso/graphical Lasso.  
**Importance of question:** Moderate-to-high — iOT is a growing area and theoretical guarantees are scarce.  
**Claims supported:** Mostly, but the exponential factor in Theorem 1 requires more transparent discussion.  
**Soundness of experiments:** Adequate for a theory paper — numerics validate the certificate condition.  
**Clarity of writing:** Good — the paper is well-structured and the key ideas are explained.  
**Value to community:** Positive — opens a rigorous avenue for understanding sparse cost recovery in iOT.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>