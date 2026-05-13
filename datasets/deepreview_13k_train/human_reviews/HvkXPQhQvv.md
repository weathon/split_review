# Evaluating multiple models using labeled and unlabeled data

- Decision: Reject
- Scores: 8, 5, 5, 6

## Abstract
It remains difficult to evaluate machine learning classifiers in the absence of a large, labeled dataset. While labeled data can be prohibitively expensive or impossible to obtain, unlabeled data is plentiful.
Here, we introduce Semi-Supervised Model Evaluation (SSME), a method that uses both labeled and unlabeled data to evaluate machine learning classifiers. SSME is the first evaluation method to take advantage of the fact that: (i) there are frequently multiple classifiers for the same task,  (ii) continuous classifier scores are often available for all classes, and (iii) unlabeled data is often far more plentiful than labeled data. 
The key idea is to use a semi-supervised mixture model to estimate the joint distribution of ground truth labels and classifier predictions.
We can then use this model to estimate any metric that is a function of classifier scores and ground truth labels (e.g., accuracy or expected calibration error). 
We present experiments in four domains where obtaining large labeled datasets is often impractical: (1) healthcare, (2) content moderation, (3) molecular property prediction, and (4) image annotation. Our results demonstrate that SSME estimates performance more accurately than do competing methods, reducing error by 5.1x relative to using labeled data alone and 2.4x relative to the next best competing method. SSME also improves accuracy when evaluating performance across subsets of the test distribution (e.g., specific demographic subgroups) and when evaluating the performance of large language models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces Semi-Supervised Model Evaluation (SSME), a novel method designed to evaluate machine learning classifiers using both labeled and unlabeled data, addressing the challenge of obtaining large labeled datasets. SSME leverages the availability of multiple classifiers, continuous classifier scores, and abundant unlabeled data to estimate the joint distribution of true labels and classifier predictions through a semi-supervised mixture model.  The authors validate SSME across four challenging domains—healthcare, content moderation, molecular property prediction, and image annotation—showing that it significantly reduces error rates in performance estimation compared to traditional methods.

### Strengths
Originality: SSME is a pioneering approach that creatively combines labeled and unlabeled data for model evaluation, filling a critical gap in existing methodologies.
Clarity: The abstract effectively communicates the core concepts and findings, making it accessible to a broad audience while maintaining technical depth.
Significance: This work addresses a significant challenge in machine learning evaluation, potentially benefiting many fields where labeled data is scarce. Its implications for improving model assessment and performance understanding are substantial.

### Weaknesses
In fact, there has been a lot of work in recent years on evaluating language models, but none of these are mentioned in this paper. Moreover, since the datasets and classifiers selected for the experiment also involve the architecture of large language models, these methods of evaluating language models are not mentioned in the comparison method.

### Questions
What is the complexity of the method in this paper? In other words, is this approach worth the computational resources we consume compared to tolerating the errors that come with traditional evaluation methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper provides a semi supervised method for evaluation of a set of classifiers. Given a small amount of labeled data, a large amount of unlabeled data on which a set of classifiers can provide scores on any input, estimate accuracies of these classifiers. In particular for unlabeled data $x^1, \dots x^n$ and classifiers $1, \dots m$ , we have scores $s^1, \dots s^n$ where $s^i$ is the set of scores for $x^i$, $s^i = \{s_1^i, \dots s_m^i\}$. For classifier $j$,  $s_j^i$ is the score vector in $\Delta^K$ where $\Delta^K$ is the $K$ dimensional simplex, and $K$ is the number of classes.

Their method comprises on fitting a mixture model that estimates true class probabilities given classifier scores, i.e. learn $P(y | s_1, \dots s_m)$. The mixture model is fit by minimizing a joint distribution over scores and true class probabilities parameterized as 
$$P(y, s) = \lambda_L \sum_{i\in D_L} \log P(s^i|y^i) + \sum_{i\in D_U} \log \left(\sum_{k=1}^K P(s^i|y^i = k)P(y^i = k)\right)$$
where $P(s^i|y^i = k)$ is parameterized as 
$$P(s | y = k) = \frac{1}{\sum_i P(y^i=k|s^i)} \sum_i \mathcal{K}_h(s - s^i) P(y^i = k |s^i)$$

An EM algorithm is used to estimate $P(y^i = k |s^i)$. In the E step given, the mixture component each data point belongs to, i.e. $P(y^i = k |s^i)$ is estimated by maximizing the objective keeping $\mathcal{K}_h$ fixed, and in the M step, $\mathcal{K}_h$ is optimized keeping $P(y^i = k |s^i)$. 

Finally given the fitted $P(y^i | s^i)$, any metric $m$ such as classification accuracy is estimated as  $1/n \sum_{i=1}^n E_{y^i \sim P(y^i | s^i)}[m(s_j^i , y_i)]$.

To evaluate their method, the authors use a 6 publicly available datasets. Their evaluation procedure involves first getting a set of classifiers by training on a split of the data, then estimating $P(y^i | s^i)$ on another estimation split and finally comparing the estimated metric against the true metric from a larger evaluation split of the data. 

The authors show that their method performs superior to a number of baselines including labeled, Pseudo labeled, David-Skene, and Bayesian Calibration. Further they provide some ablations on their method 1) when only one instead of many classifier is available, and 2) using a normalization flow based model instead of Kernel Density estimation for the mixture model.

### Strengths
1. The presentation of the estimation method given a set of classifiers was clear and easy to understand. 

2. The method of fitting a mixture model is sound however not novel.

3. The results are superior compared to baselines. 

4. Adequate ablations were performed such as using just one classifier instead of many, providing insights on estimation error with classifier accuracy, and studying the estimation error of method by partitioning into different subgroups.

### Weaknesses
1. Under what assumptions does the particular joint model over classifier scores and true latent distribution makes sense is not described. Specifically, the assumption that the joint distribution of classifier scores and true labels is the same for labeled and unlabeled data is not sufficiently justified. It's unclear if this assumption holds when the unlabeled data comes from a different distribution than the labeled data, which is a common scenario in real-world applications. The method's robustness to violations of this assumption needs to be discussed.

2. The details regarding how are different classifiers distinct from each other is not given. If I understand correctly, each classifier is trained on the same training data, so I assume the only difference arises from different random initialization ? In that case, it appears that different classifier scores should be very similar to each other. Then the point of using multiple classifiers is not clear. It is not clear if the classifiers are trained using different architectures or different training procedures, and how this would affect the diversity of their predictions. The paper should clarify whether the classifiers are expected to have complementary strengths or if they are simply redundant.

3. A simple baseline such as majority vote weighted by some function of classifier accuracy could be provided. The current baselines do not fully explore the potential of combining multiple classifiers, and a weighted majority vote could serve as a strong comparison point. The method should also be compared to more advanced ensemble methods that are designed to leverage the diversity of multiple classifiers.

3. The exact implementation details of baselines such as David Skene is not provided. The lack of specific details makes it difficult to reproduce the results and to assess the validity of the comparisons. The paper should provide the exact parameters used for the baselines, as well as the specific versions of the software packages used.

4. Assumption of availability of multiple classifiers appears like a strong assumption. The method's applicability in scenarios where only a single classifier is available is not discussed. The paper should clarify if the method can be adapted to single classifier settings and if so, how its performance compares to other single classifier evaluation methods.

5. The experiment section could be structured better. Instead of figure 2 and figure 3, tables could have provided more information. Some tables in appendix should be used in the main paper. The figures are not very informative, and the paper should provide more detailed numerical results in the main text. The use of tables would allow for a more precise comparison of the proposed method with the baselines.

### Questions
Describe more details on how the baselines were used and how are the set of trained classifiers different from each other.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces **Semi-Supervised Model Evaluation (SSME)**, a method that leverages both labeled and unlabeled data to evaluate multiple machine learning classifiers. SSME is built on the premise that unlabeled data is often more abundant than labeled data,  addressing scenarios where multiple classifiers are available but labeled data is scarce. Using a semi-supervised mixture model, SSME estimates the joint distribution of ground truth labels and classifier scores, which allows it to assess metrics such as accuracy and expected calibration error  without requiring extensive labeled datasets. Through experiments in healthcare, content moderation, molecular property prediction, and image annotation, SSME is shown to reduce estimation error in the metrics compared to baselines.

### Strengths
1. The paper presents a novel approach to evaluate classifiers by leveraging unlabeled data alongside limited labeled data, addressing a common bottleneck in evaluating models. The method is simple and the paper is well written overall.

2. SSME’s performance is evaluated across multiple domains and tasks, such as healthcare and content moderation.  The results indicate improvements over baselines in estimating standard metrics, providing evidence of the method's applicability.

3.  The study also shows methods ability to evaluate subgroup-specific metrics, which is beneficial for fairness assessments. This application is particularly relevant for sensitive domains like healthcare, where performance disparities among demographic groups can be critical.

### Weaknesses
1.  There is no theoretical analysis provided,  limiting our understanding of when and why the method may succeed or struggle in different data distributions or model configurations e.g. high or low accuracy models. Specifically, the paper lacks discussion on the identifiability of the mixture model parameters and how the number of classifiers and their individual performance characteristics affect the estimation error. It's unclear how the method would perform if the classifiers are highly correlated or if some classifiers are significantly less accurate than others, potentially leading to biased estimates.

2.  The main empirical results in Figures 2, 3 and Table 1, report absolute error in estimates. I'd like to see the actual estimates, I believe if the models are highly accurate then it would be easier to infer the groundtruth label and hence the estimates are expected to be better but for models with low accuracy, or models with less correlation the observations could be different. It is important to understand the range of the estimated metrics and how they compare to the ground truth values, rather than just the absolute error. This is particularly important for interpreting the practical significance of the results. For instance, a small absolute error might be negligible if the true metric value is also small, but significant if the true value is large.

3. There are several baselines that have not been considered for evaluation. Some of them are based on weak supervision and active testing. You can use the same amount labeling budget as $n_l$ to run active testing and use $n_l$ points to estimate source quality or write labeling functions in weak supervision pipelines. See some of the references below,

https://arxiv.org/pdf/1711.10160

https://arxiv.org/abs/2107.00643

https://arxiv.org/abs/2002.11955

https://arxiv.org/pdf/2211.13375

https://arxiv.org/abs/2103.05331

### Questions
See the weakness above. I have a few more questions,

1. The estimated joint model is specific to the number of classifiers. So if one comes up with a new classifier how is that going to be evaluated? This modeling choice does not seem flexible to me.

2. The assumptions on the classification models are not clear. In particular, how accurate should they be and what's the correlation between them?

3. How will this approach work if the user gives classifiers one at a time, i.e. you don't see all the classifiers ahead of the time but instead they arrive sequentially. For instance, during model training we iteratively improve a single classifier and even during the developement cycle we maintain and update a single model.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies a practical setting which is to evaluate the performance of $M$ classifiers pre-trained targetting the same tasks on two subsets, one with labels and the other without labels. The solution proposed in the paper is to employ semi-supervised learning following a generative modelling through a mixture model to estimate the joint probability of the ground truth labels of unlabelled data and the predictions made by those $M$ classifiers. The ground truth is them inferred from such a modelling to evaluate the performance. The empirical experiment presented in the paper covers a number of datasets.

### Strengths
The paper introduces a setting often encountered in practice: evaluating performance of $M$ classifiers pre-trained for a task on a new dataset. In addition, that dataset has a small portion labelled, while the remaining is unlabelled. The paper is well-written to explain the idea at high-level.

### Weaknesses
Despite the easy-to-understand being of the paper at high level, the paper poorly explains how the main idea can be done in technical details (including the text in section 4 and the one in Appendix C). The explanation is too vague for me to understand how the paper is doing to achieve its goal.

According to the problem setting in section 3, the problem is equivalent to infer the ground truth labels on unlabelled data using the labelled data and some additional pre-trained classifiers. If one knows the distribution of the ground truth for each sample, it is easier to evaluate the performance of those pre-trained classifiers. Stating this equivalence would significantly improve the clarity of the paper.

The main idea of the paper is to follow the generative approach in semi-supervised learning to find the joint probability between label $y$ and another variable (in the paper, it is the concatenated predictions of all the classifiers, denoted as $\mathbf{s}$). The equation at line 167 can be rewritten in a more understandable form as follows:

$$
\max_{\theta} \ln \Pr(S, Y, S^{\prime}; \theta) =  \max \ln \prod_{i = 1}^{n_{l}} \Pr(\mathbf{s}_{i}, y_{i}; \theta) \prod_{j = 1}^{n_{u}} \Pr(\mathbf{s}_{j}; \theta) = \max \sum_{i = 1}^{n_{l}} \ln \Pr_{\theta}(\mathbf{s}_{i}, | y_{i}) \Pr(y_{i}) + \sum_{j = 1}^{n_{u}} \ln \sum_{k = 1}^{K} \Pr_{\theta}(\mathbf{s}_{j} | y_{j} = k) \Pr(y_{j} = k).
$$

Here, it is not explained why the vector concatenated predictions of all the classifiers, $\mathbf{s}$, is used as one of the variables, instead of the raw input data $\mathbf{x}$ as in conventional semi-supervised learning. This may lead to a bad estimation if most of the classifiers are bad. My guess is that the setting does not allow to access to the raw data $\mathbf{x}$. However, in section 3, the raw input data $\mathbf{x}$ is accessible.

Another concern is how to know the label distribution $\Pr(y_{j})$ of the unlabelled data (the very last term in the equation above). In the text, the authors only explain how to calculate $\Pr(\mathbf{s} | y)$ at line 181, without specifying how to calculate $\Pr(y_{j})$ of the unlabelled data term. This distribution must be known to estimate $\Pr(y | \mathbf{s}$ from the learnt $\Pr(\mathbf{s}, y)$, which is claimed by the paper, but is never explained how to perform such inference.

### Questions
My concern is the main method proposed to infer the ground truth labels of unlabelled data. Could the authors clarify how such ground truth labels are inferred in more details? The current explanation is too vague to understand.

In addition, could the authors clarify why using $\mathbf{s}$ instead of $\mathbf{x}$ in the formation?

### Soundness
2

### Presentation
1

### Contribution
1
