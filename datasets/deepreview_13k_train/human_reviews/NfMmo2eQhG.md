# The Relevancy Metric: Understanding the Impact of Training Data

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
Deep learning models are central to many critical decision-making processes, making it imperative to gain deeper insights into their behavior to improve performance, transparency, interpretability, and fairness. 
A key challenge is understanding how training data shapes model predictions on unseen test data. 
In this paper, we introduce a novel metric, $\textbf{\textit{Relevancy}}$, which quantifies the impact of individual training samples on inference predictions. 
Our proposed metric is calculated by observing the learning dynamics of the model during training, and it is computationally efficient and applicable across a wide range of tasks. 
We demonstrate that it is between $80\times$ and $100,000\times$ more efficient than existing metrics for capturing the train-test relationship. 
Using $\textit{relevancy}$, we enable the identification of coresets — compact datasets that represent the essence of the training distribution. 
Quantitative evaluations show that coresets selected using our metric outperform state-of-the-art methods by up to $5.2$% on CIFAR-100. 
Additionally, we qualitatively demonstrate how $\textit{relevancy}$ can be extended to assess various training data properties, such as identifying mislabeled samples in widely used datasets like ImageNet, CIFAR-100, and Fashion-MNIST.
These examples illustrate just a few of the many potential uses of $\textit{relevancy}$, highlighting its versatility in promoting more interpretable, efficient, and fair deep learning systems across diverse tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces "Relevancy," a novel metric to evaluate the influence of individual training samples on model predictions. Relevancy measures the correlation between the loss trajectories of training and test samples, aiming to understand how specific training samples impact generalization to unseen data.

### Strengths
1. The paper is well written and organized. 
2. The proposed metric is both simple and innovative, providing an effective way to measure the influence of training samples on the model’s generalization capabilities. This simplicity does not compromise its effectiveness, making it broadly applicable across tasks that require interpretability and efficient data utilization.
3. The paper demonstrates the versatility of the proposed metric through its applications in coreset generation, memorization analysis, and mislabeled sample detection. The experimental results are thorough, covering multiple datasets and convincingly supporting the metric's utility.

Overall, this paper makes a meaningful contribution to deep learning research by proposing a practical and impactful metric.

### Weaknesses
1. The metric relies on loss trajectory data from training checkpoints, which could limit its use in models or systems where saving and processing frequent checkpoints is impractical or unavailable. Could you address potential methods to mitigate this limitation, such as using fewer checkpoints or approximations? How does the length of the trajectory T impact the metric?

2. Generalization Across Tasks: While the paper demonstrates the effectiveness of Relevancy, its performance on tasks beyond classification (e.g., regression or sequential tasks) is not explored. Testing the metric's adaptability to a wider range of applications would enhance its impact.

### Questions
see weakness.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel metric called Relevancy to quantify the impact of individual training samples on model predictions. The metric aims to efficiently capture the relationship between different samples by analyzing the loss trajectories over epochs, allowing insights into data memorization, generalization, and the identification of mislabeled samples. The authors demonstrate that the proposed metric is computationally efficient—up to 100,000× faster than traditional metrics like influence functions and input curvature—and effective in generating coresets that improve classification accuracy on CIFAR-100.  This paper also demonstrates mislabeled samples detection use case for relevancy.

### Strengths
1.	This paper is well-organized and easy to read. The authors first introduce the proposed metric and then provide a comprehensive comparison with other alternative metrics in terms of score results and computation cost. Subsequently, several use cases, such as coreset generation and mislabeled sample identification, and consistency investigation are provided to show the versatility of this metric.
2.	The proposed metric relevancy is simple, efficient, and computation-friendly. The Relevance metric is a simple approach that captures the impact of individual training samples through correlation in loss trajectories. The computational efficiency is well-documented, showing up to 100,000× improvement over other metrics.
3.	Relevancy’s applications in coreset selection and mislabeled sample identification highlight its broad relevance and potential for practical use in dataset management, model interpretability, and error reduction.

### Weaknesses
1.	Can the authors provide more details about the impact of individual training samples on inference prediction? What kind of impact does this paper aim to quantify? Any formal definition on this impact? From my understanding, the impact this paper aims to quantify is different from that using the influence function. The train-test relationship depends on the sample pair, the well-trained model, and the target loss while relevancy depends on the learning dynamics.
2.	Although the relevancy definition is simple, I have concerns about the definitions using correlation. (1) why is the learning dynamic involved in impact quantification? Suppose there are two identical well-trained models but with different training trajectories, why are the train-test relationship scores different from these two models? (2) For large training epochs T, if we continue to train the model with one epoch in a different task, the relevancy score should not change significantly since the correlation coefficient is dominated by the loss curve in the first large T epochs. However, the model at T+1 epoch could be significantly different from the model at T epoch and thus with different impact for train-test sample pairs. (3) Since the relevancy metric only considers loss values, it may not be dominated by some huge loss value. The robustness may be a potential issue. (4) The biggest concern is about the order preservation among loss transformation. Suppose two train-test pairs with the same relevancy (e.g., loss value A1=[2.0, 1.0, 0.5], B1=[4.0, 2.0, 1.0], and A2 = [3, 2, 1] B2=[6, 4, 2]), if we use different loss mapping (e.g., CE and perplexity), the relevancy order could be changed. Overall, it would be better to start from some principles to design such metrics and then justify the proposed metric by satisfying these principles.
3.	The limitation discussion of this paper is missing. The relevancy score computation requires the storage of all model checkpoints for all epochs, which narrows the applicability of this metric.  
4.	Experiments can be more convincing. (a) There are no experiments to evaluate the relevancy score quality. It would be better to design some synthetic experiments. For example, the impact of a training example on a pure noise image should be very small. What’s the relevancy score and other metrics score in this case? (b) Why can the proposed metric achieve the best performance than other coreset generation methods? Any possible reason/rationale for this? (c) For noisy sample detection, I am curious whether this method can still perform well in high noise ratio regime. Considering the extreme case with almost 100% noise ratio for some class, the average relevancy score may be dominated by noisy samples and cannot reflect the real impact of the sample. (d) It would be better to compare the consistency over different model backbones for different metrics. Does relevancy show higher consistency than influence function?

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes relevancy, which quantifies each training data's attribution for model's inference.
Relevancy tracks how correlated the train data loss is to that of the target data during training, and evaluate the data as relevant if positively correlated, and vice versa.
Such suggested metrics are computationally efficient, and adopted to various applications such as dataset compression and detecting mislabeled data.

### Strengths
This paper is well-written and addresses the critical research question of attributing training data to model performance, especially as the significance of data continues to grow in the era of large-scale models.

### Weaknesses
 **1. Missing important baselines**: This paper lacks important previous studies that tackle the same goal, i.e., training data attributions (TDA) [1,2]. These work evaluates TDA via training data's counterfactual on model's output on target data. Also, this paper lacks the evaluation on existing metric of TDA, called linear datamodeling score (LDS), as proposed in Park et al.[2]

**2. Wrong definition**: The proposed relevancy, which measures correlation between train and target data's losses, does NOT mean the influences of train data onto the target data. In other words, train data is simply correlated, but not causal, to target data's reduced loss. For instance, there is the true causal train data (i.e., *tr1*) that helps minimize both (another) train data (i.e., *tr2*) and target data (i.e., *te*), while training on *tr2* does not induces lower loss on *te*. Still, the proposed relevancy will identify *tr1* as strongly influencing train data for *te*, which is not true. Therefore, I'm not convinced that the proposed Relevancy is capable of measuring true influence of training data to the target data.

**3. Incomplete analysis**: While authors claim that Fig.4-(b) reveals "meaningful relationships" across all test samples, it is unclear what meaningful relationships regarding true influences between data are represented in the figure. 

**4. Potential computational complexity**: Since Relevancy relies on loss, it might be highly stochastic across different training setup, e.g., data orders, architectures, learning rates. How invariant or reliable the Relevancy is given such stochasticity? Is just a single run sufficient to obtain reliable evaluation, or it requires multiple iterative runs for reliable results that would result in additional computational complexity, unlike stated in Table 1.?

### Questions
See weaknesses.

### Soundness
1

### Presentation
4

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce a novel metric termed 'relevancy,' which aims to measure the influence of individual training samples on predictions. 
Essentially, relevancy is derived by the similarity between a training instance and a testing point on the training loss during the training process. 
The metric is computationally efficient, provided access to the model's checkpoints at each training epoch is available. 
The authors leverage this relevancy metric to construct a coreset and demonstrate its utility in identifying mislabeled samples within datasets. 

While the proposed approach is intriguing, there are aspects that could benefit from further elucidation. 
My major concern pertain to the metric's underlying insights, particularly in scenarios where relevancy might fail to show actual influence. 
Additionally, the paper's experimental section does not sufficiently address these concerns, preventing me from endorsing its acceptance at this stage.

### Strengths
Contributions:
1. The authors introduce a relevancy metric grounded in the similarity between training samples and testing points, offering a means to assess the contribution of individual samples to test predictions.
2. The metric is computationally efficient, assuming access to model checkpoints throughout the training process.
3. Utilizing the relevancy metric, the authors construct a coreset and achieve state-of-the-art results on CIFAR-100.
4. They also demonstrate the metric's potential in detecting mislabeled samples within datasets.
5. The paper is well-structured and clearly written.
6. The comparison with other metrics is useful.

### Weaknesses
Flaws:

1. [Major Concern] The metric's reliability is questionable, as it relies solely on loss information. 
In extreme cases, such as when using 0-1 loss, the metric could be highly unstable. 
There may be instances where high relevancy does not equate to significant contribution to the testing point, and vice versa, yet the paper lacks discussion on these scenarios. 
The authors should provide insights into the conditions under which the metric is effective and when it is not. Without this, it is challenging to advocate for its use on new datasets. For instance, if the loss landscape is highly non-convex, the correlation of loss changes might not accurately reflect the true influence of a training sample. The metric could be misled by spurious correlations in the loss trajectory, especially if the model is near a saddle point or a local minimum. A more rigorous analysis is needed to understand how the metric behaves under different loss landscapes and optimization dynamics.

2. Building on the first point, if the authors do not clarify the metric's applicability, the current experiments are insufficient. Additional experiments showcasing the metric's utility across various models and datasets are needed to establish its broad usefulness. The current experiments do not sufficiently explore the limitations of the metric, especially in scenarios where the loss function is not smooth or the data distribution is highly complex. It is crucial to demonstrate the metric's robustness across diverse settings, including different optimization algorithms and network architectures.

3. Would the selected coreset overfit to test points? Did the authors validate the coreset against a separate test set or use validation samples to derive the coreset?

4. What is the implication of negative relevancy? Does it suggest that training samples negatively impact the testing point?


Small concerns: 
1. Figure 2 is unclear and difficult to read.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2
