### Summary

This paper proposes a meta-learning method for learning classifiers from a limited number of labeled data given from multiple annotators. The method embeds each example in tasks to a latent space by using a neural network and constructs a probabilistic model for learning classifiers from the embedded data. The method also models the confusion matrices for annotators and adaptively learns them during the meta-learning process. The experimental results show that the proposed method outperforms the existing methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The proposed method is a meta-learning method for learning classifiers from a limited number of labeled data given from multiple annotators. The method embeds each example in tasks to a latent space by using a neural network and constructs a probabilistic model for learning classifiers from the embedded data. The method also models the confusion matrices for annotators and adaptively learns them during the meta-learning process.

- The experimental results show that the proposed method outperforms the existing methods.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is based on the EM algorithm, which requires a large number of iterations to converge. The paper does not provide a clear justification for the choice of the number of iterations used in the experiments, nor does it discuss the computational cost associated with this iterative process, which could be a significant limitation for practical applications.

- The paper does not provide a detailed analysis of the sensitivity of the method to the choice of hyperparameters, such as the learning rate, the architecture of the neural network used for embedding, and the prior parameters for the confusion matrices. This lack of analysis makes it difficult to assess the robustness and generalizability of the proposed method.

- The paper does not compare the proposed method with other state-of-the-art meta-learning algorithms for learning from multiple annotators. While the paper compares against several existing methods, it does not include comparisons with more recent and potentially stronger baselines, which could provide a more comprehensive evaluation of the proposed method's performance.

- The paper does not discuss the limitations of the proposed method, such as its performance under different types of noise or its sensitivity to the quality of the source tasks. A thorough discussion of these limitations would provide a more balanced and realistic assessment of the method's capabilities.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the EM algorithm, including the time complexity of each iteration and the overall training time. It would be beneficial to provide a comparison of the computational cost of the proposed method with other meta-learning algorithms. Furthermore, the paper should explore the impact of different numbers of iterations on the performance of the method and provide a rationale for the chosen number of iterations. This analysis should include a discussion of the trade-off between computational cost and accuracy.

To address the lack of hyperparameter sensitivity analysis, the paper should include a thorough investigation of the impact of different hyperparameter choices on the performance of the method. This analysis should include a systematic exploration of the parameter space, using techniques such as grid search or random search. The paper should also provide a discussion of the optimal hyperparameter settings for different datasets and tasks, as well as the sensitivity of the method to these settings. This analysis should also include a discussion of the impact of different neural network architectures for embedding, and the choice of activation functions and regularization techniques.

Finally, the paper should include a more comprehensive comparison with other state-of-the-art meta-learning algorithms for learning from multiple annotators. This comparison should include a discussion of the strengths and weaknesses of the proposed method compared to these baselines. The paper should also discuss the limitations of the proposed method, such as its performance under different types of noise or its sensitivity to the quality of the source tasks. This discussion should include an analysis of the scenarios where the proposed method is expected to perform well and the scenarios where it may not be suitable. The paper should also discuss potential avenues for future research to address these limitations.

### Questions

- What is the reason for the choice of the number of iterations of the EM algorithm?

- How sensitive is the proposed method to the choice of hyperparameters?

- How does the proposed method compare with other state-of-the-art meta-learning algorithms for learning from multiple annotators?

- What are the limitations of the proposed method?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
