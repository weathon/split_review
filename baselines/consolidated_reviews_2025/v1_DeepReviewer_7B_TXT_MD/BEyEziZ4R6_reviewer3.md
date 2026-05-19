### Summary

This paper proposes a new method to train differentially private neural networks without per-sample gradient clipping. The authors introduce a method that leverages Lipschitz constrained networks, which are neural networks whose parameter-wise gradients are bounded by a constant, ideally 1. This approach allows for the computation of the Lipschitz constant of each layer with respect to its parameters, which can be used to estimate the sensitivity of the gradient computation queries. The authors demonstrate that this method can achieve privacy guarantees without the need for per-sample gradient clipping, which is a common technique in differentially private learning. The paper also provides a Python package that enforces Lipschitz constraints in practice and demonstrates the effectiveness of the proposed method on several datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow, with clear explanations of the proposed method and its theoretical foundations.
- The authors provide a comprehensive analysis of the proposed method, including theoretical guarantees and empirical evaluations.
- The proposed method is novel and addresses an important problem in differentially private learning, which is the computational cost and memory usage associated with per-sample gradient clipping.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method relies on the assumption that the Lipschitz constant of the neural network is known or can be estimated accurately. This assumption may not hold in practice, especially for complex neural networks, and the accuracy of the estimated Lipschitz constant can significantly impact the performance of the proposed method.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to other differentially private learning methods. While the authors claim that their method is more efficient than per-sample gradient clipping, they do not provide any empirical evidence to support this claim.
- The paper does not discuss the limitations of the proposed method, such as its applicability to different types of neural networks or its performance on different datasets. It is unclear whether the proposed method can be applied to other types of neural networks, such as recurrent neural networks or transformers, and how it performs on datasets with different characteristics.

### Suggestions

The authors should provide a more thorough analysis of the impact of the Lipschitz constant estimation on the performance of the proposed method. Specifically, they should investigate how the accuracy of the estimated Lipschitz constant affects the privacy-utility trade-off and the convergence of the training process. It would be beneficial to include experiments with different methods for estimating the Lipschitz constant and to analyze the sensitivity of the proposed method to the accuracy of the estimation. Furthermore, the authors should explore techniques to adaptively adjust the Lipschitz constant during training to improve the robustness of the method. This could involve using a dynamic Lipschitz constant that is updated based on the observed gradients or using a more sophisticated estimation method that takes into account the local geometry of the loss landscape.

To address the lack of computational cost analysis, the authors should provide a detailed comparison of the computational cost of their method with other differentially private learning methods. This comparison should include not only the training time but also the memory usage and the number of floating-point operations. The authors should also analyze the scalability of their method with respect to the size of the neural network and the dataset. It would be helpful to include experiments with different network architectures and dataset sizes to demonstrate the practical applicability of the proposed method. Furthermore, the authors should discuss the potential for optimizing the implementation of their method to reduce its computational cost. This could involve using more efficient algorithms for computing the Lipschitz constant or using parallel computing techniques to speed up the training process.

Finally, the authors should provide a more comprehensive discussion of the limitations of their method and its applicability to different types of neural networks and datasets. They should investigate whether the proposed method can be applied to other types of neural networks, such as recurrent neural networks or transformers, and how it performs on datasets with different characteristics. It would be beneficial to include experiments with different types of neural networks and datasets to demonstrate the generalizability of the proposed method. The authors should also discuss the potential challenges of applying their method to real-world problems and provide guidance on how to overcome these challenges. This could involve using domain-specific knowledge to adapt the method to the specific requirements of the problem or using techniques for data augmentation to improve the robustness of the method.

### Questions

- How does the proposed method compare to other differentially private learning methods in terms of computational cost and memory usage?
- What are the limitations of the proposed method, and how can they be addressed in future work?
- How does the proposed method perform on different types of neural networks and datasets?

### Rating

6

### Confidence

3

**********
