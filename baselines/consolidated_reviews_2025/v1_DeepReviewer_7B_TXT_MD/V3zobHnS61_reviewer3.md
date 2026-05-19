### Summary

This paper proposes a retrieval-augmented test-time adaptation (RA-TTA) method for vision-language models (VLMs) to adapt to test distribution. The method first retrieves relevant external images and text descriptions for the test image and then fuses the retrieved information with the original prediction to produce an adapted prediction. The retrieval process is divided into two stages: image-to-text retrieval and text-to-image retrieval. The image-to-text retrieval selects relevant text descriptions for the test image, while the text-to-image retrieval retrieves external images aligned with the selected text descriptions. The final prediction is adjusted on the fly using both the initial prediction and the retrieved external images. The authors conduct extensive experiments on 17 datasets and demonstrate that RA-TTA outperforms state-of-the-art test-time adaptation methods by 2.49-8.45% on average.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective, as demonstrated by the experimental results.
3. The authors conduct extensive experiments on 17 datasets and demonstrate that RA-TTA outperforms state-of-the-art test-time adaptation methods by 2.49-8.45% on average.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The idea of leveraging external knowledge through retrieval has been explored in previous works. The paper does not clearly articulate how the proposed method differs from existing retrieval-based approaches, particularly in the context of test-time adaptation for VLMs. The specific mechanisms for image-to-text and text-to-image retrieval, as well as the relevance score calculation, lack sufficient novelty compared to existing retrieval-based methods.
2. The paper does not provide a clear explanation of how the proposed method addresses the distribution shift problem. While the motivation section mentions that the internal knowledge encoded within the model parameters may not generalize well to unseen test data, the paper does not provide a detailed analysis of how the retrieval process helps to mitigate this issue. The connection between the retrieval process and the reduction of distribution shift is not clearly established.
3. The paper lacks a detailed analysis of the computational cost of the proposed method. The retrieval process involves multiple steps, including image-to-text retrieval, text-to-image retrieval, and relevance score calculation, which may introduce significant computational overhead. The paper does not provide a quantitative analysis of the computational cost, including the time and memory requirements, which makes it difficult to assess the practicality of the proposed method.
4. The paper does not provide a thorough discussion of the limitations of the proposed method. For example, the performance of the proposed method may be sensitive to the quality of the external knowledge base and the retrieval process. The paper does not discuss how the method would perform in scenarios with noisy or incomplete external knowledge. The paper also does not discuss the potential biases in the external knowledge base and how these biases may affect the performance of the proposed method.

### Suggestions

The paper would benefit from a more thorough comparison with existing retrieval-based methods, particularly those used in test-time adaptation. The authors should clearly articulate the specific differences in their approach, focusing on the unique aspects of their method that address the limitations of prior work. For instance, a detailed analysis of how the proposed image-to-text and text-to-image retrieval processes differ from existing techniques, and how these differences contribute to improved performance, would be valuable. Furthermore, the relevance score calculation should be compared to other methods used in retrieval-based adaptation, highlighting the novelty and advantages of the proposed approach. This would help to establish the significance of the proposed method and its contribution to the field.

To strengthen the paper, the authors should provide a more detailed explanation of how the proposed method addresses the distribution shift problem. The paper should include a theoretical analysis or empirical evidence to demonstrate how the retrieval process helps to mitigate the issue of internal knowledge not generalizing well to unseen test data. For example, the authors could analyze the feature space of the retrieved images and text descriptions and show how they align with the test image, thus reducing the distribution shift. Additionally, the authors should discuss the limitations of their approach in scenarios with noisy or incomplete external knowledge. They should also explore potential strategies to mitigate these limitations, such as using robust retrieval techniques or incorporating uncertainty measures into the adaptation process. This would provide a more comprehensive understanding of the method's robustness and applicability.

Finally, the paper needs a more detailed analysis of the computational cost of the proposed method. The authors should provide a quantitative analysis of the time and memory requirements for each step of the retrieval and adaptation process. This analysis should include a comparison with existing test-time adaptation methods to demonstrate the trade-offs between performance and efficiency. Furthermore, the authors should discuss the scalability of their method to larger datasets and more complex models. This would help to assess the practicality of the proposed method and its potential for real-world applications. The authors should also consider the impact of different retrieval strategies on the computational cost and discuss how to optimize the method for efficiency.

### Questions

1. How does the proposed method compare to existing retrieval-based methods in terms of novelty and performance?
2. What is the computational cost of the proposed method, and how does it compare to existing test-time adaptation techniques?
3. How does the proposed method address the distribution shift problem, and what is the theoretical basis for its effectiveness?

### Rating

5

### Confidence

4

**********
