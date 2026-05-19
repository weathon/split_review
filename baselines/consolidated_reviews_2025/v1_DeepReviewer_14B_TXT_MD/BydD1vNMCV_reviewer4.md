### Summary

The paper proposes a stochastic variant of the deep neural network known as the stochastic neural network (StoNet). The authors show that the StoNet falls into the framework of statistical modeling. It not only enables us to address fundamental issues in deep learning, such as structure interpretability and uncertainty quantification, but also provides with us a platform for transferring the theory and methods developed for linear models to the realm of deep learning. Specifically, the authors show how the sparse learning theory with the Lasso penalty can be adapted to deep neural networks (DNNs) from linear models; establish that the sparse StoNet is consistent in network structure selection; and provides a recursive method to quantify the prediction uncertainty for the Stonet. Furthermore, the authors extend this result to the DNN by its asymptotic equivalence with the Stonet, showing that consistent sparse deep learning can be obtained by training a DNN with an appropriate Lasso penalty. Additionally, the authors propose to remodel the last hidden layer output and the target output of a well-trained DNN model using a Stonet on the validation dataset, and then assess the prediction uncertainty of the DNN model via the Stonet.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. 
2. The authors provide a novel approach to address fundamental issues in deep learning, such as structure interpretability and uncertainty quantification, by introducing a stochastic variant of deep neural networks, called stochastic neural networks (StoNet). 
3. The paper shows that the StoNet falls into the framework of statistical modeling, enabling the adaptation of theory and methods developed for linear models to deep learning. 
4. The authors demonstrate how the sparse learning theory with the Lasso penalty can be adapted to deep neural networks (DNNs) from linear models, establish that the sparse StoNet is consistent in network structure selection, and provide a recursive method to quantify the prediction uncertainty for the Stonet. 
5. The paper also extends this result to the DNN by its asymptotic equivalence with the Stonet, showing that consistent sparse deep learning can be obtained by training a DNN with an appropriate Lasso penalty. 
6. Additionally, the paper proposes to remodel the last hidden layer output and the target output of a well-trained DNN model using a Stonet on the validation dataset, and then assess the prediction uncertainty of the DNN model via the Stonet.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed comparison of the proposed method with other existing methods for addressing the issues of structure interpretability and uncertainty quantification in deep learning. It would be beneficial to include a comprehensive comparison with other methods to highlight the advantages and limitations of the proposed approach.
2. The paper does not discuss the computational complexity of the proposed method. It is important to analyze the computational cost of training and inference using the StoNet, especially when compared to traditional deep learning models. This analysis should include the time and memory requirements for both training and inference phases.
3. The paper lacks a thorough discussion on the sensitivity of the StoNet to the choice of hyperparameters, such as the noise variance and the regularization parameters. It is crucial to understand how these parameters affect the performance and stability of the model. A sensitivity analysis should be included to guide practitioners in selecting appropriate values for these hyperparameters.

### Suggestions

The paper would benefit from a more detailed comparison with existing methods for structure interpretability and uncertainty quantification in deep learning. Specifically, the authors should compare their approach with methods that directly address these issues, such as techniques based on attention mechanisms for interpretability or Bayesian neural networks for uncertainty quantification. A clear comparison should highlight the advantages and disadvantages of the proposed StoNet approach in terms of accuracy, computational cost, and interpretability. For example, the authors could compare the performance of StoNet with methods that use L1 regularization directly on the weights of a standard DNN, or with methods that employ dropout as a Bayesian approximation. This comparison should not only focus on quantitative metrics but also on qualitative aspects, such as the interpretability of the learned structures and the reliability of the uncertainty estimates.

Furthermore, a more thorough analysis of the computational complexity of the proposed StoNet method is needed. The authors should provide a detailed breakdown of the time and memory requirements for both the training and inference phases. This analysis should consider the impact of the network size, the number of layers, and the choice of hyperparameters on the computational cost. It would be beneficial to compare the computational complexity of StoNet with that of standard DNNs and other methods for uncertainty quantification. For instance, the authors could analyze the number of operations required for a single forward and backward pass in both StoNet and a standard DNN, and discuss how the introduction of stochasticity affects the computational cost. This analysis should also include the memory requirements for storing the network parameters and intermediate activations, which can be a limiting factor for large-scale applications.

Finally, the paper should include a sensitivity analysis of the StoNet to the choice of hyperparameters, such as the noise variance and the regularization parameters. The authors should investigate how these parameters affect the performance and stability of the model. This analysis should include a systematic exploration of the parameter space and provide guidelines for selecting appropriate values for these hyperparameters. For example, the authors could perform experiments with different values of the noise variance and regularization parameters and analyze their impact on the prediction accuracy, the sparsity of the learned network, and the quality of the uncertainty estimates. This analysis should also discuss the trade-offs between different parameter choices and provide recommendations for practitioners on how to tune these parameters for optimal performance.

### Questions

1. How does the proposed StoNet method compare to other existing methods for addressing the issues of structure interpretability and uncertainty quantification in deep learning?
2. What is the computational complexity of the proposed StoNet method compared to traditional deep learning models?
3. How sensitive is the StoNet to the choice of hyperparameters, such as the noise variance and the regularization parameters?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
