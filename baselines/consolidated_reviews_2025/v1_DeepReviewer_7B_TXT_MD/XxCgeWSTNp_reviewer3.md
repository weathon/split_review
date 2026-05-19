### Summary

This paper proposes a parametric family of stochastic differential equations (SDEs) to improve the efficiency of sampling in Lévy-Itô diffusion models. The authors derive a new SDE that allows for more flexibility in the reverse diffusion process by introducing a parameter ηt that controls the amount of noise added at each step. This approach is shown to outperform existing methods in terms of sample quality when using a small number of function evaluations (NFEs). The paper also demonstrates the applicability of the proposed method to a text-to-speech model, showing that it can handle imbalanced datasets effectively.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive evaluation of their proposed method on image generation tasks, comparing it to existing approaches and demonstrating its effectiveness in terms of sample quality and computational efficiency.
3. The authors also provide a detailed analysis of the results, including ablation studies and visualizations, which helps to understand the behavior of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, particularly in comparison to existing approaches. While the authors mention that their method can achieve better performance with fewer function evaluations (NFE), they do not provide any information about the actual runtime or memory usage of their method. This makes it difficult to assess the practical benefits of the method and its suitability for real-world applications.
2. The paper does not provide a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters, such as the step size and the number of function evaluations (NFE). While the authors mention that their method is robust to the choice of hyperparameters, they do not provide any specific details or experiments to support this claim. This makes it difficult to assess the robustness of the method and its potential for practical use.

### Suggestions

The authors should provide a more thorough analysis of the computational cost of their proposed method. This should include a comparison of the runtime and memory usage of their method with existing approaches, such as DDIM and DPM-Solver, under various settings. Specifically, the authors should report the wall-clock time for generating samples with different numbers of function evaluations (NFEs) and compare these results to those of DDIM and DPM-Solver. This analysis should be performed on a standard hardware setup to ensure reproducibility. Furthermore, the authors should investigate the memory footprint of their method, as this can be a limiting factor for large-scale applications. It would be beneficial to include a table or figure that shows the runtime and memory usage of their method for different values of NFE, as well as the performance of DDIM and DPM-Solver for comparison. This would allow readers to better understand the trade-offs between computational cost and sample quality.

In addition to the computational cost, the authors should also provide a more detailed analysis of the sensitivity of their method to the choice of hyperparameters. This should include an investigation of how the performance of their method varies with different step sizes and numbers of function evaluations (NFEs). The authors should conduct experiments with a range of step sizes and NFE values and report the corresponding sample quality metrics. It would be helpful to include a plot or table that shows the performance of their method as a function of these hyperparameters. Furthermore, the authors should discuss the optimal values for these hyperparameters and provide guidelines for choosing appropriate values for different applications. This would help readers to understand the robustness of the method and its potential for practical use. It is also important to analyze the impact of different noise schedules on the performance of the proposed method, as this can significantly affect the quality of the generated samples.

Finally, the authors should provide a more detailed discussion of the limitations of their proposed method. While the paper demonstrates the effectiveness of the method on image generation tasks, it is important to acknowledge the potential limitations of the method in other applications. For example, the authors should discuss the potential challenges of applying their method to high-dimensional data or complex noise distributions. It would also be helpful to compare the performance of their method with other state-of-the-art sampling techniques for diffusion models, such as those based on neural ordinary differential equations (ODEs). This would provide a more comprehensive evaluation of the proposed method and its potential impact on the field. The authors should also discuss the potential for future research directions, such as exploring adaptive step size control or more sophisticated noise schedules.

### Questions

1. How does the proposed method compare to other state-of-the-art sampling algorithms for diffusion models, such as DDIM and DPM-Solver, in terms of both performance and computational cost?
2. Can the proposed method be applied to other types of diffusion models, such as those used in audio or video generation? If so, what modifications would be necessary?
3. How sensitive is the proposed method to the choice of hyperparameters, such as the step size and the number of function evaluations (NFE)? Are there any guidelines for choosing appropriate hyperparameter values for different applications?

### Rating

6

### Confidence

2

**********
