### Summary

This paper proposes a two-stage text-video retrieval architecture. In the first stage, the cosine similarity network is used to obtain text-video candidate pairs. In the second stage, the proposed re-ranker is applied for fine-grained retrieval. The proposed method is evaluated on several text-video retrieval benchmarks, including MSRVTT, VATEX, LSMDC, ActivityNet, and DiDeMo.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is simple and effective.
2. The proposed method can be widely applied to existing cosine similarity-based methods and effectively improve the SOTA retrieval performance with marginal additional computation cost.
3. The proposed method can scale to larger pre-train visual models with small computational resources.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not novel. The hierarchical attention has been widely applied to various vision-language models. The frame-level cross-attention and video-level cross-attention are widely applied to various video-language models. The token selector is also proposed in TS2Net. 
2. The proposed method is not efficient. In the inference stage, the proposed method requires calculating the similarity scores between the text and video using cosine similarity, followed by employing multi-grained video-text cross-attention for re-ranking the top K videos based on the previous similarity scores.
3. The proposed method is not fair. In the experiments, this paper selects some one-stage methods for comparison. Since the proposed method is a two-stage method, it should be compared with other two-stage methods, e.g., CLIP4clip-tight and DRL.

### Suggestions

The paper should more clearly articulate the specific novelty of their approach beyond the combination of existing techniques. While the authors claim a novel application of hierarchical attention, they need to provide a more detailed explanation of how their specific implementation differs from existing methods. For example, they should specify the exact differences in the attention mechanisms, the input features used, and the training procedures compared to other vision-language models that use hierarchical attention. Furthermore, the paper should include a more thorough ablation study to demonstrate the contribution of each component of their proposed method. This should include a comparison of the performance with and without the hierarchical attention, the token selector, and the two-stage re-ranking process. This would help to isolate the impact of each component and better justify the design choices.

To address the efficiency concerns, the authors should provide a more detailed analysis of the computational cost of their method, including the time and memory requirements for both training and inference. They should also compare the computational cost of their method with other state-of-the-art methods, including both one-stage and two-stage approaches. This comparison should include a breakdown of the time spent on each stage of the inference process, such as the initial cosine similarity calculation and the subsequent re-ranking with cross-attention. Furthermore, the authors should explore potential optimizations to reduce the computational cost of their method, such as using more efficient attention mechanisms or reducing the number of tokens used in the cross-attention. The paper should also include a discussion of the trade-offs between accuracy and efficiency, and how their method balances these two factors.

Finally, the authors should conduct a more comprehensive comparison with other two-stage methods, such as CLIP4clip-tight and DRL, to provide a fairer evaluation of their method. This comparison should include a detailed analysis of the performance of each method on different datasets and under different evaluation metrics. The authors should also discuss the limitations of their method and identify potential areas for future research. This would help to provide a more complete and balanced assessment of the proposed method and its contribution to the field. The paper should also include a discussion of the potential impact of their method on real-world applications and the ethical considerations associated with its use.

### Questions

Please refer to the Weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
