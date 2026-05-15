Now I have verified all the reviewer claims against the paper. Let me construct the final review.

## Summary

The paper introduces TabDPT, a tabular foundation model that combines a row-transformer encoder (adapted from TabPFN) with retrieval-augmented self-supervised pre-training on real-world OpenML data. TabDPT performs both classification and regression via in-context learning, requiring no per-dataset fine-tuning or hyperparameter optimization at inference time. The model achieves competitive results on CC18 (classification) and CTR23 (regression) benchmarks, demonstrates scaling behavior with model size and data volume, and is orders of magnitude faster at inference than methods requiring per-dataset training.

## Strengths

- **Competitive zero-shot performance on established benchmarks**: Table 1 shows TabDPT achieves the highest AUC (0.929, CI [0.927–0.930]) on CC18 classification and the highest correlation (0.833) and R² (0.729) on CTR23 regression—without any per-dataset fine-tuning or hyperparameter optimization. On CC18 AUC, TabDPT's confidence interval does not overlap with XGBoost, CatBoost, or LightGBM, which are the dominant methods in tabular learning and were tuned with extensive HPO. This is a genuine empirical contribution.

- **Dramatic inference-time efficiency**: Figure 3a (runtime analysis) demonstrates that TabDPT is at least one order of magnitude (and up to four orders) faster per 1,000 rows than HPO-tuned baselines when accounting for total runtime. This directly leverages ICL to eliminate per-dataset training, a practical advantage over any method requiring dataset-specific tuning.

- **First scaling-law analysis for tabular ICL models**: Section 5.2 presents a systematic study varying model size (33K to 78M params) and training data volume (52M to 2B cells). The fit to a joint power-law model (α=0.42, β=0.39) demonstrates that tabular ICL models respond predictably to increased scale, and the comparison with synthetic-data-trained PFN++ shows real data becomes increasingly beneficial at larger model sizes. This provides evidence that scaling up tabular models is a viable path forward.

- **Clean ablation isolating key components**: The ablation study (Figure 3b) shows that removing the self-supervised objective causes the largest performance drop, and that retrieval during training (vs. inference-only) provides a clear additional gain. This causally links the paper's methodological choices to its results, even if the mechanism of SSL benefit warrants further analysis.

- **Duel-based ranking as a methodological contribution**: Figures 2a/2b introduce Elo ratings and win-rate matrices for tabular model comparison, addressing the lack of a single accepted benchmark. This is a practical tool the community can adopt.

## Weaknesses

### Fatal
None.

### Major

1. **SSL benefit is confounded with increased training data quantity, not cleanly attributable to cross-task representation learning.** The ablation shows the largest drop when SSL is replaced with supervised target-only training (Figure 3b). However, because SSL generates a target from every training column, it dramatically increases the number of training examples. The paper does not control for total gradient updates or effective data size: a supervised-only model trained for the same number of steps with repeated epochs or synthetic augmentation could potentially match the SSL-trained model's performance. Without this control, the claimed benefit of SSL for *cross-task generalization* cannot be disentangled from brute-force data scaling. This is the most significant methodological gap and directly affects interpretation of the paper's core contribution.

2. **Performance gains are modest on several metrics, especially regression, and the headline "state-of-the-art" claim requires qualification.** On CC18 Accuracy, TabDPT (0.873) is statistically tied with TabR (0.874) and PFN++(kNN) (0.870). On CTR23, TabDPT's correlation (0.833) and R² (0.729) have confidence intervals overlapping with TabR, XGBoost, LightGBM, CatBoost, and MLP-PLR. The improvement over PFN++(kNN)—the architecture-matched baseline differing only in synthetic vs. real pre-training data—is 0.002 AUC on CC18 with overlapping CIs. While TabDPT clearly leads on CC18 AUC, the overall picture is that gains are concentrated on the classification AUC metric and are more equivocal elsewhere. The paper would benefit from tempering the SOTA claim to reflect this heterogeneity.

3. **Contamination analysis, while present, has gaps given that both training and evaluation data are drawn from the same repository (OpenML).** The paper performs metadata-level checks (dataset names, file hashes, feature statistics, linear fit coefficients) and manual inspection of flagged pairs (Section 4.3). This is reasonable as a first pass but does not rule out near-duplicates or datasets that share substantial feature overlap with evaluation tasks. A stronger analysis would measure feature-space similarity between training and evaluation datasets or test on a held-out set of non-OpenML benchmarks. Since the performance advantage is marginal on several metrics, even subtle leakage could affect the conclusions. This concern is amplified by the paper's central claim of zero-shot generalization.

### Minor

1. **The scaling analysis varies data volume from a fixed pool of 123 datasets, not data diversity.** The experiments increase the number of rows/cells drawn from the same 123 datasets, which is meaningfully different from scaling the number of distinct pre-training tasks. The claim "tabular data obeys scaling laws like other domains" would be substantially stronger if it also showed that adding *new, diverse* datasets continues to improve performance. As presented, the scaling law is demonstrated for data quantity, not data diversity. The paper acknowledges that future work could curate larger pre-training datasets, but this conflates "more data" with "more diverse data."

2. **The SSL description lacks detail needed for exact reproducibility.** The paper states that for high-cardinality columns in the self-supervised task, values are "distributed over random partitions" and used as target classes, but does not specify the partitioning procedure (e.g., number of bins, whether partitioning is stratified or random, how ties are handled). Similarly, the criteria for selecting a "random column" (e.g., minimum unique values threshold) are not quantified.

3. **The ablation figure (Figure 3b) reports only relative reduction without absolute values or y-axis labels**, making it impossible to assess the magnitude of performance drops. The text describes which components matter most but provides no numerical grounding.

4. **The impact of the training-time retrieval approximation (local groups vs. exact kNN) is not analyzed.** The paper acknowledges the approximation (Section 3.3) but provides no comparison of retrieval fidelity between the two approaches, making it unclear how much performance is lost relative to exact search.

### Trivial
- The caption of Figure 3c (runtime) and the ablation figure use font sizes that are very small, making the plots hard to read in print.
- The conclusion re-uses near-identical phrasing from the abstract and introduction without adding synthesis.

## Nice-to-Haves
- A controlled ablation where the supervised-only model is trained for the same number of gradient updates as the SSL model (using repeated epochs) to disentangle SSL's mechanism from data quantity.
- A data-diversity scaling experiment (varying the number of distinct training datasets while holding total rows/cells approximately constant).
- A per-dataset breakdown of TabDPT vs. TabR (the strongest baseline) to reveal which dataset characteristics favor or disfavor the method.
- Evaluation on non-OpenML benchmarks (e.g., Grinsztajn et al.'s benchmark, Financial datasets) to strengthen the zero-shot generalization claim.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"TabDPT's AUC overlaps with XGBoost and CatBoost"** — Factually wrong. TabDPT's CI [0.927–0.930] does NOT overlap with XGBoost [0.923–0.926] or CatBoost [0.922–0.925]. This error inflates the severity of the empirical-gains criticism.
2. **"The only unambiguous improvement is over TabPFN and kNN—weak baselines"** — Factually wrong. TabDPT clearly beats XGBoost, CatBoost, and LightGBM on CC18 AUC with non-overlapping CIs. Tree-based methods are the dominant paradigm in tabular learning and are not "weak baselines."
3. **"The Elo ratings are biased and this is not accounted for"** — The paper directly addresses this: "we were able to simply omit them due to the paired nature of duel-based metrics. Thus, the outcome is more favourable for the baselines, making the leading position of TabDPT even more impressive." This is a strawman.
4. **"The scaling figure caption is misleading because synthetic data volume cannot be varied"** — The paper is clear that PFN++ uses a fixed prior generator and plots it as a separate (dotted) curve not fit to the scaling law. The claim "synthetic data becomes less useful as models grow larger" is about model size, which is varied for both conditions. The comparison is valid on its own terms.
5. **"Tabula-8B comparison on 61 datasets is irrelevant"** — This is a judgment call, not a factual weakness. Including it provides useful context about LLM-based TFMs' limitations.
6. **"The paper should include more missing related work"** — Per meta-reviewer guidelines, this cannot be verified without external sources.

## Novel Insights
The most interesting cross-perspective insight is not a weakness but a tension: the harsh critic argues the gains are marginal and the scaling analysis incomplete, while the strengths show consistent evidence across multiple benchmarks and ablations. The disagreement largely dissolves once one separates classification (where TabDPT's advantage on AUC is clear) from regression (where the picture is noisier). This suggests the paper's framing should more carefully distinguish between these settings rather than claiming uniform SOTA. A second synthesis: both the reviewer and the paper agree that the SSL benefit is real, but disagree on its explanation. The paper attributes it to cross-task representation learning (plausible but untested); the reviewer attributes it to brute-force data scaling (also plausible). Resolving this would require the controlled ablation suggested above and would significantly strengthen the paper.

## Suggestions

1. **Temper the "state-of-the-art" claim** to acknowledge that the advantage is clearest on CC18 AUC and more equivocal on Accuracy and all CTR23 metrics. Add a summary sentence in the abstract/results that qualifies which metrics show clear separation.
2. **Add a controlled SSL ablation** training a supervised-only model for the same number of gradient updates (via repeated epochs or synthetic augmentation) to disentangle representation quality from data quantity.
3. **Strengthen contamination analysis** with feature-space similarity measures between training and evaluation datasets, or include results on at least one non-OpenML benchmark suite.
4. **Add a data-diversity scaling experiment** varying the number of distinct training datasets while controlling for total data volume.
5. **Provide absolute performance numbers and labeled y-axes** in the ablation figure.
6. **Quantify the retrieval approximation loss** by comparing exact vs. approximate retrieval on a held-out set.

## Score and Decision

The paper makes a meaningful empirical contribution: it demonstrates that real-data pre-training with SSL and retrieval can produce a tabular ICL model competitive with tuned tree-based methods on widely-used benchmarks, while being orders of magnitude faster at inference. The scaling analysis, while limited to data quantity rather than diversity, is a first step in an underexplored direction. The weaknesses—particularly the SSL confound and modest gains on regression—are real but not fatal to the paper's main contribution. The central empirical result (CC18 AUC leadership over HPO-tuned XGBoost/CatBoost/LightGBM) is robust and non-trivial. The paper would benefit from stronger controls and more precise claims, but the core results support acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>