# Asymptotically Free Sketched Ridge Ensembles: Risks, Cross-Validation, and Tuning

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
We employ random matrix theory to establish consistency of generalized cross validation (GCV) for estimating prediction risks of sketched ridge regression ensembles, enabling efficient and consistent tuning of regularization and sketching parameters. Our results hold for a broad class of asymptotically free sketches under very mild data assumptions. For squared prediction risk, we provide a decomposition into an unsketched equivalent implicit ridge bias and a sketching-based variance, and prove that the risk can be globally optimized by only tuning sketch size in infinite ensembles. For general subquadratic prediction risk functionals, we extend GCV to construct consistent risk estimators, and thereby obtain distributional convergence of the GCV-corrected predictions in Wasserstein-2 metric. This in particular allows construction of prediction intervals with asymptotically correct coverage conditional on the training data. We also propose an ``ensemble trick'' whereby the risk for unsketched ridge regression can be efficiently estimated via GCV using small sketched ridge ensembles. We empirically validate our theoretical results using both synthetic and real large-scale datasets with practical sketches including CountSketch and subsampled randomized discrete cosine transforms.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is about the (asymptotic) consistency of generalized cross validation (GCV) for estimating prediction risks of sketched ridge regression ensembles using tools from random matrix theory. 

For general subquadratic prediction risk functionals, they extend GCV to construct consistent risk estimators, and obtain distributional convergence of the GCV-corrected predictions in Wasserstein-2 metric.

Although the consistency result seems intuitive and natural, they point out that GCV of the observation sketched ridge regression, is inconsistent, highlighting the subtlety of this subject.

### Strengths
This paper presents the theorems in a clear and rigorous way. All notations are presented again on a table in appendix. Theoretical result is supported by experimental result.

### Weaknesses
No major weakness is spotted.

Asymtpotic freeness seems to be an essential assumption in the paper. Although this assumption is experimentally supported by artifical datasets, I wonder if one can observe similar matching on real-world dataset.

### Questions
Asymtpotic freeness seems to be an essential assumption in the paper. Although this assumption is experimentally supported by artifical datasets, I wonder if one can observe similar matching on real-world dataset.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Motivating by hyparameter tuning (size of the ensemble, size of the sketches), this paper studies the statistical properties of Generalized-Cross-Validation applied on an ensemble of sketched ridge regressors with skecthing applied to the feature space. First, the authors develop squared risk asymptotics and provide consistency results (Thoerem 2) and then, extend these results to subquadratic error functionals (Theorem 3). These findings hold for the general class of asymptotically free sketching matrices. At the origin of the study, is a key theorem (LeJeune et al. 2022), that states that the sketched inversion of a sketched regularized matrix corresponds to the inversion of the initial regularized matrix with another hyperparameter. This gives rise to Theorem 2 that nicely relates the quadratic risk of the ensemble-based estimator to the risk of the rigde estimator plus a randomness term depending on the sketch via Theorem 1 and the so-cllaed S-transform. Moreover, functional and distribution consistency for general error functional are also proved. Simulations on toy and real data shown in the main paper and appendix confirm the interest of the approach for tuning both the regularization level (or sketch size in fine) and the size of the ensemble.

### Strengths
First of all, I would like to say that this is a very nice paper, very well written, solid and with a strong and insightful content. I have learned a lot when reading it.
The main strengths of the paper is its depth of view not only about GCV (which has a simple form) but also about the link between sketched ridge regression and regualrization in ridge regression, and the role of the ensemble trick. 
I appreciated the richness of the discussion and the comments all along the paper.
Originality is also present here, with the exploitation of very recent results (LeJeune et al. 2022) but with a special angle here (GCV).

### Weaknesses
 * Improvment of clarity in Assumption 2 statement and explanation. 
The paper has the merit to introduce elements of free probability theory useful in Assumption 2. I regret not to have more intuition here: I can easily imagine that a form of independence (I've read the appendix) between $X^TX$ and $SS^T$ is useful but the notion of limiting S-transform is not at all discussed at this stage (page 4) and Assumption 2 remains not clear at all when beginning to read what follows. Specifically, the assumption requires the existence of a limiting S-transform but does not provide any insight into what this implies about the structure of the sketching matrix S, beyond the asymptotic freeness. This makes it difficult to assess the practical implications of this assumption. The connection between the asymptotic freeness and the rotational invariance of the sketching matrix, while mentioned in the appendix, should be more explicitly stated in the main text to improve clarity. Same thing for Theorem 1, describe the $|ambda^+$ function. The description of $\lambda^+_{min}$ as the minimum non-zero eigenvalue is not immediately clear, especially in the context of the sketched matrix. It would be beneficial to explicitly state why the zero eigenvalues are irrelevant in this context and how the sketched inversion effectively handles the non-invertibility of the original matrix.
* A simple analysis of the complexity in time and memory for the full aproach in constrat to other estimators (CV) would be welcome. The paper lacks a detailed discussion on the computational cost of the proposed ensemble method. A comparison with standard cross-validation techniques, both in terms of time and memory requirements, is crucial for practical applicability. For instance, while the sketching operation may reduce the dimensionality, the ensemble averaging could introduce additional computational overhead. A concrete analysis, possibly with asymptotic complexity bounds, would be very helpful.
* Bonus: Is it interesting to come back on other risk estimators (Bootstrap) and clearly identify what could be done with this estimator or not with ensemble of sketched ridge regression.

### Questions
See my previous comments.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The current paper considers generalized cross validation (GCV) for sketched ridge regression ensembles. Specifically, sketching is done across different features and ensembles are based on finite sketches. The paper first derives the asymptotics of squared risk and its GCV estimator (section 2) and then extends to more general subquadratic prediction risk functionals (section 3). The paper also proposes a method for estimating the risk of unsketched ridge regression using sketched ridge ensembles (section 4). All the theoretical results are illustrated using both synthetic and real datasets with CountSketch and subsampled randomized discrete cosine transforms.

### Strengths
1. Overall the paper is very well written and persuasive. The experimental results are very well summarized in the figures.

2. It is impressive that the current paper considers all asymptotically free sketched ensembles and allows for zero or negative penalty 
 in ridge regularization.

3. Distributional consistency in Corollary 5 is nice: this allows for classification errors and construction of prediction intervals among other things.

4. It is interesting to know that the finite ensembles by sketching observations do not have GCV consistency, as given in Proposition 7.

### Weaknesses
It would be beneficial to provide more details regarding computational aspects in the main text. For example, I presume that it is not necessary to compute $\hat{\beta}_{\lambda}^k$ alone in equation (1). 

In other words,  it is only necessary to compute the predicted values 
$X \hat{\beta}_{\lambda}^k$. 

This seems important because it is not necessary to explicitly premultiply $S_k$ to $\hat{\beta}_{\lambda}^{S_k}$ in equation (1). If I am correct, this point can be emphasized at the end of section 2 when it is discussed that matrix inversions are inexpensive after precomputing $X S_k$.

Generally speaking, it would be helpful to provide more details regarding computational aspects.

It is also not clear whether the computational gains of the ensemble approach are fully realized in practice, especially when the sketch dimension $q$ is close to the original feature dimension $p$. The paper should discuss the computational cost of forming the sketched matrices $XS_k$ and the impact of sketch size on overall runtime. Furthermore, the practical implications of using a large number of ensembles $K$ should be addressed, as this could potentially negate the computational benefits of sketching if not handled efficiently. The paper should also discuss the memory requirements of storing multiple sketched matrices and their corresponding ridge regression solutions, especially when $K$ is large.

In figure 1, it would be good to indicate that SRDCT refers to subsampled randomized discrete cosine transform because SRDCT first appears toward the end of page 2.

In proposition 6, $S_k^T S_k$ is assumed to be invertible. How strong is this assumption? Some further remarks might be helpful.

The ensemble trick in section 5 seems very useful. However, there is no explicit discussion of computational gains over unsketched GCV. Especially, when $K$ is large as in proposition 6, one might need to rely on parallel computing to fully speed up computations. More discussions might be desirable in terms of computational complexity. 

Is there a known S-transform for CountSketch? Table 4 in the appendix does not include CountSketch.

### Questions
1. In figure 1, it would be good to indicate that SRDCT refers to subsampled randomized discrete cosine transform because SRDCT first appears toward the end of page 2.

2. In proposition 6, $S_k^T S_k$ is assumed to be invertible. How strong is this assumption? Some further remarks might be helpful.

3. The ensemble trick in section 5 seems very useful. However, there is no explicit discussion of computational gains over unsketched GCV. Especially, when $K$ is large as in proposition 6, one might need to rely on parallel computing to fully speed up computations. More discussions might be desirable in terms of computational complexity. 

4. Is there a known S-transform for CountSketch? Table 4 in the appendix does not include CountSketch.

[Update after the discussion period] The author(s) responded well with my questions. I am satisfied with their replies. This is indeed a good paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper established consistency of generalized cross validation for estimating prediction risks of sketched ridge regression that enables it to fast tune ensemble parameters. The authors further proposed an resembling trick so that the risk for unsketched ridge regression can be estimated through GCV using small sketched ridge ensembles. Simulations are conducted to validate the theoretical results.

### Strengths
The paper gives asymptotic of squared risk and its GCF estimator for sketched ridge regression so that an it is intuitively understandable as the implicit unsketched ridge regression risk and an inflation term due to randomness of the sketch that is controlled by ensemble size. And this is exploited to provide a method to tune unsketched ridge regression using only sketched ensembles. None of the assumptions are very strong for these theoretical results.

### Weaknesses
While the results in this paper is interesting, the authors failed to illustrate while tuning (ensembled) sketched ridge is preferred over tuning unsketched ridge regression. It would be better if they provide some intuition and explanation to the results, especially for readers who are not that familiar with sketching.



### Questions
Because GCV and risk for sketched ensembles converge at rate 1/K to the equivalent ridge for sketched ensembles, does this imply the larger the K the faster the convergence and the better it is? It there a downside if K is too large?
Could the authors why the result that tuning (ensembled) sketched ridge is equivalent to tuning unsketched ridge regression is useful?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
