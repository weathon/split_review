### Summary

The paper proposes a meta-learning method for learning from multiple noisy annotators. The method embeds each example in tasks to a latent space by using a neural network and constructs a probabilistic model for learning classifiers from the embedded data. The method also models the confusion matrices for annotators and adaptively learns them during the meta-learning process. The experimental results show that the proposed method outperforms the existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The paper proposes a meta-learning method for learning from multiple noisy annotators.
3. The method embeds each example in tasks to a latent space by using a neural network and constructs a probabilistic model for learning classifiers from the embedded data.
4. The method also models the confusion matrices for annotators and adaptively learns them during the meta-learning process.
5. The experimental results show that the proposed method outperforms the existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed explanation of the neural network used for embedding. The paper mentions that a neural network is used to embed each example in tasks to a latent space, but it does not specify the architecture of the neural network, the activation functions, or the optimization algorithm used. This lack of detail makes it difficult to reproduce the results and understand the method's behavior. Furthermore, the paper does not discuss the sensitivity of the method to different neural network architectures or hyperparameters.
2. The paper does not provide a detailed explanation of the probabilistic model used for learning classifiers from the embedded data. The paper mentions that a probabilistic model is constructed, but it does not specify the form of the model, the likelihood function, or the prior distributions. This lack of detail makes it difficult to understand the method's assumptions and limitations. The paper also does not discuss the identifiability of the model parameters and the potential for overfitting.
3. The paper does not provide a detailed explanation of how the confusion matrices for annotators are modeled and learned. The paper mentions that the confusion matrices are modeled and adaptively learned, but it does not specify the form of the model, the learning algorithm, or the convergence properties. The paper also does not discuss the sensitivity of the method to different confusion matrix models or hyperparameters.
4. The paper does not provide a detailed explanation of the meta-learning process. The paper mentions that a meta-learning process is used, but it does not specify the meta-objective, the meta-learner, or the meta-optimization algorithm. The paper also does not discuss the sensitivity of the method to different meta-learning algorithms or hyperparameters.
5. The paper does not provide a detailed explanation of the experimental setup. The paper mentions that experiments are conducted on three datasets, but it does not specify the details of the datasets, the evaluation metrics, or the baselines. The paper also does not discuss the sensitivity of the method to different experimental settings or hyperparameters.
6. The paper does not provide a detailed explanation of the results. The paper mentions that the proposed method outperforms the existing methods, but it does not specify the statistical significance of the results, the effect sizes, or the limitations of the method. The paper also does not discuss the potential for overfitting or the generalizability of the method.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the neural network architecture used for embedding. The authors should specify the number of layers, the activation functions, the optimization algorithm, and the hyperparameters used. They should also discuss the rationale behind their choice of architecture and provide an ablation study to demonstrate the impact of different architectural choices on the performance of the method. Furthermore, the authors should discuss the sensitivity of the method to different neural network architectures and hyperparameters. For example, they could explore the impact of using different activation functions, such as ReLU or tanh, or different optimization algorithms, such as Adam or SGD. This would provide a more complete understanding of the method's behavior and allow for better reproducibility.

The paper should also provide a more detailed explanation of the probabilistic model used for learning classifiers from the embedded data. The authors should specify the form of the model, the likelihood function, and the prior distributions. They should also discuss the identifiability of the model parameters and the potential for overfitting. For example, they could discuss the use of regularization techniques or the choice of prior distributions to prevent overfitting. The authors should also provide a theoretical analysis of the model's properties, such as its convergence properties or its generalization bounds. This would provide a more rigorous understanding of the method's theoretical foundations and limitations. Furthermore, the authors should discuss the sensitivity of the method to different probabilistic model choices and hyperparameters.

Finally, the paper should provide a more detailed explanation of the meta-learning process. The authors should specify the meta-objective, the meta-learner, and the meta-optimization algorithm. They should also discuss the sensitivity of the method to different meta-learning algorithms and hyperparameters. For example, they could explore the impact of using different meta-optimizers, such as Adam or SGD, or different meta-objective functions. The authors should also discuss the computational cost of the meta-learning process and the scalability of the method to large datasets. Furthermore, the authors should provide a theoretical analysis of the meta-learning process, such as its convergence properties or its generalization bounds. This would provide a more rigorous understanding of the method's theoretical foundations and limitations.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
