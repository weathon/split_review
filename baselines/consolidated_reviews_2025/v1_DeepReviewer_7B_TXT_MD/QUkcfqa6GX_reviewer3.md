### Summary

This paper presents a novel framework called STLLM (Spatio-Temporal Graph Learning with Large Language Model), which integrates LLMs with a cross-view mutual information maximization paradigm to capture implicit spatio-temporal dependencies and preserve point of interest information across urban space. The proposed method is evaluated on three distinct prediction tasks: crime prediction, traffic flow forecasting, and property price prediction. The results show that STLLM outperforms state-of-the-art baselines in various prediction tasks, demonstrating its effectiveness in capturing complex spatio-temporal patterns.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel framework that combines LLMs with a cross-view mutual information maximization paradigm to capture implicit spatio-temporal dependencies and preserve point of interest information across urban space. This approach is innovative and addresses the limitations of traditional methods that rely on predefined graph structures.
2. The paper provides a comprehensive evaluation of the proposed method on three distinct prediction tasks: crime prediction, traffic flow forecasting, and property price prediction. The results demonstrate that STLLM outperforms state-of-the-art baselines in various prediction tasks, showcasing its effectiveness in capturing complex spatio-temporal patterns.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of the limitations of the proposed method. For example, the authors do not discuss the computational complexity of the proposed method, especially when dealing with large-scale urban datasets. The paper also does not discuss the sensitivity of the proposed method to hyperparameter settings, such as the learning rate, the number of LLM layers, and the size of the GNN. It is unclear how these parameters affect the performance of the model and how they should be tuned for different datasets.
2. The paper does not provide a detailed analysis of the interpretability of the proposed method. While the authors claim that the LLM-based knowledge can serve as robust and invariant representations, it is not clear how the LLM's output can be interpreted in the context of spatio-temporal data. The paper should provide a more detailed analysis of the LLM's output and how it relates to the underlying spatio-temporal patterns. It would be beneficial to visualize the learned representations and provide insights into how the LLM captures spatial and temporal dependencies.
3. The paper does not provide a comparison with other state-of-the-art methods that use LLMs for spatio-temporal data analysis. While the authors compare their method with traditional GNN-based methods, it is not clear how the proposed method compares with other LLM-based methods for spatio-temporal data analysis. The paper should include a more comprehensive comparison with other state-of-the-art methods to demonstrate the advantages of the proposed method.

### Suggestions

The paper should include a more detailed analysis of the computational complexity of the proposed method. Specifically, the authors should provide a theoretical analysis of the time and space complexity of the algorithm, and they should also provide empirical results on the runtime and memory usage of the model on different datasets. This analysis should include a discussion of how the computational cost scales with the size of the input data, the number of LLM layers, and the size of the GNN. Furthermore, the authors should provide guidelines on how to choose the hyperparameters of the model, such as the learning rate, the number of LLM layers, and the size of the GNN, to achieve optimal performance. This should include a sensitivity analysis of the model's performance to different hyperparameter settings, and it should also provide practical recommendations for tuning the model for different datasets. The authors should also discuss the limitations of the proposed method in terms of computational cost and scalability, and they should suggest potential solutions to address these limitations.

To improve the interpretability of the proposed method, the authors should provide a more detailed analysis of the LLM's output and how it relates to the underlying spatio-temporal patterns. This could include visualizing the learned representations and providing insights into how the LLM captures spatial and temporal dependencies. For example, the authors could use attention maps to visualize which parts of the input data the LLM is focusing on, and they could also provide a qualitative analysis of the LLM's output to understand what kind of information it is capturing. The authors should also discuss the limitations of the LLM's interpretability and suggest potential solutions to improve it. This could include using techniques such as feature importance analysis or counterfactual analysis to understand how the LLM's output is affected by different input features. The authors should also discuss the potential ethical implications of using LLMs for spatio-temporal data analysis, such as the risk of bias and the potential for misuse.

The paper should include a more comprehensive comparison with other state-of-the-art methods that use LLMs for spatio-temporal data analysis. This comparison should include both quantitative and qualitative analysis, and it should also discuss the strengths and weaknesses of each method. The authors should also discuss the potential advantages of the proposed method over other LLM-based methods, such as its ability to capture implicit spatio-temporal dependencies and preserve point of interest information. The authors should also discuss the limitations of the proposed method in terms of its performance compared to other LLM-based methods, and they should suggest potential solutions to address these limitations. This comparison should include a discussion of the different types of LLMs that have been used for spatio-temporal data analysis, and it should also discuss the different techniques that have been used to integrate LLMs with GNNs.

### Questions

1. How does the proposed method handle the curse of dimensionality in high-dimensional spatio-temporal data?
2. How does the proposed method ensure the privacy of the data, especially when dealing with sensitive information such as crime data or traffic patterns?
3. How does the proposed method handle the uncertainty and noise in the data, especially when dealing with real-world datasets?

### Rating

5

### Confidence

4

**********
