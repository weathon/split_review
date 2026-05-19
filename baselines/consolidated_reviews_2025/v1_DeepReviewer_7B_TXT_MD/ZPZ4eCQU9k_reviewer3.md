### Summary

This paper proposes xLSTM-Mixer, a model for time series forecasting that combines a linear forecast with xLSTM blocks. The authors claim that xLSTM-Mixer outperforms existing state-of-the-art methods on various benchmark datasets. The paper provides extensive experimental results and ablation studies to support their claims.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-organized and clearly written, making it easy to follow the proposed methodology and experimental setup.
2. The authors provide a thorough evaluation of their model, including comparisons with multiple baseline models and ablation studies to analyze the contribution of each component.
3. The results demonstrate that the proposed model achieves competitive performance on various benchmark datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed model is limited. The core architecture is based on xLSTM, and the main contribution is the addition of a linear forecast component and multi-view mixing. While these additions may provide some performance improvements, they do not represent a significant departure from existing approaches. The multi-view mixing, in particular, appears to be a relatively straightforward application of existing techniques, and the paper does not provide a strong justification for its specific design choices over other possible mixing strategies. The linear forecast component, while potentially useful, is also not a novel contribution in itself, and its integration with the xLSTM architecture seems incremental rather than transformative.
2. The paper lacks a detailed discussion of the limitations of the proposed model. For example, the authors do not address the computational cost of the model, especially when dealing with large datasets or long time series. Additionally, the sensitivity of the model to hyperparameter choices is not thoroughly explored, which is crucial for practical applications. The paper also does not discuss the potential impact of the model on real-world applications, such as the ethical implications of using the model in decision-making processes. Furthermore, the paper does not provide a clear analysis of the model's performance under different noise levels or in the presence of missing data, which are common in real-world time series datasets.

### Suggestions

The authors should provide a more detailed analysis of the multi-view mixing mechanism, including a comparison with other established methods for handling multivariate time series data. Specifically, they should investigate how the proposed method compares to standard attention mechanisms, concatenation followed by a linear layer, and other relevant techniques. This analysis should include a discussion of the computational complexity of each method and a comparison of their performance on a range of benchmark datasets. Furthermore, the authors should explore the impact of different mixing strategies on the model's ability to capture long-term dependencies and cross-variate relationships. This could involve conducting ablation studies to assess the contribution of each mixing component and analyzing the model's performance under different mixing configurations. A more thorough investigation into the design choices of the multi-view mixing is crucial to justify its novelty and effectiveness.

To address the lack of discussion on limitations, the authors should include a thorough analysis of the computational cost of the proposed model, including the number of parameters, training time, and inference time. They should also investigate the sensitivity of the model to hyperparameter choices and provide guidelines for selecting appropriate values. This could involve conducting a sensitivity analysis to assess the impact of different hyperparameters on the model's performance and providing a discussion of the trade-offs between model complexity and performance. Additionally, the authors should discuss the potential impact of the model on real-world applications, including the ethical implications of using the model in decision-making processes. This discussion should include an analysis of the model's potential biases and the steps that can be taken to mitigate these biases. The authors should also consider the impact of different data preprocessing techniques on the model's performance and provide guidelines for selecting appropriate preprocessing methods.

Finally, the authors should provide a more comprehensive evaluation of the model's performance under different conditions, including different noise levels and in the presence of missing data. This could involve conducting experiments on benchmark datasets with varying levels of noise and missing data and analyzing the model's performance under these conditions. The authors should also discuss the limitations of the model in these scenarios and suggest potential improvements. This analysis should include a discussion of the model's robustness to different types of data corruption and its ability to generalize to unseen data. The authors should also consider the impact of different data preprocessing techniques on the model's performance and provide guidelines for selecting appropriate preprocessing methods.

### Questions

1. How does the proposed model compare to other state-of-the-art models in terms of computational cost and memory usage?
2. What are the limitations of the proposed model, and how can these limitations be addressed in future work?
3. How does the model perform under different noise levels or in the presence of missing data?

### Rating

5

### Confidence

3

**********
