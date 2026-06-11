Now I have sufficient calibration data. Let me synthesize the final review.

**Round 1 bracket**: Between 3.0 and 6.0. Clearly better than weak blockchain anomaly detection papers (3.0-4.0) due to much larger dataset and systematic ablation. Comparable to rejected SSL papers (5.0-5.5) but with a stronger dataset contribution and weaker methodological novelty.

**Round 2 narrowing**: Between 4.0 and 5.5. Comparing against FE-GNN (4.25, blockchain classification, rejected for incremental improvement + no error bars), DIPS (5.0, pseudo-labeling quality, rejected despite good writing and novel framework), and Multimodal Banking Dataset (5.5, large dataset contribution, rejected with mixed reviews 3-8).

**Final positioning**: The paper has a genuine dataset contribution (163M CoinJoin transactions) that exceeds most anchors, plus novel domain-specific features (KeyLinker, SSU) with solid ablation. However, the central SSL claim is unsupported by results, the pseudo-labeling is underspecified, and there are no error bars. The paper is clearly better than FE-GNN (4.25) but comparable to or slightly worse than DIPS (5.0) which had a stronger methodological contribution. I score it at **4.5**.

---

## Summary
This paper presents a large-scale CoinJoin transaction dataset (163M transactions) with domain-specific feature engineering (KeyLinker address clustering and SSU complexity metrics) and a semi-supervised learning framework using pseudo-labeling for detecting illicit Bitcoin transactions. The authors argue that SSL success depends on feature/data quality rather than data quantity, evidenced through systematic feature ablation across XGBoost, CatBoost, and Random Forest.

## Strengths
- **Large-scale, valuable dataset**: Table 1 documents 1.15 billion total transactions, 163.4M CoinJoin transactions, and 4.6M labeled CoinJoin transactions—significantly larger than prior work cited in the paper (e.g., Nerurkar 2022 used 13M transactions). This is a genuine infrastructure contribution for the blockchain forensics community.
- **Systematic feature ablation across models and settings**: Tables 2 and 3 jointly provide ablation across 5 feature groups (DEFAULT, REUSE, CS, OTC, SSU) and 3 model families in both supervised and SSL settings. The consistent pattern—REUSE+CS features improve F1 (e.g., XGBoost from 0.814→0.837→0.844, Table 2) while OTC features degrade it across all models and both settings—provides solid empirical evidence for the importance of feature selection.
- **Domain-grounded novel features**: KeyLinker leverages cryptographic key reuse patterns (a signal based on cryptographic proof rather than behavioral heuristics), and SSU complexity metrics classify transactions into 5 untangling categories. These are specifically designed for CoinJoin structures and yield measurable gains when added.

## Weaknesses

### Fatal
None.

### Major
- **Central third contribution ("SSL outperforms supervised baselines") is not supported by the reported results.** Introduction point 3 (line 29) claims to "demonstrate that a semi-supervised learning framework outperforms supervised baselines." However, comparing the best results: XGBoost SSL best F1 = 0.845 (Table 3, line 315) is identical to the supervised best F1 = 0.845 (text, line 250); CatBoost SSL shows +0.004 F1 (0.830→0.834); Random Forest SSL shows −0.004 F1 (0.830→0.826). No error bars, confidence intervals, or statistical significance tests are reported. With 5-fold cross-validation, these differences are almost certainly within noise. The paper itself acknowledges SSL "did not produce dramatic metric gains" (line 293) but continues to frame results as confirming its thesis.

- **Pseudo-labeling methodology is critically underspecified.** Section 5.3 (line 228) states "in each batch only the most confident predictions are retained" and "we select the top fraction of samples on both sides of the decision boundary, adjusting the share of positives and negatives." The actual fraction(s) used, the number of pseudo-labels added per configuration, and confidence score distributions are never reported. For a paper whose central methodological contribution is pseudo-labeling, this makes the SSL experiments non-reproducible.

- **"Quality over quantity" thesis conflates feature selection with a novel SSL insight.** The paper claims SSL gains depend on feature quality (line 287). The evidence is that adding OTC features degrades performance in both supervised AND SSL settings. However, the paper never reports: (a) how many pseudo-labels were generated under each feature configuration, (b) the estimated accuracy of those pseudo-labels, or (c) data showing OTC produces *more but worse* pseudo-labels. Without this, the observation reduces to the well-known principle that noisy features degrade any model—not a novel insight specific to SSL and data quality.

### Minor
- **PR AUC listed as evaluation metric but never reported.** Line 222 states models were assessed using "ROC AUC, Precision-Recall AUC, F1-score, precision, and recall metrics," but Tables 2 and 3 only show Precision, Recall, F1, and ROC AUC. Given the ~12% class imbalance (line 220), PR AUC would be more informative than ROC AUC.
- **Only tree-based models evaluated.** Given that the paper cites prior work achieving 91–92% accuracy with GNNs (lines 116–119), the absence of any neural or graph-based baselines limits the scope of the evaluation.
- **Conclusion overstates findings.** Line 331 states "models trained on strategically expanded high-quality data outperform those trained on larger, noisier datasets," which is not demonstrated by the ±0.004 F1 differences.

### Trivial
- Table formatting: Multiple rows in Tables 2 and 3 appear to have identical checkmark patterns across all 5 feature columns but different metric values, making the feature combinations difficult to parse (likely a layout/annotation issue).

## Nice-to-Haves
- Reporting pseudo-label statistics (count, distribution, estimated accuracy per feature configuration) would directly substantiate the claimed mechanism.
- Adding standard deviations from 5-fold cross-validation to all reported metrics.
- Reframing the paper around the dataset and features (genuine contributions) with SSL as a secondary demonstration would be more honest.
- A deeper analysis of *why* OTC is harmful (feature noise vs. label noise propagated through OTC clusters) would strengthen the contribution.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Strength finder's claim about "formal problem formulation connecting domain concepts to ML" in Section 4: this is a reasonable but standard formulation, not a distinguishing strength.
- Strength finder's claim about "appropriate evaluation methodology for imbalanced classification": using F1/ROC-AUC and class weighting is standard practice, not a novel methodological choice.
- Harsh critic's concern about comparison fairness: the comparison between supervised and SSL is fair in that the same models are used; the issue is that the results don't show improvement, not that the comparison is unfair.

## Novel Insights
The paper's genuinely novel observation is that in CoinJoin transaction classification, the One-Time Change (OTC) clustering heuristic consistently degrades model performance (both supervised and SSL) despite being widely used in blockchain analytics. Combined with the finding that KeyLinker (cryptographic key reuse) and Common Spending (CS) features consistently improve F1, this provides domain-specific evidence for feature quality in blockchain forensics. However, the extension to a general SSL principle ("quality over quantity") is not substantiated by the reported experiments.

## Suggestions
- Report pseudo-label statistics: number of pseudo-labels generated per feature configuration, their confidence distributions, and estimated accuracy (validated against the labeled test set).
- Add standard deviations from 5-fold cross-validation to all reported metrics.
- Reframe the SSL component as a secondary, exploratory demonstration rather than a primary contribution, centering the paper on the dataset and feature engineering.
- Add at least one comparison beyond tree-based classifiers (e.g., a simple MLP or GNN approach) to contextualize against prior work.

## Calibration Report

**All retrieved anchors:**

| Paper Path | Avg Score | Round | Comparison |
|---|---|---|---|
| q7Xi4yZYcH (Ethereum anomaly detection) | 3.00 | 1 | Weaker: less novel methodology, smaller dataset |
| 51cjeYcXjs (Malware search/retrieval) | 2.50 | 1 | Much weaker: different domain |
| ctzGqxE3O0 (Android malware detection) | 2.50 | 1 | Much weaker: different domain |
| YZ7NWYBd5z (Identity swap detection) | 3.00 | 1 | Weaker: different domain |
| uw5U7FfTRf (Backdoor detection) | 3.00 | 1 | Weaker: different domain |
| X8RTdxzqJQ (Two-sample testing SSL) | 4.80 | 1 | Comparable: rejected, clearer writing, stronger theory |
| dpnPOXoqVQ (S²MAM SSL) | 4.75 | 1 | Similar: rejected, limited empirical novelty |
| dnqPvUjyRI (SemiReward SSL) | 6.00 | 1 | Stronger: accepted, extensive benchmarks, novel method |
| DFQCJmHPoe (Adversarial PU learning) | 3.75 | 1 | Weaker: different domain |
| YO6Je9jOJI (LLM tabular self-supervised) | 4.00 | 1 | Similar: rejected |
| xriGRsoAza (Interpretable time series) | 8.00 | 1 | Much stronger: accepted, different domain |
| cJs4oE4m9Q (Anomaly detection) | 8.00 | 1 | Much stronger: accepted |
| IGzaH538fz (GNN certification) | 8.00 | 1 | Much stronger: accepted, theoretical contribution |
| bWcnvZ3qMb (FITS time series) | 8.00 | 1 | Much stronger: accepted |
| WyEdX2R4er (VLM data type) | 8.00 | 1 | Much stronger: accepted |
| yM7rw8Bo1f (FE-GNN blockchain) | 4.25 | 1 | Comparable: same domain, smaller dataset, incremental |
| ns0KIpfQVy (Multimodal Banking Dataset) | 5.50 | 1 | Comparable: dataset contribution, mixed reviews |
| GrHewano8m (XXLTraffic) | 5.75 | 1 | Slightly stronger: rejected, domain-specific benchmark |
| cNThpik3Jz (LLM feature engineering) | 4.50 | 1 | Similar: feature engineering focus |
| jhiByZpuIS (MSfusion) | 4.67 | 1 | Similar: rejected |
| eSO9quCgmz (DIPS pseudo-labeling) | 5.00 | 1/2 | Comparable: stronger methodology, similar overall |
| jjjxp9Wgjp (Pseudo-labels OOD) | 4.25 | 2 | Similar: rejected |
| huwR9N2ea0 (SSDG domain generalization) | 5.50 | 2 | Slightly stronger: clearer methodology |
| AEi2wyAMyb (BOPL pseudo-labeling) | 5.33 | 2 | Comparable: rejected despite novel optimization |
| EjJD16oaly (GTR SSL thresholding) | 4.50 | 2 | Similar: rejected, limited improvements |
| 1CeIRl147S (Domain-specific benchmarking) | 4.33 | 2 | Similar: benchmark/dataset paper |
| hKeHfOUCXL (Energy forecasting benchmarks) | 4.25 | 2 | Similar: benchmark paper |
| powufeT93G (Domain-specific embeddings) | 5.25 | 2 | Slightly stronger: cleaner empirical study |
| ybiwT2yP1c (BIRB bioacoustics) | 5.00 | 2 | Comparable: dataset contribution |
| GtnNhtuVrc (SSL semantic segmentation) | 5.25 | 2 | Slightly stronger: clearer contribution |
| 2OwSqvxjP2 (Boosting SSL confidence) | 5.50 | 2 | Slightly stronger: more targeted method |
| XT2yAa6Bbp (Sinkhorn pseudo-labels) | 5.50 | 2 | Slightly stronger: novel SSL method |
| 6yXAKleluj (Probabilistic TRW-GCN) | 4.00 | 2 | Weaker: smaller scale, similar blockchain domain |
| p2QAOORDoG (TIDMAD dark matter) | 3.75 | 2 | Weaker: different domain |
| cazOlqncU6 (Trustworthy dataset proof) | 4.50 | 2 | Similar: rejected |

**Round 1 bracket**: 3.0–6.0. The paper is clearly better than weak blockchain papers (3.0–4.0) due to the much larger dataset and systematic ablation, but weaker than accepted SSL methods (6.0).

**Round 2 narrowing**: 4.0–5.5. The paper is comparable to FE-GNN (4.25, same domain, smaller dataset) but has a much larger dataset contribution. It's comparable to DIPS (5.0) and BOPL (5.33) which had stronger SSL methodology but were also rejected. The paper's dataset contribution pushes it above 4.25, but the unsupported SSL claim keeps it below 5.0.

**Final score**: 4.5. The genuine dataset and feature engineering contributions elevate the paper above the blockchain-specific anchors, but the unsupported central SSL claim, underspecified pseudo-labeling, and missing error bars keep it below the rejected SSL papers in the 5.0–5.5 range. The paper has real contributions but overstates its SSL findings.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>