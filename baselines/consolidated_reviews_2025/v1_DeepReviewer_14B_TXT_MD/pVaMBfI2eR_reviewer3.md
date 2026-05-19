### Summary

This paper proposes a novel federated learning method, Federated Dual Prompt Tuning (Fed-DPT), to address the challenges of domain shift and communication efficiency. The method combines CLIP and prompt learning techniques for both visual and textual inputs, enhancing parameter efficiency and minimizing communication costs. Fed-DPT introduces domain-specific prompts and facilitates correlations between visual and textual representations through self-attention mechanisms. The paper demonstrates the effectiveness of Fed-DPT through extensive experiments on three benchmark datasets, showing significant improvements over existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel Federated Dual Prompt Tuning (Fed-DPT) method that addresses the challenges of domain shift and communication efficiency in federated learning. The combination of CLIP and prompt learning techniques for both visual and textual inputs is innovative and enhances parameter efficiency while minimizing communication costs.

2. The paper is well-structured and clearly presents the problem, the proposed solution, and the experimental results. The use of figures and tables effectively illustrates the concepts and findings.

3. The experimental results demonstrate the effectiveness of Fed-DPT, showing significant improvements over existing methods on three benchmark datasets. The ablation studies provide valuable insights into the contributions of different components of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential future research directions. Specifically, the paper does not address the potential impact of highly heterogeneous domain shifts, where the visual and textual prompt tokens might not generalize well across all clients. Furthermore, the paper lacks a discussion on the computational overhead of the proposed method, especially when dealing with a large number of clients and complex models.

2. The paper could provide more details on the implementation of the proposed method, such as the specific choices of hyperparameters and the computational resources required for training. For example, the paper does not specify the learning rate, batch size, and optimizer used for training the prompt tokens. Additionally, the paper lacks information on the hardware specifications used for the experiments, making it difficult to reproduce the results.

3. The paper could include a more comprehensive comparison with other state-of-the-art methods in federated learning and domain adaptation. While the paper compares with some existing methods, it does not include a comparison with other prompt-based federated learning methods or domain adaptation techniques that could provide a more complete picture of the performance of the proposed method. The comparison could also benefit from including metrics beyond accuracy, such as communication cost and convergence speed.

### Suggestions

To enhance the paper, the authors should delve deeper into the limitations of Fed-DPT, particularly concerning the generalization of prompt tokens under extreme domain shifts. It would be beneficial to analyze scenarios where the visual and textual domains of different clients are vastly different, potentially leading to negative transfer. For instance, if one client has images of natural scenes while another has medical images, the shared prompt tokens might not be effective. The authors could explore adaptive prompt learning strategies that allow for client-specific prompt adjustments based on the local data distribution. This could involve techniques like meta-learning or reinforcement learning to dynamically tune the prompts. Furthermore, the paper should include a discussion on the computational complexity of Fed-DPT, especially in terms of the number of clients and the size of the models. This analysis should consider the memory and time requirements for training and inference, providing a more complete picture of the method's practicality.

To improve the reproducibility of the results, the authors should provide a detailed description of the implementation details. This includes specifying the exact hyperparameters used for training, such as the learning rate, batch size, optimizer, and the number of training epochs. The authors should also provide information on the hardware specifications used for the experiments, such as the type of GPUs, the amount of memory, and the CPU model. Furthermore, the authors should consider releasing the source code of Fed-DPT to facilitate further research and development in this area. This would allow other researchers to easily replicate the results and build upon the proposed method. The paper should also include a sensitivity analysis of the hyperparameters to understand their impact on the performance of Fed-DPT. This analysis would provide valuable insights into the robustness of the method and help practitioners to choose appropriate hyperparameters for their specific applications.

Finally, the authors should expand the comparison with other state-of-the-art methods in federated learning and domain adaptation. This should include a comparison with other prompt-based federated learning methods, as well as domain adaptation techniques that are not based on prompt learning. The comparison should also include metrics beyond accuracy, such as communication cost, convergence speed, and the number of parameters that need to be communicated. This would provide a more comprehensive evaluation of the performance of Fed-DPT and help to identify its strengths and weaknesses compared to other methods. The authors could also consider using a wider range of datasets to evaluate the generalization ability of Fed-DPT across different domains and tasks. This would provide a more robust assessment of the method's performance and help to identify potential limitations.

### Questions

1. How does the performance of Fed-DPT compare to other state-of-the-art methods in federated learning and domain adaptation?
2. What are the potential limitations of Fed-DPT, and how can they be addressed in future research?
3. How does the choice of hyperparameters affect the performance of Fed-DPT, and what are the optimal values for different datasets and tasks?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
