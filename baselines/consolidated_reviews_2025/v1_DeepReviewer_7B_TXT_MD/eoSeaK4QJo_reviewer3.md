### Summary

This paper proposes a pruning framework that combines unstructured weight and neuron pruning to enhance the energy efficiency of SNNs. The authors argue that existing pruning methods do not fully exploit the sparsity of neuromorphic computing, and they introduce a novel approach that combines unstructured weight and neuron pruning to maximize energy savings. The paper presents a detailed analysis of the energy consumption of SNNs and designs a penalty term to address the ill-posed problem of combining weight and neuron pruning. Experimental results demonstrate the effectiveness of the proposed method in reducing energy consumption while maintaining comparable performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow, with a clear motivation and a well-structured methodology.
2. The authors provide a detailed analysis of the energy consumption of SNNs and design a penalty term to address the ill-posed problem of combining weight and neuron pruning. The proposed method is technically sound and innovative.
3. The experimental results demonstrate the effectiveness of the proposed method in reducing energy consumption while maintaining comparable performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of the proposed method and potential future directions.
2. The experiments are conducted on relatively small datasets and models. It would be beneficial to evaluate the proposed method on larger and more complex datasets and models to demonstrate its scalability and generalizability.
3. The paper does not provide a comparison with other state-of-the-art pruning methods for SNNs. It would be helpful to compare the proposed method with other pruning methods in terms of both performance and energy efficiency.

### Suggestions

The paper would benefit from a more thorough discussion of its limitations. Specifically, the authors should address the potential impact of their pruning method on the robustness of the SNNs. While the paper focuses on energy efficiency, it is crucial to understand if aggressive pruning might lead to a decrease in the model's ability to handle noisy inputs or adversarial examples. Furthermore, the authors should discuss the computational overhead associated with the proposed pruning method itself. While the inference energy is reduced, the process of identifying and removing neurons and weights might introduce additional computational costs, especially during training. A detailed analysis of this overhead would provide a more complete picture of the method's practical applicability. Finally, the authors should also consider the impact of their pruning method on the training time and convergence rate. While the paper focuses on post-training pruning, it would be beneficial to understand if the proposed method affects the initial training process of the SNN.

To strengthen the experimental evaluation, the authors should consider evaluating their method on larger and more complex datasets and models. While the current experiments on CIFAR-10 and ImageNet are valuable, it is important to demonstrate the scalability of the proposed method to more challenging scenarios. For instance, evaluating the method on datasets with higher resolution images or more complex tasks, such as object detection or segmentation, would provide a more comprehensive assessment of its generalizability. Additionally, the authors should explore the impact of different pruning ratios on the performance and energy efficiency of the model. A more detailed analysis of the trade-off between sparsity and accuracy would provide valuable insights for practical applications. It would also be beneficial to explore the impact of different pruning ratios on the energy consumption of the model. A more detailed analysis of the trade-off between sparsity and accuracy would provide valuable insights for practical applications.

Finally, the paper needs a more comprehensive comparison with existing state-of-the-art pruning methods for SNNs. The authors should compare their method with other pruning techniques, both structured and unstructured, in terms of both performance and energy efficiency. This comparison should include a detailed analysis of the advantages and disadvantages of each method. For example, the authors could compare their method with techniques that use magnitude-based pruning or gradient-based pruning. Furthermore, the authors should also consider comparing their method with other energy-efficient techniques for SNNs, such as quantization or pruning. This would help to position their method within the broader context of energy-efficient SNN research. A more thorough comparison would provide a clearer understanding of the novelty and effectiveness of the proposed method.

### Questions

1. How does the proposed method perform on larger and more complex datasets and models?
2. What are the limitations of the proposed method, and what are the potential future directions?
3. How does the proposed method compare with other state-of-the-art pruning methods for SNNs in terms of both performance and energy efficiency?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
