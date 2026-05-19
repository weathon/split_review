### Summary

This paper investigates the impact of chunking, or the division of data into discrete chunks, on continual learning (CL) performance. The authors argue that the challenges associated with chunking have been relatively overlooked in the CL literature, despite their significant impact on learning outcomes. They demonstrate that CL methods do not effectively address the sub-problem of chunking, resulting in performance levels that are comparable to those achieved through plain SGD training in the absence of task shifts. The paper also delves into the reasons behind performance declines when learning occurs in chunks, highlighting the role of forgetting, which is often attributed to distribution shifts. To mitigate these issues, the authors propose a method based on per-chunk weight averaging, drawing insights from an analysis of the linear case. They show that this approach not only improves performance in the chunking setting but also generalizes to the full CL setting.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel perspective by focusing on the "chunking" problem within continual learning, highlighting an often-overlooked aspect that significantly impacts performance. This fresh angle provides a valuable contribution to the field.
2. The authors provide a thorough analysis of the impact of chunking on continual learning, backed by empirical evidence demonstrating the significance of the problem.
3. The paper is well-structured and clearly written, making complex concepts accessible to readers.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on empirical results and the analysis of the linear case to support its claims. However, it lacks a robust theoretical foundation that could provide deeper insights into the mechanisms at play. A more comprehensive theoretical framework could enhance the paper's contributions by offering a more generalized understanding of the chunking problem and the efficacy of the proposed weight averaging method. Specifically, the paper does not delve into the mathematical properties of the loss landscape and how chunking affects the optimization trajectory. A theoretical analysis could explore, for example, how the curvature of the loss function changes with different chunk sizes and how this impacts the convergence of the proposed weight averaging method. Furthermore, the paper lacks a formal analysis of the generalization error under the chunking setting, which would be beneficial to understand the performance limitations of the proposed method.
2. The paper's analysis and results are primarily based on experiments conducted on specific datasets and models. To strengthen the paper's conclusions, it would be beneficial to include a more diverse range of datasets and model architectures. This would help demonstrate the generalizability of the findings and ensure that the proposed methods are effective across different domains and model types. For example, the paper could include experiments on datasets with different characteristics, such as those with imbalanced classes or those with a larger number of classes. Additionally, the paper could explore the performance of the proposed method on different model architectures, such as transformers or recurrent neural networks, to ensure that the findings are not specific to the ResNet18 model used in the experiments.

### Suggestions

To address the lack of theoretical foundation, the authors should consider incorporating a more rigorous analysis of the optimization process under the chunking setting. This could involve analyzing the convergence properties of the proposed weight averaging method, perhaps by leveraging tools from optimization theory such as Lyapunov functions or gradient descent analysis. Specifically, the authors could investigate how the per-chunk weight averaging affects the effective learning rate and the stability of the optimization process. Furthermore, a theoretical analysis of the generalization error under the chunking setting would be beneficial. This could involve deriving bounds on the generalization error that take into account the chunk size and the number of chunks. Such an analysis would provide a more principled understanding of the performance limitations of the proposed method and could guide the development of more effective techniques for mitigating the negative effects of chunking.

To strengthen the empirical validation, the authors should expand their experiments to include a more diverse range of datasets and model architectures. This should include datasets with different characteristics, such as those with imbalanced classes, those with a larger number of classes, or those with different input modalities. Additionally, the authors should explore the performance of the proposed method on different model architectures, such as transformers or recurrent neural networks. This would help demonstrate the generalizability of the findings and ensure that the proposed methods are effective across different domains and model types. Furthermore, the authors should consider including experiments that compare the proposed method with other existing techniques for mitigating the negative effects of chunking, if such techniques exist. This would provide a more comprehensive evaluation of the proposed method and help to establish its advantages and limitations.

Finally, the authors should provide a more detailed analysis of the computational overhead of the proposed weight averaging method. While the method is presented as simple, it is important to quantify the additional computational cost compared to standard SGD. This analysis should include both the training time and the memory requirements. Furthermore, the authors should discuss the potential limitations of the proposed method, such as its sensitivity to the choice of the averaging parameter or its performance under different chunking strategies. This would provide a more balanced and comprehensive evaluation of the proposed method and help to guide future research in this area.

### Questions

1. Could the authors elaborate on the theoretical underpinnings of the proposed weight averaging method? Specifically, how does this method address the challenges posed by chunking from a theoretical standpoint, and what guarantees can be provided regarding its performance?
2. How does the performance of the proposed method scale with the complexity of the task or the diversity of the data? Are there any specific domains or types of tasks where the method is expected to be particularly effective or, conversely, less effective?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
