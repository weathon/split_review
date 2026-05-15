Now I have all the verification I need. Let me produce the consolidated review.

## Summary

This paper investigates the relationship between effective dimensionality — a Hessian eigenspectrum-based complexity metric — and adversarial robustness in image classifiers. Across 20+ models (ResNet, ShuffleNet, YOLO, VGG, MobileNet, RepVGG), three datasets (CIFAR-10/100, ImageNet), and three attack types (AutoAttack, PGD, Gaussian noise), the authors find an inverse correlation: models with lower effective dimensionality tend to be more robust. They further show that adversarial training consistently reduces effective dimensionality (by up to 31.3% for WRN34 with AWP+ED), and that this reduction follows a roughly linear trend with improved robustness (R² ≥ 0.73, ~5.5% relative performance gain per 10-point effdim drop).

## Strengths

- **Large-scale empirical scope spanning commercial architectures.** The paper tests 20+ models from 6 architecture families across 3 datasets with 3 attack types at multiple perturbation budgets. This goes well beyond prior work on effective dimensionality, which focused on small models. Production-relevant architectures (YOLOv8 variants up to x-cls, ResNet-101) are included.

- **Consistent inverse trend across diverse experimental conditions.** Despite architecture- and dataset-specific variation, the broad pattern — lower effective dimensionality associated with higher relative robustness — holds across nearly all combinations of model family, dataset, and attack method, strengthening the case that this is a genuine empirical regularity.

- **Adversarial training experiments with quantified reductions.** The finding that adversarial training methods (AT, TRADES, MART, AWP, AWP+ED) consistently reduce effective dimensionality, and that the reduction correlates linearly with improved robustness (R² ≥ 0.73 for all three architectures), is the cleanest evidence in the paper. The quantified slope (~5.5% relative performance gain per 10-point effdim drop) is practically actionable.

- **Outlier analysis partially separates effdim from parameter count.** The paper identifies ResNet on ImageNet and VGG on CIFAR as outliers in the effdim-vs-parameter-count plot (Figure 1) and notes that their robustness still follows the effdim trend (§4.3). This provides some evidence that effective dimensionality captures predictive signal beyond what parameter count alone provides, since these outliers deviate from the parameter-count trend.

## Weaknesses

### Fatal

None.

### Major

- **The computation of effective dimensionality is critically underspecified, threatening reproducibility and validity.** The paper defines effective dimensionality in terms of the Hessian eigenspectrum on test data (§2.3) and states that "a slightly modified version of the code provided by Maddox et al." was used (§3), but provides no details on: (a) the number of test examples used (full test set or subset?), (b) how the Hessian is approximated (Lanczos? exact? stochastic sub-sampling?), (c) the number of eigenvalues computed for models up to ~68M parameters, (d) convergence criteria, (e) computational budget, or (f) the value of the regularization parameter *z* on which effective dimensionality depends (only "z > 0" is stated). Scaling Hessian-based metrics from small models (where Maddox et al. validated them) to ResNet-101 and YOLOv8x on ImageNet is non-trivial, and without these details the core quantity on which all results rest cannot be independently verified or reproduced. This is the single most important issue to address.

- **The paper does not adequately control for the model-size confound, limiting support for the claim that effdim is "more nuanced and effective than parameter count."** The paper acknowledges (§4.2) that within a model class, larger models are more robust, and Figure 1 shows effective dimensionality generally decreases with parameter count. The paper never performs a controlled comparison (e.g., models with similar parameter counts but different effective dimensionalities, or partial correlation analysis) to show that effdim explains robustness variance beyond what parameter count already captures. The outlier analysis (ResNet on ImageNet, VGG on CIFAR) partially addresses this by showing cases where effdim and parameter count give different predictions and effdim tracks robustness better, but this is a handful of data points. The paper's central comparative claim is not commensurate with the experimental design used to support it.

### Minor

- **The "near-linear inverse relationship" claim is stronger than the evidence for the main results.** For the primary results (Figure 2), the paper provides no correlation coefficients, R² values, or error bars. The paper itself acknowledges "inconsistencies" (PGD on CIFAR), "outliers" (ResNet on ImageNet, VGG on CIFAR), and "model-specific variations." Calling this a "near-linear" relationship is overclaiming given the admitted deviations. (The adversarial training experiments are better supported with R² ≥ 0.73, but even there outliers are removed without justification — "mainly poorly pre-trained models" — and the specific removed points are not identified.)

- **The relative accuracy metric (p*/p) is defensible but the paper should report absolute clean and robust accuracies alongside it.** The paper provides a rationale for relative accuracy (line 82: measuring relative degradation rather than absolute drop), but not reporting clean accuracy *p* and absolute robust accuracy *p\** for each model makes it impossible to assess whether the effdim-robustness correlation is driven by the choice of metric. The concern that lower-effdim models might also have lower clean accuracy (which could artifactually produce the inverse correlation) is not addressed.

- **The paper claims effective dimensionality is "more nuanced and effective than... previously-tested measures" (abstract, conclusion) but does not experimentally compare against any of them.** The paper cites Kim et al. (2023) showing that boundary thickness, flatness, and Lipschitzness are inadequate, but never computes these metrics for the same models to demonstrate that effdim offers superior predictive power. The comparative claim is unsupported by direct evidence.

### Trivial

- The limitation section states the paper was "unable to test larger more complex models" (§5), which is oddly worded given the paper tests up to ResNet-101 and YOLOv8x-cls (both reasonably large). The models tested are more accurately described as production-scale, not "smaller."

- The adversarial training experiments (§3, §4.4) do not explicitly state which dataset is used (the MAIR framework cited is a CIFAR-10 benchmark, so it is implied, but should be stated).

- The regularization parameter *z* in the effective dimensionality formula is not specified even as a chosen value; without this the metric is not well-defined.

## Nice-to-Haves

- A controlled experiment comparing models with similar parameter counts but different effective dimensionalities (e.g., same architecture trained with different weight decay or data augmentations) would strengthen the claim that effdim adds information beyond parameter count.
- Comparison against at least one baseline complexity metric (e.g., flatness or boundary thickness) on the same models would substantiate the comparative claim.
- An ablation study on the *z* regularization parameter showing results are robust to its choice.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper never reports R² for main results"** — retained as a minor weakness but the critic's framing as a fatal omission is overwrought; the adversarial training experiments do report R². Merged above.
- **"Effective dimensionality-vs-size outliers (ResNet/ImageNet, VGG/CIFAR) are unexplained and undermine the claim"** — removed because the paper actually uses these outliers *as evidence* that effdim tracks robustness where parameter count fails (§4.1, §4.3). The paper notes this is an open question for future work, which is honest.
- **"The MAIR framework is mentioned but not cited"** — removed because the MAIR framework *is* cited (kim2023fantastic). The dataset is implicitly CIFAR-10 through the MAIR benchmark, though this should be explicit.
- **Formatting/style nitpicks and speculative reproducibility concerns** about "cannot be independently verified" regarding cited works — removed per hard rules.
- **"Missing related works"** — removed per hard rules (cannot confirm existence of missing references without external sources).
- **"Missing appendix"** — removed per hard rules (parser strips appendices).

## Novel Insights

None beyond the paper's own contributions. The key empirical finding — a consistent inverse correlation between effective dimensionality and adversarial robustness across diverse architectures, datasets, and attack methods — is the paper's main contribution, and the reviews do not surface a fundamentally new interpretation of this finding beyond what the paper already states.

## Suggestions

1. **Specify the effective dimensionality computation in full.** Provide: Hessian approximation method (Lanczos / exact / subset-based), number of eigenvalues computed per model, number of test examples used, convergence criteria, the chosen *z* value, and the compute budget. Without these details the paper's central quantity is a black box.
2. **Report clean accuracies and absolute robust accuracies** alongside the relative metrics, ideally in a table or in the figures, so readers can verify that the effdim-robustness correlation is not an artifact of the relative metric.
3. **Quantify the relationship for the main results (Figure 2)** with Spearman/Pearson correlations and, where feasible, confidence intervals. "Near-linear" needs quantitative backing.
4. **Conduct at least one model-size-controlled analysis:** either partial correlation controlling for parameter count, or a comparison of models with similar parameter counts but different effective dimensionalities.
5. **Explicitly state the dataset used for adversarial training experiments** and identify which data points were removed as outliers in the regression analysis (Figure 4), with justification.

## Score and Decision

The paper presents an interesting and genuinely large-scale empirical investigation of a plausible hypothesis. The core finding — an inverse correlation between effective dimensionality and adversarial robustness — is supported by evidence across diverse settings and represents a useful empirical contribution. However, two issues significantly limit the paper's impact: (1) the underspecified computation of the paper's central metric threatens reproducibility, and (2) the paper's strongest comparative claim (that effdim is more nuanced/effective than parameter count) is inadequately supported by the experimental design. These are addressable with revisions but are not fatal — the core correlation finding stands.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>