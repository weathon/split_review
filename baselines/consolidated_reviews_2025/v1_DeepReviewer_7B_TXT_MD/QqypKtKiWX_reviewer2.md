### Summary

This paper proposes a simple data-parameter balancing framework for ventricular arrhythmia origin localization. The authors introduce an onset-based data augmentation strategy to expand the training dataset and a small-scale 1D convolution model to balance the relationship between the available training data and model complexity. The proposed method is evaluated on a pacing-site dataset and achieves a localization error of 9.83 mm, which is below the clinical acceptable error of 10 mm.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-organized and easy to follow.
2. The authors provide a comprehensive discussion of related work, highlighting the limitations of existing methods and the advantages of the proposed approach.
3. The authors conduct extensive experiments to evaluate the performance of the proposed method, including comparisons with state-of-the-art methods and ablation studies to analyze the impact of different components.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The authors primarily focus on data augmentation and model architecture, which have been widely explored in previous studies. The specific combination of these techniques, while potentially effective, does not represent a significant departure from existing approaches in the field of ECG analysis and arrhythmia localization. The paper lacks a clear articulation of how the proposed data augmentation strategy differs from existing methods, and how the specific model architecture is tailored to the problem beyond a general small-scale convolutional approach.
2. The paper lacks a detailed analysis of the computational complexity and efficiency of the proposed method. The authors do not provide information on training time, inference time, or memory usage, which are critical for assessing the practical applicability of the method, especially in resource-constrained environments. This omission makes it difficult to evaluate the trade-offs between performance and computational cost.
3. The authors do not provide a thorough discussion of the limitations of the proposed method. For example, the performance of the method under different recording conditions, such as varying noise levels or different sampling rates, is not explored. The paper also does not discuss the potential for overfitting or the generalizability of the method to different patient populations or arrhythmia types. This lack of discussion limits the understanding of the method's robustness and applicability.
4. The authors do not provide a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. The paper mentions specific hyperparameters, such as the learning rate and batch size, but does not provide a systematic analysis of how these parameters affect the training process and the final performance. This lack of analysis makes it difficult to reproduce the results and to understand the sensitivity of the method to different parameter settings.

### Suggestions

The authors should provide a more detailed explanation of the novelty of their approach, specifically highlighting how their data augmentation strategy and model architecture differ from existing methods. A more thorough comparison with related work, including a discussion of the specific advantages and disadvantages of each approach, would be beneficial. The authors should also clarify the specific design choices in their model architecture and explain why these choices are suitable for the task of ventricular arrhythmia origin localization. For example, they could discuss the specific type of convolutional layers used, the number of filters, and the activation functions, and justify these choices with respect to the characteristics of the ECG signals and the localization task. Furthermore, a more detailed analysis of the data augmentation strategy is needed, including a discussion of the specific parameters used and their impact on the performance of the method. This would help to demonstrate the effectiveness of the proposed approach and to provide a more comprehensive understanding of the method's behavior.

To address the lack of computational analysis, the authors should include a detailed evaluation of the computational complexity and efficiency of their method. This should include a comparison of the training time, inference time, and memory usage of the proposed method with other state-of-the-art methods. The authors should also discuss the scalability of their method and its suitability for real-time applications. This analysis should be performed on different hardware platforms to provide a more comprehensive understanding of the method's performance. Furthermore, the authors should discuss the potential for optimizing the method for resource-constrained environments, such as mobile devices or embedded systems. This could include techniques such as model pruning, quantization, or knowledge distillation.

The authors should also provide a more thorough discussion of the limitations of their method, including an analysis of its performance under different recording conditions, such as varying noise levels, different sampling rates, and different patient populations. This analysis should include a discussion of the potential for overfitting and the generalizability of the method to different arrhythmia types. The authors should also discuss the potential for bias in the training data and its impact on the performance of the method. Furthermore, the authors should provide a systematic analysis of the impact of different hyperparameters on the performance of the proposed method. This should include a discussion of the sensitivity of the method to different parameter settings and a discussion of the optimal parameter values for different scenarios. This analysis should be performed using techniques such as grid search or random search, and the results should be presented in a clear and concise manner.

### Questions

1. How does the proposed method compare to other state-of-the-art methods in terms of computational complexity and efficiency?
2. What are the limitations of the proposed method, and how might these limitations affect its performance in real-world applications?
3. How sensitive is the proposed method to different hyperparameters, and what are the optimal parameter values for different scenarios?

### Rating

3

### Confidence

4

**********
