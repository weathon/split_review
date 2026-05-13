# On Gradient-Weight Alignment

- Decision: Reject
- Scores: 5, 3, 5, 1

## Abstract
Evaluating the performance of deep networks against unseen validation data is a crucial step to measure generalization performance.
However, ostensibly neither the training nor validation and test data are ever sufficiently extensive to replicate real-world application.
This works advocates for a change of perspective for evaluating performance of deep networks.
Instead of evaluating against unseen validation data, we propose to rather capture when the model starts to prioritize learning unnecessary or even detrimental specifics of training data instead of general patterns. 
While this has been challenging to theoretically derive, we propose *gradient-weight alignment* as an empirical metric to determine performance on unseen data from training information alone.
Our performance measure is efficient and widely applicable, closely tracking validation accuracy during training.
It connects model performance to individual training samples, enabling its use not only for assessing generalization and as an early stopping criterion, but also for offering insights into training dynamics.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes gradient weight alignment (GWA) as a metric to evaluate the generalization of neural networks during training without requiring a validation set. Specifically, GWA captures the similarity between per-sample gradients and model weights. Furthermore,  directional dispersion (kurtosis of alignment distribution) is used to measure how heavy the tail of alignment score distribution is. A computationally efficient mini-batch estimator for GWA is introduced, making it feasible for large-scale models.

Empirical results show that GWA is a good metric for generalization, and can serve as an early stopping criterion.

### Strengths
1. The paper is well-written and easy to follow.

2. The paper conducts extensive experiments to support the claims.

### Weaknesses
1. The motivation for using GWA is not clear. Why does a good alignment of training sample gradients indicate good generalization? Specifically, the paper does not adequately explain why aligning per-sample gradients with model weights, which represent the current state of the model, is a meaningful indicator of generalization. The gradients quantify the direction of weight updates, and it's not immediately obvious why their alignment with the weights themselves should correlate with the model's ability to generalize to unseen data. What if the training samples are noisy and some of the samples may not be useful?

2. It is unclear what properties the lightweight GWA estimator satisfies. The paper introduces a computationally efficient mini-batch estimator, but it lacks a rigorous analysis of its statistical properties. For example, it is not clear whether the estimator is biased or consistent, and how its variance scales with the mini-batch size. Without such analysis, it's difficult to assess the reliability of the estimator, especially when applied to complex models and datasets.

3. Minor

- abstract line 12, "This works advocates" -> "This work advocates"

- lines 408-409, "during in the" -> "during the"

### Questions
1. What is the intuition to use alignment between per-sample gradients and the model weights? The former quantifies the change of the weights, which can be very different from the model weights. Is it only suitable for classification models or can also be used in regression models?

2. The paper regards the lightweight GWA estimator to be one of the core contributions. However, it is unclear whether the estimator has desirable properties such as unbiasedness.

3. Why does a good alignment of training sample gradients indicate good generalization? What if the training samples are noisy and some of the samples may not be useful?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a novel approach to assessing model generalization by focusing on the alignment between model gradients and weights during training. Specifically, it introduces a metric termed Gradient-Weight Alignment (GWA). Motivated by the limitations of validation sets in representing real-world distributions, the authors seek a method to evaluate model performance using only training data. The proposed algorithm calculates the cosine similarity between per-sample gradients and model weights. This implementation involves monitoring directional alignment and directional dispersion as two key indicators. The authors claim that high alignment and low dispersion correlate with effective generalization. Experimentally, GWA is shown to closely track validation accuracy across various models and datasets, and it serves as a robust early stopping criterion—especially useful in scenarios with label noise or significant domain shifts.

### Strengths
1. This paper introduces a lightweight and scalable estimator for alignment scores that is applicable to large models and noisy datasets. The two proposed indicators can be used to predict generalization performance.
2. The proposed metric is easy to implement and expected to be more stable than previous methods.

### Weaknesses
1. The main concern is the significance of this work. The idea of measuring gradient similarity is not new. Although this paper considers the alignment between gradients and weights, which is different from existing methods, it’s not clear why the former is superior to the latter in terms of generalization estimation. Regarding memory cost and computational complexity, I think some existing methods, such as Stiffness, can also be extended to a faster stochastic version, similar to the operation in Algorithm 1, line 9. Apart from empirical evaluations, it would be better to see more insightful analyses of GWA’s effectiveness, specifically, why GWA is more effective than measuring gradient similarity between samples for generalization estimation.
2. For the experiment assessing the generalization gap in Section 4.4, only a validation set is used as the baseline. Other popular metrics that do not rely on a validation set should also be evaluated. Specifically, sharpness estimation (e.g., sensitivity to input noise) and gradient norm are two common ideas that could serve as baselines. Additionally, the reported accuracies on both CIFAR-10 and CIFAR-100 are too low. Popular deep models, such as ResNet-18, typically achieve >90% accuracy on CIFAR-10 and >70% on CIFAR-100 with standard training techniques. The current experiments do not sufficiently demonstrate that GWA achieves state-of-the-art performance in predicting the generalization gap. For CIFAR-C and CIFAR-P in Table 1, validation accuracy can't be supposed to be an upper bound since the test set follows a different distribution with the training/validation sets.
3. The experiments in Sections 4.1 and 4.2 are mostly qualitative, showing the correlation between directional alignment and validation accuracy. This could be evaluated in a more rigorous way, such as through quantitative analyses comparing model selection using GWA with baseline algorithms. For example, the correlation between the alignment scores and validation accuracy could be quantified by sampling multiple checkpoints along the training trajectory.
4. Minor Issues: 
   - 1) The y-axis of the second and fourth plots in Figure 3 should be labeled *Val. error* instead of *Val. acc.*
   - 2) The discussion in lines 412-416 seems unclear, as alignment is naturally easier when only a subset is used to train the model (making fitting easier).
   - 3) The second and third paragraphs in Section 4.4 lack clear logic. They initially suggest that directional alignment is a good predictor of generalization but then recommend using directional dispersion rather than alignment to decide when to stop training.

### Questions
1. In Figure 7 (right), do you choose a specific time/epoch t or calculate the average over the entire training process?
2. In Table 1, what is the size of the validation set?

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
The paper proposes a novel approach to evaluating the performance of deep neural networks without relying on unseen validation data. Recognizing that training, validation, and test datasets are often insufficient to replicate real-world applications, the authors advocate for a shift in perspective. Instead of traditional validation methods, they introduce gradient-weight alignment as an empirical metric to determine a model's generalization performance using only training data.

This metric identifies when a model prioritises learning unnecessary or detrimental specifics of the training data rather than capturing general patterns. The proposed method is efficient and widely applicable, mirroring validation accuracy during training. Connecting model performance to individual training samples not only aids in assessing generalization and serves as an early stopping criterion but also offers valuable insights into the training dynamics of deep networks.

### Strengths
1. The method proposed in this paper is interesting and well-motivated, which allows the evaluation of model generalization without using a validation dataset. 
2. The method is efficient and allows performance at each time step during training, which allows the model to stop training before overfitting occurs on general unseen data. 
3. The author shows extensive empirical results that reveal the correlation between proposed metrics and model performance on different image-classification tasks.

### Weaknesses
The paper provides many evaluations on C10 and C100 image classification tasks, which are pretty narrow analyses for evaluation generalization purposes; more experiments on ImageNet-1k would be beneficial. The exclusive focus on image classification, specifically CIFAR datasets, limits the assessment of the proposed metric's robustness across diverse data modalities and task complexities. Furthermore, while the authors demonstrate a correlation between their metric and validation accuracy, the causal relationship remains unclear. It is not definitively shown that optimizing for gradient-weight alignment directly leads to improved generalization, or if it is merely a correlated phenomenon. This raises concerns about the practical utility of the metric as a standalone optimization target or early stopping criterion without further validation on a wider range of tasks.

### Questions
1. Based on the abovementioned weakness, will these metrics work on other tasks, such as object detection or segmentation?
2. Many recent works on Zero-cost NAS metrics also mention training dynamics, such as:
[1] Li, G., Yang, Y., Bhardwaj, K., & Marculescu, R. ZiCo: Zero-shot NAS via inverse Coefficient of Variation on Gradients. In The Eleventh International Conference on Learning Representations.
[2] Xiang, L., Hunter, R., Xu, M., Dudziak, Ł., & Wen, H. (2023, December). Exploiting network compressibility and topology in zero-cost NAS. In International Conference on Automated Machine Learning (pp. 18-1). PMLR.

How do the proposed methods perform differently with those works? It would be good to compare the performance prediction ability by showing the correlation on specific NAS benchmarks, like NASbench101, 201 or NASlib, that might be a good approach to show that this metrics is well correlated to the trained validation accuracy.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
For each sample $x$ and training step $t$, the paper considers the alignment between the negative sample gradient ${\bf g}_t (x)$ of the loss function corresponding to the sample $x$ and the model weight vector ${\bf w}_t$ at the training step $t$ and defines a notion called per-sample alignment score $\gamma_t (x)$ as the correlation between  ${\bf g}_t (x)$ and ${\bf w}_t$. Since $x$ can be regarded as a random variable, so is  the per-sample alignment score $\gamma_t (x)$. The paper then refers to the first moment of the random variable  $\gamma_t (x)$ as the directional alignment, and the kurtosis of the random variable  $\gamma_t (x)$ as the directional dispersion. Both the directional alignment and dispersion are estimated from a mini batch during the course of training via the standard exponential moving average approach. The estimated directional alignment and dispersion are then used to analyze empirically the training dynamics during the course of training. Based on limited experiments, some observations are made in terms of using directional alignment and dispersion to track validation accuracy during the course of training, determine an early stopping time without using any information from the validation set, and analyze performance contributions from individual samples.

### Strengths
The only strength I can think of is the introduction of per-sample alignment score $\gamma_t (x)$ defined as the correlation between  ${\bf g}_t (x)$ and ${\bf w}_t$.

### Weaknesses
The paper is not mature enough. Its position is not clear, experiments are limited, research statements are inconclusive, and no new insights are really provided.

The authors have to think harder on how to position the paper. As a suggestion, a promising position is to investigate how to use the estimated directional alignment and dispersion to determine an early stopping time without relying on any information from validation sets so that the trained DNN is more robust with respect to different validation sets in the downstream applications. The results presented for this direction so far are limited and not convincing enough. The authors are encouraged to continue along this direction. Other observations and discussions are vague and inconclusive, and will not go anywhere.

1. The explanations and discussions near the bottom of Page 5 are not new. They are well-known and can be explained from the values of cross entropy loss.

2. Something is wrong in Figure 3. For each model in Figure 3, the blue curve on the right sub-figure seems to be validation error rate, not validation accuracy. In addition, why not put the three curves (the validation accuracy curve, directional alignment curve, and directional dispersion curve) into one sub-figure?

3. The observations from Figures 3 and 4 are not conclusive, and vague. The descriptions of the trends are too high-level and lack specific details about the magnitude of changes or the precise timing of these changes relative to the training process. For example, stating that directional alignment increases initially is not very informative without quantifying how much it increases and how this relates to the learning rate or the number of training epochs.

4. Contradicting to the statement made in Lines -3 and -2 on Page 6 (bottom of Page 6), the rightmost sub-figure in Figure 4 does not show any negative directional alignment. The claim that the directional alignment and dispersion stay consistently around 0 without showing any sign of learning is not clearly supported by the figure, which requires a more detailed analysis of the numerical values and their variance.

5. Figures 3 and 4 contradict to Figure 5. Putting three together, one cannot conclude that the directional alignment curve tracks the validation accuracy closely. The correlation between directional alignment and validation accuracy appears inconsistent across different experiments, and the paper does not provide a clear explanation for these discrepancies. The claim that directional alignment is correlated to stiffness also needs more rigorous justification.

### Questions
1. The explanations and discussions near the bottom of Page 5 are not new. They are well-known and can be explained from the values of cross entropy loss.

2. Something is wrong in Figure 3. For each model in Figure 3, the blue curve on the right sub-figure seems to be validation error rate, not validation accuracy. In addition, why not put the three curves (the validation accuracy curve, directional alignment curve, and directional dispersion curve) into one sub-figure? 

3. The observations from Figures 3 and 4 are not conclusive, and vague. 

4. Contradicting to the statement made in Lines -3 and -2 on Page 6 (bottom of Page 6), the rightmost sub-figure in Figure 4 does not show any negative directional alignment. 

5. Figures 3 and 4 contradict to Figure 5. Putting three together, one cannot conclude that the directional alignment curve tracks the validation accuracy closely.

### Soundness
1

### Presentation
2

### Contribution
1
