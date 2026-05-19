### Summary

This paper proposes a method to learn a causal model in MBRL and use the causal structure to guide exploration. Specifically, the authors propose to use empowerment as an intrinsic reward to guide exploration. The authors show that the proposed method outperforms existing baselines in multiple tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The idea of using empowerment to guide exploration in MBRL is interesting.
- The authors conduct extensive experiments to show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The authors claim that the proposed method is method-agnostic, but it seems that the method is only evaluated with two causal discovery methods. It would be better if the authors could show that the proposed method can be combined with more causal discovery methods.
- The authors should provide more details about the implementation of the proposed method, e.g., how to calculate the empowerment gain.

### Suggestions

The claim of method-agnosticism needs further clarification and more rigorous evaluation. While the framework might be adaptable to different causal discovery methods, the current evaluation only demonstrates its effectiveness with two specific methods. To strengthen this claim, the authors should evaluate the framework with a wider range of causal discovery techniques, including those based on different principles (e.g., score-based methods, constraint-based methods with different assumptions). This would involve not only implementing these methods but also analyzing the performance of the overall framework under different causal discovery settings. For example, how does the performance vary when using methods with different levels of sensitivity to noise or different assumptions about the underlying data distribution? This would provide a more comprehensive understanding of the framework's robustness and generalizability.

Furthermore, the paper lacks crucial implementation details, particularly regarding the calculation of empowerment gain. The authors should provide a step-by-step explanation of how empowerment is computed, including the specific equations used and the rationale behind each step. For instance, what is the precise definition of the channel capacity used in the empowerment calculation? How is the distribution over actions determined? What is the method used to estimate the channel capacity from the available data? The authors should also clarify how the empowerment gain is used to guide exploration. Is it used as a direct reward signal, or is it combined with other intrinsic rewards? Providing these details is essential for reproducibility and for understanding the practical implications of the proposed method. Without these details, it is difficult to assess the validity and effectiveness of the approach.

Finally, the paper would benefit from a more detailed analysis of the computational cost of the proposed method. Specifically, the authors should provide a breakdown of the computational complexity of each step, including the causal discovery process, the empowerment calculation, and the policy optimization. This analysis should consider the impact of different factors, such as the size of the state space, the number of causal variables, and the complexity of the causal model. It would also be helpful to compare the computational cost of the proposed method with that of existing baselines. This would provide a more complete picture of the trade-offs between performance and computational efficiency.

### Questions

- The authors claim that the proposed method is method-agnostic, but it seems that the method is only evaluated with two causal discovery methods. It would be better if the authors could show that the proposed method can be combined with more causal discovery methods.
- The authors should provide more details about the implementation of the proposed method, e.g., how to calculate the empowerment gain.

### Rating

6

### Confidence

3

**********
