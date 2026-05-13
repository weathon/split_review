# Flat Minima in Linear Estimation and an Extended Gauss Markov Theorem

- Decision: Accept
- Scores: 6, 5, 6

## Abstract
We consider the problem of linear estimation, and establish an extension of the Gauss-Markov theorem, in which the bias operator is allowed to be non-zero but bounded with respect to a matrix norm of Schatten type.  We derive simple and explicit formulas for the optimal estimator in the cases of Nuclear and  Spectral norms (with the Frobenius case recovering ridge regression). Additionally, we analytically derive the generalization error in multiple random matrix ensembles, and compare with Ridge regression. Finally, we conduct an extensive simulation study, in which we show that the cross-validated Nuclear and Spectral regressors can outperform Ridge in several circumstances.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The Gauss-Markov theorem says that the best unbiased linear estimator is the pseudoinverse of the data matrix (in the paper denoted by $X$), which can be obtained by minimizing the Frobenius norm of the estimator $L$ subject to the constraint that $L$ is the left inverse of the data matrix, $LX=I$. The paper generalizes this formulation by relaxing this constraint to $||LX-I||_p\le C$ where $||\cdot||_p$ is the Schatten $p$-norm (vector $p$-norm on the singular values), thus allowing some bias $C$. A special case is the ridge/Tichonov regression, obtained for $p=2$. The parameter $C$ (or a monotonically related parameter $\alpha$) is determined by validation, by minimizing the test error. The advantage is that for $p\neq2$, the minimum of the test error over $C$ may be flatter than for $p=2$. 

The authors derive a closed form solution for the optimal estimator $L$ for $p=1$ (nuclear norm) and $p=\infty$ (spectral norm). Next, they derive explicit form (as integrals) of for the test error in thermodynamical limit for two special distributions of the data: spherical Gaussians (elements of $X$ and noise in right-hand sides are i.i.d. normal) and diagonal data (when the Gramian $X^TX$ is diagonal). The integrals are solved in closed form for $p=1$ and $p=\infty$. This theoretical formula is shown to agree with test error on synthetically generated data.

The cases $p=1,2,\infty$ are compared in a simulated experiment in which $\alpha$ with smallest test error is estimated by x-validation, where best $\alpha$ is selected by "grid search" from 9 log-spaced values. This showed that the nuclear-norm regression is comparable to or better than (depending on methodology) ridge regression. A similar result is obtained for the similar experiments for nonlinear regressors (random Fourier features).

### Strengths
The observation that a wider minima of $\alpha$ can be achieved at the cost of a little bias is interesting.
The theoretical results (test errors) are non-trivial to derive.
The text is clear enough, though clarity could be improved by more effort.

### Weaknesses
I cannot assess novelty reliably because my expertise is mainly in optimisation rather than estimation (however, I understand all parts of the main paper well). In fact, rather than extending Gauss-Markov theorem, the paper generalizes ridge regression (please, consider changing the title accordingly). It is well-known that ridge regression has non-zero bias but a smaller variance than pseudoinverse. So the main novelty seems to be that of flatter minima of test error, rather than the generalization of ridge regression.

Though the minima for the nuclear-norm regression are indeed flatter than for the ridge regression, the difference is sometimes only minor, as seen in Figure 2. It is true that the experiments show that in estimating $\alpha$ by x-correlation, the nuclear norm most often wins. However, this might be due to the experimental methodology. E.g., if there were more than 9 values of $\alpha$, the deeper minima of the ridge regression might have been hit much more often. The grid search for the optimal $\alpha$ is a crucial aspect of the experimental setup, and the limited number of values explored could significantly bias the comparison, especially if the ridge regression's error landscape is more sharply peaked than that of nuclear norm regression. This is a critical point that needs further investigation.

A major weakness, in my opinion, is that the experiments are done only on synthetic data. The applications of linear regression are abundant, so it should be possible to find many suitable real datasets for this. The lack of real-world data limits the practical relevance of the findings. It is unclear how the observed trends would translate to real-world scenarios where the data distribution might be far from the assumed Gaussian or diagonal structures.

Minor/fixable issues:

1st formula in section 2.1: symbol $L(X)$ is used here but then never more. Change to $L$.

Thm 2: Letter $\Sigma$ is usually used to denote the diagonal matrix with singular values. For vector of singular values, better use $\sigma$ or $s$.

There are many small mistakes/typos in the text. E.g., references to figures in sections 2.2.4 and 3 refer to non-existent figures (e.g., figure 2.2.4 in section 2.2.4).

In the 5th line of section 2.2.1, can the formula for MSE be simplified (i.e., calculate the mean value in closed form)? It is confusing that the MSE has quite different form in sections 2.2.1 and 2.2.2 (this lets the reader wonder if this difference is substantial or just due to little care for text clarity). This might deserve a comment.

Most displayed equations are unnumbered, which is not friendly for reviewers (given that lines are not numbered in the ICLR style).

The asterisk symbol in Proposition 2.1 and in the first displayed formula in section 2.2.2 has not been defined.

The integrals for $Err(\alpha)$ in sections 2.2.1 and 2.2.2 are almost the same, up to the integrating measures. I wonder if they are correct or there are typos in them..?

### Questions
It would be helpful to vary the number of values of $\alpha$ in the grid method (currently this value is 9) in the experiments, i.e., to make it a hyperparameter. Pls see my remark on this in "weaknesses".

It would be helpful in Figure 5 to report not only winners but also MSE for different models (as in Figure 6 left) - because a winner can win by only a small margin.

Why are any experiments on real data not included? Is there a theoretical obstacle? Or, perhaps, you believe that the results of such experiments would not be informative enough? Please comment (also in the paper, if accepted).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers a variant of linear regression with constraints placed on a "bias operator". Under this framework, the paper discusses an extension of the Gaussian-Markov theorem, showing empirical and theoretical evidence for its main result, Theorem 2. Later discussions in the paper surround "flatness" and "deepness" of various losses considered within the paper.

### Strengths
The paper tackles an interesting class of linear regression models and delivers a thorough presentation of various aspects of the problem, from the problem definition, main theorem statement, to several case studies, all of which help to paint the overall picture of the problem. The constrained setup considered in the paper is also interesting and intuitive. Considering that linear models are a core concept of machine learning, the paper is of sufficient interest to ICLR.

### Weaknesses
There are several dimensions of weaknesses presented in the paper:

a. Clarity and overall quality of presentation. The paper does not appear to be carefully edited and revised, with multiple typographical errors in the first paragraph of the introduction alone (examples: "somewht" in line 3, lack of period at end of sentence in line 4, reverted quotation marks on line 5, etc.). The graphs, equations, and tables in latter parts of the paper can also benefit from detailed revisions. These issues surrounding clarity and presentation are not constrained to the first paragraph and can be found throughout the paper and also the supplementary material.

b. Discussion of main theorem. While the problem setting itself is interesting, the discussions of the main theorem (Theorem 2) leave an impression that it can be further discussed. For example, what are the values of alpha? Although it is shown in the supplementary that alpha is a consequence of solving Equation 1 using Lagrange multipliers, it is also unclear how large (or small) the value of alpha is and how it impacts the interpretations of the main result. The paper does not provide sufficient intuition for how the constraint parameter C relates to the resulting alpha, and how this relationship impacts the final solution.

c. Considering that one of the paper's main claims is a "flat minima" phenomenon, the paper would benefit from stronger theoretical results (apart from simulation-based arguments) surrounding this claim. The paper's analysis of flatness relies heavily on empirical observations, and lacks a rigorous theoretical framework to support the claim. The connection between the observed flatness and the specific constraints imposed on the bias operator is not sufficiently explored.

d. Possible typo in main theorem. In the main theorem's statement for the nuclear norm, the result relies on $\max(\Sigma,\alpha)$: should $\Sigma$ be replaced with something like the maximum eigenvalue? The use of element-wise maximum between a matrix and a scalar is unconventional and requires further clarification. It is not immediately clear how this operation is defined and what its implications are for the theorem's result.

### Questions
Several questions were listed in the above "weaknesses" section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the trade-off between the variance (MSE) and bias (bias norm) for the regularized linear regression model, where the authors consider various Schatten norms for the regularized term. Then, the authors derive the expected MSE for the Gaussian and diagonal ensembles and compare it with the ridge regression model's one and show that the ridge regression model is not always the best in term of the trade-off by using some experiments on sythetic datasets.  There exit some similar works such as Bayatti and Montanari (2011), Samet et al. (2013) for Lasso, however the authors limit their work to the class of Schatten norms.

### Strengths
+  The authors can obtain an exact expression for the average test error (MSE) for the spherical Gaussian model, and this bound is nearly matched to the experiment results (cf. Figure 2).
+ Experiments show that Ridge regression, which used Frobenius norm, is not always the best option for the linear model in term of the trade-off between the variance (MSE) and the bias (the bias norm). More specifically, the authors show that the Frobenius norm and the nuclear one are likely to have the same average MSE on the spherical Gaussian ensemble (model) or the diagonal matrix model, but using the nuclear norm usually achieves better MSE than the Frobenius norm. This fact also holds when mapping the dataset via a random fourier transform (RFF).

### Weaknesses
 +  The theoretical results only hold in the thermodynamic limit $N\rightarrow \infty, d \rightarrow \infty$ and $d/N\rightarrow \lambda$. This means that the results only hold when the number of observations is linear to the signal dimension. However, in common high-dimensional settings, the number of observations is usually sub-linear to the signal dimension. This severely limits the practical applicability of the theoretical findings, as many real-world datasets do not conform to this asymptotic regime. The analysis should explicitly address this limitation and discuss the potential impact on the conclusions when applied to finite-sized datasets, where the derived bounds may not hold.
+ The result looks not an extension of the Gauss-Markov theorem since it only holds under expectation over $X$ when $X$ is an Gaussian ensemble or a diagonal ensemble. The Gauss-Markov theorem works for any $X$. The reliance on specific distributions for $X$ significantly restricts the scope of the theoretical results. The authors should clarify that the presented results are not a generalization of the Gauss-Markov theorem, but rather a specific analysis under particular distributional assumptions. A discussion on how these assumptions affect the applicability of the results would be beneficial.
+ It looks more interesting to compare your experiment results with other norms (outside the class of  Schatten norms) such as between the nuclear norm and Lasso (norm-$1$). The lack of comparison with other regularization techniques, particularly those outside the Schatten norm family, limits the impact of the experimental results. A comparison with Lasso, which promotes sparsity, would provide a more comprehensive view of the performance of Schatten norm regularization. This comparison would be especially relevant given the frequent use of Lasso in high-dimensional settings.
+ Too many typos. Please check and correct them.

### Questions
How do your results in comparison with other norms which don't belong to Schatten class of norms such as Lasso (norm-$1$)?

Besides, please check and correct the following typos and unprecise.

+ $L \in \mathbb{R}^{k \times N} \rightarrow L \in \mathbb{R}^{d \times N}$
+ p.2, line 21 from the top: $\mbox{var}\_{\epsilon}=L^T L$ should be changed to $\mbox{var}\_{\epsilon}=\sigma^2 L L^T$. To keep the later, you may change the definition of $\hat{\beta}$ to $L^T(X)Y$ throughout your paper.
+ In the definition 1, you aim to minimize the variance subject to a constraint on bias by $C$. But, in the later (Theorem 2, Figure 1, etc.), it seems to me that you don't mention $C$ again, but only mention $\alpha$. At least you should mention what is $\alpha$ as a function of $C$ or vice versa in Theorem 2.
+ In Figure 1, you only plot for the very special case when $X$ is diagonal. You should also plot for other cases of $X$. 
+ Typo in Theorem 2.1, the expectation should be over $\epsilon$ only since you already take expectation over $X$ in MSE, and $Y$ is a function of $X$ and $\epsilon$. 
+ Right below Figure 2: Figure 3.1 $\rightarrow$ Figure 3. 
+ Similarly, Figure 3.2.1 $\rightarrow$ Figure 5.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
