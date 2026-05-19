- Decision: Reject
- Avg Score: 2.00
- Scores: 3, 3, 1, 1
Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper applies a standard 1D CNN to single-channel EEG signals for binary classification of major depressive disorder (MDD). Using the Mumtaz et al. (2017) dataset (30 MDD, 28 control subjects, 5-minute eyes-closed resting-state EEG), the authors segment recordings into 10-second non-overlapping windows, tune hyperparameters (kernel size, pooling layers, threshold), and evaluate via leave-one-subject-out (LOSO) cross-validation. They test five single channels from different brain regions and report 88% accuracy for channels C3, Fp1, and O1. The main finding is that single-channel accuracy matches or slightly exceeds the 10-channel 87.5% result previously reported on the same dataset by Rafiei et al. (2022).

## Strengths

- **Subject-independent evaluation via LOSO cross-validation (Section 2.7)**: The paper uses leave-one-subject-out evaluation, which prevents any data leakage between training and test sets at the subject level. This is a more rigorous protocol than k-fold cross-validation that mixes segments from the same subject across folds, which many prior deep learning EEG studies (e.g., Acharya et al. 2018, Ay et al. 2019) have used.

- **Meaningful comparison with a multi-channel baseline on the same dataset (Discussion)**: The paper directly compares its single-channel results (88% on C3, Fp1, O1) with the 10-channel InceptionTime result from Rafiei et al. (2022) (87.5% on the same dataset). Achieving comparable accuracy with one channel instead of ten provides concrete evidence that minimal-electrode MDD detection is feasible, directly supporting the paper's stated contribution.

- **Channel-specific analysis across multiple brain regions (Section 3, Figure 5)**: The paper evaluates five single channels spanning frontal (Fp1), central (C3), temporal (T4), occipital (O1), and parietal (P3) regions. Finding that frontal channel Fp1 (forehead location) achieves 88% accuracy is practically relevant for wearable deployment, since forehead electrodes are more convenient and comfortable than scalp electrodes requiring hair preparation.

- **Systematic hyperparameter grid search (Section 2.5, Figure 4)**: The authors perform a grid search over kernel sizes (3–31), number of pooling layers (2–5), and decision thresholds (10%–90%), demonstrating that the chosen architecture and hyperparameters were empirically tuned rather than arbitrary.

## Weaknesses

### Fatal

None.

### Major

1. **Segment-level hyperparameter tuning introduces potential data leakage (Section 2.5)**:
   The paper states: "we employ hyper-parameter tuning using the 80:20 training/validation split of the total segments" (line 73) for kernel size and number of pooling layers. Since a 5-minute recording yields ~30 segments per subject, splitting *segments* rather than *subjects* means segments from the same subject can appear in both training and validation sets. This allows the hyperparameter search to exploit within-subject correlations rather than optimizing for subject-level generalization. While the final LOSO evaluation is clean and the reported results are not inflated, the chosen hyperparameters (kernel size 21, 3 pooling layers) may be suboptimal for cross-subject performance. The decision threshold was tuned using a proper subject-wise split, but the inconsistency between the two tuning protocols is not explained or justified. This casts uncertainty over whether the reported 88% reflects the best achievable subject-level performance.

2. **Only accuracy is reported; no clinical metrics provided**:
   The paper reports only accuracy (Section 2.8, Section 3). For a clinical screening tool, sensitivity, specificity, precision, recall, F1-score, and AUC are essential. Without these, it is impossible to assess the model's practical utility — for example, the false-negative rate (missed MDD cases) or false-positive rate (unnecessary referrals). The paper acknowledges that decision threshold affects the tradeoff but never actually reports the sensitivity/specificity at the chosen threshold. With 58 subjects and 88% accuracy (~51/58 correct), even basic confidence intervals would be wide (~77–95% at 95% confidence), making the result less precise than implied.

3. **No baselines or comparisons with simpler methods**:
   The paper includes no baselines — not even a simple classifier (e.g., logistic regression on band-power features, SVM on raw features, or a k-nearest neighbor baseline) on the same data. The only comparison is with Rafiei et al. (2022), which is helpful but not a substitute for within-study baselines. Without a baseline, we cannot tell whether the CNN is learning meaningful EEG patterns or simply exploiting dataset artifacts; nor can we assess whether deep learning adds value over classical feature-based approaches on this dataset. A direct comparison with a multi-channel model using the full 19-channel data on the same dataset would also help quantify the information loss from channel reduction.

### Minor

4. **Standard CNN architecture with limited novelty**:
   The model is a conventional 1D CNN with three convolutional layers (64, 128, 256 filters, kernel size 21, ReLU, max pooling). Similar architectures have been standard in EEG classification for years. The paper's contribution is primarily empirical (demonstrating that single-channel EEG can work for this specific dataset) rather than methodological. This is not a flaw per se, but it limits the paper's significance: there is no analysis of *why* certain channels perform better, no principled channel selection method, and no architectural innovation that might generalize to other settings.

5. **Hyperparameters tuned only on channel C3, then applied to all other channels without justification**:
   The hyperparameter grid search was performed exclusively on channel C3 data (Section 3, "Figure 4 presents the variation of classification accuracy using the CNN model with channel C3 EEG data"). The optimal kernel size (21) and pooling layers (3) were then used for all other channels (Fp1, T4, O1, P3) without any validation that these hyperparameters transfer across brain regions. Different brain regions produce signals with different spectral and temporal characteristics, so the optimal architecture may differ per channel.

6. **No comparison with the full 19-channel set**:
   The paper tests only five pre-selected channels and does not compare single-channel performance against using all 19 channels on the same dataset. Such a comparison would directly quantify the information loss from channel reduction and could help identify whether the best single channel captures most of the discriminative information present in the full montage.

7. **Small dataset with limited demographic diversity**:
   The dataset contains 58 subjects (30 MDD, 28 control) from a single hospital in Malaysia (HUSM). The authors do not discuss potential limitations to generalizability due to demographic homogeneity, age range (22–53), or the specific clinical setting. The results should be interpreted as preliminary evidence rather than a validated clinical tool.

8. **Spectral analysis (Figure 6) is not tied to the CNN's decision process**:
   The band-power analysis shows differences between MDD and non-MDD subjects, but there is no quantitative link — no feature importance analysis, ablation, or explanation — connecting these spectral differences to what the CNN actually learns. The paper acknowledges this ("requires further investigation," line 141) but does not address the gap.

### Trivial

9. **Threshold notation inconsistency**: The optimal threshold is reported as "0.6" (line 110), but the search range is described as "10–100% with 10% step" (line 76), making it unclear whether 0.6 means 60% or a continuous probability threshold of 0.6. Given the search range, 60% is likely intended, but the notation should be consistent.

10. **"Number of parameters 9, 39, 265" appears garbled** (line 133): This likely means ~9.39 million or similar, but the formatting is broken. The intended number should be stated clearly.

## Nice-to-Haves

- A subject-level confusion matrix or per-subject accuracy breakdown would strengthen confidence in the results and show consistency across individuals.
- Including confidence intervals or standard deviations across LOSO folds would better characterize result precision. With 58 subjects, accuracy of 88% has a ~95% CI spanning roughly 77–95%.
- Reporting computational cost (inference time, model size) would directly support the wearable motivation.
- Feature attribution or saliency maps linking CNN decisions to specific frequency bands would connect the spectral analysis (Figure 6) to the model's behavior.

## Removed Points

These points were flagged by reviewers but are removed or demoted per the filtering rules:

- *"Missing training details (optimizer, learning rate, batch size, weight initialization, dropout)"* — Removed per hard rules: nitpicks about undisclosed hyperparameters and trivial implementation details are excluded.
- *"No analysis of computational cost"* — The paper does mention model parameters (line 133, albeit garbled). This is a minor omission but better placed in Nice-to-Haves.
- *"Related work does not critically discuss limitations of prior studies"* — The paper does note that Khan et al. (2022) achieved 100% accuracy and states "further assessments are needed to validate these findings" (line 14), which is an appropriate caveat.
- *"Figure 4 should show error bars"* — The tuning used a single 80:20 split (not cross-validation), so error bars across folds are not applicable in the same way.
- *"Threshold tuned on single 80:20 split rather than fold-wise"* — This is a valid concern, but it is absorbed into weakness #1 above (the broader inconsistency in tuning protocols).
- *Strength about "Systematic hyperparameter optimization"* — Partially undermined by the segment-level split issue (Weakness #1). The fact that a grid search was performed is still a positive, but the methodology concern tempers its strength.

## Novel Insights

None beyond the paper's own contributions. The harsh critic raised a valid methodological concern (segment-level vs. subject-level tuning) that is not discussed in the paper itself. Beyond that, the reviews did not surface any unexpected insight that the paper misses.

## Suggestions

1. **Retune hyperparameters using subject-wise cross-validation** — Hold out subjects rather than segments when selecting kernel size and pooling layers. If the current architecture is confirmed optimal under subject-wise tuning, the results are strengthened; if different hyperparameters are found, report both for comparison.

2. **Add at least two baselines** — (a) a simple classifier trained on band-power features (e.g., logistic regression or SVM) to isolate the benefit of deep learning, and (b) the same CNN trained on all 19 channels (or the 10 channels from Rafiei et al.) to quantify the information loss from using a single channel.

3. **Report sensitivity, specificity, F1-score, and AUC** alongside accuracy. Since the decision threshold (0.6/60%) was tuned, the paper should report the operating characteristics at that threshold. A brief ROC analysis would also be informative.

4. **Clarify the tuning protocol inconsistency** — Explain why kernel size and pooling layers were tuned on a segment-level split while the threshold used a subject-level split, and justify why this is acceptable (or fix it).

5. **Add subject-level results** — A confusion matrix or per-subject accuracy breakdown would demonstrate consistency across individuals and build confidence in the 88% aggregate figure.
