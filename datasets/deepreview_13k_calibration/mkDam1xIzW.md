# Probabilistic Geometric Principal Component Analysis

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
Dimensionality reduction is critical across various domains of science including neuroscience.  Probabilistic Principal Component Analysis (PPCA) is a prominent dimensionality reduction method that provides a probabilistic approach unlike the deterministic approach of PCA and serves as a connection between PCA and Factor Analysis (FA). Despite their power, PPCA and its extensions are mainly based on linear models and can only describe the data in a Euclidean coordinate system around the mean of data. However, in many neuroscience applications, data may be distributed around a nonlinear geometry (i.e., manifold) rather than lying in the Euclidean space around the mean. We develop Probabilistic Geometric Principal Component Analysis (PGPCA) for such datasets as a new dimensionality reduction algorithm that can explicitly incorporate knowledge about a given nonlinear manifold that is first fitted from these data. Further, we show how in addition to the Euclidean coordinate system, a geometric coordinate system can be derived for the manifold to capture the deviations of data from the manifold and noise. We also derive a data-driven EM algorithm for learning the PGPCA model parameters. As such, PGPCA generalizes PPCA to better describe data distributions by incorporating a nonlinear manifold geometry. In simulations and brain data analyses, we show that PGPCA can effectively model the data distribution around various given manifolds and outperforms PPCA for such data. Moreover, PGPCA provides the capability to test whether the new geometric coordinate system better describes the data than the Euclidean one. Finally, PGPCA can perform dimensionality reduction and learn the data distribution both around and on the manifold. These capabilities make PGPCA valuable for enhancing the efficacy of dimensionality reduction for analysis of high-dimensional data that exhibit noise and are distributed around a nonlinear manifold, especially for neural data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this work, the author proposes a Probabilistic Geometric Principal Component Analysis (PGPCA) method which can be seen as an extension of PPCA with a better description of data distributions by incorporating a nonlinear manifold geometry. A data-driven EM algorithm is also proposed to solve the PGPCA problem. Experimental results verify the performance of the PGPCA is better than that of PPCA.

### Strengths
The method and algorithms are technically sound, with reasonable insights and solutions.

### Weaknesses
Comparison with other nonlinear PPCA methods is not provided.

### Questions
1. As some works focus on nonlinear PPCA, such as 

Lawrence, Neil, and Aapo Hyvärinen. "Probabilistic non-linear principal component analysis with Gaussian process latent variable models." Journal of Machine Learning Research 6.11 (2005).

Zhang, Jingxin, et al. "An improved mixture of probabilistic PCA for nonlinear data-driven process monitoring." IEEE transactions on cybernetics 49.1 (2017): 198-210.

how is the performance of the proposed PGPCA compared with these nonlinear PPCA methods?


2. How does PGPCA compare with other methods in terms of computational efficiency?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper's main idea is the PPCA extension containing nonlinear manifold terms. The reason for this assumption is not clear. 
But the formulation and mathematical analysis are true.
Also, its performance should be seen in real data. However the experiments on real data are not clear and also they should apply it for more general data like well-known image data sets, or at least mention the class of real data that this method can work well for them in comparison with PPCA. By this version of experiments the importance and quality of the proposed method are not clear.
Also, they should report the complexity of the proposed method.

### Strengths
The writing is good and also the mathematics are true.

### Weaknesses
The paper's main idea is the PPCA extension containing nonlinear manifold terms. The reason for this assumption is not clear. 
But the formulation and mathematical analysis are true.
Also, its performance should be seen in real data. However the experiments on real data are not clear and also they should apply it for more general data like well-known image data sets, or at least mention the class of real data that this method can work well for them in comparison with PPCA. By this version of experiments the importance and quality of the proposed method are not clear.
Also, they should report the complexity of the proposed method.

### Questions
_ experiments for real data should be done?
what is the specific class of data that this idea works good?
why they did not report the complexity?
if they report one can compare them with methods like deep factor models

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a generalization of probabilistic principal component analysis (PPCA) to data that lies on a (nonlinear) manifold rather than in Euclidean space around the mean. 

The key contributions of the paper are (i) the introduction of the PGPCA model, (ii) an expectation-maximization algorithm to fit the proposed model and (iii) empirical experiments with real and simulated data to compare PGPCA with vanilla PPCA.

### Strengths
- The problem of dimensionality reduction for data on a manifold is well motivated, and the proposed method closes the gap between PPCA and data on manifolds. 
- The proposed extension PPCA is innovative and well explained.
- The mathematical derivation of the EM-algorithm is concise and understandable, and the empirical experiments show promising results.

### Weaknesses
 - The simulated data seems to be favorable for PGPCA compared to PPCA as it lies on non-linear manifolds. It remains open how well PGPCA compares to PPCA for data in other settings, e.g. in linear subspaces. Specifically, it is unclear how the method would perform if the data were generated from a distribution where the underlying manifold is actually a linear subspace, or a space very close to it. The paper should include experiments to demonstrate the performance of PGPCA in such scenarios.
- PGPCA is only compared to PPCA and not other - potentially stronger - baseline methods. Especially, comparisons with other dimension reduction methods for data on manifolds is missing. For example, methods such as Isomap, Laplacian Eigenmaps, or diffusion maps, which are designed for manifold learning, should be included in the comparison. This is a significant oversight, as it is not clear if PGPCA offers any advantage over these existing methods.
- The evaluation on real data is rather limited. Only brain signals of two mice were used. The paper should include more real-world datasets to demonstrate the general applicability of the method. The current evaluation is insufficient to make strong claims about the practical relevance of PGPCA.

### Questions
- Please add literature on dimensionality reduction for data on a manifold.
- How well does PGPCA work with other choices of $K(z)$ than geometric and Euclidean?
- What theoretical guarantees for the hypothesis test on EuCOV vs. GeCOV are there? (e.g. in terms of statistical power/or asymptotic level)
- How does PGPCA compare to PPCA for data in linear subspaces?
- How does PGPCA compare against stronger competitors?
- How well does PGPCA work on other real data?
- Can the i.i.d. assumptions in model (1) be relaxed? E.g. by allowing (temporal) dependence or slightly varying distributions?
- Can the assumption of normality be relaxed to allow for non-normal errors?

### Soundness
3

### Presentation
3

### Contribution
3
