### Summary

This paper proposes SC-MCTS*, a novel Monte Carlo Tree Search (MCTS) reasoning algorithm for Large Language Models (LLMs), which improves both reasoning accuracy and speed. The authors conduct extensive ablation studies and quantitative analysis on components of MCTS, revealing the impact of each component on the MCTS reasoning performance of LLMs. The proposed method achieves an average speed improvement of 51.9% per node using speculative decoding and outperforms o1-mini by an average of 17.4% on the Blocksworld multi-step reasoning dataset using Llama-3.1-70B.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.
3. The authors provide a detailed analysis of the results, including ablation studies and comparisons with baseline methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from more detailed explanations of the experimental setup and results.
2. The paper could provide more insights into the limitations of the proposed method and potential directions for future research.

### Suggestions

The paper would benefit from a more granular description of the experimental setup, particularly regarding the hyperparameter tuning process. For instance, while the authors mention using grid search, they do not specify the range of values explored for each hyperparameter, such as the number of MCTS iterations, the exploration parameter, or the learning rate. Providing this level of detail would enhance the reproducibility of the results and allow other researchers to build upon this work more effectively. Furthermore, the paper should include a discussion of the sensitivity of the results to these hyperparameters. For example, how does the performance of SC-MCTS* vary when the number of MCTS iterations is doubled or halved? Such an analysis would provide valuable insights into the robustness of the proposed method. Additionally, the paper should clarify the specific hardware and software configurations used for the experiments, including the type of GPUs, the amount of memory, and the versions of the software libraries. This information is crucial for ensuring the reproducibility of the results.

Regarding the limitations, the paper should delve deeper into the potential failure modes of SC-MCTS*. For example, under what conditions does the method struggle to find optimal solutions? Does it perform poorly on tasks with a high degree of branching in the search space, or does it struggle with tasks that require long-range planning? A more detailed analysis of these limitations would provide a more balanced view of the method's capabilities. The paper should also discuss the computational cost of SC-MCTS* in more detail. While the authors mention a speed improvement of 51.9% per node, they do not provide a clear comparison of the overall computational cost with other methods. A more detailed analysis of the time and memory requirements of SC-MCTS* would be valuable for practitioners who are considering using this method in real-world applications. Furthermore, the paper should discuss the potential for bias in the training data used for the reward model. If the training data is biased, it could lead to biased reward signals, which could in turn affect the performance of SC-MCTS*.

Finally, the paper should provide more concrete suggestions for future research directions. While the authors mention the potential for applying SC-MCTS* to other tasks, they do not provide specific examples or discuss the challenges that might be encountered. For instance, how would SC-MCTS* perform on tasks that require natural language understanding or common-sense reasoning? What modifications would be necessary to adapt the method to these tasks? The paper should also discuss the potential for combining SC-MCTS* with other techniques, such as reinforcement learning or imitation learning. Such a discussion would provide a more comprehensive view of the potential of SC-MCTS* and would help to guide future research in this area. The authors should also consider exploring the use of different reward models and their impact on the performance of SC-MCTS*. This could lead to further improvements in the method's accuracy and efficiency.

### Questions

1. How does the proposed method compare to other state-of-the-art methods in terms of computational efficiency?
2. What are the potential limitations of the proposed method, and how can they be addressed in future work?

### Rating

6

### Confidence

3

**********
