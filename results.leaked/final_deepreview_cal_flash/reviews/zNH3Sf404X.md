Now I have all the information needed to write the final consolidated review. Let me produce the review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes a semi-supervised learning framework for detecting illicit CoinJoin transactions in Bitcoin, emphasizing feature quality over data quantity. It introduces a large-scale dataset of 163M CoinJoin transactions, adopts KeyLinker address clustering and SSU complexity metrics as features, and shows through systematic ablation across three gradient-boosted models that (a) key-reuse and SSU features improve detection, (b) the common OTC heuristic degrades performance, and (c) these patterns hold in both supervised and semi-supervised settings.

## Strengths

**S1. Systematic ablation demonstrating that OTC features consistently degrade performance across models and settings.** Tables 2 and 3 show that adding OTC features to any feature set lowers F1 and ROC AUC for all three models in both supervised and semi-supervised experiments (e.g., XGBoost F1 drops from 0.845 to 0.836 when OTC is added). This is the paper's strongest empirical finding and provides concrete evidence for the "quality over quantity" thesis.

**S2. KeyLinker and SSU complexity features measurably improve classification.** Table 2 shows that adding REUSE (key-reuse features) and CS (Common Spending) raises supervised XGBoost F1 from 0.814 to 0.844, and SSU categories further improve robustness. These features capture mixing-relevant structure that standard heuristics miss.

**S3. Thorough ablation across three models and seven feature-set combinations in both supervised and SSL settings.** Every combination of {DEFAULT, REUSE, CS, OTC, SSU} is evaluated on XGBoost, CatBoost, and Random Forest, and the same 21 conditions are repeated under SSL. This systematic design gives confidence that the observed effects are not model-specific.

**S4. Large-scale dataset covering Bitcoin's full history up to February 2025.** The dataset spans 1.15B total transactions, 163M CoinJoin transactions, and 4.6M labeled instances with per-transaction SSU complexity classification. If properly constructed, this would be a valuable resource for the community.

**S5. Actionable insight on the precision-recall trade-off when deploying SSL for blockchain forensics.** The paper explicitly reports that pseudo-labeling increases recall by up to +0.03 at a precision cost of –0.04 to –0.05, and argues this trade-off is acceptable for forensic use — practical guidance absent from most SSL papers.

## Weaknesses

### Major

**W1. The method for identifying CoinJoin transactions is not specified, and the available evidence suggests a potentially invalid definition.** The paper claims 163.4M CoinJoin transactions but never explains how they were identified. The SSU complexity sub-categories sum to essentially the same number (99.1+24.2+10.5+5.4+24.3 = 163.5M), which is suspiciously close to the CoinJoin count. The SSU category includes "Regular" (24.3M) transactions with fewer than two inputs or outputs — transactions that are definitionally not CoinJoins by any standard definition (single-party payments or straightforward sends). If the paper is equating "has an SSU classification" with "is a CoinJoin," then the dataset conflates ordinary multi-input transactions (exchange consolidations, wallet reorganizations, simple payment+change transactions) with actual CoinJoin mix transactions. This would invalidate the core dataset contribution and call all downstream experimental results into question. Even if a proper identification method exists (e.g., inherited from the SSU framework of Larionov & Yanovich 2023), the paper must describe it; the current omission is a fundamental reproducibility and validity gap. (Verifiable: Table 1 row sums; §5.1 data collection description; §2.3 SSU description.)

**W2. No comparisons to prior detection methods.** The related work (§3) surveys many ML approaches for detecting illicit transactions and mixing services (Rathore et al. 2022, Alarab et al. 2020, Nerurkar 2022, etc.), several reporting >90% accuracy. Yet the experiments (§6) compare only three gradient-boosting models across different feature sets. No baseline from prior work is implemented on the same data. The reader consequently cannot judge whether the proposed features or the SSL framework improve upon the state of the art. For a paper that claims to advance coinjoin forensics, this omission fundamentally limits the significance of the reported results. (Verifiable: §3 discussion of prior work; §6.2–6.3 experiment descriptions — no external baselines appear.)

**W3. The central claim about quality-aware pseudo-labeling is not directly tested.** The paper argues that SSL succeeds "precisely when guided by these quality-focused features" and that pseudo-label quality matters. However, the SSL experiments only compare final model performance after selective pseudo-labeling; they never compare against a standard pseudo-labeling baseline that uses a simple confidence threshold without quality-based filtering. The observed pattern — that the best feature set in supervised learning is also best in SSL, and that adding OTC harms both — could simply reflect feature quality in the base model rather than any quality-aware pseudo-labeling mechanism. A direct comparison between (a) selective pseudo-labeling using only simple/separable SSU classes, (b) retaining all confident predictions regardless of SSU class, and (c) standard confidence-threshold pseudo-labeling is needed to support the claimed mechanism. (Verifiable: §5.2 data quality principle; §6.3 SSL results — no standard SSL baseline included.)

**W4. Overclaimed novelty of features.** The abstract and introduction repeatedly describe KeyLinker and SSU metrics as "novel" features "introduced" by this paper. However, §5.1 and §2.3 explicitly cite Smolenkova & Yanovich (2025) for KeyLinker and Larionov & Yanovich (2023) for SSU. No adaptation, enhancement, or original algorithmic modification to either technique is described. The paper is frank about these citations in the body text, which makes the "novel" framing in the abstract and introduction inconsistent with what the paper actually presents. This inflates the perceived contribution. (Verifiable: Abstract lines; §1 Contribution 2; §5.1 attribution to prior work.)

**W5. No variance or confidence intervals reported.** Despite evaluating on a large dataset (4.6M labeled transactions) with 5-fold cross-validation, all results in Tables 2 and 3 are reported as point estimates without standard deviations, confidence intervals, or any measure of statistical significance. Given the scale of the dataset, even tiny metric differences may be reliable, but the paper offers no way to assess whether the observed gaps (e.g., F1 of 0.844 vs. 0.841) are meaningful. (Verifiable: Tables 2, 3 — single numbers per cell.)

### Minor

**W6. The pseudo-labeling procedure is underspecified.** The paper states that "the top fraction of samples on both sides of the decision boundary" is selected, but does not report how many pseudo-labels were added per iteration, how the positive-negative ratio was adjusted, how many iterations were run, or how the threshold was chosen across feature sets. This makes the SSL results difficult to reproduce or assess. (Verifiable: §5.3 pseudo-labeling description; §6.3 — no numerical details.)

**W7. The "label scarcity" framing is inconsistent with the 4.6M labeled transaction count.** The paper motivates SSL by appealing to label scarcity, yet trains on 4.6 million labeled CoinJoin transactions — a number that is large in absolute terms even if it represents only ~2.8% of the CoinJoin pool. This is not a fatal issue but weakens the motivating narrative. (Verifiable: Introduction §1; Table 1; §5.3 training set size.)

### Trivial

**W8. Table 2 contains formatting anomalies** — some feature-set columns have checkmarks for SSU in unexpected positions, and certain rows have duplicate entries (e.g., two identical rows for the same feature combination in the SSL table).

## Nice-to-Haves
- Add at least one prior-method baseline (e.g., a model using features from Rathore et al. 2022) to ground the reported improvements in the broader literature.
- Validate pseudo-label quality by having a human (or trusted oracle) label a random sample of pseudo-labeled transactions from each feature-set condition and report accuracy.
- Include a standard confidence-threshold pseudo-labeling baseline (without quality filtering) to isolate the effect of the proposed quality-aware selection.
- Report standard deviations or 95% CIs for all metrics, especially given the large dataset.
- Discuss how the results would transfer to entity-level or flow-level forensic analysis (the current evaluation is transaction-level).

## Removed Points

The following points from the inputs were considered and removed per the filtering rules:

- **Harsh critic point about dataset not yet released**: Removed per hard rules — questioning availability/release status of cited resources is not permitted.
- **Harsh critic claim that SSL gains "could simply reflect feature quality in the base model" as a fatal weakness**: Demoted to Major (W3). This is a legitimate concern but the paper does provide some evidence (correlation between feature quality and SSL performance); the issue is that the paper's specific claim about quality-aware pseudo-labeling is not directly tested, rather than that the overall thesis is unsupported.
- **Harsh critic point about tag propagation rule and label conflicts**: This is a valid technical detail but is a minor implementation concern common to any address-clustering-based approach; not central to the paper's claims.
- **Strength Finder's claim about "novel high-fidelity features"**: Removed because the features are from prior work, contradicting the "novel" framing. The useful finding that these features improve classification is kept in Strengths S2.
- **Strength Finder's claim about "first complete historical dataset"**: Demoted to S4 with the caveat about dataset construction, because the identification methodology is unclear.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension between the paper's strong empirical finding (OTC harms performance; KeyLinker/SSU helps; these patterns are consistent across models and settings) and the significant methodological gaps that undermine confidence in the results (unclear CoinJoin identification, missing baselines, untested pseudo-labeling mechanism). No genuinely novel analytical insight emerges from the reviews that the paper itself does not already offer.

## Suggestions

1. **Clarify the CoinJoin identification methodology.** Provide a precise, replicable definition of how transactions are classified as CoinJoin (e.g., equal-output denominations, coordination-round markers, or a citation to a specific detection algorithm). If the SSU framework itself is used for detection, state this explicitly. If all SSU-classified transactions are counted as CoinJoin, the paper must justify this equivalence — and explain how "Regular" (SSU_5) transactions qualify.
2. **Add external baselines.** Implement at least one representative method from the surveyed related work (e.g., Rathore et al. 2022's 8-feature decision tree, or a simple GNN) and compare on the same train/test splits.
3. **Add a standard SSL baseline.** Compare selective quality-aware pseudo-labeling against simple confidence-threshold pseudo-labeling (without SSU-based filtering) to directly test the central hypothesis.
4. **Report variance.** Add standard deviations or confidence intervals to all tables.
5. **Correct the novelty framing.** Replace "novel features" with "adopted features from prior work" or "features based on existing techniques" throughout the abstract and introduction.

## Score and Decision

**Round 1 bracketing:** I queried for anchors with avg scores <3.5, 3.5–7.5, and >7.5 on topics similar to this paper (blockchain forensics, SSL, feature engineering). The weak-band anchors (avg ~2.5–3.0) were clearly weaker papers with less empirical content. The strong-band anchors (avg 8.0) were theoretical SSL papers at a different quality tier. This placed the plausible bracket between 3.5 and 5.5.

**Round 2 narrowing:** I queried for anchors in the 3.5–6.0 and 3.0–5.5 ranges on more specific topics. The best comparators were:
- *FE-GNN* (yM7rw8Bo1f, avg 4.25, Reject) — similar scope (blockchain address classification with feature engineering + GNNs), similar issues (incremental novelty, missing baselines, no error bars). Our paper has more thorough feature ablation but shares the same structural weaknesses.
- *BlockFound* (LPXfOxe0zF, avg 5.75, Reject) — stronger evaluation framework despite ambiguous anomaly definition. Our paper has less methodological novelty.
- *DIPS* (eSO9quCgmz, avg 5.00, Reject) — SSL data-quality paper with similar thematic goals but stronger experimental validation.
- *BCG* (nwjgeFGbAF, avg 5.25, Reject) — dataset paper with mixed reviews; similar tension between dataset contribution and methodological novelty.

Our paper is stronger than the 3.0–4.0 anchors (more data, systematic ablation) but weaker than the 5.0+ anchors (missing baselines, opaque dataset construction, no direct test of the core SSL hypothesis). The unresolved CoinJoin identification issue (W1) is the most serious problem and prevents the paper from reaching the 5+ tier.

**Final score: 4.0.** This paper has real empirical content (systematic feature ablation, consistent OTC degradation) and addresses a timely problem. However, the unclear dataset construction (W1), missing prior-method baselines (W2), untested pseudo-labeling mechanism (W3), and overclaimed novelty (W4) collectively prevent it from meeting the bar for publication in its current form.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>