### Summary

The paper studies the universal approximation property of a neural network with permutation invariant initialization. The authors prove that such a network can approximate any continuous function with arbitrary precision. The paper also presents some numerical experiments to support the theoretical findings.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper presents a novel approach to studying the universal approximation property of neural networks, which is a fundamental problem in the field. The authors introduce the concept of permutation invariant initialization and prove that such an initialization can lead to a network that approximates any continuous function with arbitrary precision. This is a significant contribution to the understanding of neural network approximation capabilities.

### Weaknesses

#### Some Related Works


#### comment

The paper's theoretical results are based on a specific type of network architecture and initialization scheme, which may limit the applicability of the findings. The authors should discuss the limitations of their approach and the potential challenges in extending their results to more general settings. Specifically, the reliance on a two-layer network with a specific form of basis functions (step functions derived from ReLU) is a significant constraint. The proof of universal approximation is heavily dependent on the ability to construct these step functions and then combine them to approximate any continuous function. This approach, while novel, may not easily generalize to deeper networks or different activation functions. The paper should address the limitations imposed by this specific architecture and initialization scheme, and discuss the challenges in extending the results to more general settings.

### Suggestions

The authors should provide a more detailed discussion on the limitations of their specific network architecture and initialization scheme. While the use of permutation invariant initialization is interesting, the restriction to a two-layer network with step function approximators derived from ReLU activations limits the scope of the theoretical results. It would be beneficial to explore the challenges in extending these results to deeper networks, where the approximation capabilities are not as well understood. For example, the authors could discuss how the complexity of the network architecture affects the approximation rate and the required network width. Furthermore, the authors should consider the implications of using different activation functions, such as sigmoid or tanh, and how these might impact the permutation invariant property and the universal approximation capability. A more thorough analysis of these limitations would significantly strengthen the paper's contribution and provide a clearer understanding of the scope of the theoretical findings.

To enhance the practical relevance of the paper, the authors should provide more details on the numerical experiments. While the experiments demonstrate the effectiveness of the proposed approach, it would be helpful to include a more detailed analysis of the experimental results. For example, the authors could discuss the convergence behavior of the network during training, the sensitivity of the approximation to different hyperparameters, and the computational cost of the proposed method. Furthermore, the authors should compare their results with existing methods for universal approximation, such as those based on random initialization or other network architectures. This would provide a more comprehensive evaluation of the proposed approach and highlight its advantages and disadvantages. The authors should also discuss the potential for using their approach in practical applications, such as function approximation or system identification.

Finally, the authors should clarify the relationship between their work and existing research on permutation invariant networks. While the paper introduces a novel approach to studying the universal approximation property, it is important to clearly distinguish it from other related work. The authors should discuss how their approach differs from existing methods, such as those based on permutation equivariant networks or other techniques for achieving permutation invariance. A more detailed comparison with existing literature would help to contextualize the paper's contribution and highlight its unique aspects. The authors should also discuss the potential for combining their approach with other techniques to further improve the performance of neural networks.

### Questions

Can the authors provide more details on the numerical experiments? How do the results compare with existing methods for universal approximation?

### Rating

3

### Confidence

3

**********
