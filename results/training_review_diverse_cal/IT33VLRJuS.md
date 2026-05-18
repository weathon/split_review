I've thoroughly read the paper and verified all claims. Let me now construct the final review.

---

## Summary

This paper introduces Marlene, a deep neural network for recovering time-varying gene regulatory networks (GRNs) from single-cell RNA sequencing time-series data. The architecture combines three components: (1) gene featurization via Set Transformer's Pooling by Multihead Attention (PMA) to obtain fixed-size gene representations from variable-size cell batches, (2) dynamic graph construction via self-attention whose key/query weights are evolved by a GRU across time points, and (3) Model-Agnostic Meta-Learning (MAML) to enable accurate inference for rare cell types by treating each cell type as a task. The method is validated on three scRNA-seq datasets (SARS-CoV-2 vaccination, lung aging, and lung fibrosis) against six baselines, consistently finding more validated TF-gene interactions from TRRUST and RegNetwork databases and capturing biologically meaningful temporal dynamics.

## Strengths

- **Novel architectural adaptation for feature-level dynamic graphs**: The paper reformulates dynamic graph learning for a setting where genes are features rather than nodes. The PMA gene featurization step (Methods, Eq. 1) maps variable-size cell-batch inputs to fixed gene feature representations, enabling self-attention-based graph construction on the gene level. This directly addresses the problem of learning "graphs of features" rather than graphs of samples (lines 37-41, 70-75).

- **GRU-evolved self-attention captures realistic temporal dynamics**: The model uses a GRU to evolve the key and query projection weights of the self-attention module across time points (Eq. 3), inspired by EvolveGCN but adapted for self-attention. This design produces networks that change smoothly over time, with the IoU analysis (Figure 2a) showing the expected pattern of strongest rewiring immediately after vaccination followed by stabilization—unlike static methods (low constant IoU) or TVGL/Graphs4mer (constant or decreasing IoU patterns that are biologically implausible).

- **Strong and consistent empirical validation across three diverse datasets**: The method outperforms six existing approaches (GENIE3, SCODE, GRNBoost2, PIDC, DeepSEM, TVGL, Graphs4mer) in recovering known TF-gene interactions from TRRUST and RegNetwork databases, with Fisher's exact test significance, across all three datasets and most cell types. For example, on the SARS-CoV-2 vaccination data, Marlene identified over 800 validated RegNetwork links for B cells (FDR ≤ 1e-67), far exceeding the second-best method (lines 136, 171, 187).

- **Practical efficiency**: The model trains in "only a few minutes per run" on a single NVIDIA RTX 3060 (line 130), making it accessible to researchers without large-scale compute—a meaningful practical advantage.

- **Biologically meaningful dynamic edge enrichment**: Genes that gain regulatory edges at the post-vaccination time point are enriched for relevant immune processes (Interferon Gamma Response, TNF-alpha Signaling) across multiple cell types, with other methods showing weaker or inconsistent enrichment (Figure 2b). This provides convergent evidence that the recovered dynamics capture genuine biology.

## Weaknesses

### Fatal

None.

### Major

- **No ablation studies for core components**: The method is presented as a joint system of PMA featurization, GRU-evolved self-attention, and MAML meta-learning, but none of these components is tested in isolation. Without ablations—e.g., a static variant with tied weights across time (isolating the GRU's contribution), a variant without MAML (isolating meta-learning's contribution), or a variant using average pooling instead of PMA—it is impossible to attribute the performance gains to specific architectural choices. This is the paper's most significant methodological gap, as key claims ("the GRU enables dynamic modeling," "MAML facilitates recovery for rare cell types") rest on unsubstantiated component-level assertions. The critic's worry that the approach "may reduce to a self-attention mechanism that could be replicated more simply" cannot be dismissed without these experiments.

### Minor

- **Cell-type classification as a proxy objective lacks direct validation**: The model is trained to predict cell type from reconstructed expression, rather than to reconstruct expression directly. While the paper provides a reasonable justification (sparsity makes reconstruction loss ineffective, lines 54-56) and the database overlap results serve as indirect validation, a controlled comparison (e.g., training the same architecture with a reconstruction loss vs. the classification proxy on synthetic data with known ground truth) would substantially strengthen confidence that the proxy leads to correct regulatory edges rather than cell-type-discriminative features that correlate with but do not causally determine regulation.

- **SCODE may be used suboptimally as a baseline**: SCODE was originally designed for time-series scRNA-seq data using ODE-based modeling. Applying it independently to each time point (line 128) discards the temporal information it was designed to exploit. While this treatment is consistent with how SCODE appears in static benchmarks (e.g., BEELINE), a fairer comparison would also include SCODE in its intended dynamic mode. That said, this does not invalidate the overall comparison, as Marlene still outperforms the other static baselines (GENIE3, GRNBoost2, PIDC, DeepSEM) that are genuinely per-time-point methods, and the IoU analysis includes TVGL and Graphs4mer as dynamic-capable alternatives.

- **Inconsistent baseline coverage across evaluation settings**: TVGL and Graphs4mer appear in the IoU analysis (Figure 2a) but are largely absent from the main database-overlap comparisons (Figures 1 and 3, with one exception in the fibrosis results where TVGL is briefly mentioned on line 187). The paper does not explain this discrepancy, making the comparison across methods feel uneven.

- **Top 2% sparsification threshold may influence results**: The paper selects the top 2% of edges by attention weight for all methods to match database sizes (line 126). No analysis of how this threshold affects the overlap results is provided; for a method outputting soft weights, the rank-ordering and thus the overlap could be sensitive to this cutoff.

- **No analysis of hyperparameter sensitivity**: Key hyperparameters—batch size, number of PMA seeds, number of MAML inner steps, learning rates—are reported (line 130) but not varied. Given the modest number of datasets and time points, it is unclear how robust the method is to these choices.

- **Code and trained models not mentioned for release**: The paper does not state whether code will be released. Given the complexity of MAML training and GRU weight evolution, reproducibility is a concern without public implementation.

### Trivial

- None.

## Nice-to-Haves

- A synthetic-data experiment where ground-truth regulatory networks are known would directly address the proxy-objective concern and provide a cleaner test of the architecture.
- Reporting memory usage (given the acknowledged quadratic memory issue, line 208) and runtime per dataset would help practitioners assess practical feasibility.
- The observation that "SCODE performed well in some static evaluations" (line 171) could be followed by a brief discussion of when/why SCODE succeeds relative to Marlene, which would calibrate claims and help readers choose between methods.

## Removed Points

The following points from the reviewers were removed or downgraded with justification:

- **"Circular evaluation due to TRRUST restriction"** — REMOVED. The critic claims that restricting columns of the adjacency matrix to TFs from TRRUST and then evaluating against TRRUST creates a circular validation. This is incorrect. The model uses TRRUST to determine *which genes are transcription factors* (a structural constraint common to all GRN inference), not to learn which specific TF→gene pairs exist in the database. It must still learn the correct target genes. RegNetwork (150K+ edges) provides independent validation. The critic's framing of this as a "fatal" circularity that "undermines the entire validation" is a misunderstanding of what the architecture constraint entails.

- **"SCODE misuse invalidates comparison"** — DOWNGRADED to Minor (see above). The critic's characterization as a "serious issue" that "makes the comparison unfair" overstates the impact. The paper compares against multiple methods, and even properly used, SCODE would not output per-time-point networks (needed for the dynamic analysis). The paper is transparent about how baselines were applied.

- **"No evidence that proxy objective leads to correct edges"** — DOWNGRADED to Minor (see above). The paper's empirical results (database overlap, GSEA enrichment) *are* evidence that the proxy works. A controlled experiment would strengthen the case, but the claim that "no evidence is provided" inaccurately dismisses the paper's main experimental results.

- **"The models compared against are different methods, not ablations"** — This observation is correct but is already captured under the "no ablation studies" major weakness.

- **"GSEA is computed on genes, not edges"** — This is how GSEA works by design; it is a standard biological validation approach for GRN studies. Not a weakness.

## Novel Insights

The most interesting observation emerging from this review is the tension between the paper's strong empirical validation (three datasets, consistent outperformance, meaningful biological enrichment) and the lack of component-level ablation. The paper's architecture makes intuitive sense—PMA for featurization, GRU for dynamics, MAML for few-shot adaptation—but without ablations, the reader cannot distinguish between a genuinely synergistic design and a system where one or two components do all the heavy lifting while others add complexity without benefit. This is a common pattern in modern ML-for-science papers: the architectural sophistication outpaces the evaluation's ability to attribute credit, leaving the reader with a "works well" result but an incomplete understanding of why. The paper would be substantially strengthened by a simple set of ablations that would also serve as a tutorial on which design choices matter most for dynamic GRN inference.

## Suggestions

1. **Add ablation studies** comparing Marlene against (a) a static variant with tied self-attention weights across time, (b) a variant without MAML (joint training across cell types), and (c) a variant without PMA (e.g., simple averaging). This is the single most impactful improvement.
2. **Include a properly used dynamic baseline** (e.g., SCODE in its intended time-series mode, or a time-varying VAR) to strengthen the claim that dynamic modeling per se provides benefits beyond static per-time-point inference.
3. **Release code and trained models** to ensure reproducibility given the method's complexity.
4. **Include hyperparameter sensitivity analysis** for the key knobs (batch size, PMA seeds, inner steps) to demonstrate robustness.

## Score and Decision

This paper makes a genuine contribution to an important problem. The architecture is novel and addresses the unique challenges of dynamic GRN inference from scRNA-seq data (feature-level graphs, varying cell counts per time point, rare cell populations). The validation is strong: three diverse datasets, multiple baselines, two independent ground-truth databases, and enrichment analysis that confirms biological plausibility. The main weakness—lack of ablation studies—is significant but not fatal; it limits mechanistic understanding of the method but does not undermine the core results. The circularity concern raised by the harsh critic is a misunderstanding and does not hold. The method appears to work, and the paper communicates its contributions clearly.

**Score**: 7.0 — The paper has a solid contribution and strong empirical validation. The missing ablations and minor baseline concerns prevent it from being excellent, but the core results are believable and the method is novel.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>