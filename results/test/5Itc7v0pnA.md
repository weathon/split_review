Now I have a thorough understanding of the paper and can synthesize the review. Let me produce the final consolidated review.

## Summary

This paper introduces Quantile-Free Regression (QFR), a new loss function for directly learning prediction intervals without first estimating specific quantiles. The key idea is a piecewise quadratic loss based on κ=(y-μ₁)(y-μ₂) that asymptotically achieves α coverage when minimized, and can be augmented with regularization terms (width penalty QFR-W, orthogonality penalty QFR-O) to prioritize narrower intervals or better conditional coverage. The paper provides theoretical coverage guarantees, demonstrates on synthetic data that the added flexibility yields narrower intervals for skewed noise, and shows competitive or superior performance on 9 real-world benchmarks.

## Strengths

- **Novel and well-motivated loss function for direct interval learning.** The QFR loss (Eq. 1) is simple, avoids prespecifying quantiles, and is backed by an asymptotic coverage guarantee (Theorem 3.1). The connection to Vapnik's heuristic — solving the interval problem directly rather than the more general quantile estimation problem — provides a principled motivation. This is a genuine contribution over existing interval construction methods.

- **Flexible regularization framework.** The paper introduces two regularized variants (QFR-W for width, QFR-O for conditional coverage) that give practitioners control over which interval property to optimize. Theoretical bias correction for QFR-W (Theorem 3.3) is provided, and Proposition 3.1 gives convexity conditions for the regularized objective. This flexibility is a clear advantage over standard quantile regression's fixed symmetric quantile protocol.

- **Empirical verification of the core thesis on synthetic data.** Table 2 directly validates the paper's central claim: on skewed (truncated Gaussian) noise, QFR-W achieves MPIW 0.45 vs. 0.62 for QR, while all methods maintain ~90% coverage. On symmetric noise, all methods perform equally — confirming that QFR does not sacrifice quality where the symmetric default is already optimal.

- **Competitive benchmark performance.** Table 3 shows QFR-W achieving the lowest or near-lowest MPIW across multiple UCI datasets (e.g., Boston MPIW 2.97 vs. QR's 3.84) while staying within coverage tolerance. Results are averaged over 20 seeds with standard errors, lending credibility to the empirical claims.

- **Demonstrated gains in conditional coverage.** Table 4 shows QFR-O substantially improves Pearson correlation and HSIC metrics over OQR across most datasets (e.g., Boston: 39.8% improvement in Pearson correlation), using the *same* regularization term — directly isolating the benefit of pairing it with the QFR loss rather than a quantile-based objective.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Unregularized QFR loss is not convex; optimization not discussed.** The QFR loss (Eq. 1) is piecewise quadratic with an indefinite Hessian for individual points. While Proposition 3.1 shows the *regularized* QFR-W is convex under certain conditions, Theorems 3.1–3.2 concern the *unregularized* loss, whose optimization landscape may have multiple local minima. The paper does not discuss initialization strategies, sensitivity to local optima, or whether gradient descent is guaranteed to find a global solution in practice. Given that the empirical results are strong, this is not fatal, but it is a gap the authors should address.

- **Interpretability trade-off not acknowledged.** One strength of quantile regression is that bounds correspond to interpretable quantile statements ("with 95% probability, the value is below q₀.₉₅"). QFR outputs intervals without specifying which quantiles the bounds represent, losing this interpretability. The paper frames QFR as a "direct replacement" for QR but does not acknowledge this trade-off.

- **Theorem 3.2's finite-sample exact coverage claim lacks caveats.** The statement claims the empirical minimizer achieves *exactly* α coverage when α·N is integer, without discussing conditions such as no ties, data positioning, or potential non-uniqueness of the minimizer. Even if the proof (in the appendix) is correct, the body's presentation would benefit from a remark about the conditions under which exact equality holds, or a note that in practice, approximate coverage is what matters. The asymptotic guarantee (Theorem 3.1) is what is needed for the paper's contributions.

- **Notation issues in theorem statements reduce readability.** Theorem 3.1's conclusion includes "α₁–α₂" (presumably a rendering artifact or typo for "α"). Theorem 3.3 includes "α+β–1" where β is undefined in context. While these could be parser artifacts, they appear in the body and undermine reader confidence in the theoretical exposition.

### Trivial

- No discussion of computational cost or training stability differences between QFR's piecewise quadratic loss and QR's piecewise linear pinball loss (e.g., gradient variance, convergence speed).

- The SQR baseline is evaluated using symmetric (0.05, 0.95) intervals per the original protocol, but SQR's flexibility (learning all quantiles) could potentially yield better intervals if non-symmetric pairs were selected. The paper follows the standard protocol, so this is not a flaw, but noting this limitation of the comparison would strengthen the evaluation.

## Nice-to-Haves

- Empirically verify the first-order bias correction from the width penalty (Theorem 3.3: coverage ≈ α–2λ) by sweeping λ and plotting achieved coverage vs. intended coverage for synthetic data.
- Include a supplementary table with coverage and width for all methods on all datasets (including those struck through), so readers can see raw trade-offs.
- Add a brief discussion of when QFR might be expected to perform worse than QR (e.g., near-symmetric noise, very heavy-tailed distributions).

## Removed Points

- **Criticism that Theorem 3.2 is not credible without the proof.** The proof is in the appendix (stripped by the parser). Per guidelines, missing appendix content must not be held against the paper. The substantive concern about missing caveats is retained above as a minor weakness.
- **"Ambiguity in central limitation being addressed" / straw-man framing.** The paper clearly describes the *standard practice* (symmetric quantiles) and offers the alternative of learning many quantiles as option (b). It does not claim QR is *fundamentally incapable* of producing non-symmetric intervals. The critic's complaint misreads the paper's precise language.
- **"Proposition 3.1 condition involves an unusual and incompletely explained quantity."** The condition λ > max(0, ∫ dℙ_Y(y) – α) integrated over the optimization domain bounds is a standard technical condition for convexity proofs. It is adequately explained.
- **Generic/superficial strengths from the Strength Finder** (e.g., "Clear identification of the symmetric-quantile limitation" as a standalone strength — this is motivation, not a technical contribution, and is already covered in the novel method strength).

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments primarily clarify the paper's scope and identify presentation issues rather than adding external insights.

## Suggestions

1. Add a brief discussion of the unregularized loss's optimization landscape (non-convexity, initialization, empirical success).
2. Clean up the notation in Theorem 3.1 and Theorem 3.3 in the camera-ready version.
3. Acknowledge the interpretability trade-off between quantile-based intervals and QFR's direct interval outputs.
4. Include a supplementary table showing coverage and width for all methods on all datasets, even those struck through.

## Score and Decision

The paper makes a genuine contribution: a simple, well-motivated loss for direct interval learning with asymptotic guarantees and strong empirical results across multiple benchmarks. The weaknesses are minor — notation issues, missing discussion of optimization challenges, and an unacknowledged interpretability trade-off — none of which undermine the core claims. I recommend acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>