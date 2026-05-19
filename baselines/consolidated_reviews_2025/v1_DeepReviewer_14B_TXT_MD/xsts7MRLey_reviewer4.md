### Summary

The paper presents a benchmark for evaluating unsupervised domain adaptation (UDA) methods for time series classification. It introduces seven new datasets and evaluates nine UDA algorithms with state-of-the-art neural network backbones. The benchmark provides insights into the strengths and limitations of different UDA approaches and serves as a valuable resource for researchers and practitioners working on domain adaptation for time series data.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper addresses an important and underexplored area of research: unsupervised domain adaptation for time series classification. The proposed benchmark fills a gap in the literature by providing a standardized framework for evaluating UDA methods for time series data.
2. The authors introduce seven new benchmark datasets covering various domain shifts and temporal dynamics, which is a significant contribution to the field.
3. The paper evaluates nine UDA algorithms with state-of-the-art neural network backbones, providing a thorough comparison of different approaches. The results offer insights into the strengths and limitations of each method and can guide researchers and practitioners in selecting appropriate techniques for their specific applications.
4. The paper is well-written and organized, making it easy to follow and understand.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses primarily on deep learning-based UDA methods. It would be beneficial to include a discussion of traditional machine learning approaches for time series domain adaptation and how they compare to deep learning methods. This would provide a more comprehensive view of the field and help readers understand the trade-offs between different approaches.
2. The paper could provide more details on the computational cost and efficiency of the evaluated UDA algorithms. This information is crucial for practitioners who need to consider the trade-off between performance and computational resources when selecting a UDA method.
3. The paper could benefit from a more in-depth analysis of the impact of different hyperparameter settings on the performance of UDA algorithms. A sensitivity analysis of key hyperparameters would provide valuable insights into the robustness of the methods and help practitioners tune their models effectively.

### Suggestions

The paper would be significantly strengthened by expanding the discussion to include traditional machine learning methods for time series domain adaptation. While deep learning methods have shown promise, it is crucial to understand how they compare to established techniques such as kernel-based methods, ensemble methods, or feature alignment techniques that are not based on deep neural networks. A comparative analysis, even if brief, would provide a more complete picture of the landscape of time series domain adaptation. For example, the authors could discuss how methods like Maximum Mean Discrepancy (MMD) or Correlation Alignment (CORAL) could be applied to time series data and how their performance compares to the deep learning approaches evaluated in the paper. This would not only broaden the scope of the paper but also provide valuable insights for practitioners who may be working with limited computational resources or who prefer simpler, more interpretable models.

Furthermore, the paper should include a more detailed analysis of the computational cost associated with each UDA algorithm. This should go beyond simply reporting the training time and should include an analysis of the memory requirements, the number of parameters, and the inference time. This information is critical for practitioners who need to choose an algorithm that is not only accurate but also computationally feasible for their specific application. For example, some deep learning models may achieve high accuracy but require significant computational resources, making them impractical for real-time applications or deployment on resource-constrained devices. The authors could also discuss the scalability of each algorithm with respect to the size of the dataset and the length of the time series. This would allow practitioners to make informed decisions about which algorithm is most suitable for their specific needs.

Finally, a more thorough investigation into the impact of hyperparameter settings is needed. The paper should include a sensitivity analysis of the key hyperparameters for each UDA algorithm, such as learning rate, batch size, and regularization parameters. This analysis should explore how the performance of each algorithm varies as these hyperparameters are changed. This would provide valuable insights into the robustness of each method and help practitioners to tune their models effectively. For example, the authors could show how the performance of a specific algorithm changes as the learning rate is varied or how the choice of batch size affects the convergence of the model. This would not only improve the reproducibility of the results but also provide practical guidance for practitioners who are looking to apply these methods to their own data.

### Questions

1. How do traditional machine learning methods for time series domain adaptation compare to the deep learning methods evaluated in the paper?
2. What is the computational cost and efficiency of the evaluated UDA algorithms?
3. How do different hyperparameter settings impact the performance of UDA algorithms for time series classification?

### Rating

8: accept, good paper

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
