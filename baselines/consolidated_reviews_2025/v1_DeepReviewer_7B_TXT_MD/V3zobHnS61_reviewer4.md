### Summary

This paper proposes a novel test-time adaptation method for vision-language models (VLMs) that leverages external knowledge from a web-scale image database. The method, named RA-TTA, first retrieves relevant images and text descriptions for a given test image and then uses these retrieved items to adapt the VLM's predictions. The retrieval process is divided into two stages: image-to-text retrieval and text-to-image retrieval. The final prediction is adjusted on the fly using both the initial prediction and the retrieved external images. The authors demonstrate the effectiveness of RA-TTA through extensive experiments on 17 datasets, showing that it outperforms state-of-the-art methods by 2.49-8.45% on average.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the motivation, methodology, and experimental results.
2. The proposed method is simple yet effective. The authors demonstrate the effectiveness of RA-TTA through extensive experiments on 17 datasets, showing that it outperforms state-of-the-art methods by 2.49-8.45% on average.
3. The authors provide a comprehensive analysis of the proposed method, including ablation studies and hyperparameter sensitivity analysis. This helps to understand the contribution of each component of the method and the robustness of the method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method. The retrieval process involves multiple steps, including image-to-text retrieval, text-to-image retrieval, and relevance score calculation, which may introduce significant computational overhead. The paper should provide a quantitative analysis of the time and memory requirements for each step of the retrieval and adaptation process. This analysis should be compared with existing test-time adaptation methods to demonstrate the trade-offs between performance and efficiency.
2. The paper does not provide a detailed analysis of the limitations of the proposed method. For example, the performance of the proposed method may be sensitive to the quality of the external knowledge base and the retrieval process. The paper should discuss how the method would perform in scenarios with noisy or incomplete external knowledge. The paper should also discuss the potential biases in the external knowledge base and how these biases may affect the performance of the proposed method.
3. The paper does not provide a detailed analysis of the hyperparameter sensitivity of the proposed method. The authors should discuss how the performance of the method is affected by different hyperparameters, such as the number of retrieved images and the similarity threshold used in the retrieval process. This analysis would provide a better understanding of the robustness and generalizability of the method.

### Suggestions

The paper would benefit from a more thorough investigation into the computational demands of the proposed RA-TTA method. Specifically, the authors should provide a detailed breakdown of the time complexity for each stage of the retrieval process, including image-to-text retrieval, text-to-image retrieval, and relevance score calculation. This analysis should not only consider the theoretical complexity but also provide empirical measurements of the actual time taken for each step on the used hardware. Furthermore, a comparison of the memory footprint of RA-TTA with other test-time adaptation methods would be valuable. This would allow readers to better understand the practical trade-offs between performance gains and computational costs, which is crucial for real-world applications. The authors should also explore potential optimizations to reduce the computational overhead, such as using more efficient indexing techniques for the image and text databases or employing parallel processing strategies.

To address the limitations regarding the external knowledge base, the authors should conduct experiments to evaluate the robustness of RA-TTA under various conditions. This could involve introducing noise or incompleteness into the retrieved images and text descriptions and observing how the performance of the method is affected. For instance, the authors could simulate scenarios where some retrieved items are irrelevant or misleading, and then analyze how the method handles these cases. Additionally, the authors should investigate the potential biases present in the external knowledge base and their impact on the adaptation process. This could involve analyzing the distribution of retrieved items and identifying any systematic biases that might lead to skewed predictions. The authors could also explore techniques to mitigate these biases, such as using adversarial training or data augmentation methods.

Finally, a more comprehensive analysis of the hyperparameter sensitivity is needed. The authors should systematically vary key hyperparameters, such as the number of retrieved images, the similarity threshold, and the weighting of the relevance score, and evaluate their impact on the overall performance. This analysis should not only focus on the average performance but also examine the variance in performance across different datasets and tasks. The authors should also provide guidelines for selecting appropriate hyperparameter values based on the characteristics of the dataset and the task at hand. This would make the method more practical and easier to use for other researchers. Furthermore, the authors should discuss the potential for automating the hyperparameter tuning process, such as using Bayesian optimization or grid search techniques.

### Questions

1. How does the proposed method compare to existing retrieval-based methods in terms of novelty and performance?
2. What is the computational cost of the proposed method, and how does it compare to existing test-time adaptation techniques?
3. How does the proposed method address the distribution shift problem, and what is the theoretical basis for its effectiveness?

### Rating

6

### Confidence

4

**********
