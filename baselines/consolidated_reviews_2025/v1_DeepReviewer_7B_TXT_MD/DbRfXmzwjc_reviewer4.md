### Summary

The paper presents a novel approach to molecular generation using a graph-based model called MAGNet. The key innovation of MAGNet is its factorisation of the molecular graph into a set of shapes, which represent the global context of the molecule, and the atom and bond types, which are generated sequentially. This approach allows for a more flexible and comprehensive representation of molecular structures, which can lead to more diverse and complex molecules. The authors demonstrate the effectiveness of MAGNet on standard benchmarks and show that it outperforms existing graph-based methods in terms of structural diversity and atom/bond assignment accuracy.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The factorisation of molecular graphs into shapes and atom/bond types is a novel and effective approach to molecular generation. This factorisation allows for a more flexible and comprehensive representation of molecular structures, which can lead to more diverse and complex molecules.
- The paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup.
- The authors provide a thorough evaluation of MAGNet on standard benchmarks, demonstrating its effectiveness in terms of structural diversity and atom/bond assignment accuracy.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is important for understanding its scalability and applicability to large molecular datasets.
- The paper does not discuss the limitations of the proposed method, such as its performance on specific types of molecules or its sensitivity to hyperparameters.

### Suggestions

The authors should provide a more thorough analysis of the computational complexity of MAGNet, including a breakdown of the time and memory requirements for each step of the generation process. This analysis should consider the impact of different molecular sizes and complexities on the computational cost. For example, the authors could analyze how the number of shapes and the size of the shape vocabulary affect the runtime and memory usage. Furthermore, it would be beneficial to compare the computational cost of MAGNet with existing methods, such as JT-VAE and MoLeR, to provide a clearer understanding of its efficiency. This analysis should also include a discussion of potential optimizations that could be implemented to improve the scalability of the method, such as parallelization or the use of more efficient data structures. This would help to make the method more practical for large-scale molecular design tasks.

In addition to computational complexity, the authors should also discuss the limitations of MAGNet in more detail. This should include an analysis of the types of molecules for which the method performs well, as well as the types of molecules for which it struggles. For example, the authors could investigate the performance of MAGNet on molecules with specific functional groups or ring systems. It would also be useful to analyze the sensitivity of the method to different hyperparameters, such as the size of the shape vocabulary and the number of layers in the neural networks. The authors should also discuss the potential impact of these hyperparameters on the quality of the generated molecules. Furthermore, the authors should provide a more detailed discussion of the types of molecules that are not well-represented by the shape vocabulary. This analysis should include a discussion of the potential reasons for these limitations and suggest possible solutions for addressing them. This would help to provide a more complete understanding of the capabilities and limitations of the proposed method.

Finally, the authors should provide more details on the training process of MAGNet, including the specific optimization algorithms used, the learning rate schedule, and the batch size. It would also be useful to discuss the convergence behavior of the model and the impact of different training parameters on the final performance. The authors should also provide a more detailed analysis of the generated molecules, including their structural diversity and atom/bond assignment accuracy. This analysis should include a comparison with the results of existing methods, such as JT-VAE and MoLeR, to provide a more comprehensive evaluation of the proposed method. The authors should also discuss the potential applications of MAGNet in real-world molecular design tasks, such as drug discovery and materials science. This would help to demonstrate the practical relevance of the proposed method.

### Questions

- How does the proposed method handle molecules with complex 3D structures?
- What are the limitations of the proposed method, and how can they be addressed in future work?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
