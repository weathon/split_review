### Summary

This paper introduces Hebbian View Orthogonal Projection (HVOP), a novel framework designed to address the challenge of view forgetting in dynamic multi-view learning. Traditional multi-view learning methods often struggle with retaining knowledge from previously acquired views when new views are introduced, leading to the loss of previously learned information. HVOP tackles this issue by drawing inspiration from the human brain’s ability to seamlessly integrate and transfer knowledge across multiple views. The framework incorporates mechanisms such as Hebbian learning and orthogonal projection to enable efficient knowledge retention and transfer between different views. By simulating the brain’s dynamic adaptability, HVOP enhances its ability to handle evolving data and maintain coherent representations across multiple views. The paper presents extensive experiments across various multi-view datasets, demonstrating that HVOP outperforms traditional methods in knowledge retention and transfer, particularly in scenarios with incremental views. The results highlight the potential of biologically inspired mechanisms to advance multi-view learning and mitigate the problem of view forgetting, offering a robust solution for dynamic learning environments.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel framework, Hebbian View Orthogonal Projection (HVOP), which addresses the critical issue of view forgetting in dynamic multi-view learning. This is a significant contribution to the field, as traditional multi-view learning methods often struggle with retaining knowledge from previously acquired views when new views are introduced. By drawing inspiration from the human brain’s ability to seamlessly integrate and transfer knowledge across multiple views, HVOP offers a fresh perspective on how to handle evolving data and maintain coherent representations across multiple views.

2. The paper provides a comprehensive review of existing multi-view learning methods and transfer learning approaches, clearly articulating the limitations of these methods in handling dynamic, incrementally available data. This sets a strong foundation for the proposed HVOP framework, highlighting the need for a more robust solution that can effectively manage the integration and transfer of knowledge across multiple views.

3. The paper is well-structured and clearly written, making it easy for readers to follow the complex concepts and methodologies presented. The use of visual aids and examples effectively illustrates the points being made, enhancing the overall readability and understanding of the paper.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on a specific type of dynamic multi-view learning scenario where views are added incrementally. While this is a common scenario in many real-world applications, the paper could benefit from a more detailed discussion of how the proposed framework might perform in other dynamic scenarios, such as when views are added in a non-sequential order or when the number of views changes drastically over time. Specifically, the paper lacks a discussion on the sensitivity of HVOP to the order of view introduction. For instance, does the performance degrade if a view with a large amount of data is introduced early on, potentially dominating the learning process and hindering the integration of subsequent views? Furthermore, the paper does not explore the impact of view redundancy, where some views might be highly correlated, and how this might affect the orthogonal projection and knowledge retention mechanisms.

2. The paper does not provide a thorough analysis of the computational complexity of the proposed method. While the authors mention that the method is efficient, a more detailed analysis of the time and space complexity, especially in comparison to other multi-view learning methods, would be beneficial. This analysis should include a breakdown of the computational cost associated with each component of the framework, such as the Hebbian learning, orthogonal projection, and recursive lateral connections. It would also be useful to discuss the scalability of the method to large-scale datasets and high-dimensional feature spaces. The paper should also consider the impact of the number of views and the size of the data on the computational cost.

3. The paper could benefit from a more detailed discussion of the limitations of the proposed method. For example, under what conditions might the method fail to effectively retain knowledge from previously acquired views, or when might it struggle to integrate new views effectively? The paper should also discuss the potential impact of noisy or irrelevant data on the performance of HVOP. Furthermore, the paper should explore the sensitivity of the method to hyperparameter settings and provide guidelines for selecting optimal parameters. It is also important to discuss the potential for overfitting, especially when dealing with a large number of views or complex datasets.

### Suggestions

To address the limitations regarding dynamic view addition, the authors should conduct a more thorough analysis of the framework's performance under various scenarios. This should include experiments where views are added in random orders, with varying degrees of correlation, and with significant changes in the number of views. The authors should also investigate the impact of different view selection strategies, such as selecting views based on their information content or their correlation with other views. Furthermore, the paper should include a discussion on the potential for using techniques like curriculum learning to improve the learning process when views are added in a non-sequential order. This would provide a more comprehensive understanding of the framework's robustness and adaptability to different dynamic environments.

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the time and space complexity of each component of the HVOP framework. This analysis should include a comparison with other multi-view learning methods, highlighting the trade-offs between performance and computational cost. The authors should also discuss the scalability of the method to large-scale datasets and high-dimensional feature spaces, and provide guidelines for optimizing the implementation of the framework for different computational environments. Furthermore, the paper should explore the use of techniques like parallel processing or distributed computing to improve the efficiency of the method for large datasets. This would provide a more practical understanding of the method's applicability in real-world scenarios.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This should include an analysis of the conditions under which the method might fail to effectively retain knowledge from previously acquired views, or when it might struggle to integrate new views effectively. The authors should also discuss the potential impact of noisy or irrelevant data on the performance of HVOP, and provide guidelines for mitigating these effects. Furthermore, the paper should explore the sensitivity of the method to hyperparameter settings and provide guidelines for selecting optimal parameters. The authors should also discuss the potential for overfitting, especially when dealing with a large number of views or complex datasets. This would provide a more balanced and realistic assessment of the method's capabilities and limitations.

### Questions

1. How does the proposed method handle the scenario where the number of views changes drastically over time? For instance, what happens if new views are added or removed frequently, potentially disrupting the existing knowledge representations?

2. Can the authors provide a more detailed analysis of the computational complexity of the proposed method, especially in comparison to other multi-view learning methods? How does the method scale to large-scale datasets and high-dimensional feature spaces?

3. What are the limitations of the proposed method, and under what conditions might it fail to effectively retain knowledge from previously acquired views or struggle to integrate new views effectively?

### Rating

6

### Confidence

3

**********
