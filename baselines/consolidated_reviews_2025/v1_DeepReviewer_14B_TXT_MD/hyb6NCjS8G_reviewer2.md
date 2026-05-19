### Summary

This paper introduces a novel framework called Hebbian View Orthogonal Projection (HVOP) aimed at addressing the challenge of knowledge retention and transfer in multi-view learning scenarios. The authors draw inspiration from neural processing mechanisms to tackle the "view forgetting phenomenon," where traditional multi-view learning methods struggle to retain knowledge from previous views when new views are introduced. HVOP constructs a Knowledge Transfer Space (KTS) and employs an orthogonal learning mechanism to reduce interference between old and new views. By incorporating recursive lateral connections and Hebbian learning, the framework enhances knowledge transfer and integration, mimicking the adaptability of the human brain.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach by drawing inspiration from neuroscience to address a significant challenge in multi-view learning. The integration of Hebbian learning and orthogonal projection mechanisms is innovative and provides a fresh perspective on handling the "view forgetting phenomenon."

2. The experimental validation is thorough, with the proposed model demonstrating superior performance in knowledge retention and transfer compared to traditional methods. The use of multiple datasets and comparison with state-of-the-art methods strengthens the credibility of the results.

3. The paper is well-structured and clearly written, making it accessible to readers across different backgrounds. The authors effectively communicate complex ideas and provide sufficient detail to understand the proposed framework and its implementation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed framework. Specifically, the authors should address scenarios where the HVOP model might underperform or face challenges. For instance, how does the model handle highly heterogeneous views where the feature spaces have minimal overlap or are inherently contradictory? Additionally, a discussion on the computational complexity and scalability of the framework, particularly in terms of memory usage and training time as the number of views and data dimensionality increase, would be valuable. The current analysis lacks a rigorous examination of these aspects, making it difficult to assess the practical applicability of the method in resource-constrained environments.

2. While the paper compares HVOP with several state-of-the-art methods, a more in-depth analysis of why HVOP outperforms these methods would enhance the understanding of its advantages. For example, a breakdown of the performance gains on a per-view basis, or an analysis of the gradient updates in the KTS, could provide more granular insights. Furthermore, the paper should explore the sensitivity of HVOP to hyperparameter settings, such as the learning rate for Hebbian updates or the dimensionality of the KTS. Without this, it is difficult to determine whether the reported performance is robust or highly dependent on specific parameter choices.

3. The paper primarily focuses on node classification tasks. Expanding the evaluation to other types of tasks, such as link prediction or graph classification, would provide a more comprehensive understanding of the model's applicability and robustness. The current evaluation does not fully explore the potential of the proposed method in diverse graph-based learning scenarios. It is unclear whether the benefits observed in node classification would translate to other tasks with different structural and semantic requirements.

### Suggestions

To address the limitations regarding the handling of heterogeneous views, the authors should consider incorporating a mechanism that explicitly measures and mitigates the dissimilarity between feature spaces. For instance, a contrastive loss could be introduced to encourage the model to learn view-specific representations that are both discriminative and aligned in the KTS. This could involve calculating the distance between view-specific embeddings and penalizing large distances for similar instances while encouraging larger distances for dissimilar ones. Furthermore, the authors could explore the use of adaptive weighting schemes that dynamically adjust the contribution of each view based on its relevance to the current learning task. This would allow the model to focus on the most informative views and mitigate the impact of noisy or irrelevant views. A detailed analysis of the model's performance under varying degrees of view heterogeneity would also be beneficial to understand the robustness of the proposed approach.

To enhance the analysis of HVOP's performance advantages, the authors should provide a more detailed breakdown of the results. This could include visualizing the learned representations in the KTS to understand how different views are integrated and how the orthogonal projection mechanism mitigates interference. Additionally, the authors should analyze the gradient updates in the KTS to understand how the Hebbian learning rule contributes to knowledge retention and transfer. A sensitivity analysis of the model's performance to hyperparameter settings is also crucial. This could involve systematically varying the learning rate for Hebbian updates, the dimensionality of the KTS, and other relevant parameters, and reporting the impact on performance. This would help to determine the optimal parameter settings and assess the robustness of the model. Furthermore, the authors should compare the computational cost of HVOP with other methods, providing a detailed breakdown of the time and memory requirements for each component of the framework.

To broaden the evaluation of the proposed method, the authors should include experiments on other graph-based learning tasks, such as link prediction and graph classification. For link prediction, the authors could evaluate the model's ability to predict missing edges in a graph based on the learned node representations. For graph classification, the authors could evaluate the model's ability to classify entire graphs based on their structural and feature information. These experiments would provide a more comprehensive understanding of the model's applicability and robustness. The authors should also consider using datasets with different characteristics, such as varying graph sizes, densities, and feature dimensionalities, to assess the generalizability of the proposed method. This would help to identify the strengths and weaknesses of the model and provide a more complete picture of its performance.

### Questions

1. How does the proposed HVOP framework handle highly heterogeneous views where the feature spaces have minimal overlap or are inherently contradictory? Are there specific mechanisms in place to address such scenarios, or is it an area for future work?

2. Can the authors provide more insights into the computational complexity and scalability of the HVOP framework? Specifically, how does the model's performance and resource requirements scale with an increasing number of views and larger datasets?

3. The paper primarily focuses on node classification tasks. How might the HVOP framework be adapted or extended to handle other types of tasks, such as link prediction or graph classification? Are there any modifications needed to apply the framework to these scenarios?

### Rating

6

### Confidence

3

**********
