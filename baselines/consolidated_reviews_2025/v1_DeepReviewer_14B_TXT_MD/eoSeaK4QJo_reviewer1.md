### Summary

This paper proposes a novel pruning framework that combines unstructured weight pruning with unstructured neuron pruning, enhancing the energy efficiency of SNNs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The writing is clear and easy to understand.
2. The experiments are comprehensive, and the results are convincing.
3. The discussion on the energy consumption model is insightful.

### Weaknesses

#### Some Related Works


#### comment

1. This paper should clearly describe the differences between the proposed model and existing energy consumption models. Specifically, it needs to articulate what limitations or issues in previous models are being addressed and how this model offers a more effective solution. The current discussion lacks a detailed comparison of the assumptions, scope, and accuracy of the proposed model against established models, making it difficult to assess the novelty and impact of the work.
2. The paper should provide more explanation regarding the implementation of the method and the differences in hyperparameter settings compared to traditional methods. It is crucial to understand how the pruning strategy is integrated into the training process, including the specific optimization techniques used, and how these differ from standard training procedures. The lack of detail makes it challenging to reproduce the results and evaluate the practical applicability of the method.
3. The paper should include a discussion on the potential limitations of the proposed method and suggest directions for future research. This should include an analysis of the computational overhead of the pruning process, the sensitivity of the method to different network architectures, and the potential for further optimization. Without this, it is difficult to assess the robustness and generalizability of the proposed approach.

### Suggestions

To address the lack of clarity regarding the energy consumption model, the paper should include a detailed comparative analysis with existing models. This analysis should not only highlight the differences in the mathematical formulations but also discuss the underlying assumptions and the specific scenarios where each model is most applicable. For instance, the paper should discuss whether existing models fail to account for the sparsity introduced by pruning, or if they make simplifying assumptions about the hardware architecture that limit their accuracy. A table summarizing the key features of each model, including their strengths and weaknesses, would be beneficial. Furthermore, the paper should provide a more in-depth explanation of how the proposed model captures the energy savings achieved through unstructured pruning, and how this is validated through experimental results. This would strengthen the claims of the paper and provide a more solid foundation for the proposed method.

Regarding the implementation details, the paper needs to provide a step-by-step description of how the pruning method is integrated into the training process. This should include a clear explanation of how the pruning masks are initialized, updated, and applied during training. The paper should also discuss the specific optimization techniques used to train the pruned network, and how these differ from standard training procedures. For example, it should clarify whether the pruning process is performed jointly with the weight optimization, or if it is a separate step. Furthermore, the paper should provide a detailed analysis of the hyperparameter settings used in the experiments, including the learning rate, batch size, and the parameters specific to the pruning method. A sensitivity analysis of these hyperparameters would also be valuable, as it would help to understand the robustness of the method and its applicability to different datasets and network architectures. The paper should also include a discussion of the computational cost of the pruning process, and how it compares to the cost of training the original network.

Finally, the paper should include a thorough discussion of the potential limitations of the proposed method. This should include an analysis of the computational overhead of the pruning process, the sensitivity of the method to different network architectures, and the potential for further optimization. For example, the paper should discuss whether the proposed method is applicable to recurrent SNNs, or if it is limited to feedforward networks. The paper should also explore the potential for combining the proposed method with other optimization techniques, such as quantization or knowledge distillation. Furthermore, the paper should suggest specific directions for future research, such as exploring the application of the method to different types of SNNs, or developing more efficient algorithms for pruning SNNs. This would help to position the work within the broader context of SNN research and highlight its potential for future impact.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
