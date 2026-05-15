Now I have all the evidence I need. Here is my consolidated review:

## Summary

This paper revisits similarity-based metrics (BERTScore, ROUGE) for summary factual consistency detection, showing that their previously reported failure stems from comparing summaries against reference texts rather than source documents. It proposes SBERTScore, a sentence-level extension of BERTScore that uses sentence transformers, and demonstrates that zero-shot similarity-based metrics can compete with trained NLI- and QA-based factuality metrics. The paper further shows that different metric families detect complementary error types and that a simple AND combination can improve overall balanced accuracy.

## Strengths

- **Clean empirical identification of the root cause of previous negative results (Table 3).** The paper convincingly demonstrates that switching the comparison text from (reference, summary) to (source, summary) dramatically improves BERTScore and ROUGE from near-random to competitive levels. This single finding directly overturns a widely-held negative assessment in prior work and is the paper's most impactful empirical contribution.

- **Systematic ablation of text granularity with practical guidance (Table 4).** The experiments isolate the contributions of sentence-level representation and sentence-level comparison, showing that naive averaging harms performance and that sentence-level processing avoids the truncation issues that plague document-level methods (45.76% of source documents exceed 512 tokens at document level). This gives clear, reproducible guidelines for using similarity-based metrics.

- **SBERTScore achieves competitive zero-shot performance against trained baselines (Table 7).** Without any fine-tuning on factuality data, SBERTScore achieves 0.71 balanced accuracy on the CNNDM split, second only to QAFactEval (a trained QA-pipeline system), and outperforms all zero-shot NLI metrics plus several trained approaches (SummaC_Conv, DAE). The authors also demonstrate a practical computational advantage — O(N+M) complexity vs. O(NM) for NLI-based methods — substantiated with a runtime measurement.

- **Error-type analysis reveals complementary strengths (Table 8, Figure 1).** The finding that SBERTScore has the highest recall on correct summaries (96.4% on CNNDM) — i.e., it rarely misclassifies consistent summaries as inconsistent — is a valuable and non-obvious property that differs from NLI/QA metrics. The low agreement between metric families and the demonstration that a simple AND combination improves accuracy supports the paper's call for diversity in evaluation approaches.

## Weaknesses

### Fatal
None.

### Major

- **ROC-AUC promised but not reported.** Section 4.2 (line 113) states: "In addition, we report Area Under Curve of Receiver Operating Characteristic (ROC-AUC) … which does not require a threshold to reflect the metric's ability to discriminate consistent and inconsistent summaries." However, no ROC-AUC values appear anywhere in the results — all tables and figures report only balanced accuracy. Since balanced accuracy depends on a threshold chosen per dataset on the validation set, the threshold-free ROC-AUC would provide important complementary evidence that the headline results are not artifacts of a particular threshold choice. The authors explicitly argued for the importance of this metric; omitting it without explanation is a significant gap.

### Minor

- **Significance testing is underspecified and likely underpowered for some comparisons.** The paper states only that "Results' significance is computed via t-test" (Section 4.2) and reports p<0.05 across multiple tables. It never states what the unit of observation is (examples? datasets?), how many observations are used, or whether corrections for multiple comparisons are applied. Some comparisons involve only 3–5 datasets (e.g., Table 7: XSum split has 3 sub-datasets); a paired t-test on 3 observations has extremely low power and the normality assumption is questionable. While the general findings are likely robust, the specific significance claims as presented cannot be verified.

- **Metric combination experiment uses naïve AND/OR without threshold recalibration.** Section 5.6 combines metrics by applying logical AND/OR to their binary decisions using thresholds that were optimized separately for each individual metric. This is acknowledged as a "simple test," but the reported improvements from AND may partly reflect the specific choice of un-recalibrated thresholds rather than a genuine benefit of diversity. A proper fusion (e.g., re-optimizing a threshold on a weighted combination of scores, or a simple logistic regression) would more convincingly demonstrate that combining diverse metrics is beneficial. As presented, the experiment shows that AND can work but not that the approach is near-optimal.

- **Unweighted averaging across sub-datasets of vastly different sizes.** Tables 7a/7b aggregate results by taking the average balanced accuracy across sub-datasets within each split (CNNDM: 5 datasets; XSum: 3 datasets). Sub-datasets vary dramatically in size — XENT has 32 examples while SummEval has 1,600. Equal weighting of sub-datasets gives small datasets disproportionate influence on the aggregate. Per-dataset results in Table 6 partially mitigate this, but the aggregate claims (e.g., "SBERTScore outperforms BERTScore across the whole dataset") would be stronger with size-weighted or example-pooled aggregates.

- **Error-type analysis reports only recall, not precision or F1, per error type.** Table 8 reports recall (sensitivity) for each error category. However, a metric could achieve high recall on a specific error type by being overly sensitive (e.g., marking everything as inconsistent). Without precision or F1 per error type, the reader cannot assess whether high recall on a given error type comes at the cost of many false positives. Balanced accuracy (reported elsewhere) provides an aggregate view, but per-category precision would substantiate the error-type claims.

### Trivial

- **The paper does not discuss how often individual summary sentences exceed the 512-token limit of the sentence transformer or how such cases were handled.** For news articles, sentences occasionally exceed this length. The paper notes that 45.76% of *documents* are truncated at the document level, but single-sentence handling is not discussed.

## Nice-to-Haves

- Reporting ROC-AUC for all metrics on all sub-datasets, as promised.
- Specifying the significance test details: null hypothesis, unit of observation, number of comparisons, and correction method (if any).
- Re-running the metric combination experiment with a recalibrated threshold on the combined score (e.g., a simple weighted sum with a new cutoff) and testing whether gains remain significant.
- Providing size-weighted or example-pooled aggregates alongside the per-dataset averages.

## Removed Points

- **Data leakage for trained baselines (Critic's Issue #4):** The critic argued that trained metrics (QAFactEval, SummaC_Conv, FactCC) may have been trained on datasets overlapping with the benchmark, making the "zero-shot vs. trained" comparison unfair. However, any such data leakage would *inflate* the trained metrics' scores, meaning the zero-shot similarity metrics' competitiveness is *understated*, not overstated — this concern actually strengthens the paper's claims, not weakens them. The paper already addresses the related issue for DAE (Section 5.5). Removed because the criticism's logical direction is backwards with respect to the paper's claims.

- **Vagueness of related work on Bao et al. (2023) (Critic's Section 2.3 note):** The paper adequately describes what Bao et al. did ("attempted to extend BERTScore to sentence-level without using sentence embeddings, leading to unsuccessful results") for a related work section. Removed as a nitpick.

- **FactCC as a weak baseline (Critic's Section 4.3 note):** Including weak baselines is standard practice in empirical papers. Removed.

- **Terminology of "simplification" in Section 5.3 (Critic's Section 5.3 note):** A trivial terminology preference. Removed.

- **Formatting/style/parsing artifacts:** Removed per hard rules.

## Novel Insights

The most insightful observation that emerges from the reviews — beyond what the paper itself states — is that the paper's core finding (similarity metrics work when compared to source documents) is so stark that it survives the weaknesses in the significance testing and aggregation methodology. Table 3 shows BERTScore going from near-random (~0.50) to competitive (~0.60–0.70) simply by switching the comparison text. This effect is large enough that concerns about threshold selection, significance test validity, or unweighted averaging do not threaten the primary claim. The paper's secondary claims (that SBERTScore specifically outperforms BERTScore, and that AND combination is beneficial) are more moderately supported and would benefit from the suggested methodological improvements.

## Suggestions

1. **Add ROC-AUC results** to all main tables (Tables 2, 3, 4, 6, 7) to provide the threshold-free evaluation promised in Section 4.2.
2. **Provide significance testing details:** specify the unit of observation, the test statistic, and whether multiple comparison corrections were applied. Consider bootstrapping over examples as an alternative.
3. **Improve the metric combination analysis:** re-optimize the threshold on a combined score (e.g., weighted sum) rather than applying AND to independently-thresholded binary decisions, and report whether improvements remain significant.
4. **Include size-weighted aggregates** alongside the current unweighted per-dataset averages in Tables 7a/7b, or pool all examples.
5. **Add precision or F1 per error type** to Table 8 alongside recall to complete the error-type sensitivity picture.

## Score and Decision

The paper's central finding — that similarity-based metrics work for factuality detection when compared to source documents, overturning a decade of negative results — is genuine and important. The SBERTScore extension is methodologically clean and the empirical evaluation is broad. The weaknesses (missing ROC-AUC, underspecified significance tests, simplistic metric fusion) are all addressable in revision and do not invalidate the core contributions. The paper makes a real, non-incremental contribution to the field.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>