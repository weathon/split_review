### Summary

This paper proposes Pathformer, a multi-scale Transformer with adaptive pathways for time series forecasting. It integrates both temporal resolution and temporal distance for multi-scale modeling. Multi-scale division divides the time series into different temporal resolutions using patches of various sizes. Based on the division of each scale, dual attention is performed over these patches to capture global correlations and local details as temporal dependencies. We further enrich the multi-scale Transformer with adaptive pathways, which adaptively adjust the multi-scale modeling process based on the varying temporal dynamics of the input, improving the accuracy and generalization of Pathformer. Extensive experiments on eleven real-world datasets demonstrate that Pathformer not only achieves state-of-the-art performance by surpassing all current models but also exhibits stronger generalization abilities under various transfer scenarios.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.

2. The paper introduces a novel multi-scale Transformer model, Pathformer, which integrates both temporal resolution and temporal distance for multi-scale modeling. This is a unique approach compared to existing methods.

3. The paper demonstrates the superior performance of Pathformer through extensive experiments on eleven real-world datasets. The results show that Pathformer not only achieves state-of-the-art performance but also exhibits stronger generalization abilities under various transfer scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation of the paper is not clear. The authors claim that the incompleteness of multi-scale modeling and the fixed multi-scale modeling process are the two main challenges in Transformers for time series forecasting. However, it is not explained why these are the main challenges and how they affect the performance of time series forecasting. For example, the authors could provide some examples of time series data that exhibit different scales and fluctuations, and show how existing methods fail to capture these characteristics. Also, the authors should explain the meaning of temporal resolution and temporal distance more clearly, and how they relate to the multi-scale modeling problem.

2. The technical contribution is limited. The multi-scale division and dual attention mechanisms are similar to existing methods in CNN and Transformers. The main novelty seems to come from the adaptive pathways, but the details of how they work are not very clear. For example, how are the pathway weights generated and updated? How do they ensure the sparsity and diversity of the selected patch sizes? The authors should provide more analysis and explanation of the adaptive pathways mechanism, and compare it with other adaptive methods in the literature.

### Suggestions

The paper needs to significantly improve its motivation by providing concrete examples of time series data that exhibit multi-scale characteristics and demonstrating how existing methods struggle with these. For instance, the authors could show how a purely global model fails to capture rapid local fluctuations, or how a fixed multi-scale model might miss important temporal dynamics that vary across the time series. The concepts of temporal resolution and temporal distance should be defined more rigorously, perhaps with mathematical formulations, to clarify their role in the proposed multi-scale modeling approach. It would be beneficial to illustrate how different patch sizes relate to different temporal resolutions and how the dual attention mechanism captures both local and global dependencies at these resolutions. Furthermore, the authors should provide a more detailed explanation of how the adaptive pathways address the limitations of fixed multi-scale models, including a discussion of the trade-offs between model complexity and performance.

To enhance the technical contribution, the authors should provide a more in-depth analysis of the adaptive pathway mechanism. Specifically, the paper should detail the mathematical formulation of how pathway weights are generated and updated, including the specific functions used and the parameters involved. The authors should also explain how the model ensures sparsity and diversity in the selected patch sizes, and how these properties contribute to the model's performance. A comparison with other adaptive methods, such as those using reinforcement learning or evolutionary algorithms, would help to contextualize the novelty and effectiveness of the proposed approach. It is crucial to demonstrate that the adaptive pathways are not just a simple selection mechanism but rather a sophisticated method that dynamically adjusts the model's architecture based on the input data.

Finally, the paper should include more comprehensive experimental results to support the claims made. This includes a more detailed ablation study that systematically evaluates the impact of each component of the proposed model, such as the multi-scale division, dual attention, and adaptive pathways. The authors should also provide a more thorough comparison with state-of-the-art methods, including a discussion of the strengths and weaknesses of each approach. The experimental results should be presented with clear visualizations and statistical analysis to demonstrate the significance of the proposed method. Furthermore, the authors should discuss the computational cost of the proposed method and compare it with other methods, which is important for practical applications.

### Questions

1. How are the pathway weights generated and updated in the adaptive pathways? What mechanisms ensure the sparsity and diversity of the selected patch sizes?

2. How does the proposed model compare to other adaptive methods in the literature? What are the advantages and disadvantages of the proposed approach?

3. What is the computational cost of the proposed method compared to other methods? How does the model's complexity affect its performance and generalization capabilities?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
