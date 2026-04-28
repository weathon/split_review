# Boosting Methods for Interval-censored Data with Regression and Classification

- Decision: Accept
- Avg Score: 5.60
- Scores: 6, 5, 6, 5, 6

## Abstract
Boosting has garnered significant interest across both machine learning and statistical communities. Traditional boosting algorithms, designed for fully observed random samples, often struggle with real-world problems, particularly with interval-censored data. This type of data is common in survival analysis and time-to-event studies where exact event times are unobserved but fall within known intervals. Effective handling of such data is crucial in fields like medical research, reliability engineering, and social sciences. In this work, we introduce novel nonparametric boosting methods for regression and classification tasks with interval-censored data. Our approaches leverages censoring unbiased transformations to adjust loss functions and impute transformed responses while maintaining model accuracy. Implemented via functional gradient descent, these methods ensure scalability and adaptability. We rigorously establish their theoretical properties, including optimality and mean squared error trade-offs, offering solid guarantees. Our proposed methods not only offer a robust framework for enhancing predictive accuracy in domains where interval-censored data are common but also complement existing work, expanding the applicability of boosting techniques. Empirical studies demonstrate robust performance across various finite-sample scenarios, highlighting the practical utility of our approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents boosting algorithms for regressors and classifiers  for the censored data. The censoring naturally introduces a bias into the estimator as it collapses  the mass of the tails of the underlying distribution on the censoring boundary.  In particular, the main contribution of the paper is in presenting the novel boosting framework with censoring unbiased transformation which focuses on modifying the loss function. Authors also present a model for imputing the missing data in censoring context. Authors investigate the theoretical properties of the algorithms and conclude that incorporating the spline estimators into the base learner results in optimal MSE rates for the predictor.

### Strengths
- The paper is mathematically well written. The notation is consistent and precise. Definitions and proofs are provided in the Appendix.
- The theoretical results are novel, clearly structured and formulated. The implications of each theoretical result are well discussed and framed within the literature context if relevant. 
- The proposed algorithms are experimentally tested on the synthetic dataset under various scenarios. The method is further applied to real-life dataset.

### Weaknesses
1) The underlying part of the model is estimating survival function. It would be interesting to include the experiment with different survival function estimators to assess how sensitive the method is to the potential biases of the estimator of  the survival times as this part of the model is not properly covered by presented theory. Specifically, the paper uses a Kaplan-Meier estimator, but it does not explore how the choice of this estimator affects the performance of the boosting algorithm, especially in scenarios with heavy censoring or non-proportional hazards. It would be beneficial to see experiments with alternative estimators such as the Nelson-Aalen estimator or even parametric survival models to understand the robustness of the proposed method.
2) It is not clear how sensitive the proposed method is to the noise in the underlying data. The paper only presents results for a single noise level in the synthetic data experiments. It is important to investigate how the performance of the algorithm degrades as the noise level increases. This would involve varying the variance of the error term in the data generation process and observing the impact on the prediction accuracy. Such analysis is crucial to understand the practical applicability of the method in real-world noisy datasets.
3) Authors did not provide much insights into how well the algorithm scales to the larger datasets. The experiments are conducted on datasets of order 10^3, which is relatively small. It is important to evaluate the computational complexity and memory requirements of the algorithm as the dataset size increases. This would involve testing the algorithm on datasets with varying sizes and reporting the computational time and memory usage. This is particularly important for the boosting algorithm, which can be computationally expensive.

### Questions
1) What are the scaling capabilities of the models to the large datasets? (provided datasets are of order of magnitude 10^3? It would be good to see experiments for varying sizes of the dataset.
2) The imputation algorithm and the CUT boosting in the presented experiments (especially Figure 3, E.3) seems to produce similar results. Can you provide more insights into why that is?
3) It would be great to see performance for other real-life datasets with already known benchmarks to demonstrate that the presented method performs well against other well explored survival dataset problems. 
4) For the synthetic dataset, e.g. scenario 1, how does the performance changes based on the amount of the noise in the data, so when you change the variance in the error term $epsilon_i$, e.g. instead of only 0.25 variance for normal, when you increase the noise for to 0.5, 1., 1.5?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work the authors propose a new algorithm based on boosting for interval-censored data. They provide an extensive theoretical analysis and an empirical comparison of both simulated and real data, for which their proposed methods have a performance similar to that of the state of the art.

### Strengths
The article is clearly written and provides a thorough theoretical analysis of the proposed algorithm, which is really important to ground further applicative work using this method in practice.

### Weaknesses
There are several limitations of this work.
- my main concern is that the paper does not clarify the empirical improvement compared to the use of ICRF. It is slightly different indeed to use boosted trees compared to random forests (bagging), but the article fails to show a clear gain in performance, both on simulated and real data
- there should be more baselines, like Cox models, even if they are designed for right-censored data rather than interval data. There are very few baselines included in the benchmark presented here. It's unclear whether the I method is similar to ICRF or a novel method. If not, ICRF should be included as a baseline to demonstrate the contributions of this work clearly.
- I don't think there is any mention that the code to use L2Boost-CUT or L2Boost-Impute will be made available, is it?

### Questions
see limitations
- are there any additional performance metrics that could be used? like the c-index (or a variation of it)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript introduces a framework that extends boosting techniques to effectively handle interval-censored data. The authors offer a thorough theoretical analysis, examining mean squared error (MSE), variance, and bias, building on foundational results from Bühlmann & Yu (2003). The proposed methods are further substantiated through experiments conducted on both synthetic and real-world datasets, demonstrating the framework’s applicability and effectiveness.

### Strengths
- The manuscript is clearly written and accessible, making the methodology easy to follow.
- The authors conduct a rigorous theoretical analysis of their proposed methods, assessing mean squared error (MSE), variance, and bias to establish a solid foundation for their approach.

### Weaknesses
 - In Proposition 2, using a distinct notation for the smoother matrix would help prevent confusion with the survival function $S$.
- Adding experiments for the Cox proportional hazards model would strengthen the manuscript's applicability and support its conclusions.
- Additional ensemble methods exist for interval-censored data, such as:
    - Yao, W., Frydman, H., and Simonoff, J.S., 2021. An ensemble method for interval-censored time-to-event data. Biostatistics, 22(1), pp.198-213.

  Including comparisons with such methods would enhance the evaluation of the proposed approach.
- In both synthetic and real data experiments, the proposed CUT method and the imputation approach (Bian et al. 2024a) yield comparable results, with the imputation method occasionally performing better (e.g., in real data). Could the authors further elaborate on the unique advantages of their proposed method?
- In Appendix A, the authors outline several conditions primarily related to the smoother matrix $S$. Providing relevant examples of $S$ that meet these conditions would improve clarity.
- All theoretical results assume consistent estimation of the survival function. How does the convergence rate of the survival function estimator impact the final estimator?

### Questions
- In page 3 line 108, should the survival probability be P(Y>s)?
- In page 3 Equation (5), what is the update compared to Equation (3)?
- In traditional boosting methods, a learning rate is typically included. Is there a similar parameter in Algorithm 1?
- In Condition (C1), what does $Q_i^2$ mean? Does it denote $Q_i'Q_i$ as $Q_i$ is an eigenvector?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The boosting method is widely used in machine learning field, but it is not obvious to extend it to interval-censored data, that is, the outcome value is not specifically given but its interval is given. To apply the boosting to such datasets, the paper applies the method called the "censoring unbiased transformation" (CUT) to the loss function. As described in Proposition 1, the application of CUT does not change the expected loss between the interval-censored data and the true (uncensored) data, if we know the conditional survivor function $S$ (in reality we need to estimate it from the dataset). With this conversion of the problem, they showed that we can apply L2boost, an existing method of boosting for regression datasets (it can be extended to binary classifications).

### Strengths
-   The paper found that, by CUT, existing L2boost algorithm can be applied to interval-censored datasets.
    -   There is a constraint that we need to estimate the joint distribution of $X$ and $Y$ without knowing $Y$ itself but knowing only intervals. They showed that estimating the distribution by ICRF experimentally worked well.
-   Theoretical convergence rates and lower bounds of MSE (for regressions) and misclassifications (for classifications) are presented.

### Weaknesses
 -   The procedure itself looks somewhat simple; first we apply CUT and then L2boost. If there is a difficulty or interesting results of these combinations, please emphasize.
    -   Perhaps, the combination of boosting and interval-censored data is the novelty? If so, please emphasize the discussion on the novelty (e.g., limitations in existing methods).



### Questions
Key questions

-   It uses ICRF to estimate the conditional survivor function, but perhaps can we just impute interval-censored outcomes by ICRF (instead of using (Bian et al., 2024a))?
-   Section 1.1: The paper presented several tree-based interval-censored regression methods, but is it difficult to extend these methods to boosting? If so, why?
-   Section 1.2: It states that L2Boost-Impute is a proposed method, but the procedure appears only in Section 5, and the imputation method is just a reference. What is the novelty?
-   Section 5, Figure 1: Why the methods "O" (oracle) and "R" (reference) are compared in these plots? It is true that these results uses unknown information in reality and they can produce better results, but it looks that these results are not discussed in the paper.

Minor questions and suggestions

-   Some overlaps of letters found, so please consider replacing either of them with another letter.
    -   $L$: overlapped between the "loss function" and the "left of the interval"
    -   $S$: overlapped between the "conditional survivor function" and the "smoother matrix"
-   Section 3.1, line 182: Should $L = l, R = r, l < Y \leq r$ be $L = l, R = r, L < Y \leq R$, as far as reading the succeeding equation? (Does it mean that the distribution of $Y$ depends on the observation of the random variables $L$ and $R$ but independent of the distributions of $L$ and $R$?)
-   Section 3.1, line 187: It looks that the randomness of $M$ is not used anywhere else. How does the randomness work?
-   Section 3.2, line 238: It states that we need to estimate $S(y|X_i)$, but the procedure has not been described at this point. Please consider referring Section 3.3 as the section that describes how to estimate it.
-   Section 5: The "sample-based maximum absolute error" is abbreviated as "S-MAE", but please consider another abbreviation, since "MAE" also stands for **mean** absolute error. (It is confusing since "S-MSE" represents the "sample-based **mean** squared error".)
-   Section 5, line 471: adpots --> adopts
-   Section 5, line 510: boxlplots --> boxplots
-   Section 5, Figure 1(b): lines for "CUT" are not visible since they look overlapped with other lines, so please change line style or transparency so that the lines appear.

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript extends the boosting framework to regression and classification tasks with interval-censored data. The framework is particularly applicable in survival analysis, due to the prevalence of interval-censored data. The approach combines the L2Boost method with the censoring unbiased transformation (CUT) approach to form L2Boost-CUT, which is implemented via functional gradient descent. The manuscript also introduces an impute method based on L2Boost. L2Boost-CUT is applied to both synthetic and real data.

### Strengths
The paper is generally very well written and easy to follow. The authors excellently introduce the problem and previous methods. The manuscript also clearly motivates the problem. Specific strengths are:

1. The manuscript contains detailed and extensive theoretical results, providing strong theoretical guarantees. 
2. The theoretical results are described very well. Each theorem and proposition is described in terms of its broader importance and the purpose for it being used. This is very important in theoretical papers, to allow the reader to follow without getting bogged down by extensive theory.
3. The manuscript tackles an interesting problem and the contribution is important. The method is applicable to many important settings.

### Weaknesses
My main concerns are regarding the empirical results. I'm not convinced by both the scope and outcome of the results. Specifically:

1. Both the synthetic and real data studies are very limited in scope. For an approach that is so widely useful, it is a shame that it has not been applied to more settings to showcase its usefulness. It would be insightful to find and present scenarios showing the extreme ends of performance (very good and very bad performance)  of the approach and discuss why this is.
2. The results from the studies are not overly convincing. The method performs the same as imputation and standard boosting (which already exists) and does not provide a large benefit over the naive approach in the synthetic study. I have asked a clarifying question around this in the Questions, so this weakness can be addressed. 
3. I think there should be more discussion on the assumptions and limitations of the method. This would help to understand under which scenarios we might expect the method to not do well.
4. There is no discussion on computational cost or complexity. This could either be a theoretical complexity analysis or even just simple timing tests. Either would provide useful insights for practitioners who wish to decide on whether to apply the method to their problem.
5. There is no reproducibility. It would be helpful to have reproducible code, even for just a basic example. This would also partly help alleviate weakness 4, as I could run the code myself and observe the execution time.

I would like to see more evidence that the approach is beneficial in practice. I think the paper could do with some rearrangement: some of the theoretical results moved to the appendix to make space for further empirical results.

### Questions
1. How easily could the framework be extended to other boosting approaches (such as XG)?
2. Relating to the weakness point above: what's the benefit of L2Boost-CUT if it provides the same results as imputation + standard boosting?

### Soundness
3

### Presentation
3

### Contribution
3
