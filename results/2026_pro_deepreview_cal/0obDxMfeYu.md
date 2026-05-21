Now I have a clear picture. Let me synthesize the final review.

---

## Summary

This paper introduces Medix, a two-stage framework for out-of-distribution (OOD) detection that leverages unlabeled "wild" data. The first stage uses element-wise median (EWM) of classifier gradients to filter candidate outliers from the wild mixture via a greedy leave-one-out algorithm. The second stage trains a binary OOD detector on the extracted outliers and labeled in-distribution data. The paper provides theoretical bounds on inlier and outlier misclassification rates and demonstrates strong empirical performance against 20 baselines on CIFAR-10/100 across five OOD test sets.

## Strengths

- **Novel median-based filtering mechanism.** The use of element-wise median of gradients as a robust criterion for separating InD from OOD samples in unlabeled mixtures is genuinely novel. The motivation from Figure 1 — showing monotonic increase in EWM-to-mean distance as OOD samples are added — is clear and empirically grounded, directly motivating both the optimization objective (Equation 4) and the algorithm's stopping criterion.

- **Strong empirical performance against comprehensive baselines.** Tables 1–2 demonstrate that Medix consistently outperforms 20 baselines across five OOD test sets on both CIFAR-10 and CIFAR-100. On CIFAR-100, Medix achieves an average FPR95 of 5.42% vs. WOODS at 6.74% and KNN+ at 46.40%. The improvements over the prior wild-data state-of-the-art (WOODS) are consistent across datasets (e.g., 7.21% FPR95 reduction on PLACES365, 5.25% on TEXTURES for CIFAR-10). Results include standard deviations over five runs, lending credibility.

- **Theoretical analysis with error decomposition.** Theorems 4.1 and 4.2 provide upper bounds that decompose misclassification error into contamination, concentration, and separation effects. The analysis formally shows why the median is robust when π < 0.5 and when InD gradients concentrate sub-Gaussianly. Remark 4.3 provides empirical validation of the sub-Gaussian assumption with histogram and Q-Q plots, and Theorem C.3 offers a version relaxing this assumption.

- **Practical algorithmic design.** The greedy top-k removal in Algorithm 1 avoids exhaustive subset search while remaining effective. The synthetic 2D experiment (Figure 2) demonstrates 87.5% correct outlier identification, and the paper defers extensive ablation studies (hyperparameter sensitivity, EWM vs. geometric median, unseen OOD, computational efficiency) to the appendix, suggesting a thorough empirical investigation.

## Weaknesses

### Fatal

None.

### Major

- **Theoretical bounds are uninformative at the experimental operating point (π = 0.5).** In Theorem 4.1, the contamination term is π/[2(1−π)], which equals 0.5 when π = 0.5. The bound therefore guarantees an inlier error rate of at most ~50% plus concentration terms — a trivial guarantee that does not demonstrate "low error." The paper is careful to state that bounds are "controlled as long as π < 0.5" (line 142), and the introduction says "as long as OOD proportion is below 50%" (line 29). However, the abstract and conclusion claim the theory "demonstrates Medix achieves a low error rate" (line 13) and "maintains robustness even under significant OOD contamination (up to 50%)" (line 266). These claims are not supported by the bound at π = 0.5. The theory and the experimental setting are misaligned, and the theoretical contribution's strength is overstated. This matters because the claimed theoretical guarantee is one of the paper's three main contributions (C2).

- **Hyperparameter selection procedure is ambiguous.** Section 5.2 states that ε and k are selected "with the objective of maximizing OOD performance." It is unclear whether this tuning uses a held-out validation set (e.g., a split of the wild mixture), the test OOD sets directly, or some other protocol. If tuned on test OOD data, the reported results would not be a valid evaluation of generalization. The paper must clarify this, as it affects the credibility of the reported improvements.

- **Main evaluation uses matched wild and test OOD distributions, weakening the open-world claim.** The wild mixture is constructed using the same OOD dataset later used for testing (e.g., wild contains PLACES365, test OOD is PLACES365). This means the outlier extraction stage sees examples from the exact distribution it will be evaluated on — a substantially easier setting than genuine open-world detection where test OOD diverges from wild OOD. The paper does report unseen-OOD results (where P_out^test ≠ P_out) in Appendix A.4, and the main text (line 242) claims Medix "outperforms baselines by a significant margin" there. However, relegating this to the appendix while presenting the matched-setting results as the primary evidence overstates the method's real-world robustness. The abstract's claim of "open-world settings" is not fully supported by the main experimental tables.

### Minor

- **No empirical analysis of how π affects filtering and detection.** All experiments fix π = 0.5. Given that the theoretical bounds are sensitive to π (contamination terms explode as π → 0.5 from below), varying π (e.g., 0.1, 0.3, 0.5, 0.7) would help readers understand the method's practical robustness across contamination regimes and connect theory to practice.

- **Training set size discrepancy with InD-only baselines.** Medix uses 25k labeled CIFAR samples while InD-only baselines use the full 50k. The ~2.6% drop in InD accuracy is acknowledged (line 186), but the effect on baseline OOD scores is not discussed. This is a minor concern since the comparison against wild-data methods (WOODS, OE) is on equal footing and Medix still wins.

- **Separation condition in Theorem 4.2 is not empirically verified.** The theorem requires ||μ_out − ∇̄_in||₂ ≥ Δ√d for the exponential separation term to provide meaningful guarantees. While Remark 4.3 validates the sub-Gaussian assumption, no analogous empirical check is provided for the separation gap on real networks and datasets. This limits confidence in whether the theoretical guarantees of Theorem 4.2 actually apply in practice.

### Trivial

None.

## Nice-to-Haves

- Developing a tighter bound or a refined analysis that remains informative at π = 0.5 would substantially strengthen the theoretical contribution. Alternatively, restating the theory's scope honestly (e.g., "the bound guarantees low error for π bounded away from 0.5") would align claims with results without new mathematics.
- Moving the unseen-OOD evaluation to the main paper would better support the open-world framing.
- Reporting confidence intervals or statistical tests for all baselines (not just Medix) would strengthen comparative claims.
- An ablation on which layer's gradients are used (the penultimate layer is chosen by citation to Huang et al. 2021a, but within-method sensitivity is not explored).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The i.i.d. assumption is overly simplistic"** — REMOVED. Standard theoretical simplification; the paper also provides Theorem C.3 relaxing the sub-Gaussian assumption to bounded second moments. Theory papers routinely make i.i.d. assumptions.
- **"No justification for penultimate layer choice"** — REMOVED. The paper explicitly cites Huang et al. (2021a) on line 174 for this choice.
- **"Perfect detection on LSUN-C raises overfitting concerns"** — REMOVED. Speculative; the paper reports standard deviations across five runs, and the FPR95 of 0.01 ± 0.01 is within the range of empirical possibility for easy OOD datasets like LSUN-C vs. CIFAR-10.
- **"Synthetic 2D example is too simplified"** — REMOVED. The paper explicitly states (line 240): "This simulation is designed to be simple to facilitate better understanding." This is self-aware and appropriate for a pedagogical illustration.
- **"Computational cost not discussed"** — REMOVED. The paper states that Appendix A.6 covers computation and memory efficiency (line 242).
- **"The claim about Du et al. (2024a) being the only work with theoretical foundation may be an overstatement"** — REMOVED. Cannot verify without external sources; the paper's claim is qualified with "to the best of our knowledge."

## Novel Insights

The connection between element-wise median of gradients and outlier detection in unlabeled mixtures is novel and well-motivated. The key insight — that the L₂ distance between the average InD gradient and the EWM of wild-data gradients increases monotonically with OOD contamination (Figure 1) — provides a simple, intuitive principle that directly motivates both the optimization objective and the algorithm's stopping criterion. This is a clean empirical observation that the paper builds its entire method around, and it is more direct than prior gradient-based approaches (e.g., SAL's singular vector criterion). The theoretical decomposition of error into contamination, concentration, and separation effects, while standard in structure, is applied to a novel filtering mechanism and provides useful conceptual scaffolding even if the bounds are loose at the experimental π.

## Suggestions

- Clarify the hyperparameter selection protocol explicitly: state whether ε and k are selected on a held-out validation split of the wild mixture (which would be valid) or on test OOD data, and ensure the former.
- Either restate the theoretical claims to accurately reflect that the bounds are informative for π < 0.5 (not at π = 0.5), or develop a refined analysis that tightens the contamination term.
- Consider moving the unseen-OOD results from Appendix A.4 into the main tables, or at minimum add a dedicated main-paper table for this setting, to substantiate the open-world framing.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `3ZdGSTxKuy` (Harry Potter video OOD) | 2.00 | R1 | Much weaker; different problem, limited evaluation |
| `l5ouuojPGe` (Thresholding for NN monitoring) | 3.00 | R1 | Weaker; different problem, narrower scope |
| `6Z8rZlKpNT` (Normalizing flows OOD) | 3.40 | R1 | Weaker; post-hoc method, no wild data |
| `i28ZjVxl81` (OOD on tabular data) | 2.50 | R1 | Much weaker |
| `bcWwhF8cTZ` (Gradient norm OOD error) | 5.50 | R1 | Weaker; rejected, limited novelty concerns |
| `am7BPV3Cwo` (OOD on imbalanced data) | 5.75 | R2 | Weaker; narrower scope |
| `jlEjB8MVGa` (SAL — direct predecessor) | 6.50 | R1/R2 | Medix is stronger: harder π=0.5, more baselines, stronger results, unseen OOD eval |
| `VTYg5ykEGS` (ImageNet-OOD analysis) | 6.50 | R2 | Different focus (benchmarking), not directly comparable |
| `mUXdysoxEP` (Neural Collapse OOD) | 6.75 | R2 | Medix has stronger empirical evaluation and theory; comparable quality |
| `ljwoQ3cvQh` (DNNs extrapolate predictably) | 7.00 | R2 | Comparable quality; both have theory+empirical, different contributions |
| `xUO1HXz4an` (NegLabel VLM OOD) | 7.50 | R2 | Different setting (VLMs); Medix is in a harder setting without pretrained VLMs |
| `iriEqxFB4y` (DOS outlier sampling) | 7.33 | R2 | Different approach (regularization with surrogate outliers); Medix handles wild data which is harder |

**Bracket:** Round 1 placed Medix between 6.0–7.5. Round 2 narrowed this: Medix is clearly stronger than SAL (6.50) and the NC-OOD paper (6.75), and roughly comparable to Extrapolate (7.00). The three major weaknesses — theoretical bound vacuity at π=0.5, hyperparameter ambiguity, and matched wild/test OOD — are real and prevent a score much above 7.0. However, the method is genuinely novel, the empirical gains are substantial and broad, and the theoretical analysis, while imperfect at the experimental operating point, provides useful structural insights.

**Final score: 7.0**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>