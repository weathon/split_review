### Summary

This paper proposes a dataset distillation approach that leverages large language models (LLMs) to enhance instance-level conceptual completeness during the distillation process. By incorporating LLM-derived concepts, CONCORD aims to improve the quality and controllability of distilled datasets, addressing limitations in existing methods that lack explicit instance-level control. The method is evaluated on multiple benchmarks, demonstrating state-of-the-art performance and offering a promising direction for more controllable and effective dataset distillation.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand.
2. The paper provides a thorough comparison with existing state-of-the-art methods, demonstrating the effectiveness of the proposed CONCORD approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the computational cost associated with the proposed CONCORD method, which is important for practical applications. Specifically, the overhead introduced by the LLM concept retrieval and the concept-informed diffusion process is not quantified, making it difficult to assess the method's feasibility for large-scale datasets or real-time applications. The paper should include a detailed analysis of the time and memory requirements for each step of the pipeline, including concept retrieval, diffusion, and generation.
2. The paper does not address the potential biases that may arise from using large language models (LLMs) for concept retrieval. These biases could affect the diversity and representativeness of the distilled datasets. The paper should investigate how the inherent biases in LLMs, such as those related to cultural, social, or gender perspectives, might propagate into the distilled datasets and potentially skew the results. A more thorough analysis of the impact of these biases on the distilled datasets is needed.

### Suggestions

The paper should include a detailed analysis of the computational cost associated with the CONCORD method. This analysis should quantify the time and memory requirements for each step of the pipeline, including concept retrieval, diffusion, and generation. Specifically, the authors should provide a breakdown of the computational cost for each component, such as the LLM concept retrieval, the diffusion process, and the final image generation. This analysis should also consider the impact of different LLMs and diffusion models on the overall computational cost. Furthermore, the authors should compare the computational cost of CONCORD with existing dataset distillation methods to provide a clear understanding of the trade-offs between performance and computational resources. This would allow readers to assess the practical applicability of the method in different scenarios.

To address the potential biases introduced by LLMs, the authors should conduct a more thorough investigation into how these biases might affect the distilled datasets. This should include an analysis of the types of biases that can arise from LLMs, such as cultural, social, or gender biases. The authors should also explore methods to mitigate these biases, such as using diverse LLMs, incorporating fairness constraints into the distillation process, or post-processing the distilled datasets to remove biased examples. For example, the authors could investigate techniques like adversarial training or data augmentation to reduce the impact of biased concepts. Additionally, the authors should evaluate the impact of these biases on the performance of downstream tasks to determine whether the biases are merely artifacts of the distillation process or if they have a more significant impact on the quality of the distilled datasets. This analysis should also include a discussion of the limitations of the proposed method in terms of its robustness to biases.

Finally, the paper should explore the impact of different concept choices on the performance of the distillation process. While the paper mentions using GPT-3.5 and GPT-4, it does not provide a detailed analysis of how different concept choices affect the quality of the distilled datasets. The authors should investigate the sensitivity of the method to different concept sets and explore methods for selecting the most appropriate concepts for each class. This analysis should include a discussion of the trade-offs between the number of concepts used, the quality of the concepts, and the computational cost of the distillation process. Furthermore, the authors should investigate whether there are specific types of concepts that are more effective for certain classes or categories. This would provide valuable insights into the design of effective concept-informed distillation methods.

### Questions

1. How does the CONCORD method handle the potential biases introduced by large language models (LLMs) during concept retrieval?
2. What is the computational cost of the CONCORD method compared to existing dataset distillation approaches?
3. How does the choice of concepts influence the performance of the distillation process?

### Rating

6

### Confidence

3

**********
