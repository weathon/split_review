# A Differentiable Rank-Based Objective for Better Feature Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In this paper, we leverage existing statistical methods to better understand feature learning from data. We tackle this by modifying the model-free variable selection method, Feature Ordering by Conditional Independence (FOCI), which is introduced in Azadkia & Chatterjee (2021). While FOCI is based on a non-parametric coefficient of conditional dependence, we introduce its parametric, differentiable approximation. With this approximate coefficient of correlation, we present a new algorithm called difFOCI, which is applicable to a wider range of machine learning problems thanks to its differentiable nature and learnable parameters. We present difFOCI in three contexts: (1) as a variable selection method with baseline comparisons to FOCI, (2) as a trainable model parametrized with a neural network, and (3) as a generic, widely applicable neural network regularizer, one that improves feature learning with better management of spurious correlations. We evaluate difFOCI on increasingly complex problems ranging from basic variable selection in toy examples to saliency map comparisons in convolutional networks. We then show how difFOCI can be incorporated in the context of fairness to facilitate classifications without relying on sensitive data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new method called difFOCI, which bases on an existing approach called FOCI. FOCI is a tool for choosing important features from data based on their statistical relationships, but it is not easy to use in some deep learning tasks because it does not adapt well to different models.  Motived by this, difFOCI creates a flexible, learnable version of FOCI that can be used in more situations.

This submision uses difFOCI in three ways: as a tool to pick important features, as part of a model that learns using a neural network, and as a method to help models learn better by reducing irrelevant correlations in the data. To validate this, this submission tests difFOCI on a range of tasks, from simple examples to more complex problems like understanding which parts of images are important in neural networks. Also, difFOCI is shown to be helpful in making fairer predictions by letting models classify without depending on sensitive information.

### Strengths
- The motivation is clear to me. FOCI is a tool for selecting important features from data based on their statistical relationships. However, it is not differentiable, which hinders its use in deep neural networks. To address this limitation, this submission proposes a differentiable, parametric approximation.
- This submission provides a clear definition of difFOCI. The toy examples offer some intuition into how difFOCI works.
- The three applications are well-chosen. They effectively demonstrate the usefulness of difFOCI.

### Weaknesses
 - While some real-world datasets are used in the experiments to demonstrate the effectiveness of difFOCI, it is unclear if it can be extended to large-scale datasets. Specifically, the datasets in Section 5.1 are small-scale, and the neural networks or learning algorithms used are relatively simple. The Waterbird task, for example, is simpler compared to multi-class tasks. Please discuss the scalability and generalization potential of difFOCI. It would be beneficial to see experiments on datasets with significantly more samples and higher dimensionality to assess the practical applicability of the method. The current experiments do not fully explore the computational cost associated with difFOCI, which could be a limiting factor for large-scale applications.
- The fairness study is interesting; however, the dataset and task here are relatively simple. Can difFOCI be applied in large-scale settings? The fairness evaluation is limited to a binary classification problem with a single sensitive attribute. It would be more compelling to see evaluations on datasets with multiple sensitive attributes and more complex fairness criteria. The current evaluation does not fully explore the potential trade-offs between accuracy and fairness that might arise in more complex scenarios.
- The visualization in Figure 2 is not very clear. What is the main takeaway from this figure? Additional visualization examples would be helpful. The visualization lacks clear labels and annotations, making it difficult to interpret the results. It is not immediately obvious what aspects of the image are being highlighted by the difFOCI method. The figure would benefit from a more detailed explanation of the visualization process and the specific features being analyzed.

### Questions
- Please discuss the scalability of difFOCI on large-scale datasets and its applicability to more challenging tasks.
- Additionally, please clarify the purpose of the visualization in Figure 2.

### Soundness
3

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
3

### Summary
This paper uses existing statistical methods to better understand feature learning from data, by modifying an existing model-free variable selection method to a trainable version. Experiments on toy examples and real world datasets show the effectiveness of the proposed method.

### Strengths
1. The motivation of the paper is well stated.
2. The paper is well-structured and well-written.
3. Providing results on both toy experiments and real world datasets makes the paper more solid.

### Weaknesses
1. The real world datasets seem to be out-dated, where the latest one was released in 2019. It would be more convincing to presents results on more recent are more complex datasets, such as those in WILDS benchmark.

2. This paper only considers one model architecture, i.e., ResNet-50. With the increasing usage of Transformer-based models, it is also important to show the effectiveness on more complex models.

3. Simply showing the improved performance on worst group accuracy does not sufficiently suggest the decrease reliance on the spurious features. Note that, the overall performance of the proposed method shows consistently lower performance \(2 - 4%\) for average accuracy. It would be suggested to conduct the synthetic experiments in [1].

4. Another concern is that the experiments are conducted on the case where the train test set share the same distribution. Given that the feature selector is a trained NN, it is interesting to show if such a method maintains its performance of feature selection where the train test set have a different distribution.  For example, CIFAR10 vs CIFAR10.1, DomainNet-real vs DomainNet-Sketch? as in [2].

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces an algorithm (difFOCI) that gives a measure of correlation based on Feature Ordering by Conditional Independence (FOCI). The method is differentiable and can be used in ML methods. It is used in 3 ways: 

dF1) maximize T(Y,fθ(X)); 

dF2) minimize loss + T(X_G,fθ(X)) such that the features are independent of group features

dF3) maximize T(Y,fθ(X)|X_S) such that features are correlated with Y when conditioned on X_s

Synthetic and more real data experiments are performed for all cases.

### Strengths
* S1. The proposed method is sound and has good potential for feature selection and feature debiasing 

* S2. The method has mainly good results in synthetic and some real datasets.

### Weaknesses
 * W1. The experiments on real datasets are not that strong. 

* W1.1 For the spurious correlation experiments, Waterbirds dataset is a small and simple dataset and a successful method should be tested on other datasets besides it. How many seeds were used? Was the same protocol used to select hyperparameters for the baselines and the proposed method? The benchmark used in [A] can be used to evaluate the proposed method more rigorously. The results of the method will be more reliable if multiple datasets from [A] were used, together with similar hyperparameter selection and evaluation.


* W2. For the fairness experiments, some additional explanations are needed. 

* W2.1 Are the explicit features Xs a subset of X? 

* W2.2 The authors state that “the predictor should be independent of one or more sensitive features”. How is this enforced? By maximizing T (Y , θ ⊙ X | Xs ) the model would learn to predict the target when we know Xs. Is this right? Can the authors explain this?

* W2.3 Is there a measure to evaluate if the model relies on sensitive features? At the moment the results only report performance, and it is not clear if these results incorporate sensitive features or not.


 
Minor: 
* In the context of Waterbirds, group refers to the combination of class and spurious variable (background). So X_G should be denoted as a spurious variable, not a group variable.

### Questions
See weak points.

### Soundness
3

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
2

### Summary
This paper introduces Chatterjee’s coefficient into feature learning by proposing a differentiable formulation to estimate it. The conditional dependence metric proposed by the authors is applicable to feature learning and enhances performance in downstream tasks.

### Strengths
1. The proposed correlation estimation term is highly versatile and “plug-and-play,” making it adaptable for feature selection, predictor training, and as a regularizer to mitigate spurious correlations.
2. The paper is well-organized, with clear sections on methodology, relevant theorems, and extensive evaluation experiments that strengthen the contribution.

### Weaknesses
1. There is a disconnect between the theoretical foundation and its practical application, leading to a potentially vacuous theorem. The assumption that the coefficient \(\beta\) of the Softmax function is infinite is impractical, as it is only set to values like 5 in the experiments. This discrepancy undermines the theoretical claims, as the practical implementation operates far from the conditions under which the theoretical results are derived. The theoretical analysis relies on an asymptotic regime that is not achievable in practice, making the connection between theory and practice tenuous.
2. Symbol definitions are ambiguous, as discussed in the questions below.
3. The comparison of the proposed method focuses on conventional methods such as LDA and PCA. It would be beneficial to include comparisons with more state-of-the-art methods. The lack of comparison against contemporary techniques limits the assessment of the proposed method's true potential and relative advantage in the current landscape of feature learning.

### Questions
1. The definition of the rank \( r \) in Line 096 is unclear. What is meant by \( Y_{(j)} \leq Y_{(i)} \)?
2. Line 076 declares \(\sigma\) as a Sigmoid function, yet it denotes the Softmax function. Could the authors clarify this discrepancy?

### Soundness
2

### Presentation
3

### Contribution
2
