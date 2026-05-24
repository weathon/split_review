Confirmed: line 77 correctly uses ρ_s for space, line 141 (Theorem 7) incorrectly uses ρ_q. Now I'll write the consolidated review.

---

## Summary

This paper introduces asymmetric locality-sensitive hashing (LSH) into the LSH-based kernel density estimation (KDE) framework of Charikar et al. (2020). By replacing the symmetric LSH with the asymmetric LSH of Andoni et al. (2017), the authors achieve a substantially improved query time of ≈ 1/μ^0.05 (vs. the prior best ~1/μ^0.173) at the cost of ~1/μ^4.15 space. More broadly, they provide the first space–query tradeoff curve for Gaussian KDE, parameterized by δ ≥ 0, with query exponent ξ(δ) computed via a numerical min-max optimization. Even in the linear-space regime (δ = 0), the query exponent 0.1865 improves the previous non-adaptive bound of 0.25. The paper also offers an analytical explanation of why constant query time appears unreachable under current ANN technology.

## Strengths

- **Significant quantitative improvement over prior art**: The query time drops from ~1/μ^0.173 (Charikar et al. 2020, data-dependent) to ~1/μ^0.05 (Theorem 17), a roughly 3.5× reduction in the exponent. In the linear-space regime, the authors improve the data-independent bound from 0.25 to 0.1865, nearly matching the data-dependent result with a simpler analysis.

- **First space–query tradeoff for KDE**: Theorem 16 gives a tunable family of data structures parameterized by δ. The tradeoff curve (Figure 1, right) shows a continuous spectrum from linear space (query exponent ~0.1865) to a plateau at ~0.05 for space ~1/μ^4.15. This is genuinely new in the KDE literature.

- **Novel technical synthesis**: The core idea—plugging asymmetric LSH into the Charikar et al. level-set recovery framework—is elegant and non-obvious. The asymmetric LSH allows decoupling the space and query exponents for each distance scale, which directly enables the tradeoff. The optimization formulation (Equation 10) that captures intermediate-scale collision overhead is carefully derived.

- **Insightful barrier analysis**: Section 1.2 provides a clear explanation (Equations 6–7) of why constant query time cannot be achieved even with unbounded polynomial space under this framework—the max-over-y term from intermediate distance scales forces a non-zero exponent. This analytical insight points toward necessary new techniques.

- **Clean modular presentation**: The paper faithfully reproduces and generalizes the Charikar et al. reduction (Section 3, Definitions 9–11, Algorithms 1–2), then plugs in the asymmetric LSH (Section 4). The decomposition makes the novelty transparent.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Central technical proof deferred to appendix**: Lemma 31, which formally analyzes how the asymmetric LSH data structure achieves exact recovery of all points in a level set under density constraints, appears only in the (stripped) appendix. While the main text gives a substantive derivation sketch (Equations 6–10, the min-max formulation), a reader cannot fully verify the core claim without the appendix. This is routine for theory papers but limits self-contained assessment. The authors would benefit from including a one-paragraph proof sketch of the key collision-probability expression in Section 4.

- **Numerical rather than analytical optimization**: The final exponents are obtained by numerically solving the min-max problem in Equation (10). The authors acknowledge this honestly, and the numerical results are credible, but an analytical closed form (even for special cases) would strengthen confidence and insight.

### Trivial

- **Typo in Theorem 7**: The space complexity is written as n^{1+ρ_q+o(1)} instead of the intended n^{1+ρ_s+o(1)} (cf. line 77, which correctly uses ρ_s for space). This is a clear notation slip that should be corrected.

- **Ambiguous dimension notation**: The setup states d = Õ(1), which is non-standard. The intended meaning (d = O(log n) or d log n = o(log(1/μ))) should be stated explicitly for clarity.

## Nice-to-Haves

- A brief discussion of whether asymmetric LSH could be combined with data-dependent methods to further reduce the exponent would enrich the related-work and future-work sections.
- Making the collision-probability derivation more self-contained in Section 4 (e.g., stating the two-point collision probability for asymmetric LSH explicitly, sketching the density-constraint union bound) would improve readability without requiring the appendix.
- Explicitly noting that the constants c₀, c₁ (for the "nice" range) contribute only an o(1) term in the exponent would preempt a natural concern about their impact on the final bounds.

## Removed Points

These points were flagged for removal; treat them with caution.

- **"Without a careful verification of [Lemma 31], the claimed improvements cannot be confirmed"** — This is inherent to any theory paper with appendix-deferred proofs. The parser strips the appendix; the original submission contains it. This is not a weakness of the paper as written, merely a limitation of our viewing format. Demoted from potential fatal/major to the Minor observation above.

- **"The precise collision-probability expressions... are not fully spelled out"** — The paper does spell these out: Equation 6 gives the specific form, and the paragraph starting "For any x ∈ [0,1] and a general ρ_q ≥ 0" gives the general expression. The derivation is sketched, not fully formal, but sufficient for a technical overview. Kept only as a minor presentation suggestion.

- **Missing comparison with data-dependent LSH** — The paper does mention the data-dependent bound of 0.173 from Charikar et al. (2020) and notes their result is simpler. A deeper discussion of combining techniques is speculative and outside scope. Moved to Nice-to-Haves.

- **"The influence of the constants c₀, c₁ on the final exponents is not analyzed"** — The paper states these can be made arbitrarily small, which is standard and suffices. Moved to Nice-to-Haves.

- **Criticism about missing related work (random Fourier features, etc.)** — The paper is a worst-case theory paper targeting sublinear-time guarantees. Practical approximate kernel methods address a different setting. Removed as scope mismatch.

- **Strength Finder: "Illustrative visualization of internal scale-dependent behavior"** — Generic. The figure is useful but not a core strength. Removed.

- **Strength Finder: "Modular and rigorous reduction of KDE to a Level-j Recovery problem"** — This is accurate but somewhat generic; merged into the broader strength about clean presentation.

## Novel Insights

The paper's most interesting conceptual contribution is the demonstration that the bottleneck in LSH-based KDE shifts across distance scales when using asymmetric LSH, and that the worst-case scale differs from the one that determines the space bound. This decoupling—visible in Figure 1 (left) through the ξ(δ, x) curves and their relationship to the threshold θ(δ)—is the structural insight that makes the time–space tradeoff possible. Previous symmetric-LSH approaches forced a single ρ for all scales, which is why they could not exploit this phenomenon.

## Suggestions

- Correct the Theorem 7 typo (ρ_q → ρ_s for space).
- Add a one-paragraph proof sketch of Lemma 31's collision-probability bound in Section 4 to make the paper more self-contained.
- Clarify the d = Õ(1) notation by stating the intended asymptotic condition explicitly.
- Consider reporting the analytical form of ξ(δ) for the limiting case δ → ∞ (the plateau region) if one exists, to complement the numerical evaluation.

## Score and Decision

**Calibration anchors compared:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| tra8ktyk0E (Dynamic KDE) | 5.50 | R1 | Our paper has a stronger, more novel theoretical contribution |
| wLnls9LS3x (Kernel M-V Multiplication) | 7.00 | R1 | Our paper's improvement is more dramatic; technique is more novel |
| RsJwmWvE6Q (Optimal Sketching) | 6.75 | R1 | Our paper's contribution is comparably solid but more impactful |
| HMe5CJv9dQ (DP KDE) | 7.50 | R2 | Similar-level contribution; DP paper has experiments, ours has a more dramatic theoretical improvement |
| 49v8meXjHS (kNN Attention) | 6.20 | R2 | Our paper is substantially stronger in both novelty and clarity |
| N4rYbQowE3 (Learning-Augmented Search) | 7.00 | R2 | Comparable level of theoretical contribution |

**Round-1 bracket**: 5.5–8.0, narrowed to 6.5–7.5 after reading anchors.

**Round-2 narrowing**: The paper is clearly stronger than the 6.20 anchor and comparable to or slightly above the 7.00 anchors. It is somewhat below the 7.50 DP KDE anchor, which had broader scope (privacy + KDE + distance queries + experiments + theory) and received three 8s. The paper's core contribution—introducing asymmetric LSH into KDE with a 3.5× exponent improvement—is genuinely novel and well-executed, but the appendix-dependent proof and numerical-only optimization keep it from the top tier.

**Score**: 7.0

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>