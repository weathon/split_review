# Weight-Based Performance Estimation for Diverse Domains

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
One of the limitations of applying machine learning methods in real-world scenarios is the existence of a domain shift between the source (i.e., training) and target (i.e., test) datasets, which typically entails a significant performance drop. This is further complicated by the lack of annotated data in the target domain, making it impossible to quantitatively assess the model performance. As such, there is a pressing need for methods able to estimate a model's performance on unlabeled target data. Most of the existing approaches addressing this train a linear performance predictor, taking as input either an activation-based or a performance-based metric. As we will show, however, the accuracy of such predictors strongly depends on the domain shift. By contrast, we propose to use a weight-based metric as input to the linear predictor. Specifically, we measure the difference between the model's weights before and after fine-tuning it on a self-supervised loss, which we take to be the entropy of the network's predictions. This builds on the intuition that target data close to the source domain will produce more confident predictions, thus leading to small weight changes during fine-tuning. Our extensive experiments on standard object recognition benchmarks, using diverse network architectures, demonstrate the benefits of our method, outperforming both activation-based and performance-based baselines by a large margin.  Our code is available in an anonymous repository: https://anonymous.4open.science/r/79E9/

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method for estimating the generalization performance of deep neural networks under distribution shifts. The key contribution is the analysis of network weights to estimate generalization. The authors show that the distribution shift between the source and target datasets can be captured by the difference in network weights. Insipire by this, they propose a weight-based approach that estimates the performance of the network from the degree of weight changes incurred by fine-tuning the network on the target dataset with an unsupervised loss. Experimental results show that the proposed method is effective in estimating generalization performance on three image classification datasets with different backbones.

### Strengths
1. In addition to activation-based approaches and performance-based approaches, the paper proposes a weight-based approach for model accuracy prediction. This approach makes sense and is somewhat novel to me. The method is simple and straightforward.

2. The performance of the proposed approach is good compared to performance-based and activation-based methods.

3. The paper writing is clear and easy to understand.

### Weaknesses
1. The paper presents a reasonable alternative to performance-based and activation-based accuracy prediction methods. However, the conclusion is not much surprising to me, since utilizing the change of weights has already been a common approach, showing effectivenss in extensive unsupervised and semi-supervised learning literature. Besides this point, I didn't see many significant flaws in this paper. Therefore, the paper is kind of on the 'borderline' to me. My initial rating is borderline accept.

2. An experiment of $N$-model accuracy ranking would make the conclusion stronger. The proposed only evaluates one model compared against a GT accuracy. However, the MAE of accuracy is hard to interpret, e.g., would 1% on one dataset be better than 3% on another one? It's more meaningful to rank accuracies of $N$ models trained on the same dataset then compare the predicted ranking list to GT ranking list. This evaluation may be a better metric than MAE.

3. Some related work that investigated model weight changes for SSL are expected be discussed, e.g., MeanTeacher [1] and Temporal Ensembling [2].

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This study challenges the standard in performance prediction models that utilize activation or performance metrics, highlighting their diminished accuracy when facing domain shifts. This work suggests employing a weight-based metric, observing the variance in the model's weights pre- and post-fine-tuning with a self-supervised loss—specifically, the entropy of the network's predictions. The premise is that minor weight adjustments post-fine-tuning correlate with target data similarity to the source domain, suggesting higher confidence in predictions.

### Strengths
+ This motivation is sound. Existing methods aim to explore a proxy that can reflect the model accuracy on unlabeled test sets. They typically use feature representations or model outputs. This work explores the weights information. 

+ It seems the authors try very hard to build up the experimental setups, including dataset creation, and train various models, and build up baselines.

### Weaknesses
 - *Lack of Novelty*: The method proposed in this manuscript closely resembles the technique described in "ProjNorm" by Yu et al. (2022). While the authors have introduced Shannon entropy as a means to differentiate from the aforementioned work, this change appears marginal and does not substantially deviate from the core idea presented in ProjNorm. The application of Shannon entropy in this context does not seem to provide a significant methodological improvement or lead to new insights, as the primary concept and application remain largely unchanged.

- *Limited Experimental Setup*: The experimental framework, as it stands, is limited in scope. For the work to be comparative and relevant, inclusion of standard datasets such as CIFAR-10 and ImageNet-1K is essential. These datasets are benchmarks in the field and are used across recent literature, providing a common ground for comparing innovative approaches. Furthermore, the paper should benchmark against recent studies, particularly those concerning prediction under distribution shift and unsupervised accuracy estimation. I recommend the authors examine works such as "Predicting out-of-distribution error with the projection norm," "Agreement-on-the-line: Predicting the performance of neural networks under distribution shift," and "Confidence and Dispersity Speak: Characterising Prediction Matrix for Unsupervised Accuracy Estimation."

### Questions
- Please see the above weakness and pay attention to ProjNorm which already reported the same idea. Please consider the current methods and especially the setups as so to make experiment more convincing.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors tackle the practical and challenging problem of estimating performance of a given trained model on new data that is unlabeled and could be out of distribution from the model’s original training and test data. Making progress on this problem has the potential to save downstream users of machine learning models significant time and effort implementing an ML-appropriate data labeling process to evaluate performance of a model, only to determine that existing models do not perform well enough to be useful for their task of interest. This has the downside of making that labeling process a significant investment of resources without clear benefit, which is increasingly harmful if the users have limited resources, for example nonprofits or historically under-resourced communities. The authors propose an alternate approach for unlabeled performance estimation that is designed to be more predictive when domain shifts occur between the training dataset and the unlabeled test data. This method utilizes a self-supervised finetuning step on the unlabeled dataset and looks at the amount of weight change in the network activations pre and post finetuning as the input to a linear predictor of performance, based on the idea that a smaller change in model weights would correspond to more similarity between train and the unlabeled dataset and thus higher performance. They show that this method outperforms previous performance estimation methods focused on linear prediction from activations or predicted scores on some types of domain shift.

### Strengths
The paper is clearly written, the related work section is clear and their contributions and how those contributions compare to prior work is thorough. The characterization of model weight change into magnitude and consistency of updates provides an intuitive framing of the method, and their approximation of both of these these changes as a weight difference after a fixed number of model updates makes the method simple and tractable. The figures are useful when building intuition about the method, and clearly show how this method improves over prior work on very specific examples of domain shift.

### Weaknesses
This method strongly relies on the self-supervised objective being able to capture similarity and difference between train and test domains. They show that this is an effective measure for many traditional domain adaptation benchmarks, where there is a strong visual distinction between the target and source (major shifts in color or background for digit classification, for example). This type of domain shift, where there are clear visual differences that can be easily captured by a self-supervised objective, is unlikely to be as beneficial for performance estimation for both (1) domain shifts that are visually similar, but where the subpopulation shift of categories of interest leads to lower performance, and (2) domains where self-supervised objectives fail to build useful representations vs supervised ones, for example domains with fine-grained categories (see https://arxiv.org/abs/2105.05837).

### Questions
The lack of demonstration of the method on more diverse or possibly more realistic types of domain shift does not render the value of the method useless, as there are many domain shift problems that are mainly characterized by visual shift or where visual shift is a strong component of performance degradation (like the shifts seen between MNIST and USPS). I would have liked to see a more nuanced discussion of what types of signal or shift this method is well-posed to capture and for what types of domain shift it is not as well-posed. This could be demonstrated with performance estimation results on more realistic domain shift benchmarks that capture the types of complex changes between “domains” seen in the real word, like the WILDS benchmark. I think this would improve the clarity of the claims the authors are making, and help possible practitioners determine whether they should rely on this performance estimation method in practice. Similarly, some discussion or formalization of what types of shift may cause maximal weight change with their chosen self-supervised objective, and why, would also strengthen the paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
