### Summary

The authors propose a secure distributed differentially private algorithm for training SVMs and softmax-activated single-layer perceptrons. The algorithm is based on local training of models followed by a secure sum aggregation of the models. The authors show that the objective function of the models is smooth and strongly convex, which implies that the average of the models converges to the centralized model. The authors also show utility guarantees for the proposed algorithm.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well written and easy to follow.
- The proposed algorithm is simple and easy to implement.
- The authors provide utility guarantees for the proposed algorithm.

### Weaknesses

#### Some Related Works

[1] Differentially private distributed learning with communication efficiency and non-convexity.

#### comment

 - The proposed algorithm is not very novel. The idea of secure aggregation is not new, and the paper does not provide any new insights into the design of the secure aggregation protocol.
- The paper does not compare the proposed algorithm with existing differentially private distributed learning algorithms, such as [1]. It is unclear how the proposed algorithm performs compared to existing algorithms in terms of accuracy, privacy, and communication efficiency.
- The paper does not provide a detailed discussion of the limitations of the proposed algorithm. For example, the paper does not discuss the impact of the number of users, the number of local iterations, and the privacy budget on the performance of the algorithm.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing differentially private distributed learning algorithms. Specifically, the authors should benchmark their approach against state-of-the-art methods, such as those employing secure aggregation protocols, across a range of datasets and privacy budgets. This comparison should not only focus on the final accuracy achieved but also consider the computational overhead, communication costs, and convergence rates. For instance, a detailed analysis of how the proposed algorithm scales with an increasing number of users and local iterations would be crucial to understand its practical applicability. Furthermore, the authors should investigate the impact of different data distributions on the performance of their algorithm, as non-IID data can significantly affect the convergence and accuracy of distributed learning methods. This analysis should include a discussion of the trade-offs between privacy and utility, and how these trade-offs are affected by the choice of hyperparameters.

To address the lack of novelty, the authors should clearly articulate the specific contributions of their work beyond the existing literature. While the idea of secure aggregation is not new, the authors could explore novel ways to integrate it into the distributed learning framework, or propose a new aggregation strategy that is tailored to the specific challenges of differentially private learning. For example, the authors could investigate the use of adaptive aggregation techniques that dynamically adjust the aggregation weights based on the sensitivity of the local models. This could potentially lead to improved convergence rates and better privacy guarantees. Additionally, the authors should provide a more detailed explanation of the theoretical underpinnings of their algorithm, including a rigorous analysis of the convergence properties and the privacy guarantees. This analysis should go beyond the existing results and provide new insights into the behavior of the proposed algorithm.

Finally, the paper needs a more comprehensive discussion of the limitations of the proposed algorithm. The authors should explicitly address the potential impact of various factors, such as the number of users, the number of local iterations, and the privacy budget, on the performance of the algorithm. For example, the authors could investigate how the convergence rate is affected by the number of users and the number of local iterations, and how the accuracy is affected by the privacy budget. This analysis should also include a discussion of the practical challenges of implementing the proposed algorithm in real-world scenarios, such as the communication overhead and the computational cost. By addressing these limitations, the authors can provide a more balanced and realistic assessment of the proposed algorithm and its potential for practical applications.

### Questions

Please see the weaknesses above.

### Rating

5

### Confidence

4

**********
