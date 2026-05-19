### Summary

This paper proposes a novel training framework, predictive differential training (PDT), based on the Koopman operator. The proposed method can predict the weights of the network in the next few steps and use these weights to accelerate the training process. The authors have conducted experiments on several different network architectures and datasets, which demonstrate the effectiveness of the proposed method.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The idea of using the Koopman operator to predict network weights in the next few steps is novel and interesting.
2. The authors have conducted experiments on several different network architectures and datasets, which demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the proposed method can accelerate the training process, but the speedup is not significant. For example, in Table 1, the training time of PDT is only 1-2 epochs faster than the baseline. Besides, the authors do not provide a comparison of the training time with other acceleration methods, such as learning rate scheduling. The lack of comparison against established acceleration techniques makes it difficult to assess the practical utility of the proposed method. A more thorough analysis should include comparisons with methods like cosine annealing or cyclical learning rates, which are commonly used for training acceleration.
2. The proposed method is based on the Koopman operator, which is a linear operator. However, the neural network training process is highly non-linear. Therefore, the prediction effect of the Koopman operator is limited, and it is hard to predict the training process in the long term. The authors do not provide a detailed analysis of the limitations of using a linear operator to approximate a non-linear process. Specifically, it is unclear how the method performs when the training trajectory deviates significantly from a linear path, which is likely to occur in the later stages of training or with more complex loss landscapes.
3. The authors do not provide the code for reproducibility.

### Suggestions

The authors should provide a more comprehensive evaluation of the proposed method's training acceleration capabilities. This should include a comparison against a wider range of established acceleration techniques, such as various learning rate schedules (e.g., cosine annealing, cyclical learning rates), momentum-based optimizers, and adaptive gradient methods. The comparison should not only focus on the number of epochs to convergence but also on the actual training time, considering the computational overhead of the proposed method. Furthermore, the authors should analyze the sensitivity of the method to different hyperparameter settings, such as the prediction horizon and the frequency of Koopman operator updates. A detailed ablation study would help to understand the contribution of each component of the proposed method and identify potential bottlenecks.

To address the limitations of using a linear operator for a non-linear process, the authors should provide a more in-depth analysis of the approximation error introduced by the Koopman operator. This analysis should include a discussion of the conditions under which the linear approximation is valid and the potential impact of non-linearities on the prediction accuracy. The authors could also explore techniques to mitigate the effects of non-linearities, such as using a moving window for the Koopman operator approximation or incorporating non-linear terms into the prediction model. Additionally, the authors should investigate the performance of the proposed method on more complex datasets and network architectures, where the non-linearities are likely to be more pronounced. This would provide a more realistic assessment of the method's practical applicability.

Finally, the authors should provide the code for reproducibility. This is essential for the scientific community to validate the results and build upon the proposed method. The code should be well-documented and easy to use, including clear instructions on how to reproduce the experiments presented in the paper. The authors should also consider releasing the code under an open-source license to facilitate further research and development. Without the code, it is difficult to assess the practical implementation details and the overall robustness of the proposed method.

### Questions

1. The authors claim that the proposed method can accelerate the training process, but the speedup is not significant. Besides, the authors do not provide a comparison of the training time with other acceleration methods, such as learning rate scheduling. How does the training time of the proposed method compare to these methods?
2. The proposed method is based on the Koopman operator, which is a linear operator. However, the neural network training process is highly non-linear. Therefore, the prediction effect of the Koopman operator is limited, and it is hard to predict the training process in the long term. How do the authors address this limitation?
3. The authors do not provide the code for reproducibility. Can the authors provide the code to reproduce the results?

### Rating

3

### Confidence

3

**********
