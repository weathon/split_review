### Summary

This paper introduces Hebbian View Orthogonal Projection (HVOP), a novel framework inspired by human brain mechanisms to address the issue of view forgetting in multi-view learning. Traditional multi-view learning methods struggle with dynamic data, where new views are constantly added, leading to the loss of knowledge from previous views. HVOP tackles this problem by using Hebbian learning and orthogonal projection to integrate new views while retaining knowledge from previous ones. The framework also incorporates recursive lateral connections and lateral connections to simulate the brain's dynamic adaptability, enabling efficient knowledge retention and transfer across different views. The experimental results show that HVOP outperforms traditional methods in knowledge retention and transfer, demonstrating its potential to enhance multi-view learning in dynamic environments.

### Soundness

2

### Presentation

1

### Contribution

2

### Strengths

1. The paper introduces a novel framework, Hebbian View Orthogonal Projection (HVOP), which is inspired by the human brain's ability to integrate and transfer knowledge across multiple views. This approach is innovative and addresses a significant gap in traditional multi-view learning methods, particularly in dynamic environments where new views are constantly added.
2. The paper provides a thorough explanation of the HVOP framework, including the use of Hebbian learning and orthogonal projection to integrate new views while retaining knowledge from previous ones. The incorporation of recursive lateral connections and lateral connections to simulate the brain's dynamic adaptability is also well-explained.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's experimental evaluation is limited to a few datasets and tasks, which may not be sufficient to demonstrate the generalizability of the HVOP framework. Expanding the evaluation to include a wider range of datasets and tasks would strengthen the claims of the paper.
2. The paper lacks a detailed analysis of the computational complexity of the HVOP framework, which is important for understanding its scalability and efficiency. A thorough analysis of the time and space complexity of the framework would be beneficial.
3. The paper does not provide a clear comparison of the HVOP framework with other state-of-the-art methods in multi-view learning, particularly those that address the issue of view forgetting. A more comprehensive comparison would help to highlight the advantages and limitations of the HVOP framework.

### Suggestions

The authors should consider expanding their experimental evaluation to include a more diverse set of datasets, encompassing different domains and characteristics. For example, datasets from areas such as natural language processing, time-series analysis, or graph-based data could provide a more comprehensive assessment of the HVOP framework's generalizability. Furthermore, the evaluation should include a wider range of tasks beyond the current classification tasks, such as clustering, dimensionality reduction, or even generative modeling. This would provide a more robust understanding of the framework's capabilities and limitations across various applications. The inclusion of more complex datasets and tasks would also help to validate the claim that HVOP can effectively handle dynamic environments with constantly added views.

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the time and space complexity of the HVOP framework. This analysis should include a discussion of the computational cost associated with each component of the framework, such as the Hebbian learning, orthogonal projection, and recursive lateral connections. The analysis should also consider the impact of the number of views, the size of the data, and the dimensionality of the feature space on the computational cost. Furthermore, the authors should compare the computational complexity of HVOP with that of other state-of-the-art multi-view learning methods, highlighting the trade-offs between performance and computational efficiency. This would provide a more complete picture of the framework's scalability and practical applicability.

Finally, the authors should provide a more comprehensive comparison of the HVOP framework with other state-of-the-art methods in multi-view learning, particularly those that address the issue of view forgetting. This comparison should include a detailed analysis of the strengths and weaknesses of each method, as well as a discussion of the specific scenarios in which each method performs best. The comparison should also include a quantitative evaluation of the performance of HVOP and other methods on a common set of benchmark datasets. This would provide a more objective assessment of the advantages and limitations of the HVOP framework and help to position it within the broader landscape of multi-view learning research.

### Questions

1. How does the HVOP framework handle the issue of catastrophic forgetting in dynamic environments with a large number of views?
2. What is the computational complexity of the HVOP framework, and how does it compare to other state-of-the-art methods in multi-view learning?
3. How does the HVOP framework perform on more complex datasets and tasks, such as clustering or dimensionality reduction?

### Rating

5

### Confidence

3

**********
