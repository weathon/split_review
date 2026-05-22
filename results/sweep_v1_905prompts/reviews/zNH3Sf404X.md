Now let me write the consolidated review.

## Summary

This paper tackles the problem of detecting illicit Bitcoin flows in CoinJoin (Shared Send Mixer) transactions. It makes three claimed contributions: (1) the first complete historical dataset of ~163M CoinJoin transactions with SSM classification; (2) application of KeyLinker address clustering and SSU complexity metrics as features; and (3) a semi-supervised learning framework showing that SSL success depends on feature quality rather than pseudo-label volume. The core empirical finding is a clean feature-ablation result: adding OTC (One-Time Change) heuristic features consistently degrades performance across Random Forest, XGBoost, and CatBoost, while the `Default+REUSE+CS+SSU` feature set yields the best results.

## Strengths

- **Large-scale, carefully constructed dataset of CoinJoin transactions.** The paper assembles a dataset of 163.4M CoinJoin transactions (4.6M labeled) with SSU complexity breakdowns, spanning Bitcoin's full history up to block 882,421 (Table 1). This is a substantial resource for the blockchain forensics community, and its planned release is valuable.

- **Clean empirical demonstration that OTC features harm performance.** Across all three model families (XGBoost, CatBoost, Random Forest) and both supervised and SSL settings, Tables 2 and 3 consistently show that adding OTC features reduces precision, recall, and F1-score. This is the paper's strongest and most reproducible result — it gives practitioners a clear, actionable guideline.

- **Thorough feature ablation across multiple models and configurations.** The paper evaluates 7 feature configurations per model (21 total), with metrics including precision, recall, F1, and ROC AUC. The breadth of this evaluation provides a solid empirical foundation for the feature quality claim.

## Weaknesses

### Major

1. **Central claim about SSL is unsupported by the evidence.** The paper's abstract and introduction claim that "SSL effectively leverages unlabeled data" and that "a semi-supervised learning framework outperforms supervised baselines." However, the best supervised F1 is 0.844 (XGBoost, Default+REUSE+CS, Table 2) while the best SSL F1 is 0.845 (XGBoost, Default+REUSE+CS+SSU, Table 3) — an improvement of 0.001, which is effectively flat. The paper candidly acknowledges this ("The semi-supervised phase did not produce dramatic metric gains," Section 6.3) yet still frames SSL as a core contribution in the title, abstract, and conclusion. This creates a significant mismatch between claims and evidence. The feature-quality story is well-supported by the *supervised* ablation; the SSL framing adds no empirical weight and actively misrepresents what the data shows.

2. **Unexplained duplicate rows in Tables 2 and 3.** Both tables contain multiple rows with identical feature-set checkmarks but different metric values, with no explanation of what these rows represent. For example, in Table 2, CatBoost rows 5-7 and XGBoost rows 5-7 all show identical checkmarks (Default+REUSE+CS+OTC+SSU) yet report substantially different F1-scores (e.g., row 5: 0.800, row 6: 0.830, row 7: 0.827 for CatBoost). If these are different hyperparameter configurations, different random seeds, or different pseudo-label fractions, the paper must say so. In their current form, these rows erode trust in the reported metrics and make the tables effectively uninterpretable.

3. **Inconsistency between text and tables.** The paper states (Section 6.2) that "XGBoost achieves the best supervised performance with an F1-score of 0.845 (default+reuse+cs+ssu)." Table 2, however, shows the XGBoost Default+REUSE+CS row at F1=0.844 and the Default+REUSE+CS+SSU row at F1=0.842 — neither matches the text's claim. This suggests either the text or the table is wrong, and the inconsistency is not acknowledged.

4. **No variance or significance reporting.** All metrics are reported as point estimates without standard deviations, confidence intervals, or any measure of variability. Given that many F1 differences between configurations are 0.01–0.02, it is impossible to tell whether these differences are meaningful or noise. Stratified 5-fold CV is mentioned but no fold-level results are provided. This is a basic expectation for experimental reporting and its absence undermines the quantitative claims.

5. **The "quality vs. quantity" framing is not directly tested.** The paper contrasts smarter feature engineering (quality) with larger datasets (quantity), but the experiments never vary dataset size. They vary feature sets and compare SSL (adding pseudo-labels) to supervised. The "quantity" axis is tested only indirectly through the observation that adding OTC features increases pseudo-label count but harms performance. A direct test — e.g., training on random subsets of labeled data to see whether more data helps or harms with different feature sets — would substantially strengthen the claim.

### Minor

- **Insufficient specification of dataset construction.** The paper states that 163M CoinJoin transactions were extracted from 1.15B total transactions and classified via SSU, but provides minimal detail on how CoinJoin transactions were identified in the first place (e.g., via specific heuristics, the SSU untangling algorithm itself, or known mixer addresses). The label propagation pipeline ("Tags propagate through clustering relationships") is described at a high level without specifics on conflict resolution beyond "manually resolved duplicates and conflicting labels." This limits reproducibility.

- **KeyLinker and SSU metrics are attributed to prior work but claimed as novel contributions.** Contribution 2 says "Novel Forensic Features," then immediately cites KeyLinker to Smolenkova & Yanovich (2025) and SSU metrics to Larionov & Yanovich (2023). The features are not novel to this paper; their application in the SSL context may be, but this is not clearly distinguished. The paper would benefit from precise language about what is newly proposed vs. adapted from prior work.

- **Pseudo-labeling procedure lacks implementation details.** The paper mentions selecting "the top fraction of samples on both sides of the decision boundary" but does not report the actual fraction, the resulting number of pseudo-labels added, or any sensitivity analysis around this threshold. This makes the SSL experiments difficult to reproduce or compare against.

- **No comparison to prior CoinJoin detection methods.** The paper cites Rathore et al. (2022) reporting 97% accuracy for mixing service detection with decision trees, but does not compare its own results to any existing method, even approximately. Even acknowledging different evaluation setups, a discussion would help calibrate the contribution.

### Trivial/Removed

Most style/formatting nits, missing appendix references, and concerns about the existence of cited datasets are parser artifacts and are not included here (see Removed Points).

## Nice-to-Haves

- An ablation on pseudo-label selection thresholds (what fraction is optimal? how does it interact with feature quality?) would directly support the "data quality principle."
- Precision-recall curves or confusion matrices would help the reader assess the precision-recall trade-off the authors describe as "acceptable."
- Varying the amount of labeled data (e.g., training on 25%, 50%, 75% of labels) would directly test the quality-vs-quantity thesis rather than relying on the indirect SSL comparison.

## Removed Points

- Concerns about whether the dataset "cannot be independently verified" or the release status of cited references: removed per hard rules — cited entities are assumed to exist.
- Claims about missing related work: removed per hard rules — I cannot verify the existence of missing citations.
- Typographical and formatting nitpicks: removed — these are parser artifacts.
- The critic's concern that "this conflates two different notions of quantity" (pseudo-labels vs. labeled data): partially valid but weakened — the paper's framing does test one meaningful interpretation of "quantity" (pseudo-labeled data volume), even if a more direct test would be stronger.
- Strength Finder's generic strengths ("this paper addressed an important problem," "systematic benchmarking... provides a reliable baseline"): removed — generic/superficial without specific evidence.

## Novel Insights

None beyond the paper's own contributions. The finding that OTC features consistently degrade performance across multiple models is the most striking and practically useful result, but the paper's own analysis captures this adequately.

## Suggestions

1. **Reframe the paper around the feature engineering contribution.** Drop the SSL-centric narrative or substantially temper the claims. The dataset and the OTC-degradation finding are strong enough to stand on their own. A more honest title would be something like "Feature Quality Matters More Than Data Volume: Detecting Illicit Bitcoin Flows with High-Fidelity Features."

2. **Fix the tables.** Explain what the duplicate rows represent (different hyperparameters? random seeds?). Add variance reporting (standard deviations across CV folds). Reconcile the text claims (F1=0.845) with the table values (F1=0.842/0.844).

3. **Add implementation details:** CoinJoin identification criteria, pseudo-label fraction used, number of pseudo-labels added per iteration, and label conflict resolution protocol.

4. **Either improve the SSL results** (with statistical testing to show meaningful improvement) or honestly present them as "SSL performed comparably to supervised, confirming that feature quality — not pseudo-label volume — drives performance" without claiming SSL "outperforms."

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak anchors (<3.5): `q7Xi4yZYcH` (3.0, Bitcoin anomaly detection), `ctzGqxE3O0` (2.5, malware detection), `51cjeYcXjs` (2.5, malware analysis), `HYsU5X4kE5` (3.0, graph feature transformation)
- Middle anchors (3.5–7.5): `X8RTdxzqJQ` (4.8, SSL two-sample testing), `dpnPOXoqVQ` (4.75, SSL additive model), `DgRdeJF0k7` (5.25, SSL time-series), `yM7rw8Bo1f` (4.25, FE-GNN Ethereum classification)
- Strong anchors (>7.5): `tc90LV0yRL` (8.67, cybersecurity benchmark), `EUSkm2sVJ6` (7.6, data usage inference), `z8sxoCYgmd` (8.0, synthetic data detection), `WyEdX2R4er` (8.0, VLM understanding)

**Round 2 (Narrowing, read in full):**
- `yM7rw8Bo1f` (4.25, FE-GNN) — blockchain address classification with GNN, similar domain. The paper under review has a larger dataset and more thorough ablation, but comparably overclaims (GNN as "novel" when it's standard). **The current paper is slightly stronger** due to cleaner empirical findings and broader evaluation.
- `LPXfOxe0zF` (5.75, BlockFound) — blockchain foundation model, rejected despite decent scores. Had genuine technical novelty (custom tokenizer, MLM pretraining) but limited anomaly data (28 malicious txs). **The current paper is weaker** — less technical sophistication, and its core claim is contradicted by its own results.
- `juE0rWGCJW` (6.33, EX-Graph) — dataset paper, accepted. Dataset was available at submission. **The current paper is weaker** — no dataset availability at submission, and the overclaimed SSL narrative detracts from the dataset contribution.

**Bracket:** Round 1 placed the paper between 4.0 and 5.75. Round 2 reading confirms it is stronger than FE-GNN (4.25) but noticeably weaker than BlockFound (5.75) because the latter had actual technical novelty and honest presentation, while this paper overclaims its central result. Score is anchored toward the lower end of the bracket.

**Final Score:** 4.5/10

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>