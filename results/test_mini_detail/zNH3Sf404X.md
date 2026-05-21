Now I have a solid understanding of the paper and the calibration landscape. Let me write the final consolidated review.

## Summary

This paper introduces a large-scale dataset of 163M Bitcoin CoinJoin transactions (4.6M labeled), applies existing address clustering techniques (KeyLinker, CS, OTC) and SSU complexity metrics as features, and evaluates supervised and semi-supervised classifiers (XGBoost, CatBoost, Random Forest) for illicit transaction detection. The core thesis is that SSL success depends on feature quality rather than pseudo-label volume.

## Strengths

- **Large-scale CoinJoin dataset.** The paper assembles the first comprehensive historical dataset of 163.4M CoinJoin transactions with SSU complexity classification (Table 1), integrating on-chain data with multiple off-chain label sources (WalletExplorer, Elliptic++, MBAL, Kaggle). The 4.6M labeled CoinJoin transactions substantially exceed the scale of prior labeled Bitcoin datasets focused on mixed transactions. This is a genuine resource for the community.

- **Empirical finding that OTC features degrade performance.** The paper consistently shows across both supervised and SSL settings that adding the OTC heuristic reduces F1-score (e.g., Table 2: XGBoost F1 drops from 0.844 to 0.841 when OTC is added; Table 3: drops from 0.845 to 0.836). This is a concrete, reproducible finding that challenges the common practice of including all available heuristics, and it is the strongest empirical result in the paper.

- **Thorough evaluation across multiple models and feature configurations.** The paper evaluates XGBoost, CatBoost, and Random Forest across 42 feature-set configurations with stratified 5-fold cross-validation and hyperparameter tuning (Section 6.2). The finding that XGBoost with DEFAULT+REUSE+CS+SSU is the best configuration is consistent across both supervised and SSL settings, supporting the claim that the feature set drives performance.

## Weaknesses

### Fatal
None.

### Major

- **The central claim that SSL "outperforms" supervised baselines is not supported.** The paper repeatedly states that SSL outperforms supervised learning by leveraging unlabeled data. However, comparing Tables 2 and 3, the best supervised F1 (XGBoost, 0.844) and the best SSL F1 (XGBoost, 0.845) are effectively identical. The same feature set (DEFAULT+REUSE+CS+SSU) yields the top result in both settings. The paper's own text acknowledges this (Section 6.3: "performance remained stable across models," "pseudo-labeling slightly increased recall...but at the cost of introducing additional false positives"), yet the abstract and introduction claim SSL "outperforms supervised baselines." This is a significant disconnect between the paper's framing and its evidence. The SSL experiment does not demonstrate meaningful improvement, and the paper's narrative would be more honest if it reframed the contribution around the dataset and feature analysis rather than an SSL breakthrough.

- **The "data quality principle" for pseudo-labeling is asserted but never tested.** Section 5.2 describes a principle that pseudo-labels should be selected based on transaction structural quality (SSU class) and clustering heuristic quality (KeyLinker vs. OTC). However, the paper provides no ablation that varies the selection strategy. There is no comparison against (a) using all available pseudo-labels, (b) random selection, or (c) selection based solely on confidence thresholds (the standard approach). The actual implementation described ("select the top fraction of samples on both sides of the decision boundary") is a standard confidence-based technique, not a quality-aware one. Without a controlled experiment, the paper cannot attribute any result to quality-aware selection, and the principle remains an untested hypothesis.

### Minor

- **Feature novelty is overstated.** KeyLinker address clustering is directly adopted from Smolenkova & Yanovich (2025), and SSU complexity metrics are adopted from Larionov & Yanovich (2023). The paper cites these works but frames the features as "novel, high-fidelity features" (Abstract) and "novel forensic features" (Section 1). The contribution lies in applying these features in a new context (SSL for CoinJoin detection), which is legitimate, but the framing as introducing novel features is misleading. The paper would benefit from more precise language.

- **Tables 2 and 3 contain duplicated rows with the same feature checkmarks but different metrics.** For example, CatBoost with all features (DEFAULT+REUSE+CS+OTC+SSU) appears three times in Table 2 with F1 scores of 0.800, 0.830, and 0.827. Similarly, XGBoost with all features appears three times with F1 scores of 0.821, 0.842, and 0.840. The paper does not explain what differs between these rows (e.g., different hyperparameter settings, different random seeds, or different validation folds). This undermines confidence in the data pipeline and makes it impossible to interpret which result is the intended one.

- **No comparison against standard SSL baselines.** The paper compares pseudo-labeling only to supervised versions of the same models. Standard SSL methods (self-training, co-training, mean teacher, or graph-based SSL on transaction graphs) are not evaluated. Without these, the reader cannot judge whether the proposed method is competitive with alternatives or merely adequate.

- **No statistical significance testing.** Differences between models and feature sets are reported to three decimal places, but there is no error bar, confidence interval, or significance test. Given the small F1 differences (e.g., 0.844 vs 0.842), it is impossible to know whether they reflect real effects or noise.

### Trivial

- The paper claims "XGBoost achieves the best supervised performance with an F1-score of 0.845" (line 254), but Table 2 shows 0.844 for the best configuration. This is a minor inconsistency.

## Nice-to-Haves

- An ablation of the pseudo-label selection strategy (comparing quality-filtered vs. all pseudo-labels vs. random selection) would directly test the paper's central hypothesis and could turn a weakness into a strength.
- Ablating KeyLinker/REUSE against a baseline that includes only CS and OTC (without REUSE) would clarify whether KeyLinker adds independent value beyond the combination of CS and SSU.
- An analysis of pseudo-label correctness (what fraction of selected pseudo-labels are actually correct?) would strengthen the quality claim.
- A brief description of how KeyLinker and SSU features were computed at scale (163M transactions) would aid reproducibility.

## Removed Points

- **"SSL is needed because supervised methods suffer from label scarcity" contradiction**: The harsh critic claims this is contradicted by the fact that supervised models achieve good performance with 4.6M labeled transactions. However, 4.6M labeled out of 163M total is indeed label-scarce (2.8%), and the paper's argument is about the difficulty of labeling more, not about supervised performance being bad. Weakened: the critic's framing is too strict; the label scarcity argument is still valid even if supervised models perform decently on the available labels.

- **"Dataset claims are ambiguous"**: The critic claims that calling the dataset "complete" and "with SSM classification" is ambiguous. The paper clearly states that SSM classification refers to SSU complexity classes (which are computed for all CoinJoin transactions), not just the labeled subset. The dataset description in Table 1 is clear about what is labeled vs. unlabeled. Removed: the paper is sufficiently clear on this point.

- **"No analysis of pseudo-label correctness"**: The critic notes the paper doesn't report human evaluation of pseudo-labels. This is a reasonable point but belongs in nice-to-have; it's not a core weakness since the experiment compares SSL to supervised baselines, not to ground truth.

- **"Missing description of KeyLinker and SSU computation"**: The critic notes this would aid reproducibility. However, the paper cites the prior works that describe these methods, which is standard practice. Removed as a minor reproducibility nitpick.

- **Strength Finder point 3 about "KeyLinker clustering as a cryptographic-proof-based alternative"**: The strength is real but the framing as "cryptographic-proof-based" is a bit grandiose — KeyLinker is based on public key reuse, which is a heuristic (albeit a strong one). Kept in spirit but softened.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the central tension: the paper's strongest assets (dataset, feature ablation showing OTC harms performance) are at odds with its framing (SSL quality principle). The most interesting observation emerging from the reviews is that the OTC degradation finding is the paper's most robust and surprising result, yet it is somewhat buried in the SSL narrative.

## Suggestions

1. **Reframe the paper's contribution.** The dataset and the feature analysis (particularly the finding that OTC degrades performance while KeyLinker/REUSE helps) are the paper's strongest contributions. Consider repositioning away from the "SSL outperforms supervised" narrative toward "a dataset and feature engineering benchmark for CoinJoin detection." The SSL component can be presented as a secondary exploration rather than the headline result.

2. **Either test the quality principle or drop it.** If the paper wants to claim that quality-aware pseudo-label selection matters, it must provide an ablation. If the authors cannot run this experiment, the principle should be removed from the claims and presented as a hypothesis for future work.

3. **Clean up the tables.** The duplicated rows in Tables 2 and 3 need to be explained or removed. If the different rows correspond to different hyperparameter settings or fold results, this should be made explicit.

4. **Add statistical significance measures.** Even simple standard deviations across cross-validation folds would help the reader assess whether the reported F1 differences (e.g., 0.844 vs 0.842) are meaningful.

## Score and Decision

Based on calibration against the reviewed corpus, I place this paper at **4.0**. 

**Bracket rationale (Round 1):** The paper is clearly above the weak-anchor band (avg < 3.5) — papers like the QUIC dataset (3.5) and the Ethereum GCN paper (4.0) represent the lower bound of passable work with some contribution. It is clearly below the strong-anchor band (avg > 7.5) — papers like the SSL evaluation framework (8.0) have rigorous methodology and well-supported claims. The initial bracket was [3.5, 5.5].

**Narrowing (Round 2):** Comparing against the Ethereum GCN paper (4.0 avg, rejected), the Bitcoin paper has a larger dataset, more thorough feature analysis, and stronger empirical grounding. However, it shares similar issues with overclaimed contributions and untested hypotheses. Comparing against the ICFI paper (5.0 avg, rejected), the Bitcoin paper has a less coherent central claim but a more substantial empirical contribution (dataset + feature analysis). The paper is closer to the Ethereum GCN paper in overall quality because the central claim mismatch is a significant flaw that undermines the narrative.

**Final score: 4.0** — marginally below the acceptance threshold. The paper has genuine value in its dataset and feature engineering insights, but the disconnect between the claimed SSL contribution and the actual results, combined with the untested "quality principle," prevents it from meeting the bar for acceptance. A revised version that reframes the contribution and tests the quality principle could be publishable.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>