I now have a thorough understanding of the paper and all the claims. Let me write the consolidated review.

## Summary

This paper proposes MILAD (Multi-Instance Learning for Anomaly Detection), a method that combines attention-based MIL with a two-stage training pipeline (attention-based sample weighting followed by XGBoost classification) for detecting anomalous transactions in sequence data, with an application to credit card delinquency risk control. The method is evaluated on a synthetically constructed bag-of-transactions dataset derived from the Credit Card Fraud Detection (CCFD) dataset against the DAGMM unsupervised anomaly detection method.

## Strengths

- **Interpretability from attention weights**: The paper demonstrates (Table 3) that MILAD's attention weights assign higher values to known abnormal samples within anomaly bags, providing a mechanism for transaction-level explanation that unsupervised methods like DAGMM cannot offer. This is a concrete advantage for the stated application domain.

- **Principled handling of the weakly-supervised setting**: The MIL framework correctly models the realistic scenario where only bag-level labels (monthly overdue status) are available but individual transaction labels are not, avoiding the need for expensive manual labeling of individual transactions.

- **Flexibility to different anomaly definitions**: The paper evaluates under both the standard assumption (any single abnormal transaction triggers bag anomaly) and the collective assumption (abnormal transaction amount proportion matters), with the Self-Attention variant designed to capture inter-sample interactions relevant to the collective case.

## Weaknesses

### Major

1. **Evaluation dataset does not support the claimed application domain.** The paper's title and motivation target "credit card delinquency risk control," but the evaluation uses the CCFD fraud detection dataset, where (a) fraud is not the same as delinquency-precursor behavior, and (b) transactions are randomly grouped into fixed-size bags (J=10) with no temporal structure preserved. Real monthly credit card statements have variable length, temporal ordering, and spending-pattern dependencies. The paper provides no evidence that performance on these synthetic random bags transfers to real monthly transaction sequences. The lack of a real-world case study or a more realistic data generation procedure means the claimed practical utility for delinquency risk control is unsubstantiated. The paper itself acknowledges data limitations (lines 157-160), but this does not bridge the gap between the claimed application and the actual evaluation.

2. **The comparison against DAGMM does not isolate the method's contribution.** MILAD uses bag-level labels (weak supervision) while DAGMM is purely unsupervised. Unsurprisingly, MILAD outperforms DAGMM by large margins (Table 2: AUC 0.97 vs. 0.52 under standard assumption). The paper acknowledges this (lines 232-234: "because DAGMM is an unsupervised learning method, while MILAD is a supervised learning algorithm"), yet frames this as evidence of MILAD's superiority. This confounds method architecture with supervision availability. Without comparisons against other weakly-supervised or MIL-based anomaly detection methods (e.g., naive MIL with max-pooling, other attention-based MIL models, or pseudo-labeling followed by supervised learning), it is impossible to tell whether MILAD's specific design choices — the attention mechanism, the self-attention variant, or the two-stage training — add value beyond any generic method that assigns bag labels to all instances and trains a supervised classifier.

3. **Critical experimental details are missing, making key results uninterpretable.**
   - **Sample-level predictions**: Table 2 reports Precision, Recall, F1, and AUC for sample-level anomaly detection, but the paper never specifies how MILAD's bag-level probabilities and attention weights are converted into binary sample-level predictions (or even sample-level scores for AUC). The pseudo-label generation step is mentioned (line 124: "anomaly set S = {ŷ₁, ..., ŷⱼ}") but the procedure for obtaining these pseudo-labels from attention weights is never described.
   - **DAGMM bag-level adaptation**: For the sequence-level detection experiment (Table 4), where bag-level predictions are needed, the paper does not describe how DAGMM's sample-level outputs are aggregated into bag-level predictions. The paper simply states "All models are trained to achieve their best performances" (line 247).
   - **Hyperparameter sensitivity**: Key parameters (bag size J=10, threshold Δ=0.1, training set sizes N₁=200, N₂=50) are stated without justification or sensitivity analysis, with only a single dataset split and no variance estimates reported.

### Minor

- **Overclaim relative to evidence**: The Abstract states that MILAD "outperforms the most commonly used algorithms" (line 57-58), but the paper only compares against DAGMM. Framing DAGMM as "the most commonly used unsupervised deep learning algorithm for credit card risk control" (lines 199-200) is itself an overstatement — DAGMM is a general anomaly detection method, not a standard tool in credit card risk control.

- **Limited methodological novelty**: The method applies existing techniques — Attention-based MIL (Ilse et al., 2018), Self-Attention (Vaswani et al., 2017; Rymarczyk et al., 2021), and a two-stage pseudo-labeling pipeline — in a straightforward combination. No new architectural component, learning objective, or theoretical insight is introduced. The paper's contribution is confined to applying these existing tools to a synthetic version of a credit card problem.

- **Loss function not specified**: The paper mentions the Adam optimizer (line 88) and a Sigmoid output layer (line 504) but never explicitly states the loss function (presumably binary cross-entropy). This is a basic implementation detail that should be stated.

- **Author Contributions and Acknowledgments are placeholders** (lines 260-261), suggesting the manuscript may have been submitted in an incomplete state.

### Trivial

- Equation (1) uses a nonstandard binomial notation `\binom{1}{0}` for binary classification.
- The loss curves (Figure 2) show MILAD overfitting after 10-30 epochs with only 200 training bags — the paper reports using early stopping based on this observation, but does not describe using a validation split for early stopping.

## Nice-to-Haves

- A comparison against simple weakly-supervised baselines (e.g., treating all samples in positive bags as anomalous and training a supervised classifier; max-pooling MIL without attention).
- A realistic bag construction that preserves temporal ordering and variable bag sizes to better approximate real monthly credit card statements.
- Variance estimates (e.g., standard deviations over multiple random seeds or bag constructions) to assess result stability given the small training set (N₁=200).

## Removed Points

These points were flagged by the reviewers but are removed after verification:

- *"The threshold δ is never explicated"* — The paper states (lines 174-175) that δ is chosen to maximize F1 on the training set. The criticism is factually incorrect.
- *"The Basic method and Self-Attention method pairing with standard/collective assumptions has no rationale"* — The appendix (lines 416-428) explains that the Basic method assumes sample independence (standard assumption) while Self-Attention captures inter-sample interactions (collective assumption). The critic appears to have missed this.
- *"Logical inconsistency: paper claims only bag labels are available but uses transaction labels to construct bags"* — This is standard MIL evaluation methodology. The paper uses known transaction labels to construct the evaluation data (with known ground truth) while the method itself never accesses them during training. No inconsistency exists.
- *"The paper misrepresents existing work"* regarding citations to XGBoost and GeniePath — These are general-purpose algorithms but have indeed been applied to financial risk problems. The characterization is not misleading.
- *"Typographical errors ('hiden label')"* — Per instructions, formatting/typographical issues are likely parser artifacts and are removed.
- *Strength: "Significant performance improvement over DAGMM"* — This conflicts with the verified weakness (#2 above) that the comparison is unfair and uninformative. The performance gap is attributable to supervision availability, not to MILAD's design. Moved here per rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring pattern: papers that propose a combination of existing methods for a specific application domain often fail to bridge the gap between the claimed application and the actual evaluation setup. Here, the disconnect is between "credit card delinquency risk" (the motivation) and "fraud detection with synthetic random bags" (the evaluation). Additionally, the paper's framing of a supervised-vs-unsupervised comparison as evidence of methodological superiority reflects a common but fallacious argument pattern in the literature.

## Suggestions

1. **Replace or substantially augment the evaluation**: The core weakness is that the evaluation does not match the claimed application. Either (a) obtain a dataset with actual monthly transaction sequences and overdue labels (e.g., from a financial institution, Kaggle credit risk competition, or synthetic generation that preserves temporal structure and realistic bag compositions), or (b) reposition the paper as a general MIL anomaly detection method without the specific credit card delinquency claim.

2. **Add competitive weakly-supervised baselines**: Without comparisons against methods that also use bag-level labels, there is no evidence that MILAD's specific design choices matter. At minimum, include naive MIL baselines (max-pooling, mean-pooling), ABMIL (Ilse et al., 2018) as a direct ablation, and a simple pseudo-labeling approach.

3. **Document the sample-level prediction procedure**: Clearly state how attention weights and/or bag-level probabilities are converted to sample-level predictions/scores for the metrics in Table 2.

4. **Describe the DAGMM bag-level adaptation** used for Table 4, or replace DAGMM with a baseline that natively produces bag-level outputs.

5. **Report variance** over multiple data constructions or train/test splits given the small dataset.

## Score and Decision

This paper has a fundamental disconnect between its claimed application (credit card delinquency risk control) and its evaluation (fraud detection with synthetic random bags). Additionally, the only baseline comparison is uninformative (supervised vs. unsupervised), critical experimental details are missing, and the methodological novelty is limited to combining existing techniques. These issues collectively undermine the paper's core claims.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>