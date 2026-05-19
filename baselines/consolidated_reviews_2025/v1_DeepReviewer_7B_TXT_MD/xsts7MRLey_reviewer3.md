### Summary

This paper presents a benchmark for evaluating unsupervised domain adaptation (UDA) methods for time series classification. The benchmark includes seven new benchmark datasets covering various domain shifts and temporal dynamics, facilitating fair and standardized UDA method assessments. The authors provide a comprehensive evaluation of nine UDA algorithms, including both adversarial and non-adversarial approaches, and analyze the impact of hyperparameter tuning methods and model backbones on performance. The results highlight the strengths and limitations of different UDA methods, offering insights into their effectiveness and robustness across various datasets and scenarios.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper introduces a comprehensive benchmark for unsupervised domain adaptation (UDA) in time series classification, which is a significant contribution to the field. The benchmark includes seven new datasets covering various domain shifts and temporal dynamics, providing a diverse and challenging testbed for evaluating UDA methods.

2. The authors conduct a thorough evaluation of nine UDA algorithms, including both adversarial and non-adversarial approaches, and analyze the impact of hyperparameter tuning methods and model backbones on performance. This comprehensive evaluation provides valuable insights into the strengths and limitations of different UDA methods, offering guidance for future research and practical applications.

3. The paper is well-written and easy to follow, with clear explanations of the methodology, experimental setup, and results. The authors provide a detailed analysis of the benchmark datasets, UDA algorithms, and hyperparameter tuning methods, making the paper accessible to both researchers and practitioners in the field.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear motivation for why unsupervised domain adaptation is necessary for time series classification. The authors should provide more context on the challenges of time series classification and how UDA can address these challenges. Specifically, the paper lacks a discussion on the inherent difficulties in time series data, such as variable lengths, non-stationarity, and noise, and how these characteristics make unsupervised domain adaptation particularly relevant. A more detailed explanation of the practical scenarios where UDA would be beneficial would strengthen the paper's motivation.

2. The paper does not provide a clear explanation of the proposed method for selecting the best hyperparameters. The authors should provide more details on the method and its advantages over existing methods. The paper mentions using hyperparameter tuning methods but does not specify which methods were used (e.g., grid search, random search, Bayesian optimization) or how they were implemented. A more detailed explanation of the hyperparameter selection process, including the search space and evaluation metrics, is needed to assess the validity of the results.

3. The paper does not provide a clear comparison of the proposed method with existing methods. The authors should provide more details on the comparison and its significance. While the paper compares different UDA algorithms, it lacks a comparison with other hyperparameter tuning methods. The authors should clarify how their proposed method compares to existing hyperparameter optimization techniques in terms of performance, computational cost, and robustness. A more thorough analysis of the proposed method's performance relative to established baselines is necessary.

### Suggestions

To enhance the paper, the authors should begin by providing a more detailed discussion of the challenges inherent in time series classification, particularly focusing on the issues of variable length, non-stationarity, and noise. This discussion should be contextualized within real-world applications where these challenges are prevalent, such as in sensor data analysis or financial time series. The authors should then clearly articulate how unsupervised domain adaptation addresses these specific challenges, providing concrete examples of scenarios where UDA would be particularly advantageous. For instance, they could discuss how UDA can help in adapting models trained on data from a specific region to perform well on data from a different region with different environmental conditions, or how it can be used to adapt models trained on data from a specific time period to perform well on data from a future time period with different market trends. This would provide a stronger motivation for the proposed benchmark and its relevance to the broader field of time series analysis.

Furthermore, the paper needs to provide a more detailed explanation of the hyperparameter selection method. The authors should specify the exact hyperparameter tuning methods used, including the search space explored, the optimization algorithm (e.g., Bayesian optimization, random search), and the evaluation metrics used to assess the performance of different hyperparameter configurations. It is crucial to explain how the validation set is used to select the best hyperparameters and how this process is different from standard hyperparameter tuning approaches. The authors should also discuss the computational cost associated with their hyperparameter selection method and compare it to other existing methods. This would allow readers to better understand the trade-offs between performance and computational efficiency. A clear description of the hyperparameter tuning process is essential for the reproducibility and validity of the results.

Finally, the authors should include a more comprehensive comparison of their proposed method with existing hyperparameter tuning methods. This comparison should not only focus on performance metrics but also consider computational cost, robustness, and ease of implementation. The authors should clearly articulate the advantages and disadvantages of their method compared to other approaches, providing a more nuanced understanding of its contribution. For example, they could compare their method to Bayesian optimization techniques or other meta-learning approaches for hyperparameter tuning. This would help to position their work within the broader context of hyperparameter optimization and highlight its unique contributions. The comparison should also include a discussion of the limitations of the proposed method and potential areas for future improvement.

### Questions

1. What is the motivation for using unsupervised domain adaptation for time series classification? How does it address the specific challenges of time series data?

2. How does the proposed method for selecting the best hyperparameters compare to existing methods? What are its advantages and limitations?

3. How does the proposed method compare to other hyperparameter tuning methods in terms of performance, computational cost, and robustness?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
