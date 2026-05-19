## Summary
This paper presents MUBen, a benchmark that systematically evaluates eight uncertainty quantification (UQ) methods across four categories (deterministic, Bayesian, post-hoc, ensembles) applied to six molecular representation models (including pre-trained backbones) on 14 molecular property prediction tasks. The study provides actionable insights about which UQ methods work best with which backbone architectures under distribution shift, and offers practical guidance for selecting UQ strategies.

## Strengths
- **Comprehensive and systematic coverage.** The benchmark covers 8 UQ methods spanning four methodological categories and 6 backbone models spanning SMILES (ChemBERTa), 2D graphs (GROVER, GIN), 3D conformations (Uni-Mol, TorchMD-NET), and hand-crafted features (DNN). Every combination is evaluated on 14 datasets from MoleculeNet. This breadth directly addresses the paper's stated gap in prior work. (Evidence: Sections 4.1–4.3; Tables 5.1, 5.2.)

- **Principled out-of-distribution evaluation.** The benchmark uses scaffold splitting to create realistic OOD test sets and further validates robustness via Tanimoto-similarity binning analysis (Figure 5.5), showing that calibration error remains relatively stable across distribution-shift levels while prediction error degrades as expected. (Evidence: Section 4.3, Section 5 "Impact of Training-Test Distribution Shift", Figure 5.5.)

- **Actionable, evidence-grounded insights.** The analysis yields concrete findings supported by quantitative results: Deep Ensembles consistently improve both prediction and calibration but at computational cost; Temperature Scaling and MC Dropout are effective for classification calibration; BBP and SGLD perform well for regression uncertainty but can degrade accuracy in smaller models; larger expressive models (Uni-Mol) are more prone to overconfidence, making UQ especially critical for them. (Evidence: Tables 5.1, 5.2; Figures 5.2–5.4.)

- **Ablation studies that reinforce conclusions.** Frozen backbone and random split experiments (Table 5.3) provide additional validation, showing that frozen backbones calibrate better (less overfitting) and random splits yield overconfident predictions — consistent with the main analysis. (Evidence: Section "Frozen Backbone and Randomly Split Datasets", Table 5.3.)

## Weaknesses
### Fatal

None.

### Major

- **No variance reporting across runs.** The paper averages results over only 3 random seeds (0, 1, 2) and reports no standard deviations, confidence intervals, or any measure of variability. For a benchmark where conclusions depend on fine-grained comparisons (e.g., ranking tables, comparing BBP/SGLD to Deep Ensembles), the reader cannot assess whether reported differences are meaningful relative to random variation. This is the most significant limitation for a paper whose core contribution is comparative analysis. (Evidence: Line 216: "Each reported metric is the average of 3 individual training-test runs with random seeds 0, 1, and 2.")

- **The regression calibration metric assumes Gaussianity without discussion.** The Regression Calibration Error (CE) formula (Equation 3) parameterizes a Gaussian CDF for the predicted quantile function, tying the evaluation to a specific distributional form. If the true predictive distribution is non-Gaussian (e.g., heavy-tailed), the CE may give misleading scores. The paper neither acknowledges this limitation nor explores distribution-free alternatives (e.g., interval-based coverage diagnostics). This does not invalidate the results (Gaussian NLL is standard practice), but the omission should be addressed. (Evidence: Line 119: "such as a Gaussian cumulative distribution function ... assuming a Gaussian distribution for the labels.")

### Minor

- **Coarse hyperparameter tuning may affect conclusions about specific UQ methods.** The paper acknowledges using "coarse-grained hyperparameter grids" (Section 6/line 330). This is reasonable for a benchmark of this scope, but it has real consequences for specific claims — e.g., that "BBP and SGLD deliver commendable performance in predicting regression uncertainty" — because these methods are known to be sensitive to learning rate, prior variance, and Langevin step count. The observation that they improve calibration at the cost of accuracy could partially reflect suboptimal tuning rather than an inherent property. The paper already flags this as a limitation, but the conclusion about BBP/SGLD should be read as tentative.

- **Ensemble size is not explicitly stated or ablated in the main text.** The paper notes "even when the number of ensembles is limited, such as the QM9 case (appsec:uncertainty)," referring to an appendix we cannot verify. The main text does not state how many ensemble members are used or whether results are stable with respect to this hyperparameter, which is important for practitioners applying Deep Ensembles.

### Trivial

- The ECE formula (Equation 1) uses an unspecified number of bins $S$; the paper does not state the bin count or discuss sensitivity to binning choices.

## Suggestions
1. **Report standard deviations** for all metrics across seeds. This is the single highest-leverage improvement for a benchmark paper — it would allow readers to assess whether ranking differences are meaningful.
2. **Add a brief discussion of the Gaussian assumption** in the regression CE metric, and optionally include a non-parametric calibration diagnostic (e.g., interval-based coverage) to verify robustness.
3. **State the ensemble size used** for Deep Ensembles explicitly in the main text, and ideally include a small ablation showing sensitivity to this parameter.
4. **Provide a computational cost table** showing per-method training time, inference time, and memory — this would make the benchmark substantially more useful for practitioners choosing UQ methods.
5. **Soften the BBP/SGLD regression conclusion** to explicitly note that the finding is conditional on the coarse hyperparameter search.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
