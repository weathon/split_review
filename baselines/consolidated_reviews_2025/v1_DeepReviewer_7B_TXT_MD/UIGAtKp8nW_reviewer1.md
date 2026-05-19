### Summary

This paper presents a benchmark to evaluate uncertainty quantification (UQ) methods for molecular representation models. The authors evaluate different uncertainty quantification methods with four pre-trained molecular representation models on multiple datasets. The authors find that Deep Ensembles consistently improve performance compared to deterministic baselines. Temperature Scaling and MC Dropout are effective for classification tasks, while BBP and SGLD are better for regression tasks. The authors also find that Uni-Mol, which uses 3D molecular conformations, is prone to overconfidence.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The paper provides a comprehensive evaluation of uncertainty quantification methods across different molecular representation models and datasets.
- The paper identifies trends in UQ method performance based on model architecture and task type.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear guideline on how to select the best UQ method for a given task and model architecture. The authors only provide a general guideline based on the type of task (classification vs. regression) and the architecture of the model (e.g., Uni-Mol vs. DNN). However, there is no clear explanation of how to choose the best UQ method for a specific task and model architecture. For example, the authors do not provide a detailed analysis of the trade-offs between different UQ methods in terms of computational cost, calibration performance, and uncertainty estimation accuracy. This makes it difficult for practitioners to choose the most appropriate UQ method for their specific needs.
- The paper does not provide a detailed analysis of the impact of different hyperparameters on the performance of UQ methods. The authors mention using coarse-grained hyperparameter grids, but there is no discussion of how these hyperparameters affect the results. For example, the authors do not analyze the sensitivity of the results to different learning rates, batch sizes, or optimization algorithms. This makes it difficult to reproduce the results and to apply the methods to new datasets.
- The paper does not provide a detailed analysis of the limitations of the proposed benchmark. The authors do not discuss the potential biases in the datasets or the limitations of the evaluation metrics. For example, the authors do not analyze the performance of the UQ methods on different subsets of the data or on different types of molecules. This makes it difficult to assess the generalizability of the results and to identify areas for future research.

### Suggestions

The paper would benefit from a more detailed analysis of the trade-offs between different uncertainty quantification (UQ) methods. The authors should provide a more granular analysis of the computational cost, calibration performance, and uncertainty estimation accuracy of each method, rather than just providing a general guideline based on task type and model architecture. For example, the authors could analyze the time complexity of each method, the calibration error (e.g., Expected Calibration Error, Maximum Calibration Error) on different datasets, and the variance of the uncertainty estimates. This analysis should be presented in a way that is easy to understand for practitioners, perhaps using tables or plots that summarize the key performance metrics for each method. Furthermore, the authors should provide specific recommendations on which UQ methods are most suitable for different types of molecular property prediction tasks, such as binding affinity prediction or ADMET property prediction. This would make the benchmark more useful for practitioners who need to choose the most appropriate UQ method for their specific application.

In addition, the paper should include a more detailed analysis of the impact of hyperparameters on the performance of UQ methods. The authors should conduct a sensitivity analysis of the key hyperparameters, such as the learning rate, batch size, and optimization algorithm, and report how these hyperparameters affect the results. For example, the authors could perform a grid search over a range of hyperparameter values and report the performance of each UQ method on different hyperparameter settings. This analysis should be presented in a way that is easy to understand for practitioners, perhaps using tables or plots that show how the performance of each method varies with different hyperparameter values. Furthermore, the authors should provide guidance on how to choose the optimal hyperparameters for each UQ method, based on the characteristics of the dataset and the task at hand. This would make the benchmark more robust and reliable, and would allow practitioners to apply the methods to new datasets with confidence.

Finally, the paper should include a more detailed analysis of the limitations of the proposed benchmark. The authors should discuss the potential biases in the datasets, such as the distribution of molecules or the types of properties being predicted, and how these biases might affect the results. For example, the authors could analyze the performance of the UQ methods on different subsets of the data, such as molecules with different sizes or different functional groups. The authors should also discuss the limitations of the evaluation metrics, such as the fact that they may not capture all aspects of uncertainty, and suggest alternative metrics that could be used. Furthermore, the authors should discuss the generalizability of the results to other datasets and tasks, and identify areas for future research. This would make the benchmark more transparent and would allow practitioners to understand the limitations of the results and to identify areas for future research.

### Questions

- How does the performance of UQ methods vary with different hyperparameters?
- What are the limitations of the proposed benchmark?
- How can the benchmark be improved to provide more guidance on UQ method selection?

### Rating

5

### Confidence

3

**********
