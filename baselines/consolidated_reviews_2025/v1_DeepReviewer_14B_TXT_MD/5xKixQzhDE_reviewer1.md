### Summary

This paper proposes a new dataset condensation method aimed at hyperparameter search. It first formulates the data condensation for hyperparameter search in the HPO framework and then proposes the hyperparameter calibrated dataset condensation framework by using the equivalence relationship between preserving the performance ranking and the hypergradient alignment. The proposed method scales linearly with respect to the size of hyperparameter search space and the experiments demonstrate that the proposed framework effectively maintains the validation-performance rankings of models and speeds up hyperparameter/architecture search for image and graph tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The formulation of dataset condensation for hyperparameter search is interesting and novel.
2. The author shows that aligning the hyperparameter gradients is equivalent to preserving the performance ranking, which is a novel finding.
3. The author uses implicit differentiation and efficient inverse Hessian approximation to improve the efficiency.
4. The experiments for both image and graph data demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. As shown in Algorithm 1, it seems that the hyperparameters are updated by the hypergradient calculated by the entire validation set of the original dataset and the synthetic validation set. Since the synthetic validation set is a small set, the hypergradient calculated by it may not be very accurate. Although the author uses implicit differentiation and efficient inverse Hessian approximation to improve the efficiency, the computational cost of calculating the hypergradient for each hyperparameter in the validation set may still be very high. Specifically, the hypergradient calculation involves a Hessian inverse, which, even with approximations, can be computationally expensive, especially when the validation set is large. Furthermore, the accuracy of the hypergradient estimated from a small synthetic validation set is a concern, as it may not accurately reflect the true gradient landscape of the original validation set, potentially leading to suboptimal hyperparameter updates.

2. The author assumes that there exists a continuous extension of the search space and formulates an extended search space. However, many hyperparameters such as batch size, number of layers, and nodes are integers. It is unclear whether these hyperparameters can be continuously extended. The practical implications of this continuous extension, especially when dealing with discrete hyperparameters, are not fully explored. For instance, while learning rate can be continuously extended, it's not clear how the method handles the discrete nature of other hyperparameters and how the continuous relaxation impacts the final performance.

3. In the experiments, the author only tests the proposed method on small datasets such as CIFAR10, CIFAR100, Cora, Citeseer, etc. It is unclear whether the proposed method can be applied to large datasets such as ImageNet. The scalability of the proposed method to larger datasets is a significant concern, as the computational cost of hyperparameter optimization can increase dramatically with dataset size. The experiments should include a more diverse range of datasets, including larger ones, to demonstrate the general applicability of the method.

### Suggestions

The paper introduces an interesting approach to dataset condensation for hyperparameter optimization, but there are several areas where further clarification and investigation are needed. First, the computational cost of the proposed method needs to be addressed more thoroughly. While the authors mention using implicit differentiation and inverse Hessian approximation, the actual computational overhead of calculating hypergradients for each hyperparameter in the validation set, especially with a large number of hyperparameters, needs to be quantified. It would be beneficial to provide a detailed analysis of the computational complexity of the proposed method, including the time and memory requirements, and compare it with existing hyperparameter optimization techniques. Furthermore, the authors should explore alternative methods for approximating the hypergradients that may be more computationally efficient, such as using stochastic approximations or sampling techniques, to reduce the computational burden.

Second, the assumption of a continuous hyperparameter search space needs further justification and analysis. While continuous relaxation is a common technique, the paper should provide a more detailed discussion on how this assumption affects the optimization process, especially for discrete hyperparameters like batch size, number of layers, and nodes. The authors should investigate the impact of this continuous relaxation on the final performance and provide guidelines on how to choose appropriate continuous extensions for different types of hyperparameters. It would also be beneficial to explore alternative methods that can handle discrete hyperparameters directly, such as using combinatorial optimization techniques, to avoid the potential issues associated with continuous relaxation. The paper should also include experiments that compare the performance of the proposed method with and without continuous relaxation to demonstrate the impact of this assumption.

Finally, the experimental evaluation needs to be expanded to include larger and more diverse datasets. The current experiments are limited to small datasets, which may not accurately reflect the performance of the proposed method on real-world applications. The authors should include experiments on larger datasets, such as ImageNet, to demonstrate the scalability and generalizability of the method. Furthermore, the experiments should include a more diverse range of tasks and architectures to show the broad applicability of the proposed method. It would also be beneficial to compare the performance of the proposed method with other state-of-the-art hyperparameter optimization techniques on these larger datasets to provide a more comprehensive evaluation.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
