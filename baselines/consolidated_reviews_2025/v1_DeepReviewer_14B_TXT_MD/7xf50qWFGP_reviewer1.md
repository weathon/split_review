### Summary

This paper studies online Laplacian-based representation learning, which updates the graph-based representation simultaneously while the policy is updated in RL. The authors introduce the Asymmetric Graph Drawing Objective (AGDO) and provide a theoretical analysis of the convergence of running online projected gradient descent on AGDO. The theoretical results show that if the policy learning algorithm induces a bounded drift on the policy, running online projected gradient descent on AGDO exhibits ergodic convergence. The experiments validate the theoretical results.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The problem studied in this paper is interesting and the theoretical analysis is detailed.

### Weaknesses

#### Some Related Works


#### comment

1. I am not sure whether the online Laplacian-based representation learning has significant advantages over other representation learning methods in RL. The authors should provide more discussions on this. 
2. I don't think the theoretical results of this paper are significant. The authors should provide more discussions on the significance of the theoretical results.
3. The authors should provide more discussions about the related work, like successor features and contrastive learning in RL.
4. The experiments are conducted only in simple grid world environments, which makes the results not convincing.

### Suggestions

The paper would benefit from a more thorough discussion of the practical advantages of online Laplacian-based representation learning compared to other methods. While the theoretical analysis is detailed, its practical significance remains unclear. The authors should provide concrete examples of scenarios where this approach offers a clear advantage over alternative representation learning techniques in RL, such as those based on autoencoders or contrastive learning. For instance, do the learned representations exhibit better generalization properties, or do they lead to more efficient policy learning in specific types of environments? A more detailed analysis of the computational cost of the proposed method compared to other representation learning techniques would also be beneficial. Furthermore, the authors should discuss the limitations of the proposed approach and identify potential areas for future research.

To strengthen the theoretical contributions, the authors should provide a more in-depth discussion of the significance of their convergence results. While the paper demonstrates ergodic convergence of the online projected gradient descent on the Asymmetric Graph Drawing Objective (AGDO), it is not clear how this result translates into practical benefits for RL. The authors should discuss the implications of this convergence result for the stability and performance of RL algorithms that use the proposed representation learning method. For example, how does the convergence rate of the representation learning process affect the overall learning performance? What are the practical implications of the bounded drift assumption on the policy learning algorithm? A more detailed analysis of the relationship between the theoretical results and the empirical findings would also be valuable. The authors should also discuss the limitations of their theoretical analysis and identify potential areas for future research.

Finally, the experimental evaluation needs to be significantly expanded to include more complex and diverse environments. The current experiments in simple grid world environments are not sufficient to demonstrate the effectiveness of the proposed method in realistic scenarios. The authors should consider evaluating their method in more challenging environments, such as those with high-dimensional state spaces or complex dynamics. Furthermore, the authors should compare their method against a wider range of baseline algorithms, including state-of-the-art representation learning techniques. A more thorough analysis of the experimental results, including a discussion of the limitations of the proposed method, would also be beneficial. The authors should also provide more details about the implementation of their method and the experimental setup.

### Questions

1. In the experiments, how do the authors obtain the "true Laplacian representation"?
2. What does the x-axis "steps (1 steps = 1M samples)" mean? Why the curves do not converge as steps increase?

### Rating

3

### Confidence

3

**********
