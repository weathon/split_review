### Summary

The paper presents a novel graph synthesis framework called PROVCREATOR, designed to address the issue of class imbalance in system provenance datasets. The framework generates synthetic provenance graphs that maintain structural and attribute fidelity, improving the performance of machine learning models for downstream tasks such as program classification and malware detection. The authors demonstrate that PROVCREATOR produces provenance graphs with higher structural fidelity, attribute fidelity, and downstream utility compared to existing graph synthesis methods.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel graph synthesis framework, PROVCREATOR, specifically designed for system provenance graphs, which are crucial for cybersecurity applications.
2. The paper provides a comprehensive evaluation of PROVCREATOR, demonstrating its effectiveness in generating synthetic graphs that are structurally and attribute-wise similar to real-world data.
3. The paper is well-written and easy to follow, with clear explanations of the proposed method and its evaluation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is important for assessing its scalability and practicality in real-world applications.
2. The paper does not discuss the potential limitations of the proposed method, such as its sensitivity to hyperparameter settings or its performance on different types of system provenance graphs.
3. The paper does not provide a comparison with other state-of-the-art graph synthesis methods, which makes it difficult to assess the novelty and effectiveness of the proposed method.

### Suggestions

The paper should include a more thorough analysis of the computational complexity of the PROVCREATOR framework. Specifically, the authors should provide a breakdown of the time and space complexity for each stage of the graph generation process, including the structure generation and attribute generation. This analysis should consider the impact of graph size and density on the overall computational cost. Furthermore, it would be beneficial to compare the computational complexity of PROVCREATOR with existing graph synthesis methods, such as GDSS, to highlight the efficiency gains or limitations of the proposed approach. This analysis should also consider the practical implications of the computational cost, such as the feasibility of generating large-scale synthetic graphs for real-world applications. The authors should also discuss the hardware requirements for running the framework, including the memory and processing power needed for different graph sizes.

In addition to computational complexity, the paper should also address the limitations of the proposed method in more detail. This should include a discussion of the sensitivity of the method to hyperparameter settings, such as the number of generated graphs, the number of synthetic graphs used for augmentation, and the choice of diffusion steps. The authors should provide guidelines for selecting appropriate hyperparameter values based on the characteristics of the input data. Furthermore, the paper should discuss the potential impact of different types of system provenance graphs on the performance of PROVCREATOR. For example, the authors should analyze the performance of the method on graphs with different structures, such as those with high clustering coefficients or those with long-range dependencies. The authors should also discuss the limitations of the method in handling graphs with complex node and edge attributes, and how these limitations might affect the quality of the generated graphs.

Finally, the paper needs a more comprehensive comparison with other state-of-the-art graph synthesis methods. The authors should include a quantitative comparison of PROVCREATOR with methods such as GDSS, GraphDiffusion, and other relevant techniques, using metrics that capture both structural and attribute fidelity. This comparison should not only focus on the performance of the generated graphs but also on the computational cost and scalability of the methods. The authors should also discuss the advantages and disadvantages of PROVCREATOR compared to these other methods, highlighting the specific scenarios where PROVCREATOR is expected to perform better. This comparison should be supported by empirical results, demonstrating the effectiveness of PROVCREATOR in generating high-quality synthetic graphs for various downstream tasks.

### Questions

1. How does PROVCREATOR handle the generation of graphs with varying sizes and complexities, especially in scenarios with highly dynamic or rapidly changing programs?
2. What are the limitations of PROVCREATOR in terms of scalability and computational cost, especially when dealing with large-scale datasets?
3. How does PROVCREATOR compare to other state-of-the-art graph synthesis methods in terms of structural and attribute fidelity, and what are the advantages and disadvantages of each method?

### Rating

5

### Confidence

4

**********
