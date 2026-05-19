### Summary

The paper proposes a new class of activation functions, elephant activation functions, that can generate both sparse representations and sparse gradients. The paper shows that by simply replacing classical activation functions with elephant activation functions, we can significantly improve the resilience of neural networks to catastrophic forgetting. The method has broad applicability and benefits for continual learning in regression, class incremental learning, and reinforcement learning tasks.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of exploring the activation function to reduce catastrophic forgetting is interesting.
3. The proposed elephant activation functions show some benefits for continual learning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks the discussion of the limitations of the proposed method.
2. The paper lacks the comparison with other activation functions that can create sparse representations for reducing catastrophic forgetting.
3. The paper lacks the comparison with other baseline continual learning methods that can create sparse representations for reducing catastrophic forgetting.
4. The paper lacks the comparison with other baseline continual learning methods in RL.

### Suggestions

The paper should include a more thorough discussion of the limitations of the proposed elephant activation functions. Specifically, the authors should explore the computational overhead introduced by these functions compared to more standard activation functions like ReLU or sigmoid. It would be beneficial to analyze the impact of the additional parameters, 'a' and 'd', on the training process, and whether these parameters need to be tuned for each specific task or dataset. Furthermore, the paper should discuss the potential for the elephant activation function to lead to vanishing or exploding gradients, especially in deep networks, and how this can be mitigated. A more detailed analysis of the function's behavior in different scenarios is needed to fully understand its practical limitations.

In addition to comparing against classical activation functions, the paper should include a more comprehensive comparison with other activation functions specifically designed to promote sparsity. For example, activation functions like the Rectified Linear Unit with Top-K sparsity (ReLU-K) or other sparse activation functions could provide a more relevant baseline. The comparison should not only focus on the final performance but also on the sparsity level achieved by each activation function and the trade-off between sparsity and performance. This would help to better understand the specific benefits of the elephant activation function compared to other sparsity-inducing methods. The authors should also investigate the impact of different parameter settings for these activation functions to ensure a fair comparison.

Finally, the paper needs to include a more extensive comparison with other continual learning methods, particularly those that also leverage sparse representations. While the paper mentions SR-NN, a more detailed comparison with other methods that explicitly encourage sparsity, such as those using L1 regularization or other sparse coding techniques, is necessary. In the RL domain, the paper should compare against a wider range of continual learning baselines, not just the method in [4]. This would provide a more comprehensive understanding of the proposed method's performance relative to the state-of-the-art in continual learning. The comparison should include metrics beyond just the final return, such as the average reward and the number of steps required to converge.

### Questions

1. In the experiments, the paper only compares the elephant activation functions with classical activation functions. Do the elephant activation functions also perform better than other activation functions that can create sparse representations for reducing catastrophic forgetting?
2. In the experiments, the paper only compares the elephant activation functions with the baseline continual learning methods in class incremental learning. How about the comparison with the baseline continual learning methods in RL?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
