# RePaFormer: Ferocious and Scalable Acceleration of MetaFormers via Structural Reparamterization

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
We reveal that feed-forward network (FFN) layers significantly contribute to the latencies of Vision Transformers (ViTs). This effect scales up quickly as the model size escalates, and hence presents a major opportunity in efficiency optimization for ViTs via structural reparameterization on FFN layers. However, directly reparameterizing the linear projection weights is difficult due to the non-linear activation in between. In this work, we propose an innovative channel idle mechanism that establishes a linear pathway through the activation function, facilitating structural reparameterization on FFN layers during inference. Consequently, we present a family of efficient ViTs embedded with the introduced mechanism called **RePa**rameterizable Vision Trans**Formers** (RePaFormers). This technique brings remarkable latency reductions with small sacrifices (sometimes gains) in accuracy across various MetaFormer-structured architectures investigated in the experiments. The benefits of this method scale consistently with model sizes, demonstrating increasing efficiency improvements and narrowing performance gaps as model sizes grow. Specifically, the RePaFormer variants for DeiT-Base and Swin-Base achieve 67.5% and 49.7% throughput accelerations with minor changes in top-1 accuracy (-0.4% and -0.9%), respectively. Further improvements in speed and accuracy are expected on even larger ViT models. In particular, the RePaFormer variants for ViT-Large and ViT-Huge enjoy 66.8% and 68.7% inference speed-ups with +1.7% and +1.1% higher top-1 accuracies, respectively. RePaFormer is the first to employ structural reparameterization on FFN layers to expedite ViTs to our best knowledge, and we believe that it represents an auspicious direction for efficient ViTs. Codes are provided in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a reparameterization technique for vision transformers (ViTs) to improve their test-time efficiency. It achieves this by leaving some channels idle, which are not passed through activation functions and can thus be merged at inference time. Experiments show that the proposed method can notably reduce the latency of ViT-based classification models at the cost of some accuracy loss.

### Strengths
1. This paper is clearly written and easy to follow.

2. The proposed method is motivated by a comprehensive latency analysis.

3. Experiments demonstrate that the proposed method significantly improves the throughput of ViT-based classification models.

### Weaknesses
1. The main concern with this paper is the significant accuracy drop induced by the reparameterization. As shown in Table 2, the throughput improvement comes at the cost of a substantial accuracy loss, such as -7.9% on DeiT-Tiny and -6.7% on PoolFormer-s12. It appears that the proposed method scales poorly to smaller models, and simpler compression techniques like pruning might be a better option for model acceleration.

2. Another major concern is the lack of analysis and comparison with other reparameterization strategies. Specifically, it is unclear why the proposed method is preferable to RepVGG-style multi-branch reparameterization, as leaving some channels idle without passing through activation functions can be considered a special case of a dual-branch structure. The authors should analyze the underlying reasons and key differences that make the proposed method distinct.

3. The experimental benchmarks are insufficient. A comparison with (1) vanilla reparameterization techniques (e.g., RepVGG-style multi-branch structure) and (2) other compression methods that offer different accuracy-efficiency trade-offs should be included.

4. The latency improvement on dense prediction tasks is small, potentially because FFNs occupy a smaller portion of the runtime for high-resolution inputs.

5. Minor: Tables 1 and 2 have considerable overlap. Retaining only Table 2 should be sufficient.

### Questions
My questions and concerns are listed in the weakness section. My main question is why the proposed method is a better choice than RepVGG-style multi-branch reparameterization.

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
4

### Summary
This paper studies the feed-forward network (FFN) layers in MetaFormer architecture and finds it play a significant role in introducing latencies. Based on this observation, the authors propose ReParameterizable Vision Transformers (RePaFormers) with the structural reparameterization technique and reduces the latency remarkably with minor sacrifice in accuracy. Extensive experiments on various tasks and datasets demonstrate the effectiveness of the proposed method.

### Strengths
1. The idea of applying structural reparameterization in FFN layers in great and it brings actually speedup in GPU latency.
2. The experimental results are extensive as the method is validated not only on classification tasks, but on downstream tasks and self-supervised learning setting as well, which highlight the generalization ability of the proposed method.
3. Overall, the paper is clear written and well-organized.

### Weaknesses
 1. Advantage over other model compression techniques. The goal of the proposed method is to increase the efficiency of current architectures, while it can be also realized by other model compression techniques, including pruning, distillation or quantization. The reviewer understands that comparing with those methods is out of the scope of this work, but it would be great if the authors could provide some justification of the advantage of the proposed method. For example, whether the proposed method is more generalizable across model architectures, easier to implement, or has less impact on accuracy compared to other techniques. It is unclear how this method compares to existing compression techniques in terms of computational overhead during training and inference, and whether it introduces any specific hardware requirements or constraints.
2. Performance gap with self-supervised baselines. It is noticeable that the performance gap with self-supervised baselines is larger than the gap in supervised learning, which may hinder its application on foundation models. Meanwhile, it is also unknown that if the proposed method will brings negative impact on the generalization ability of self-supervised learning methods, and experiments on downstream tasks like fine-grained classification may validate this point. The paper does not explore the impact of the reparameterization on the learned representations in the self-supervised setting, which is a crucial aspect for foundation models.
3. Performance gap at downstream tasks. It is also noteworthy that the performance gap at dense prediction tasks is non-negligible compared to the gap in classification tasks. It would better if the authors could provide some explanations or analysis. The paper lacks a detailed analysis of why the performance gap is more pronounced in dense prediction tasks, and whether the reparameterization process affects the spatial sensitivity of the model.

### Questions
Apart from the questions in weakness, the reviewer has two additional questions:

1. Training costs. What would be the training time of the proposed method compared to the vanilla version?
2. The authors have mentioned in the abstract that 'improvements in speed and accuracy are expected on even larger models', which may not be convincing enough, as the improvements in accuracy should be supported by empirical results.

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
5

### Summary
This paper presents a new method for accelerating FFN layers in MetaFormer-structured architectures. The core idea is to combine structured reparameterization and partial channel skipping. Experiments are done on ImageNet classification, self-supervised learning, and dense prediction tasks. The proposed method can accelerate various ViT models with some accuracy drop.

### Strengths
1. The proposed method is interesting and technically sound. 
2. The problem studied in this paper is critical, as FFN is a big efficiency bottleneck for ViTs.
3. I appreciate seeing results outside ImageNet classification.

### Weaknesses
1. This paper lacks direct comparisons with network pruning. 
2. This paper lacks an essential baseline, training Figure 1 (c) from scratch. 
3. This paper lacks direct comparisons with previous structured reparameterization methods in previous works (e.g., FastViT's design). 
4. According to the results, the proposed method still suffers from accuracy drops.

### Questions
It seems the proposed method has to be used with BatchNorm. Is there any workaround to avoid using BatchNorm?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes RePaFormer, a novel approach that leverages a channel idle mechanism to enable structural reparameterization of Feed-Forward Network (FFN) layers during inference. Experiments on Vision Transformer families show its improved inference speed compared to baselines with minor performance loss.

### Strengths
1. The paper is well-written and well-motivated.

### Weaknesses
The major concern of the paper is that the current experimental setup raises concerns about the effectiveness of the proposed method.
1. **The effects of BatchNorm.**  Specifically, if I understand correctly, the vanilla backbone uses LayerNorm while RePaFormer family uses BatchNorm. It is unclear whether BatchNorm alone could improve the test performance, i.e., accuracy, of the vanilla backbone. The paper does not provide a direct comparison of a vanilla model with LayerNorm replaced by BatchNorm, keeping all other components the same, to isolate the impact of the normalization layer. This makes it difficult to ascertain if the performance gains are due to the proposed reparameterization or simply the change in normalization.
2. **Similarly, the effectiveness of channel idle mechanism is inadequately tested.** Specifically, consider the default case where $\mu=1$, and 75% percent of the features are idle. This implies for the RePa Linear 3 (Figure 1), the features go through a linear transformation $W_2W_1$ where $W_1 \in \mathbb{R}^{3C \times C}$ and $W_2 \in \mathbb{R}^{C \times 3C}$. However, such transformation can be represented by a $C \times C$ matrix, suggesting that the models use $6C^2$ parameters to learn a linear function that can be represented by just $C^2$ parameters. That means, RePaFormer will be useful only if it is much better in terms of accuracy than the baseline where the channel idle part is processed by a single linear layer with weight  $W \in \mathbb{R}^{C \times C}$. More specifically, this baseline should be in the form of Figure (b) [without BatchNorm inference reparameterization] and test its throughput and performance. Furthermore, the proposed channel idle mechanism introduces a specific sparsity pattern that may not be optimal; a more thorough investigation into different sparsity patterns and their impact on performance is needed.

### Questions
See my weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
2
