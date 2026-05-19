### Summary

This paper proposes a multi-grained re-ranker, namely CrossTVR, which achieves comprehensive interaction between text and video at the frame level and video level. The proposed re-ranker can be applied to existing cosine similarity-based methods and effectively improve the retrieval performance with marginal additional computation cost. The proposed re-ranker can scale to larger pre-train visual models with small computational resources.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed CrossTVR is simple and effective.
2. The proposed CrossTVR can scale to larger pre-train visual models with small computational resources.
3. The paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not novel. The hierarchical attention has been widely applied to various vision-language models. The frame-level cross-attention and video-level cross-attention are widely applied to various video-language models. The token selector is also proposed in TS2Net. The overall technical contribution seems incremental, primarily combining existing techniques without substantial innovation in the attention mechanisms themselves or their application to the text-video retrieval task.
2. The proposed method is not efficient. In the inference stage, the proposed method requires calculating the similarity scores between the text and video using cosine similarity, followed by employing multi-grained video-text cross-attention for re-ranking the top K videos based on the previous similarity scores. This two-stage process introduces additional computational overhead, especially with the re-ranking step, which involves cross-attention calculations. The paper lacks a detailed analysis of the inference time complexity compared to single-stage methods.
3. The proposed method is not fair. In the experiments, this paper selects some one-stage methods for comparison. Since the proposed method is a two-stage method, it should be compared with other two-stage methods, e.g., CLIP4clip-tight and DRL. The lack of comparison with other two-stage methods makes it difficult to assess the true performance gains of the proposed method in its appropriate context.

### Suggestions

The paper should address the lack of novelty by exploring more sophisticated attention mechanisms or by demonstrating a novel application of existing mechanisms to the text-video retrieval task. For example, the authors could investigate adaptive attention mechanisms that dynamically adjust the attention weights based on the input text and video content, rather than using a fixed hierarchical structure. Furthermore, the paper should provide a more detailed analysis of the computational cost of the proposed method, including a breakdown of the time spent in each stage of the inference process. This analysis should compare the inference time of the proposed method with that of single-stage methods, as well as other two-stage methods, to provide a more comprehensive understanding of its efficiency. The authors should also consider exploring techniques to reduce the computational overhead of the re-ranking stage, such as using a more efficient attention mechanism or by reducing the number of candidates for re-ranking.

To address the issue of unfair comparison, the authors should include a more comprehensive evaluation of the proposed method against other two-stage text-video retrieval methods. This evaluation should include a variety of metrics, such as recall and precision, and should be conducted on multiple datasets. The authors should also provide a detailed analysis of the performance differences between the proposed method and other two-stage methods, highlighting the strengths and weaknesses of each approach. This would provide a more fair and accurate assessment of the proposed method's performance. Additionally, the authors should consider exploring the impact of different pre-training strategies on the performance of the proposed method, as well as the impact of different visual backbone architectures. This would provide a more comprehensive understanding of the proposed method's capabilities and limitations.

Finally, the paper should provide a more detailed explanation of the token selector and its impact on the overall performance of the proposed method. The authors should also consider exploring alternative token selection strategies and comparing their performance with that of the proposed token selector. This would provide a more comprehensive understanding of the role of token selection in the text-video retrieval task. The authors should also provide a more detailed explanation of the frame-level and video-level cross-attention mechanisms, including the specific implementation details and the rationale behind their design choices. This would help the reader better understand the proposed method and its contributions.

### Questions

1. Why not compare the proposed method with other two-stage methods?
2. What is the inference speed of the proposed method?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
