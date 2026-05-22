Now I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper studies sparse support recovery when observations come from two sources with different noise levels (high-quality/low-quality). It establishes sufficient conditions for information-theoretic recovery in agnostic and informed settings, introducing a **Price of Quality** (γ) that quantifies how many low-quality samples replace one high-quality sample under these conditions. On the algorithmic side, it extends the LASSO phase transition (Wainwright 2009) to the heterogeneous-noise agnostic setting, showing the threshold depends only on the average noise level.

## Strengths

- **First study of mixed-quality data for sparse recovery.** The problem is well-motivated (LLM-labeled data, citizen science, multi-site trials) and the paper provides the first sample-size conditions for this setting. The distinction between agnostic and informed decoders is natural and leads to qualitatively different mathematical structures.

- **Principle-based extension of the LASSO phase transition.** Theorem 3 generalizes Wainwright (2009) to heterogeneous noise, proving that the algorithmic threshold (2s log(p−s) + s + 1) is robust to data heterogeneity. The proof overcomes the loss of Wishart structure via a QR decomposition of X_S and Haar-measure arguments on the orthogonal group — a non-trivial technical extension.

- **Closed-form price-of-quality expressions across SNR regimes.** The paper derives explicit asymptotic formulas for γ in both settings (equations 12–14, 18–21), giving concrete, interpretable guidance (e.g., γ ≈ 1 when both SNRs are high, γ < 2 in the agnostic low-SNR regime). Remark 3.4 generalizes the sufficient conditions to arbitrary invertible noise covariances.

- **Honest and precise discussion of limitations.** Remark 3.2 explicitly states that the agnostic condition arises from a Chernoff-bound relaxation and "is not expected to be information-theoretically sharp." The conclusion acknowledges that the informed and LASSO thresholds are sharp but the agnostic information-theoretic condition is not. This transparency is commendable.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The headline price-of-quality result (γ ≤ 2) is derived from a sufficient condition acknowledged as non-sharp.** The paper is transparent about this (Remark 3.2), and the price-of-quality γ is defined as a property of the *sufficient condition*, not the true recovery threshold. However, the paper's most striking practical claim — "one high-quality sample is never worth more than two low-quality samples" — is the result most likely to be cited and remembered. The connection between γ derived from the relaxed Chernoff bound and the true information-theoretic sample-complexity trade-off is unestablished. Without at least a lower bound (even under additional assumptions), the reader cannot assess whether the γ ≤ 2 bound reflects the actual problem or is an artifact of the relaxation. This limits the significance of the paper's main conceptual contribution.

- **The LASSO necessity direction (Theorem 3(i)) carries a mild technical restriction on λₚ.** The necessity holds "for any sequence λₚ > 0 such that (n₁σ₁²+n₂σ₂²)/(λₚ² n²) has a limit in ℝ≥₀ ∪ {+∞}." This excludes λₚ sequences without a well-defined asymptotic limit (e.g., oscillatory choices). While this is a standard technical caveat (one can pass to a subsequence) and covers all practically relevant scalings, the paper does not explicitly discuss it. A brief remark clarifying why this is non-restrictive would strengthen the presentation.

### Trivial

- None.

## Nice-to-Haves

- A simple simulation study confirming that the sufficient condition (9) is not grossly loose would strengthen the practical relevance. For a theory paper this is not required, but the non-sharpness acknowledged in Remark 3.2 makes even a small empirical validation helpful.
- A discussion (even heuristic) of whether the informed sufficient condition (16) is tight — the Chernoff exponent is optimized exactly, but necessity is not proved.
- Clarifying that the λₚ restriction in Theorem 3(i) is non-restrictive because one can always pass to a subsequence where the limit exists.

## Removed Points

- **"The price of quality is defined and analyzed only for sufficient conditions, so the paper's main findings may not reflect the actual problem"** — This is already acknowledged by the paper. The paper repeatedly qualifies its claims with "under our sufficient condition" / "for the sufficient condition to hold" (see lines 95, 193, 205, 350). Remark 3.2 discusses the non-sharpness explicitly. The paper's contribution is stated as providing sufficient conditions, which it delivers. Downgraded from "structural/fatal" to Minor.
- **"The LASSO necessity condition may not cover all relevant λₚ choices"** — The condition covers all limit values in ℝ≥₀ ∪ {+∞}, which is essentially any λₚ with well-defined asymptotic behavior. This is standard in asymptotic analysis. Downgraded from Major to Minor.
- **"The paper overclaims by calling Theorem 3 a phase transition while necessity has a restriction"** — The restriction is mild, and the paper provides both directions. The term "phase transition" is justified.
- **"The comparison of agnostic vs informed (Remark 3.3) may not be valid at the information-theoretic level"** — The paper's comparison is framed appropriately as a comparison of sufficient conditions. The remark notes that the informed estimator "constitutes a better use of high-quality data" in the sense of yielding a higher γ from the derived sufficient conditions. This is a correct comparison of the quantities the paper analyzes.
- **Strength Finder: generic/superlative strengths removed** — None found; all strengths listed are concrete and evidence-based.

## Novel Insights

The reviews surface an important nuance that the paper itself addresses but could emphasize more: the agnostic price-of-quality (γ ≤ 2) and the informed price-of-quality (γ → ∞) are both derived from sufficient conditions, but the *types* of relaxations differ. The agnostic condition involves an explicit relaxation of the Chernoff exponent (cubic equation → closed form), while the informed condition optimizes the Chernoff exponent exactly. This means the agnostic γ bound is doubly conditional (on the sufficient-condition framework *and* on the relaxation), while the informed γ is conditional only on the sufficient-condition framework. This asymmetry is already present in the paper (Remark 3.2 vs. Remark 3.3's second bullet) but is worth surfacing explicitly. A reader concerned about the non-sharpness should focus on the agnostic setting as the weaker link.

## Suggestions

1. Add a brief remark after Theorem 3(i) clarifying that the limit condition on λₚ is non-restrictive because one can always restrict to a subsequence where the limit exists, and that the covered scalings include all standard choices (λₚ → 0 at various rates).
2. If possible, add a lower bound (necessary condition) for the agnostic information-theoretic setting under the same model assumptions. Even a looser lower bound would help the reader understand how much gap exists between the sufficient condition and the true threshold. In the absence of such a bound, consider explicitly discussing whether the gap could change the γ ≤ 2 conclusion.
3. In the conclusion, reinforce the qualifier when summarizing the price-of-quality result (e.g., "under the sufficient condition derived here, one high-quality sample is never worth more than two low-quality samples" — the current wording drops the qualifier in one sentence, though the preceding sentence includes it).

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>