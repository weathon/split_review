### Summary

The paper proposes a novel graph data augmentation method, Dual-Prism (DP), which operates in the spectral domain to preserve essential graph properties while diversifying augmented graphs. The authors introduce two augmentation strategies, DP-Noise and DP-Mask, which modify the high-frequency components of the graph spectrum while retaining the low-frequency components. The paper provides extensive experimental results demonstrating the effectiveness of DP in various learning paradigms, including supervised, semi-supervised, unsupervised, and transfer learning.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The experimental results are comprehensive and convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the eigen-decomposition of the Laplacian matrix, which is computationally expensive. The paper does not provide a detailed analysis of the computational complexity of the proposed method, especially in comparison to other graph augmentation techniques. This is a significant concern, especially for large graphs where eigen-decomposition can become a bottleneck. Furthermore, the paper lacks a discussion on potential approximations or optimizations to mitigate this computational burden.
2. The paper does not provide a clear explanation of how the proposed method can be applied to directed graphs. The Laplacian matrix is typically defined for undirected graphs, and the extension to directed graphs is not straightforward. The paper should discuss the specific challenges and potential solutions for applying the proposed method to directed graphs, including how to define the Laplacian and perform eigen-decomposition in this context.
3. The paper does not provide a clear explanation of how the proposed method can be applied to dynamic graphs. The current formulation of the method seems to assume a static graph structure, and it is unclear how it would handle temporal changes in the graph topology. The paper should discuss the challenges of applying the proposed method to dynamic graphs and propose a strategy for handling temporal changes, such as how to update the Laplacian matrix and perform augmentation over time.

### Suggestions

The paper should include a more thorough analysis of the computational complexity of the proposed Dual-Prism (DP) method. Specifically, the authors should provide a detailed breakdown of the time complexity of each step, including the eigen-decomposition of the Laplacian matrix, and compare it to other graph augmentation techniques. This analysis should consider the impact of graph size and density on the computational cost. Furthermore, the authors should explore and discuss potential approximations or optimizations to reduce the computational burden, such as using sparse matrix representations or iterative eigen-decomposition algorithms. It would also be beneficial to include empirical results on the runtime of the proposed method for different graph sizes to demonstrate its practical scalability.

To address the applicability of the proposed method to directed graphs, the authors should provide a detailed explanation of how the Laplacian matrix can be defined for directed graphs and how the eigen-decomposition can be performed in this context. The paper should discuss the specific challenges of applying the proposed method to directed graphs, such as the potential for complex eigenvalues and the need for alternative spectral analysis techniques. The authors should also provide experimental results on directed graph datasets to demonstrate the effectiveness of their method in this setting. Furthermore, the paper should discuss the limitations of the proposed method for directed graphs and potential future research directions to overcome these limitations.

Finally, the paper should discuss the challenges of applying the proposed method to dynamic graphs and propose a strategy for handling temporal changes. The authors should explain how the Laplacian matrix can be updated over time and how the augmentation can be performed in a way that preserves the temporal dependencies in the graph. The paper should also discuss the potential for using techniques such as temporal graph neural networks to incorporate the augmented graphs into a dynamic learning framework. It would be beneficial to include experimental results on dynamic graph datasets to demonstrate the effectiveness of the proposed method in this setting. The authors should also discuss the limitations of the proposed method for dynamic graphs and potential future research directions to overcome these limitations.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
