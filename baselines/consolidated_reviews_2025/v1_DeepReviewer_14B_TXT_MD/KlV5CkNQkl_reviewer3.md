### Summary

The paper introduces a novel instance-level, example-based explanation method called Highly-precise and Data-centric Explanation (HD-Explain). This method leverages the properties of Kernelized Stein Discrepancy (KSD) to identify training samples that provide the best predictive support for a given test point. The authors demonstrate the effectiveness of HD-Explain through experiments on multiple classification tasks, showing improvements in preciseness, consistency, and computational efficiency compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-organized and easy to follow.

2. The proposed method is novel, simple, effective, and efficient.

3. The experimental results are comprehensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details on the experimental setup, including the specific models used and the hyperparameter settings for each method. This information is crucial for reproducibility and for understanding the performance of the proposed method in different contexts. For example, it is unclear what specific architectures were used for the ResNet-18 model, and what optimization algorithms and learning rates were employed during training. Furthermore, the hyperparameter settings for the baseline methods, such as the influence function and TracIn, are not specified, making it difficult to assess the fairness of the comparison.

2. The authors should also consider evaluating the proposed method on more diverse datasets and tasks to demonstrate its generalizability. The current evaluation is limited to image classification tasks, and it is unclear how the method would perform on other types of data, such as text or time-series data. Additionally, the method's performance on tasks with different levels of complexity should be investigated to assess its robustness. For example, evaluating on datasets with varying degrees of class imbalance or noise would provide a more comprehensive understanding of the method's capabilities.

3. The authors should provide a more detailed analysis of the computational cost of the proposed method, especially in comparison to existing methods. While the paper claims computational efficiency, a more rigorous analysis is needed, including a breakdown of the time complexity of each step in the algorithm. For example, the time required to compute the Kernelized Stein Discrepancy should be analyzed in relation to the size of the training dataset and the dimensionality of the input features. Furthermore, a comparison of the actual runtime of the proposed method with the baselines on different hardware configurations would be beneficial.

### Suggestions

To enhance the reproducibility and understanding of the proposed method, the authors should provide a detailed description of the experimental setup. This should include the specific architectures used for each model, such as the number of layers and the activation functions in the ResNet-18 model. The optimization algorithms, learning rates, and other hyperparameters used during training should also be clearly stated. For the baseline methods, the authors should specify the hyperparameter settings used, such as the number of steps for iterative methods or the regularization parameters for methods that involve optimization. This level of detail is crucial for other researchers to replicate the results and to understand the performance of the proposed method in different contexts. Furthermore, the authors should consider releasing the code and the trained models to facilitate reproducibility.

To demonstrate the generalizability of the proposed method, the authors should evaluate it on a wider range of datasets and tasks. This should include datasets from different domains, such as text, time-series, and tabular data. The authors should also consider evaluating the method on tasks with different levels of complexity, such as multi-class classification, regression, and anomaly detection. This would provide a more comprehensive understanding of the method's capabilities and limitations. For example, evaluating on datasets with varying degrees of class imbalance or noise would provide a more comprehensive understanding of the method's capabilities. Additionally, the authors should analyze the performance of the method on datasets with different sizes to assess its scalability.

Finally, the authors should provide a more detailed analysis of the computational cost of the proposed method. This should include a breakdown of the time complexity of each step in the algorithm, such as the computation of the Kernelized Stein Discrepancy and the selection of the most influential training samples. The authors should also compare the actual runtime of the proposed method with the baselines on different hardware configurations. This analysis should include the time required for both training and inference. Furthermore, the authors should discuss the memory requirements of the proposed method and how they scale with the size of the training dataset. This detailed analysis would provide a more complete picture of the computational efficiency of the proposed method.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
