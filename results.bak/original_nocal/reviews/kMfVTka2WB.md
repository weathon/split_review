Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes Covariance-adjusted SVM (CSVM), which uses class-specific Cholesky decomposition to transform data from "statistical space" (where Mahalanobis distance is natural) to Euclidean space, performs SVM there, and reverse-transforms to obtain a decision boundary in the original space. The key theoretical claims are: (1) class-specific margins depend on each class's covariance matrix, yielding a margin ratio (Eq. 14); (2) an N-class problem produces N linear classifiers in the input space (Lemma 2.2); (3) KKT boundary conditions are not directly applicable in the "non-Euclidean" input space. The paper also proposes the SM Algorithm — a semi-supervised iterative procedure to estimate population covariance from training samples and adjust the SVM intercept. Experiments on 5 binary datasets compare CSVM against linear, RBF, sigmoid, polynomial SVMs and PCA/ZCA whitening.

## Strengths

- **Mathematical derivation of class-specific margins (Eq. 8–14, Lemmas 2.2–2.3).** The paper analytically shows that when each class is whitened by its own Cholesky factor, the margin for each class in the original space becomes a function of its covariance matrix. The margin ratio in Eq. 14 is a concrete, algebraically derived consequence that distinguishes this approach from standard SVM's equal-margin assumption. This is a genuine theoretical contribution.

- **Explicit vector-space rationale for whitening.** The paper provides a self-contained derivation (Eq. 1–2) explaining that Mahalanobis distance equals Euclidean distance after a linear transformation (whitening), and positions SVM within this framework. This offers a cleaner vector-space explanation for why whitening aids SVM performance, which the paper correctly notes is often treated heuristically in the literature (Section 4).

- **Consistent empirical improvement on 4 of 5 datasets.** CSVM achieves the highest accuracy on Breast Cancer (0.974 vs. 0.956 linear), Diabetes (0.786 vs. 0.760), Red Wine (0.744 vs. 0.731), and Pulsar (0.981 vs. 0.979), and the highest or joint-highest AUC on 4 datasets (Figures 1–3). The improvements, while modest, are directionally consistent across diverse domains.

## Weaknesses

### Fatal
None.

### Major

1. **Misleading "non-Euclidean" framing that overstates the claims.** The paper repeatedly calls the input space "non-Euclidean" (e.g., Abstract, lines 19, 49, Lemma 2.1) and claims SVM "should not be valid" there. This is terminologically incorrect: the input space R^d with the standard Euclidean inner product *is* a Euclidean space. Mahalanobis distance is a different metric on the *same* underlying space, obtained by a linear transformation — it does not make the space non-Euclidean. The paper also overclaims that "KKT Boundary conditions are not valid" in the input space (Section 2) and that SVM "carries risk of misclassification" there (Section 6). These strong statements are not justified. The mathematical derivations (Eq. 8–14) are valid regardless of the label attached to the space, but the paper's framing and the rhetorical weight placed on it are misleading and undermine its credibility. *(Verifiable: lines 19, 49, Lemma 2.1, Section 6 claim (1).)*

2. **Gap between the theoretical derivation and the SM algorithm.** The paper derives two separate optimization problems (Eq. 10 for class y=1, Eq. 12 for class y=-1) and Lemma 2.2 states there are "two unique linear classifiers" for a binary problem. However, the SM Algorithm (Section 3) does not solve these derived problems. Instead, it takes the normal vector from a standard linear SVM trained on the *original* input-space data (step d) and heuristically adjusts only the intercept (step e) using a ratio computed from the Euclidean-space SVM. How this single-classifier intercept adjustment relates to the two-class optimization framework is never established. The algorithm is a heuristic applied *after* the theory, not derived *from* it. *(Verifiable: Eq. 10, 12; Lemma 2.2; SM Algorithm steps d–e, Section 3.)*

3. **Experimental validation lacks statistical rigor and omits a critical baseline.** (a) No standard deviations, confidence intervals, or significance tests are reported for any metric across the 5 datasets. The reported improvements are small (0.2–2.6 percentage points in accuracy), and without variance measures it is impossible to assess whether they are statistically meaningful. (b) The most natural baseline is missing: class-specific whitening (apply each class's Cholesky transformation to its own data, train a linear SVM on the combined whitened data). The paper compares against PCA and ZCA whitening applied to the *entire* dataset, which is a different operation. Without class-specific whitening as a control, it is unclear whether the SM algorithm's iterative procedure adds any value beyond a single round of class-specific preprocessing. (c) Kernel SVM hyperparameters (e.g., RBF γ, polynomial degree) are not reported, raising fairness concerns about the comparisons. *(Verifiable: Tables 1–4, no error bars; Section 5 experimental setup; Section 4 only compares against global PCA/ZCA.)*

### Minor

4. **SM algorithm is a heuristic with no analysis.** The algorithm is a semi-supervised self-training procedure (iteratively labeling test data, recomputing covariances, adjusting the classifier). The paper provides no convergence analysis, no discussion of confirmation bias (where incorrect early labels reinforce themselves), and no justification for the specific margin-ratio adjustment formula used in step (e). The paper acknowledges it is heuristic (Section 6), but does not analyze when it succeeds or fails. *(Verifiable: SM Algorithm steps, Section 6 limitations.)*

5. **Prior work criticized without explanation.** The paper states that prior variance-adjusted SVM studies (Huang et al., Zafeiriou et al., etc.) have "gaps in application of appropriate vector spaces and dimensional inconsistencies" (Section 1) but never explains what these inconsistencies are. This makes the criticism unverifiable and weakens the case for the paper's claimed novelty. *(Verifiable: lines 25–26, "dimensional inconsistencies" without elaboration.)*

6. **Claim about N-class extension is untested.** Lemma 2.2 derives N classifiers for N classes, but experiments are limited to binary datasets. The multi-class claim is a theoretical consequence that has no empirical support. *(Verifiable: Lemma 2.2, Section 5 only binary.)*

### Trivial
None.

## Nice-to-Haves

- Compare against MCVSVM (Zafeiriou et al., 2007) and other variance-aware SVM methods that the paper criticizes, to validate the claimed advantages.
- Provide synthetic-data experiments with known ground-truth covariance matrices to directly validate the margin-ratio formula (Eq. 14).
- Visualize decision boundaries on 2D synthetic data to illustrate how the margin split changes with class covariance.

## Removed Points

*These points were raised by reviewers but removed from the main review after cross-checking against the paper and applying filtering rules:*

- The criticism about ROC curve filenames looking "imported" (`a71911ad87414271aeb190e0eebcb989_img.jpg`, etc.) — this is a PDF extraction formatting artifact, not an issue with the submission. **Removed per formatting-artifact rule.**
- The claim that "the statement 'is the increase in classification performance worth the computational complexity?' is particularly damning" — this is the authors transparently stating a limitation, not a weakness. **Removed.**
- Criticisms about missing appendix content, missing proofs in appendix, or absent references — parser-stripped content. **Removed per rules.**
- The suggestion that compared baselines are unfair because asymmetry favors the author's method — the asymmetry (if any) favors the baselines, not CSVM. **Removed per hard rule.**
- Generic "reproducibility concern" about cited entities — all cited works, datasets, methods are assumed to exist. **Removed per hard rule.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface the disconnect between the theoretical framing and the algorithm, and the insufficiency of the experimental validation, but do not contribute a fundamentally new perspective on the problem.

## Suggestions

1. **Reframe the theoretical contribution.** Drop the "non-Euclidean" terminology. The paper's genuine contribution is deriving class-specific margin constraints from class-specific Cholesky whitening — present it as a *class-conditional metric learning* extension of SVM, not as a claim about the geometry of the input space.
2. **Derive the algorithm from the theory.** Either show how the SM algorithm's intercept adjustment follows from jointly solving the two optimization problems (Eq. 10 and 12), or simplify the contribution to class-specific whitening + SVM without the iterative SM procedure.
3. **Add the class-specific whitening baseline** — this is essential to determine whether the iterative SM algorithm adds value over one-shot whitening.
4. **Report statistical significance** (standard deviations across multiple splits, or p-values) for all metrics.
5. **Report hyperparameter choices** for kernel SVMs, especially RBF γ and polynomial degree.

## Score and Decision

The paper contains a genuine theoretical insight (class-specific margins as a function of class covariance, the margin ratio formula) and proposes a practical heuristic to address the population-covariance estimation problem. However, the misleading "non-Euclidean" framing overstates the contribution and undermines the paper's credibility. The experimental validation is substantially weaker than required for a top venue — no statistical significance, missing the most natural baseline (class-specific whitening), and unstated kernel hyperparameters. Most critically, there is a gap between the theoretical derivation (two optimization problems, two classifiers) and the algorithm (one classifier, heuristic intercept adjustment). These are not minor presentation issues; they are substantive gaps that prevent the paper from delivering on its claims.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>