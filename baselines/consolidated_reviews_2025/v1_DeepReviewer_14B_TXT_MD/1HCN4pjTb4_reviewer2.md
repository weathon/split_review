### Summary

The paper provides a theoretical analysis of neural collapse in deep neural networks. The authors prove that neural collapse emerges in deep networks with at least two linear layers under certain conditions, such as low training error and balancedness of the linear layers. They also show that these conditions are satisfied by gradient descent training with weight decay for networks with a wide first layer. The paper presents numerical experiments that support the theoretical results, showing that neural collapse becomes more pronounced as the depth of the linear head increases.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses an important problem in deep learning, providing a theoretical understanding of neural collapse, a phenomenon observed in the last layer of deep neural networks.
2. The authors prove generic guarantees on neural collapse under certain assumptions and show that these assumptions hold for gradient descent training with weight decay.
3. The paper is well-organized, with clear definitions and a logical flow of ideas. The theoretical results are presented in a rigorous manner, and the numerical experiments are well-designed to support the theoretical findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's analysis is limited to deep networks with at least two linear layers, and it is unclear how the results would generalize to networks with different architectures or activation functions. Specifically, the reliance on a linear head for the analysis raises concerns about the applicability of the results to networks employing non-linear output layers, which are common in practice. The theoretical framework seems tightly coupled to the properties of linear transformations, and it's not immediately obvious how the core arguments would extend to scenarios with non-linear activations in the final layers. This limitation restricts the scope of the conclusions.
2. The assumptions made in the paper, such as low training error and balancedness of the linear layers, may not always hold in practice, especially for networks with different initializations or training procedures. The assumption of low training error, while often observed in practice, is not guaranteed, and the paper does not provide a detailed analysis of how deviations from this assumption might affect the emergence of neural collapse. Similarly, the balancedness condition, which requires the linear layers to have similar singular values, is a strong constraint that might not be satisfied in all training scenarios, particularly when using different initialization schemes or optimization algorithms. The paper lacks a discussion on the sensitivity of the results to these assumptions.

### Suggestions

The paper makes a valuable contribution by providing a theoretical analysis of neural collapse in deep linear networks. However, to strengthen the paper, it would be beneficial to explore the limitations of the current analysis and discuss potential avenues for future research. Specifically, the authors should investigate how the theoretical results might be extended to networks with non-linear activation functions in the output layer. This could involve exploring alternative theoretical frameworks or developing approximations that capture the behavior of non-linear networks. For example, one could consider using techniques from kernel methods or neural tangent kernels to analyze the behavior of networks with non-linear activations, and compare the results with the current analysis of linear networks. Furthermore, it would be useful to provide a more detailed discussion on the practical implications of the assumptions made in the paper. The authors should investigate how the neural collapse phenomenon is affected by different initialization schemes, optimization algorithms, and training procedures. This could involve conducting additional numerical experiments or developing theoretical bounds on the deviation from the assumed conditions. For instance, the authors could explore the impact of different weight initialization strategies on the balancedness of the linear layers and how this affects the emergence of neural collapse. 

Additionally, the paper could benefit from a more in-depth discussion of the relationship between neural collapse and other phenomena observed in deep learning, such as the double descent phenomenon or the lottery ticket hypothesis. Exploring these connections could provide a more comprehensive understanding of the underlying mechanisms driving neural collapse and its implications for deep learning. For example, the authors could investigate whether the conditions that lead to neural collapse also correlate with the occurrence of double descent or whether the presence of neural collapse affects the ability to find winning tickets. Furthermore, the authors should consider the impact of different regularization techniques on the neural collapse phenomenon. While the paper focuses on weight decay, it would be interesting to explore how other regularization methods, such as dropout or batch normalization, affect the emergence and characteristics of neural collapse. This could involve conducting additional experiments or developing theoretical extensions to the current framework. 

Finally, the authors should provide more concrete guidance on how the theoretical results can be used to improve the design and training of deep neural networks. While the paper demonstrates that neural collapse emerges under certain conditions, it is not clear how this knowledge can be leveraged to develop more effective training strategies or network architectures. For example, the authors could explore whether the balancedness condition can be enforced during training to promote neural collapse and improve generalization performance. This could involve developing new regularization techniques or modifying the optimization algorithm to encourage the emergence of balanced linear layers. Furthermore, the authors could investigate whether the neural collapse phenomenon can be used as a diagnostic tool to assess the quality of the learned representations and identify potential issues in the training process.

### Questions

1. How do the theoretical results extend to networks with non-linear activation functions in the output layer? Can the authors provide any insights or analysis on this aspect?
2. What are the practical implications of the neural collapse phenomenon for the design and training of deep neural networks? How can the theoretical results be used to improve the performance of deep learning models in real-world applications?

### Rating

5

### Confidence

2

**********
