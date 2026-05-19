### Summary

This paper studies the problem of data selection for pre-fine-tuning of large language models (LLMs). The goal is to select a subset of unlabeled data that is most relevant to the target task, such that fine-tuning on this subset improves the performance on the target task. The authors propose a novel approach called GOT-D (Gradients of Optimal Transport for Data Selection) that leverages optimal transport (OT) to measure the distance between the pre-training distribution and the target distribution. The key idea is to select data that minimizes the OT distance between the pre-training distribution and the target distribution, which is equivalent to maximizing the gradient of the OT distance with respect to the pre-training distribution. The authors prove the optimality of this approach under certain conditions and show that it can be efficiently computed using the dual formulation of OT. The authors evaluate their approach on various tasks, such as model detoxification, domain adaptation, and general language understanding, and show that it outperforms existing methods in terms of both effectiveness and efficiency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and organized, with a clear motivation, problem definition, and solution. The authors provide a thorough literature review and a detailed explanation of their method, including the theoretical analysis and the practical implementation.
- The paper proposes a novel and principled approach for data selection that is based on optimal transport, which is a well-established and powerful tool for measuring the distance between distributions. The authors also provide a theoretical justification for their approach, showing that it is optimal under certain conditions and that it can be efficiently computed using the dual formulation of OT.
- The paper evaluates their approach on various tasks and datasets, and shows that it outperforms existing methods in terms of both effectiveness and efficiency. The authors also provide a detailed analysis of their results, highlighting the strengths and limitations of their approach.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not discuss the limitations of their approach in detail, such as the sensitivity to the choice of the OT cost function, the regularization parameters, and the approximation methods. For example, how does the performance change when using different cost functions, such as the squared Euclidean distance or the cosine distance? How does the choice of the regularization parameters affect the stability and convergence of the OT computation? How does the approximation method affect the accuracy and efficiency of the data selection?
- The paper does not compare their approach with other data selection methods that are based on different criteria, such as diversity, representativeness, or uncertainty. For example, how does their approach compare with methods that select data based on the entropy of the model's predictions, or the distance of the data points from the decision boundary? How does their approach compare with methods that select data based on the diversity of the selected subset, or the representativeness of the selected subset with respect to the target distribution?
- The paper does not provide a clear explanation of how the selected data is used for fine-tuning. For example, what is the fine-tuning objective, the learning rate, and the number of epochs? How does the fine-tuning performance vary with different fine-tuning settings? How does the fine-tuning performance vary with different sizes of the selected subset?

### Suggestions

The paper would benefit from a more thorough investigation into the sensitivity of the proposed method to various hyperparameters and design choices. Specifically, the authors should explore the impact of different cost functions within the optimal transport framework, such as the squared Euclidean distance or cosine distance, and provide a rationale for their choice. Furthermore, a detailed analysis of how the regularization parameters affect the stability and convergence of the OT computation is needed. The authors should also investigate the trade-off between accuracy and efficiency when using approximation methods for OT, and provide guidelines for selecting appropriate approximation techniques based on the size of the dataset and the desired level of accuracy. This analysis should include empirical results demonstrating the effect of these choices on the final performance of the fine-tuned model.

In addition to the optimal transport based approach, the paper should include a comparison with other data selection methods that use different criteria. For instance, methods that select data based on the entropy of the model's predictions, or the distance of the data points from the decision boundary, should be considered. The authors should also compare their approach with methods that select data based on the diversity of the selected subset, or the representativeness of the selected subset with respect to the target distribution. This comparison should not only focus on the final performance of the fine-tuned model, but also on the computational cost and the interpretability of the selected data. A more comprehensive comparison would provide a better understanding of the strengths and weaknesses of the proposed method and its position relative to existing techniques.

Finally, the paper needs to provide more details on the fine-tuning process. The authors should clearly specify the fine-tuning objective, the learning rate, the number of epochs, and any other relevant hyperparameters. It is also important to analyze how the fine-tuning performance varies with different fine-tuning settings and different sizes of the selected subset. This analysis should include a discussion of the potential limitations of the proposed method, such as the possibility of overfitting to the selected subset or the sensitivity to the choice of the fine-tuning parameters. A more detailed explanation of the fine-tuning process would make the paper more reproducible and provide a better understanding of the practical implications of the proposed method.

### Questions

- How sensitive is your approach to the choice of the OT cost function, the regularization parameters, and the approximation methods? How do you choose these parameters in practice?
- How does your approach compare with other data selection methods that are based on different criteria, such as diversity, representativeness, or uncertainty? What are the advantages and disadvantages of your approach compared to these methods?
- How do you use the selected data for fine-tuning? What is the fine-tuning objective, the learning rate, and the number of epochs? How does the fine-tuning performance vary with different fine-tuning settings and different sizes of the selected subset?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
