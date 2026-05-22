Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper tackles the detection of illicit transactions within Bitcoin CoinJoin (Shared Send Mixer) transactions, proposing a semi-supervised learning framework guided by feature engineering. The authors contribute: (1) a large-scale historical dataset of 1.15B transactions with 163M CoinJoin transactions and SSU complexity labels, (2) features derived from KeyLinker address clustering and Shared Send Untangling (SSU) metrics, and (3) an SSL scheme with confidence-based pseudo-labeling. The central thesis is that data quality (guided by high-fidelity features) matters more than data quantity for SSL in blockchain forensics.

## Strengths

- **Large-scale curated dataset with multi-source labeling.** The paper integrates blockchain data from Bitcoin Core (up to block 882,421) with address labels from WalletExplorer, Elliptic++, MBAL, and Kaggle sources, producing 1.15B transactions and 163M CoinJoin transactions with SSU complexity classification. This is a significant data curation effort and, if released, would be a valuable community resource. (Table 1)

- **Systematic ablation across models and feature sets.** Experiments test three classifiers (XGBoost, CatBoost, RandomForest) across seven feature combinations in both supervised (Table 2) and SSL (Table 3) settings. This allows for controlled observation of how each feature group (REUSE, CS, OTC, SSU) affects performance, providing more evidence than a single-model comparison would.

- **Well-motivated problem framing.** The paper correctly identifies that traditional supervised approaches struggle with mixed transactions (CoinJoin) precisely where labels are scarcest, and that SSL is a natural fit. The tension between data quantity and data quality in blockchain forensics is a genuinely important practical concern.

## Weaknesses

### Major

1. **The SSL results do not support the central claim that SSL "effectively leverages unlabeled data."** The best supervised F1 (XGBoost, Default+REUSE+CS) is 0.844 (Table 2, line 274). The best SSL F1 (XGBoost) is 0.845 (Table 3, line 319). This delta of 0.001 is negligible and well within cross-validation noise. Given that no confidence intervals or variance estimates are reported, the paper provides no statistical evidence that SSL adds any value over the supervised baseline. The paper acknowledges "performance remained stable" (line 289) and "did not produce dramatic metric gains" (line 297), yet the abstract and conclusion repeatedly claim SSL "effectively leverages unlabeled data" — the evidence for this is absent.

2. **The text description of the best feature set contradicts the tables, and several claimed patterns are not borne out by the data.**

   - **Line 291 claims:** "the best results were consistently achieved with the `Default+REUSE+CS+SSU` feature set." However, **this exact combination does not appear in either Table 2 or Table 3.** What appears is "Default+REUSE+CS" (no SSU) and the full set (all five features including OTC). There is no row showing "Default+REUSE+CS+SSU" (SSU without OTC).
   
   - **Line 252 claims:** "Adding OTC features reduced metrics." For XGBoost, adding OTC to Default+REUSE+CS reduces F1 from 0.844 to 0.841 (delta -0.003). But for CatBoost, the best supervised result (0.830, bolded) uses **all five features including OTC** (Table 2, line 270), outperforming Default+REUSE+CS (0.824). Similarly for RandomForest, all five features (0.830) beats Default+REUSE+CS (0.829). The OTC-degradation claim is model-dependent at best, and the paper's blanket assertion is misleading.
   
   - **Bolding is inconsistent:** In Table 2, XGBoost line 274 (F1=0.844) is not bolded, while line 277 (F1=0.842, a lower value) is bolded.

3. **The Data Quality Principle (Section 5.2) is not implemented in the SSL experiment.** Section 5.2 proposes prioritizing pseudo-labels from SSU Simple/Separable transactions and KeyLinker-clustered addresses. However, the actual pseudo-labeling procedure (Section 5.3) uses standard confidence-based thresholding: "we select the top fraction of samples on both sides of the decision boundary" (line 232). The paper asserts these confidence-selected examples are "disproportionately found in the more tractable SSU complexity classes" (line 289) but provides no evidence for this claim — no distribution of pseudo-labels by SSU class, no comparison of KeyLinker vs. OTC pseudo-label quality. The core methodological principle is stated but untested, severing the link between the proposed quality framework and the experiments.

4. **The claimed "novel features" (KeyLinker, SSU) are cited from prior work without clear differentiation.** The abstract states "Novel, high-fidelity features—KeyLinker address clustering and Shared Send Untangling (SSU) complexity metrics" as a contribution. But KeyLinker is cited as "Smolenkova & Yanovich (2025)" (line 32, 203) with no description of how it works, and SSU metrics are cited as "Larionov & Yanovich (2023)" (line 83). The paper does not explain what makes these "enhanced" (line 32) relative to the cited prior work, nor does it describe the methodology behind KeyLinker (e.g., how it exploits cryptographic key reuse, its accuracy, coverage). This makes the claimed contribution opaque.

### Minor

- **No statistical significance or variance reported.** All comparisons (e.g., OTC degrading F1 by 0.003, SSL improving F1 by 0.001) rely on point estimates without confidence intervals, standard deviations, or significance tests from the 5-fold cross-validation. Given the tiny magnitude of the claimed effects, this is a significant gap in evidence quality.

- **Tables 2 and 3 contain duplicate rows with identical feature sets but different metrics.** For example, in Table 2, CatBoost lines 269-271 all have the same checkmarks (all five features) but F1-scores of 0.800, 0.830, 0.827. In Table 3, XGBoost lines 318-321 all have the same checkmarks but F1-scores of 0.814, 0.845, 0.836, 0.836; CatBoost lines 312-313 are exact duplicates (F1=0.829). If these reflect different hyperparameter configurations, this should be explicitly stated in the table; as presented, the tables appear corrupted or poorly formatted.

- **The SSL experiment lacks comparison to alternative SSL methods.** The paper uses only self-training (confidence-based pseudo-labeling). No comparison to co-training, label propagation, MixMatch, or graph-based SSL methods — particularly odd given that the related work section discusses GNN-based SSL (Nerurkar 2022) and metapath-aware GNNs (Song & Gu 2023). A comparison would contextualize whether the specific approach matters or if SSL generically fails to improve here.

### Trivial

- XGBoost precision for the best SSL result (0.897, line 319) is rounded but previously listed as row 274's supervised precision (0.897) — the paper claims "pseudolabeling reduced precision (from -0.04 to -0.05)" but the supervised precision for the comparable model is 0.897 and SSL precision is also 0.897, showing no precision drop for XGBoost.
- The "Pseudolabeling slightly increased recall (up to +0.03)" claim (line 295) is not clearly verifiable from the table since comparable rows are not directly aligned.

## Nice-to-Haves

- An experiment comparing (a) confidence-based pseudo-labeling vs. (b) pseudo-labeling restricted to SSU Simple/Separable transactions vs. (c) pseudo-labeling restricted to KeyLinker-clustered addresses would directly test the quality-over-quantity hypothesis that the paper motivates but never evaluates.
- Feature importance analysis (SHAP or permutation importance) for the best model would show whether SSU complexity classes and KeyLinker features are actually among the top predictors, making the quality argument concrete.
- Releasing a data sample or schema for review would allow the community to assess the dataset's quality and labeling methodology.

## Removed Points

- **"SSL results are identical to supervised"** (Harsh Critic #1): Strictly, the best SSL is 0.845 vs supervised 0.844 — a difference exists. However, the delta is 0.001 with no significance testing, so the *substance* of this criticism remains in Major #1 above, just slightly softened from "identical" to "negligible improvement."

- **"No comparison to existing methods like GNNs"** (Harsh Critic #4): The paper is about feature-engineered SSL on CoinJoin transactions — a different methodological approach and task. GNN baselines on the Elliptic dataset target a different problem (general illicit detection, not CoinJoin-specific). The paper's scope is reasonably bounded. The absence of SSL method comparisons is retained as a Minor weakness.

- **"KeyLinker not defined"** (Harsh Critic #2): This is retained but reframed as Major #4 — the issue is not that it's undefined (it's cited as prior work) but that the paper claims it as a "novel" contribution while providing no description of what is novel relative to the cited work.

- **"Missing data collection details — how were 163M CoinJoin transactions identified?"** (Harsh Critic Section-by-Section): This is a reasonable question but not a fatal weakness. The paper states CoinJoin transactions are identified via standard heuristics and cites prior work. Moved to Removed as insufficiently specific to harm the core claims.

- **"Tag propagation rule assumes perfect clustering"** (Harsh Critic): This is a standard simplifying assumption in clustering-based label propagation and is not unique to this paper.

- **"Table 2 XGBoost Default+REUSE+CS+SSU listed twice with different F1"** (Harsh Critic #2): The critic misread the table — the rows in question have all five features (including OTC), not "Default+REUSE+CS+SSU." This combination doesn't appear in the table at all. However, the duplicate-row issue is a real concern (retained as Minor).

- **"Cannot be independently verified / dataset not released"** (Harsh Critic Missing Parts): The paper promises release upon acceptance, which is standard practice. Removed per hard rules.

- **"The paper should evaluate on the Elliptic dataset"** (Harsh Critic Missing Experiments): The paper focuses on CoinJoin transactions, which Elliptic does not specifically target. Scope creep.

- Various typos/formatting complaints: Removed per hard rules — these are parser artifacts.

- Strength Finder claims about "empirical proof that SSL gains depend on feature quality" and "novel high-fidelity features that demonstrably improve detection": Removed — these conflict with verified weaknesses (SSL shows no gain; features are from prior work).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension clearly — the paper's data collection and feature ablation efforts are substantial, but the experimental evidence does not support the central narrative about SSL effectively leveraging unlabeled data. This gap between what the paper does and what it claims is the most important observation to emerge from the review process.

## Suggestions

1. **Resolve the text-table contradictions.** Ensure that every feature combination discussed in the text has a corresponding row in the tables, and that the bolded best values actually reflect the highest metric values. If multiple hyperparameter configurations were tested for the same feature set, label these explicitly (e.g., with a hyperparameter ID).

2. **Either demonstrate SSL improvement or revise the claims.** If SSL provides no meaningful gain over supervised learning, this is a valid finding, but the paper must reframe its contributions accordingly — e.g., as a supervised feature-engineering study with an SSL extension that confirms the difficulty of improving on strong supervised models.

3. **Implement the quality-filtering principle.** Run an experiment that actually filters pseudo-labels by SSU class (Simple/Separable only) and/or KeyLinker clusters. Compare this to unfiltered confidence-based pseudo-labeling to test whether quality-filtering yields better SSL performance. Without this, the paper's core principle remains unvalidated speculation.

4. **Report variance or confidence intervals.** Five-fold cross-validation produces variance estimates; report them for the key comparisons (especially the OTC vs. no-OTC comparisons and the SSL vs. supervised comparison) so readers can assess whether the tiny observed differences are meaningful.

5. **Clarify novelty attribution.** Distinguish clearly which features and methods are original to this paper vs. adopted from prior work. If KeyLinker and SSU are existing tools being applied in a novel context, state this explicitly rather than calling them "novel features."

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>