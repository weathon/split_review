Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper benchmarks 12 single-cell retrieval methods (non-ML, VAE-based, and scFM-based) across cross-platform, cross-species, and cross-omics settings using both label-dependent metrics (Vote-Acc, Batch Diversity, Recall) and newly proposed label-free metrics (AvgOverlap, DE-gene Jaccard). The main contributions are: (1) a comprehensive head-to-head comparison that reveals top scFMs (SCimilarity, UCE, scFoundation) generally lead, (2) the finding that non-ML methods like CellFishing.jl remain highly competitive, (3) identification of scFM failure regimes (distant species + omics), and (4) proposal of label-free evaluation as a complement when cell-type annotations are unreliable.

## Strengths

- **Most comprehensive benchmark of single-cell retrieval methods to date** — Evaluates 12 methods spanning three classes across 8+ datasets under cross-platform, cross-species, and cross-omics settings. This breadth substantially exceeds any prior single study and establishes a clear performance hierarchy (Tables 1–3).

- **Novel label-free evaluation metrics with empirical support** — Introduces AvgOverlap (retrieved-cell consistency across methods) and DE-gene Jaccard similarity. The paper shows these correlate with the standard label-dependent Vote-Acc across four benchmark datasets (Figure 2c) and demonstrates that top methods identify common DE-gene sub-groups within coarse cell types (Figure 3a,b).

- **Key finding that non-ML methods remain competitive** — CellFishing.jl (LSH-based) frequently ranks among the top 3 methods in cross-platform and cross-species settings (Tables 1–2), challenging the assumption that deep learning is always necessary and providing a strong baseline for future work.

- **Rigorous analysis of scFM failure modes** — Cross-omics experiments on mouse multi-omics data (Chen-2019, Ma-2020) show all scFMs perform near-random while VAE-based methods (scVI, LDVAE) lead (Table 3), cleanly identifying a critical limitation: scFMs fail when both species and omics are distant from the pre-training corpus.

- **Biological insight from DE-gene sub-group analysis** — The CD4+ T cell analysis (Figure 3a) shows top methods (SCimilarity, scFoundation, CellFishing.jl) identify internal sub-groups with distinct expression patterns within a single cell-type label, suggesting these methods capture finer cell-state differences beyond coarse annotations.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the evidence presented. No weakness identified undermines the central findings.

### Minor

- **No measure of variance or statistical significance for any metric** — All results in Tables 1–3 are reported as single values without standard deviations, confidence intervals, or statistical tests. VAE training involves stochasticity, and retrieval metrics depend on query cell selection. The paper uses language like "significant advantage" (Section 4.1) without supporting significance tests. While the numerical gaps are often large enough to be credible, the absence of any variance estimate weakens the statistical rigor expected of a benchmark paper.

- **Label-free metric validation lacks quantitative grounding** — The paper states AvgOverlap and Vote-Acc are "strongly correlated" (Section 4.4) but reports no correlation coefficient, p-value, or any numerical statistic — only a visual claim about Figure 2c. With only 48 data points (12 methods × 4 datasets), the strength of this correlation is unknown. The paper's claim that label-free metrics "can be employed in a broader scenario" is partially supported but would benefit from quantitative evidence.

- **Cross-species retrieval does not specify whether tissue is controlled** — The cross-species evaluation (Section 4.2) uses human and mouse scRNA-seq "across 10 tissues" but does not state whether retrieval is restricted to the same tissue (e.g., query mouse immune cells only retrieve from human immune cells). If retrieval is across all tissues without restriction, performance metrics may be confounded by tissue mismatch rather than reflecting true cross-species capability. This ambiguity should be clarified.

- **VAE training details for cross-omics settings are underspecified** — The paper states VAE methods are trained (Section 3.3.1) and that scATAC-seq peaks are aligned to gene space via DeepMAPS (Section 3.3.3). However, it does not specify whether the same likelihood function (e.g., negative binomial) is retained when modeling gene-level regulatory potential derived from binary accessibility data, which has fundamentally different statistical properties. This is a detail that affects interpretability of the cross-omics comparisons.

- **Query/reference split sizes not reported** — The paper gives total cell counts for multi-omics datasets but does not report how many cells are used as queries versus reference in any setting. This information is essential for assessing the statistical reliability and computational cost of the reported metrics.

- **Gene-vocabulary mismatch not discussed** — scFMs use different gene vocabularies (e.g., scGPT's 4000 HVGs vs. scFoundation's 20,000 genes). The paper adopts each method's default preprocessing (Section 3.3.3) but does not state how genes in the evaluation data that are not covered by a given scFM's vocabulary are handled (set to zero, omitted, imputed?). This could affect retrieval quality differentially across methods.

### Trivial

- **"Trillions of cells" in the introduction (Section 1) is an overstatement** — Current atlas scales are in the tens of millions, not trillions. This is a framing exaggeration in a single sentence and does not affect any technical claim.

## Nice-to-Haves

- **Computational cost comparison** — Runtime, memory usage, and indexing time are practical concerns for retrieval benchmarks. Adding a brief comparison would increase the paper's utility for practitioners selecting a method.
- **Sensitivity analysis for K** — The paper uses K = 10, 20, 50 across experiments but does not discuss whether method rankings change with K. A brief ablation would be informative.
- **Correlation coefficient for label-free validation** — Reporting Pearson/Spearman correlation with a p-value for Figure 2c would quantitatively strengthen the claim that label-free metrics are a reliable proxy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Unclear whether VAE methods are trained or zero-shot in cross-omics/species"* — REMOVED because the paper explicitly states "for VAE-based methods, we train the model for both query and reference" (Section 3.3.1, line 86) as a general procedure covering all settings. The reviewer misread this.
- *"Formatting of tables is garbled"* — REMOVED as a parser artifact, not an author error.
- *"Batch diversity metric should be normalized"* — REMOVED as a minor suggestion that does not affect the paper's claims and was not flagged by the reviewer as a structural issue.
- *"The paper does not present results" / missing appendix content* — REMOVED as parser-stripped content that exists in the original submission.
- *Generic strength "addressed an important problem"* — REMOVED from Strengths as superficial/unsubstantiated.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add error bars or bootstrap-based variance estimates** for the main results in Tables 1–3, at minimum for VAE-based methods where training randomness applies. Even bootstrapping over query cells would provide a useful measure of reliability.
2. **Report the correlation coefficient (with p-value)** for the AvgOverlap vs. Vote-Acc relationship shown in Figure 2c, and ideally hold out one dataset for a prediction test of the label-free ranking.
3. **Clarify the cross-species retrieval design** — specify whether retrieval is restricted to the same tissue or conducted across all tissues, and discuss the implications.
4. **Specify the likelihood function and architecture** used for VAE methods when applied to gene-aligned scATAC-seq data in the cross-omics setting.
5. **Report query/reference split sizes** for all datasets, and describe how genes missing from a scFM's vocabulary are handled.

## Score and Decision

The paper addresses an important and timely problem with a well-designed benchmark spanning realistic and challenging settings. Its contributions — the broad comparative evaluation, the label-free metrics, and the identification of scFM failure regimes and non-ML method competitiveness — are genuine and useful to the community. The weaknesses identified are genuine but minor: they concern presentation, statistical rigor, and documentation clarity rather than structural flaws in the methodology or conclusions. All are addressable without changing the experimental design.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>