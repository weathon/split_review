## Summary

This paper proposes Covariance-Adjusted SVM (CSVM), which uses class-specific Cholesky decomposition of covariance matrices to transform data to a space where Euclidean distance is appropriate, performs SVM there, and reverse-transforms the resulting classifier. The paper derives that the margin ratio in the input space depends on class covariances (Eq. 14), and proposes a self-training algorithm (SM Algorithm) to estimate population covariances when test labels are unavailable. Experiments on 5 datasets compare CSVM against standard SVM kernels and PCA/ZCA whitening.

## Strengths

1. **Concrete algebraic derivation connecting margin to class covariance.** Equations (9)–(14) derive that when SVM is solved in the Cholesky-transformed space and reverse-mapped to the input space, the margin ratio between classes becomes √(θᵀ Σ_{y=-1}⁻¹ θ) / √(θᵀ Σ_{y=1}⁻¹ θ). This is a specific, verifiable mathematical result that ties the decision boundary to intra-class covariance — something the cited prior methods (MCVSVM, Mahalanobis TSVM) do not derive from the vector-space geometry of Mahalanobis distance.

2. **CSVM-Cholesky achieves the highest point estimates on most datasets.** Across 5 datasets spanning healthcare, astronomy, quality, and safety, CSVM-Cholesky obtains the highest accuracy, F1, and recall on 4/5 datasets (Breast Cancer, Diabetes, Red Wine, Pulsar) and the highest AUC on 3/5 datasets (Tables 1–4, Figs. 1–3), against baselines that include linear SVM, RBF, polynomial, sigmoid, PCA whitening, and ZCA whitening.

## Weaknesses

### Major

1. **Structurally unfair evaluation: the proposed method uses test data while baselines do not.** The SM Algorithm (Section 3, steps f–h) is a self-training procedure: it labels test points, adds them to the training set, recomputes class covariances, and refits the classifier. This gives CSVM access to the distribution of the test set. All baselines (linear SVM, RBF SVM, polynomial SVM, PCA/ZCA whitening + linear SVM) are applied as purely supervised methods on the training set only. The paper does not acknowledge this asymmetry, nor does it compare against any standard semi-supervised SVM methods (e.g., transductive SVM, self-training SVM without the covariance adjustment) that would isolate whether performance gains come from the covariance adjustment or the self-training loop.

2. **No empirical comparison against the specific prior work the paper claims to improve upon.** The introduction cites MCVSVM (Zafeiriou et al. 2007), Mahalanobis TSVM (Peng & Xu 2012), MD-BLSSVM (Ke et al. 2018), the maxi-min margin machine (Huang et al. 2004), and weighted Mahalanobis distance kernels (Wang et al. 2007), stating that these methods have "gaps in application of appropriate vector spaces and dimensional inconsistencies." None of these methods appear in the experimental comparison. Without comparisons against the very methods the paper claims to fix, the central claim of improvement over prior covariance-adjusted SVM work cannot be evaluated.

3. **No uncertainty quantification; results are point estimates from a single train/test split.** All metrics in Tables 1–4 and AUC values in Figures 1–3 come from a single 80:20 split per dataset. No cross-validation, bootstrapped confidence intervals, or standard deviations are reported. Several improvements are modest in absolute terms (e.g., accuracy 0.974 vs 0.956 on Breast Cancer, 0.786 vs 0.760 on Diabetes, AUC 0.74 tied with linear SVM on Diabetes) and could easily fall within the noise of a single split. On the OSHA dataset, CSVM is not the best on any metric (RBF achieves the highest accuracy at 0.760 and AUC at 0.72, tied with CSVM).

4. **No hyperparameter tuning for baseline kernel SVMs.** The paper does not mention tuning C, RBF bandwidth γ, or polynomial degree for the baseline SVMs. Default or arbitrary hyperparameter choices can severely disadvantage kernel methods, making the comparison favor CSVM. A fair comparison requires either hyperparameter optimization for all methods or a clear statement of how parameters were set.

5. **Overclaimed theoretical framing.** The paper repeatedly asserts that KKT boundary conditions are "not valid" in the input space (Lemma 2.3, abstract, introduction). KKT conditions are mathematical properties of a well-posed constrained optimization problem and remain valid regardless of how the space's metric is labeled. The paper's valid intuition — that data covariance should influence the margin — does not imply that standard SVM optimization is mathematically invalid. This framing inflates the contribution and risks misleading readers.

### Minor

1. **Hard-margin assumption.** The derivation explicitly assumes ξ_i = 0 throughout (Eqs. 7, 11, 13). Real-world data is rarely perfectly separable; a soft-margin formulation is essential for practical use and is not provided.

2. **Lack of dataset characteristics.** No information is given about dataset sizes, dimensionality, class balance, or the specific train/test split sizes for any of the five datasets, making it difficult to assess generalizability.

3. **Unclear role of two separate SVMs in the SM Algorithm.** The algorithm performs SVM in the Euclidean space (step c) and a separate linear SVM in the input space (step d), then adjusts the latter's bias using the former's margin ratio. The paper does not explain why both classifiers are needed or how they interact theoretically.

4. **Vague convergence criterion for the SM Algorithm.** The convergence check (Section 3, step 3a) states "changes in test data labels are below a certain threshold" without specifying what threshold is used or how it is chosen.

### Trivial

None.

## Nice-to-Haves

- **Ablation study** isolating: (a) class-specific vs. pooled whitening, (b) iterative SM Algorithm vs. single-pass estimation, (c) ratio-adjusted margin vs. standard margin. Without these, the source of performance gains is unknown.
- **Soft-margin extension** for non-separable data.
- **Analysis of error propagation** in the self-training loop and sensitivity to the initial training split.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Non-Euclidean" framing criticism from the Harsh Critic's Point 1 (partial removal).** The critic argues that calling the input space "non-Euclidean" is a category error. However, the paper defines the statistical space by its appropriate metric (Mahalanobis distance) and calls it non-Euclidean — a framing choice that is internally coherent even if some readers may disagree. The more substantive issue (the claim that KKT conditions are "invalid") is retained in Major weakness #5 above. The pure "non-Euclidean" terminology criticism is removed as a framing preference, not a factual error.

- **Error propagation concern about self-training (speculative).** The critic's concern that mislabeled test points contaminate covariance estimates is valid in principle but is not evidenced in the paper. Demoted from a concrete weakness to an implicit acknowledgment reflected in Nice-to-Haves.

- **Strength: "Vector-space explanation for why whitening works."** The claim that "whitening transforms data to Euclidean space" is a well-understood property of whitening in the metric learning literature, not a novel insight. Removed as generic.

- **Strength Finder's characterization of "consistent empirical superiority."** The point estimates do favor CSVM, but given the unfair comparison (major weakness #1) and missing variance (major weakness #3), "superiority" overstates the evidence. The raw empirical pattern is kept but contextualized.

## Novel Insights

None beyond the paper's own contributions. The Harsh Critic and Strength Finder largely recapitulate the paper's content without identifying patterns that the paper itself does not surface.

## Suggestions

1. Reframe the theoretical motivation: present CSVM as a principled way to incorporate class-specific covariance information via a learned metric, rather than claiming that standard SVM is "invalid" in the input space.
2. Compare against the cited covariance-adjusted SVM methods (MCVSVM, Mahalanobis TSVM, etc.) and against a semi-supervised baseline (e.g., standard self-training SVM without the covariance adjustment).
3. Report cross-validated or bootstrapped performance metrics with confidence intervals.
4. Tune hyperparameters for all baseline methods following a consistent protocol, or clearly state the settings used.

---

**Calibration Anchors Report**

**Round 1 (Bracketing)**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/.../ZDoaLbOFaP.md` (Sparse Covariance Neural Networks) | 3.00 | R1-Low | Worse than our paper — poor presentation, minor novelty. Our paper is clearer with a more concrete derivation. |
| `/home/.../q1t0Lmvhty.md` (Understanding Matrix Function Normalizations) | 6.00 | R1-Mid | Significantly stronger — rigorous theory, extensive experiments across architectures. Our paper's evaluation is much weaker. |
| `/home/.../anek0q7QPL.md` (Covariance + Hessian Eigenanalysis) | 5.00 | R1-Mid | Comparable but with better evaluation protocols. Our paper has a more concrete derivation but worse evaluation. |
| `/home/.../EyWKb7Ltcx.md` (Intrinsic Riemannian Classifiers) | 5.00 | R1-Mid | More extensive experiments but incremental contribution. Our paper has more original theory but weaker evaluation. |
| `/home/.../SLUr06QUuw.md` (SymCL: Riemannian Contrastive Learning) | 4.00 | R1-Mid | Limited novelty with straightforward combination of ideas. Our paper has stronger theoretical contribution. |

**Round 1 bracket:** The paper sits between 3.0 and 5.5, most likely in the 3.5–5.0 range.

**Round 2 (Narrowing)**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/.../PhanPLSHRt.md` (EXCOST Self-Training) | 4.00 | R2 | Better evaluation but limited performance improvement. Our paper is comparable — different weakness profiles. |
| `/home/.../fBlHaSGKNg.md` (UPA Sample Selection) | 4.00 | R2 | Similar quality level — incremental contribution with methodological concerns about missing comparisons. |
| `/home/.../X8RTdxzqJQ.md` (Two-sample Testing as SSL) | 4.80 | R2 | Stronger — adopts a fresh perspective on an established problem. Our paper is weaker in evaluation. |
| `/home/.../kaZAKvjLro.md` (Semi-supervised Long-tailed) | 3.50 | R2 | Weaker evaluation and less clear contribution. Our paper has a stronger theoretical component. |

**Final score determination:** The paper's concrete mathematical derivation (the margin ratio result) lifts it above the 3.0–3.5 level. However, the severe evaluation issues — most critically an unfair semi-supervised vs. supervised comparison and missing comparisons against the very methods it claims to improve — prevent it from reaching the 4.5–5.0 level of the better-calibrated anchors. The score of 4.0 reflects a paper with a genuine but narrowly-scoped theoretical contribution whose empirical evidence is undermined by an evaluation protocol that does not support the claims made.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>