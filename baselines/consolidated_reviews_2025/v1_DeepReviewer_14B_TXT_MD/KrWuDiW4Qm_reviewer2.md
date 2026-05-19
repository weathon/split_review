### Summary

The authors propose a meta-learning based method to improve the OOD robustness in physics-informed machine learning. The proposed method is based on three components: (1) learning shared causal structure among all tasks, (2) learning task-specific parameters and (3) test-time adaption of the task-specific parameters. The authors show that their method outperform existing methods on three different OOD settings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors show that their method outperform existing methods on three different OOD settings. The authors also provide ablation studies to show the importance of each component of their method.

### Weaknesses

#### Some Related Works


#### comment

I think that the paper can benefit from more experiments on more complex dynamical systems. The current experiments are on relatively simple ODEs. I think that the authors should also discuss on how their method will scale with the system size.

### Suggestions

The paper would significantly benefit from a more thorough exploration of the method's performance on complex, high-dimensional dynamical systems. The current experiments, while demonstrating the core concept, are limited to relatively simple ODEs. It is crucial to evaluate the method on systems with a larger number of interacting components, such as those found in real-world applications. For example, the authors could consider systems with chaotic behavior or stiff ODEs, which are known to be challenging for many numerical methods. Furthermore, the evaluation should include a detailed analysis of the computational cost associated with the proposed method as the system size increases. This would involve measuring the time and memory requirements for both training and test-time adaptation, providing a clearer picture of the method's scalability. Such experiments would not only strengthen the paper's claims but also provide valuable insights into the practical applicability of the proposed approach.

In addition to the complexity of the dynamical systems, the paper should also address the sensitivity of the method to the choice of basis functions. The current approach relies on a predefined set of basis functions, and it is unclear how the performance would be affected by different choices. A systematic study of the impact of basis function selection on the accuracy and robustness of the method is needed. This could involve comparing different types of basis functions, such as polynomials, Fourier series, or wavelets, and analyzing their performance across various dynamical systems. Furthermore, the authors should discuss the potential limitations of the method when the true underlying dynamics cannot be well-represented by the chosen basis functions. This discussion should include strategies for mitigating these limitations, such as adaptive basis function selection or the use of more flexible function approximators.

Finally, the paper should provide a more detailed analysis of the test-time adaptation process. While the authors mention that the task-specific parameters are adapted at test time, the paper lacks a thorough investigation of how this adaptation affects the overall performance. It would be beneficial to analyze the convergence behavior of the adaptation process and how it depends on the initial conditions and the observed trajectory length. Furthermore, the authors should discuss the potential for overfitting during test-time adaptation, especially when the observed trajectory is noisy or limited. This discussion should include strategies for preventing overfitting, such as early stopping or regularization techniques. A more detailed analysis of the test-time adaptation process would provide a deeper understanding of the method's strengths and limitations and would help to guide its practical application.

### Questions

The authors claim that the existing methods fail in OOD tasks, including the one in Wang et al. (2021b). When we compare the results of MetaPhysiCa and Wang et al. (2021b), I see that the results are very similar for the in-distribution case. Is there any difference in the implementation of Wang et al. (2021b)?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
