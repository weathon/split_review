### Summary

This paper introduces ODEFormer, a transformer model designed for symbolic regression of dynamical systems. ODEFormer is trained on a large dataset of synthetic ODEs and can infer multidimensional ODE systems in symbolic form from a single solution trajectory. The authors also introduce a new benchmark dataset, odeBench, which contains 63 ODEs ranging from 1D to 4D. The paper evaluates ODEFormer on both odeBench and the existing Strogatz dataset, demonstrating that it outperforms existing methods in terms of accuracy and robustness to noise and irregular sampling.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a new transformer model, ODEFormer, which is specifically designed for symbolic regression of dynamical systems. This is a novel approach that has not been explored in previous work.
- The paper introduces a new benchmark dataset, odeBench, which provides a more comprehensive evaluation of dynamical SR methods than existing datasets.
- The paper demonstrates that ODEFormer outperforms existing methods in terms of accuracy and robustness to noise and irregular sampling.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational complexity of ODEFormer. This is an important consideration for practical applications, as the model may be computationally expensive to train and evaluate.
- The paper does not discuss the limitations of ODEFormer in detail. For example, the model may struggle with ODEs that have complex or chaotic dynamics, or with ODEs that have a large number of parameters. A more thorough discussion of the limitations of the model would be valuable.
- The paper does not provide a comparison of ODEFormer with other state-of-the-art methods for symbolic regression of dynamical systems. While the paper demonstrates that ODEFormer outperforms existing methods on the Strogatz and odeBench datasets, it would be useful to see how it compares to other methods on a wider range of datasets and tasks.

### Suggestions

The paper should include a more detailed analysis of the computational complexity of ODEFormer, including both training and inference time, as well as memory requirements. This analysis should consider the impact of various factors such as the length of the input trajectory, the dimensionality of the ODE system, and the size of the transformer model. For example, the authors could provide a breakdown of the time complexity of the different operations within the transformer architecture, and how these scale with the input size. Furthermore, it would be beneficial to include empirical measurements of training and inference time on different hardware configurations, and to compare these to other methods. This would provide a more practical understanding of the computational cost of using ODEFormer.

The paper should also provide a more thorough discussion of the limitations of ODEFormer. This should include a discussion of the types of ODEs that the model struggles with, such as those with complex or chaotic dynamics, or those with a large number of parameters. The authors could provide examples of specific ODEs where ODEFormer fails to produce accurate results, and analyze the reasons for these failures. For example, they could investigate whether the model struggles with long-range dependencies in the solution trajectories, or whether it is sensitive to the choice of initial conditions. Additionally, the authors should discuss the limitations of the model in terms of the complexity of the symbolic expressions that it can discover. It would be useful to know if the model can handle ODEs with trigonometric, exponential, or logarithmic functions, and how the performance degrades as the complexity of the symbolic expressions increases. 

Finally, the paper should include a more comprehensive comparison of ODEFormer with other state-of-the-art methods for symbolic regression of dynamical systems. This comparison should include a wider range of datasets and tasks, and should consider both the accuracy and robustness of the different methods. The authors could include a comparison with methods based on genetic programming, neural networks, or other machine learning techniques. Furthermore, it would be useful to compare ODEFormer with methods that are specifically designed for symbolic regression of dynamical systems, such as those based on sparse identification of nonlinear dynamics (SINDy) or other similar approaches. This would provide a more complete picture of the strengths and weaknesses of ODEFormer compared to other methods.

### Questions

- How does the computational complexity of ODEFormer compare to other methods for symbolic regression of dynamical systems?
- What are the limitations of ODEFormer in terms of the types of ODEs that it can handle effectively?
- How does the performance of ODEFormer vary with the length of the solution trajectory?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
