### Summary

This paper proposes a new benchmark for structure-based drug design (SBDD), called CBGBench. It unifies various existing SBDD tasks into a graph completion framework and adapts generative models for diverse applications in drug design. The benchmark evaluates models across multiple aspects, including chemical properties, interaction patterns, and geometric validity, using a standardized protocol. Experimental results highlight the strengths and limitations of current methods, providing insights for future improvements in SBDD.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. CBGBench standardizes SBDD tasks, enabling fair comparisons across different models and facilitating a more systematic evaluation of AI-driven drug design methods.
2. The benchmark includes a wide range of evaluation metrics, such as chemical property analysis, interaction assessment, and geometric validity, providing a comprehensive view of model performance.
3. By framing SBDD as a graph completion task, CBGBench allows for a unified and modular evaluation framework that can be extended to various drug design applications, including linker design and scaffold hopping.

### Weaknesses

#### Some Related Works


#### comment

1. The benchmark does not include CNN-based methods, which limits the scope of the evaluation. Specifically, the exclusion of voxel-based methods, which represent molecules as 3D grids, is a significant gap. These methods, such as those using 3D convolutional neural networks, offer a different approach to capturing spatial relationships and should be considered for a comprehensive benchmark.
2. Reliance on computational metrics without wet-lab validation may not fully reflect real-world chemical properties. For instance, the synthetic accessibility score (SA) calculated computationally might not accurately represent the true ease of synthesis in a laboratory setting. Similarly, the binding affinity predicted by AutoDock Vina, while useful, is an approximation and can differ from experimental results. This discrepancy could lead to an overestimation of the performance of some methods.
3. The paper does not provide detailed guidelines for the practical implementation of CBGBench, which may make it challenging for other researchers to adopt and extend the benchmark. For example, specific details on how to preprocess input data, handle edge cases, or integrate new models into the framework are lacking. This lack of clarity could hinder the reproducibility and widespread adoption of the benchmark.

### Suggestions

To enhance the benchmark, it is crucial to incorporate CNN-based methods, particularly those employing voxel-based representations. This would involve adapting the current framework to handle 3D grid inputs and outputs, which would require careful consideration of grid resolution, voxelization strategies, and the appropriate evaluation metrics for these methods. For example, metrics like voxel-wise accuracy or intersection-over-union (IoU) could be used to assess the quality of the generated voxel grids. Furthermore, the benchmark should include a more diverse set of CNN architectures, such as those using transposed convolutions for generative tasks, to provide a more comprehensive evaluation of the landscape of SBDD methods. This would not only broaden the scope of the benchmark but also provide valuable insights into the strengths and weaknesses of different modeling approaches.

To address the limitations of relying solely on computational metrics, the benchmark should incorporate experimental validation as a key component. This could involve selecting a subset of generated molecules and testing their binding affinity using biophysical assays, such as surface plasmon resonance (SPR) or isothermal titration calorimetry (ITC). Additionally, the synthetic accessibility of the generated molecules should be evaluated by attempting to synthesize them in the laboratory. This would provide a more realistic assessment of the practical utility of the generated molecules and help identify methods that are not only computationally efficient but also practically viable. The inclusion of experimental validation would significantly increase the credibility and impact of the benchmark.

Finally, to improve the practical implementation of CBGBench, the authors should provide detailed guidelines and documentation. This should include step-by-step instructions on how to set up the benchmark, preprocess input data, train and evaluate models, and integrate new methods into the framework. The documentation should also include examples of how to use the benchmark with different models and datasets. Furthermore, the authors should consider providing a modular codebase that allows researchers to easily extend and customize the benchmark for their specific needs. This would make the benchmark more accessible and encourage its widespread adoption within the drug discovery community.

### Questions

1. How can the benchmark be extended to include CNN-based methods, particularly those using voxel-based representations for molecules?
2. What steps could be taken to validate the computational metrics used in CBGBench with experimental data?
3. Can the authors provide more detailed guidelines or a modular codebase to help other researchers implement and extend CBGBench for additional SBDD tasks?

### Rating

6

### Confidence

3

**********
