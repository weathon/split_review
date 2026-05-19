### Summary

This paper proposes to improve the performance of decision transformer in stochastic environments. The authors first show that DT can recover the optimal trajectory in deterministic environments. The authors attribute the worse performance in stochastic environments to the variance of returns-to-go (RTG). To reduce the variance, the authors propose to replace the RTG with a learned value function. The authors further propose to use this value function to derive a goal for DT, and name the method D2T2. D2T2 is empirically evaluated on 2 illustrative stochastic examples, 2 stochastic CARLA benchmarks, and 3 suites from D4RL.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a solid theoretical analysis of the performance of DT in deterministic environments.
3. The performance of D2T2 is empirically demonstrated on a variety of tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The authors argue that the worse performance of DT in stochastic environments is due to the variance of RTG. However, the authors fail to provide any empirical evidence to support this argument. It is entirely possible that the stitching ability (Yamagata et al., 2023) of DT in stochastic environments is worse than that in deterministic environments, thus resulting in the worse performance. Specifically, the authors should investigate how the variance of RTG impacts the performance of DT, and whether reducing this variance directly leads to improved results. A controlled experiment where the variance of RTG is manipulated, while keeping other factors constant, would be beneficial to isolate the effect of RTG variance. Furthermore, the authors should provide a more detailed analysis of how the proposed method addresses the stitching problem, if at all, and how it compares to existing methods that explicitly tackle this issue.
2. The authors propose to use a learned value function to reduce the variance of RTG. However, the authors fail to discuss the limitations of this approach. For example, if the value function is learned via Q-learning, there is no guarantee that it will be accurate, especially in complex environments. In such a case, it is possible that D2T2 will perform worse than DT. The authors should provide a more detailed analysis of the sensitivity of D2T2 to the accuracy of the learned value function. It would be beneficial to show how the performance of D2T2 degrades as the value function becomes less accurate, and to compare this with the performance of DT under the same conditions. Additionally, the authors should discuss the computational cost of learning the value function, and how this cost compares to the computational cost of training DT.

### Suggestions

The authors should conduct a more thorough investigation into the relationship between RTG variance and DT performance. This could involve experiments where the variance of RTG is explicitly controlled, for example, by adding noise to the RTG or by using different methods to estimate it. The authors should also analyze how the variance of RTG affects the stitching ability of DT, and whether reducing the variance of RTG directly leads to better stitching. Furthermore, the authors should compare the performance of D2T2 with existing methods that explicitly address the stitching problem, such as those that use trajectory segmentation or other techniques to improve the consistency of stitched trajectories. This would help to clarify the specific advantages and disadvantages of D2T2 compared to other approaches.

To address the limitations of using a learned value function, the authors should conduct experiments where the accuracy of the value function is varied. This could be achieved by training the value function with different amounts of data, or by using different learning algorithms that produce value functions with varying degrees of accuracy. The authors should then analyze how the performance of D2T2 changes as the accuracy of the value function changes. This would provide a more complete understanding of the robustness of D2T2 to errors in the value function. Additionally, the authors should explore alternative methods for reducing the variance of RTG, such as using ensemble methods or other techniques for uncertainty estimation. This would provide a more comprehensive analysis of the different approaches for addressing the variance of RTG, and would help to identify the most effective methods for improving the performance of DT in stochastic environments.

Finally, the authors should provide a more detailed analysis of the computational cost of D2T2, including the cost of learning the value function and the cost of using the value function to derive a goal for DT. This analysis should compare the computational cost of D2T2 with the computational cost of DT, and should also consider the trade-off between computational cost and performance. The authors should also discuss the practical implications of these computational costs, and should provide guidance on when D2T2 is likely to be more appropriate than DT, and vice versa. This would help to make the paper more useful for practitioners who are interested in applying these methods to real-world problems.

### Questions

1. Could the authors provide empirical evidence to support the argument that the worse performance of DT in stochastic environments is due to the variance of RTG?
2. Could the authors discuss the limitations of using a learned value function, and how the performance of D2T2 might be affected by the accuracy of the value function?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
