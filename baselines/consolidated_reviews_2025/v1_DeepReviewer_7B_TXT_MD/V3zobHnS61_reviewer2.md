### Summary

This paper proposes a retrieval-augmented test-time adaptation method for vision-language models (VLMs). The method leverages external knowledge to enhance the model's ability to adapt to test data distribution. The retrieval process is divided into two stages: image-to-text retrieval and text-to-image retrieval. The final prediction is adjusted on the fly using both the initial prediction and the retrieved external images.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective, as demonstrated by the experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The idea of leveraging external knowledge through retrieval has been explored in previous works. The paper does not clearly articulate how the proposed method differs from existing retrieval-based approaches, particularly in the context of test-time adaptation for VLMs. The specific mechanisms for image-to-text and text-to-image retrieval, as well as the relevance score calculation, lack sufficient novelty compared to existing retrieval-based methods.
2. The paper does not provide a clear explanation of how the proposed method addresses the distribution shift problem. While the motivation section mentions that the internal knowledge encoded within the model parameters may not generalize well to unseen test data, the paper does not provide a detailed analysis of how the retrieval process helps to mitigate this issue. The connection between the retrieval process and the reduction of distribution shift is not clearly established.
3. The paper lacks a detailed analysis of the computational cost of the proposed method. The retrieval process involves multiple steps, including image-to-text retrieval, text-to-image retrieval, and relevance score calculation, which may introduce significant computational overhead. The paper does not provide a quantitative analysis of the computational cost, including the time and memory requirements, which makes it difficult to assess the practicality of the proposed method.
4. The paper does not provide a thorough discussion of the limitations of the proposed method. For example, the performance of the proposed method may be sensitive to the quality of the external knowledge base and the retrieval process. The paper does not discuss how the method would perform in scenarios with noisy or incomplete external knowledge. The paper also does not discuss the potential biases in the external knowledge base and how these biases may affect the performance of the proposed method.

### Suggestions

The paper should provide a more detailed comparison with existing retrieval-based methods, particularly those used in test-time adaptation. A thorough analysis of the differences in methodology, including the specific retrieval algorithms, feature extraction methods, and relevance scoring mechanisms, is needed to justify the novelty of the proposed approach. The authors should clearly articulate how their method addresses the limitations of existing retrieval-based techniques, especially in the context of VLMs. For example, the paper could discuss how the proposed method handles the high dimensionality of VLM embeddings and how it ensures the robustness of the retrieval process. Furthermore, the paper should include a more detailed analysis of the computational cost of the proposed method, including the time and memory requirements for each step of the retrieval and adaptation process. This analysis should be compared with the computational cost of existing test-time adaptation methods to provide a clear understanding of the trade-offs between performance and efficiency. The paper should also discuss the potential limitations of the proposed method, such as its sensitivity to the quality of the external knowledge base and the retrieval process. The authors should explore how the method would perform in scenarios with noisy or incomplete external knowledge and discuss the potential biases in the external knowledge base and how these biases may affect the performance of the proposed method. 

To improve the evaluation, the paper should include a more detailed analysis of the impact of different components of the proposed method on its performance. For example, the authors could conduct ablation studies to evaluate the contribution of the image-to-text retrieval, text-to-image retrieval, and relevance score calculation to the overall performance. The paper should also explore the sensitivity of the proposed method to different hyperparameters, such as the number of retrieved images and the similarity threshold used in the retrieval process. This analysis would provide a better understanding of the robustness and generalizability of the proposed method. The paper should also include a more detailed discussion of the evaluation metrics used in the experiments. The authors should justify the choice of these metrics and discuss their limitations. The paper should also consider using additional evaluation metrics that are more suitable for evaluating the performance of VLMs, such as metrics that measure the alignment between the visual and textual features. 

Finally, the paper should provide a more detailed explanation of the motivation behind the proposed method. The authors should clearly articulate the limitations of existing test-time adaptation methods and explain how the proposed method addresses these limitations. The paper should also discuss the potential applications of the proposed method and its limitations. The authors should also discuss the potential ethical implications of the proposed method, such as the potential for bias amplification. The paper should also discuss the potential for future research in this area, such as the development of more robust and efficient retrieval-based test-time adaptation methods.

### Questions

Please see the weakness.

### Rating

5

### Confidence

4

**********
