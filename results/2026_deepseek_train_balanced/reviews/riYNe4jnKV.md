## Summary

The paper proposes Calibrated Loss, a framework that reduces the variance of standard evaluation metrics (Log Loss, Quadratic Loss) by calibrating the bias term of model predictions on a held-out portion of the test set before computing the metric on the remaining data. The motivation is sound: deep learning pipelines are often run only once due to computational constraints, and metric variance from training randomness can mask real improvements. The method is simple, computationally cheap, and supported by a theoretical analysis (under linear regression) and experiments on CTR prediction (Avazu) and image classification (CIFAR10).

## Strengths

- **Theoretical variance-reduction guarantee (Theorem 4.1, Corollary 4.2):** The paper proves that for linear regression with jointly Gaussian features, the Calibrated Quadratic Loss has strictly smaller variance than the vanilla Quadratic Loss after scaling by (1+1/n), while preserving mean ordering. This is a non-trivial mathematical result that directly supports the paper's central intuition.

- **Consistent accuracy improvements across diverse pipeline comparisons on Avazu (Tables 1, 3, 5, 6):** Calibrated Log Loss achieves higher accuracy than vanilla Log Loss for every tested comparison — different feature sets, model architectures (DCN, DeepFM, FNN, DCNMix), hyperparameters (batch normalization, dropout, layer size, regularization weight), and regularization levels. The breadth of validation across multiple axes is a genuine strength.

- **Metric inconsistency correction on CIFAR10 (Table 7, line 278):** The paper identifies cases where vanilla Log Loss yields accuracy below 50% even though pipeline A is genuinely better by classification accuracy — meaning Log Loss contradicts the ground-truth ranking. Calibrated Log Loss mitigates this. This finding goes beyond simple variance reduction to demonstrate that calibration can correct ranking distortions caused by miscalibration.

- **The method is simple, practical, and computationally cheap:** Calibrated Loss requires no retraining — only splitting the existing test set and solving a one-dimensional optimization (finding the bias shift c). This makes it directly applicable in resource-constrained industrial settings where multiple training runs are infeasible.

## Weaknesses

### Major

- **Empty synthetic data section (Section 5.2, line 195):** The paper advertises "extensive experimental validations" using a "synthetic dataset" as Contribution 3, but Section 5.2 contains exactly one sentence with no results, tables, figures, or comparisons. This is not a formatting artifact — the content is simply absent. The synthetic setting would have been the cleanest test of the method's mechanism, and its absence is a significant gap in the experimental evidence presented.

- **Inconsistent ground truth definitions across experiments without discussion (lines 206 vs. 268):** For the Avazu experiments, the paper states: "we use 'Log Loss' as our ground truth metric to determine the performance rank of different pipelines." For CIFAR10: "we use 'Classification Accuracy' as our ground truth metric." These are different ground truths, and the paper neither acknowledges this shift nor justifies it. The Avazu experiments largely show that a variance-reduced Log Loss better tracks Log Loss's own ordering — which is consistent but less interesting than the CIFAR10 case where Calibrated Log Loss better predicts an accuracy-based ordering. By not distinguishing these settings, the paper conflates two different claims under a single narrative.

- **The calibrated metric is evaluated on a smaller test set than the vanilla metric, creating an uncontrolled confound (lines 202, 264):** Calibrated Log Loss splits the test set: a portion is used for calibration and the remainder for evaluation. For Avazu, 2% of data is used for calibration and 18% for evaluation (vanilla presumably uses the full 20%). For CIFAR10, 20% for calibration and 80% for evaluation (vanilla presumably uses 100%). Using fewer test samples increases the variance of the metric estimate, which counteracts the variance reduction from calibration. The paper never reports what vanilla Log Loss yields when computed on the same reduced test subset, nor does it analyze the net effect of the trade-off. Without this control, the reported variance reductions (16–40%) may be either over- or understated.

### Minor

- **The theory analyzes Calibrated Quadratic Loss under linear regression, while the proposed method is Calibrated Log Loss for classification (line 129):** The paper openly acknowledges this gap, stating the choice is due to analytical simplicity. However, this means the theoretical guarantee does not directly apply to the method being proposed. The theory supports the intuition but does not constitute a direct proof for the actual proposal, and the nonlinearities of logistic regression and neural networks could alter the relationship between bias calibration and variance reduction.

- **Experiments do not resample training data (line 206):** The paper states that in neural network experiments, training data is not resampled across runs — only initialization seeds and data ordering vary. The problem setting (Section 2) explicitly includes data randomness as a source of variance, but the experiments only cover intrinsic training randomness. The paper acknowledges this but does not discuss what portion of total variance is captured or how this affects generalization of the findings.

### Trivial

- Several tables referenced in the text (e.g., Tables 12, 13 at lines 247, 257) appear to be missing from the parsed text — likely a parser artifact, but in the original submission these should be verified to exist.

## Nice-to-Haves

- A sensitivity analysis of the test-validation split ratio (2% vs. 20% across datasets) would help readers understand how the calibration/evaluation trade-off behaves.
- A control experiment reporting vanilla Log Loss on the same reduced test subset would disentangle the effect of calibration from the effect of using less data.
- A variance decomposition showing how much of the total variance comes from the bias term vs. other sources would make the mechanism more transparent and help predict when the method will help.
- A discussion of boundary conditions (e.g., when models are trained to convergence and bias variance is already small) would strengthen the paper's practical guidance.

## Removed Points

- *Criticism about the theoretical result not connecting to the proposed method being a "critical issue":* Downgraded to Minor. The paper is transparent about the theory's scope (line 129) and uses it as intuition support, not proof for the exact setting.
- *Criticism about "Table 12, 13" references being missing:* These may be parser artifacts. Trivial enough to not merit inclusion.
- *Criticism about tables being embedded as images:* This is a parser artifact, not an author error.
- *Strength about "the paper addresses an important problem":* Generic; removed. The sustained strengths are concrete enough.
- *Strength claims that conflict with verified weaknesses:* The strength about "inconsistent ground truth" being an inconsistency correction on CIFAR10 is retained as it is specific and factual, but the broader strength about the evaluation framework being well-designed is tempered by the weaknesses above.
- *Criticism about the paper lacking comparison to multiple-run baselines or statistical testing procedures:* Weakened to Nice-to-Have; requesting additional baselines beyond the paper's stated single-run scope is scope creep.

## Novel Insights

The most interesting observation emerging from this review — one that goes beyond the paper's own framing — is the tension between the paper's theoretical framing (variance reduction) and its empirical evidence. The CIFAR10 results (Table 7) show Calibrated Log Loss not just reducing variance, but actually *correcting ranking inconsistencies* where Log Loss contradicts accuracy-based rankings. This suggests the method's value may extend beyond variance reduction per se: by removing bias-related distortions, Calibrated Loss may serve as a better proxy for a fundamentally different notion of model quality (e.g., accuracy or calibration) even in the single-run setting. The paper does not develop this insight, instead framing everything through the lens of variance reduction, but the evidence hints at a richer story that future work could explore.

## Suggestions

1. **Fill Section 5.2** with the synthetic data results. This is the single highest-impact change the authors can make, as it directly addresses a claimed contribution that is currently absent.
2. **Run a control experiment** where vanilla Log Loss is computed on the same remaining-test subset used for Calibrated Log Loss. Report this alongside the existing results to isolate the effect of calibration from the effect of test-set size.
3. **Explicitly discuss the ground truth discrepancy** between the Avazu and CIFAR10 experiments. Either unify the ground truth definition across experiments, or transparently frame the CIFAR10 results as a separate claim about Calibrated Log Loss being a better proxy for accuracy-based rankings.
4. **Add a brief analysis of when the method might not help** (e.g., when models are trained to convergence and bias variance is small, or when the calibration split is too small relative to noise).
5. **Consider reporting variance decomposition** to show empirically how much variance is attributable to the bias term versus other sources.

## Score and Decision

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>