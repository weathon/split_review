### Summary

This paper studies the relationship between generalization ability of a neural network and the intrinsic dimension of its training dataset. The authors propose a new metric called label sharpness to measure the intrinsic dimension of the training set. The authors also show that the adversarial robustness of a neural network is positively correlated with the label sharpness. The authors conduct extensive experiments to validate their theoretical findings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a comprehensive review of related work and clearly state their contributions.
2. The authors propose a new metric called label sharpness to measure the intrinsic dimension of the training set. The authors also show that the adversarial robustness of a neural network is positively correlated with the label sharpness.
3. The authors conduct extensive experiments to validate their theoretical findings.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical results are based on some strong assumptions, such as the Lipschitz continuity of the loss function and the model. These assumptions may not hold in practice, and the authors do not provide any justification for why these assumptions are reasonable.
2. The authors claim that their theoretical results are based on the assumption that the model is well-trained, but they do not provide any empirical evidence to support this claim. It is unclear whether the theoretical results hold in practice when the model is not well-trained.
3. The authors use a simple linear model to estimate the intrinsic dimension of the training set, but they do not provide any justification for why this model is appropriate. It is unclear whether the results obtained using this model are reliable.
4. The authors do not provide any analysis of the computational complexity of their proposed method. It is unclear whether the method is computationally efficient.

### Suggestions

The paper introduces a novel metric, label sharpness, to measure the intrinsic dimension of a training set and explores its relationship with generalization and adversarial robustness. While the empirical results are promising, several aspects of the theoretical framework require further investigation. Specifically, the reliance on Lipschitz continuity for both the loss function and the model is a significant limitation. In practice, neural networks, especially those with non-smooth activation functions, may not satisfy this condition. The authors should explore the implications of relaxing this assumption or provide empirical evidence that the observed trends are robust to deviations from Lipschitz continuity. Furthermore, the assumption of a well-trained model is not adequately justified. The authors should provide empirical evidence demonstrating that their theoretical results hold for models that are not perfectly trained, perhaps by varying the training parameters or by using models with different levels of overfitting. This would make the theoretical results more applicable to real-world scenarios where perfect training is often not achievable.

The choice of a linear model for estimating intrinsic dimension also warrants further scrutiny. While linear methods are computationally efficient, they may not accurately capture the true underlying structure of the data, especially if the data lies on a non-linear manifold. The authors should compare the results obtained using linear methods with those obtained using more sophisticated techniques, such as manifold learning or fractal analysis. This would help to determine whether the choice of estimation method significantly affects the conclusions of the paper. Additionally, a more detailed analysis of the computational complexity of the proposed method is needed. The authors should provide a formal analysis of the time and space complexity of their method, including the cost of computing the Lipschitz constant and the intrinsic dimension. This would help to assess the scalability of the method and its applicability to large datasets. It would also be beneficial to explore potential optimizations or approximations that could reduce the computational burden.

Finally, the paper would benefit from a more thorough discussion of the limitations of the proposed metric and its applicability to different types of datasets. The authors should acknowledge that label sharpness may not be a universal measure of intrinsic dimension and that its interpretation may depend on the specific characteristics of the dataset. They should also discuss the potential biases that may be introduced by the choice of the linear model for estimating intrinsic dimension. Furthermore, it would be valuable to explore the relationship between label sharpness and other measures of intrinsic dimension, such as the doubling dimension or the Assouad dimension. This would provide a more comprehensive understanding of the proposed metric and its place within the broader context of dimensionality estimation.

### Questions

See the weakness above.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
