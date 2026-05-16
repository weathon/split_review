Now I have a thorough understanding of the paper and can evaluate the reviewer claims carefully. Let me produce the final consolidated review.

## Summary

This paper initiates the complexity-theoretic study of training graph neural networks. It proves that training 1-dimensional ReLU-activated GNNs (with SUM, MEAN, or SPECTRAL aggregation and Lp error for p∈[0,1)) is NP-hard, via a reduction from POSITIVE-1-IN-3-SAT using rank-layered decision gadgets and a 6-regular graph construction. The paper also provides algorithmic upper bounds: an exponential-time algorithm for general ReLU-GNNT via branching and ETR solving, and polynomial-time tractability for two restricted settings (edgeless 1D ReLU-GNNs and linearly-activated GNNs with uniform dimensionality).

## Strengths

- **Novel complexity-theoretic result for a timely problem.** The paper tackles the computational complexity of training GNNs, a question that (as the authors correctly note) has not been systematically studied despite extensive empirical work. Establishing NP-hardness for the minimal 1-dimensional setting is a meaningful contribution: it shows the hardness cannot be blamed solely on the dimensionality of classical neural networks.

- **Interesting gadget design exploiting shared weights.** The reduction's rank-based architecture, where each variable is associated with a pair of consecutive layers and the shared weights/biases determine variable assignments, is creative. The observation that weights apply globally (unlike classical NNs where each edge has its own weight) makes the construction non-trivial.

- **Solid algorithmic complements.** Theorem 5 provides the first explicit algorithmic upper bound for ReLU-GNNT, and Theorems 8 and 10 identify tractable special cases (edgeless 1D GNNs → polynomial-time via equivalence to 1D NNT; linear activation with uniform dimensionality → polynomial-time via weight normalization). These help delineate the boundary of hardness.

## Weaknesses

### Major

- **The backward direction of the NP-hardness proof (Theorem 1) contains an unjustified uniformity claim that undermines the reduction's verification.** In the backward direction (lines 158–188), the proof asserts that "for all r∈[d], all vertices in rank r and their adjacent dummy vertices have the same, uniform feature in all layers ℓ<r." This claim is not adequately justified. The argument "as by construction the non-uniform values from rank 0 only propagate by one rank each layer" explains propagation bounds but does **not** establish uniformity across vertices of the same rank — different vertices in the same rank may have different neighborhoods (especially with the K₇-based dummy vertex augmentation) and therefore different feature values under arbitrary unknown weights. The paper's more cautious follow-up statement about "two vertices with isomorphic (r−1)-distance-neighborhoods" is in tension with the sweeping uniformity claim. From this uniform feature value `a`, the paper derives the key equations (1)–(2) that force a satisfying 1-IN-3-SAT assignment. If the uniformity does not hold — specifically, if different labeled vertices (clause check vs. integrity check vs. variable check) have different `a` values because their dummy-vertex neighborhoods differ — the derivation collapses. The paper does not analyze the ranks of the K₇ dummy vertices, their feature propagation patterns, or whether they can break the uniformity among labeled vertices at rank d=2n+1. This is not a minor presentation nitpick — it is a gap in the proof of the paper's central result.

- **The coefficients in the constraint equations (lines 161–188) are not derived from the graph construction.** The equations for the integrity check vertex (2·sum + a + b^(d) = 3), the clause check vertex (sum + 4a + b^(d) = 2), and the variable check vertices (H+6a+b^(d) = 2 or 1) involve coefficients (2, 4, 6, 1) whose relationship to the 6-regular graph structure and the dummy vertex attachments is never explained. Without this derivation, the equations read as asserted rather than proven. Since these equations are the core of the backward direction — they enforce the 1-IN-3-SAT constraint — the gap here compounds the uniformity problem. Both issues must be resolved before the proof can be considered sound.

These two weaknesses together mean the paper's main contribution (Theorem 1) is not established at the required level of rigor. The forward direction (satisfying assignment → weights with error ≤ n) is clearly presented and appears correct. The backward direction, however, has significant gaps.

### Minor

- **The handling of dummy vertices from the K₇ construction is incomplete.** In the forward direction (where specific weights are chosen), the paper correctly argues that dummy vertices do not affect the result because non-positive biases prevent propagation. In the backward direction, the paper asserts (without proof) that dummy vertices "have the same, uniform feature" as their adjacent labeled vertices. The ranks of the K₇ dummy vertices relative to the ranking scheme are not defined, and their potential to carry non-zero features that could differentiate otherwise-identical vertices is not analyzed. A complete proof would need to either (a) assign ranks to dummy vertices and analyze their feature propagation explicitly, or (b) prove that the K₇ augmentation cannot affect the uniformity conclusion.

- **The reduction's bit complexity is not discussed.** For an NP-hardness reduction, the constructed numbers should be polynomially bounded. In this case the numbers are small (0, 1, −1, 2, 3), so this is not actually a problem, but the absence of even a brief note is a minor oversight.

### Trivial

- None (the paper is generally well-written given its technical density; the issues are substantive, not presentational).

## Nice-to-Haves

- A concrete small example (e.g., a 2-variable, 1-clause instance) with the full constructed graph and explicit feature values would greatly help readers verify the reduction.
- Clarifying whether the (★)-marked results have full proofs in an appendix (which the parser may have stripped) would address reviewer concerns about completeness.

## Removed Points

These points are flagged to be removed by the meta-reviewer; treat them with caution.

- *"Lemma 4... its proof is not given"* — Removed per instruction: proofs marked (★) are deferred to the appendix, which was stripped by the parser; they exist in the original submission.
- *"Proposition 7... proof is missing"* — Same as above; removed per instruction.
- *"The paper references a complete graph for an exemplary instance ('Fig.') that is not provided"* — The reference to a figure of a complete example was cut off in parsing ("visualized in Fig."); this is a parser artifact, not an author omission.
- *"The backward direction uses the same variable name a for the uniform feature... and also for a term in the equations"* — This is a notational choice, not a substantive error; the equations consistently use `a` as the uniform feature value.
- *Weakness about missing confidence intervals or standard experimental ML practices* — Not applicable; this is a theoretical complexity paper.

## Novel Insights

The most interesting observation emerging from the reviews — beyond the paper's own claims — is the subtle way in which GNN training hardness differs from classical NN training hardness. The paper's approach (using rank-based propagation with global layer-wise weights) highlights that the crucial difficulty in GNN training is not just the activation function or the aggregation function individually, but their interaction through the graph structure. The fact that the reduction must work with global (layer-shared) weights rather than per-edge weights makes standard NN-hardness techniques inapplicable, which the reviews correctly note as a genuine technical challenge. However, the reviews also surface the concern that this very challenge makes the proof especially susceptible to gaps — the global weight sharing forces the reduction to rely on careful uniformity arguments that are harder to verify than standard SAT-gadget constructions.

## Suggestions

1. **Fix the backward direction of Theorem 1.** Provide a rigorous analysis that: (a) assigns ranks to all vertices including K₇ dummy vertices; (b) proves by induction on ℓ that all vertices in each rank have uniform features in layer ℓ (or explains why this holds despite heterogeneous neighborhoods); (c) derives the coefficients in equations (1)–(2) explicitly from the graph structure and the 6-regular construction. This is the single most important revision.

2. **Add a full analysis of the K₇ dummy vertices.** Show that their features are uniform across copies attached to vertices of the same original degree, and that they cannot differentiate vertices whose features need to be equal for the reduction to work.

3. **Include a small concrete example** in the main text or appendix to illustrate the construction and the feature propagation, making the proof significantly easier to verify.

## Score and Decision

This paper tackles an important and timely question with a creative reduction and useful algorithmic complements. The secondary contributions (Theorems 5, 8, 10) are well-presented and appear sound. However, the core contribution (Theorem 1) is not established with sufficient rigor: the backward direction of the NP-hardness proof contains a significant, unsubstantiated uniformity claim and unexplained coefficients in the constraint equations. Because the paper's central claimed result hinges on this proof, the current exposition is not acceptable for publication. A major revision providing a fully rigorous proof of the backward direction is needed.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>