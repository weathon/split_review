# Contrastive Unlearning: A Contrastive Approach to Machine Unlearning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Machine unlearning aims to eliminate the influence of a subset of training samples (i.e., unlearning samples) from a trained model. Effectively and efficiently removing the unlearning samples without negatively impacting the overall model performance is still challenging. In this paper, we propose a contrastive unlearning framework, leveraging the concept of representation learning for more effective unlearning. It removes the influence of unlearning samples by contrasting their embeddings against the remaining samples so that they are pushed away from their original classes and pulled toward other classes. By directly optimizing the representation space, it effectively removes the influence of unlearning samples while maintaining the representations learned from the remaining samples.
    Experiments on a variety of datasets and models on both class unlearning and sample unlearning showed that contrastive unlearning achieves the best unlearning effects and efficiency with the lowest performance loss compared with the state-of-the-art algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors propose a new machine unlearning method, inspired by contrastive learning. 

The proposed contrastive unlearning pushes away the positive pairs (from the same class) and pulls the negative pairs close to each other. 

The idea is validated on several backbones and datasets.

### Strengths
- It seems that the contrastive paradigm is new for the field of unlearning. 
- The experimental results, from both efficiency and efficacy, seem to show the advantages of the proposed contrastive unlearning (while I'm quite confused about *unlearning acc*, which will be elaborated in Weaknesses and Questions).

### Weaknesses
I'm not familiar with machine unlearning. I read some papers from recent ML conferences, such as ICML, NeurIPS, and CVPR, and try my best to provide a fair review. Some comments may be naive and I'd like to update my score after reading the response from the authors and reviews from other reviewers. Here are my concerns:

- I'm quite confused about the setting of single class unlearning. If we expect a model to forget a class, why don't we just add some rules? For a simple classification task, the rule could be very simple: assign random labels if the model outputs the class to unlearn. The rule may be useless for more powerful models, such as zero-shot classifiers (e.g., CLIP) and LLMs. However, the authors fail to conduct experiments on these models. The paper does not adequately justify why a more straightforward rule-based approach is insufficient, particularly in scenarios where only the model's output is accessible. The lack of comparison to such a baseline makes it difficult to assess the true benefit of the proposed method.

- Some visualization may be helpful for the "contrastive" unlearning. It is quite common to show some t-SNE visualization in contrastive learning. With the visualization, we can know whether the unlearning samples are pushed to the decision boundary. The absence of such visualizations makes it hard to verify the core claim of the method, which is that the unlearned samples are being pushed away from their original class representations. Without visual evidence, it's difficult to assess if the contrastive loss is truly achieving the desired effect or if it's simply modifying the embeddings in a way that does not correspond to effective unlearning.

- In Eq. (5) and Eq. (6), $z_i$ is not normalized, which is a standard step in contrastive learning. In CL, $z_i$ is usually processed by $z_i = \frac{z_i}{\|\|z_i\|\|}$. Is it a special setting to ensure the performance? The lack of normalization is a significant deviation from standard contrastive learning practices. The authors should provide a clear justification for this choice and analyze its impact on the unlearning process. It is unclear if this is a deliberate design choice or an oversight, and its effect on the overall performance needs to be clarified.

- The theoretical analysis is lacking. Although it is not necessary, some theoretical analysis may help to improve the quality of this paper.

- There are some typos, such as  $ \mathcal D_{ts} \cup \mathcal{D}_{tr} = \emptyset $ in Line-198.

### Questions
- Why do the authors test the single class unlearning only on simple classification models? 
- How will the embeddings of unlearning samples change? Are they really pushed to the decision boundary? 
- If we normalize the representation $z_i$ in Eq. (5) and (6), how will the performance change?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces a novel framework for machine unlearning, which is the process of removing the influence of specific training samples from a trained model. The authors propose a method called contrastive unlearning that leverages representation learning to effectively eliminate the impact of unlearning samples while maintaining the model's performance on the remaining data. The approach contrasts the embeddings of unlearning samples with those of the remaining samples, adjusting the model's representation space to make the unlearning samples' embeddings similar to those of unseen test samples. The paper concludes that contrastive unlearning is a promising technique for machine unlearning, with potential applications in complying with privacy regulations. Through extensive experiments on various datasets and models, the paper demonstrates that contrastive unlearning outperforms existing methods in terms of unlearning efficacy, model performance preservation, and computational efficiency.

### Strengths
1. The paper introduces contrastive learning to the machine unlearning, effectively removing the influence of unlearning samples without significant loss in model performance. Contrastive unlearning is computationally efficient, requiring fewer iterations to achieve the desired unlearning effect compared to other methods.

2. The experiments are comprehensive, including accuracy gap and membership inference attack for unlearning performance. They convinced me of the SOTA performance of the proposed contrastive paradigm.

### Weaknesses
1. Weak scalability compared to non-contrastive methods. The proposed contrastive learning method constructs the positive pair and negative pair in a batch, hence, it might need a large batch size in the practical application which has a large class number. So I suggest using a MoCo-like, more advanced contrasive learning method to further enhance the scalability of the proposed method. 

2. The assumption for test samples is a little bit strong, e.g., " If the embeddings of the unlearning samples become indistinguishable from the embeddings of the test samples, we can claim that the model is no longer influenced by the unlearning samples". We usually assume the training and test examples follow I.I.D. However, it seems that this paper did not have this assumption.

### Questions
1, Could you provide some discussion for the limits regarding the number of unlearning samples. More unlarning samples in the contrastive framework might damage the representation of ramaining samples.
2. Following the weakness 2, do the existing methods have the same assumption as line 62-65?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The author introduces a novel form of contrastive loss tailored to the machine unlearning paradigm. The main insight is to selectively remove the most relevant features of the unlearning samples while preserving the quality of embeddings for the remaining samples. Experimental results demonstrate that the proposed contrastive loss achieves superior performance on single-class and sample-unlearning tasks, surpassing state-of-the-art methods.

### Strengths
1. The proposed supervised contrastive learning framework is well-structured and easy to understand. By constructing positive and negative pairs, the encoder effectively deactivates the embedding of unlearning samples.
2. The framework performs well across three benchmarks, showing improved unlearning efficiency and effectiveness over existing methods.

### Weaknesses
1. The approach of using supervised contrastive learning for unlearning is somewhat simplistic, as it overlooks the potential generalization decay of the model, as noted in Question 1. Merely introducing a framework that achieves improved performance is not sufficiently insightful. ICLR standards are high, and this work could benefit from a deeper exploration of these issues for the community.
2. The presentation quality could be enhanced, especially regarding punctuation usage. For example, there is a missing comma after Eq. (5) and an extra period before Eq. (6). The writing also lacks precision in certain areas, making it difficult to fully grasp the nuances of the proposed method. For instance, the description of how the contrastive loss specifically targets the unlearning samples could be more detailed, explaining the exact mechanism by which the embeddings are deactivated and how this differs from simply reducing the magnitude of the embeddings.


### Questions
1. Is the metric in Eq. (1) for machine unlearning reasonable? In the case of a well-performing pre-trained model, strong generalization should allow it to handle unseen samples effectively without degradation.
2. In Tables 2 and 5, the efficacy metric is the retraining time. However, retraining time can vary due to multiple factors, such as I/O rates and the number of GPU cores, which may affect the reliability of this metric.
3. Given that cross-entropy loss is included in the retraining, why is the processing time less than other baselines?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
In this paper, the authors design a contrastive unlearning method. This method could remove the influence of unlearning samples by constrastive their embeddings against the remaining samples' embeddings.

### Strengths
1. The paper is well-organized.

2. The motivation is clearly described.

3. The appendix is comprehensive.

### Weaknesses
1. Table 1 is confusing. The results for “remain test” on RN18 seem to suggest that higher is better, so why is 85.79 bolded?

2. A similar issue appears in Table 3.

3. The datasets used are only CIFAR-10 and SVHN. It is recommended to include additional datasets.

4. The authors should release the code to ensure reproducibility.

### Questions
Please see weakness.

### Soundness
3

### Presentation
2

### Contribution
3
