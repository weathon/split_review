### Summary

This paper proposes ODEFormer, a transformer-based model for symbolic regression of ODEs from trajectory data. The authors also introduce a new benchmark dataset, ODEBench, for evaluating dynamical SR methods. ODEFormer is shown to outperform existing methods in terms of robustness to noise and irregular sampling while maintaining computational efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and interesting, and the authors have done a good job of explaining the model architecture and training process.
- The authors have provided a new benchmark dataset, ODEBench, which will be useful for future research in this area.
- The experiments are thorough and demonstrate the effectiveness of ODEFormer on both synthetic and real-world datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the limitations of the proposed method. It would be helpful to discuss the types of ODEs that ODEFormer can and cannot handle, and the potential challenges in applying the method to more complex systems.
- The authors should provide more details on the computational cost of ODEFormer, including training and inference time, and compare it with other methods. It would also be helpful to discuss the scalability of the method to larger datasets and more complex models.
- The paper does not discuss the potential biases in the training data or the evaluation metrics. It would be helpful to analyze the impact of these biases on the performance of ODEFormer and to discuss potential ways to mitigate them.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of ODEFormer, particularly regarding the types of ODEs it can effectively handle. While the authors mention that the method can handle up to 4-dimensional systems, it is unclear what specific characteristics of these systems make them amenable to the proposed approach. For instance, are there limitations in terms of the complexity of the non-linearities, the presence of chaotic behavior, or the nature of the initial conditions? A detailed analysis of these aspects would provide a clearer understanding of the scope and applicability of ODEFormer. Furthermore, it would be valuable to explore the performance of the method on systems with known identifiability issues, as this could reveal potential weaknesses in the model's ability to recover the true underlying equations. This analysis should include a discussion of the sensitivity of the method to the choice of hyperparameters and the potential for overfitting to the training data.

In addition to the limitations, a more detailed analysis of the computational cost of ODEFormer is needed. The authors should provide a breakdown of the training and inference times, including the time spent on different stages of the process, such as data preprocessing, model training, and equation evaluation. This analysis should also compare the computational cost of ODEFormer with other existing methods for symbolic regression of ODEs. It would be beneficial to discuss the scalability of the method to larger datasets and more complex models, including the memory requirements and the potential for parallelization. Furthermore, the authors should investigate the impact of different model architectures and hyperparameters on the computational cost. This analysis should also consider the trade-offs between accuracy and computational efficiency, providing guidance on how to choose the appropriate model configuration for different applications.

Finally, the paper should address the potential biases in the training data and evaluation metrics. The authors should analyze the impact of these biases on the performance of ODEFormer and discuss potential ways to mitigate them. For example, if the training data is biased towards certain types of ODEs or initial conditions, the model may not generalize well to other scenarios. Similarly, if the evaluation metrics are not well-suited for the specific characteristics of the ODEs being considered, the results may be misleading. The authors should also discuss the limitations of the evaluation metrics and consider alternative metrics that may provide a more comprehensive assessment of the model's performance. This analysis should include a discussion of the potential for adversarial attacks on the model, where the input data is designed to mislead the model into producing incorrect equations.

### Questions

- How does ODEFormer handle systems with chaotic behavior or high-dimensional dynamics?
- What are the computational requirements for training and inference with ODEFormer, and how do they compare to other methods?
- Are there any potential biases in the training data or evaluation metrics that could affect the performance of ODEFormer?

### Rating

6

### Confidence

3

**********
