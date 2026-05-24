Now let me produce the final consolidated review.

## Summary

This paper studies sparse signal support recovery when observations come from two sources with different noise levels (heterogeneous Gaussian noise). It establishes sufficient sample-size conditions for information-theoretic recovery in both an agnostic setting (decoder unaware of per-sample quality) and an informed setting (decoder knows noise variances), defining a "Price of Quality" γ that quantifies how many low-quality samples replace one high-quality sample. It also extends the LASSO phase transition (Wainwright, 2009) to the heterogeneous-noise agnostic setting, showing the algorithmic threshold depends only on total sample size and average noise, not individual noise levels.

## Strengths

- **Theorem 1 and Theorem 2 provide the first explicit sufficient conditions for sparse support recovery under heterogeneous Gaussian noise.** The conditions take the form of a linear combination of sample sizes exceeding a threshold (eq. 9, 16), yielding a clean, interpretable trade-off between high- and low-quality samples.

- **Theorem 3 extends the classical LASSO phase transition (Wainwright, 2009) to heterogeneous noise and shows the threshold depends only on total sample size n and average noise variance σ²_avg.** The necessary condition (26) and sufficient condition (27) match the homogeneous-noise threshold n_ALG = 2s log(p−s)+s+1, and the regularization condition (28) depends on noise only through σ²_avg. This is a substantive technical extension that requires overcoming the broken Wishart structure using QR decomposition and Haar-measure arguments.

- **Proposition 4.1 provides a clean necessary and sufficient condition on noise scaling** (eq. 30) for the LASSO recovery conditions to be achievable, linking σ²_avg to sample size and sparsity.

- **The paper clearly delineates the agnostic vs. informed settings**, providing distinct sufficient conditions (Theorems 1, 2) that highlight how access to noise information changes the sample trade-off. The contrast between the settings is a genuine conceptual contribution.

## Weaknesses

### Major

- **The asymptotic analysis of the agnostic Price of Quality in the "Low SNR₂ regime" (eq. 14) contains a mathematical error that invalidates the claimed bound γ < 2.** The derivation applies the approximation log(1+x) ≈ x to both numerator and denominator of γ under the stated condition s = o(σ₂²). However, the numerator argument x_num = δ(2σ₂²−σ₁²)s/(2σ₁⁴) → ∞ as p→∞ (since s→∞), making this approximation invalid. The denominator approximation is valid (x_den → 0). Consequently, the claim that γ < 2 "for any σ₁², σ₂²" is not justified by the derivation given. This claim appears prominently in the abstract ("one high-quality sample is never worth more than two low-quality samples"), the introduction, and the conclusion. A corrected analysis likely shows that γ can grow without bound in this regime (as x_num → ∞ while x_den → 0, giving γ → ∞). **This error does not invalidate the paper's core theorems (Theorems 1-3), which remain mathematically sound as stated. The exact expression for γ (eq. 12) is correct. However, the asymptotic interpretation and the headline claim about a uniform bound of 2 are not supported by the current derivation.** A major revision is needed to either correct the asymptotic analysis with proper scaling conditions, qualify the claim, or replace it with the correct behavior.

- **The impossibility of verifying proofs without appendices.** The full proofs of all three theorems are deferred to the appendix, which is stripped from the submission. While the proof sketches in the main text are plausible and follow standard techniques, the core contribution of a theory paper depends on proof correctness. The necessity condition of Theorem 3 in particular involves technical details (Haar measure on the orthogonal group, QR decomposition) whose correctness cannot be assessed from the sketch alone. This is a structural limitation of the review format rather than the paper itself, but it means the evaluation must be conditional on the proofs being correct.

### Minor

- **The Price of Quality is defined from a sufficient (non-sharp) condition, not the true information-theoretic threshold.** The paper acknowledges this in Remark 3.2, but the abstract and conclusion present the γ<2 result without this qualification. A casual reader will take it as a fundamental bound rather than a property of a relaxed Chernoff bound. The paper should consistently signal that γ reflects a sufficient condition that is known to be loose (Remark 3.2: "the potential looseness arises from a relaxation in the Chernoff bound").

- **Potential inconsistency between eq. (9) and eq. (12).** Eq. (9) gives the coefficient of n₁ as log(1 + δ(2σ₂²−σ₁²)s/(2σ₂²)), while eq. (12) defines γ using log(1 + δ(2σ₂²−σ₁²)s/(2σ₁⁴)). These differ in the denominator (2σ₂² vs. 2σ₁⁴). The authors should verify the correct expression.

### Trivial

- None.

## Nice-to-Haves

- Adding a small simulation study (e.g., comparing the predicted threshold to actual LASSO performance under heterogeneous noise) would significantly strengthen the paper's credibility and illustrate the practical meaning of the Price of Quality and Theorem 3.
- A brief discussion of why averaging over noise levels suffices for the LASSO's ℓ₁ penalty but not for exact support recovery would deepen the paper's narrative about the robustness of algorithmic thresholds.

## Novel Insights

The most genuinely novel insight is the contrast between the information-theoretic and algorithmic thresholds: Theorem 3 shows the LASSO recovery condition depends only on total n and average noise (as if all samples had that average quality), while the information-theoretic sufficient condition exhibits a quality-dependent trade-off that differs between the agnostic and informed settings. This reveals a structural difference in how computational and information-theoretic thresholds respond to data heterogeneity that goes beyond the specific quantity being measured.

## Suggestions

1. **Correct the Price of Quality asymptotic analysis.** Specify the joint scaling conditions on σ₁², σ₂², and s under which each regime analysis is valid. If γ is actually unbounded under the "Low SNR₂" condition, state this honestly — it is still an interesting finding that differs from the informed setting.
2. **Consistently qualify the Price of Quality claims** in the abstract and conclusion as being derived from a sufficient (non-sharp) condition.
3. **Resolve any inconsistency** between eq. (9) and eq. (12) in the denominator of the first log term.

## Calibration Report

**Round 1 — Bracketing.** Three queries on "sparse recovery heterogeneous noise mixed quality data":
- Low band (avg ≤ 3.5): anchors with scores 2.67, 3.33, 2.67, 3.33 — mostly withdrawn/rejected papers.
- Mid band (3.5 < avg < 7.5): anchors with scores 6.00, 5.00, 4.00, 4.67 — spanned reject to accept decisions.
- High band (avg ≥ 7.5): anchors with scores 8.00, 8.00, 8.00, 8.50 — strong accept papers.

Initial bracket: [4.5, 6.5]

**Round 2 — Narrowing.** Queries on "theoretical paper sparse recovery LASSO" and "sparse recovery phase transition information theoretic":
- "Recovery Guarantee for Sparse Neural Networks" (avg 6.40, Accept Poster) — sound theory with scope limitations. This paper is weaker due to a derivation error.
- "Column Thresholding: Sparse Spiked Wigner" (avg 5.00, Reject) — overclaimed significance. Similar in severity to this paper's Price of Quality issue.
- "DogRot" (avg 4.67, Reject) — practical concerns but solid theory.
- "Fast Escape, Slow Convergence" (avg 5.50, Accept Oral) — rigorous analysis.

Comparing: This paper has genuine theoretical contributions (Theorems 1-3) but a clear error in the derivation of a headline claim (the γ<2 bound). This places it near the 5.0 anchor (Column Thresholding) where an overclaimed result undermined an otherwise solid paper. It is below the 6.40 anchor (Recovery Guarantee) which had no errors, only scope limitations.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>