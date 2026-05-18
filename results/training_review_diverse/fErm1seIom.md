Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary

This paper proposes FMP-AE, a hybrid unsupervised time series anomaly detection method that combines a 1D-CNN-based Matrix Profile (MP) loss with an Autoencoder reconstruction loss. The model is trained on normal data only, using a total loss that normalizes and balances both terms. At test time, the anomaly score combines softmax-weighted MP values with reconstruction error. Experiments on the UCR250 benchmark (250 files) report an F1-score of 86.79% and precision of 81.03%, outperforming 14 baselines. A five-way ablation study shows that each component contributes to overall performance.

## Strengths

1. **Novel hybrid loss combining MP and AE signals.** The idea of integrating a Matrix-Profile-based loss into an autoencoder training objective is original and well-motivated. The ablation confirms the synergy: removing the MP loss ("Only AE") drops F1 from 86.79% to 67.87%, and removing the autoencoder ("MP+1D-CNN") drops it to 40.12% (lines 277, 283). This demonstrates that both components are complementary.

2. **Strong reported performance on the UCR250 benchmark.** FMP-AE achieves the highest precision (81.03%) and F1-score (86.79%) among 14 baselines, outperforming ADTransformer (F1=82.37%), LSTM-VAE, OmniAnomaly, and others (Table 1, line 136). The margin over prior methods is substantial.

3. **Comprehensive five-way ablation study.** The paper systematically ablates each component (replacing CNN with MLP, removing CNN, removing MP loss, removing AE, removing MP). Every removal degrades performance, and the results are reported across accuracy, precision, recall, F1, and AUC (Table 2, lines 220–285), providing evidence for each design choice.

4. **Fully unsupervised operation.** The model is trained on normal data only and requires no labeled anomalies, directly addressing the label-scarcity challenge highlighted in the introduction (line 126).

## Weaknesses

### Fatal
None.

### Major

1. **Section 3.1 ("CALCULATE OPTIMIZED-MP BY 1D-CNN") contains no textual description — only a figure placeholder.** The core technical question of how the Matrix Profile is computed from 1D-CNN feature maps is never answered. The paper states that subsequences are passed through a 1D-CNN to extract feature maps and "we subsequently compute the Matrix Profile based on these feature maps" (line 59), but the actual computation — what algorithm is used (e.g., STOMP, SCRIMP, or a learned approximation), what distance metric, whether z-normalization is applied, what "optimized" means, how the MP subsequence length relates to the CNN receptive field — is entirely absent. This is not a minor omission: the entire pipeline depends on this step. Without it, the method cannot be reproduced, and the efficiency claims ("optimized MP computation") cannot be evaluated. This is the most serious weakness in the paper.

2. **Evaluation protocol is critically underspecified.** The paper reports Precision, Recall, and F1-score but does not describe: (a) how the detection threshold τ is chosen (fixed across all 250 datasets? per-dataset? based on validation data?), (b) whether point-adjustment (the standard practice in TSAD evaluation on UCR, where a detection within a tolerance window around a labeled anomaly is counted as correct) is used, and (c) how hyperparameters are selected and validated per dataset. These gaps make the reported numbers difficult to interpret or compare against published results. The very high recall of LOF (98.80%, line 136) — a method with no temporal structure — further suggests the evaluation protocol may be lenient in ways that obscure method differences.

### Minor

3. **The softmax-weighted anomaly score is an unusual design choice with no justification.** The anomaly score is AS_i = softmax(p_i) · e_i, where softmax normalizes MP values across all subsequences in the test series (lines 105–111). Because softmax is a competitive normalization, if one subsequence has a high MP value (anomalous), its weight approaches 1 and all other weights approach 0, suppressing their reconstruction error signal. For UCR (one anomaly per test series) this may not harm performance, but the design is peculiar and the paper provides no analysis or ablation justifying why softmax is preferable to a simpler additive or multiplicative combination (e.g., AS_i = p_i + e_i or AS_i = p_i · e_i). This makes the anomaly score less principled than it should be.

4. **Efficiency claims are made but never substantiated.** The abstract and conclusion claim "computational efficiency" and "efficiently process large-scale datasets," and Section 2 states the aim to "optimize the MP computation to reduce costs" (line 32). However, the paper provides zero runtime measurements, no flop/s complexity analysis, and no training or inference time comparison against any baseline. Without evidence, these claims are speculative.

5. **Risk of representation collapse from MP loss minimization is not discussed.** Minimizing the mean MP distance among normal subsequences encourages a compact representation, but if pushed too far, the model could collapse all subsequences to a nearly identical feature vector — a trivial solution that would render anomalies undetectable. The reconstruction loss likely counteracts this collapse, but the paper does not discuss this tension, analyze feature geometry, or show that representations remain diverse.

### Trivial

6. **The dynamic λ schedule is mentioned but not specified.** The paper states λ is "dynamically increased during training" (line 94) and that adjustments prevent "gradient explosion," but no schedule, functional form, initial value, final value, or termination criterion is given. This detail is needed for reproducibility.

## Nice-to-Haves

- Provide a precise algorithm or pseudocode for the "optimized MP" computation from 1D-CNN features, and validate its correctness against exact MP (e.g., STOMP) on a small dataset.
- Specify and justify the threshold selection mechanism. Display precision-recall curves or threshold-vs-metric plots to clarify how thresholds are chosen across variants.
- Explicitly state whether point-adjustment is used, or discuss why a different evaluation protocol is followed.
- Include runtime measurements (training and inference) against at least 2–3 baselines (e.g., SCRIMP, LSTM-VAE) to support the efficiency claims.
- Discuss the softmax choice more carefully, or replace it with a simpler combination.

## Removed Points

These points from the reviewers were checked against the paper and removed:

- **"The MP loss is contradictory: minimizing it suppresses the signal anomaly detection requires."** This criticism misunderstands the training setup. The model is trained on *normal data only*. Minimizing MP distance among normal subsequences is correct — it makes normal representations compact so anomalies stand out at test time. There is no contradiction. (Source: line 126 confirms training data is normal only.)
- **"Figures stripped by parser."** These are formatting artifacts introduced by the PDF extraction pipeline, not author errors.
- **"The paper claims to handle more general cases (multiple anomalies)."** The paper evaluates only on UCR (single anomaly per test series) and makes no claim about handling multiple simultaneous anomalies.
- **Generic comments about missing appendix content.** The parser strips appendices; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a design tension that the paper does not address (softmax weighting suppressing multi-point signals, risk of MP-loss-induced representation collapse), but these are observations about the paper's gaps rather than new insights.

## Suggestions

1. **Write Section 3.1.** Describe explicitly how the Matrix Profile is computed from 1D-CNN feature maps — which algorithm, which distance metric, what subsequence length, and what "optimized" means. A short pseudocode block would suffice.
2. **Document the evaluation protocol.** State how τ is chosen, whether point-adjustment is used, and how hyperparameters are selected per dataset. Add a reference to the standard UCR evaluation protocol (Wu & Keogh, 2021) if it is followed.
3. **Justify or replace the softmax weighting.** Compare the current AS_i = softmax(p_i)·e_i against simpler alternatives (e.g., AS_i = p_i + e_i or AS_i = p_i · e_i) in an ablation or provide a synthetic experiment showing why the competitive normalization is beneficial.
4. **Add runtime measurements.** Report training time and inference latency for FMP-AE and 2–3 baselines (e.g., SCRIMP, LSTM-VAE, ADTransformer) to support the efficiency claims.
5. **Discuss representation collapse.** Explain why the reconstruction loss prevents the MP loss from collapsing representations, or show feature-space visualizations that confirm representations remain diverse.

## Score and Decision

**Overall assessment:** The paper proposes a genuinely novel combination of Matrix Profile loss and autoencoder reconstruction loss for time series anomaly detection, and the ablation study convincingly shows that both components matter. However, the paper has two structural gaps that prevent it from being accepted in its current form: (a) the core technical mechanism — how the Matrix Profile is computed from CNN feature maps — is entirely undescribed (Section 3.1 is empty prose), and (b) the evaluation protocol is critically underspecified, making the reported state-of-the-art numbers unverifiable. These are not minor clarifications; they are fundamental to assessing the validity and reproducibility of the contribution. The softmax weighting concern, though less severe, adds to the sense that key design decisions lack principled justification. Major revision addressing all major issues could make this a strong paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>