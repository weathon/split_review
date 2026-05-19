### Summary

This paper provides a theoretical guarantee for a permutation-based training method for ReLU networks. The authors prove that this method can approximate any one-dimensional continuous function, and they provide numerical results to validate the efficiency of this method in regression tasks. They also observe that permutation training can provide an innovative tool for describing network learning behavior.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and concise introduction to the problem and their proposed method. The theoretical results are presented in a rigorous and accessible manner, and the numerical results are clearly presented and analyzed.

2. The paper makes a significant contribution to the field of deep learning by providing a theoretical guarantee for a permutation-based training method. This is an important result, as it provides a theoretical foundation for a method that has been shown to be effective in practice.

3. The paper also makes a novel contribution by observing that permutation training can provide an innovative tool for describing network learning behavior. This is a new and interesting perspective on the problem of network learning, and it could lead to new insights into the behavior of neural networks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only considers the case of one-dimensional continuous functions. It is not clear if the results can be generalized to higher-dimensional functions. Specifically, the theoretical analysis relies on the ability to construct specific step function approximations using ReLU networks with permuted weights. This construction is highly dependent on the one-dimensional nature of the problem, and it is unclear how such a construction would be achieved in higher dimensions. The paper does not provide any discussion or analysis of the challenges involved in extending the theoretical results to higher dimensions, which is a significant limitation.

2. The paper only considers the case of ReLU networks. It is not clear if the results can be generalized to other types of neural networks. The theoretical proof relies on the specific properties of the ReLU activation function, such as its piecewise linearity and non-negativity. These properties are crucial for the construction of the step function approximations, and it is not obvious how these constructions would be adapted to other activation functions, such as sigmoid or tanh. The paper does not discuss the limitations of the ReLU activation function in the context of permutation-based training, nor does it provide any insights into how the results might be extended to other activation functions.

### Suggestions

The paper makes a valuable contribution by providing a theoretical foundation for permutation-based training in ReLU networks for one-dimensional continuous functions. However, the limitations regarding the dimensionality of the input and the type of activation function significantly restrict the practical applicability of the results. To address the issue of dimensionality, future work could explore alternative constructions for step function approximations in higher dimensions. This might involve investigating different network architectures or activation functions that are better suited for higher-dimensional data. For example, one could consider using convolutional layers or other specialized architectures that are designed to handle multi-dimensional inputs. Furthermore, it would be beneficial to analyze the complexity of the required network architecture as the dimensionality increases, and to investigate whether the permutation-based training method remains efficient in higher dimensions. It would also be useful to explore the use of techniques such as dimensionality reduction or feature mapping to project high-dimensional data onto a lower-dimensional space where the current theoretical results could be applied.

Regarding the limitation to ReLU networks, it would be important to investigate the behavior of permutation-based training with other activation functions. This could involve both theoretical analysis and empirical studies. For example, one could explore whether similar step function approximations can be constructed using sigmoid or tanh activations, and if so, what modifications to the theoretical proofs would be necessary. It would also be useful to compare the performance of permutation-based training with different activation functions on various benchmark datasets. This would provide insights into the practical trade-offs between different activation functions in the context of permutation-based training. Furthermore, it would be beneficial to analyze the impact of the activation function on the convergence properties of the training method and to investigate whether certain activation functions are more suitable for permutation-based training than others.

Finally, while the paper provides a theoretical guarantee for the approximation capabilities of permutation-based training, it would be valuable to explore the practical implications of these results. For example, it would be interesting to investigate whether the permutation-based training method can achieve better generalization performance compared to traditional training methods. It would also be useful to analyze the sensitivity of the method to different hyperparameter settings and to investigate how the choice of permutation affects the performance of the trained network. Furthermore, it would be beneficial to explore the use of permutation-based training in different application domains and to compare its performance with other state-of-the-art methods. This would provide a more comprehensive understanding of the strengths and limitations of the proposed method and would help to identify potential areas for future research.

### Questions

1. Can the results be generalized to higher-dimensional functions? If so, what are the key challenges in extending the results to higher dimensions?

2. Can the results be generalized to other types of neural networks? If so, what are the key challenges in extending the results to other types of neural networks?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
