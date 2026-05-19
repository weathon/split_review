### Summary

This paper presents a novel neural network architecture, Cyclic Neural Networks (Cyclic NNs), which departs from the traditional layer-by-layer, Directed Acyclic Graph (DAG) structure of most artificial neural networks (ANNs). Inspired by the complex, interconnected structure of biological neural networks, Cyclic NNs allow for neuron connections in any graph-like structure, including cycles. This flexibility is a significant departure from current ANN designs and could lead to more biologically realistic AI systems. The authors introduce the Graph Over Multi-layer Perceptron (GOMLP) as the first detailed model based on this new paradigm. They demonstrate the effectiveness of Cyclic NNs through experiments on widely tested datasets, showing that they outperform traditional DAG-based neural networks in most cases. The paper also highlights the Forward-Forward training algorithm's superior performance compared to the Back-Propagation algorithm when used with Cyclic NNs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a transformative design paradigm for ANNs that moves beyond the traditional layer-by-layer, DAG structure. This is a significant contribution to the field, as it opens up new possibilities for neural network architectures.
2. The introduction of Cyclic NNs, which allows for cycles in the network structure, is a novel concept that could lead to more biologically realistic AI systems.
3. The paper provides a detailed model, the Graph Over Multi-layer Perceptron (GOMLP), as a concrete example of the Cyclic NN design paradigm.
4. The experimental validation on widely tested datasets demonstrates the practical advantages of Cyclic NNs over traditional DAG-based neural networks.
5. The paper shows that the Forward-Forward training algorithm outperforms the Back-Propagation algorithm when used with Cyclic NNs, which is a significant finding.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of Cyclic NNs compared to traditional ANNs. This is important for understanding the practical implications of using Cyclic NNs in real-world applications. Specifically, the paper lacks a discussion on how the number of parameters and the computational cost scale with the size of the graph, which is crucial for assessing the feasibility of the proposed approach for large-scale problems. A comparison of the number of floating-point operations (FLOPs) required for both training and inference would be beneficial.
2. The paper does not discuss the potential challenges of implementing Cyclic NNs in hardware. This is an important consideration for the practical deployment of Cyclic NNs. For example, the paper does not address how the cyclic dependencies in the network would affect the parallelizability of the computations, which is a key factor in the efficiency of hardware implementations. Furthermore, the paper should discuss the memory access patterns and the potential bottlenecks that could arise from the graph-based structure.
3. The paper does not explore the potential of Cyclic NNs for other types of data or tasks beyond the datasets used in the experiments. This limits the understanding of the generalizability of the proposed approach. It would be beneficial to see experiments on tasks such as time-series forecasting, reinforcement learning, or natural language processing to assess the versatility of Cyclic NNs. The current experiments are limited to image classification and text classification, which may not fully capture the potential of the proposed architecture.

### Suggestions

To address the lack of computational complexity analysis, the authors should include a detailed theoretical analysis of the time and space complexity of Cyclic NNs. This analysis should consider the number of neurons, the number of connections, and the depth of the network. It would be beneficial to compare the computational cost of Cyclic NNs with that of traditional feedforward networks and recurrent networks. The authors should also provide empirical results on the training and inference time of Cyclic NNs on different hardware platforms. Furthermore, the authors should discuss the potential for optimizing the implementation of Cyclic NNs to reduce their computational cost. This could include techniques such as pruning, quantization, and knowledge distillation. A clear understanding of the computational trade-offs is crucial for the practical adoption of Cyclic NNs.

To address the challenges of hardware implementation, the authors should discuss the potential for parallelizing the computations in Cyclic NNs. This could involve exploring different scheduling strategies for the computations in the graph. The authors should also discuss the memory access patterns in Cyclic NNs and how they could be optimized for different hardware architectures. It would be beneficial to explore the potential for using specialized hardware accelerators, such as FPGAs or ASICs, to improve the performance of Cyclic NNs. The authors should also discuss the potential for using sparsity in the connections to reduce the memory footprint and computational cost of Cyclic NNs. A detailed discussion of the hardware implications is essential for the practical deployment of Cyclic NNs.

To explore the generalizability of Cyclic NNs, the authors should conduct experiments on a wider range of tasks and datasets. This could include tasks such as time-series forecasting, reinforcement learning, and natural language processing. The authors should also explore the potential for using Cyclic NNs in combination with other machine learning techniques, such as attention mechanisms or graph neural networks. It would be beneficial to compare the performance of Cyclic NNs with that of state-of-the-art methods on these tasks. The authors should also discuss the potential for adapting the architecture of Cyclic NNs to different types of data and tasks. A thorough exploration of the generalizability of Cyclic NNs is crucial for understanding their potential impact.

### Questions

1. How does the computational complexity of Cyclic NNs compare to traditional ANNs, especially in terms of training time and resource consumption?
2. What are the potential challenges in implementing Cyclic NNs in hardware, and how can they be addressed?
3. How does the choice of graph structure impact the performance of Cyclic NNs, and are there guidelines for selecting the optimal structure for a given task?
4. Can the authors provide more details on the hyperparameter sensitivity of Cyclic NNs, especially regarding the number of neurons and the connectivity patterns?
5. How do Cyclic NNs perform on tasks beyond the datasets used in the experiments, such as time-series forecasting or reinforcement learning?

### Rating

6

### Confidence

3

**********
