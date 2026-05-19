### Summary

The paper proposes a novel approach to weight parameterization using neural representations for network parameterization. The proposed method decouples the training process into two stages: reconstruction and distillation. The reconstruction stage focuses on improving model performance by increasing the capacity of the predictor network, while the distillation stage focuses on reducing the model size by transferring knowledge from a high-performing teacher network. The paper demonstrates the effectiveness of the proposed approach through extensive experiments on various datasets and architectures, showing significant improvements in both model accuracy and compression.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental setup.
2. The proposed approach is novel and addresses an important problem in neural network weight parameterization.
3. The paper provides extensive experimental results on various datasets and architectures, demonstrating the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential directions for future research.
2. The authors should provide a more thorough analysis of the computational cost of the proposed method, especially in comparison to other state-of-the-art methods.
3. The paper could benefit from a more detailed discussion of the relationship between the proposed method and other related works in the field of neural network weight parameterization.

### Suggestions

The paper would benefit from a more in-depth discussion of the limitations of the proposed approach. Specifically, the authors should explore the sensitivity of the method to the choice of predictor network architecture and the distillation process. For instance, how does the performance vary when using different types of neural networks for the predictor, or when the distillation process is not well-tuned? A more detailed analysis of these factors would provide a clearer understanding of the robustness and generalizability of the proposed method. Furthermore, the authors should discuss the potential for the method to be applied to different types of neural network architectures beyond the ones presented in the paper. For example, how would the method perform on recurrent neural networks or graph neural networks? Addressing these questions would significantly enhance the paper's impact and practical relevance.

In addition to the limitations, the paper needs a more thorough analysis of the computational cost associated with the proposed method. While the paper demonstrates improved performance, it lacks a detailed comparison of the computational resources required by the proposed approach versus other state-of-the-art methods. The authors should provide a breakdown of the computational cost, including training time, memory usage, and inference time. This analysis should also consider the impact of different predictor network sizes and distillation strategies on the overall computational cost. A clear understanding of these trade-offs is crucial for practitioners to assess the practical applicability of the proposed method. Furthermore, the authors should discuss the scalability of the method to larger models and datasets. How does the computational cost scale with the size of the network and the dataset? Addressing these questions would provide a more complete picture of the method's efficiency and practicality.

Finally, the paper should include a more detailed discussion of the relationship between the proposed method and other related works in the field of neural network weight parameterization. The authors should clearly articulate how their approach differs from and builds upon existing methods. For example, how does the proposed method compare to techniques such as pruning, quantization, and knowledge distillation? A more comprehensive comparison would help to contextualize the contribution of the paper and highlight its unique advantages. Furthermore, the authors should discuss the potential for combining their method with other techniques to achieve even better performance. For instance, could the proposed method be combined with pruning or quantization to further reduce the model size and computational cost? Exploring these possibilities would provide a more complete understanding of the potential of the proposed method.

### Questions

1. How does the proposed method perform on larger and more complex datasets?
2. How does the proposed method compare to other state-of-the-art methods in terms of computational cost and efficiency?
3. What are the potential limitations of the proposed method, and how can they be addressed in future work?

### Rating

6

### Confidence

3

**********
