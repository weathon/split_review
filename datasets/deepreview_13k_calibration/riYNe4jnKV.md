# Calibration-then-Calculation: A Variance Reduced Metric Framework

- Decision: Reject
- Avg Score: 4.60
- Scores: 3, 6, 5, 3, 6

## Abstract
Deep learning has been widely adopted across various fields, but there has been little focus on evaluating the performance of deep learning pipelines. With the increased use of large datasets and complex models, it has become common to run the training process only once and compare the result to previous benchmarks. However, this procedure can lead to imprecise comparisons due to the variance in neural network evaluation metrics. The metric variance comes from the randomness inherent in the training process of deep learning pipelines. Traditional solutions such as running the training process multiple times are usually not feasible in deep learning due to computational limitations. In this paper, we propose a new metric framework, Calibrated Loss, that addresses this issue by reducing the variance in its vanilla counterpart. As a result, the new metric has a higher accuracy to detect effective modeling improvement. Our approach is supported by theoretical justifications and extensive experimental validations in the context of Deep Click-Through Rate Prediction Models and Image Classification Models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The submission proposes a new metric to evaluate deep learning models. The main idea is to calibrate the "bias" of the deep learning model that contributes to the randomness in evaluating them. The algorithm is proposed to split the test set into test-val and test-remaining splits and then using the test-val set to calibrate the model predictions before calculating the metric values. The accuracy of the proposed metric itself is also defined as the probability that a better model A will be measured as being better by the proposed metric.
The evaluation of the proposed metrics is done using deep CTR prediction and image classification.

### Strengths
- The idea of tackling randomness in evaluation of deep learning models is important.
- The proposed method seems to have strong theoretical background.
- The empirical evaluations are in favor of the proposed metric.

### Weaknesses
 - I am not fully convinced that the proposed algorithm is realistic. For instance, to obtain the calibrated metric one must have a separate validation set, which is not always the case. One could split the test set into test-val and test-test splits like described in the submission, but that means using a different set of data to test the model, which in itself would be another problem. Furthermore, the calibrated metric seems to be model and data specific as it uses a specific model's predictions and validation data to calibrate the bias term. This would lead to evaluating multiple models which all use individually different metrics. I do not particularly think that would be a step towards robust and fair comparison of deep learning models.

### Questions
- As mentioned in the weakness, wouldn't the proposed algorithm lead to different metrics being used for different combinations of models and validation data?

### Soundness
3 good

### Presentation
3 good

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
This paper provides a new framework to evaluate deep learning pipelines. For classification, the model output is adjusted by a posthoc calibration method on the test-validation dataset, then the adjusted model is evaluated on the remaining test set. For normal regression, the bias-adjusted term is calculated on the test-validation dataset, then the quadratic loss is applied to the bias-adjusted predictions on the remaining test set. 
Theoretically, the paper shows the proposed metric has lower variance for linear regression. Empirically, on click through rate predictions and image classification data sets, the proposed metric has low variance and better accuracy.

### Strengths
Providing a better evaluation of the deep learning pipeline is an interesting topic. This paper provides an easy-to-understand and easy-to-implement framework to improve the metric variance and accuracy. Numerical examples demonstrate the proposed metrics provide a better way to compare different deep learning pipelines.

### Weaknesses
1. My understanding is that the proposed framework applied a posthoc calibration on the trained model using a calibration set to adjust model prediction, then used the same loss function(cross-entropy loss for classification and $L_2$ loss for regression) to the adjusted model output on a separate test set. Frame it as a new loss is a bit confusing

2. The $\text{Acc}(\bar{e})$ defined in equation 5 relies on a ground truth metric, which makes the framework a bit hard to interpret. For example, in the CIFAR10 experiment, accuracy and log loss give different comparison results, I think this can happen because the larger model overfits in terms of cross-entropy loss, but accuracy doesn't drop(e.g. Figure 3 in [1]). The larger model is more accurate but not well-calibrated[1]. In the paper, it says "this metric inconsistency can be mitigated by Calibrated Log Loss", but I think a better way to explain the result is that after applying the posthoc calibration method, the larger model can have better calibration(in terms of cross-entropy loss).

3. Some subtle issues: 

(1) accuracy is used as the ground truth metric in CIFAR10 experiments, but a model with higher accuracy or lower loss is better, this can cause some problems in the definition 3. 

(2) On top of page 4, it says the bias-adjusted predictions $q_i$ are well-calibrated. But calibration usually means $E(Y|f(X)) = f(X)$ for all $f(X)$, the property only says the calibration error is 0 if evaluated using only 1 bin. So I think the claim is not appropriate.

(3) For the Generalization to Quadratic Loss, $e_1$ is defined using $E_{D}$, I think $E_{D}$ needs to be estimated on the val-test set, would it be better to define $e_1$ using $E_{\hat{D}_{\text{val-test}}}$?

### Questions
Please see the weakness part.

An additional question, in several comparison results shown in the paper, although the "Calibrated Log Loss Acc" is larger, it is still around 60% or 70%, far from the significance level usually used in statistical hypothesis testing to compare two methods. When we have these comparison accuracies, what would the authors suggest to say about the comparison of the two pipelines?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors use the validation set loss (in Algorithm 1) to recalibrate their model for the  quadratic loss, the binary logistic loss (with a additional intercept tuned on the validation set) and multi-class logistic losses (with a temperature parameter).
For the quadratic loss in linear regression, they prove that this procedure leads to variance reduction and verify that via synthetic experiments.
There is no such mathematical proof for the binary or the multi-class logistic loss, but the authors demonstrate variance reduction via a series of experiments on synthetic, CTR and image datasets.

### Strengths
1.
The large number of experiments with sparse and dense features, synthetic, CTR and image datasets seem to illustrate the basic idea of the paper on re-calibration quite well.

2.
Corollary 4.2 regarding linear regression seems to be an interesting new result.

### Weaknesses
1.
Since the log loss accuracy reported in Tables 1 - 7 does not benefit from the use of the validation set to tune additional calibration hyper-parameters, whereas the calibrated log loss accuracy uses this validation set, it is no surprise that the calibrated log loss accuracy is always higher than the log loss accuracy. This is akin to comparing a model whose hyperparameters are tuned via cross-validation with one that only sees the training set and does not undergo hyperparameter tuning via cross-validation, with the only difference being that the additional hyperparameter introduced in this method is separately introduced via a connection to calibration. The variance reduction property should also not be considered a surprise if the baseline is overfit on the training set.

2.
The lack of theoretical guarantees on the binary or the multi-class logistic loss also makes one wonder if the variance reduction property holds in general.

3.
Typos exist in the paper, e.g., "Calibratied" after Corollary 4.2

### Questions
Is the first pipeline in Table 2 labeled "dense" the same as the first pipeline B in Table 1 labled "remove dense" ?
If not, the reason for removing dense in Table 1's first row and keeping dense in Table 2's first row is not clear.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new metric, Calibrated Loss, that addresses the challenges of evaluating deep learning pipelines. Calibrated Loss is a variance-reduced version of the vanilla loss metric, which makes it more accurate in detecting effective modeling improvement.

The authors provide theoretical justifications for their approach and validate it on two different types of deep learning models: Click Through Rate Prediction and Image Classification models.

### Strengths
1. Effective evaluation is critical for the development of machine learning algorithms.
2. The paper is well-organized and easy to follow.
3. Implementation is provided in the supplementary material.

### Weaknesses
### Major issues
1. The notations are unnecessarily redundant. For example, we can use $e, f$ to represent the metrics, and $A, B$ to represent the pipelines. $h$ represents the model name. It is redundant since it is a subset of the pipeline. Please reduce the usage of necessary superscripts and subscripts.
2. The paper focuses on the comparisons between two pipelines, which was not necessary. The paper should pay attention to the variance reduction in the performance evaluation of pipelines, i.e., the equation at the bottom of Page 2. For example, the histograms in Figure 1 are good visualization for the variance reduction. Please add similar figures for other experiments. The core issue is demonstrating the reduction in variance of the metric itself, not just in the context of comparing two pipelines. The focus should be on showing that the proposed metric, when applied to the same pipeline multiple times, yields a more consistent result than the original metric.
3. How do we handle the bias-variance tradeoff in the equation at the bottom of Page 2? The paper does not discuss how the calibration process might introduce bias into the metric, which is a critical consideration. A method that reduces variance at the cost of introducing significant bias is not necessarily an improvement. There needs to be a discussion of how the calibration method is chosen to minimize bias while reducing variance.
4. The Calibrated Loss for multiclass classification is the existing method of "Temperature Scaling". Why is it a proposed method? What is the contribution on that in this paper? The paper needs to clearly articulate the novelty of applying temperature scaling in this specific context, beyond simply stating that it is used for calibration. The connection between temperature scaling and the broader goal of reducing variance in pipeline evaluation needs to be more explicit.
5. Calibration of the evaluation results is a general topic. The paper lacks discussions and comparisons of the related work. The paper should discuss existing methods for calibrating evaluation metrics, and how this work relates to those methods. It should also discuss the limitations of the proposed approach compared to other calibration techniques.
6. In Section 4, there is less randomness with a larger test dataset. The original metric $e$ is good enough for evaluation. The difference between $e_1$ and $e$ will become smaller with a larger $n$. However, for the $e_1$, we may need to split the test dataset into two disjoint subsets, one for calibration and one for true evaluation, which will decrease the effective dataset size $n$. In that case, can we claim that $e_1$ is better than $e$? If $n=2$, $e$ can use the average of these two samples to obtain the final result, while $e_1$ should use one example for calibration and use the other one as the final result. In this case, which case is better? What if $n=10k$ and even infinity?

### Minor issues
1. Please number every equation in the paper.
2. In Equation 3, $R_e(h)$ is a random variable. A is better than B iff $P(R_e(h_A) < R_e(h_B)) > 0.5$. However, we usually use expectation or its estimations to compare A and B. Specifically, A is better than B iff $\mathbb{E}(R_e(h_A)) < \mathbb{E}(R_e(h_B))$. For example, we mainly compare the average classification accuracy. Equation 3 seems uncommon, which may require further discussions and citations.
3. The theoretical justification is only on the linear regression, and the randomness only comes from the dataset, which is limited. A more general setting (e.g., convex problem, randomness in SGD) is expected.

### Questions
Please see the weaknesses for details.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presented a new approach to comparing the performance of different deep learning pipelines and proposed a new metric framework, Calibrated Loss, which has a higher accuracy and smaller variance than its vanilla counterpart for a wide range of pipelines.

### Strengths
A new evaluation framework which can save much computation resource when it face accurate or multiple evaluations.

### Weaknesses
The generalization part in section 3 is vague. It is better to illustrate how to generalise in detail. The paper does not sufficiently explain the practical limitations of the proposed Calibrated Loss framework. Specifically, while the paper claims the framework saves computation resources, it does not discuss the computational overhead introduced by the calibration process itself. This is a critical oversight, as the calibration step might be computationally expensive, especially for large models or datasets, potentially negating the claimed savings. Furthermore, the paper lacks a discussion on the sensitivity of the Calibrated Loss to the choice of calibration method. Different calibration techniques might lead to different results, and the paper should provide guidance on selecting appropriate calibration methods for various scenarios.

### Questions
1. I don't understand the first line of Table 7 shows the log loss acc is only 5.6% for resnet101 over resnet18. Could you please explain more?
2. Log loss can sometime indicate the classification accuracy of a model, but they are not identical. How you define model A is better than model B? If I want to focus on accuracy, not log loss, how to apply your method?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
