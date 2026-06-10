Now I have complete verification. Let me write the final consolidated review.

---

## Summary

This paper introduces a framework for analyzing oversquashing in topological (simplicial) message passing by modeling simplicial complexes as relational structures with multiple relation types (boundary, co-boundary, lower/upper adjacency). It extends existing GNN oversquashing results — sensitivity bounds (Lemma 3.2), curvature-based bounds (Proposition 3.4), and depth-dependent exponential decay (Theorem 3.5) — to this relational setting via an aggregated "influence graph." Empirical experiments on TUDatasets and the RingTransfer benchmark demonstrate that rewiring improves performance across graph and topological models.

## Strengths

- **Formal construction of simplicial complexes as relational structures (Section 2.2).** The paper defines a precise mapping from a simplicial complex κ to a relational structure with five explicit relations (identity, binary boundary/co-boundary, ternary lower/upper adjacency) and shows the equivalence of their message-passing schemes. This provides a concrete formalism — including the shift operator tensors — that enables the theoretical analysis that follows. This goes beyond the high-level Hasse-diagram perspective mentioned in prior work (Hajij et al., Eitan et al., Papillon et al.) by making the algebraic structure explicit.

- **Lemma 3.2 — Sensitivity bound for relational message passing.** The paper proves ‖∂hₛ⁽ᵗ⁾/∂hₜ⁽⁰⁾‖₁ ≤ (∏α⁽ˡ⁾β⁽ˡ⁾)(Bᵗ)ₛₜ, where B = γI + Ã is the augmented influence matrix. This cleanly extends the GNN sensitivity results of Topping et al. and Di Giovanni et al. to the setting of multi-relational (including topological) message passing, providing a formal starting point for oversquashing analysis where none previously existed.

- **Theorem 3.5 — Impact of depth on relational message passing.** Extends Di Giovanni et al. (2023, Theorem 4.1) to relational structures, proving that sensitivity can decay exponentially with depth at a rate (2α_max β_max M)ʳ, where r is the combinatorial distance in the influence graph. This provides a formal characterization that connects structural connectivity of the aggregated relational graph to oversquashing in higher-order architectures.

## Weaknesses

### Major

- **The experiments do not directly validate the theoretical claims.** The paper presents three theoretical results (Lemma 3.2, Proposition 3.4, Theorem 3.5) and claims in Sections 3.3 and 3.5 that "We present experimental validation of this result in Section 5.2." However, the RingTransfer experiments (Section 5.2) only test qualitative trends: larger rings → worse performance, larger hidden dimensions → better then worse, rewiring → better. These trends are consistent with many explanations, including well-known effects unrelated to the specific bounds derived. There is no measurement of the Jacobian norms that Lemma 3.2 explicitly bounds, no test of whether the exponential decay predicted by Theorem 3.5 follows the predicted rate, and no comparison of observed sensitivity to the derived bounds. The theory and experiments are essentially disconnected, making the claim of "experimental validation" an overstatement.

- **The rewiring heuristic (Section 4) is critically underspecified.** The paper claims to "propose a rewiring heuristic" for relational structures, defines the collapsed adjacency matrix (Definition 4.1), and then states "Our proposed relational rewiring algorithm is as follows" (line 220) — followed by no description, pseudocode, or explanation of how edges are added, which candidates are considered, or how the rewiring interacts with the multi-relational structure. The experiments (line 237) mention applying "relational rewiring for 40 iterations using three choices for REWIREALGO: SDRF, FoSR, and AFRC," but how these graph rewiring algorithms are adapted to the relational setting is never explained. Even if the algorithm is straightforward (apply graph rewiring to the collapsed adjacency matrix), the paper must state this explicitly, not leave it implied. A claimed contribution of a "rewiring heuristic" cannot be presented without specification.

- **The 75% agreement claim (line 241) is over-interpreted from weak evidence.** The paper states that "for ENZYMES, MUTAG, NCI1, and PROTEINS, in 75% of cases, the best-performing rewiring algorithm for Lif=None and Lif=Clique are the same." With four datasets, 75% means 3 out of 4 — hardly a robust statistical pattern. No significance test is provided. This claim should be presented with appropriate humility or omitted.

### Minor

- **The aggregated influence graph loses the multi-relational structure that distinguishes TDL.** The paper's central analytical device, the influence graph G(S, B), aggregates all five relations (boundary, co-boundary, lower/upper adjacency, identity) into a single weighted directed graph via Ã = ∑_i Ã^{R_i}. Every theoretical result (Lemma 3.2, Proposition 3.4, Theorem 3.5) is then stated in terms of this aggregated graph. The four distinct adjacency types, which have genuine geometric meaning in simplicial complexes, are subsumed into scalar entries. The analysis never identifies an oversquashing phenomenon specific to the multi-relational or simplicial structure that could not be captured by a suitable graph analysis. This limits the depth of insight the framework delivers beyond being a notational generalization.

- **Proposition 3.4's "curvature" framing is misleading.** The bound in Proposition 3.4 simplifies to (∏αβ)[w_T + (2/3)w_F] — purely a weighted sum of triangle and quadrangle counts. The extended Forman curvature terms (wₜᵒᵘᵗ, wₛⁱⁿ) cancel with the extra terms (wₜᵒᵘᵗ + wₛⁱⁿ - 4) appended in the bound. The curvature quantity EFC does not survive in the final simplified expression; the bound depends solely on motif counts. Calling this a "curvature" result misrepresents what is actually a motif-counting bound.

- **The TUDataset benchmarks are a weak testbed for oversquashing analysis.** The datasets used (ENZYMES, IMDB-B, MUTAG, NCI1, PROTEINS) contain small graphs where oversquashing is unlikely to be the dominant performance factor. Additionally, the clique-complex lifting creates very large complexes, making it hard to disentangle oversquashing effects from model capacity and computational burden. The RingTransfer benchmark partially addresses this, but the primary experimental results are on these small datasets.

- **Fixed hyperparameter methodology weakens interpretability.** Using dataset- and model-agnostic hyperparameters (line 237) conflicts with standard practice in TUDataset evaluations, where hyperparameter tuning is routine. The paper references Tori et al. (2024) as justification, but this choice makes it impossible to determine whether observed performance differences reflect genuine oversquashing dynamics or poorly chosen hyperparameters for specific model-dataset combinations.

### Trivial

- **Notation error in the definition of γ (Eq. 7, line 116).** The definition states γ = max_σ ∑_{ξ ∈ S^{n_i-1}} Ã_{σ,ξ}, but Ã is a |S|×|S| matrix, so ξ should be a single entity index, not an element of S^{n_i-1} (a tuple). The subscript n_i is also undefined at that point. The intended meaning (max row sum of Ã) is clear, but the notation is inconsistent.

## Nice-to-Haves

- Derive at least one result that exploits the multi-relational nature of simplicial complexes rather than collapsing all relations. For example, do boundary vs. upper adjacency relations contribute differently to oversquashing?
- Directly measure Jacobian norms or sensitivity on the RingTransfer benchmark to compare against the bounds from Lemma 3.2 and Theorem 3.5.
- Clarify the positioning of this work relative to prior Hasse-diagram perspectives (Hajij et al., Eitan et al., Papillon et al.) — what specifically does the relational structure framing add beyond what can be derived from the augmented Hasse diagram?

## Removed Points

These points were considered but removed per filtering rules:

- **"The proofs are in the appendix which was stripped"** — Removed per policy: parser strips appendix content from all papers; not a valid criticism.
- **"No Related Work section"** — Removed per policy: do not mention missing related work sections.
- **"The paper does not delineate what is new over prior work"** — Partially addressed by the paper's own Remark 2.7, which states the framework "aligns with, and extends" the cited works; the novelty is specifically in the oversquashing analysis, which those works did not address.
- **"Speculative claim about appendix content"** — Removed per policy on not speculating about appendix content.
- **"The graph lifting subsection is empty"** — Likely a parser artifact; removed per formatting artifact policy.
- **Strength: "Empirical evaluation with fixed, dataset-agnostic hyperparameters is more rigorous"** — Removed because it conflicts with a verified weakness (fixed hyperparameters reduce interpretability); per policy, when strength and weakness disagree, weakness wins.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations — that the aggregation collapses the multi-relational structure, that the EFC curvature terms cancel in Proposition 3.4, and that the 75% claim is 3-out-of-4 — are mathematically valid cross-checks but do not constitute new findings about the paper's subject matter.

## Suggestions

1. **Specify the rewiring algorithm completely in the main text.** State explicitly: compute the collapsed adjacency matrix (Definition 4.1), then run graph rewiring algorithm X (e.g., SDRF, FoSR, AFRC) on the resulting graph for T iterations, adding/removing edges according to the algorithm's criterion. Clarify whether rewiring modifies the relational structure or only the collapsed graph.

2. **Bridge the theory-experiment gap.** On the RingTransfer benchmark, compute the Jacobian norm bound from Lemma 3.2 for the models studied and compare with empirically estimated sensitivity. Alternatively, construct a synthetic setting where the bound can be directly measured (e.g., a small simplicial complex with controlled shortest-path distances).

3. **Tone down the "experimental validation" language** for the theoretical results if only qualitative trends are tested, or add experiments that directly probe the quantitative bounds.

4. **Fix the notation for γ** (Eq. 7) — the sum should be over ξ ∈ S, not ξ ∈ S^{n_i-1}.

5. **Present the 75% agreement result with appropriate statistical caution** — explicitly note it is a 3-out-of-4 pattern on four datasets.

6. **Discuss the limitation** that the aggregated influence graph discards the multi-relational specificity of simplicial complexes, and note what kinds of insights this approach can and cannot provide.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>