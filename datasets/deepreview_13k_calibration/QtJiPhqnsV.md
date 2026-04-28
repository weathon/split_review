# Inferences on Covariance Matrix with Blockwise Correlation Structure

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 5, 6

## Abstract
Utilizing the sample moments of variable means within groups, we develop a novel closed-form estimator for blockwise correlation matrix of $p$ variables.
When the block number and group memberships of the variables are known, we demonstrate the asymptotic normality of parameter estimators and establish the stochastic convergence rate of the estimated blockwise correlation matrix and corresponding estimated covariance matrix, under certain moment conditions.
The method ensures positive semi-definiteness of the estimated covariance matrix without requiring a predetermined variable order, and can be applicable for high-dimensional data.
Moreover, to estimate the number of blocks and recover their memberships, respectively,
we employ the ridge-type ratio criterion and spectral clustering, and establish their consistency. Based on this, we extend the aforementioned properties of the asymptotic normality and stochastic convergence rate to the scenario where the group memberships are unknown and the block number is given.
Extensive simulations and an empirical study of stock returns in the Chinese stock market are analyzed to illustrate the usefulness of our proposed methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a method to estimate bock equicorrelation matrix, the number of blocks and recover their memberships. Theoretical results on asymptotic normality and stochastic convergence rate of parameter estimators are provided. Numerical experiments shows the effectiveness of the approach.

### Strengths
The paper is well-motivated and presents interesting theoretical results that justify the approach, making it applicable for high-dimensional data. The proposed method is computationally straightforward and addresses multiple aspects, including parameter estimation, block number estimation, and membership recovery.

### Weaknesses
1. The literature review on existing methods appears limited, which may lead to the proposed approach overlapping with established techniques. From the simple derivation below, the proposed blockwise correlation matrix estimation (BCME) in Equation (3) is closely related to Equation (12) in [1]. (Hat on $\hat{Y}$ is omitted due to compilation issue.)

$$
\frac{\frac{1}{n} \sum_{i=1}^n  
e_{p_{k_1}}^{\top} Y_{i}^{(S_{k_1})} Y_{i}^{{(S_{k_2})}^{\top}} e_{p_{k_2}} }{p_{k_1} p_{k_2}}
= \frac{
  e_{p_{k_1}}^{\top} \left( \frac{1}{n} \sum_{i=1}^n   Y_{i}^{(S_{k_1})} Y_{i}^{{(S_{k_2})}^{\top}} \right) e_{p_{k_2}} }{p_{k_1} p_{k_2}}
=  \frac{
  e_{p_{k_1}}^{\top} Cov(Y^{(S_{k_1}, S_{k_2})}) e_{p_{k_2}} }{p_{k_1} p_{k_2}}
= \frac{
 \sum_{i,j = 1}^N \rho_{ij} }{p_{k_1} p_{k_2}}
$$

Furthermore, the issue of positive definiteness mentioned in the Introduction is examined in Corollary 2 of [2].

2. The notation is not rigorous. $Y_i$ inconsistently denotes the random variable and realization (sample) of the random variable.

3. The technical conditions lack intuitive explanation, making it unclear how practical they are in real-world applications.

4. The experiments omit the turnover ratio, a significant metric in portfolio optimization analysis.

5. The topic somewhat diverges from the primary area of probabilistic methods.

### Questions
The paper could be improved by addressing the following points

1. Providing a comprehensive review of existing methods.

2. Using more rigorous and consistent notation.

3. Offering a clearer explanation of the intuition behind the technical conditions.

4. Reporting the turnover ratio for the portfolios.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new estimation method for the covariance matrix based on a clockwise correlation structure. The approach is straightforward: data from the same cluster are pooled and averaged as a single observation. The authors establish the asymptotic normality of the proposed estimator when cluster memberships are known for all data points. Additionally, they suggest using a spectral clustering algorithm, adapted from the network community detection literature, to identify cluster memberships. Overall, the paper is well-written, and the proposed methodology has potential applications in various fields.

### Strengths
The proposed method may be useful for many applications.

### Weaknesses
 A significant theoretical gap may exist in the paper: the clustering consistency of data memberships, discussed at the end of Section 2.2, may not be sufficient to guarantee the asymptotic normality stated in Theorem 1. The paper's idea is essentially simultaneous clustering and estimation of a covariance matrix. Such an idea has been studied in some recent relevant literature; see, e.g., [1], [2], [3], [4]. I think it will be helpful to discuss this line of research for a more complete picture. The main theorem, Theorem 1, assumes that the group memberships for all variables are fully known. Later in the paper, however, these memberships are estimated through spectral clustering, which is shown to be consistent. I’d like to highlight a potential issue: the consistency established in Lei and Rinaldo (2015) indicates only that the percentage of mis-clustered nodes converges to zero in probability. For Theorem 1's asymptotic normality to hold, the rate of convergence would need this mis-clustered percentage to decrease faster than $n^{-1/2}$ , which appears unachievable under current assumptions. Similar challenges are noted in references [2] and [3], but these works resolve the issue by establishing almost sure convergence for group membership estimation, which may also be necessary here. Please elaborate on this issue.

### Questions
Although the proposed methodology is simple and straightforward, I see potential for its usefulness in certain applications. Overall, my perspective on the methodology is positive. Below are some specific questions.

1. This paper's idea is essentially simultaneous clustering and estimation of a covariance matrix. Such an idea has been studied in some recent relevant literature; see, e.g., [1], [2], [3], [4]. I think it will be helpful to discuss this line of research for a more complete picture.

2. The main theorem, Theorem 1, assumes that the group memberships for all variables are fully known. Later in the paper, however, these memberships are estimated through spectral clustering, which is shown to be consistent. I’d like to highlight a potential issue: the consistency established in Lei and Rinaldo (2015) indicates only that the percentage of mis-clustered nodes converges to zero in probability. For Theorem 1's asymptotic normality to hold, the rate of convergence would need this mis-clustered percentage to decrease faster than $n^{-1/2}$ , which appears unachievable under current assumptions. Similar challenges are noted in references [2] and [3], but these works resolve the issue by establishing almost sure convergence for group membership estimation, which may also be necessary here. Please elaborate on this issue.

3. What happens if the estimated $\hat K$ is greater than the true $K$? Intuitively, it should still be ok as long as  $\hat K$ is finite. For example, in [2] and [3], the group estimators are still consistent even if $K$ is over-specified. Can you at least provide some simulation studies to investigate this issue? This would certainly add to the applicability of the proposed methodology.

References:

[1] Su, L., Shi, Z., & Phillips, P. C. (2016). Identifying latent structures in panel data. Econometrica, 84(6), 2215-2264.

[2] Liu, R., Shang, Z., Zhang, Y., & Zhou, Q. (2020). Identification and estimation in panel models with overspecified number of groups. Journal of Econometrics, 215(2), 574-590.

[3] Zhu, X., Xu, G., & Fan, J. (2023). Simultaneous estimation and group identification for network vector autoregressive model with heterogeneous nodes. Journal of Econometrics, 105564.

[4] Liu, W., Xu, G., Fan, J., & Zhu, X. (2024). Two-way Homogeneity Pursuit for Quantile Network Vector Autoregression. arXiv preprint arXiv:2404.18732.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper presents a closed-form estimator for the blockwise correlation matrix of variables that ensures positive semi-definiteness and is suitable for high-dimensional data. The authors demonstrate consistency and asymptotic properties without distributional assumptions and use spectral clustering to identify block structures. Their method is tested with simulations and applied to stock data from the Chinese market.

### Strengths
1- The problem solved by the authors are interesting 
2- The method comes with theoretical guarantees

### Weaknesses
The paper is challenging to read due to its dense presentation. The authors should make a substantial effort to improve clarity by introducing a dedicated notation section. This section should simplify the notations, provide clear definitions of each variable, and organize the symbols systematically for easy reference. Additionally, a more logical reorganization of the paper’s sections would enhance readability.

The experimental results are also difficult to interpret. The tables do not clearly indicate which method performs best; highlighting the best values in bold would improve clarity. Furthermore, the presentation of results would benefit from including statistical tests, such as p-values, to provide a more robust comparison between methods. Also the other should include more baselines as comparisons since a lot of covariance estimators have recently been developed in Random Matrix Theory and statistical physics ( linear and non linear shrinkage of ledoit Wolf,...)

### Questions
1- How does this method compared to other covariance estimator ( Linear and non linear shrinkage of Ledoit Wolf,...)?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a closed-form estimator for the blockwise correlation matrix of high-dimensional data without imposing specific distributional assumptions. By utilizing sample moments of variable means within known groups, the method ensures the positive semi-definiteness of the estimated covariance matrix without requiring predetermined variable ordering. The authors also introduce a ridge-type ratio criterion to estimate the number of blocks and employ spectral clustering to recover group memberships, proving the consistency of these approaches. Extensive simulations and an empirical study on Chinese stock market returns demonstrate the method's effectiveness.

### Strengths
1. The introduction of a closed-form estimator for the blockwise correlation matrix addresses the challenges posed by high-dimensional data, such as the singularity of the sample covariance matrix when $p > n$.

2. The paper provides thorough theoretical analysis, including proofs of asymptotic normality and convergence rates without relying on stringent distributional assumptions, enhancing the robustness and general applicability of the proposed method.

3. The method guarantees the positive semi-definiteness of the estimated covariance matrix without necessitating a predetermined variable order, overcoming limitations of some existing methods like the TP estimator.

### Weaknesses
1. While the empirical study shows that the proposed method outperforms existing methods in portfolio optimization, the paper lacks a clear explanation or theoretical justification for why this is the case. It remains unclear how the statistical properties of the proposed estimator translate into better portfolio performance.

2. The paper could offer more intuitive explanations or theoretical insights into why the proposed estimator is expected to perform better in applications like portfolio optimization. Connecting the methodological advancements to practical outcomes would enhance the paper's impact.

3. The comparisons in the empirical study are primarily with the TP method and the Ledoit-Wolf estimator. Including a wider range of contemporary high-dimensional covariance estimation methods in the comparison would provide a more comprehensive evaluation of the proposed method's performance.

### Questions
Please refer to the Weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a closed-form estimator for the blockwise correlation matrix by utilizing the sample moments of variable means within groups. It also addresses the scenario where the block number and group memberships of the variables are unknown.

### Strengths
The paper is well organized. It demonstrates the performance of the proposed method through both theoretical and numerical analyses.

### Weaknesses
1. In the abstract, the authors state that "without imposing any distribution assuptions". This statement lacks precision, as certain technical conditions are required. Specifically, the method likely relies on some form of moment conditions for the sample means and variances to converge to their population counterparts. The precise nature of these conditions should be stated explicitly, such as bounds on higher-order moments or sub-Gaussian tails. Without such assumptions, the theoretical guarantees of the estimator are not well-defined.

2. The notation is somewhat heavy, please consider improving the presentation for clarity. For example, the use of multiple subscripts and superscripts can be confusing. It would be helpful to introduce the notation more gradually and provide a clear glossary of all symbols used.

3. In Theorem 1, how should the convergence result be interpreted as the dimension $p$ approaches infinity? Discuss the possible connection with high-dimensional Gaussian approximation. The convergence rate should be explicitly stated in terms of $n$ and $p$, and it should be discussed whether the convergence holds under a high-dimensional regime where $p$ grows with $n$. The connection to high-dimensional Gaussian approximation should be clarified. Does the method rely on a specific sparsity structure or low-rank assumption in the covariance matrix?

4. Please provide references for the comparative methods in the experimental studies. Moreover, why are the results of BCME and TP exactly identical? It is crucial to understand the implementation details of the compared methods. The authors should provide the exact name and reference of the methods used, and explain why BCME and TP give the same results. This could be due to a specific implementation choice or a particular data structure.

5. What are the results under different values of $K$ with a fixed dimension $p$? The performance of the proposed method should be evaluated under different choices of the number of blocks $K$. It is important to see how the method behaves when $K$ is misspecified or when the true number of blocks is unknown.

6. It would be helpful to include an arrow indicating whether a larger metric corresponds to better performance. The direction of the metric should be specified to make the results interpretable. It should be clearly stated whether a larger metric means better or worse performance.

### Questions
1. In the abstract, the authors state that "without imposing any distribution assuptions". This statement lacks precision, as certain technical conditions are required.

2. The notation is somewhat heavy, please consider improving the presentation for clarity.

3. In Theorem 1, how should the convergence result be interpreted as the dimension $p$ approaches infinity? Discuss the possible connection with high-dimensional Gaussian approximation.

4. Please provide references for the comparative methods in the experimental studies. Moreover, why are the results of BCME and TP exactly identical?

5. What are the results under different values of $K$ with a fixed dimension $p$?

6. It would be helpful to include an arrow indicating whether a larger metric corresponds to better performance.

### Soundness
3

### Presentation
3

### Contribution
3
