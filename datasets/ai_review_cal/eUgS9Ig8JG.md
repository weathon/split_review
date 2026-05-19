- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6
Now I have all the evidence needed. Let me produce the consolidated review.

## Summary

This paper proposes SaNN, a simplicial neural network that precomputes multi-hop, multi-type neighborhood features (upper, lower, boundary, co-boundary) before training, then feeds these fixed features through MLPs. This decouples the expensive message-passing from learned transformations. The paper provides theoretical conditions under which SaNN matches the simplicial WL test in expressiveness and demonstrates competitive performance across trajectory prediction, simplicial closure, and graph classification tasks with substantially lower per-epoch training cost than existing SNNs.

## Strengths

- **Provably matches the SWL test in expressive power under injective conditions (Theorem 4.2)**: This is the strongest theoretical result. It establishes that a model which precomputes all aggregations before training can still be as expressive as the most powerful known simplicial isomorphism test, despite not interleaving transformations with aggregation. This is non-trivial and meaningfully extends the precomputation idea from the graph domain (SIGN, GAMLP, SPIN) to simplicial complexes.

- **Reduces per-epoch training complexity from quadratic to linear in the number of simplices**: The paper's complexity analysis (Section 3) shows existing SNNs incur O(T(2N_k²D_k + …)) per epoch, while SaNN's per-epoch cost is O(T(3N̂_k D_k² + N_k D_{k-1}² + N_k D_{k+1}²)). This reduction from roughly O(N_k²) to O(N_k) is the core computational contribution. Empirical results (Table 2) confirm SaNN completes training in seconds on datasets where MPSN runs out of memory.

- **Strictly more powerful than the WL test (Theorem 4.1)**: The paper provides a concrete pair of non-isomorphic clique-lifted graphs (Figure 4) that SaNN distinguishes while WL cannot, demonstrating that precomputed co-boundary information (edges, triangles) provides discriminative power beyond WL.

- **Permutation and orientation equivariance**: Property 1 and Section 4.2 prove the aggregation scheme and the full SaNN model are permutation and orientation equivariant, matching the equivariance guarantees of existing SNNs.

- **Systematic ablation studies**: Section 5.2 ablates the effects of features from different depths and different simplex orders, confirming that combining information from multiple hops and multiple orders is empirically beneficial. The discussion of local vs. higher-hop information is informative.

- **Explicit identification of non-injective aggregation pitfalls**: The paper identifies (Section 4.1, Figure 5) that degree-weighted summation is not injective and provides a concrete counterexample, demonstrating careful theoretical analysis of when injectivity is lost.

## Weaknesses

### Fatal
None.

### Major

- **The "constant runtime" claim in the abstract and introduction is contradicted by the paper's own complexity analysis.** The abstract claims "constant run-time and memory requirements independent of the size of the simplicial complex" and the introduction repeats "constant training time and memory requirement (independent of the number of interacting simplices)." However, the complexity formula in Section 3 gives **O(T(3N̂_k D_k² + N_k D_{k-1}² + N_k D_{k+1}²))**, which depends linearly on N_k (the number of k-simplices). The body text more cautiously says the runtime is "almost constant" (Figure 3 caption), but the headline claims in the abstract and introduction are factually inaccurate. *Why this matters*: The "constant" claim is the paper's marquee advertised advantage, and it does not hold even by the authors' own formulas. The real achievement — reducing per-epoch cost from quadratic to linear — is still meaningful and should be stated accurately. This is not a fatal flaw (the linear cost is still a huge improvement over quadratic), but the paper must correct this overstatement throughout.

- **Gap between the theoretical conditions for expressiveness and the architecture used in experiments.** Theorem 4.2 requires that all aggregation functions f_{k,·} be *injective* for SaNN to be as powerful as the SWL test. The example architecture in Section 4.1 uses summation as the aggregator. The paper correctly notes that sum preserves injectivity **only under the restricted setting of uniform scalar features** ("Consider simplicial complexes with the same scalar feature a as initial feature on all the simplices," line 122–124). However, the experiments use real datasets with non-uniform, often high-dimensional features — conditions where sum aggregation is **not** injective (different multisets can yield the same sum). The paper does not acknowledge this gap. Section 4.2 asserts that the example architecture "satisfies the requirements in Theorem 4.2" (line 168) without re-stating the uniform-scalar qualifier, which is misleading. *Why this matters*: The paper's theoretical expressiveness guarantees do not necessarily apply to the model that was empirically evaluated. While this kind of idealized-to-practical gap is common in GNN expressiveness papers, the paper should at minimum discuss the issue and clarify what, if any, expressiveness guarantees hold for the actual experimental setup.

### Minor

- **Figure 3 does not clarify whether precomputation time is included in the runtime measurement.** The caption says "Average run-time of SaNN and MPSN (over 20 experiments of 50 epochs)" and the text refers to "forward pass." The paper separately reports precomputation times in Tables 2 and 3, so the data is available — but Figure 3's "almost constant" empirical claim would be more informative if it were clear whether precomputation is included or excluded. Since precomputation cost grows with the simplicial complex, including it would change the interpretation of the empirical flatness.

- **The proof sketches for Theorems 4.1 and 4.2 are abbreviated to a few sentences each.** The proof of Theorem 4.1 describes one direction ("if SaNN embeddings are equal then WL colors are equal") in a sentence. While full proofs are presumably in the appendix (stripped by the parser), the main text alone does not provide enough reasoning for a reader to verify the claim. The paper would benefit from a more detailed proof outline in the main body.

- **The paper's statistical framing is honest but undercuts the "state-of-the-art" claim.** The paper notes (line 195) that "standard deviations are too high compared to the difference in their means" and that comparisons "are insignificant." This is a transparent acknowledgment, but the abstract claims "state-of-the-art performance," which is not supported by the evidence — SaNN is competitive and sometimes best, but not consistently SOTA. The abstract should be toned down to "competitive performance" or similar.

### Trivial
None.

## Nice-to-Haves

- The paper could report end-to-end wall-clock time (precomputation + total training) for at least one large-scale dataset to clearly demonstrate the break-even point relative to message-passing SNNs.
- A discussion of how (or whether) the injectivity conditions of Theorems 4.1/4.2 can be satisfied for non-uniform, non-scalar features in practice would be valuable.

## Removed Points

- **"Proof sketches are insufficient because the appendix is missing"**: Removed per instructions — the parser strips appendices; they exist in the original submission.
- **"No code, no dataset splits, no hyperparameter settings, no hardware details"**: Removed per instructions as nitpicks about reproducibility that are impractical to fully address in a submission.
- **"Missing baselines (GIN, GCN) for graph classification"**: Removed as scope creep — the paper's contribution is compared against simplicial neural network baselines, which is appropriate for the setting.
- **"Garbled footnotes and LaTeX artifacts"**: Removed per instructions — these are parser errors, not author errors.
- **"Clarify what 'clique-lifted' means"**: Removed as a minor undefined term; moved to minor territory but ultimately not central enough to include.
- **Strength about "constant-time training complexity"** (Strength Finder #2): Removed because the paper's own complexity analysis shows linear (not constant) dependence on N_k, making this strength factually incorrect.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight from the cross-review is the tension between the paper's two central narratives: the computational advantage (decoupling aggregation from learning) and the expressiveness guarantee (matching SWL). The gap between the idealized theoretical conditions (uniform scalar features, injective aggregators) and the practical architecture (sum aggregation on real features) highlights that the paper is advancing two somewhat independent claims — one about efficiency and one about expressiveness — and the evidence for the expressiveness claim does not directly support the empirical architecture. A reader should evaluate the efficiency contribution (real and demonstrated) and the theoretical contribution (valid under stated conditions but not verified for the experimental setup) as separate claims.

## Suggestions

1. **Correct the "constant" claim throughout the paper.** Replace with a precise statement: "per-epoch training cost is linear in the number of simplices (avoiding the quadratic cost of message-passing SNNs)" and clarify that precomputation cost scales with the complex size but is a one-time cost.
2. **Explicitly acknowledge the theory-practice gap.** Add a paragraph discussing that the injectivity conditions required for Theorems 4.1/4.2 are satisfied in the uniform scalar setting, and discuss what guarantees (if any) hold for the non-uniform features used in experiments.
3. **Clarify Figure 3's timing protocol** — state explicitly whether precomputation is included or excluded.
4. **Tone down the abstract's "state-of-the-art" claim** to reflect the paper's own statistical insignificance caveat.
5. **Verify that MLP injectivity is correctly invoked.** The statement "injectivity of multi-layer perceptrons (MLPs)" (line 153) is imprecise — MLPs with non-polynomial activation and sufficient width can be universal approximators, but injectivity requires specific architectural choices (e.g., strictly increasing activations, no pooling layers that collapse distinct inputs).
