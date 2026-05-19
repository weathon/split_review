### Summary

This paper proposes a reranker for text-video retrieval (TVR) task, which is called CrossTVR. It explores the fine-grained and comprehensive interaction between text and all the vision tokens of a given video at the frame level and the video (clips or segments) level. The frozen CLIP model strategy is used for fine-grained retrieval. Experimental results on text-video retrieval datasets demonstrate the effectiveness and scalability of the proposed reranker when combined with existing mainstream one-stage text-video retrieval approaches.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is effective and efficient, which can be widely applied to existing cosine similarity-based methods and effectively improve the SOTA retrieval performance with marginal additional computation cost.
2. The proposed method is scalable, benefiting from the frozen visual coder training method, the approach can scale to larger pretrain visual models with small computational resources.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not novel. The frame-level and video-level cross attention is not new in the TVR task. The authors should highlight the difference between the proposed method and existing methods.
2. The authors claim that the proposed method can scale to larger pretrain visual models with small computational resources. However, the authors do not report the inference speed of the proposed method.
3. The authors should report the performance of the proposed method on Video2Text task.

### Suggestions

The paper introduces a re-ranking approach for text-video retrieval, which leverages frame-level and video-level cross-attention mechanisms. While the approach demonstrates effectiveness, the novelty is questionable given the existing literature on cross-attention in TVR. The authors should more clearly articulate the specific differences and advantages of their approach compared to existing methods. For instance, they could provide a detailed comparison of the architectural differences, the training procedures, and the specific types of attention mechanisms used in their method versus those in prior work. A more thorough analysis of the computational complexity of the proposed method is also needed. While the authors claim efficiency, they should provide concrete metrics such as inference time and memory usage, especially when scaling to larger pre-trained visual models. This would allow for a more objective evaluation of the method's practical applicability. Furthermore, the paper should include a more comprehensive evaluation of the proposed method, including the performance on the video-to-text retrieval task. This would provide a more complete picture of the method's capabilities and limitations.

To address the concerns about novelty, the authors should provide a more detailed analysis of how their method differs from existing cross-attention based approaches in TVR. Specifically, they should highlight the unique aspects of their approach, such as the specific way they combine frame-level and video-level attention, or any novel architectural components. A table comparing the proposed method with existing methods, focusing on the architectural differences, training procedures, and attention mechanisms, would be beneficial. This would help to clarify the contribution of the proposed method and justify its novelty. Furthermore, the authors should provide a more detailed analysis of the computational complexity of the proposed method. This should include a breakdown of the computational cost of each component of the method, as well as the overall inference time. This analysis should be performed for different model sizes and input lengths, to provide a comprehensive understanding of the method's scalability. The authors should also report the memory usage of the proposed method, as this is an important factor in practical applications.

Finally, the authors should include a more comprehensive evaluation of the proposed method, including the performance on the video-to-text retrieval task. This would provide a more complete picture of the method's capabilities and limitations. The evaluation should include a comparison with existing methods on both text-to-video and video-to-text retrieval tasks. The authors should also report the performance of the proposed method on different datasets, to demonstrate its generalizability. Furthermore, the authors should provide an analysis of the error cases, to identify the limitations of the proposed method and suggest potential directions for future research. This would help to improve the understanding of the method's strengths and weaknesses, and guide future work in this area.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
