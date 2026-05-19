### Summary

This paper introduces Cyclic Neural Networks (Cyclic NNs), a novel architecture that departs from the traditional layer-by-layer design of ANNs. Inspired by biological neural networks, Cyclic NNs allow for flexible, cyclic connections between neurons, enhancing information flow and model expressiveness. The authors propose Graph Over Multi-layer Perceptron (GOMLP) as a concrete model based on this paradigm and validate its effectiveness through experiments on MNIST, NewsGroup, and IMDB datasets. The results demonstrate that Cyclic NNs, trained with the Forward-Forward algorithm, outperform traditional Back-Propagation trained models in most cases, showcasing the potential of cyclic structures and localized training in ANNs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a transformative design that departs from traditional ANN structures by allowing cyclic connections between neurons, which increases the flexibility and expressiveness of the model.

2. The introduction of localized training, where each neuron is optimized with its own local loss function, is a novel approach that frees the network from the need for Directed Acyclic Graph (DAG) dependencies.

3. The paper provides a comprehensive comparison of Cyclic NNs with traditional models, demonstrating superior performance on multiple datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough analysis of the computational complexity of Cyclic NNs compared to traditional ANNs. While the authors mention that the time complexity can be reduced in practice, a more detailed theoretical analysis and empirical evidence are needed to understand the scalability of the proposed model, especially with respect to the number of neurons and the connectivity density. It is unclear how the localized training impacts the overall training time when the network size increases, and whether the asynchronous updates introduce any overhead.

2. The paper does not provide a detailed discussion on the potential challenges and limitations of implementing Cyclic NNs in real-world applications. For instance, the paper does not address how the model would handle noisy or incomplete data, which is common in many real-world scenarios. Furthermore, the paper lacks a discussion on the robustness of the model to adversarial attacks, which is a critical consideration for practical deployment.

3. The paper could benefit from a more in-depth analysis of the impact of different graph structures on the performance of Cyclic NNs. While the authors experiment with different graph types, a more systematic exploration of how specific graph properties (e.g., average path length, clustering coefficient, degree distribution) affect the learning dynamics and final performance is missing. This analysis should include a discussion on how to choose the optimal graph structure for a given task.

### Suggestions

To strengthen the paper, the authors should provide a more rigorous analysis of the computational complexity of Cyclic NNs. This should include a theoretical analysis of the time and space complexity as a function of the number of neurons, the number of connections, and the number of propagation steps. The authors should also provide empirical evidence of the scalability of the model by conducting experiments with varying network sizes and connectivity densities. Furthermore, it would be beneficial to compare the training time of Cyclic NNs with traditional ANNs on the same hardware, using a consistent number of parameters. This analysis should also consider the impact of localized training and asynchronous updates on the overall training time. The authors should also investigate the potential overhead introduced by these updates and how they can be mitigated.

In addition, the authors should address the practical challenges of implementing Cyclic NNs in real-world applications. This should include a discussion on how the model handles noisy or incomplete data, and how it can be made more robust to adversarial attacks. The authors should also explore the potential of using techniques such as data augmentation or regularization to improve the robustness of the model. Furthermore, the paper should discuss the limitations of the current implementation and suggest potential solutions for addressing these limitations. For example, the authors could explore the use of more efficient data structures or algorithms to improve the scalability of the model. The authors should also consider the practical implications of the model's architecture, such as the need for specialized hardware or software.

Finally, the authors should conduct a more in-depth analysis of the impact of different graph structures on the performance of Cyclic NNs. This should include a systematic exploration of how specific graph properties affect the learning dynamics and final performance. The authors should also discuss how to choose the optimal graph structure for a given task, and provide guidelines for selecting the appropriate graph structure. This analysis should include a discussion on the trade-offs between different graph structures, such as the balance between connectivity and computational cost. The authors should also explore the potential of using adaptive graph structures that can change during training to improve the model's performance.

### Questions

1. How does the computational complexity of Cyclic NNs scale with the size of the network, and how does it compare to traditional ANNs in terms of training time and resource consumption?

2. What are the potential challenges in implementing Cyclic NNs in real-world applications, and how can they be addressed?

3. How does the choice of graph structure impact the performance of Cyclic NNs, and are there guidelines for selecting the optimal structure for a given task?

### Rating

5

### Confidence

3

**********
