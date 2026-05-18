Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes a novel approach for formally verifying transformers using polynomial zonotopes—a non-convex set representation that preserves nonlinear dependencies through attention layers exactly, rather than relying on convex relaxations. The key technical contributions are: (1) exact computation of attention-matrix set multiplication via polynomial zonotopes, (2) tunable precision via a single parameter ρ_lim that controls order reduction of higher-order generators, and (3) a direct generalization of prior zonotope-based transformer verification (Bonaert et al., 2021). Experiments on four small classifier models (trained from scratch) across two datasets show verified embedding volumes up to 4.0× larger than the zonotope baseline.

## Strengths

- **Exact preservation of nonlinear dependencies through attention multiplication**: The paper correctly identifies that attention-layer matrix multiplication is the primary source of nonlinear dependency growth in transformers, and shows (Section 3.3, line 194) that "this multiplication of sets is exact using polynomial zonotopes... which is the unique advantage of our approach over related work." This is a genuine technical advance over prior convex-relaxation methods.

- **Tunable precision with a single parameter**: The ρ_lim parameter (Section 3.5, line 249) provides a clean mechanism to trade off tightness vs. runtime by controlling how many higher-order generators are retained after order reduction. Setting ρ_lim=1 recovers interval bounding of higher-order terms, creating a spectrum from cheap/loose to expensive/tight.

- **Scaling beyond brute-force enumeration**: Figure 3a demonstrates a concrete practical advantage—verifying an input with ~2 billion synonym sentences in seconds, which brute-force enumeration cannot handle. This grounds the theoretical contribution in a real problem.

- **Theoretical complexity guarantees**: Lemma 3 and Theorem 1 provide rigorous bounds on generator growth (O(g_X^{3^κ}) before reduction) and overall complexity (O(t h d_V d_model g_max κ)), establishing that the approach is tractable in principle despite the richer set representation.

## Weaknesses

### Fatal
None.

### Major

- **Missing architectural details and absolute metrics impede evaluation**: The paper does not report the architectures of the four models tested—no parameter counts, layer counts, attention head counts, or embedding dimensions (line 260). Without these, readers cannot assess whether the method is being evaluated on nontrivial models or only on trivial ones. Furthermore, Table 2 reports only *normalized* verified volumes (zonotope baseline = 1), without the absolute ε values found by binary search, making it impossible to gauge the practical significance of the improvements. These omissions make the experimental results difficult to interpret or reproduce.

- **Softmax enclosure quality is unanalyzed and could confound results**: The paper states (line 194) that "we only induce outer approximations through the enclosure of the softmax function," but provides no analysis of how tight the softmax enclosure is or how its looseness compounds across multiple transformer blocks. The softmax bounding (Lemma 2) delegates to existing techniques (Bonaert et al., 2021; Wei et al., 2023) with a hand-wavy condition (line 187) that "our method works well as long as the dependencies between dimensions are sufficiently well preserved." Because the softmax is the sole source of approximation, its quality determines the overall tightness. Without isolating softmax error from the exact-multiplication benefit, the source of the reported improvement is ambiguous—it could partly come from softmax bounds rather than the polynomial zonotope multiplication.

### Minor

- **The generalization claim is slightly overstated**: The paper states (line 249) that setting ρ_lim=1 "corresponds to the approach in related work (Bonaert et al., 2021)" and calls the approach a "direct generalization." However, polynomial zonotopes even with ρ_lim=1 still maintain a different structural representation (exponent matrix, linear generators as polynomial generators) than standard zonotopes. The *idea* of interval-bounding higher-order terms is shared, but the representations are not identical. This is a minor imprecision—the paper does not need the representations to be identical, only functionally comparable—but it should be clarified that ρ_lim=1 *approximates* rather than *recovers* the zonotope baseline.

- **No ablation of how ρ_lim and g_max interact with model depth**: The paper asserts (correctly) that generator count grows as O(g_X^{3^κ}) before reduction, but provides no empirical analysis of how the choice of ρ_lim and g_max affects verified volume as the number of transformer blocks κ increases. All four models appear to be shallow (the paper never states κ), so it is unclear whether the method's advantage persists for deeper models or collapses under accumulated approximation.

- **ℓ∞ embedding perturbation vs. synonym coverage not quantified**: Section 1 motivates the problem with synonym substitution, and Section 6 acknowledges that "we cannot guarantee that we capture all synonyms." However, the paper never quantifies the relationship between the tested ε radii and actual synonym coverage. Table 1 lists 96 synonyms for one sentence, but it is not shown that the ε values found by binary search correspond to embedding distances that cover meaningful numbers of synonyms.

### Trivial
None.

## Nice-to-Haves

- An ablation that isolates the benefit of exact multiplication from the softmax enclosure quality (comparing enclosures with identical softmax bounds, varying only the multiplication method).
- A precision-aware sweep showing how verified volume degrades as ρ_lim decreases, on a fixed model and input, to directly support the claim of tunable precision.
- Evaluation on at least one deeper model (e.g., 3–6 blocks) to test whether the dependency-preservation strategy scales.
- Reporting absolute ε values alongside normalized volumes so readers can gauge practical significance.

## Removed Points

- **Criticism about models being "tiny" and "not large language models"**: The paper explicitly acknowledges in Section 6 (line 306) that "all methods are not yet applicable to modern-size large language models." The paper frames its contribution as a step toward that goal, not as a completed solution for production-scale LLMs. The criticism is noted by the authors and does not invalidate the contribution within the stated scope.
- **Criticism that ρ_lim=1 does not recover the exact zonotope method**: The paper uses the word "corresponds to," not "is equivalent to." The reviewer's strict reading is technically correct but the paper's claim is proportionally modest. Moved from Major to Minor above.

## Novel Insights

None beyond the paper's own contributions. The core insight—using polynomial zonotopes to make attention-matrix multiplication exact rather than relaxing it—is clearly the paper's own contribution and is well articulated.

## Suggestions

1. **Add a table describing the four models** (number of transformer blocks, attention heads, embedding dimension, parameter count) to make the experiments interpretable and reproducible.
2. **Report absolute ε values** alongside normalized volumes so readers can assess practical significance.
3. **Include an ablation isolating the softmax enclosure's contribution** to the overall tightness, e.g., by comparing against a variant that uses the same softmax bounding as the baseline.
4. **Add a diagnostic plot** showing how verified volume degrades as ρ_lim decreases on a fixed model, to directly validate the tunable-precision claim.
5. **Clarify the generalization claim**: state explicitly what structural differences remain between polynomial zonotopes with ρ_lim=1 and standard zonotopes, rather than claiming direct equivalence.

## Score and Decision

The paper introduces a genuinely novel technical contribution—using polynomial zonotopes to avoid convex relaxation of attention multiplication—and provides a clean tunable-precision mechanism backed by theoretical complexity guarantees. The core idea is sound and represents a real step forward for transformer verification. However, the experimental validation is substantially thinner than what is needed to support the paper's central claims: architectural details of the evaluated models are absent, only normalized (not absolute) metrics are reported, the softmax enclosure's influence on results is unanalyzed, and all models appear to be very small (the paper never states their depth or size). These omissions prevent the reader from assessing whether the claimed improvements are robust or whether they would survive in deeper, more realistic settings. The paper's transparency about limitations is commendable, but the gap between the contribution's ambition and its empirical support is too large for acceptance at a venue requiring strong experimental validation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>