Now let me write the final consolidated review.

---

## Summary

This paper studies sparse signal support recovery when observations come from two sources with different noise variances (high-quality and low-quality data). It establishes sufficient conditions for information-theoretic recovery in both the agnostic setting (decoder ignores per-sample noise levels) and the informed setting (decoder knows them), defining a "Price of Quality" γ — the number of low-quality samples that can replace one high-quality sample under those sufficient conditions. On the algorithmic side, it extends the LASSO phase transition (Wainwright 2009) to the heterogeneous-noise agnostic setting, showing the threshold depends only on total sample size and average noise variance regardless of how noise is distributed between the two sources.

## Strengths

1. **First sufficient conditions for sparse recovery under heterogeneous noise with an explicit trade-off.** Theorems 1 and 2 provide concrete sample-size conditions (9) and (16) that are linear in (n₁, n₂), giving a clean analytical form for the cost-quality trade-off. The contrast between agnostic γ (uniformly bounded; ≤ 2 under the derived sufficient condition) and informed γ (which can diverge) is novel and conceptually clear. The paper correctly qualifies these as sufficient conditions, including Remark 3.2 that acknowledges the looseness from the Chernoff relaxation.

2. **Extension of the LASSO phase transition to the heterogeneous-noise agnostic setting (Theorem 3).** This is the paper's most technically novel result. It shows that the necessary and sufficient sample-size condition for signed-support recovery by the LASSO depends only on total sample size n and the average noise variance σ²_avg, not on the individual noise levels σ₁², σ₂². This is a non-obvious robustness result that meaningfully extends Wainwright (2009) to a setting where the classical inverse-Wishart arguments break down. The proof framework — QR decomposition of X_S plus Haar-measure analysis of the resulting orthogonal matrix — is a genuine technical innovation for handling the non-scalar noise covariance matrix Σ.

3. **Clear framing and honest limitations.** The paper clearly distinguishes the agnostic and informed settings, defines the three SNR regimes explicitly, and is transparent about where its results are sufficient versus tight. Remark 3.2 candidly discusses the relaxation used and the cubic equation that would give a tighter bound. Remark 4.2 honestly discusses why the informed LASSO extension remains open. This intellectual honesty strengthens the paper's credibility.

## Weaknesses

### Fatal

None.

### Major

1. **The headline γ ≤ 2 claim rests on a sufficient condition acknowledged to be not sharp, and the paper does not quantify how loose this bound might be.** The authors state in Remark 3.2 that the agnostic sufficient condition is "not expected to be information-theoretically sharp" due to a Chernoff relaxation, and that tightening it would require solving a cubic equation. Because γ is defined as the ratio of coefficients in this *sufficient* condition (not in a necessary condition), the statement "one high-quality sample is never worth more than two low-quality samples" is a property of the specific relaxation, not necessarily of the underlying problem. A tighter analysis could yield γ > 2, which would weaken the central contrast between the agnostic and informed settings that the paper's narrative relies on. The paper provides no bound on this gap — neither a numerical estimate of how far the relaxed bound is from the optimized (cubic-equation) bound, nor a necessary condition giving a lower bound on γ. Without some quantification, the reader cannot assess whether "γ ≤ 2" is a genuine feature of the agnostic recovery problem or an artifact of the proof technique. This limitation is particularly consequential because the paper's main comparative message (γ bounded in agnostic vs. arbitrarily large in informed) depends on the contrast being meaningful.

### Minor

2. **The comparison between the information-theoretic and algorithmic thresholds is structurally asymmetric.** The algorithmic result (Theorem 3) is sharp — both necessary and sufficient conditions are established. The agnostic information-theoretic result (Theorem 1) is only sufficient, and its looseness is acknowledged. The informed information-theoretic result (Theorem 2) optimizes the Chernoff exponent exactly but is also only sufficient (Remark 3.3 notes necessity in the heterogeneous setting remains open). The paper's narrative that the algorithmic threshold is "more robust" to heterogeneity (e.g., "revealing a striking robustness" in the abstract, "seems to be more robust" in the conclusion) compares a sharp algorithmic characterization against a loose sufficient information-theoretic one, so it is unclear whether the claimed robustness is a property of the thresholds themselves or of the asymmetry in tightness. The authors do acknowledge this in the conclusion ("the agnostic information-theoretic condition is sufficient but not proven tight"), but the framing throughout the paper leans on the contrast without adequately flagging this asymmetry to the reader.

3. **Theorem 3 requires n₁, n₂ = ω(s), meaning the high-quality samples alone suffice for support identification.** The LASSO result requires both n₁ and n₂ to scale faster than s, so in particular n₁ > s. This means the high-quality dataset is already large enough to identify the support by itself — the mixed-quality setting is really "enough high-quality data plus extra low-quality data," rather than the more interesting regime where high-quality data alone would be insufficient. The paper does not discuss this limitation or whether the result might extend to the n₁ = o(s) regime.

4. **The Price of Quality γ depends on the error tolerance δ, but this dependence is not explored.** The expressions (12) and (18) for γ both depend on δ, yet the paper treats δ as a fixed constant and does not discuss how γ varies with δ. Since δ is a free parameter, different choices could yield different qualitative behavior of γ. At a minimum, the paper should discuss whether the leading-order scalings (γ → 1, γ → 2, etc.) are independent of δ.

### Trivial

None.

## Nice-to-Haves

- A numerical comparison between the relaxed bound (Theorem 1) and the tighter bound that would come from solving the cubic equation (37) for representative SNR values. This would give readers a sense of how loose the sufficient condition is and whether γ can exceed 2 under the tighter bound.
- A baseline comparison: what happens if the decoder simply ignores low-quality data entirely? The price of quality could be compared against this trivial strategy.
- Simulation results demonstrating that the sufficient conditions are not vacuous and that the LASSO recovery indeed occurs near the predicted thresholds. For a paper with "Price of Quality" claims, numerical illustrations of the trade-off would significantly strengthen practical relevance.
- Discussion of the δ-dependence of γ: whether the qualitative behavior (γ ≤ 2, γ → 1, etc.) is robust to different choices of δ.

## Removed Points

1. **Criticism about Theorem 3 proof being insufficiently substantiated** (Critical Issue 3 from the harsh critic). *Reason for removal*: The paper explicitly states "The full proof of Theorem 3 is given in Appendix D." The appendix was stripped by the PDF parser, as noted at the end of the paper ("Rest of paper (reference and Appendix) is removed"). Per instructions, criticisms about missing appendix content are parser artifacts and must be removed.

2. **Criticism about the paper not defining what "replacing one high-quality sample by γ low-quality samples" means.** *Reason for removal*: This is factually wrong. The paper defines this operationally in lines 91–93: "if (n₁, n₂) verify this condition... then so do (n₁ − 1, n₂ + α₁/α₂)." The Price of Quality is then defined in equations (5) and (12). The paper clearly states the operational meaning.

3. **Criticism that the informed setting threshold is "sharp" while the agnostic one is loose.** *Reason for removal*: The paper states in Remark 3.3 that the informed condition is obtained by optimizing the Chernoff exponent exactly, but also notes "Establishing full necessity in the heterogeneous setting remains an interesting direction for future work." Both results are sufficiency results, not necessary conditions. The harsh critic's framing overstates the contrast.

4. **Criticism about "no comparison to simple baselines" presented as a weakness** — moved to Nice-to-Haves, as it is a suggestion for strengthening the paper rather than a flaw in the presented results.

5. **Various formatting/presentation nitpicks** — removed per instructions.

## Novel Insights

The harsh critic's observation that the γ ≤ 2 bound may be an artifact of the Chernoff relaxation (not a property of the problem) and the asymmetry between the sharp LASSO result and loose information-theoretic condition interact in an interesting way: even if the information-theoretic agnostic bound were tightened, the paper's LASSO result (Theorem 3) would remain unchanged and still show robustness. This means the paper's contribution is more robust than its main critical vulnerability suggests. The LASSO result stands as a genuine advance regardless of what happens to the γ bound under a tighter analysis. Conversely, the strength of the paper's conceptual contribution is tied to whether γ ≤ 2 survives tightening. This creates an unusual situation where the strongest result (Theorem 3) is the least vulnerable to criticism, while the most narratively prominent result (γ ≤ 2) is the most vulnerable. The Strength Finder correctly identified Theorem 3 as the "single most important piece of evidence," and the reviews' focus on the γ bound confirms this asymmetry.

## Suggestions

1. **Quantify the gap between the relaxed sufficient condition and the optimized cubic-equation bound (37).** Even a numerical evaluation for a few representative (σ₁², σ₂², s, δ) values would show how far γ ≤ 2 is from the true bound and whether the qualitative claim survives tightening. This single addition would substantially mitigate the paper's main vulnerability.
2. **Add a discussion explicitly flagging the asymmetry** between the sharp LASSO result and the sufficient-only agnostic information-theoretic result whenever the paper compares their "robustness." The current acknowledgments (Remark 3.2, conclusion) are present but buried.
3. **Discuss the δ-dependence of γ** — even a brief remark that the leading-order asymptotics (γ → 1, γ → 2) are δ-independent would address the concern.
4. **Clarify the n₁, n₂ = ω(s) requirement in Theorem 3** and discuss whether the interesting mixed-quality regime (n₁ small, n₂ large) is covered or whether alternative analysis would be needed.

## Score and Decision

### Round-1 Bracketing

I retrieved anchors in three bands on the topic of "sparse recovery information-theoretic threshold LASSO high-dimensional statistics":
- **Weak band (avg < 3.5)**: Scores 1.67–3.00. Papers with serious motivational gaps, oversimplifications, or unclear contributions. This paper is clearly stronger — it has a well-motivated problem, clean results, and honest limitations.
- **Middle band (3.5–7.5)**: Scores 5.00–7.00. Papers with solid theoretical contributions but some issues in presentation, comparison fairness, or result strength.
- **Strong band (> 7.5)**: Scores 7.75–8.00. Papers with exceptional contributions, thoroughness, or novelty.

**Round-1 bracket: [5.5, 7.5]** — the paper is far stronger than the weak-band anchors but does not match the comprehensiveness and polish of the strong-band anchors.

### Round-2 Narrowing

I retrieved anchors inside the bracket with queries related to heteroscedastic/high-dimensional sparse recovery theory:
- **Inverse Optimal Transport (avg 6.75, Accept Poster)**: Solid theoretical contribution but limited experiments and abstract practical implications. The current paper has a cleaner experimental-free theoretical framing and clearer motivation.
- **Beyond Worst-Case Dim Reduction (avg 6.50, Accept Poster)**: Thorough theoretical work with some novelty concerns and disconnected results. The current paper has a more cohesive single-story narrative.
- **Robust Regression (avg 6.33, Reject)**: Interesting theory but presentation issues and non-rigorous aspects (cavity method). The current paper is more rigorous and better presented.
- **Sketching Regularized LS (avg 6.50, Accept Poster)**: Solid but with questions about incremental novelty and presentation. Comparable in quality to the current paper.
- **Sparse Phase Retrieval (avg 7.00, Accept Poster)**: New algorithm with quadratic convergence and experiments — a stronger all-around package with both theory and experiments.

### Final Score

The paper sits at **6.5**. It is clearly stronger than papers scoring 5 or below (which have significant flaws in motivation or validity), comparable to well-regarded theoretical papers scoring 6–6.5 (solid contributions with acknowledged limitations), but not at the level of 7+ papers which typically combine theoretical depth with experiments or tighter results. The main limitation — the central γ ≤ 2 claim depending on a sufficient condition that may be loose — prevents a higher score, but the LASSO extension (Theorem 3) is genuinely novel and the paper is well-structured, honest about its limitations, and addresses a timely problem.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>