Now let me write the final review.

## Summary

This paper studies the computational complexity of computing the positive non-clashing teaching dimension for concept classes represented as balls in a graph. It delivers four contributions: (1) NP-hardness of STRICT NON-CLASH even when the teaching dimension is k=2 (settling an open question from Chalopin et al. 2024), (2) near-tight exponential running-time bounds with only a logarithmic gap between lower and upper bounds, (3) fixed-parameter tractability of NON-CLASH when parameterized by vertex integrity (significantly extending prior work that only handled the more restrictive vertex cover parameter), and (4) a W[1]-hardness result that rules out FPT for feedback vertex number and pathwidth, even when combined with k.

## Strengths

1. **Settling the open question of NP-hardness for constant teaching dimension (k=2).** Theorem 1 proves STRICT NON-CLASH is NP-hard even when k=2 via a reduction from 3-SAT to split graphs of diameter 2. This is tight since k=1 is trivially solvable (testing whether G is edgeless), directly answering the first open question of Chalopin et al. (2024). The reduction is carefully described in the body with a schematic figure (lines 68–84), and the correctness is stated via Lemma 2 and Lemma 3.

2. **Pushing tractability from vertex cover to the less restrictive vertex integrity parameter.** Theorem 17 establishes FPT for NON-CLASH (the more general non-strict setting) parameterized by vertex integrity, whereas prior work only handled the more restrictive vertex cover number. The proof introduces novel technical machinery — blueprints (Definition 2), compact teaching maps (Definition 7), twin-block equivalence (Definition 1), and a kernelization that reduces the instance to size bounded by a function of the parameter alone — representing substantial intellectual work. The proof progression through Lemmas 7–16 is clearly laid out.

3. **Near-tight running time bounds.** The lower bound 2^{o(|V(G)|·d·k)} (Theorem 4, under ETH) and upper bound 2^{O(|V(G)|·d·k·log|V(G)|)} (Proposition 5) improve significantly over the prior bounds of 2^{o(n·d)} and 2^{O(n²·d)} from Chalopin et al. (2024) and leave only a logarithmic gap in the exponent.

4. **W[1]-hardness delineating the boundary of tractability.** Theorem 18 proves NON-CLASH is W[1]-hard parameterized by feedback vertex number + pathwidth + k, thereby ruling out FPT for treewidth and clique-width as well. This provides a meaningful lower bound matching the FPT result and explicitly addresses the open question about alternative parameterizations.

5. **Constructive FPT algorithm.** The FPT algorithm (Theorem 17) is constructive — it outputs a witness set of teaching examples — and Lemma 16 explicitly shows how to lift a compact solution from the reduced instance back to the original instance with a running time of 2^{2^{O(p³)}}·|V(G)|^{O(1)}.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The "near-tight" bounds claim spans two problem variants without explicit bundling.** Theorem 4 states the lower bound for STRICT NON-CLASH, while Proposition 5 states the upper bound for the more general NON-CLASH. Although the bounds transfer in both directions by restriction (STRICT NON-CLASH ⊆ NON-CLASH, so the lower bound applies to NON-CLASH and the upper bound applies to STRICT NON-CLASH), the paper does not explicitly note this. A concise clarifying sentence would eliminate any ambiguity.

2. **The W[1]-hardness source problem NAE-INTEGER-3-SAT is used without motivation.** The reduction in Section 5 invokes NAE-INTEGER-3-SAT (Bringmann et al., 2016) as the source problem. While the construction naturally requires integer-valued variable assignments to match the distance-based ball structure, the paper does not explain why this particular problem is the natural choice. A brief justification would improve readability.

### Trivial
1. Line 168 contains a garbled formula ("f(p) = c(p) + p·cs((pp))+p b(p) + twin-blocks") — clearly a parser artifact; the original submission would benefit from proofreading this passage.

## Nice-to-Haves
- The paper could add a short intuitive explanation of why vertex integrity enables tractability while feedback vertex number and pathwidth do not. For instance: "Vertex integrity bounds both the separator size and each component's size, enabling the twin-block decomposition and kernelization; feedback vertex number and pathwidth bound only global graph structure, leaving enough room for the W[1]-hardness construction to embed arbitrary variable assignments."
- A brief sketch of Lemma 14's proof (preserving ball structure in induced subgraphs) in the body would improve readability, though its presence in the appendix is standard.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **Harsh critic: "NP-hardness reduction's correctness proof is in the appendix, so the body lacks reasoning about the strict setting."** The proofs of Lemmas 2 and 3 are stated in the body; full proofs are naturally deferred to the appendix. Per the hard rule: the parser strips appendix content from all papers — these proofs exist in the original submission. This is standard practice for theory papers at top venues. REMOVED.

2. **Harsh critic: "Pathwidth bound argument in Theorem 18 is imprecise because pathwidth does not decompose additively across components."** The critic's objection reflects a misunderstanding. The paper is not decomposing pathwidth additively across components. It uses the standard fact (stated in Section 2, line 54) that deleting t vertices reduces pathwidth by at most t. After deleting 3|𝒳| vertices and one additional vertex per component, the remaining graph is a disjoint union of subdivided caterpillars, which has pathwidth 2. The reasoning (line 204) is standard and correct. REMOVED.

3. **Harsh critic's "Strengthening the Paper on Its Own Terms" section.** These are general suggestions (e.g., "stronger treatment of pathwidth bound," "intuitive explanation of vertex integrity"). The critic's specific pathwidth concern is removed above; the remaining suggestions are captured in Nice-to-Haves. REMOVED from weaknesses.

4. **Strength Finder's generic-sounding claims.** All five identified strengths are concrete, specific, and grounded in specific theorems, definitions, and lemmas visible in the paper. None are generic, superficial, or sycophantic. RETAINED.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- In the introduction or after Theorem 4/Proposition 5, add one sentence clarifying that the lower bound (Theorem 4, for STRICT NON-CLASH) applies to NON-CLASH by restriction, and the upper bound (Proposition 5, for NON-CLASH) applies to STRICT NON-CLASH similarly, so the "near-tight" claim is valid for both settings.
- Add a brief justification for the choice of NAE-INTEGER-3-SAT as the source problem in Section 5, explaining that its integer-valued assignments map naturally to distance-based ball inclusions in the constructed graph.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>