### Summary

This paper proposes a brain-inspired multi-view incremental learning framework named Hebbian View Orthogonal Projection (HVOP) to address the "view forgetting phenomenon" in traditional multi-view learning methods. When new views are introduced, these methods often fail to retain knowledge from previous views. HVOP aims to enable knowledge transfer and retention by constructing a Knowledge Transfer Space (KTS) and leveraging Hebbian learning and orthogonal projection to reduce interference between old and new views. The effectiveness of the model is demonstrated on node classification tasks, showing improved performance in knowledge retention and transfer.

### Soundness

2

### Presentation

3

### Contribution

3

### Strengths

1. The paper proposes an innovative framework that mimics the neural mechanisms of the human brain, particularly the hippocampus, to address the issue of catastrophic forgetting in multi-view learning.
2. The use of Hebbian learning and orthogonal projection to simulate brain-like dynamic adaptability is a creative approach that adds novelty to the field of multi-view incremental learning.
3. The paper provides a thorough experimental evaluation, demonstrating the model's superior performance in knowledge retention and transfer compared to traditional methods.

### Weaknesses

#### Some Related Works


#### comment

1. The explanation of how lateral connections and Hebbian learning specifically contribute to orthogonal projection could be more detailed. Additional theoretical analysis or empirical evidence on this mechanism's effectiveness would strengthen the paper. Specifically, the paper lacks a clear mathematical formulation of how the Hebbian update rule interacts with the lateral connection weights to achieve the claimed orthogonal projection. It would be beneficial to see a derivation or at least a clear explanation of how the update dynamics of the lateral connection weights lead to the desired orthogonality, rather than simply stating that it does.
2. The paper primarily focuses on node classification tasks. Expanding the evaluation to other types of tasks could provide a more comprehensive understanding of the model's applicability and robustness. For instance, it is unclear how the model would perform on tasks such as link prediction or community detection, which are also common in graph-based multi-view learning. The current evaluation is limited in scope and does not fully demonstrate the generalizability of the proposed approach.
3. The paper could benefit from a discussion on the scalability of the HVOP framework, especially when dealing with large-scale datasets or a high number of views. The computational complexity of the Hebbian learning and orthogonal projection mechanisms, particularly in relation to the size of the input features and the number of views, is not addressed. This is a critical consideration for practical applications, and the paper should provide some analysis of the computational and memory requirements of the proposed method.

### Suggestions

To address the lack of detail regarding the interaction between Hebbian learning and lateral connections for orthogonal projection, the authors should include a more rigorous mathematical treatment. This should involve a clear definition of the Hebbian update rule used for the lateral connection weights, denoted as \(R\), and a demonstration of how this update rule, in conjunction with the recurrent application of \(R\), leads to the extraction of principal components. The paper should explicitly show how the update dynamics of \(R\) approximate the principal direction of the features, possibly by relating the Hebbian update to the Oja's rule or a similar mechanism. A step-by-step derivation or a detailed explanation of the convergence properties of the update rule would significantly strengthen the theoretical foundation of the proposed method. Furthermore, it would be beneficial to include a visualization of the feature space before and after the orthogonal projection to empirically demonstrate the effect of the proposed mechanism.

To broaden the evaluation of the HVOP framework, the authors should include experiments on a wider range of tasks beyond node classification. This could include tasks such as link prediction, where the goal is to predict missing edges in the graph, or community detection, where the objective is to identify clusters of nodes with similar properties. These tasks would provide a more comprehensive assessment of the model's capabilities and its ability to generalize to different types of problems. For each task, the authors should clearly define the evaluation metrics and provide a detailed comparison with existing state-of-the-art methods. This would help to establish the practical utility of the proposed framework and its advantages over existing approaches. Additionally, the authors should consider using datasets with varying characteristics, such as different graph sizes and view numbers, to evaluate the robustness of the model.

Finally, the paper needs a more thorough discussion of the scalability of the HVOP framework. The authors should provide a detailed analysis of the computational complexity of the Hebbian learning and orthogonal projection mechanisms, particularly in relation to the size of the input features and the number of views. This analysis should include both time and space complexity considerations. It would be helpful to provide empirical results on the training time and memory usage of the model on datasets of varying sizes and with different numbers of views. The authors should also discuss any potential bottlenecks in the proposed method and suggest possible strategies for improving its scalability. This discussion is crucial for assessing the practical applicability of the framework in real-world scenarios.

### Questions

1. How does the choice of Hebbian learning rules impact the performance of the HVOP framework? Are there specific types of Hebbian learning that are more effective for this application?
2. The paper mentions that the principal component matrix K is dynamically updated. How stable are these updates across different views, and could this lead to instability in the model's performance?
3. Are there any limitations in terms of the types of data or tasks for which the HVOP framework is best suited? How might the model perform in non-graph-based multi-view learning scenarios?

### Rating

6

### Confidence

3

**********
