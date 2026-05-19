### Summary

This paper proposes Swin4TS algorithm, which incorporates the window-based attention and hierarchical representation techniques from the Swin Transformer and applies them to the long-term forecasting of time series data. The proposed method achieves state-of-the-art performance on 8 benchmark datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The authors propose a new method for long-term time series forecasting, which achieves state-of-the-art performance on 8 benchmark datasets.
2. The authors provide a comprehensive experimental analysis of the proposed method, including comparisons with other methods, ablation studies, and visualizations of the attention maps.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the proposed method has linear computational complexity, but do not provide a formal proof or analysis to support this claim.
2. The authors only provide the inference time and memory usage for one baseline model (PatchTST). A more comprehensive comparison with other baselines would be helpful for a thorough evaluation.
3. The authors do not discuss the limitations of the proposed method in detail.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational complexity of the proposed Swin4TS method. While the authors claim linear complexity, a formal proof or detailed analysis is needed to substantiate this claim. Specifically, the analysis should consider the complexity of the window-based attention mechanism and the hierarchical representation in relation to the input sequence length and the number of channels. It would be helpful to provide a breakdown of the computational cost for each component of the model, including the attention layers, feed-forward networks, and any other relevant operations. This analysis should also consider the impact of different hyperparameter choices, such as the window size and the number of attention heads, on the overall computational complexity. Furthermore, a comparison of the computational complexity of Swin4TS with other state-of-the-art methods, such as Transformer, Informer, Autoformer, FEDformer, PatchTST, Crossformer, and TimesNet, would provide a more comprehensive understanding of its efficiency. This comparison should not only focus on the theoretical complexity but also include empirical measurements of inference time and memory usage on a common hardware platform.

To provide a more thorough evaluation of the proposed method, the authors should include a more comprehensive comparison of inference time and memory usage with other baseline models. The current comparison is limited to PatchTST, which is insufficient to fully assess the computational efficiency of Swin4TS. A more detailed comparison should include a wider range of baseline models, such as Transformer, Informer, Autoformer, FEDformer, Crossformer, and TimesNet, to provide a more complete picture of the computational trade-offs. This comparison should be conducted on a common hardware platform and using a consistent evaluation protocol. The authors should also provide a detailed analysis of the memory usage of each model, including the memory required for storing the model parameters, intermediate activations, and other relevant data structures. This analysis should help to identify the bottlenecks in the proposed method and provide insights into potential areas for optimization. Furthermore, the authors should discuss the impact of different batch sizes on the inference time and memory usage of the proposed method and the baseline models.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method. This discussion should include a consideration of the factors that may affect the performance of Swin4TS, such as the quality and quantity of the training data, the complexity of the underlying time series patterns, and the presence of noise or outliers in the data. The authors should also discuss the potential failure cases of the proposed method and provide insights into the scenarios where it may not perform well. For example, it would be helpful to discuss how the method would handle time series with abrupt changes or non-stationary behavior. Additionally, the authors should discuss the sensitivity of the proposed method to different hyperparameter settings and provide guidelines for selecting appropriate values for these parameters. A more thorough discussion of the limitations of the proposed method would help to provide a more balanced and realistic assessment of its capabilities.

### Questions

1. Can you provide a formal proof or analysis to support the claim of linear computational complexity?
2. Can you provide a more comprehensive comparison of inference time and memory usage with other baselines?
3. What are the limitations of the proposed method? How does the effectiveness of Swin4TS/CD depend on the quality and quantity of the training data and the complexity of the underlying time series patterns?
4. How does the proposed method handle the uncertainty in the forecasting process?
5. How does the proposed method compare to other state-of-the-art methods in terms of interpretability? Can you provide some insights into the learned representations and attention patterns?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
