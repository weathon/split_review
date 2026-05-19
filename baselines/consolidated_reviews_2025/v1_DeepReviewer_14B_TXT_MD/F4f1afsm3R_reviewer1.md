### Summary

This paper proposes SC-MCTS, a variant of MCTS for LLM reasoning. SC-MCTS is equipped with various techniques to make it perform better and run faster, including a new reward model based on contrastive decoding, an improved node selection strategy, an improved backpropagation strategy, and speculative decoding. The authors also conduct an interpretability study, showing statistical properties of the distribution of each reward model.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The authors made a great effort to improve the performance and interpretability of MCTS for LLM reasoning, with a wide range of techniques to make MCTS run better and faster. The authors also conducted a wide range of experiments, analyzing the effects of each technique.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that they improved the UCT node selection strategy of previous works, but I don't see any improvement. They just analyzed the importance of the exploration parameter in UCT and found the best value for the parameter, which is a standard practice for applying UCT.
2. The authors claim that their proposed method is more interpretable than previous methods, but I don't see any evidence for that. They show some statistical properties of the reward models, but that doesn't make the method more interpretable. The only conclusion they can draw from the statistical properties is which reward model performs better, but that is already shown in the ablation study in Table 2.
3. The authors claim that their proposed method is more generalizable than previous methods, but I don't see any evidence for that. They only tested their method on the Blocksworld dataset, so how can they make that claim?
4. The authors should compare their method to more baselines. They only compared their method to CoT and RAP-MCTS, but there are many other methods that apply MCTS to LLM reasoning.
5. The authors should compare their method to other methods using speculative decoding. The results reported in Figure 3 are misleading because they only show the speedup compared to vanilla MCTS, not the speedup compared to other methods using speculative decoding.
6. The authors should compare the accuracy of their method to baselines at the same time. The speedup of their method is meaningless if it comes at a cost of accuracy.

### Suggestions

The authors should clarify the specific limitations of the UCT implementation in previous works that they are addressing. If the issue is indeed just finding a better value for the exploration parameter, then it should be framed as such, rather than claiming a novel improvement to the UCT strategy itself. A more detailed analysis of how the optimal value was determined, including the range of values tested and the sensitivity of performance to this parameter, would be beneficial. Furthermore, the authors should provide a more rigorous justification for why their chosen value is optimal, rather than just stating that it yielded the best results. This could involve analyzing the exploration-exploitation trade-off at different stages of the search process and how the chosen parameter affects this balance. Without this level of detail, the claim of improving UCT remains unsubstantiated.

To support the claim of improved interpretability, the authors need to demonstrate how the statistical properties of the reward models provide insights into the reasoning process of the MCTS algorithm, beyond just indicating which reward model performs better. For example, they could show how specific statistical features of the reward distributions correlate with the quality of the chosen actions or the final outcome. This could involve analyzing the variance of the reward distributions at different nodes in the search tree and how this variance relates to the uncertainty in the model's predictions. Additionally, they could investigate whether certain statistical properties of the reward models can be used to identify biases or limitations in the model's reasoning process. Without such analysis, the statistical properties of the reward models are just descriptive, not interpretative.

Finally, the authors need to provide more evidence to support their claim of generalizability. Testing the method on a single dataset is insufficient to make such a strong claim. They should evaluate their method on a diverse set of reasoning tasks, including those with different characteristics and complexities. This could include tasks from different domains, such as mathematical reasoning, commonsense reasoning, and code generation. Furthermore, they should analyze the performance of their method across these different tasks and identify any patterns or trends that might indicate the limitations of their approach. This would provide a more robust assessment of the generalizability of their method and help to identify areas for future improvement.

### Questions

1. What is the novelty and contribution of your improved UCT strategy? What is wrong with the UCT strategy used in previous works?
2. How do the statistical properties of the reward models make your method more interpretable? What insights do these properties provide about the reasoning process of MCTS?
3. How do you evaluate the generalizability of your method using only the Blocksworld dataset? What are the limitations of using a single dataset to evaluate generalizability?
4. Why don't you compare your method to more baselines that apply MCTS to LLM reasoning? How does your method compare to these other methods?
5. Why don't you compare the speedup of your method to other methods using speculative decoding? How does the speedup of your method compare to these other methods?
6. How does the accuracy of your method compare to baselines at the same time? Does the speedup of your method come at a cost of accuracy?

### Rating

3

### Confidence

4

**********
