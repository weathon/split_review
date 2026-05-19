### Summary

This paper proposes a new dataset condensation method specifically designed for hyperparameter optimization. The authors introduce the concept of hyperparameter calibration, which ensures that the performance rankings of different hyperparameters are preserved between the original and condensed datasets. To achieve this, they propose an objective function that aligns the hyperparameter gradients between the original and condensed datasets. The authors also provide a theoretical analysis of the proposed method and demonstrate its effectiveness through experiments on image classification tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel perspective on dataset condensation by focusing on hyperparameter optimization, which is an important aspect of machine learning.
2. The authors provide a theoretical analysis of the proposed method, demonstrating its effectiveness in preserving the performance rankings of different hyperparameters.
3. The experimental results show that the proposed method can significantly reduce the computational cost of hyperparameter optimization while maintaining the performance of the best hyperparameters found.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on image classification tasks. It would be beneficial to evaluate the proposed method on other types of tasks, such as natural language processing or time series analysis, to demonstrate its generalizability. The current evaluation is limited to image datasets, and it is unclear how the method would perform on tasks with different data modalities and characteristics. For example, the method's performance on sequence data or tabular data, which have different structural properties compared to images, remains unexplored.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to compare the computational cost of the proposed method with other dataset condensation methods and provide insights into the trade-off between computational cost and performance. While the paper claims reduced computational cost, a rigorous comparison with existing methods, including a breakdown of the computational overhead of each step, is missing. This makes it difficult to assess the practical benefits of the proposed approach.
3. The paper does not discuss the sensitivity of the proposed method to different hyperparameter settings. It would be helpful to analyze the impact of different hyperparameter settings on the performance of the proposed method and provide guidelines for selecting appropriate hyperparameter values. The method's performance might be highly dependent on the choice of hyperparameters, and without a sensitivity analysis, it is difficult to determine the robustness of the method and provide practical guidance for its use.

### Suggestions

To address the limitation of focusing solely on image classification, the authors should extend their evaluation to include tasks from other domains, such as natural language processing and time series analysis. For NLP, the method could be tested on tasks like text classification or sequence-to-sequence learning using datasets like SST or IMDB. For time series, the method could be evaluated on tasks like anomaly detection or forecasting using datasets like Traffic or Electricity. These additional experiments would provide a more comprehensive understanding of the method's generalizability and its ability to handle different data modalities. Furthermore, it would be beneficial to analyze the performance of the method on tasks with varying levels of complexity and data dimensionality to understand its limitations and strengths. This would involve testing the method on datasets with different characteristics, such as varying sequence lengths, feature dimensions, and data distributions.

To provide a more detailed analysis of the computational cost, the authors should compare the proposed method with other dataset condensation techniques, such as herding or gradient matching, in terms of both training time and memory usage. This comparison should include a breakdown of the computational cost of each step in the proposed method, such as the hyperparameter gradient alignment and the dataset condensation process. The authors should also provide a theoretical analysis of the computational complexity of the proposed method and compare it with the complexity of other methods. This analysis should consider the number of parameters, the size of the datasets, and the number of iterations required for convergence. Additionally, the authors should provide empirical results on the training time and memory usage of the proposed method and other methods on different datasets and hardware configurations. This would allow for a more informed assessment of the trade-off between computational cost and performance.

Finally, to address the sensitivity of the method to hyperparameter settings, the authors should conduct a thorough sensitivity analysis by varying the key hyperparameters of the proposed method and analyzing their impact on the performance. This analysis should include a discussion of the optimal range for each hyperparameter and the trade-offs between different settings. The authors should also provide guidelines for selecting appropriate hyperparameter values based on the characteristics of the dataset and the task. This could involve providing a set of rules of thumb or a more principled approach for hyperparameter selection. Furthermore, the authors should investigate the robustness of the method to different initializations and random seeds to ensure that the results are consistent and reliable. This would involve running the method multiple times with different initializations and random seeds and reporting the average performance and standard deviation.

### Questions

1. How does the proposed method perform on other types of tasks, such as natural language processing or time series analysis?
2. Can the authors provide a more detailed analysis of the computational cost of the proposed method and compare it with other dataset condensation methods?
3. How sensitive is the proposed method to different hyperparameter settings, and what are the guidelines for selecting appropriate hyperparameter values?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
