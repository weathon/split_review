### Summary

This paper proposes a concept-informed diffusion process for dataset distillation, which leverages large language models (LLMs) to enhance instance-level conceptual completeness. The proposed method, CONCORD, retrieves distinguishable concepts based on category labels and utilizes these concepts to inform the diffusion-based sample generation process. The authors demonstrate the effectiveness of CONCORD on multiple benchmarks, including ImageNet-1K and its subsets, showing state-of-the-art performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The authors provide a clear motivation for their work and present their method in a logical and understandable manner.
- The proposed CONCORD method is novel and addresses a gap in dataset distillation by focusing on instance-level conceptual completeness. The use of LLMs to retrieve distinguishable concepts is an innovative approach that enhances the quality of distilled images.
- The authors conduct extensive experiments on multiple benchmarks, including ImageNet-1K and its subsets, demonstrating the effectiveness of CONCORD. The results show consistent improvements over baseline methods, particularly in terms of accuracy and interpretability.
- The paper includes ablation studies that analyze the impact of different components and hyperparameters, providing valuable insights into the method's behavior and performance.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not discuss the computational cost associated with the proposed CONCORD method, which is important for practical applications. Specifically, the overhead introduced by the LLM concept retrieval and the concept-informed diffusion process is not quantified, making it difficult to assess the method's feasibility for large-scale datasets or real-time applications. The paper should include a detailed analysis of the time and memory requirements for each step of the pipeline, including concept retrieval, diffusion, and generation.
- The paper does not address the potential biases that may arise from using large language models (LLMs) for concept retrieval. These biases could affect the diversity and representativeness of the distilled datasets. The paper should investigate how the inherent biases in LLMs, such as those related to cultural, social, or gender perspectives, might propagate into the distilled datasets and potentially skew the results. A more thorough analysis of the impact of these biases on the distilled datasets is needed.
- The paper could benefit from a more detailed discussion of the limitations of the proposed method. For example, the authors do not discuss the sensitivity of the method to the choice of LLMs or the potential for the method to fail in certain scenarios. The paper should also discuss the potential for the method to introduce artifacts or biases into the distilled datasets, and how these artifacts might affect the performance of downstream tasks.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their method. This should include a breakdown of the time and memory requirements for each step of the pipeline, such as the LLM concept retrieval, the diffusion process, and the final image generation. It would be beneficial to compare the computational cost of CONCORD with existing dataset distillation methods to provide a clear understanding of the trade-offs between performance and computational resources. Furthermore, the authors should investigate the scalability of their method to larger datasets and more complex models. This could involve profiling the runtime of different components of the pipeline and identifying potential bottlenecks. The authors should also consider providing guidelines for optimizing the implementation of their method to reduce its computational footprint. For example, they could explore techniques such as model quantization or pruning to reduce the computational cost of the LLM and diffusion processes.

To address the potential biases introduced by LLMs, the authors should conduct a more thorough investigation into how these biases might affect the distilled datasets. This should include an analysis of the types of biases that can arise from LLMs, such as cultural, social, or gender biases. The authors should also explore methods to mitigate these biases, such as using diverse LLMs, incorporating fairness constraints into the distillation process, or post-processing the distilled datasets to remove biased examples. For example, they could investigate techniques like adversarial training or data augmentation to reduce the impact of biased concepts. Additionally, the authors should evaluate the impact of these biases on the performance of downstream tasks to determine whether the biases are merely artifacts of the distillation process or if they have a more significant impact on the quality of the distilled datasets. This analysis should also include a discussion of the limitations of the proposed method in terms of its robustness to biases.

Finally, the authors should provide a more detailed discussion of the limitations of their method. This should include a discussion of the sensitivity of the method to the choice of LLMs, the potential for the method to fail in certain scenarios, and the potential for the method to introduce artifacts or biases into the distilled datasets. For example, the authors could investigate how the performance of CONCORD varies with different LLMs and whether certain LLMs are more suitable for specific tasks. They should also discuss the potential for the method to fail in cases where the concepts retrieved from the LLM are not representative of the class or when the LLM retrieves concepts that are not relevant to the task. Furthermore, the authors should discuss the potential for the method to introduce artifacts or biases into the distilled datasets, and how these artifacts might affect the performance of downstream tasks. This discussion should also include a comparison of the limitations of CONCORD with those of existing dataset distillation methods.

### Questions

- How does the CONCORD method handle the potential biases introduced by large language models (LLMs) during concept retrieval? Are there any specific strategies or techniques used to mitigate these biases?
- What is the computational cost of the CONCORD method compared to existing dataset distillation approaches? How does the method scale with larger datasets and more complex models?
- Are there any limitations or failure cases of the CONCORD method? For example, how sensitive is the method to the choice of LLMs, or are there specific scenarios where the method might not perform well?

### Rating

6

### Confidence

4

**********
