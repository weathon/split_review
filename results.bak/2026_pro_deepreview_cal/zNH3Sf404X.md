Now I have a thorough understanding of both the paper and the calibration landscape. Let me write the consolidated review.

---

## Summary

This paper presents a semi-supervised learning framework for detecting illicit Bitcoin transactions within CoinJoin (Shared Send Mixer) flows. The authors construct a large dataset of 163 million CoinJoin transactions with 4.6 million labeled instances drawn from multiple external sources, engineer features based on cryptographic key-reuse clustering (KeyLinker) and Shared Send Untangling (SSU) complexity metrics, and evaluate three ensemble classifiers (XGBoost, CatBoost, RandomForest) under both supervised and pseudo-labeling regimes. The central claim is that detection performance is driven by feature quality — specifically, that high-fidelity features like KeyLinker and SSU enable effective SSL, while noisy heuristics like One-Time Change (OTC) degrade it.

## Strengths

- **Substantial dataset contribution.** The paper constructs a dataset of 163 million CoinJoin transactions with 4.6 million labeled instances aggregated from multiple public sources (WalletExplorer, Elliptic++, Kaggle datasets), with manual resolution of conflicting labels. The scale and curation effort, including explicit CoinJoin classification and SSU complexity annotations, is genuinely valuable for the blockchain forensics community (Section 5.1, Table 1).

- **Well-motivated, domain-specific feature engineering.** The KeyLinker clustering (leveraging cryptographic public-key reuse patterns) and SSU complexity metrics (classifying transactions by untangling difficulty: regular/simple/separable/ambiguous/time-limited) directly target the structural obfuscation that makes CoinJoin analysis difficult. These features are grounded in prior forensic literature and represent sensible operationalizations for the task.

- **Consistent ablation pattern across three classifier families.** In both supervised (Table 2) and SSL (Table 3) settings, the same qualitative pattern holds across XGBoost, CatBoost, and RandomForest: adding REUSE and CS features improves metrics, adding OTC features degrades them, and the REUSE+CS+SSU combination (without OTC) yields the best or near-best results. The cross-model consistency lends credibility to the core claim that OTC is a noisier signal than the alternatives.

- **Transparent treatment of class imbalance and evaluation.** The paper uses stratified 5-fold cross-validation, class weighting, reports multiple metrics beyond accuracy (F1, ROC AUC, precision, recall), and explicitly notes that the illicit class constitutes ~12% of labeled data. These are sound practices for the problem setting.

## Weaknesses

### Fatal

None.

### Major

- **No external baselines — the paper cannot situate its results relative to existing methods.** The related work section cites GNNs achieving 92% accuracy on similar tasks, gradient-boosted models at 91% for multi-class entity classification, and decision trees detecting 97% of mixing services. None of these appear as baselines; the evaluation compares only internal feature-set variants of the same three classifiers. Without at least one external comparison, the paper cannot establish whether its feature engineering and SSL framework offer any advantage over prior approaches — the core contribution is evaluated in a vacuum.

- **No error bars or statistical tests despite very small effect sizes.** The metric differences between feature combinations are frequently 0.01–0.03 F1 (e.g., XGBoost supervised F1 ranges from 0.814 to 0.844; adding OTC changes F1 by 0.003). With a dataset of 4.6M labeled transactions, even tiny differences can be statistically significant, but without standard deviations, confidence intervals, or significance tests, the reader cannot distinguish genuine effects from run-to-run variation. The central claims about OTC "degrading" performance and SSL providing "robustness" rest on these small, unqualified differences.

- **Text-table discrepancy in the reported best result.** Section 6.2 states: "XGBoost achieves the best supervised performance with an F1-score of 0.845 (default+reuse+cs+ssu)." However, Table 2 shows F1=0.842 for the XGBoost row with DEFAULT+REUSE+CS+SSU checked. The value 0.845 appears only in Table 3 (the SSL table), not in the supervised results. The claimed best result does not match the evidence table it refers to.

- **SSL methodology is underspecified and unreproducible.** The pseudo-labeling procedure is described only in general terms: "only the most confident predictions are retained," "select the top fraction of samples on both sides of the decision boundary," "adjusting the share of positives and negatives." No concrete threshold, fraction, batch size, or iteration count is provided. A reader cannot reproduce the SSL experiments from the paper as written. Furthermore, SSL performance is evaluated only on the held-out labeled test set, never on the unlabeled pool where SSL is supposed to provide benefit — whether pseudo-labeling improves generalization to the unlabeled majority is not tested.

### Minor

- **Overclaimed novelty of features.** The abstract and conclusion describe KeyLinker and SSU as "novel forensic features," but both are explicitly cited from prior publications (Smolenkova & Yanovich, 2025; Larionov & Yanovich, 2023). The actual contribution is their integration into an SSL pipeline, not their invention. The framing inflates the contribution.

- **Unvalidated ground truth labels.** Labels are propagated from external sources through clustering heuristics (including OTC, which the paper itself critiques as noisy). The paper acknowledges that "off-chain labeling sources may introduce inaccuracies" but provides no estimate of label error rates, no analysis of how clustering propagation may amplify noise, and no discussion of how label conflicts are resolved beyond a mention of manual resolution. If OTC-derived labels are noisy, the evaluation's foundation is uncertain. This is a known challenge in blockchain forensics and the paper is transparent about it, but it limits the strength of any conclusions drawn from the labeled data.

- **Conclusion overreaches relative to experimental design.** The paper concludes that "simply acquiring more labeled data is insufficient" and that the work "reframes the problem from data quantity to data quality." However, the experiments vary only which features are included — the labeled dataset size is never manipulated. The quantity-versus-quality framing is not directly tested; what is tested is feature-set ablation.

- **Apparent citation error.** Lee et al. (2024) is cited in the related work as presenting "CENSor, hypergraph-based model that integrates Cluster-GCN embeddings with Random Forest classifiers to achieve robust illicit transaction detection." However, the Lee et al. (2024) entry in the reference list is titled "Exploring the relationship between rarity and price of profile picture NFT: A formal concept analysis on the BAYC NFT collection," which appears unrelated to illicit transaction detection. This may be a wrong citation key.

### Trivial

- The SSL principle (Section 5.2) claims pseudo-labels from simpler SSU classes are higher quality, but this is never empirically validated — there is no check that pseudo-labels on SSU-Simple transactions have higher precision than those on Ambiguous ones. The connection between the principle and the implemented scheme (which selects high-confidence predictions globally, not by SSU class) is asserted rather than demonstrated.

## Nice-to-Haves

- An experiment that explicitly controls for labeled data quantity (training on increasing fractions of labeled data and comparing supervised vs. SSL curves) would directly test the "quantity vs. quality" framing.
- Direct validation of the data quality principle by evaluating pseudo-label precision stratified by SSU complexity class.
- A back-of-the-envelope estimate of the false-positive burden for a full blockchain scan, to ground the claim that the recall/precision trade-off is "acceptable for forensic analysis."
- Learning curves or feature importance rankings to complement the ablation tables.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic point about "Missing Parts — Error analysis on misclassifications"**: This is a nice-to-have, not a weakness. The paper is an ablation study over features; an error analysis would strengthen it but is not a required component.

- **Harsh critic point about "the paper never varies data quantity independently of quality"**: Already captured in the Minor weakness about the conclusion overreaching. The experimental design is about feature sets, not data quantity — this is a framing issue, not a separate methodological flaw.

- **Harsh critic criticism that tables are "uninterpretable" and contain "duplicated or inconsistent rows"**: The tables are dense but decipherable. The actual problem is the specific text-table discrepancy (0.845 vs. 0.842), which is retained as a Major weakness. The broader claim of uninterpretability is not supported — the tables are readable once one understands the checkmark convention.

- **Strength Finder claim about "Principled pseudo-label selection based on feature quality, not raw confidence"**: The paper describes this as a principle but does not implement explicit SSU-class filtering — it relies on confidence-based selection and argues that confident predictions happen to fall in simpler classes. This is moved to Trivial as an unvalidated assertion.

- **Strength Finder claim about "Robust experimental design and reproducibility" with "dataset is promised for release"**: The dataset promise is a strength of intent, but the SSL methodology is underspecified, so "reproducibility" as a blanket claim is too strong. The cross-validation and class weighting practices are retained in Strengths.

- **Harsh critic point about "the abstract states that the work proves that common heuristics like OTC introduce noise"**: This is essentially the same as the Minor weakness about overclaiming. Merged rather than duplicated.

- **Harsh critic point about "no sensitivity analysis to label balancing or to the choice of evaluation metric"**: This is a generic "could do more" request, not a specific weakness. Removed.

- **Harsh critic point about "the mapping from categorical SSU labels to features"**: The paper states categorical features are one-hot encoded (Section 5.1). This criticism is already addressed in the paper. Removed.

- **Harsh critic point about "no learning curves or feature importance rankings"**: Nice-to-have, not a weakness. Removed.

## Novel Insights

None beyond the paper's own contributions. The observation that SSL performance in blockchain forensics may depend more on feature fidelity than on pseudo-label volume is interesting but is hypothesized rather than rigorously demonstrated by the current evidence.

## Suggestions

- **Fix the 0.845 / 0.842 discrepancy immediately.** The best supervised result claimed in the text must match the corresponding row in Table 2.
- **Add error bars** (standard deviations across cross-validation folds) to Tables 2 and 3. With a dataset this large and 5-fold CV, this is straightforward and would transform the persuasiveness of the ablation.
- **Include at least one external baseline** — even a simple reimplementation of a cited method (e.g., the decision tree approach from Rathore et al. 2022) on the same data split would provide essential context.
- **Specify the pseudo-labeling hyperparameters** (selection fraction, batch size, iteration count, positivity adjustment mechanism) so the SSL experiments are reproducible.
- **Tone down novelty claims** — describe KeyLinker and SSU as "recently developed" or "forensic-aware" features rather than "novel," and clarify that the contribution is their integration and evaluation within an SSL framework.
- **Verify and correct the Lee et al. (2024) citation** — if CENSor is by a different set of authors, fix the reference.

---

**Originality:** Moderate. The dataset and the integration of KeyLinker/SSU into an SSL pipeline are genuine contributions, but the individual components (features, classifiers, pseudo-labeling) are all established techniques. The quality-over-quantity framing is a valuable perspective but is not itself a novel methodological insight.

**Importance of research question:** High. Illicit cryptocurrency transaction detection is a problem of clear practical significance, and the scarcity of reliable labels in mixing contexts is a real bottleneck that SSL could help address.

**Claim support:** Weak to moderate. The consistent ablation pattern across three models is genuine evidence, but the lack of error bars, missing baselines, text-table discrepancy, and underspecified SSL methodology prevent the central claims from being fully substantiated.

**Soundness of experiments:** Below the bar for acceptance in current form. Stratified CV, class weighting, and multiple metrics are good practices, but the absence of uncertainty quantification, external baselines, and reproducible SSL details are significant gaps.

**Clarity:** Adequate. The paper is generally well-written and the motivation is clear, though the table presentation could be improved and the SSL section needs more detail.

**Value to the research community:** The dataset, if released, would be a genuine resource. The feature analysis provides useful guidance for practitioners. However, the paper's conclusions are not yet on firm enough footing to serve as a reliable foundation for follow-up work.

### Score anchored against calibration set:

- **FE-GNN (4.25)**: Ethereum account classification with feature-enhanced GNN; rejected for limited novelty, missing baselines, no error bars. Our paper has a far larger and more carefully curated dataset, more thorough ablation, and a clearer narrative — clearly stronger.
- **BlockFound (5.75)**: Customized blockchain foundation model for anomaly detection; rejected despite more technical novelty due to dataset limitations (28 malicious transactions). Our paper has a substantially better data foundation but less methodological novelty. Comparable overall, but our paper's evaluation gaps are more structural (no error bars, missing baselines, text-table discrepancy) while BlockFound's weakness is more about the limited anomaly sample. Slightly below BlockFound.
- **EX-Graph (6.33)**: Dataset paper linking Ethereum and Twitter; accepted. Cleaner execution, better evaluation, clearer contribution. Our paper has more ambition but poorer execution — clearly below.

The paper falls between FE-GNN (4.25) and BlockFound (5.75), closer to BlockFound in overall merit given the dataset scale, but pulled down by the evaluation gaps. Placed at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>