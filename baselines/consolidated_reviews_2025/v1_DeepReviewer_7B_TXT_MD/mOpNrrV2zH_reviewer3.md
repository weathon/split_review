### Summary

This paper introduces CBGBench, a benchmark for 3D binding graph completion in SBDD and lead optimization. The authors unify tasks as graph completion and categorize existing methods to provide a comprehensive evaluation framework. They conduct extensive experiments across multiple tasks and metrics, offering valuable insights into model performance and limitations.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The benchmark covers a wide range of tasks and evaluation metrics, providing a comprehensive assessment of model performance.
3. The authors conduct extensive experiments across multiple tasks and metrics, offering valuable insights into model performance and limitations.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on GNN-based methods, which limits the scope of the benchmark. The authors should consider including other types of methods, such as those based on transformers or other graph neural networks.
2. The benchmark's evaluation metrics, while comprehensive, may not fully capture the nuances of real-world applications. For example, the authors could consider including metrics that assess the stability and robustness of the generated molecules.
3. The paper does not provide a detailed analysis of the computational cost of the different methods. This information is crucial for practical applications, where computational resources may be limited.

### Suggestions

The authors should broaden the scope of their benchmark by incorporating a more diverse set of methods, particularly those that utilize transformer architectures or other non-GNN approaches. While GNNs have shown promise in this domain, the field is rapidly evolving, and methods based on transformers are gaining significant traction. Including these methods would make the benchmark more comprehensive and relevant to a wider audience. Specifically, the authors could explore methods that leverage attention mechanisms to model complex interactions between atoms and the binding pocket. Furthermore, the benchmark could benefit from the inclusion of methods that use different types of graph representations, such as those based on molecular fingerprints or other structural descriptors. This would allow for a more thorough evaluation of the strengths and weaknesses of different approaches. The authors should also consider the inclusion of methods specifically designed for lead optimization tasks, as this is a critical application of SBDD.

To address the limitations of the evaluation metrics, the authors should consider incorporating metrics that assess the stability and robustness of the generated molecules. While the current metrics provide a good starting point, they may not fully capture the nuances of real-world applications. For example, the authors could include metrics that evaluate the strain energy of the generated molecules, which would provide insights into their stability. Additionally, the authors could consider including metrics that assess the robustness of the generated molecules to small perturbations in the binding pocket. This would be particularly relevant for lead optimization tasks, where the goal is to identify molecules that are stable and effective across a range of binding conditions. The authors could also explore the use of metrics that assess the drug-likeness of the molecules, such as the predicted binding affinity or the predicted toxicity. This would make the benchmark more relevant to real-world applications.

Finally, the authors should provide a more detailed analysis of the computational cost of the different methods. This information is crucial for practical applications, where computational resources may be limited. The authors should provide a breakdown of the time and memory requirements for each method, as well as the hardware used for the experiments. This would allow users of the benchmark to make informed decisions about which methods are most suitable for their specific needs. Furthermore, the authors could explore the use of techniques such as model pruning or quantization to reduce the computational cost of the methods. This would make the benchmark more accessible to researchers who do not have access to high-performance computing resources. The authors should also consider providing guidelines on how to optimize the performance of the methods on different hardware platforms.

### Questions

1. How do the authors plan to address the limitations of the current evaluation metrics in future iterations of the benchmark?
2. What are the authors' plans for expanding the benchmark to include other types of methods, such as those based on transformers?
3. How do the authors plan to address the computational cost of the different methods in future iterations of the benchmark?

### Rating

6

### Confidence

4

**********
