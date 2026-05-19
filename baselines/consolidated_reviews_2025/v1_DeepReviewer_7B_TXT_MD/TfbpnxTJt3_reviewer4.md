### Summary

The paper addresses the challenge of learning with local openset noisy labels in federated learning. The authors propose a novel framework, FedDPCont, which generates openset labels via globally shared private contrastive labels to avoid overfitting to noisy labels. The privacy of the shared contrastive labels is protected by label differential privacy (DP). The authors also provide theoretical guarantees for the proposed method. Experiments on both benchmark datasets and practical datasets demonstrate the effectiveness of FedDPCont.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper addresses a novel and practical problem of learning with local openset noisy labels in federated learning.
2. The authors propose a novel framework, FedDPCont, which generates openset labels via globally shared private contrastive labels to avoid overfitting to noisy labels.
3. The privacy of the shared contrastive labels is protected by label differential privacy (DP).
4. The authors provide theoretical guarantees for the proposed method.
5. Experiments on both benchmark datasets and practical datasets demonstrate the effectiveness of FedDPCont.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion on the limitations of the proposed method and potential future research directions. Specifically, the paper does not address the potential impact of the privacy mechanism on the utility of the model, or the sensitivity of the method to the choice of hyperparameters. It would be beneficial to explore the trade-offs between privacy and accuracy more thoroughly, and to discuss how the method might scale to larger and more complex datasets.
2. The paper does not provide a comprehensive comparison with existing methods for handling noisy labels in federated learning. While the authors mention that existing methods are not directly applicable, they do not provide a detailed analysis of why this is the case, or how their method compares to alternative approaches in terms of performance and computational cost. A more thorough comparison would help to contextualize the contribution of the proposed method and highlight its advantages and disadvantages.

### Suggestions

The authors should provide a more detailed analysis of the limitations of their proposed method, particularly concerning the privacy-utility trade-off. While differential privacy is a strong privacy guarantee, it can sometimes lead to a significant reduction in model accuracy. The paper should include experiments that systematically vary the privacy parameters (e.g., epsilon and delta) and analyze the impact on model performance. This analysis should not only focus on the final accuracy but also consider other metrics such as convergence speed and robustness to different types of noise. Furthermore, the authors should discuss the computational overhead introduced by the privacy mechanism and how it scales with the size of the dataset and the number of clients. It would be beneficial to explore alternative privacy mechanisms or techniques that could potentially reduce the impact on model utility while maintaining strong privacy guarantees.

In addition to the privacy-utility trade-off, the paper should also discuss the limitations of the proposed method in terms of its applicability to different types of datasets and tasks. The current experiments are limited to image classification tasks, and it is unclear how the method would perform on other types of data, such as text or time-series data. The authors should also discuss the sensitivity of the method to the choice of hyperparameters, such as the learning rate, the batch size, and the privacy parameters. A sensitivity analysis would help to identify the optimal hyperparameter settings for different datasets and tasks. Moreover, the authors should explore the potential for extending the method to handle more complex noise patterns, such as label-dependent noise or instance-dependent noise.

Finally, the paper should provide a more comprehensive comparison with existing methods for handling noisy labels in federated learning. While the authors mention that existing methods are not directly applicable, they do not provide a detailed analysis of why this is the case, or how their method compares to alternative approaches in terms of performance and computational cost. A more thorough comparison would help to contextualize the contribution of the proposed method and highlight its advantages and disadvantages. For example, the authors could compare their method with techniques that use robust loss functions or data augmentation to handle noisy labels. They could also compare their method with approaches that use meta-learning or transfer learning to adapt to noisy labels. This comparison should include both theoretical analysis and empirical results on a variety of datasets and tasks.

### Questions

1. How does the proposed method perform on datasets with different characteristics, such as larger datasets or datasets with more complex noise patterns?
2. How does the proposed method compare to existing methods for handling noisy labels in federated learning?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
