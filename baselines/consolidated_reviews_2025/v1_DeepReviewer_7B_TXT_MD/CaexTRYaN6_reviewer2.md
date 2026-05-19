### Summary

This paper proposes a dataset distillation method that uses LLMs to enhance instance-level conceptual completeness. The authors introduce CONCORD, a concept-informed diffusion process that leverages LLMs to retrieve fine-grained concepts for each class, which are then used to refine the quality of generated images during the diffusion process. The method is evaluated on multiple benchmarks, demonstrating state-of-the-art performance and offering a promising direction for more controllable and effective dataset distillation.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective. The authors have conducted extensive experiments to validate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the computational cost associated with the proposed CONCORD method, which is important for practical applications. Specifically, the overhead introduced by the LLM concept retrieval and the concept-informed diffusion process is not quantified, making it difficult to assess the method's feasibility for large-scale datasets or real-time applications. The paper should include a detailed analysis of the time and memory requirements for each step of the pipeline, including concept retrieval, diffusion, and generation.
2. The paper does not address the potential biases that may arise from using large language models (LLMs) for concept retrieval. These biases could affect the diversity and representativeness of the distilled datasets. The paper should investigate how the inherent biases in LLMs, such as those related to cultural, social, or gender perspectives, might propagate into the distilled datasets and potentially skew the results. A more thorough analysis of the impact of these biases on the distilled datasets is needed.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their method. This should include a breakdown of the time and memory requirements for each step of the pipeline, such as the LLM concept retrieval, the diffusion process, and the final image generation. It would be beneficial to compare the computational cost of CONCORD with existing dataset distillation methods to provide a clear understanding of the trade-offs between performance and computational resources. Furthermore, the authors should investigate the scalability of their method to larger datasets and more complex models. This could involve profiling the runtime of different components of the pipeline and identifying potential bottlenecks. The authors should also consider providing guidelines for optimizing the implementation of their method to reduce its computational footprint.

To address the potential biases introduced by LLMs, the authors should conduct a more thorough investigation into how these biases might affect the distilled datasets. This should include an analysis of the types of biases that can arise from LLMs, such as cultural, social, or gender biases. The authors should also explore methods to mitigate these biases, such as using diverse LLMs, incorporating fairness constraints into the distillation process, or post-processing the distilled datasets to remove biased examples. For example, the authors could investigate techniques like adversarial training or data augmentation to reduce the impact of biased concepts. Additionally, the authors should evaluate the impact of these biases on the performance of downstream tasks to determine whether the biases are merely artifacts of the distillation process or if they have a more significant impact on the quality of the distilled datasets. This analysis should also include a discussion of the limitations of the proposed method in terms of its robustness to biases.

Finally, the authors should investigate the impact of different concept choices on the performance of the distillation process. While the paper mentions using GPT-3.5 and GPT-4, it does not provide a detailed analysis of how different concept choices affect the quality of the distilled datasets. The authors should explore the sensitivity of the method to different concept sets and investigate whether there are specific types of concepts that are more effective for certain classes or categories. This analysis should include a discussion of the trade-offs between the number of concepts used, the quality of the concepts, and the computational cost of the distillation process. Furthermore, the authors should provide guidelines for selecting the most appropriate concepts for each class, potentially based on the specific characteristics of the class or the available data.

### Questions

Please see the weakness.

### Rating

6

### Confidence

3

**********
