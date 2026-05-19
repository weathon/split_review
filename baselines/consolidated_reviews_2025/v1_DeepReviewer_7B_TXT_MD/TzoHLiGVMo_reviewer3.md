### Summary

The authors introduce ODEFormer, a transformer-based model for inferring multidimensional ordinary differential equations (ODEs) from noisy, irregularly sampled time series data. They also introduce ODEBench, a new benchmark dataset for evaluating dynamical system regression methods. ODEFormer is shown to outperform existing methods in terms of robustness to noise and irregular sampling while maintaining computational efficiency.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The authors have provided a new benchmark dataset, ODEBench, which will be useful for future research in this area.
4. The experiments are thorough and demonstrate the effectiveness of ODEFormer on both synthetic and real-world datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the limitations of the proposed method. It would be helpful to discuss the types of ODEs that ODEFormer can and cannot handle, and the potential challenges in applying the method to more complex systems.
2. The authors should provide more details on the computational cost of ODEFormer, including training and inference time, and compare it with other methods. It would also be helpful to discuss the scalability of the method to larger datasets and more complex models.
3. The paper does not discuss the potential biases in the training data or the evaluation metrics. It would be helpful to analyze the impact of these biases on the performance of ODEFormer and to discuss potential ways to mitigate them.

### Suggestions

The authors should provide a more thorough analysis of the limitations of ODEFormer. Specifically, they should discuss the types of ODEs that the model is likely to struggle with, such as those with highly chaotic behavior or those with very high dimensionality. It would be beneficial to include a discussion of the model's sensitivity to the choice of hyperparameters and the potential for overfitting to the training data. Furthermore, the authors should explore the performance of the method on systems with known identifiability issues, as this could reveal potential weaknesses in the model's ability to recover the true underlying equations. A more detailed analysis of the model's limitations would provide a more balanced view of its capabilities and applicability.

Regarding computational cost, the authors should provide a more detailed breakdown of the training and inference times for ODEFormer, including the time spent on different stages of the process. This should include a comparison with other existing methods for symbolic regression of ODEs, highlighting the trade-offs between accuracy and computational efficiency. It would be useful to discuss the memory requirements of the model and the potential for parallelization. The authors should also investigate the impact of different model architectures and hyperparameters on the computational cost. A more comprehensive analysis of the computational aspects would be valuable for assessing the practical applicability of ODEFormer.

Finally, the authors should address the potential biases in the training data and evaluation metrics. They should analyze the impact of these biases on the performance of ODEFormer and discuss potential ways to mitigate them. For example, if the training data is biased towards certain types of ODEs or initial conditions, the model may not generalize well to other scenarios. Similarly, if the evaluation metrics are not well-suited for the specific characteristics of the ODEs being considered, the results may be misleading. The authors should also discuss the limitations of the evaluation metrics and consider alternative metrics that may provide a more comprehensive assessment of the model's performance. A more thorough discussion of these aspects would enhance the rigor and reliability of the paper.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
