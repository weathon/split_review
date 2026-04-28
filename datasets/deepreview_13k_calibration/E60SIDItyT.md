# Learning from Aggregate responses: Instance Level versus Bag Level Loss Functions

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Due to the rise of privacy concerns, in many practical applications the training data is aggregated before being shared with the learner, in order to protect privacy of users' sensitive responses. In an aggregate learning framework, the dataset is grouped into bags of samples, where each bag is available only with an aggregate response, providing a summary of individuals’ responses in that bag. In this paper, we study two natural loss functions for learning from aggregate responses: bag-level loss and the instance-level loss. In the former, the model is learnt by minimizing a loss between aggregate responses and aggregate model predictions, while in the latter the model aims to fit individual predictions to the aggregate responses. In this work, we show that the instance-level loss can be perceived as a regularized form of the bag-level loss. This observation lets us compare the two approaches with respect to bias and variance of the resulting estimators, and introduce a novel interpolating estimator which combines the two approaches. For linear regression tasks, we provide a precise characterization of the risk of the interpolating estimator in an asymptotic regime where the size of the training set grows in proportion to the features dimension.  Our analysis allows us to theoretically understand the effect of different factors, such as bag size on the model prediction risk. In addition, we propose a mechanism for differentially private learning from aggregate responses and derive the optimal bag size in terms of prediction risk-privacy trade-off.  We also carry out thorough experiments to corroborate our theory and show the efficacy of the interpolating estimator.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of learning a model from a dataset partitioned into non-overlapping 'bags' of equal size, given the average value of the response variable in each bag. The difference with respect to usual regression analysis is that the individual responses are not provided, and so we cannot calculate the usual loss function. This calls for the definition of a modified loss function that depends only on the aggregate response in each bag.

The present paper analyses two such modified loss functions : L_bag, which measures the distance between the aggregate responses and the aggregates of model predictions ; and L_ins, which measures the distance between the aggregate responses and the individual model predictions.

While L_bag gives rise to an unbiased estimator, the estimator corresponding to L_ins has a lower variance, at the cost of introducing a bias. The author(s) interpret the difference L_ins - L_bag as a sort of regularization term.

The paper also studies a loss function L_int, depending on a parameter rho, that interpolates linearly between L_bag and L_ins. (This corresponds to tuning the strength of the regularization.) The choice of rho involves a trade-off between the bias and variance of the resulting estimator, and one can make this choice in order to minimize the 'prediction risk' of the estimator.

The paper illustrates the above ideas in the case of linear models, with a quadratic loss function. In a rather specific asymptotic regime, with the training data drawn from standard normal distributions and then assigned uniformly at random to the bags, the paper computes several quantities of interest, such as the bias and variance of the estimator corresponding to L_int (and, by specialization, of that corresponding to L_bag and L_int). The results support the qualitative conclusions mentioned above.

The paper also contains certain numerical experiments, verifying the theoretical results in the asymptotic regime mentioned above, and exploring in the case of the Boston Housing dataset the optimal value of rho as a function of bag size.

Finally, the paper also shows that truncating and adding a Laplace noise to the original aggregate responses makes the dataset epsilon-label Differentially Private. The resulting estimator is also Differentially Private, and the paper studies the optimal bag size (in the aforementioned asymptotic regime) as a function of the optimal regularization parameter rho.

### Strengths
A. Clarity
     1. The content is well organized. The introduction succinctly motivates the problems and summarizes the results.
     2. The intuitions are made explicit and are transparently described. This made the review process painless.
     3. The main text is clutter free and the proofs of all the technical claims are included in the supplementary material. The submission, is as a result, largely self contained and has no technical gaps.
     4. The literature review is thorough and the authors have gone the extra mile organizing the ideas and summarizing the current state of a rapidly evolving niche in ML research.

B. Significance, Quality
     1. The subject is topical since Privacy preserving ML is a burning issue and an active area of current research.
     2. The results shed new light on the interplay between instance-level and bag-level loss. It is interesting to see that the interpolate improves generalization in a real world dataset. 
     3. The qualitative conclusions derived in the asymptotic regime are clarifying and may be useful in more "hairy" real world datasets.

C. Originality
     1. Mixed loss function: The idea of interpolating between the loss functions is interesting and the idea that this could result in better generalization for aggregates-based learning appears to be novel.
     2. The authors go beyond showing empirical results and derive closed form expressions and provide compelling interpretations for them.

### Weaknesses
1. This is a minor comment on terminology: regularizers in the ML context, to the best of this reviewer's knowledge, only depend on model parameters and not on the data (which includes the feature vectors). Shrinkage and variance-reduction are related but not identical, and regularization in ML refers to the former. If indeed this term is used more broadly it may be helpful to include a few clarifying sentences and/or references. 

2. The theoretical results are proved under the following
      a. Random Bags
      b. Equal Sized Bags
      c. Non-Overlapping Bags

The introduction cites the Google(Privacy Sandbox) and Apple(SKAd) APIs as motivations for the problem but the assumptions (a),(b),(c) do not hold in this regimes. In fact, a critical feature of both (a) Google's Private Aggregation API and (b) Apple's SKAd Network is that the aggregation keys are configurable (eg. aggregate behavior of traffic from California, visiting sports content at a certain time of day) ie the bags are specified by the consumer of the API, not by random aggregations. This enables ML algorithms to effectively use these aggregates for prediction.

This is an essential part of the problem. For example, here is a quasi-technical [report published by Google](https://github.com/google/ads-privacy/blob/master/Combining%20the%20Event%20and%20Aggregate%20Summary%20Reports%20from%20the%20Privacy%20Sandbox%20Attribution%20Reporting%20API.pdf)

If there is indeed a connection/insight in the paper that this reviewer has missed, please respond to the question below.

### Questions
1. Are there explicit connections/insights to be gleaned from the results in the paper and the Google/Apple approaches for aggregated-feedback?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the challenge of learning with restricted access to labels. Specifically, the authors explore two categories: Instance Level and Bag Level Losses. The proposed algorithm begins by partitioning data points into k non-overlapping bags, each containing m examples. Subsequently, the authors introduce two sets of loss functions: bag-level (as seen in Eq. 1) and instance-level (as seen in Eq. 2).

The primary contributions of this paper are as follows:

1- Demonstrating that for a wide range of loss functions, a regularized bag-level loss can effectively serve as a surrogate for instance-level losses.

2- In the context of well-specified linear regression, providing a precise characterization of the tradeoff between bias and variance.

3- Introducing a label-DP variant of their algorithm tailored to bag-level losses.

### Strengths
I think the paper is well-written and the theoretical results are presented with lots of intuitions. I think the main strength of the paper is the exact characterization of the bias and variance tradeoff. This characterization let them compare two family of losses.

### Weaknesses
I think the motivation behind the definition of instance-level and bag-level losses is not clear. It would be beneficial to provide more context on why these two distinct loss formulations are considered, especially given that instance-level loss seems more intuitive. The paper should elaborate on the specific scenarios or data characteristics that would make bag-level loss a more appropriate choice, beyond simply stating that it is an alternative. Another weakness is that the authors do not compare their results with the prior results on label DP. In this paper the authors use bag-level loss and then consider the noisy labels. Is that the best approach? It's not clear if this approach is optimal compared to directly applying DP to individual labels, and the paper lacks a discussion on the trade-offs between these two approaches in terms of privacy and utility.

### Questions
1- What are the use-cases of instance-level loss and bag-level loss? To me, instance-level seems more intuitive and I want to know about the scenarios in which it is preferable to use bag-level loss.

2- What is the significance of non-overlapping bags? Is it because of the analysis?

3- For DP variants, the authors propose first forming the bag-level loss and then applying Laplace mechanism to the aggregated labels. Is that the best approach? What is the comparison of this method with the prior work on label-DP?

4- Randomness in placing the samples in bags may help in privacy amplification.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies learning from aggregated responses with loss functions from both an instance level and a bag level with motivation from keeping individual privacy. It investigated the tradeoff between risk and privacy by inserting a multiplicative parameter for the regularization term $\rho$ such that the instance-level loss and bag-level loss are well balanced. It also investigated different parameters such as signal-to-noise ratio, bag size, and overparameterization, and their effects on the convergence of the bias and variance of the model, and derived the optimal choice of parameter $\rho$ with evidence from numerical experiments.

### Strengths
The paper investigates the trade-off between bias and variance by taking into account various factors that might influence the model performance, which is considered thorough.

### Weaknesses
The presentation can be improved. For example, some high-level ideas on the tradeoff could be included earlier in the paper (in more detail) instead of introducing them in the latter parts of the paper which makes it hard to grasp the contribution at the beginning. More explanation on Theorem 2.5 should be discussed. For example, the intuition of the actual meaning of the fixed point or the solution of the equation systems; what quantities the bias and the variance are converging to.

### Questions
Can you explain a bit more on the fixed point and the solution of the equation systems in Theorem 2.5?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studied the problem of learning from average response.
The author compared two loss functions (error of average output, average as instance label) theoretically and analyzed the bias and variance for linear models.
Then, the author proposed a method for differential privacy based on the theoretical result.

### Strengths
- This paper is well-written and easy to follow. The mathematical notation is clear.
- The author did a good job discussing real-world examples and related works.
- The analyses are sound and reasonable.
- The private aggregate learning method is a solid contribution.

### Weaknesses
 - Most analyses are restricted to linear models. Thus, the range of applications may be limited. Even for tabular data, gradient boosting machines may perform better than linear models. There's a gap between theory and practice: for the Boston housing dataset, the author used an MLP instead. The theoretical analysis focuses on linear models, which may not capture the complexities of real-world data. While the authors use an MLP in experiments, this is not well-supported by the theory, making it difficult to understand why the observed results occur.
- The experiment is limited to one dataset. The labels generated in this way may not be a good proxy of real-world aggregate label problems. The method of generating labels by averaging individual labels within a bag may not accurately reflect how aggregate labels are formed in practice. This limits the generalizability of the experimental results. For example, in real-world scenarios, aggregate labels might be derived from more complex processes, such as weighted averages or medians, which are not considered here.
- A minor issue: the title "learning from aggregate responses" may be imprecise since here, the author only considered the average. There are other types of aggregate information, such as max, median, and rank.

### Questions
- Why non-overlapping?
- "The bag-level loss does not have a unique minimizer": is this proven?
- Why should we reduce the variance? It seems that the regularization could lead to an over-smoothed solution.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the relationship between instance-loss and bag-loss in the setting of aggregate label. In practice, the latter would provide stronger privacy protection in the model training process. The authors showed that instance loss can be viewed as having an extra regularization term similar to the within-cluster square loss from k-means. Based on this, a interpolative loss is proposed between these two as well as the bias-variance tradeoff on this factor.

### Strengths
- The paper is clearly written and provides a very intuitive view on the connection between the bag-loss and individual-loss.
- The authors derived theoretical results on the SNR which has practical implications on selecting optimal bag size.

### Weaknesses
 - The authors did not include the proof of the theorems, which I think is essential given the paper is largely centered around Theorem 2.5. In particular, (please let me know if I'm wrong), equation (8) simplifies to $2\alpha_{\ast}-1$ when k=1 which is not always 0 based on the fixed point assumption.
- There is a little incoherence between the assumption and application. The authors focused on very practical applications with DP and aggregate learning, but it's rare in those cases for the proportional regime to hold which appears to be essential to the analysis. More commonly we see d = o(n), and I also assume k could not be fixed as d grows to satisfy k-anon.

### Questions
As aforementioned, I would like the authors to provide the derivation of the theoretical results in the supplementary, and address the generalizability of the results if one or few assumptions do not hold in the paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
