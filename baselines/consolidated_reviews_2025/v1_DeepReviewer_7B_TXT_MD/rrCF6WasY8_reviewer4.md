### Summary

This paper introduces a secure distributed learning algorithm for training SVMs and softmax-activated single-layer perceptrons in a privacy-preserving manner. The algorithm leverages a secure sum protocol to aggregate locally trained models, ensuring differential privacy. The authors provide theoretical guarantees for the convergence of the algorithm and demonstrate its utility through experiments on CIFAR-10 and CIFAR-100 datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper addresses the important problem of privacy-preserving distributed learning, which is highly relevant in today's data-driven world.
- The theoretical analysis of the algorithm's convergence properties is thorough and provides a solid foundation for understanding its behavior.
- The paper is well-written and easy to follow, making it accessible to a wide audience.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not compare the proposed algorithm with existing differentially private distributed learning algorithms, such as DP-SGD-based federated learning. It is unclear how the proposed algorithm performs compared to existing algorithms in terms of accuracy, privacy, and communication efficiency.
- The paper does not provide a detailed discussion of the limitations of the proposed algorithm. For example, the paper does not discuss the impact of the number of users, the number of local iterations, and the privacy budget on the performance of the algorithm.

### Suggestions

The paper should include a more comprehensive comparison with existing differentially private distributed learning algorithms, such as DP-SGD-based federated learning. This comparison should not only focus on the final accuracy achieved but also consider the computational overhead, communication costs, and convergence rates. For instance, a detailed analysis of how the proposed algorithm scales with an increasing number of users and local iterations would be crucial to understand its practical applicability. Furthermore, the authors should investigate the impact of different data distributions on the performance of their algorithm, as non-IID data can significantly affect the convergence and accuracy of distributed learning methods. This analysis should include a discussion of the trade-offs between privacy and utility, and how these trade-offs are affected by the choice of hyperparameters. 

To address the lack of a detailed discussion on the limitations of the proposed algorithm, the authors should explicitly address the potential impact of various factors on the performance of the algorithm. For example, the authors should investigate how the convergence rate is affected by the number of users and the number of local iterations, and how the accuracy is affected by the privacy budget. This analysis should also include a discussion of the practical challenges of implementing the proposed algorithm in real-world scenarios, such as the communication overhead and the computational cost. For example, the authors could explore the trade-offs between communication efficiency and privacy guarantees, and how these trade-offs affect the overall performance of the algorithm. Furthermore, the authors should discuss the sensitivity of the algorithm to different hyperparameter settings and provide guidelines for selecting appropriate values for these parameters. 

Finally, the authors should provide a more in-depth analysis of the theoretical guarantees provided by their algorithm. While the paper mentions convergence, it would be beneficial to explore the convergence rate and provide a more detailed analysis of the factors that affect it. For example, the authors could investigate how the convergence rate is affected by the number of users, the number of local iterations, and the privacy budget. Furthermore, the authors should discuss the limitations of their theoretical analysis and identify potential areas for future research. This could include exploring alternative theoretical frameworks or developing tighter bounds on the convergence rate. A more thorough analysis of the theoretical guarantees would strengthen the paper and provide a more complete understanding of the proposed algorithm.

### Questions

- How does the proposed algorithm compare to existing differentially private distributed learning algorithms in terms of accuracy, privacy, and communication efficiency?
- What are the limitations of the proposed algorithm, and how do these limitations affect the practical performance of the algorithm?

### Rating

6

### Confidence

3

**********
