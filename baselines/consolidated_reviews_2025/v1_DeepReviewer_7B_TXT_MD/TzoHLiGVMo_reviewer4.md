### Summary

This paper introduces ODEFormer, a transformer-based model designed for inferring multidimensional ordinary differential equations (ODEs) from noisy, irregularly sampled time series data. The authors also present ODEBench, a benchmark dataset for evaluating dynamical system regression methods. ODEFormer is shown to outperform existing methods in terms of robustness to noise and irregular sampling while maintaining computational efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and interesting.
- The authors have provided a new benchmark dataset, ODEBench, which will be useful for future research in this area.
- The experiments are thorough and demonstrate the effectiveness of ODEFormer on both synthetic and real-world datasets.

### Weaknesses

#### Some Related Works

[1] Neural controlled differential equations for irregular time series.
[2] Learning stochastic differential equations with neural networks.
[3] Learning neural controlled differential equations with -stochatsiic interpolants.
[4] Learning stochastic differential equations with deep learning: A hybrid framework combining deep learning and numerical methods.
[5] Learning neural controlled differential equations for irregular sequential data.

#### comment

 - The paper does not provide a detailed analysis of the limitations of the proposed method. It would be helpful to discuss the types of ODEs that ODEFormer can and cannot handle, and the potential challenges in applying the method to more complex systems.
- The authors should provide more details on the computational cost of ODEFormer, including training and inference time, and compare it with other methods. It would also be helpful to discuss the scalability of the method to larger datasets and more complex models.
- The paper does not discuss the potential biases in the training data or the evaluation metrics. It would be helpful to analyze the impact of these biases on the performance of ODEFormer and to discuss potential ways to mitigate them.

### Suggestions

The authors should provide a more detailed analysis of the limitations of ODEFormer, particularly regarding the types of ODEs it can effectively handle. While the method is presented as general, it is crucial to understand its boundaries. For instance, are there specific characteristics of ODEs, such as stiffness or high dimensionality, that pose challenges? A discussion of the model's sensitivity to the complexity of the underlying dynamics, perhaps through a systematic analysis of performance across different ODE families, would be beneficial. Furthermore, the paper should explore the performance of ODEFormer on systems with known identifiability issues, as this could reveal potential weaknesses in the model's ability to recover the true underlying equations. This analysis should include a discussion of the model's sensitivity to the choice of hyperparameters and the potential for overfitting to the training data. 

Regarding computational cost, the authors should provide a more detailed breakdown of the training and inference times for ODEFormer, including the time spent on different stages of the process, such as data preprocessing, model training, and equation evaluation. This should be compared with other existing methods for symbolic regression of ODEs, highlighting the trade-offs between accuracy and computational efficiency. It would be useful to discuss the memory requirements of the model and the potential for parallelization. The authors should also investigate the impact of different model architectures and hyperparameters on the computational cost. A more comprehensive analysis of the computational aspects would be valuable for assessing the practical applicability of ODEFormer. For example, the authors could explore the use of techniques like model pruning or quantization to reduce the computational footprint of the model without significantly sacrificing accuracy.

Finally, the authors should address the potential biases in the training data and evaluation metrics. They should analyze the impact of these biases on the performance of ODEFormer and discuss potential ways to mitigate them. For example, if the training data is biased towards certain types of ODEs or initial conditions, the model may not generalize well to other scenarios. Similarly, if the evaluation metrics are not well-suited for the specific characteristics of the ODEs being considered, the results may be misleading. The authors should also discuss the limitations of the evaluation metrics and consider alternative metrics that may provide a more comprehensive assessment of the model's performance. This analysis should include a discussion of the potential for adversarial attacks on the model, where the input data is designed to mislead the model into producing incorrect equations. A more thorough discussion of these aspects would enhance the rigor and reliability of the paper.

### Questions

- Can ODEFormer handle systems with chaotic behavior or high-dimensional dynamics?
- What are the computational requirements for training and inference with ODEFormer, and how do they compare to other methods?
- Are there any potential biases in the training data or evaluation metrics that could affect the performance of ODEFormer?

### Rating

8

### Confidence

3

**********
