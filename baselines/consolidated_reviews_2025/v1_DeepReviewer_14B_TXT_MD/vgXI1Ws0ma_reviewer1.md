### Summary

This paper proposes a novel framework, Empowerment through Causal Learning (ECL), which combines causal structure learning with empowerment-based exploration in model-based reinforcement learning. ECL leverages causal structures to improve the agent’s understanding and control over the environment while using empowerment as an intrinsic motivation to guide exploration. The method involves training a causal dynamics model, optimizing it through empowerment-driven exploration, and learning policies for downstream tasks with improved sample efficiency and generalization. The approach is evaluated across multiple environments, demonstrating superior performance over other causal model-based RL methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents an interesting approach by integrating causal structure learning with empowerment in model-based reinforcement learning, which is a novel combination that could advance the field.
2. The method is evaluated across multiple environments, including both simple and complex tasks, and the results indicate that ECL outperforms baseline methods in terms of causal discovery accuracy, sample efficiency, and asymptotic performance.
3. The paper is generally well-organized, with clear figures and explanations that aid in understanding the proposed framework and its components.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison with existing causal model-based RL methods, such as CDL, which could provide a clearer understanding of the specific advancements and unique aspects of ECL. While the paper mentions CDL, a deeper dive into the algorithmic differences is needed. For instance, the specific mechanisms by which ECL's empowerment-driven exploration interacts with and refines the causal model during learning are not clearly contrasted with CDL's approach to causal structure learning. A more granular comparison, perhaps outlining the specific mathematical formulations or algorithmic steps that differentiate ECL from CDL, would be beneficial.
2. The ablation studies are not comprehensive; for example, the impact of the curiosity reward and the empowerment-driven exploration on the overall performance and learning efficiency is not thoroughly analyzed. The paper does not provide sufficient detail on how the curiosity reward is implemented, nor does it explore the sensitivity of the results to different curiosity reward coefficients. Furthermore, the analysis of empowerment-driven exploration lacks a detailed examination of how the empowerment objective is optimized and how this optimization affects the learned policies. It is unclear how the empowerment is calculated and how it is used to guide exploration, and whether this exploration is truly beneficial for downstream task performance.
3. The paper does not provide an in-depth analysis of the method’s limitations, such as scenarios where ECL may underperform or the computational costs associated with learning causal structures. The paper lacks a discussion on the potential failure modes of the causal discovery process, such as when the underlying assumptions of the causal model are violated or when the data is insufficient for reliable causal inference. Additionally, the computational complexity of learning and updating the causal graph is not addressed, which is a critical factor for practical applications.

### Suggestions

To address the lack of detailed comparison with existing methods, the authors should include a table that explicitly contrasts ECL with other causal model-based RL methods, such as CDL, highlighting the key differences in their approaches to causal discovery, empowerment-driven exploration, and policy learning. This table should include specific details on the mathematical formulations, algorithmic steps, and the interaction between causal structure learning and exploration. For example, the table could compare how each method initializes the causal structure, how they update the structure during learning, and how they use the learned structure for exploration and policy learning. Furthermore, the authors should provide a more detailed explanation of how ECL's empowerment-driven exploration differs from standard exploration techniques used in other model-based RL methods, and how this difference contributes to the improved performance.

To improve the ablation studies, the authors should conduct a more thorough analysis of the impact of the curiosity reward and the empowerment-driven exploration on the overall performance and learning efficiency. This should include experiments with different curiosity reward coefficients to assess the sensitivity of the results to this parameter. The authors should also provide a detailed explanation of how the empowerment is calculated and how it is used to guide exploration. This should include a discussion of the optimization process for the empowerment objective and how this optimization affects the learned policies. Furthermore, the authors should analyze the exploration behavior of the agent with and without the empowerment objective to demonstrate the benefits of this approach. The ablation study should also include a comparison of the performance of the agent when trained with and without the curiosity reward to isolate the impact of each component.

Finally, the authors should provide a more in-depth analysis of the method’s limitations, including scenarios where ECL may underperform and the computational costs associated with learning causal structures. This should include a discussion of the potential failure modes of the causal discovery process, such as when the underlying assumptions of the causal model are violated or when the data is insufficient for reliable causal inference. The authors should also analyze the computational complexity of learning and updating the causal graph, and discuss the scalability of the method to larger and more complex environments. This analysis should include a discussion of the trade-offs between the accuracy of the causal model and the computational cost of learning it. The authors should also consider providing guidelines on when ECL is most applicable and what alternative approaches might be more suitable in different scenarios.

### Questions

1. Could the authors provide a more detailed comparison between ECL and existing methods like CDL, specifically highlighting the unique contributions and improvements of ECL?
2. Can the authors conduct more comprehensive ablation studies to evaluate the impact of the curiosity reward and empowerment-driven exploration on the overall performance and learning efficiency?
3. What are the limitations of ECL, particularly in scenarios where it might underperform, and what is the computational cost associated with learning causal structures?

### Rating

6

### Confidence

3

**********
