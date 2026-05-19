- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 8, 3, 3
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

The paper proposes Marlene, a deep learning method for inferring time-varying gene regulatory networks (GRNs) from single-cell RNA sequencing time series. The architecture combines three components: (1) permutation-invariant gene featurization via PMA (Pooling by Multihead Attention), (2) self-attention-based graph construction with GRU-evolved projection weights (inspired by EvolveGCN but adapted to the feature-graph setting), and (3) MAML meta-learning treating each cell type as a task to enable recovery of networks for rare cell types. The model is trained on a cell-type classification objective rather than expression reconstruction. Marlene is evaluated on three public datasets (SARS-CoV-2 vaccination, human lung aging atlas, mouse lung fibrosis) and shows statistically significant improvements over existing static and dynamic baselines, along with biologically meaningful enrichment of time-dependent regulatory edges.

## Strengths

- **Statistically significant improvements over multiple baselines across datasets.** In the SARS-CoV-2 vaccination dataset, Marlene outperforms all competing methods (GENIE3, GRNBoost2, PIDC, SCODE, DeepSEM, TVGL, Graphs4mer) on 5 out of 7 cell types, with highly significant FDR values (e.g., FDR ≤ 1e-67 for B cells against RegNetwork, line 136). This is a concrete, measured result directly supporting the method's effectiveness.

- **Demonstrated capability for rare cell types via meta-learning.** On the HLCA dataset, non-classical monocytes (only 138 cells in one age group) still yield >800 known TF-gene links with FDR ≤ 1e-27 across transitions (line 171). This provides direct evidence that MAML helps recover networks for cell types with very limited data.

- **Biologically plausible temporal dynamics captured by IoU and enrichment analyses.** Marlene's graph transitions show low IoU during the early post-vaccination period (days 0→2) and higher stability later, consistent with a strong early immune response followed by stabilization. Other methods either show constant high IoU (TVGL) or decreasing IoU (Graphs4mer), both biologically less plausible (line 146). Additionally, genes added by Marlene at day 2 are significantly enriched for immune-relevant terms like "Interferon Gamma Response" (FDR = 1e-6) and "TNF-alpha Signaling via NF-kB" (line 155).

- **Cross-species validation.** Marlene outperforms competing methods on 4 out of 6 cell types in the mouse lung fibrosis dataset against RegNetwork, and captures increasing IoU over time reflecting lung regeneration (lines 187-189), showing generalization beyond human data.

- **Novel architecture adaptation for the feature-graph setting.** The paper adapts EvolveGCN's GRU-based weight evolution to evolve self-attention projection weights (key/query matrices) rather than graph convolution weights, and combines this with PMA-based gene featurization to handle the unique structure of scRNA-seq data (graphs of genes as features, with cells as samples). This is a clear technical adaptation to a novel problem domain.

## Weaknesses

### Fatal
None.

### Major

- **The primary evaluation metric does not directly validate the *dynamic* aspect of the recovered networks.** The central claim is recovery of *time-varying* GRNs, yet the main validation metric (overlap with TRRUST/RegNetwork) measures how many predicted edges match *static* known interactions at any individual time point. This overlap cannot distinguish whether a method truly captures temporal rewiring or simply recovers different static networks per time point that all happen to match known interactions. The IoU analysis and enrichment of dynamically added genes provide *indirect* support (and the enrichment results are biologically meaningful), but they do not substitute for a controlled experiment with known ground-truth dynamic edges (e.g., synthetic data or perturbation experiments). The paper acknowledges other limitations (memory, vanishing gradients) but does not flag this evaluation gap in the Limitations section.

- **Ablation studies are missing for key architectural components.** The model has three notable design choices — GRU-based weight evolution vs. independent self-attention per time point, MAML meta-learning vs. joint training across cell types, and PMA featurization vs. simpler aggregation (e.g., mean pooling) — yet none are ablated. Without isolating these components, it is unclear which drives the reported improvements. The comparison against static baselines applied per time point independently provides some context for the GRU component, but this is not a controlled ablation.

### Minor

- **Two baselines (TVGL and Graphs4mer) appear in the results with inadequate documentation.** TVGL is cited only via a general reference in the introduction (Hallac2017, line 30) but is never described in the Methods or Experiments — its parameterization, tuning, and implementation for this task are absent. Graphs4mer (line 146) appears in the results without any citation or method description at all. This undermines the reproducibility of the comparison and the ability to assess whether these baselines were fairly configured.

- **No sensitivity analysis for the sparsification threshold.** The paper selects the top 2% of edges for all methods when evaluating against TRRUST/RegNetwork (line 126) but does not discuss how this threshold was chosen or whether the reported advantages are robust across different thresholds (e.g., 1%, 5%). Since the threshold determines which edges are counted as "discovered," it could affect the comparison.

- **Multiple comparisons are not aggregated.** Fisher's exact tests are performed per time point per cell type, leading to many comparisons. While FDR correction is applied per test, the paper does not report whether the overall pattern (e.g., Marlene's superiority across cell types) is significant when aggregated (e.g., via a paired test or meta-analysis).

### Trivial

- The restriction to TRRUST TFs (line 87) limits the method to known transcription factors, meaning any novel regulators not in the database cannot be discovered. This is inherent to the design choice and could be stated more explicitly as a limitation rather than left implicit.

## Nice-to-Haves

- **Synthetic data or perturbation-based validation.** The paper's central claim about *dynamic* networks would be substantially strengthened by a controlled experiment with known ground-truth temporal edges (e.g., synthetic time series with known switching regulators, or a TF knockout experiment where downstream changes are known). This is a suggestion for strengthening, not a deficiency given current community standards — most GRN inference papers face the same limitation.

- **Ablation of the GRU component specifically.** Replacing the GRU-evolved weights with independently fitted self-attention per time point would directly quantify the value of temporal coupling in the model.

## Removed Points

These points from the reviewers were assessed and removed or downgraded:

- **"Loss function mismatch — model might learn to ignore the graph and output a fixed vector per batch"** (Harsh Critic): This is speculative. The graph is used integrally in the forward pass (X^{TF} A^T, lines 89-92), and the model must produce logits over *all* cell types, not just recognize which homogeneous batch it is in. The classification objective was explicitly motivated against autoencoder alternatives (line 54). Downgraded from major claim to removed as unsubstantiated speculation.

- **"The model might learn to copy information via self-attention"** (Harsh Critic): No mechanism or evidence is provided for this concern; it is a generic speculation without specific grounding in the paper's architecture.

- **"Missing code/reproducibility details — number of training runs, variance across seeds"** (Harsh Critic): Single-GPU runs taking "a few minutes" with fixed hyperparameters are provided. Reporting variance across random seeds would strengthen the paper but is not uncommon to omit in a method paper. Downgraded (removed).

- **Strength Finder claim about "novelty"** is sufficiently specific to the architecture and is retained as a strength. However, the Strength Finder's generic phrasing about "addressing an important problem" was dropped as it was not a concrete, paper-specific strength.

## Novel Insights

A genuinely novel observation arises from comparing the two *dynamic* baselines (TVGL and Graphs4mer) against Marlene's temporal profiles: each method produces a qualitatively different IoU-over-time signature (constant high for TVGL, decreasing for Graphs4mer, U-shaped for Marlene). The paper argues — persuasively, though not definitively — that only Marlene's pattern matches the expected biology (strong early rewiring → stabilization). This suggests that IoU dynamics could serve as a *sanity check* for dynamic GRN methods even without ground-truth edges: a method that fails to produce a biologically plausible temporal profile is likely flawed, and the specific shape of the profile contains information about the method's inductive biases. This meta-observation about evaluation methodology is worth developing further.

## Suggestions

1. Add an ablation study comparing the full model against two variants: (a) independent self-attention per time point (no GRU), and (b) joint training across cell types (no MAML). This would directly isolate the contributions of the two key design claims.

2. Add a sensitivity analysis for the top-2% sparsification threshold (e.g., 1%, 2%, 5%) to confirm that the reported improvements are not artifacts of this choice.

3. Provide a brief description of how TVGL and Graphs4mer were configured for this task (software package, parameters, tuning), and add a citation for Graphs4mer.

4. Report the rare cell type results with and without MAML in a dedicated figure or table to substantiate the claim that meta-learning specifically benefits low-data regimes.

5. Either add synthetic time-series validation with known ground-truth dynamic edges or explicitly reframe the central contribution to acknowledge that dynamic correctness is inferred indirectly rather than directly measured.
