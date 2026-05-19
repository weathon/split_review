### Summary

This paper proposes Uni-O4, a unified framework for offline and offline-to-online reinforcement learning (RL) that leverages an ensemble of policies for offline training and offline policy evaluation (OPE) for efficient fine-tuning. The key contributions include: (1) an ensemble-based policy initialization that addresses state-action support mismatch between the estimated behavior policy and the offline dataset, (2) a multi-step policy improvement approach that leverages offline data for policy updates, and (3) an offline OPE method that avoids the need for online evaluation. The method is evaluated on a range of simulated and real-world robotic tasks, demonstrating superior performance compared to state-of-the-art baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses a critical challenge in RL, namely bridging the gap between offline and online learning, which is essential for real-world applications.
- The proposed method is well-motivated, with a clear connection to existing work and a logical progression of ideas.
- The experimental evaluation is comprehensive, covering a range of simulated and real-world tasks, and the results demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method, which is an important consideration for practical applications.
- The paper does not discuss the limitations of the proposed method, such as its sensitivity to hyperparameters or the potential for overfitting.

### Suggestions

The paper would benefit from a more thorough analysis of the computational demands of the proposed Uni-O4 framework. While the experimental results demonstrate its effectiveness, the practical applicability of the method hinges on its computational efficiency. Specifically, the authors should provide a detailed breakdown of the time complexity for each component of the algorithm, including the ensemble policy training, offline policy evaluation (OPE), and online fine-tuning. This analysis should consider the number of parameters in the ensemble policies, the size of the offline dataset, and the number of environment interactions required for fine-tuning. Furthermore, it would be beneficial to compare the computational cost of Uni-O4 with other state-of-the-art offline-to-online RL methods, providing a clear understanding of its relative efficiency. This analysis should also include a discussion of the memory requirements for storing the ensemble policies and the offline dataset, which are crucial factors for real-world deployment. Without a detailed computational analysis, it is difficult to assess the practical feasibility of the proposed method.

Additionally, the paper should include a more comprehensive discussion of the limitations of the proposed method. While the experimental results are promising, it is important to acknowledge the potential challenges and drawbacks of the approach. For example, the sensitivity of the method to hyperparameter settings is a critical issue that needs to be addressed. The authors should provide a sensitivity analysis of the key hyperparameters, such as the ensemble size, the learning rate, and the regularization parameters, to demonstrate the robustness of the method. Furthermore, the potential for overfitting to the offline dataset should be discussed, and the authors should provide insights into how to mitigate this issue. This could involve techniques such as regularization, early stopping, or data augmentation. A thorough discussion of these limitations would provide a more balanced and realistic assessment of the proposed method and would help guide future research in this area.

Finally, the paper should include a more detailed analysis of the offline-to-online transfer performance of the proposed method. While the results demonstrate that Uni-O4 can achieve good performance in the offline setting, the paper lacks a thorough analysis of how well the method can adapt to new environments or tasks during online fine-tuning. The authors should provide a quantitative analysis of the performance of the method in different online fine-tuning scenarios, including varying degrees of domain shift and task complexity. This analysis should also compare the performance of Uni-O4 with other offline-to-online RL methods, providing a clear understanding of its relative strengths and weaknesses. Furthermore, the authors should discuss the potential challenges of adapting the method to new environments, such as the need for exploration or adaptation strategies. A more detailed analysis of the offline-to-online transfer performance would provide a more complete picture of the capabilities of the proposed method and would help guide future research in this area.

### Questions

- How does the proposed method handle the exploration-exploitation trade-off during online fine-tuning?
- How does the proposed method perform in environments with high-dimensional state and action spaces?

### Rating

6

### Confidence

4

**********
