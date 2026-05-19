### Summary

The paper proposes a method to improve the accuracy and parameter efficiency of neural networks through weight reconstruction using predictor networks. The authors present surprising findings where the predicted model not only matches but also surpasses the original model's performance through the reconstruction objective (MSE loss) alone. They propose a novel training scheme that decouples the reconstruction objective from auxiliary objectives such as knowledge distillation that leads to significant improvements compared to state-of-the-art approaches.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and intuitive.
3. The method is demonstrated on multiple datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on CNNs and does not address the applicability of the method to other architectures like Transformers or MLPs. The lack of experiments on diverse architectures limits the generalizability of the findings. It is unclear if the proposed method would be effective for models with different structural properties, such as those found in Transformers, which rely on attention mechanisms rather than convolutional layers. The method's reliance on layer indices and channel counts, which are explicitly defined in CNNs but not in Transformers, raises concerns about its direct applicability to other architectures.
2. The multiple rounds of training required for progressive training could be resource-intensive and time-consuming. The paper does not provide a detailed analysis of the computational cost associated with each round of training, making it difficult to assess the practical feasibility of the approach. The cumulative training time for multiple rounds could be prohibitive for large models or datasets, and the paper lacks a discussion of potential optimizations to mitigate this issue.
3. The predictor network's capacity needs to be larger than the original network to achieve better performance, which could be a limitation in resource-constrained environments. While the authors mention that the predictor network needs to be larger, they do not provide a detailed analysis of the relationship between the predictor network size and the performance gains. This lack of analysis makes it difficult to determine the optimal size of the predictor network and whether there are diminishing returns with increasing size. The need for a larger predictor network also increases the memory footprint and computational cost, which could be a significant limitation in resource-constrained environments.
4. The paper does not provide a baseline without knowledge distillation for the model compression scenario. Without this baseline, it is difficult to isolate the specific contribution of the proposed method from the effects of knowledge distillation. It is unclear whether the performance gains are due to the weight reconstruction process or simply the knowledge distillation. A baseline without knowledge distillation is necessary to properly evaluate the effectiveness of the proposed method for model compression.

### Suggestions

The authors should investigate the applicability of their method to other architectures, such as Transformers and MLPs, to broaden the scope and impact of their work. This would involve adapting the method to handle the different structural properties of these architectures, such as attention mechanisms in Transformers. Specifically, the authors could explore how to define layer indices and channel counts in a way that is compatible with Transformers. Furthermore, they should provide a detailed analysis of the computational cost associated with each round of training in the progressive training approach. This analysis should include the training time, memory usage, and energy consumption. The authors could also explore potential optimizations to reduce the computational cost, such as using more efficient training algorithms or reducing the number of training rounds. This would make the approach more practical for large models and datasets. The authors should also provide a more detailed analysis of the relationship between the predictor network size and the performance gains. This analysis should include a study of the optimal size of the predictor network and whether there are diminishing returns with increasing size. The authors could also explore techniques to reduce the memory footprint and computational cost of the predictor network, such as model compression or pruning. This would make the approach more feasible for resource-constrained environments. Finally, the authors should include a baseline without knowledge distillation for the model compression scenario. This baseline would allow for a more accurate assessment of the specific contribution of the proposed method. The authors should also provide a more detailed comparison of their method with other model compression techniques, such as quantization and pruning, to better understand its strengths and weaknesses.

### Questions

1. Can the proposed method be extended to Transformer-based models or large language models (LLMs)? If so, how would the approach need to be adapted?
2. What is the computational overhead of the progressive training approach, and how does it scale with the size of the model and dataset?
3. Are there any potential optimizations or alternative strategies to reduce the predictor network's parameter count while maintaining performance?
4. How does the proposed method compare to other model compression techniques, such as quantization or pruning, in terms of accuracy, compression rate, and computational efficiency?

### Rating

5

### Confidence

4

**********
