- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper identifies a critical bias in bioactivity prediction benchmarks: models can exploit pocket-only features because datasets like PDBbind have few ligands per pocket and traditional Pearson/Spearman metrics measure inter-pocket differences rather than intra-pocket discrimination. To address this, the authors construct the SIU dataset — a million-scale structural dataset (5.34 M conformations, 1.38 M labels, 50× larger than PDBbind) with multiple small-molecule ligands per protein pocket, built via multi-software docking with a consensus filter. They redefine evaluation by computing correlations *within* each pocket before averaging across pockets (Pearson*/Spearman*). Experiments show that this redefined task produces a dramatic performance drop compared to traditional metrics, confirming that prior evaluations overestimated model capability.

## Strengths

- **Empirical diagnosis of shortcut learning (Fig. 1A,B):** The paper shows that a pocket-only baseline (no ligand input) matches or exceeds full complex models on Atom3D LBA, cleanly demonstrating that existing benchmarks permit a degenerate solution. This motivation is clearly evidenced and strengthens the case for the proposed changes.

- **Large-scale, systematically constructed dataset:** SIU provides 1.38 M bioactivity labels across 214 k molecules and 1,720 protein targets, organized by label type (Kd, Ki, IC50, EC50). The multi-software docking consensus (Glide + GOLD + Vina, ≥2 agreeing) with a validated 2 Å RMSD cutoff (Fig. 3A) is a principled quality-control approach, and the scale is a genuine advance over PDBbind (~20 k complexes).

- **Well-motivated per-pocket evaluation metrics:** Equations (2)–(3) define Pearson* and Spearman* within pockets, directly targeting the diagnosed bias. Figure 5 shows the metric causes a large drop (e.g., Ki Pearson from 0.485 to 0.036), empirically confirming that traditional across-pocket metrics overestimate models' ability to discriminate among ligands for the same target. The logic that a pocket-only model yields NaN on Pearson* (constant predictions = undefined correlation) is theoretically sound.

- **Separation of label types with statistical justification:** Figure 4 provides pairwise t-test p-values and distribution plots across Kd, Ki, IC50, EC50, demonstrating that mixing label types introduces systematic bias. Organizing the dataset by label type is a practical and well-justified design choice.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Docking validation covers only co-crystal redocking, not held-out complexes.** Figure 3A validates the consensus pipeline by redocking known co-crystal ligands back into their own pockets. However, for the vast majority of SIU molecules (which lack co-crystal structures), there is no external validation that the pipeline recovers near-native poses. A consensus among wrong poses could still be wrong. The paper does not discuss this limitation or provide validation on a held-out set of crystallized complexes not used during pipeline calibration (e.g., recent PDB entries). While redocking validation is standard practice, the paper's claim of "high-quality structural data" would be strengthened by acknowledging the inherent uncertainty of docking-generated poses.

2. **PDBbind vs. SIU comparison uses only one model (Uni-Mol) in the single-task setting.** Table 2 compares Uni-Mol trained on PDBbind vs. SIU (0.6 and 0.9), but only this single architecture is used. Table 1 shows multiple models (3D-CNN, GNN, Uni-Mol, ProFSA) on SIU alone. Demonstrating the cross-dataset comparison with additional architectures (at least a 3D-CNN or GNN) would strengthen the claim that SIU consistently improves performance across model types.

3. **Statistical reliability of the per-pocket metric is unanalyzed.** The Pearson* metric averages correlations across pockets via mean pooling, but the paper does not report: (i) the distribution of ligands per pocket, (ii) the number of pockets that meet a minimum n_t threshold to yield a meaningful correlation, or (iii) the variance or bootstrap standard error of the metric. Low Pearson* values could partly reflect high-variance estimates from pockets with very few ligands rather than genuinely harder discrimination. The paper should specify a minimum number of ligands per pocket for inclusion and report how many pockets contribute to the final average.

4. **No limitations or future work section.** The paper does not discuss limitations of its approach, such as: (a) the uncertainty in docking-generated poses for novel molecules, (b) label noise from diverse experimental protocols in ChEMBL/BindingDB, (c) the requirement that a dataset have multiple ligands per pocket for the metric to be applicable, or (d) potential sources of remaining bias. A brief limitations section would improve the paper's scholarly rigor.

5. **Conditional deduplication threshold is not justified.** The paper applies ECFP-based deduplication (Tanimoto ≥0.8) only to targets with >2,146 molecules (the 90th percentile). The rationale for this conditional threshold is not explained — why not apply it uniformly, or use a statistically principled per-target cutoff? This does not undermine the dataset but the design choice merits justification.

### Trivial
None that are not parser artifacts.

## Nice-to-Haves

- **Pocket-only ablation on SIU:** Directly testing a pocket-only model on SIU with both traditional and Pearson* metrics would close the loop by empirically confirming that the new metric is immune to the shortcut (yielding near-NaN values) while the traditional metric is not.
- **Controlled PDBbind comparison on a common held-out test set:** Comparing on the same set of held-out pockets (e.g., recent PDBbind refined complexes) would eliminate any ambiguity from different test set compositions.
- **Comparison against single-docking-software baselines:** The paper claims consensus voting is superior to single software or docking-score-based selection, but does not provide experimental comparison.
- **Virtual screening enrichment analysis:** Evaluating whether SIU-trained models produce better enrichment factors would further demonstrate real-world utility for drug discovery.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unexpected interpretation or contradiction that was not already present in the paper.

## Suggestions

1. Add a brief limitations section acknowledging docking pose uncertainty, label noise, and metric sparsity concerns.
2. Report the distribution of ligands per pocket (mean, median, min, max) and specify a minimum n_t for the per-pocket correlation to be computed.
3. Extend the PDBbind vs. SIU comparison to at least one more model architecture (e.g., 3D-CNN or GNN).
4. Justify the conditional deduplication threshold, or replace it with a uniform strategy.
5. Add a sentence defining "Pearson*" / "Spearman*" explicitly in the main text (currently defined only in figure captions and equations).

---
