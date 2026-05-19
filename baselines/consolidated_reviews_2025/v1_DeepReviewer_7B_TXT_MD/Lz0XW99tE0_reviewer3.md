### Summary

This paper proposes a novel crystal generation method, CrysBFN, which leverages Bayesian Flow Networks (BFN) to generate crystal structures in the hyper-torus. The authors address the theoretical challenges of periodic Bayesian flow and propose a periodic Bayesian flow for crystal generation. They also introduce an entropy conditioning mechanism and a fast sampling algorithm to enhance the method's efficiency. The experimental results demonstrate that CrysBFN achieves state-of-the-art performance on several crystal generation benchmarks and significantly improves sampling efficiency compared to previous diffusion-based methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to crystal generation by extending Bayesian Flow Networks (BFN) to handle periodic boundary conditions and crystal symmetries. This is a significant contribution to the field, as it addresses the unique challenges posed by crystal structures.
2. The authors provide a thorough theoretical analysis of the proposed method, including the challenges of periodic Bayesian flow and the introduction of a periodic BFN. This analysis is well-supported by mathematical formulations and diagrams.
3. The experimental results are comprehensive and demonstrate the effectiveness of CrysBFN. The method achieves state-of-the-art performance on several crystal generation benchmarks and significantly improves sampling efficiency compared to previous diffusion-based methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method, particularly in comparison to existing approaches. This makes it difficult to assess the scalability of the method for larger and more complex crystal structures. Specifically, the paper lacks a breakdown of the computational cost associated with each step of the Bayesian flow process, such as the evaluation of the von Mises distribution and the matrix operations involved in the equivariant layers. A more granular analysis of the time complexity, including the dependence on the number of atoms and the dimensionality of the latent space, is needed.
2. While the paper demonstrates the effectiveness of CrysBFN on several benchmark datasets, it does not explore the performance of the method on more complex or diverse crystal structures, such as those with non-trivial symmetries or complex bonding patterns. This limits the generalizability of the findings. The evaluation should include a more diverse set of crystal structures, including those with varying unit cell sizes, chemical compositions, and crystal systems. Furthermore, the paper should investigate the sensitivity of the method to different hyperparameter settings and provide guidelines for selecting appropriate values for different types of crystal structures.
3. The paper does not provide a detailed discussion of the limitations of the proposed method, such as potential biases in the generated structures or the challenges of generating certain types of crystal structures. A more thorough analysis of the failure modes of the method is needed. For example, it would be beneficial to understand if the method struggles with generating structures that have specific geometric constraints or unusual bonding patterns. The paper should also discuss the potential for the method to generate physically unrealistic structures and provide strategies for mitigating these issues.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the time complexity of each step in the CrysBFN algorithm. This should include a clear analysis of the dependence on the number of atoms, the dimensionality of the latent space, and the number of iterations required for convergence. The authors should also compare the computational cost of CrysBFN with existing methods, such as diffusion-based approaches, and discuss the trade-offs between accuracy and efficiency. Furthermore, the authors should provide empirical results on the runtime of the method for different crystal sizes and complexities, which would help to assess its scalability. This analysis should also consider the memory requirements of the method, which can be a limiting factor for large-scale crystal structures.

To improve the evaluation of the method, the authors should include a more diverse set of crystal structures in their benchmark datasets. This should include structures with varying unit cell sizes, chemical compositions, and crystal systems, as well as structures with non-trivial symmetries and complex bonding patterns. The authors should also investigate the sensitivity of the method to different hyperparameter settings and provide guidelines for selecting appropriate values for different types of crystal structures. This could involve conducting a hyperparameter search and analyzing the impact of different parameter choices on the quality of the generated structures. Additionally, the authors should explore the use of more sophisticated evaluation metrics that can capture the structural properties of the generated crystals, such as the distribution of bond lengths and angles, and the presence of specific motifs.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method, including potential biases in the generated structures and the challenges of generating certain types of crystal structures. This should include an analysis of the failure modes of the method and strategies for mitigating these issues. For example, the authors could investigate the method's ability to generate structures with specific geometric constraints or unusual bonding patterns. They should also discuss the potential for the method to generate physically unrealistic structures and provide strategies for mitigating these issues, such as using constraints or post-processing techniques. A thorough analysis of these limitations would provide a more complete picture of the capabilities and limitations of the proposed method.

### Questions

1. How does the proposed method handle the computational complexity of generating large crystal structures, and what are the limitations in terms of scalability?
2. What are the potential biases in the generated crystal structures, and how can they be mitigated?
3. How does the method perform on crystal structures with non-trivial symmetries or complex bonding patterns, and what are the challenges in generating such structures?

### Rating

6

### Confidence

3

**********
