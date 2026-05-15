Now I have thoroughly verified the paper content against the reviewer claims. Let me produce the consolidated review.

## Summary

This paper introduces SCHull, a hyperparameter-free method for constructing graph representations of 3D point clouds (especially molecules) by projecting points onto a unit sphere centered at their centroid and taking the convex hull edges as the graph. The method provides three theoretical guarantees: sparsity (edge-to-node ratio < 3), connectivity, and rigidity (enabling a single-layer maximally expressive GNN to distinguish any two non-isomorphic generic point clouds). Experiments on force prediction, protein fold/reaction classification, and binding affinity show that integrating SCHull with existing GNNs consistently improves performance with negligible computational overhead.

## Strengths

- **Clean theoretical guarantee of simultaneous sparsity and connectivity.** Proposition 3.1 and Corollary 3.2 prove that SCHull graphs are always connected and have an edge-to-node ratio bounded above by 3, directly addressing a well-motivated problem (Figure 1). This is the paper's most solid and verifiable theoretical contribution.

- **Consistent empirical improvements across diverse tasks and models.** Tables 3–5 show that integrating SCHull into multiple GNN backbones (DimeNet, SphereNet, LEFTNet, ProNet, GVP-GNN, SEGNN, MACE) yields consistent gains in force prediction MAE, protein fold/reaction classification accuracy, and binding affinity correlations, all with minimal runtime overhead.

- **Hyperparameter-free construction with low computational cost.** The method requires no tunable parameters (unlike radial cutoff threshold or k in kNN) and runs in O(m log m) time, making it practical for large proteins.

- **Clear empirical demonstration that benefit grows with graph size.** Figure 5 shows the accuracy gain of SCHull-integrated ProNet-Backbone over the baseline increases monotonically as protein graphs grow larger, directly supporting the claim that ensuring connectivity matters more for larger molecules.

## Weaknesses

### Fatal

None.

### Major

1. **The NestedSquares synthetic experiment does not validate Theorem 3.6 as claimed.** The paper states it was designed "to solidify Theorem 3.6" (line 171), but Theorem 3.6 concerns (i) 3D generic point clouds, (ii) a maximally expressive GNN with specifically attributed SCHull graphs encoding dihedral angles, and (iii) distinguishing *any* two non-isomorphic configurations. NestedSquares is a 2D task with symmetric (non-generic) nested squares, uses standard MPNN (not a provably maximally expressive one), and does not involve dihedral angles (undefined in 2D). The experiment does show that SCHull's graph structure benefits GNNs on a geometric reasoning task — which is supportive in a broad sense — but it cannot be taken as direct validation of the paper's central rigidity theorem. This is an overclaim that should be corrected.

2. **No ablation isolating rigidity from connectivity as the source of empirical gains.** In all experiments, SCHull is combined with the baseline graph (e.g., radial cutoff), adding both new edges and connectivity. The paper never compares against a simple control that adds a minimal set of edges to restore connectivity without any rigidity guarantee (e.g., a spanning tree or a few long-range edges). Figure 5 shows gains grow with protein size, which is consistent with a pure connectivity story. Without this ablation, the headline claim that improvements are "due to [SCHull's] rigidity and connectivity" is unsupported — connectivity alone may be the full explanation. This is the most significant experimental gap.

### Minor

3. **The combined graph (SCHull + radial cutoff) loses the strict sparsity guarantee.** The theoretical bound (edge-to-node ratio < 3) applies only to SCHull alone, but all real-world experiments use the union of SCHull and the baseline graph. Section 3.4 recommends this combination and states it "maintain[s] connectivity and sparsity," but the combined graph's density is no longer provably bounded. The paper should explicitly acknowledge which guarantees carry over to the combined graph and which do not.

4. **No comparison against alternative constructions that also aim for sparsity and connectivity.** The paper compares against radial cutoff, kNN, chemical graphs, and Voronoi, but does not evaluate α-shapes, power graphs (Sverdlov & Dym, 2024), or other methods. (The sphere Delaunay triangulation is essentially dual to the convex hull and thus equivalent, so this is not a gap.) While the existing comparison set is reasonable, the claim that SCHull "uniquely" achieves all three properties would benefit from a wider set of baselines.

### Trivial

- The generic condition (Equation 3) excludes points at the centroid and collinear projections. Lemma 3.4 notes this holds with probability 1 for uniformly distributed points, but real molecules (especially symmetric ones) may violate it. The paper could briefly discuss how to handle such edge cases in practice.

## Nice-to-Haves

- **Ablation control for connectivity:** Compare SCHull integration against adding a minimum spanning tree (or a small set of long-range edges) to the baseline graph to match the connectivity of SCHull without adding its specific structural/rigidity properties.
- **Disconnectivity statistics:** Report what percentage of baseline graphs are disconnected in each dataset (Fold, React, LBA) to help the reader assess whether connectivity alone could explain the gains.
- **Visualization of SCHull on a real protein:** A direct visual comparison of SCHull edges vs. radial cutoff edges on a concrete protein example would make the contribution more tangible.

## Removed Points

These points were removed from consideration with justification:

1. **"Theorem 3.6 proof is missing / unverifiable."** — Removed per rule: The parser strips appendix content from all papers; the proof exists in the original submission. The critic's substantive concerns about one-layer sufficiency are legitimate but can only be evaluated against the actual proof, which is not available in the parsed text.
2. **"Paper does not show real-world rigidity failures."** — The paper motivates rigidity with a synthetic example (Figure 2), which is standard and appropriate for a theoretical motivation. Requiring real-world evidence of rigidity failures asks the paper to address a problem outside its stated scope.
3. **"Missing comparison to Delaunay triangulation on the sphere."** — The convex hull of points on a sphere is the dual of the spherical Delaunay triangulation; these constructions produce essentially the same graph, making the requested comparison circular.
4. **Generic formatting and style observations.**
5. **Strength Finder's claim that NestedSquares "empirically validates" Theorem 3.6** — Dropped because it conflicts with verified weakness #1 (the experiment does not actually validate the 3D rigidity theorem).

## Novel Insights

Across the reviews, a clear pattern emerges: the paper's most solid and independently verifiable contribution is the sparsity + connectivity guarantee (Proposition 3.1, Corollary 3.2), which is well-proven and well-motivated by Figure 1. The rigidity claim (Theorem 3.6) is theoretically interesting and could be a genuine advance if the proof holds, but its empirical support is weak — the NestedSquares experiment is misaligned with the theorem's conditions, and the real-world experiments do not isolate rigidity from connectivity. The consistent empirical improvements suggest SCHull has practical value regardless, but whether this value stems from rigidity or merely from restoring connectivity is an open question that the paper does not resolve. Reframing the contribution around the clean sparsity/connectivity guarantee (with rigidity as a theoretical bonus property) would better match the evidence presented.

## Suggestions

1. **Reframe or remove the claim that NestedSquares "solidifies Theorem 3.6."** The experiment demonstrates that SCHull's graph structure helps GNNs on a 2D geometric task, which is a worthwhile finding in its own right, but it does not test the theorem's conditions. Either redesign the experiment to test 3D rigidity directly, or present it as independent evidence that SCHull benefits geometric reasoning without linking it to Theorem 3.6.

2. **Add a connectivity-only ablation control.** Compare SCHull + baseline against baseline + a spanning tree or a few random long-range edges that restore connectivity but carry no rigidity guarantee. If SCHull still outperforms this control, the case for rigidity's role would be much stronger. If not, the paper should honestly attribute gains to connectivity.

3. **Explicitly state which guarantees apply to the combined graph** used in experiments versus the SCHull graph alone, particularly regarding the sparsity bound.

4. **Report the percentage of disconnected baseline graphs** in each real-world dataset, and discuss how this correlates with observed improvements.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>