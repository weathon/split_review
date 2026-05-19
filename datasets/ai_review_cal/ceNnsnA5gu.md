- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have all the information I need. Let me write the consolidated review.

## Summary

The paper introduces **WL-trees**, a tree-based representation of the structural information encoded in GNN node representations. WL-trees are constructed by running a BFS (that allows revisits except to the direct parent) on the input graph and then dropping node ids. The paper proves a bijection between 1-WL colors and WL-trees (Theorem 5), provides an algorithm to recover anchored subgraphs compatible with a given WL-tree (Section 4.3), connects WL-trees to subgraph matching (Theorem 11), and analyzes two improved GNN variants (CLIP-2 and Nested GNN) through the WL-tree lens (Section 6). Empirical evaluation counts compatible subgraphs and computes conditional entropy on three datasets.

---

## Strengths

- **Formal bijection between 1-WL colors and WL-trees (Theorem 5).** The paper proves that WL-trees and 1-WL colors carry the same information, grounding WL-trees as a valid equivalent representation. The proof sketch (via Lemma 4 and Figure 4) shows how shallower WL-trees correspond to previous-round colors.

- **Constructive algorithm for recovering anchored graphs from a WL-tree (Section 4.3, Theorem 10).** The paper provides a concrete method (Condition 1 with three sub-conditions) to enumerate all anchored subgraphs consistent with a given WL-tree. This goes beyond what the 1-WL algorithm alone offers and gives a tool for understanding which graph structures are conflated by a GNN.

- **Formal subgraph-matching test (Theorem 11).** The paper shows that a WL-tree contains a subtree matching the WL-tree of any anchored subgraph of the original graph, providing a necessary condition for subgraph containment that can be checked purely from the WL-tree — a capability not available from neural representations.

- **Explicit distinction from prior tree-based methods (Definition 1 vs. roll-out trees).** The paper clearly differentiates its BFS-tree construction (which avoids revisiting the direct parent) from prior roll-out trees used in graph-kernel and GNN analysis, making the novelty of WL-trees concrete.

- **Application of WL-trees to analyze improved GNNs (Theorems 12–13).** The paper derives WL-tree analogues for CLIP-2 and Nested GNN, then quantifies how extra node colors reduce the number of compatible anchored subgraphs and lower conditional entropy. This applies WL-trees as an analytic tool beyond vanilla MPNNs.

---

## Weaknesses

### Fatal
None.

### Major

1. **The paper overclaims that WL-trees provide "deeper understanding" without concretely demonstrating a uniquely enabled insight.**  
   The abstract, introduction, and conclusion repeatedly assert that WL-trees "deepen the understanding" of node representations. However, because Theorem 5 establishes a bijection between 1-WL colors and WL-trees, the two representations carry the same information. The paper does not demonstrate a concrete analytical result, design principle, or bound that is *uniquely* enabled by the tree perspective and inaccessible to standard 1-WL analysis. The recovery algorithm and subgraph matching test are the most novel elements, but the paper does not argue why they are easier or more natural with WL-trees than with the flat multiset of colors.

2. **The experimental evaluation is descriptive rather than probative, and does not use WL-trees to derive new insights about GNN behavior.**  
   Tables 1–4 count compatible anchored subgraphs and compute conditional entropy for three coloring schemes. The finding that extra colors (from CLIP-2 or Nested GNN) reduce ambiguity is expected — adding information to node labels strictly refines the partition — and does not rely on WL-trees. The same quantities could be computed from 1-WL color sequences. The paper also conflates distinguishability in the discrete coloring space with what a neural network can learn, concluding that "a GNN has the ability to differentiate nodes by their WL-trees" when small conditional entropy may simply reflect dataset structure rather than model capacity. The paper acknowledges inductive settings may yield underestimates but does not address this substantively.

3. **The three-layer error categorization (Discussion) is insightful but orthogonal to WL-trees.**  
   The categorization of errors into (1) different labels with same anchored graphs, (2) different labels with same WL-tree but different anchored subgraphs, and (3) different labels distinguished by WL-trees but not by GNN, could be stated without the WL-tree formalism. The final claim that "the solution to [the third error] boils down to better representation learning of WL-trees" is a restatement of the problem, not a derived design principle.

### Minor

1. **Algorithm 1 (recovering anchored graphs) is described at a high level without a precise specification or complexity analysis.**  
   The algorithm is presented in prose with Condition 1 formally stated, but no explicit pseudocode is given. The paper acknowledges it "can optionally decide use existing id in each 'while' loop" without specifying how choices are made or enumerated. No runtime or scaling analysis is provided, even for the small graphs studied. While the algorithm is reasonable as a conceptual tool, the description is too vague for reproducibility without filling in significant implementation details.

2. **The analysis of CLIP-2 and Nested GNN (Theorems 12–13) is straightforward given the bijection theorem.**  
   Theorem 12 states that if WL-trees are the same under a random coloring, the representations are the same — a direct corollary of the WL-to-MPNN equivalence. Theorem 13 characterizes Nested GNN as computing WL-trees with WL-trees as node colors, which is a clean application of the bijection but yields no new bound or design principle. The paper does not use WL-trees to identify any limitation of these GNNs or suggest a concrete improvement.

3. **Theorem 5 contains a typographical inconsistency** (the mapping is written as `c_i^k ↔ W_i^k` where `W` should likely be `T`) and does not explicitly specify the domain/codomain of the bijection (e.g., whether it is for a fixed ℓ, a fixed graph, or all orders). The surrounding text clarifies the meaning, but the formal statement is imprecise.

### Trivial
None.

---

## Nice-to-Haves

- Extend Algorithm 1 with explicit pseudocode and a complexity analysis (even for the diagnostic use case, knowing the enumeration cost guides practitioners).
- Discuss how WL-trees extend naturally to attributed graphs (the paper handles colors as surrogates for attributes, but real-valued attributes are not addressed).
- Use WL-trees to construct concrete adversarial examples where two non-isomorphic anchored subgraphs produce the same WL-tree (and thus the same GNN representation), demonstrating a concrete failure mode of GNNs.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic: "The paper states several theorems without any proof sketch in the main text."** — The paper provides proof sketches for Theorem 5 (paragraph after the statement, referencing Lemma 4 and Figure 4), Theorem 10 (correctness follows from the algorithm description), Theorem 11 (a paragraph derives it from BFS-tree properties), and Theorems 12–13 (follow from Theorem 5). The Appendix may contain full proofs, but the main text does sketch the reasoning. **Reason: Factually inaccurate — proof sketches exist in the main text.**

- **Harsh critic: "The paper acknowledges that node attributes are not considered (only colors)" — suggesting WL-trees should be extended to attributed graphs.** The paper explicitly considers node colors from the 1-WL algorithm, which can represent attributes. The paper states "Assume each node i is associated with a color c_i. If there is not a natural way to color graph nodes, then let c_i=0 for all i." Colors are the paper's mechanism for handling attributes. **Reason: Misunderstands the paper; colors are the paper's treatment of attributes.**

- **Harsh critic: missing proofs in the appendix.** The instructions state that parser-stripped appendix content is not an author error. **Reason: Parser artifact; the original submission contains this material.**

- **Strength Finder: Empirical conditional-entropy evaluation is a core strength.** The experiments show expected behavior (adding information reduces ambiguity) and do not use WL-trees to derive new insights about GNN behavior. The critic correctly notes the quantity could be computed from 1-WL color sequences directly. **Reason: Conflicts with a verified weakness; the experiments are descriptive, not probative.**

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on WL-trees that the paper itself does not already articulate.

---

## Suggestions

1. **Demonstrate a concrete advantage of WL-trees over 1-WL colors.** For example, use the tree structure to efficiently count substructures (analogous to graphlet kernels) or to derive a compositional analysis of node representations that the flat multiset-of-colors view obscures. Without this, the claim of "deeper understanding" remains aspirational.

2. **Strengthen the empirical evaluation.** Instead of reporting conditional entropy (which is expected to decrease with more colors), use WL-trees to identify specific graph structures that two nodes share despite having different labels — i.e., concrete examples where WL-trees explain GNN failures. Or compare the expressiveness of GNN architectures by analyzing their induced WL-tree partitions.

3. **Provide a concrete application of Theorem 11 to a subgraph matching task** where WL-trees provide guarantees that neural representations cannot, and show this leads to measurable improvement.

4. **Add explicit pseudocode for Algorithm 1** with a worked example and a worst-case complexity bound to make the recovery algorithm reproducible and practically usable.

---
