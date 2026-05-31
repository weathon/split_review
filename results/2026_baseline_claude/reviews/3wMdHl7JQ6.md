## Summary

The paper proposes a simplified spectral algorithm for community detection in the two-community stochastic block model (SBM) under constant edge density. The key claims are: (1) the degree-based deletion preprocessing step (zeroing rows/columns with high degree) can be removed without harming the spectral norm bound; and (2) the full algorithm's Correction step is unnecessary—Spectral Partition alone achieves the inverse-log error rate (Theorem 1.3) that previously required the Correction step. The authors support these claims via Chernoff-based analysis, normal approximations, and empirical experiments on graphs with n ∈ {500, …, 1000}.

## Strengths

- **Genuine technical contribution on Theorem 2.2**: The argument that the spectral norm bound ‖M‖ ≤ C₂√(a+b) holds for the full matrix A without the deletion step is technically sound. The use of Füredi & Komlos (1981) and Krivelevich & Vu (2000) to handle non-uniform variances is appropriate, and this result is a clean improvement over the original.
- **Interesting theoretical observation about Theorem 3.2**: The paper correctly identifies that the quadratic bound γ ≤ C sin²θ is not tight for vectors produced by the spectral algorithm, even though it is tight in the worst case over all unit vectors. The optimization argument in Section 3.2 cleanly separates the worst-case from the algorithm-specific case.
- **Multi-faceted analysis**: The paper employs Chernoff bounds, a normal approximation, and Monte Carlo simulation as complementary tools to characterize the eigenvector entry distribution, showing consistency across methods.

## Weaknesses

### Fatal
- **The central theoretical claim (that Spectral Partition alone achieves Theorem 1.3) is not proven.** Section 4 fits the empirical relationship sin θ = C/(log 2/γ)^{1/3} (Eq. 13) via OLS regression to experimental data, then asserts this functional form "directly yields the final result stated in Theorem 1.3." This is not a proof—it is circular: using experimental observations to claim a theorem. There is no theoretical derivation of Eq. 13; it is entirely data-driven. A theorem of the form claimed in Theorem 1.3 requires a rigorous probabilistic argument bounding γ in terms of (a−b)²/(a+b), not an empirically-fitted curve.

### Major
- **The theoretical analysis chain contains unresolved gaps.** Section 3.4 derives Chernoff constraints assuming the eigenvector entries follow the distribution of Au₂/(a−b), relying on the approximation ‖w₂ − Au₂/(a−b)‖∞ = o(1/√n) from Abbe et al. (2019). However, the paper does not show that this ∞-norm approximation error is small enough to preserve the derived Chernoff constraints when substituting v₂ (the output of the algorithm) for Au₂. The O(1/√n) error is applied to constrain the rank ordering of entries, and its effect on the optimization problem is not analyzed.

- **The normal approximation in Section 3.5 is acknowledged to be invalid and is rescued by OLS.** The paper explicitly states that the "unit variance assumption is not" valid, then corrects for this by fitting a scaling factor via OLS. This means Eq. 12 does not constitute a closed-form bound—it is a heuristic fit. Presenting it as a "theoretical prediction" while acknowledging a foundational assumption fails is misleading.

- **Experiments are conducted in an easy, far-from-threshold regime.** All experiments use a = 0.06n and b = 0.04n, giving (a−b)²/(a+b) = 0.004n, which grows linearly with n. For n = 500, this equals 2, and for n = 1000 it equals 4—far above the threshold where the algorithm faces any difficulty. In this regime, both the Correction step and the deletion preprocessing are nearly irrelevant because the SNR is so large. The near-threshold regime—where claims of information-theoretic optimality are most meaningful—is never probed, making the experiments insufficient to substantiate the paper's claims.

### Minor
- The relationship γ ≤ (4/3) sin²θ used in Section 3 is stated to follow from Chin et al. (2015) but no derivation or proof is provided in the paper. This is the pivotal link between subspace angles and error rates, and its precise form matters for the quantitative claims.
- The optimization framework in Section 3.4 produces Chernoff-derived bounds that are looser than the Monte Carlo simulation results, as the paper itself notes. The paper does not explain why the Chernoff bounds are loose here, which undermines confidence in their tightness.

### Trivial
- The legend in Figure 4 inconsistently labels "Chernoff-optimizer" vs. "Chernoff-optimized" across the two subplots.

## Nice-to-Haves
- A proof attempt (even a sketch) of Eq. 13 from first principles, rather than empirical fitting, would substantially strengthen the paper's main claim.
- Experiments varying (a−b)²/(a+b) near the information-theoretic threshold (Eq. 2) would demonstrate whether the Correction step is truly unnecessary in the hard regime, not just the easy one.
- A comparison of runtime between the simplified and original algorithms to substantiate claims of computational efficiency.

## Novel Insights

The observation that Theorem 3.2 is not tight for eigenvectors produced by the spectral algorithm—despite being tight in the worst case—is a genuinely interesting structural insight. The paper correctly argues that the spectral algorithm imposes distributional regularity on eigenvector entries (via the connection w₂ ≈ Au₂/(a−b)) that the generic bound ignores. This suggests that average-case analyses of spectral algorithms can yield substantially tighter bounds than worst-case analyses. However, this insight is not developed into a complete proof, which is the paper's central unresolved weakness.

## Suggestions
- Replace the OLS-fitted Eq. 13 with a rigorous derivation that bounds sin θ as a function of γ from the Chernoff constraints established in Section 3.4, even if this requires stronger assumptions on a and b.
- Conduct experiments at fixed n (e.g., n = 10,000) while varying (a−b)²/(a+b) from near-threshold to well above threshold to show the algorithm's behavior as SNR approaches the lower bound in Eq. 2.
- Clarify whether Eq. 11 is a proved upper bound or a heuristic approximation—the current framing is ambiguous.
- Consider framing the paper's contribution more precisely: the removal of the deletion step with a proof (Theorem 2.2) is a clean, rigorous result; the empirical observation that Correction appears unnecessary is an interesting conjecture worth highlighting as such.

## Score and Decision

The paper identifies a genuinely interesting structural property of spectral community detection algorithms and provides a clean improvement of one auxiliary bound (Theorem 2.2 without deletion). However, the central claimed contribution—a rigorous proof that Spectral Partition alone achieves the information-theoretic inverse-log error rate—is not delivered. The key result (Eq. 13) is empirically fitted via OLS and not theoretically derived, and the experiments are confined to a regime far from the information-theoretic threshold where the claim would be most significant. For a venue expecting theoretical rigor, this is a fundamental shortcoming, not a minor gap.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>