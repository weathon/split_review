### Summary

The paper introduces a new model called xLSTM-Mixer, which is a novel approach to time series forecasting. The model integrates temporal and variate mixing within the xLSTM architecture to improve long-term forecasting accuracy. The authors claim that xLSTM-Mixer outperforms existing state-of-the-art methods on various benchmark datasets and provide extensive evaluations and ablation studies to support their claims.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel combination of techniques in the xLSTM architecture, specifically addressing the challenges of temporal and variate mixing in time series forecasting.
2. The authors provide extensive experimental results across multiple datasets, demonstrating the effectiveness of xLSTM-Mixer in long-term forecasting tasks.
3. The paper includes an ablation study to analyze the contribution of each component in the model, providing insights into its design choices.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's novelty is somewhat limited as it primarily builds upon the existing xLSTM architecture, with the main contribution being the addition of a linear forecast component and multi-view mixing. The integration of these components, while potentially effective, does not introduce a fundamentally new approach to time series forecasting. The core mechanism of xLSTM remains largely unchanged, and the modifications, though present, do not represent a significant departure from the original architecture's design principles.
2. The paper lacks a detailed discussion of the limitations of the proposed method and potential areas for future research. For example, the paper does not address the computational cost of the model, especially when dealing with large datasets or long time series. Furthermore, the sensitivity of the model to hyperparameter choices is not thoroughly explored, which is crucial for practical applications. The absence of a discussion on the model's performance under noisy or non-stationary conditions also limits the understanding of its robustness.
3. The paper's writing could be improved for clarity and conciseness. There are instances of redundant phrasing and overly complex sentence structures that make it difficult to follow the authors' arguments. For example, the description of the multi-view mixing mechanism could be simplified to enhance readability. The use of technical jargon without sufficient explanation also contributes to the lack of clarity.

### Suggestions

The authors should provide a more detailed analysis of the computational complexity of the xLSTM-Mixer, including both training and inference time. This analysis should consider the impact of the number of variates, the length of the time series, and the model's hyperparameters on the computational cost. Furthermore, it would be beneficial to compare the computational efficiency of xLSTM-Mixer with other state-of-the-art time series forecasting models. This would help to contextualize the practical applicability of the proposed method, especially in resource-constrained environments. The authors should also investigate and discuss the sensitivity of the model's performance to different hyperparameter settings. A thorough hyperparameter sensitivity analysis would provide valuable insights into the robustness and generalizability of the model. This analysis should include a discussion of how to choose appropriate hyperparameter values for different datasets and forecasting tasks. The authors should also explore the model's performance under various challenging conditions, such as noisy data, non-stationary time series, and missing values. This would help to assess the robustness of the model and identify potential limitations. 

To improve the clarity of the paper, the authors should revise the writing to eliminate redundant phrasing and overly complex sentence structures. The description of the multi-view mixing mechanism should be simplified to enhance readability. The authors should also provide more detailed explanations of technical jargon, making the paper more accessible to a wider audience. The paper would benefit from a more structured presentation of the experimental results, with a clear separation of the main findings from the supporting evidence. The authors should also consider including visualizations of the model's performance, such as plots of the predicted versus actual values, to provide a more intuitive understanding of the model's behavior. The discussion of the results should be more focused, highlighting the key contributions of the paper and the limitations of the proposed method. 

Finally, the authors should provide a more comprehensive discussion of the potential applications of xLSTM-Mixer in real-world scenarios. This discussion should include specific examples of how the model could be used in different domains, such as finance, energy, and healthcare. The authors should also address the ethical implications of using the model, particularly in high-stakes applications. This discussion should include a consideration of the potential for bias and discrimination, as well as the need for transparency and accountability. The authors should also discuss the limitations of the model and suggest potential directions for future research. This would help to contextualize the contributions of the paper and provide a roadmap for future work in this area.

### Questions

1. Could the authors provide more details on the computational complexity of the xLSTM-Mixer, especially when dealing with large datasets or long time series?
2. How sensitive is the performance of xLSTM-Mixer to different hyperparameter settings, and what guidelines can the authors provide for selecting appropriate values?
3. What are the potential limitations of the proposed method, and how might it be improved for future research?

### Rating

3

### Confidence

4

**********
