### Summary

This paper proposes a differentially private distributed learning algorithm, where each user locally trains a model and then the server aggregates the models via a secure sum protocol. The paper studies two types of models: (1) SVMs with a smooth hinge loss, and (2) Softmax-activated single-layer perceptrons. The paper proves that the objective function of each type of model is smooth and strongly convex, which allows the average of the local models to converge to the global model. The paper also provides experimental results on CIFAR-10 and CIFAR-100 datasets to demonstrate the performance of the proposed algorithm.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper studies an interesting problem of differentially private distributed learning.
- The paper provides a comprehensive analysis of the proposed algorithm, including theoretical guarantees and experimental results.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works

[1] Differentially private distributed learning with communication efficiency and non-convexity.

#### comment

 - The proposed algorithm is not very novel. The idea of secure aggregation is not new, and the paper does not provide any new insights into the design of the secure aggregation protocol.
- The paper does not compare the proposed algorithm with existing differentially private distributed learning algorithms, such as [1]. It is unclear how the proposed algorithm performs compared to existing algorithms in terms of accuracy, privacy, and communication efficiency.
- The paper does not provide a detailed discussion of the limitations of the proposed algorithm. For example, the paper does not discuss the impact of the number of users, the number of local iterations, and the privacy budget on the performance of the algorithm.

### Suggestions

The paper should provide a more thorough comparison with existing differentially private distributed learning algorithms. Specifically, the authors should compare their algorithm with [1] and other relevant baselines in terms of accuracy, privacy, and communication efficiency. This comparison should be done on the same datasets and with the same experimental settings. The authors should also discuss the advantages and disadvantages of their algorithm compared to existing algorithms. For example, the authors should discuss whether their algorithm is more robust to non-IID data, or whether it is more communication efficient. The paper should also include a discussion of the computational cost of the proposed algorithm, and how it compares to the computational cost of existing algorithms.

The paper should also provide a more detailed discussion of the limitations of the proposed algorithm. For example, the authors should discuss how the performance of the algorithm is affected by the number of users, the number of local iterations, and the privacy budget. The authors should also discuss the impact of the data distribution on the performance of the algorithm. For example, the authors should discuss how the performance of the algorithm is affected by the degree of non-IID data. The authors should also discuss the limitations of the theoretical analysis, and how these limitations affect the practical performance of the algorithm. For example, the authors should discuss the assumptions made in the theoretical analysis, and how these assumptions may not hold in practice.

Finally, the paper should provide a more detailed explanation of the secure sum protocol used in the algorithm. The authors should discuss the security properties of the protocol, and how it ensures differential privacy. The authors should also discuss the computational cost of the protocol, and how it affects the overall performance of the algorithm. The authors should also discuss the limitations of the secure sum protocol, and how these limitations may affect the practical performance of the algorithm. For example, the authors should discuss the impact of the protocol on the communication cost and the computational cost.

### Questions

- How does the proposed algorithm compare to existing differentially private distributed learning algorithms in terms of accuracy, privacy, and communication efficiency?
- What are the limitations of the proposed algorithm, and how do these limitations affect the practical performance of the algorithm?

### Rating

5

### Confidence

4

**********
