### Summary

This paper addresses the variable subset forecasting (VSF) problem, where the forecasting model is trained on complete time series but must predict missing variables during testing. The authors propose a novel framework called Shift-Resilient Diffusive Imputation (SRDI), which integrates divide-and-conquer strategies with the denoising process to handle inter-series shifts and a meta-learning paradigm to address intra-series shifts. The method decomposes the input time series into invariant and variant patterns, which are then processed separately to improve forecasting performance. Extensive experiments on four datasets demonstrate that SRDI outperforms state-of-the-art methods, highlighting its effectiveness in handling distribution shifts.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow. The authors clearly articulate the problem, methodology, and experimental setup.

2. The proposed SRDI framework is innovative and addresses a practical challenge in time series forecasting. By combining divide-and-conquer strategies with a meta-learning paradigm, SRDI effectively handles distribution shifts caused by inter-series and intra-series variations.

3. The experimental results are compelling, with SRDI outperforming state-of-the-art methods on multiple datasets. The ablation studies provide valuable insights into the effectiveness of each component of the framework.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed SRDI framework. Understanding the time and space complexity is crucial for assessing its scalability and practical applicability, especially for large-scale time series datasets.

2. The paper could benefit from a more in-depth discussion of the limitations of the proposed method. For example, under what conditions might SRDI fail to perform well, and how could these limitations be addressed in future work?

3. While the paper compares SRDI with several state-of-the-art methods, it would be beneficial to include a discussion of the hyperparameter tuning process for each method. This would provide a more comprehensive comparison and ensure that the results are not biased by suboptimal hyperparameter settings.

### Suggestions

The paper would be significantly strengthened by a more thorough analysis of the computational demands of the SRDI framework. Specifically, the authors should provide a detailed breakdown of the time and space complexity associated with each component of the model, including the divide-and-conquer strategy and the meta-learning paradigm. This analysis should consider the impact of various factors, such as the length of the time series, the number of variables, and the size of the meta-learning model. Furthermore, it would be beneficial to include empirical results demonstrating the actual runtime and memory usage of SRDI on datasets of varying sizes. This would provide a more practical understanding of the framework's scalability and its suitability for real-world applications. Without this information, it is difficult to assess the feasibility of deploying SRDI in resource-constrained environments or with very large datasets.

In addition to the computational analysis, the paper should include a more detailed discussion of the limitations of the proposed SRDI framework. While the experimental results demonstrate its effectiveness in handling distribution shifts, it is important to acknowledge scenarios where the method might not perform optimally. For instance, the authors should discuss the potential impact of highly non-stationary time series or the presence of extreme outliers. Furthermore, it would be valuable to explore the sensitivity of SRDI to the choice of hyperparameters and the potential for overfitting. A thorough discussion of these limitations would provide a more balanced perspective on the method's strengths and weaknesses and would help guide future research in this area. This discussion should also include potential failure modes and how the method might be adapted to handle such cases.

Finally, the paper should provide a more detailed description of the hyperparameter tuning process for both SRDI and the baseline methods. This should include a discussion of the range of hyperparameters explored, the optimization algorithm used, and the criteria for selecting the best hyperparameters. It is crucial to ensure that the comparison between SRDI and other methods is fair and that the results are not biased by suboptimal hyperparameter settings. For example, the authors should specify whether a grid search, random search, or Bayesian optimization was used, and they should provide details on the computational resources allocated for hyperparameter tuning. This level of detail is essential for reproducibility and for ensuring that the reported performance gains are genuine and not an artifact of the hyperparameter selection process.

### Questions

1. Could you provide more details on the computational complexity of the SRDI framework, particularly in terms of time and space requirements?

2. How sensitive is SRDI to the choice of hyperparameters, and what strategies were used for hyperparameter tuning?

3. Are there specific scenarios or types of time series where SRDI might not perform as well as other methods?

### Rating

6

### Confidence

4

**********
