Now I have all the information I need. Let me consolidate my analysis.

## Round-1 Bracket: 5.5 to 7.5

The paper sits clearly above the weak anchors (~2-3) and below the strong pure-theory anchors (8+). Among middle anchors, the closest topical match is the KMV paper (7.0), which also uses LSH-based techniques on Gaussian kernels building on Charikar et al. (2020).

## Round-2 Narrowing

Compared to the KMV anchor at 7.0: Both build on Charikar et al. (2020) with LSH techniques for kernel computation. The current paper has stronger theoretical novelty (first KDE tradeoffs, using asymmetric LSH in a genuinely new way), but no experimental validation. The KMV paper had experiments and more immediate practical motivation. I judge the current paper as comparable — slightly stronger in theoretical contribution, slightly weaker in presentation verification of numerical results.

Compared to DP similarities at 7.5: That paper has broader scope, experiments, and a different angle (privacy). The current paper is narrower but the tradeoff result is clean.

Compared to Dynamic KDE at 5.5: The current paper is significantly stronger in theoretical novelty and contribution.

**Final score: 7.0** — a strong theory paper making a genuine first contribution (the tradeoff curve), with modest but real presentation gaps around numerical verification.

Now I'll write the consolidated review.

---

Actually, let me also reconsider: the harsh critic's point about the numerical optimization not being verifiable from the main text. Let me look at Equation 10 again:

ξ(δ, x) = min_{ρ ≥ ρ_q(δ, x)} max_{y ∈ [x, 1]} (y - x) + (1 - x)(ρ - (x/(y(1-x)^2))((y-x)/√x - (y-1)√ρ)^2)

This is presented in Lemma 15 as the query exponent. Then Theorem 16 defines ξ(δ) = max_{x ∈ [0,1]} ξ(δ, x). The paper states that "using numerical methods" these yield 0.05 and 0.1865. 

The optimization problem is clearly stated. The specific numerical values require solving it. For a theory paper, it's acceptable to report numerically obtained values from a clearly stated optimization problem, as long as the problem is correctly derived. The concern about verification is valid but not fatal — the paper presents the optimization problem, and a reader could verify the values from it.

I'll keep this as a minor weakness.

Now, what about the harsh critic's point about the "nice range" assumption? The paper states (lines 222-230): "we make the assumption that j lies within the nice range [c_0 J, (1-c_1)J] for some small constants c_0, c_1 ∈ (0, 1/2)... In this range, j = O(J) and the size of the dataset is m_j = (1/μ)^{O(1)}. These simplify our calculations, and have little influence since c_0, c_1 are chosen arbitrarily small."

The paper also says on lines 185-187: "Assuming the nice range c_0, c_1 is fixed, for x < c_0, x > 1-c_1 we use the data-structure from Charikar et al. (2020) for the Level-j Recovery problem for these small j's. We provide the formal statement about the guarantee of this data-structure in Appendix B.2."

So the paper does address this — it says extreme scales are handled by a separate data structure from prior work. The claim that the overhead doesn't dominate is justified by c_0, c_1 being arbitrarily small, so the contribution of the ignored scales is o(1) in the exponent. This is standard in the literature. I'd say this is adequately addressed for a conference paper.

I'll keep a softened version of this as a minor point.

Let me write the review now.Now I'll write the consolidated final review.

## Summary

This paper introduces the first query-time vs. space tradeoffs for high-dimensional Gaussian kernel density estimation (KDE). The core idea is to instantiate the density-constrained near-neighbor framework of Charikar et al. (2020) with *asymmetric* locality-sensitive hashing (Andoni et al., 2017), which permits different space and query exponents at each distance scale. The main results are: (1) expected query time ≈ 1/μ^0.05 with space ≈ 1/μ^4.15, significantly improving over the previous best query exponent of 0.173; (2) expected query time ≈ 1/μ^0.1865 with space ≈ 1/μ (linear space), improving the data-independent bound of 0.25 and nearly matching the data-dependent bound of 0.173 with a simpler analysis; and (3) a general tradeoff curve ξ(δ) parameterized by a space exponent δ ≥ 0.

## Strengths

- **First known query-time vs. space tradeoffs for Gaussian KDE.** Theorem 16 and Figure 1 give the first systematic tradeoff curve, parameterized by δ ≥ 0, showing how the query exponent ξ(δ) decreases as the space exponent 1+δ increases. Prior work only had individual points (linear space, fixed query exponent).

- **Significant query-time improvement using polynomial space.** Theorem 17 achieves query exponent ≈ 0.05 with space exponent ≈ 4.15, a clear improvement over the previous best data-dependent exponent of 0.173 (Charikar et al., 2020). The plateau at 0.05 is honestly identified and explained in terms of fundamental ANN constraints.

- **Improved linear-space data-independent bound.** The exponent 0.1865 beats the prior data-independent bound of 0.25 and comes within 0.02 of the data-dependent 0.173, while using a simpler, data-independent construction.

- **Clean incorporation of asymmetric LSH into the density-constrained framework.** The paper provides a principled optimization problem (Equation 10) that derives ξ(δ, x) from the ANN tradeoff (Equation 8) combined with density constraints and the subsampling framework. The analysis shows exactly where the improvement over symmetric LSH comes from.

- **Honest discussion of limitations.** Section 1.2 explicitly explains why constant query time is not possible with current ANN technology, describes the plateau effect, and positions the results honestly relative to Charikar et al. (2020).


## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Numerical exponents lack verification from the main text.** The headline values 0.05 and 0.1865 are obtained by solving the optimization problem in Equation 10 "using numerical methods," but no details of the numerical procedure, error bounds, or a reproducibility protocol are presented. While the optimization problem itself is clearly stated, a reader cannot verify the claimed exponents from the paper alone. The paper would be strengthened by including a table of exponents for representative δ values (e.g., δ = 0, 1, 2, 3, 4) and a brief description of the numerical method used.

- **Handling of extreme distance scales is asserted but not justified.** The analysis restricts to the "nice range" j ∈ [c₀J, (1−c₁)J] and defers extreme scales (x near 0 or 1) to a separate data-structure from Charikar et al. (2020). The paper states that c₀, c₁ can be "chosen arbitrarily small" and that the overhead "has little influence," but does not provide a formal argument that the contribution of extreme scales is o(1) in the exponent. A few sentences making this reasoning explicit would close the gap.

- **Definition 10 contains garbled formulas** — the sampling rate appears as min(1/2^{J+n}, 1) and the expected size as 1/(2^J μ), neither of which is consistent with the earlier Equation 3 or the surrounding prose. The intended meaning is clear from context (p_j = (1/μ)^{1−x_j}·1/n), but the formal definition as printed in the extracted text is incorrect and must be corrected. (Acknowledged as a likely parser artifact.)

### Trivial

None.


## Nice-to-Haves

- A small-scale synthetic verification of the exponents (e.g., simulating the query time scaling for synthetic datasets) would increase confidence in the numerical optimization, though this is not standard for a purely theoretical paper.
- A brief remark on how the o(1) terms in the ANN data-structure (polynomial in d, log n, 1/ε) interact with the asymptotic exponents would help readers assess practical relevance.


## Removed Points

- **No experimental verification** — removed because experimental validation is not required for theoretical contributions; the paper is purely analytical.
- **Constant factors in Õ notation not discussed** — removed because this is standard in the sublinear-KDE literature; the paper follows the conventions of Charikar et al. (2020).
- **High-dimensional assumptions (d = Õ(1))** — removed because this is the standard regime in the literature and is stated explicitly (Definition 5).
- **Success probability not fully explained** — removed because the paper states 0.9 overall success probability and describes K repetitions; the logic is standard and adequately conveyed.
- **Missing related works** — removed as per policy (cannot verify without external sources).
- Strengths about the "importance of the problem" or "novelty" that were generic without concrete evidence have been merged into the specific strengths above.


## Novel Insights

None beyond the paper's own contributions.

The key insight — that the KDE query-time bottleneck arises from a different distance scale than the space bottleneck, and that asymmetric LSH can exploit this misalignment — is clearly articulated in the paper itself. The review process did not surface additional insights beyond what the authors already present.

## Suggestions

1. **Correct Definition 10** to match the intended formula p_j = (1/μ)^{1−x_j}/n and the corresponding expected size m_j = (1/μ)^{1−x_j}.
2. **Add a table** of numerical values of ξ(δ) for a few representative δ values (e.g., δ = 0, 1, 2, 3, 4, ∞) so readers can see the tradeoff curve numerically without relying on Figure 1 alone.
3. **Include a brief justification** (1–2 sentences) that extreme scales (x near 0 and 1) contribute o(1) to the exponent: since c₀, c₁ → 0, the measure of the excluded interval goes to 0, and the pointwise query exponents ξ(δ, x) are bounded, so the max over [0,1] is unaffected.
4. **Briefly describe the numerical optimization method** (e.g., grid search, gradient descent on the min-max) to give readers confidence that the reported values are genuine optima.


## Score and Decision

**Calibration anchors used:**

| Anchor path | Avg Score | Round | Comparison |
|---|---|---|---|
| wLnls9LS3x (KMV paper) | 7.00 | R1 | Similar theory paper using LSH for Gaussian kernel computation; the current paper has stronger theoretical novelty but no experiments |
| tra8ktyk0E (Dynamic KDE) | 5.50 | R1 | Weaker paper on a related KDE topic; current paper is significantly stronger in theoretical contribution |
| N4rYbQowE3 (Learning-Augmented Search) | 7.00 | R1 | Comparable-scored data structure theory paper; similar level of rigor and contribution |
| HMe5CJv9dQ (DP similarities) | 7.50 | R2 | Stronger paper with broader scope (privacy + theory + experiments); current paper is slightly narrower |
| 6tqgL8VluV (Learned DB operations) | 6.00 | R1 | Lower-scored theory paper; current paper is stronger |
| oY2jw2NLiM (Coresets for k-means) | 3.00 | R1 | Weak anchor, not relevant to topic |
| fMTPkDEhLQ (Lower bounds) | 8.00 | R1 | Strong theory anchor at the high end |

**Round-1 bracket:** 5.5–7.5  
**Round-2 narrowing:** The paper is comparable to the KMV paper at 7.0 and slightly below the DP similarities paper at 7.5. It is clearly stronger than the dynamic KDE paper at 5.5 and the learned databases paper at 6.0.

**Final score:** 7.0  
**Final decision:** Accept

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>