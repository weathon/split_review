Now I have a thorough understanding of the paper and can systematically verify each claim. Let me compose the final review.

## Summary

This paper presents a comprehensive benchmark of 12 single-cell retrieval methods (2 non-ML, 3 VAE-based, 7 scFM-based) across cross-platform, cross-species, and cross-omics settings. The authors propose both label-dependent metrics (cell type accuracy, batch diversity, recall) and label-free metrics (AvgOverlap, DE gene consistency) for evaluation, and report findings about top-performing methods and their limitations.

## Strengths

- **First comprehensive benchmark of cell retrieval methods across diverse settings.** The paper systematically compares 12 methods on cross-platform (PBMC: 9 platforms, pancreas: 4 platforms), cross-species (human/mouse atlas, 10+ tissues), and cross-omics (3 multi-omics datasets) settings — substantially broader than any prior single study (Sections 3.3.2, 4.1–4.3).

- **Novel label-free evaluation metrics with empirical support.** AvgOverlap (consistency of retrieved cells across methods) shows strong correlation with Vote-Acc across four datasets (Fig. 2c), providing a complementary evaluation tool when cell-type annotations are unavailable or unreliable. The DE-gene consistency analysis (Fig. 3) offers a deeper, gene-level perspective.

- **Key finding: traditional non-ML methods remain competitive.** CellFishing.jl, a simple LSH-based method, ranks among the top performers in cross-platform and cross-species settings (Tables 1, 2), challenging the assumption that large foundation models always dominate. The paper correctly highlights this as a practical insight.

- **Actionable characterization of scFM failure modes.** The benchmark systematically identifies when scFMs fail: when both target species and omics are distant from the pre-training corpus (mouse scATAC-seq, Table 3). The recommendation that VAE-based methods (scVI, LDVAE) serve as alternatives in these scenarios is grounded in the data.

- **Cross-omics recall metric.** The paper introduces a recall metric for paired multi-omics data and shows that even the best methods barely outperform random (Table 3), quantifying an important open challenge.

## Weaknesses

### Fatal
None.

### Major

- **No uncertainty quantification for any metric.** All tables (1, 2, 3) report single scalar values per method and setting without confidence intervals, standard deviations, or multiple runs. Given that several claimed findings hinge on small margins (e.g., SCimilarity vs. UCE at close values in Table 1), the absence of error bars undermines the strength of the comparative conclusions. This is a gap the authors should address to make rankings trustworthy.

### Minor

- **Label-free metrics validated against labels, not ground truth.** The correlation between AvgOverlap and Vote-Acc (Fig. 2c) shows consistency with the best available proxy, but does not rule out the possibility that shared systematic biases among methods (e.g., all scFMs encoding similar latent geometries) drive the correlation. The paper would benefit from acknowledging this limitation more explicitly. The claim that these metrics "can be employed in a broader scenario" (abstract) is reasonable for a complementary metric but stops short of a full validation.

- **Batch diversity metric has conceptual limitations and is not validated.** The metric equates high batch diversity (retrieving cells from many batches) with good batch mixing, but retrieving cells from many batches is not necessarily desirable if those batches contain cells of a different type than the query. The metric is not validated against established batch-mixing metrics (e.g., kBET, iLISI). Since BatchDiv results are reported in Table 1 and used to compare methods, this limits the strength of the batch-mixing conclusions.

- **Cross-species evaluation limited to human and mouse.** The finding that "human-centered scFMs can well generalize in cross-species retrieval" (Section 4.2) is demonstrated only between two closely related species with well-annotated one-to-one homologs. The paper does acknowledge this limitation (line 142: "Generalization of scFMs to other distant species without explicit homolog mapping still remains an open problem"), which is appropriate, but this caveat should be more prominent when the claim is stated.

- **CD4+ T cell sub-group analysis is exploratory.** The identification of sub-groups via DE-gene consensus (Fig. 3, red boxes) is presented as evidence that top methods "can identify common cells with similar gene expression patterns" and "may correspond to certain unannotated sub-types." This is biologically plausible speculation, but no external validation (e.g., known marker genes, pathway enrichment) is provided. The paper's hedging language is appropriate, but the analysis remains suggestive rather than evidential.

### Trivial
None.

## Nice-to-Haves
- Adding statistical replicates or bootstrapped confidence intervals would strengthen the comparative claims.
- Validating the batch diversity metric against established batch-mixing metrics (kBET, iLISI) on a held-out dataset.
- Validating the label-free AvgOverlap metric against the exact cell-pair ground truth available in multi-omics datasets (where recall is already measured).
- Reporting computational cost (retrieval time, memory usage) per method, since scalability is a stated motivation.
- Reporting the number of genes retained after cross-species homolog alignment.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Cross-omics evaluation is confounded by peak-to-gene mapping.** REMOVED because the mapping is applied uniformly to ALL methods (VAE, scFM, non-ML), so comparisons between methods on the same data remain fair. There is no evidence that the mapping systematically biases comparisons.
- **Recommendation about VAE methods is contradicted by human multi-omics results.** REMOVED because the paper specifically recommends VAE methods "when the target species and omics are both distant" (line 156, 198) — the human multi-omics setting has omics shift but same species, so the condition is not met. This is a misreading.
- **Formula ambiguity in batch diversity metric.** REMOVED because the formula is garbled by PDF extraction; the original LaTeX likely rendered correctly. The conceptual concern about the metric is kept above.
- **"Arbitrary thresholds" for DE genes.** REMOVED because p<0.02 and logFC>0.5 are standard thresholds in single-cell DE analysis.
- **Missing related works / overstating the gap / missing implementation details.** REMOVED because either the paper cites relevant work (Section 5.1), addresses the point ("Details in our codebase"), or the criticism reflects scope creep or nitpicking.
- **Failure to define "similar" biologically.** REMOVED because similarity is operationalized through standard retrieval metrics, which is appropriate for an empirical benchmark.
- **CD4+ sub-groups lack external validation.** The paper's hedging language ("may correspond to," "can be further explored") is appropriate for exploratory analysis; this is not a weakness but an invitation for follow-up work.

## Novel Insights
The reviews largely corroborate the paper's own contributions without introducing genuinely novel perspectives beyond the paper's framing. The most useful meta-insight is that the label-free consensus metric, while intuitively appealing, inherits the biases of its constituent methods — a limitation the paper could address more directly.

## Suggestions
1. **Add error bars or confidence intervals** to all main results (Tables 1–3). Even bootstrapped 95% CIs over queries would substantially strengthen the comparative claims.
2. **Validate the label-free AvgOverlap metric** using the exact cell-pair matches available in multi-omics datasets (where recall is already computed) to directly test whether method consensus predicts true cell-pair retrieval.
3. **Acknowledge the shared-bias limitation** of label-free consensus metrics more explicitly in the text, and discuss scenarios where consensus could be misleading (e.g., all methods encoding similar inductive biases).
4. **Validate the batch diversity metric** against established batch-mixing metrics (kBET, iLISI) or provide a clearer rationale for why the metric is an appropriate indicator of good mixing.
5. **Broaden the CD4+ sub-group analysis** with external validation (e.g., known marker genes, GO enrichment) to move from speculation to evidence.

## Score and Decision

The paper makes a timely and useful contribution by providing the first comprehensive benchmark of single-cell retrieval methods across multiple challenging settings, with a broad method zoo (12 methods) and both label-dependent and novel label-free metrics. The core findings — top scFMs lead but have well-characterized failure modes, traditional methods remain competitive, label-free metrics correlate with label-dependent ones — are practically valuable and supported by the data. The main weaknesses (no uncertainty quantification, limited validation of novel metrics, conceptual caveats about batch diversity) are real but addressable and do not invalidate the paper's core contributions. The paper represents solid empirical work that advances the field's understanding of cell retrieval methods.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>