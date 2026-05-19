### Summary

This paper proposed a simple yet effective method, called Skip-Attention, to reduce the costly O(n^2) self-attention computation in vision transformers (ViT). The authors proposed to reuse self-attention computation from preceding layers to approximate the attention at one or more subsequent layers. A simple parametric function is introduced to ensure the performance is not degraded. The authors demonstrated the effectiveness of Skip-Attention on several tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is simple and effective.
2. The authors conducted extensive experiments to demonstrate the effectiveness of the proposed method.
3. The paper is well written.

### Weaknesses

#### Some Related Works

[1] Sharing is Caring: Attention Map in Attention Network

#### comment

1. The novelty of the paper is only average. The idea of sharing the attention map across layers has been investigated in previous works in NLP, such as [Sharing is Caring: Attention Map in Attention Network]. The main difference between the proposed method and these previous works is the introduced parametric function in Skip-Attention. However, the design of the parametric function is straightforward, which somewhat weakens the novelty and contribution of the paper.
2. The authors claimed that the introduced parametric function could capture the cross-token relations. However, from my understanding, the function is independent for each token, which means it cannot model the dependency between different tokens.
3. In the experiments, the authors only compared Skip-Attention with the vanilla ViT. However, there are several works aiming to improve the efficiency of ViT. It is necessary to compare Skip-Attention with these methods.

### Suggestions

The paper's core idea of reusing attention computations across layers to reduce the quadratic complexity of self-attention is promising, but its novelty is somewhat limited due to prior work exploring similar concepts in NLP. While the authors introduce a parametric function to adapt the reused attention, the design is relatively simple, and the paper would benefit from a more in-depth exploration of more sophisticated methods for cross-layer attention adaptation. For instance, the authors could investigate incorporating techniques like attention heads or dynamic weighting schemes within the parametric function to allow for more fine-grained control over the reused attention. This could potentially lead to more significant performance improvements and a more substantial contribution to the field.

Furthermore, the paper's claim that the parametric function captures cross-token relations is not entirely accurate. The current implementation applies the function independently to each token, which limits its ability to model dependencies between tokens. To address this, the authors could explore incorporating mechanisms that allow the parametric function to consider the context of neighboring tokens, such as using convolutional layers with larger receptive fields or incorporating a lightweight self-attention mechanism within the parametric function itself. This would enable the function to capture more complex relationships between tokens and potentially improve the overall performance of the proposed method. Additionally, a more detailed analysis of the impact of different kernel sizes on the depth-wise convolution would be beneficial, as this parameter likely plays a crucial role in capturing cross-token relations.

Finally, the experimental evaluation needs to be significantly expanded to include comparisons with other state-of-the-art methods for efficient ViT computation. The current evaluation only compares against the vanilla ViT, which does not provide a comprehensive understanding of the proposed method's performance relative to existing techniques. The authors should include comparisons with methods that reduce computational cost by dropping redundant tokens, merging tokens, or using token sampling techniques. This would provide a more thorough evaluation of the proposed method's strengths and weaknesses and help to establish its practical value. Specifically, it would be important to compare against methods that achieve similar FLOPs reductions to provide a fair comparison of the performance trade-offs.

### Questions

1. The authors claimed that the introduced parametric function could capture the cross-token relations. However, from my understanding, the function is independent for each token, which means it cannot model the dependency between different tokens.
2. In the experiments, the authors only compared Skip-Attention with the vanilla ViT. However, there are several works aiming to improve the efficiency of ViT. It is necessary to compare Skip-Attention with these methods.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
