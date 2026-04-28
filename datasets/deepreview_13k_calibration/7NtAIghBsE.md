# Covariances for Free: Exploiting Mean Distributions for Federated Learning with Pre-trained Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 6, 8, 6

## Abstract
Using pre-trained models has been found to reduce the effect of data heterogeneity and speed up federated learning algorithms. Recent works have investigated the use of first-order statistics and second-order statistics to aggregate local client data distributions at the server and achieve very high performance without any training. In this work we propose a training-free method based on an unbiased estimator of class covariance matrices. Our method, which only uses first-order statistics in the form of class means communicated by clients to the server, incurs only a fraction of the communication costs required by methods based on communicating second-order statistics. We show how these estimated class covariances can be used to initialize a linear classifier, thus exploiting the covariances without actually sharing them. When compared to state-of-the-art methods which also share only class means, our approach improves performance in the range of 4-26\% with exactly the same communication cost. Moreover, our method achieves performance competitive or superior to sharing second-order statistics with dramatically less communication overhead. Finally, using our method to initialize classifiers and then performing federated fine-tuning yields better and faster convergence.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce FedCOF, a training-free federated learning approach that utilizes a pretrained model's feature extractor while updating only the classifier. Unlike previous methods that only aggregate global means, FedCOF improves performance by also deriving and leveraging unbiased global covariances from these means. Local clients send first-order statistics (class-wise feature means) to the server, which then uses these to estimate global covariances. This innovation allows for efficient communication while significantly enhancing the effectiveness of the global classifier updates.

### Strengths
**Strengths of  FedCOF:**

FedCOF presents a timely contribution that leverages pretrained models in federated learning (FL), addressing the deep learning (DL) field's growing emphasis on foundation models. FedNCM is communication-efficient but suffers from limited performance, while Fed3R improves performance using both first- and second-order statistics but at a high communication cost. In contrast, FedCOF achieves strong performance with minimal communication overhead by deriving unbiased global covariances using only first-order statistics.

### Weaknesses
## Review

### summary:
 The authors introduce FedCOF, a training-free federated learning approach that utilizes a pretrained model's feature extractor while updating only the classifier. Unlike previous methods that only aggregate global means, FedCOF improves performance by also deriving and leveraging unbiased global covariances from these means. Local clients send first-order statistics (class-wise feature means) to the server, which then uses these to estimate global covariances. This innovation allows for efficient communication while significantly enhancing the effectiveness of the global classifier updates.

### soundness:
 2

### presentation:
 2

### contribution:
 1

### strengths:
 **Strengths of  FedCOF:**

FedCOF presents a timely contribution that leverages pretrained models in federated learning (FL), addressing the deep learning (DL) field's growing emphasis on foundation models. FedNCM is communication-efficient but suffers from limited performance, while Fed3R improves performance using both first- and second-order statistics but at a high communication cost. In contrast, FedCOF achieves strong performance with minimal communication overhead by deriving unbiased global covariances using only first-order statistics.

### weaknesses:
 ***Concerns on Presentation***

**Related Works**
I recommend enhancing the Related Works section to include a broader range of studies that cover both the use of fixed classifiers and the potential limitations of pretrained models in federated learning settings.

In **Line L101**, the section discussing the application of **fixed classifiers** in federated learning could be expanded by incorporating recent and relevant studies. Specifically, it would be valuable to reference works such as FedBABU [1], SphereFed [2], and Neural Collapse-inspired approaches [3,4], which explore the impact of classifier freezing in federated scenarios.

Furthermore, the discussion in **Line L102** and beyond about **federated learning with pretrained models** should present a more balanced view. The current description highlights only the positive outcomes of using pretrained models. However, it is important to acknowledge that pretrained models are not always advantageous in federated settings. For example, findings from FedFN [5], particularly in Section 5.2, demonstrate situations where pretrained models can adversely affect the performance of the global model, especially under heterogeneous data conditions. Including this perspective would provide a more comprehensive understanding of the complexities involved in using pretrained models within federated learning frameworks.

**Preliminaries**

L117: D_k seems to refer to the local dataset rather than local data.

L127: There is no clarification on the type of loss function or how the loss is calculated (whether as a batch mean or batch sum).

L129-130: "After initializing \theta with pretrained weights, the models can be optimized in a federated manner" — In this paper, local clients do not perform local updates based on the pretrained model, and this information seems to hinder the understanding of the paper.

**Concerns on Privacy Discussion in Section 4:**

The algorithm sends the class-wise frequency of the data held by clients to the central server. I believe this information could also raise privacy concerns, yet there is no mention of this issue. In fact, there are many previous FL papers that have communicated class frequency information and provided justifications. Citing these studies would strengthen the discussion, but this type of content is entirely missing.

***Concern on Incremental Contribution***

The problem may seem incremental, as it combines existing methods' strengths, but it addresses the practical challenge of balancing communication cost and performance in FL.


### Questions
While I currently have several concerns that have led to a lower score, I am open to increasing the score if these issues are adequately addressed during the rebuttal period.

**Questions and Suggestions:**

The use of pretrained models in federated learning (FL) is a promising and timely research direction, especially given the current trend in the deep learning community toward leveraging foundation models effectively. However, as mentioned earlier in the Related Work section, using a pretrained model is not always superior to using a randomly initialized model. Specifically, findings from FedFN [1], Section 5.2, highlight scenarios where pretrained models can negatively impact global model performance in high heterogeneous settings.

Given this, it would be beneficial for the authors to include experimental comparisons between using a pretrained model and a randomly initialized model. These comparisons should cover various baselines and the proposed algorithm to provide a clearer understanding of whether the pretrained model genuinely improves performance.

Additionally, if the characteristics of the training data used for the pretrained model(e.g. ImageNet) are significantly different from the test data(e.g. SVHN) targeted by the global model, using a pretrained model could potentially be detrimental. It is important to clarify what specific test dataset the final foundation model and redefined classifier are targeting, as this information does not seem to be explicitly stated in the Preliminaries section.


Furthermore, a fundamental challenge in FL is the heterogeneity of client data, which often leads to **class imbalance** issues within each client’s local dataset. However, what differentiates FL from traditional class imbalance problems is the presence of **missing classes**, where certain classes are entirely absent from a client's dataset. This problem is especially pronounced as data heterogeneity increases, causing missing classes to occur more frequently across clients.

The proposed algorithm sends class frequency information from each client, but in the case of missing classes, this would simply convey a value of 0. I am concerned that the algorithm might be particularly vulnerable to the impact of these missing classes. Could the authors explain how their proposed algorithm is designed to mitigate this vulnerability in the context of FL, and why it might still perform well despite the challenges posed by missing classes?


[1]FedFN: Feature Normalization for Alleviating Data Heterogeneity Problem in Federated Learning. NeurIPS Workshop 2023, Federated Learning in the Age of Foundation Models.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes to use pre-trained models to perform federated classification. More specifically, Fed-COF uses pre-trained models to extract features of each example on the client, then averages the features within each class. The class-averaged features from clients are aggregated in the server to estimate the first-order and second-order statistics, which are then used in ridge regression to fit a classifier. The communication cost of Fed-COF scales only linearly with the size of the embedding.

### Strengths
The paper is well written. The derivations are clear and easy to understand. The proposed Fed-COF achieves decent empirical performance. Fed-COF also seems to work well with fine-tuning.

### Weaknesses
 - The steps of Fed-COF + Fine-tuning can be made clearer. The description around line 357 is difficult to follow.

- The choice of ridge regularization parameter $\lambda$ seems important for the classification performance. Can authors give more empirical suggestions on how $\lambda$ should change with different numbers of clients/means per client?

- What is the difference between Fed-COF oracle and Fed3R? In Table 2, it is surprising to see Fed3R sometimes achieves lower accuracy with more communication. The authors should provide more explanations for the phenomenon.

- In line 472, atleast should be at least.

### Questions
- What is the difference between Fed-COF oracle and Fed3R? In Table 2, it is surprising to see Fed3R sometimes achieves lower accuracy with more communication. The authors should provide more explanations for the phenomenon.

- In line 472, atleast should be at least.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper tackles training-free federated learning. It proposes to estimate the per-class covariances in a federated learning setting using the variance of local per-class means. This covariance can be used to obtain a ridge regression classifier, which outperforms a nearest-neighbor classifier based on class means. The proposed approach thereby avoids sending local covariance matrices which reduces communication and potential privacy risks. 

The derivation of the estimator for the per-class covariance is sound. The empirical evaluation is comprehensive.

### Strengths
- Training-free federated learning using feature extractors is a relevant and interesting problem.
- The proposed estimator of covariances is sound and novel.
- Experiments show substantial improvement over existing training-free methods and potential for its combination with federated fine-tuning or linear probing.

### Weaknesses
 - The impact of the iid assumption on realistic scenarios is evaluated empirically. It would be great to quantify how heterogeneous distributions impact the estimator theoretically, e.g., under the assumptions that local distributions are Gaussians with different mean or covariance.
- The dimension of the feature space could impact the accuracy of the estimator. This impact should be evaluated, e.g., using a synthetic dataset with varying number of feature dimensions. Specifically, the impact of high dimensionality on the rank of the estimated covariance matrix should be investigated, as the number of clients per class might limit the rank of the estimated covariance, potentially hindering performance in high-dimensional feature spaces.
- The paper focusses on label shifts, i.e., a heterogeneous distribution of classes. It is unclear how the method performs in case of feature shift, i.e., a heterogeneous distribution of features, e.g., via locally different covariance structures [1]. Furthermore, the performance under more complex forms of distribution shift, beyond simple label or feature shifts, should be evaluated.



### Questions
- Why is this approach better in terms of accuracy that Fed3R? Shouldn't it perform slightly worse or en-par, since it only approximates the covariance matrix? Here it would be good to investigate the approximation of the covariance matrix and compare it to the one produced by Fed3R.
- It would be great to compare the results using a strong pre-trained feature extractor with a classical end-to-end federated learning baseline, e.g., training a ResNet-50 on CIFAR100. 
- For consistency I suggest to use $\widehat{\Sigma}$ instead of $\widehat{S}$ in Eq. 10.
- Please compare your approach also to distributed training of linear models (using standard FedAvg), since ideally the training-free approach should perform at least en-par in terms of model performance and should outperform them in terms of communication. Here, it would be particularly interesting to compare to communication-efficient approaches [2]. 
- Since ridge regression might not always be ideal approach given a fixed feature extractor, I wonder whether a kernel ridge regression could be applicable. This would require sending the kernel matrix, but also has a closed form solution. The communication cost in that case would be quadratic in the number of data points, rather then linear in the features, so for many scenarios communication might be higher. Once could employ compression techniques here, though, like the Nyström method.


[1] Li, Xiaoxiao, et al. "FedBN: Federated Learning on Non-IID Features via Local Batch Normalization." International Conference on Learning Representations, 2021.
[2] Kamp, Michael, et al. "Communication-efficient distributed online prediction by dynamic model synchronization." Machine Learning and Knowledge Discovery in Databases, 2014.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel training-free FL method called FedCOF, which approximates the covariance on the server side to eliminate the enormous communication overhead. Numerical results demonstrate that FedCOF achieves comparable performance to Fed3R by merely transmitting class means to the server.

### Strengths
1. Building on theoretical guarantees, this paper introduces a novel algorithm that eliminates the need for transmitting covariances between the server and clients while maintaining performance levels. This represents a valuable step for training-free federated learning.

2. The authors have carried out extensive experiments to validate the effectiveness of the proposed method, demonstrating considerable effort in their research.

### Weaknesses
While the motivation of this paper is clear, I have the following questions/discussions.

1. The algorithm necessitates the transmission of $n_{k,c}$ to the server, which introduces certain privacy concerns. Although other methods also require this information, it would be beneficial if the authors could discuss potential techniques to address or mitigate this issue. Specifically, the transmission of class-wise counts, $n_{k,c}$, reveals the distribution of data across different classes within each client's local dataset. This information could potentially be exploited to infer sensitive attributes about the client's data, especially in scenarios where the number of classes is small or the class distribution is highly skewed. The authors should consider exploring differential privacy techniques or other methods to obfuscate these counts before transmission.

2. As modern pre-trained models tend to be generative models (e.g., GPT), it would be interesting to explore the possibility of extending the proposed methods to handle generative models by initializing the decoding heads accordingly. The current method focuses on classification tasks, and it's not immediately clear how it would be applied to generative models where the output space is significantly different. Specifically, generative models often involve complex decoding processes, and the proposed method's reliance on class means might not be directly applicable. The authors should discuss the challenges and potential adaptations required to extend their approach to generative models.

### Questions
Please see weakness.

### Soundness
3

### Presentation
3

### Contribution
2
