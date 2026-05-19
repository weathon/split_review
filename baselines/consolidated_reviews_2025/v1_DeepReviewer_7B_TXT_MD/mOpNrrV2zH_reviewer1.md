### Summary

This paper introduces a new benchmark, CBGBench, for evaluating 3D binding graph completion tasks, which unifies molecule generation and lead optimization. The benchmark includes four tasks and a unified evaluation framework, allowing for fair comparisons between different methods. The authors also provide a comprehensive evaluation of existing methods and derive several insightful conclusions.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive evaluation of existing methods, covering both molecule generation and lead optimization tasks.
3. The benchmark includes a variety of evaluation metrics, which are well-suited for assessing the performance of different methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on GNN-based methods, which limits the scope of the benchmark. The authors should consider including other types of methods, such as those based on transformers or other graph neural networks.
2. The benchmark's evaluation metrics, while comprehensive, may not fully capture the nuances of real-world applications. For example, the authors could consider including metrics that assess the stability and robustness of the generated molecules.
3. The paper does not provide a detailed analysis of the computational cost of the different methods. This information is crucial for practical applications, where computational resources may be limited.

### Suggestions

The authors should broaden the scope of their benchmark by incorporating a more diverse set of methods, particularly those that utilize transformer architectures or other non-GNN approaches. While GNNs have shown promise in this domain, the field is rapidly evolving, and methods based on transformers are gaining significant traction. Including these methods would make the benchmark more comprehensive and relevant to a wider audience. Specifically, the authors could explore methods that leverage attention mechanisms to model complex interactions between atoms and the binding pocket. Furthermore, the benchmark could benefit from the inclusion of methods that use different types of graph representations, such as those based on molecular fingerprints or other structural descriptors. This would allow for a more thorough evaluation of the strengths and weaknesses of different approaches.

To address the limitations of the evaluation metrics, the authors should consider incorporating metrics that assess the stability and robustness of the generated molecules. While the current metrics provide a good starting point, they may not fully capture the nuances of real-world applications. For example, the authors could include metrics that assess the strain energy of the generated molecules, which would provide insights into their stability. Additionally, the authors could consider including metrics that assess the robustness of the generated molecules to small perturbations in the binding pocket. This would be particularly relevant for lead optimization tasks, where the goal is to identify molecules that are stable and effective across a range of binding conditions. The authors could also explore the use of metrics that assess the novelty of the generated molecules, which would be important for identifying novel drug candidates.

Finally, the authors should provide a more detailed analysis of the computational cost of the different methods. This information is crucial for practical applications, where computational resources may be limited. The authors could provide a breakdown of the time and memory requirements for each method, as well as the hardware used for the experiments. This would allow users of the benchmark to make informed decisions about which methods are most suitable for their specific needs. Furthermore, the authors could explore the use of techniques such as model pruning or quantization to reduce the computational cost of the methods. This would make the benchmark more accessible to researchers who do not have access to high-performance computing resources.

### Questions

1. How do the authors plan to address the limitations of the current evaluation metrics in future iterations of the benchmark?
2. What are the authors' plans for expanding the benchmark to include other types of methods, such as those based on transformers?
3. How do the authors plan to address the computational cost of the different methods in future iterations of the benchmark?

### Rating

5

### Confidence

4

**********
