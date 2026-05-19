- Decision: Reject
- Avg Score: 6.50
- Scores: 10, 6, 5, 5
Now I have a solid understanding of the paper and can verify the reviewer claims against the actual text. Let me synthesize the final review.

## Summary

This paper proposes CeGNN, a graph neural network for spatiotemporal PDE learning that introduces two architectural innovations: (1) a **cell-embedding mechanism** that upgrades message passing from node-edge to node-edge-cell, incorporating volumetric (triangle-level) information; and (2) a **feature-enhanced (FE) block** that enriches latent node features via an outer-product operation treated as higher-order basis function expansion. Experiments on four synthetic PDE systems (Burgers, FitzHugh-Nagumo, 2D/3D Gray-Scott) and one real-world ocean dataset (Black-Sea) show CeGNN achieving substantially lower RMSE than baselines including MeshGraphNets and MP-PDE, with up to ~14× improvement on Gray-Scott systems.

## Strengths

- **Novel higher-order message passing via cell attribution.** The paper introduces a learnable cell (triangle-level) feature that enables information flow from volume → edge → node, upgrading beyond the standard node-edge scheme in MeshGraphNets and MP-PDE. This is a concrete architectural innovation clearly described in Section 3.2.2 (Processor) and Figure 4. The ablation study (Table 3) confirms that removing cell features degrades performance across all datasets.

- **FE block is effective and generalizable.** The feature-enhanced block (Algorithm 1, Figure 3) is well-motivated: it treats latent features as basis functions and creates second-order terms via outer products. Table 2 shows adding FE to MGN improves RMSE by 30–62% on synthetic PDEs; Table 3 shows removing FE from CeGNN consistently increases error (e.g., on 2D FN from 0.00364 to 0.00910). This demonstrates the block's value both as a component of CeGNN and as a plug-in for other architectures.

- **Order-of-magnitude error reduction on multiple PDE systems.** In Table 1, CeGNN achieves 0.00248 RMSE on 2D Gray-Scott vs. the best baseline (MGN: 0.02917) and 0.00138 vs. 0.01925 on 3D Gray-Scott — improvements of ~11.8× and ~13.9×, directly supporting the abstract's "up to 1 order of magnitude" claim (which is correctly qualified to "several PDE systems").

- **Nuanced analysis of FE-attention conflict.** The paper (Section "Feature-enhanced effect") explains *why* the FE block harms GAT/GATv2 performance: outer-product features disrupt the global normalization of attention weights. This demonstrates genuine understanding of the method's limitations and provides a principled diagnostic for the failure case.

- **Efficiency comparison at similar parameter budgets.** Table 4 shows CeGNN (4 layers, 1.48M params, 17.31 s/epoch) achieving better RMSE than MGN with 12 layers (1.44M params, 20.90 s/epoch) and MP-PDE with 12 layers (1.23M params, 17.44 s/epoch), partially mitigating the concern that gains come purely from additional capacity.

## Weaknesses

### Fatal

None.

### Major

- **Parameter-count disparity undermines the headline comparison (Table 1).** CeGNN (1.48M params) is compared against MGN (0.51M) and MP-PDE (0.53M) — a ~3× gap. The paper's attempt to control for this (Table 4) uses *deeper* MGN and MP-PDE (12 layers) to match parameter counts, but deeper networks suffer from optimization difficulties and oversmoothing that are independent of capacity. A *wider* baseline (increased latent dimension, same depth) would be the proper control. Without it, the reader cannot fully attribute CeGNN's gains to the proposed architecture rather than to additional capacity. This weakens but does not invalidate the central claim, since the ablation study (Table 3) shows that even "w/o Cell" (MGN + FE, ~0.97M params) and "w/o FE" (cell only, ~0.97M params) both outperform the 0.51M-param MGN — but both variants still have more parameters.

- **Training strategy inconsistency for MP-PDE.** The Experimental Setup section (line 174) states: *"For fairness, we set the latent dimension to 128 and utilize the one-step training strategy (i.e., one-step forward, one-step backward) for all tasks."* However, the Results section (line 226) states: *"Although MP-PDE is trained by the multi-step prediction strategy during the training stage, its results are only slightly better than MGN on the BS dataset."* These are directly contradictory. If MP-PDE was in fact trained with multi-step rollouts while other baselines used one-step, the comparison is unfair. The paper must clarify which protocol was actually used and, if there was a discrepancy, rerun with a consistent protocol. This inconsistency undermines trust in the entire experimental comparison.

### Minor

- **Modest real-world improvement vs. core narrative.** On the Black-Sea dataset (irregular mesh, real-world), CeGNN achieves 8.4% improvement over MP-PDE. The paper's motivation emphasizes generalization to complex irregular domains, so the modest gain on the only irregular-mesh dataset weakens the narrative. The paper would benefit from deeper analysis of *why* the improvement is smaller here (mesh coarseness? noise? cell structure less informative for this problem?).

- **FE block algorithm lacks tensor contraction specification.** Algorithm 1 (step 4) states: *"Multiply the masked states $\hat{\mathbf{h}}^{*l*}$ with the weight $\mathbf{W}^{l}$ to construct the final states."* The masked states have shape $N \times D \times D$ and the weight tensor $D \times D \times D$. The output $N \times D$ is not uniquely determined without specifying which axes are contracted. This ambiguity affects reproducibility.

- **Cell mechanism assumes triangular meshes without discussion.** The cell feature $c_{ijk}^{l+1}$ (Eq. 6) uses exactly three nodes per cell, which is natural for triangles. The paper claims applicability to "arbitrary geometric domains" but does not discuss generalization to polygonal meshes (quads, mixed elements) commonly found in real-world applications.

- **Generalization evaluation lacks quantitative rigor.** The generalization test (Figure 5 violin plots) is presented only qualitatively. No mean ± std over random seeds, no statistical significance tests, and no direct comparison of generalization variance between methods. Given that baselines also generalize reasonably well, the *relative* robustness of CeGNN is unclear.

- **Ablation pattern inconsistency not discussed.** Table 3 shows that on 2D FN and 2D GS, removing FE hurts less than removing cell, but on 3D GS the pattern reverses. The paper does not comment on this, missing an opportunity to understand when each component matters most.

### Trivial

- None (the minor issues above are the appropriate level of concern).

## Nice-to-Haves

- Reporting mean ± std over multiple random seeds would improve statistical reliability.
- A wider (rather than deeper) parameter-matched baseline (e.g., MGN with latent dimension ~220 to match 1.48M params) would cleanly resolve the parameter-count concern.
- Discussion of GPU memory trade-offs for the FE block (45.87 GB vs. ~33 GB) with smaller FE variants would help practitioners assess the cost-benefit.

## Removed Points

- **Criticism about the abstract claim needing qualification**: The abstract already says *"up to 1 order of magnitude on several PDE systems"* — it is correctly qualified. Removed.
- **Criticism about missing Black-Sea dataset details in appendix**: The supplementary table is referenced; the parser strips appendix content. Removed (per hard rule).
- **Criticism about missing related works (higher-order GNNs)**: Per instructions, I cannot verify existence of uncited works. Removed.
- **Criticism about no confidence intervals**: Single-run evaluation is common practice in this field (mesh-based GNN PDE solvers). Downgraded from weakness to nice-to-have.
- **Strength Finder's generic praise** ("important problem," "interesting question"): Removed as generic/superficial. Only concrete, evidence-grounded strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives converge on the same core tension: the paper has genuinely novel architectural ideas (cell-embedding + FE block) and compelling results on synthetic PDEs, but the experimental validation is undercut by a parameter-count confound and a training-protocol inconsistency that need resolution before the claims can be fully trusted.

## Suggestions

1. **Resolve the MP-PDE training inconsistency.** State clearly in a revision whether all models used one-step training (and correct the contradictory sentence in Results) or run a controlled experiment with all models using an identical protocol.

2. **Add a wider baseline control.** Train MGN and MP-PDE with the same depth (4 layers) but a larger latent dimension to reach ~1.5M parameters. If CeGNN still outperforms them at equal parameter budgets, the architectural advantage is cleanly established.

3. **Clarify the tensor contraction in Algorithm 1** by specifying which axes of the $N \times D \times D$ masked states and $D \times D \times D$ weight tensor are summed to produce the $N \times D$ output.

4. **Add a quantitative summary for the generalization test** — e.g., mean ± std rollout RMSE over multiple initial conditions — to move beyond visual inspection of violin plots.

5. **Discuss the ablation pattern inconsistency** (why removing cell vs. FE has different relative importance on different datasets) to deepen understanding of when each component contributes.
