Now I have all the information needed to write the consolidated review. Let me compile and write it carefully.

---

## Summary

This paper proves novel structural bounds on the connectivity graph of the polyhedral complex defined by fully-connected ReLU networks. The main theoretical result — that the average degree of this graph is at most \(2d\) (twice the input dimension) regardless of network width or depth — is established via an inductive argument on bent hyperplanes. The paper also provides complementary bounds on the graph diameter that are independent of the input dimension, and an algorithm for enumerating the polyhedral complex and constructing its connectivity graph. Experiments on synthetic and real-world data confirm the theoretical bounds and reveal that data points tend to lie in polyhedra with higher-than-average connectivity.

## Strengths

- **Theorem 3.4 (average degree ≤ 2d) is proven for all fully-connected ReLU networks via a clean inductive argument.** The proof uses Lemma 3.2 (categorization of cells when a BH is removed) and Lemma 3.3 (cell-count recurrence) to reduce the problem to an induction on the number of neurons and input dimension. This is the first non-asymptotic, architecture-independent upper bound on the average degree of the connectivity graph, extending prior results that only applied to single-layer hyperplane arrangements. The proof sketch in the main text is well-structured and the key ideas are communicated clearly.

- **Theorem 3.7 shows that for shallow networks the average degree converges to exactly \(2d\) as \(n \to \infty\).** Together with Theorem 3.6 (monotonic increase), this demonstrates the upper bound is tight in the limit. The synthetic experiments (Table 1, Figure 4) corroborate this: deeper networks also approach the bound as the number of neurons grows.

- **Theorem 3.8 gives a diameter upper bound \(O(m^\ell)\) that does not depend on the input dimension \(d\).** This is a non-trivial structural observation: the number of regions grows exponentially with \(d\), yet the diameter can be bounded independently of \(d\). The empirical results in Figure 5 confirm that for fixed architectures, diameter estimates for different input dimensions are nearly identical, supporting the dimension-independence claim.

- **Algorithm 1 provides a practical method for constructing the connectivity graph via BFS and LP-based redundancy checking.** While the BFS approach is similar to prior work (Xu et al., 2022; Liu et al., 2023a,b), the addition of explicit graph construction and edge recording enables the empirical studies in Section 5.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theorem 3.5 (lower bound) is stated without any proof sketch.** At the start of Section 3 the paper promises "Proof outlines are given here while detailed proofs are in Appendix B." Theorem 3.5 receives zero exposition — no reasoning, no intuition, no sketch. The claim that "every \(d\)-cell has at least \(\min(n_1, d)\) neighbors" is not obviously true for deep networks where first-layer hyperplanes may not all generate faces of a given region. Even a brief one-paragraph justification would substantially improve the exposition. This does not threaten the core contribution (Theorem 3.4), but it is a clear gap in the promised proof-outline structure.

- **Theorem 3.8 (diameter bounds) lacks any proof sketch in the main text.** The upper bound \(O(m^\ell)\) is stated with only a vague intuition ("may rarely be reached in practice") and no hint of the combinatorial argument that produces it. While detailed proofs are deferred to the appendix (which the conference format can accommodate), the complete absence of reasoning in the main text prevents the reader from assessing the plausibility of the bound. This is particularly notable because the paper otherwise provides sketches for the more central Theorems 3.1/3.4.

- **Potential sampling bias in the real-data experiments (Section 5.2).** For CIFAR10 and California Housing, the BFS enumeration is truncated at 8 million polyhedra from a single starting point, producing a connected subgraph that may systematically undersample regions far from the start. Data-containing polyhedra are then force-included (if not already found), creating an asymmetry between the "data" and "non-data" sets that could partially explain the observed higher connectivity of data regions. The paper acknowledges the truncation but does not analyze this specific bias. For MNIST, the full enumeration avoids this concern, and the observation remains plausible, but the evidence from the partial-enumeration datasets is weaker than presented.

### Trivial
None.

## Nice-to-Haves

- A brief intuition for Theorem 3.6 (monotonicity) — even one sentence explaining why adding a neuron increases the average number of faces — would help the reader.
- The diameter upper bound could be made more informative with a brief explanation of the construction that achieves \(O(m^\ell)\), or at least the worst-case path that attains this scaling.
- An ablation on the BFS starting point for the real-data experiments (e.g., starting from multiple random polyhedra and comparing the sampled degree distributions) would strengthen the empirical claims.

## Removed Points

These points from the reviewers are removed as they do not constitute valid weaknesses:

- *"The diameter upper bound is too weak to be informative / a tighter bound would be more interesting"* — This is a qualitative assessment, not a flaw in the presented result. The paper acknowledges the bound is loose. The interesting aspect is dimension-independence, which is a valid structural insight irrespective of looseness. Speculation about what a "tighter" bound could be is not grounded in the paper's analysis.
- *"No discussion of the effect of training on genericity"* — The assumptions from Masden (2025) hold with probability 1 over weight assignments, which includes trained weights. There is no reason to believe training systematically lands on measure-zero degenerate configurations. The paper's experimental results also confirm the bounds hold for trained networks.
- *"Missing related work"* — The reviewer requests additional citations without specifying concrete works. This is not a valid weakness.
- *Section-by-section notes about Theorems 3.6 and 3.7 lacking proof sketches* — Subsumed by the more general point about Theorem 3.5 and 3.8; the paper explicitly defers detailed proofs to the appendix, which is standard for page-limited conferences.
- *Strength Finder's generic or unsupported strengths* — Several strengths claimed by the Strength Finder (e.g., "This paper addressed an important problem") are generic and not specific to the paper's content. These are removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a brief proof sketch for Theorem 3.5 in the main text — even the intuition that each \(d\)-cell is bounded by hyperplanes from the first layer, and at most \(d\) hyperplanes can be linearly independent around a single point, so the number of distinct first-layer faces is at least \(\min(n_1, d)\). This would close the most conspicuous exposition gap.
2. Clarify the reasoning behind the Theorem 3.8 upper bound by stating the combinatorial argument (even at a high level) rather than deferring entirely to the appendix.
3. Discuss the potential BFS sampling bias in Section 5.2 explicitly — acknowledge that the non-data polyhedra form a connected subgraph from one root, while data polyhedra are preferentially included, and explain why the observed trend is still meaningful despite this asymmetry.

## Score and Decision

**Calibration procedure.** Round 1 bracketing used three queries over the review corpus to find anchors in the (<3.5), (3.5–7.5), and (>7.5) score bands:

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| CiB4te6gGq | 2.00 | R1 | Much weaker; not topically related |
| zbiWoFe60O | 3.20 | R1 | Much weaker; not about ReLU geometry |
| mesI72n7m1 | 3.00 | R1 | Much weaker |
| I30HO3xth3 | 3.00 | R1 | Much weaker |
| AGVH53xu2n | 4.50 | R1 | About dual graph construction; less theoretical depth, rejected. Current paper is stronger. |
| jDSrbmo0sY | 5.00 | R1 | About ReLU polyhedral homology; rejected due to strong assumptions. Current paper is stronger. |
| O4Oy7NsSwG | 5.50 | R1 | About parameter-space topology; accepted poster. Comparable quality but different focus. |
| 248ysaRatx | 8.00 | R1 | Not topically related |
| 444mACDffR | 4.50 | R1 | Not about geometry |
| P2GIT8LpV2 | 5.00 | R2 | GNN theory; not directly comparable |
| zVmS7G6Dyi | 6.00 | R2 | ReLU generalization theory; solid but different topic |
| L5jYWeycAx | 6.80 | R2 | Polynomial NN theory; strong but limited to polynomial activations |
| ditBKIciC3 | 5.60 | R2 | Loss geometry; not directly comparable |
| qPKTDOJ5Xs | 6.00 | R2 | Linear regression theory |

**Initial bracket:** 5.0–7.0. The paper is clearly stronger than the Rejected anchors (4.5–5.0) in the same subarea and comparable to Accepted Poster anchors (5.5–6.8). **Narrowing:** The paper is stronger than the 5.5 anchor (which had a narrower scope of analysis) and comparable to lower-6 anchors, but not as theoretically deep as the 6.8 polynomial NN paper (which has a more complete theoretical characterization but limited to a less practical setting). **Final score: 6.0.** The paper makes a genuine, well-supported contribution (the \(2d\) bound is novel, clean, and empirically confirmed). The main weaknesses are exposition gaps that do not undermine the core result. This places it in the solid-accept range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>