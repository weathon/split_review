## Summary

This paper proposes Covariance-Adjusted SVM (CSVM), which uses class-specific Cholesky decomposition of covariance matrices to "whiten" data before applying SVM. The authors argue that standard SVM's Euclidean-distance-based formulation is invalid in "non-Euclidean" input spaces where Mahalanobis distance is more appropriate, and that class-specific whitening yields two separate classifiers whose margin ratio depends on class covariances. An iterative algorithm (SM Algorithm) is proposed to estimate population covariances from training data. Experiments on five benchmark datasets compare CSVM against linear, RBF, sigmoid, polynomial SVMs, and PCA/ZCA whitening.

## Strengths

- **Correct identification of a practical issue**: Standard SVM ignores within-class covariance structure, and there is genuine value in incorporating class dispersion information into margin-based classification. The empirical results, while weak, are directionally consistent with this intuition.

- **Honest acknowledgment of limitations**: The paper explicitly notes that the SM Algorithm is heuristic, that population covariance is unknown, and that computational complexity is higher than linear SVM. This transparency is commendable.

- **The mathematical link between Mahalanobis distance and Cholesky decomposition (Eq. 1) is correctly stated**: For a single class, the derivation showing that Mahalanobis distance can be expressed as Euclidean distance after whitening by Ψ⁻¹ is standard and valid.

## Weaknesses

### Major

- **Fundamental conceptual confusion about "non-Euclidean" spaces undermines the theoretical framework.** The paper claims that standard SVM is invalid in "non-Euclidean" input spaces and that "KKT boundary conditions are not valid" there (Lemmas 2.1, 2.3). The input space of SVM is ℝ^d with the standard dot product — it is Euclidean by construction. The fact that Mahalanobis distance may be a more appropriate similarity metric does not make the space non-Euclidean; it simply means Euclidean distance is not the most informative metric for that data. The paper conflates *metric appropriateness* with *space geometry*. This category error propagates through the entire derivation (Lemmas 2.1–2.3) and the claim that the framework "addresses gaps in previous studies about vector space and dimensional inconsistencies" is built on this shaky premise.

- **Class-specific transformations are mathematically inconsistent with a single shared Euclidean space for SVM.** Equations (3) and (8) apply different transformation matrices Ψ⁻¹_{y=1} and Ψ⁻¹_{y=-1} to each class. The resulting "Euclidean space" is not a single space — points from each class are mapped by different linear operators, so distances between points of different classes are not well-defined under a common inner product. The SM Algorithm (step c) then performs SVM on data transformed by different operators per class, which is problematic because SVM's decision function θ^T x + θ_0 = 0 requires a single coordinate system. The paper's derivation gives two separate optimization problems (Eqs. 10–13), yet the algorithm reduces to a single adjusted bias without resolving this inconsistency.

- **Experimental results lack statistical rigor and are too weak to support the claimed superiority.** Tables 1–4 show small improvements (e.g., 0.974 vs 0.956 on Breast Cancer, 0.981 vs 0.979 on Pulsar). No error bars, confidence intervals, cross-validation, or statistical significance tests are reported. Without these, the observed differences could easily arise from chance. The most directly relevant baseline — class-wise whitening followed by linear SVM — is not included, making it impossible to attribute improvements to the proposed method's specific mechanism rather than to whitening in general.

- **The SM Algorithm is a heuristic disconnected from the mathematical derivation.** The paper derives two separate classifiers (Lemma 2.2, Eqs. 10–13) but the algorithm (steps d–e) uses a single bias adjusted by a ratio derived from the Euclidean-space θ vector. There is no theoretical justification for this reduction, no convergence analysis, and no sensitivity study. The algorithm's steps (transforming each class separately by different matrices, then running SVM on the transformed data) appear to ignore the very issue (non-comparable coordinate systems) that the earlier lemmas raise.

### Minor

- **Key experimental details are missing**: dataset sizes, dimensionality, hyperparameter selection for kernel SVMs (cost parameter C, kernel parameters), train/test split methodology beyond "80:20," and whether covariance matrices were checked for invertibility (necessary for Cholesky decomposition).

- **The paper overclaims the contribution relative to existing whitening approaches.** The claim that this work "addresses the limitations of previous studies done in variance adjusted SVM" by being "vector space and dimensionally consistent" is not substantiated — the related work section is too brief to establish what specific gaps are being filled (pp. 3–4).

### Trivial

- The ROC curves (Figures 1–3) are described in the text but visual inspection for fine-grained comparison is difficult.
- The paper uses nonstandard terminology ("statistical space") without explicitly contrasting it against standard usage, which could confuse readers.

## Nice-to-Haves

- A 2D synthetic data experiment showing the decision boundary and margins of CSVM vs. standard SVM would help illustrate the claimed covariance-adjusted margin ratio.
- Comparison against class-wise whitening + linear SVM (the direct ablation) would clarify whether the benefit comes from class-specific whitening or from the iterative SM Algorithm.
- Convergence analysis of the SM Algorithm (number of iterations, stability of label assignments, sensitivity to initialization) would strengthen the empirical contribution.

## Removed Points

- **Criticism about missing appendix sections or references**: The parser strips these; they exist in the original submission. *(Removed per hard rule)*
- **Criticism about the paper not "proving" KKT conditions are invalid**: The reviewer demanded a proof the paper does not provide, but the paper asserts this based on its (flawed) non-Euclidean premise — the weakness is better captured by the conceptual confusion issue above. *(Merged into Major weakness #1)*
- **Formatting/style nitpicks**: Pure presentation issues removed per hard rules.
- **Strength Finder's "theoretical foundation via vector space transformation"**: Conflicts with the verified conceptual confusion weakness. *(Removed per conflict rule)*
- **Strength Finder's "novel lemmas addressing fundamental limitations of KKT conditions"**: These lemmas are built on the contested non-Euclidean premise and are not independently novel. *(Removed per conflict rule)*
- **Strength Finder's "clear explanation of whitening's effectiveness"**: The explanation is based on the same conceptual confusion. *(Removed per conflict rule)*
- **Strength Finder's "iterative SM Algorithm for population covariance estimation"**: The algorithm is heuristic and the paper acknowledges this; calling it a strength overstates its rigor. *(Downgraded — moved here)*

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses converge on identifying a fundamental conceptual error in the paper's framing—the conflation of "appropriate metric" with "space geometry"—which is a clear and correct diagnosis, but it is a critique of the paper, not a novel observation arising from synthesis.

## Suggestions

1. **Reformulate the theoretical contribution**: Drop the incorrect claim that the input space is "non-Euclidean" and that KKT conditions are invalid. Instead, frame the method as a class-conditioned whitening preprocessing step for SVM, where the margin ratio naturally depends on class covariances. This is a weaker but defensible claim.

2. **Resolve the class-specific transformation issue**: Either use a single whitening transformation (e.g., pooled covariance) as standard practice does, or provide a mathematical justification for why distances between differently-transformed class points are meaningful in a common SVM formulation.

3. **Add statistical rigor**: Report results with error bars (cross-validation), significance tests, and the missing class-wise whitening baseline. Without these, the empirical claims are not convincing.

4. **Provide convergence analysis**: Even empirical convergence curves for the SM Algorithm would be helpful.

5. **Acknowledge the relationship to existing work more precisely**: Minimum Class Variance SVMs (Zafeiriou et al. 2007) and Mahalanobis-SVM variants already address similar goals; the paper should clearly state what is genuinely new beyond these.

## Score and Decision

**Comparative calibration (retrieved anchors):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/4i66VARUHD.md` (DIEM) | 2.0 | Comparable conceptual issue — both papers have a fundamental flaw in their core premise (DIEM's metric violates metric axioms; this paper's "non-Euclidean" premise is a category error). |
| `/home/wg25r/review_agent/human_reviews_2026/Oe5Min0Na2.md` (FINDER) | 2.5 | Similar overall quality — FINDER had weak novelty and insufficient empirical support; this paper has a more serious theoretical flaw but slightly more grounded experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/XQ0VTUIhEJ.md` (WSA) | 3.5 | This paper is substantially weaker — WSA had a coherent theoretical motivation and stronger empirical signal despite limited scale; this paper's theory is confused and its improvements are small and unvalidated. |
| `/home/wg25r/review_agent/human_reviews_2026/bp9DOHb1mk.md` (GDA) | 5.0 | Significantly stronger — GDA provides a coherent theoretical framework with rigorous experiments across 27 datasets; this paper lacks comparable rigor on both theory and experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/5S8ruWKe8l.md` (Cholesky SPD) | 5.0 | Far stronger — rigorous mathematical development with clear closed-form operators and thorough empirical validation, also using Cholesky decomposition but in a mathematically sound way. |

The paper's core theoretical premise is conceptually confused, the class-specific transformation creates an inconsistency the paper does not resolve, and the experimental results lack the statistical rigor needed to support the claimed advantages. These are structural issues that cannot be fixed by minor revisions.

MY FINAL SCORE: <pineapple>2.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>