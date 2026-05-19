### Summary

The paper proposes Maestro, a method for training low-rank DNNs by progressively finding the optimal rank for each layer during training. The method is based on an extension of the ordered dropout method, and it includes a hierarchical group lasso penalty to enforce a nested structure in the ranks across layers. The paper provides theoretical results showing that the proposed method recovers SVD and PCA in specific cases. Empirically, Maestro is compared to other low-rank training methods and shows improved performance.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

- The proposed method is well-motivated and addresses an important problem in the field of deep learning. The idea of progressively finding the optimal rank for each layer during training is novel and interesting. 

- The paper provides theoretical results showing that the proposed method recovers SVD and PCA in specific cases. This is a valuable contribution that adds theoretical rigor to the paper.

- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works

[1] Pruning with pyknosese
[2] A simple and effective pruning approach for deep neural networks

#### comment

 - The paper lacks a detailed comparison with other pruning methods. While the paper compares Maestro to other low-rank training methods, it does not discuss how Maestro compares to pruning methods that remove unimportant weights after training. A detailed comparison with pruning methods would be valuable, especially since pruning methods can achieve high compression rates while maintaining accuracy. The paper should clarify whether Maestro is intended to be used as a training method or a post-training compression technique, and how it compares to pruning methods in both scenarios.

- The paper does not provide a detailed analysis of the computational cost of Maestro. While the paper mentions that Maestro is more efficient than other low-rank training methods, it does not provide a detailed analysis of the computational cost of the proposed method. The paper should provide a breakdown of the computational cost of each step of the algorithm, including the cost of finding the optimal rank for each layer and the cost of training the low-rank network. It would also be helpful to compare the computational cost of Maestro to other low-rank training methods and to standard training methods.

- The paper does not provide a detailed analysis of the memory cost of Maestro. While the paper mentions that Maestro is more efficient than other low-rank training methods, it does not provide a detailed analysis of the memory cost of the proposed method. The paper should provide a breakdown of the memory cost of each step of the algorithm, including the cost of storing the low-rank weights and the cost of computing the gradients. It would also be helpful to compare the memory cost of Maestro to other low-rank training methods and to standard training methods.

- The paper does not provide a detailed analysis of the sensitivity of Maestro to the choice of hyperparameters. The paper should provide a detailed analysis of the sensitivity of Maestro to the choice of hyperparameters, such as the learning rate, the batch size, and the rank of the low-rank approximation. It would also be helpful to provide guidelines for choosing the optimal hyperparameters for different datasets and architectures.

- The paper does not provide a detailed analysis of the robustness of Maestro to adversarial attacks. The paper should provide a detailed analysis of the robustness of Maestro to adversarial attacks. It would also be helpful to compare the robustness of Maestro to other low-rank training methods and to standard training methods.

### Suggestions

The paper should include a more thorough comparison with pruning methods, both as a post-training compression technique and as a method that can be used during training. The authors should clarify the specific scenarios where Maestro is most effective, and how it compares to pruning methods in terms of accuracy, compression rate, and computational cost. For example, the paper could include experiments where Maestro is used as a post-training compression method, where the network is first trained using standard methods and then compressed using Maestro. This would provide a more complete picture of the capabilities of Maestro and its potential advantages and disadvantages compared to pruning methods. The paper should also discuss the computational cost of Maestro during training, including the overhead of finding the optimal rank for each layer. A detailed breakdown of the computational cost of each step of the algorithm would be beneficial, as well as a comparison to other low-rank training methods.

Furthermore, the paper should provide a more detailed analysis of the memory cost of Maestro, including the cost of storing the low-rank weights and the cost of computing the gradients. The paper should also discuss the memory overhead of Maestro compared to standard training methods. The paper should also include a sensitivity analysis of Maestro to the choice of hyperparameters, such as the learning rate, the batch size, and the rank of the low-rank approximation. The paper should provide guidelines for choosing the optimal hyperparameters for different datasets and architectures. This analysis should include a discussion of how the performance of Maestro varies with different hyperparameter settings, and how to choose the hyperparameters to achieve the best performance. The paper should also include a discussion of the robustness of Maestro to adversarial attacks, and how it compares to other low-rank training methods and standard training methods. This analysis should include experiments where the network is attacked with adversarial examples, and the performance of Maestro is compared to other methods.

Finally, the paper should clarify the theoretical results presented in Section 3.3. The authors should provide a more detailed explanation of how the proposed method recovers SVD and PCA in the specific cases considered. The paper should also discuss the limitations of the theoretical results and the conditions under which they hold. The paper should also provide a more detailed explanation of the connection between the proposed method and the Ordered Dropout method, and how the proposed method extends the Ordered Dropout method. The paper should also provide a more detailed explanation of the hierarchical group lasso penalty and how it enforces a nested structure in the ranks across layers.

### Questions

- The paper mentions that Maestro is a training method that can be used to train low-rank DNNs. However, it does not discuss how Maestro compares to pruning methods that remove unimportant weights after training. Can Maestro be used as a post-training compression technique? If so, how does it compare to pruning methods in terms of accuracy, compression rate, and computational cost?

- The paper does not provide a detailed analysis of the computational cost of Maestro. Can the authors provide a breakdown of the computational cost of each step of the algorithm, including the cost of finding the optimal rank for each layer and the cost of training the low-rank network? How does the computational cost of Maestro compare to other low-rank training methods and to standard training methods?

- The paper does not provide a detailed analysis of the memory cost of Maestro. Can the authors provide a breakdown of the memory cost of each step of the algorithm, including the cost of storing the low-rank weights and the cost of computing the gradients? How does the memory cost of Maestro compare to other low-rank training methods and to standard training methods?

- The paper does not provide a detailed analysis of the sensitivity of Maestro to the choice of hyperparameters. How sensitive is Maestro to the choice of hyperparameters, such as the learning rate, the batch size, and the rank of the low-rank approximation? What guidelines can the authors provide for choosing the optimal hyperparameters for different datasets and architectures?

- The paper does not provide a detailed analysis of the robustness of Maestro to adversarial attacks. How robust is Maestro to adversarial attacks? How does the robustness of Maestro compare to other low-rank training methods and to standard training methods?

- The paper mentions that the proposed method is theoretically motivated, but it does not provide a detailed explanation of how the proposed method recovers SVD and PCA in the specific cases considered. Can the authors provide a more detailed explanation of the theoretical results presented in Section 3.3? What are the limitations of the theoretical results, and under what conditions do they hold?

- The paper mentions that the proposed method is an extension of the ordered dropout method. Can the authors provide a more detailed explanation of how the proposed method extends the ordered dropout method? How does the proposed method differ from the ordered dropout method, and what are the advantages of the proposed method over the ordered dropout method?

- The paper mentions that the hierarchical group lasso penalty enforces a nested structure in the ranks across layers. Can the authors provide a more detailed explanation of how the hierarchical group lasso penalty enforces a nested structure in the ranks across layers? How does the hierarchical group lasso penalty differ from other regularization methods that encourage sparsity in the ranks?

### Rating

5

### Confidence

3

**********
