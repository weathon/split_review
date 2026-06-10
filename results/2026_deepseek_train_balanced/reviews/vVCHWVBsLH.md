## Summary
This paper introduces "decomposition polyhedra," a novel geometric framework for studying the decomposition of continuous piecewise-linear (CPWL) functions into differences of convex CPWL functions (DC decompositions). By fixing a regular polyhedral complex, the set of compatible decompositions is shown to form a polyhedron arising as the intersection of two shifted cones. The paper proves that reduced decompositions correspond to bounded faces, minimal decompositions must be vertices, and identifies function classes (hyperplane functions, order statistics) with unique minimal decompositions. Applications include disproving a recent higher-dimensional construction claim, connections to submodular functions, and a depth-width tradeoff for neural network representations of convex CPWL functions.

## Strengths
1. **Novel geometric framework (Theorem 1):** The decomposition polyhedron — the set of DC decompositions compatible with a fixed polyhedral complex — is proven to be a polyhedron arising as the intersection of two shifted copies of the cone V⁺_P. This converts an open-ended search problem into a concrete polyhedral geometry question, providing a genuinely new structural lens on DC decompositions.

2. **Clean characterization of reduced and minimal decompositions (Theorems 2, 4):** Reduced decompositions correspond exactly to bounded faces of the decomposition polyhedron (Theorem 2), and minimal decompositions must be vertices (Theorem 4). These are non-trivial geometric characterizations that link combinatorial optimality notions to well-defined polyhedral properties.

3. **Sufficient condition for unique minimal decompositions (Proposition 10, lines 261–264):** The support-based certificate is a clean criterion that identifies important function classes — hyperplane functions (which subsume 1-hidden-layer ReLU networks) and order statistics (including the median) — as having unique minimal decompositions with at most as many pieces as the original function. This is a concrete positive result.

4. **Disproof of Tran et al.'s higher-dimensional claim:** The paper provides a counterexample showing that a recently proposed construction for minimal DC decompositions does not generalize beyond dimension 2. This is a meaningful negative result that clarifies the state of the art and is explicitly acknowledged as such.

5. **Depth-width tradeoff for convex CPWL neural networks (Theorem 7, lines 386–388):** By blending two existing incomparable constructions via a free parameter (r,s), the paper enables interpolation between low-depth/high-size and low-size/higher-depth representations of convex CPWL functions. The extremes recover the previously known bounds from Hertrich et al. (2021) and Chen et al. (2022), and no prior work offered this continuous tradeoff.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **The Pareto notion of minimality is stated without motivation or comparison to alternatives:** Definition 4 defines minimality as Pareto-optimality over the pair (pieces(g), pieces(h)). The paper does not discuss why this specific notion is preferred over alternatives such as minimizing pieces(g)+pieces(h), max(pieces(g), pieces(h)), or the total number of linear regions of g+h. Under the Pareto definition, (10,10) and (5,100) can both be "minimal" even though the latter is clearly worse under any aggregate measure. The paper's central characterization (minimal ⇒ vertex) holds for this specific definition, and it is unclear whether analogous results would hold for more aggregated notions. A brief justification would strengthen the framing, especially since the paper positions minimality as a key concept.

2. **The "finite procedure" language overstates the algorithmic implication:** The paper states (line 252) that enumerating vertices of the decomposition polyhedron provides a "simple finite procedure" to find a minimal decomposition. However: (a) no bound on the number of vertices is given, (b) the polyhedron lives in WP × WP whose dimension equals the number of codimension-1 faces of P (potentially large), and (c) vertex enumeration is #P-hard in general. The paper does not discuss these practical limitations. The theoretical finiteness claim is correct, but "simple" is misleading without any complexity discussion. The paper's own limitations section (line 38) says implementation is beyond scope, which partially mitigates this but does not address the overstatement.

3. **The submodular functions section is sketchy and lacks new domain-specific results:** Section 5 translates the general framework to submodular functions via the Lovász extension isomorphism, but the only concrete example given (cut functions) is already covered by the hyperplane function case. The "informal" corollary (line 347) is an unusual label for a theoretical paper, and the section does not prove any new results specific to submodularity — e.g., bounds on the base polytope or connections to known submodular analysis beyond the Lovász extension. This reads more as a brief pointer to future work than a substantive application.

4. **The nonconvex neural network extension (Corollary 8) is conditional on solving the core open problem:** The extension to nonconvex CPWL functions requires both (a) compatibility with a regular polyhedral complex (a nontrivial restriction) and (b) a good decomposition being available — Problem 1, which the paper's own open problems section identifies as wide open. The paper is honest about this, but as a result the nonconvex contribution is essentially a conditional statement and a direction for future work rather than a concrete result.

### Trivial
None.

## Nice-to-Haves
- A structural sketch of the counterexample to Tran et al. in the main text would strengthen the paper's most prominent negative claim, even if full details remain in the appendix.
- An explicit worked example demonstrating the decomposition polyhedron, its vertices, and which vertices correspond to minimal decompositions for a small concrete function would help illustrate the framework's utility.
- A brief discussion of the computational complexity of constructing the decomposition polyhedron and computing its vertices would provide useful context for the "finite procedure" claim.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **Harsh critic's Point 1 (Counterexample in appendix — cannot evaluate from main text):** The criticism that the counterexample to Tran et al. is described only in the appendix and "cannot be evaluated from the main text." **Removed per rule:** "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections from all papers; they exist in the original submission." The main text (lines 306–312) describes the failure mechanism (the gluing step is not well-defined), and the full counterexample exists in the appendix of the original submission. This is a presentation/structure preference, not a flaw in the paper's content.

2. **Harsh critic's Point 4 (Neural network contribution is incremental):** The claim that the convex construction "blends two existing constructions" and is therefore incremental, and that the nonconvex extension is conditional. **Removed:** The paper explicitly frames this as interpolation between two incomparable prior results, which is a valid contribution — the parameter (r,s) tradeoff did not exist before. The nonconvex section is honestly scoped as conditional. Neither is a weakness; both are accurately described contributions.

## Novel Insights
None beyond the paper's own contributions. The paper's framing — that fixing a polyhedral complex turns the decomposition problem into a tractable polyhedral geometry question, with vertices corresponding to minimal decompositions — is itself the key insight. The reviews do not surface additional novel observations beyond what the paper already provides.

## Suggestions
1. **Motivate the Pareto notion of minimality:** Add a brief discussion explaining why Pareto-optimality over (pieces(g), pieces(h)) is the natural definition for DC programming and neural network applications. This would address the concern without requiring changes to the mathematics.
2. **Tone down or qualify the "simple finite procedure" language (line 252):** Replace "simple finite procedure" with "theoretically finite procedure" or add a caveat that vertex enumeration can be computationally expensive in practice.
3. **Expand the submodular section with one nontrivial example or result** that does not follow immediately from the general theory, to make it a genuine application rather than a translation exercise.
4. **Add a structural sketch of the counterexample in the main text** to give readers intuition for why the gluing step fails, even if the full technical details remain in the appendix.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>