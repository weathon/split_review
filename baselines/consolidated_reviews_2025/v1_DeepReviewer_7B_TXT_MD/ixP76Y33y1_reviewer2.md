### Summary

This paper studies the relationship between the generalization ability of a neural network and the intrinsic dimension of its training set. The authors propose a new metric called label sharpness to measure the intrinsic dimension of the training set, and show that the generalization ability of a neural network is negatively correlated with the label sharpness. The authors also show that the adversarial robustness of a neural network is positively correlated with the label sharpness. The authors conduct extensive experiments to validate their theoretical findings.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow. The authors provide a comprehensive review of related work and clearly state their contributions.
- The authors propose a new metric called label sharpness to measure the intrinsic dimension of the training set, and show that the generalization ability of a neural network is negatively correlated with the label sharpness. The authors also show that the adversarial robustness of a neural network is positively correlated with the label sharpness.
- The authors conduct extensive experiments to validate their theoretical findings.

### Weaknesses

#### Some Related Works


#### comment

 - The theoretical results are based on some strong assumptions, such as the Lipschitz continuity of the loss function and the model. These assumptions may not hold in practice, and the authors do not provide any justification for why these assumptions are reasonable.
- The authors claim that their theoretical results are based on the assumption that the model is well-trained, but they do not provide any empirical evidence to support this claim. It is unclear whether the theoretical results hold in practice when the model is not well-trained.
- The authors use a simple linear model to estimate the intrinsic dimension of the training set, but they do not provide any justification for why this model is appropriate. It is unclear whether the results obtained using this model are reliable.
- The authors do not provide any analysis of the computational complexity of their proposed method. It is unclear whether the method is computationally efficient.

### Suggestions

The paper's theoretical framework relies on several strong assumptions that need further justification. Specifically, the Lipschitz continuity of the loss function and the model is a significant constraint. While this assumption might hold for some simple loss functions, it is unlikely to be true for complex neural networks, especially those with non-smooth activation functions or when dealing with high-dimensional data. The authors should explore the implications of relaxing these assumptions or provide empirical evidence that these assumptions are not too restrictive in practice. For example, they could investigate how the theoretical bounds change when using different activation functions or when the data is not uniformly distributed. Furthermore, the assumption of a well-trained model is not well-supported. The authors should provide empirical evidence that their theoretical results hold when the model is not perfectly trained, perhaps by varying the training parameters or by using models with different levels of overfitting. This would make the theoretical results more applicable to real-world scenarios.

The use of a linear model to estimate intrinsic dimension is also a potential weakness. While linear methods are computationally efficient, they might not accurately capture the true underlying structure of the data, especially if the data lies on a non-linear manifold. The authors should consider using more sophisticated methods for estimating intrinsic dimension, such as methods based on manifold learning or fractal analysis. They should also provide a comparison of the results obtained using different methods to assess the robustness of their findings. For example, they could compare the intrinsic dimension estimates obtained using linear methods with those obtained using non-linear methods. This would help to determine whether the choice of estimation method significantly affects the conclusions of the paper. Additionally, the authors should provide a more detailed analysis of the computational complexity of their proposed method. While they mention that the intrinsic dimension estimation is fast, they do not provide a formal analysis of the time and space complexity of their method. This analysis should include the cost of computing the Lipschitz constant and the intrinsic dimension, as well as the cost of training the neural network. This would help to assess the scalability of the method and its applicability to large datasets.

Finally, the authors should provide more details about the experimental setup. For example, they should specify the exact architectures of the neural networks used, the optimization algorithms, and the hyperparameters. They should also provide more details about the datasets used, such as the size, dimensionality, and class distribution. This would make it easier for other researchers to reproduce their results and to compare their findings with other studies. Furthermore, the authors should provide a more detailed analysis of the experimental results. For example, they should investigate how the generalization ability of the neural network varies with the label sharpness for different datasets and model architectures. They should also investigate the relationship between the adversarial robustness and the label sharpness for different attack methods. This would help to provide a more comprehensive understanding of the relationship between these concepts.

### Questions

- Could the authors provide any empirical evidence to support the claim that the theoretical results hold when the model is not well-trained?
- Could the authors provide any justification for why the Lipschitz continuity of the loss function and the model is a reasonable assumption?
- Could the authors provide any analysis of the computational complexity of their proposed method?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
