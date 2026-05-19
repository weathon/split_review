### Summary

This work aims to improve the accuracy of text-video retrieval (TVR) while maintaining efficiency. It thus proposes a two-stage retrieval strategy, where the first stage adopts existing TVR methods to shortlist candidates, and the second stage improves the accuracy based on a cross-attention mechanism that involves multi-grained features. By using a frozen CLIP encoder, the method can scale to larger pre-trained models like ViT-G. Extensive experiments on five TVR benchmarks demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow, with clear motivation and good visual illustrations for the proposed method. The proposed method is effective, as demonstrated by extensive experiments on five mainstream text-video retrieval benchmarks. It can be applied to existing TVR methods to improve their accuracy. Notably, the method can be scaled up to large ViT-G with minimal additional computation cost.

### Weaknesses

#### Some Related Works


#### comment

The novelty of the proposed method is somewhat limited. The cross-attention mechanism is a common technique, and using a token selector and averaging selected tokens for re-ranking has been seen in TS2Net. The two-stage retrieval strategy is also not new, as seen in CLIP4Clip and DRL. The paper lacks a detailed analysis of the computational cost of the proposed method, especially the cross-attention mechanism, and does not provide a comparison of the computational cost with other state-of-the-art methods. Furthermore, the paper does not explore the impact of different token selection strategies on the performance of the proposed method. The choice of using averaged features from the token selector for re-ranking is not sufficiently justified, and the paper lacks an ablation study to demonstrate the importance of this design choice.

### Suggestions

The paper should provide a more thorough analysis of the computational cost of the proposed method, including a breakdown of the cost of each component, such as the cross-attention mechanism and the token selector. A comparison of the computational cost with other state-of-the-art methods, including both one-stage and two-stage approaches, should be included to better understand the efficiency of the proposed method. This analysis should also consider the impact of using different pre-trained models, such as ViT-G, on the computational cost. Furthermore, the paper should explore the impact of different token selection strategies on the performance of the proposed method. For example, instead of averaging the selected tokens, the paper could explore using max pooling or other aggregation methods. An ablation study should be conducted to justify the choice of averaging the selected tokens for re-ranking. This study should compare the performance of the proposed method with different aggregation methods and demonstrate the importance of the chosen design choice. The paper should also investigate the sensitivity of the proposed method to the number of selected tokens and provide guidelines for choosing the optimal number of tokens for different datasets and tasks. Finally, the paper should provide a more detailed analysis of the limitations of the proposed method and discuss potential future research directions. This analysis should include a discussion of the scenarios where the proposed method may not perform well and potential solutions to address these limitations.

### Questions

1. In Table 8, why is CLIP4Clip significantly slower than CLIP4Clip (Ours)? Is the inference speed of CLIP4Clip reported in this paper measured using a single A100, similar to the others?
2. What is the performance of applying the proposed method to a method that already uses a two-stage retrieval strategy, such as CLIP4Clip or DRL?
3. What is the performance if only one stage is used?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
