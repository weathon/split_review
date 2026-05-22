Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper tackles the detection of illicit Bitcoin flows through Shared Send Mixers (CoinJoin transactions). It makes three contributions: (1) the first complete historical dataset of 163M CoinJoin transactions with Shared Send Untangling (SSU) complexity classifications; (2) novel forensic features — KeyLinker address clustering (based on cryptographic key reuse) and SSU complexity metrics — designed to capture mixing structures; and (3) a semi-supervised learning framework guided by these quality-focused features. The central thesis is that SSL effectiveness in blockchain forensics depends on feature quality rather than data quantity.

## Strengths

- **Large-scale, domain-specific dataset**: The dataset of 163.4M CoinJoin transactions with SSU complexity labels (simple, separable, ambiguous, time-limit, regular) and 4.6M labeled transactions (Table 1) is a significant resource. This is the first complete historical dataset of its kind by the paper's account, spanning Bitcoin's full history up to block 882,421, and is slated for public release.

- **Novel forensic features with clear domain grounding**: KeyLinker address clustering (based on cryptographic key reuse — a higher-fidelity signal than heuristic-based methods) and the SSU complexity metrics are well-motivated by the blockchain domain. The paper plausibly explains why these features should carry better signal than the widely used OTC heuristic.

- **Empirical support for the "quality over quantity" thesis**: Tables 2 and 3 consistently show that adding OTC (a noisy, abundant feature) degrades or does not improve F1 and ROC AUC across all three models (XGBoost, CatBoost, RandomForest), while the REUSE (KeyLinker) and CS features improve performance. This is a clean ablation that supports the paper's central claim about feature quality.

- **Sound experimental design fundamentals**: Three complementary model types are evaluated, stratified 5-fold cross-validation is used, class imbalance is handled through weighting (avoiding oversampling that would conflate with the SSL design), and the dataset is partitioned with a clear train/validation/test split.

## Weaknesses

### Major

1. **Ambiguous and potentially unreliable table presentation (Tables 2 and 3)**: In both tables, multiple rows share identical feature-set checkmarks (all five features selected) but report different metrics — e.g., CatBoost in Table 2 shows three rows with all features checked yielding F1=0.800, 0.830, and 0.827. In Table 3, there are rows that are exact duplicates (e.g., CatBoost SSL rows 7 and 8 both show Precision=0.874, Recall=0.788, F1=0.829, ROC AUC=0.966). The paper states that "We evaluated each model on validation and hold-out datasets" and conducted hyperparameter search, yet the tables do not annotate what distinguishes rows with identical checkmark patterns. This ambiguity undermines reader trust in the quantitative results as presented. The authors must clarify what each row represents (different hyperparameter configs? validation vs. test? cross-validation folds?) and remove exact duplicates.

2. **Pseudo-labeling scheme is critically underspecified for reproducibility**: The paper states that pseudo-labels are selected based on "the top fraction of samples on both sides of the decision boundary, adjusting the share of positives and negatives." No concrete thresholds, fractions, stopping criteria, or iteration counts are reported. The number of pseudo-labels added in each experiment is not disclosed. Without these details, the SSL experiment cannot be reproduced, and the reader cannot assess whether results are sensitive to these choices.

3. **Overclaimed contribution relative to results**: The introduction claims SSL "outperforms supervised baselines," yet the best supervised F1 (0.845) and best SSL F1 (0.845) are identical. The paper later accurately acknowledges that "the semi-supervised phase did not produce dramatic metric gains," but this honest admission contradicts the framing in the contributions. The core thesis (quality over quantity) is supported by the feature ablation, but the paper would benefit from more measured claims about SSL's added value.

### Minor

1. **No confidence intervals or variance estimates**: All metrics in Tables 2 and 3 are reported as point estimates without standard deviations, confidence intervals, or any indication of variability. Given the modest effect sizes (e.g., F1 changes of ~0.02–0.03), it is impossible to assess whether observed differences are statistically significant or within noise. This is a significant gap for an empirical paper.

2. **The "quantity vs. quality" comparison could be more direct**: The paper's experiments compare across feature sets, showing that OTC degrades performance. A stronger test would directly compare: (a) pseudo-labeling using all high-confidence predictions (quantity-driven) vs. (b) pseudo-labeling restricted to quality-filtered predictions (quality-driven) using the same feature set. The current design is an informative ablation but doesn't isolate the quantity-vs-quality tradeoff as sharply as the paper's framing suggests.

### Trivial

1. The claim that SSL is tested against a quantity-driven baseline is not correct — the experiments compare feature sets, not pseudo-labeling strategies — though the feature ablation does speak to the underlying thesis. This is more of a framing mismatch than an experimental flaw.

## Nice-to-Haves

- Quantify pseudo-label reliability: for each feature subset, measure the accuracy of generated pseudo-labels against a held-out labeled set. This would directly validate the "quality" premise.
- Report the number of pseudo-labels added in each SSL experiment so the "quantity" side of the argument is quantified.
- Add a label noise analysis (e.g., noise injection robustness tests) to address the acknowledged limitation of off-chain label sources.
- Compare against a standard SSL baseline (e.g., confidence-thresholded self-training on the full unlabeled pool with the same base classifier).

## Removed Points

- *"The experimental results are unreliable due to duplicated rows"* — Modified and moved to Major weakness #1. The tables have presentation issues (ambiguous rows, some exact duplicates) but the underlying data is not shown to be invalid; different metrics for identical checkmarks likely reflect unlabeled hyperparameter configurations rather than data corruption. The concern is valid but overstated as "untrustworthy."
- *"Label noise not addressed"* — Moved to Nice-to-Haves. The paper acknowledges the limitation and many blockchain papers use the same label sources. Requiring noise quantification is scope creep for this paper's contribution.
- *"Central claim not actually tested"* — Modified and moved to Minor weakness #2. The paper does test it through feature ablation; the criticism about a missing direct quantity-vs-quality control is fair but partial.
- *"SSL doesn't add value"* — Merged into Major weakness #3 (overclaimed contribution). The paper's own results show identical F1 between supervised and SSL; the issue is framing, not a fatal flaw.
- Strength Finder's claim about "Principled selective pseudo-labeling" — Removed. The paper describes the idea but provides insufficient implementation detail to call it "principled" in the strong sense.

## Novel Insights

None beyond the paper's own contributions. The observation that OTC heuristics degrade model performance in CoinJoin detection while KeyLinker and SSU features improve it is the paper's core empirical finding and is well-grounded in the blockchain domain.

## Suggestions

1. Redesign Tables 2 and 3: add a column clarifying what distinguishes rows (hyperparameter config? validation vs. test? cross-validation fold?), remove exact duplicate rows, and ideally report means ± std across cross-validation folds.
2. Provide concrete details on the pseudo-labeling scheme: the selection fraction, the stopping criterion (single batch or iterative), and the number of pseudo-labels added.
3. Tone down the claim that SSL "outperforms supervised baselines" — the results show comparable performance, not superiority.
4. Add confidence intervals or std. devs for all metrics, especially since the reported differences between feature sets are small (0.01–0.03 F1).

## Calibration Report

**Round 1 (Bracketing)**: Weak anchors ~2.5–3.0 (clearly worse: basic blockchain experiments, rejected); middle anchors 4.25–5.75 (FE-GNN at 4.25, BlockFound at 5.75); strong anchors ~7.6+ (clearly better: established methods with stronger results). **Initial bracket: 4.5–7.0.**

**Round 2 (Narrowing)**: Anchors queried at (4.5, 6.5) and (5.5, 7.5). Key comparisons:
- **BlockFound (5.75, rejected)**: Blockchain anomaly detection with only 28 malicious transactions. This paper has a larger, more credible dataset (33K illicit labels) and clearer thesis. **This paper is better.**
- **EX-Graph (6.33, accepted)**: Dataset bridging Ethereum and Twitter. Comparable dataset-scale contribution, similar experimental quality. **Comparable.**
- **FE-GNN (4.25, rejected)**: Incremental GCN+GAT hybrid. This paper has more novelty in features and dataset. **This paper is better.**

These comparisons place the paper near the boundary where solid dataset + feature contributions outweigh experimental presentation issues but where the presentation gaps prevent a higher score.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>