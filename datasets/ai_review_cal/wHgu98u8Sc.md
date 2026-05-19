- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 5, 6, 3, 3
Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual text. Let me compose the consolidated review.

---

## Summary

This paper introduces ν-ensembles, a simple method to improve deep ensemble calibration in the small-data regime. Given an unlabeled set, each ensemble member is trained with a different randomly assigned label for each unlabeled point. The paper provides a PAC-Bayes bound (Theorem 1) that links test negative log-likelihood to training NLL, ensemble diversity (variance on unlabeled data), and a weight-norm penalty. Empirically, on CIFAR-10 and CIFAR-100 with varying training set sizes (1K–40K) and three architectures (LeNet, MLP, WideResNet22), ν-ensembles match standard ensembles in accuracy while achieving substantially better calibration (ECE, TACE, Brier Score Reliability, NLL). The method requires no changes to the standard ensemble training loop beyond randomly labeling unlabeled data, preserving its computational and memory profile.

## Strengths

- **Novel, extremely simple method with clear motivation.** The core idea — giving each ensemble member a different random label on unlabeled data — is strikingly simple and can be implemented by modifying only the data loading step of standard deep ensemble training. This stands in contrast to prior diversity-promoting methods (Ramé & Cord, 2021; Masegosa, 2020; Matteo et al., 2023) that require significantly more complex training procedures and hyperparameter tuning. The paper provides direct evidence of this advantage: Section 5.1 notes ν-ensembles have O(1) memory cost with sequential training, while Masegosa and Agree-to-Disagree ensembles scale as O(K); Figure 4 confirms that training time per member is comparable to standard ensembles and far lower than Agree-to-Disagree.

- **Consistent and substantial calibration improvements across architectures, datasets, and metrics.** Table 1 reports improvements on CIFAR-10 and CIFAR-100 with 1000 training samples for LeNet, MLP, and WideResNet22. The gains are large in many configurations (e.g., CIFAR-100/LeNet ECE dropping from 57.65 to 2.70; CIFAR-10/LeNet from 3.21 to 0.43), and they hold across four calibration metrics (ECE, TACE, Brier Score Reliability, NLL) while accuracy remains nearly identical. The improvements generalize beyond i.i.d. data: Figure 3 shows similarly better calibration under 15 common corruptions at 5 severity levels for CIFAR-10.

- **Theoretical PAC-Bayes bound provides a principled foundation.** Theorem 1 gives an upper bound on expected test NLL that includes a positive diversity term (the empirical variance of ensemble predictions on unlabeled data). This formally connects the paper's mechanism (increasing variance via random labels) to an upper bound on test loss, providing theoretical motivation that standard deep ensembles lack. The bound is not tight enough to make quantitative predictions (the function *h* is left unspecified), but it serves its role as qualitative motivation.

- **Analysis of sampling strategy (with vs. without replacement).** Proposition 2 and the numerical comparison in Figure 4 show that sampling labels without replacement yields higher expected variance (and thus better calibration) than sampling with replacement, and the paper provides an empirical confirmation of this prediction. This gives the practitioner a clear design choice.

## Weaknesses

### Fatal

None.

### Major

1. **No error bars or uncertainty quantification on any empirical result.** Every reported number (Table 1: accuracy, ECE, TACE, Brier Score Reliability, NLL, MI; Figure 2: ECE improvement across training set sizes; Figure 3: OOD accuracy and ECE) is a point estimate from a single run with no indication of variance. The paper mentions a "random hyperparameter search with 50 trials" (Section 5.1) but this is for hyperparameter tuning, not for estimating run-to-run variability. Given that neural network training is stochastic, that the evaluation uses small training sets (1K–4K samples) where variance is naturally higher, and that the paper's central claim is about *improvement* relative to a baseline, the absence of error bars makes it impossible to assess whether the reported gains are statistically reliable. Mitigations: the improvements are consistent across architectures, datasets, and metrics, and some are very large (e.g., CIFAR-100 ECE from 57.65→2.70), which makes it unlikely that all gains are noise. But for moderate or close-to-zero improvements (e.g., CIFAR-10 with 40K samples), uncertainty is critical. This is the most significant weakness in the paper.

2. **Incomplete baseline comparisons across the paper's primary experimental variable (training set size).** The paper compares ν-ensembles to two prior diversity methods (Masegosa ensembles, Agree-to-Disagree ensembles) — as well as temperature scaling — but only at a single training size of 1000 samples (Table 1). The full analysis varying training set size (Figure 2, 1000–40,000) compares ν-ensembles only to standard ensembles, not to Masegosa or Agree-to-Disagree. The paper motivates ν-ensembles as a method that achieves calibration gains "while avoiding the complexity and cost of prior diversity methods" (Introduction), yet never shows how those prior methods fare at larger data sizes. It is possible that Masegosa or Agree-to-Disagree also improve calibration at, say, 4000 or 10,000 samples — or that they degrade accuracy further. Without this comparison, the relative merit of ν-ensembles across the full range where they claim benefit cannot be assessed.

### Minor

3. **The PAC-Bayes bound is presented as a guarantee but is not empirically validated or checked.** The abstract states the bound "guarantees that for such a labeling we obtain low negative log-likelihood and high ensemble diversity on testing samples." However, the bound (Theorem 1) is an upper bound that includes the average training NLL (which must increase when fitting random labels) and an unspecified function *h*(‖ŵ_i‖₂²). Whether the bound actually *tightens* under ν-ensembles — i.e., whether the diversity gain offsets the increase in training NLL and penalty term — is not checked empirically. The bound serves as reasonable motivation but the claim of a "guarantee" is overstated, and the paper would be strengthened by showing the bound's value for a representative configuration.

4. **Mutual Information not reported for Masegosa and Agree-to-Disagree ensembles.** Table 1 reports MI for standard and ν-ensembles (showing diversity increases), but not for the two comparison methods. Since the paper argues that diversity drives calibration improvement, reporting MI for all methods would enable a cleaner comparison of the diversity–calibration relationship across approaches.

5. **Sampling-with-replacement comparison stated qualitatively, not quantified.** Section 5.3 reports that "on average, sampling without replacement results in better calibration across our different metrics" without showing the actual numbers in a table or figure. While Proposition 2 and Figure 4 give the theoretical motivation, the empirical confirmation is too brief. A supplemental table showing the comparison for the same configurations as Table 1 would make this result concrete.

### Trivial

6. **The bound's "with high probability" clause is left without a confidence level or sample complexity term in the main text.** This is standard practice in PAC-Bayes papers (details typically appear in an appendix), but in a self-contained submission it would be helpful to state the scaling explicitly.

## Nice-to-Haves

- Sensitivity analysis varying the number of unlabeled samples |U| (fixed at 5000 throughout). Exploring whether more unlabeled data monotonically improves calibration or whether there is a sweet spot would strengthen the practical guidance.
- A comparison between ν-ensembles and standard ensembles with more members (e.g., 20 standard members vs. 10 ν-ensemble members). If calibration gains can be matched by simply using more standard members, the relative value of ν-ensembles is different.
- Reporting absolute ECE (not just improvement) alongside Figure 2, so readers can see absolute calibration levels.

## Removed Points

These points were flagged for removal; treat them with caution if shared externally.

1. **"The bound's 'with high probability' lacks a confidence level"** — This detail is standard for the main-text exposition of a PAC-Bayes bound; the full derivation and δ-dependence are expected in the appendix (stripped by the parser). Removed per the rule against criticizing missing appendix content.

2. **"Figure 2 y-axis label is ambiguous"** — The paper's caption (line 113) reads "the improvement in Expected Calibration Error (ECE) compared to standard ensembles," which is adequately clear given the context. Removed as not a real ambiguity.

3. **"Number of unlabeled samples not explored"** — This asks the paper to expand its experimental scope beyond what is stated. Removed as scope creep.

4. **"Pre-defined labels baseline not compared"** — This asks for an additional ablation not central to the paper's stated contribution. Removed as a suggestion, not a weakness.

5. **"No wall-clock times for computational cost"** — The paper already provides a normalized comparison of training time in Figure 4. Removed as the existing analysis is sufficient.

6. **"Reproducibility: hyperparameter search space not described"** — The paper mentions 50-trial Hydra search, which is standard detail. Removed per the rule against nitpicking trivial reproducibility details.

## Novel Insights

The reviewer critiques surfaced one genuinely non-obvious point: the paper's theoretical bound actually involves a *trade-off* (training NLL increases when fitting random labels, while diversity increases). The bound does not automatically tighten — it depends on whether the diversity gain outweighs the training-loss penalty and the weight-norm cost. This is a subtle but important distinction from the paper's presentation, which frames the bound as a straightforward guarantee. A second insight from cross-referencing the evaluations: Table 1 shows that Masegosa ensembles "have somewhat better calibration than ν-ensembles in most cases" but with lower accuracy due to underfitting, while ν-ensembles maintain accuracy. This frames ν-ensembles not as the best calibrator but as the best *accuracy-preserving* calibrator, which is a more nuanced positioning than the paper's main narrative suggests.

## Suggestions

1. **Add error bars.** Re-run each experimental configuration (architecture × dataset × ensemble type × training size) over at least 3–5 random seeds and report means with standard deviations or confidence intervals for all metrics. This is by far the highest-leverage improvement.

2. **Extend Masegosa and Agree-to-Disagree comparisons to at least a subset of the training set sizes** (e.g., 1000, 4000, 10,000). Even a partial comparison would substantially strengthen the paper's claims about ν-ensembles' relative advantages.

3. **Empirically check the PAC-Bayes bound for one configuration.** Compute the bound's value (using a concrete choice of *h*) for both standard ensembles and ν-ensembles to show that the bound does indeed improve, turning the theory from motivation into evidence.

4. **Quantify the sampling-without-replacement vs. with-replacement comparison** with a table showing the actual effect sizes across architectures and datasets.

---
