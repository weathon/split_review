### Summary

This paper presents a new model for time series forecasting, xLSTM-Mixer, which integrates a linear forecast with xLSTM blocks. The model is designed to effectively integrate temporal and variate mixing, and the authors claim that it outperforms existing state-of-the-art methods in long-term forecasting tasks. The paper provides extensive experimental results and ablation studies to support their claims.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-organized and clearly written, making it easy to follow the proposed methodology and experimental setup. The authors provide a thorough evaluation of their model, including comparisons with multiple baseline models and ablation studies to analyze the contribution of each component. The results demonstrate that the proposed model achieves competitive performance on various benchmark datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed model is limited. The core architecture is based on xLSTM, and the main contribution is the addition of a linear forecast component and multi-view mixing. While these additions may provide some performance improvements, they do not represent a significant departure from existing approaches. The paper does not sufficiently explore the novelty of the multi-view mixing approach, particularly in comparison to existing methods for handling multivariate time series data. It is unclear how this specific mixing strategy offers advantages over simpler alternatives, such as standard attention mechanisms or concatenation followed by a linear layer, especially given the computational overhead of the proposed method.
2. The paper lacks a detailed discussion of the limitations of the proposed model. For example, the authors do not address the computational cost of the model, especially when dealing with large datasets or long time series. Additionally, the sensitivity of the model to hyperparameter choices is not thoroughly explored, which is crucial for practical applications. The paper also does not discuss the potential impact of the model on real-world applications, such as the ethical implications of using the model in decision-making processes. Furthermore, the paper does not provide a clear analysis of the model's performance under different noise levels or in the presence of missing data, which are common in real-world time series datasets.

### Suggestions

The authors should provide a more detailed analysis of the multi-view mixing mechanism, including a comparison with other established methods for handling multivariate time series data. Specifically, they should investigate how the proposed method compares to standard attention mechanisms, concatenation followed by a linear layer, and other relevant techniques. This analysis should include a discussion of the computational complexity of each method and a comparison of their performance on a range of benchmark datasets. Furthermore, the authors should explore the impact of different mixing strategies on the model's ability to capture long-term dependencies and cross-variate relationships. This could involve conducting ablation studies to assess the contribution of each mixing component and analyzing the model's performance under different mixing configurations.

To address the lack of discussion on limitations, the authors should include a thorough analysis of the computational cost of the proposed model, including the number of parameters, training time, and inference time. They should also investigate the sensitivity of the model to hyperparameter choices and provide guidelines for selecting appropriate values. This could involve conducting a sensitivity analysis to assess the impact of different hyperparameters on the model's performance and providing a discussion of the trade-offs between model complexity and performance. Additionally, the authors should discuss the potential impact of the model on real-world applications, including the ethical implications of using the model in decision-making processes. This could involve a discussion of the model's potential biases and the steps that can be taken to mitigate these biases.

Finally, the authors should provide a more comprehensive evaluation of the model's performance under different conditions, including different noise levels and in the presence of missing data. This could involve conducting experiments on benchmark datasets with varying levels of noise and missing data and analyzing the model's performance under these conditions. The authors should also discuss the limitations of the model in these scenarios and suggest potential improvements. This analysis should include a discussion of the model's robustness to different types of data corruption and its ability to generalize to unseen data. The authors should also consider the impact of different data preprocessing techniques on the model's performance and provide guidelines for selecting appropriate preprocessing methods.

### Questions

1. How does the proposed model compare to other state-of-the-art models in terms of computational cost and memory usage?
2. What are the limitations of the proposed model, and how can these limitations be addressed in future work?
3. How does the model perform under different noise levels or in the presence of missing data?

### Rating

5

### Confidence

4

**********
