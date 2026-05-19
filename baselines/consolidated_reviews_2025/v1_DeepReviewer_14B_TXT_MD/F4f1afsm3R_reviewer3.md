### Summary

This paper proposes a new MCTS reasoning algorithm for LLMs, called SC-MCTS*. The authors address the limitations of previous MCTS-based reasoning methods, such as their slow speed compared to CoT and the lack of in-depth studies on reward models. The key contributions of SC-MCTS* include: (1) a highly interpretable reward model based on contrastive decoding, (2) a 51.9% speed improvement per node using speculative decoding, and (3) improvements to the UCT node selection strategy and backpropagation. The authors demonstrate that SC-MCTS* outperforms o1-mini by an average of 17.4% on the Blocksworld multi-step reasoning dataset using Llama-3.1-70B.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses an important problem in LLM reasoning, where MCTS-based methods are often slower than CoT. The proposed speculative decoding approach provides a practical solution to improve the speed of MCTS.
- The paper introduces a novel reward model based on contrastive decoding, which is highly interpretable and does not require external tools, training, or datasets. This is a valuable contribution to the field of MCTS-based reasoning.
- The authors conduct extensive quantitative analysis and ablation studies on every component of MCTS, providing better interpretability for MCTS multi-step reasoning. This is a significant contribution to the understanding of MCTS in LLMs.

### Weaknesses

#### Some Related Works


#### comment

 - The paper only evaluates the proposed method on the Blocksworld dataset. It would be beneficial to evaluate the method on other multi-step reasoning datasets to assess its generalizability.
- The paper does not provide a detailed analysis of the computational cost of SC-MCTS*. It would be helpful to compare the computational cost of SC-MCTS* with other methods, such as CoT and RAP-MCTS.
- The paper does not provide a detailed analysis of the impact of different hyperparameters on the performance of SC-MCTS*. It would be helpful to conduct a sensitivity analysis of the hyperparameters and provide guidelines for selecting appropriate values.

### Suggestions

The paper's evaluation is limited to the Blocksworld dataset, which raises concerns about the generalizability of the proposed SC-MCTS* method. While Blocksworld is a useful benchmark for multi-step reasoning, it is a relatively constrained environment. To strengthen the paper, the authors should evaluate their method on more diverse and challenging datasets, such as those involving mathematical reasoning, commonsense reasoning, or planning tasks. This would provide a more comprehensive assessment of the method's capabilities and limitations. For example, datasets like the MATH dataset, which requires mathematical problem-solving, or the PlanBench dataset, which focuses on planning tasks, could be used to evaluate the method's performance in different domains. Furthermore, the authors should analyze the performance of SC-MCTS* on these datasets and discuss any potential challenges or limitations that may arise.

Another area that requires further investigation is the computational cost of SC-MCTS*. While the paper mentions a speed improvement per node using speculative decoding, it lacks a detailed analysis of the overall computational cost compared to other methods like CoT and RAP-MCTS. The authors should provide a comprehensive comparison of the computational resources required by each method, including the number of GPU hours, memory usage, and inference time. This analysis should also consider the impact of different hyperparameters on the computational cost. For example, the number of MCTS iterations and the size of the language model can significantly affect the computational cost. The authors should provide guidelines for selecting appropriate hyperparameter values based on the available computational resources. Furthermore, the authors should discuss the trade-offs between computational cost and performance and provide recommendations for practical applications.

Finally, the paper lacks a detailed analysis of the impact of different hyperparameters on the performance of SC-MCTS*. The authors should conduct a sensitivity analysis of the hyperparameters, such as the number of MCTS iterations, the exploration parameter in the UCT strategy, and the parameters of the reward model. This analysis should provide insights into how these hyperparameters affect the performance of the method and provide guidelines for selecting appropriate values. For example, the authors could analyze the impact of different exploration parameters on the convergence of the MCTS algorithm and the quality of the solutions found. They could also analyze the impact of different reward model parameters on the interpretability and effectiveness of the reward signal. The authors should provide a clear explanation of how these hyperparameters were chosen and justify their choices based on empirical evidence.

### Questions

- How does the performance of SC-MCTS* compare to other methods on other multi-step reasoning datasets?
- What is the computational cost of SC-MCTS* compared to other methods, such as CoT and RAP-MCTS?
- How sensitive is the performance of SC-MCTS* to different hyperparameters, and what are the guidelines for selecting appropriate values?

### Rating

5

### Confidence

3

**********
