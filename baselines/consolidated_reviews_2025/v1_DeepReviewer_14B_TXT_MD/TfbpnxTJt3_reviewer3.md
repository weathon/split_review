### Summary

This paper studies the problem of federated learning with local open-set noisy labels. The authors observe that existing noisy label solutions are ineffective in federated learning due to overfitting to noisy labels and being not generalizable to open-set labels. To address the problems, the authors design a label communication mechanism that shares randomly selected "contrastive labels" among clients. The privacy of the shared contrastive labels is protected by label differential privacy (DP). The authors also provide theoretical guarantees for the privacy and effectiveness of their approach. Experimental results on public benchmarks and real-world datasets demonstrate the efficiency of the proposed solution under various noise ratios and noise models.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper addresses an important and practical problem in federated learning, where local openset noisy labels can significantly impact the performance of the global model.
2. The authors provide a thorough analysis of the challenges posed by local openset noisy labels and motivate the need for a new approach.
3. The proposed label communication mechanism is novel and addresses the limitations of existing noisy label solutions in federated learning.
4. The authors provide theoretical guarantees for the privacy and effectiveness of their approach, which adds credibility to their work.
5. The experimental results on public benchmarks and real-world datasets demonstrate the efficiency of the proposed solution under various noise ratios and noise models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the label space is identical across different clients, which may not be the case in real-world scenarios. The authors should consider extending their work to handle the case where the label space differs across clients. Specifically, the current approach does not account for the possibility of clients having unique label sets, which is a common occurrence in federated learning. This limitation could significantly impact the applicability of the proposed method in practical settings where data heterogeneity is a major challenge.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be beneficial to compare the computational cost of the proposed method with existing approaches. The authors should provide a more rigorous analysis of the time and space complexity of their algorithm, especially in comparison to other federated learning algorithms. This analysis should consider the cost of the label communication mechanism and the impact of the contrastive loss function on the overall computational burden.
3. The paper does not provide a detailed analysis of the scalability of the proposed method. It would be beneficial to investigate how the performance of the proposed method scales with the number of clients and the size of the dataset. The authors should investigate the performance of their method with a larger number of clients and datasets of varying sizes. This analysis should include the impact of increasing the number of clients on the convergence rate and the overall performance of the model. It is also important to understand how the method performs with datasets of different sizes, as this can affect the practical applicability of the approach.

### Suggestions

The paper presents an interesting approach to address the problem of noisy labels in federated learning, but there are several areas where the work could be strengthened. First, the assumption of identical label spaces across clients is a significant limitation. In real-world federated learning scenarios, it is common for clients to have different label sets due to the heterogeneity of data sources. To address this, the authors could explore techniques such as open-set recognition or domain adaptation to handle the case where clients have unique label sets. This would involve modifying the label communication mechanism to account for the possibility of unseen labels and adapting the contrastive loss function to handle the open-set nature of the problem. Furthermore, the authors should consider incorporating techniques to handle the case where the label distributions across clients are imbalanced, as this can also impact the performance of the proposed method. 

Second, the paper lacks a detailed analysis of the computational complexity of the proposed method. The authors should provide a more rigorous analysis of the time and space complexity of their algorithm, especially in comparison to other federated learning algorithms. This analysis should consider the cost of the label communication mechanism and the impact of the contrastive loss function on the overall computational burden. Specifically, the authors should analyze the computational cost of the label perturbation and recovery process, as well as the cost of computing the contrastive loss. It would be beneficial to compare the computational cost of the proposed method with existing approaches, such as FedAvg and other noisy label learning algorithms. This analysis should also consider the impact of the number of clients and the size of the dataset on the computational cost of the proposed method. 

Finally, the paper should include a more detailed analysis of the scalability of the proposed method. The authors should investigate the performance of their method with a larger number of clients and datasets of varying sizes. This analysis should include the impact of increasing the number of clients on the convergence rate and the overall performance of the model. It is also important to understand how the method performs with datasets of different sizes, as this can affect the practical applicability of the approach. The authors should also consider the impact of client heterogeneity on the scalability of the method, as this can affect the convergence rate and the overall performance of the model. The authors should also investigate the impact of different noise ratios on the performance of the proposed method, as this can affect the robustness of the approach.

### Questions

1. How does the proposed method handle the case where the label space differs across clients? Can the method be extended to handle this scenario?
2. What is the computational complexity of the proposed method compared to existing approaches? How does the computational cost scale with the number of clients and the size of the dataset?
3. How does the performance of the proposed method scale with the number of clients? Does the method perform well with a large number of clients?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
