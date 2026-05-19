### Summary

This paper proposes a novel framework called Shift-Resilient Diffusive Imputation (SRDI) to address the variable subset forecasting (VSF) problem. The authors identify two types of distribution shift: inter-series shift and intra-series shift. They propose a divide-and-conquer strategy with the denoising process to decompose the input into invariant patterns and variant patterns, representing the temporally stable parts of inter-series correlation and the highly fluctuating parts, respectively. To handle intra-series shift, they introduce a meta-learning paradigm within the diffusion model to learn from a variety of distribution scenarios. Extensive experiments on four datasets demonstrate the superior performance of SRDI compared to state-of-the-art methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured and easy to follow. The authors clearly articulate the problem, motivation, and methodology, making it accessible to readers.
2. The proposed SRDI framework is innovative and addresses a practical challenge in time series forecasting. The decomposition of input patterns into invariant and variant parts is a novel approach that effectively mitigates the impact of inter-series shifts.
3. The paper provides extensive experimental results on four datasets, demonstrating the effectiveness of SRDI compared to state-of-the-art methods. The ablation studies further validate the contribution of each component in the proposed framework.
4. The paper includes a comprehensive discussion of related work, situating the proposed method within the broader context of time series forecasting and imputation techniques.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed SRDI framework. Understanding the time and space complexity is crucial for assessing its scalability and practical applicability, especially for large-scale time series datasets.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed method. For example, under what conditions might SRDI fail to perform well, and how could these limitations be addressed in future work?
3. While the paper compares SRDI with several state-of-the-art methods, it would be beneficial to include a discussion of the hyperparameter tuning process for each method. This would provide a more comprehensive comparison and ensure that the results are not biased by suboptimal hyperparameter settings.

### Suggestions

The authors should provide a more detailed analysis of the computational complexity of the SRDI framework. Specifically, they should analyze the time and space complexity of each component of the model, including the divide-and-conquer strategy and the meta-learning paradigm. This analysis should consider the impact of various factors, such as the length of the time series, the number of variables, and the size of the meta-learning model. Furthermore, it would be beneficial to include empirical results demonstrating the actual runtime and memory usage of SRDI on datasets of varying sizes. This would provide a more practical understanding of the framework's scalability and its suitability for real-world applications. Without this information, it is difficult to assess the feasibility of deploying SRDI in resource-constrained environments or with very large datasets.

In addition to the computational analysis, the paper should include a more thorough discussion of the limitations of the proposed method. The authors should acknowledge scenarios where SRDI might not perform optimally. For instance, they should discuss the potential impact of highly non-stationary time series or the presence of extreme outliers. Furthermore, it would be valuable to explore the sensitivity of SRDI to the choice of hyperparameters and the potential for overfitting. A thorough discussion of these limitations would provide a more balanced perspective on the method's strengths and weaknesses and would help guide future research in this area. This discussion should also include potential failure modes and how the method might be adapted to handle such cases.

Finally, the paper should provide a more detailed description of the hyperparameter tuning process for both SRDI and the baseline methods. This should include a discussion of the range of hyperparameters explored, the optimization algorithm used, and the criteria for selecting the best hyperparameters. It is crucial to ensure that the comparison between SRDI and other methods is fair and that the results are not biased by suboptimal hyperparameter settings. For example, the authors should specify whether a grid search, random search, or Bayesian optimization was used, and they should provide details on the computational resources allocated for hyperparameter tuning. This level of detail is essential for reproducibility and for ensuring that the reported performance gains are genuine and not an artifact of the hyperparameter selection process.

### Questions

1. Could you provide more details on the computational complexity of the SRDI framework, particularly in terms of time and space requirements?
2. How sensitive is SRDI to the choice of hyperparameters, and what strategies were used for hyperparameter tuning?
3. Are there specific scenarios or types of time series where SRDI might not perform as well as other methods?

### Rating

6

### Confidence

3

**********
