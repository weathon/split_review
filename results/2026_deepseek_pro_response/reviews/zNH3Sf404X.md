Now I have a clear picture from calibration. Let me finalize the review.

**Calibration comparison:**
- Our paper is clearly above 3.00 (TRW-GCN — weak paper with vague theorems) and above 4.25 (FE-GNN — incremental GNN, missing baselines).
- Our paper is comparable to BlockFound (5.75) — both blockchain anomaly detection with some novelty but significant weaknesses. BlockFound had better methodological novelty but terrible data (28 malicious samples). Our paper has stronger data but weaker methodology and no external baselines.
- Our paper is a bit stronger than Better Call Graphs (5.25) — a pure dataset paper criticized as "engineering effort." Our paper has more going on (feature ablation, SSL).
- Our paper is clearly below EX-Graph (6.33) — genuinely novel dataset with thorough experiments and accept decision.
- Our paper is far below the 8.00 anchors (strong theoretical SSL contributions).

**Final score: 5.5, Reject.** The dataset contribution and systematic ablation are real strengths, but the core SSL claim is unsupported (0.001 F1 gain), there are no external baselines, and the novelty is overstated. For ICLR, the bar requires stronger evidence for methodological claims.

---

## Summary
This paper presents a large-scale dataset of 163M CoinJoin transactions with multi-source labels and applies semi-supervised learning (SSL) with engineered features (KeyLinker address clustering, SSU complexity metrics) for illicit Bitcoin transaction detection. The central claim is that feature quality matters more than data quantity: high-fidelity features like KeyLinker improve detection while noisy heuristics like OTC degrade it, and SSL amplifies this divergence.

## Strengths
- **Large-scale, well-documented dataset (Table 1, Section 5.1):** 163M CoinJoin transactions spanning Bitcoin's entire history up to block 882,421, with labels integrated from WalletExplorer, Elliptic++, MBAL, and Kaggle. Label conflicts are manually resolved. This is a genuine infrastructure contribution to blockchain forensics research.
- **Systematic feature ablation across models and learning paradigms (Tables 2-3):** The paper evaluates 7-8 feature combinations across XGBoost, CatBoost, and RandomForest in both supervised and SSL settings. The consistent pattern — REUSE and CS features improve F1 while OTC degrades it — provides credible evidence that address-clustering heuristic quality matters for detection. This pattern holds across all three model families.
- **Honest acknowledgment of SSL limitations (Section 6.3):** The paper explicitly states "The semi-supervised phase did not produce dramatic metric gains" and transparently reports the precision-recall tradeoff introduced by pseudo-labeling (recall +0.03, precision −0.04 to −0.05). This candor is a methodological strength.
- **Practical design choices:** Class weighting instead of SMOTE (reasoning that pseudo-labeling will later add positives), F1/ROC-AUC rather than accuracy for the 12%-illicit imbalanced dataset, and stratified 5-fold cross-validation for hyperparameter tuning — all sensible, domain-appropriate decisions.

## Weaknesses

### Fatal
None.

### Major
- **No comparison to any existing method from the literature:** The related work (Section 3) cites multiple prior detection methods — GNNs at 92% accuracy (Nerurkar 2022), gradient-boosted models at 91% (Nerurkar et al. 2021), decision trees detecting 97% of mixing services (Rathore et al. 2022), metapath-aware GNNs (Song & Gu 2023), and hypergraph-based models (Lee et al. 2024). Not one appears as a baseline. The experiments compare only variants of the authors' own feature sets across three classifiers. This makes it impossible to assess whether the proposed approach is competitive. The paper should either adapt these baselines or explicitly justify why a direct comparison is infeasible for CoinJoin detection specifically.
- **SSL gains are negligible, yet the paper frames SSL as a successful contribution:** The best supervised XGBoost result is F1=0.844 (DEFAULT+REUSE+CS), and the best SSL result is F1=0.845 (DEFAULT+REUSE+CS+SSU) — a difference of 0.001. When comparing the same feature set (DEFAULT+REUSE+CS), SSL degrades performance from 0.844 to 0.839. Yet the abstract claims "SSL effectively leverages unlabeled data (F1-score: 0.84)" and the introduction (line 29) states SSL "outperforms supervised baselines." Section 6.3's honest discussion partially mitigates this, but the framing in the abstract, introduction, and conclusion overstates the finding. A null SSL result honestly reported would be more valuable than a 0.001 improvement presented as success.

### Minor
- **Pseudo-labeling procedure is materially under-specified (Section 5.3):** The paper states it selects "the top fraction of samples on both sides of the decision boundary, adjusting the share of positives and negatives" but does not specify batch size, number of iterations, the concrete selection fraction, or how the positive/negative share is adjusted. The claim that pseudo-labels are "disproportionately found in the more tractable SSU complexity classes" (line 285) is asserted without supporting data — no table or figure shows this distribution. These omissions impede reproducibility.
- **No confidence intervals or variance estimates:** With ~3,300 illicit test examples, standard errors on F1 are non-trivial. The reported fine-grained differences between feature sets (e.g., 0.844 vs. 0.841 for adding OTC) could fall within noise without formal testing. Reporting variance across CV folds would substantially strengthen the ablation analysis.
- **Cumulative-add feature ablation confounds feature type with feature count:** Features are added cumulatively (DEFAULT → +REUSE → +CS → +OTC → +SSU). When OTC is added and performance drops, the design cannot cleanly distinguish "OTC is noisy" from "more features cause overfitting." The paper partially mitigates this by including OTC-excluded combinations (e.g., DEFAULT+REUSE+CS+SSU without OTC in row 6 of each model block), but a cleaner design (e.g., replacing OTC with same-dimensionality random-noise features) would make the central quality-over-quantity claim more rigorous.
- **Novelty framing is overstated:** The abstract and introduction describe KeyLinker and SSU as "novel" features (abstract: "Novel, high-fidelity features—KeyLinker address clustering and Shared Send Untangling (SSU) complexity metrics"). However, KeyLinker is from Smolenkova & Yanovich (2025) and SSU is from Larionov & Yanovich (2023) — both are cited as prior work in the same sentence that calls them novel. The genuine contribution is the application and integration of these existing techniques, not their invention.

### Trivial
- Line 250 contains a factual discrepancy: it claims supervised XGBoost achieves F1=0.845 for DEFAULT+REUSE+CS+SSU, but Table 2 shows 0.842 for that configuration (line 273). The 0.845 figure appears in Table 3 as an SSL result.

## Nice-to-Haves
- A clean ablation isolating feature *quality* from feature *quantity* (e.g., replacing OTC features with random-noise features of the same dimensionality) would make the central claim more rigorous.
- Analysis of the dataset's properties beyond raw counts — e.g., SSU class distribution over time, inter-source label agreement rates — would strengthen the dataset contribution.
- Explicit justification for why existing methods from the literature cannot be adapted as baselines, if indeed the CoinJoin detection task is sufficiently distinct.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh Critic's claim that "SSU features actually reduce F1 from 0.844 to 0.842 when added to DEFAULT+REUSE+CS — this contradicts the narrative." Removed as a standalone criticism because the paper's core claim about SSU is that it helps in SSL (where SSU-combinations achieve the best result, 0.845), not that it universally improves supervised performance. The paper does not claim SSU improves supervised F1.
- Harsh Critic's suggestion that the OTC degradation of 0.003 F1 is "well within what could be explained by random seed variation." While technically true given absent variance estimates, the consistent pattern across all three models makes the paper's interpretation broadly reasonable. This concern is already covered by the "no confidence intervals" minor weakness.
- Strength Finder's "Clear mathematical problem formulation" — the formalization in Section 4 exists but is fairly standard notation for the domain, not a distinctive strength. Removed as generic.
- Harsh Critic's demand that the paper compare its dataset size to Elliptic/Elliptic++ to substantiate "complete." Removed: this is a nice-to-have analysis, not a weakness — the paper's dataset scale is genuinely large regardless of comparison.
- Harsh Critic's worries about label quality and inter-source agreement — the paper explicitly acknowledges "off-chain labeling sources may introduce inaccuracies" (line 23-24) and describes manual conflict resolution (line 199). The criticism overstates a limitation the paper already addresses.

## Novel Insights
None beyond the paper's own contributions. The core insight — that heuristic quality (cryptographic key reuse vs. behavioral OTC) matters more than heuristic quantity — is intuitive but well-demonstrated through the consistent ablation pattern.

## Suggestions
- If SSL truly adds nothing beyond supervised learning here (which the evidence suggests), reframe that as the finding: that 4.6M labeled CoinJoin transactions already saturate what tree-based models can extract from these features. A null SSL result honestly reported is more valuable than a 0.001 improvement framed as success.
- Add at least one adapted baseline from the cited literature (e.g., a GNN variant or the Rathore et al. decision-tree approach) to contextualize performance and demonstrate competitiveness.
- Report variance estimates (standard deviation across CV folds for all metrics) to distinguish signal from noise in the fine-grained feature-set comparisons.
- Specify the pseudo-labeling procedure with sufficient detail for reproducibility: batch size, number of iterations, selection fraction, and the distribution of pseudo-labels across SSU classes.

## Calibration Anchors
- `q7Xi4yZYcH` (3.00, Round 1): TRW-GCN for Ethereum anomaly detection. Our paper is clearly stronger — larger dataset, more thorough ablation, better writing.
- `yM7rw8Bo1f` (4.25, Round 1): FE-GNN for Ethereum account classification. Our paper is stronger — larger dataset contribution, more systematic feature ablation, more honest about limitations.
- `nwjgeFGbAF` (5.25, Round 2): Better Call Graphs dataset paper. Our paper is comparable but slightly stronger — more going on beyond just a dataset (feature engineering, SSL, ablation). Similar weakness: methodological novelty is limited.
- `LPXfOxe0zF` (5.75, Round 2): BlockFound blockchain foundation model. Comparable quality — BlockFound has better methodological novelty but weaker data. Our paper has stronger data but weaker methodology and no external baselines.
- `juE0rWGCJW` (6.33, Round 1): EX-Graph dataset bridging Ethereum and X. Our paper is weaker — EX-Graph has genuine novelty (first dataset linking two platforms) and thorough multi-task experiments. Our SSL contribution is marginal in comparison.

Round 1 bracket: 4.5–6.0. Round 2 narrowed to 5.25–5.75. Final score: **5.5**, positioned between Better Call Graphs (5.25, weaker dataset-only paper) and BlockFound (5.75, better methodology but worse data).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>