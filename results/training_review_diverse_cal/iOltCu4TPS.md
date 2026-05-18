I have fully verified all claims against the paper content. Here is the consolidated review.

---

## Summary

This paper benchmarks 12 cell retrieval methods spanning three classes (non-ML, VAE-based, and single-cell foundation models) across cross-platform, cross-species, and cross-omics settings. It proposes two types of evaluation metrics — label-dependent (Vote-Acc, BatchDiv, Recall) and label-free (AvgOverlap, DE-gene Jaccard similarity) — and finds that top scFMs (UCE, scFoundation, SCimilarity) generally outperform other methods, traditional non-ML methods remain competitive, and label-free metrics correlate with label-dependent ones. The study fills a genuine gap, as no prior work directly compares scFMs with classical retrieval methods under a unified framework.

## Strengths

- **Comprehensive and systematic benchmarking across method classes and evaluation settings**: The paper evaluates 12 methods on cross-platform (9 PBMC platforms, 4 pancreas platforms), cross-species (human/mouse atlas), and cross-omics (three multi-omics datasets) settings, providing the first direct comparison between scFMs and traditional methods under a unified framework. This breadth enables the paper's key findings on relative performance and failure modes (Tables 1–3).

- **Novel label-free evaluation metrics**: The paper proposes AvgOverlap (consistency of retrieved cells across methods) and DE-gene Jaccard similarity as label-free metrics. This directly addresses the acknowledged problem that cell-type annotations are often coarse, inconsistent, or incorrect. The approach is well-motivated by the difficulty of establishing ground-truth cell pairs.

- **Actionable insights on method selection grounded in empirical results**: The paper yields concrete, evidence-based recommendations — e.g., scFMs excel in standard settings but fail on mouse scATAC-seq (Section 4.3), non-ML methods like CellFishing.jl remain competitive (Section 4.1), and VAE methods are good alternatives when target species/omics are far from scFM pre-training data (Section 6).

- **Biological validation of retrieval quality via DE-gene expression patterns**: The analysis in Section 4.4 (Figure 3) shows that top scFMs and CellFishing.jl identify sub-groups within a cell type (e.g., CD4+ T cells) with distinct expression patterns, suggesting these methods retrieve biologically meaningful cell states rather than merely matching coarse cell-type labels.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Ambiguous VAE training protocol description (Section 3.3.1)**: The paper states "For VAE-based methods, we train a low-dimensional embedding for both {x_i} and {y_i}." What is ambiguous is whether "train for both" means the VAE model is trained on the union of query and reference cells (which would be problematic) or, as is standard practice, trained on reference cells only and then used to encode both. The natural reading in this field (scVI, LDVAE) is the latter — train on reference, encode both — but the text should be explicit. The reviewer's concern that this "could be a structural flaw" is a reasonable reading of the ambiguous language, not an actual flaw in the experimental design. The authors should clarify: *"We train each VAE on the reference cells only, then extract low-dimensional embeddings for both query and reference cells using the trained encoder."*

- **No uncertainty quantification for any evaluation result**: Tables 1–3 report single-point estimates without standard deviations, confidence intervals, or significance tests. VAE training is stochastic (multiple seeds would be relevant for scVI, LDVAE, CellBlast), and query set composition varies. While single-run evaluation is common in large-scale benchmarks of this scope, the absence of any error characterization makes it difficult to assess whether observed ranking differences between closely-performing methods are reliable. At minimum, bootstrapped confidence intervals across query cells for scFM methods (which are deterministic) and multiple-seed runs for VAE methods would strengthen the claims.

- **Correlation claim for label-free metrics lacks statistical support**: The paper claims "strong correlation" between Vote-Acc and AvgOverlap (Figure 2c) but reports no correlation coefficient, p-value, or summary statistics. It is also unclear what each point in the scatter plot represents (a method on one dataset? aggregated across datasets?). This is a central claim that validates the label-free approach; it needs quantitative backing (Pearson/Spearman correlation with confidence intervals and a clear description of the plotting units).

- **Missing random baseline column in Table 3**: The text states "most methods do not show significant improvement over the random baseline" (line 158), but Table 3 does not include a random baseline column for direct verification. Adding it would make this claim verifiable and strengthen the point about cross-omic difficulty.

- **scFM embedding extraction not specified**: The paper does not detail how each scFM's cell embedding is obtained (layer choice, pooling strategy, normalization). Different extraction choices can significantly affect retrieval performance. This information is needed for reproducibility.

- **Batch diversity metric limitations not discussed**: The BatchDiv metric assumes higher entropy across retrieved cells' batch labels is always desirable. However, if a query cell comes from a biological condition that is batch-specific, mixing batches could retrieve biologically irrelevant cells. A brief discussion of when batch mixing is and is not appropriate would improve the paper.

### Trivial
- **Training hyperparameters for VAE methods not reported**: Epochs, learning rate, latent dimension, and convergence criteria are not stated. While a codebase is referenced, key hyperparameters should be summarized for quick assessment.

## Nice-to-Haves

- Report runtime (embedding extraction + retrieval) for each method on a common hardware setting — directly relevant for practitioners choosing a method.
- Validate label-free metrics against an independent ground truth beyond correlation with Vote-Acc, such as enrichment for known marker genes or consistent pathway activity in commonly retrieved cells.
- Distill findings into a compact decision table: given the user's species, omics, and label availability, which method class is preferred and why.

## Removed Points

- **VAE training as a "structural flaw" / "potentially invalidates central comparisons"**: The reviewer's alarmist framing (that VAEs were trained on query data) is speculative. The standard practice in this field is to train VAEs on reference data only, then encode both reference and query. The paper's phrasing is ambiguous, but there is no evidence this was actually done incorrectly. Moved to minor (clarity issue only).
- **"Criticisms about missing appendix / proofs in appendix"**: None raised — included for completeness.
- **"Should also cover Y / domain Z" concerns about scope**: The reviewer's suggestions to validate against marker genes and provide a decision table are reasonable suggestions but are not weaknesses; moved to Nice-to-Haves.
- **Pure reproducibility nitpicks about undisclosed large artifacts**: The request for "complete training logs" or similar is absent from the review; no points removed here.

## Novel Insights

None beyond the paper's own contributions. The reviews largely affirm the paper's stated contributions rather than revealing unexpected new interpretations.

## Suggestions

1. Clarify the VAE training protocol in Section 3.3.1: explicitly state that VAEs are trained on reference cells only, then used to encode both reference and query.
2. Add correlation coefficients (Pearson/Spearman + p-values) for the Vote-Acc vs. AvgOverlap relationship in Figure 2c, and clarify what each point represents.
3. Add a random baseline column to Table 3 to make the "no significant improvement over random" claim directly verifiable.
4. Report bootstrapped confidence intervals across query cells for all metrics, and/or multiple-seed results for VAE methods.
5. Specify how each scFM's embedding is extracted (layer, pooling, normalization) in the main text or appendix.
6. Add a brief limitations paragraph for the BatchDiv metric discussing when batch mixing may or may not be desirable.
7. Report runtime and memory usage for each method on a common hardware setup.

## Score and Decision

Originality: 6/10 — The benchmarking framework itself is not novel, but the label-free metrics and the first systematic comparison of scFMs vs. classical methods are contributions.  
Importance of research question: 8/10 — Fills a clear gap; practitioners need this guidance.  
Claims supported: 6/10 — Core findings are supported, but the label-free correlation claim lacks statistical rigor, and the VAE training description is ambiguous.  
Soundness of experiments: 7/10 — Broad coverage is a strength; missing error bars and the unclear VAE protocol are the main weaknesses.  
Clarity of writing: 6/10 — Generally clear but has ambiguous phrasing in a critical methodology section.  
Value to community: 8/10 — High; serves as a foundation for future development in cell retrieval.

The paper's core contributions (a comprehensive benchmark, novel label-free metrics, and actionable findings) are solid. The weaknesses are addressable in a revision and do not undermine the central claims. The ambiguous VAE training description is the most consequential issue, but resolving it merely requires explicit phrasing — the underlying experimental design is almost certainly standard practice.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>