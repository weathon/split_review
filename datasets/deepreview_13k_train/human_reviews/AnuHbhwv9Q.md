# Out of the Ordinary: Spectrally Adapting Regression for Covariate Shift

- Decision: Reject
- Scores: 6, 6, 5, 8

## Abstract
Designing deep neural network classifiers that perform robustly on distributions differing from the available training data is an active area of machine learning research.
However, out-of-distribution generalization for regression---the analogous problem for modeling continuous targets---remains relatively unexplored.
To tackle this problem, we return to first principles and analyze how the closed-form solution for Ordinary Least Squares (OLS) regression is sensitive to covariate shift.
We characterize the out-of-distribution risk of the OLS model in terms of the eigenspectrum decomposition of the source and target data.
We then use this insight to propose a method for adapting the weights of the last layer of a pre-trained neural regression model to perform better on input data originating from a different distribution. We demonstrate how this lightweight spectral adaptation procedure can improve out-of-distribution performance for synthetic and real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the problem of out-of-distribution generalization for regression models. The authors first analyze the sensitivity of the Ordinary Least Squares (OLS) regression model to covariate shift and characterize its out-of-distribution risk. Then they use this analysis to propose a lightweight spectral adaptation procedure(called Spectral Adapted Regressor) for the last layer of a pre-trained neural regression model. The paper demonstrates the effectiveness of this method on synthetic and real-world datasets, and it works well with data enhancement techniques such as C-Mixup.

### Strengths
1. Although there has been extensive research on distribution shifts in classification tasks, the authors focus on regression models which is a relatively unexplored problem of out-of-distribution generalization. The authors provide a novel analysis of the sensitivity of the Ordinary Least Squares (OLS) regression model to covariate shift. And they propose a spectral adaptation procedure specifically tailored for regression models, this adds to the originality of the paper.
2. The authors provide a thorough analysis of the OLS regression model's out-of-distribution risk, utilizing the spectrum decomposition of the source and target data.
3.  The paper provides a concise abstract that outlines the problem, methodology, and results.

### Weaknesses
1. The proposed method assumes access to unlabeled test data for estimating the subspaces with spectral inflation. However, in practical scenarios, obtaining unlabeled test data may not always be feasible. Specifically, the method requires estimating the target covariance matrix, which is not possible without access to target data, and while the authors mention using a separate unlabeled dataset from the same distribution, this is also a strong assumption that may not hold in many real-world cases. It would be beneficial to explore alternative approaches or modifications to the method that do not rely on unlabeled test data, or at least investigate the sensitivity of the method to distributional differences between the unlabeled data used for adaptation and the actual target data.
2. The compared methods are limited to me. The persuasiveness of the proposed approach would be stronger if more comparative data could be provided. For instance, the paper could benefit from comparisons against other domain adaptation techniques that are commonly used in the regression setting, including methods based on adversarial training or kernel mean matching, to better contextualize the performance of the proposed method.

### Questions
How computationally efficient is SpAR? The paper does not provide a detailed analysis of the computational efficiency of the proposed method. Considering the increasing complexity and size of neural regression models, it is important to assess the computational cost of the spectral adaptation procedure.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce a novel post-processing technique to address the unsupervised domain adaptation challenge under the premise of covariate shift. This method stems from an intricate analysis of Ordinary Least Squares (OLS). The authors delve into the theoretical examination of the OLS loss in the context of covariate shift, leading to a proposal to project the estimator into a distinct subspace. The authors contend that selecting this subspace based on a comparative analysis of loss with respect to bias and variance across eigenvectors ensures enhanced performance on the target distribution. Empirical evaluations on multiple datasets substantiate the efficacy of the proposed approach.

### Strengths
1. The paper offers a rigor analysis of OLS in the presence of covariate shift. The proposed projection technique is sound, and the decomposition of the loss function is notably interesting.
2. The estimation strategy derived from finite samples is also sound.
3. The paper is generally well-written and easy to follow.

### Weaknesses
1. The paper sheds light on an interesting post-processing technique, aligning the linear layer from the source to the target domain. However, in the realm of deep learning, adapting the representational function across both domains is crucial. It raises the question: Can the proposed technique outperform other domain adaptation methods that also focus on refining the representation function? If such outperformance is challenging, is it feasible for the proposed post-processing technique to boost the performance of existing domain adaptation methods?
2. Stemming from the aforementioned concern, it would be enlightening to see the proposed method compared with a broader spectrum of domain adaptation baselines in Table 3 for the CommunitiesAndCrime and Skillcraft datasets. Moreover, an exploration of the combination of the proposed method and these baselines could be insightful.
3. For the PovertyMap-WILDS dataset, the setting aligns more with an out-of-distribution generalization task rather than traditional domain adaptation. Hence, it may be more judicious to include OOD methods for comparison. Furthermore, the performance enhancement attributed to the proposed method on this dataset seems marginal since the variance in performance exceeds the difference between the proposed method and the top-performing baseline.

### Questions
See the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study how deep regression models can be adapted to perform better under covariate shifts.

They do a detailed theoretical analysis of the ordinary least squares method and how it is affected by covariate shifts. Motivated by these findings, they propose a post-hoc method that can be used to update the final layer of pre-trained deep regression models, utilizing unlabeled data from the target distribution.

The proposed method is evaluated on three real-world regression datasets, two tabular datasets and one image-based. The regression performance is compared to that of standard training and C-Mixup (with or without the proposed final layer update).

### Strengths
I agree with the authors that out-of-distribution generalization specifically for _regression_ problems is relatively unexplored. Thus, the problem studied in this paper is definitely interesting and important.

The paper is well written overall, and the authors definitely seem knowledgeable.

Although I did not entirely follow all parts of the theoretical analysis in Section 3, I did find it quite interesting. Especially Figure 2. The resulting proposed method then also makes some intuitive sense overall.

### Weaknesses
I found it quite difficult to follow parts of Section 3, especially Section 3.4.

The experimental evaluation could be more extensive. The proposed method is applied just to three real-world datasets, of which two are tabular datasets where small networks with a single hidden layer are used.

The experimental results are not overly impressive/convincing. The gains of ERM+SpAR compared to the ERM baseline in Figure 3, Table 2 and Table 3 seem fairly small.

The computational cost of the proposed method (Algorithm 1) is not discussed in the main paper, and only briefly mentioned in the Appendix.

The results in Table 3 seem odd, do all other baseline methods really degrade the regression performance compared to ERM?

### Questions
1. Could the discussion of the computational cost be expanded and moved to the main paper? How does the cost of Algorithm 1 scale if X and/or Z contains a large number of examples? How about the memory requirements?

2. Could you evaluate the proposed method on at least on more image-based regression dataset? (one of the datasets in _"How Reliable is Your Regression Model’s Uncertainty Under Real-World Distribution Shifts?"_ (TMLR 2023) could perhaps be used, for example?)

3. The results in Table 3 seem odd, do all other baseline methods really degrade the regression performance compared to ERM?

4. Can you please discuss the results in Figure 3, Table 2 and Table 3 a bit more, the gains of ERM+SpAR compared to ERM seems quite small? Does the proposed method actually improve the performance of ERM in a significant way?


Minor things:
- Section 3.4, last paragraph: "the the variance" typo.
- I would consider modifying the appearance of Table 1 - 3, removing some horizontal lines.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the problem of regression generalization to out of sample distributions. This is an important problem as many models suffer from poor performance when applied to different samples. The authors focus on the case of linear regression with fixed covariate shift and derive a clean decomposition of the out of sample error in terms of the model primitives. Through the decomposition the authors identify a cause of generalization error which they coin Spectral Inflation. Spectral Inflation occurs when the training set and evaluation set are misaligned in the sense that the dimensions along which most of the variation is explained do not coincide. 

The paper proposes a novel post-processing algorithm that projects the OLS solution to a subspace that is well aligned with the evaluation set. The authors offer theoretical guarantees on how to choose the projection subspace given the data and researcher chosen hyper-parameters. Finally, they show the performance of the proposed method in a simulation exercise and across various empirical applications.

Overall the paper is very well written and I enjoyed reading it a lot.

### Strengths
* The paper tackles and important problem by considering a clean and simple setting. I found this very useful as it helps highlight the crux of the problem and offer an intuitive solution. Furthermore, the paper is well written, the exposition is good and the theoretical results are clean and technically correct.

* In terms of relevance, the decomposition results are not very surprising, but they do offer a straightforward and intuitive way to think of the generalization error in the context of linear regression. Researchers may find them useful as a framework for OOD error in these settings.

* The algorithm proposed is intuitive and the theory developed offers an interesting way of thinking why it is a good algorithm under different potential underlying models. 

* The simulations and empirical examples are careful and offer a wide range of settings in which the method performs well.

### Weaknesses
 * While the theoretical results are clean and correct, I wonder if the authors have solved the problem they set to solve rather than just offer one solution that is weakly better than OLS. I expand on this in the questions.

* While the proposed method performs well through the simulations and empirical tests it is unclear if it is better than other methods. For example, in Table 2 and 3 accounting for the errors it does not seem to be statistically different from the other methods (for example ERM in Table 2). The authors also do not compare it in simulations with alternative methods besides simple OLS. For instance, it seems that PCR might perform well in this setting.

### Questions
* In the decomposition results, what is the expectation being taken over? I thought that X and Z are treated as random, but in the proof in page 13 in the appendix it seems that X and Z are fixed. Are X and Z random or fixed? Are the decomposition results conditional on X and Z?

* Theorem 3 states that S^* is weakly better than the OLS solution, not that it is the best solution amongst all possible S. However in the paragraph above it is stated that it is the ideal set. Is it the case that S^* is the projection set that minimizes the expected loss amongst all possible S sets? It may be trivial, but it would be worth it fully explaining this in the main body of the text. If S^* is the the projection set that minimizes the expected loss then it should be stated as a theorem, if not then you should explain why you focus on S^* rather than the minimizing S. 

* Can you use the plug in variance estimator to estimate the variance on the same data? Why is a sample split not necessary? (this could be trivial given the assumptions) 

* How do you choose the hyperparameter alpha? Is there a data driven way to choose it or an optimal way of choosing it? 

* It would be useful to decompose the MSE into bias and variance in the simulations to check that Spar indeed is trading off bias and variance as described by the theory in relation to OLS. 

* What would change if Z was noisy? If we assume conditionally independent errors like for X, the conditional expectation would still be the same so it seems that most of the theory would go through with little changes (and the additional Z variance).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
