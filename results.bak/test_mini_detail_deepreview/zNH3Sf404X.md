Now I have good calibration context. Let me write the consolidated review.

## Summary

This paper proposes a semi-supervised learning framework for detecting illicit Bitcoin flows through CoinJoin mixers, combining a large-scale dataset of 163M CoinJoin transactions (collected up to block 882,421) with feature engineering that applies KeyLinker address clustering, SSU complexity metrics, and standard heuristics (CS, OTC). The central thesis is that data quality (via careful feature engineering) matters more than data quantity for SSL in this domain. The main empirical findings are (1) that OTC features degrade performance despite increasing feature count, and (2) that the best feature set (DEFAULT+REUSE+CS+SSU) gives F1 ~0.84 with gradient-boosted models.

## Strengths

- **Large-scale, carefully constructed CoinJoin dataset integrating multiple labeling sources.** The paper provides the first complete historical dataset of 163M Bitcoin CoinJoin transactions (Table 1), integrating on-chain data up to block 882,421 with off-chain labels from WalletExplorer, Elliptic++, MBAL, and Kaggle. At 163M transactions with 4.6M explicitly labeled, this is substantially larger than most public blockchain forensic datasets. The manual resolution of duplicate/conflicting labels (Section 5.1) is a genuine data-quality step that many related works omit.

- **Systematic feature ablation across three models and five feature groups.** Tables 2 and 3 exhaustively report precision, recall, F1, and ROC-AUC for every combination of DEFAULT, REUSE, CS, OTC, and SSU features on CatBoost, XGBoost, and Random Forest. This rigorous ablation cleanly isolates the contribution of each feature type and provides actionable guidance for practitioners. The finding that OTC features *degrade* performance (e.g., XGBoost F1 drops from 0.844 to 0.841 in supervised, and from 0.845 to 0.836 in SSL) is counterintuitive and empirically well-demonstrated.

- **Addresses an important and underserved problem.** Detecting illicit flows in CoinJoin transactions is inherently difficult due to obfuscation, and the scarcity of reliable labeled data in this domain makes the semi-supervised framing appropriate. The paper's emphasis on feature quality over blind data accumulation is a sensible methodological lens.

## Weaknesses

### Major

- **The central claim that SSL outperforms supervised learning is not supported by the reported metrics.** The introduction (Contribution 3) states that the SSL framework "outperforms supervised baselines by leveraging unlabeled data strategically." However, the best supervised XGBoost F1 is 0.844 (Table 2, DEFAULT+REUSE+CS) and the best SSL XGBoost F1 is 0.845 (Table 3, DEFAULT+REUSE+CS+SSU). This difference of 0.001 is essentially identical performance, not "outperformance." No variance is reported (no standard deviations, confidence intervals, or per-fold results), so even this tiny difference is uninterpretable. The paper's own Section 6.3 acknowledges that SSL "did not produce dramatic metric gains," which directly contradicts the stronger framing in the introduction and abstract. The SSL results show modest recall improvements (+0.03) at the cost of precision drops (−0.04 to −0.05) with no net F1 gain. A paper whose central narrative is "SSL works when guided by quality features" needs to demonstrate SSL meaningfully improving over a strong supervised baseline, not merely matching it.

- **Features described as "novel" are drawn without adaptation from prior work.** The paper presents as contributions "novel, high-fidelity features—KeyLinker address clustering and Shared Send Untangling (SSU) complexity metrics" (Section 1, Contribution 2). Both are cited as existing techniques: KeyLinker from Smolenkova & Yanovich (2025) and SSU from Larionov & Yanovich (2023). The paper applies these features in a new pipeline and evaluates them, which is a valid contribution, but claiming them as novel features is misleading. The actual novelty lies in the systematic evaluation and the finding that OTC features are harmful, not in the features themselves. Reframing would be appropriate.

- **No comparison to existing methods for illicit Bitcoin/blockchain detection.** The Related Work section (Section 3) extensively cites prior methods achieving high accuracy — GNN-based approaches (Nerurkar 2022, 92% accuracy), gradient-boosted ensemble models (Nerurkar et al. 2021, 91%), decision-tree mixing service detection (Rathore et al. 2022, 97% detection rate), and hypergraph-based methods (Lee et al. 2024). Yet the paper evaluates only Random Forest, XGBoost, and CatBoost on its own dataset. Without benchmarking against any of these prior methods (either by reimplementation on the same dataset or by evaluating on a common benchmark like Elliptic), it is impossible to assess whether the proposed feature pipeline or SSL framework advances the state of the art. This omission weakens the significance claim.

- **The "quality over quantity" principle for pseudo-labeling is stated but not directly implemented or tested.** Section 5.2 articulates a principle that pseudo-labels should be selected based on SSU complexity class (Simple/Separable) and clustering heuristic fidelity (KeyLinker over OTC). However, the actual SSL method (Section 5.3) uses standard confidence-thresholding pseudo-labeling — selecting the top fraction of most confident predictions on both sides of the decision boundary. The paper asserts (Section 6.3) that confident predictions are "disproportionately found in the more tractable SSU complexity classes," but provides no empirical analysis of pseudo-label distribution across SSU classes, no comparison of pseudo-labels from high-SSU vs. low-SSU transactions, and no ablation varying pseudo-label quality. The principle is supported only by the feature-level ablation (OTC harms), not by any direct test of pseudo-label quality filtering. The paper conflates "using high-quality input features" with "selecting high-quality pseudo-labels," but these are distinct.

### Minor

- **No uncertainty or variance reported for any metric.** All tables show point estimates only. With only 33K illicit examples across a highly imbalanced dataset (12% illicit in the labeled set), per-fold variation could be substantial. Without confidence intervals or standard deviations, the reader cannot assess whether the reported differences (e.g., F1 0.844 vs 0.845) are meaningful or noise. This is especially problematic given that the paper's headline comparison depends on such small differences.

- **Dataset label quality is not validated.** The paper acknowledges that off-chain labeling sources may introduce inaccuracies (Section 5.1) and mentions manual resolution of conflicts, but provides no details on the expected label error rate, how many conflicts were encountered, or how they were resolved. No comparison to established datasets (e.g., Elliptic) or manual verification study is performed. For a dataset claimed as a primary contribution, this validation gap is significant.

- **No comparison to any alternative SSL method.** The paper evaluates only one SSL approach (self-training with confidence thresholding). There is no comparison to other SSL methods (e.g., co-training, graph-based SSL, FixMatch-style approaches applied to tabular data) that could contextualize whether the chosen scheme is particularly effective. Since the paper does not propose a novel SSL algorithm, this comparison would be needed to support the claim that SSL "works" in this domain.

### Trivial

- Table formatting in the extracted text is difficult to parse (multiple rows with repeated checkmarks). This appears to be a parser artifact, but clearer presentation would help.
- The paper uses "prove" (abstract, line 13) in reference to empirical findings, which is too strong for correlational evidence from a single observational study.

## Nice-to-Haves

- A direct ablation comparing pseudo-labels filtered by SSU class (Simple/Separable only) vs. all confident predictions would directly test the quality principle.
- Reporting pseudo-label statistics (counts, class distribution, estimated accuracy on held-out simulated unlabeled data) would quantify the SSL behavior.
- Computational cost of the SSL phase (dataset size increase, training time) would help practitioners assess the practical trade-off.
- Precision-recall curves would be more informative than ROC-AUC for this highly imbalanced setting.

## Removed Points

*Harsh critic point about Section 2 overstating CoinJoin deanonymization difficulty:* The paper acknowledges later that many CoinJoin transactions are partially untangled (citing Larionov & Yanovich 2023-2024). The early framing is a minor presentational choice, not a substantive error.

*Harsh critic point about "12% illicit is less extreme than claimed":* The paper does not claim extreme imbalance in the labeled set; it says "high class imbalance" (Section 5.3), which is standard for fraud detection. This is not a misrepresentation.

*Harsh critic point about "pseudo-labeling scheme is standard":* This is true but not a weakness per se — the paper's contribution is in the feature engineering and dataset, not a novel SSL algorithm. Using a standard SSL method is appropriate for an applied paper testing whether quality features help.

*Strength Finder point about "causal evidence that feature quality drives SSL success":* The evidence shows correlation from feature ablation, not causation. The tables show that features improve supervised performance, and SSL with those features maintains similar performance. This conflates two observations. Downgraded to the feature ablation strength already listed.

*Strength Finder point about "quality-aware pseudo-labeling principle":* The principle is stated but not directly tested (see Major Weakness 4). The paper's SSL uses confidence thresholding, not explicit quality filtering of pseudo-labels. This claimed strength conflicts with a verified weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contributions honestly.** The dataset and the empirical finding that OTC features are harmful are the strongest contributions. De-emphasize the "SSL outperformance" narrative and instead present SSL as maintaining supervised-level performance while enabling slightly higher recall at the cost of precision — a trade-off that may be useful for forensic recall-oriented applications.

2. **Add variance reporting.** Report standard deviations or 95% confidence intervals across the 5 cross-validation folds for all metrics. This would clarify whether the small F1 differences (e.g., 0.844 vs 0.845) are within noise.

3. **Add at least one SOTA comparison.** Reimplementing a simple prior method (e.g., random forest on Elliptic-like features, or a basic GNN from the cited works) on the same dataset would provide an important baseline. Even reporting results on a common benchmark (Elliptic dataset) would contextualize the performance.

4. **Directly test the quality principle for pseudo-labels.** Add an experiment comparing (a) all confident pseudo-labels vs. (b) only pseudo-labels from SSU Simple/Separable transactions vs. (c) only pseudo-labels from KeyLinker-clustered addresses. This would turn the stated principle into an actionable, testable claim.

5. **Acknowledge the feature novelty situation.** Reframe Contribution 2 as "systematic application and evaluation of existing forensic features (KeyLinker, SSU) in a semi-supervised pipeline, with the novel finding that OTC features are detrimental."

## Score and Decision

Below is my calibration reasoning:

**Round 1 bracketing:** I queried for similar-topic papers in three bands:
- Weak band (<3.5): Ethereum anomaly detection papers at ~3.0 (TRW-GCN: 3.00)  
- Middle band (3.5–7.5): FE-GNN (4.25), BlockFound (5.75), Better Call Graphs (5.25), DIPS (5.00)
- Strong band (>7.5): SSL theory papers at ~8.0 (FixMatch analysis, etc.)

The paper clearly does not belong in the strong band (no theoretical contribution, no novel method). It sits in the middle band, but near the lower end due to overclaimed results and missing rigor.

**Round 2 narrowing (within 3.5–7.5):**
- **FE-GNN (4.25):** Blockchain account classification paper with similar issues: no error bars, missing SOTA baselines, incremental contribution. This paper has a more substantial dataset but similarly overclaims novelty. Slightly stronger than FE-GNN due to the dataset size and systematic ablation → anchor around 4–5.
- **Better Call Graphs (5.25):** Dataset paper for malware classification. This paper's dataset contribution is comparable in significance, but BCG was rejected as dataset-only being insufficient for ICLR. This paper has a larger gap between claims and evidence. → marginally weaker than BCG.
- **DIPS (5.00):** SSL pseudo-labeling quality paper with comprehensive evaluation across domains. This paper lacks similar rigor (no variance, no SSL baselines, no SOTA comparison). → weaker than DIPS.
- **BlockFound (5.75):** Blockchain foundation model with genuine architecture novelty and ablation studies. This paper has less methodological novelty. → notably weaker than BlockFound.

**Final placement:** The paper is comparable to FE-GNN (4.25) but with a stronger dataset contribution and more systematic feature ablation. However, the central claim mismatch (SSL "outperforming" when F1 is essentially unchanged) and the misrepresentation of feature novelty are significant flaws that prevent it from reaching the 5+ range. Score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>