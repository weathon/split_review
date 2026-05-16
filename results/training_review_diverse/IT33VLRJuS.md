Now I have all the evidence needed. Let me compose the final authoritative review.

## Summary

This paper presents Marlene, a deep learning framework for inferring time-varying gene regulatory networks (GRNs) from single-cell RNA-seq data. The architecture has three main components: (1) a PMA (Pooling by Multihead Attention) operator to featurize genes across multiple cells per time point, (2) a self-attention module whose key/query weights evolve via GRUs to produce dynamic adjacency matrices, and (3) a MAML-based meta-learning procedure treating each cell type as a task to enable recovery of networks for rare cell populations. The method is evaluated on three scRNA-seq datasets (SARS-CoV-2 vaccination, lung aging, and mouse fibrosis) against five static and two dynamic baselines.

## Strengths

- **Novel architecture adapted to the "graphs of features" problem in scRNA-seq.** The paper correctly identifies that standard temporal graph learning methods assume node feature vectors, whereas scRNA-seq data gives a cell-by-gene matrix. The PMA-based gene featurization (converting a set of cells into gene feature vectors) followed by self-attention with GRU-evolved weights is an inventive and well-motivated adaptation of ideas from Set Transformers and EvolveGCN (Section 2.2). This is a genuine technical contribution.

- **Consistent outperformance of static baselines on overlap with known regulatory databases.** Across three diverse datasets, Marlene recovers significantly more validated TF-gene interactions (measured via Fisher's exact test against TRRUST and RegNetwork) than five static methods (PIDC, GENIE3, GRNBoost2, SCODE, DeepSEM) applied independently per time point. For example, in the SARS-CoV-2 vaccination dataset, Marlene recovers >800 RegNetwork links per time point in B cells (FDR ≤ 1e-67), while the second-best method (SCODE) peaks at 579 links at a single time point (FDR ≤ 1e-15) (Figure 2).

- **Biologically realistic temporal dynamics.** Marlene's learned networks show the expected pattern of substantial rewiring immediately after perturbation (low IoU from day 0→2 in the vaccination dataset) followed by stabilization (higher IoU later). Static methods produce uniformly low IoU, TVGL yields near-constant IoU, and Graphs4mer shows decreasing IoU — none of which match the expected biological response (Figure 3a). Genes added at day 2 by Marlene are enriched for immune-response pathways (e.g., Interferon Gamma Response in dendritic cells, FDR = 1e-6), while other methods show weaker or less consistent enrichment (Figure 3b).

- **Computational efficiency.** Marlene trains in only a few minutes on a single RTX 3060 GPU (Section 3), making it practical for typical scRNA-seq datasets.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation of the MAML meta-learning component.** The paper claims that MAML "enables the reconstruction of dynamic graphs even for rare cell types" (Section 2.3) and presents results for low-cell-count types (e.g., non-classical monocytes with 138 cells, recovering >800 RegNetwork links with FDR ≤ 1e-27). However, there is **no experiment comparing Marlene with vs. without MAML**. The observed performance on rare cell types could reflect the robustness of the base architecture, the gradient clipping mentioned in Section 2.3, or some other aspect of the training procedure. Without this ablation, the meta-learning contribution — which is one of the paper's three stated contributions — remains unvalidated. This is the most consequential gap in the evaluation.

2. **No ablation of the GRU or self-attention components.** The method combines PMA featurization, self-attention for graph construction, GRU for temporal evolution, and a cell-type classification objective. No experiment isolates which components drive the observed performance. For instance, a version with a shared static adjacency across time points (removing the GRU), or with mean-pooling instead of PMA, would demonstrate the necessity of the proposed designs. While the overall system works well, the paper cannot attribute this to any specific architectural choice, which weakens the technical contribution.

3. **Reliance on overlap with incomplete databases as the primary accuracy metric without false-positive analysis.** The evaluation uses Fisher's exact test for overlap with TRRUST and RegNetwork, both of which are known to be incomplete and biased toward well-studied interactions. The top-2% edge selection partially controls for network size, but the paper does not report precision or examine whether edges *not* in the databases are biologically plausible. The GSEA enrichment analyses provide valuable orthogonal validation, but they are limited to one transition in one dataset. The paper briefly acknowledges database incompleteness ("The differing results between two databases may reflect their incomplete coverage," line 187), but this limitation is not discussed in the formal Limitations section (Section 4) where it would carry appropriate weight.

### Minor

1. **No variance or reproducibility reporting.** No error bars, standard deviations, or multiple-run statistics are reported anywhere. Given stochasticity in MAML inner-loop optimization, random seeds, and batch composition, the stability of results is unknown. While single-run evaluation is not uncommon in GRN inference, the paper's claims about statistical significance (FDR values) would be strengthened by reporting variance across runs.

2. **Ambiguous methodological details.** (a) The `TopK(G_t)` operation (line 82) is not explained — what is being thresholded (features per gene? values per row?) and what value of K is used? This is a hyperparameter that affects the GRU input. (b) The softmax axis in the self-attention (line 85–86) is ambiguous. Since A_t is g×p (targets × TFs), the softmax could normalize per target (row-wise, indicating a soft selection of TFs) or per TF (column-wise). The paper should state this explicitly. These details matter for reproducibility.

3. **Dynamic baselines compared only on IoU, not on overlap metrics.** TVGL and Graphs4mer appear only in the IoU analysis (Figure 3a) and are absent from the main overlap evaluation (Figures 1, 4a). While there are practical reasons for this (TVGL produces undirected graphs; Graphs4mer requires graph-structured inputs), the paper's central claim about recovering *time-varying* networks would be stronger if at least one dynamic baseline were compared on edge-level overlap. The TVGL comparison in the fibrosis dataset (line 187) is a step in this direction but is limited to one dataset.

4. **No enrichment comparison for the HLCA aging dataset.** For the SARS-CoV-2 dataset, the paper reports GSEA enrichment for Marlene and other methods (Figure 3b). For the HLCA dataset (Figure 4b), only Marlene's enrichment is shown — the paper says other methods "contained fewer marker genes" but does not report their significance levels. A side-by-side comparison similar to Figure 3b would strengthen the claim that Marlene uniquely captures relevant biology.

### Trivial

- The claim in the Introduction (line 33) that "prior methods do not directly account for the fact that multiple cells are profiled for each time point" is slightly overstated — some methods (e.g., SCODE) can handle multiple cells through distributional assumptions or pseudotime — but this is a framing nuance, not a technical error, and does not affect the paper's contribution.

## Nice-to-Haves

- **Synthetic data validation.** Generating synthetic scRNA-seq data with known ground-truth dynamic networks (edges that change at known times) would allow direct precision/recall evaluation and sidestep the database bias issue. This would substantially strengthen the paper.
- **Ablation of the PMA operator** (e.g., replacing it with mean-pooling) to justify the architectural complexity.
- **Null-model control for GSEA** (e.g., randomly permuting time-point labels) to ensure that the temporal enrichment patterns are not artifacts of the method.
- **Reporting of GRU hidden size, number of layers, dropout rates, and optimization schedule** beyond what is currently provided (batch size, learning rates, number of inner steps).

## Removed Points

These points were flagged for removal because they do not hold up under verification against the paper:

- *"The evaluation does not test the core dynamic contribution because baselines do not even attempt to model dynamics"* — **Overly strong framing.** The paper does compare against two dynamic methods (TVGL, Graphs4mer) on the IoU metric, and the results show that Marlene produces more realistic temporal patterns. The issue is more about the *absence of dynamic methods from the overlap metric* and the *lack of ablations*, both of which are already captured in Major/Minor weaknesses above. The paper's dynamic contribution is partially tested.

- *"The paper does not acknowledge that the evaluation relies on heavily biased databases"* — **Partly inaccurate.** The paper does acknowledge this at line 187: "The differing results between two databases may reflect their incomplete coverage, highlighting the need for further refinement." The acknowledgment is present but brief. This nuance is absorbed into Major weakness #3.

- *"The Fisher test p-values should be interpreted with caution given the small overlap sizes"* — **Generic concern that applies to all Fisher tests with sparse overlap.** The test's design accounts for the full contingency table (total possible edges, database edges, predicted edges, overlap). This is a standard application of Fisher's test and not a specific weakness of this paper.

- *"Prior methods do not directly account for multiple cells per time point' is misleading"* — **Disagreement on framing.** The paper's claim is about how these methods are *applied* (independently per time point), not about their internal capabilities. SCODE uses pseudotime for ordering, not for pooling multiple cells at a discrete time point — the distinction is defensible.

- *"Code and data availability: Not mentioned"* — This may be in a stripped appendix section, in accordance with the submission format.

- *"The method requires known TF lists for each species; in non-model organisms this may not be available"* — This is a general limitation of TF-focused GRN inference, not specific to Marlene. Most GRN methods require known TF lists.

## Novel Insights

The most interesting insight to emerge from the reviews is that the paper's three claimed contributions (PMA featurization, GRU-evolved self-attention, MAML) are asserted without individual validation, yet the combined system produces clearly superior results on three diverse datasets. This creates a tension: the architecture-level contribution is novel and the empirical results are strong, but we do not know *why* Marlene works — whether the performance comes from the PMA pooling, the temporal GRU constraint, the self-attention inductive bias, the MAML meta-learning, or simply the increased parameter count. The reviews collectively suggest that the paper's empirical contributions (the method works well on real data) are more solid than its scientific contributions (understanding why it works), and that a set of well-designed ablations could elevate this from a "promising method" paper to a genuinely insightful one.

## Suggestions

1. **Add ablation studies as the priority revision.** Compare Marlene against: (a) itself without MAML (standard training), (b) itself with a static adjacency shared across time (removing the GRU), and (c) itself with mean-pooling instead of PMA. Even one of these (especially the MAML ablation) would significantly strengthen the paper's claims.

2. **Report variance** across at least 3 random seeds/initializations for the overlap metrics on at least one dataset, to establish result stability.

3. **Clarify the TopK operation** (what is being thresholded, what K value is used) **and the softmax normalization axis** in the self-attention — this is necessary for reproducibility.

4. **Include the dynamic baselines (TVGL, Graphs4mer) in the overlap comparison** if feasible given their output format, adding a brief justification if they cannot be directly compared.

5. **Expand the Limitations section** to explicitly acknowledge the database-bias issue and the lack of novel-edge validation.

## Score and Decision

The paper makes a genuine architectural contribution to an important problem and demonstrates meaningful empirical results across three datasets. However, the evaluation has significant gaps: none of the three architectural/training components (MAML, GRU, PMA) are ablated, making it impossible to attribute the observed performance to any specific design choice. The meta-learning claim — one of the three stated contributions — is completely unvalidated. These gaps do not invalidate the paper's core finding (the overall system works well), but they prevent the paper from supporting its stronger claims about why it works and which components are responsible.

**Score: 6.5** — borderline between weak accept and revise-and-resubmit. The contribution is real but the experimental rigor needs improvement before the paper fully earns its claims.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>