# Proxy-FDA: Proxy-based Feature Distribution Alignment for Fine-tuning Vision Foundation Models without Forgetting

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Vision foundation models pre-trained on massive data encode rich representations of real-world concepts, which can be adapted to downstream tasks by fine-tuning. However, fine-tuning foundation models on one task often leads to the issue of concept forgetting on other tasks, and this issue is exacerbated by the typically limited data for fine-tuning. Recent methods of robust fine-tuning aim to mitigate forgetting of prior knowledge without affecting the fine-tuning performance. Knowledge is often preserved by matching the original and fine-tuned model weights or feature pairs. However, such point-wise matching can be too strong, without explicit awareness of the feature neighborhood structures that encode rich knowledge as well. We propose a novel regularization method Proxy-FDA that explicitly preserves the structural knowledge in feature space. Proxy-FDA performs Feature Distribution Alignment (using nearest neighbor graphs) between the pre-trained and fine-tuned feature spaces, and the alignment is further improved by informative proxies that are generated dynamically to increase data diversity. We show in end-to-end fine-tuning experiments that Proxy-FDA significantly reduces concept forgetting, and we find a strong correlation between forgetting and a distributional distance metric (in comparison to L2 distance). We further demonstrate Proxy-FDA's utility in both few-shot (based on prompt tuning) and continual fine-tuning settings, where we achieve consistent gains over the corresponding baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a regularization method to mitigate the forgetting problem during fine-tuning foundation models by aligning the nearest neighbor graphs between the pre-trained and fine-tuned feature spaces. The authors experimentally demonstrate that this method outperforms baseline models on both few-shot image classification and continual learning tasks.

### Strengths
1.This work is clearly presented and easy to understand.

2.Experimental results show that this method outperforms some baseline methods.

### Weaknesses
1.why does aligning feature distributions help alleviate forgetting? The essence of feature subspace alignment is to make the feature distributions learned by the pre-trained and fine-tuned models more consistent. In the extreme case, this alignment could lead to a collapse back to the original state. It's unclear how the proposed method avoids this collapse, especially when the fine-tuning task requires a significant shift in the feature space. The paper lacks a detailed analysis of the trade-off between preserving pre-trained knowledge and adapting to new tasks, which is crucial for understanding the method's limitations.

2.While the authors argue for the advantages of Proxy-FDA, it would be beneficial to include a theoretical foundation or empirical evidence that explains why this approach is expected to outperform traditional methods. Specifically, the paper needs to clarify why aligning nearest neighbor graphs is superior to other forms of feature alignment. The current justification relies heavily on intuition, and a more rigorous analysis of the underlying mechanisms is needed. For example, how does the choice of the proxy network affect the performance, and what are the conditions under which this method is most effective?

3.One potential concern is that the comparative methods presented by the authors do not include recent works from 2024 onward, which could result in an incomplete or potentially inaccurate assessment of the method's performance. This is especially important given the rapid advancements in the field of continual learning and few-shot learning. The lack of comparison with state-of-the-art methods makes it difficult to gauge the true contribution of the proposed method.

4.The author’s motivation is difficult to discern from Figure 1, which could benefit from clearer visual cues or annotations to enhance interpretability. Figure 2 could be improved to more effectively present the technology in a clear and understandable manner. The current figures are too abstract and do not provide sufficient insight into the practical implications of the proposed method. For instance, Figure 1 does not clearly demonstrate the problem of forgetting, and Figure 2 does not effectively illustrate the mechanism of Proxy-FDA.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

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
This paper introduces Proxy-FDA, a feature-based regularization method for fine-tuning vision foundation models (e.g., CLIP, DINOv2) on downstream tasks. Unlike point-wise regularization, FDA preserves the structure-wise knowledge by aligning the feature space of the pre-trained and fine-tuned models, incorporating local neighborhood structures. Proxy-FDA further generates synthetic features (proxies) to increase data diversity. The method is evaluated across end-to-end fine-tuning, few-shot tuning, and continual learning scenarios.

### Strengths
-  The method is well-motivated. 
- The evaluation seems comprehensive and the results appear impressive.

### Weaknesses
 - Some recent related works lack discussion in the related work section but are directly compared in the experimental section, such as CLIPood and PromptSRC, which are both regularization-based fine-tuning approaches. Including a discussion of these methods in the related work section would provide better context for readers.
- Several technical details require further clarification. (1) Details about the network architecture and training parameters for the proxy generator are absent. Specifically, the number of layers, activation functions, and optimization details are not provided. (2) The hard class mining strategy specifies $n=4$ (Line 777), but it is unclear how this approach is used in few-shot cases (e.g., 1- or 2-shot). It is not clear if data augmentation is used to reach n=4, and if so, how this impacts the comparison with other methods that do not use data augmentation. (3) The scalar $s=0.4$ is not introduced or explained in Section 3.2 but it is discussed and analyzed in hyper-parameter analysis (e.g., Figure 5)
- Important implementation details are not provided. (1) Detailed specifications for hype-parameters (e.g., temperature $\tau$, bias $b$, loss coefficient $\lambda$) are missing. It is unclear how these parameters are initialized and tuned. (2) The specific $K$ value for each dataset is also absent. Providing these details would benefit the community. (3) Implementation details are missing for the continual fine-tuning setting (e.g., Table 8), making it difficult to confirm evaluation fairness across methods. For example, the specific dataset splits and training procedures are not described.
- Evaluation should be improved. (1) How does FDA/Proxy-FDA perform when compared to previous SoTA FD-Align in its official evaluation setting (e.g., compare APE-T+FD-Align and APE-T+Proxy-FDA by training the model on ImageNet and testing on ImageNet V2/Sketch) ? (2) CLAP [1], another regularization-based linear probing method, seems more efficient as it does not require a validation set for extensive hyper-parameter selection. Including a comparison with CLAP would clarify the strengths and limitations of the proposed method. It is not clear if the performance gain is worth the extra complexity and hyperparameter tuning required by the proposed method.
- Ablation study on batch size. Since the FDA relies on batch-based feature alignment, it is essential to analyze the impact of varying batch sizes. Specifically, it is unclear how the performance varies with different batch sizes, and what the optimal batch size is for different datasets.

### Questions
- Please find the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a new approach to mitigate concept forgetting in model fine-tuning (robust fine-tuning) by building on existing feature-matching methods. Specifically, the authors aim to align the feature structure by regularizing the feature space using k-nearest neighbors (KNN) within each batch. They also propose generating proxies from the data to preserve diversity across datasets.

### Strengths
- Robust fine-tuning is a highly active and valuable area of research with significant relevance and potential.
- The motivation for the proposed method is strong, as preserving data structure during feature matching is both reasonable and innovative.
- The writing is clear, and the approach is presented in a way that is easy to follow.

### Weaknesses
 - Motivation and Selection of Distribution Alignment Method: The motivation for using distribution alignment through feature matching, specifically with regularization on nearest-neighbor features, is not fully explained. This approach resembles knowledge distillation; therefore, clarification on how this method differs from distillation between the original and fine-tuned models would strengthen the argument. Specifically, the paper needs to clarify why preserving the feature structure through k-NN is superior to directly matching feature distributions, and how this approach avoids the pitfalls of standard knowledge distillation, such as relying on the teacher model's potentially flawed representations. The paper should also discuss the potential limitations of using a fixed pre-trained model's feature space as the target for alignment, as this might restrict the fine-tuned model's ability to learn novel features relevant to the downstream task.

- Design of Equation 2: Equation 2 appears to follow a sigmoid loss structure but replaces traditional labels (+1, -1) with a weight, $w_{ij}$​. Is this weight defined as $w_{ij}=\cos⁡(x_i,x_j)$? An additional explanation of the rationale and comparative benefits of this design choice would be helpful. Furthermore, the paper needs to elaborate on why cosine similarity is the chosen metric for weighting, as opposed to other similarity measures such as Euclidean distance or learned similarity metrics. The impact of this choice on the overall performance and robustness of the method should be discussed, along with potential scenarios where this choice might be suboptimal.

- Clustering with KNN: The method clusters features in each batch using KNN, which may not adequately group samples with the same or similar labels, especially during fine-tuning. The clustering might benefit from label-based constraints, either including or excluding samples based on label proximity, to enhance feature alignment. The paper should address the potential for the KNN clustering to be unstable or inconsistent across batches, especially when batch sizes are small or when the feature space is highly non-uniform. This could lead to noisy gradients and hinder the convergence of the fine-tuning process. A discussion of the sensitivity of the method to the choice of K and strategies for mitigating these issues is needed.

- Proxy Generator Motivation: The purpose and function of the proxy generator remain unclear. Specifically, the reason for incorporating an attention layer is not well-justified, as it is unclear how it assists in integrating information across positive and negative feature sets. An ablation study or additional analysis of the generator architecture would clarify its contribution and effectiveness. The paper should provide a more detailed explanation of how the attention mechanism facilitates the generation of diverse proxies and why this is crucial for preventing concept forgetting. The specific benefits of using attention over simpler methods, such as averaging or concatenating features, should be discussed, along with the computational overhead associated with this design choice.

- (minor) Some descriptions need clarification: 
 Line 167: What is meant by "low task loss $L_{task}$​"?
 Line 168: Please clarify "whilst preventing concept forgetting on any target dataset $D\neq D_{ft}$".

### Questions
See the weakness above.
Generally, this is a solid paper. However, some remaining concerns should be further discussed. I may adjust the score according to the response from the authors.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Proxy-FDA, a structural regularization method designed to mitigate concept forgetting in fine-tuning large pre-trained vision models. Proxy-FDA achieves this by preserving local feature neighborhood structures in the pre-trained feature space through
Feature Distribution Alignment (FDA), leveraging nearest neighbor graphs. Additionally, Proxy-FDA employs dynamic proxy generation to increase data diversity, which enhances feature alignment. The method is evaluated in few-shot and continual fine-tuning contexts,
demonstrating strong performance.

### Strengths
1. Preserving the neighbor structure within the pre-trained feature space beyond class semantics is novel and may bring some insight to the model adaptation community.
2. State-of-the-art performance validates the effectiveness of the proposed approach in reducing concept forgetting.
3. This paper is well-written and organized.

### Weaknesses
1. As the output pooling weights are softmax-normalized and convex combinations are expected, figure 2(c) may be problematic. Neither the synthesized proxy P+ nor P- lies within the convex hull of corresponding neighbors.
2. In L261, why do both the positive set and the negative set lack diversity? How does hard-class mining lead to the semi-hard nature of X^-? And how does this nature alleviate “limited diversity”? More explanations for the above questions should be provided.

### Questions
1. How is the number of proxy positives n^{p+} and negatives n^{p-} determined? Is it dynamic across different batches?
2. How can the generated proxies within the convex hull help shape the decision boundary?

### Soundness
3

### Presentation
3

### Contribution
3
