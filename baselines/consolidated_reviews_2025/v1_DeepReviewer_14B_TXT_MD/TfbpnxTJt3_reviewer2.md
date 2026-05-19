### Summary

This paper addresses the challenge of federated learning with local open-set noisy labels. The authors observe that existing solutions in the noisy label literature are ineffective in federated learning due to overfitting to noisy labels and the openset nature of the label space. To tackle this issue, the paper proposes a label communication mechanism that shares randomly selected "contrastive labels" among clients, with the privacy of these labels protected by label differential privacy. The paper provides theoretical guarantees for both the privacy and effectiveness of the proposed approach. Experimental results on public benchmarks and real-world datasets demonstrate the efficiency of the solution under various noise ratios and models.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper introduces a novel framework, FedDPCont, to address the openset label noise problem in federated learning. The idea of using globally shared private contrastive labels to prevent overfitting to local noisy labels is innovative and provides a new perspective on tackling this challenge.

2. The paper provides theoretical guarantees for the privacy and effectiveness of the proposed approach. The authors prove that the gradient update of aggregating local loss with private labels is equivalent to the corresponding centralized loss. They also establish the robustness of their approach to label noise.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the label space is identical across different clients, which may not be the case in real-world scenarios. The authors should consider extending their work to handle the case where the label space differs across clients. Specifically, the paper does not address the scenario where different clients might have completely disjoint sets of labels, which is a significant limitation in practical federated learning settings. The assumption of a shared, albeit noisy, label space is a strong one that limits the applicability of the proposed method.

2. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be beneficial to compare the computational cost of the proposed method with existing approaches. The analysis should include not only the overall complexity but also the communication overhead, which is a critical factor in federated learning. A breakdown of the time spent on local computations versus communication would be valuable.

3. The paper does not provide a detailed analysis of the scalability of the proposed method. It would be beneficial to investigate how the performance of the proposed method scales with the number of clients and the size of the dataset. The paper should include experiments with a varying number of clients to demonstrate the scalability of the approach. It is important to understand how the performance degrades as the number of clients increases, especially in terms of convergence speed and final accuracy.

4. The paper does not provide a detailed analysis of the sensitivity of the proposed method to hyperparameters. It would be beneficial to investigate how the performance of the proposed method varies with different hyperparameter settings. The paper should include a sensitivity analysis of the key hyperparameters, such as the learning rate, the number of communication rounds, and the parameters related to the differential privacy mechanism. This analysis is crucial for understanding the robustness of the method and for providing practical guidance on parameter tuning.

### Suggestions

The paper introduces an interesting approach to federated learning with noisy labels, but several aspects need further investigation to enhance its practical applicability and robustness. First, the assumption of identical label spaces across clients is a significant limitation. In real-world scenarios, clients may have vastly different data distributions and label sets. Future work should explore methods to handle heterogeneous label spaces, potentially by incorporating techniques from open-set learning or domain adaptation. For example, the method could be extended to allow clients to share information about their label spaces, enabling the server to better understand the overall label distribution and adapt the learning process accordingly. This could involve using techniques like prototype learning or meta-learning to learn representations that are robust to label space variations.

Second, a more detailed analysis of the computational complexity and communication overhead is needed. The paper should provide a breakdown of the time spent on local computations, communication, and other overheads. This analysis should compare the proposed method with existing federated learning algorithms, highlighting the trade-offs between accuracy and computational cost. Furthermore, the paper should investigate the impact of different communication strategies on the performance of the proposed method. For example, the authors could explore techniques like gradient compression or sparsification to reduce the communication overhead. This would be particularly important in scenarios with a large number of clients or limited bandwidth.

Finally, the paper should include a more comprehensive experimental evaluation, including a sensitivity analysis of the hyperparameters and a scalability analysis with a varying number of clients. The sensitivity analysis should investigate the impact of different hyperparameter settings on the performance of the proposed method, providing practical guidance on parameter tuning. The scalability analysis should demonstrate how the performance of the method changes as the number of clients increases, especially in terms of convergence speed and final accuracy. This analysis should also consider the impact of client heterogeneity on the scalability of the method. The paper should also explore the impact of different noise ratios on the performance of the proposed method, providing a more comprehensive understanding of its robustness to label noise.

### Questions

1. How does the proposed method handle the case where the label space differs across clients? Can the method be extended to handle this scenario?

2. What is the computational complexity of the proposed method compared to existing approaches? How does the computational cost scale with the number of clients and the size of the dataset?

3. How does the performance of the proposed method scale with the number of clients? Does the method perform well with a large number of clients?

4. How sensitive is the proposed method to hyperparameters? How does the performance vary with different hyperparameter settings?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
