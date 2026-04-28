# Attributing Model Behavior: The Predominant Influence of Dataset Complexity Over Hyperparameters in Classification

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 5, 3, 3

## Abstract
Understanding the drivers of machine learning performance is essential for optimizing model accuracy and robustness. While significant attention has been given to hyperparameter tuning and data preprocessing, the impact of intrinsic data complexity (e.g., class overlap, feature overlap, dimensionality, etc) remains less explored. This study investigates the comparative influence of data complexity and hyperparameter configurations on the performance of classification algorithms, specifically Random Forests (RF), Support Vector Machines (SVM), Decision Tree (DT), Adaptive Boosting (AB) and Multi-layer Perceptron (MLP). Using 270 diverse OpenML datasets and 304 hyperparameter configurations, we employ functional analysis of variance (fANOVA) and Ordinary Least Squares (OLS) regression to quantify the relative importance and effect sizes of hyperparameters and complexity meta-features. Our results reveal that data complexity exerts a more substantial influence on both bias and variance components than hyperparameter tuning, underscoring the importance of addressing intrinsic dataset challenges. These findings suggest that efforts to mitigate data complexity factors, such as class overlap or imbalance, may yield greater performance improvements than extensive hyperparameter optimization. This study provides actionable insights for machine learning practitioners and highlights the need for further research into the interplay between dataset properties and algorithmic performance.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes an analysis of the influence of hyperparameter tuning and training "data complexity" (the author call it "complexity meta-features") on the performance of two classic classification algorithms:SVMs and Random forests. the paper includes  run extensive experiments on 290 OpenML tabular datasets. The author's end with a summary of their findings: dataset complexity matters the most.

### Strengths
1) the paper is easy to read
2) The paper confirms a fact that is well know by most data science / ML prectioners, the complexity of the data set matters for classification performance.

### Weaknesses
1) The content, experiments and conclusions of the papers are very outdated. It reads like a paper that was written 15-20 years ago. Most citations are from many years ago. Hence the contribution are practically irrelevant to the current state of ML / data science in 2024. Hence there is no significant contribution or relevance to the ICLR community.

2) Furthermore, the main conclusion of the paper is that dataset complexity (class overlap, dimensionality, etc) matters when training a classifier (RF or SVM). These are well known fact that are thought in introductory ML class and hence there is no new information provided here.

### Questions
I dont have any follow-up questions.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the relative influence of dataset complexity and hyperparameters on classification model behavior, specifically for RF and Kernel SVM. \
Authors utilize the fANOVA framework and OLS to quantify the influence on bias and variance brought by dataset complexity and hyperparameters. \
Based on the analysis across 290 datasets and 304 hyperparameter configurations, the study finds that dataset complexity meta-features—such as class overlap, data sparsity, and class imbalance—have a more substantial impact on bias and variance than hyperparameters.

### Strengths
The paper addresses a gap by directly comparing the impacts of dataset complexity and hyperparameters on model performance. Previous studies have often examined these factors separately, but this research provides a unified framework to assess their relative influence on bias and variance. 

The paper comprehensively considered nearly 300 datasets and over 300 configurations, enabling a more convincing conclusion.

Apart from the numerical results, the paper also includes very detailed arguments of why this happens and what this indicates.

Some of the estimated coefficients shown in the OLS summary table do align with our common understanding of how random forests deal with bias-variance tradeoffs, e.g. coefficients associated with min samples leaf, bootstrap, and max features.

### Weaknesses
1. lack of details on the experiment design. 

 (1) as the paper claims, nearly 300 datasets of varying sample sizes, response categories, and feature dimensions are used. Why are they comparable? I believe 0-1 loss is not a typical loss function people use for multiclassification problems.  And high-dimensional datasets wouldn't react necessarily the same as n>p datasets in terms of hyperparameters. 
 
(2) hyperparameters like C and gamma have huge variations in scale. How is it being included in OLS? Is it logarithmized?

 (3) For readers not familiar with meta-features of datasets, it would be very helpful to at least sketch some general ideas of how these meta-features are defined. Are those features immune to data transformation?  The same for how fANOVA works. 


2. lack of details on why the experiments are conducted in such a way. 

 (1) In my perspective, the number of trees is RF's one of the most important hyperparameters. Why is this not considered?
 
(2) I believe the neural net is the framework that people are most curious about. The authors also mention it in the introduction. Why is that not considered? 
 
(3) Based on the pymfe package, there are plenty of meta-features that characterize data complexity from different perspectives. Why specifically these 3, N1, T2, C1, are chosen?

3. Some of the results that are confusing to me. 

 (1) if those meta-features are immune to data transformation, how can we benefit from your research even though we know that data complexity itself is much more important than tuning hyperparameters? if not, shouldn't you include some examples of how bias and variance are reduced after some preprocessing of the data that reduces data complexity? For example, class imbalance issues can be alleviated by reweighing samples or bootstrapping.

In general, I do agree that the data's quality is much more important than tuning parameters. If the data is always linearly separable, I believe logistic regression would suffice. It's just the data quality is not something we can work on but the model and the model's parameter choice. Please correct me if I am wrong. 

 (2) Based on your OLS example, the features included are all significant neq to 0. If the trend is determined, does it mean that choosing a smaller c or some certain kernel can always help with the prediction?

### Questions
please check the weakness.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Authors compare impact of dataset complexity and hyperparameter tuning on the performance of binary Random Forest and SVM classifiers. They perform extensive experiments which support their finding that the dataset complexity has dominant impact on the performance.

### Strengths
- extensive experiments

- clearly written, easy to read

- the topic of bias/variance tradeoff is very important

### Weaknesses
I think the paper sends, in essence, a wrong message to readers.
Authors are basically suggesting that hyperparameter optimization
isn't useful, which I disagree with.  As I write this, I am tuning
hyperparameters of a neural network classifier, and the AUROC has gone
from 0.55 to 0.75, exclusively due to the (gradually improving) choice
of hyperparameters. The conclusion is at best narrowly limited to SVM
and RF, but that makes the manuscript 1) not that useful, given
limited scope 2) misleading, since many readers may walk away with a
wrong impression that the conclusions apply generally 

To be clear, not disagreeing with the idea that hyperparameter tuning
has a natural limit, and going beyond that may require additional or
different data. But the paper leaves an impression to the reader that
hyperparameter tuning doesn't help in general, which I disagree with. At a minimum, the title should say that the results are limited to SVM and RF binary classifiers. 

Also keep in mind that "optimizing dataset complexity" is a vague and
hardly actionable advice. I personally don't quite know how to
optimize dataset complexity, whereas hyperparameter tuning is well
understood. This should be clearly stated/discussed.


3.3
---

- 2 out of 3 is not really "generally". Please just be specific: for
  N1 and T1, higher values indicate greater classification
  difficulty. For C1, lower values indicate greater classification
  difficulty. That would be simpler and easier to read. 

  "Higher values of these meta-features generally indicate greater
  classification difficulty (except for C1)."

4.2.2
-----

- "When considering variance, a similar trend emerges. According to
  the fANOVA results (Figure 3b), C1 continues to dominate, accounting
  for 37.78% of the variability in variance."

  I wouldn't call this a similar trend. For bias, C1 accounts for 71%,
  for variance, 38%. Please point out that the C1 impact on variance is significantly lower than on bias. This suggests other factors play greater role. Discuss what those factors might be.

### Questions
No questions, but recommendations for future submission:

- drop the analysis of dataset complexity vs. hyperparameters; just
  focus on the impact of hyperparameters on the bias/variance
  trade-off. It is sufficiently important topic on its' own. Impact of dataset complexity is not useful because 1) it is well understood that dataset complexity has major impact on classifier performance 2) it is not clear what to do about it.

- include multi-class problems

- include XGBoost and neural networks in the analyses. I don't think
  one can make practically useful conclusions without including those
  state-of-the-art classifiers. I would personally also add logistic
  regression

- consider adding image classification datasets in your analyses. If
  the behavior - in terms of bias/variance, and hyperparameter tuning
  contribution - is quite different from tabular data, that would be a
  valuable result

I think this *could* become a good paper, but not without extensive
revision, which is not feasible in the ICLR timeframe.


Minor points

3.3
---

- 2 out of 3 is not really "generally". Please just be specific: for
  N1 and T1, higher values indicate greater classification
  difficulty. For C1, lower values indicate greater classification
  difficulty. That would be simpler and easier to read. 

  "Higher values of these meta-features generally indicate greater
  classification difficulty (except for C1)."

4.2.2
-----

- "When considering variance, a similar trend emerges. According to
  the fANOVA results (Figure 3b), C1 continues to dominate, accounting
  for 37.78% of the variability in variance."

  I wouldn't call this a similar trend. For bias, C1 accounts for 71%,
  for variance, 38%. Please point out that the C1 impact on variance is significantly lower than on bias. This suggests other factors play greater role. Discuss what those factors might be.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper focuses on the attribution of predictive model behavior. In particular, it describes a comprehensive empirical comparison of the influence of hyperparameters and dataset meta-features on the bias and variance of classifiers. The analysis utilizes functional ANOVA. The main result is that most of bias and variance can be attributed to dataset characteristics, as opposed to hyperparameters.

### Strengths
- Well structured and clearly written paper.
- A many ways a very comprehensive experiment.
- Tackles an important issue for ML practitioners.

### Weaknesses
I have two main concerns. The first is that the experiments, while in some ways very comprehensive, are in other ways very limited:

- Only two classification algorithms.
- No missing values in the dataset is a very strong criterion.
- A limited number of complexity measures.

The second is that when carefully interpreted, the results are not that general or actionable:
- N1 is in essence a classifier (probably along the lines of LDA). So the results can basically be summarized that most of the bias and variability of RF and SVM can be explained by running another reasonable classifier and seeing how it performs. That of course makes perfect sense, but it can also be derived from what we already know, that classifiers tend to perform similarly (the differences between classifiers are less than the differences between datasets).
- We should be more careful when interpreting the result that model performance can be attributed more to dataset characteristics than to hyperparameters. First, it is the nature of commonly used classifiers that they are relatively robust in terms of hyperparameter selection - being easy to tune is what makes them popular. Second, . And third, the range of several parameters is limited. For example, would results change if max_features was allowed to go below 0.1 or above 0.9? Or if 20 different kernels were considered? Similarly, the experiments are limited to 1500 features, which diminishes the importance of regularization.
- In practice, I can in most cases freely tune the parameters and select models. I can't really change my problem (or dataset) though.
- The paper does not consider model selection, which I would in this context consider as part of hyperparameter tuning. I would not be surprised that a lot more can be attributed to model selection than to tuning the parameters in this paper. Choosing a different model is also actionable.

There are also other methodological concerns (see Questions).

### Questions
1. fANOVA is one of many ways of decomposing model predictions. Why this approach? And are there any potential issues due to taking into account pairwise interactions only?
2. l. 60: How can normalization or scaling affect the intrinsic complexity of the datasets? Intuitively, wouldn't a reasonable measure of complexity be invariant to these? Of the three in the paper, C1 is invariant. T2 is not, because it depends on PCA, but that just makes me wonder if T2 even makes sense. I wouldn't want my dataset to become more complex, just because I convert a feature from meters to centimeters. N1 is based on a two-sample test, so, while I didn't go into the details of the test, I'd assume that we'd like all of our two sample tests also to be invariant to scaling. ... To clarify, I'm not criticizing the choice of not scaling, we can argue either way. But I am concerned about the use of complexity metrics that are not invariant.
4.But not normalizing does have an effect on SVM and regularization? This is not how we would apply SVM in practice.
5. N1 is a bit outdated. Two sample tests have progressed a lot in recent years. In particular, tests based on machine learning models directly or using classification performance as a proxy.
6. It seems that N1 would fail to be attributed when the dataset is so complicated that RF and SVM can perform well, but the test in N1 doesn't?
7. The attribution to C1 for SVM is to me the most surprising result in the paper. Any explanations of this difference between SVM and RF? How correlated are N1 and C1?
8. l. 658: How reasonable is this assumption that there are no hidden confounding factors?
9. Parameter configurations were generated by sampling uniformly and independently from each hyperparameter range? I'm asking because of the following scenario. Let's say that the optimal range for a parameter is relatively narrow (0 - 0.05), while after that (0.05 - 1.0) the model performs majority class baseline poorly. Because the range of good values is small, this, as a variable in a regression, would not be that important. So, it would not get much of an attribution in the experiment, but it is definitely important in practice. In other words, isn't the importance of a hyperparameter determined by the difference it can make, not by the variability of the performance over some arbitrary set of its values?

### Soundness
2

### Presentation
4

### Contribution
2
