### Summary

The authors propose a novel dataset condensation algorithm that can be used to accelerate hyperparameter optimization. The authors propose to align the hypergradients of the original and the condensed dataset to preserve the performance ranking of the architectures. The authors show that the proposed method is efficient and can be used to accelerate hyperparameter optimization.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The authors propose a novel dataset condensation algorithm that can be used to accelerate hyperparameter optimization.
2. The authors show that the proposed method is efficient and can be used to accelerate hyperparameter optimization.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details on the experimental setup. Specifically, the paper lacks clarity on how the hyperparameters for the proposed method are chosen, and how they compare to the hyperparameters used in the baselines. The paper should also clarify the specific architecture and hyperparameter search space used for each dataset, as this significantly impacts the performance of hyperparameter optimization methods. It is unclear if the baselines were tuned using the same search space as the proposed method, which could lead to an unfair comparison.
2. The authors should provide more details on the computational cost of the proposed method. While the authors claim that the method is efficient, they do not provide a detailed analysis of the computational overhead associated with calculating the hypergradients and performing the dataset condensation. It is important to understand the scalability of the method with respect to the size of the dataset and the complexity of the model. The paper should include a breakdown of the time spent on different parts of the algorithm, such as gradient computation, dataset condensation, and hyperparameter optimization.

### Suggestions

The authors should provide a more detailed description of the experimental setup, including the specific hyperparameters used for the proposed method and the baselines. It is crucial to specify the search space for each hyperparameter, as this can significantly impact the performance of the methods. For example, if the proposed method uses a specific learning rate schedule, the authors should clearly state this and justify its choice. Furthermore, the authors should clarify whether the baselines were tuned using the same search space as the proposed method. If not, the comparison may be biased. The authors should also provide a detailed description of the architecture used for each dataset, including the number of layers, the number of units per layer, and the activation functions. This information is essential for reproducibility and for understanding the performance of the methods. The authors should also clarify how the hyperparameter search space was defined for each dataset, including the range of values for each hyperparameter and the method used to sample or explore the space.

To address the lack of clarity on computational cost, the authors should provide a detailed breakdown of the time spent on different parts of the algorithm. This should include the time spent on gradient computation, dataset condensation, and hyperparameter optimization. The authors should also analyze the scalability of the method with respect to the size of the dataset and the complexity of the model. For example, the authors could show how the runtime of the method scales with the number of training examples or the number of parameters in the model. This analysis should be performed on different datasets and with different model architectures to provide a comprehensive understanding of the computational cost of the method. The authors should also compare the computational cost of the proposed method with the baselines, to provide a clear picture of the trade-offs between performance and computational efficiency.

Finally, the authors should provide more details on the hypergradient matching process. Specifically, they should clarify how the hypergradients are calculated and how they are used to update the condensed dataset. The authors should also discuss the convergence properties of the proposed method and provide theoretical guarantees on the performance of the condensed dataset. It would be beneficial to include a visualization of the hypergradient matching process to provide a better understanding of how the method works. The authors should also discuss the limitations of the proposed method and suggest potential directions for future research.

### Questions

1. How did the authors choose the hyperparameters for the proposed method and the baselines?
2. How did the authors choose the architecture for each dataset?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
