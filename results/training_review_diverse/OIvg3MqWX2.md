Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper introduces SCHull, a hyperparameter-free graph construction for 3D point clouds (especially molecules) based on projecting points onto a unit sphere and taking the convex hull of the projections. The method provably produces connected, sparse graphs (edge-to-node ratio < 3) and is claimed to guarantee rigidity — meaning edge lengths, dihedral angles, and node norms suffice for a maximally expressive GNN to distinguish any two non-isomorphic generic point clouds. Empirical results on MD17 force prediction, protein fold classification, enzyme reaction classification, and binding affinity show consistent improvements when SCHull edges are integrated into existing GNN architectures.

## Strengths

- **Provably sparse and connected graph construction with a clean theoretical guarantee.** Corollary 3.2 proves that SCHull graphs are always connected with an edge-to-node ratio bounded above by 3. This directly addresses a known limitation of radial cutoff graphs, which cannot simultaneously guarantee sparsity and connectivity (Figure 1). The proof of the sparsity/connectivity result is present and verifiable.

- **Hyperparameter-free method.** Unlike radial cutoff (which requires tuning the distance threshold) or k-NN (which requires choosing k), SCHull deterministically produces a graph from the point cloud. This is a practically valuable property for deployment and reproducibility.

- **Consistent empirical improvements across diverse molecular benchmarks.** SCHull-integrated models outperform baselines on force prediction (Table 3), protein fold classification (Table 4, e.g., ProNet-Backbone accuracy improving from 68.8% to 74.1% on the Fold test set), enzyme reaction classification (Table 4), and ligand binding affinity prediction (Table 5). The improvements are consistent across multiple GNN architectures (DimeNet, SphereNet, LEFTNet, ProNet, GVP-GNN).

- **Connectivity benefit scales with graph size.** Figure 5 shows that the accuracy improvement of SCHull-integrated ProNet-Backbone increases as protein graphs grow larger (subsets up to 150, 300, 450, 600 nodes), directly supporting the claim that connectivity is increasingly important for capturing global geometric information in large molecules.

- **Computational efficiency and easy integration.** The convex hull construction runs in O(m log m) time, and Tables 4-5 show minimal runtime overhead. Section 3.4 describes a straightforward integration procedure that adds SCHull edges on top of existing radial cutoff graphs without changing the GNN architecture.

## Weaknesses

### Fatal

None.

### Major

- **Theorem 3.6 — the central rigidity claim — is presented without a proof.** The paper states "Due to page limitations, this version of Theorem 3.6's proof is omitted." This theorem asserts that a maximally expressive GNN with depth 1 can distinguish any two non-isomorphic generic point clouds using the attributed SCHull graph. The proof is not merely deferred to an appendix; it is omitted entirely from this submission. Since the paper's title, abstract, and motivation all heavily emphasize rigidity as a key contribution, the absence of this proof is a significant gap. Moreover, the mapping from Stoker's theorem (which applies to strictly-convex polyhedral graphs) to the SCHull graph (which is a non-convex graph on the *original* points, inheriting connectivity from the convex hull of *projected* points) is nontrivial. The paper acknowledges the convexity gap (lines 157-159) and claims that adding node norms bridges it, but without the proof, the argument cannot be verified. The authors should either provide the proof or clearly state Theorem 3.6 as a conjecture with supporting reasoning.

- **No ablation isolates the role of rigidity vs. added edges and features.** The integration procedure (Section 3.4) simultaneously adds (i) SCHull edges, (ii) dihedral angle features, and (iii) node-center distance features to the baseline radial cutoff graph. The reported improvements could come from any combination of these factors. Without ablations that control for (a) adding the same number of random global edges, (b) adding global edges from an alternative sparse construction (e.g., minimum spanning tree, farthest-point sampling), or (c) adding dihedral angle features to the original radial cutoff graph alone, the specific claim that *rigidity* drives the improvement is unsupported. The NestedSquares experiment (Table 2) also compares MPNN+SCHull (using full SCHull features) against competitors using only their default features, which demonstrates that SCHull's feature set helps but does not isolate *which* aspects are responsible.

### Minor

- **Planar and linear molecules are not addressed.** The rigidity analysis (Lemma 3.5, Theorem 3.6) requires that the projected points are not coplanar, which holds for generic point clouds. However, many real molecules are planar (e.g., benzene appears as a test molecule in MD17) or nearly linear. For planar molecules, the projected points lie on a great circle, the convex hull is a planar polygon rather than a convex polyhedron, and Stoker's theorem does not apply. The paper acknowledges the generic condition but does not discuss how common molecular structures that violate it are handled in practice. A practical workaround (e.g., small perturbations, fallback construction) or an analysis showing such cases are negligible in the tested benchmarks would strengthen the paper.

- **Some empirical gains are marginal, and the claim of "significant margin" is overstated.** In Table 3, several improvements are very small (e.g., LEFTNet on Malonaldehyde: 0.070→0.069 MAE; DimeNet on Toluene: 0.809→0.810, which is a *decrease*). The paper's claim that SCHull "consistently improve... by a significant margin" does not hold uniformly across all benchmarks.

- **Unverifiable standard deviation reporting.** The paper states (line 199) that experiments are run five times with standard deviation recorded, but the tables are images and it is unclear whether stds are actually reported in Tables 3, 4, and 5 (they are explicitly stated for Table 2). This inconsistency should be resolved.

### Trivial

- Remark 3.7 says the node attributes "can be omitted without affecting the theorem's result if we consider removing an additional measure zero subset of point clouds." The description of this subset is too vague to be useful — what condition characterizes this subset?

## Nice-to-Haves

- An ablation comparing SCHull edges against alternative sparse global graphs (e.g., edges from the convex hull of the original points without projection, or edges from a minimum spanning tree on pairwise distances) would help isolate whether the projection step specifically contributes to the improvement.
- A runtime comparison against k-NN and other graph constructions beyond the radial cutoff results would strengthen the efficiency claims.
- Discussion of how edge overlap between SCHull edges and the original radial cutoff edges is handled (or why it does not matter).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Lemma 3.5's proof is in the appendix (not available)."** The parser strips appendix content from all papers; the proof exists in the original submission. Removed per rule on missing appendix content.
- **"The paper does not fully describe NestedSquares experimental details."** These details are referenced as "see Appendix [...] for experimental details," which was stripped by the parser. Removed per rule on missing appendix content.
- **"The 48Å cutoff claim references data not fully described (Fold dataset has max ~600 nodes)."** The paper's statement about "large proteins with more than 1000 amino acids" is a general observation about what cutoff is needed for large proteins, and the Fold dataset analysis in Fig. 1(e) serves as supporting evidence. Without external verification of the Fold dataset's maximum size, this criticism is too speculative to retain. Removed.
- **"Missing hyperparameter disclosure for cutoff choice."** Hyperparameter settings are referenced as being in Appendices H.2 and I.2, which were stripped. Removed per rule on missing appendix content.
- **"The paper mentions SEGNN/MACE but doesn't provide results for them in the main text."** The critic states these results appear in Table 4, so this is internally contradictory. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide the proof of Theorem 3.6, or at minimum a detailed proof sketch in the main paper explaining how edge lengths, dihedral angles, and node norms jointly enable reconstruction of the point cloud up to isometry, and why a 1-step message-passing GNN can compute this. If the proof is not yet complete, clearly state the result as a conjecture.

2. Run ablation studies that separate: (i) adding SCHull edges alone (without dihedral features), (ii) adding dihedral angle features to the baseline graph alone, (iii) adding an alternative set of global edges (e.g., random edges matched in degree, or edges from a minimum spanning tree) to the baseline graph, and (iv) the full SCHull integration. This is the only way to support the claim that rigidity — rather than simply increased connectivity or extra features — drives improvements.

3. Address planar/linear molecules explicitly. Either (a) show that such molecules are rare in the tested benchmarks and empirically verify SCHull still works, (b) propose a fallback construction (e.g., adding a small random perturbation), or (c) add a small random rotation to the points before projection to break coplanarity with probability 1.

4. Ensure standard deviations are reported in all main experimental tables, and tone down the claim of "significant margin" where improvements are marginal.

5. Clarify Remark 3.7 by stating what measure-zero subset of point clouds allows omitting node attributes.

## Score and Decision

This paper presents a clever and clean graph construction with a provably useful sparsity/connectivity guarantee and strong empirical results across multiple molecular tasks. The idea of using the convex hull of sphere-projected points to obtain a sparse connected graph with a bounded edge ratio is genuinely novel and practically useful. The experimental validation is broad and shows consistent gains.

However, the paper's central theoretical claim about rigidity (Theorem 3.6) is presented without proof, making it unverifiable. The experimental evaluation does not separate the contribution of rigidity from the contribution of simply adding more edges and features. The method also has an unaddressed limitation for planar/linear molecules that constitute real chemical structures.

These weaknesses are substantial but not fatal — the sparsity/connectivity contribution stands on its own, and the empirical results are credible evidence of practical utility even if the rigidity claim remains a conjecture. With the proof provided (or the claim downgraded to a conjecture) and ablation studies added, the paper would be strong. In its current form, it is borderline.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>