### Summary

The paper introduces Hebbian View Orthogonal Projection (HVOP), a novel framework designed to address the challenge of view forgetting in dynamic multi-view learning scenarios. Traditional multi-view learning methods struggle with retaining knowledge across newly added views, as they often fail to effectively integrate new information without disrupting previously learned knowledge. Inspired by the human brain's ability to seamlessly integrate and transfer knowledge, HVOP leverages Hebbian learning and orthogonal projection to enable efficient knowledge transfer and retention between different views. The framework incorporates recursive lateral connections and Hebbian learning to simulate the brain's dynamic adaptability, enhancing its ability to handle diverse and evolving data. The authors demonstrate through extensive experiments that HVOP outperforms traditional methods in knowledge retention and transfer, particularly in tasks such as node classification and semi-supervised classification. The results highlight the potential of biologically inspired mechanisms to improve multi-view learning in dynamic environments.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-structured and clearly written, making it easy to follow and understand the complex concepts and methodologies presented. The authors effectively use visual aids and examples to illustrate their points, enhancing the clarity of their arguments.

- The paper provides a comprehensive review of related work in multi-view learning and transfer learning, placing the proposed method in the context of existing research. The authors clearly articulate the limitations of current approaches and how their method addresses these challenges.

- The paper presents extensive experimental results that demonstrate the effectiveness of the proposed method. The authors compare HVOP against several state-of-the-art methods, showing that it outperforms them in terms of knowledge retention and transfer. The experiments are conducted on multiple datasets, including NoisyMNIST and various multi-view datasets, which adds to the credibility of the results.

- The paper discusses the potential applications of the proposed method in real-world scenarios, such as medical image analysis and social network analysis. This highlights the practical relevance and impact of the research.

- The authors provide a detailed analysis of the proposed method, including its computational complexity and scalability. This analysis helps to understand the practical implications of the method and its potential for real-world deployment.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses primarily on classification tasks, but it does not explore the performance of HVOP on other types of tasks, such as clustering or dimensionality reduction. It would be beneficial to see how the method performs on these tasks, as they are also common in multi-view learning. Specifically, the paper lacks experiments on how the orthogonal projection and Hebbian learning components of HVOP affect the quality of embeddings for clustering or dimensionality reduction tasks, which are crucial for understanding the general applicability of the method.

- The paper does not provide a detailed analysis of the computational complexity of the proposed method. While the authors mention that the method is efficient, it would be helpful to see a more rigorous analysis of the time and space complexity, especially in comparison to other multi-view learning methods. This analysis should include a breakdown of the computational cost of each component of the HVOP framework, such as the orthogonal projection, Hebbian learning, and recursive lateral connections. Furthermore, the paper should discuss the scalability of the method to large-scale datasets and high-dimensional feature spaces.

- The paper does not discuss the sensitivity of the proposed method to hyperparameter settings. It would be helpful to see an analysis of how the performance of HVOP is affected by different hyperparameter values, and whether there are any guidelines for selecting optimal hyperparameters. This analysis should include a discussion of the impact of hyperparameters such as the learning rate, the regularization parameters, and the parameters related to the orthogonal projection and Hebbian learning. The paper should also discuss the robustness of the method to different hyperparameter settings and provide recommendations for hyperparameter tuning.

- The paper does not provide a detailed discussion of the limitations of the proposed method. It would be helpful to see a discussion of the scenarios where HVOP may not perform well, and what are the potential areas for future research. This discussion should include a consideration of the assumptions made by the method and the potential impact of these assumptions on the performance of the method. For example, the paper should discuss the limitations of the method when dealing with noisy or incomplete data, or when the views are not well-aligned.

### Suggestions

To address the lack of exploration beyond classification tasks, the authors should include experiments on clustering and dimensionality reduction. For clustering, the authors could evaluate the quality of the embeddings produced by HVOP using metrics such as the Adjusted Rand Index (ARI) or Normalized Mutual Information (NMI). For dimensionality reduction, the authors could visualize the embeddings using techniques such as t-SNE or UMAP and assess the quality of the reduced representations using metrics such as reconstruction error or downstream task performance. These experiments would provide a more comprehensive understanding of the general applicability of HVOP and its ability to learn meaningful representations across different types of tasks. Furthermore, the authors should analyze how the orthogonal projection and Hebbian learning components of HVOP contribute to the performance on these tasks, which would provide valuable insights into the inner workings of the method.

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the time and space complexity of each component of the HVOP framework. This analysis should include a discussion of the computational cost of the orthogonal projection, Hebbian learning, and recursive lateral connections. The authors should also compare the computational complexity of HVOP with that of other multi-view learning methods, such as GCNs and other state-of-the-art approaches. This comparison should be done in terms of both time and space complexity, and should consider the impact of different factors such as the number of views, the size of the data, and the dimensionality of the feature space. Furthermore, the authors should discuss the scalability of the method to large-scale datasets and high-dimensional feature spaces, and provide recommendations for optimizing the implementation of HVOP for large-scale applications.

To address the lack of sensitivity analysis and discussion of limitations, the authors should include a detailed analysis of the sensitivity of HVOP to hyperparameter settings. This analysis should include a discussion of the impact of hyperparameters such as the learning rate, the regularization parameters, and the parameters related to the orthogonal projection and Hebbian learning. The authors should also provide guidelines for selecting optimal hyperparameters, and discuss the robustness of the method to different hyperparameter settings. Furthermore, the authors should discuss the limitations of the method, including the assumptions made by the method and the potential impact of these assumptions on the performance of the method. This discussion should include a consideration of the scenarios where HVOP may not perform well, such as when dealing with noisy or incomplete data, or when the views are not well-aligned. The authors should also discuss potential areas for future research, such as how to improve the robustness of the method to different hyperparameter settings and how to extend the method to handle more complex data types and tasks.

### Questions

- How does the proposed method perform on other types of tasks, such as clustering or dimensionality reduction?

- What is the computational complexity of the proposed method, and how does it compare to other multi-view learning methods?

- How sensitive is the proposed method to hyperparameter settings, and what are the guidelines for selecting optimal hyperparameters?

- What are the limitations of the proposed method, and what are the potential areas for future research?

### Rating

6

### Confidence

3

**********
