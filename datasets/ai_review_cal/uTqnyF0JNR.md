- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper introduces IGL-Bench, a comprehensive benchmark for Imbalanced Graph Learning (IGL) that integrates **24** state-of-the-art IGL algorithms and **16** diverse graph datasets under a standardized experimental protocol. The benchmark systematically evaluates algorithms across effectiveness (RQ1), robustness to varying imbalance ratios (RQ2), classifier boundary visualization (RQ3), and efficiency/scalability (RQ4), covering both node-level and graph-level tasks for class-imbalance and topology-imbalance scenarios.

## Strengths

- **First unified IGL benchmark with broad coverage.** The paper integrates 24 algorithms and 16 datasets covering both node-level and graph-level tasks, addressing both class-imbalance and topology-imbalance — a scope not achieved by any prior work. This is explicitly stated and demonstrated through the algorithm taxonomy and dataset selection in Sections 3.1–3.2.

- **Standardized experimental protocol enabling fair comparison.** The paper adopts uniform data processing, consistent 1:1:8 train/val/test splits, and reports **four metrics** (Accuracy, Balanced Accuracy, Macro-F1, AUC-ROC) over 10 runs (Section 3.3, RQ1 design). This directly addresses the incomparability caused by inconsistent setups in prior work, as noted in the introduction (items 182–184).

- **Multi-faceted evaluation beyond single-metric effectiveness.** The benchmark systematically analyzes robustness (RQ2) by varying imbalance ratios across five sub-categories with standard deviations, efficiency (RQ4) with training time and GPU memory measurements, and provides qualitative visualizations (RQ3). This goes beyond prior works that typically report only fixed-setting accuracy.

- **Open-sourced benchmark package.** The authors commit to releasing a publicly accessible package for evaluating IGL algorithms (contribution item 3, Section 1), facilitating reproducibility and lowering the barrier for future research.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **RQ2 robustness analysis uses Accuracy rather than imbalance-appropriate metrics.** While the paper correctly uses bAcc, M-F1, and AUC-ROC for RQ1 (line 111), the RQ2 robustness analysis (Section 4.2) explicitly uses Accuracy (lines 192, 228). On imbalanced data, Accuracy is dominated by the majority class, so the robustness claims (e.g., "resampling algorithms are more robust") would be more reliable when verified with balanced metrics. The paper should either repeat this analysis with bAcc or justify why Accuracy is sufficient for the relative-decrease analysis.

- **RQ3 lacks reported quantitative metrics.** The paper states that Silhouette scores are used for quantitative analysis of classifier boundaries (line 119), and describes the score range (line 270), but **never reports any numerical Silhouette values**. RQ3 is supported only by t-SNE visualizations, making its conclusions (e.g., "IGL algorithms shift decision boundaries toward the minority class") qualitative rather than evidenced. Numerical scores should be reported.

- **Overlapping algorithm categories weaken isolation of findings.** Several algorithms (TAM, TOPOAUC, LTE4G, TopoImb) appear in both class-imbalance and topology-imbalance categories because they address both. The RQ2 robustness analysis compares "class-imbalance" against "topology-imbalance" algorithms, but the sets are not exclusive (line 184 acknowledges this). This does not invalidate the benchmark but makes the claim of "orthogonal issues" (line 185) premature. A dedicated "joint" category or clearer separation would strengthen the analysis.

- **Some claims in Section 4.1 are generic without quantified support.** Statements like "All algorithms surpass GCN on at least 5 datasets" and "performance gain on heterophilic datasets is smaller" are qualitative patterns. The paper would benefit from reporting average performance gains or statistical significance tests to substantiate these claims.

- **Missing "balanced oracle" baseline.** The paper compares IGL methods to vanilla GCN/GIN, but does not include a baseline of the same backbone trained on a balanced subsample of the data. Such a baseline would measure how much of the performance gap IGL methods actually close.

### Trivial
- The RQ3 t-SNE figures use multiple subfigures with labels but no visible content (parser issue in the extracted text — the original PDF likely contains them). No change needed.
- The paper mentions "consistent ratio of 1:1:8" for train/val/test splits, which is an unusual choice (80% test) — a brief justification would be helpful.

## Nice-to-Haves
- Report algorithm out-of-memory (OOM) status on the large-scale ogbn-arXiv dataset in a dedicated table, rather than only mentioning it in passing (line 280).
- Provide a brief explanation for the chosen imbalance ratio values (e.g., why Low=ρ=20).
- Add statistical significance tests (e.g., paired t-tests) to claims about which algorithm is "best" on a given dataset.

## Removed Points

- **"Evaluation relies almost entirely on Accuracy, which is inappropriate for imbalanced settings" (Harsh Critic, Issue 1, framed as Fatal).** REMOVED as factually inaccurate regarding RQ1. The paper explicitly states in line 111: *"Results are reported with the metric of Accuracy (Acc.), Balanced Accuracy (bAcc.), Macro-F1 (M-F1), and AUC-ROC over 10 runs."* The tables referenced (e.g., Table~\ref{tab:main_res_node_cls_acc_20}) are included via `\input` and their content is not visible in the extracted text due to parser limitations — there is no evidence they contain only Accuracy. The critic's assertion that the paper's evaluation is "structurally undermined" and that "every table caption mentions only Accuracy" is based on partial information from a parser-stripped document. The Accuracy complaint is valid only for RQ2 (which explicitly uses Accuracy), and this has been kept as a Minor weakness above.

- **"Missing standard deviations in main tables" (Harsh Critic, Issue 3).** REMOVED as unverifiable. The RQ2 robustness figures explicitly include standard deviations (line 228: *"Results are reported with the algorithm performance (Accuracy) with the standard deviation"*). The RQ1 tables are included via `\input` and their content is not visible; we cannot determine whether they contain std devs or not. The paper states results are over 10 runs (line 111), implying variability is tracked. This criticism may be valid for certain tables but cannot be confirmed from the extracted text, so it is removed.

- **"Algorithm selection criteria unclear; GraphSMOTE-NR excluded" (Harsh Critic, Section-by-Section).** REMOVED. The paper clearly states its selection criteria in Section 3.2 — it covers "10 representative" class-imbalance algorithms and lists all included methods with citations. Criticizing the absence of a specific method not included is a subjective scope choice.

- **"Missing related work" (implied).** REMOVED per instructions — I cannot verify the existence of related works.

- **Various formatting/style nitpicks and speculation about appendices.** REMOVED.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation that the paper itself does not already identify.

## Suggestions

1. **For RQ2**: Re-run the robustness analysis using Balanced Accuracy instead of (or in addition to) Accuracy, and verify that the key findings (e.g., resampling algorithms are more robust) hold under imbalance-appropriate metrics.
2. **For RQ3**: Report the numerical Silhouette scores in a table or figure so the "clearer boundaries" claim is quantitatively supported rather than purely qualitative.
3. **Add a "balanced oracle" baseline**: Show how much of the gap between vanilla GCN/GIN and IGL methods is closed, by training on a class-balanced subsample.
4. **Consider a dedicated "joint" algorithm category** for methods that simultaneously address class- and topology-imbalance, to avoid double-counting in category-level comparisons.
5. **Quantify the headline claims** in Section 4.1 with average performance gains or effect sizes rather than generic pattern descriptions.
