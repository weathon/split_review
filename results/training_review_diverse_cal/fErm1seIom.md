Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper proposes FMP-AE, an unsupervised anomaly detection model for univariate time series that combines a Matrix Profile (MP) loss with an autoencoder reconstruction loss. A 1D-CNN extracts feature maps from sliding-window subsequences; MP is computed from these features and its mean is used as a loss term alongside reconstruction MSE. The anomaly score weights reconstruction error by a softmax over MP values. Experiments on the 250-dataset UCR benchmark report an F1 of 86.79%, outperforming 14 baselines, and five ablation studies show each component contributes to performance.

## Strengths

- **Novel hybrid loss function with clear ablation evidence.** The paper's central idea—combining a Matrix-Profile-based loss with reconstruction loss—is sensible and supported by the ablation study (Table 2). Removing the MP loss drops F1 from 86.79% to 67.87%; removing the AE drops it to 40.12%. This systematic evidence credibly demonstrates that both terms contribute.

- **Strong empirical results on a large benchmark.** An F1 of 86.79% on 250 diverse UCR datasets (lengths 6,680–900,000) across medicine, biology, industry, and meteorology is a meaningful result. The model tops 14 baselines including THOC, OmniAnomaly, InterFusion, and ADTransformer on precision (81.03%) and F1.

- **Five controlled ablations that validate each design choice.** Replacing 1D-CNN with MLP (F1 drops to 74.92%), removing 1D-CNN entirely (F1 drops to 31.41%), removing AE (40.12%), removing MP (69.30%), and removing MP loss (67.87%)—each change produces a substantial degradation. This is the paper's strongest evidence.

## Weaknesses

### Major

- **MP computation is underspecified; the method cannot be reproduced.** The paper repeatedly states it "computes the Matrix Profile based on feature maps" extracted by a 1D-CNN (Section 3.2, line 59), but never specifies *how*. Is this an exact pairwise distance computation over CNN feature vectors? An approximation using STAMP, STOMP, or SCRIMP? What distance measure (Euclidean, cosine, Manhattan)? Section 3.1 ("CALCULATE OPTIMIZED-MP BY 1D-CNN") consists of an image placeholder with no textual algorithmic detail. The central technical claim—a novel loss that integrates MP with reconstruction—cannot be evaluated or replicated without this information.

- **No network architecture or hyperparameter details.** The paper provides zero architectural specifications for the 1D-CNN or autoencoder: no number of layers, kernel sizes, strides, latent dimension, activation functions, optimizer, learning rate, or batch size. The window length \(k\)—a critical parameter that determines the MP subsequence scale—is never stated. Without these, the claimed results cannot be reproduced independently.

- **Key training mechanism (\(\lambda\) schedule) unspecified.** The hyperparameter \(\lambda\) that balances reconstruction and MP loss is described as "dynamically increased during training" (line 94), and the paper states that "prioritizing local anomaly detection too early may lead the model to converge to local minima" (line 94). Yet no schedule, rule, initial value, or final value for \(\lambda\) is given. The behavior of the proposed method depends critically on this schedule, and it cannot be replicated in its absence.

- **Evaluation transparency gaps undermine the claimed SOTA.** Several missing details prevent proper assessment of the reported F1 of 86.79%:
  - **Aggregation method not specified.** It is unclear whether Table 1 reports macro-average, micro-average, median, or some other aggregation across the 250 UCR datasets. These choices produce different numbers, especially on imbalanced data.
  - **Threshold selection for baselines not described.** F1 depends on the threshold; without a shared, principled thresholding protocol (e.g., maximizing F1 on a validation split), the comparison is unreliable.
  - **AUC not reported for baselines.** AUC is threshold-agnostic and avoids the above confound, but Table 1 only shows Precision, Recall, and F1. AUC is reported only for the proposed model (Figure 6) and ablations (Figure 7).
  - **Baseline adaptation details missing.** Several baselines (OmniAnomaly, InterFusion, GDN) were originally designed for multivariate time series. How they were adapted to univariate UCR data is not described, which could affect their relative performance.
  - **No runtime measurements.** The paper repeatedly claims computational efficiency (abstract, line 4; conclusion, line 295), but provides zero runtime or complexity data.

### Minor

- **Loss normalization is a constant scaling factor with unexplained purpose.** The normalized MP loss \(\tilde{\mathcal{L}}_{\mathrm{MP}} = \mathcal{L}_{\mathrm{MP}} / \bar{p}\) divides by \(\bar{p}\), the global mean of batch-wise mean MP across all batches (lines 70–76). If computed once, this is a fixed scalar—it does not change the optimization direction. If recomputed during training, the paper does not say so. Either way, its purpose is not explained.

- **Abstract promises metrics not presented in main comparison.** The abstract states the model demonstrates "superior performance across multiple metrics, including accuracy, precision, recall, F1-score, and AUC." However, Table 1 does not report accuracy or AUC for any method. Accuracy values appear only in the ablation text (Table 2 discussion).

- **Anomaly score heuristic lacks justification.** The score \(AS_i = w_i \cdot e_i\) uses a softmax over MP values to weight reconstruction error. As the reviewer notes, the exponential in softmax can produce extreme weights when one MP value dominates, effectively suppressing reconstruction error from other positions. No theoretical or empirical justification is given for this design over simpler alternatives (raw reconstruction error, sum, max, or unweighted combination).

### Trivial

- The paper does not specify whether point-level or segment-level evaluation is used for the UCR datasets, which matters because UCR contains collective/contextual anomalies where point-level detection is notoriously hard.

## Nice-to-Haves

- A sensitivity analysis of the window length \(k\) and the \(\lambda\) scheduling function would substantially strengthen the paper.
- A comparison using AUC for all baselines (in addition to F1) would eliminate threshold-selection concerns and make the comparison more reliable.
- Reporting per-dataset result distributions (e.g., box plots of F1 across the 250 datasets) rather than a single aggregate number would be informative.

## Removed Points

- The harsh reviewer's point about "the MP+1D-CNN achieving highest AUC, which the paper acknowledges but then dismisses" is retained in spirit but downgraded: the paper does self-report this finding (line 285) and offers an explanation. It is a valid observation worth deeper analysis but not a weakness per se, since the paper's stated goal is balanced precision-recall, not pure ranking performance.
- The strength about "Efficient MP computation via 1D-CNN" from the Strength Finder is removed because no runtime data is provided to substantiate the efficiency claim, and the MP computation algorithm is not specified—the weakness here overrides the claimed strength.
- The strength about "Dynamic λ adjustment" from the Strength Finder is removed because the λ schedule is not specified, contradicting the notion that this is a verified strength.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the critical gap between claiming a hybrid MP-deep learning method and actually specifying it, which is a recurring issue in this area.

## Suggestions

1. **Specify the MP computation algorithm.** State explicitly: (a) the distance measure used on 1D-CNN feature vectors, (b) whether the computation is exact (pairwise) or approximate (and if approximate, which algorithm), and (c) its time complexity.
2. **Provide full architecture and hyperparameter details.** Include number of layers, kernel sizes, strides, latent dimension, activations, optimizer, learning rate, batch size, and the window length \(k\) (per-dataset or a principled default).
3. **Specify the λ scheduling mechanism.** Provide the initial value, growth function (linear, step, plateau), and final value.
4. **Report AUC for all baselines** alongside F1 to remove threshold-selection confounds. Describe the thresholding protocol used for F1 computation.
5. **Clarify the evaluation aggregation** (macro-average, micro-average, or per-dataset statistics) and whether point-adjust or range-based AUC was used.
6. **Add runtime or complexity analysis** to substantiate the efficiency claims, or remove those claims.

## Score and Decision

The paper presents a reasonable high-level idea and empirically demonstrates it on a large benchmark with informative ablations. However, the method is insufficiently specified for replication: the MP computation algorithm, network architecture, hyperparameters, and λ scheduling are all absent. The evaluation comparison lacks crucial transparency (aggregation method, threshold selection protocol, baseline adaptation). These are not minor omissions—they prevent independent verification of the claimed SOTA results and assessment of the actual contribution. Substantial revision is required before the paper can be fairly evaluated.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>