### Summary

This paper proposes a novel offline RL method called Contrastive Diffuser (CDiffuser) to improve the performance of offline RL algorithms by making full use of low-return trajectories. CDiffuser groups the states of trajectories in the offline dataset into high-return states and low-return states and treats them as positive and negative samples correspondingly. Then, it designs a contrastive mechanism to pull the trajectory of an agent toward high-return states and push them away from low-return states. Experiments on 14 commonly used D4RL benchmarks demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The experimental results are promising.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity of the proposed method. It would be helpful to provide a comparison of the computational cost of CDiffuser with other offline RL methods.
2. The paper does not discuss the sensitivity of the proposed method to hyperparameters. It would be beneficial to analyze how the performance of CDiffuser varies with different hyperparameter settings.

### Suggestions

The paper would benefit from a more thorough investigation into the computational demands of the Contrastive Diffuser (CDiffuser) method. Specifically, a detailed breakdown of the time complexity for each stage of the algorithm, such as the contrastive learning component and the diffusion process, should be provided. This analysis should not only consider the asymptotic complexity but also the practical runtime, potentially including a comparison of wall-clock time against other offline RL methods on the same hardware. Furthermore, it would be valuable to explore the memory footprint of CDiffuser, especially when dealing with large datasets, and how this scales with the size of the state and action spaces. Such an analysis would allow readers to better understand the practical limitations and applicability of the proposed method in resource-constrained environments. For example, providing a table that shows the training time and memory usage for CDiffuser and other methods on different datasets would be very helpful.

In addition to computational complexity, a more rigorous analysis of the hyperparameter sensitivity of CDiffuser is needed. The paper should include a systematic study of how the performance of CDiffuser varies with different settings of key hyperparameters, such as the learning rate, the batch size, the number of diffusion steps, and the contrastive loss parameters. This analysis should not only focus on the final performance but also on the convergence speed and stability of the training process. It would be beneficial to visualize the performance landscape with respect to different hyperparameter combinations, for example, using heatmaps or contour plots. This would help to identify the optimal hyperparameter ranges and provide guidance for practitioners on how to tune the method for different tasks. Furthermore, the paper should discuss the potential reasons behind the observed sensitivity and provide insights into how to choose appropriate hyperparameter values for new datasets or environments.

Finally, the paper should also discuss the limitations of the proposed method. For example, it would be beneficial to analyze the performance of CDiffuser in scenarios with sparse rewards or when the offline dataset is not diverse enough. It would also be interesting to investigate the robustness of CDiffuser to different types of noise in the offline dataset. Addressing these limitations would provide a more complete picture of the strengths and weaknesses of the proposed method and help to guide future research in this area.

### Questions

1. How does the performance of CDiffuser compare to other offline RL methods in terms of computational cost?
2. How sensitive is the performance of CDiffuser to the choice of hyperparameters?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
