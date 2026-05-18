Now I have enough information to produce the consolidated review. Let me write it.

## Summary

This paper proposes SCHull, a novel hyperparameter-free graph construction for 3D point clouds (especially molecules) based on projecting points onto the unit sphere and taking the convex hull of the projections. SCHull graphs are proven to be simultaneously connected, sparse (edge-to-node ratio ≤ 3), and rigid (edge distances + dihedral angles uniquely determine spatial arrangement up to isometries). The method is integrated with existing GNNs by combining SCHull edges with base graph edges, and empirical results show consistent improvements across four molecular benchmarks (MD17 force prediction, protein fold classification, enzyme reaction classification, ligand binding affinity) using five different GNN architectures, with minimal computational overhead.

## Strengths

- **Novel graph construction with simultaneous theoretical guarantees:** The paper proves that SCHull graphs achieve connectivity, sparsity (edge-to-node ratio ≤ 3, Corollary 3.2), and rigidity (Theorem 3.6) — properties that prior constructions (radial cutoff, kNN, chemical graphs) cannot simultaneously guarantee, as highlighted in Table 1. The connection to Stoker's theorem for convex polyhedral graphs (Theorem 2.1) is elegant and principled.

- **Consistent empirical gains across diverse tasks, models, and scales:** SCHull improves performance when integrated into five different GNNs (DimeNet, SphereNet, LEFTNet, ProNet, GVP-GNN) across all four benchmarks. The improvement grows with graph size (Figure 5 shows ~1% gain on ≤150 nodes increasing to ~11% on >450 nodes), supporting the claim that connectivity becomes increasingly important for large molecules where radial cutoff graphs tend to disconnect.

- **Hyperparameter-free, simple integration, and minimal overhead:** The construction runs in O(m log m) time and requires no threshold tuning. Table 4 shows training epoch time increases only marginally (e.g., ProNet-Backbone: 1.83s vs 1.93s). The integration is straightforward — take the union of edge sets and concatenate node features.

- **Synthetic experiment validates the rigidity claim directly:** The NestedSquares task (Section 3.3, Table 2) is designed so that radial-cutoff and kNN graphs fail because edge lengths alone cannot distinguish rotations, while SCHull's rigidity (via dihedral angles) allows a one-layer MPNN to achieve near-perfect MSE of 0.0000, outperforming all baselines by nearly an order of magnitude. This cleanly validates the theoretical separation-power claim of Theorem 3.6.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation to attribute gains to specific properties:** SCHull is integrated with base graphs by simply taking the union of edges and concatenation of node features. The paper attributes empirical gains to "connectivity and sparsity" and "rigidity," but there is no ablation controlling for the effect of adding any sparse global connectivity. A simple baseline — e.g., adding a minimal spanning tree, a Delaunay triangulation, or even a few random long-range edges to make the base graph connected — would show whether the benefit comes from SCHull's specific convex-hull structure or from any mechanism that provides global connectivity. Without this, the empirical contribution is partially confounded. This is the most significant weakness, as it limits the ability to attribute improvements to the paper's core theoretical claims.

### Minor

- **Synthetic experiment is too small to be a standalone validation of the theoretical claim:** The NestedSquares dataset comprises only 10 graphs total (6 train, 2 test, 2 validation). While the experiment is well-designed as a proof-of-concept and does cleanly demonstrate the principle, the extremely small dataset size means the large gap in Table 2 could be partly influenced by random seed luck or overfitting. A larger-scale synthetic benchmark (even moderately scaled, e.g., hundreds of graphs with varying complexity) would substantially strengthen the connection between Theorem 3.6 and empirical validation. As it stands, this experiment is illustrative rather than confirmatory.

### Trivial
- The paper references appendices (e.g., Appendices H.2, I.2) but does not include them in the main text. This is a formatting issue common to submissions with page limits.
- Rare edge cases (points at the exact center of mass) are discussed generically (lines 102-108) but a brief practical handling note (e.g., "in practice such points are discarded or perturbed by epsilon") would be helpful for implementers.

## Nice-to-Haves
- An experimental comparison against power graphs (Sverdlov & Dym, 2024), which the paper discusses only textually in Remark 3.8, would strengthen the paper by directly situating SCHull against the closest theoretical competitor.
- Timing breakdown including the preprocessing overhead of the convex hull construction (not just per-epoch training time) would help practitioners assess the full efficiency picture.
- For the NestedSquares experiment, scaling to a larger synthetic dataset (even just 50–100 graphs) would increase confidence in the empirical demonstration of Theorem 3.6.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No uncertainty reported for Tables 3, 4, and 5"**: The paper explicitly states (line 199) that experiments are run five times with standard deviations recorded. The tables are embedded as images in the PDF, so their content cannot be verified from the text extraction, but the paper's stated methodology indicates standard deviations are reported. This criticism likely reflects a parser artifact rather than an author omission.

- **"Disconnect between theory and experiment"**: The critic claims Theorem 3.6 (about maximally expressive GNNs with depth 1 on SCHull alone) does not support experiments (which use real GNNs on combined graphs). This misunderstands standard practice: the theorem establishes what is possible in principle (separation power), while experiments test practical utility in real settings. The NestedSquares experiment directly tests the theorem. Using real (non-maximally-expressive) GNNs on combined graphs for practical benchmarks is standard and does not create a "disconnect."

- **"Code not mentioned with repository URL"**: For a double-blind submission, not including an identifiable repository URL is standard practice. The paper promises code release (line 271).

- **"Does not discuss rare cases violating generic condition"**: The paper explicitly discusses this (lines 102-108), assumes the generic condition for analysis, and notes (Lemma 3.4) that generic point clouds satisfy it with probability 1.

- **"Theoretical proof details relegated to appendix"**: The paper references appendices that exist in the original submission but are stripped by the parser. This is a PDF extraction artifact, not an author omission.

- **Demand for experimental comparison with power graphs**: This is a reasonable suggestion but not a weakness; moved to Nice-to-Haves.

## Novel Insights

The most striking observation across the reviews is the tension between the paper's strong theoretical framing and the relatively weak empirical attribution. The paper proves that SCHull has three theoretically desirable properties (connectivity, sparsity, rigidity), shows that SCHull helps empirically, but never tests whether the *specific* structure of SCHull (convex hull on the sphere) is what drives the gains versus any method for adding global connectivity. This gap means the paper's strongest contribution remains the theoretical construction itself, while the empirical claims would benefit from sharper experimental design. The NestedSquares experiment is the one place where the theory-to-evidence link is clean, making its small scale particularly unfortunate.

## Suggestions

1. **Add an ablation study** that compares SCHull integration against other methods of adding global connectivity to a base graph (e.g., minimum spanning tree, Delaunay edges, a small number of strategically added long-range edges). This is the single most important improvement, as it would directly test whether SCHull's specific structure — and its rigidity guarantee — drives the empirical gains, or whether any connected sparse augmentation would suffice.

2. **Scale up the NestedSquares experiment** to a larger synthetic benchmark with hundreds of graphs, varying complexity (e.g., multiple nested shapes, varying numbers of nodes), to provide a more robust validation of Theorem 3.6.

3. **Report standard deviations explicitly in all tables** (if not already present in the image-based tables — the paper states they are recorded).

## Score and Decision

The paper presents a genuinely novel, theoretically motivated graph construction with strong formal guarantees (sparsity ≤ 3, connectivity, rigidity). The empirical results show consistent improvements across a diverse set of tasks and models. The main weakness is the absence of an ablation that isolates whether the gains come from the specific convex-hull structure or simply from adding any global connectivity — this limits attribution but does not invalidate the core contribution. The paper's theoretical analysis is sound, the method is practically useful and easy to integrate, and the experimental coverage (four tasks, five GNNs) is commendable. A major revision adding an ablation study would substantially strengthen the paper.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>