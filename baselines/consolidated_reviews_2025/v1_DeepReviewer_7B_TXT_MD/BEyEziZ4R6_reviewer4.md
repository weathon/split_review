### Summary

This paper proposes a new method to train differentially private neural networks without per-sample gradient clipping. The authors leverage Lipschitz constrained networks, which are neural networks whose parameter-wise gradients are bounded by a constant, ideally 1. The paper provides a Python package that enforces Lipschitz constraints in practice and demonstrates the effectiveness of the proposed method on several datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper addresses an important problem in differentially private learning, which is the computational cost and memory usage associated with per-sample gradient clipping. The proposed method is novel and provides a new approach to train differentially private neural networks without per-sample gradient clipping. The paper is well-written and easy to follow, with clear explanations of the proposed method and its theoretical foundations. The authors provide a comprehensive analysis of the proposed method, including theoretical guarantees and empirical evaluations. The paper also includes a Python package that enforces Lipschitz constraints in practice, which can be used by other researchers in the field.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to other differentially private learning methods. While the authors claim that their method is more efficient than per-sample gradient clipping, they do not provide any empirical evidence to support this claim. It would be beneficial to include a more thorough analysis of the computational cost of the proposed method, including the time and memory requirements for training and inference. The paper also does not discuss the limitations of the proposed method, such as its applicability to different types of neural networks or its performance on different datasets. It is unclear whether the proposed method can be applied to other types of neural networks, such as recurrent neural networks or transformers, and how it performs on datasets with different characteristics. The paper also does not provide a detailed comparison of the proposed method with other differentially private learning methods, such as those that use gradient compression or quantization. It would be beneficial to include a more thorough comparison of the proposed method with other differentially private learning methods, including a discussion of the advantages and disadvantages of each method.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their proposed method, including a comparison with other differentially private learning methods. This analysis should include not only the training time but also the memory usage and the number of floating-point operations. It would be beneficial to include experiments with different network architectures and dataset sizes to demonstrate the scalability of the proposed method. Furthermore, the authors should discuss the limitations of their method, such as its applicability to different types of neural networks and its performance on different datasets. Specifically, they should investigate whether the proposed method can be applied to other types of neural networks, such as recurrent neural networks or transformers, and how it performs on datasets with different characteristics. This would help to clarify the scope of the proposed method and identify potential areas for future research. Finally, the authors should provide a more detailed comparison of their method with other differentially private learning methods, including a discussion of the advantages and disadvantages of each method. This comparison should include a discussion of the trade-offs between privacy, accuracy, and computational cost.

To further strengthen the paper, the authors should consider including a more in-depth analysis of the theoretical properties of their proposed method. This analysis should include a discussion of the convergence properties of the method and its sensitivity to the choice of hyperparameters. It would also be beneficial to provide a more detailed explanation of the Lipschitz constant estimation method and its impact on the overall performance of the method. The authors should also discuss the potential limitations of their method, such as the assumption that the Lipschitz constant is known or can be estimated accurately. This would help to provide a more complete picture of the proposed method and its potential limitations. Additionally, the authors should consider including a discussion of the potential for future research, such as the development of more efficient algorithms for computing the Lipschitz constant or the application of the proposed method to other types of neural networks.

Finally, the authors should consider providing more details about the implementation of their proposed method, including the specific algorithms used for computing the Lipschitz constant and the gradient clipping. This would help to make the method more accessible to other researchers in the field and facilitate the reproducibility of the results. The authors should also provide a more detailed explanation of the experimental setup, including the specific datasets used and the hyperparameters used for training. This would help to ensure that the results are reproducible and that the method can be easily applied to other problems. It would also be beneficial to include a more detailed discussion of the potential limitations of the experimental setup and how these limitations might affect the results.

### Questions

How does the proposed method compare to other differentially private learning methods in terms of computational cost and memory usage?

What are the limitations of the proposed method, and how can they be addressed in future work?

How does the proposed method perform on different types of neural networks and datasets?

### Rating

6

### Confidence

3

**********
