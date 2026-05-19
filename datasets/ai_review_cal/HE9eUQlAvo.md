- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 8, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes a framework that combines influence functions with regression trees (with hierarchical shrinkage) to identify which training samples benefit or harm a convex classifier's performance across utility, fairness, and robustness. It then uses a simple trimming strategy (removing the most negatively-influential samples) to improve model performance. The approach is evaluated on synthetic and real-world datasets across seven application scenarios: conventional classification, distribution-shift fairness, fairness-poisoning defense, evasion-attack defense, online learning with noisy labels, and active learning.

## Strengths

- **Interpretable influence estimation via feature-space trees (Algorithm 1).** The paper goes beyond per-sample influence scores (Koh & Liang 2017, TracIn, etc.) by training a regression tree with hierarchical shrinkage to map feature ranges to influence values. This provides practitioners a visualization of *which feature regions* help or hurt the model, which prior influence-function work does not directly offer. Figure 3 shows an example subtree.

- **First effective defense against fairness-poisoning attacks.** Section 5.2 (Table 1) shows that influence-based trimming substantially improves fairness (lower DP) after RAA and NRAA attacks on German, Compas, and Drug datasets, without sacrificing utility. The paper correctly notes there are currently no well-performing defenses for these attacks in the supervised setting, making this a genuinely novel contribution.

- **Consistent performance gains across utility, fairness, and robustness demonstrated on multiple real-world datasets.** Figure 2 shows that trimming as little as 5% of training data via Algorithm 2 yields large fairness and robustness improvements across Adult, Bank, CelebA, and Jigsaw Toxicity, while random trimming fails. The adversarial robustness accuracy on the toy example improves from ~0.01 to 0.42.

- **Improved fairness under distribution shift with multiple baselines.** Section 5.1 (Figure 4) compares trimming against Correlation Shift, FairBatch, RLL, and Influence-based Reweighing on ACS Income under three distribution shifts. Trimming boosts both the vanilla model and existing fairness interventions, showing generalizability as a pre-processing step.

- **Effective active learning with competitive baselines.** Section 5.5 (Figure 6E) shows that influence-based sampling outperforms random, entropy, margin, uncertainty, and ISAL on the Diabetic Retinopathy dataset over 5 runs, demonstrating a practical advantage in the unlabeled setting.

- **Defense against adaptive evasion attacks and online learning with noisy labels.** Sections 5.3–5.4 show that trimming 2.5% of training data restores accuracy above pre-attack levels under adaptive evasion (10 runs), and consistently improves accuracy over baselines in online streaming with one-third label noise across four datasets.

## Weaknesses

### Fatal
None.

### Major

- **No error bars or variance on the core trimming experiments (Figure 2).** The main results that drive the paper's central claim — improvements in utility, fairness, and robustness on Adult, Bank, CelebA, and Jigsaw Toxicity — are presented as single curves without any measure of variability. While the evasion-attack experiment (Section 5.3) reports 10 runs and the active learning experiment (Section 5.5) reports 5 runs, the foundational Figure 2 does not. Given the small trimming budgets (≤5%), stochasticity in the training process, and known noise in influence estimates, the reader cannot assess whether the observed improvements over random trimming are statistically significant or artifacts of a particular initialization/split.

- **Only random trimming as a baseline in the core trimming experiments (Figure 2).** For a paper whose central claim is that influence-based data selection improves classifier performance, random removal is the weakest possible baseline. The paper discusses Shapley-value-based approaches (TMC-Shapley, KNN-Shapley), TracIn, representer points, and Datamodels in the Introduction but never compares against any of them in the core trimming experiments. Even simple heuristics (e.g., removing high-loss or low-margin samples) would provide a more informative comparison. The lack of strong baselines makes it difficult to gauge whether the proposed method is genuinely effective or merely exploiting easy-to-remove outliers.

### Minor

- **The active learning method's underlying assumption is not fully justified.** Section 5.5 trains the influence-prediction tree "without labels" on the unlabeled pool and then uses it to predict influence. Since influence values depend on class labels (via the gradient term), predicting influence from features alone assumes that influence is mainly a function of feature geometry — a strong assumption that is acknowledged but not validated. The empirical results (Figure 6E) suggest the approach works, but a theoretical justification or ablation (e.g., comparing to a version that uses pseudo-labels) would strengthen this line.

- **Limited baseline comparisons in poisoning and evasion experiments.** Table 1 (Section 5.2) compares only against pre-attack and post-attack metrics, not against alternative defenses (even simple ones like loss-based filtering). Similarly, Section 5.3's evasion defense is shown only against the "no defense" baseline. The paper's claim of being "potentially the first defense" may be accurate, but demonstrating that the approach outperforms a simple heuristic baseline would strengthen the contribution.

- **The interpretability contribution is minimally validated.** The regression tree (Figure 3) is presented as a tool for interpreting which feature ranges correspond to positive/negative influence, but no analysis is provided to verify that the identified regions correspond to meaningful data characteristics. For instance, the paper does not show that samples in the "positive influence" region consistently help across different random seeds, or compare the tree's insights against simple influence-score ranking to demonstrate added value.

- **The toy experiments (Section 4, Figure 1) are illustrative but the paper over-interprets them.** The alignment between influence regions and intuitive patterns (e.g., boundary points harming robustness) is a sanity check, not a rigorous validation. The claim that robustness is "significantly improved from 0.01 to 0.42" relies on a single synthetic setup with one random seed.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing trimming based on raw influence scores vs. tree-predicted influence scores would clarify whether the tree component adds value beyond noise reduction.
- Reporting runtime or computational cost (Hessian inversion, tree training) for the datasets used would help practitioners assess feasibility for larger-scale problems.
- An analysis of the characteristics of trimmed samples (e.g., Are they outliers? Mislabeled? Near decision boundaries?) would directly support the paper's interpretability framing.

## Removed Points
Points from the inputs that are flagged to be removed; treat them with caution:

- *"The claim that 'influence functions can be used interchangeably with Shapley values' is not tested."* — The paper actually says "allowing for any influence approach to be used interchangeably" (referring to different influence estimation methods, not Shapley values). The critic misread the text. **Removed: factually incorrect.**

- *"The active learning extension is methodologically unsupported... results unreliable."* — The method is clearly described (Section 5.5), and the empirical validation (Figure 6E) demonstrates it works. The assumption that influence can be predicted from features is a reasonable transfer-learning approximation, and the critic's claim that it is "untested" is contradicted by Figure 6E. **Removed: overstatement contradicted by evidence in the paper.**

- *"The double-y-axis format is hard to read / the left and right scales are not aligned."* — A formatting nitpick about figure presentation. **Removed: formatting nitpick.**

- *"The paper's empirical contribution is not believable in its current form"* and *"does not meet the standard of evidence required."* — These are summary judgments that overstate the severity of the gaps. The paper has real contributions with multiple experiments and baselines in several scenarios. **Removed: opinion unsupported by systematic review of the paper's actual evidence.**

- *"The paper dismisses Shapley-based methods as computationally expensive but never evaluates them."* — The paper provides a valid rationale: Shapley-based methods are designed for utility, not fairness/robustness; KNN-Shapley is model-agnostic and cannot guarantee performance on a specific downstream classifier. This is a reasonable justification for not including them as baselines. **Removed: the paper provides a substantive justification.**

- *"Missing appendix, missing proofs in appendix."* — These sections were stripped by the PDF parser; they exist in the original submission. **Removed: parser artifact.**

- Criticisms about *"weaknesses"* that are actually the paper's self-acknowledged limitations (e.g., the trimming being a simple heuristic — the paper says exactly this in the Conclusion). **Removed: the paper already addresses these.**

## Novel Insights
None beyond the paper's own contributions. The two inputs (harsh critic and strength finder) largely re-describe the paper's content and trade-offs rather than providing a new perspective on the work.

## Suggestions
1. **Add variance estimates** (error bars or confidence intervals from multiple runs) to Figure 2 and the toy experiments. This single change would substantially increase the credibility of the core results.
2. **Include at least one non-random baseline** in the core trimming experiments. A simple alternative like removing high-loss samples or, on a smaller dataset, comparing to a Shapley-based approximation (e.g., TMC-Shapley on Adult) would provide a meaningful point of reference.
3. **Expand the baseline comparisons** in the poisoning defense (Table 1) and evasion defense (Figure 5) to include a simple heuristic (e.g., loss-based filtering) so the reader can assess relative effectiveness.
4. **Validate the interpretability contribution** by analyzing the characteristics of samples in the positive/negative influence regions identified by the tree (e.g., statistics on label noise, distance to decision boundary, or outlier scores).
5. **Clarify the active learning assumption** — either provide a theoretical justification for predicting influence from features alone, or add an ablation comparing to a version that uses pseudo-labels from the base model.
