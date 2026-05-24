Now I have all the information I need to produce the final consolidated review. Let me compile everything carefully.

---

## Summary

This paper addresses the detection of illicit transactions within Bitcoin's CoinJoin (Shared Send Mixer) transactions. It contributes (1) a large historical dataset of 1.15B Bitcoin transactions including 163M CoinJoin transactions with 4.6M labeled instances, (2) novel high-fidelity forensic features—KeyLinker address clustering (based on cryptographic key reuse) and Shared Send Untangling (SSU) complexity metrics—and (3) an empirical study applying supervised and self-training-based semi-supervised learning across three tree-ensemble classifiers with systematic feature ablation. The paper's central thesis is that data quality (high-fidelity features) matters more than data quantity, and that SSL succeeds only when guided by quality-focused features.

## Strengths

- **Exceptional dataset scale and completeness.** Table 1 documents 1.15 billion total transactions, 163 million CoinJoin transactions, and 4.6 million labeled CoinJoin instances—an order of magnitude larger than any prior public resource for this task. The dataset integrates multiple labeling sources (WalletExplorer, Elliptic++, MBAL, Kaggle) with manual deduplication of conflicting labels, and spans Bitcoin's entire history up to February 2025. This alone is a substantial contribution to blockchain forensics research.

- **Convincing feature ablation demonstrating that high-fidelity features (KeyLinker, SSU) outperform noisy heuristics (OTC).** Across all three models and both supervised (Table 2) and SSL (Table 3) settings, adding OTC consistently degrades F1-score (e.g., XGBoost supervised drops from 0.844 to 0.841 when OTC is added to default+reuse+cs; SSL drops from 0.842 to 0.821 when OTC is added to default+reuse+cs+ssu). Conversely, KeyLinker (REUSE) and CS features produce measurable gains. This ablation is systematic and the pattern is consistent across models.

- **Novel, well-motivated domain-specific features.** KeyLinker (Smolenkova & Yanovich, 2025) leverages cryptographic key reuse for address clustering, providing a higher-fidelity alternative to heuristic-based clustering. The SSU complexity classification (Larionov & Yanovich, 2023) categorizes transactions by untangling difficulty (simple, separable, ambiguous, time-limited, regular), capturing structural properties of mixing that are directly relevant to forensic analysis. Both are grounded in prior published work and are non-trivial to implement.

- **The quality-over-quantity principle is demonstrated across both supervised and SSL regimes.** The consistent degradation from OTC across all model types and training paradigms provides empirical evidence that not all features (or pseudo-labels) are equally valuable—a finding with practical implications for forensic tool-building.

## Weaknesses

### Fatal
None.

### Major

- **The central SSL claim is overstated and the experimental design does not test the scenario that motivates the paper.** The paper's introduction frames SSL as a solution to label scarcity for CoinJoin transactions, yet the experiments train on all 4.6M available labeled instances before applying self-training. The resulting SSL gains are negligible: XGBoost improves from 0.842 (supervised, default+reuse+cs+ssu) to 0.845 (SSL, same features), a difference of 0.003. The paper itself acknowledges this (line 297: "The semi-supervised phase did not produce dramatic metric gains"). A proper test of the motivating claim would require training on small fractions of the labeled set (e.g., 1%, 5%, 10%) and measuring whether SSL recovers performance, and whether high-quality features amplify that recovery. Without this, the headline conclusion that SSL "effectively leverages unlabeled data" and that the framework "outperforms supervised baselines" is not supported by the evidence presented.

- **No external SSL baselines or comparisons with cited state-of-the-art methods.** The paper evaluates only XGBoost, CatBoost, and Random Forest with self-training. Missing are comparisons against (i) standard SSL methods applicable to tabular data (e.g., label propagation, label spreading, or self-training variants with confidence calibration), or (ii) the GNN-based and gradient-boosted detectors the paper itself cites as achieving >90% accuracy on related tasks (Nerurkar, 2022; Nerurkar et al., 2021). Without such baselines, it is impossible to assess whether the proposed combination of features and self-training is competitive, or whether the dataset and features offer advantages over existing techniques.

### Minor

- **Feature specification is insufficient for reproducibility.** The "DEFAULT" features are described only at a high conceptual level (line 205: "UTXO attributes, such as the average lifetime of outputs and the number of inputs and outputs"; "transaction values, from basic sums and fees to more nuanced indicators like the market concentration index"; "address-level behavior, for instance, whether addresses repeat across inputs and outputs"). The exact feature set, cardinality, how each is computed from raw blockchain data, and how categorical features (e.g., off-chain service associations) are one-hot encoded are never enumerated. The pseudo-labeling scheme is similarly underspecified: batch size, the top fraction used for selection, and how the positive/negative share is adjusted are not disclosed.

- **The SSL-specific mechanism is not isolated from the supervised feature-quality effect.** The feature-quality ranking (KeyLinker+CS+SSU > ... > +OTC) is already fully visible in the supervised results (Table 2). The SSL results (Table 3) simply mirror this same ranking. There is no experiment that isolates pseudo-label quality independently of input features—for example, comparing confidence-based selection to random selection while holding the feature set fixed, or grouping pseudo-labels by SSU complexity class while controlling for feature set. The paper therefore demonstrates that certain features are better than others, but not that SSL depends on quality in a way that is distinct from supervised learning.

- **Table presentation is confusing.** Tables 2 and 3 use a checkmark-only notation where several rows per model appear to have identical checkmark patterns but report different metrics (e.g., XGBoost rows 6 and 7 in Table 2 both show all five columns checked but give F1-scores of 0.842 and 0.840 respectively). It is unclear what distinguishes these rows. Additionally, the text (line 254) reports "XGBoost achieves the best supervised performance with an F1-score of 0.845 (default+reuse+cs+ssu)" but Table 2 shows 0.842 for that feature set—the 0.844 is on a different row (default+reuse+cs without SSU). This inconsistency between text and table undermines confidence in the reported numbers.

- **No variance estimates or significance testing.** Given that the SSL-vs-supervised differences are often ≤0.005 in F1, reporting standard deviations or confidence intervals across cross-validation folds would allow the reader to distinguish signal from noise. The claim that "pseudolabeling slightly increased recall (up to +0.03) while reducing precision (from -0.04 to -0.05)" may fall within experimental noise.

### Trivial
- The paper references related work that uses GNNs and gradient-boosted models achieving >90% accuracy, but the reported F1-scores (~0.84) are not directly comparable since the cited works operate on different tasks (general transaction classification vs. CoinJoin-specific detection). This context could be clarified.

## Nice-to-Haves

- A label-scarcity experiment (training on 1%, 5%, 10% of labeled data) comparing supervised vs. SSL performance across feature sets would directly address the paper's motivating claim and dramatically strengthen the contribution. This is a feasible experiment given the dataset size.
- A direct pseudo-label quality analysis: compare model performance when pseudo-labels are selected by confidence vs. randomly, holding the feature set fixed, to isolate whether selective pseudo-labeling itself provides benefit beyond the feature quality.
- Including at least one standard SSL baseline (e.g., label propagation) would help contextualize the self-training approach.
- Clarifying the dataset release terms (which artifacts—raw transactions, feature vectors, labels—and under what license) would help the community assess the contribution's long-term impact.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"No handling of potential label leakage between the unlabeled pool and the test set"* — The paper states (line 218): "We partitioned the labeled dataset of 4.62 million CoinJoin transactions into training (80%), validation (10%), and test sets (10%), maintaining class proportions." The split is described; pseudo-labels come from unlabeled CoinJoin transactions, not from the test set. The harsh critic's concern about leakage is speculative without evidence.

- *"The dataset release is promised, but the paper does not specify what artifacts will be shared"* — This is a valid minor point but was moved to Nice-to-Haves since dataset release commitments are typically negotiable during the publication process.

- *"DEFAULT features are vaguely listed"* — Kept as Minor; the specification is indeed vague, but the paper gives enough context (four groups with examples) that a domain expert could reconstruct something similar. The concern is real but not fatal.

- *"The SSL comparison amounts to an ablation study rather than a comparison with the state of the art"* — This is a framing issue. The ablation is genuinely useful. The absence of external SSL baselines is retained as Major.

- *"Could the metric be measuring a proxy?" / "Are confounders controlled?"* — These speculative concerns from the harsh critic have no concrete anchor in the paper and are removed.

- *The strength finder's claim that "SSL experiments directly validate the quality over quantity principle"* — This overstates what the experiments show for SSL specifically; the pattern is present in both supervised and SSL results. Retained only the supervised ablation as a strength.

## Novel Insights

The paper's most interesting empirical finding is the consistent and cross-model degradation caused by the One-Time Change (OTC) heuristic when used as a feature. OTC is widely used in blockchain forensics as a standard clustering heuristic, yet adding it to any feature combination in either supervised or SSL settings reduces F1-score across all three model architectures. This is a concrete, actionable finding: a widely-adopted heuristic in the forensics community may actually harm machine-learning-based detection. The paper demonstrates that cryptographic-proof-based clustering (KeyLinker) is a superior alternative, which is a genuinely useful insight for practitioners building forensic ML pipelines.

## Suggestions

- Reframe the paper as a dataset + feature engineering contribution with a supervised ablation study, and demote the SSL claim from a headline contribution to an exploratory extension. The dataset and feature analysis are strong enough to stand on their own.
- If the SSL framing is retained, the label-scarcity experiment described in Nice-to-Haves is essential. The paper's motivating scenario (scarce labels for mixed transactions) is exactly what that experiment would test.
- Add standard deviations or confidence intervals for all metrics. With differences as small as 0.003-0.005 in F1, readers need to know whether these are meaningful.
- Clarify Table 2/3 rows: if rows with identical checkmarks represent different experimental configurations or are duplicates, this must be made explicit.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| q7Xi4yZYcH (TRW-GCN for Ethereum) | 3.00 | R1 | Current paper has much larger dataset and more thorough feature ablation |
| FE-GNN (yM7rw8Bo1f) | 4.25 | R1 | Current paper has orders-of-magnitude larger dataset, more novel features |
| BCG (nwjgeFGbAF) | 5.25 | R2 | Pure dataset paper; current paper adds novel feature contributions and ablation |
| BlockFound (LPXfOxe0zF) | 5.75 | R1/R2 | More novel model design; current paper has stronger dataset but weaker model novelty |
| EX-Graph (juE0rWGCJW) | 6.33 | R2 | Dataset paper accepted; current paper's dataset is larger but SSL claim is oversold |

**Round-1 bracket:** 4.5–6.5. The paper is clearly stronger than FE-GNN (4.25, incremental GNN with smaller dataset) and weaker than the high-band anchors (8.0, which are strong SSL theory/benchmarking papers not topically comparable).

**Round-2 narrowing:** Compared to BCG (5.25), this paper offers a much larger dataset plus novel algorithmic features (KeyLinker, SSU) rather than just dataset construction. Compared to EX-Graph (6.33), this paper's dataset is substantially larger and includes novel feature contributions, but EX-Graph had cleaner framing and better-supported claims. The current paper's SSL overselling and missing baselines pull it below EX-Graph. Compared to BlockFound (5.75), the current paper has less model novelty but stronger empirical breadth (feature ablation across models). The paper sits between BCG (5.25) and BlockFound (5.75), closer to the latter.

**Final assessment:** The dataset and feature engineering contributions are genuine and well-executed. The systematic demonstration that OTC degrades performance while KeyLinker/SSU improves it is a valuable empirical finding. However, the paper's central framing around SSL is not supported by the experiments: SSL gains are negligible (≤0.003 F1), no label-scarcity regime is tested, and no external SSL baselines are included. These are structural weaknesses in the experimental design that prevent the paper from convincingly supporting its headline claim. The paper would be stronger reframed as a dataset + feature engineering contribution.

**Score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>