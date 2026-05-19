### Summary

This paper proposes a new method called D2T2 for Decision Transformer. The motivation is that the performance of Decision Transformer is highly sensitive to the stochasticity of the environment. The authors first identify the reason behind this phenomenon and then propose to solve it by introducing temporal difference (TD) learning. The experimental results show that D2T2 outperforms the original Decision Transformer and other baselines in various stochastic tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The motivation is clear and the proposed method is reasonable.
3. The experimental results are promising.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only consider the stochasticity of the environment. However, the performance of Decision Transformer also depends on the stochasticity of the dataset. It is not clear how the proposed method can address this issue.
2. The authors only compare the proposed method with Decision Transformer and some offline RL baselines. It is not clear how the proposed method compares with other sequence prediction-based methods.
3. The authors only consider the performance of D2T2 on stochastic tasks. It is not clear how the proposed method performs on deterministic tasks.

### Suggestions

The paper would benefit from a more thorough investigation into the impact of dataset stochasticity on Decision Transformer's performance. While the authors focus on environmental stochasticity, the inherent randomness in the training data can also significantly degrade performance. It would be valuable to see experiments that explicitly vary the degree of stochasticity in the dataset, perhaps by introducing noise into the reward signals or the state transitions. This would help to isolate the effects of environmental and dataset stochasticity and provide a more complete picture of the method's robustness. Furthermore, the authors should explore how the proposed TD-based guidance mechanism interacts with different levels of dataset stochasticity. For example, does the guidance signal become less effective or more noisy when the dataset is highly stochastic, and how does this affect the overall performance of the model? A more detailed analysis of these interactions would strengthen the paper's claims and provide a more nuanced understanding of the method's capabilities.

To better contextualize the contribution of D2T2, the authors should include comparisons with other sequence prediction-based methods. While Decision Transformer is a strong baseline, there are other approaches that also frame the problem as a sequence prediction task. For example, methods that use recurrent neural networks or transformers to predict the next action given a sequence of past states and rewards could be relevant baselines. Comparing D2T2 against these methods would help to clarify its specific advantages and disadvantages. Furthermore, the authors should discuss the computational complexity of D2T2 compared to these other sequence prediction methods. This would provide a more complete picture of the trade-offs involved in using D2T2. It would also be helpful to see a comparison of the training time and inference time of D2T2 and the other sequence prediction methods. This would help to understand the practical implications of using D2T2 in real-world scenarios.

Finally, the paper should include a more comprehensive evaluation of D2T2 on deterministic tasks. While the authors argue that their method is designed to handle stochasticity, it is important to understand how it performs in deterministic environments. This would help to establish the generalizability of the method and identify any potential limitations. The authors should also consider comparing D2T2 against other methods that are specifically designed for deterministic environments. This would provide a more complete picture of the method's performance across different types of tasks. Furthermore, the authors should analyze the performance of D2T2 on tasks with varying levels of determinism. This would help to understand how the method adapts to different types of environments and provide insights into its robustness.

### Questions

See the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
