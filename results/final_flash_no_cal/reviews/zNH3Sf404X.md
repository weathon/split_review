Now I have a clear picture of the paper and can verify the reviewer claims against the actual content. Let me produce the consolidated review.

## Summary

The paper presents a semi-supervised learning (SSL) framework for detecting illicit Bitcoin CoinJoin transactions, introducing a large-scale labeled dataset (163M CoinJoin transactions), novel forensic features (SSU complexity metrics and KeyLinker-based address clustering), and a pseudo-labeling approach. The main empirical finding is that the widely-used OTC (One-Time Change) heuristic degrades detection performance across both supervised and SSL settings, while features derived from SSU complexity classes and key-reuse patterns consistently yield better results. The paper argues that feature quality, not data volume, drives SSL success.

## Strengths

1. **Systematic empirical demonstration that OTC degrades performance.** Tables 2 and 3 show that across three model families (XGBoost, CatBoost, Random Forest) in both supervised and semi-supervised settings, adding OTC features consistently reduces F1 and ROC AUC compared to the same feature set without OTC. This is a clean, reproducible finding that challenges a widely used heuristic, and it is the paper's strongest concrete contribution.

2. **Introduction of a large-scale CoinJoin transaction dataset.** The paper compiles and describes the first complete historical dataset of ~163M CoinJoin transactions with SSU complexity classifications and multi-source legality labels. Dataset construction is a substantial effort that enables reproducibility and future research in this space.

3. **Validation of SSU complexity metrics as predictive features.** The paper demonstrates that adding SSU complexity class labels as features improves detection (e.g., XGBoost F1 from 0.837 to 0.842 in supervised, reaching the best SSL F1 of 0.845). This operationalizes transaction untangling complexity as a usable forensic signal.

## Weaknesses

### Major

1. **The "quality-guided" pseudo-labeling principle is described but not implemented.** Section 5.2 describes a principle of prioritizing pseudo-labels by SSU class and KeyLinker clusters. However, the actual pseudo-labeling procedure (Section 5.3, Section 6.3) is standard confidence-threshold selection—"only the most confident predictions are retained," "select the top fraction of samples on both sides of the decision boundary." No mechanism explicitly filters, weights, or prioritizes by SSU complexity class or KeyLinker clustering. The paper observes that confident predictions are "disproportionately found in the more tractable SSU complexity classes" (Section 6.3), but this is a post-hoc correlation, not a causal implementation of quality guidance. The paper's central methodological claim—that SSL success is contingent on *quality-aware* pseudo-labeling—is therefore unsupported by the experimental design. The approach is effectively standard self-training framed as quality-driven.

2. **The "quality over quantity" thesis is not tested.** The paper's title and narrative argue that feature quality matters more than data quantity in SSL. However, no experiment varies the *quantity* of pseudo-labels while holding features fixed, nor varies features while holding pseudo-label quantity fixed. The experiments compare different feature sets (with/without OTC) within a fixed pseudo-labeling procedure, which tests feature *composition* but not the quantity-versus-quality tradeoff. The claim that "additional data harms performance" (Section 6.3) is based on adding OTC as a feature—which changes the feature set, not the data quantity. Whether adding more pseudo-labels (e.g., by lowering confidence thresholds) degrades performance is never tested. The thesis is asserted in the framing but never subjected to a controlled experiment.

3. **SSL gains over supervised are negligible and lack statistical grounding.** The best SSL result (XGBoost F1=0.845) exceeds the best supervised result (F1=0.844) by 0.001. Comparing the same feature set (DEFAULT+REUSE+CS+SSU), SSL goes from 0.842 to 0.845, a gain of 0.003. No confidence intervals, standard deviations across cross-validation folds, or significance tests are reported anywhere. The paper acknowledges "not dramatic metric gains" but still concludes that "SSL effectively leverages unlabeled data" (abstract) and "outperforms supervised baselines" (Section 1, contribution 3). A difference this small cannot be interpreted as evidence of SSL benefit without variance estimates, and the accompanying precision drop (from -0.04 to -0.05) is not discussed as a potential cost. The practical value of SSL for this task is not demonstrated.

4. **No comparison against alternative SSL methods or external baselines.** The SSL evaluation compares only against the same model trained without pseudo-labels. There is no comparison to standard SSL baselines (e.g., self-training with fixed threshold, entropy minimization, pseudo-labeling with data augmentation) or to graph-based SSL methods that are natural for blockchain transaction graphs. Given that the related work cites GNNs achieving 92% accuracy on related tasks, the absence of any GNN or SSL baseline limits the paper's ability to contextualize its results or test whether its claims about quality-guided SSL extend beyond gradient-boosted self-training.

### Minor

1. **Pseudo-labeling procedure is under-specified for reproducibility.** Section 5.3 states that "we select the top fraction of samples on both sides of the decision boundary, adjusting the share of positives and negatives," but no concrete fractions, thresholds, or adjustment rules are given. The number of pseudo-labels added, their positive/negative composition, and how the top fraction was chosen per model are not reported. Without these details the experiment cannot be reproduced or assessed for conservativeness.

2. **Ambiguity between KeyLinker (clustering technique) and REUSE (model feature).** The paper presents KeyLinker as a "novel, high-fidelity feature" (abstract, Section 1), but the feature column in Tables 2 and 3 is labeled REUSE (key reuse), not KeyLinker. From the methodology, KeyLinker is an address-clustering technique used for dataset construction and label propagation, while REUSE is a transaction-level feature capturing address-repetition patterns. The relationship between the two is never explained, making it difficult to assess what exactly KeyLinker contributes to the classification model versus the dataset.

3. **Inconsistency between text and tables for supervised best F1.** Section 6.2 states "XGBoost achieves the best supervised performance with an F1-score of 0.845 (default+reuse+cs+ssu)," but Table 2 shows F1=0.842 for this configuration (XGBoost row 6). The table shows the best supervised XGBoost F1 as 0.844 (row 3, DEFAULT+REUSE+CS, without SSU). At minimum, the text and table are inconsistent; at worst, the improvement claimed for SSL is based on comparing against the wrong supervised number.

4. **No discussion of limitations.** The paper has no explicit limitations section despite acknowledging label inaccuracies from off-chain sources, marginal SSL gains, and potential noise from clustering propagation. Including a limitations paragraph would improve credibility.

## Nice-to-Haves

- **Explicit quantity-versus-quality experiment.** Varying pseudo-label quantity (e.g., by changing confidence thresholds) while holding features fixed, and plotting F1 against pseudo-label count, would directly test the core thesis.
- **GNN or graph-based SSL baseline.** Given the transaction graph structure, a graph-based method would contextualize the tree-based results.
- **Ablation of pseudo-labels by SSU class.** If the paper's quality principle is correct, filtering pseudo-labels to only Simple/Separable transactions should outperform or match unfiltered pseudo-labeling. This experiment would directly support the claimed mechanism.

## Removed Points

The following points from the reviews were considered but removed under the filtering rules:

- **Table formatting/alignment complaints (harsh critic §Section-by-Section, Tables 2 and 3):** The duplicated checkmarks and apparent alignment errors in the extracted tables are PDF parsing artifacts, not errors in the paper itself. Removed per the rule against formatting/style nitpicks.
- **Criticism that SSL doesn't compare against "adding the same pseudo-labels to the training set and retraining in a fully supervised manner":** This misunderstands the method. The SSL procedure *is* retraining with pseudo-labels in a supervised manner; there is no separate "semi-supervised algorithm" distinction beyond the self-training loop. The comparison is supervised (no pseudo-labels) vs. self-training (with pseudo-labels), which is standard.
- **Generic "could be stronger with more models/data" concerns:** The model zoo (3 families) and dataset size (163M transactions) are already adequate for the paper's scope. These demands would be scope expansion, not fixes to the current claims.
- **Strength Finder's generic claim that the problem is "important":** The importance of the domain is not a strength of this specific paper's contribution. Removed as generic praise.
- **Strength Finder's claim about "rigorous and granular ablation study design":** The ablation is systematic but not exceptional; the claim overstated its novelty. Replaced with the concrete verification that OTC degrades performance across settings, which is precise and evidenced.

## Novel Insights

The harsh critic's central observation—that the paper's narrative about "quality-guided SSL" was written before the experiments, and the experiments do not implement the mechanism the narrative describes—points to a structural mismatch that a superficial reading might miss. The paper is essentially a well-executed feature-ablation study (showing OTC harms, SSU helps) wrapped in an SSL framing that adds nothing beyond standard self-training. The dataset and the OTC finding are real contributions, but the paper would be significantly stronger if it acknowledged this and pitched itself as "a feature engineering study for blockchain forensics" rather than "a quality-driven SSL framework." Conversely, the Strength Finder correctly identifies that the OTC degradation result is robust and reproducible across models—this is the paper's strongest empirical finding, not the SSL comparison.

## Suggestions

1. **Reframe the paper around its actual contributions:** the large-scale SSM dataset, the feature engineering analysis, and the clear demonstration that OTC degrades detection. Either implement a genuine quality-filtering mechanism in the pseudo-labeling pipeline, or drop the "quality-driven SSL framework" narrative and present the SSL component as a straightforward self-training baseline with the feature analysis as the primary contribution.

2. **Add cross-validation variance** (std of F1, precision, recall across folds) to all main tables. Without this, the 0.001–0.003 F1 differences between SSL and supervised are uninterpretable.

3. **Report concrete pseudo-labeling details:** number of pseudo-labels added per model, the fraction selected from each confidence quantile, and the resulting class distribution. This is essential for reproducibility.

4. **Clarify the relationship between KeyLinker and REUSE** in the feature column. If KeyLinker is used only for label propagation during dataset construction and REUSE is the actual model feature, state this explicitly. If KeyLinker-derived signals enter the model through some other path, describe it.

5. **Correct the inconsistency** between the text (Section 6.2 claims supervised F1=0.845 for the SSU feature set) and Table 2 (shows F1=0.842 for that configuration).

## Score and Decision

This paper has genuine contributions—the large-scale dataset and the robust finding that OTC degrades performance are valuable to the blockchain forensics community. However, the paper's central thesis about a quality-driven SSL framework is not supported by the implemented experiments: the pseudo-labeling is standard confidence-threshold self-training with no quality-filtering mechanism, the SSL gains over supervised are vanishingly small (F1 +0.001 to +0.003) with no variance estimates, and the "quality over quantity" hypothesis is never tested in a controlled way. The narrative consistently overstates what the evidence can support. The paper could become a solid contribution if reframed around its genuine strengths (dataset, feature ablation) and the SSL claims were either substantiated with proper experimentation or scaled back. In its current form, the evidence does not match the claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>