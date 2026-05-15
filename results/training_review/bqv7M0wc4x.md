## Summary

This paper proposes ICL-TSVD, a method that bridges the gap between empirically strong CL approaches (RanPAC) and theoretically principled frameworks (Ideal Continual Learner, ICL). The key technical insight is that random ReLU features used by both RanPAC and ICL become highly ill-conditioned as more tasks are observed, causing numerical and generalization errors. ICL-TSVD addresses this via continual truncated SVD—preserving only the top singular values of the feature matrix before solving the min-norm ICL least-squares problem. The method is supported by theoretical bounds on training MSE and generalization error (Theorems 1 and 2) and demonstrates strong empirical results across 8 datasets, including challenging Inc-1 settings with hundreds of tasks.

## Strengths

- **Novel identification of the root cause of instability**: The paper provides compelling empirical evidence that ill-conditioning of the random ReLU feature matrix (emergence of extremely small eigenvalues) is directly correlated with accuracy collapse in both min-norm ICL and RanPAC (Figures 1–3). This spectral analysis is a key contribution that motivates the truncated-SVD solution in a principled way, rather than through heuristic regularization.

- **Principled continual SVD update with theoretical guarantees**: The continual SVD procedure (Algorithm 1, Equation 13) is a practical and scalable implementation that achieves \(O(E(k_{t-1}+m_t)^2)\) complexity versus RanPAC's \(O(E^3)\), while Theorems 1 and 2 provide explicit bounds on training MSE and test error in terms of the eigenvalue ratio \(\gamma_t\) and accumulated truncation error \(a_t\). These bounds capture the continual learning dynamics through a non-trivial recurrence relation (Lemma 2), going beyond existing offline PCR analyses.

- **Consistently strong empirical performance**: ICL-TSVD outperforms RanPAC and other baselines across 8 datasets in the main CIL setting (Table 1). The method is stable over a wide range of truncation percentages (Figure 4a), unlike RanPAC's sensitivity to \(\lambda\). The Inc-1 results (Table 2) are particularly striking—ICL-TSVD maintains high accuracy (average 77.65% final vs RanPAC's 66.00%) in the most challenging setting where RanPAC collapses on some datasets (e.g., StanfordCars: 74.44% vs 1.19%).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Linear model assumption limits the scope of theoretical guarantees**: The bounds in Theorems 1 and 2 assume \(\mathbf{Y}_{1:t} = \mathbf{W}_{\mathrm{gt}} \mathbf{H}_{1:t} + \boldsymbol{\varepsilon}\), where one-hot label vectors are modeled as a linear function of the random ReLU features plus noise. While this is a *stated* assumption (not "unstated" as the reviewer claims—see the "Model Assumption" paragraph, lines 251–257), the paper does not justify its validity for classification with one-hot labels beyond observing that empirical performance is good, which is somewhat circular. The theoretical results are rigorous under this assumption, but the gap between the assumption and the actual classification problem means the theory does not directly prove that the method will generalize well in practice. A discussion of conditions under which this assumption might approximately hold (e.g., wide enough features, or connection to universal approximation) would strengthen the paper.

2. **Empirical comparison to RanPAC confounds method and embedding dimension**: ICL-TSVD uses \(E=10^5\) while RanPAC uses its default \(E=10^4\). The paper argues this is fair because ICL-TSVD's greater efficiency enables the larger dimension, and shows that at matched \(E\), ICL-TSVD is 1000× faster. This is a reasonable position—comparing each method at its strongest feasible configuration—but it does mean the performance difference in Tables 1 and 2 cannot be cleanly attributed to the TSVD truncation alone. An ablation showing RanPAC with \(E=10^5\) (where computationally feasible) or ICL-TSVD with \(E=10^4\) would disentangle the effect of the algorithm from the effect of the embedding dimension and strengthen the claim of "uniformly outperforming."

3. **No variance or confidence intervals reported**: The paper reports single-run accuracy without standard deviations or confidence intervals. While this is common practice in some CL benchmarks, the large gap in Inc-1 results (e.g., StanfordCars 74.44% vs 1.19%) is so extreme that it raises questions about potential implementation issues with RanPAC on that dataset rather than a genuine algorithmic advantage. A study of what \(\lambda\) values cross-validation selected for the failure cases would clarify whether the issue is cross-validation failure or an inherent limitation of ridge regression.

4. **The bounds are expressed in terms of algorithm-internal quantities**: The quantities \(\gamma_t\) and \(a_t\) in Theorems 1 and 2 are defined in terms of eigenvalues of \(\widetilde{\mathbf{B}}_t\) (the algorithm's own approximation), not of the true data matrix \(\mathbf{H}_{1:t}\). The paper argues empirically that these are close (citing figures in the appendix), but there is no theoretical guarantee connecting \(\widetilde{\mathbf{B}}_t\)'s spectrum to the true data distribution. This means the bounds cannot be used to make predictions about generalization without additional empirical verification.

### Trivial
- The accuracy matrices in Figure 6 lack a colorbar, making them hard to interpret quantitatively.

## Nice-to-Haves
- Reporting RanPAC with \(E=10^5\) on a subset of datasets (e.g., CIFAR100 Inc-5, ImageNet-A Inc-5) to directly control for the embedding dimension.
- Comparing the continual SVD approximation against the offline full SVD truncation on small to medium datasets to validate the approximation quality quantitatively.
- Providing a theoretical analysis that bounds the excess risk under a weaker assumption (e.g., using random feature analysis to bound how well one-hot labels can be approximated by a linear model of random ReLU features).

## Removed Points
- **"Unstated" linear model assumption**: The paper *explicitly* states this assumption in a dedicated "Model Assumption" paragraph (lines 251–257). This is a factual error by the reviewer. The criticism about the assumption's validity is retained (see Minor weakness 1), but the claim that it is "unstated" is removed.
- **"ICL-TSVD's connection to ICL is misleading because it doesn't guarantee zero forgetting"**: The paper transparently describes that ICL-TSVD uses truncated SVD to *approximately* solve the ICL constraints, and the whole theoretical section bounds this approximation error. The paper does not claim ICL-TSVD guarantees zero forgetting—it claims the original ICL formulation prevents forgetting "by design" (line 66), and then proposes TSVD as a practical approximation. This criticism misreads the paper's own narrative.
- **Criticism about missing appendix content**: The parser strips appendix content. All appendices exist in the original submission.
- **Demand for a theoretical analysis without the linear model assumption**: This goes beyond what is standard for ML theory papers and would constitute a different paper. The softened version is moved to Nice-to-Haves.
- **Strength Finder's generic praise**: Dropped some generic phrasing from Strengths that lacked specific evidence.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's positioning and its actual contributions. The paper claims to "bridge theory and practice," but the theoretical analysis relies on a linear model assumption that is standard in the random features / PCR literature yet is not obviously satisfied by classification with one-hot labels. Meanwhile, the *empirical* contribution—identifying spectral ill-conditioning as the root cause of instability and fixing it through continual TSVD—is stronger than the theory might suggest. The practical finding that truncating a fixed percentage of singular values is robust across datasets, while ridge regularization parameter \(\lambda\) is dataset-sensitive, is a genuine insight that could influence CL system design beyond this specific paper. The continual SVD update (Equation 13) is a non-trivial algorithmic contribution that deserves recognition as a practical engineering solution, independent of whether the theoretical bounds are tight.

## Suggestions

1. Add a controlled experiment with matched embedding dimensions (either RanPAC at \(E=10^5\) for a subset or ICL-TSVD at \(E=10^4\)) to isolate the effect of the TSVD truncation from the effect of larger \(E\).
2. Add a brief discussion of when the linear model assumption might approximately hold (e.g., universal approximation properties of random ReLU features when \(E\) is sufficiently large, or connection to the fact that the min-norm solution still performs well empirically).
3. Report what \(\lambda\) values RanPAC's cross-validation selected on ImageNet-A Inc-5 and StanfordCars Inc-5 to clarify whether the poor performance is due to cross-validation failure or ridge regression's inherent limitations.
4. Add standard deviations or confidence intervals for the main results, especially for the striking Inc-1 comparisons.
5. Include the colorbar annotation on the accuracy matrices and clarify whether the values in Figure 6 are absolute accuracy or relative performance.

## Score and Decision

The paper makes a genuine contribution: it identifies a concrete cause of instability in CL with pre-trained models (spectral ill-conditioning), proposes a well-motivated fix (continual TSVD), provides non-vacuous theoretical bounds, and demonstrates strong empirical results. The weaknesses are real but not severe: the theoretical assumption is transparently stated (not hidden), the empirical comparison is partially but not fully controlled, and the lack of variance estimates is a presentation gap. These are issues that can be addressed in revision without altering the core contributions.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>