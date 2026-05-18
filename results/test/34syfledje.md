Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes using feature discrimination (the ratio of inter-class to intra-class scatter, following Fisher's discriminant) as an alternative to quantization error for analyzing how binary and ternary threshold quantization affects classification. It derives explicit theoretical conditions (Theorems 1 and 2) under which quantization improves discrimination for a single Gaussian-modeled coordinate, and validates the predicted improvement across diverse domains (images, speech, text) with KNN and SVM classifiers.

## Strengths
- **Novel feature-discrimination framework for quantization analysis**: Instead of relying on quantization error (which lacks theoretical grounding for classification and contradicts the empirical observation that low-bit quantization can sometimes outperform full-precision data), the paper directly analyzes how quantization affects the ratio of inter-class to intra-class scatter. The paper explicitly states this is "the first study that exploits feature discrimination to analyze the impact of quantization on classification" (Section 1), providing a principled alternative to the signal-processing view.

- **Exact mathematical conditions for discrimination improvement**: Theorems 1 and 2 derive explicit inequalities (Eqs. 8 and 9) characterizing when binary and ternary quantization yield better discrimination than original data, under a Gaussian-per-coordinate model. These conditions are analytically derived and verified numerically (Figure 1 shows consistency between the theoretical threshold ranges and Monte Carlo estimates of D_b > D and D_t > D), giving concrete, checkable criteria that prior work lacked.

- **Extensive, multi-domain empirical validation**: Experiments span five real-world datasets across images (YaleB, CIFAR10, ImageNet1000), speech (TIMIT), and text (Newsgroup), using two linear classifiers (KNN with Euclidean and cosine distances, SVM with linear kernel). Across all domains, the experiments show that within specific threshold ranges, quantized data achieves higher classification accuracy than the original full-precision data (Figures 4–6, 13, 14, 21). The paper also demonstrates extension to multiclass (ImageNet1000, Figure 22) and nonlinear classification (MLP, decision trees, Figures 19–20).

- **Discovery of ternary quantization's broader applicability**: The theoretical analysis reveals ternary quantization can improve discrimination for a wider range of class separability (μ ∈ (0.66, 1)) than binary quantization (μ ∈ (0.76, 1)), consistent across synthetic and real-data experiments. This provides practical guidance for method selection.

## Weaknesses

### Fatal
None.

### Major
- **The element-wise theoretical results are not formally connected to the vector-level experimental claims**. The paper's entire theoretical apparatus (Theorems 1 and 2, numerical analysis) operates on a single coordinate modeled as X ~ N(μ, σ²), Y ~ N(-μ, σ²). The paper justifies this by claiming "the discrimination between the two random vectors **X** and **Y** positively correlates with the discrimination between their each pair of corresponding elements" (Section 2.2), but this statement is presented as a heuristic rather than proven. The definition of vector-level discrimination (ratio of sums across coordinates) does not decompose cleanly into independent per-coordinate discrimination ratios. While the paper's empirical validation on synthetic and real data partially bridges this gap — showing the predicted improvement does occur at the vector level — the theoretical framework does not formally explain why or under what precise conditions element-level improvement translates to vector-level improvement. The paper would be stronger with a formal argument (e.g., under independent coordinates or via a bound) showing how the per-coordinate analysis aggregates.

### Minor
- **The parameter regime for improvement is narrow and not explicitly checked on real data**. The analysis shows that binary quantization requires μ ∈ (0.76, 1) and ternary requires μ ∈ (0.66, 1) for any threshold to improve discrimination (Section 3.2). The paper acknowledges this ("the improved discrimination tends to be achieved when μ is sufficiently large") and claims that "as depicted in Figure 17, the two specific ranges of μ values are attainable for the commonly-used features of real data." However, the paper does not report the actual estimated μ values for the real datasets used in its experiments, making it difficult to verify that the theoretical conditions are satisfied. Including such an analysis would substantially strengthen the connection between theory and practice.

- **The claim about {0,1}-binary and {-1,1}-binary equivalence is underspecified**. The paper states (Section 3.1, Remark 3) that the conclusion for {0,1}-binary quantization "also applies to another popular {-1,1}-binary quantization, since the Euclidean distance of the former is equivalent to the cosine distance of the latter." While the Euclidean distances are proportional (differing by a factor of 4, preserving KNN ordering), the claim about equivalence to cosine distance on the latter is not elaborated. This remark would benefit from a brief clarification.

- **No robustness analysis for violations of the Gaussian assumption**. The theory assumes equal-variance Gaussian classes with symmetric means after standardization. Real data will violate all three assumptions. While the paper acknowledges this ("real data usually cannot" conform perfectly to the distribution conditions, Section 4, and "each data class does not adequately conform to the Gaussian distribution assumption," Section 4.2.2), it does not provide any sensitivity analysis (e.g., simulations with skewed or heavy-tailed distributions, unequal variances) to assess how robust the predicted improvement is to deviations from the model.

- **Choice of τ for real data requires held-out search**. The paper uses a scaling parameter γ and searches over it on held-out data (τ = γ·η). While the bisection method is mentioned for the theoretical setting, no practical guidance is given for selecting τ efficiently on real data without exhaustive search. This limits immediate practical utility.

### Trivial
None that survive filtering.

## Nice-to-Haves
- A formal bound or argument connecting element-wise discrimination improvement to vector-level discrimination improvement (e.g., under coordinate independence, or via a ratio-of-sums inequality).
- Reporting the empirical distribution of |μ_i| (estimated from the real feature vectors used in experiments) to directly verify that they fall in the predicted ranges.
- A synthetic-data simulation studying how violations of the equal-variance or Gaussian assumption affect the improvement threshold.
- Providing a simple heuristic for selecting the quantization threshold τ without exhaustive search on held-out data.

## Removed Points
- **Missing proofs in appendix**: The reviewer criticized the absence of proofs for Theorems 1 and 2. Per reviewer instructions, the parser strips appendix sections from all papers; these proofs exist in the original submission and this criticism is not valid.
- **"The theory does not predict the experimental results" (overall fatal framing)**: The reviewer argued that because the theory is element-level and the experiments are vector-level, the paper's core explanatory claim is unsupported. This overstates the issue — the paper's empirical validation on synthetic data (which strictly follows the distributional assumptions) and extensive real-data experiments provide evidence that the predicted improvement generalizes, even if the formal bridge is heuristic. The gap is real and noted above (Major), but it does not invalidate the paper's contribution.

## Novel Insights
The most interesting tension that emerges from these reviews is that the paper's theoretical apparatus is deliberately narrow (single coordinate, known-variance Gaussians, equal class balance) yet the empirical results are surprisingly robust across datasets that violate almost every assumption. The harsh critic correctly identifies this as a gap, but a different interpretation is possible: the paper may have identified a phenomenon more general than its theory currently covers, and the narrow assumptions were analytical convenience rather than essential preconditions. This makes the work a promising foundation — the theory explains *a* mechanism (noise reduction in discriminative coordinates via thresholding), and the empirical results suggest this mechanism operates even when the strict assumptions are relaxed. What the paper needs is not to reject its approach, but to make the bridge more explicit in a revision.

## Suggestions
1. **Add a formal connection from element-level to vector-level discrimination**: At minimum, show that under independent coordinates, the vector-level discrimination is a ratio of sums where the numerator and denominator each decompose across coordinates, and argue (or bound) how per-coordinate improvements aggregate. This would not require new theorems but would significantly strengthen the paper's core explanatory claim.
2. **Report empirical μ values**: For real datasets, estimate the per-coordinate class separability |μ_i| from the features used in experiments and show that a sufficient fraction falls in the predicted ranges (μ > 0.66 for ternary, μ > 0.76 for binary). This directly connects the theoretical condition to the experimental setting.
3. **Add a robustness simulation**: Test the theoretical predictions under unequal variances, non-Gaussian distributions, and unbalanced class proportions to characterize how the improvement thresholds degrade under assumption violations.
4. **Clarify the {0,1} vs {-1,1} claim**: Briefly state the proportionality of Euclidean distances (factor of 4) and, if the cosine claim is needed, provide the explicit relationship.

## Score and Decision

**Originality**: High — feature discrimination as a direct metric for quantization analysis is novel.
**Importance of research question**: High — addresses a genuine gap (why low-bit quantization can improve classification despite high quantization error).
**Claims support**: Moderate — theoretical claims are well-supported for the element-level setting; the connection to vector-level experiments is heuristic but empirically validated.
**Soundness of experiments**: Good — extensive evaluation across domains, classifiers, and both synthetic and real data.
**Clarity of writing**: Adequate — generally clear but could benefit from tightening the connection between theory sections and experimental sections.
**Value to research community**: Good — provides a new perspective that could inform quantization method design.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>