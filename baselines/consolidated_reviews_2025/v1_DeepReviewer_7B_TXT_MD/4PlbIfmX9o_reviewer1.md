### Summary

This paper proposes a graph-attention-based DRL approach for dynamic workflow scheduling in cloud computing. The proposed approach features three key innovations: (1) a task-specific graph representation and a Graph Attention Actor Network for dynamically assigning focused tasks to heterogeneous machines; (2) a system-oriented graph representation and a Graph Attention Critic Network for managing complex interactions across workflows and machines; and (3) an offline-online method that utilizes imitation learning for efficient offline training and applies gradient control and decoupled high-frequency critic training to stabilize online learning. Experimental results show that the proposed approach outperforms several baselines in terms of mean flowtime.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper is well-structured and clearly written. The proposed approach is well-motivated and addresses a challenging problem in cloud computing. The experimental results demonstrate the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed description of the workflow execution environment, including the types of workflows, the characteristics of the machines, and the workflow execution patterns. This lack of detail makes it difficult to assess the generalizability of the proposed approach. The paper also lacks a thorough discussion of the limitations of the proposed approach, such as the computational complexity of the algorithm and the sensitivity to hyperparameter settings. Furthermore, the paper does not provide a clear explanation of how the proposed approach handles dynamic changes in the workflow execution environment, such as the addition or removal of machines or workflows. The paper also does not discuss the scalability of the proposed approach to large-scale cloud environments. The paper also does not provide a detailed comparison of the proposed approach with existing state-of-the-art methods for dynamic workflow scheduling, including both DRL-based and non-DRL-based approaches. The paper also does not provide a discussion of the potential impact of the proposed approach on the overall performance of the cloud system, such as the impact on energy consumption or the impact on the user experience.

### Suggestions

The paper should provide a more detailed description of the workflow execution environment, including the types of workflows used in the experiments, the characteristics of the machines (e.g., processing power, memory, network connectivity), and the workflow execution patterns (e.g., sequential, parallel, nested). This information is crucial for understanding the context in which the proposed approach is evaluated and for assessing its generalizability to different cloud environments. The paper should also include a discussion of the limitations of the proposed approach, such as the computational complexity of the algorithm, the sensitivity to hyperparameter settings, and the scalability to large-scale cloud environments. The authors should also discuss how the proposed approach handles dynamic changes in the workflow execution environment, such as the addition or removal of machines or workflows. This discussion should include specific mechanisms and strategies for adapting the scheduling decisions in response to these changes. Furthermore, the paper should provide a more comprehensive comparison of the proposed approach with existing state-of-the-art methods for dynamic workflow scheduling, including both DRL-based and non-DRL-based approaches. This comparison should not only focus on the performance metrics, such as mean flowtime, but also on other relevant factors, such as computational complexity, scalability, and robustness. The paper should also discuss the potential impact of the proposed approach on the overall performance of the cloud system, such as the impact on energy consumption, the impact on the user experience, and the impact on the system's ability to handle dynamic workloads. This discussion should include specific examples and case studies to illustrate the potential benefits and challenges of the proposed approach.

To improve the evaluation of the proposed approach, the authors should consider conducting experiments on a wider range of workflow execution environments and under different conditions. This could include varying the number of workflows, the number of machines, the types of workflows, and the characteristics of the machines. The authors should also consider evaluating the proposed approach under different types of dynamic changes, such as the addition or removal of machines, the addition or removal of workflows, and changes in the workflow execution patterns. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach and its applicability to different cloud environments. The authors should also consider using more realistic and complex workflow execution environments, such as those based on real-world data or simulations. This would help to validate the practical relevance of the proposed approach and its ability to handle real-world challenges. The authors should also provide a more detailed explanation of the experimental setup, including the hardware and software used, the network configuration, and the workload generation process. This information is crucial for ensuring the reproducibility of the results and for allowing other researchers to build upon the work.

Finally, the authors should consider providing a more detailed analysis of the performance of the proposed approach under different conditions. This could include analyzing the impact of different hyperparameters on the performance of the approach, as well as analyzing the impact of different types of dynamic changes on the performance of the approach. The authors should also consider providing a more detailed explanation of the decision-making process of the proposed approach, including the specific rules and algorithms used to assign tasks to machines. This would help to understand the strengths and weaknesses of the approach and to identify potential areas for improvement. The authors should also consider providing a more detailed comparison of the proposed approach with other state-of-the-art methods for dynamic workflow scheduling, including both DRL-based and non-DRL-based approaches. This comparison should not only focus on the performance metrics, such as mean flowtime, but also on other relevant factors, such as computational complexity, scalability, and robustness.

### Questions

1. What are the specific types of workflows used in the experiments?
2. What are the characteristics of the machines used in the experiments?
3. How does the proposed approach handle dynamic changes in the workflow execution environment, such as the addition or removal of machines or workflows?
4. What is the computational complexity of the proposed approach?
5. How sensitive is the proposed approach to hyperparameter settings?

### Rating

5

### Confidence

3

**********
