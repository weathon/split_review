Now I have sufficient calibration context. Let me write the consolidated review.

**Bracket analysis:** Round 1 placed this paper well above the weak blockchain-anchors (2.0–3.33: papers with limited novelty, missing baselines, marginal improvements) and below the strong-anchor band (8.0: no topically relevant papers there). Round 2 narrowed within 3.5–7.5, with the battery dataset paper (4.00, accepted) as the closest topical analog — it too had opaque data generation, weak baselines, and overclaims, but the paper under review has more thorough experimentation (3 models × 7 feature sets × 4 metrics), compensating slightly. The AMLGentex paper (3.00, withdrawn) is weaker. Overall this paper sits around 4.5–5.5 territory. I anchor at **5.0**.

---

## Summary

This paper addresses illicit transaction detection in Bitcoin's Shared Send Mixer (CoinJoin) transactions. It contributes (1) a dataset of ~163M CoinJoin transactions with ~4.6M labeled, (2) novel forensic features (KeyLinker address clustering, SSU complexity metrics), and (3) a semi-supervised learning framework that selectively pseudo-labels unlabeled data based on feature quality. The core thesis is that *feature quality, not data quantity, drives performance*. The strongest empirical finding is that adding OTC heuristic features consistently degrades classifier performance, while high-fidelity features (REUSE, CS, SSU) produce the best results (XGBoost F1=0.845, ROC AUC=0.97). However, the SSL contribution is essentially unsupported — F1 improves by 0.001 over supervised baselines — and the paper claims more than its evidence warrants.

## Strengths

1. **Large-scale, first-of-its-kind CoinJoin transaction dataset.** The paper compiles 163.4M CoinJoin transactions with 4.6M labeled, spanning Bitcoin's full history up to block 882,421 (Table 1). This is orders of magnitude larger than prior datasets (e.g., Elliptic's ~200K transactions) and could be a valuable community resource if properly released and validated.

2. **Thorough multi-model, multi-metric feature ablation across 7 feature sets.** Tables 2 and 3 report precision, recall, F1, and ROC AUC for XGBoost, CatBoost, and Random Forest on every combination of DEFAULT, REUSE, CS, OTC, and SSU features using 5-fold cross-validation. This systematic ablation directly supports the paper's main claim about feature quality driving performance.

3. **Empirically demonstrated finding that OTC features are harmful.** The consistent pattern across all three models and both supervised/SSL settings — adding OTC features degrades F1 and ROC AUC — is a concrete, reproducible result. This is the paper's most defensible contribution and has practical value for practitioners building blockchain forensic tools.

4. **Clean formalization of the problem domain.** Section 4 provides a well-structured mathematical definition of the transaction classification task, UTXO representation, address tagging, and cluster propagation, providing a reproducible foundation for future work.

## Weaknesses

### Major

1. **The SSL contribution is not supported by the results.** The paper claims that "SSL effectively leverages unlabeled data" and "outperforms supervised baselines," yet the best supervised XGBoost (F1=0.845, Table 2) and best SSL XGBoost (F1=0.845, Table 3) are identical. Most model/feature combinations show flat or slightly worse SSL performance. The paper acknowledges no "dramatic metric gains" but continues to frame SSL as a successful contribution in the abstract ("A demonstration that SSL effectively leverages unlabeled data") and conclusion ("quality-aware semi-supervised learning successfully leverages Bitcoin's inherent pseudonymity to overcome label scarcity"). This overstates what the data shows. The experiment at best demonstrates that SSL does not *harm* performance when guided by good features — a useful but significantly weaker finding.

2. **Dataset labeling and CoinJoin identification are not validated.** The paper states labels come from WalletExplorer, Elliptic++, MBAL, and Kaggle with "manual resolution of duplicates and conflicting labels," but provides no criteria for how conflicts were resolved, no validation of label accuracy (e.g., held-out expert review, agreement rates across sources), and no description of how CoinJoin transactions were distinguished from ordinary transactions. For a contribution that is partly defined by its dataset, this is a significant gap that prevents assessment and reuse.

3. **No comparison to existing SSL methods or graph-based approaches.** The paper cites prior work achieving 92% accuracy with semi-supervised GNNs (Nerurkar 2022) but compares against no such method. The SSL component is limited to simple pseudo-labeling with tree-based classifiers. Without comparison to at least one alternative SSL approach (e.g., self-training with a different base model, label propagation, or a graph SSL baseline), the claim of an "SSL framework" as a contribution is unsubstantiated by the surrounding literature.

4. **Overclaiming in framing: "quality vs. quantity" is used in two different senses.** The paper's rhetorical thesis ("quality over quantity") shifts meaning between the abstract (where "quantity" = number of labeled examples) and the experiments (where "quantity" = feature count, specifically OTC features). The SSL experiment adds pseudo-labels (quantity of examples) but shows no benefit, so the central thesis is not tested in the way it is sold. The paper should clarify which notion of "quantity" it addresses and calibrate its claims accordingly.

### Minor

1. **KeyLinker is not isolated in the experiments.** The REUSE feature (presumably KeyLinker) is always combined with DEFAULT and often with CS. While comparing DEFAULT vs. DEFAULT+REUSE does show marginal improvement (F1 0.814→0.837 for XGBoost), the paper claims "KeyLinker outperforms OTC" without a direct comparison of REUSE-only vs. OTC-only vs. CS-only configurations. An ablation isolating each clustering heuristic would substantiate this claim.

2. **Pseudo-labeling details are missing.** Section 5.2 describes the "data quality principle" qualitatively, but no quantitative details are provided: how many pseudo-labels were selected per batch, what selection fractions were used, how the SSU class distribution of pseudo-labels compared to the labeled set, or what confidence thresholds were applied. These are standard reporting requirements for SSL papers.

3. **The 80/10/10 labeled-data split (3.7M training transactions) is not a label-scarce regime.** The paper motivates SSL by citing "scarcity of reliable labels," yet 3.7M labeled CoinJoin transactions is a substantial training set. The SSL framing would be better tested by showing improvement when labeled data is scarce (e.g., 1% or 5% of the labeled set), which is the realistic scenario that motivates SSL.

4. **No variance or significance reporting.** All results are point estimates without standard deviations despite 5-fold cross-validation. The differences between feature sets (e.g., 0.844 vs. 0.841 F1) may or may not be significant; without variance, the reader cannot assess this.

### Trivial

None.

## Nice-to-Haves

- Direct comparison of REUSE-only, CS-only, and OTC-only feature configurations to substantiate the KeyLinker quality claim.
- An experiment training on a small fraction of labeled data (e.g., 1-5%) and measuring SSL gains, to test the label-scarcity motivation.
- Documentation of dataset schema, license, and CoinJoin identification methodology in the release.
- A comparison to at least one alternative SSL baseline from the cited related work.

## Removed Points

The following points from the reviewers were removed after verification:

- **"Tables have duplicated rows"** — The duplicate check-mark patterns in Tables 2 and 3 are PDF extraction artifacts (checkmark columns misaligning during parsing). The original submission's formatting is not accessible, but there is no evidence of reporting errors beyond the parser. Removed per formatting-artifact rule.
- **"KeyLinker has no description of its mechanism, error rates, or computational cost"** — The paper cites Smolenkova & Yanovich (2025) for the KeyLinker mechanism. A full re-description is not required for a cited existing method; requesting error rates and computational costs is a nice-to-have, not a weakness. Downgraded to a minor note about the missing ablation.
- **Various nitpicks about undisclosed hyperparameters and trivial implementation details** — Removed per reproducibility nitpick rule.
- **"OTC as straw-man"** — While OTC's known failure modes are acknowledged in the literature, the paper's empirical demonstration that OTC features degrade ML classifier performance (across 3 models) is still a valid, non-obvious contribution. This criticism conflates "OTC has known failure modes" with "adding OTC as an ML feature predictably harms performance," which are different claims.

## Novel Insights

None beyond the paper's own contributions. The observation that feature quality (REUSE + SSU) dominates feature quantity (OTC) in SSL for blockchain forensics is the paper's core insight, but it is mainly validated by the feature ablation rather than the SSL component.

## Suggestions

1. **Re-title and reframe the paper around feature engineering, not SSL.** The most defensible contribution is the feature ablation showing that high-quality features (KeyLinker, SSU) outperform noisier ones (OTC). Drop or significantly downplay the "SSL framework" claim unless new experiments demonstrate a meaningful improvement over supervised baselines in a genuinely label-scarce regime.

2. **Document the dataset properly.** Add a clear description of CoinJoin transaction identification criteria, label conflict resolution rules, and a validation of label accuracy (e.g., random-sample audit, cross-source agreement rates).

3. **Add a direct ablation isolating each clustering heuristic.** Compare REUSE-only, CS-only, OTC-only, and their combinations to directly support the claim that KeyLinker provides higher-fidelity signals than OTC.

4. **Report standard deviations** for all metrics across cross-validation folds so the reader can assess whether performance differences between feature sets are significant.

## Score and Decision

**Initial bracket (Round 1):** The paper is clearly above weak blockchain-forensic anchors scoring 2.0–3.33 (which had missing baselines, limited novelty, marginal improvements) and below the strong-anchor band (8.0+), placing it in the 3.5–7.5 range.

**Narrowing (Round 2):** Compared to the battery dataset paper (avg 4.00, accepted) — which also had opaque data generation and validation gaps — this paper has more thorough experimentation (3 models × 7 feature sets) and a more interesting empirical finding (OTC harms performance). It is comparable in quality to the AMLGentex paper (avg 3.00, withdrawn). The paper sits around 4.5–5.5; I anchor at **5.0**.

**Final calibration anchors consulted:**
- `jOZCfCvH4c` (2.00, withdrawn) — Ethereum DeFi SSL detection; weaker experiments, no significant improvement over baselines. Our paper is stronger.
- `Wj0qUfH7b3` (2.67, reject) — Bitcoin address clustering with GNN; missing SOTA baselines, limited validation. Our paper is stronger.
- `KRUNuLzQD1` (3.00, withdrawn) — AML synthetic data generator; opaque validation, limited novelty. Our paper is comparable or slightly stronger.
- `jSM71b1JsV` (4.00, accepted) — Battery fault dataset; opaque generation, weak baselines, but accepted as poster. Our paper is comparable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>