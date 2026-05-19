### Summary

This paper addresses the challenge of federated learning with local openset noisy labels. The authors observe that existing solutions in the noisy label literature are ineffective during local training due to overfitting to noisy labels and being not generalizable to openset labels. To address the problems, the authors design a label communication mechanism that shares randomly selected "contrastive labels" among clients. The privacy of the shared contrastive labels is protected by label differential privacy (DP). Both the DP guarantee and the effectiveness of the approach are theoretically guaranteed. The experimental results on public benchmarks and real-world datasets demonstrate the efficiency of the proposed solution under various noise ratios and noise models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel framework, FedDPCont, to address the openset label noise problem, which builds on the idea of using globally shared private contrastive labels to avoid overfitting to local noisy labels. The idea is interesting and novel.
2. The paper provides theoretical guarantees for the privacy and effectiveness of the proposed approach. The authors prove that the gradient update of aggregating local loss with private labels is equivalent to the corresponding centralized loss. They also establish the robustness of their approach to label noise.
3. The paper conducts extensive experiments on public benchmarks and real-world datasets to demonstrate the effectiveness of the proposed solution. The results show that the proposed method outperforms existing approaches under various noise ratios and noise models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the label space is identical across different clients, which may not be the case in real-world scenarios. The authors should consider extending their work to handle the case where the label space differs across clients. This assumption is a significant limitation, as in many practical federated learning scenarios, clients may have access to different subsets of the overall label space. For instance, in a medical diagnosis scenario, different hospitals might specialize in different types of diseases, leading to varying label sets. The proposed method's reliance on a shared label space could severely limit its applicability in such heterogeneous settings.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be beneficial to compare the computational cost of the proposed method with existing approaches. The paper lacks a thorough discussion of the computational overhead introduced by the label communication mechanism and the contrastive loss calculation. A detailed analysis of the time and space complexity, especially in comparison to standard federated learning algorithms, is crucial for assessing the practical feasibility of the proposed method. The absence of such analysis makes it difficult to evaluate the trade-off between performance gains and computational costs.
3. The paper does not provide a detailed analysis of the scalability of the proposed method. It would be beneficial to investigate how the performance of the proposed method scales with the number of clients and the size of the dataset. The paper does not explore the impact of increasing the number of clients on the convergence rate and overall performance. It is important to understand how the method behaves with a large number of clients, as this is a common scenario in real-world federated learning deployments. Furthermore, the paper should investigate the impact of dataset size on the performance of the proposed method, as this can affect the generalizability of the results.

### Suggestions

The paper introduces an interesting approach to address the challenge of federated learning with noisy labels, but several aspects need further investigation to enhance its practical applicability and robustness. First, the assumption of identical label spaces across clients is a significant limitation. In real-world scenarios, clients may have vastly different data distributions and label sets. Future work should explore methods to handle heterogeneous label spaces, potentially by incorporating techniques from open-set learning or domain adaptation. For example, the method could be extended to allow clients to share information about their label spaces, enabling the server to better understand the overall label distribution and adapt the learning process accordingly. This could involve using techniques like prototype learning or meta-learning to learn representations that are robust to label space variations. Furthermore, the paper should investigate the impact of different levels of label space overlap on the performance of the proposed method. 

Second, a more detailed analysis of the computational complexity and communication overhead is needed. The paper should provide a breakdown of the time spent on local computations, communication, and other overheads. This analysis should compare the proposed method with existing federated learning algorithms, highlighting the trade-offs between accuracy and computational cost. Furthermore, the paper should investigate the impact of different communication strategies on the performance of the proposed method. For example, the authors could explore techniques like gradient compression or sparsification to reduce the communication overhead. This would be particularly important in scenarios with a large number of clients or limited bandwidth. The paper should also provide a detailed analysis of the memory requirements of the proposed method, especially when dealing with large datasets and a large number of clients.

Finally, the paper should include a more comprehensive experimental evaluation, including a sensitivity analysis of the hyperparameters and a scalability analysis with a varying number of clients. The sensitivity analysis should investigate the impact of different hyperparameter settings on the performance of the proposed method, providing practical guidance on parameter tuning. The scalability analysis should demonstrate how the performance of the method changes as the number of clients increases, especially in terms of convergence speed and final accuracy. This analysis should also consider the impact of client heterogeneity on the scalability of the method. The paper should also explore the impact of different noise ratios on the performance of the proposed method, providing a more comprehensive understanding of its robustness to label noise.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
