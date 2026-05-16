Now I have a thorough understanding of the paper and all reviewer claims. Let me write the consolidated review.

## Summary

The paper introduces **WL-trees** — rooted labeled trees obtained by running BFS on a graph (allowing revisits) and then stripping node identities, leaving only colors. The main claims are: (1) WL-trees are in bijection with 1-WL colors (Theorem 5); (2) this tree representation enables an algorithm (Algorithm 1) to recover all anchored subgraphs compatible with a given node's 1-WL color; and (3) WL-trees can serve as an analytic tool — the paper demonstrates this by analyzing CLIP-2 and NGNN, counting compatible anchored subgraphs and computing conditional entropies across three datasets.

## Strengths

- **Novel representation with formal ties to 1-WL.** The WL-tree re-packages the information captured by 1-WL colors into a tree structure that makes the underlying graph neighborhood directly visible. While equivalent to 1-WL in discriminative power, the tree form is more amenable to certain operations — most notably anchored subgraph recovery — that the flat color representation does not directly support.

- **Anchored subgraph recovery algorithm (Algorithm 1, Theorem 10).** This is the paper's clearest concrete contribution: given a WL-tree, the algorithm constructs an anchored graph whose WL-tree matches it. The key idea (Condition 1 for reusing node IDs when subtrees match) is non-trivial and goes beyond what 1-WL colors alone provide. This turns WL-trees from a passive representation into an active diagnostic tool.

- **Formal characterization of cyclic vs. tree graphs (Corollaries 7–8).** The paper proves that WL-trees of cyclic graphs continue to grow with depth while tree anchored graphs stabilize, and that 1-WL can always distinguish a cyclic graph from a tree given enough rounds. This reframes a known limitation of GNNs in simple graph-theoretic terms.

- **Subgraph matching connection (Theorem 11).** The theorem shows that if a WL-tree does not contain another WL-tree as a subtree, the corresponding anchored subgraph cannot be a subgraph of the larger one. This provides a principled, provable way to exclude matching candidates — a type of guarantee that neural representations alone cannot offer.

- **Error source categorization (Section 6 Discussion).** The paper uses WL-trees to decompose node classification errors into three layers (identical anchored graphs, same WL-tree but different subgraphs, same WL-tree but GNN fails), providing a structured framework for diagnosing GNN failures.

## Weaknesses

### Fatal
None.

### Major

1. **Incomplete proof of the central bijection (Theorem 5).** The theorem claims a bijection between 1-WL colors and WL-trees, but the proof is a sketch, not a rigorous induction. The paper states "From their equivalency, we can establish the equivalency" — this is essentially circular. The reasoning (using Lemma 4 to read out subtrees that correspond to previous-round colors) correctly indicates *how* the induction would go, but it never states the inductive hypothesis, never verifies the base case, and never formalizes the bijection between the full tree structure and the iterated color refinement. As this equivalence is the foundation for every subsequent use of WL-trees, the lack of a complete proof leaves the central theoretical claim under-substantiated. Additionally, the theorem statement uses $W_i^k$ (walk notation) where it presumably intends $T_i^k$ (WL-tree), creating confusion about what exactly the bijection relates.

2. **Overclaiming relative to actual novelty.** The paper repeatedly asserts that WL-trees "deepen the understanding" and "enable a more intuitive and insightful understanding of node representations." However, the paper's own Theorem 5 establishes that WL-trees are **equivalent** to 1-WL colors — they provide a different *representation* of the same information. The one operation that genuinely goes beyond what 1-WL colors directly expose is the anchored-subgraph recovery algorithm. The paper would be stronger if it framed itself as introducing a tree representation that facilitates subgraph enumeration, rather than claiming a fundamentally deeper understanding that is not demonstrated to yield insights inaccessible from 1-WL.

### Minor

1. **Experimental evaluation is too thin to carry the weight it is asked to bear.** The experiments report subgraph counts (Table 1) and conditional entropies (Tables 2–4) on three small datasets. The paper's own text acknowledges the limitations: "when ℓ is large, all conditional entropy values are small," and "the reported numbers underestimate the true entropy in an inductive setting." The conditional entropy results lack error bars, vary inconsistently across datasets and depth ℓ, and the claim that "CLIP-2 and NGNN both reduce conditional entropy when ℓ=3" is stated as a general conclusion without statistical support. These experiments are presented as evidence that WL-trees can "measure expressiveness gains," but the signal is weak. Given that this is primarily a theoretical/analysis paper, the experiments are supplementary — however, if they are included, they should be rigorous.

2. **Anchored-graph recovery algorithm is described but not demonstrated.** Algorithm 1 is referenced but appears in an appendix that was stripped (the body text describes its logic). The algorithm is the paper's most novel component, yet there is no worked example showing its output, no enumeration of how many compatible graphs exist for a particular WL-tree, and no application to a concrete diagnostic task. Theorem 10 asserts correctness, but the reader cannot assess practical utility.

3. **No discussion of computational complexity or feasibility.** The paper acknowledges that enumeration generates many graphs ("the computation is much higher") but provides no complexity analysis. WL-trees grow exponentially with depth ℓ in the worst case, and the recovery algorithm is worst-case exponential in the number of nodes. These limitations should be stated explicitly so that readers understand when the tool is usable.

### Trivial

- Theorem 5 uses $W_i^k$ (previously defined as a walk) where it should use $T_i^k$ (WL-tree).

## Nice-to-Haves

- A worked example of the anchored-graph recovery algorithm on a small graph, showing the set of compatible graphs.
- Error bars or variance estimates for the conditional entropy experiments.
- A comparison of the WL-tree representation to the "unfolding tree" or "rooted subtree" constructions known in the 1-WL literature, with explicit discussion of how they differ.
- Complexity bounds (even asymptotic) for tree construction and anchored-graph recovery.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing related works / comparison to "unfolding tree" or "rooted subtree."** The paper does cite Shervashidze et al. (2011), Zhang & Li (2021), and Cai et al. (1992). Without external sources to verify what other specific works exist, this criticism cannot be confirmed and is removed per instructions.

- **"No discussion of limitations."** The paper does acknowledge at lines 221–222 that enumeration has high computational cost and is for diagnostic use only, and at lines 284–285 that conditional entropy underestimates true inductive entropy. While a dedicated limitations section would be an improvement, the paper does not entirely omit discussion of limitations.

- **"Conditional entropy numbers are small in all conditions" as a structural weakness.** The paper itself notes this (line 284: "when ℓ is large, all conditional entropy values are small") and provides an explanation (data probabilities concentrate on a few subgraphs). The small values are a property the paper reports, not an error.

- **"Lack of error bars" elevated to major.** For an analysis paper where experiments are illustrative rather than competitive benchmarking, the absence of error bars is a minor presentation issue, not a structural flaw.

- **"Theorem 5 proof is a single sentence."** The proof spans a paragraph (lines 151–152) that sketches the inductive reasoning using Lemma 4. It is insufficient as a proof, but describing it as a single sentence is inaccurate.

## Novel Insights

The reviews surface an interesting tension: the reviewer criticizes the paper for overclaiming novelty relative to 1-WL, while simultaneously the paper's own concrete algorithmic contribution (anchored-graph recovery) does go beyond what 1-WL colors directly provide. The real issue is not whether WL-trees are useful — they are a clean way to visualize the equivalence class of neighborhoods with the same 1-WL color — but whether the paper demonstrates that utility convincingly. The reviewer's insistence on a rigorous proof and the observation that the recovery algorithm is the true contribution (not the WL-tree per se) are both sharper than the paper's own framing. Notably, the fact that WL-trees can be used to *enumerate* the set of anchored subgraphs that collapse to the same 1-WL color gives a concrete measure of "structural ambiguity" that the color itself does not expose — this is a genuinely novel diagnostic use that deserves clearer emphasis and better experimental support.

## Suggestions

1. **Strengthen the proof of Theorem 5.** Provide an explicit inductive argument: state the inductive hypothesis (bijection holds at depth ℓ−1), use Lemma 4 to extract subtrees corresponding to neighbor colors, and construct the bijection between the full tree at depth ℓ and the 1-WL hash at round ℓ. Verify the base case (ℓ=0). Correct the typographical inconsistency ($W_i^k$ → $T_i^k$).

2. **Reframe the paper's contribution more precisely.** Instead of claiming "deeper understanding," describe WL-trees as a tree representation that (a) makes the neighborhood structure of 1-WL colors directly accessible, and (b) enables anchored-subgraph enumeration — a task that 1-WL colors alone do not support. This frames the recovery algorithm as the primary novel contribution, which is defensible.

3. **Demonstrate the recovery algorithm on a concrete case.** Pick one WL-tree from one dataset, enumerate all compatible anchored subgraphs (or even a subset), and show what structural ambiguity looks like. This would immediately illustrate the diagnostic value that the paper claims but does not fully demonstrate.

4. **Either strengthen the experiments or acknowledge their illustrative nature more explicitly.** If the experiments stay, add variance estimates and clarify which conclusions are statistically meaningful. Alternatively, reframe Section 6 as a proof-of-concept and state that a thorough empirical evaluation is future work.

## Score and Decision

**Originality:** 3/5 — WL-trees are a new representation, though equivalent to a known object (1-WL colors). The recovery algorithm is genuinely novel.

**Importance of research question:** 4/5 — Understanding what structural information GNNs encode is a central problem.

**Claims well-supported:** 2/5 — The central theorem lacks a rigorous proof; experimental support is thin.

**Soundness of experiments:** 2/5 — No error bars, inconsistent trends, acknowledged limitations.

**Clarity of writing:** 3/5 — Definitions are clear; the proof sketch and recovery algorithm description could be more precise.

**Value to the research community:** 3/5 — The recovery algorithm could be a useful diagnostic tool, but the paper does not yet demonstrate this convincingly.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>