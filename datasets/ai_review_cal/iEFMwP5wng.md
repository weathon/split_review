- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper makes the empirical finding that test-time adapted (TTAed) models exhibit substantially stronger agreement-on-the-line (AGL) and accuracy-on-the-line (ACL) phenomena than their vanilla counterparts, including on distribution shifts where vanilla models fail to show these trends. The paper leverages this observation to enable three reliability tools for TTA without OOD labels: (1) OOD accuracy estimation, (2) unsupervised calibration via temperature scaling matched to estimated accuracy, and (3) hyperparameter selection via best ID accuracy. Experiments cover 7 TTA methods, multiple architectures, and diverse distribution shifts.

## Strengths

- **Novel and well-supported empirical finding.** The paper demonstrates that TTA strengthens AGL/ACL across diverse settings, with quantitative evidence (e.g., R² on CIFAR10-C Gaussian Noise improves from 0.16→0.95 for SHOT and 0.00→0.95 for ETA, Figure 1, line 57). This holds even on shifts where TTA degrades accuracy (CIFAR10.1, ImageNetV2), making the finding robust and practically relevant.

- **Accuracy estimation on TTAed models achieves substantially lower error than vanilla alternatives.** Table 1 reports e.g. CIFAR10-C: vanilla ALine-D MAE 5.17% vs. TENT ALine-D 0.53%, consistently outperforming prior baselines (ATC, DOC-feat, average confidence) across CIFAR100-C, ImageNet-C, and ImageNet-R (line 81).

- **Unsupervised calibration reduces ECE to near-oracle levels.** The temperature-scaling variant matches average confidence to estimated accuracy, and Table 3 shows it closes the gap to the oracle lower-bound across multiple TTA methods. On CIFAR100-C with TENT, ECE drops from 11.70 (uncalibrated) to 5.97 (proposed), vs. oracle 4.27 (Table 3 caption).

- **Forecasting TTA improvement/degradation with no OOD labels.** Table 2 shows that estimated improvement/degradation direction matches ground truth on all 8 evaluated shifts, including cases where TTA hurts (CIFAR10.1, ImageNetV2), enabling practitioners to decide when not to adapt (lines 88–91).

- **Comprehensive experimental scope.** The study covers 7 TTA baselines (BN Adapt, SHOT, TTT, TENT, ConjPL, ETA, SAR), multiple architectures (ResNet, ResNext, VGG, GoogLeNet, DenseNet, MobileNet), and diverse shifts (synthetic corruptions, dataset reproductions, real-world shifts like ImageNet-R, FMoW-WILDS) (Section 2.1).

- **Honest limitation analysis.** The paper identifies and discusses a clear failure case (TTT with varying learning rates, where ACL becomes negative) and shows that hyperparameter selection correspondingly fails (large MAE in Table 4, Figure 4, Section 5).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Imprecise "no labels" claim.** The abstract and introduction state methods work "without any labeled data at all" (line 21). However, ALine-S accuracy estimation requires ID labels to compute ID accuracy, and the hyperparameter selection strategy uses ID accuracy (which also requires ID labels). The ALine-D variant is truly label-free, and the conclusion acknowledges that "access to ID test data (and its labels for ACL) is required" (line 161), but the main presentation conflates label requirements. This is a precision issue — the core contributions remain valid — but the framing should be corrected to distinguish which methods require ID labels and which do not.

- **Hyperparameter selection lacks comparison to label-free baselines.** The paper validates hyperparameter selection (best ID accuracy → best OOD accuracy) against the oracle (ground-truth labels), but does not compare against other label-free strategies (e.g., lowest OOD entropy, highest ID confidence). The paper acknowledges this strategy follows from prior work (Miller et al., 2021; Wenzel et al., 2022, line 125), and the results are strong, but the absence of alternative baselines makes it hard to assess whether this is a meaningful advance over simpler heuristics.

- **Calibration method's sensitivity to accuracy estimation errors is unexamined.** The calibration method (Section 3.2) sets temperature by matching average confidence to estimated accuracy. When accuracy estimation is poor (e.g., on the TTT failure case or shifts where AGL is weaker), the calibration would inherit those errors, but this failure mode is not discussed or analyzed.

- **Missing experimental details.** The paper does not report the number of model checkpoints or hyperparameter settings used to generate scatter plots and R² values (Section 2.2). Confidence intervals or variance across seeds/runs are not provided for MAE and ECE results, even though TTA can be sensitive to stochastic factors.

- **Potential confound in vanilla vs. TTA model-set comparison.** In Table 1, the vanilla models are the source models before adaptation, while the TTAed models are adapted variants — these are different model sets with potentially different sizes. The paper does not control for or discuss whether the improved AGL/ACL arises partly from having more models in the TTA set.

### Trivial

None.

## Nice-to-Haves

- A broader investigation of when AGL/ACL is strengthened vs. when it breaks (beyond the TTT learning rate case), such as across severity levels or TTA methods with different update strategies, would help practitioners understand scope of applicability.
- Comparing hyperparameter selection against label-free heuristics (e.g., minimum OOD entropy) would strengthen the third contribution.
- Reporting variance across random seeds in accuracy estimation and calibration results.

## Removed Points

- **"'Stronger' used qualitatively"** (Harsh Critic): The paper provides quantitative R² values (0.16→0.95, 0.00→0.95). The criticism is factually incorrect.
- **"Dismissive of existing work on calibration in TTA"** (Harsh Critic): The paper cites Chen et al. 2022 and Rusak et al. 2022; the claim is about "little work effectively addressing" the shortcomings, not that no work exists. Overstated criticism.
- **"R² only for few settings"** (Harsh Critic): The paper reports R² across Figures 1–3 for multiple settings; this is adequate for an empirical paper illustrating a phenomenon.
- **"Algorithm 1 missing"** (Harsh Critic): Appendix content stripped by parser; not an author error.
- **"Oracle lower-bound not zero"** (Harsh Critic): The paper never claims it should be zero; this is an irrelevant observation.
- **"Hyperparameter selection is not a new contribution"** (Harsh Critic): The paper transparently cites prior work (Miller et al., 2021; Wenzel et al., 2022) and frames this as a novel application to TTA. The contribution is in validation and application, not a fundamentally new method.
- **"Calibration depends on accuracy estimation"** (Harsh Critic): The method is explicitly defined using estimated accuracy; this is not a hidden dependency but the method itself. The valid sub-point about failure-case analysis is retained in Minor.

## Novel Insights

None beyond the paper's own contributions. The two reviewers largely converge: the harsh critic identifies legitimate precision issues but overstates several of them, while the strength finder correctly identifies the paper's core empirical and practical contributions. Neither review surfaces a genuinely novel observation beyond what the paper itself articulates.

## Suggestions

1. **Correct the "without any labeled data" framing.** Explicitly state that ALine-S requires ID labels (for ID accuracy) while ALine-D is fully label-free; the calibration method (using estimated accuracy) and hyperparameter selection (using ID accuracy) should be clearly attributed to their respective label requirements.

2. **Add at least one label-free baseline for hyperparameter selection.** Compare against selecting the model with lowest OOD entropy or highest average ID confidence to validate that the ACL-based approach outperforms simple heuristics.

3. **Discuss failure propagation in calibration.** Add a paragraph analyzing how accuracy estimation errors affect the calibration method, particularly on shifts where AGL is weaker or in the TTT failure case.
