I now have a thorough understanding of the paper and both reviews. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes a computational framework for data-driven gene-gene interaction (GGI) discovery from single-cell transcriptomics. It combines a Transformer model (CelluFormer) trained to classify Alzheimer's disease status with a weighted diversified sampling (WDS) algorithm that selects a representative subset of cells for efficient attention-map-based interaction discovery. The WDS algorithm estimates a minmax kernel density for each cell via a two-pass randomized hashing procedure, then uses the inverse density as a sampling probability. Experiments on the SEA-AD dataset show that WDS with 1% of cells yields NES scores closer to the full-data result than uniform sampling at the same rate.

## Strengths

- **Computationally efficient two-pass density estimation.** Algorithm 1 runs in O(n·nnz(X)) time with O(R×B) memory, which is linear in the dataset size and avoids the O(n²) pairwise computation that a naive minmax density estimate would require. This is a practical contribution for large-scale single-cell data where memory is the bottleneck.

- **Novel application of attention maps from trained Transformers to GGI discovery.** The pipeline (Section 2.4) of averaging attention across layers/heads, scatter-adding over cells, and normalizing by co-occurrence frequency provides a clean methodology for extracting population-level gene-gene interactions from a Transformer trained purely for classification, without requiring prior knowledge of TF networks or existing GGI databases.

- **WDS consistently outperforms uniform sampling at small sample sizes.** Across all seven cell types and at 1% sampling, WDS yields higher NES and lower MSE than uniform sampling (Table 3). At 1%, WDS NES averages ~1.13 across cell types vs ~0.88 for uniform — a meaningful improvement. The gap narrows at larger sample sizes, consistent with the intuition that WDS is most valuable when compute constraints force small subsamples.

- **Transformer-based methods outperform correlation baselines for GGI discovery.** Table 2 shows that transformer-based methods (CelluFormer, scGPT, scFoundation) generally achieve higher NES than Pearson, Spearman, and CS-CORE across 8 datasets, supporting the premise that learned attention captures interaction structure beyond simple co-expression.

## Weaknesses

### Fatal
None. The paper makes a non-trivial methodological contribution and the claims, while overstated in places, are supported by the experimental evidence modulo the issues below.

### Major

- **The WDS estimator (Definition 3.3) targets a different estimand than the full-data aggregation, making the MSE comparison asymmetric.** The full-data procedure (Section 2.4) computes an unweighted average of attention maps across cells (normalized by co-occurrence count). The WDS estimator uses a weighted average with weights equal to the sampling probability I(x), which the paper explicitly states is unbiased for E_{x~I(x)}[Z_x(v_i,v_j)] — the expectation under a distribution that upweights diverse cells. The paper does not specify what estimator the uniform sampling baseline uses, but if it uses a simple unweighted mean (the natural choice), then WDS has an advantage: its weighting scheme changes the target quantity while uniform does not. The reported lower MSE for WDS could thus partially reflect the reweighting rather than the sampling strategy itself. A proper evaluation would use a Horvitz-Thompson estimator (weights = 1/I(x)) targeting the unweighted population mean for both methods, or alternatively the paper should explicitly acknowledge that WDS targets a scientifically motivated weighted interaction score and re-frame the "comparable to full data" claim accordingly.

- **No variance or confidence intervals reported.** Tables 2 and 3 report only means across five runs. NES is a rank-based GSEA statistic that can have substantial variability at small sample sizes. Without standard deviations, confidence intervals, or any measure of dispersion, it is impossible to assess whether the observed differences between methods or between sampling conditions are statistically meaningful. This is a standard expectation for any experimental paper making comparative claims.

### Minor

- **The "performance comparable" claim is overstated for some cell types.** At 1% sampling, the gap between WDS and full-data NES varies considerably: L6_CT (1.19 vs 1.18, close) but L5_ET (0.95 vs 1.15, gap of 0.20) and Pax6 (1.08 vs 1.25, gap of 0.17). Characterizing these differences uniformly as "comparable" papers over the variation.

- **The biological validation via BioGRID + DisGenet is of limited strength for the specific claim of AD-oriented interactions.** While the paper filters BioGRID to only include genes present in a DisGenet AD gene set, the interactions themselves come from BioGRID's aggregation of physical and genetic interactions across all biological contexts (not AD-specific). Enrichment in this filtered set shows that top-ranked gene pairs contain known interactors, but does not demonstrate that the method identifies interactions *differentially relevant to Alzheimer's disease* (e.g., enriched in AD pathways, replicable across independent AD cohorts, or differentially connected in AD vs. non-AD cells). For a methods paper this is a limitation worth noting rather than a fatal flaw, but the claims about "disease-oriented" interactions would benefit from stronger validation.

- **No theoretical or empirical analysis linking the IMD sampling objective to interaction discovery quality.** The paper motivates IMD as a "diversity score" that identifies unique cells, but does not establish why sampling diverse cells should preserve the population-level gene-gene interaction ranking. Is the attention-based interaction score smooth over the cell manifold? Do rare cell types carry disproportionately discriminative signal for AD? Without some analysis, WDS remains a plausible heuristic whose empirical success on this particular dataset may or may not generalize.

- **No analysis of the cell-type distribution of WDS-selected subsets.** The dataset contains 18 neuronal cell types with presumably imbalanced abundances. Does WDS systematically oversample rare types or undersample abundant ones? If so, the improved NES might partly reflect this stratified effect rather than the diversity metric per se. A simple breakdown of selected cell types would clarify the mechanism.

- **Hyperparameter sensitivity for R and B is not studied.** The algorithm's performance depends on the number of hash functions R and the hash range B. No analysis shows how these choices affect the diversity estimates or the downstream interaction scores.

### Trivial
- Several claims in the abstract and introduction use unnecessarily strong language (e.g., "pioneering approach," "revolutionize") that is not supported by the paper's actual results.
- Table 2 reports NES to two decimal places but the computation involves random hashing and multiple runs; the precision suggests a stability that is not demonstrated.

## Nice-to-Haves

- Showing that the top-ranked gene pairs from the subsample are enriched in AD-relevant KEGG/Reactome pathways, or that they replicate on an independent AD cohort, would substantially strengthen the biological claim.
- Concrete attention heatmaps for a few high-ranking gene pairs in AD vs. non-AD cells would help biological interpretability.
- A sensitivity analysis for hash parameters R and B would help practitioners apply the method.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about MLP vs CelluFormer training being not apples-to-apples (from Harsh Critic, Section-by-Section "Section 2"):** The critic claims MLP is trained per cell type while CelluFormer is trained on all cell types jointly. However, Table 1 explicitly includes an MLP row for "All Neuronal Cell Types" (97.23 F1) trained on the same multi-cell-type data as CelluFormer. The individual cell-type MLP rows are separate reference results; the main comparison in the table (All vs All) is fair. This criticism is factually inaccurate.

- **"No AD-specific signal" claim about BioGRID validation (from Harsh Critic, Critical Issue 2, first bullet):** The paper explicitly filters BioGRID to only include genes present in a DisGenet AD gene set (lines 247-249), so there is partial AD-specific filtering. While this doesn't fully address the concern (BioGRID interactions themselves are cross-context), the critic's statement that there is "no AD-specific signal" is inaccurate. The point is retained in weakened form in the Minor section.

- **"No comparison of attention-mapped interactions to held-out biological validation" (from Harsh Critic, Critical Issue 2, second bullet):** This asks for validation beyond what is standard for a computational methods paper at this stage. It is moved to Nice-to-Haves.

- **Pure formatting/style nitpicks** (the critic's section-by-section notes about "no theoretical analysis of how sampling probabilities relate to estimation accuracy" etc. — these are subsumed by the Minor weaknesses above and the specific actionable ones are retained; the generic versions are removed).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the estimator-mismatch issue, which is a methodological concern that the paper's own framing does not engage with, but this is a critique rather than a novel observation.

## Suggestions

1. **Reformulate the WDS estimator to target the unweighted population mean** using inverse-probability weighting (Horvitz-Thompson): weight each sampled cell by 1/I(x) instead of I(x). This would make the comparison to the full-data ground truth apples-to-apples and remove the ambiguity about whether WDS's advantage comes from the sampling or the reweighting.

2. **Report standard deviations or 95% confidence intervals** for all NES scores. Five runs is sufficient to estimate variability; failing to report it undermines the ability to assess significance.

3. **Include an analysis of which cell types WDS selects** relative to their abundance in the full dataset. This would help validate that the diversity score is working as intended and clarify the mechanism behind WDS's advantage.

4. **Tone down the "comparable to full data" claim** to acknowledge the cell-type-specific variation, or report per-cell-type comparisons more prominently.

5. **Add a controlled experiment** where uniform sampling uses the same weighted estimator as WDS (with uniform weights = 1/n), to isolate the effect of the sampling distribution from the effect of the weighting scheme.

## Score and Decision

This paper addresses an important problem (scaling Transformer-based interaction discovery to massive single-cell data) with a technically clean randomized algorithm. The core methodological contribution — the two-pass minmax density estimator and its use for diversity-based sampling — is novel and well-motivated. However, the evaluation has a significant methodological confound: the WDS estimator targets a different quantity than the full-data ground truth, and the paper does not acknowledge or address this. Additionally, the lack of variance reporting and overstated claims about "comparable" performance weaken the empirical case. The paper's central claim about WDS achieving full-data performance at 1% sampling cannot be fully accepted without resolving the estimator mismatch. A major revision addressing this issue could make the paper a solid contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>