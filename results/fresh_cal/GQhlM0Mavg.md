Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper advocates for cross-fertilization between Out-of-Distribution (OOD) detection and Conformal Prediction (CP). It makes two contributions: (1) it adapts CP-based corrections from Bates et al. (2022) to define "conformal AUROC" and "conformal FPR@TPRβ" metrics that provide conservative probabilistic guarantees on OOD evaluation, demonstrating their impact on OpenOOD and ADBench benchmarks; and (2) it explores using OOD scores (KNN, Mahalanobis, ReAct, Gram, ODIN) as nonconformity scores for CP to potentially improve prediction set efficiency.

## Strengths

- **Concrete, practically-motivated adaptation of CP corrections to OOD metrics (Section 4.4).** The paper defines conformal AUROC and conformal FPR@TPRβ by replacing the empirical FPR with the corrected conformal FPR from Bates et al. (2022). This is a clean methodological adaptation that gives OOD evaluation probabilistic conservativeness guarantees (Equation 11), which standard OOD benchmarks lack. The framing of the FPR as a p-value (Section 4.1) and the connection to hypothesis testing is pedagogically effective.

- **Empirical demonstration that the correction is material yet preserves practical utility.** Table 1 shows conformal AUROC is often >1% lower than classical AUROC (e.g., CIFAR-100 with Mahalanobis: 87.22 classical vs. 86.25 conformal), but the ranking of top methods is preserved. Figure 3 (right) shows the correction affects all ADBench baselines similarly. This demonstrates the metric is usable for fair comparison while being safety-relevant.

- **Verification of FPR variability on real data matching theory (Section 4.3.1).** Using the SVHN extra dataset with 53 simulated calibration sets, the paper shows the histogram of \(F(0.1; \mathcal{D}^{cal})\) closely matches the theoretical Beta distribution predicted by Bates et al. (Figure 1). This grounds the need for the proposed corrections with concrete evidence rather than purely theoretical argument.

- **Novel exploration of OOD scores as nonconformity scores for CP (Section 5).** Adapting multiple OOD scores (KNN, Mahalanobis, ReAct, ODIN, Gram) for CP classification and evaluating with LAC, APS, and RAPS procedures on CIFAR-10 and CIFAR-100 is a genuinely novel cross-application. Table 2 shows that KNN and Mahalanobis sometimes achieve better mean efficiency than softmax-based scores (e.g., KNN with LAC on CIFAR-10 at 0.95 coverage yields 1.99 vs. softmax 2.04).

## Weaknesses

### Fatal
None.

### Major

- **The second contribution's claims outpace its evidence, and the adaptation of OOD scores to class-dependent CP scores is underspecified.** The abstract claims OOD scores "can improve the efficiency of the prediction sets" and the conclusion states they "improve existing CP techniques," yet the paper's own results section (line 209) admits "all OOD scores are inefficient for CP" — with KNN and Mahalanobis occasionally outperforming softmax on only 2 datasets (CIFAR-10/100). This is preliminary, exploratory evidence, not support for the unqualified claim of "improvement." Furthermore, the paper does not explain how class-conditional OOD scores \(s(x, y_i)\) are obtained for methods like ReAct, Gram, or KNN, which produce per-example (unconditional) scores. The transformation \(\hat{s}(x, y_i) = \exp(s(x,y_i)) / \sum_j \exp(s(x,y_j))\) is stated (line 205-206) but the critical step of defining \(s(x,y_i)\) for each class is not specified. This methodological gap makes the experimental results difficult to interpret or reproduce.

- **The first contribution is a straightforward application of Bates et al. (2022) corrections to OOD metrics, not a conceptual innovation.** The paper is transparent about this (Section 4.4: "Based on the previously defined conformal FPR (already defined in Bates et al. (2022))"), but the abstract frames it as "new *conformal AUROC* and *conformal FRP@TPRβ* metrics" without sufficiently signaling that the novelty lies in the *demonstration and practical recommendation* rather than the metric definitions themselves. This is a meaningful contribution (and likely the stronger half of the paper), but it should be framed as a practical application of existing theory, which would also clarify what the paper adds beyond prior work like Liang et al. (2022) and Kaur et al. (2022).

### Minor

- **Missing experimental details for reproducibility.** For the ADBench experiments, the correction method (Simes, DKWM, Asymptotic, or Monte Carlo) is not specified (the ADBench section only reports \(\delta=0.05\)). Calibration set sizes are not reported per dataset for the OpenOOD and ADBench experiments. While the paper says the ID validation set serves as the calibration set, the exact number of points is not stated, making it difficult to assess whether the finite-sample corrections are appropriate.

- **Section 5 experiments are limited in scope.** Only CIFAR-10 and CIFAR-100 are tested with ResNet18 backbones. The paper claims OOD scores could "improve" CP, but two small-scale datasets are insufficient to support this or to understand when OOD scores help vs. hurt. The comparison with softmax-based CP scores would also benefit from including the maximum softmax probability as a baseline (which is itself an OOD score, as the paper notes).

- **No analysis of when correction is most needed.** The paper reports the overall effect on AUROC but does not analyze which datasets or settings produce the largest corrections, or provide practical guidelines for when to use conformal vs. classical metrics. The discussion of the ADBench scatter plot (Figure 3, left) notes variability exists but does not identify which datasets drive the large corrections.

### Trivial

- The paper references "Table 5" in the text (lines 207, 209) while the table image is labeled "Table 2" — a numbering inconsistency likely from the PDF extraction, but worth fixing.
- The guarantee in Remark 4.1 says conformal metrics "do not require extra validation data" — this is true in the sense that the correction reuses the existing validation set, but the correction does reduce the effective sample size for the FPR estimate, which could be clarified.

## Nice-to-Haves

- Report standard deviations or confidence intervals for the classical and conformal AUROC values in Table 1 (across random calibration splits), since the correction introduces stochasticity.
- For the first contribution: show how the cost in AUROC varies with \(\delta\) (the paper mentions running experiments for other \(\delta\) values but those results appear truncated).
- For the second contribution: provide a principled explanation of why certain OOD scores (KNN, Mahalanobis) might yield tighter prediction sets than softmax-based scores, e.g., by analyzing their calibration properties.

## Removed Points

These points were raised by the reviewers but are removed for the reasons given:

- **"Table 1 appears garbled"** — This is a PDF-extraction formatting artifact, not an issue in the submitted paper.
- **"The paper should report the full set of baselines from OpenOOD"** — The paper's goal is to evaluate a new metric, not to propose a new OOD method. Showing a representative subset of baselines is standard practice for this type of contribution.
- **"The results are not statistically significant"** — The paper reports standard deviations for stochastic methods (APS, RAPS) over 10 evaluations. For deterministic methods (LAC), single-run evaluation is standard in the CP literature.
- **"Missing related works"** — Cannot be verified independently; the paper's related works section is adequate for the scope.
- **"The correction affects baselines differently (Figure 3 right)"** — This contradicts the paper's actual statement ("the correction affects all baselines similarly") and the figure description. The harsh critic's own reading acknowledges variation across methods, which doesn't invalidate the claim of similar relative ordering.
- **"The paper doesn't specify which calibration set size was used for each dataset"** — The SVHN simulation (Section 4.3.1) specifies 10,000-point calibration sets, and the CP experiment (Section 5) specifies \(n_{cal} = 2000\). For OpenOOD/ADBench, the standard validation splits serve as calibration sets — the criticism is partially valid but downgraded to minor above.

## Novel Insights

The most interesting observation that emerges from the reviewers' synthesis but is not explicitly highlighted in the paper is the asymmetry between the two contributions: the CP→OOD direction (conformal metrics) works cleanly because it directly leverages CP's p-value corrections without changing the underlying scores, while the OOD→CP direction (OOD scores as nonconformity scores) requires bridging a fundamental mismatch — OOD scores are typically unconditional detection scores, while CP requires class-conditional scores. This asymmetry suggests that future work on score adaptation (rather than simple softmax-like transformations) could be more productive than directly plugging OOD scores into CP procedures.

## Suggestions

1. **Reframe the contributions more honestly.** The first contribution is well-supported and practically useful — lean into it. Tone down the abstract and conclusion claims about the second contribution from "improve" to "explore" or "suggest that some OOD scores may be competitive with softmax scores in certain settings." The paper would be stronger if it clearly distinguishes between the established contribution (conformal OOD metrics) and the exploratory one (OOD scores for CP).

2. **Specify the class-conditional score construction for each OOD method.** The paper must explain how \(s(x, y_i)\) is defined for each of ReAct, Gram, KNN, Mahalanobis, and ODIN. If some methods cannot produce class-conditional scores naturally, either omit them or explain the approximation used.

3. **Add the missing experimental details:** state which correction method (Simes/DKWM/Monte Carlo) was used for ADBench, and report calibration set sizes per dataset for both benchmarks.

4. **Either strengthen Section 5 or acknowledge its preliminary nature.** Add more datasets (e.g., ImageNet subsets), more architectures, and a discussion of why KNN/Mahalanobis sometimes outperform softmax. If the experiments cannot be expanded, explicitly frame Section 5 as a preliminary exploration with the honest conclusion that "most OOD scores are inefficient for CP, but some (KNN, Mahalanobis) merit further investigation."

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>