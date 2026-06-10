## Summary

The paper proposes WL-trees — rooted trees derived from BFS on a graph with node IDs dropped — as a new algorithmic model for analyzing message-passing GNNs. The central claim is that WL-trees are equivalent to 1-WL node colors (Theorem 5) but provide a more intuitive, structural representation. Additional contributions include an algorithm to recover anchored subgraphs compatible with a given WL-tree (Section 4.3) and an analysis of two enhanced GNN variants (CLIP-2 and NGNN) through the WL-tree lens.

## Strengths

- **The WL-tree concept offers a potentially useful structural perspective on the information encoded by 1-WL colors.** Representing the content of a 1-WL color as an explicit tree with color-labeled nodes makes the neighborhood structure that a GNN "sees" more directly tangible than the hashed color representation. The paper clearly distinguishes WL-trees from prior roll-out trees by excluding the parent from children (line 127), which is a deliberate and consequential design choice.

- **The three-layer error categorization for node classification (Section 6, Discussion, lines 286) provides a clean conceptual framework.** The decomposition into (1) same anchored subgraph → different labels, (2) same WL-tree → different anchored subgraphs (the 1-WL indistinguishability problem), and (3) distinguishable by WL-trees but not by the GNN (over-smoothing/over-squashing) is genuinely insightful and directly links WL-trees to practical failure modes.

- **Condition 1 (lines 205–211) for recovering anchored graphs from a WL-tree addresses a natural and non-trivial question** — what graph structures are compatible with a given (WL-tree / 1-WL color) profile? The subtree isomorphism constraints are a reasonable formalization, and the idea of enumerating compatible graphs has clear diagnostic value for understanding what information message-passing loses.

## Weaknesses

### Major

- **No proofs are provided for any of the six theorems or two lemmas.** Theorems 5, 6, 10, 11, 12, and 13 are all stated without proof or even a sketch of a proof. Lemma 2 and Lemma 4 likewise receive no justification. For a paper whose main contribution is positioned as a *theoretical* analytical tool, this is a critical gap. Most concerning is Theorem 5 — the central claim that WL-trees are in bijection with 1-WL colors — which receives only a brief informal argument (lines 149–151). The sketch does not address how the depth alignment works between the WL-tree's multi-level color retention and the 1-WL's recurrent hashing, why the parent-exclusion design preserves the bijection, or why the mapping is bijective rather than merely surjective. The paper's entire framework rests on this theorem, and it is unsubstantiated.

- **The empirical evaluation (Section 6, Tables 1–4) is too weak to support the paper's claims about WL-trees' utility.** The tables are embedded as images with unreadable numeric values; the surrounding text reports only qualitative trends. No standard deviations, variance estimates, or per-node statistics are reported. The datasets are oddly chosen for an expressiveness analysis: MUTAG (188 graphs) is tiny; Road-MN and CiteSeer are single-graph transductive settings with all node colors set to 0 — stripping away the feature information that drives expressiveness comparisons. Standard expressiveness benchmarks (EXP, BREC, or synthetic iso/auto-regressive tests) are absent. Most critically, the paper interprets small conditional entropy $\mathbb{H}[S_i^\ell|T_i^\ell]$ as evidence that "a GNN has the ability to differentiate nodes by their WL-trees at least on the training set" (line 285), but this leaps from *the WL-tree's informativeness about the anchored subgraph in this dataset* to *a GNN can learn to exploit this*, which is unsupported. No comparison is made to the information captured by 1-WL colors directly — the most natural baseline — so it is unclear what the entropy analysis adds beyond what is already known from the claimed equivalence. The paper also acknowledges that the reported numbers "underestimate the true entropy in an inductive setting" (line 284) for MUTAG but treats this as a minor caveat when it significantly weakens the conclusions drawn from that dataset.

- **Algorithm 1 (recovering anchored graphs from WL-trees) is under-specified.** The algorithm is described entirely in prose via Condition 1 (lines 205–211), and for the enumeration variant the paper states "we omit the implementation details" (line 221). The correctness claim (Theorem 10) is stated without proof. Given that this algorithm is presented as one of the paper's main concrete contributions, the lack of precise specification (even an appendix-level pseudocode) makes it difficult to assess correctness or implement independently.

### Minor

- **The practical added value of WL-trees over existing constructs is asserted but not demonstrated.** The paper states that WL-trees "provide a more fine-level analysis" (line 162) and "make the underlying structures easier to analyze," but no concrete examples are given where WL-trees reveal something that 1-WL colors or standard computation trees cannot. For instance, Figure 2 shows two nodes with identical 1-WL colors but different structures — the paper could walk through what their WL-tree representations reveal, but does not. The claimed "intuitiveness" is stated, not shown.

- **Computational complexity is not discussed.** The BFS-tree construction allows revisits and can grow as $O(d^\ell)$ where $d$ is node degree. Algorithm 1's enumeration variant could be exponential. For an analysis tool that is meant to be used, this matters and should be acknowledged.

- **Notation inconsistency in Theorem 5 (line 149).** The theorem is stated as a bijection $c_i^k \leftrightarrow W_i^k$, but $W_i^k$ was previously defined as a walk (line 38); the WL-tree is denoted $T_i^\ell$ throughout the paper. This creates ambiguity in reading the paper's central claim.

### Trivial

None.

## Nice-to-Haves

- A rigorous inductive proof of Theorem 5 would resolve the paper's central gap and is the single highest-leverage improvement.
- A direct worked example comparing what WL-trees reveal vs. what 1-WL colors reveal (e.g., for the Figure 2 case) would concretely demonstrate the claimed "intuitiveness."
- Adding a comparison to information captured by raw 1-WL colors in the entropy analysis would clarify whether WL-trees add value beyond the claimed equivalence.

## Removed Points

These points from the input reviews are removed; treat them with caution:

- *"Line 48 has a nonsensical equation" and "Line 57 $c_i^{k-1}=c_i^{k-1}$ is tautological"*: The first is a PDF-extraction parser artifact; the second correctly describes a documented property of 1-WL (colors never decrease). Neither is an author error.
- *Criticism about missing comparison to GC2 logic*: Scope creep; the paper addresses GC2 in its related work and is not required to perform a comparative analysis.
- *"The paper does not discuss the relationship between WL-trees and rooted isomorphism types / unfolding trees"*: The paper explicitly distinguishes WL-trees from roll-out trees and computation trees (line 127), which are the relevant prior constructs.
- *"Theorem 11 is a near-tautology and does not add substance"*: Theorem 11 is a simple but correct formal implication that provides a guaranteed pruning rule for subgraph matching — a contribution acknowledged by the paper and useful in context.

## Novel Insights

None beyond the paper's own contributions. The core synthesis from the reviews is that the paper's theoretical scaffolding (Theorem 5) and its empirical support are both too under-developed to carry the claimed contributions, despite the genuine potential of the core idea. The three-layer error categorization is the most novel conceptual contribution as-written, but it occupies only a few lines in the discussion section.

## Suggestions

1. Provide rigorous proofs — at minimum, a detailed inductive proof of Theorem 5, which is the paper's foundational claim.
2. Replace or substantially overhaul the empirical evaluation: use readable tables with actual numeric values and error bars, include standard expressiveness benchmarks (EXP, BREC, or synthetic isomorphism tests), and compare directly against the information captured by 1-WL colors.
3. Provide pseudocode for Algorithm 1 (at least in the appendix) and discuss its computational complexity and worst-case behavior.
4. Add a concrete worked example demonstrating what WL-trees reveal that 1-WL colors or standard computation trees do not, to substantiate the claimed "intuitiveness" and "more fine-level analysis."

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>