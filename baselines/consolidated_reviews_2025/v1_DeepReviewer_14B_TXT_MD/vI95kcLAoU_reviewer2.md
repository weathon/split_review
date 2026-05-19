### Summary

This paper introduces Skip-Attention to improve the efficiency of ViTs. The authors find that the attention of the CLS tokens to the spatial patches has a very high correlation across the transformer’s blocks, thus leading to unnecessary computations. Therefore, they reuse self-attention computation from preceding layers to approximate attention at one or more subsequent layers. A simple parametric function is introduced to ensure the performance is not degraded. The proposed method is evaluated on several tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is technically sound. 
2. The authors evaluate the proposed method on several tasks.

### Weaknesses

#### Some Related Works

[1] Swin transformer: Hierarchical vision transformer using shifted windows
[2] EfficientViT: Memory Efficient Vision Transformer with Cascaded Group Attention

#### comment

1. The novelty of the paper is only average. The idea of sharing the attention map across layers has been investigated in previous works in NLP, such as Sharing is Caring: Attention Map in Attention Network. The main difference between the proposed method and these previous works is the introduced parametric function in Skip-Attention. However, the design of the parametric function is straightforward, which somewhat weakens the novelty and contribution of the paper.
2. In the experiments, the authors only compared Skip-Attention with the vanilla ViT. However, there are several works aiming to improve the efficiency of ViT. It is necessary to compare Skip-Attention with these methods. For example, Swin-Transformer [1] reduces the computation cost by restricting the self-attention within a window. EfficientViT [2] reduces the computational cost by group attention and low-rank self-gating. It is necessary to compare the proposed method with these works to evaluate the performance of the proposed method.

### Suggestions

The paper's core idea of reusing attention computations across layers to reduce the quadratic complexity of self-attention is promising, but its novelty is somewhat limited due to prior work exploring similar concepts in NLP. While the authors introduce a parametric function to adapt the reused attention, the design is relatively simple, and the paper would benefit from a more in-depth exploration of more sophisticated methods for cross-layer attention adaptation. For instance, the authors could investigate incorporating techniques like attention heads or dynamic weighting schemes within the parametric function to allow for more fine-grained control over the reused attention. This could potentially lead to more significant performance improvements and a more substantial contribution to the field. Furthermore, a more detailed analysis of the impact of different parameter settings for the parametric function would be beneficial to understand its behavior and limitations.

To strengthen the experimental evaluation, it is crucial to compare the proposed method against a wider range of state-of-the-art efficient ViT architectures. The current comparison with only the vanilla ViT is insufficient to demonstrate the practical advantages of Skip-Attention. Specifically, the paper should include comparisons with methods that reduce computational cost by dropping redundant tokens, merging tokens, or using token sampling techniques. This would provide a more comprehensive understanding of the proposed method's strengths and weaknesses relative to existing techniques. For example, comparing against methods that use hierarchical token merging or adaptive token selection would be particularly relevant. Additionally, the evaluation should include a more detailed analysis of the trade-off between computational cost and performance for the proposed method, as well as for the compared baselines. This would help to better understand the practical applicability of Skip-Attention in different scenarios.

Finally, the paper should provide a more thorough analysis of the impact of the proposed method on different types of data and tasks. The current evaluation is limited to a few specific tasks, and it is not clear how well the method would generalize to other domains. For example, it would be interesting to see how the method performs on tasks with different levels of complexity or on datasets with different characteristics. Furthermore, the paper should investigate the sensitivity of the proposed method to different hyperparameter settings, such as the number of layers to skip or the parameters of the parametric function. This would help to better understand the robustness of the method and provide practical guidance for its application.

### Questions

Please refer to the Weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
