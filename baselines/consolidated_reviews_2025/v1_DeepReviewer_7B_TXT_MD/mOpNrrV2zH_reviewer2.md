### Summary

This paper introduces CBGBench, a benchmark for evaluating 3D binding graph completion tasks in SBDD and lead optimization. It unifies tasks into a 3D binding graph completion framework, categorizes existing methods, and provides a comprehensive evaluation protocol. The benchmark is tested on both de novo molecule generation and lead optimization tasks, with a focus on assessing interaction patterns, chemical properties, geometry, and stability.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to understand.
2. The benchmark is comprehensive, covering a wide range of tasks and evaluation metrics.
3. The benchmark provides a unified framework for evaluating different methods in SBDD and lead optimization.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on the evaluation of existing methods, but it does not propose any new methods or techniques. The contribution of the paper is limited in terms of advancing the state of the art in SBDD and lead optimization.
2. The benchmark is primarily based on GNNs, which may not be suitable for all types of molecules or binding interactions. The authors should consider including other types of methods, such as those based on transformers or other graph neural networks, to make the benchmark more comprehensive.
3. The evaluation metrics used in the benchmark may not fully capture the nuances of real-world applications. For example, the authors could consider including metrics that assess the stability and robustness of the generated molecules, or metrics that evaluate the drug-likeness of the molecules.
4. The paper does not provide a detailed analysis of the computational cost of the different methods. This information is important for practical applications, where computational resources may be limited.

### Suggestions

The authors should consider expanding the benchmark to include a wider range of methods, particularly those based on transformer architectures or other non-GNN approaches. This would make the benchmark more comprehensive and relevant to a wider audience. For example, methods that leverage attention mechanisms to model complex interactions between atoms and the binding pocket could be included. Furthermore, the benchmark could benefit from the inclusion of methods that use different types of graph representations, such as those based on molecular fingerprints or other structural descriptors. This would allow for a more thorough evaluation of the strengths and weaknesses of different approaches. The authors should also consider incorporating methods that are specifically designed for lead optimization tasks, as this is a critical application of SBDD.

To address the limitations of the evaluation metrics, the authors should consider including metrics that assess the stability and robustness of the generated molecules. For example, the authors could include metrics that evaluate the strain energy of the generated molecules, which would provide insights into their stability. Additionally, the authors could consider including metrics that assess the robustness of the generated molecules to small perturbations in the binding pocket. This would be particularly relevant for lead optimization tasks, where the goal is to identify molecules that are stable and effective across a range of binding conditions. The authors should also explore the use of metrics that assess the drug-likeness of the molecules, such as the predicted binding affinity or the predicted toxicity. This would make the benchmark more relevant to real-world applications.

Finally, the authors should provide a more detailed analysis of the computational cost of the different methods. This information is crucial for practical applications, where computational resources may be limited. The authors should provide a breakdown of the time and memory requirements for each method, as well as the hardware used for the experiments. This would allow users of the benchmark to make informed decisions about which methods are most suitable for their specific needs. Furthermore, the authors could explore the use of techniques such as model pruning or quantization to reduce the computational cost of the methods. This would make the benchmark more accessible to researchers who do not have access to high-performance computing resources.

### Questions

1. How do the authors plan to address the limitations of the current evaluation metrics in future iterations of the benchmark?
2. What are the authors' plans for expanding the benchmark to include other types of methods, such as those based on transformers?
3. How do the authors plan to address the computational cost of the different methods in future iterations of the benchmark?

### Rating

5

### Confidence

4

**********
