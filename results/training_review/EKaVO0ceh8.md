Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces Tree-Sliced Wasserstein distance on Systems of Lines (TSW-SL), which replaces the one-dimensional projection lines in Sliced Wasserstein (SW) with tree-structured systems of lines. Each system of k intersecting lines inherits a tree metric, enabling closed-form tree-Wasserstein computation on the projected measures. The paper provides theoretical analysis (injectivity of the generalized Radon transform, metric property of TSW-SL) and experiments across gradient flows, color transfer, GANs, and diffusion models showing consistent improvements over SW and several of its variants.

## Strengths

- **Novel geometric structure for slicing.** Replacing single lines with tree-connected systems of lines (Definition 3.1, Figure 1) is a genuinely new idea that generalizes the projection domain of SW while retaining a closed-form OT solution via the tree metric (Theorem 3.2, Equation 13). This directly addresses the limitation SW faces in capturing topological information from low-dimensional projections.

- **Rigorous theoretical foundations.** Theorem 4.2 proves injectivity of the Radon Transform on Systems of Lines for any continuous splitting map α, and Theorem 5.2 establishes that TSW-SL is a metric on 𝒫(ℝ^d). The theory is carefully developed (definitions of tree systems, their topology, the generalized Radon transform).

- **Closed-form computation with equivalent complexity to SW.** Equation (13) provides a closed-form expression for the tree-Wasserstein distance on a tree system, and the paper shows the overall complexity is O(L k n log n + L k d n) — matching SW when the number of total projection operations is matched. The remark after Equation (13) explicitly addresses this.

- **Proper generalization of Sliced Wasserstein.** The paper explicitly verifies that when k=1, the Radon transform reduces to the classic Radon transform and TSW-SL reduces to standard SW (remark after Theorem 5.2). This provides a clean theoretical unification.

- **Consistent empirical improvements across diverse tasks.** The paper demonstrates TSW-SL outperforming SW across gradient flows (Tables 1–2), color transfer (Figure 5), GANs (Table 3: e.g., CelebA FID 17.6 vs 26.3 with 500 directions), and denoising diffusion models (Table 4).

## Weaknesses

### Fatal
None.

### Major

1. **No uncertainty estimates on any quantitative result.** Tables 1–2 report "average of 10 runs" with no standard deviations. Table 3 reports "average of 3 runs" with no variance. Table 4 reports single numbers with no runs info. Given that the method introduces multiple sources of randomness (sampling tree systems, possibly random α, optimization noise) and that some improvements are small (e.g., Table 4: 11.83 vs 11.98 FID), it is impossible to assess whether the claimed improvements are statistically significant or within the noise of the random process. This is the most serious evidential gap in the paper.

2. **The splitting map α is a free parameter whose effect is completely unstudied.** The paper states α is "either a trainable constant vector or a random vector" (Section 6), with no ablation comparing different choices, no analysis of what values are learned, and no principled guidance for how to set it. Since α determines how each point's mass is distributed across lines in the tree system, it is a fundamental component of the method. Without understanding its role, it is impossible to attribute improvements to the tree structure versus the splitting mechanism. An ablation comparing: (i) uniform constant α, (ii) learned α, and (iii) randomly resampled α, is the minimal requirement.

3. **MaxTSW-SL is introduced in experiments but never formally defined.** The paper contrasts MaxTSW-SL with MaxSW (Tables 1, 3; Figure 5) and claims it "enhances the original MaxSW through optimized tree construction" (Section 6), but the optimization procedure and formal definition of MaxTSW-SL are not provided. The reader cannot tell how this variant differs from TSW-SL or how the maximization is performed.

### Minor

1. **The theoretical guarantees (injectivity, metric property) are established for the population version, but the gap to the empirical estimator is not discussed.** The injectivity in Theorem 4.2 is over the full product space 𝕃_k^d (all possible systems of k lines), while TSW-SL integrates over 𝕋 (the space of chain-like tree systems samplable by Algorithm 1), and the practical algorithm uses L Monte Carlo samples. The paper does not discuss whether the metric property extends to the empirical estimator, nor does it provide consistency results. While this is standard in the SW literature (the population SW is a metric but the empirical estimator only approximates it), the paper should at least acknowledge this gap.

2. **The conversion from continuous projected measures on a tree system to the discrete tree Wasserstein formula is not explained.** The paper states that ℛ^α_ℒ produces discrete projected measures (supports at projections of input points) and then applies Equation (13) using the tree Wasserstein formula from Equation (5). However, Equation (5) requires measures supported on nodes of a discrete tree with explicitly defined edges, edge lengths, and subtree structures. The paper does not describe how the continuous metric tree (copies of ℝ glued at intersection points) is discretized — i.e., how nodes (intersection points, projected support points), edges (segments between consecutive nodes along each line), and subtree masses are constructed. This is a non-trivial algorithmic step that should be documented.

3. **Only chain-like tree systems are considered.** Algorithm 1 produces only chain-like structures (each new line intersects the previous one). The paper does not discuss whether branching tree systems (e.g., a line intersecting multiple existing lines at different points) are possible or would provide additional benefits. This limits the generality of the proposed framework.

4. **No ablation on the tree chain length k.** All experiments use fixed values k ∈ {3, 4, 5} with no study of how performance varies with k. Understanding the sensitivity to this key parameter is important for practical use.

### Trivial

- The paper uses notation inconsistently in a few places (e.g., using both 𝕋 and ℒ to denote the space/set of tree systems; Equation (12) uses index "i=l" instead of "i=1").
- Figure numbers are embedded as image placeholders in the parsed text; the actual figures are not visible in the submission format but are described in captions.

## Nice-to-Haves

- Study the learned α values in the trainable-α configuration to understand how mass is split across lines — does the model learn to concentrate mass on certain lines?
- Compare TSW-SL to SW using the same line sampling distribution (same offsets and directions) but without the tree connection, to isolate the benefit of the tree metric.
- Visualize sampled tree systems in 2D and show the projected measures ℛ^α_ℒ μ on the tree, to help readers understand the geometry.
- Report computation time breakdowns to verify the claimed complexity equivalence in practice.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Injectivity gap characterized as "structural flaw" and "decoupled from the real method."** Removed because this is a standard limitation shared by all sliced methods (the population version is a metric, the empirical estimator approximates it). The paper follows the standard theoretical setup. The point is retained as a minor weakness (see Minor #1) but not a structural flaw.
- **"The distributions are only vaguely specified."** Removed because the paper actually gives concrete examples: μ₁ = 𝒰([-1,1]^d), μ_i = 𝒰([-1,1]) for i>1, θ_i = 𝒰(𝕊^{d-1}). This is specific enough for implementation.
- **"The paper does not verify that the distribution over lines induced by Algorithm 1 with k=1 matches the uniform distribution over 𝕊^{d-1} and over offsets."** Removed because when k=1, the direction is sampled uniformly from the sphere and the offset distribution is irrelevant (1D Wasserstein is translation-invariant). This is a pedantic point that does not affect the validity of the claim.
- **"The definition of TSW-SL depends on... the splitting function α. For simplifying the notation, we omit them" — Claimed as a weakness.** Removed because this is a standard notational convenience; the paper explicitly acknowledges the dependence.
- **"The proof is deferred to the appendix" style complaints.** Removed per guidelines (the parser strips the appendix; it exists in the original submission).
- **Typo/formatting nitpicks.** Removed per guidelines.
- **Criticism that the splitting map "contradicts the stated motivation."** Removed because the stated motivation (replacing lines with tree systems for richer structure) is about the projection domain, not about geometric correspondence of the projection mechanism. The splitting map is a technical component of the generalized Radon transform, not a conceptual contradiction.

## Novel Insights

Beyond the paper's own contributions, the reviews reveal a genuinely interesting question that the paper leaves open: **the role of the splitting map α is a design axis that is not present in standard SW.** In SW, a point's mass goes entirely to its projection onto a single line. In TSW-SL, α distributes the mass across all k lines in the tree system. This introduces a fundamentally new degree of freedom in sliced optimal transport — how to allocate "signal" across projection domains — that warrants standalone theoretical and empirical study. The fact that TSW-SL works even with random or constant α (as the paper's experiments seem to suggest) raises the question of whether the benefit comes primarily from the tree metric (comparing projections across lines in a structured way) rather than from the splitting mechanism. Disentangling these two effects would be a valuable contribution to the field.

## Suggestions

1. **Add error bars to every quantitative result.** Report standard deviations or confidence intervals for all tables, with a minimum of 10 independent runs for gradient flow experiments and 5 runs for generative model experiments.
2. **Add an ablation study on α.** Compare at least three settings: (i) uniform constant α (equal mass split), (ii) learned α (as used in the paper), (iii) random α per tree sample. This will disentangle the benefit of the tree structure from the splitting mechanism.
3. **Formally define and describe MaxTSW-SL.** Clarify how the maximization over tree systems is performed, or rename the method if it simply uses a heuristic construction.
4. **Describe the discretization of the continuous tree system** for computing Equation (13). Provide explicit details on how nodes (intersection points, projected support points), edges, edge lengths, and subtree masses are derived from the continuous tree geometry.
5. **Acknowledge the gap between population and empirical TSW-SL.** Add a brief discussion that the metric property holds for the population version and that the empirical estimator is a consistent approximation (with a citation or brief argument if possible).
6. **Study the sensitivity to k** (tree chain length) with a sweep over k ∈ {1, 2, 3, 4, 5, 6, 8} on a simple task (e.g., 2D gradient flow) to understand how performance scales.

## Score and Decision

On the evaluation axes:
- **Originality:** High. Replacing lines with tree-connected systems is a novel direction.
- **Importance of research question:** Good. Improving sliced Wasserstein distances has broad applicability.
- **Claims supported by evidence:** Partially. The theoretical claims are well-supported, but the empirical claims lack uncertainty quantification and the role of α is not isolated.
- **Soundness of experiments:** Moderate. Breadth is good but the lack of error bars and the underspecified MaxTSW-SL weaken the conclusions.
- **Clarity of writing:** Good overall; the theoretical development is clearly structured, though some algorithmic details are missing.
- **Value to the research community:** Positive. The idea is likely to inspire follow-up work on structured projection domains for sliced OT.

The paper presents a genuinely novel generalization of sliced Wasserstein with solid theoretical foundations and consistent empirical improvements across multiple tasks. However, the experimental evaluation has significant gaps: no uncertainty estimates on any result, the effect of the central splitting map α is completely unstudied, and one variant (MaxTSW-SL) is used but not defined. These are addressable but non-trivial. The paper would benefit from revisions addressing these gaps before final publication.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>